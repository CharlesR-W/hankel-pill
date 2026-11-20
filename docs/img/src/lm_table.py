"""Compute a real 'prompts x continuations' log-probability table from GPT-2 (small).

Optional, slow-ish step (needs torch + transformers, ~1-3 min on CPU). Its output,
data/lm_table.npz, is checked in so the figures can be rebuilt without torch:

    uv run --with torch --with transformers --with pyarrow --with numpy \
        --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple \
        python docs/img/src/lm_table.py [path/to/pile-10k.parquet]

Rows = prompts (short spans of web text, or the hand-written ones below),
columns = single-token continuations, entry = log P(continuation | prompt).
"""
import sys
from pathlib import Path

import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

HERE = Path(__file__).parent
OUT = HERE / "data" / "lm_table.npz"

SHOW_PROMPTS = [
    "The capital of France is",
    "She poured a cup of",
    "The sky was a deep shade of",
    "He ate a slice of",
    "The cat sat on the",
    "I drank a glass of",
    "Her dress was bright",
    "They visited the city of",
]
SHOW_CONTS = [" Paris", " London", " tea", " coffee", " blue", " red", " bread", " cake"]


def main():
    torch.manual_seed(0)
    tok = GPT2TokenizerFast.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2").eval()

    def last_logprobs(prompts):
        out = []
        for p in prompts:
            ids = tok(p, return_tensors="pt").input_ids
            with torch.no_grad():
                logits = model(ids).logits[0, -1]
            out.append(torch.log_softmax(logits, -1).numpy())
        return np.stack(out)

    # small labelled table
    show_ids = [tok(c).input_ids[0] for c in SHOW_CONTS]
    assert all(len(tok(c).input_ids) == 1 for c in SHOW_CONTS)
    show = last_logprobs(SHOW_PROMPTS)[:, show_ids]

    # big table from real text: 400 prompts (12-token spans) x 400 common next tokens
    big_prompts = []
    if len(sys.argv) > 1:
        import pyarrow.parquet as pq
        texts = pq.read_table(sys.argv[1], columns=["text"]).column("text").to_pylist()
        rng = np.random.default_rng(0)
        while len(big_prompts) < 400:
            t = texts[rng.integers(len(texts))]
            ids = tok(t[:2000]).input_ids
            if len(ids) < 40:
                continue
            s = rng.integers(0, len(ids) - 13)
            big_prompts.append(tok.decode(ids[s:s + 12]))
    full = last_logprobs(big_prompts)
    cols = np.argsort(-np.exp(full).mean(0))[:400]
    big = full[:, cols]
    np.savez_compressed(OUT, show=show, show_prompts=np.array(SHOW_PROMPTS),
                        show_conts=np.array(SHOW_CONTS), big=big.astype(np.float32))
    print("saved", OUT, show.shape, big.shape)


if __name__ == "__main__":
    main()
