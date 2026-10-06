"""Render the PNG charts for the Word document (200 dpi)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import data as D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "charts")
os.makedirs(OUT, exist_ok=True)

INK = "#1F2A44"
INK2 = "#52514e"
MUTED = "#8a8984"
GRID = "#e6e5e1"
BRAND_COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
TYPE_COLORS = {"online": "#2a78d6", "retail": "#eb6834", "social": "#1baf7a",
               "capital": "#4a3aa7", "marker": "#8a8984"}
TYPE_MARKERS = {"online": "o", "retail": "s", "social": "D", "capital": "^", "marker": "P"}

plt.rcParams.update({
    "font.family": ["Inter", "DejaVu Sans"],
    "font.size": 9,
    "text.color": INK, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": GRID, "axes.spines.top": False, "axes.spines.right": False,
})


def finish(fig, title, source, path, subtitle=None):
    fig.suptitle(title, x=0.01, ha="left", fontsize=12.5, fontweight="bold", color=INK, y=0.985)
    if subtitle:
        h = fig.get_size_inches()[1]
        fig.text(0.01, 1 - 0.40 / h, subtitle, ha="left", va="top", fontsize=9, color=INK2)
    fig.text(0.01, 0.012, source, ha="left", fontsize=7.5, color=MUTED)
    fig.savefig(path, dpi=200, facecolor="white")
    plt.close(fig)


def scorecard():
    fig, ax = plt.subplots(figsize=(8, 5.2))
    fig.subplots_adjust(left=0.2, right=0.97, top=0.84, bottom=0.17)
    n = len(D.BRAND_KEYS)
    h = 0.15
    crit = D.CRITERIA[::-1]
    for bi, k in enumerate(D.BRAND_KEYS):
        vals = D.SCORES[k][::-1]
        ys = [ci + (n / 2 - bi - 0.5) * h for ci in range(len(crit))]
        ax.barh(ys, vals, height=h - 0.02, color=BRAND_COLORS[bi], label=D.BRAND_META[k]["name"],
                edgecolor="white", linewidth=0.6)
        for y, v in zip(ys, vals):
            ax.text(v + 0.05, y, f"{v:g}", va="center", fontsize=6.8, color=INK2)
    ax.set_yticks(range(len(crit)))
    ax.set_yticklabels(crit, fontsize=9, color=INK)
    ax.set_xlim(0, 5.4)
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xlabel("Score (1 = weak, 5 = strong)")
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.4, -0.12), frameon=False, fontsize=8.5,
              handlelength=1.2, columnspacing=1.2)
    finish(fig, "Story clarity scores highest; story-product fit scores lowest",
           D.SOURCE_SCORES, os.path.join(OUT, "fig_scorecard.png"),
           subtitle="Average across brands: clarity 4.4, marketing 4.2, sales 4.0, overall 3.9, story-product 3.6")


def pattern_counts():
    pats = D.PATTERNS[::-1]
    fig, ax = plt.subplots(figsize=(8, 5.4))
    fig.subplots_adjust(left=0.43, right=0.96, top=0.9, bottom=0.17)
    colors = ["#2a78d6" if p["group"] == "Shared" else "#eb6834" for p in pats]
    ax.barh(range(len(pats)), [p["count"] for p in pats], color=colors, height=0.66,
            edgecolor="white", linewidth=0.6)
    for i, p in enumerate(pats):
        ax.text(p["count"] + 0.06, i, f"{p['count']} of 5", va="center", fontsize=8, color=INK2)
    ax.set_yticks(range(len(pats)))
    ax.set_yticklabels([f"{p['id']}  {p['name']}" for p in pats], fontsize=8.3, color=INK)
    ax.set_xlim(0, 5.7)
    ax.set_xticks(range(6))
    ax.set_xlabel("Number of the five brands that support the pattern")
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(handles=[Patch(color="#2a78d6", label="Shared success trait"),
                       Patch(color="#eb6834", label="Warning sign")],
              loc="upper center", bbox_to_anchor=(0.3, -0.12), ncol=2, frameon=False, fontsize=8.5)
    finish(fig, "Two success traits and two warning signs appear in all five brands",
           D.SOURCE_LINE + ". Count = brands the report lists as supporting each pattern",
           os.path.join(OUT, "fig_pattern_counts.png"))


def heatmap():
    pats = D.PATTERNS
    fig, ax = plt.subplots(figsize=(8, 5.6))
    fig.subplots_adjust(left=0.42, right=0.98, top=0.86, bottom=0.13)
    cmap = {"S": "#2a78d6", "X": "#f3c4ad", "U": "#efeeea"}
    label = {"S": "Yes", "X": "No", "U": "?"}
    tcol = {"S": "white", "X": INK, "U": INK2}
    for r, p in enumerate(pats):
        for c, k in enumerate(D.BRAND_KEYS):
            v = p["cells"][k]
            ax.add_patch(plt.Rectangle((c + 0.04, r + 0.06), 0.92, 0.88, color=cmap[v], linewidth=0))
            ax.text(c + 0.5, r + 0.5, label[v], ha="center", va="center", fontsize=8, color=tcol[v],
                    fontweight="bold" if v == "S" else "normal")
    ax.set_xlim(0, 5)
    ax.set_ylim(len(pats), 0)
    ax.set_xticks([i + 0.5 for i in range(5)])
    ax.set_xticklabels([D.BRAND_META[k]["name"] for k in D.BRAND_KEYS], fontsize=8.5, color=INK)
    ax.xaxis.tick_top()
    ax.set_yticks([i + 0.5 for i in range(len(pats))])
    ax.set_yticklabels([f"{p['id']}  {p['name']}" for p in pats], fontsize=8.2, color=INK)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.axhline(9, color=INK, linewidth=1)
    ax.legend(handles=[Patch(color=cmap["S"], label="Yes: brand supports the pattern"),
                       Patch(color=cmap["X"], label="No: named exception"),
                       Patch(color=cmap["U"], label="?: not found or unconfirmed")],
              loc="upper center", bbox_to_anchor=(0.3, -0.02), ncol=3, frameon=False, fontsize=7.8)
    finish(fig, "MaryRuth's matches all 13 patterns; Vida Glow is the most frequent exception",
           D.SOURCE_LINE + ". Rows P1-P9 = shared traits, W1-W4 = warning signs",
           os.path.join(OUT, "fig_heatmap.png"))


def timeline():
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    fig.subplots_adjust(left=0.13, right=0.98, top=0.84, bottom=0.22)
    keys = D.BRAND_KEYS
    for r, k in enumerate(keys):
        evs = D.TIMELINE[k]
        xs = [e[0] for e in evs]
        ax.plot([min(xs), 2026.8], [r, r], color=GRID, linewidth=2.2, zorder=1)
        for x, when, what, typ, tag in evs:
            ax.scatter(x, r, s=48, color=TYPE_COLORS[typ], marker=TYPE_MARKERS[typ],
                       edgecolor="white", linewidth=0.9, zorder=3)
        # annotate first online launch and first physical retail milestone only
        first_online = next(e for e in evs if e[3] == "online")
        first_retail = next(e for e in evs if e[3] == "retail")
        ax.annotate(first_online[1].split(" (")[0], (first_online[0], r), xytext=(0, 8),
                    textcoords="offset points", ha="center", fontsize=6.8, color=INK2)
        ax.annotate(first_retail[1].split(" (")[0], (first_retail[0], r), xytext=(0, -13),
                    textcoords="offset points", ha="center", fontsize=6.8, color="#b84a1f")
    ax.set_yticks(range(len(keys)))
    ax.set_yticklabels([D.BRAND_META[k]["name"] for k in keys], fontsize=9, color=INK)
    ax.set_ylim(len(keys) - 0.4, -0.6)
    ax.set_xlim(2010, 2027)
    ax.set_xticks(range(2010, 2028, 2))
    ax.set_xlabel("Year")
    ax.xaxis.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    handles = [Line2D([], [], marker=TYPE_MARKERS[t], color="white", markerfacecolor=TYPE_COLORS[t],
                      markersize=7, label=l) for t, l in D.EVENT_TYPES.items()]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.13), ncol=5,
              frameon=False, fontsize=7.8, handletextpad=0.3)
    finish(fig, "Major retail came years after the online launch for four of the five brands",
           D.SOURCE_TIMELINE + ".\nLabels: online launch (above the line), first dated retail milestone in the brand report (below).",
           os.path.join(OUT, "fig_timeline.png"),
           subtitle="Vida Glow is the exception: AU health-food wholesale began c. 2014-16, alongside DTC")


if __name__ == "__main__":
    scorecard(); pattern_counts(); heatmap(); timeline()
    print("charts written to", OUT)
