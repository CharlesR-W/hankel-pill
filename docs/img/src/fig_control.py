"""Realization / balanced truncation on a small stable linear system (8 internal states)."""
from scipy import linalg, signal

from style import *


def system():
    # four lightly damped modes of decreasing strength -> 8 internal states
    blocks, Bs, Cs = [], [], []
    for w, z, g in [(1.0, 0.18, 1.0), (2.2, 0.15, 0.5), (3.7, 0.1, 0.04), (5.9, 0.08, 0.012)]:
        blocks.append(np.array([[0, 1], [-w * w, -2 * z * w]]))
        Bs.append([[0], [1]])
        Cs.append([g * w * w, g * w * 0.3])
    A = linalg.block_diag(*blocks)
    B = np.vstack(Bs).astype(float)
    C = np.hstack(Cs)[None, :]
    return A, B, C


def balanced_truncation(A, B, C, r):
    P = linalg.solve_continuous_lyapunov(A, -B @ B.T)
    Q = linalg.solve_continuous_lyapunov(A.T, -C.T @ C)
    Lp = linalg.cholesky(P, lower=True)
    Lq = linalg.cholesky(Q, lower=True)
    U, s, Vt = linalg.svd(Lq.T @ Lp)
    S = np.diag(s[:r] ** -0.5)
    T = Lp @ Vt.T[:, :r] @ S
    Ti = S @ U[:, :r].T @ Lq.T
    return Ti @ A @ T, Ti @ B, C @ T, s


def make():
    A, B, C = system()
    r = 4
    Ar, Br, Cr, hsv = balanced_truncation(A, B, C, r)
    # if r splits a conjugate pair the reduced model is still a valid real system
    D = np.zeros((1, 1))
    Tp, Tf = 12.0, 18.0
    t = np.linspace(-Tp, Tf, 3001)
    u = np.where(t < 0, np.sin(1.2 * (t + 5.5)) * np.exp(-((t + 5.5) / 2.4) ** 2)
                 + 0.6 * np.exp(-((t + 8.5) / 1.2) ** 2), 0.0)
    _, y, _ = signal.lsim((A, B, C, D), u, t - t[0])
    _, yr, _ = signal.lsim((Ar, Br, Cr, D), u, t - t[0])
    fut = t >= 0
    print("HSV", np.round(hsv, 4), "bound", 2 * hsv[r:].sum(),
          "max err", np.abs(y - yr)[fut].max(), "max y", np.abs(y).max())

    fig = plt.figure(figsize=(14, 4.6))
    # panel A: past input -> black box -> future output
    ax = fig.add_axes([0.02, 0.1, 0.38, 0.66])
    past = t < 0
    sc = np.abs(y[fut]).max() / np.abs(u).max()
    ax.plot(t[past], u[past], color=PAST, lw=2.4)
    ax.plot(t[fut], y[fut] / sc, color=FUT, lw=2.4)
    ax.axvline(0, color=MUTED, ls=(0, (3, 3)), lw=1.2)
    ax.axhline(0, color=DROP, lw=0.8, zorder=0)
    ax.set_xlim(-Tp, Tf)
    yl = 1.25 * np.abs(u).max()
    ax.set_ylim(-yl * 1.15, yl * 1.75)
    blank_axis = ax
    blank_axis.axis("off")
    ax.text(-Tp / 2, yl * 1.7, "past input\n(what you push)", ha="center", va="top",
            color=PAST, fontsize=BASE, fontweight="bold")
    ax.text(Tf / 2, yl * 1.7, "future output\n(what you see)", ha="center", va="top",
            color=FUT, fontsize=BASE, fontweight="bold")
    ax.add_patch(Rectangle((-3.2, -0.2 * yl), 6.4, 0.4 * yl, fc=INK, ec=INK, zorder=5))
    ax.text(0, 0, "black box", ha="center", va="center", color="white", fontsize=BASE - 3,
            fontweight="bold", zorder=6)
    ax.text(0, -yl * 1.15, "now", ha="center", va="bottom", color=MUTED, fontsize=BASE - 2,
            bbox=dict(fc="white", ec="none"))
    ax.set_title("A black box: past inputs → future outputs", loc="left", fontsize=BASE + 1,
                 fontweight="bold")

    # panel B: Hankel singular values
    ax = fig.add_axes([0.47, 0.17, 0.2, 0.56])
    sv_bars(ax, hsv, r)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks(range(1, len(hsv) + 1))
    ax.set_xlabel("internal states, ranked", fontsize=BASE - 2, color=MUTED)
    ax.text(2.5, hsv[0] * 1.02, "keep r = 4", ha="center", va="bottom", color=STATE,
            fontsize=BASE - 1, fontweight="bold")
    ax.text(6.5, hsv[0] * 0.62, "drop 4", ha="center", va="center", color=MUTED,
            fontsize=BASE - 2)
    mtext(ax, 6.5, hsv[0] * 0.48, r"error $\leq 2\, \Sigma_{i>r}\, \sigma_i$", ha="center")
    mtext(fig, 0.47, 0.0, r"bars: $\sigma_1 \geq \sigma_2 \geq \cdots$", va="top")
    ax.set_ylim(0, hsv[0] * 1.18)
    ax.set_title("Rank the hidden states", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=-0.05)

    # panel C: reduced model reproduces the future output
    ax = fig.add_axes([0.74, 0.17, 0.25, 0.56])
    ax.plot(t[fut], y[fut], color=FUT, lw=5, alpha=0.45, label="original (8 states)")
    ax.plot(t[fut], yr[fut], color=STATE, lw=2.0, ls=(0, (4, 2)),
            label="simplified (4 states)")
    ax.axhline(0, color=DROP, lw=0.8, zorder=0)
    ax.set_xlim(0, Tf)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("time after now", fontsize=BASE - 2, color=MUTED)
    ax.legend(frameon=False, fontsize=BASE - 3, loc="lower right", handlelength=1.8)
    m = np.abs(y[fut]).max()
    ax.set_ylim(-2.0 * m, 1.15 * m)
    ax.set_title("Simplified model", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=-0.05)
    mtext(fig, 0.02, 0.0, r"$H[p,f] = C\, e^{A(p+f)} B$   (input at time $-p$ $\to$ output at $+f$)",
          va="top")
    fig_arrow(fig, (0.405, 0.45), (0.455, 0.45))
    fig_arrow(fig, (0.68, 0.45), (0.725, 0.45))
    save(fig, "control.png")


if __name__ == "__main__":
    make()
