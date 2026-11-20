"""Causal states of the Even Process: 1s come in runs of even length.
Machine: A --0 (1/2)--> A, A --1 (1/2)--> B, B --1 (1)--> A.
A past ending in 0 followed by an even number of 1s is in A; odd -> B."""
from style import *

PASTS = ["…0", "…01", "…011", "…00", "…0111", "…0110", "…01101", "…011011"]


def cls(p):
    run = len(p) - len(p.rstrip("1"))
    return run % 2  # 0 -> A, 1 -> B


PRED = {0: (0.5, 0.5), 1: (0.0, 1.0)}  # P(next=0), P(next=1)
NAME = {0: "A", 1: "B"}


def minibars(ax, x, y, probs, col, w=0.22, h=0.5, labels=False, fs=BASE - 4):
    ax.plot([x - 0.08, x + 2 * w + 0.12], [y, y], color=MUTED, lw=1)
    for k, p in enumerate(probs):
        ax.add_patch(Rectangle((x + k * (w + 0.06), y), w, max(p * h, 0.0), fc=col, ec="none"))
        if labels:
            ax.text(x + k * (w + 0.06) + w / 2, y - 0.05, str(k), ha="center", va="top",
                    fontsize=fs, color=MUTED, family="DejaVu Sans Mono")


def make():
    fig, ax = plt.subplots(figsize=(13, 5.0))
    blank(ax, (0, 13.6), (-0.15, 5.4), equal=True)
    n = len(PASTS)
    ys = np.linspace(4.45, 0.35, n)
    xs_txt, xs_bar = 1.75, 2.05
    ax.text(1.0, 5.1, "pasts", ha="center", va="center", color=PAST, fontsize=BASE,
            fontweight="bold")
    ax.text(2.4, 5.1, "next?", ha="center", va="center", color=FUT, fontsize=BASE - 1,
            fontweight="bold")
    binA, binB = (5.6, 3.35), (5.6, 1.3)
    for p, y in zip(PASTS, ys):
        c = cls(p)
        col = GROUPS[c]
        ax.text(xs_txt, y + 0.15, p, ha="right", va="center", family="DejaVu Sans Mono",
                fontsize=BASE - 1, color=PAST)
        minibars(ax, xs_bar, y - 0.05, PRED[c], FUT, h=0.42)
        tgt = binA if c == 0 else binB
        bezier(ax, (2.85, y + 0.15), (tgt[0] - 0.95, tgt[1]), col, lw=1.8, alpha=0.7)
    for k in range(2):
        ax.text(xs_bar + k * 0.28 + 0.11, -0.02, str(k), ha="center", va="center",
                fontsize=BASE - 3, color=MUTED, family="DejaVu Sans Mono")
    # bins
    for c, (bx, by) in zip((0, 1), (binA, binB)):
        box(ax, bx - 0.95, by - 0.7, 1.9, 1.4, fc=GROUPS_L[c], ec=GROUPS[c], lw=2.2, r=0.12)
        ax.text(bx - 0.5, by, NAME[c], ha="center", va="center", fontsize=BASE + 6,
                fontweight="bold", color=GROUPS[c])
        minibars(ax, bx + 0.0, by - 0.3, PRED[c], FUT, w=0.28, h=0.75, labels=True)
    ax.text(5.6, 4.55, "group pasts that\npredict the same", ha="center", va="bottom",
            fontsize=BASE - 1, color=INK)
    ax.text(5.6, 0.25, "A: even run of 1s so far\nB: odd run (a 1 must follow)",
            ha="center", va="top", fontsize=BASE - 3, color=MUTED)
    arrow(ax, (6.85, 2.35), (7.85, 2.35), color=MUTED, lw=3, ms=24)
    # epsilon machine
    R = 0.55
    A, B = (9.3, 2.1), (12.1, 2.1)
    state_circle(ax, A, R, "A", fc=GROUPS_L[0], ec=GROUPS[0], fs=BASE + 2)
    state_circle(ax, B, R, "B", fc=GROUPS_L[1], ec=GROUPS[1], fs=BASE + 2)
    self_loop(ax, A, R, "0  (½)", angle=90, size=0.7, fs=BASE - 1)
    edge(ax, A, B, R, "1  (½)", curve=-0.3, fs=BASE - 1, label_off=0.3)
    edge(ax, B, A, R, "1  (always)", curve=-0.3, fs=BASE - 1, label_off=0.3)
    ax.text(10.7, 4.55, "the ε-machine:\nthe smallest predictor", ha="center", va="bottom",
            fontsize=BASE - 1, color=INK)
    ax.text(10.7, 0.25, "Even Process: 1s come\nin runs of even length",
            ha="center", va="top", fontsize=BASE - 3, color=MUTED)
    save(fig, "epsilon.png")


if __name__ == "__main__":
    make()
