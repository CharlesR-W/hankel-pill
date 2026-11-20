from style import *


def make():
    fig, ax = plt.subplots(figsize=(12, 4.6))
    blank(ax, (0, 12), (0, 4.6))
    pasts = ["…0110", "…1011", "…0001", "…1110", "…0101", "…1000", "…0011"]
    futs = ["10…", "011…", "1…", "00…", "110…", "0101…", "01…"]
    s = [1.0, 0.72, 0.5, 0.26, 0.15, 0.09, 0.05]
    r = 3
    k = bowtie(ax, xc=6.0, yc=2.05, s=s, r=r, x_left=2.3, x_right=9.7, half_h=1.45,
               n_past=7, n_fut=7, past_labels=pasts, fut_labels=futs, bar_w=1.5, bar_h=0.17,
               bar_gap=0.07, fs=BASE - 1, lw=1.8, alpha=0.6, knot_label=None, show_bracket=False)
    ax.text(1.35, 4.25, "what has happened", ha="center", color=PAST, fontsize=BASE + 3,
            fontweight="bold")
    ax.text(1.35, 3.9, "(pasts)", ha="center", color=PAST, fontsize=BASE)
    ax.text(10.65, 4.25, "what happens next", ha="center", color=FUT, fontsize=BASE + 3,
            fontweight="bold")
    ax.text(10.65, 3.9, "(futures)", ha="center", color=FUT, fontsize=BASE)
    ax.text(6.0, 4.25, "the state", ha="center", color=STATE, fontsize=BASE + 3,
            fontweight="bold")
    ax.text(6.0, 3.9, "what you need to remember", ha="center", color=STATE, fontsize=BASE)
    ax.text(6.0, k["top"] + 0.14, f"keep the top r = {r}", ha="center", va="bottom",
            color=STATE, fontsize=BASE, fontweight="bold")
    mtext(ax, 6.0, 0.02, r"error $\sim\ \sigma_{r+1},\ \sigma_{r+2},\ \ldots$", ha="center",
          va="bottom")
    ax.annotate("drop the rest", xy=(6.0, k["tail_bot"] - 0.04),
                xytext=(6.0, 0.42), ha="center", va="bottom", color=MUTED,
                fontsize=BASE - 2,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1.0, shrinkA=2, shrinkB=2))
    mtext(ax, 6.0, -0.35, r"$H[p,\,f] = \langle\, s(p),\ g(f)\, \rangle,\qquad s(p) \in \mathbb{R}^r$",
          ha="center", va="center", fs=MATH_FS + 1)
    save(fig, "bowtie.png")


if __name__ == "__main__":
    make()
