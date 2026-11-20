# Page spec 05: Sparsity with guarantees

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 5 |
| id (hash, file stem) | `sparsity` |
| tab label | Sparsity |
| kicker | Page 5 · spectral sparsification |
| title | Sparsity with guarantees: thin graphs and sparse eigenbases |
| lede (one-sentence claim, ≤ 45 words) | Sparsity can be earned rather than imposed: a graph can be thinned to O(n log n/ε²) reweighted edges while every cut and energy changes by at most a factor 1 ± ε, and SEBA turns an eigenspace into sparse set indicators under stated conditions. |
| depends on | 4 (graphs, conductance, eigenspaces, the gap) |
| edges (SPEC 2.2) | E8, E9, E10, E18 |
| faces of the running example | A (equilibrium samples, N = 600, as a dense kernel graph); a planted companion for SEBA's failure modes (CoherentModes S.7) |
| main-path words | 2,100-2,500 |
| spec status | v1.3, 2026-11-17 (round-2 review fixes; change log) |

## 1. Reader outcome

After this page the reader can:

1. Say what a spectral sparsifier guarantees (every quadratic energy, hence every cut weight, degree and Laplacian eigenvalue, within a factor 1 ± ε) and what it does not (individual edge weights; eigenvectors without a gap; anything about signed or directed weights).
2. Sample a sparsifier by effective resistance, explain why a true bridge has the maximum leverage and is kept with high probability (and must be kept by every successful sparsifier with ε < 1) while edges inside dense regions are thinned and reweighted, why in a dense graph a bottleneck is protected as a whole (the leverages across any cut sum to at least 1) rather than edge by edge, and certify the achieved ε after the fact.
3. Translate a sparsifier's ε into an operator-norm error for a degree-one walk (2ε/(1+ε), CoherentModes S.2), then into a subspace error with Davis-Kahan, and say when that error is informative (when it is below half the gap).
4. Run SEBA on an eigenspace, read its sparse vectors as candidate set memberships, and state exactly when its output is guaranteed: exact recovery from an aligned start in the exact-indicator regime, an existence bound near it, and no guarantee from arbitrary starts (with a counterexample).
5. Assemble the certified chain "dense operator → sparse surrogate → eigenspace → sparse sets", with each arrow's bound and hypotheses, and say which links are deterministic, which are probabilistic and which are existence statements.

What they see: a haze of tens of thousands of edges thinned to a skeleton in which a few of the many faint edges crossing the barriers survive, now carrying large weights, so that each barrier's cut weight is kept; cut weights and eigenvalues that barely move; a kNN truncation with the same edge count that has no such guarantee (its measured error is shown, whatever it is); four sparse vectors that light up the four wells; a certificate box that reports a bound when its conditions hold and "certificate unavailable" when they do not; and a planted example where SEBA from random starts sometimes returns a wrong answer that its own diagnostics do not flag.

## 2. Skim path

1. Lede (header).
2. Hero figure `sparsity-fig-hero`: "Thin the graph, keep the cuts". Fig-sub: *A dense similarity graph on the particle's samples (left) and a sparsifier with a fraction of its edges (right): a few of the many faint edges across each barrier survive, heavily reweighted, and every cut weight moves by at most the stated factor.*
3. Section headings (verbatim, these are the claims):
   - "Sparsity can be a consequence rather than an assumption"
   - "A spectral sparsifier keeps every cut and energy"
   - "Every bottleneck keeps enough edges to carry its cut"
   - "SEBA turns an eigenspace into sparse set indicators"
   - "Sparse readouts are certified relative to a candidate"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `sparsity-fig-sparsifier`, `sparsity-fig-seba`, `sparsity-fig-chain`, `sparsity-fig-cifar`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: there are two principled sources of sparsity here, a sparse operator and a sparse readout; a spectral sparsifier keeps all cuts and energies within 1 ± ε with about n log n/ε² edges (n/ε² deterministically), so every bound of page 4 survives with a known loss; it samples edges by leverage, which keeps true bridges with high probability (every sparsifier with ε < 1 must contain them) and, in a dense graph, protects every bottleneck as a whole (the leverages across any cut sum to at least 1), keeping a few heavily reweighted crossing edges rather than every one; its accuracy can be certified after drawing; kNN truncation is not a sparsifier; SEBA rotates and thresholds an eigenspace into sparse memberships; its guarantees are conditional (aligned start, near-indicator eigenspace) and it can fail from arbitrary starts; the whole chain from dense operator to sparse sets has a bound, but the last step is an existence statement relative to a candidate partition, not a discovery guarantee.

## 3. Section outline

Section ids are `sparsity-<slug>`; figure ids are `sparsity-fig-<slug>`. An "Arriving here first?" aside (≤ 80 words) opens section 3.1: "A similarity graph joins data points with weights; its Laplacian's quadratic form $f^\top Lf = \frac12\sum W_{xy}(f_x - f_y)^2$ is the energy of a function on the points, and for an indicator it is the cut weight. The eigenvectors with the smallest eigenvalues relax the best cuts, and they are trustworthy when there is a gap after them. Page 4 builds all of this." Link page 4.

### 3.1 `sparsity-earned` "Sparsity can be a consequence rather than an assumption" (≈ 350 words)

Placement: the hero sits between the lede and this heading.

- For an interpretability reader, "sparse" usually means a sparse code: a sparse autoencoder is trained so that few features are active. Sparsity there is a premise, imposed by a penalty. This page shows two places where sparsity is a consequence of a theorem instead.
- (1) **A sparse operator.** A dense similarity graph on N points has about N²/2 edges. A spectral sparsifier keeps a reweighted subset of size O(N log N/ε²) with every cut and energy preserved to 1 ± ε. Which edges it keeps is not arbitrary: they are the ones that carry the graph's coarse structure. On page 10's NCS this is the "Z" term of the error budget.
- (2) **A sparse readout.** An eigenspace is a dense object: each eigenvector mixes the sets it describes. SEBA (sparse eigenbasis approximation) rotates the eigenspace and soft-thresholds it into a few sparse vectors, each supported on one set. This is the "R" (rounding) term.
- Running example (two sentences): the particle's equilibrium samples (face A), N = 600, joined by a Gaussian kernel; this dense graph is the input for every widget on the page. Say once that the kernel graph is dense by construction (all pairs above a negligible weight floor, builder-reported edge count) because a sparsifier is a statement about thinning a dense graph; page 4's kNN graph is already sparse, and is not a sparsifier of anything (section 3.3).
- One sentence of scope: everything here concerns undirected graphs with nonnegative weights (similarity graphs, reversible walks), not the signed, directed weights of a neural network; sparsifying a similarity graph is not pruning a network.

Key callout: "Two kinds of sparsity come with guarantees here: a thinned graph that keeps every cut, and sparse vectors read out of an eigenspace. Neither is imposed by a penalty on the data."

Disclosure "In other fields: sparse" (≤ 250 words): sparse code / SAE activations; sparse graph (few edges); sparse regression (SINDy, page 3); sparse eigenvectors (SEBA, this page). Link the glossary entry. Note that SEBA's sparse vectors are memberships over data points, not features over neurons, and that recovery of overlapping or k-sparse superpositions (what SAEs target) is not covered by anything on this page (CoherentModes `SPARSITY.md` introduction).

### 3.2 `sparsity-sparsifiers` "A spectral sparsifier keeps every cut and energy" (≈ 450 words)

Centrepiece: `sparsity-fig-sparsifier` after the fourth bullet.

- Definition (displayed equation 1): a reweighted subgraph with Laplacian $\tilde L$ is an ε-spectral sparsifier of L if
  $$(1-\varepsilon)\,x^\top Lx \le x^\top\tilde Lx \le (1+\varepsilon)\,x^\top Lx\qquad\text{for every } x\in\mathbb R^n.$$
  Gloss: the inequality is for **every** vector at once (Loewner order).
- Consequences, each in a sentence: every cut weight ($x = \mathbf 1_A$); every degree ($x = e_v$, so $d_v = e_v^\top Le_v$); every Laplacian eigenvalue (Courant-Fischer); every energy of page 4's recipe. Normalized quantities (conductance, normalized eigenvalues) pick up the ratio of the two factors, so they move by at most $(1+\varepsilon)/(1-\varepsilon)$ (edge E8). Eigenvectors are not preserved individually; an isolated block moves by the Davis-Kahan amount, so only when its gap dominates the error.
- Existence and construction (displayed equation 2 is the edge count):
  - Spielman & Srivastava 2011: sample $q = O(n\log n/\varepsilon^2)$ edges with replacement, edge e with probability proportional to $w_eR_e$ (weight times effective resistance), and give each sampled copy weight $w_e/(q\,p_e)$; with constant probability the result is an ε-sparsifier. The constant in O(·) is universal but not explicit, and the theorem asks n large and ε > 1/√n.
  - Batson, Spielman & Srivastava 2012: deterministically, $O(n/\varepsilon^2)$ edges with $(1-\varepsilon)^2L \preceq \tilde L \preceq (1+\varepsilon)^2L$ (note the squared factors; do not silently replace them).
