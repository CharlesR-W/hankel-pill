"""Minimal realization as a factorization: pasts ->> states >-> rows (behaviours)."""
from matplotlib.patches import Ellipse

from style import *


def blob(ax, c, w, h, fc, ec, label, sub=None, fs=BASE, lab_dy=0.0):
    ax.add_patch(Ellipse(c, w, h, fc=fc, ec=ec, lw=2, zorder=1))
    ax.text(c[0], c[1] + h / 2 + 0.12 + lab_dy, label, ha="center", va="bottom", color=ec,
            fontsize=fs, fontweight="bold")
    if sub:
        ax.text(c[0], c[1] - h / 2 - 0.1, sub, ha="center", va="top", color=MUTED,
                fontsize=BASE - 3)


def make():
    fig = plt.figure(figsize=(14, 5.2))

    # ---- left: sets (Myhill-Nerode) ----
    ax = fig.add_axes([0.0, 0.0, 0.6, 0.88])
    blank(ax, (0, 10), (0, 6.2), equal=True)
    P, S, F = (1.5, 3.9), (5.0, 1.75), (8.5, 3.9)
    blob(ax, P, 2.2, 3.4, PAST_L, PAST, "pasts")
    blob(ax, S, 1.5, 1.3, STATE_L, STATE, "", sub="the minimal\nmachine")
    ax.text(S[0], S[1] + 0.75, r"states $S$", ha="center", va="bottom", color=STATE,
            fontsize=BASE, fontweight="bold")
    blob(ax, F, 2.2, 3.4, FUT_L, FUT, "possible rows")
    rng = np.random.default_rng(2)
    n = 11
    pp = np.c_[P[0] + rng.uniform(-0.55, 0.55, n), np.linspace(P[1] + 1.3, P[1] - 1.3, n)]
    grp = np.array([0, 1, 2, 0, 1, 2, 0, 2, 1, 0, 2])
    ss = np.array([[S[0] - 0.42, S[1]], [S[0], S[1] + 0.05], [S[0] + 0.42, S[1]]])
    ff_all = np.c_[F[0] + rng.uniform(-0.6, 0.6, 12), np.linspace(F[1] + 1.3, F[1] - 1.3, 12)]
    hit = [2, 6, 9]
    for i, (x, y) in enumerate(pp):
        g = grp[i]
        ax.annotate("", xy=ss[g], xytext=(x, y),
                    arrowprops=dict(arrowstyle="-", color=GROUPS[g], lw=1.0, alpha=0.55,
                                    shrinkA=4, shrinkB=6, connectionstyle="arc3,rad=0.1"),
                    zorder=2)
        ax.plot(x, y, "o", color=GROUPS[g], ms=6, zorder=3)
    for j, (x, y) in enumerate(ff_all):
        ax.plot(x, y, "o", color=DROP if j not in hit else GROUPS[hit.index(j)], ms=6,
                zorder=3)
    for g in range(3):
        ax.annotate("", xy=ff_all[hit[g]], xytext=ss[g],
                    arrowprops=dict(arrowstyle="-|>", color=GROUPS[g], lw=1.6, shrinkA=6,
                                    shrinkB=5, mutation_scale=12,
                                    connectionstyle="arc3,rad=-0.1"), zorder=2)
        ax.plot(*ss[g], "o", color=GROUPS[g], ms=11, zorder=4)
    # big arrows
    arrow(ax, (P[0] + 1.25, P[1] + 1.0), (F[0] - 1.25, F[1] + 1.0), color=INK, lw=2.4, ms=22,
          rad=-0.12)
    ax.text(5.0, 5.75, r"the table $H$: past $\mapsto$ its row", ha="center", va="bottom", fontsize=BASE,
            color=INK, fontweight="bold")
    arrow(ax, (P[0] + 0.7, P[1] - 1.55), (S[0] - 0.85, S[1] - 0.15), color=STATE, lw=2.6,
          ms=22, style="-|>")
    arrow(ax, (S[0] + 0.85, S[1] - 0.15), (F[0] - 0.7, F[1] - 1.55), color=STATE, lw=2.6,
          ms=22, style="-|>")
    ax.text(2.2, 1.25, "reachable\n(onto: every state\nis reached)", ha="center", va="top",
            color=STATE, fontsize=BASE - 2)
    ax.text(7.9, 1.25, "observable\n(one-to-one: different\nstates look different)",
            ha="center", va="top", color=STATE, fontsize=BASE - 2)
    mtext(ax, 2.2, 1.6, r"pasts $\twoheadrightarrow S$", ha="center")
    mtext(ax, 7.9, 1.6, r"$S \rightarrowtail$ rows", ha="center")
    mtext(ax, 5.0, -0.25, r"$H = (S \rightarrowtail \mathrm{rows}) \circ "
          r"(\mathrm{pasts} \twoheadrightarrow S)$", ha="center", fs=MATH_FS + 1)
    ax.set_title("The table factors through the states", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=0.03)

    # ---- right: the same with numbers ----
    ax = fig.add_axes([0.62, 0.0, 0.37, 0.88])
    blank(ax, (0, 6.2), (0, 6.2), equal=True)
    P2, S2, F2 = (0.9, 3.9), (3.1, 1.7), (5.3, 3.9)
    for c, col, lc, lab in [(P2, PAST_L, PAST, "pasts"), (F2, FUT_L, FUT, "rows")]:
        box(ax, c[0] - 0.75, c[1] - 1.2, 1.5, 2.4, fc=col, ec=lc, lw=2, r=0.1)
        ax.text(c[0], c[1] + 1.32, lab, ha="center", va="bottom", color=lc, fontsize=BASE,
                fontweight="bold")
        ax.text(c[0], c[1], "weighted\nmixes of\npasts" if lab == "pasts" else
                "rows of\nnumbers", ha="center", va="center", color=lc, fontsize=BASE - 3)
    # state: r bars
    sv = [1.0, 0.7, 0.45]
    for i, v in enumerate(sv):
        ax.add_patch(Rectangle((S2[0] - 0.5 * v, S2[1] + 0.25 - i * 0.28), v, 0.18,
                               fc=STATE, ec="none", zorder=3))
    box(ax, S2[0] - 0.62, S2[1] - 0.42, 1.24, 0.98, fc="white", ec=STATE, lw=2, r=0.08, z=2)
    mtext(ax, S2[0], S2[1] - 0.8, r"$\dim S = \mathrm{rank}\, H$", ha="center")
    ax.text(S2[0], S2[1] + 0.68, r"$S$", ha="center", va="bottom", color=STATE,
            fontsize=BASE, fontweight="bold")
    arrow(ax, (P2[0] + 0.8, P2[1] + 0.9), (F2[0] - 0.8, F2[1] + 0.9), color=INK, lw=2.4,
          ms=22, rad=-0.15)
    ax.text(3.1, 5.4, r"the table $H$", ha="center", va="bottom", fontsize=BASE, color=INK,
            fontweight="bold")
    arrow(ax, (P2[0] + 0.3, P2[1] - 1.3), (S2[0] - 0.7, S2[1]), color=STATE, lw=2.6, ms=22)
    arrow(ax, (S2[0] + 0.7, S2[1]), (F2[0] - 0.3, F2[1] - 1.3), color=STATE, lw=2.6, ms=22)
    ax.set_title("With numbers: the middle has size = rank", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=0.0)
    save(fig, "category.png")


if __name__ == "__main__":
    make()
