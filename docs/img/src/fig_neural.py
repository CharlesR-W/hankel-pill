"""A language model's prompts x continuations table (GPT-2 small, real numbers from
data/lm_table.npz, made by lm_table.py) and its singular values."""
from pathlib import Path

from style import *

DATA = Path(__file__).parent / "data" / "lm_table.npz"


def make():
    d = np.load(DATA)
    S, prompts, conts = d["show"], list(d["show_prompts"]), list(d["show_conts"])
    B = d["big"].astype(float)
    Bc = B - B.mean(0) - B.mean(1)[:, None] + B.mean()   # remove row/column averages
    s = np.linalg.svd(Bc, compute_uv=False)
    rng = np.random.default_rng(0)
    sh = rng.permutation(Bc.ravel()).reshape(Bc.shape)
    ss = np.linalg.svd(sh, compute_uv=False)
    energy = np.cumsum(s ** 2) / np.sum(s ** 2)
    r = int(np.searchsorted(energy, 0.8)) + 1
    print("r for 80%", r)

    fig = plt.figure(figsize=(14, 5.0))
    ax = fig.add_axes([0.25, 0.08, 0.3, 0.66])
    ax.imshow(S, cmap="Blues", vmin=-17, vmax=0, aspect="auto")
    for i in range(S.shape[0]):
        for j in range(S.shape[1]):
            ax.text(j, i, f"{S[i, j]:.0f}", ha="center", va="center", fontsize=BASE - 4,
                    color="white" if S[i, j] > -5 else INK)
    ax.set_yticks(range(len(prompts)))
    ax.set_yticklabels([p + " …" for p in prompts], fontsize=BASE - 3, color=PAST)
    ax.set_xticks(range(len(conts)))
    ax.set_xticklabels([c.strip() for c in conts], fontsize=BASE - 3, color=FUT, rotation=40,
                       ha="left", rotation_mode="anchor")
    ax.xaxis.tick_top()
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    fig.text(0.01, 0.95, "A language model's table", fontsize=BASE + 1, fontweight="bold")
    fig.text(0.01, 0.89, "rows: prompts   columns: next word\nentry: log-probability under GPT-2\n(darker = more likely)",
             fontsize=BASE - 2, color=MUTED, va="top")

    ax = fig.add_axes([0.66, 0.2, 0.32, 0.56])
    k = 120
    idx = np.arange(1, k + 1)
    ax.bar(idx[:r], s[:r] / s[0], color=STATE, width=0.9)
    ax.bar(idx[r:], s[r:k] / s[0], color=DROP, width=0.9)
    ax.plot(idx, ss[:k] / s[0], color=MUTED, lw=1.6, ls=(0, (4, 2)))
    ax.set_yscale("log")
    ax.set_xlim(0, k + 1)
    ax.set_ylim(0.03, 1.3)
    ax.set_yticks([])
    ax.minorticks_off()
    ax.set_xticks([1, r, 50, 100])
    ax.tick_params(labelsize=BASE - 4)
    ax.set_xlabel("directions, ranked  (table: 400 web-text prompts\n× 400 common next words; log scale)", fontsize=BASE - 2, color=MUTED)
    ax.text(r + 2, s[3] / s[0], f"top {r} carry\n80% of the variation", ha="left", va="center",
            color=STATE, fontsize=BASE - 1, fontweight="bold")
    ax.text(k * 0.97, ss[k - 1] / s[0] * 1.2, "same numbers shuffled:\nno structure",
            ha="right", va="bottom", color=MUTED, fontsize=BASE - 3)
    ax.set_title("Approximately low rank", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=-0.02)
    fig_arrow(fig, (0.585, 0.45), (0.635, 0.45), text="SVD", text_dy=0.02)
    save(fig, "neural.png")


if __name__ == "__main__":
    make()
