"""Koopman / DMD on a damped pendulum, plus Takens delay embedding of Lorenz."""
from scipy.integrate import solve_ivp

from style import *

MODE_COLS = [STATE, "#5f9e6e", "#9cc7a6"]


def pendulum(x0, T=40, dt=0.05, c=0.25):
    t = np.arange(0, T, dt)
    sol = solve_ivp(lambda t, x: [x[1], -np.sin(x[0]) - c * x[1]], (0, T), x0, t_eval=t,
                    rtol=1e-10, atol=1e-10)
    return t, sol.y


def hankel_dmd(y, d, r):
    N = len(y) - d
    H = np.stack([y[i:i + N] for i in range(d)])
    X, Y = H[:, :-1], H[:, 1:]
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    U, s, V = U[:, :r], s[:r], Vt[:r].T
    lam, W = np.linalg.eig(U.T @ Y @ V / s)
    Phi = U @ W
    b = np.linalg.lstsq(Phi, H[:, 0], rcond=None)[0]
    k = np.arange(len(y))
    comps = (Phi[0][:, None] * b[:, None]) * lam[:, None] ** k[None]
    return lam, comps


def make():
    fig = plt.figure(figsize=(14, 4.7))

    # A: phase portrait
    ax = fig.add_axes([0.02, 0.08, 0.25, 0.72])
    for x0 in [[2.6, 0], [-2.4, 0.0], [0.0, 1.9], [0, -1.6], [-2.8, 0.6], [2.8, -0.5]]:
        t, X = pendulum(x0, T=30)
        ax.plot(X[0], X[1], color=DROP, lw=1.3, zorder=1)
    t, X = pendulum([1.8, 0])
    ax.plot(X[0], X[1], color=INK, lw=2.0, zorder=2)
    for i in [8, 40, 75, 130]:
        arrow(ax, (X[0, i], X[1, i]), (X[0, i + 2], X[1, i + 2]), color=INK, lw=0, ms=16)
    ax.plot([1.8], [0], "o", color=PAST, ms=9, zorder=3)
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.4, 2.4)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("angle", fontsize=BASE - 1)
    ax.set_ylabel("speed", fontsize=BASE - 1)
    ax.set_title("Points move nonlinearly", loc="left", fontsize=BASE + 1,
                 fontweight="bold")
    ax.text(0.02, 1.0, "damped pendulum", transform=ax.transAxes, fontsize=BASE - 2,
            color=MUTED, va="top")

    # B: measurement = sum of modes
    th = X[0]
    lam, comps = hankel_dmd(th, d=80, r=6)
    order = np.argsort(-np.abs(comps[:, 0]))
    # pair conjugates -> real oscillating modes
    pairs, used = [], set()
    for i in order:
        if i in used:
            continue
        j = int(np.argmin(np.abs(lam - np.conj(lam[i])) + 1e9 * np.isin(np.arange(len(lam)),
                                                                       [i])))
        if np.isreal(lam[i]) or np.abs(lam[j] - np.conj(lam[i])) > 1e-6:
            pairs.append(np.real(comps[i]))
            used.add(i)
        else:
            pairs.append(np.real(comps[i] + comps[j]))
            used.update([i, j])
    pairs = sorted(pairs, key=lambda c: -np.linalg.norm(c))
    recon = np.sum(pairs, axis=0)
    print("modes", len(pairs), "max err", np.abs(recon - th).max())
    ax = fig.add_axes([0.35, 0.08, 0.34, 0.72])
    tt = t
    gap = 2.6
    ax.plot(tt, th, color=PAST, lw=4, alpha=0.4)
    ax.plot(tt, recon, color=INK, lw=1.4, ls=(0, (4, 2)))
    ax.text(41, 0, r"$g$ = angle of" "\nthe black path", ha="left", va="center", color=PAST, fontsize=BASE - 2)
    for k, c in enumerate(pairs[:3]):
        off = -gap * (k + 1) - 0.6
        sc = 1.0 if np.abs(c).max() > 0.3 else 10.0
        ax.plot(tt, c * sc + off, color=MODE_COLS[k], lw=2.0)
        ax.axhline(off, color=DROP_L, lw=0.8, zorder=0)
        sign = "=" if k == 0 else "+"
        ax.text(-1.2, off, sign, ha="right", va="center", fontsize=BASE + 4, color=INK)
        ax.text(41, off, f"mode {k + 1}" + (" (×10)" if sc > 1 else ""), ha="left", va="center", color=MODE_COLS[k],
                fontsize=BASE - 2, fontweight="bold")
    ax.set_xlim(-3.5, 49)
    ax.set_ylim(-gap * 3 - 2.4, 3.2)
    ax.axis("off")
    ax.annotate("", xy=(40, -gap * 3 - 2.2), xytext=(0, -gap * 3 - 2.2),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2))
    ax.text(20, -gap * 3 - 2.0, "time", ha="center", va="bottom", color=MUTED,
            fontsize=BASE - 2)
    ax.set_title("Measurements evolve linearly", loc="left", fontsize=BASE + 1,
                 fontweight="bold")
    mtext(ax, 0.0, 1.0, r"$(Kg)(x) = g(T(x))$:  linear in $g$", transform=ax.transAxes,
          va="top")
    mtext(fig, 0.35, -0.04, r"$g(x_t) \approx \Sigma_i\, c_i\, \lambda_i^{\,t}$  (a few decaying waves)",
          va="top")
    mtext(fig, 0.02, -0.04, r"$x_{t+1} = T(x_t)$  (nonlinear)", va="top")

    # C: Takens delay embedding of Lorenz
    def lorenz(t, v, s=10, r=28, b=8 / 3):
        x, y, z = v
        return [s * (y - x), x * (r - z) - y, x * y - b * z]
    dt = 0.01
    tl = np.arange(0, 60, dt)
    sol = solve_ivp(lorenz, (0, 60), [1, 1, 1], t_eval=tl, rtol=1e-9, atol=1e-9)
    x = sol.y[0][1000:]
    lag = 10
    axs = fig.add_axes([0.745, 0.62, 0.245, 0.15])
    axs.plot(np.arange(600) * dt, x[:600], color=FUT, lw=1.4)
    axs.axis("off")
    axs.set_title("One measurement rebuilds the state", loc="left", fontsize=BASE + 1,
                  fontweight="bold", x=-0.02)
    axs.text(6.1, 0, "y(t)", ha="left", va="center", fontsize=BASE - 1, color=FUT)
    ax3 = fig.add_axes([0.765, -0.02, 0.21, 0.6], projection="3d")
    n = len(x) - 2 * lag
    ax3.plot(x[2 * lag:2 * lag + n], x[lag:lag + n], x[:n], color=STATE, lw=0.5, alpha=0.8)
    ax3.set_axis_off()
    ax3.view_init(elev=22, azim=-55)
    ax3.text2D(0.5, 0.14, "its rows rebuild the Lorenz attractor",
               transform=ax3.transAxes, ha="center", va="top", fontsize=BASE - 3,
               color=MUTED)
    mtext(fig, 0.745, -0.04, r"$H[t,k] = y(t - k\tau)$:  one signal $\to$ a table", va="top")
    fig_arrow(fig, (0.86, 0.6), (0.86, 0.52), lw=2, ms=18)
    save(fig, "koopman.png")


if __name__ == "__main__":
    make()
