"""Myhill-Nerode for L = binary numerals (read most-significant bit first) divisible by 3.
The empty string counts as the number 0 (so it is accepted)."""
from style import *

PREFIXES = ["", "1", "10", "11", "100", "101", "110", "111"]
SUFFIXES = ["", "0", "1", "01", "10"]


def val(w):
    return int(w, 2) if w else 0


def in_L(w):
    return val(w) % 3 == 0


def make():
    T = np.array([[in_L(p + s) for s in SUFFIXES] for p in PREFIXES], int)
    cls = [val(p) % 3 for p in PREFIXES]
    # sanity: rows equal iff same remainder
    for i in range(len(PREFIXES)):
        for j in range(len(PREFIXES)):
            assert (T[i] == T[j]).all() == (cls[i] == cls[j])

    fig = plt.figure(figsize=(13, 5.0))
    ax = fig.add_axes([0.0, 0.0, 0.5, 0.86])
    n, m = T.shape
    blank(ax, (-0.6, 9.4), (-1.6, 9.45))
    x0, y0, cw, ch = 3.0, 8.4, 1.05, 0.95
    lab = lambda w: w if w else "ε"
    for i in range(n):
        g = cls[i]
        for j in range(m):
            on = T[i, j]
            ax.add_patch(Rectangle((x0 + j * cw, y0 - (i + 1) * ch), cw, ch,
                                   fc=GROUPS[g] if on else GROUPS_L[g], ec="white", lw=2))
            ax.text(x0 + (j + .5) * cw, y0 - (i + .5) * ch, "yes" if on else "no",
                    ha="center", va="center", fontsize=BASE - 3,
                    color="white" if on else MUTED, fontweight="bold" if on else "normal")
        ax.text(x0 - 0.15, y0 - (i + .5) * ch, lab(PREFIXES[i]), ha="right", va="center",
                color=PAST, fontsize=BASE, family="DejaVu Sans Mono")
        ax.text(x0 + m * cw + 0.15, y0 - (i + .5) * ch, f"rem {g}", ha="left", va="center",
                color=GROUPS[g], fontsize=BASE - 1, fontweight="bold")
    for j, s in enumerate(SUFFIXES):
        ax.text(x0 + (j + .5) * cw, y0 + 0.12, lab(s), ha="center", va="bottom", color=FUT,
                fontsize=BASE, family="DejaVu Sans Mono")
    ax.text(x0 - 1.5, y0 - n * ch / 2, "beginnings (pasts)", rotation=90, ha="center",
            va="center", color=PAST, fontsize=BASE, fontweight="bold")
    ax.text(x0 + m * cw / 2, y0 + 0.75, "endings (futures)", ha="center", va="bottom",
            color=FUT, fontsize=BASE, fontweight="bold")
    ax.text(x0 + m * cw / 2, y0 - n * ch - 0.35,
            "entry: is beginning+ending a multiple of 3?\nonly 3 different rows",
            ha="center", va="top", color=INK, fontsize=BASE - 2)
    ax.set_title("Language: binary numbers divisible by 3", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=0.08, pad=14)

    fig_arrow(fig, (0.505, 0.47), (0.585, 0.47), text="3 rows =\n3 states", text_dy=0.03)

    # DFA
    ax = fig.add_axes([0.59, 0.0, 0.41, 0.86])
    blank(ax, (-1.3, 5.6), (-2.2, 2.6), equal=True)
    R = 0.55
    P = {0: (0, 0), 1: (2.4, 0), 2: (4.8, 0)}
    for g, xy in P.items():
        state_circle(ax, xy, R, f"rem {g}", fc=GROUPS_L[g], ec=GROUPS[g], fs=BASE - 2,
                     accept=(g == 0))
    # transitions: reading bit b from remainder q goes to (2q+b) mod 3
    trans = {}
    for q in range(3):
        for b in (0, 1):
            trans.setdefault((q, (2 * q + b) % 3), []).append(str(b))
    for (q, t), bits in trans.items():
        lab_ = ",".join(bits)
        if q == t:
            ang = 90
            self_loop(ax, P[q], R, lab_, angle=ang, size=0.75, fs=BASE)
        else:
            curve = -0.35
            edge(ax, P[q], P[t], R, lab_, curve=curve, fs=BASE, label_off=0.22)
    # start arrow
    arrow(ax, (-1.2, -1.15), (-0.42, -0.4), lw=2, color=INK)
    ax.text(-1.25, -1.3, "start", ha="center", va="top", fontsize=BASE - 2, color=MUTED)
    ax.text(2.4, -2.05, "rem = remainder after dividing by 3\ndouble circle = accept; read bits left to right",
            ha="center", va="center", fontsize=BASE - 3, color=MUTED)
    ax.set_title("Smallest machine: 3 states", loc="left", fontsize=BASE + 1,
                 fontweight="bold")
    save(fig, "automata.png")


if __name__ == "__main__":
    make()
