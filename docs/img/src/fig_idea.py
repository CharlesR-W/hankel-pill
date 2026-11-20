from style import *

PASTS = ["…aa", "…ab", "…ba", "…bb", "…aab", "…bba"]
FUTS = ["a", "b", "ab", "ba", "bb"]
# three distinct row patterns (states A, B, C); rows sharing a pattern are the same state
PAT = {"A": [1, 0, 1, 0, 1], "B": [0, 1, 1, 1, 0], "C": [1, 1, 0, 0, 1]}
ROWSTATE = ["A", "B", "C", "A", "B", "C"]
GCOL = {"A": (GROUPS[0], GROUPS_L[0]), "B": (GROUPS[1], GROUPS_L[1]),
        "C": (GROUPS[2], GROUPS_L[2])}


def grid_table(ax, rows, cols, cell, x0, y0, cw=1.0, ch=1.0, row_lab=None, col_lab=None,
               fs=BASE - 1):
    """cell(i, j) -> (facecolor, text, textcolor)."""
    n, m = rows, cols
    for i in range(n):
        for j in range(m):
            fc, t, tc = cell(i, j)
            ax.add_patch(Rectangle((x0 + j * cw, y0 - (i + 1) * ch), cw, ch, fc=fc,
                                   ec="white", lw=2.0))
            if t:
                ax.text(x0 + (j + .5) * cw, y0 - (i + .5) * ch, t, ha="center",
                        va="center", fontsize=fs, color=tc)
    if row_lab:
        for i, t in enumerate(row_lab):
            ax.text(x0 - 0.12, y0 - (i + .5) * ch, t, ha="right", va="center", color=PAST,
                    fontsize=fs, family="DejaVu Sans Mono")
    if col_lab:
        for j, t in enumerate(col_lab):
            ax.text(x0 + (j + .5) * cw, y0 + 0.12, t, ha="center", va="bottom", color=FUT,
                    fontsize=fs, family="DejaVu Sans Mono")


def axis_names(ax, x0, y0, n, m, cw=1, ch=1, fs=BASE - 1):
    ax.text(x0 + m * cw / 2, y0 + 0.75, "futures", ha="center", va="bottom", color=FUT,
            fontsize=fs, fontweight="bold")
    ax.text(x0 - 1.55, y0 - n * ch / 2, "pasts", ha="center", va="center", color=PAST,
            fontsize=fs, fontweight="bold", rotation=90)


def make():
    fig = plt.figure(figsize=(14, 4.6))
    W = [0.215, 0.215, 0.215, 0.2]
    X = [0.03, 0.285, 0.54, 0.79]
    axs = [fig.add_axes([x, 0.04, w, 0.78]) for x, w in zip(X, W)]
    n, m = len(PASTS), len(FUTS)
    x0, y0 = 1.9, 6.6
    for ax in axs[:3]:
        blank(ax, (0, 7.6), (-0.3, 8.0))

    # 1: the table
    ax = axs[0]
    grid_table(ax, n, m, lambda i, j: ((DROP_L, "", INK) if not PAT[ROWSTATE[i]][j]
                                       else ("#4b5563", "", "white")),
               x0, y0, row_lab=PASTS, col_lab=FUTS)
    axis_names(ax, x0, y0, n, m)
    ax.add_patch(Rectangle((x0 + 0.1, -0.15), 0.5, 0.5, fc="#4b5563", ec="none"))
    ax.text(x0 + 0.75, 0.1, "= yes, past then future\n   is allowed", va="center",
            fontsize=BASE - 3, color=MUTED)
    ax.set_title("1  Table: pasts × futures", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=0.0)

    # 2: same rows -> same state
    ax = axs[1]

    def c2(i, j):
        g = ROWSTATE[i]
        return (GCOL[g][0], "", "white") if PAT[g][j] else (GCOL[g][1], "", INK)
    grid_table(ax, n, m, c2, x0, y0, row_lab=PASTS, col_lab=FUTS)
    for i, g in enumerate(ROWSTATE):
        ax.text(x0 + m + 0.25, y0 - (i + .5), g, ha="left", va="center", color=GCOL[g][0],
                fontsize=BASE, fontweight="bold")
    ax.text(x0 + m / 2, -0.05, "identical rows = same state\n6 pasts, only 3 states",
            ha="center", va="center", fontsize=BASE - 2, color=INK)
    ax.set_title("2  Same row = same state", loc="left", fontsize=BASE + 1,
                 fontweight="bold")

    # 3: blends
    ax = axs[2]
    R = np.array([[.9, .1, .5, .3], [.1, .7, .3, .5], [.4, .4, .8, .2]])
    R = np.vstack([R, (R[0] + R[1]) / 2])
    labs = ["…aa", "…ab", "…ba", "…bb"]
    clab = ["a", "b", "ab", "ba"]
    xx = x0 + 0.3

    def c3(i, j):
        if i == 3:
            return (DROP_L, f"{R[i, j]:.1f}", MUTED)
        return (STATE_L, f"{R[i, j]:.1f}", INK)
    grid_table(ax, 4, 4, c3, xx, y0, cw=1.05, ch=1.1, row_lab=labs, col_lab=clab,
               fs=BASE - 1)
    ax.text(xx + 2.1, y0 - 4.4 - 0.3, "row 4 = ½ row 1 + ½ row 2:\nnothing new",
            ha="center", va="top", color=MUTED, fontsize=BASE - 2)
    ax.text(xx + 2.1, 0.0, "3 independent rows = rank 3\n→ smallest machine: 3 states",
            ha="center", va="center", fontsize=BASE - 2, color=INK)
    ax.set_title("3  Blends add nothing", loc="left", fontsize=BASE + 1, fontweight="bold")

    # 4: singular values
    ax = axs[3]
    s = np.array([5.0, 3.4, 2.3, 0.62, 0.45, 0.33, 0.26, 0.2, 0.15, 0.11])
    r = 3
    sv_bars(ax, s, r, width=0.75)
    ax.set_ylim(0, 5.9)
    ax.set_yticks([])
    ax.set_xticks([1, 2, 3, 5, 10])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("directions, most important first", fontsize=BASE - 2, color=MUTED)
    ax.text(2.0, 5.25, "keep top r = 3", ha="center", color=STATE, fontsize=BASE - 1,
            fontweight="bold")
    ax.annotate("what you lose\nis bounded by\nthe grey bars", xy=(6.5, 0.6),
                xytext=(7.0, 2.4), ha="center", va="center", fontsize=BASE - 2, color=MUTED,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.0))
    ax.set_title("4  Keep the top r", loc="left", fontsize=BASE + 1, fontweight="bold")
    save(fig, "idea.png")


if __name__ == "__main__":
    make()
