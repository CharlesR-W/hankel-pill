# Page spec 06: Computational mechanics

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 6 |
| id (hash, file stem) | `compmech` |
| tab label | Comp. mechanics |
| kicker | Page 6 · computational mechanics |
| title | Causal states and closed coarse-grainings |
| lede (one-sentence claim, ≤ 45 words) | Causal states merge pasts that predict the same future; they are exact, and can be infinitely many even when the Hankel rank is four. Coherent sets are their approximate, spectral counterpart, and closure says when a coarse-graining is a state in its own right. |
| depends on | 1 (Hankel tables, predictive states), 4 (conductance, metastable sets) |
| edges (SPEC 2.2) | E11, E12, E13, E21 |
| faces of the running example | A′ (the four-state chain, read out exactly as the well label, or through the instrument as symbols), A (the particle, for the Markov-state-model bound), the asymmetry knob κ |
| main-path words | 2,100-2,300 (five sections, each ≤ 450) |
| spec status | v1.3, 2026-11-17 (round-2 review fix; change log) |

## 1. Reader outcome

After this page the reader can:

1. Define causal states and the ε-machine; state precisely in what sense the ε-machine is minimal (smallest statistical complexity, and coarsest, among prescient history-based statistics) and why that is not "smallest generative model".
2. Relate causal states to the Hankel table of page 1: they are the classes of equal rows of the conditional table, so Hankel rank ≤ number of causal states; give one example with equality, one with strict inequality and finitely many states, and one with rank four and infinitely many causal states.
3. Explain why approximate causal states need a tolerance and a divergence, and keep three operations apart: exact row equivalence (causal states), discrete merging into K groups (quantization, scored by the predictive information it loses, a KL divergence: the information bottleneck), and linear rank reduction (the SVD/CCA of the whitened table of pages 1 and 3, whose discarded tail is a projection error and only a lower bound on any K-group merge's χ² loss); and say where KL and the whitened ℓ² (χ²) agree (to second order, near the reference law).
4. Define the υ-machine and informational, causal and computational closure (Rosas et al. 2024) and lumpability, and decide on the running example when the "which pair" label is a closed macro-state (exactly at κ = 0, not for κ > 0).
5. State the Sarich-Noé-Schütte bound on the error of treating a metastable partition as a Markov chain, read its two ingredients (how far the slow eigenfunctions are from step functions; the spectral ratio at the chosen lag), and see on the particle why a longer lag tightens it.
6. Say which links of this page are theorems and which are motivating analogies ("coherent sets as approximate Markov blankets"; coherent sets of data-point flow as computational states).

What they see: the same particle read out two ways, once with four causal states and once with finite-history predictive states that keep multiplying while the rank stays four (and an argument, on page 1, that the causal states are infinitely many); a curve of predictive information lost against number of merged states for two different ways of merging; a slider that tilts the potential so that the upper wells switch pairs more readily than the lower ones, and makes the "which pair" label stop being a state of its own (the wells of a pair start predicting the pair's future differently); and a Markov-state-model error that a theorem bounds, loosely at a short lag and tightly at a long one.

## 2. Skim path

1. Lede (header).
2. Hero figure `compmech-fig-hero`: "One particle, two readouts". Fig-sub: *Read out exactly, the particle's pasts fall into four causal states; read through the coarse noisy instrument, distinct predictive states of finite histories keep appearing as histories lengthen, while the Hankel rank stays four.*
3. Section headings (verbatim, these are the claims):
   - "Causal states group pasts that predict the same future"
   - "Rank counts predictive dimensions; causal states count classes of pasts"
   - "Approximate causal states depend on a tolerance and a divergence"
   - "A coarse-graining is a state in its own right when closed"
   - "Metastable partitions are approximately closed, with a computable bound"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `compmech-fig-merge`, `compmech-fig-norms`, `compmech-fig-closure`, `compmech-fig-msm`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: causal states are the exact classes of pasts with equal futures, and the ε-machine is the minimal prescient history-based predictor (not the smallest generator); Hankel rank ≤ number of causal states, often strictly, and the running example's instrument has rank 4 with infinitely many causal states (a proof on page 1; the rising count in the figure is of finite histories); approximating causal states means choosing a divergence and an operation: merging pasts into K groups so as to lose the least predictive information (KL) is the information bottleneck, while the SVD/CCA of the whitened table reduces rank, and its discarded tail bounds a merge's χ² loss only from below; KL and χ² agree to second order; a macro-variable is a state of its own when it is closed (its own past predicts its future as well as the micro past does), which for a Markov chain is lumpability; the pair label is exactly closed at κ = 0 and not for κ > 0; a metastable partition is approximately Markov with a bound that improves with the lag.

## 3. Section outline

Section ids are `compmech-<slug>`; figure ids are `compmech-fig-<slug>`. An "Arriving here first?" aside (≤ 80 words) opens section 3.2: "Page 1 arranges a process as a table: rows are pasts, columns futures, entries the probability of the past followed by the future. Dividing each row by its past's probability gives the conditional table, whose row for past p is the law of the future given p, the past's predictive state. The table's rank is the size of the smallest linear machine that reproduces it." Link page 1. A second aside opens section 3.5 (≤ 80 words) glossing conductance and metastable sets with a link to page 4.

### 3.1 `compmech-causal` "Causal states group pasts that predict the same future" (≈ 450 words)

Placement: the hero `compmech-fig-hero` sits between the lede and this heading.

- Motivation for an interpretability reader in two sentences: a model that predicts well must keep some summary of its past; the question "what is the least it must keep?" has an exact answer for any stationary process, and that answer is a natural candidate for "the computational state".
- Definition (displayed equation 1): two (semi-infinite) pasts are causally equivalent when they give the same conditional law of the entire future,
  $$\overleftarrow{x} \sim_\epsilon \overleftarrow{x}{}' \iff P(\overrightarrow{X} \mid \overleftarrow{x}) = P(\overrightarrow{X} \mid \overleftarrow{x}{}').$$
  The classes are the **causal states**; their number is $n_c$ (SPEC appendix A). Reading a new symbol moves a causal state to a determined next causal state (unifilarity), with a symbol probability that depends only on the state: this machine is the **ε-machine** (Crutchfield & Young 1989; Shalizi & Crutchfield 2001). "Causal" here means predictive equivalence, not intervention (glossary).
- What is proved (Shalizi & Crutchfield 2001): the causal state is prescient (it predicts as well as the whole past; Theorem 1); every other prescient statistic of the past determines it, so it is the coarsest such statistic (Lemma 7 and Corollary 1, the minimal-sufficient-statistic argument); it has the smallest statistical complexity $C_\mu$ (entropy of the causal-state distribution) among prescient rivals (Theorem 2) and is unique with that property (Theorem 3).
- What is not claimed (SPEC appendix D): the ε-machine is not the smallest model of every kind. Nonunifilar generators can be far smaller: the running example's instrument process is generated by four hidden wells, yet (section 3.2) it has infinitely many causal states.
- Running example (hero tour `wells`): read the particle's well exactly every Δ = 0.25 (the four-state chain, face A′, observed directly). Because the chain is Markov and its four rows differ, the last well is the causal state: four causal states, and $C_\mu$ equals the entropy of the stationary well distribution (builder value; 2 bits at κ = 0 by symmetry).

Key callout: "A causal state is everything about the past that matters for the future, and nothing else. It is the coarsest prescient summary of history; it is not the smallest possible generator."

Disclosures:
- "Two small ε-machines" (≤ 350 words): the Golden Mean process (no two 1s in a row; two causal states, "last symbol 0" and "last symbol 1"; stationary (2/3, 1/3); $C_\mu = H(2/3, 1/3) \approx 0.918$ bits) and the Even process (1s come in runs of even length; two causal states, but not a Markov chain of any finite order, because a past of all 1s does not reveal its parity until a 0 is seen). Both have Hankel rank 2 (their two-state machines realize them; neither is i.i.d.). Drawn as two small state diagrams in the disclosure (static SVG, no figure id; part of the prose).
- "In other fields: state, causal, minimal" (≤ 300 words): glossary entries for "state" (hidden, predictive, belief, causal, LTI, candidate), "causal" (predictive equivalence vs intervention) and "minimal" (Hankel rank vs ε-machine vs nonnegative HMM).

### 3.2 `compmech-rank` "Rank counts predictive dimensions; causal states count classes of pasts" (≈ 450 words)

Aside at the top ("Arriving here first?", page 1).

- Causal states are the classes of **equal rows** of the conditional Hankel table: a row is a past's predictive state (page 1), and two pasts share a causal state exactly when their rows coincide (Haslinger, Klinkner & Shalizi 2010, App. C; edge E11). Since the ε-machine is a realization of the process (a hidden Markov model with $n_c$ states), page 1's factorization gives
  $$\mathrm{rank}\,H \le n_c$$
  (displayed equation 2; when $n_c$ is finite).
- Three cases, each shown in the hero by a tour:
  - **Equality** (tour `wells`): the exact well readout has four causal states and rank 4 (the four rows of $T_\Delta$ are linearly independent: builder assertion).
  - **Strict, finitely many** (tour `b8`): a three-symbol Markov chain observed directly, whose third row is the average of the first two (CoherentModes register B.8): three causal states, rank 2. Rank counts linearly independent future laws; distinct laws can be linearly dependent (register B.7: the centred rank is the dimension of the span of centred future laws, ≤ $n_c - 1$, with equality iff the laws are affinely independent).
  - **Finite rank, infinitely many** (tour `instrument`, the default): the particle read through the instrument (three symbols, `a` shared by the left pair's wells). Rank 4, and infinitely many causal states. Two different things must be kept apart. The hero's counter shows distinct **finite-history** predictive distributions (beliefs after finite words, starting from the stationary prior) climbing with L while the rank tile stays at 4; such counts can climb even for a process with finitely many causal states (a two-state unifilar process does), so the counter illustrates, it does not prove. The proof is page 1's (section 3.3 there): causal states condition on semi-infinite pasts; the instrument's symbol matrices are strictly positive and invertible, so each symbol's belief update is a strict contraction of the projective (Hilbert) metric and is injective, and a finite set of causal beliefs closed under the updates would have to be permuted by the `a` update and hence collapse to its single fixed point, which reading `b` moves. Quote, do not re-derive; its hypotheses are builder-checked.
  - Mention Mess3 (tour `mess3`): rank 3, and its predictive states form a fractal (Shai et al. 2024); the counter climbs likewise.
- The spectral side, exactly (register B.7): under stated completeness conditions and finite rank, the past canonical coordinates of a past-future CCA separate exactly the causal states. So spectral coordinates do not lose causal-state distinctions when the rank is finite; they place infinitely many causal states in finitely many dimensions.

Key callout: "Hankel rank is at most the number of causal states, and can be far smaller: here, four dimensions hold infinitely many causal states (page 1 proves it; the rising count shows finite histories). Rank counts linear predictive dimensions; causal states count classes."

Disclosure "Hypotheses: when spectral coordinates separate causal states" (≤ 350 words): B.7's four conditions in plain words (the past summary is predictively sufficient; the feature space contains all past-predictable directions; the target features are prediction-complete; finite rank), what fails without each, and that "separate" is not "count": B.8 shows three states in a rank-two embedding.

### 3.3 `compmech-approx` "Approximate causal states depend on a tolerance and a divergence" (≈ 450 words)

Placement: `compmech-fig-merge` (live) after the fourth bullet; `compmech-fig-norms` (static) after the sixth.

- Infinitely many causal states cannot be used as they are, and finite data could never certify exact equality of rows anyway. Approximate causal states merge pasts whose futures are **close**. Two choices are then unavoidable: how close (a tolerance, or a target number of states K) and close in what sense (a divergence between future laws). The predictive states lie in a bounded region, so at any positive tolerance finitely many merged states suffice; their number is a resolution knob.
- Keep three operations apart (one sentence each): **exact row equivalence** gives the causal states; **discrete quantization** merges pasts into K groups (a partition); **linear rank reduction** keeps an r-dimensional subspace of the whitened table (an SVD). An SVD chooses a subspace, a merge chooses groups: different feasible sets, so the SVD's discarded tail is not the loss of a merge.
- Information choice. Merge pasts into K groups T so as to lose the least predictive information. For a deterministic merge, the loss is exactly an average KL divergence (displayed equation 3):
  $$I(P;F) - I(T;F) = \sum_p P(p)\,\mathrm{KL}\big(P(F\mid p)\,\big\|\,P(F\mid t(p))\big).$$
  This is the information bottleneck's relevance term (Tishby, Pereira & Bialek 1999); its past-future form trades $I(T;P)$ against $I(T;F)$ with a multiplier $\beta_{\rm IB}$ (page-local), recovers the causal states as the compression penalty vanishes (Still, Crutchfield & Ellison 2010, optimal causal inference), and for Gaussian processes its optimal compressions are noisy linear projections onto CCA directions, with β-dependent scales and noise (Creutzig, Globerson & Tishby 2009; Chechik et al. 2005): it shares CCA's directions, not its solution, and is neither hard K-way merging nor plain SVD truncation (edge E13, schematic beyond these exact cases).
- Spectral choice. Weight each future by its overall probability and measure rows in the whitened ℓ² (chi-square) metric, $\sum_f(P(f\mid p) - P(f\mid p'))^2/P(f)$. Its natural coordinates are the singular vectors of the whitened table $D_p^{-1/2}JD_f^{-1/2}$ (J the joint table of past and future windows, $D_p, D_f$ its marginals): the CCA of past and future of pages 1 and 3. What ties the choices together, exactly: KL ≈ ½ χ² to second order, for future laws close to the reference; the total χ² dependence is the sum of the squared nontrivial canonical correlations; the best rank-r **projection** loses exactly $\sum_{i>r}\sigma_i^2$ of it (Eckart-Young); and any merge into K groups loses **at least** $\sum_{i>K}\sigma_i^2$ (σ₁ = 1 the trivial one), with equality only when the top-K block is spanned by group indicators. So the spectral tail is a lower bound for merging, and a merge's own loss is computed from the merge. (Derivation in the disclosure.)
- `compmech-fig-merge` on the instrument (histories of length L = 5, futures of length 3): predictive information lost against K for agglomerative information-bottleneck merging (Slonim & Tishby 2000) and for weighted k-means in the whitened coordinates. Quote the builder's values for K = 2, 4, 8 and the total $I(P;F)$, each computed from the actual merge. At K = 4 the well readout loses nothing (its four causal states); the instrument loses a small, nonzero amount. The χ² view of the figure adds the spectral tail $\sum_{i>K}\sigma_i^2$ as a lower reference line under both merges' χ² losses.
- `compmech-fig-norms` puts the three readings of one table side by side: equality of rows (causal states), KL between rows with K groups (information bottleneck), whitened ℓ² with a rank-r subspace (SVD/CCA); with the bowtie.
- One sentence, inside the section 8 hook (C6.15): "More generally, approximate predictive coarse-graining can be read as page 4's recipe with the divergence between future laws as the energy; for quadratic divergences this is the spectral relaxation of page 4, and for KL it is the information bottleneck, but the recipe's Cheeger-type bounds are proved only for the quadratic case."

Key callout: "To approximate causal states you must say how different two futures may be and still be merged. Merging into groups by KL is the information bottleneck; the SVD of pages 1 and 3 reduces rank instead, and its discarded tail is a lower bound on the χ² loss of any merge into as many groups, not on the predictive information (KL) it loses."

Disclosures:
- "The maths: lost information, χ², and canonical correlations" (≤ 500 words): the chain-rule derivation of equation 3; the expansion $\mathrm{KL}(p\|q) = \tfrac12\sum_f(p_f - q_f)^2/q_f + O(\|p - q\|^3)$; the identity $\sum_{p,f}(J_{pf} - P(p)P(f))^2/(P(p)P(f)) = \sum_{i\ge2}\sigma_i^2$ for the whitened table (correspondence analysis; Greenacre 1984); that k-means in whitened coordinates minimizes the χ² analogue of equation 3 with the marginal as reference, so the two objectives differ where future laws are far from the marginal; and why a K-group merge retains at most $\sum_{2\le i\le K}\sigma_i^2$ of the χ² dependence (the merged table has rank ≤ K, and Ky Fan's principle bounds what a rank-K block can carry), hence loses at least the tail, with equality iff the top-K left block is spanned by the groups' indicators.
- "In other fields: information bottleneck" (≤ 250 words): Tishby, Pereira & Bialek's general IB; its deep-learning usage; the past-future specialization; what is special in the Gaussian case (Chechik et al. 2005: the optimal projection's rows are scaled left eigenvectors of $\Sigma_{x|y}\Sigma_x^{-1}$, i.e. CCA directions, with scales that switch on at β-dependent thresholds and added noise; the basis is shared with CCA, the compression is not).

### 3.4 `compmech-closure` "A coarse-graining is a state in its own right when closed" (≈ 450 words)

Centrepiece: `compmech-fig-closure` after the fourth bullet.

- The interpretability question in a sentence: if we group micro-states into macro-states (wells into pairs, data points into coherent sets), when does the macro-variable behave like a state, so that its own history is all one needs to predict its future?
- Rosas et al. 2024 make this precise for a micro process X and a macro process Z = f(X) (definitions in their numbering; displayed equation 4 is informational closure):
  - the **υ-machine** (Def. 2): group micro pasts by the law they give to the **macro** future; it is the best predictor of Z from X's history;
  - **causal closure** (Def. 3): the υ-machine and Z's own ε-machine induce the same classes, so knowing the micro past adds nothing to predicting the macro future;
  - **informational closure** (Def. 4):
    $$I\big(\overleftarrow{X}_t;\ \overrightarrow{Z}^{L}_{t+1} \,\big|\, \overleftarrow{Z}_t\big) = 0\quad\text{for all } L;$$
  - **computational closure** (Def. 5): coarse-graining the micro ε-machine's states yields Z's ε-machine, a smaller automaton running on its own.
  Their Theorem 1: informational and causal closure are equivalent. Theorem 2: for spatial coarse-grainings Z_t = f(X_t), causal closure implies computational closure. Theorem 3 links closure to lumpability **of the micro ε-machine's causal states** (not of arbitrary micro states), with hypotheses that differ by direction: for a stationary process, computational closure implies weak lumpability of the ε-machine and conversely; the strong-lumpability directions (informational closure of a spatial coarse-graining implies strong lumpability, and strongly lumpable coarse-grainings of the causal states give closed macro-processes) additionally assume the micro ε-machine **irreducible and aperiodic** (their Appendix A.7). State both hypothesis sets on the page. The running chain meets them: it is stationary, irreducible and aperiodic (all entries of $T_\Delta$ positive), and observed directly with distinct rows its causal states are its states.
- Lumpability (Kemeny & Snell 1960), in the form needed: a Markov chain is strongly lumpable for a partition when the probability of jumping into each block is the same from every state of a given block; then the block label is itself a Markov chain from every start.
- Running example (`compmech-fig-closure`): micro X = the four-state chain observed exactly; macro Z = which pair. At κ = 0 the chain is exactly the product $T^x_\Delta\otimes T^y_\Delta$ (builder assertion), so the probability of switching pairs does not depend on the well: strongly lumpable, Z is a two-state Markov chain, the υ-machine has two classes, equal to Z's ε-machine: closed in every sense (tour `closed`). With κ > 0 the between-pair barrier is lower on the upper side than on the lower side (SPEC 3.2), so the upper wells $w_2, w_4$ switch pairs more readily than the lower wells $w_1, w_3$: the two wells of a pair predict the pair's future differently (four υ-classes), the lumpability defect is positive and grows with κ (expected ≈ 0.0014, 0.0042, 0.0075 at κ = 0.1, 0.3, 0.5; quote the builder), and Z's own predictive states multiply with history length (tour `tilted`; builder counts; the page does not claim they are infinite). A finite-window version of the closure defect, $I(X_t; Z_{t+1..t+3}\mid Z_{t-2..t})$ in bits, is shown as a diagnostic (exactly zero at κ = 0). One sentence: the tilt keeps the left-right mirror symmetry, so the up/down label stays exactly lumpable at every κ; closure is a property of a particular label, not of the chain.
- Companion (tour `modular`): Rosas et al.'s modular random walk (§IV.4): a walker on modules of nodes, strongly linked inside a module and weakly between, with move probabilities that make the chance of entering each module depend only on the current module. The module label is lumpable, hence closed (their analysis); the page's parameters are its own (section 6).

Key callout: "A macro-variable is a state of its own when its past predicts its future as well as the micro past does. For a Markov chain this is lumpability; here the pair label is exactly closed only when switching pairs does not depend on the well (κ = 0)."

Disclosures:
- "The maths: lumpability and closure for a Markov chain" (≤ 400 words): the Kemeny-Snell condition as a matrix identity ($T\,U = U\,\hat T$ with U the block-indicator matrix); why it makes Z Markov from every initial law; that for a micro chain observed directly the micro causal states are the micro states (when rows differ), so Rosas et al.'s Theorem 3 converse applies to X itself, given its hypotheses (stationary for the weak directions; irreducible and aperiodic as well for the strong ones); weak versus strong lumpability.
- "In other fields: closed, closure" (≤ 200 words): invariant subspace (Koopman, realization: page 1's "closed set of macrostates" is the linear version), closed macro-variable (here), closed form; glossary link.

### 3.5 `compmech-msm` "Metastable partitions are approximately closed, with a computable bound" (≈ 450 words)

Aside at the top ("Arriving here first?", ≤ 80 words): "A partition is metastable when a random walker rarely leaves the set it is in: each set's conductance (probability of leaving in one step) is small. For a reversible process, such sets are read off the slowest eigenfunctions of the transition operator, and Cheeger's inequality ties their leakage to the eigenvalues. Page 4 builds this." Link page 4.

Placement: `compmech-fig-msm` (static) after the third bullet.

- Exact lumpability is fragile (one κ away). What survives is approximate: a Markov state model (MSM) keeps only which set the process is in, with transition matrix $P_\mu[X_\tau\in A_j \mid X_0\in A_i]$, and the question is how well its powers reproduce the true dynamics on those sets.
- Sarich, Noé & Schütte 2010, Theorem 3.1 (displayed equations 5-6). For a reversible process with transfer operator $T = T_\tau$, m dominant nontrivial eigenvalues with orthonormal eigenfunctions $u_j$, the rest of the spectrum inside a disc of radius $r_{\rm SNS}$ smaller than the m-th (page-local symbol), and a partition into sets $A_1..A_n$ with step-function projector Q, the error $E(k) = \|QT^kQ - (QTQ)^k\|$ obeys
  $$E(k) \le \min\big[2,\ C(\delta, \eta, k)\big]\,\lambda_2^k,\qquad C = (m\delta + \eta)\Big[\sqrt m\,(k-1)\,\delta + \frac{\eta\,(1-\eta^{k-1})}{1-\eta}\Big],$$
  with $\delta = \max_j\|(I - Q)u_j\|$ (how far the slow eigenfunctions are from step functions on the sets) and $\eta = r_{\rm SNS}/\lambda_2 = e^{-\tau\Delta_{\rm SNS}}$ (how much faster the rest decays; page-local). State the index shift (the paper writes $\lambda_1$ for this site's $\lambda_2$). Read it: good sets make δ small; a longer lag makes η small; both are needed (the paper's §3.3 notes that the spectral term grows without bound as τ → 0 for long horizons).
- `compmech-fig-msm` on the particle (face A, generator eigenpairs from `grid.json`): the pair partition (n = 2, m = 1) and the four-basin partition (n = 4, m = 3), lags τ = 0.25, 1, 4: actual E(k) and the bound against k. Quote builder values; expect (not promise) that the pair partition's bound is vacuous at τ = 0.25 (η ≈ 0.93) and informative at τ = 4, and the four-basin partition's is informative already at τ = 0.25 (η ≈ λ₅/λ₂ ≈ 0.13).
- With fuzzy memberships that are exact combinations of the dominant eigenfunctions (PCCA+, Deuflhard & Weber 2005), δ = 0 and the MSM is exact (SNS Theorem 3.3 and §4.1), at the price that the model is no longer a chain on sets; and only if the eigenfunctions are known exactly.
- This is edge E12: a partition with small conductance and a large gap (page 4) is approximately lumpable, with an error controlled by step-function approximation and the spectral ratio.
- Two motivating links, each wrapped in the section 8 hook:
  - (C6.29) "Informational closure is a conditional independence: the macro-variable's own past screens its future off from the micro past, the defining property of a Markov blanket in Pearl's sense. Coherent sets, being approximately closed, can be read as approximate Markov blankets, with the KL closure defect as one measure of the approximation and the MSM error E(k) as a spectral one; no theorem here relates the two magnitudes." (The first sentence's conditional-independence reading of Definition 4 is a restatement; the blanket analogy and the comparison are the schematic part. The widget of 3.4 shows the two defects moving together on the chain, as a demonstration only.)
  - (C6.30, edge E21) "Coherent sets of a network's data-point flow (page 10) are candidate coarse-grained computational states; calling them states would require approximate closure, which has not been tested for networks."

Key callout: "A partition whose sets nearly carry the slow eigenfunctions is nearly Markov: the error is bounded by how far those eigenfunctions are from step functions and by how fast everything else decays at the chosen lag."

Disclosure "Hypotheses: the Sarich-Noé-Schütte theorem" (≤ 400 words): assumptions (7), (8), (12), (13) of the paper in words: m real dominant eigenvalues with orthonormal eigenfunctions, rest of the spectrum in a disc of radius $r_{\rm SNS} < \lambda_m$ (their indexing), the dominant and remaining subspaces do not mix (true for reversible processes; their Remark 2.1); a full partition; the norm is the $L^2_\mu$ operator norm restricted to step functions. The trivial bound $E(k) \le 2\lambda_2^k$ holds for any partition; the theorem's content is the prefactor. Theorem 3.3 generalizes Q to any subspace containing the constants.

### 3.6 `compmech-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.7 `compmech-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.8 `compmech-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C6.1 | Causal states are the classes of pasts with equal conditional future laws; the ε-machine is their unifilar transition structure. | standard | Crutchfield & Young 1989; Shalizi & Crutchfield 2001 | stationary process | 3.1 |
| C6.2 | The causal state is prescient, is determined by every prescient statistic (coarsest), has minimal statistical complexity among prescient rivals, and is unique with that property. | theorem | Shalizi & Crutchfield 2001, Thms 1-3, Lemma 7, Cor. 1 | history-based prescient rivals | 3.1 |
| C6.3 | The ε-machine is not the smallest generator: the instrument process has a four-state generator and infinitely many causal states. | theorem (proof on page 1) + builder checks | page 1 C1.7; SPEC appendix D | page 1's checked hypotheses (strictly positive, invertible symbol matrix for `a`; reading `b` moves the `a`-run limit; rank 4) | 3.1 |
| C6.4 | The exact well readout has four causal states and $C_\mu$ = entropy of the stationary well distribution. | construction + builder values | hero tour `wells`; `p06.json` | four distinct rows of $T_\Delta$ | 3.1 |
| C6.5 | Golden Mean and Even processes have two causal states; the Even process is not Markov of any finite order; both have rank 2. | standard + construction | Shalizi & Crutchfield 2001; disclosure | — | 3.1 |
| C6.6 | Causal states are the classes of equal rows of the conditional Hankel table, and rank H ≤ $n_c$. | theorem | E11; Haslinger, Klinkner & Shalizi 2010, App. C; register B.7 | $n_c$ finite for the inequality | 3.2 |
| C6.7 | The exact well readout has rank 4 = $n_c$. | widget + builder values | hero tour `wells` | rows of $T_\Delta$ linearly independent (builder) | 3.2 |
| C6.8 | A three-state Markov chain with one row the average of the others has three causal states and rank 2; centred rank = dimension of the span of centred future laws ≤ $n_c - 1$, equality iff affinely independent. | theorem | register B.7, B.8; hero tour `b8` | — | 3.2 |
| C6.9 | The instrument process has rank 4 and infinitely many causal states; the hero's rising count is of distinct finite-history predictive distributions, which illustrates but does not prove this. | theorem (proof on page 1) + builder values | page 1, section 3.3 and C1.7; hero tour `instrument` | page 1's checked hypotheses ($A_{\texttt a}$ strictly positive and invertible; $f_{\texttt b}(\eta^*_{\texttt a}) \ne \eta^*_{\texttt a}$; rank 4); finite-history counts can rise for finite ε-machines too | 3.2 |
| C6.10 | Mess3 has rank 3 and a fractal set of predictive states. | standard (cited) + builder values | Shai et al. 2024 (Mess3's origin to verify, Sources); hero tour `mess3` | — | 3.2 |
| C6.11 | Under completeness and finite rank, past canonical coordinates separate exactly the causal states. | theorem | register B.7 | B.7's four conditions | 3.2 |
| C6.12 | At any positive tolerance finitely many merged states suffice (predictive states lie in a bounded finite-dimensional set when the rank is finite). | construction | compactness; merge widget | finite rank | 3.3 |
| C6.13 | For a deterministic merge t, $I(P;F) - I(T;F) = \sum_pP(p)\mathrm{KL}(P(F\mid p)\|P(F\mid t(p)))$. | standard (identity) | chain rule; Tishby, Pereira & Bialek 1999; disclosure | finite past and future windows | 3.3 |
| C6.14 | The past-future IB recovers causal states as the compression penalty vanishes and, for Gaussian processes, its optimal compressions are noisy projections onto CCA directions (same directions as CCA; β-dependent scales and noise; not hard merging, not SVD truncation). | theorem (scope-limited) | Still, Crutchfield & Ellison 2010; Creutzig, Globerson & Tishby 2009; Chechik et al. 2005; E13 (`~` beyond these cases) | Gaussian case for the directions; their model assumptions | 3.3 |
| C6.15 | Approximate predictive coarse-graining can be read as page 4's recipe with a divergence between future laws as the energy; Cheeger-type bounds are proved only for the quadratic case. | motivation (section 8 hook) | — | — | 3.3 |
| C6.16 | KL ≈ ½χ² to second order; total χ² dependence of the window table = $\sum_{i\ge2}\sigma_i^2$ of the whitened table; the best rank-r projection loses exactly $\sum_{i>r}\sigma_i^2$; any merge into K groups loses at least $\sum_{i>K}\sigma_i^2$ of χ², with equality only if the top-K block is spanned by group indicators. | standard + construction | Taylor expansion; correspondence analysis (Greenacre 1984); Eckart-Young; Ky Fan; disclosure | whitened by the marginals; merges' own losses computed from the merge | 3.3 |
| C6.17 | On the instrument, agglomerative IB and whitened k-means lose the stated predictive information at K = 2, 4, 8; the well readout loses none at K = 4. | widget + builder values | `compmech-fig-merge`; `p06.json` `merge` | L = 5, future length 3 | 3.3 |
| C6.18 | Rosas et al.'s definitions (υ-machine; causal, informational, computational closure) and Theorems 1-3. | theorem | Rosas et al. 2024, Defs 2-5, 7; Thms 1-3 (Theorem 3 checked in the arXiv v2 text during this revision) | Theorem 2 for spatial coarse-grainings; Theorem 3: lumpability of the micro ε-machine's causal states; items 1-2 (weak lumpability ⇔ computational closure) for a stationary process; items 3-4 (strong lumpability, informational closure) also need the ε-machine irreducible and aperiodic | 3.4 |
| C6.19 | Strong lumpability: block label Markov from every start iff jump probabilities into each block are constant within blocks. | standard | Kemeny & Snell 1960 | finite chain | 3.4 |
| C6.20 | At κ = 0 the pair label of the chain is strongly lumpable, its υ-machine has two classes equal to its ε-machine, and it is informationally, causally and computationally closed. | construction + theorem + builder assertion | $T = T^x\otimes T^y$ (builder, 1e-10); Rosas Thms 1-3; closure widget tour `closed` | chain observed directly | 3.4 |
| C6.21 | For κ > 0 the lumpability defect is positive (≈ 0.004 at κ = 0.3), the υ-machine has four classes, the pair label's predictive states multiply with history length, and the finite-window closure defect is positive; the up/down label stays exactly lumpable. | widget + builder values | closure widget tour `tilted`; `p06.json` `kappa`; SPEC 3.2 | SPEC 3.2's knob (upper wells switch pairs more readily); builder values; "multiply" is a count up to length 10, not a proof of infinitely many | 3.4 |
| C6.22 | The modular random walk's module label is lumpable and closed. | theorem (cited) + widget | Rosas et al. 2024 §IV.4; tour `modular` | the page's own parameters | 3.4 |
| C6.23 | Sarich-Noé-Schütte Theorem 3.1 bound on $E(k)$. | theorem | Sarich, Noé & Schütte 2010, Thm 3.1, eqs (27)-(32) | assumptions (7), (8), (12), (13); full partition; index shift | 3.5 |
| C6.24 | On the particle, the bound against the actual error for pairs and wells at τ = 0.25, 1, 4 (vacuous or informative as computed). | widget + builder values | `compmech-fig-msm`; `p06.json` `msm` | builder values | 3.5 |
| C6.25 | Fuzzy memberships spanned by the dominant eigenfunctions give an exact MSM (δ = 0), not a chain on sets. | theorem | Sarich, Noé & Schütte 2010, Thm 3.3, §4.1; Deuflhard & Weber 2005 | exact eigenfunctions | 3.5 |
| C6.26 | A metastable partition is approximately lumpable with the above control (E12). | theorem (via C6.23) | E12 | as C6.23 | 3.5 |
| C6.27 | Informational closure is the conditional independence $\overleftarrow X_t \perp \overrightarrow Z_{t+1} \mid \overleftarrow Z_t$. | construction (restatement of Def. 4) | Rosas et al. 2024 Def. 4 | — | 3.5 |
| C6.28 | On the chain, the KL closure defect and the MSM error move together as κ varies. | widget (demonstration only) | closure widget, tiles across κ | not a theorem | 3.4-3.5 |
| C6.29 | Coherent sets are approximate Markov blankets; KL closure defect and MSM error are two measures of the same approximation. | motivation (section 8 hook) | — | — | 3.5 |
| C6.30 | Coherent sets of data-point flow are candidate coarse-grained computational states; closure is untested for networks. | motivation (section 8 hook) | E21 | — | 3.5 |

Things not to claim on this page (SPEC appendix D and page-specific): Hankel rank = number of causal states; ε-machines are minimal among all generative models; coherent sets are the network's computational states; the υ-machine is the mixed-state presentation (the programme's 2026 epsilon-machine blog post uses "upsilon machine" for mixed states; on this site υ-machine means Rosas et al.'s Definition 2 only); the information bottleneck is in general a CCA/eigenproblem (only in the Gaussian case); Markov blankets are established for coherent sets; the pair label of the particle (face A) is exactly closed (only the four-state chain's is, at κ = 0); the tilted pair label has infinitely many causal states (not shown); the hero's rising count proves infinitely many causal states (it counts finite histories); the spectral tail $\sum_{i>r}\sigma_i^2$ is the loss of a K-state merge (it is a projection error and a lower bound); Gaussian IB is CCA (it shares CCA's directions); Rosas et al.'s strong-lumpability directions hold without irreducibility and aperiodicity; the SNS bound applies to non-reversible dynamics without its assumption (13).

## 5. Figures and widgets

Running-example processes on this page: **well readout** (the four-state chain $T_\Delta$ observed directly; symbols $w_1..w_4$ shown as well labels, not letters); **instrument** (the chain through the emissions E: symbols `a`, `b`, `c`, monospace, as page 1); companions **b8** (register B.8's chain $\mathsf T_c$ observed directly), **Mess3** (matrices from `crw-blog/assets/widgets/hankel-hmm-src/build.py:27-70`, as page 1), **modular** (section 6). Automaton convention as page 1: $A_s = \mathrm{diag}(E_{\cdot s})\,T$, α = π, β = 1.

### 5.1 `compmech-fig-hero` "One particle, two readouts" (live, hero; key `hr`)

- **Purpose:** exact readout, four causal states; coarse readout, finite-history predictive states that keep appearing (an illustration; page 1 proves the causal states infinite); the rank does not see the difference.
- **Layout:** `figure.fig.full.card`; (a) left (≈ 55 %): predictive-state map: each history of length 1..L placed at its conditional future law (words of length ≤ 3), projected on the top two weighted principal directions (page 1's coordinates), coloured by belief over wells (`mixBary`, as page 1); new points of the current L drawn with a ring; for `instrument` the `b a^n` and `c a^n` chains joined by thin lines; for finite cases (`wells`, `b8`) an inset draws the ε-machine as a small state diagram (nodes at the four well positions for `wells`). (b) right: line chart "distinct predictive states of finite histories of length ≤ L (from the stationary start)" against L = 0..8 (log y), with a flat dashed line "Hankel rank" at the table's numerical rank; tiles below.
- **Data:** live, `lib/hankel.js` (forward filter, conditional rows) on the chain/companion automata; distinct = after merging predictive states closer than 1e-9 in ℓ∞ (the empty history's stationary law counted, labelled "start (transient)").
- **Controls:** transport (play/pause; L advances 0 → 8 at 1 s per step), process: `instrument` | `wells` | `b8` | `mess3`.
- **Default state (= first tour):** `instrument`, L = 0, autoplays when scrolled into view (centrepiece rule); reduced motion shows L = 8.
- **What changes:** L adds points and extends the count curve; process swaps everything.
- **Stat tiles:** "Hankel rank" (numerical rank of the depth-3 conditional table, tol 1e-10 σ₁); "distinct finite-history predictive states (≤ L)"; "causal states" (text: "4" for wells, "3" for b8, "infinitely many (proved on page 1)" for instrument, "infinitely many (fractal; Shai et al.)" for Mess3). A one-line legend under (b): "Finite-history counts can rise even when there are finitely many causal states; the count illustrates, page 1 proves."
- **Tours:** `instrument` (default; L = 0, playing); `instrument-late` (instrument, paused at L = 8; the fallback frame); `wells` (note: "Read exactly: four causal states, rank four."); `b8` (note: "Three causal states, rank two: distinct futures need not be independent."); `mess3` (note: "Rank three; the predictive states form a fractal.").
- **fallbackTour:** `instrument-late` (a named paused tour, since capture loads tours only; SPEC 6.5).
- **Caption:** *Plotted:* (a) each history of length 1..L at its predictive state $P(f\mid p)$ (f over words of length ≤ 3), projected on two weighted principal directions, coloured by the belief over wells; (b) number of distinct predictive states (conditional future laws) of finite histories of length ≤ L, starting from the stationary law, and the rank of the conditional Hankel table (words ≤ 3). *Values:* four-state chain at Δ = 0.25, κ = 0, read as the well label or through the instrument (bins `a` $y<0$, `b` $0\le y\le1$, `c` $y>1$, σ_y = 0.25); companions as labelled. Running example, face A′. `synthetic`.
- **Static fallback:** `assets/fallback/compmech-fig-hero-instrument-late.png` (L = 8), PNG per other tour; GIF `assets/fallback/compmech-fig-hero.gif` (L = 0..8, instrument, 1 s per step).
- **Accessibility:** alt text: "Points spreading over a curved region as histories lengthen, with a count that keeps rising while a dashed rank line stays at four." The fig-sub carries the message without motion.
- **Performance:** histories ≤ 8 (9,840) filtered incrementally < 40 ms per L step; distinct counting by hashing rounded rows.

### 5.2 `compmech-fig-merge` "Merging pasts: states against lost prediction" (live; key `mg`)

- **Purpose:** the number of approximate states is a resolution knob whose price is predictive information; two ways of merging pasts into K groups (information bottleneck by KL; k-means in whitened coordinates) are compared by the information each actually loses, and, in a χ² view, against the spectral tail, which is a projection error and a lower bound on any merge's χ² loss (not on its KL information loss), not the loss of either.
- **Layout:** `figure.fig.wide.card`; (a) line chart: predictive information lost (bits) against K = 1..32 (log x), two series: "information bottleneck (agglomerative)" and "spectral (k-means in whitened coordinates)", with a dashed horizontal line at $I(P;F)$ (all predictive information in the windows) and a vertical accent line at the selected K; (b) the histories (fixed length L) on page 1's predictive-state map coloured by merged state at the selected K (categorical palette; at K = 2 and 4, matched to pair/well colours by the builder's belief-based matching).
- **Data:** live. Past = the last L symbols (all $3^L$ words with their stationary probabilities), future = the next 3 symbols; P(F | p) from the automaton. IB: agglomerative merging that at each step merges the pair with the smallest information loss $(p_i + p_j)\,\mathrm{JS}_{\pi}(P(F\mid i), P(F\mid j))$ (Slonim & Tishby 2000). Spectral: SVD of $D_p^{-1/2}JD_f^{-1/2}$; coordinates of past p = the top-d left singular vectors (excluding the trivial one) scaled by $\sigma_i/\sqrt{P(p)}$; weighted k-means (weights P(p), k-means++, 10 restarts, seed 0). Loss for both computed exactly by equation 3.
- **Controls (primary):** process: `instrument` | `wells` | `mess3`; K: slider 1-32 (default 4); L: 3 | 4 | 5 (default 5); spectral dimension d: 3 | all (default 3). Advanced: loss measure: `information` (bits, default) | `χ²` (both merges' χ² losses, with the tail $\sum_{i>K}\sigma_i^2$ of the whitened table as a dashed line labelled "rank-K projection loses exactly this; any K-group merge loses at least this").
- **What changes:** process/L recompute both curves; K moves the cursor and recolours (b); d recomputes the spectral curve.
- **Stat tiles:** "$I(P;F)$" (bits); "lost at K: IB / spectral" (bits and % of $I(P;F)$); "distinct predictive states among the $3^L$ pasts".
- **Tours:** `instrument4` (default: instrument, K = 4, L = 5; note "Four merged states keep almost all the predictive information; not all of it."); `wells4` (wells, K = 4; note "Exact readout: four states lose nothing, they are the causal states."); `instrument2` (K = 2; note "Two states: the pairs."); `mess3` (mess3, K = 3).
- **fallbackTour:** `instrument4`.
- **Caption:** *Plotted:* (a) predictive information lost by merging pasts into K states, $I(P;F) - I(T;F)$, for agglomerative information-bottleneck merging and for k-means in whitened (canonical) coordinates; dashed: total $I(P;F)$; (b) pasts on the predictive-state map coloured by merged state at the selected K. *Values:* pasts = last L symbols, futures = next 3 symbols, exact probabilities; process as set; Δ = 0.25, κ = 0. Running example, face A′. `synthetic`.
- **Static fallback:** PNG per tour.
- **Accessibility:** alt text: "Two falling curves of information lost against number of states, close together, with a map of points coloured into four groups."
- **Performance:** L = 5: 243 pasts × 27 futures; agglomerative merging O(n²·27) < 60 ms; k-means sweep K = 1..32 < 150 ms.

### 5.3 `compmech-fig-norms` "One table, three ways to merge its rows" (static SVG, with the shared bowtie)

- **Purpose:** causal states, the information bottleneck and the SVD are three readings of the same conditional table, differing in the divergence between rows and in the operation (exact classes, K groups, an r-dimensional subspace).
- **Content:** centre: a small schematic conditional table (pasts × futures). Three arrows out, each naming its operation: "rows equal → causal states, ε-machine (exact classes)"; "KL between rows, K groups → information bottleneck (a merge; loses $I(P;F) - I(T;F)$, computed from the merge)"; "whitened ℓ², r-dimensional subspace → SVD / CCA, pages 1 and 3 (a projection; loses exactly $\sum_{i>r}\sigma_i^2$ of χ², a lower bound on the χ² loss of any merge into r groups, not on its KL loss)"; a bracket between the last two labelled "KL ≈ ½χ² near the reference; Gaussian case: the IB uses CCA's directions, not its solution (E13)". Below, the shared `bowtie`: left "histories", right "future observations", left norm "KL (information)", right norm "whitened ℓ² (spectral)", knot bars = the instrument's canonical correlations of past and future windows of length 3 (page 1's builder values, `p01.json` `chain.whitened`), r = 4, bound label "lost: I(P;F) − I(T;F) or Σ_{i>r} σ_i²".
- **Generation:** SVG built by `p_compmech.js` with `bowtie.js` from data.
- **Caption:** *Plotted:* schematic; bars are the canonical correlations of past and future windows of length 3 for the instrument process. *Values:* four-state chain through the instrument, Δ = 0.25. Running example, face A′.
- **Fallback:** `assets/fallback/compmech-fig-norms-default.png` (key `nm`, tour `default`).
- **Accessibility:** alt text: "A table in the middle with three arrows: equal rows to causal states, KL to the information bottleneck, whitened distance to the SVD; below, a bowtie from histories to future observations."

### 5.4 `compmech-fig-closure` "Is the pair label a state of its own?" (live, centrepiece; key `cl`)

- **Purpose:** at κ = 0 the pair label is exactly closed; tilting the potential so that the upper wells switch pairs more readily (SPEC 3.2) makes the micro past matter for the macro future.
- **Layout:** `ui.simLayout`; main view three panels: (a) **chain**: the four wells at their positions, arrows with width ∝ off-diagonal $T_\Delta[j,k]$ (log-scaled; labels on hover), pairs shaded by hue; (b) **macro futures from each well**: for each well, the law of the pair labels over the next three steps, $P(Z_{t+1..t+3} = z \mid X_t = w)$ (8 outcomes), as grouped bars, wells of the same pair adjacent; (c) **Z's own predictive states**: number of distinct $P(Z_{\rm future}\mid Z_{\rm past}=z)$ among pair-label histories of length ≤ L, L = 1..10 (tol 1e-9), with the line "υ-machine classes" for comparison. Side panel: controls, tiles.
- **Data:** chain $T_\Delta(\kappa)$ for κ ∈ {0, 0.05, …, 0.5} precomputed (`p06.json`, `kappa.T`, numerically computed basins for κ ≠ 0, SPEC 3.2); everything else live (exact sums over the four states). Modular companion built live (section 6).
- **Controls (primary):** system: `chain` | `modular`; κ: slider 0-0.5, step 0.05 (chain only); tolerance for "distinct" (1e-9 | 1e-6 | 1e-3), default 1e-9.
- **What changes:** κ swaps $T_\Delta$ and recomputes all panels and tiles; tolerance changes the counts in (c) and the υ-class tile.
- **Stat tiles:** "lumpability defect" $\max_{B,C}\max_{j,j'\in C}|T[j,B] - T[j',B]|$; "υ-machine classes" (distinct rows in (b) at the tolerance); "finite-window closure defect" $I(X_t; Z_{t+1..t+3}\mid Z_{t-2..t})$ in bits (exact, under stationarity); "Z's predictive states up to length 10".
- **Tours:** `closed` (default: chain, κ = 0; note "Symmetric potential: switching pairs does not depend on the well. The pair label is a two-state chain, closed."); `tilted` (κ = 0.3; note "Tilted: the upper wells switch pairs more readily than the lower ones, so the two wells of a pair predict the pair's future differently. Not closed."); `slight` (κ = 0.05; note "A small tilt: small defects, all nonzero."); `modular` (system modular; note "Rosas et al.'s modular walk: the module label is exactly lumpable.").
- **fallbackTour:** `tilted`.
- **Caption:** *Plotted:* (a) transition probabilities between wells over one sampling interval; (b) for each well, the probability of each sequence of pair labels over the next three steps; (c) number of distinct predictive states of the pair label among its own histories of length ≤ L. Tiles: lumpability defect, number of υ-machine classes, finite-window closure defect (bits). *Values:* four-state chain at Δ = 0.25, κ as set, D = 0.5; or the modular walk (sizes 3, 4, 5; q = 0.5; within-module weight 1, between 0.02). Running example, face A′ (or companion). `synthetic`.
- **Static fallback:** PNG per tour; GIF sweeping κ = 0 → 0.5 (0.5 s per step).
- **Accessibility:** alt text: "Four wells joined by arrows; bar groups showing each well's forecast of the pair label, equal within a pair at zero tilt and unequal when tilted."
- **Performance:** all quantities are sums over ≤ 4 states and ≤ 2¹³ label sequences; < 20 ms per κ step.

### 5.5 `compmech-fig-msm` "How far a metastable partition is from Markov" (static, rendered by the page module; key `ms`)

- **Purpose:** the SNS bound against the actual MSM error, for two partitions and three lags.
- **Data:** precomputed by the builder from the grid generator (`grid.json`: first 100 eigenpairs, π) and the basin partition (quadrants at κ = 0) into `p06.json` (`msm`): for partitions `pairs` (n = 2, m = 1) and `wells` (n = 4, m = 3) and τ ∈ {0.25, 1, 4}: δ, η (with $r_{\rm SNS} = \lambda_{m+2}(1 + 10^{-9})$, site indexing), the actual $E(k) = \|QT^kQ - (QTQ)^k\|_{L^2_\pi}$ for k = 1..20 computed on the n-dimensional step-function space in the orthonormal basis $\mathbf 1_{A_i}/\sqrt{\pi(A_i)}$ using the 100-mode expansion of $T^k$ (assert the neglected modes change E(k) by < 1e-8), the bound $\min[2, C]\lambda_2^k$, and the trivial bound $2\lambda_2^k$.
- **Content:** 2 × 3 small multiples (rows: pairs, wells; columns: τ = 0.25, 1, 4), log y, x = k (and a secondary axis label with time kτ); series: actual E(k) (ink dots), SNS bound (`seq-5` line), trivial bound (dashed grey); each panel's δ and η printed in its corner.
- **Caption:** *Plotted:* for a Markov state model on the two pairs (top) or the four basins (bottom), the error $E(k) = \|QT^kQ - (QTQ)^k\|$ against the number of steps k, with the Sarich-Noé-Schütte bound $\min[2, C(\delta,\eta,k)]\lambda_2^k$ and the trivial bound $2\lambda_2^k$; δ = largest distance of a dominant eigenfunction from the step functions, η = ratio of the first non-dominant to the top nontrivial eigenvalue. *Values:* particle at κ = 0, D = 0.5, lags τ = 0.25, 1, 4; generator eigenpairs from the grid discretization (spacing 0.05). Running example, face A. `synthetic`.
- **Fallback:** `assets/fallback/compmech-fig-msm-default.png`.
- **Accessibility:** alt text: "Six small log-scale panels; in each, dots for the actual error lie below a bound line; at the shortest lag for two sets the bound is flat at its trivial value."

## 6. Running example on this page

- Faces: A′ (default), A (section 3.5), κ ∈ [0, 0.5] (closure widget). Parameters as SPEC 3.2: $h_x = 2.5$, $h_y = 1.5$, b = 0.6, D = 0.5, $\sigma_y = 0.25$, Δ = 0.25, bins as page 1.
- Precomputed (`tools/build_example.py` → `site/data/compmech/p06.json`, with config and assertions):
  - `wells`: stationary π over wells, $C_\mu$ (bits), rank of the depth-3 conditional table.
  - `hero`: for each process (instrument, wells, b8, mess3), distinct predictive-state counts for L = 0..8 (tol 1e-9) and the table rank; the a-run check is page 1's (`p01.json`), referenced, not recomputed.
  - `merge`: for instrument, wells, mess3 and L ∈ {3, 4, 5}: $I(P;F)$, IB and spectral loss curves K = 1..32 (seed 0), so live values can be checked.
  - `kappa`: $T_\Delta(\kappa)$ for κ = 0, 0.05, …, 0.5 with SPEC 3.2's knob (basins computed numerically for κ ≠ 0 on a cell-centred grid with no node on a basin boundary, SPEC 3.2), and per κ: lumpability defect of the pair label and of the up/down label, υ-classes (tol 1e-9), Z's predictive-state counts for L ≤ 10, finite-window closure defect.
  - `msm`: as in 5.5.
  - **Assertions** (if one fails, stop and amend this spec; do not retune silently): $T_\Delta(0) = T^x\otimes T^y$ to 1e-10; lumpability defect at κ = 0 < 1e-10 and finite-window closure defect < 1e-10 bits; pair-label defect at κ = 0.3 > 1e-3 (expected ≈ 0.004; the old knob gave 0 here up to tie-breaking artefacts of ~1e-5, which is why the threshold is 1e-3, not 1e-6); up/down-label defect < 1e-10 at every κ (the mirror symmetry the knob keeps); well-readout rank 4 and four distinct rows; b8 rank 2 and three causal states; SNS bound ≥ actual E(k) for every panel and k; IB loss at K = 4 for `wells` < 1e-12 bits.
- Live: everything else (filters, conditional rows, merging, closure quantities, modular walk).
- **Modular companion parameters (this page's, after Rosas et al. §IV.4):** 12 nodes in modules of sizes 3, 4, 5; from node x in module c: stay with probability 1 − q, q = 0.5; otherwise move to another node y with probability proportional to $r_w = 1$ if y is in c and $r_b = 0.02$ otherwise. The probability of entering module c′ ≠ c is then $q\,r_b|c'|/\phi(c)$ with $\phi(c) = (|c|-1)r_w + (12 - |c|)r_b$, a function of c only: strongly lumpable. Label "companion (after Rosas et al. 2024), parameters ours".
- Strain stated on the page: the IB / Markov-blanket links are not exercised numerically beyond the finite-window closure demonstration (SPEC 3.7); the four-state chain is an idealization of the particle, and the particle's pair label (sign of $x_1$) is not exactly closed even at κ = 0 (position within the pair matters), which is why section 3.5 uses the approximate SNS bound for the particle.
- Companions: Golden Mean and Even (disclosure diagrams), b8 and Mess3 (hero tours), modular walk (closure tour).

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E11 | 1 Hankel | `=` | Causal states are the classes of equal rows of page 1's conditional table, so the ε-machine is a realization and rank ≤ number of causal states; the instrument has rank 4 and infinitely many. |
| E12 | 4 Spectral clustering | `≈` | A metastable partition from page 4 is approximately lumpable: its Markov state model's error is bounded by step-function approximation of the slow eigenfunctions and the spectral ratio; exact only when lumpable. |
| E13 | 3 Koopman | `~` | The past-future information bottleneck can be read as one choice of energy in page 4's recipe. Exact cases: it recovers the causal states without compression; for Gaussian processes it uses CCA's directions, not CCA's solution. |
| E21 | 10 LLMs from inside | `~` | Coherent sets of data-point flow are candidate coarse-grained computational states; calling them states would need approximate closure, which has not been tested for networks. |

Map card text: "Comp. mechanics · pasts merged by equal futures; macro-variables that are states of their own · knob: tolerance, horizon, β_IB · bound: rank ≤ n_c; MSM error ≤ min[2, C(δ, η, k)]λ₂^k."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The conditional Hankel table (pasts × future laws) under predictive equivalence; for a coarse-graining Z = f(X), micro pasts × macro futures (υ-machine); for a partition, the transfer operator projected on step functions (MSM). |
| Knob | Number of retained predictive classes K (merging tolerance) and the divergence used; horizon; information-bottleneck trade-off $\beta_{\rm IB}$; lag τ for the MSM. |
| Discarded at r | Predictive distinctions below the tolerance (e.g. which well within the left pair, for the instrument at K = 2); for υ, micro detail irrelevant to the macro future; for an MSM, where in each set the process is. |
| Bound | Exact: rank H ≤ $n_c$; the ε-machine is the coarsest prescient history-based statistic with minimal statistical complexity (Shalizi & Crutchfield 2001; `theorem`). Merging: lost predictive information = expected KL (identity; `standard`), computed from the merge; the whitened table's tail $\sum_{i>r}\sigma_i^2$ is the exact χ² error of rank-r projection and only a lower bound on the χ² loss of a merge into r groups, not on its KL information loss (`standard`). Closure: informational ⇔ causal closure; causal ⇒ computational for spatial coarse-grainings; lumpability of the micro ε-machine's causal states ⇔ closure in the stated directions, weak directions for stationary processes, strong directions also needing an irreducible, aperiodic ε-machine (Rosas et al. 2024, Thms 1-3; `theorem`). Approximate closure of a partition: $E(k) \le \min[2, C(\delta,\eta,k)]\,\lambda_2^k$ (Sarich, Noé & Schütte 2010, Thm 3.1; reversible, dominant/rest non-mixing, full partition; `theorem`). "Coherent sets as approximate Markov blankets": `none` (schematic, section 8). |
| From data | CSSR-type reconstruction consistency (Shalizi & Klinkner 2004) — `conditional`; finite blocks never certify equality of rows. |
| Running example | From the builder (`p06.json`): four causal states and rank 4 for the well readout; rank 4 and infinitely many causal states for the instrument (page 1's proof, hypotheses checked), with finite-history predictive-state counts rising with L; IB and spectral losses at K = 2, 4, 8; lumpability defect of the pair label at κ = 0 (zero) and κ = 0.3; υ-classes 2 vs 4; SNS δ, η, bound and actual E(k) for pairs and wells at τ = 0.25, 1, 4. |
| Budget line | I (closure is what would license calling a coarse-graining a state), T. |

## 9. Things not to claim

Hankel rank = number of causal states (rank ≤ $n_c$, often strictly; the instrument has rank 4 and infinitely many); ε-machines are minimal among all generative models (minimal among prescient history-based predictors); coherent sets are the network's computational states (candidates; closure untested); the υ-machine is the mixed-state presentation; the information bottleneck is CCA in general (Gaussian case only); coherent sets are Markov blankets (motivating analogy); the particle's pair label is exactly closed; the tilted pair label provably has infinitely many causal states; finite-window closure defects equal the infinite-past definition; the SNS bound is informative at every lag.

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, $\lambda_i$ (with the index shift for SNS), H, p, f, $\mathcal A$, $n_c$, τ, Δ, $s_t$, $w_1..w_4$, L/R, κ, $\beta_{\rm IB}$ (page-local per SPEC appendix A), π, D.
Page-local: $\overleftarrow x$, $\overrightarrow X$ (past and future), $\sim_\epsilon$, $C_\mu$ (statistical complexity), X and Z (micro and macro processes; X here is not the particle position x — a side note says so), f (coarse-graining map; distinct from a future f — the page writes the map as $f_{\rm cg}$ if both appear in one paragraph), T (merged-state variable in the IB; distinct from $T_\Delta$ — a side note), P, F (past and future windows as random variables), K (number of merged states), J, $D_p$, $D_f$ (window table and marginals), Q (step-function projector), E(k) (MSM error), δ (SNS projection error; **not** the spectral gap $\delta_r$ — the page writes δ with the gloss "projection error" every time and never as $\delta_r$), η (SNS spectral ratio; **not** page 5's residual η — a side note), m (number of dominant nontrivial eigenvalues), n (number of sets), $r_{\rm SNS}$, $\Delta_{\rm SNS}$, U (block-indicator matrix in the lumpability disclosure).

## 11. Sources

Cite as in SPEC appendix C; status there unless noted.

- Crutchfield & Young 1989 [M].
- Shalizi & Crutchfield 2001, Theorems 1-3, Lemma 7, Corollary 1 [P].
- Shalizi & Klinkner 2004 (CSSR) [M].
- Haslinger, Klinkner & Shalizi 2010, Appendix C [P].
- Tishby, N., Pereira, F. C. & Bialek, W. (1999). The information bottleneck method. *Proc. 37th Allerton Conference*, 368-377; arXiv:physics/0004057. [V]
- Slonim, N. & Tishby, N. (2000). Agglomerative information bottleneck. *NIPS 12*, 617-623. [V]
- Still, Crutchfield & Ellison 2010 [A].
- Creutzig, Globerson & Tishby 2009 [A].
- Chechik, G., Globerson, A., Tishby, N. & Weiss, Y. (2005). Information bottleneck for Gaussian variables. *JMLR* 6, 165-188. [V; optional addition for the Gaussian case]
- Greenacre, M. J. (1984). *Theory and Applications of Correspondence Analysis*. Academic Press. [M; for the χ²/inertia identity]
- Rosas et al. 2024 (arXiv:2402.09090): Definitions 1-5, 7; Theorems 1-3; §IV.4. [W; checked again during this spec: Def. 2 (υ-machine), Def. 3 (causal closure: ε- and υ-machine coarse-grainings equivalent), Def. 4 ($I(\overleftarrow X_t; \overrightarrow Z^L_{t+1}\mid\overleftarrow Z_t) = 0$), Def. 5 (computational closure), Def. 7 (strong/weak lumpability); Thm 2 "spatial coarse-grainings that are causally closed are also computationally closed"; Thm 3 as summarized in section 3.4; §IV.4 module label with entering probabilities depending only on the module]
- Kemeny & Snell 1960 [M].
- Sarich, Noé & Schütte 2010, Theorem 3.1 (eqs (27)-(32)), Lemma 2.2, Theorem 3.3, §4.1, assumptions (7), (8), (12), (13), Remark 2.1. [P: checked in the published text during this spec]
- Deuflhard & Weber 2005 [V].
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann. (Markov blanket.) [M]
- Shai et al. 2024 [W: authors] (Mess3 fractal belief geometry); Marzen & Crutchfield 2017 [V] as the candidate original source of Mess3 (SPEC appendix C): verify which paper introduced Mess3 before attributing it.
- CoherentModes theorem register (programme source): `THEOREMS.md` B.7 (`:1877-1906`), B.8 (`:1910-1920`).
- Code/content provenance (not citations): Mess3 and catalogue matrices from `crw-blog/assets/widgets/hankel-hmm-src/build.py:27-70`; the epsilon-machine blog post (`crw-blog/_posts/2026-01-21-Computational-Mechanics-and-Epsilon-Machines.md`) as a content reference for Golden Mean and Even only, correcting its overgeneralized minimality claim and **not** following its use of "upsilon machine" for mixed-state presentations.

## 12. Implementation notes

- Files: `site/content/compmech.html`, `site/js/p_compmech.js`, helpers `p_compmech_hero.js`, `p_compmech_merge.js`, `p_compmech_closure.js`, `p_compmech_msm.js`; data `site/data/compmech/p06.json`, `site/data/compmech/widgets.json`.
- Shared modules used: `lib/hankel.js` (forward filter, conditional rows, word enumeration, projection coordinates as page 1), `lib/example.js` (chain loader), `lib/linalg.js` (SVD), `lib/rng.js`, `lib/bowtie.js`, `charts.js`, `ui.js`.
- `lib/hankel.js` additions requested (or page helpers): `predictiveStates(wfa, maxLen, horizon)` → rows and beliefs; `distinctRows(rows, tol)`; `windowJoint(wfa, L, H)` → J, marginals. Page helpers: agglomerative IB, weighted k-means, mutual information, lumpability defect, closure defect.
- Widget keys and URL state: hero `hr` (`hr_proc`, `hr_L`, `hr_tour`); merge `mg` (`mg_proc`, `mg_K`, `mg_L`, `mg_d`, `mg_tour`); closure `cl` (`cl_sys`, `cl_kappa`, `cl_tol`, `cl_tour`); norms `nm` (tour `default`); msm `ms` (tour `default`).
- Tests: parity of conditional rows and distinct counts with the builder (exact counts; rows 1e-12); IB and spectral loss curves vs `p06.json` (1e-9); closure tiles vs `p06.json` per κ; SNS figure reads only builder data.

## 13. Page-specific definition-of-done additions

- [ ] "Minimal" for the ε-machine always appears with its class ("among prescient history-based statistics").
- [ ] "υ-machine" appears only in Rosas et al.'s sense; no sentence equates it with mixed states.
- [ ] The section 8 hook wraps exactly C6.15, C6.29, C6.30 and the E13 card's first sentence (E13 is `~` in SPEC v1.2; its exact cases are stated outside the hook).
- [ ] Every count of "infinitely many" is attributed to page 1's proof (instrument) or a citation (Mess3); the hero's rising counts are described as finite-history counts, never as causal-state counts; the tilted pair label's counts are described as counts.
- [ ] Merging and projection are never conflated: every quoted merge loss is computed from the merge; the spectral tail is called a projection error or a lower bound on a merge's χ² loss (never on its KL information loss).
- [ ] δ and η of the SNS theorem are glossed at each use and never confused with $\delta_r$ or page 5's η (screen-read the section).
- [ ] The `closed` tour shows defect tiles reading 0 (to display precision) and the `tilted` tour nonzero values.

## Change log

- v1 (2026-11-17): first full spec. SNS Theorem 3.1 quoted from the published paper; Rosas et al. definitions and theorems rechecked; Banisch-Koltai and Froyland numbers recorded on page 4. The 2026 blog post's "upsilon machine = mixed-state presentation" usage is flagged for SPEC appendix D.
- v1.1 (2026-11-17): reconciled with SPEC v1.1 (SNS, Rosas, υ-machine and bibliography now in SPEC 4.2, appendices C and D). The hero's fallback became the named paused tour `instrument-late` (capture loads tours only, SPEC 6.5; the map's thumbnail uses it); the norms figure reads page 1's `p01.json` `chain.whitened`; the Mess3 attribution is still to verify.
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) Asymmetry knob replaced (SPEC 3.2): the old tilt kept the
  $x_2$ reflection and left the pair label exactly lumpable for every κ; the new one makes the upper wells switch
  pairs more readily, giving a positive defect (≈ 0.004 at κ = 0.3); 3.4's running-example text, the closure widget's
  purpose and `tilted` note, C6.21 and the builder assertion (now > 1e-3, plus up/down defect < 1e-10, and the
  basin-grid tie rule) follow. (2) Causal states: the hero's rising count is described as distinct finite-history
  predictive distributions, which can rise for finite ε-machines; the infinitely-many claim rests on page 1's new
  contraction proof (C6.3, C6.9, tiles, legend, DoD). (3) Approximate causal states: exact equivalence, K-group
  merging and rank reduction are kept apart; the spectral tail is a projection error and only a lower bound on a
  merge's χ² loss (3.3, C6.16, merge widget χ² view, norms figure, ledger); Gaussian IB shares CCA's directions, not
  its solution (C6.14, disclosure); E13 is `~`. (4) Rosas et al. Theorem 3's hypotheses stated per direction
  (stationary; plus irreducible and aperiodic for the strong directions) and its lumpability placed on the causal
  states (checked in arXiv v2 during this revision; C6.18, 3.4, ledger). Reviewer findings: math-1-6 1, 2, 5, 6;
  math-7-10 9 (E13).
- v1.3 (2026-11-17): round-2 review fix (SPEC v1.3). 3.3's key callout said the discarded tail bounds "what any merge
  loses", which a skim reader takes as the KL information loss; it is a lower bound on the merge's χ² loss only (KL ≈
  ½χ² holds only to second order, so the χ² bound does not transfer to the KL loss). Callout, merge widget
  purpose, norms figure label, ledger Bound row and DoD now say χ². Reviewer finding: round 2, item 8.
