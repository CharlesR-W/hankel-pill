"""Rebuild every README figure into docs/img/.

    uv run --with matplotlib --with numpy --with scipy python docs/img/src/build_all.py

neural.png reads data/lm_table.npz (GPT-2 numbers); regenerate that with lm_table.py.
"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

FIGS = ["idea", "bowtie", "automata", "learning", "category", "control", "koopman", "hmm",
        "epsilon", "cca", "clustering", "coherent", "spectra", "neural"]

if __name__ == "__main__":
    for name in sys.argv[1:] or FIGS:
        importlib.import_module(f"fig_{name}").make()
