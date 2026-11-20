"""Trace-formula teaser: closed paths <-> tones (round drum), primes <-> zeta zeros."""
from scipy.special import jn_zeros

from style import *

ZETA = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052,
        49.7738]
PRIMES = [p for p in range(2, 50) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def lines(ax, xs, col, h=1.0, lw=2.2):
    for x in xs:
        ax.plot([x, x], [0, h], color=col, lw=lw, solid_capstyle="butt")


def make():
    fig = plt.figure(figsize=(13, 5.0))
    # --- row 1: drum
    ax = fig.add_axes([0.02, 0.5, 0.2, 0.42])
    blank(ax, (-1.25, 1.25), (-1.15, 1.15), equal=True)
    th = np.linspace(0, 2 * np.pi, 300)
    ax.fill(np.cos(th), np.sin(th), color=DROP_L, zorder=0)
    ax.plot(np.cos(th), np.sin(th), color=INK, lw=2.2)
    cols = [PAST, STATE, FUT, GROUPS[0]]
    for (q, w, rot), c in zip([(2, 1, 0.3), (3, 1, 1.2), (4, 1, 0.1), (5, 2, 0.6)], cols):
        k = np.arange(q + 1)
        a = rot + 2 * np.pi * w * k / q
        ax.plot(np.cos(a), np.sin(a), color=c, lw=2.0, alpha=0.9)
    ax.text(0, -1.22, "closed paths of a ball\nbouncing inside", ha="center", va="top",
            fontsize=BASE - 2, color=MUTED)
    ax.set_title("A round drum", loc="left", fontsize=BASE + 1, fontweight="bold")
    fig.text(0.255, 0.71, "↔", fontsize=BASE + 16, ha="center", va="center", color=INK)
    ax = fig.add_axes([0.3, 0.6, 0.66, 0.2])
    tones = np.sort(np.concatenate([jn_zeros(m, 6) for m in range(0, 14)]))
    tones = tones[tones < 20]
    lines(ax, tones, STATE)
    ax.set_xlim(0, 20.5)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("pitch →", fontsize=BASE - 2, color=MUTED, loc="right")
    ax.set_title("The tones it can play", loc="left", fontsize=BASE + 1,
                 fontweight="bold")

    # --- row 2: primes and zeros
    ax = fig.add_axes([0.02, 0.09, 0.2, 0.22])
    lines(ax, PRIMES, PAST, lw=2.0)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([])
    ax.set_xticks([2, 10, 20, 30, 40, 50])
    ax.tick_params(labelsize=BASE - 4)
    ax.spines["left"].set_visible(False)
    ax.set_title("The primes", loc="left", fontsize=BASE + 1, fontweight="bold")
    fig.text(0.255, 0.2, "↔", fontsize=BASE + 16, ha="center", va="center", color=INK)
    ax = fig.add_axes([0.3, 0.09, 0.66, 0.22])
    lines(ax, ZETA, FUT)
    ax.set_xlim(0, 51)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([])
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.tick_params(labelsize=BASE - 4)
    ax.spines["left"].set_visible(False)
    ax.set_title("Zeros of the Riemann zeta function (heights)", loc="left",
                 fontsize=BASE + 1, fontweight="bold")
    fig.text(0.98, 0.43,
             "trace formulas: either side can be computed from the other",
             fontsize=BASE - 1, color=MUTED, ha="right", va="center", style="italic")
    save(fig, "spectra.png")


if __name__ == "__main__":
    make()
