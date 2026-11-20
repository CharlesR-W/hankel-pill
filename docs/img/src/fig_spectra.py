"""Trace-formula teaser for a round drum: closed bouncing paths <-> tones.
Path lengths: periodic billiard orbits of the unit disk are star polygons (q, w),
length 2 q sin(pi w / q), plus their repeats.  Tones: Dirichlet eigenfrequencies of the
unit disk = zeros of Bessel functions j_{m,n}."""
from math import gcd

from scipy.special import jn_zeros

from style import *


def lines(ax, xs, col, h=1.0, lw=2.2):
    for x in xs:
        ax.plot([x, x], [0, h], color=col, lw=lw, solid_capstyle="butt")


def make():
    fig = plt.figure(figsize=(13, 5.0))
    # drum with a few closed paths
    ax = fig.add_axes([0.01, 0.1, 0.3, 0.74])
    blank(ax, (-1.15, 1.15), (-1.15, 1.15), equal=True)
    th = np.linspace(0, 2 * np.pi, 300)
    ax.fill(np.cos(th), np.sin(th), color=DROP_L, zorder=0)
    ax.plot(np.cos(th), np.sin(th), color=INK, lw=2.4)
    cols = [PAST, STATE, FUT, GROUPS[0]]
    orbits = [(2, 1, 0.3), (3, 1, 1.2), (4, 1, 0.1), (5, 2, 0.6)]
    for (q, w, rot), c in zip(orbits, cols):
        a = rot + 2 * np.pi * w * np.arange(q + 1) / q
        ax.plot(np.cos(a), np.sin(a), color=c, lw=2.2, alpha=0.9)
    ax.set_title("A round drum", loc="left", fontsize=BASE + 1, fontweight="bold")

    # path lengths (with repeats) up to Lmax
    Lmax = 13.0
    lens, lcol = [], []
    for q in range(2, 60):
        for w in range(1, q // 2 + 1):
            if gcd(q, w) != 1:
                continue
            L = 2 * q * np.sin(np.pi * w / q)
            k = 1
            while k * L <= Lmax:
                lens.append(k * L)
                hit = [(qq, ww) for qq, ww, _ in orbits].index((q, w)) if (q, w) in \
                    [(qq, ww) for qq, ww, _ in orbits] else None
                lcol.append(cols[hit] if hit is not None and k == 1 else DROP)
                k += 1
    axl = fig.add_axes([0.38, 0.58, 0.6, 0.22])
    for x, c in sorted(zip(lens, lcol), key=lambda t: t[1] != DROP):
        axl.plot([x, x], [0, 1], color=c, lw=2.2 if c != DROP else 1.4,
                 solid_capstyle="butt")
    axl.set_xlim(0, Lmax + 0.3)
    axl.set_ylim(0, 1.05)
    axl.set_yticks([])
    axl.set_xticks([])
    axl.spines["left"].set_visible(False)
    axl.set_xlabel("length →", fontsize=BASE - 2, color=MUTED, loc="right")
    axl.set_title("Lengths of its closed paths", loc="left", fontsize=BASE + 1,
                  fontweight="bold")

    fig.text(0.68, 0.44, "↕", fontsize=BASE + 14, ha="center", va="center", color=INK)

    axt = fig.add_axes([0.38, 0.12, 0.6, 0.2])
    tones = np.sort(np.concatenate([jn_zeros(m, 8) for m in range(0, 20)]))
    tones = tones[tones < 20]
    lines(axt, tones, STATE)
    axt.set_xlim(0, 20.5)
    axt.set_ylim(0, 1.05)
    axt.set_yticks([])
    axt.set_xticks([])
    axt.spines["left"].set_visible(False)
    axt.set_xlabel("pitch →", fontsize=BASE - 2, color=MUTED, loc="right")
    axt.set_title("The tones it can play", loc="left", fontsize=BASE + 1, fontweight="bold")

    mtext(fig, 0.7, 0.44, r"trace formula:  $\Sigma_{\mathrm{tones}} \cdots\ \leftrightarrow\ "
          r"\Sigma_{\mathrm{closed\ paths}} \cdots$", ha="left")
    ax.text(0, -1.12, "a ball bouncing inside: some closed paths\n(same colours on the right)", ha="center", va="top",
            fontsize=BASE - 2, color=MUTED)
    save(fig, "spectra.png")


if __name__ == "__main__":
    make()
