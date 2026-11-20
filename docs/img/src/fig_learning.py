"""Spectral learning sketch: estimate a corner of the table from samples of a 2-state HMM,
SVD shows 2 big directions, recover a 2-state machine."""
from itertools import product

from style import *

T = np.array([[0.9, 0.1], [0.1, 0.9]])  # hidden transitions
E = np.array([[0.95, 0.05], [0.05, 0.95]])      # emissions P(a), P(b)


def sample(n, rng):
    pi = np.array([0.5, 0.5])  # stationary
    s = rng.choice(2, p=pi)
    out = []
    for _ in range(n):
        out.append("ab"[rng.choice(2, p=E[s])])
        s = rng.choice(2, p=T[s])
    return "".join(out)


def make():
    rng = np.random.default_rng(1)
    seq = sample(20000, rng)
    words = [""] + ["".join(w) for L in (1, 2) for w in product("ab", repeat=L)]
    counts = {}
    L = 4
    for i in range(len(seq) - L):
        for k in range(L + 1):
            counts[seq[i:i + k]] = counts.get(seq[i:i + k], 0) + 1
    N = len(seq) - L
    H = np.array([[counts.get(p + s, 0) / N for s in words] for p in words])
    sv = np.linalg.svd(H, compute_uv=False)
    print("sv", np.round(sv, 4))

    fig = plt.figure(figsize=(14, 4.6))
    ax = fig.add_axes([0, 0, 1, 0.88])
    blank(ax, (0, 14), (0, 4.6))
    # 1: data / queries
    ax.text(1.35, 4.25, "Ask or observe", ha="center", fontsize=BASE + 1, fontweight="bold")
    qs = ["seen: abbbaab…", "seen: aaaabba…", "seen: bbbaaab…", "ask: is “abba” OK?",
          "ask: is “bab” OK?"]
    for i, q in enumerate(qs):
        ax.text(0.15, 3.5 - i * 0.62, q, ha="left", va="center", fontsize=BASE - 2,
                family="DejaVu Sans Mono", color=INK if i < 3 else MUTED)
    arrow(ax, (2.85, 3.0), (3.55, 3.0), color=MUTED, lw=3, ms=22)

    # 2: big table with a filled corner
    ax.text(5.55, 4.25, "Fill a small corner", ha="center", fontsize=BASE + 1,
            fontweight="bold")
    gx0, gy1, c = 3.75, 3.85, 0.25
    n_big = 15
    for i in range(n_big):
        for j in range(n_big):
            if i < len(words) and j < len(words):
                v = H[i, j] / H.max()
                col = plt.cm.Greys(0.15 + 0.75 * v)
            else:
                col = DROP_L
            ax.add_patch(Rectangle((gx0 + j * c, gy1 - (i + 1) * c), c, c, fc=col, ec="white",
                                   lw=0.8))
    ax.text(gx0 + n_big * c + 0.08, gy1 - n_big * c, "…", fontsize=BASE + 2, color=MUTED,
            va="bottom")
    ax.text(gx0 + n_big * c / 2, gy1 + 0.05, "futures →", ha="center", va="bottom",
            fontsize=BASE - 3, color=FUT)
    ax.text(gx0 - 0.08, gy1 - n_big * c / 2, "pasts →", ha="right", va="center",
            fontsize=BASE - 3, color=PAST, rotation=270)
    ax.text(gx0 + n_big * c / 2, gy1 - n_big * c - 0.12,
            "estimated: how often\npast-then-future occurs", ha="center", va="top",
            fontsize=BASE - 3, color=MUTED)
    arrow(ax, (7.75, 2.2), (8.35, 2.2), color=MUTED, lw=3, ms=22)
    ax.text(8.05, 2.35, "SVD", ha="center", va="bottom", fontsize=BASE - 2, color=MUTED)

    # 3: singular values
    ax.text(9.65, 4.25, "Find its rank", ha="center", fontsize=BASE + 1, fontweight="bold")
    axb = fig.add_axes([0.61, 0.2, 0.15, 0.52])
    sv_bars(axb, sv, 2)
    axb.set_yticks([])
    axb.spines["left"].set_visible(False)
    axb.set_xticks(range(1, len(sv) + 1))
    axb.tick_params(labelsize=BASE - 4)
    axb.text(1.5, sv[0] * 0.98, "2 big", ha="left", color=STATE, fontsize=BASE - 1,
             fontweight="bold", va="top", transform=axb.transData)
    axb.text(len(sv) * 0.62, sv[0] * 0.3, "the rest:\n≈ 0 (noise)", ha="center",
             color=MUTED, fontsize=BASE - 3)
    arrow(ax, (11.05, 2.2), (11.6, 2.2), color=MUTED, lw=3, ms=22)

    # 4: recovered machine
    ax.text(12.75, 4.25, "Recover the machine", ha="center", fontsize=BASE + 1,
            fontweight="bold")
    R = 0.42
    A, B = (12.05, 2.2), (13.45, 2.2)
    state_circle(ax, A, R, "1", fc=STATE_L, ec=STATE, fs=BASE)
    state_circle(ax, B, R, "2", fc=STATE_L, ec=STATE, fs=BASE)
    self_loop(ax, A, R, "", angle=90, size=0.45)
    self_loop(ax, B, R, "", angle=90, size=0.45)
    edge(ax, A, B, R, "", curve=-0.35)
    edge(ax, B, A, R, "", curve=-0.35)
    ax.text(12.05, 1.55, "mostly a", ha="center", va="top", fontsize=BASE - 3, color=MUTED)
    ax.text(13.45, 1.55, "mostly b", ha="center", va="top", fontsize=BASE - 3, color=MUTED)
    ax.text(12.75, 1.0, "2 hidden states,\nno local optima", ha="center", va="top",
            fontsize=BASE - 3, color=INK)
    ax.set_aspect("equal")
    save(fig, "learning.png")


if __name__ == "__main__":
    make()
