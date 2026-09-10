#!/usr/bin/env python3
"""Curva de saturacion del eje c (Estudio C, "el otro eje: vectores por paso").

Mismos datos que la tabla "Init x granularidad" del poster/paper: accuracy (%)
para c=1,2,3 en las tres combinaciones init x granularidad de pasos. Usa
figstyle.SERIES (paleta de 3 colores de alto contraste) porque las tres curvas
hay que poder distinguirlas de un vistazo, igual que M0/M1/M2 en la frontera.

Uso (desde la raiz del repo):
    python3 paper/paper_sp/figures/scripts/plot_c_sweep_poster.py \
        --out poster/poster_Symposium_sp/paperfigures/c_sweep_accuracy.png
"""
import argparse
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figstyle  # noqa: E402

_PAGELLA_DIR = Path("/usr/share/texmf/fonts/opentype/public/tex-gyre")
_PAGELLA_NAME = None
if _PAGELLA_DIR.exists():
    for _f in _PAGELLA_DIR.glob("texgyrepagella-*.otf"):
        fm.fontManager.addfont(str(_f))
    _PAGELLA_NAME = fm.FontProperties(
        fname=str(_PAGELLA_DIR / "texgyrepagella-regular.otf")).get_name()


def _use_pagella():
    if _PAGELLA_NAME:
        mpl.rcParams.update({
            "font.family": "serif",
            "font.serif": [_PAGELLA_NAME, "DejaVu Serif"],
            "mathtext.fontset": "custom",
            "mathtext.rm": _PAGELLA_NAME,
            "mathtext.it": f"{_PAGELLA_NAME}:italic",
            "mathtext.bf": f"{_PAGELLA_NAME}:bold",
        })


C = [1, 2, 3]
WARM_ATOMICA = [27.5, 39.4, 39.9]
WARM_GRUESA = [25.5, 36.6, 40.3]
COLD_GRUESA = [5.3, 5.5, 5.5]

FS_LABEL = 30
FS_TICK = 26
FS_LEGEND = 22


def _style(ax):
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(figstyle.GRID)
        ax.spines[spine].set_linewidth(1.6)
    ax.tick_params(colors=figstyle.TEXT, labelsize=FS_TICK, width=1.6, length=6)


def plot_c_sweep(out_path: Path) -> None:
    figstyle.set_style("poster")
    _use_pagella()
    fig, ax = plt.subplots(figsize=(7.2, 5.6))

    ax.plot(C, WARM_ATOMICA, color=figstyle.BLUE, marker="o", markersize=11,
            linewidth=3.4, zorder=3, label="warm + atómica")
    ax.plot(C, WARM_GRUESA, color=figstyle.GOLD, marker="^", markersize=11,
            linewidth=3.4, zorder=3, label="warm + gruesa")
    ax.plot(C, COLD_GRUESA, color=figstyle.TEAL, marker="s", markersize=9,
            linewidth=2.6, linestyle="--", zorder=2, label="cold + gruesa")

    ax.set_xlabel(r"$c$ (vectores por paso)", fontsize=FS_LABEL, color=figstyle.TEXT)
    ax.set_ylabel("Accuracy (%)", fontsize=FS_LABEL, color=figstyle.TEXT)
    ax.set_xticks(C)
    ax.set_xlim(0.85, 3.15)
    ax.set_ylim(0, 46)
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.legend(loc="center right", frameon=False, fontsize=FS_LEGEND,
              handlelength=1.6, borderpad=0.2, labelspacing=0.35)
    _style(ax)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"[poster] escrito {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path,
                         default=Path("poster/poster_Symposium_sp/paperfigures/c_sweep_accuracy.png"))
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    plot_c_sweep(args.out)
