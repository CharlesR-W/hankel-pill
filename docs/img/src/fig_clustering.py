"""Spectral clustering as 'where a random walker gets stuck'."""
from style import *


def make():
    rng = np.random.default_rng(4)
    centers = np.array([[0, 0], [3.2, 0.4], [1.4, 2.6]])
    X = np.vstack([c + rng.normal(0, 0.55, (70, 2)) for c in centers])
    n = len(X)
    D2 = ((X[:, None] - X[None]) ** 2).sum(-1)
    W = np.exp(-D2 / (2 * 0.62 ** 2))
    np.fill_diagonal(W, 0)
    d = W.sum(1)
    P = W / d[:, None]               # random-walk step table: here -> next
    Ssym = W / np.sqrt(np.outer(d, d))
    lam, V = np.linalg.eigh(Ssym)
    order = np.argsort(-lam)
    lam, V = lam[order], V[:, order]
    vec = V / np.sqrt(d)[:, None]    # right eigenvectors of P
    print("eigs", np.round(lam[:8], 3))
    # groups from the top 3 eigenvectors: assign by nearest of 3 well-separated rows
    E = vec[:, 1:3]
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    seeds = [0]
    for _ in range(2):
        dist = np.min([((E - E[s]) ** 2).sum(1) for s in seeds], 0)
        seeds.append(int(np.argmax(dist)))
    lab = np.argmin([((E - E[s]) ** 2).sum(1) for s in seeds], 0)
    # relabel by position
    lab = np.argsort(np.argsort([X[lab == k, 0].mean() + 10 * X[lab == k, 1].mean()
                                 for k in range(3)]))[lab]

    # random walk
    T = 700
    path = [5]
    for _ in range(T):
        path.append(rng.choice(n, p=P[path[-1]]))
    path = np.array(path)
    switches = (lab[path[1:]] != lab[path[:-1]]).sum()
    print("switches", switches)

    fig = plt.figure(figsize=(14, 4.7))
    ax = fig.add_axes([0.01, 0.04, 0.3, 0.74])
    ax.scatter(*X.T, s=18, color=DROP, zorder=1)
    ax.plot(*X[path].T, color=INK, lw=0.7, alpha=0.55, zorder=2)
    ax.plot(*X[path[0]], "o", color=PAST, ms=10, zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("A random walker gets stuck", loc="left", fontsize=BASE + 1,
                 fontweight="bold")
    ax.text(0.0, 1.0, f"{T} steps, only {switches} jumps between groups",
            transform=ax.transAxes, fontsize=BASE - 2, color=MUTED, va="top")

    ax = fig.add_axes([0.36, 0.04, 0.3, 0.74])
    for k in range(3):
        ax.scatter(*X[lab == k].T, s=22, color=GROUPS[k], zorder=2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Top directions mark the groups", loc="left", fontsize=BASE + 1,
                 fontweight="bold")
    ax.text(0.0, 1.0, "colour = pattern in the top eigenvectors", transform=ax.transAxes,
            fontsize=BASE - 2, color=MUTED, va="top")

    ax = fig.add_axes([0.73, 0.2, 0.25, 0.56])
    k = 10
    sv_bars(ax, lam[:k], 3)
    ax.set_ylim(0, 1.12)
    ax.set_yticks([0, 1])
    ax.set_xticks(range(1, k + 1))
    ax.tick_params(labelsize=BASE - 4)
    ax.set_xlabel("directions, ranked", fontsize=BASE - 2, color=MUTED)
    ax.annotate("", xy=(3.6, lam[3] + 0.02), xytext=(3.6, lam[2] - 0.01),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.4))
    ax.text(3.9, (lam[2] + lam[3]) / 2, "gap → 3 groups", ha="left", va="center",
            fontsize=BASE - 1, color=INK)
    ax.set_title("How slowly each pattern fades", loc="left", fontsize=BASE + 1,
                 fontweight="bold", x=-0.12)
    fig_arrow(fig, (0.31, 0.45), (0.35, 0.45))
    fig_arrow(fig, (0.665, 0.45), (0.705, 0.45))
    save(fig, "clustering.png")


if __name__ == "__main__":
    make()
