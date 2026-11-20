"""Shared style and drawing helpers for the README figures."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Circle, FancyArrowPatch, FancyBboxPatch, PathPatch,
                                Rectangle)
from matplotlib.path import Path as MPath

OUT_DIR = Path(__file__).resolve().parent.parent  # docs/img

# ---- palette -------------------------------------------------------------
PAST = "#2563a8"      # pasts / inputs / "what has happened"
PAST_L = "#dbe7f5"
FUT = "#d9590f"       # futures / outputs / "what happens next"
FUT_L = "#fbe4d3"
STATE = "#2b8a3e"     # state / kept directions
STATE_L = "#d8f0dc"
DROP = "#b8bec6"      # discarded / tail
DROP_L = "#eceef1"
INK = "#1f2329"
MUTED = "#6b7280"
# colours for "these rows are the same state" groupings
GROUPS = ["#7c4dcc", "#0f8fa3", "#d69e00", "#c2255c"]
GROUPS_L = ["#ebe2f8", "#d5eef2", "#f8edc8", "#f7d9e4"]

BASE = 15


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": BASE,
        "axes.titlesize": BASE + 1,
        "axes.titleweight": "bold",
        "axes.labelsize": BASE,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": BASE - 2,
        "ytick.labelsize": BASE - 2,
        "text.color": INK,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "mathtext.fontset": "dejavusans",
    })


setup()


def blank(ax, xlim=(0, 1), ylim=(0, 1), equal=False):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    if equal:
        ax.set_aspect("equal")
    return ax


def title(ax, text, num=None, color=INK, loc="left", y=1.0, size=BASE + 1):
    s = f"{num}  {text}" if num is not None else text
    ax.set_title(s, loc=loc, color=color, fontsize=size, fontweight="bold", pad=10, y=y)


def save(fig, name, dpi=170):
    path = OUT_DIR / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    kb = path.stat().st_size / 1024
    if kb > 250:  # shrink with an adaptive palette; these are flat-colour schematics
        from PIL import Image
        im = Image.open(path).convert("RGB")
        im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE) \
          .save(path, optimize=True)
        kb = path.stat().st_size / 1024
    print(f"{name}: {kb:.0f} KB")
    return path


# ---- primitives -----------------------------------------------------------
def arrow(ax, p0, p1, color=INK, lw=2.2, rad=0.0, ms=18, style="-|>", ls="-", z=3,
          shrinkA=0, shrinkB=0, transform=None, alpha=1.0):
    a = FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                        connectionstyle=f"arc3,rad={rad}", linestyle=ls, zorder=z,
                        shrinkA=shrinkA, shrinkB=shrinkB, alpha=alpha,
                        transform=transform if transform is not None else ax.transData)
    ax.add_patch(a)
    return a


def fig_arrow(fig, p0, p1, color=MUTED, lw=3, ms=26, text=None, text_dy=0.03, fs=BASE - 1,
              rad=0.0):
    """Arrow in figure-fraction coordinates (between panels)."""
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw,
                        transform=fig.transFigure, connectionstyle=f"arc3,rad={rad}")
    fig.patches.append(a)
    if text:
        fig.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + text_dy, text, ha="center",
                 va="bottom", color=color, fontsize=fs, style="italic")


def box(ax, x, y, w, h, fc="white", ec=INK, lw=1.8, r=0.04, z=1, alpha=1.0, ls="-"):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec,
                       lw=lw, zorder=z, alpha=alpha, linestyle=ls)
    ax.add_patch(p)
    return p


def bezier(ax, p0, p1, color, lw=1.4, alpha=0.6, z=1, bend=0.5):
    """Horizontal S-curve from p0 to p1."""
    (x0, y0), (x1, y1) = p0, p1
    dx = (x1 - x0) * bend
    path = MPath([(x0, y0), (x0 + dx, y0), (x1 - dx, y1), (x1, y1)],
                 [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
    ax.add_patch(PathPatch(path, fc="none", ec=color, lw=lw, alpha=alpha, zorder=z,
                           capstyle="round"))


def sv_bars(ax, s, r, kept=STATE, drop=DROP, horizontal=False, labels=True, width=0.72,
            lost_text=None, fs=BASE - 1, edge=False):
    """Singular-value bar chart: first r bars kept (coloured), the rest grey."""
    s = np.asarray(s, float)
    idx = np.arange(1, len(s) + 1)
    cols = [kept if i < r else drop for i in range(len(s))]
    if horizontal:
        ax.barh(idx, s, color=cols, height=width)
        ax.invert_yaxis()
    else:
        ax.bar(idx, s, color=cols, width=width, edgecolor="none")
        ax.set_xlim(0.3, len(s) + 0.7)
    return idx


def state_circle(ax, xy, rad, label="", fc=STATE_L, ec=STATE, lw=2.2, fs=BASE, accept=False,
                 z=4, tc=INK, bold=True):
    ax.add_patch(Circle(xy, rad, fc=fc, ec=ec, lw=lw, zorder=z))
    if accept:
        ax.add_patch(Circle(xy, rad * 0.82, fc="none", ec=ec, lw=lw * 0.8, zorder=z + 1))
    if label:
        ax.text(xy[0], xy[1], label, ha="center", va="center", fontsize=fs, zorder=z + 2,
                color=tc, fontweight="bold" if bold else "normal")


def edge(ax, a, b, rad_node, label="", curve=0.25, color=INK, fs=BASE - 1, lw=1.8,
         label_off=0.12, ms=16, label_color=None, tilt=0.6):
    """Curved arrow between two state circles (centres a, b, radius rad_node).
    Positive curve bends to the right of the direction of travel (matplotlib arc3)."""
    a, b = np.array(a, float), np.array(b, float)
    d = b - a
    n = d / np.linalg.norm(d)
    v = np.array([d[1], -d[0]]) * curve          # arc3 bulge direction
    vu = v / (np.linalg.norm(v) + 1e-12)
    p0 = a + rad_node * (n + tilt * vu) / np.linalg.norm(n + tilt * vu)
    p1 = b + rad_node * (-n + tilt * vu) / np.linalg.norm(-n + tilt * vu)
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, color=color,
                                 lw=lw, connectionstyle=f"arc3,rad={curve}", zorder=3))
    if label:
        dd = p1 - p0
        apex = (p0 + p1) / 2 + 0.5 * curve * np.array([dd[1], -dd[0]])
        ax.text(*(apex + vu * label_off), label, ha="center", va="center", fontsize=fs,
                zorder=6, color=label_color or color,
                bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.9))


def self_loop(ax, c, rad_node, label="", angle=90, size=None, color=INK, fs=BASE - 1, lw=1.8,
              ms=16, label_color=None, spread=35):
    """Self-loop on the side of the node given by angle (degrees), drawn as a cubic."""
    c = np.array(c, float)
    h = size or rad_node * 1.6
    t = np.deg2rad(angle)
    u = np.array([np.cos(t), np.sin(t)])
    w = np.array([-u[1], u[0]])
    sp = np.deg2rad(spread)
    p0 = c + rad_node * (np.cos(sp) * u + np.sin(sp) * w)
    p1 = c + rad_node * (np.cos(sp) * u - np.sin(sp) * w)
    c0 = p0 + u * h + w * h * 0.55
    c1 = p1 + u * h - w * h * 0.55
    path = MPath([p0, c0, c1, p1], [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle="-|>", mutation_scale=ms, color=color,
                                 lw=lw, zorder=3))
    if label:
        q = c + u * (rad_node + h * 0.75 + 0.02)
        ax.text(*(q + u * 0.12), label, ha="center", va="center", fontsize=fs, zorder=6,
                color=label_color or color,
                bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.9))


# ---- the bowtie motif -----------------------------------------------------
def bowtie(ax, xc, yc, s, r, x_left, x_right, half_h=1.0, n_past=9, n_fut=9,
           past_labels=None, fut_labels=None, bar_h=0.11, bar_gap=0.05, bar_w=1.0,
           lw=1.3, alpha=0.55, fs=BASE - 2, show_bracket=True, bracket_text=None,
           knot_label="state", knot_fs=BASE, seed=0):
    """Many pasts (left) funnel into a knot of r bars (singular values) and fan out to
    futures (right).  Bars: kept ones coloured, the rest faint grey.  Returns knot bbox."""
    s = np.asarray(s, float) / np.max(s)
    k = len(s)
    total_h = k * bar_h + (k - 1) * bar_gap
    ys = yc + total_h / 2 - bar_h / 2 - np.arange(k) * (bar_h + bar_gap)
    kept_top = ys[0] + bar_h / 2
    kept_bot = ys[r - 1] - bar_h / 2
    kx0, kx1 = xc - bar_w / 2 - 0.08, xc + bar_w / 2 + 0.08
    # strands
    py = np.linspace(yc - half_h, yc + half_h, n_past)
    fy = np.linspace(yc - half_h, yc + half_h, n_fut)
    ky = np.linspace(kept_bot + 0.02, kept_top - 0.02, max(n_past, n_fut))
    for j, y in enumerate(py):
        t = ky[int(round(j * (len(ky) - 1) / max(n_past - 1, 1)))]
        bezier(ax, (x_left, y), (kx0, t), PAST, lw=lw, alpha=alpha, bend=0.55)
    for j, y in enumerate(fy):
        t = ky[int(round(j * (len(ky) - 1) / max(n_fut - 1, 1)))]
        bezier(ax, (kx1, t), (x_right, y), FUT, lw=lw, alpha=alpha, bend=0.45)
    # knot background
    box(ax, kx0, kept_bot - 0.06, kx1 - kx0, kept_top - kept_bot + 0.12, fc="white",
        ec=STATE, lw=2.0, r=0.05, z=4)
    for i in range(k):
        w = bar_w * s[i]
        kept = i < r
        ax.add_patch(Rectangle((xc - w / 2, ys[i] - bar_h / 2), w, bar_h,
                               fc=STATE if kept else DROP, ec="none",
                               alpha=1.0 if kept else 0.6, zorder=5))
    if past_labels:
        for y, t in zip(np.linspace(yc - half_h, yc + half_h, len(past_labels))[::-1],
                        past_labels):
            ax.text(x_left - 0.05, y, t, ha="right", va="center", color=PAST, fontsize=fs,
                    family="DejaVu Sans Mono")
    if fut_labels:
        for y, t in zip(np.linspace(yc - half_h, yc + half_h, len(fut_labels))[::-1],
                        fut_labels):
            ax.text(x_right + 0.05, y, t, ha="left", va="center", color=FUT, fontsize=fs,
                    family="DejaVu Sans Mono")
    if knot_label:
        ax.text(xc, kept_top + 0.14, knot_label, ha="center", va="bottom", color=STATE,
                fontsize=knot_fs, fontweight="bold", zorder=6)
    if show_bracket:
        bx = kx1 + 0.06
        ax.plot([bx, bx + 0.05, bx + 0.05, bx], [kept_top, kept_top, kept_bot, kept_bot],
                color=STATE, lw=1.6, zorder=6)
    return dict(kx0=kx0, kx1=kx1, top=kept_top, bot=kept_bot, ys=ys,
                tail_bot=ys[-1] - bar_h / 2)


# ---- the "math strip": one consistent style for the small formulas -----------
MATH = "#3b4048"
MATH_FS = BASE - 1


def mtext(target, x, y, s, ha="left", va="center", fs=MATH_FS, transform=None, **kw):
    """Small dark-grey mathtext label (same size and colour in every figure).
    target: an Axes (data coords unless transform given) or a Figure (figure coords)."""
    if hasattr(target, "transData"):
        tr = transform if transform is not None else target.transData
    else:
        tr = transform if transform is not None else target.transFigure
    return target.text(x, y, s, ha=ha, va=va, fontsize=fs, color=MATH, transform=tr,
                       zorder=10, **kw)
