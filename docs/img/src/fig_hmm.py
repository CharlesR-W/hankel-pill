from style import *


def make():
    fig, ax = plt.subplots(figsize=(13, 5.0))
    blank(ax, (-0.9, 11.2), (-2.6, 3.15), equal=True)
    xs = np.arange(10) * 1.1
    now = 5
    xs = xs + np.where(np.arange(10) >= now, 0.35, 0.0)
    xs = xs - 0.15
    y_h, y_o = 1.15, -0.45
    obs = list("abbabaabba")
    R = 0.32
    # shaded halves
    box(ax, xs[0] - 0.55, y_o - 0.5, xs[now - 1] - xs[0] + 1.1, 2.75, fc=PAST_L, ec="none",
        r=0.12, z=0)
    box(ax, xs[now] - 0.55, y_o - 0.5, xs[-1] - xs[now] + 1.1, 2.75, fc=FUT_L, ec="none",
        r=0.12, z=0)
    for i, x in enumerate(xs):
        is_now = i == now
        col = STATE if is_now else (PAST if i < now else FUT)
        state_circle(ax, (x, y_h), R * (1.25 if is_now else 1.0), "",
                     fc=STATE_L if is_now else "white", ec=col if is_now else MUTED,
                     lw=3 if is_now else 1.6)
        ax.text(x, y_h, r"$x$" if is_now else "?", ha="center", va="center",
                fontsize=BASE + (2 if is_now else 0), color=INK if is_now else MUTED, zorder=8)
        # emission
        ecol = PAST if i < now else FUT
        ax.add_patch(Rectangle((x - 0.24, y_o - 0.24), 0.48, 0.48, fc="white", ec=ecol, lw=2,
                               zorder=4))
        ax.text(x, y_o, obs[i], ha="center", va="center", fontsize=BASE + 1, color=ecol,
                family="DejaVu Sans Mono", fontweight="bold", zorder=5)
        r0 = R * (1.25 if is_now else 1.0)
        arrow(ax, (x, y_h - r0), (x, y_o + 0.26), color=MUTED, lw=1.4, ms=12, ls=(0, (3, 2)))
        if i < 9:
            r1 = R * (1.25 if i + 1 == now else 1.0)
            arrow(ax, (x + r0, y_h), (xs[i + 1] - r1, y_h), color=MUTED, lw=1.6, ms=14)
    ax.text(xs[now], y_h - 0.62, "", ha="center")
    # labels
    xc_p = (xs[0] + xs[now - 1]) / 2
    xc_f = (xs[now] + xs[-1]) / 2
    ax.text(xc_p, y_o - 0.72, "past: what was seen", ha="center", va="top", color=PAST,
            fontsize=BASE, fontweight="bold")
    ax.text(xc_f, y_o - 0.72, "future: what will be seen", ha="center", va="top",
            color=FUT, fontsize=BASE, fontweight="bold")
    ax.text(xs[-1] + 0.5, y_h, "hidden", ha="left", va="center", color=MUTED,
            fontsize=BASE - 2, style="italic")
    ax.text(xs[-1] + 0.5, y_o, "noisy\nsignal", ha="left", va="center", color=MUTED,
            fontsize=BASE - 2, style="italic")
    # forward / backward
    ya = 2.55
    arrow(ax, (xs[0] - 0.2, ya), (xs[now] - 0.25, ya), color=PAST, lw=3, ms=22)
    ax.text(xc_p + 0.2, ya + 0.12, "forward: sum up the past", ha="center", va="bottom",
            color=PAST, fontsize=BASE - 1)
    arrow(ax, (xs[-1] + 0.2, ya), (xs[now] + 0.25, ya), color=FUT, lw=3, ms=22)
    ax.text(xc_f + 0.4, ya + 0.12, "backward: sum up the future", ha="center", va="bottom",
            color=FUT, fontsize=BASE - 1)
    ax.text(xs[now], ya - 0.32, "state now", ha="center", va="top", color=STATE,
            fontsize=BASE, fontweight="bold")
    ax.text(xs[now] - 0.2, -1.85,
            "given the hidden state now, the past tells you nothing more about the future",
            ha="center", va="center", color=INK, fontsize=BASE - 1)
    mtext(ax, xc_p + 0.2, ya - 0.38, r"$s(p) = P(p,\, \cdot\,)$", ha="center")
    mtext(ax, xc_f + 0.4, ya - 0.38, r"$g(f) = P(f \mid \cdot\,)$", ha="center")
    mtext(ax, xs[now] - 0.2, -2.4,
          r"$H[p,f] = \Sigma_x\, P(p, x)\, P(f \mid x)$,   $x$ = hidden state now", ha="center")
    save(fig, "hmm.png")


if __name__ == "__main__":
    make()
