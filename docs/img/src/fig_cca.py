"""CCA between past and future windows of a noisy time series."""
from scipy import linalg

from style import *


def series(n, rng):
    # a slow and a faster noisy oscillation (each AR(2)), plus measurement noise
    def ar2(r, w, sd):
        a1, a2 = 2 * r * np.cos(w), -r * r
        x = np.zeros(n)
        e = rng.normal(0, sd, n)
        for t in range(2, n):
            x[t] = a1 * x[t - 1] + a2 * x[t - 2] + e[t]
        return x
    return ar2(0.97, 0.18, 1.0) + 0.6 * ar2(0.93, 0.9, 1.0) + rng.normal(0, 1.2, n)


def isqrt(S):
    w, V = np.linalg.eigh(S)
    return V @ np.diag(w ** -0.5) @ V.T


def make():
    rng = np.random.default_rng(3)
    n = 40000
    y = series(n, rng)
    y = (y - y.mean()) / y.std()
    p = 10
    idx = np.arange(p, n - p)
    P = np.stack([y[idx - k - 1] for k in range(p)], 1)   # most recent first
    F = np.stack([y[idx + k] for k in range(p)], 1)
    Spp, Sff, Spf = P.T @ P / len(idx), F.T @ F / len(idx), P.T @ F / len(idx)
    Wp, Wf = isqrt(Spp), isqrt(Sff)
    U, s, Vt = np.linalg.svd(Wp @ Spf @ Wf)
    a = Wp @ U   # past directions
    b = Wf @ Vt.T
    print("canonical correlations", np.round(s, 3))
    zp, zf = P @ a, F @ b

    fig = plt.figure(figsize=(14, 4.6))
    # A: series with past and future windows
    ax = fig.add_axes([0.02, 0.12, 0.36, 0.64])
    t0 = 5000
    tt = np.arange(-30, 30)
    seg = y[t0 + tt]
    ax.axvspan(-p - 0.5, -0.5, color=PAST_L, zorder=0)
    ax.axvspan(-0.5, p - 0.5, color=FUT_L, zorder=0)
    ax.plot(tt, seg, color=DROP, lw=1.4)
    mp, mf = (tt >= -p) & (tt < 0), (tt >= -1) & (tt < p)
    ax.plot(tt[mp], seg[mp], color=PAST, lw=2.4)
    ax.plot(tt[mf], seg[mf], color=FUT, lw=2.4)
    ax.axvline(-0.5, color=MUTED, ls=(0, (3, 3)), lw=1.2)
    ax.set_xlim(-30, 30)
    lim = np.abs(seg).max() * 1.15
    ax.set_ylim(-lim, lim * 1.55)
    ax.axis("off")
    ax.text(-1.5, lim * 1.5, "past", ha="right", va="top", color=PAST,
            fontsize=BASE - 1, fontweight="bold")
    ax.text(0.5, lim * 1.5, "future", ha="left", va="top", color=FUT,
            fontsize=BASE - 1, fontweight="bold")
    ax.text(-0.5, -lim, "now", ha="center", va="top", color=MUTED, fontsize=BASE - 2)

    # B: canonical correlations
    axb = fig.add_axes([0.475, 0.2, 0.16, 0.56])
    r = 4
    sv_bars(axb, s, r)
    axb.set_ylim(0, 1.12)
    axb.set_yticks([0, 1])
    axb.set_xticks(range(1, p + 1))
    axb.tick_params(labelsize=BASE - 4)
    axb.set_xlabel("summary pairs, ranked", fontsize=BASE - 2, color=MUTED)
    axb.set_ylabel(r"correlation $\rho_i$", fontsize=BASE - 2, color=MUTED)

    # C: scatter for pair 1 and a weak pair
    weak = 5
    for k, (pair, x0) in enumerate([(0, 0.69), (weak, 0.85)]):
        axs = fig.add_axes([x0, 0.2, 0.13, 0.42])
        sel = rng.choice(len(idx), 1500, replace=False)
        col = STATE if pair < r else DROP
        axs.scatter(zp[sel, pair], zf[sel, pair], s=5, color=col, alpha=0.5, lw=0)
        axs.set_xlim(-4, 4)
        axs.set_ylim(-4, 4)
        axs.set_xticks([])
        axs.set_yticks([])
        axs.set_aspect("equal")
        axs.set_xlabel("past summary", fontsize=BASE - 3, color=PAST)
        axs.set_ylabel("future summary", fontsize=BASE - 3, color=FUT)
        axs.set_title(rf"$\rho_{{{pair + 1}}} = {s[pair]:.2f}$", fontsize=BASE - 2,
                      color=col if pair < r else MUTED, fontweight="bold")
    for x, tl in [(0.02, "A noisy signal"), (0.44, "Ranked summaries"),
                  (0.69, "Past vs future summaries")]:
        fig.text(x, 0.86, tl, fontsize=BASE + 1, fontweight="bold", ha="left")
    mtext(fig, 0.44, 0.07, r"$H = \mathrm{Cov}(p)^{-1/2}\ \mathrm{Cov}(p, f)\ \mathrm{Cov}(f)^{-1/2}$,"
          r"   SVD: $\rho_1 \geq \rho_2 \geq \cdots$ (the $\sigma_i$)", va="top", ha="left")
    fig.text(0.02, 0.79, "summary = a weighted sum of a window", fontsize=BASE - 2,
             color=MUTED, ha="left")
    axb.text(3.0, 1.0, "keep r = 4", ha="center", va="bottom", color=STATE, fontsize=BASE - 1,
             fontweight="bold")
    fig_arrow(fig, (0.385, 0.45), (0.425, 0.45))
    fig_arrow(fig, (0.645, 0.45), (0.68, 0.45))
    save(fig, "cca.png")


if __name__ == "__main__":
    make()
