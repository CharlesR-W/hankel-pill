"""Coherent sets in the periodically forced double gyre (Shadden et al. 2005 parameters)."""
from style import *

A_, EPS, OM = 0.1, 0.1, 2 * np.pi / 10


def vel(x, y, t):
    a = EPS * np.sin(OM * t)
    b = 1 - 2 * a
    f = a * x * x + b * x
    dfdx = 2 * a * x + b
    u = -np.pi * A_ * np.sin(np.pi * f) * np.cos(np.pi * y)
    v = np.pi * A_ * np.cos(np.pi * f) * np.sin(np.pi * y) * dfdx
    return u, v


def advect(x, y, T, dt=0.02):
    t = 0.0
    for _ in range(int(round(T / dt))):
        k1 = vel(x, y, t)
        k2 = vel(x + dt / 2 * k1[0], y + dt / 2 * k1[1], t + dt / 2)
        k3 = vel(x + dt / 2 * k2[0], y + dt / 2 * k2[1], t + dt / 2)
        k4 = vel(x + dt * k3[0], y + dt * k3[1], t + dt)
        x = x + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y = y + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += dt
    return np.clip(x, 0, 2), np.clip(y, 0, 1)


def blob(cx, cy, r, n, rng):
    th = rng.uniform(0, 2 * np.pi, n)
    rr = r * np.sqrt(rng.uniform(0, 1, n))
    return cx + rr * np.cos(th), cy + rr * np.sin(th)


def make():
    rng = np.random.default_rng(0)
    T = 20.0
    n = 4000
    b1 = blob(0.5, 0.6, 0.1, n, rng)   # inside the left gyre's core
    b2 = blob(1.2, 0.55, 0.1, n, rng)   # straddling the moving boundary between gyres
    e1, e2 = advect(*b1, T), advect(*b2, T)

    # transfer-operator (Ulam) table: box now -> box later, and its 2nd singular vector
    nx, ny, m = 40, 20, 36
    gx, gy = np.meshgrid((np.arange(nx) + 0.5) / nx * 2, (np.arange(ny) + 0.5) / ny)
    jx, jy = rng.uniform(-0.5, 0.5, (2, nx * ny, m))
    sx = (gx.ravel()[:, None] + jx * 2 / nx).ravel()
    sy = (gy.ravel()[:, None] + jy / ny).ravel()
    ex, ey = advect(sx, sy, T)
    src = np.repeat(np.arange(nx * ny), m)
    dst = np.minimum((ey * ny).astype(int), ny - 1) * nx + np.minimum((ex * nx).astype(int),
                                                                     nx - 1)
    P = np.zeros((nx * ny, nx * ny))
    np.add.at(P, (src, dst), 1.0 / m)
    p = np.full(nx * ny, 1.0 / (nx * ny))
    q = p @ P
    L = np.sqrt(p)[:, None] * P / np.sqrt(np.maximum(q, 1e-12))[None, :]
    U, s, Vt = np.linalg.svd(L)
    print("singular values", np.round(s[:6], 3))
    u2 = (U[:, 1] / np.sqrt(p)).reshape(ny, nx)

    fig = plt.figure(figsize=(13, 6.0))
    wl = 0.33
    hl = wl * 13 / 2 / 6.0
    axes = [fig.add_axes([0.02, 0.5, wl, hl]), fig.add_axes([0.02, 0.05, wl, hl])]
    wr = 0.57
    axr = fig.add_axes([0.42, 0.1, wr, wr * 13 / 2 / 6.0])

    # light streamlines at t=0 as background
    yy, xx = np.mgrid[0:1:80j, 0:2:160j]
    uu, vv = vel(xx, yy, 0.0)

    def frame(ax, ttl, stream=True):
        if stream:
            ax.streamplot(xx, yy, uu, vv, color="#e3e6ea", density=0.8, linewidth=0.8,
                          arrowsize=0.8, zorder=1)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 1)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(True)
            sp.set_color(DROP)
        ax.set_title(ttl, loc="left", fontsize=BASE + 1, fontweight="bold")

    frame(axes[0], "Now: two blobs of dye")
    axes[0].scatter(*b1, s=1.5, color=STATE, lw=0, zorder=3)
    axes[0].scatter(*b2, s=1.5, color=FUT, lw=0, zorder=3)
    frame(axes[1], "Later: one blob held together")
    axes[1].scatter(*e1, s=1.5, color=STATE, lw=0, zorder=3)
    axes[1].scatter(*e2, s=1.5, color=FUT, lw=0, zorder=3)

    v = u2 * np.sign(u2.ravel()[np.argmax(np.abs(u2))])
    frame(axr, "Top direction of the now → later table", stream=False)
    axr.imshow(np.clip(v, 0, None), origin="lower", extent=(0, 2, 0, 1), cmap="Greens",
               vmin=0, vmax=v.max(), interpolation="bilinear", zorder=1)
    th = np.linspace(0, 2 * np.pi, 100)
    axr.plot(0.5 + 0.1 * np.cos(th), 0.6 + 0.1 * np.sin(th), color=INK, lw=1.4,
             ls=(0, (3, 2)), zorder=3)
    axr.text(0.5, 0.45, "where the\ngreen blob\nstarted", ha="center", va="top",
             fontsize=BASE - 3, color=INK, zorder=3)
    axr.text(1.95, 0.05, "dark = a region that stays together\n(computed from the flow alone, no dye)",
             ha="right", va="bottom", fontsize=BASE - 2, color=MUTED, zorder=3)
    fig_arrow(fig, (0.365, 0.45), (0.405, 0.45), lw=3, ms=24)
    save(fig, "coherent.png")


if __name__ == "__main__":
    make()
