# Page spec 09: LLMs from outside — the extended logit table

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 9 |
| id (hash, file stem) | `logits` |
| tab label | LLMs from outside |
| kicker | Page 9 · language models |
| title | Sequences of logits: a Hankel table for language models |
| lede (one-sentence claim, ≤ 45 words) | A language model's logits on histories followed by continuations form a Hankel-like table; its rank is exactly the dimension of the smallest time-varying input-switched affine network reproducing the model, and trained models' tables are approximately low rank, with structure that survives nonsense inputs. |
| depends on | 1 (6 helps) |
| edges (SPEC 2.2) | E16, E17 |
| faces of the running example | A (the symbol process read as a "language"), through its idealization A′ (four-state chain, default) and the particle (face A proper) |
| main-path words | 2,200-2,600 |
| spec status | v1.1, 2026-11-17 (reconciled with SPEC v1.1, which adopted this page's deviations; change log) |

## 1. Reader outcome

After this page the reader can:

1. Build the extended logit table $\Lambda[h,(f,s)]$ of a sequence model from its next-token log-probabilities, and say what a row, a column and the centring mean.
2. State Golowich, Liu & Shetty's Theorem 4.3 with its hypotheses (fixed length, exact rank, complete time-indexed tables) and explain why it is page 1's realization theorem carried into log space: a history's state is the coordinate vector of its logit row, and each token acts on it by a matrix read off shifted columns.
3. Say why logit rank and probability-Hankel rank are different numbers, and show on the running example that they differ.
4. Bound what rank-r truncation of a logit table loses, in average KL, from its discarded singular values; and say why that bound does not cover a rank-r *machine* built from the truncated table.
5. Report accurately what Golowich et al. measured on real models (approximate low rank with a power-law spectrum; column-space overlap under nonsense continuations and across models; generation from other prompts' logits, including nonsense prompts) and what they did not (a rank measurement on nonsense histories; cross-model coefficient transfer; an approximate-rank version of Theorem 4.3).
6. Place this outside view next to page 10's inside view and say that no theorem yet connects them.

What they see: a three-symbol "language" whose next-symbol logits fill a table; a spectrum that keeps going past four, although the same process's probability table has rank exactly four; a KL bound sitting above the actual KL of the truncated table at every r; a rank-r machine whose generations drift further than the table bound would suggest; generations for a target history assembled from the logits of scrambled histories.

## 2. Skim path

1. Lede (header).
2. Hero figure `logits-fig-hero`: "A language as a table of next-symbol logits". Fig-sub: *Each row is a history, each column a continuation and a next symbol; the entry is how strongly the model expects that symbol after the history and continuation.*
3. Section headings (verbatim, these are the claims):
   - "A language model's logits form a table of histories by continuations"
   - "Logit rank is exactly the dimension of a linear-in-logits machine"
   - "Truncating the table has a KL bound; truncating the machine does not"
   - "Trained language models have approximately low logit rank"
   - "What low logit rank does not tell you"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `logits-fig-bowtie`, `logits-fig-explorer`, `logits-fig-llms`, `logits-fig-lingen`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: logits on histories × (continuation, next token) make a Hankel-like table; centring keeps it linear in a hidden state; its rank equals the dimension of the smallest time-varying ISAN (fixed length, exact rank); logit rank is not probability-Hankel rank; truncating the table has a KL bound from the discarded singular values, a rank-r machine has none; real models are approximately low rank with a slowly decaying power law; their low-rank structure is shared with nonsense continuations, across models, and is usable from nonsense prompts; transfer of coefficients across models is proposed, not shown; nothing here identifies semantic states, and no theorem ties this to page 10.

## 3. Section outline

Section ids are `logits-<slug>`; figure ids are `logits-fig-<slug>` (SPEC 6.5). Word counts are main-path prose only.

Notation used throughout the page (introduce at first use; see section 10): the logit table is written $\Lambda$, never $L$ (SPEC appendix A reserves $L$ for graph Laplacians and $\mathcal L$ for generators); a history is $h$, a continuation (future) $f$, a next symbol or token $s$; the alphabet is $\mathcal A$ for the running example and $\mathcal V$ for an LLM vocabulary. Golowich et al. write $\mathcal L_M(\mathcal H,\mathcal F)$ with columns $(f,z)$; a side note at first use gives the dictionary.

### 3.1 `logits-table` "A language model's logits form a table of histories by continuations" (≈ 450 words)

Placement: the hero sits between the lede and this heading. "Arriving here first?" aside (≤ 80 words) directly under the heading: page 1's Hankel table lists $P(pf)$ for every past p and future f; its rank is the size of the smallest linear machine and its rows are predictive states. Link `#hankel`.

- A language model, viewed from outside, is a map from a text prefix to a distribution over the next token. Querying it on a history h followed by a continuation f gives a vector of next-token log-probabilities $\log P(\cdot \mid hf)$.
- Define the **extended logit table** (Golowich, Liu & Shetty 2025, Definitions 2.1-2.2):
  $$\Lambda[h,(f,s)] = \log P(s \mid hf) - \frac{1}{|\mathcal V|}\sum_{s'\in\mathcal V}\log P(s'\mid hf).$$
  Rows: histories h. Columns: pairs (continuation f, next token s). Entry: the centred logit of s after hf. Gloss every symbol at this display.
- Compare with page 1 in two sentences: page 1's table has probabilities of whole futures; this one has logits of one next token after each continuation. Summing the token-level conditionals along f recovers $\log P(f \mid h)$ (Golowich et al. §2), so the table carries the same information as the conditional Hankel table; it arranges it in log space. The difference matters for rank (3.3).
- Why centre: subtracting the mean over tokens is a linear operation, so if logits are linear in some hidden state the centred logits are too; subtracting the log-normalizer instead (using $\log P$ directly as a row of a normalized table) is not linear (Golowich et al., Remark 1). Softmax ignores the shift, so nothing is lost.
- Running example: the three-symbol stream of the four-well particle (`a`, `b`, `c`, SPEC 3.2) read as a language. Its exact predictor is known: for the four-state chain (face A′), $P(s \mid w)$ comes from the automaton of page 1 (convention $A_s = \mathrm{diag}(E_{\cdot s})T$, $\alpha = \pi$, $\beta = \mathbf 1$; $P(s \mid w) = P(ws)/P(w)$). The page's block uses 200 histories of length 1-5 and all 13 continuations of length ≤ 2 (the empty one included), so 200 rows and 39 columns; centring leaves at most 26 independent columns (two per continuation). Point at one entry in the hero ("row `cab`, column (`a`, `c`)").
- Strain, one sentence: three symbols and an exact predictor make this a caricature of a language model; it is used because every quantity can be computed exactly, and the real-model results in 3.4 are described, not reproduced.

Key callout: "The table is model-free in the same sense as page 1's: it lists what the model does after each history. Centring keeps it linear in any hidden state that produces logits linearly."

Disclosures:
- "In other fields: five tables called Hankel" (≤ 200 words): process Hankel $P(pf)$, conditional Hankel $P(f \mid p)$, block Hankel of Markov parameters (page 2), delay/trajectory Hankel (page 3), extended logit table (this page). Link the glossary entry "Hankel matrix".
- "Dictionary: this page and Golowich et al." (≤ 120 words): their $\mathcal L_M(\mathcal H,\mathcal F)$ is this page's Λ; their column $(f,z)$ is this page's $(f,s)$; their $L_M[z \mid y_{1:t}]$ is a centred logit; in experiments they keep only the k = 50 most likely next tokens per continuation (similar results at k = 200 and for a random 50; their §3.1).

### 3.2 `logits-isan` "Logit rank is exactly the dimension of a linear-in-logits machine" (≈ 550 words)

Placement: `logits-fig-bowtie` after the second bullet.

- Input-switched affine networks (Foerster, Gilmer, Sohl-Dickstein, Chorowski & Sussillo 2017): a recurrent network whose state update has no nonlinearity but a different affine map for each input token, $q_t = W_{s_t}q_{t-1} + b_{s_t}$, followed by an affine readout to logits and a softmax. Because the recurrence is linear once the tokens are fixed, the contribution of each past token to the current logits can be read off exactly, and a change of basis separates input, output and computational subspaces; the authors reverse-engineer a parenthesis-counting solution this way. The architecture was designed for interpretability; it is not a claim that transformers are ISANs.
- **Time-varying ISAN** (Golowich et al., Definition 4.2): for sequences of fixed length T, matrices $A_{s,t} \in \mathbb R^{d\times d}$ (one per token and position), readouts $B_t \in \mathbb R^{|\mathcal V| \times d}$, initial state $q_0$. At position t the next token is drawn from $\mathrm{softmax}(B_tq_{t-1})$ and the state becomes $q_t = A_{s_t,t}q_{t-1}$ (biases absorbed by a constant coordinate; no end-of-sequence token). d is the hidden dimension.
- **Theorem 4.3** (Golowich, Liu & Shetty 2025): a model of sequences of length T is a time-varying ISAN of hidden dimension d **if and only if** for every $t \le T$ the table $\Lambda(\mathcal V^t, \mathcal V^{\le T-t})$ (all histories of length t; all continuations of length at most $T - t$) has rank at most d. State the hypotheses on the page: fixed length T, exact rank, complete tables over all histories of each length, centred logits.
- Why it holds (one paragraph, main path): "only if": the logits after hf are $B q_{hf}$ with $q_{hf}$ a fixed linear map of $q_h$, so every entry of row h is linear in $q_h \in \mathbb R^d$ and the table factors through d dimensions. "If": choose a basis for each length's row space; express each history's row in it; the coordinate vector is the state; appending a token shifts which columns a row is read from, which is a linear map on coordinates. This is **page 1's realization from shifted blocks**, with logit rows in place of probability rows (edge E16): the state of a history is its row of the table written in a basis of rows, i.e. its predictive state in log space.
- Make the unification explicit in one sentence: on page 1 a history's predictive state is its row of future probabilities; here it is its row of future logits; in both cases the smallest linear state is the rank, and the machine is read off shifted copies of the same table.
- Difference to state: in page 1's table probabilities are linear in the state; here logits are linear in the state and probabilities come out of a softmax. That is why the two ranks differ (3.3).

Key callout: "A time-varying ISAN of dimension d exists exactly when every complete logit table has rank at most d. Its state is the history's row of logits written in d coordinates."

Disclosures:
- "The maths: building the ISAN from shifted columns" (≤ 600 words). Write $\Lambda_t = \Lambda(\mathcal A^t, \mathcal A^{\le T-t})$. Columns of $\Lambda_t$ indexed by $(sf, s')$ with $|f| \le T-t-1$ are exactly the columns of $\Lambda_{t+1}$ on the histories $hs$: $\Lambda_t[h,(sf,s')] = \Lambda_{t+1}[hs,(f,s')]$; write $\Pi_s$ for the column selection, so $\Lambda_{t+1}[hs,:] = \Lambda_t[h,:]\Pi_s$. If $\Lambda_t = U_t\Sigma_tV_t^\top$ has rank $\le d$ for every t (keep d right singular vectors $V_t$), set the row-vector state $q_h = \Lambda_t[h,:]V_t$, the update $A_{s,t+1} = V_t^\top\Pi_sV_{t+1}$, and the readout $B_t = V_t[(\varnothing,\cdot),:]$ (the rows of $V_t$ for the empty continuation). Then $q_{hs} = q_hA_{s,t+1}$ and the logits after h are $q_hB_t^\top$, exactly, because every row of $\Lambda_t$ lies in the span of $V_t$. This is the spectral form of Golowich et al.'s Lemma C.3 (they use a basis of d histories instead of singular vectors; the two differ by a change of basis). The converse (their Fact C.4): an ISAN's table factors as states × per-continuation maps, so its rank is at most d. Note the dimension needed is $\max_t \mathrm{rank}\,\Lambda_t$.
- "In other fields: observable operator models and ISANs" (≤ 250 words): Foerster et al. discuss the relation themselves: observable operator models (Jaeger 2000) represent normalized sequence probabilities linearly; ISANs represent logits linearly, before a nonlinear normalization. Page 1's weighted automata are the former, this page's ISANs the latter.

### 3.3 `logits-truncate` "Truncating the table has a KL bound; truncating the machine does not" (≈ 550 words)

Centrepiece: `logits-fig-explorer`.

- Running example, tour `chain-typical`: the four-state chain's logit block has more than four non-negligible singular values (quote the builder's numerical rank and σ values, `p09.json` `chain.block.typical.sv`), although page 1 showed the same process's probability table has rank exactly 4. Reason in one sentence: each centred logit is the log of a linear function of the belief over the four wells, and logs of linear functions are not linear, so the four-dimensional belief does not make the logit table rank 4. The spectrum still falls quickly, because those functions are smooth on the small region of beliefs the chain visits.
- So **logit rank and probability-Hankel rank measure different things**; here the logit table needs more dimensions than the probability table. Do not claim a general inequality in either direction (SPEC appendix B, "rank"; E16's "logs intervene").
- **The table bound.** Eckart-Young gives the best rank-r table $\Lambda_r$, with $\|\Lambda - \Lambda_r\|_F^2 = \sum_{i>r}\sigma_i^2$. Golowich et al.'s Fact A.2 turns this into a bound on next-token distributions: because log-sum-exp is 1-smooth,
  $$\sum_{h,f}\mathrm{KL}\big(\mathrm{softmax}\,\Lambda[h,(f,\cdot)]\ \big\|\ \mathrm{softmax}\,\Lambda_r[h,(f,\cdot)]\big) \le \tfrac12\|\Lambda - \Lambda_r\|_F^2 = \tfrac12\sum_{i>r}\sigma_i^2,$$
  so the mean KL over the $|\mathcal H||\mathcal F|$ (history, continuation) pairs is at most $\sum_{i>r}\sigma_i^2/(2|\mathcal H||\mathcal F|)$. Explorer panel (c) plots this bound against the actual mean KL of the truncated table at every r. Hypotheses: none beyond finiteness of the block; it is a statement about the block's rows only.
- **What it does not cover.** $\Lambda_r$ is a table, not a model. A rank-r time-varying ISAN can be built from the truncated tables by the shifted-column recipe (3.2 disclosure, with r singular vectors), and it does define a distribution over sequences; but its errors compound along a generated sequence, and no theorem in Golowich et al. 2025 bounds them for approximate rank. Explorer panel (c)'s second series shows the KL between the true distribution over all length-5 sequences and the rank-r ISAN's, per token, with no bound drawn. Parallel to page 1: Eckart-Young for the table, a separate (and here missing) guarantee for the machine.
- The follow-up paper (Golowich, Liu & Shetty 2025b) gives an efficient algorithm that learns any approximately low-logit-rank model from logit queries, the first end-to-end learning guarantee of this kind by the authors' description; on the page it is cited at abstract level with its access model (logit queries) and marked `conditional`. Low-logit-rank models can encode hard-to-learn distributions such as noisy parities, which is why the authors use queries rather than samples.
- Nonsense histories in the toy (tour `chain-nonsense`): take the same 200 histories and randomly permute all their symbols among them (Golowich et al.'s procedure, §3.3), so symbol frequencies are kept and order is destroyed. The page reports the builder's spectrum for this block next to the typical one; it does not predict which decays faster.
- The particle (tour `particle`): the same quantities from the particle's own exact word probabilities (face A); report as computed.

Key callout: "Eckart-Young plus the smoothness of softmax bound the average KL of the best rank-r table by its discarded singular values. A rank-r machine built from that table has no such bound; its error is shown, not certified."

Disclosures:
- "Why the chain's logit table is not rank 4" (≤ 350 words): $P(s \mid hf) = b_{hf}^\top E_{\cdot s}$ with $b_{hf}$ the belief after hf, and $b_{hf}$ a projective (normalized linear) image of $b_h$; centred logs of these are nonlinear functions of $b_h$; the builder's numerical rank is reported with its tolerance. No claim about the exact rank of the infinite table.
- "The maths: Fact A.2 in three lines" (≤ 250 words): KL(softmax(a) ‖ softmax(a′)) is the Bregman divergence of log-sum-exp between a′ and a; log-sum-exp has Hessian $\mathrm{diag}(p) - pp^\top \preceq I$, so the divergence is at most $\frac12\|a - a'\|_2^2$; sum over rows. Also state the cruder per-row $\ell^\infty$ form: $\mathrm{KL} \le 2\|a - a'\|_\infty$ (log-softmax is 2-Lipschitz from $\ell^\infty$ to $\ell^\infty$; SPEC 4.2's draft), and say the quadratic form composes directly with Eckart-Young.

### 3.4 `logits-llms` "Trained language models have approximately low logit rank" (≈ 550 words)

Placement: `logits-fig-llms` after the second bullet; `logits-fig-lingen` after the fourth.

All numbers in this section are from Golowich, Liu & Shetty 2025 (arXiv v1, the only version listed on 17 Nov 2026; the ICLR 2026 version was not separately checked). Each is attributed with its figure or section; section 11 lists them.

- **Setup.** Five trained models: OLMo-1b, OLMo-7b, Llama-1b, Mamba-1.4b, Gemma-1b, with untrained OLMo-1b (training step 0) as a baseline. Histories and continuations are cut from the same documents (main figures: Wikipedia text from the OLMo training mix), with lengths measured in characters (50-200) so that different tokenizers see the same text; about 10,000 histories and 10,000 continuations; the k = 50 most likely next tokens per continuation (§3.1, App. A.1).
- **Approximate low rank, with a power law.** Singular values fall roughly as $\sigma_i \approx C\,i^{-\alpha}$; fitted exponents (Fig. 6; OLMo-7b in Fig. 1(a)): OLMo-1b ≈ 0.561, OLMo-7b ≈ 0.536, Gemma-1b ≈ 0.565, Llama-1b ≈ 0.573, Mamba-1.4b ≈ 0.563; untrained OLMo-1b ≈ 0.374 with no consistent power law. Their Fact A.1 makes α = 1/2 a phase transition: above it, a fixed rank achieves a fixed relative Frobenius accuracy however large the table (relative error $O(r^{1/2-\alpha})$); below it, the rank must grow linearly with the table. Reading, marked as such: the trained exponents sit just above 1/2, so these tables are low rank in that sense, while the error falls only slowly with r. Also: on OLMo-1b checkpoints the KL to the best low-rank approximation drops sharply early in training and then rises slowly (Fig. 3).
- **Nonsense continuations.** Replace the continuations by random sequences made by permuting all tokens among them; the column spaces of the rank-r approximations with real and with nonsense continuations have many principal angles near zero, far more than random subspaces (§3.2, Fig. 4 in the HTML, cited as Fig. 5 in its text: the writer checks the camera-ready numbering).
- **Generation from other histories' logits (LINGEN, §3.3).** To generate after a target history without querying the model on it as a prompt, regress the target's row of the table on the rows of other histories (coefficients v), then sample each next token from $\mathrm{softmax}(\sum_h v_h\,\Lambda(\cdot \mid h z_{1:t-1}))$, i.e. a linear combination of the model's logits on the other histories followed by the tokens generated so far. On OLMo-1b this beats three baselines (coefficients fitted on next-token logits only; a restricted context window; an earlier checkpoint) in per-position KL to the true model, both when the other histories are real text and when they are **nonsense histories** (tokens permuted among histories), in the latter case with larger KL (Figs. 1(b), 5; App. A.3). Computing v still requires querying the model on the target history followed by each continuation.
- **Across models.** For 15 pairs of models, the low-rank column spaces (same histories and continuations) overlap significantly, except pairs involving untrained OLMo-1b (App. A.2, Fig. 11; no numerical angles are given in the text).
- **Not shown** (one short paragraph, plain): computing LINGEN's coefficients with a different, possibly weaker model is proposed as future work (§3.3); no singular-value measurement on a table of nonsense histories is reported; the theory covers exact rank only (App. C). Do not merge these into "predictive states predict logits across models on nonsense inputs" (SPEC appendix D).
- The page's `logits-fig-lingen` runs LINGEN on the running example (tour `typical`, then `nonsense`), with the paper's first two baselines, and shows the KL per generated position.

Key callout: "Five trained models have approximately low logit rank with a power-law spectrum just steeper than the critical exponent 1/2. The low-rank structure is shared with nonsense continuations and across models, and lets nonsense prompts stand in for a real one."

Disclosures:
- "Hypotheses: what 'approximately low rank' means here" (≤ 300 words): the measured objects are finite blocks with k = 50 token columns per continuation; average KL (their Def. 3.1) and the power-law fit are the two metrics; finite blocks cannot certify Theorem 4.3's universal condition; centring "doesn't make a large difference" empirically (their Remark 1) but is needed for the theorem.
- "Cross-model transfer on the toy" (≤ 250 words): the LINGEN widget's advanced option fits coefficients with the particle's table and generates with the chain's logits (or the reverse). Two models of one synthetic process are not two LLMs; the result is reported as computed and is not evidence for the proposal in Golowich et al. §3.3.

### 3.5 `logits-not` "What low logit rank does not tell you" (≈ 300 words)

- It does not identify semantic or human-readable states: Theorem 4.3's state is defined up to an invertible change of basis, as on page 1.
- It is not probability-Hankel rank (3.3), and page 1's guarantees for truncated machines (singular value automata, AAK for one letter) do not transfer automatically to logits; AAK in particular is not claimed for language models (SPEC appendix D).
- A finite block shows a lower bound on a numerical rank at a tolerance, not the universal rank condition; the outside view's budget therefore has a truncation term (Eckart-Young with Fact A.2) and no certified sampling term (ledger).
- Outside view against inside view (edge E17, schematic): the rows of this table are predictive states of the token process seen from outside; page 10 looks for predictive structure inside the network's activations. In idealized settings the two agree (inside scores span the beliefs: CoherentModes `THEOREMS.md` B.2-B.9; transformers represent belief-state geometry linearly in their residual stream, Shai et al. 2024), but a perfectly belief-sufficient layer can have infinite context rank (B.12, Mess3). No theorem relates a model's logit rank to the rank of anything inside it. Wrap the E17 sentence in the section 8 hook.

Key callout: "Logit rank counts linear dimensions of logits. It does not count states a person could name, it is not the probability table's rank, and nothing yet ties it to what the network computes inside."

### 3.6 `logits-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.7 `logits-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.8 `logits-sources` Sources

Section 11 of this spec.

## 4. Claims in order

Support types are the template's, including **empirical (cited)** for a published measurement on real models, described and attributed but not reproduced.

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C9.1 | Logits on history + continuation define the table $\Lambda[h,(f,s)]$ (centred over tokens); summing token conditionals along f recovers $\log P(f \mid h)$. | construction | Golowich et al. Defs 2.1-2.2, §2; hero | — | 3.1 |
| C9.2 | Centring is linear and loses nothing under softmax; using normalized log-probabilities would break linearity in a hidden state. | standard | Golowich et al. Remark 1 | — | 3.1 |
| C9.3 | An ISAN updates its state by a token-dependent affine map and reads logits out affinely; its linear recurrence makes each past token's contribution exactly readable. | standard | Foerster et al. 2017 | — | 3.2 |
| C9.4 | A model of length-T sequences is a time-varying ISAN of hidden dimension d iff $\mathrm{rank}\,\Lambda(\mathcal V^t,\mathcal V^{\le T-t}) \le d$ for every $t \le T$. | theorem | Golowich et al. 2025, Thm 4.3 (Lemma C.3, Fact C.4) | fixed length T, no end token; exact rank; complete tables over all histories of each length; centred logits | 3.2 |
| C9.5 | The ISAN is read off shifted columns: state = the history's row in a basis of the row space; this is page 1's realization in log space. | construction | disclosure "building the ISAN from shifted columns"; E16 | rank $\le d$ at every t | 3.2 |
| C9.6 | The four-state chain's logit block has numerical rank above 4 while its probability Hankel table has rank 4. | widget + builder assertion | explorer tour `chain-typical`; `p09.json` `chain.block.typical.numrank`, assertion `logit_numrank_gt_4` | numerical rank at the stated tolerance; finite block | 3.3 |
| C9.7 | Mean KL of the best rank-r table over its (history, continuation) pairs is at most $\sum_{i>r}\sigma_i^2/(2|\mathcal H||\mathcal F|)$. | theorem | Eckart & Young 1936; Golowich et al. Fact A.2; explorer panel (c) | concerns the block's rows only; σ of the block | 3.3 |
| C9.8 | A rank-r ISAN built from truncated tables has generation error not covered by C9.7; on the example it is shown, not bounded. | widget | explorer panel (c), tours `chain-typical`, `isan` | approximate rank: no theorem in Golowich et al. 2025 | 3.3 |
| C9.9 | Approximately low-logit-rank models can be learned efficiently from logit queries. | theorem (scope-limited), `conditional` | Golowich, Liu & Shetty 2025b, abstract | logit-query access; their structural assumptions (abstract-level check) | 3.3 |
| C9.10 | On the toy, scrambling the histories' symbols changes the logit spectrum by the amount the builder reports. | widget | explorer tour `chain-nonsense` | — | 3.3 |
| C9.11 | Five trained LMs have approximately low logit rank with fitted exponents ≈ 0.54-0.57; untrained OLMo-1b ≈ 0.374 without a clean power law. | empirical (cited) | Golowich et al. Figs 1(a), 6; `logits-fig-llms` | finite blocks (≈ 10⁴ × 10⁴ pairs, top-50 tokens) | 3.4 |
| C9.12 | For spectra $\sigma_i \asymp i^{-\alpha}$, α = 1/2 separates constant-rank from linear-rank approximability. | theorem | Golowich et al. Fact A.1 | power-law spectrum; Frobenius relative error | 3.4 |
| C9.13 | Real and nonsense continuations give strongly overlapping low-rank column spaces. | empirical (cited) | Golowich et al. §3.2, Fig. 4/5 | OLMo-1b; principal angles vs random baseline | 3.4 |
| C9.14 | LINGEN generates for a target history from linear combinations of other histories' logits, beating three baselines, also with nonsense histories (larger KL). | empirical (cited) | Golowich et al. §3.3, Figs 1(b), 5, App. A.3 | OLMo-1b; coefficients need queries on target + continuations | 3.4 |
| C9.15 | Low-rank column spaces overlap across 15 model pairs, except with the untrained model. | empirical (cited) | Golowich et al. App. A.2, Fig. 11 | same histories/continuations for both models; no numbers given | 3.4 |
| C9.16 | Computing LINGEN coefficients with another model is proposed future work, not shown. | standard (statement about the source) | Golowich et al. §3.3 | — | 3.4 |
| C9.17 | On the toy, LINGEN with typical and with scrambled reference histories gives the per-position KL the widget computes. | widget | `logits-fig-lingen` tours `typical`, `nonsense` | exact logits; ridge as specified | 3.4 |
| C9.18 | Low logit rank does not identify named states, is not probability-Hankel rank, and is not certified by a finite block. | standard | 3.2-3.3 above; page 1 | — | 3.5 |
| C9.19 | Outside (logit/predictive-state) and inside (activation) views agree in idealized settings; no theorem connects them in general; belief-sufficient layers can have infinite context rank. | motivation (E17) + theorem for the idealized parts | CoherentModes `THEOREMS.md` B.2-B.9, B.12; Shai et al. 2024 | B.x hypotheses (belief-sufficiency, affine target means, …) named, not proved for networks | 3.5 |

Things not to claim on this page (SPEC appendix D): predictive states predict logits across models on nonsense inputs; AAK gives optimal smaller language models; a rank-r truncation is a smaller model; Hankel rank equals logit rank; a finite block certifies a model's logit rank; low logit rank was measured on nonsense histories.

## 5. Figures and widgets

### 5.1 `logits-fig-hero` "A language as a table of next-symbol logits" (live, hero; key `hr`)

- **Purpose:** the running example's symbol stream, read as a language, gives for each history and continuation a vector of three centred logits; stacking them makes the table.
- **Layout:** `figure.fig.full.card`, three panels (stacked on phones): (a) a strip of the symbol stream (40 symbols, monospace letters) with a bracket marking the current history h (length ≤ 5) and a second bracket for a continuation f (length ≤ 2); (b) the three centred logits $\Lambda[h,(f,\cdot)]$ for `a`, `b`, `c` as a small diverging bar chart (`div` map, fixed symmetric range from the builder's max |Λ| over the block) with the exact next-symbol probabilities printed beside each bar; (c) the block Λ (200 × 39) as a `heatmap` (`div` map, symmetric fixed range), columns grouped by continuation (13 groups of 3), the current row and column group outlined in accent.
- **Data:** live. Chain automaton from `data/example/chain.json` (T, E, π); word probabilities by `lib/hankel.js` `wordProbs`; stream simulated by `lib/rng.js` (seed 0) from the chain; the 200 histories are the builder's typical set (`p09.json` `histories.typical`).
- **Controls:** transport (play/pause, speed ×1/×4), reset. Nothing else.
- **Default state (= first tour):** `default`: playing; at each step the bracket advances by one symbol and f cycles through the 13 continuations; under reduced motion, `frame-still` is shown.
- **What changes:** the bracketed history and continuation; panel (b)'s bars; panel (c)'s outline.
- **Tours:** `default` (t = 0, playing); `frame-still` (history `cab`, continuation `a`, paused).
- **fallbackTour:** `frame-still`.
- **Caption:** *Plotted:* (a) symbols $s_t$ of the four-state chain, history h and continuation f bracketed; (b) $\Lambda[h,(f,s)] = \log P(s \mid hf) - \frac13\sum_{s'}\log P(s' \mid hf)$ for s = `a`, `b`, `c`, with $P(s \mid hf)$; (c) Λ for the page's 200 histories (rows) and 13 continuations × 3 symbols (columns). *Values:* four-state chain at Δ = 0.25 (face A′), seed 0. `synthetic`.
- **Static fallback:** `assets/fallback/logits-fig-hero-frame-still.png`; GIF `assets/fallback/logits-fig-hero.gif` (≈ 6 s at ×4).
- **Accessibility:** alt: "A stream of symbols a, b, c with a bracketed history and continuation, three bars giving the model's centred logits for the next symbol, and a table of such logits for many histories." The fig-sub carries the message without motion.
- **Performance:** ≤ 2 ms per frame; heatmap redraw only of the outline.

### 5.2 `logits-fig-bowtie` "Histories, a few dimensions, continuations" (static SVG)

- **Purpose:** the logit table factors through a small knot; its width is the ISAN dimension.
- **Data:** shared `bowtie` component; left "histories h (prefixes)", left norm "plain", right "(continuation, next token) pairs", right norm "logits, centred over tokens"; knot bars = the chain block's σ₁..σ₈ (`p09.json` `chain.block.typical.sv`), r = 4; bound label "mean KL ≤ Σ_{i>r} σ_i² / (2|H||F|) (table only)". Bars on a square-root scale; caption says so.
- **Controls:** none required; if draggable r is enabled, the bound label updates (no URL state).
- **Caption:** *Plotted:* schematic of $\Lambda = Q\,R$ with rows of Q the histories' states and columns of R the per-(continuation, symbol) readouts; bars are the singular values of the chain's block, square-root scale. *Values:* four-state chain, 200 typical histories, continuations ≤ 2 (face A′).
- **Fallback:** the SVG; PNG `assets/fallback/logits-fig-bowtie-default.png`.

### 5.3 `logits-fig-explorer` "Logit rank, truncation and the machine" (live, centrepiece; key `ex`)

- **Purpose:** the logit table's spectrum keeps going past the probability table's rank; truncating the table has a KL bound that holds; a rank-r machine built from it has error that is shown, not bounded.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view 2 × 2 panels, side panel (320 px) with tours, controls, tiles, legend.
  - (a) **Table:** heatmap of the current block (block view: 200 × 39; time-indexed view: $\Lambda_3$, 27 × 120), `div` map, fixed symmetric range per model.
  - (b) **Spectra:** σ₁..σ₂₆ of the logit table (bars, log y, normalized by σ₁) and, as open circles, the normalized singular values of the same model's probability Hankel table (words ≤ 3, as on page 1; chain: four nonzero, the rest at the 1e-15 floor drawn as a dashed line). r is an accent line; discarded bars hatched.
  - (c) **KL against r** (r = 1..12, log y): "mean KL of the rank-r table" (solid ink, dots), "bound $\sum_{i>r}\sigma_i^2/(2|\mathcal H||\mathcal F|)$" (dashed `seq-5`), "rank-r ISAN, KL per token over all length-5 sequences" (solid `seq-3`, no bound; legend says "no theorem"). In time-indexed view the table series use $\Lambda_3$.
  - (d) **Rank by position:** numerical rank of $\Lambda_t$ (tolerance 1e-9 σ₁) for t = 0..5 at T = 5, with the ceiling $\min(3^t, 2\cdot|\mathcal A^{\le 5-t}|)$ drawn as ticks; the maximum over t (the exact ISAN dimension, Thm 4.3) labelled.
- **Data:** chain: live from the automaton (T, E from `data/example/chain.json`). Particle: exact word probabilities of all words ≤ 8 from the builder (`p09.json` `particle.word_probs`, Float64 base64; computed from the 60-mode spectral WFA of SPEC 3.6), all logits derived live. Histories: `p09.json` `histories.typical` (200 histories, lengths uniform on 1..5, drawn from the stationary chain with seed 0, duplicates allowed and kept) and `histories.nonsense` (the same multiset of symbols permuted across all 200 histories, seed 1, keeping each history's length).
- **Controls (primary):**
  1. model: `chain` | `particle` (labels "four-state chain", "particle");
  2. histories: `typical` | `nonsense (scrambled)`;
  3. r: slider 1-12 (mark at 4 "probability-table rank");
  4. view: `block` (mixed lengths, continuations ≤ 2) | `time-indexed` ($\Lambda_t$, T = 5; panel (a) shows t = 3).
  Advanced: numerical-rank tolerance (1e-6 … 1e-12, default 1e-9); ISAN length T (4 | 5).
- **What changes when each control moves:**
  - model: all panels recompute; the probability circles switch to that model's table (particle: from its word probabilities ≤ 6).
  - histories: (a)-(c) recompute; (d) unchanged (time-indexed tables use all histories).
  - r: (b) line and hatching; (c) cursor; tiles.
  - view: (a) and the table series of (c) switch between the block and $\Lambda_3$; the ISAN series is unchanged (always time-indexed).
- **Stat tiles:** "numerical rank of the table" (count of σ_i > tol·σ₁); "probability-table rank" (same count for page 1's table); "mean KL at r" (actual, nats); "bound at r" (nats); "ISAN KL per token at r".
- **Tours** (default first):
  1. `chain-typical`: chain, typical, r = 4, block. Note: "Four dimensions hold the probability table exactly; the logit table needs more."
  2. `chain-nonsense`: chain, nonsense, r = 4, block. Note: "The same histories with their symbols scrambled."
  3. `isan`: chain, typical, r = 4, time-indexed. Note: "The table bound holds; the machine built at r = 4 drifts further."
  4. `exact-isan`: chain, time-indexed, r = the builder's $\max_t$ numerical rank (`p09.json` `chain.isan_dim`). Note: "At this dimension the ISAN reproduces the model exactly (Theorem 4.3)."
  5. `particle`: particle, typical, r = 4, block. Note: "The particle's logit spectrum, from its own exact predictor."
- **fallbackTour:** `chain-typical`.
- **Caption:** *Plotted:* (a) the centred logit table Λ (rows histories, columns continuation × next symbol), or $\Lambda_3$; (b) singular values of Λ (bars) and of the probability Hankel table of the same model (circles), each divided by its largest; (c) mean over (history, continuation) pairs of KL(true next-symbol law ‖ softmax of the rank-r table), its bound $\sum_{i>r}\sigma_i^2/(2|\mathcal H||\mathcal F|)$, and the per-token KL between the true law of length-5 sequences and that of the rank-r ISAN; (d) numerical rank of $\Lambda_t$ against t. *Values:* model and histories as set; face A′ (chain) or A (particle); Δ = 0.25. `synthetic`.
- **Static fallback:** PNG per tour; GIF stepping r = 1..10 on `isan` (1 s per frame).
- **Accessibility:** panels have `aria-label`s; tiles are text; tour notes announced.
- **Performance:** chain logits for 200 histories × 13 continuations from word probabilities ≤ 8: < 20 ms; SVD of 200 × 39: < 10 ms; ISAN build for r ≤ 12 and exact KL over 243 sequences: < 30 ms. Parity: builder and JS agree on σ (1e-9 relative) and on the ISAN KL at r = 4 and at `chain.isan_dim` (1e-9 absolute).

### 5.4 `logits-fig-llms` "What was measured on five language models" (static, drawn by the page module)

- **Purpose:** the trained models' spectra decay with exponents just above 1/2; the untrained model's does not; and a list of what was and was not shown.
- **Content:** left: horizontal bar chart of the fitted exponents α for OLMo-1b, OLMo-7b, Gemma-1b, Llama-1b, Mamba-1.4b and untrained OLMo-1b, with a vertical reference line at α = 1/2 labelled "Fact A.1: constant rank suffices above this line"; the untrained bar is drawn in `--c-other` and marked "no consistent power law". Right: a two-column checklist, "shown" (approximate low rank with power law, Fig. 6; overlap with nonsense continuations, §3.2; generation from nonsense histories, §3.3; overlap across 15 model pairs, Fig. 11) and "not shown" (rank on a table of nonsense histories; coefficients transferred between models, proposed; approximate-rank theory, App. C exact only).
- **Data:** typed into `site/data/logits/llms.json` from the paper, each value with its figure reference and the access date; this is the only hand-entered data on the page and it is not running-example data.
- **Generation:** drawn by `p_logits.js` with `charts.js` (no interaction). Do not embed or trace the paper's own figures (SPEC 7.1); link them.
- **Caption:** *Plotted:* exponent α of a power-law fit $\sigma_i \approx C\,i^{-\alpha}$ to the singular values of each model's extended logit table, as reported by Golowich, Liu & Shetty (2025, Fig. 6 and Fig. 1(a)); right, which of their findings are reported in the paper. *Values:* ≈ 10⁴ histories and continuations of 50-200 characters from Wikipedia text, top 50 tokens per continuation. Data from the cited paper, not recomputed.
- **Fallback:** PNG `assets/fallback/logits-fig-llms-default.png` (single tour).

### 5.5 `logits-fig-lingen` "Generating from other histories' logits" (live; key `lg`)

- **Purpose:** a target history's continuation can be generated from a linear combination of other histories' logits, including scrambled histories, and the error per generated position is measurable.
- **Layout:** `figure.fig.wide.card`; left: per-position KL (positions 1-3) for LINGEN and two baselines (grouped bars, log y); right: the target history, its three most heavily weighted reference histories with their coefficients, and the principal-angle cosines between rank-r column spaces of the two reference sets (dots against a dashed random-subspace baseline).
- **Data:** live. Reference set $\mathcal H_{\rm ref}$: the 200 typical or 200 nonsense histories (`p09.json`), with the target removed. Continuations $\mathcal F$: the 13 continuations ≤ 2. Coefficients: $v = \arg\min_v \|\Lambda(\mathcal H_{\rm ref},\mathcal F)^\top v - \Lambda(h_{\rm targ},\mathcal F)^\top\|^2 + \rho\|v\|^2$, ρ = 1e-6·σ₁² (stated in the caption). Generation: at position k = 1..3, logits $\sum_h v_h\Lambda(\cdot \mid h\,z_{1:k-1})$ (exact logits of the model on $h z_{1:k-1}$; histories up to 7 symbols plus the next symbol: words ≤ 8, available exactly). KL: exact expectation over the generated prefixes (27 length-3 prefixes), $\mathbb E_{z_{<k}\sim\text{LINGEN}}\mathrm{KL}(P(\cdot \mid h_{\rm targ}z_{<k}) \,\|\, \text{LINGEN}_k)$, no sampling.
  Baselines (after Golowich et al. §3.3): (a) "next-symbol only": v fitted on the empty continuation's columns only; (b) "short context": the model's own prediction given only the last symbol of $h_{\rm targ}$ followed by $z_{<k}$.
- **Controls (primary):** target history (select from the builder's list `p09.json` `lingen.targets`, 8 histories of length 5); references (`typical` | `nonsense`); r for the overlap panel (1-12, default 4). Advanced: coefficients from (`same model` | `other model (toy)`), where "other model" fits v on the particle's table and generates with the chain's logits; model generated (`chain` | `particle`).
- **Default state (= first tour):** `typical`: target = `lingen.targets[0]`, typical references, r = 4, same model, chain.
- **What changes:** target and references refit v and recompute both panels; r recomputes the overlap dots only; "other model" switches the fitting table.
- **Stat tiles:** "LINGEN KL, sum over 3 positions"; "baseline (a)"; "baseline (b)"; "mean cos of principal angles at r".
- **Tours:** `typical`; `nonsense` (nonsense references); `transfer-toy` (other model; note: "Toy only: two models of one synthetic process. Golowich et al. propose this for LLMs and do not test it.").
- **fallbackTour:** `typical`.
- **Caption:** *Plotted:* left, expected KL between the model's next-symbol law after the target history and generated prefix and the LINGEN law, at positions 1-3, for LINGEN and two baselines; right, the largest coefficients $v_h$ and the cosines of principal angles between the rank-r column spaces of Λ on typical and on scrambled reference histories (dashed: random r-dimensional subspaces, mean of 100 draws). *Values:* ridge ρ = 1e-6 σ₁²; 13 continuations ≤ 2; face A′ (chain) unless set. `synthetic`.
- **Static fallback:** PNG per tour.
- **Accessibility:** bars labelled; coefficients listed as text.
- **Performance:** ridge solve 200 × 39: < 5 ms; generation with exact logits: < 20 ms.

## 6. Running example on this page

- Faces: the symbol stream of face A, as an exact predictor: A′ (four-state chain, default) and A (particle, via its exact word probabilities). Parameters exactly as SPEC 3.2 ($\kappa = 0$, Δ = 0.25, bins `a` $y < 0$, `b` $0 \le y \le 1$, `c` $y > 1$, $\sigma_y = 0.25$). Automaton convention as page 1.
- Precomputed (`tools/build_example.py` → `site/data/logits/p09.json`, with config and assertions):
  - `histories.typical`, `histories.nonsense` (seeds 0 and 1, as in 5.3); `lingen.targets` (8 length-5 histories drawn from the chain, seed 2, distinct, not in the reference sets).
  - chain: block spectra (typical, nonsense) σ₁..σ₂₆; numerical ranks at 1e-9; time-indexed ranks for t = 0..5 (T = 5); `isan_dim` = $\max_t$ numerical rank; mean table KL and bound at r = 2, 4, 6 (SPEC 4.2's requested values) and r = 1..12; ISAN per-token KL at r = 1..12; LINGEN KLs for each tour.
  - particle: `word_probs` (all words ≤ 8, Float64 base64, from the 60-mode spectral WFA; its error bound $e^{-\nu_{61}\Delta} < 10^{-8}$ is asserted per SPEC 3.6, and page 1's builder section checks it against the full grid on words ≤ 4); the same derived quantities as the chain.
  - assertions: minimum conditional probability over all histories ≤ 7 and symbols > 1e-12 (both models; logs are finite); chain probability-Hankel rank = 4 (reuse page 1's assertion); `logit_numrank_gt_4`: the chain's typical block has numerical rank > 4 at tolerance 1e-9; table KL ≤ bound at every r (both models, both history sets); at r = `isan_dim` the ISAN KL < 1e-10 (exactness of the realization); centred rows sum to zero (1e-12). **If an assertion fails, stop and amend this spec; do not retune.** In particular, if the chain's logit rank were ≤ 4, section 3.3's first bullet must be rewritten.
- Live: all chain computations; all particle computations from `word_probs`; LINGEN.
- Strain: a three-symbol exact predictor is not a learned model and has no vocabulary-scale structure; 3.1 says so. Nonsense histories are made by Golowich et al.'s permutation procedure, but on three symbols "nonsense" is a weaker change than on text; 3.3 says the page reports, not predicts, the effect.
- Companion: Golowich et al.'s results on real models (3.4, `logits-fig-llms`), described with numbers and linked.

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E16 | 1 Hankel | `=` | The logit table is page 1's Hankel table in log space: rank at most d exactly when a time-varying ISAN of dimension d reproduces the model, built from shifted columns as page 1 builds automata. Logs intervene: ranks differ. |
| E17 | 10 LLMs from inside | `~` | Rows of this table are predictive states seen from outside; page 10 looks for predictive structure among activations. They agree in idealized settings; no theorem connects them for real networks. |

Map card text: "LLMs from outside · the extended logit table · knob: logit rank r = ISAN dimension · bound: mean KL ≤ Σ_{i>r} σ_i² / (2|H||F|) for the table; none for the machine."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The extended logit table $\Lambda[h,(f,s)] = \log P(s \mid hf) - \frac{1}{\lvert\mathcal V\rvert}\sum_{s'}\log P(s' \mid hf)$: histories × (continuation, next token); plain weights on both sides, logits centred over tokens. |
| Knob | Logit rank r, which for complete time-indexed tables equals the ISAN dimension d; also the block (which histories and continuations) and, for LLMs, the number of token columns k. |
| Discarded at r | Directions in which histories' future logits differ only through the small singular values: distinctions that change next-token log-odds little, averaged over the block's continuations. |
| Bound | Exact: rank $\le d$ at every t ⟺ time-varying ISAN of dimension d (Golowich, Liu & Shetty 2025, Thm 4.3; fixed length, exact rank, complete tables; `theorem`). Table: $\|\Lambda - \Lambda_r\|_F^2 = \sum_{i>r}\sigma_i^2$ (Eckart-Young) and $\sum_{h,f}\mathrm{KL}(p_{hf}\,\|\,\mathrm{softmax}\,\Lambda_r[h,(f,\cdot)]) \le \frac12\sum_{i>r}\sigma_i^2$ (Golowich et al. Fact A.2; equivalently per row $\mathrm{KL} \le 2\|\delta_{hf}\|_\infty$; `standard`). Machine: no bound for a rank-r ISAN from approximate rank (`none`); learning from logit queries under approximate low logit rank, Golowich, Liu & Shetty 2025b (`conditional`, abstract-level check). |
| From data | Logits are queried exactly; what is sampled is the block. A finite block bounds a numerical rank from below and cannot certify the universal rank condition (`none`). |
| Running example | From `p09.json`: the chain's and particle's block σ (typical and scrambled histories), numerical ranks, `isan_dim`, mean table KL and its bound at r = 2, 4, 6, ISAN KL at r = 4; probability-Hankel rank 4 for the chain (page 1). |
| Budget line | T (outside view). |

## 9. Things not to claim

Predictive states predict logits across models on nonsense inputs; low logit rank was measured on nonsense histories; LINGEN coefficients transfer between models; logit rank equals probability-Hankel rank (or bounds it, in either direction, in general); a rank-r truncated table is a smaller language model; AAK or singular-value-automaton guarantees hold for logit truncation; a finite block certifies logit rank; ISAN states are semantic or unique; transformers are ISANs; the power-law exponents are universal constants of language; logit rank says anything proved about a model's internal activations.

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, H (page 1's table, in comparisons), p, f, $\mathcal A$, d (ISAN / hidden dimension), Δ, $s_t$, $w_1..w_4$, T S P Z R I.
Page-local:
- Λ: the extended logit table (Golowich et al.'s $\mathcal L_M$); not $L$ (graph Laplacian) or $\mathcal L$ (generator). $\Lambda_t = \Lambda(\mathcal A^t, \mathcal A^{\le T-t})$ the time-indexed table; $\Lambda_r$ its rank-r truncation (context disambiguates the two subscripts; the page writes $\Lambda_{t}$ only in 3.2 and in panel (d), $\Lambda_r$ only in 3.3).
- h history, f continuation, s next symbol or token; $\mathcal V$ an LLM vocabulary; $\mathcal H, \mathcal F$ sets of histories and continuations.
- T: sequence length in Theorem 4.3 (warn once that T is not the transition matrix of face A′, which the page calls "the chain's transition matrix" in words).
- t: position in the sequence (time, as globally).
- $q_t$: ISAN state (not x, which is the particle's position); $A_{s,t}$, $B_t$: ISAN update and readout (page-local; $A_s$ on page 1 are symbol operators, the closest analogue; $B$ on page 2 is an input matrix).
- $\Pi_s$: column selection for appending s (disclosure only); $V_t$: right singular vectors of $\Lambda_t$.
- v: LINGEN coefficients; ρ: ridge.
- α: power-law exponent of the singular values (page-local; page 1's α is an initial weight vector; a side note says so).

## 11. Sources

Cite as in SPEC appendix C; check status there, with additions marked.

- Golowich, N., Liu, A. & Shetty, A. (2025). Sequences of logits reveal the low rank structure of language models. arXiv:2510.24966 (v1, 28 Oct 2025, the only version listed); *ICLR* 2026. [P: v1 HTML checked 17 Nov 2026 for Defs 2.1-2.2, 4.1-4.2, Thm 4.3, Remark 1, Lemma C.3, Fact C.4, Facts A.1-A.2, §§3.1-3.3, Figs 1, 3-6, 11, App. A.1-A.3. Figure numbering in the HTML differs in one place (Fig. 4 vs "Fig. 5" in its text); check against the camera-ready before publication.]
- Golowich, N., Liu, A. & Shetty, A. (2025b). Provably learning from modern language models via low logit rank. arXiv:2512.09892 (v1, 10 Dec 2025). [A]
- Foerster, J. N., Gilmer, J., Sohl-Dickstein, J., Chorowski, J. & Sussillo, D. (2017). Input switched affine networks: an RNN architecture designed for interpretability. *ICML*, PMLR 70, 1136-1145. arXiv:1611.09434. [P per literature digest; abstract re-checked]
- Jaeger, H. (2000). Observable operator models for discrete stochastic time series. *Neural Computation* 12(6), 1371-1398. [V]
- Eckart, C. & Young, G. (1936). *Psychometrika* 1(3), 211-218. [V]
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A. & Riechers, P. M. (2024). Transformers represent belief state geometry in their residual stream. arXiv:2405.15943. [W: authors checked 17 Nov 2026; arXiv gives "Alexander Gietelink Oldenziel", as SPEC appendix C now does]
- CoherentModes theorem register, `THEOREMS.md` B.2-B.9, B.12 (programme's own work; for E17 only).
- Page 1 (`#hankel`) for realization from shifted blocks and probability-Hankel rank.

## 12. Implementation notes

- Files: `site/content/logits.html`, `site/js/p_logits.js`, helpers `site/js/p_logits_hero.js`, `p_logits_explorer.js`, `p_logits_lingen.js`; data `site/data/logits/p09.json`, `site/data/logits/llms.json`, `site/data/logits/widgets.json`.
- Shared modules: `lib/hankel.js` (`words`, `wordProbs`, `hankelFromProbs` for the probability table), `lib/linalg.js` (`svd`, `lstsq`, principal angles via SVD of $U_1^\top U_2$), `lib/rng.js`, `lib/example.js` (chain loader), `lib/bowtie.js`, `charts.js`, `ui.js`.
- Page helpers (owned here; candidates for `lib/` later): `logitTable(probFn, histories, continuations)` → centred Λ; `timeIndexedTables(probFn, T)`; `isanFromTables(tables, r)` → `{A[s][t], B[t], q0}` by the shifted-column recipe of 3.2; `isanSeqProbs(isan, T)`; `lingen(probFn, refs, conts, target, steps, rho)`.
- Widget keys and URL state: hero `hr` (`hr_speed`, `hr_tour`); explorer `ex` (`ex_model`, `ex_hist`, `ex_r`, `ex_view`, `ex_tol`, `ex_T`, `ex_tour`); LINGEN `lg` (`lg_target`, `lg_refs`, `lg_r`, `lg_from`, `lg_model`, `lg_tour`). Figures without widgets: bowtie (key `bw`, tour `default`), llms (key `ll`, tour `default`) for capture.
- Tests: parity of Λ, σ and ISAN KL with the builder (chain and particle; 1e-9); a node test that every tour's tiles match `p09.json`; a test that the bound series lies above the actual series at every r (fails the build otherwise).

## 13. Page-specific definition-of-done additions

- [ ] The words "nonsense histories" appear only with LINGEN (generation) or the toy's scrambled block, never with "low rank was measured".
- [ ] Every number about real models carries its figure or section reference in a tooltip or the Sources section.
- [ ] Theorem 4.3 is stated with all four hypotheses wherever it is stated (main text, ledger, connections card may abbreviate to "exact rank, fixed length").
- [ ] The explorer shows the bound above the actual table KL at every r (builder assertion surfaced; a violation shows an error, never a silent plot).
- [ ] The ISAN series in panel (c) is visually distinct from the bounded series and its legend says "no theorem".
- [ ] `transfer-toy` tour note and caption say "toy only" and "proposed, not tested, by Golowich et al.".

## Change log

- v1 (2026-11-17): first full spec. Deviations from SPEC wording, reported to the SPEC owner:
  1. SPEC 2.1's claim for this page ("real models show approximately low rank even on nonsense histories") and appendix D's right-hand column ("low logit rank holds including on nonsense histories") overstate the paper: Golowich et al. report no rank measurement on nonsense histories; they report overlap of low-rank column spaces under nonsense *continuations* and successful generation (LINGEN) from nonsense *histories*. The lede and 3.4 use the supported version.
  2. Notation: the logit table is Λ[h,(f,s)] rather than SPEC 4.2's L[h,(z,t)], because appendix A reserves L (Laplacian), t (time) and the page needs f for continuations as on page 1.
  3. The ledger's Bound row adds Fact A.2's quadratic KL bound (composes with Eckart-Young) alongside the draft's ℓ∞ form.
  4. Support type "empirical (cited)" used in the claims table; the template has no type for published measurements that the page describes but does not reproduce.
- v1.1 (2026-11-17): reconciled with SPEC v1.1, which adopts deviations 1-4 above: SPEC 2.1's claim and appendix D now
  state what Golowich et al. measured; the ledger draft (4.2) uses Λ[h,(f,s)] and Fact A.2; "empirical (cited)" is in
  the template. SPEC 3.6 lists this page's builder outputs (particle word probabilities ≤ 8, time-indexed tables to
  T = 5). The particle WFA's error assertion is attributed to SPEC 3.6 and page 1's check.