- For a degree-one walk P (NCS's Sinkhorn-balanced walks, page 10), the CoherentModes theorem register, S.2, turns the sparsifier into a sparse walk: $P_* = I - \tilde L/(1+\varepsilon)$ is again nonnegative, symmetric, doubly stochastic and PSD, with
  $$\|P_* - P\|_2 \le \frac{2\varepsilon}{1+\varepsilon}$$
  (displayed equation 3), cut and energy factors in $[(1-\varepsilon)/(1+\varepsilon), 1]$, and relative guarantees on $1 - \lambda_i$, not on $\lambda_i$. Hypothesis: normalize first (Sinkhorn of a sparsified kernel is a different object).
- An a posteriori point that makes this practical: once a sparsifier is drawn, its actual ε is determined by the extreme generalized eigenvalues of $(\tilde L, L)$. A fast iterative estimate (Lanczos) of those extremes can err in the wrong direction (its largest Ritz value can be below the true maximum, its smallest above the true minimum), so it is reported as an **estimate**. The **certificate** is a verified check: at a stated $\varepsilon_{\rm cert}$ slightly above the estimate, both $(1+\varepsilon_{\rm cert})L - \tilde L$ and $\tilde L - (1-\varepsilon_{\rm cert})L$ are proved positive definite on $\mathbf 1^\perp$ by Rump's (2006) verified test: a floating-point Cholesky factorization of each matrix with its diagonal lowered by a shift that provably exceeds every rounding error, both of the factorization and of forming the matrix (5.2 gives the recipe). An ad hoc shift would make this a numerical check, not a certificate. The probabilistic theorem tells you how many edges to try; the check turns the outcome into a deterministic certificate. The widget does both.
- Running example (explorer tour `resistance`): quote the builder's dense edge count, edges kept, certified ε, and the worst relative change of $\mu_2..\mu_5$ for the target ε of the tour. Say honestly that at N = 600 the saving is modest (the theorem is asymptotic, and its constants can eat practical savings at moderate N; register S.2 remarks the same).

Key callout: "A spectral sparsifier preserves the quadratic form for every vector at once, so every cut, degree and eigenvalue of page 4 survives with a known factor. Its accuracy can be certified after drawing it by a verified check, which turns a probabilistic construction into a certificate."

Disclosures:
- "Why this holds: sampling by leverage" (≤ 500 words): write $L = \sum_e w_e b_eb_e^\top$; in coordinates where L is the identity on $\mathbf 1^\perp$, each term has norm $w_eR_e$ (its leverage); sampling terms in proportion to their norms and reweighting gives an unbiased estimate of the identity whose deviation is controlled by a matrix concentration inequality (Rudelson's lemma in the original; matrix Chernoff bounds in later accounts). Foster's theorem $\sum_e w_eR_e = n - 1$ fixes the total, which is why the sample count scales with n, not with the number of edges.
- "Hypotheses: what the sparsifier theorems assume" (≤ 300 words): undirected connected graph, nonnegative weights; SS: n sufficiently large, $1/\sqrt n < \varepsilon \le 1$, success with constant probability; BSS: any weighted undirected graph, polynomial-time deterministic, squared factors; S.2: dense PSD bistochastic P, sparsify the loop-free part, then form $P_*$; loops cancel in L.

### 3.3 `sparsity-resistance` "Every bottleneck keeps enough edges to carry its cut" (≈ 400 words)

- Effective resistance, glossed in one line (the voltage drop between x and y when unit current flows in at x and out at y through a resistor network with conductances $W$; $R_{xy} = (e_x - e_y)^\top L^+(e_x - e_y)$). Leverage $w_eR_e$ is between 0 and 1; it equals 1 exactly for a bridge (an edge whose removal disconnects the graph) and is small for an edge with many parallel routes. Foster: the leverages sum to n − 1.
- So resistance sampling gives an edge that is the only way between two regions (a bridge) the maximum leverage, 1, and keeps it with high probability at the stated budget: with q independent draws (with replacement) it is missed with probability $(1 - 1/(n-1))^q \approx e^{-q/(n-1)}$, about $n^{-1/\varepsilon^2}$ at $q = n\ln n/\varepsilon^2$, small but not zero (the page says "kept with high probability", never "always kept"). Conversely, every successful sparsifier with ε < 1 must contain every bridge: without it the bridge's cut would have weight 0 in $\tilde L$, violating the lower Loewner inequality for that cut's indicator. Resistance sampling thins the many interchangeable edges inside dense regions, reweighting the survivors upward so the energy is unchanged. A barrier in a dense graph is usually not one bridge but thousands of faint edges, each with a tiny weight and a small leverage (the score is weight **times** resistance). What is protected is the bottleneck **as a whole**: the leverages of the edges crossing any cut sum to at least 1, exactly as a single bridge's do (disclosure), so with q samples the cut receives at least $q/(n-1) \approx \ln n/\varepsilon^2$ of them in expectation, and the few crossing edges kept are reweighted so that the cut weight is preserved to $1\pm\varepsilon$. On the running example (explorer panel (a); builder statistics, quoted as computed): the leverage summed over the between-pair cut and over each within-pair cut (each ≥ 1), the mean leverage of a crossing edge against all edges (an independent check found crossing edges far **below** the mean, ≈ 0.0002 against ≈ 0.006, and only a fraction of a percent of them kept at ε = 0.5), and the cut weights before and after.
- One sentence, marked as a reading (SPEC 5.5: "can be read as"): the surviving skeleton can be read as the graph's coarse-graining drawn in edges: dense patches where the sets are, a few heavy edges carrying each cut between them. This is the sense in which the programme calls sparsifiers a principled source of sparsity for interpretation; wrap the "principled source of sparsity for interpretation" phrasing in the section 8 hook (C5.10, motivation), since no theorem says the kept edges are the interpretable ones beyond the leverage argument.
- Contrast (explorer tours `weight` and `knn`): sampling in proportion to weight alone ignores resistance, so a bottleneck gets only its share of the total weight and a faint one can get few or no samples, with no guarantee; truncating to each point's k largest weights (kNN truncation, the usual way to "sparsify" a similarity graph) is not a reweighted sample and has no spectral guarantee; its measured ε̂ is shown, and may be large or small; the page states only that nothing certifies it (register S.2's last paragraph; THEORY treats it as a separate estimand).
- Edge E10 (`=`, pages 4/5–8): the same Laplacian's pseudo-inverse that gives effective resistance here is the resistor network of page 8's Hebbian model, whose clamped voltages solve page 4's Dirichlet problem (connections strip).

Key callout: "Resistance sampling keeps an edge in proportion to how indispensable it is. A true bridge has the largest possible leverage and is kept with high probability, and any sparsifier that succeeds must contain it; a barrier crossed by many faint edges is protected as a whole, by a few survivors made heavy enough to carry its cut."

Disclosure "The maths: effective resistance as a Dirichlet problem" (≤ 300 words): $R_{xy}$ as the minimum energy of a unit flow (Thomson's principle) and as the inverse of the energy of the harmonic function with $f_x = 1$, $f_y = 0$ (the Dirichlet problem of page 4's disclosure); leverage of a bridge = 1; **the leverages across any cut sum to at least 1**: with $\Pi = W^{1/2}BL^+B^\top W^{1/2}$ the orthogonal projector whose diagonal holds the leverages, the vector y with entries $\pm\sqrt{w_e}$ on the cut's edges and 0 elsewhere lies in Π's range ($y = W^{1/2}B\mathbf 1_A$), so the principal submatrix of Π on the cut has eigenvalue 1 and its trace, the summed leverage, is at least 1 (standard; it follows from Spielman & Srivastava's setup); cost of computing all resistances (dense pseudo-inverse here at N = 600; nearly-linear-time sketches in Spielman & Srivastava).

### 3.4 `sparsity-seba` "SEBA turns an eigenspace into sparse set indicators" (≈ 450 words)

Centrepiece: `sparsity-fig-seba` after the third bullet.

- The problem: page 4's bottom k eigenvectors span (approximately) the indicators of k sets, but each eigenvector is a dense mixture; at k = 4 on the running example, $f_2$ is "which pair", $f_3$ and $f_4$ are smooth mixtures of the within-pair splits. One wants k vectors, each supported on one set, spanning (nearly) the same space.
- SEBA (Froyland, Rock & Sakellariou 2019; register S.5), with V an orthonormal N × r basis of the eigenspace including the constant (displayed equation 4):
  $$\min_{R^\top R = I,\ \|s_j\| = 1}\ \tfrac12\|VR - S\|_F^2 + \mu\|S\|_{1,1}.$$
  Alternate: soft-threshold each column of VR at μ and normalize; then update R by orthogonal Procrustes. Finally fix signs, rescale each vector's maximum to 1, and assign each point to the vector with the largest positive value (or leave it unassigned). Nonnegativity is encouraged, not imposed; thresholding can leave the span and even lose rank, so the output is a **candidate**, not an orthonormal basis.
- What is guaranteed, each in one or two sentences with its hypothesis (all from the register; SPEC E9):
  - S.6: for fixed orthonormal V and $0 < \mu < 1/\sqrt N$, the idealized alternation decreases its objective, the objective converges, and every accumulation point is coordinatewise optimal. Not global optimality; not recovery.
  - S.7: if the eigenspace is **exactly** the span of the indicators of r disjoint sets, an aligned start with $0 < \mu < \min_j n_j^{-1/2}$ returns the indicators in one step and stays there; grouping equal rows of V finds such a start without labels; the global maximizers of the quartic (varimax) objective are exactly the signed indicator bases. But the span condition and threshold **alone do not imply recovery from arbitrary starts**: an explicit Hadamard-rotated start is a fixed point that is not an indicator basis (planted tour `stuck`), and on exact indicators of sizes (20, 5, 3, 2) the published default threshold recovered the sets from 43 of 200 random starts in the register's runs, while 0.1, 0.05, 0.02 recovered all 200 (planted tour `random-starts`; this browser's own count is shown and labelled as such).
  - Froyland & Rock 2025 (Propositions 3.8, 3.20) give geometric bounds (higher Cheeger ratios) for superlevel sets of suitable thresholded combinations, under the hypotheses that the thresholded combinations are nonzero and have pairwise disjoint supports; these are hypotheses on the output, not algorithmic guarantees.
- Running example (SEBA widget tour `wells`): at r = 4 on the dense Sinkhorn walk, SEBA from the published start finds four vectors, one per well (builder: matched agreement with the basins, unassigned fraction); at r = 2 (tour `pairs`), two pair vectors.

Key callout: "SEBA's guarantees are conditional: exact recovery from an aligned start when the eigenspace is exactly spanned by indicators, and no guarantee from arbitrary starts. A clean-looking output is not by itself evidence that the sets are right."

Disclosure "Why this holds: one SEBA step from an aligned start" (≤ 400 words): write V = HO; with R = O the matrix VR is H; soft-thresholding a normalized indicator column multiplies it by $1 - \mu\sqrt{n_j} > 0$, which normalization undoes; Procrustes returns O again. The basin condition of S.7 (off-diagonal entries of $OR_0^\top$ below $\mu\sqrt{n_i}$, diagonal above) for nearby starts. The Hadamard counterexample: every entry of V has magnitude $1/\sqrt N$, thresholding below that leaves V unchanged, Procrustes returns the identity.

### 3.5 `sparsity-certified` "Sparse readouts are certified relative to a candidate" (≈ 450 words)

Placement: `sparsity-fig-chain` (static) after the second bullet; `sparsity-fig-cifar` (static) after the fourth bullet.

- The near-indicator regime (register S.8). Given any candidate partition into r sets, with normalized indicator matrix H ($H_j = \mathbf 1_{A_j}/\sqrt{n_j}$), measure how far the eigenspace is from containing it (displayed equation 5):
  $$\eta = \|(I - VV^\top)H\|_F,\qquad c = \min_j\big(1 - \mu\sqrt{n_j}\big).$$
  If $0 < \mu < \min_jn_j^{-1/2}$ and $\sqrt2\,\eta < c$, there **exists** an orthogonal alignment whose threshold step S satisfies $\|S - H\|_F \le 2\sqrt2\,\eta/c$ (displayed equation 6). For any returned S, loadings inherit the error: $\|F^\top(S - H)\|_F \le \|F\|_2\|S - H\|_F$ for any feature matrix F (so a set's mean activation is known to that accuracy). This is a sound test of a **given** candidate, not a procedure that finds one, and not a guarantee for a SEBA run.
- The certified chain (figure `sparsity-fig-chain`), every link on the same N points so the errors add (SPEC 4.3):
  1. dense walk P → sparse surrogate $P_*$: $e_Z = 2\varepsilon_{\rm cert}/(1+\varepsilon_{\rm cert})$ with the certified ε (S.2; deterministic once the verified check passes; an uncertified estimate breaks the chain here);
  2. → eigenspace: if $e_Z < \delta_r/2$, $\|\sin\Theta\|_{\rm op} \le e_Z/(\delta_r - e_Z)$ (Davis-Kahan, register A.21);
  3. → residual: $\eta_* \le \eta + \sqrt r\,\|\sin\Theta\|_{\rm op}$ (triangle inequality, $\|H\|_F = \sqrt r$);
  4. → sets: if $\sqrt2\,\eta_* < c$, an aligned threshold step within $2\sqrt2\,\eta_*/c$ of H exists (S.8).
  The first three links are deterministic theorems; the last is an existence statement. Where a link's condition fails, the chain says "certificate unavailable", and the widget shows exactly which link failed.
- Where η comes from: page 4 (section 3.4) bounds it for any partition by its conductances over the next eigenvalue, $\eta^2 \le \sum_j\phi(A_j)/\mu_{r+1}$, for degree-one graphs where the normalized indicators are exactly these H (edge E9 is this link). So a partition with small conductances and a large next eigenvalue is certified recoverable-by-alignment; whether a given SEBA run finds it is checked, not guaranteed.
- Real data (figure `sparsity-fig-cifar`): the programme's ResNet-20 / CIFAR-10 study used SEBA on a layer block's top eigenvectors (the image shows the r = 3 case, with set sizes as printed). There is no certificate there: no candidate partition is supplied, and its graphs are kNN unions with a small dense floor, not sparsifiers. Read it as what the readout looks like on a real network, with page 10 carrying the budget (edge E18).
- Close with what is refused (register `SPARSITY.md` §5): gaps and localization alone do not certify concepts; search failure does not mean absence of sparse structure; overlapping sets are not covered.

Key callout: "Given a candidate partition, its distance η from the eigenspace certifies that an aligned sparse readout lies within $2\sqrt2\eta/c$ of it. Combined with the sparsifier and Davis-Kahan, the whole chain from dense graph to sparse sets has a bound, ending in an existence statement."

Disclosures:
- "Why this holds: the S.8 bound" (≤ 300 words): Procrustes alignment error $\le\sqrt2\eta$ (from the principal-angle cosines); soft-thresholding is 1-Lipschitz coordinatewise and maps $H_j$ to $c_jH_j$; normalizing at most doubles a relative error.
- "Hypotheses: SEBA as implemented" (≤ 300 words): the published code perturbs near-constant columns after QR and stops after 5000 iterations; S.6-S.8 concern the idealized iteration on an orthonormal V; the port in `lib/seba.js` follows `CoherentModes/explore/cifar_baselines/variants.py:261` (`seba_mu`), including the perturbation, and the page says so.

### 3.6 `sparsity-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.7 `sparsity-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.8 `sparsity-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C5.1 | Sparse codes (SAEs) impose sparsity by a penalty; a spectral sparsifier and SEBA obtain it as a consequence of a theorem or a stated optimization. | construction (framing) | text | — | 3.1 |
| C5.2 | These results concern undirected nonnegative graphs, not pruning signed directed network weights. | standard (scope) | SPEC appendix D | — | 3.1 |
| C5.3 | An ε-spectral sparsifier preserves every quadratic form, hence every cut weight, degree and Laplacian eigenvalue, within 1 ± ε. | theorem | definition + Courant-Fischer; Spielman & Srivastava 2011; register S.1-S.2 | Loewner inequality for all x | 3.2 |
| C5.4 | Conductances and normalized eigenvalues move by at most the ratio $(1+\varepsilon)/(1-\varepsilon)$; eigenvectors only through Davis-Kahan when the gap dominates. | theorem | E8; generalized Rayleigh quotients; register A.21 | as C5.3; isolated block | 3.2 |
| C5.5 | Sampling $O(n\log n/\varepsilon^2)$ edges by $w_eR_e$ with reweighting gives an ε-sparsifier with constant probability. | theorem | Spielman & Srivastava 2011, Thm 1 | n large, $1/\sqrt n < \varepsilon \le 1$; universal constant not explicit | 3.2 |
| C5.6 | $O(n/\varepsilon^2)$ edges suffice deterministically, with squared factors. | theorem | Batson, Spielman & Srivastava 2012, Thm 1.1 | any weighted undirected graph | 3.2 |
| C5.7 | For a dense PSD bistochastic P, $P_* = I - \tilde L/(1+\varepsilon)$ is PSD bistochastic with $\|P_* - P\|_2 \le 2\varepsilon/(1+\varepsilon)$ and cut/energy factors in $[(1-\varepsilon)/(1+\varepsilon), 1]$; relative guarantees are on $1 - \lambda_i$. | theorem | register S.2 | normalize first; sparsify the loop-free part | 3.2 |
| C5.8 | A drawn sparsifier's ε can be certified afterwards by a verified check of both Loewner inequalities at a stated $\varepsilon_{\rm cert}$, turning the guarantee into a deterministic certificate; a Lanczos estimate of the extreme generalized eigenvalues is only an estimate (it can understate ε). | construction + standard | explorer tiles "estimated ε̂" and "certified ε"; Rump 2006 | Rump 2006, Cor. 2.7 with bound I's shift plus a radius for the rounding in forming the test matrices (5.2); the J/n terms reduce the test to $\mathbf 1^\perp$; IEEE binary64 arithmetic with rounding to nearest (JavaScript numbers) | 3.2 |
| C5.9 | On the running example, a resistance-sampled sparsifier at the tour's target ε keeps a stated fraction of edges with certified ε and stated eigenvalue changes; savings are modest at N = 600. | widget + builder values | explorer tours `resistance`, `tight` | builder values | 3.2 |
| C5.10 | Graph sparsifiers are a principled source of sparsity for interpretation (the kept skeleton is the interpretable coarse structure). | motivation (section 8 hook) | — | — | 3.3 |
| C5.11 | Leverage $w_eR_e \in (0, 1]$, equal to 1 for a bridge; leverages sum to n − 1. | standard | Foster 1949, via Spielman & Srivastava 2011 | connected graph | 3.3 |
| C5.12 | The leverages of the edges crossing any cut sum to at least 1, so every cut receives at least $q/(n-1)$ samples in expectation; a true bridge (leverage 1, the maximum) is kept with high probability (missed with probability $(1 - 1/(n-1))^q > 0$), and every sparsifier with ε < 1 contains every bridge. | theorem (standard; proof in disclosure) | disclosure "effective resistance"; Spielman & Srivastava 2011 setup | connected graph | 3.3 |
| C5.12a | On the running example the crossing edges are many and faint: their summed leverage per cut, their mean leverage against all edges, the fraction kept and the cut weights before and after are as the builder reports (an independent check: mean crossing leverage ≈ 0.0002 against ≈ 0.006 overall, so most crossing edges are dropped while each cut's weight is kept). | widget + builder values | explorer panel (a), tour `resistance`; `p05.json` `crossing` | builder values; no direction assumed in advance | 3.3 |
| C5.13 | Weight-proportional sampling and kNN truncation carry no spectral-sparsifier guarantee; their measured errors are shown. | standard (absence of theorem) + widget | register S.2 last paragraph; tours `weight`, `knn` | — | 3.3 |
| C5.14 | SEBA alternates soft-thresholding and Procrustes on a rotated eigenbasis; output is a candidate that can leave the span or lose rank. | construction | Froyland, Rock & Sakellariou 2019, §3, Alg. 3.1; register S.5 | — | 3.4 |
| C5.15 | For fixed orthonormal V and $0 < \mu < 1/\sqrt N$, the idealized SEBA objective converges and accumulation points are coordinatewise optimal. | theorem | register S.6 (the programme's argument, not attributed to FRS) | idealized iteration; not the capped, perturbed implementation | 3.4 |
| C5.16 | In the exact-indicator regime an aligned start returns the indicators exactly; equal-row grouping supplies such a start; quartic maximizers are exactly signed indicator bases. | theorem | register S.7 (1-3) | span exactly equal to disjoint indicators; $0 < \mu < \min_jn_j^{-1/2}$ | 3.4 |
| C5.17 | Span and threshold conditions alone do not imply recovery from arbitrary starts: an explicit Hadamard fixed point; 43/200 recoveries at the default threshold on sizes (20, 5, 3, 2) in the register's runs. | theorem (counterexample) + empirical (programme) | register S.7 (4) and `SPARSITY.md:151`; SEBA widget tours `stuck`, `random-starts` | the 43/200 is the register's numpy record; the browser count is labelled as the browser's | 3.4 |
| C5.18 | Superlevel sets of suitable thresholded combinations have bounded higher Cheeger ratios. | theorem (conditional) | Froyland & Rock 2025, Props 3.8, 3.20 | thresholded combinations nonzero with pairwise disjoint supports | 3.4 |
| C5.19 | On the running example SEBA finds four well vectors at r = 4 and two pair vectors at r = 2 from the published start. | widget + builder values | SEBA tours `wells`, `pairs` | builder values; published start and threshold | 3.4 |
| C5.20 | If $0 < \mu < \min_jn_j^{-1/2}$ and $\sqrt2\eta < c$, an aligned threshold step S with $\|S - H\|_F \le 2\sqrt2\eta/c$ exists; loadings inherit $\|F^\top(S - H)\|_F \le \|F\|_2\|S - H\|_F$. | theorem (existence; conditional) | register S.8 | candidate partition into exactly r nonempty sets; V orthonormal incl. constant | 3.5 |
| C5.21 | The chain dense → sparse → eigenspace → residual → sets composes with the stated bounds on the same N points. | theorem (composition of S.2, A.21, triangle inequality, S.8) | `sparsity-fig-chain`; SEBA widget certificate box | each link's condition; last link existence only | 3.5 |
| C5.22 | For degree-one graphs, $\eta^2 \le \sum_j\phi(A_j)/\mu_{r+1}$ (page 4) feeds S.8. | theorem | page 4 C4.18; E9 | degree one so normalized indicators are $\mathbf 1_A/\sqrt{n_j}$ | 3.5 |
| C5.23 | The CIFAR-10 figure shows SEBA sets on a real network's layer block; no certificate is claimed. | empirical (programme) | `sparsity-fig-cifar` | kNN-union graphs, not sparsifiers | 3.5 |

Things not to claim on this page (SPEC appendix D and page-specific): spectral sparsification prunes networks safely; SEBA recovers the true sets; kNN truncation is a sparsifier; a sparsifier preserves eigenvectors (only blocks, with a gap); the SS constant is known or small; the S.8 bound guarantees a SEBA run's output; sparse SEBA vectors are features or concepts; SEBA handles overlapping sets; the browser's random-start count is a recovery probability.

## 5. Figures and widgets

All face A figures use the first 600 points of `samples.json` (seed 0) and draw potential contours and wells as on page 4. The base graph is the dense Gaussian kernel $W_{xy} = e^{-\|x-y\|^2/(2s^2)}$, s = 0.25 (builder may adjust, see section 6), with entries below $10^{-10}\max W$ dropped (stated in captions as "weights below 1e-10 of the maximum dropped"); "Sinkhorn" means the symmetric Sinkhorn balancing of $W$ with its unit diagonal kept (register A.1), giving a degree-one PSD walk P.

### 5.1 `sparsity-fig-hero` "Thin the graph, keep the cuts" (live, hero; key `hr`)

- **Purpose:** a sparsifier with a fraction of the edges keeps the cut weights; the edges it keeps across the barriers are few and heavy.
- **Layout:** `figure.fig.full.card`; two maps side by side (stacked on phones) plus a strip below. (a) Dense graph: all edges with opacity ∝ weight (rendered as one canvas layer; the haze is the point). (b) Sparsifier: kept edges with line width ∝ new weight; edges crossing between basins in accent. Strip: grouped bars for the cut weights of the pair partition and of the four-well partition (each set's cut), dense versus sparse, with the ratio printed on each pair of bars.
- **Data:** live, `lib/graph.js` (`effectiveResistances`, `sampleSparsifier`), seed 0, plain (unnormalized) Laplacian of W; q from the target ε (section 5.2).
- **Controls:** segmented "target ε: 0.5 | 0.3"; button "resample" (advances the seed).
- **Default state (= first tour):** `eps05` (target 0.5, seed 0).
- **Tours:** `eps05`; `eps03` (target 0.3, seed 0).
- **fallbackTour:** `eps05`.
- **Caption:** *Plotted:* (a) edges of the Gaussian kernel graph on the samples, opacity proportional to weight; (b) edges of a sparsifier drawn by effective-resistance sampling, width proportional to the reweighted weight, edges between basins highlighted; bars: cut weight of each set of the two-pair and four-well partitions in the dense graph and the sparsifier. *Values:* N = 600, s = 0.25, weights below 1e-10 of the maximum dropped, q = ⌈n ln n/ε²⌉ samples at the target ε, seed as shown. Running example, face A. `synthetic`.
- **Static fallback:** `assets/fallback/sparsity-fig-hero-eps05.png`, `...-eps03.png`.
- **Accessibility:** alt text: "Left, a dense grey haze of edges over four clusters of points; right, a sparse set of edges in which a few thick edges cross between clusters; below, paired bars of nearly equal height."
- **Performance:** resistances via dense Cholesky of $L + \mathbf 1\mathbf 1^\top/n$ and its inverse at n = 600: < 500 ms once (cached per graph); sampling q ≤ 5·10⁴ draws by alias method < 20 ms; drawing ≤ 10⁵ edges on canvas < 50 ms.

### 5.2 `sparsity-fig-sparsifier` "What survives, and what is guaranteed" (live, centrepiece; key `sp`)

- **Purpose:** measured accuracy against the guarantee; who survives; how sampling by resistance differs from sampling by weight and from kNN truncation.
- **Layout:** `ui.simLayout`; main view 2 × 2; side panel: tours, controls, tiles, legend.
  - (a) **Leverage**: histogram of $w_eR_e$ (log x) for all edges, with the barrier-crossing edges (endpoints in different basins) overlaid in accent; a marker at the mean leverage (n − 1)/m; beside it, three small bars giving the **summed** leverage across the between-pair cut and the two within-pair cuts, with a reference line at 1.
  - (b) **Quadratic forms**: ratio $x^\top\tilde Lx/x^\top Lx$ for three families: the eigenvectors $f_2..f_{12}$ of L (dots), the indicators of the pair and well partitions' sets (diamonds), and 50 random vectors orthogonal to $\mathbf 1$ (small grey dots); horizontal band $[1-\varepsilon, 1+\varepsilon]$ for the target ε and dashed lines at the measured $1 \pm \hat\varepsilon$.
  - (c) **Spectrum**: $\tilde\mu_i/\mu_i$ for i = 2..12 of the normalized Laplacian (bars around 1) with the band $[(1-\hat\varepsilon)/(1+\hat\varepsilon), (1+\hat\varepsilon)/(1-\hat\varepsilon)]$.
  - (d) **Blocks**: actual $\|\sin\Theta\|_{\rm op}$ between the dense and sparse bottom-2 and bottom-4 eigenspaces (normalized Laplacians, or P and $P_*$ in Sinkhorn mode), with the Davis-Kahan bound from the measured operator error, or "vacuous" when $e \ge \delta/2$.
- **Data:** live; edge sets and resistances as in the hero. Estimated ε̂ = max(θ_max − 1, 1 − θ_min) over the generalized eigenvalues θ of $(\tilde L + \mathbf 1\mathbf 1^\top/n,\ L + \mathbf 1\mathbf 1^\top/n)$ restricted to $\mathbf 1^\perp$, by Lanczos on $C^{-1}(\tilde L + J/n)C^{-\top}$ with $L + J/n = CC^\top$ (Cholesky); labelled "estimate". Certified ε: $\varepsilon_{\rm cert} = \hat\varepsilon + 10^{-6}$ (a floating-point number). Test matrices $T_+ = (1+\varepsilon_{\rm cert})(L + J/n) - (\tilde L + J/n)$ and $T_- = (\tilde L + J/n) - (1-\varepsilon_{\rm cert})(L + J/n)$, with L and $\tilde L$ the exact Laplacians of the stored edge weights (the J/n terms give both matrices the eigenvalue $\varepsilon_{\rm cert} > 0$ on the constant direction, which both Laplacians annihilate, so $T_\pm \succ 0$ is exactly the strict Loewner pair on $\mathbf 1^\perp$). Each is checked by `linalg.verifyPD`, a faithful implementation of Rump 2006, Corollary 2.7 with his bound I (u = $2^{-53}$, $\gamma_k = ku/(1-ku)$):
  1. form $\hat T$ in floating point (upper triangle, mirrored, so it is exactly symmetric; degrees summed in floating point); fail at once if any $\hat T_{ii} \le 0$;
  2. formation radius $R = \gamma_{n+5}\big((1+\varepsilon_{\rm cert})(|L| + J/n) + |\tilde L| + J/n\big)$ entrywise: it bounds $|T - \hat T|$ (n − 2 additions for a degree, at most six further rounded operations per entry); $r$ = the largest row sum of R ($\ge \|R\|_2$ for a nonnegative symmetric R: Collatz's bound with the all-ones vector);
  3. Rump's shift (bound I) $c = \gamma_{n+1}(1-\gamma_{n+1})^{-1}\,\mathrm{tr}(\hat T) + 3n(2n + \max_i\hat T_{ii})\,2^{-1074}$ (the last term covers underflow). R, r and c are computed in floating point from nonnegative terms and from the computed degrees; use $s = 1.02\,\mathrm{fl}(c + r)$, the factor covering every rounding in those computations (relative errors below $10^{-9}$ for n ≤ 1000);
  4. lower the diagonal without directed rounding (Rump's Lemma 2.5 and (2.11)): $d_i = \mathrm{fl}(\hat T_{ii} - s)$, $\tilde T_{ii} = \mathrm{fl}(d_i - \varphi|d_i|)$ with $\varphi = u(1 + 2u)$; off-diagonal entries unchanged;
  5. run plain floating-point Cholesky (no pivoting; the textbook recurrence, any loop order) on $\tilde T$. If every pivot is positive, every symmetric X with $|X - \hat T| \le R$, in particular the exact $T_\pm$, is positive definite (Cor. 2.7).
  JavaScript numbers meet the paper's arithmetic model (IEEE 754 binary64, rounding to nearest, every operation rounded to double, no extended precision), so the check is rigorous in the browser, provided it never uses float32 storage or GPU kernels; the builder may use LAPACK's Cholesky (Rump's own Algorithm 1 calls Matlab's `chol`) with the same steps 1-4. If either check fails, double the margin $\varepsilon_{\rm cert} - \hat\varepsilon$ and retry up to 10 times, then report "not certified". At n = 600 a full dense generalized symmetric eigensolve is also affordable in the builder, which records its extremes beside the Lanczos estimate.
- **Controls (primary):**
  1. method: `resistance` (Spielman-Srivastava sampling) | `weight` (sampling ∝ $w_e$, same reweighting) | `knn` (keep each point's $k$ largest weights, symmetrized by union, no reweighting; k chosen so the edge count matches the resistance sparsifier's distinct-edge count);
  2. target ε: 0.9 | 0.7 | 0.5 | 0.3 | 0.2 (sets q = ⌈n ln n/ε²⌉ draws; the legend says "illustrative constant 1; the theorem's constant is not explicit");
  3. normalization: `plain` (sparsify L) | `sinkhorn` (sparsify I − P, report $P_*$ and $2\hat\varepsilon/(1+\hat\varepsilon)$, S.2);
  4. seed: 0-9.
  Advanced: bandwidth s (0.15-0.4).
- **What changes:** method/ε/seed redraw the sparse graph and all panels; normalization switches (c), (d) and the tiles between normalized-Laplacian and walk quantities; s rebuilds the dense graph (resistances recomputed, "computing…").
- **Stat tiles:** "edges: dense / kept (distinct)"; "estimated ε̂ (Lanczos)" and "certified ε" (or "not certified") (and, in `sinkhorn`, "$\|P_* - P\|_2$ ≤ 2ε/(1+ε) = …" at the certified ε, with the actual norm beside it); "max change of μ₂..μ₅" (relative); "crossing edges kept" (count kept / count in dense graph, against all edges kept / all edges, whatever the comparison shows); "cut weights kept" (between-pair and within-pair cut weights, sparse over dense).
- **Tours** (default first):
  1. `resistance`: resistance, ε = 0.5, plain, seed 0. Note: "Every ratio sits inside the certified band. Few of the faint crossing edges survive, but those that do are heavy enough to keep each barrier's cut weight." (Rewrite the second sentence from `p05.json` `crossing` if the builder finds otherwise.)
  2. `tight`: resistance, ε = 0.3. Note: "More samples, a narrower band."
  3. `weight`: weight, ε = 0.5. Note: "Sampling by weight alone gives a bottleneck only its share of the total weight, with no guarantee; a faint barrier can get few or no samples." (Quote the builder's cut ratios.)
  4. `knn`: knn at the same edge count. Note: "kNN truncation keeps short edges and drops the rest without reweighting: nothing certifies it." (Do not promise that it looks worse; the tile reports what it is.)
  5. `sinkhorn`: resistance, ε = 0.5, sinkhorn. Note: "For a degree-one walk the sparse surrogate stays a walk, within 2ε/(1+ε) in operator norm."
- **fallbackTour:** `resistance`.
- **Caption:** *Plotted:* (a) leverages $w_eR_e$ of all edges, barrier-crossing edges highlighted; (b) $x^\top\tilde Lx/x^\top Lx$ for eigenvectors, set indicators and random vectors, with the target band and the certified band; (c) ratios of normalized-Laplacian eigenvalues, sparse over dense; (d) sine of the largest principal angle between dense and sparse eigenspaces, with the Davis-Kahan bound. *Values:* N = 600, s as set, method, target ε, normalization and seed as set; q = ⌈n ln n/ε²⌉. Running example, face A. `synthetic`.
- **Static fallback:** PNG per tour; no GIF.
- **Accessibility:** panels with `aria-label`; tiles as text; tour notes announced.
- **Performance:** ε̂ by Lanczos (≈ 40 iterations of two triangular solves at n = 600) < 100 ms; certification (two dense 600 × 600 Cholesky factorizations) < 150 ms; eigenpairs of sparse and dense normalized Laplacians < 200 ms; total per control change < 400 ms. Parity: resistances and the seeded sample (edge multiset) match the builder exactly for seeds 0-2.

### 5.3 `sparsity-fig-seba` "From an eigenspace to sparse sets" (live; key `sb`)

- **Purpose:** SEBA's sparse vectors pick out the wells; the certificate holds or is unavailable for stated reasons; from bad starts SEBA can fail silently.
- **Layout:** `figure.fig.wide.card`; (a) map: points coloured by SEBA set (unassigned `--c-other`); (b) the r SEBA vectors as sorted bar strips (as in the CIFAR figure: each vector's values over the points sorted by set, maximum 1); side panel: controls and the **certificate box** (rows: η; c; condition √2η < c (met / not met); S.8 bound 2√2η/c or "certificate unavailable"; actual aligned-step error $\|S_{\rm aligned} - H\|_F$; this run's error $\|S_{\rm run} - H\|_F$ after optimal signed permutation; rank of $S_{\rm run}$; unassigned fraction). When the operator is the sparse surrogate, the box adds the chain rows of 3.5 (e_Z, sinΘ bound, η_* bound).
- **Data:** live, `lib/seba.js` (port of `seba_mu`), V = top r eigenvectors of the chosen walk including the constant (Lanczos). Candidate H: normalized indicators of the ground-truth basins (r = 4) or pairs (r = 2) of the samples (quadrants at κ = 0; from `lib/example.js`). Planted mode: N = 30 with exact indicators of sizes (20, 5, 3, 2) and V = HO for a seeded Haar O (S.7's example); `stuck` uses four groups of three with O the normalized 4 × 4 Hadamard matrix with row signs chosen so no column is constant (S.7 (4)).
- **Controls (primary):**
  1. r: 2 | 4;
  2. threshold μ as a multiple of $1/\sqrt N$: slider 0.05-0.99 (default 0.99, the published default);
  3. start: `published` (rotation I on the QR'd eigenvectors) | `aligned` (Procrustes alignment of V to H) | `random` (Haar rotation, seeded);
  4. operator: `dense` (Sinkhorn walk P) | `sparse` ($P_*$ at ε = 0.5, seed 0).
  Advanced: data: `samples` | `planted` | `stuck`; seed; button "200 random starts" (planted mode only: runs 200 seeded Haar starts and reports the number whose output equals the indicators up to signed permutation within 1e-8).
- **What changes:** every control reruns SEBA (and Lanczos when operator or r changes); the certificate box recomputes; data mode swaps the point set (planted modes show points as a 1-D strip grouped by planted set).
- **Stat tiles:** inside the certificate box (above); plus "iterations to convergence".
- **Tours** (default first):
  1. `wells`: samples, r = 4, μ = 0.99/√N, published start, dense. Note: "Four sparse vectors, one per well; the certificate box reports whether the S.8 conditions hold here."
  2. `pairs`: r = 2. Note: "Two vectors: the pairs."
  3. `sparse-chain`: r = 4, operator sparse. Note: "On the sparse surrogate the certificate adds the sparsifier and Davis-Kahan terms."
  4. `stuck`: data stuck, r = 4, published start, μ = 0.5/√N. Note: "An exact indicator span and a valid threshold, yet the start is a fixed point that is not an indicator basis."
  5. `random-starts`: data planted, μ = 0.99/√30, random start (seed 0), with the 200-start count shown. Note: "At the published threshold some random starts fail; the register's own run recovered 43 of 200. Smaller thresholds recovered all."
- **fallbackTour:** `wells`.
- **Caption:** *Plotted:* (a) points coloured by the SEBA set they belong to (largest positive SEBA value; grey if none); (b) the r SEBA vectors, each rescaled to maximum 1, over the points sorted by set; box: residual η of the candidate partition, c, the S.8 bound, and actual errors. *Values:* N = 600, s = 0.25, Sinkhorn walk (or its sparse surrogate at ε = 0.5), r, μ and start as set; candidate H: the basins (or pairs) of the samples. Planted modes: N = 30 (sizes 20, 5, 3, 2) or N = 12 (four groups of three). Running example, face A, or `planted` (synthetic). `synthetic`.
- **Static fallback:** PNG per tour.
- **Accessibility:** alt text: "Points in four clusters coloured by four sparse vectors; bar strips show each vector nonzero on one cluster only; a box lists the certificate quantities." The certificate box is text.
- **Performance:** SEBA at N = 600, r = 4: O(Nr² ) per iteration, typically < 200 iterations, < 30 ms; 200 planted starts < 300 ms. Parity: SEBA labels on fixed inputs match the Python `seba_mu` exactly (SPEC 6.7).

### 5.4 `sparsity-fig-chain` "One chain of bounds from dense graph to sparse sets" (static, rendered by the page module; key `ch`)

- **Purpose:** each arrow from dense walk to sparse sets has a bound and a condition; the composition is valid because everything lives on the same N points.
- **Content:** left to right: "dense walk P" → [S.2: $\|P_* - P\| \le 2\hat\varepsilon/(1+\hat\varepsilon)$] → "sparse walk $P_*$" → [Davis-Kahan, A.21: $\sin\Theta \le e_Z/(\delta_r - e_Z)$ if $e_Z < \delta_r/2$] → "eigenspace V′" → [$\eta_* \le \eta + \sqrt r\sin\Theta$] → "residual η_*" → [S.8: exists aligned S with $\|S - H\| \le 2\sqrt2\eta_*/c$ if $\sqrt2\eta_* < c$] → "sparse sets". Under each arrow, the builder's numbers for r = 2 and r = 4 at ε = 0.5 and 0.3 (`p05.json`, `chain`), with "vacuous" or "unavailable" printed where a condition fails. Below, the shared `bowtie` with left "points (graph vertices)", right "points", both norms "degree one (Sinkhorn)", knot = eigenvalues $\lambda_1..\lambda_8$ of the dense Sinkhorn walk, r = 4, bound label "Z: ≤ 2ε/(1+ε); R: ≤ 2√2η/c (existence)". (SPEC 1.4's page-5 labels.)
- **Caption:** *Plotted:* schematic of the certified chain with the computed value of each bound for the running example; bars are walk eigenvalues. *Values:* N = 600, s = 0.25, Sinkhorn walk; sparsifier by resistance sampling, seed 0; candidate H: basins (r = 4) or pairs (r = 2). Running example, face A.
- **Fallback:** `assets/fallback/sparsity-fig-chain-default.png`.
- **Accessibility:** alt text: "Five boxes joined by arrows, from a dense walk to sparse sets, each arrow labelled with a bound and its value."

### 5.5 `sparsity-fig-cifar` "SEBA on a real network" (static image)

- **Purpose:** what SEBA's readout looks like on a trained network's data-point walk.
- **Data:** the programme's figure `CoherentModes/explore/cifar_coherent/site/assets/fig/seba.png`, copied to `site/assets/fig/sparsity/cifar-seba.png` with a provenance note (`site/assets/fig/sparsity/PROVENANCE.md`: source path, date copied, study description).
- **Content:** as printed: layer block b7-pool at the final checkpoint, r = 3: (1) images in the $(\psi_1, \psi_2)$ plane coloured by set; (2) the three SEBA vectors sorted by set; (3) sets on the study's layout.
- **Caption:** *Plotted:* (1) each probe image at its values of the first two nontrivial eigenfunctions of the layer-block walk, coloured by SEBA set; (2) the three SEBA vectors, each scaled to maximum 1, images sorted by set; (3) sets on the study's display layout (grey: unassigned). *Values:* ResNet-20 on CIFAR-10, 2,000 test images, layer block b7-pool, final checkpoint, r = 3; set sizes as printed. Programme result (CoherentModes ResNet-20/CIFAR-10 study); kNN-union graphs, not sparsifiers; no certificate.
- **Fallback:** the image itself; alt text: "Three panels: a scatter of images in two eigenfunction coordinates coloured into three groups, three sorted bar profiles, and the three groups on a layout."

## 6. Running example on this page

- Face A only, parameters as SPEC 3.2 (κ = 0, D = 0.5). Samples: first 600 of `samples.json` seed 0.
- **Graph (SPEC 3.7):** a **dense Gaussian kernel graph** is the object being sparsified, with kNN truncation as the contrast, because a spectral sparsifier is a statement about thinning a dense graph and a kNN graph (≈ 10 N edges) leaves nothing to thin at n log n/ε² samples.
- Bandwidth: default s = 0.25. The builder checks that (i) the dense graph's two-way sweep separates $x_1 < 0$ from $x_1 > 0$ (≥ 95 %) and (ii) the bottom-4 eigenspace's residual η for the basin partition is reported; if (i) fails at 0.25 the builder tries s ∈ {0.2, 0.3} and records the first that passes in `p05.json` (`config.s`), and the page uses it.
- Precomputed (`tools/build_example.py` → `site/data/sparsity/p05.json`, with config and assertions):
  - `dense`: edge count m; $\mu_1..\mu_{12}$ (normalized Laplacian) and Sinkhorn-walk $\lambda_1..\lambda_{12}$.
  - `sparsifiers`: for methods resistance/weight/knn, ε ∈ {0.5, 0.3}, seeds 0-2: distinct edges kept, estimated and certified ε, max relative change of $\mu_2..\mu_5$, block angles (r = 2, 4) and Davis-Kahan bounds, cut-weight ratios of the pair and well partitions.
  - `crossing`: summed leverage across the between-pair cut and each within-pair cut (assert each ≥ 1 − 1e-9: a check of the code); mean leverage of between-basin edges (split between-pair / within-pair) versus all edges; fraction kept at each ε; cut weights before and after. No assertion on whether crossing edges are kept more or less often than average; the page reports what is computed.
  - `seba`: for r = 2, 4, dense and sparse (ε = 0.5, seed 0): η, c, bound or "unavailable", aligned-step error, published-start run error, labels' matched agreement with basins, unassigned fraction, iterations.
  - `chain`: the numbers printed in `sparsity-fig-chain`.
  - `planted`: SEBA outcomes on the planted example for 200 seeded starts at μ = 0.99/√30 and 0.1, using the Python reference (to compare with the register's 43/200; the page quotes the register's number and may show the builder's alongside, labelled).
  - **Assertions:** every certified ε passes its verified check; every measured ratio in panel (b) lies in $[1-\varepsilon_{\rm cert}, 1+\varepsilon_{\rm cert}]$ (checks the code); the builder's dense generalized eigensolve agrees with the Lanczos estimate to 1e-6 for the stored tours (else the estimate's iteration count is raised); S.2's norm bound holds for $P_*$; every actual angle ≤ its Davis-Kahan bound when the condition holds; the S.8 aligned-step error ≤ its bound when √2η < c; SEBA labels equal the Python reference on fixed inputs. If an assertion fails, stop and amend this spec.
- Live: graphs, resistances, sparsifier sampling, ε̂, eigenpairs, SEBA, certificate box, planted runs.
- Strain: none of note (SPEC 3.7). The page says once that at N = 600 the edge savings are modest and the asymptotic theorem's constant is unknown.
- Companions: the planted examples of register S.7 (exact indicators (20, 5, 3, 2); the Hadamard fixed point), labelled "planted, not the running example".

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E8 | 4 Spectral clustering | `≈` | Every cut weight and Laplacian eigenvalue of page 4's graphs survives sparsification within 1 ± ε; conductances move by at most the degree ratio; eigenvector blocks follow where there is a gap. |
| E9 | 4 Spectral clustering | `≈` | SEBA rotates page 4's eigenspace into sparse indicators; exact from an aligned start in the exact-indicator regime, bounded near it, not guaranteed from arbitrary starts. |
| E10 | 8 Hebbian | `=` | Effective resistance is the graph Laplacian's pseudo-inverse; on page 8 the same Laplacian is a resistor network whose clamped voltages solve the graph Dirichlet problem (harmonic label propagation). |
| E18 | 10 LLMs from inside | `=` | NCS sets are SEBA readouts of Sinkhorn-balanced walks on data points; the sparsifier (Z) and rounding (R) terms of the page-10 budget are this page's bounds, with the register's hypotheses. |

Map card text: "Sparsity · thin the graph, keep every cut; read sparse sets out of an eigenspace · knob: ε and the SEBA threshold μ · bound: (1 ± ε) on every energy; 2√2η/c for an aligned readout (existence)."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The Laplacian quadratic form $x^\top Lx$ of a dense similarity graph (all cuts and energies at once); for a degree-one walk, the walk itself; for SEBA, a leading eigenspace V (constant included). |
| Knob | Sparsifier accuracy ε (edge budget $O(n\log n/\varepsilon^2)$, or $O(n/\varepsilon^2)$ deterministic); SEBA threshold μ; resolution r. |
| Discarded at r | Edges (survivors reweighted), keeping energies but not individual weights; for SEBA, the dense mixing of sets across eigenvectors and the points below threshold (unassigned). |
| Bound | $(1-\varepsilon)L \preceq \tilde L \preceq (1+\varepsilon)L$ w.h.p. with $O(n\log n/\varepsilon^2)$ edges (Spielman & Srivastava 2011), deterministic $(1-\varepsilon)^2L \preceq \tilde L \preceq (1+\varepsilon)^2L$ with $O(n/\varepsilon^2)$ (BSS 2012) — `theorem`; preserves cuts and Laplacian eigenvalues; normalized quantities move by the degree-factor ratio; for a degree-one walk $\|P_* - P\|_2 \le 2\varepsilon/(1+\varepsilon)$, cut/energy factors in $[(1-\varepsilon)/(1+\varepsilon), 1]$ (S.2; `theorem`). kNN truncation: not a sparsifier (`none`). SEBA: exact recovery from an aligned start in the exact-indicator regime (S.7); if $0 < \mu < \min_jn_j^{-1/2}$ and $\sqrt2\eta < c = \min_j(1 - \mu\sqrt{n_j})$, an aligned frame's threshold step has error $\le 2\sqrt2\eta/c$ (S.8); Froyland & Rock 2025 — `conditional`; no guarantee from arbitrary starts. |
| From data | n/a (sparsification is itself a controlled perturbation; its ε is certified after drawing by a verified check of both Loewner inequalities (Rump 2006, Cor. 2.7, including the rounding in forming the test matrices); a Lanczos estimate alone is not a certificate). Sampling of the points is page 4's and page 10's. |
| Running example | From the builder (`p05.json`): dense edge count; edges kept and certified ε at target ε = 0.3, 0.5; max relative error of $\mu_2..\mu_5$; summed leverage across each barrier cut (≥ 1) and mean leverage of crossing edges against all edges; fraction of barrier-crossing edges kept against all edges and the cut weights kept; η, c and the S.8 bound (or "unavailable") at r = 2, 4. |
| Budget line | Z (sparsification), R (rounding). |

## 9. Things not to claim

Spectral sparsification prunes networks safely (it is about undirected nonnegative Laplacians); SEBA recovers the true sets (its guarantees are conditional: aligned start, exact-indicator regime, alignment existence); kNN truncation is a sparsifier or approximately one; a sparsifier preserves individual eigenvectors or edge weights; the Spielman-Srivastava constant is 1 (the widget's q uses an illustrative constant); a successful-looking SEBA output certifies itself (the register's failure case passes the negativity diagnostic); SEBA vectors are features, concepts, or overlapping codes; the CIFAR sets are certified; the browser's 200-start count estimates a probability of success.

## 10. Notation used

Global (SPEC appendix A): r, $\lambda_i$, $\mu_i$, $\delta_r$, P, L, W, ε (sparsifier accuracy), μ (SEBA threshold; shared with page 10 per SPEC appendix A and introduced on the page — a side note warns that $\mu_i$ with an index is a Laplacian eigenvalue and μ without one is the threshold), $x, V, D, \pi$, $w_1..w_4$, L/R, η, c.
Page-local: $\tilde L$ (sparsifier Laplacian), $P_*$ (sparse surrogate walk), $\hat\varepsilon$ (measured accuracy), $R_{xy}$ (effective resistance; not a rotation), $w_e$, $b_e$ (edge weight and incidence vector), q (number of samples), $p_e$ (sampling probability), m (edge count), s (kernel bandwidth), V (eigenspace basis; not the potential V — the page writes the basis in roman bold or says "the basis V" at first use, and the potential is not used on this page except in captions as $V(x_1,x_2)$), R (SEBA rotation; distinct from $R_{xy}$ by its lack of subscripts), S (SEBA output), H (candidate normalized indicator matrix; not the Hankel H — a side note says so), $n_j$ (set sizes), $\eta_*$, $e_Z$, F (feature matrix in the loading bound), Θ. Index shift when quoting CoherentModes (S.2-S.8): say once that the register's $\lambda_1$ is this site's $\lambda_2$.

## 11. Sources

Cite as in SPEC appendix C; status there unless noted.

- Spielman & Srivastava 2011, Theorem 1 [A; theorem statement as recorded in CoherentModes `SPARSITY.md` S.2 proof].
- Batson, Spielman & Srivastava 2012, Theorem 1.1 [P].
- Spielman, D. A. & Teng, S.-H. (2011). Spectral sparsification of graphs. *SIAM J. Comput.* 40(4), 981-1025 (definition's origin; further reading). [M]
- Foster, R. M. (1949). The average impedance of an electrical network. In *Contributions to Applied Mechanics (Reissner Anniversary Volume)*, 333-340. [V; may instead be cited via Spielman & Srivastava 2011]
- Froyland, Rock & Sakellariou 2019, §3, eq. (1), Algorithm 3.1 [P].
- Froyland & Rock 2025, Propositions 3.8, 3.20 [P].
- Davis & Kahan 1970 (via register A.21).
- Stewart, G. W. & Sun, J.-G. (1990). *Matrix Perturbation Theory*, ch. V (as cited in the register for Davis-Kahan/Wedin). [M; optional]
- CoherentModes theorem register (programme source): `SPARSITY.md` S.1-S.2 (`:13-50`), S.5-S.8 (`:119-171`), §5 (`:200-204`), numerical record `:151`; `THEOREMS.md` A.1 (`:72-136`), A.21 (`:570-602`).
- Programme results: CoherentModes ResNet-20/CIFAR-10 study, figure `explore/cifar_coherent/site/assets/fig/seba.png` (copied with provenance).
- Code provenance (not citations): `lib/seba.js` ports `CoherentModes/explore/cifar_baselines/variants.py:261` (`seba_mu`); the original `gfroyland/SEBA` code has no clear licence and is not copied (SPEC 7.1).

## 12. Implementation notes

- Files: `site/content/sparsity.html`, `site/js/p_sparsity.js`, helpers `p_sparsity_hero.js`, `p_sparsity_explorer.js`, `p_sparsity_seba.js`, `p_sparsity_chain.js`; data `site/data/sparsity/p05.json`, `site/data/sparsity/widgets.json`; static image `site/assets/fig/sparsity/cifar-seba.png` + `PROVENANCE.md`.
- Shared modules used: `lib/example.js` (samples, basins, contours), `lib/graph.js`, `lib/seba.js`, `lib/linalg.js` (Cholesky, triangular solves, Lanczos, Procrustes via small SVD), `lib/rng.js` (alias sampling, Haar orthogonal matrices), `lib/bowtie.js`, `charts.js`, `ui.js`.
- `lib/graph.js` must expose (beyond page 4's list): `gaussKernel(X, s, {floor})`, `effectiveResistances(W)` (dense, n ≤ 1000), `sampleSparsifier(W, R, q, rng, {method: "resistance"|"weight"})` → reweighted edge list with multiplicities, `knnTruncate(W, k)`, `measureEps(L, Ltilde)` → `{eps, thetaMin, thetaMax}` (the Lanczos estimate), `certifyEps(W, Wtilde, epsHat)` → `{epsCert, certified, tries}` (5.2's verified test, via `linalg.verifyPD(A, R)`, the shared Rump 2006 Cor. 2.7 routine), `sparseSurrogate(P, eps)`.
- `lib/seba.js` must expose: `seba(V, r, {mu, maxIter, tol, rot0, perturbConstant: true})` → `{S, labels, iterations, rank}`, `alignedStep(V, H, mu)` → `{S, error}`, `residual(V, H)` → η, `matchSigned(S, H)` → error after optimal signed permutation.
- Widget keys and URL state: hero `hr` (`hr_eps`, `hr_seed`, `hr_tour`); sparsifier `sp` (`sp_method`, `sp_eps`, `sp_norm`, `sp_seed`, `sp_s`, `sp_tour`); SEBA `sb` (`sb_r`, `sb_mu`, `sb_start`, `sb_op`, `sb_data`, `sb_seed`, `sb_tour`); chain `ch` (tour `default`).
- Tests: parity of resistances (1e-9 relative), seeded sparsifier edge multisets (exact), ε̂ (1e-8), SEBA labels (exact) against the builder; node test that each tour's tiles match `p05.json`; `verifyPD` returns true for $L + J/n$ of a connected test graph and false for a matrix whose smallest eigenvalue is positive but below Rump's shift (e.g. $L + J/n - (\mu_2 - 10^{-14})I$ for a graph with Fiedler value $\mu_2$), and its shift equals bound I computed independently in the builder.

## 13. Page-specific definition-of-done additions

- [ ] The word "guarantee" next to SEBA always carries its condition (aligned start, exact or near-indicator regime, existence); no sentence says SEBA "recovers" sets without one.
- [ ] The certificate box shows "certificate unavailable" (with the failed condition named) whenever a condition fails; test by setting μ above $\min_jn_j^{-1/2}$.
- [ ] The widget's q formula is labelled "illustrative constant 1" wherever ε targets appear.
- [ ] The register's 43/200 and any browser count are both labelled with their origin.
- [ ] The hero's dense haze and sparse skeleton are legible at 390 px (check the phone screenshot; if not, show a cropped inset of the barrier region).
- [ ] The CIFAR image has its provenance file and the "no certificate" phrase in its caption.

## Change log

- v1 (2026-11-17): first full spec. Uses a dense Gaussian kernel graph instead of SPEC 3.7's kNN graph (reason in section 6); proposes bowtie labels for page 5 (SPEC 1.4 has none).
- v1.1 (2026-11-17): reconciled with SPEC v1.1, which adopts the dense kernel graph (3.7) and this page's bowtie labels (1.4). E10 is now "4/5–8", so this page lists E10 in its header and connections strip (the former pointer sentence in 3.3 becomes the E10 reference). μ, η and c are shared symbols in SPEC appendix A; bibliography requests removed (now in appendix C).
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) Leverage on the dense Gaussian graph: crossing edges have
  tiny weights, so their leverage $w_eR_e$ is small (an independent check: mean ≈ 0.0002 against ≈ 0.006 overall,
  under 0.5 % kept at ε = 0.5), and the claim that they have the largest leverages and survive more often is
  withdrawn. Replaced by a true and stronger statement: the leverages across any cut sum to at least 1 (proof in the
  disclosure), so every bottleneck is sampled about $\ln n/\varepsilon^2$ times and keeps its cut weight through a few
  heavily reweighted survivors; heading of 3.3, hero fig-sub, skim test, callout, C5.12/C5.12a, panel (a), tiles, tour
  notes and builder statistics follow, with no direction asserted for the per-edge comparison. (2) Measured ε: a
  Lanczos estimate is now labelled an estimate (it can understate ε); the certificate is a verified Cholesky check of
  both Loewner inequalities at a stated $\varepsilon_{\rm cert}$ (Rump 2006), used in the certified chain and the
  ledger (C5.8). Reviewer findings: math-1-6 4, 9.
- v1.3 (2026-11-17): round-2 review fixes (SPEC v1.3). (1) Certified ε: the v1.2 check (ordinary Cholesky after
  subtracting $\tau = 10\,n\,u\,\|L\|_1$, "as in Rump 2006") was not Rump's criterion (his shift scales with
  $\gamma_{n+1}\mathrm{tr}(A)$ and was several times larger on test graphs) and ignored the rounding in forming the
  test matrices. Replaced in 5.2 by a faithful implementation of Rump 2006, Corollary 2.7 with bound I: the two test
  matrices $T_\pm$ formed in floating point, an entrywise formation radius R and $r \ge \|R\|_2$, Rump's shift, the
  diagonal lowered by his rounding-to-nearest recipe (2.11), and a plain Cholesky; JavaScript's binary64 arithmetic
  meets the paper's model, so the word "certified" stays (3.2 bullet, C5.8, ledger, `certifyEps` and
  `linalg.verifyPD`, tests). Page 10's $e_Z$ and verified $e_P$ use the same routine. (2) Bridges: not "always kept"
  under independent sampling with replacement (missed with probability $(1 - 1/(n-1))^q > 0$); they get the maximum
  leverage, are kept with high probability at the stated budget, and every successful sparsifier with ε < 1 must
  contain every bridge (reader outcome 2, skim test, 3.3 bullet and callout, C5.12). Reviewer findings: round 2,
  items 5 and 9.
