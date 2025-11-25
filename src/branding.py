import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path


def load_palette():
    cfg = json.loads(Path("config/brand_palette.json").read_text())
    return cfg["colors"], cfg["matplotlib"]


def use_brand_style():
    colors, mp = load_palette()
    mpl.rcParams.update({
        "font.family": mp["font_family"],
        "axes.titlesize": mp["title_size"],
        "axes.labelsize": mp["label_size"],
        "xtick.labelsize": mp["tick_size"],
        "ytick.labelsize": mp["tick_size"],
        "axes.prop_cycle": mpl.cycler(color=[
            colors["periospot_blue"],
            colors["periospot_red"],
            colors["mystic_blue"],
            colors["crimson_blaze"],
            colors["vanilla_cream"],
            colors["black"]
        ])
    })


def savefig_brand(path, bbox_inches="tight", dpi=160):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path, bbox_inches=bbox_inches, dpi=dpi)


