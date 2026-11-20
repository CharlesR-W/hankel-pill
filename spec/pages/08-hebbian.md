# Page spec 08: Hebbian learning on a resistor network

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 8 |
| id (hash, file stem) | `hebbian` |
| tab label | Hebbian |
| kicker | Page 8 · synaptic plasticity |
| title | Hebbian learning on a resistor network |
| lede (one-sentence claim, ≤ 45 words) | On a resistor network, Hebb's rule with a pruning threshold groups neurons into clusters that are nonnegative eigenvectors of principal submatrices of the threshold-shifted input covariance; each neuron's harmonic embedding, computed from the weights alone, is the coordinate in which to read them. |
| depends on | 4 (spectral clustering), 7 (neurons); every idea is glossed on the page |
| edges (SPEC 2.2) | E10, E15, E23 |
| faces of the running example | A, through place-field features of the particle's position (instantaneous and time-filtered) |
| main-path words | 2,200-2,700 |
| spec status | v1.2, 2026-11-17 (E15 re-marked `~` after round-1 review; first full spec checked numerically at spec time, see section 6) |

**Scope decision (binding on the writer).** The page has one rule on its main path, Hebb's covariance rule with a
pruning threshold on a linear resistor network ("the threshold rule"; HebbianHarmonics' v1). A second rule, the
energy/distance rule (HebbianHarmonics' v2, "the distance rule"), appears in two places only: as the setting of the
readout demonstration (section 3.5), where it has the clean exact result, and as the different learning principle of
section 3.6. The page never presents the distance rule as the threshold rule's nonlinear extension (SPEC appendix D).
Guided path: one circuit (three inputs), one refinement example (the running example), one readout demonstration.
Everything else is optional depth in disclosures.

## 1. Reader outcome

After this page the reader can:

1. Compute a neuron's harmonic embedding from the conductances ($\mathcal H = L_{II}^{-1}W_{IB}$), explain why its
   rows are probability vectors (hitting probabilities of a random walk), and recognize it as harmonic label
   propagation.
2. State the threshold rule and show that it depends on the inputs only through the shifted covariance
   $Q = \Sigma_g - \theta\mathbf 1\mathbf 1^\top$.
3. Predict which clusters ("parts") can exist at a threshold: nonnegative eigenvectors of principal submatrices of Q,
   with a stability test; tell a part from a covariance eigenvector.
4. Explain how a slow synaptic trace reweights the covariance mode by mode ($1/(1+\nu_i\tau_s)$), and use it to predict
   that the running example's parts are wells without a trace and pairs, then wells, with one.
5. Show by example that which parts receive neurons, and how the network refines as the threshold rises, depends on
   its history.
6. Say what the weights do and do not reveal about the inputs: for the threshold rule, a sketch of the populated
   parts; for the distance rule with linear neurons, the contrast second moment exactly under a spanning condition;
   never the common mode; never the input distribution.

What they see: neurons drawn at the barycentres of their place fields gathering on the four wells; with a slow trace
the same network gathering on the two pairs; a network that learned the pairs first ending, after the threshold is
raised, with one well per pair while a fresh network finds all four; a triangle where clusters sit at corners and
edge midpoints but never at the signed eigenvector; a 16 × 16 matrix read back from the weights, exact just above
percolation, destroyed by 1% weight noise when the network is fused.

## 2. Skim path

1. Lede (header).
2. Hero figure `hebbian-fig-hero`: "Place fields on four wells, and what Hebb's rule makes of them". Fig-sub:
   *Sixteen place fields tile the four wells; under a thresholded Hebb rule the network's neurons gather on the fields
   of one well each, and, with a slow synaptic trace, on the fields of one pair.*
3. Section headings (verbatim, these are the claims):
   - "Kirchhoff's laws give every neuron a harmonic embedding"
   - "Thresholded Hebb clusters are nonnegative eigenvectors of covariance submatrices"
   - "Threshold and synaptic trace decide which parts exist"
   - "Which parts get neurons depends on the network's history"
   - "The weights record second moments, never the input distribution"
   - "Nonlinear neurons change the rule; the Koopman reading is open"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `hebbian-fig-kirchhoff`, `hebbian-fig-circuit`, `hebbian-fig-parts`,
   `hebbian-fig-readout`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: a resistor network gives each neuron a probability
vector over its inputs, computable from the weights; the thresholded Hebb rule's clusters are nonnegative eigenvectors
of submatrices of the shifted covariance, not covariance eigenvectors; the threshold (and a trace) decide which
parts exist, and in the running example these are wells, or pairs with a trace; history decides which parts get
neurons and how refinement goes; the weights give back second moments under conditions and never the input
distribution; the nonlinear rule is a different principle, and its link to Koopman operators is open.

## 3. Section outline

Section ids are `hebbian-<slug>`; figure ids are `hebbian-fig-<slug>` (SPEC 6.5). Word counts are main-path prose
only.

Placement summary: hero between the lede and 3.1; `hebbian-fig-kirchhoff` in 3.1; `hebbian-fig-circuit` in 3.2;
`hebbian-fig-parts` in 3.3; the hero's tours are linked from 3.3 and 3.4; `hebbian-fig-readout` in 3.5. No bowtie
on this page (section 13 explains).

### 3.1 `hebbian-embedding` "Kirchhoff's laws give every neuron a harmonic embedding" (≈ 400 words)

Placement: the hero sits between the lede and this heading; the "Arriving here first?" aside opens this section;
`hebbian-fig-kirchhoff` after the second bullet.

- "Arriving here first?" aside (≤ 80 words): spectral clustering finds groups by the leading eigenvectors of a
  similarity matrix and rounds them to sets (page 4); a coherent set is a region the dynamics keeps together (pages 3,
  7). This page asks what a local learning rule computes instead, and how far that is from either. Links `#cuts`,
  `#neurons`.
- The model (from the HebbianHarmonics project; say so): neurons are nodes of a resistor network, synapses symmetric
  conductances $w_{ij} \ge 0$; B input nodes are clamped to the stimulus g; the N interior nodes settle where
  Kirchhoff's current law puts them. Displayed equation 1: $u = \mathcal H g$, $\mathcal H = L_{II}^{-1}W_{IB}$, with
  $L_{II}$ the interior block of the graph Laplacian (lateral and input conductances on its diagonal) and $W_{IB}$ the
  interior-to-input conductances.
- Row $h_i$ of $\mathcal H$ is neuron i's **harmonic embedding**: nonnegative, summing to one (a constant input gives a
  constant voltage), provided every interior component is connected to an input. It is the probability that a random
  walk started at neuron i, stepping along edges with probability proportional to conductance, first reaches each
  input (Doyle & Snell 1984). Show `hebbian-fig-kirchhoff`.
- The same equation is harmonic label propagation (Zhu, Ghahramani & Lafferty 2003) with the inputs as labelled nodes:
  edge E10. The Laplacian's pseudo-inverse also gives effective resistance (page 5 uses it to sparsify).
- Why it is the natural coordinate: every voltage is a fixed linear function of the input, $u_i = h_i^\top g$, so
  $\mathrm{Cov}(u_i, u_j) = h_i^\top\Sigma_g h_j$ (displayed equation 2), and every quantity the rule below sees is an
  inner product of embeddings. $\mathcal H$ is computed from the weights alone: reading a neuron needs no data. In the
  running example, where inputs are place fields, $h_i$ is a receptive field over positions (hero, hover).

Key callout: "A neuron's harmonic embedding is a probability vector over the inputs, computed from the weights alone.
Every covariance the rule sees is an inner product of embeddings."

Disclosures:
- "The maths: Dirichlet problem, hitting probabilities, effective resistance" (≤ 450 words): the interior voltages
  minimize the network energy with inputs fixed; the minimizer is harmonic (each voltage the conductance-weighted
  average of its neighbours'); $h_{ib}$ as hitting probabilities; effective resistance $R_{\rm eff}(i,j) = (e_i -
  e_j)^\top L^+ (e_i - e_j)$ from the same Laplacian (page 5); Stock et al. (2022) analyse a plasticity rule (synaptic
  balancing, a regulatory rule, not Hebbian) through this Laplacian and effective resistance. HebbianHarmonics' note calls $\mathcal H$ "the Kron
  reduction"; strictly, Kron reduction is the boundary Schur complement and $\mathcal H$ is the Dirichlet extension map
  obtained from the same block solve.
- "In other fields: conductance" (≤ 150 words): electrical conductance of an edge here vs conductance of a cut in
  graph theory (page 4); glossary link.

### 3.2 `hebbian-parts` "Thresholded Hebb clusters are nonnegative eigenvectors of covariance submatrices" (≈ 480 words)

Placement: `hebbian-fig-circuit` after the third bullet.

- The threshold rule (displayed equation 3), in units where the decay and learning rates are 1: lateral synapses
  $\dot w_{ij} = \gamma\,h_i^\top\Sigma_g h_j - \theta - w_{ij}$, input synapses $\dot w_{ib} = (\mathcal H\Sigma_g)_{ib}
  - \theta - w_{ib}$, all clipped at a small floor $w_{\min}$. θ is a constant pruning drift (a synapse grows only where
  its two ends covary by more than θ); γ is the lateral gain.
- Because every embedding sums to one, adding a constant to every entry of $\Sigma_g$ is the same as adding it to θ: the
  rule sees only the **shifted covariance** (displayed equation 4) $Q = \Sigma_g - \theta\mathbf 1\mathbf 1^\top$.
  Pruning by θ and pruning by negative covariance are one mechanism.
- The part equation (displayed equation 5; HebbianHarmonics findings F1, derived and independently checked): if a
  cluster's members share one embedding h with support S, their mutual synapses carry no current; with synapses to
  other clusters at the floor and the floor negligible, Kirchhoff and the fixed point of the input synapses give
  $Q_{SS}h_S = c\,h_S$, $h_S > 0$, $c > 0$, $(Qh)_b \le 0$ for $b \notin S$, with c a member's summed input
  conductance. **A cluster is a nonnegative eigenvector of a principal submatrix of Q: a part.** N, γ and the lateral
  weights drop out. Stability (sufficient, not necessary): c strictly the top eigenvalue of $Q_{SS}$ and the
  off-support inequality strict.
- Three consequences, stated plainly: θ below every covariance gives one part (the Perron vector of an entrywise
  positive Q); for uniform blocks (correlation ρ within, ρ′ across) block parts are stable exactly when ρ′ < θ < ρ, so
  the rule is exact correlation clustering there; input b alone is a part iff $\Sigma_{bb} > \theta$ and
  $\Sigma_{ab} \le \theta$ for every other a.
- Show `hebbian-fig-circuit` (three inputs; every embedding a point in a triangle). Tours: `neutral-identity` (no
  pruning: one cluster), `three-corners` (pruning: one cluster per corner), `edge-midpoint` (a correlated pair: a
  cluster at the midpoint, none at the signed eigenvector $(1,-1,0)/\sqrt2$), `midpoint-splits` (θ above the
  correlation: corners, which are not eigenvectors of this $\Sigma_g$).
- Parts versus eigenvectors (edge E15, a schematic link: section 8 hook on the comparison, each rule's result stated exactly): Oja's rule converges to the top eigenvector of the input covariance, and
  similarity-matching networks to principal subspaces; those are signed. Parts are nonnegative and localized; in
  tested families they lie in the span of the top eigenvectors but are its nonnegative rotation, and each is close to
  the Perron vector of $\Sigma_{SS}$ itself (it is exactly that of $Q_{SS}$). The running example's version is in
  `hebbian-fig-parts` (3.3).
- One sentence for E23 (with the section 8 hook): both this rule and spectral clustering threshold a spectral
  computation on a similarity matrix; no theorem says the rule finds a chosen Laplacian partition.

Key callout: "A thresholded Hebbian cluster is the top, entrywise-positive eigenvector of Q restricted to its support.
The threshold, not the spectrum of $\Sigma_g$, decides how large the supports are."

Disclosures:
- "Why this holds: the part equation and its stability" (≤ 600 words): equipotential members, zero lateral current;
  $h_b \propto w_{ib}$ from Kirchhoff; fixed point of input synapses gives $h \propto (Qh)_+$; lone-neuron
  linearization with rates $-1$ and $q/c - 1$ for each other eigenvalue q of $Q_{SS}$; the stability test is
  sufficient, not necessary (example $\Sigma_g = \mathrm{diag}(2,1)$, θ = 0: the dominant vertex is stable with zero
  off-support margin); a finite floor adds $O(\omega/c)$ coupling, $\omega = N w_{\min}$. Source: HebbianHarmonics
  `docs/v1/findings.md` F1, corrected by `docs/v1/review_corrections.md` items 3 and 6; `site/content/old.html`.
- "Worked cases on three inputs" (≤ 300 words): independent unit inputs (on a support of size k the uniform vector has
  eigenvalue 1 − kθ, the others 1, so only corners are stable for 0 < θ < 1); a correlated pair (midpoint stable iff
  θ < ρ₁₂). From `old.html`.
- "Optional depth: what else the archived experiments found" (≤ 400 words): on a ring of 16 inputs, parts are
  localized bumps whose width shrinks from 10 inputs to 1 as θ rises from 0.07 to 0.85, while eigenvectors are Fourier
  modes (best cosine 0.76 → 0.46); with dense synapses cluster members are exact clones in every tested condition (so a
  cluster is not a reservoir of distinct features); a rectified-rate variant prefers heavy-tailed projections on MNIST
  pixels (projection pursuit) without coding better. All are the HebbianHarmonics project's archived results
  (`docs/v1/findings.md` F1, F7; `docs/v1/nonlin.md`), described as such.

### 3.3 `hebbian-trace` "Threshold and synaptic trace decide which parts exist" (≈ 450 words)

Placement: `hebbian-fig-parts` after the second bullet; links to hero tours `wells` and `pairs` in the third and
fifth bullets.

- The running example as inputs: sixteen place fields $g_b(x)$, Gaussian bumps on a 4 × 4 grid over Ω, four around
  each well (section 6 gives centres and widths), applied to the particle's position; inputs are the fields' centred
  values, scaled to mean variance 1. Within a well the fields covary positively; fields in different wells are
  negatively correlated, because the particle is in one well at a time.
- Without a trace (τ_s = 0): the static covariance sees wells. Exact enumeration of parts (builder) gives one part
  below a threshold, the four wells over a range of θ, and pieces of wells above it ("detail inside a well"). The
  fields of the two wells of a pair are as anti-correlated as fields of different pairs, so **no pair-level part
  exists** (SPEC 3.7 strain). Show `hebbian-fig-parts`, row τ_s = 0, and hero tour `wells`.
- The trace (a modelling choice of this site, labelled as such; HebbianHarmonics names lagged statistics as an untried
  direction, `site/content/method.html:40`): let the rule see inputs low-pass filtered over a time $\tau_s$ (a slow
  synaptic or eligibility trace, in the spirit of Földiák's 1991 trace rule). For a reversible process with relaxation
  rates $\nu_i$ and eigenfunctions $\phi_i$ (SPEC 3.2), the covariance the rule then sees is (displayed equation 6)
  $\Sigma_g(\tau_s) = \sum_{i \ge 2} \frac{a_i a_i^\top}{1 + \nu_i\tau_s}$, $a_{ib} = \langle \tilde g_b,
  \phi_i\rangle_\pi$: each mode of the input is weighted by $1/(1+\nu_i\tau_s)$, which plays the role the factor
  $e^{-\nu_i\tau}$ plays for a lag on page 3. Slow modes keep their weight; fast ones are suppressed.
- At $\tau_s = 8$ the pair mode keeps most of its weight and the within-pair modes about a quarter (builder values from
  $\nu_2, \nu_3$; spec-time ≈ 0.82 and 0.27), so fields of the two wells of a pair become positively correlated: a
  low threshold now gives **the two pairs as parts**, a higher one the four wells, a higher one pieces of wells
  (`hebbian-fig-parts` ladder; hero tour `pairs`). The pair level appears only once $\tau_s$ is comparable to the
  within-pair hopping time (builder: first $\tau_s$ in the grid with a pair level).
- The general statement, carefully: θ decides how large supports can be and $\tau_s$ decides which correlations are
  positive; together they set which parts exist. In this example the existing parts nest (one ⊃ pairs ⊃ wells ⊃
  pieces): a builder check, not a theorem. Uniform-block exactness (3.2) does not apply here; the page uses exact
  enumeration.

Key callout: "Without a trace the running example's parts are wells. A slow trace weights each input mode by
$1/(1+\nu\tau_s)$, makes the two wells of a pair covary, and adds the pairs as parts at a lower threshold."

Disclosures:
- "The maths: what a trace does to the covariance" (≤ 500 words): $\bar g(t) = \int_0^\infty \tau_s^{-1}e^{-s/\tau_s}
  g(x_{t-s})\,ds$; with the eigen-expansion of the lagged covariance, $\mathrm{Cov}(g_b(x_0), g_c(x_t)) = \sum_i
  a_{ib}a_{ic}e^{-\nu_i|t|}$, both a one-sided trace ($\mathrm{Cov}(\bar g_b, g_c)$) and a two-sided one
  ($\mathrm{Cov}(\bar g_b, \bar g_c)$; the difference of two independent exponential delays is Laplace distributed)
  give the weights $1/(1+\nu_i\tau_s)$. Equivalently $\Sigma_g(\tau_s)_{bc} = \langle \tilde g_b, (I -
  \tau_s\mathcal L)^{-1}\tilde g_c\rangle_\pi$: the generator's resolvent, which is the exponential average
  $\int_0^\infty \tau_s^{-1}e^{-t/\tau_s}\mathcal K_t\,dt$ of the Koopman operators (Laplace transform of the semigroup;
  standard, e.g. Engel & Nagel 2000), sandwiched between the centred place fields. It is the lagged cross-covariance
  $\Sigma_\tau$ of page 7's Galerkin construction with the lag averaged exponentially and without the whitening by
  $\Sigma_0$. So with a trace, the threshold rule computes nonnegative principal-submatrix eigenvectors of a
  lag-averaged Koopman cross-covariance minus θ: the same raw material page 7's neuron whitens and
  decomposes, processed differently (no whitening, a threshold, nonnegativity).
- "Hypotheses: why the trace is a modelling choice" (≤ 200 words): the threshold rule as specified uses equal-time
  covariances; a trace changes the inputs (or the plasticity signal), not Kirchhoff; reversibility is used for the
  symmetric eigen-expansion; the place-field layout is the site's choice.

### 3.4 `hebbian-history` "Which parts get neurons depends on the network's history" (≈ 420 words)

Placement: no new figure; links to hero tours `fresh-fine` and `refine`, and to circuit tours.

- Existence is not occupancy. The part equation does not contain the number of members, so for mutually compatible,
  disconnected parts any split of the neurons among them is a fixed point (zero-floor limit; a finite floor couples the
  clusters weakly, $O(\omega/c)$). Allocation is inherited from the transient: circuit tours `three-corners` and its
  seed-1 twin converge to different splits (40/30/20 versus 35/31/24).
- Lateral binding: from a random start, lateral synapses grow first if $\gamma\,h_i^\top\Sigma_g h_j > \theta$ for
  typical starting embeddings, whose mean covariance is $\kappa_0 = \mathbf 1^\top\Sigma_g\mathbf 1/B^2$; a bound
  population behaves like one neuron and lands on one part (circuit tour `corners-collective`). The crossover
  $\theta \approx \gamma\kappa_0$ is a heuristic read off the initial drift, numerically supported in the
  HebbianHarmonics sweeps (transitions predicted to within 0.03-0.08), not a derived phase boundary. In the running
  example $\kappa_0$ is close to 0 (builder value), so at positive θ neurons choose independently.
- The refinement example (hero, $\tau_s = 8$): tour `fresh-fine`, a fresh network at the wells threshold, populates all
  four wells. Tour `refine`: the same network first trained at the pairs threshold (two pair clusters), then the
  threshold raised to the same value: each pair cluster, held together by its lateral synapses while $\gamma
  E_{\rm pair} > \theta$ (E the part's self-covariance $h^\top\Sigma_g h$; builder value), moves as one body to **one**
  of its two wells. Same parameters, two outcomes: one well per pair against four wells. Quote the outcomes the
  page's test records for seeds 0-2.
- Say what is and is not known: the threshold sets which parts exist (derived); whether refinement as θ rises splits
  a cluster depends on lateral binding and history (shown by example; a heuristic predicts when). With lateral
  plasticity, a laterally bound population never split as θ rose in the HebbianHarmonics hysteresis loops, while a
  fresh start at the same θ found the finer parts (archived result, F8). There is no approximation bound for
  allocation or refinement order (ledger: `none`).

Key callout: "The threshold decides which parts exist; history decides which of them get neurons. Raise the threshold
on a network that learned the pairs and it keeps one well per pair; start fresh and it finds all four."

Disclosures:
- "Why this holds: allocation is not an equilibrium property" (≤ 350 words): the part equation has no $n_k$; the floor
  term $h_k(|w_{kB}| + w_{\min}(N-n_k)) = \dots$ is the only coupling (F4); a lone neuron runs continuous nonnegative
  power iteration on Q from its initial weights (zero floor), so where it ends depends on where it starts; fitted
  allocation laws $n_k \propto \lambda_k^\beta$ in the archived sweeps are fits, not laws (review item 7).
- "Hypotheses: the refinement tour" (≤ 200 words): mean-field (exact $\Sigma_g(\tau_s)$), dense lateral masks, the
  symmetry-breaking perturbation applied at the threshold change (section 5.1), minimum stage duration; why a small
  residual does not certify stability (an exactly symmetric unstable state can persist, F8).

### 3.5 `hebbian-readout` "The weights record second moments, never the input distribution" (≈ 480 words)

Centrepiece: `hebbian-fig-readout`, after the third bullet.

- The idea (HebbianHarmonics' note): compute $\mathcal H$ from the weights, then read the fixed-point condition of each
  live synapse as an equation for the input statistics. Given $\mathcal H$, these equations are linear in the input
  second moment. What they determine depends on which synapses are alive and on the rule.
- Under the threshold rule at a clustered fixed point, each active input synapse states $(\Sigma_g h_k)_b = \theta +
  c_k h_{kb}$ on part k's support, and lateral synapses add only each populated part's energy; clones multiply
  equations, not their rank. **The weights determine the populated parts and their conductances: a sketch, not
  $\Sigma_g$** (a parts-sum estimator has rank at most K + 1 for K parts). Readout tour `threshold` shows the rank of
  what the weights measure on the running example.
- The clean case is a different rule (introduce it in three sentences, flagged as different): the distance rule,
  $\dot w_{ij} = \zeta - \alpha w_{ij} - \tfrac12\mathcal D_{ij}^2$ with $\mathcal D_{ij}^2$ the mean squared difference
  of the two neurons' responses, which is exact gradient descent on the network's averaged equilibrium energy plus a
  weight cost (HebbianHarmonics, envelope theorem; section 3.6). At its fixed point every live edge records one
  distance exactly; with linear neurons, $\mathcal D_{ij}^2 = \mathbf d_{ij}^\top\hat C\,\mathbf d_{ij}$ with
  $\mathbf d_{ij} = h_i - h_j$, so each live edge is one linear equation (displayed equation 7): $\mathbf
  d_{ij}^\top\hat C\,\mathbf d_{ij} = 2(\zeta - \alpha w_{ij})$.
- Because rows of $\mathcal H$ sum to one, every $\mathbf d_{ij}$ is a contrast ($\mathbf d^\top\mathbf 1 = 0$), so
  (displayed equation 8) $\hat C$ and $\hat C + \mathbf 1a^\top + a\mathbf 1^\top$ give identical measurements for
  every a: **the common mode is invisible**. The target is the contrast part $P_\perp\hat CP_\perp$, $P_\perp = I -
  \mathbf 1\mathbf 1^\top/B$, and it is determined exactly when the live-edge outer products span the symmetric
  contrast matrices (dimension $B(B-1)/2$ = 120 for the running example's 16 inputs).
- Show the readout widget: tour `sweet` (just above percolation: full rank, exact, survives 1% weight noise), `few`
  (too few live edges: rank-deficient, no better than a scaled identity), `fragile` (fully fused: exact without noise,
  destroyed by 1% noise; the noise gain $2\alpha w/\mathcal D^2$ explains why), `threshold` (the threshold rule's
  sketch).
- Not the distribution: two stimuli mixed with weights p and 1 − p have centred feature covariance
  $p(1-p)\,(g(x)-g(y))(g(x)-g(y))^\top$, the same for p and 1 − p, and the atoms' locations are lost with the mean. In
  the running example this means: from the weights one can read how place fields co-vary, not where the particle spends
  its time. A non-centred feature lift could expose a mean embedding; whether the contrast-only readout keeps that was
  not examined (HebbianHarmonics `readout.html`).

Key callout: "Given the weights, compute the embeddings; each live synapse is then a linear equation in the input
second moment. For linear neurons under the distance rule this pins down the contrast second moment when enough
synapses are alive; nothing pins down the input distribution."

Disclosures:
- "The maths: the measurement operator and three errors" (≤ 500 words): contrast basis, measurement operator
  $Y \mapsto (c_e^\top Y c_e)_e$, rank and conditioning; masked ridge least squares with a tiny ridge; PSD projection;
  three separate errors (fixed-point error = 2 max |dw/dt| on live edges; sampling error $\lVert P_\perp\hat CP_\perp
  - P_\perp\Sigma_gP_\perp\rVert/\lVert P_\perp\Sigma_gP_\perp\rVert$, which no readout removes; inverse-problem error
  on the identifiable subspace). From HebbianHarmonics `site/content/readout.html`.
- "Optional depth: leaks and the common mode" (≤ 300 words): a quadratic leak proportional to each neuron's input
  conductance keeps $\mathbf d^\top\mathbf 1 = 0$; only a heterogeneous leak can expose the common mode, which is
  necessary, not sufficient (four neurons with identical attachments and different leaks measure one combination);
  the tested networks reached full rank, fragilely (archived sweep).
- "The maths: what the threshold rule's weights measure" (≤ 300 words): F10 identifiability, the parts-sum estimator
  $\theta\mathbf 1\mathbf 1^\top + \sum_k c_k h_kh_k^\top/\lVert h_k\rVert^2$, rank at most K + 1, and that the archived
  scores are of a readout given the true θ (review item 10).

### 3.6 `hebbian-nonlinear` "Nonlinear neurons change the rule; the Koopman reading is open" (≈ 380 words)

No figure.

- With an on-site potential $\mathcal V_i(u_i)$ (convex) per neuron, each neuron's equilibrium voltage becomes a
  nonlinear response function $F_i(g)$; its transfer function is the inverse of $d_i u + \mathcal V_i'(u)$
  (HebbianHarmonics `idea.html`). The harmonic embedding generalizes to the whole function $F_i$, compared in the
  geometry $\mathcal D_{ij}^2 = \mathbb E_g[(F_i - F_j)^2]$.
- The distance rule is a different learning principle, not the threshold rule with a nonlinearity: expanding,
  $-\tfrac12\mathcal D_{ij}^2 = \mathbb E[F_iF_j] - \tfrac12\mathbb E[F_i^2] - \tfrac12\mathbb E[F_j^2]$, coactivity
  minus both neurons' activity power; neurons are drawn together by being alike, not by being loud. It is exactly
  gradient descent on one objective (averaged equilibrium energy plus a weight cost), with fixed point $w_{ij} = (\zeta -
  \mathcal D_{ij}^2/2)_+/\alpha$. The objective is not convex, and outcomes depend on history.
- What it does (HebbianHarmonics, current site, described as the project's results): clusters are connected components
  of live edges, which can be chains wider than one edge's range; with random multi-input attachments no range of ζ
  held a stable count of a few clusters; for nonlinear neurons the weights give only a partial table of response
  distances (exact on live edges, bounded elsewhere), not a covariance.
- "Eigenfunctions of some sort", made precise where possible: the population's centred responses define an operator
  $f \mapsto \sum_i \tilde F_i\langle\tilde F_i, f\rangle$ on functions of the input; for linear neurons its
  eigenfunctions are input modes if and only if $\mathcal H^\top\mathcal H$ commutes with $\Sigma_g$ (derived in the
  project's diversity chapter). For nonlinear neurons nothing comparable is known.
- The Koopman reading (with the section 8 hook): with a trace, the threshold rule already works on a lag-averaged
  Koopman cross-covariance (3.3 disclosure). Whether a traced or lagged distance rule on nonlinear neurons computes something
  like Koopman eigenfunctions of the stimulus dynamics is **open**: no derivation or experiment exists. State it as an
  open question.
- Keep three nonlinear stories apart (disclosure): (i) on-site potentials change the equilibrium (distance rule);
  (ii) rectified rates in plasticity with linear Kirchhoff (a threshold-rule variant: Gaussian inputs add nothing
  beyond $\Sigma_g$; non-Gaussian inputs give projection pursuit); (iii) random output stages added outside the
  energy (a hand-made reservoir illustration, not a learned result).

Key callout: "With nonlinear neurons the rule compares whole response functions and the weights keep only a partial
distance table. Whether such a network computes Koopman-like eigenfunctions of its inputs is an open question."

Disclosures:
- "Three nonlinear stories, kept apart" (≤ 400 words): as in the last bullet, with sources (`docs/v1/nonlin.md`;
  `site/content/diversity.html:88-99`; review item 2: with rectified output the identifiable set must be assessed by
  the local Jacobian rank and can be larger).
- "Optional depth: the distance rule's fusion and resolution" (≤ 350 words): two-neuron bistability in closed form,
  $\mathcal D^2(w) = \mathcal D_0^2/(1+2w)^2$; onset of an isolated planted pair from W = 0 iff δ < $\sqrt{2\zeta/
  \hat\lambda_a}$ (a frozen-onset law, not a clustering theorem). From `docs/findings_v2.md` and `fusion.html`, as the
  project's results.

### 3.7 `hebbian-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.8 `hebbian-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.9 `hebbian-sources` Sources

Section 11 of this spec.

## 4. Claims in order

Support types follow the template; "theorem (programme derivation)" marks results derived in the HebbianHarmonics
project and independently checked there (`docs/v1/review_corrections.md`), described on the page as the project's
results (SPEC 5.5); "empirical (programme)" marks the project's numerical findings (both are in the template's
list, amended 17 Nov 2026).

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C8.1 | Interior voltages are $u = \mathcal Hg$, $\mathcal H = L_{II}^{-1}W_{IB}$; rows are nonnegative and sum to one. | construction + standard | 3.1; `hebbian-fig-kirchhoff` | every interior component connected to an input; nonnegative symmetric conductances | 3.1 |
| C8.2 | $h_{ib}$ is the probability that a conductance-weighted random walk from i first hits input b. | standard | Doyle & Snell 1984; Kirchhoff figure hover | as C8.1 | 3.1 |
| C8.3 | The same equation is harmonic label propagation with the inputs as labelled nodes; effective resistance comes from the same Laplacian. | theorem (identity) | Zhu, Ghahramani & Lafferty 2003; E10 | — | 3.1 |
| C8.4 | $\mathrm{Cov}(u) = \mathcal H\Sigma_g\mathcal H^\top$, so the rule sees only inner products of embeddings. | construction | equation 2 | linear Kirchhoff; instantaneous settling | 3.1 |
| C8.5 | Because rows sum to one, $(\Sigma_g, \theta)$ and $(\Sigma_g + s\mathbf 1\mathbf 1^\top, \theta + s)$ give identical dynamics (γ = 1): the rule sees only $Q = \Sigma_g - \theta\mathbf 1\mathbf 1^\top$. | construction | 3.2; HH `old.html`, findings F0 | γ = 1 for the exact identity (lateral threshold θ/γ otherwise) | 3.2 |
| C8.6 | A cluster sharing embedding h with support S satisfies $Q_{SS}h_S = ch_S$, $h_S > 0$, $c > 0$, $(Qh)_b \le 0$ off S; c is a member's summed input conductance; N, γ and lateral weights drop out. | theorem (programme derivation) | HH findings F1; review items 3, 6; disclosure | members share h; inter-cluster synapses at the floor; zero-floor limit (finite floor: $O(\omega/c)$ corrections) | 3.2 |
| C8.7 | Strict top eigenvalue c of $Q_{SS}$ and strict off-support margin imply stability; not necessary. | theorem (programme derivation) | F1; review item 3 counterexample | lone-neuron linearization | 3.2 |
| C8.8 | θ below every covariance gives exactly one part; uniform blocks: block parts stable iff ρ′ < θ < ρ; input b is a part iff $\Sigma_{bb} > \theta$ and $\Sigma_{ab} \le \theta$ for all a ≠ b. | theorem (programme derivation) | F1 corollaries 1, 4; review item 3 | uniform blocks for the middle statement | 3.2 |
| C8.9 | On three inputs, clusters sit at corners and edge midpoints; the signed eigenvector of a correlated pair has no cluster; above ρ₁₂ the corners, not eigenvectors, are populated. | widget | `hebbian-fig-circuit` tours `edge-midpoint`, `midpoint-splits`, `three-corners`, `neutral-identity` | tour parameters as listed | 3.2 |
| C8.10 | Oja's rule converges to the top covariance eigenvector and similarity-matching networks to principal subspaces (signed); threshold-rule parts are nonnegative, localized, in the span of the top eigenvectors (with the constant), approximately the Perron vector of $\Sigma_{SS}$. | theorem (Oja; Pehlevan et al.) + builder values | Oja 1982; Pehlevan, Hu & Chklovskii 2015; `hebbian-fig-parts` panel (a) cosines | Oja: stationary inputs, small learning rate; parts: builder-computed cosines for this example | 3.2 |
| C8.11 | Hebbian clustering and spectral clustering are both thresholded spectral computations on a similarity matrix; no theorem relates the partitions. | motivation (section 8 hook) | E23; HH `method.html:13` | — | 3.2 |
| C8.12 | Running example, no trace: parts are one (low θ), the four wells (a θ range), then pieces of wells; no pair-level part exists. | builder values (exact enumeration) | `hebbian-fig-parts` ladder, row τ_s = 0; hero tour `wells` | place-field layout of section 6; mean variance scaled to 1 | 3.3 |
| C8.13 | With a trace, $\Sigma_g(\tau_s) = \sum_{i\ge2} a_ia_i^\top/(1+\nu_i\tau_s)$, for one- or two-sided exponential traces; equivalently the resolvent $(I - \tau_s\mathcal L)^{-1}$ (an exponential average of Koopman operators) sandwiched between the centred fields. | construction + standard | disclosure "What a trace does"; Engel & Nagel 2000 | reversible stationary dynamics; exponential trace | 3.3 |
| C8.14 | Running example, τ_s = 8: pairs at low θ, wells at higher θ, pieces above; the pair level first appears at the builder's $\tau_s$; the parts nest in this example. | builder values | `hebbian-fig-parts`; hero tour `pairs` | nesting is a check on this example, not a theorem | 3.3 |
| C8.15 | The trace is a modelling choice of this site. | construction (labelled) | 3.3; HH `method.html:40` (lagged statistics untried there) | — | 3.3 |
| C8.16 | Any allocation among mutually compatible disconnected parts is a fixed point (zero floor); a finite floor adds $O(\omega/c)$ coupling. | theorem (programme derivation) | F4; review item 6; circuit tours `three-corners`, `three-corners-s1` | zero-floor limit; compatible, disconnected parts | 3.4 |
| C8.17 | From a random start, the population binds and lands on one part when θ is below roughly $\gamma\kappa_0$; heuristic, numerically supported. | empirical (programme) + widget | F3; review item 5; circuit tour `corners-collective` | exchangeable independent initial embeddings; the crossover moves with the start | 3.4 |
| C8.18 | Same parameters, two outcomes: a fresh network at the wells threshold populates four wells; one trained on pairs first keeps one well per pair. | widget + page test record | hero tours `fresh-fine`, `refine`; `data/hebbian/tours.json` | γ = 1; mean-field; symmetry-breaking perturbation; outcomes per seed as recorded | 3.4 |
| C8.19 | With lateral plasticity, a bound population never split as θ rose in the archived hysteresis loops. | empirical (programme) | F8 (with private jitter) | tested covariances only | 3.4 |
| C8.20 | Under the threshold rule at a clustered fixed point, the weights determine the populated parts and their conductances (plus inequalities); clones add equations, not rank; the parts-sum sketch has rank ≤ K + 1. | theorem (programme derivation) + widget | F10; review item 6; readout tour `threshold` | disjoint parts, zero floor; θ and rates known | 3.5 |
| C8.21 | The distance rule is gradient descent on the averaged equilibrium energy plus a weight cost; fixed point $w = (\zeta - \mathcal D^2/2)_+/\alpha$. | theorem (programme derivation, numerically checked) | HH `idea.html`, `SPEC.md`; `docs/findings_v2.md` | convex on-site potentials, positive attachments (unique equilibrium); expectation over the training bank | 3.5 |
| C8.22 | Linear neurons, distance rule: each live edge is $\mathbf d^\top\hat C\mathbf d = 2(\zeta - \alpha w)$; the common mode is invisible; $P_\perp\hat CP_\perp$ is determined iff live-edge outer products span the symmetric contrast space. | theorem (programme derivation) | HH `readout.html` | fixed point reached; attachments, ζ and α known (else up to one common factor); training-bank moment, not population | 3.5 |
| C8.23 | Too few live edges: rank-deficient; just above percolation: exact and robust to 1% noise; fully fused: exact but destroyed by 1% noise. | widget | readout tours `few`, `sweet`, `fragile` (`blocks` as the project's verified companion) | values from the page's test record | 3.5 |
| C8.24 | A covariance does not determine the input distribution (two-atom counterexample; the mean is lost). | construction | 3.5; HH `readout.html`; review item 8 | centred features | 3.5 |
| C8.25 | The distance rule is a different principle: $-\tfrac12\mathcal D^2$ = coactivity minus activity powers. | construction | 3.6 | — | 3.6 |
| C8.26 | Under the distance rule, clusters are live-edge components, possibly chains; with random multi-input attachments no stable few-cluster count was found; nonlinear weights give only a partial distance table. | empirical (programme) + theorem (programme derivation, for the table) | HH `fusion.html`, `many.html`, `readout.html` | as in the project | 3.6 |
| C8.27 | For linear neurons, population eigenfunctions are input modes iff $\mathcal H^\top\mathcal H$ commutes with $\Sigma_g$. | theorem (programme derivation) | HH `diversity.html:101-155` | nonsingular $\Sigma_g$ (projected commutator otherwise) | 3.6 |
| C8.28 | Whether a traced or lagged distance rule computes Koopman-like eigenfunctions is open. | motivation (section 8 hook) | — | — | 3.6 |

Things not to claim on this page (SPEC appendix D): Hebbian learning finds covariance eigenvectors or does spectral
clustering; the distance rule is the threshold rule's nonlinear extension; hierarchical refinement is a property of
the equilibrium (it is history-dependent, shown by example); weights reveal the input distribution; spectral
sparsification (page 5) prunes networks safely (do not imply the pruning threshold is a sparsifier).

## 5. Figures and widgets

### 5.1 `hebbian-fig-hero` "Place fields on four wells, and what Hebb's rule makes of them" (live, hero; key `hr`)

- **Purpose:** under the threshold rule, neurons fed the running example's place fields gather on the wells; with a
  slow trace, on the pairs; and refinement depends on history.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`. Main view, two rows:
  (a) **map** (full width, height 420; phones 300): contours of V over Ω (as page 1's hero), wells as ink-outlined
  circles labelled $w_1..w_4$; the 16 inputs as small squares at their field centres $z_b$, filled with the colour of
  their well (`--c-well-k`); each interior neuron as a circle at its **barycentric position** $\sum_b h_{ib}z_b$ (the
  harmonic embedding drawn in place), coloured by its cluster's class (below); clusters drawn as one circle of radius
  ∝ $0.8 + 2\sqrt{n_k/N}$ once clustering is clear-cut (as in HebbianHarmonics' old widget); ink lines for the
  strongest synapses (opacity $w/\max w$, at most 2,000 drawn), toggle in advanced; hollow dashed markers at the
  barycentres of all **stable parts** at the current $(\tau_s, \theta)$ from the builder's exact enumeration ("parts
  that exist"). Hover a neuron or cluster: its embedding as a 4 × 4 receptive-field tile over the field grid, its
  class, its $c$ and energy $h^\top\Sigma_g h$.
  (b) **covariance** $\mathcal H\Sigma_g\mathcal H^\top$ with neurons sorted by cluster (as in the old widget; `div`
  map, range ±max diag of $\Sigma_g(\tau_s)$), band colours = cluster class; and beside it
  (c) **allocation over time**: neurons per cluster, stacked, dead neurons grey (the old widget's river chart), with a
  vertical marker at a threshold change.
- **Cluster classes** (shared rule, `classifyPart(h)` in `p_hebbian_model.js`, also used by the builder for parts):
  well masses $m_k = \sum_{b \in \text{well }k} h_b$. "one" if every $m_k \ge 0.1$; "pair L" / "pair R" if the pair's
  mass ≥ 0.9 and each of its wells ≥ 0.25; "well k" if $m_k \ge 0.9$ and the support (entries ≥ 0.01) has 4 fields;
  "piece of well k" if $m_k \ge 0.9$ and the support has ≤ 3 fields; otherwise "mixed". Colours: pair → `--c-pair-L/R`;
  well and piece → `--c-well-k` (piece drawn with a lighter fill); one and mixed → `--c-other`.
- **Data:** `site/data/hebbian/p08.json` (builder): field centres and widths, scale, $\Sigma_g(\tau_s)$ for $\tau_s \in
  \{0, 0.5, 2, 8, 32\}$, the exact part enumeration on the θ grid −0.6:0.02:1.0 (support, h, c, class, energy), presets
  `theta.wells0`, `theta.pairs8`, `theta.wells8`, $\kappa_0$ per $\tau_s$, $E_{\rm pair}$ at `pairs8`. Simulation live
  with the v1 engine (`js/engine.js`, unchanged; mean-field: exact $\Sigma_g(\tau_s)$ every step) through the page
  helper `p_hebbian_model.js` (a B-generic adaptation of HebbianHarmonics' `ch_old_model.js`, which is B = 3 only).
- **Controls (primary):** transport (play/pause, speed ×1/×4/×16, reset); trace $\tau_s$ (segmented `0` | `0.5` | `2` |
  `8` | `32`); threshold θ (slider −0.6 to 1.0, step 0.02, marks at the three builder presets labelled "wells",
  "pairs (τ_s = 8)", "wells (τ_s = 8)"); lateral gain γ (segmented `0` | `0.5` | `1`). Advanced: N (48-160, default
  96), seed (0-2), $w_{\min}$ (1e-5, 1e-4, 1e-3; default 1e-4), show synapses, show stable parts.
- **What changes when each control moves:** θ, γ and $\tau_s$ act **on the running network** (history is the point);
  the stable-part markers update immediately from the enumeration; a vertical marker is added in (c). Reset restarts
  from a fresh random state at the current settings. N and seed restart. URL state for free play records the settings
  and is read as a fresh start; the two-stage protocols exist only as tours.
- **Run protocol:** Euler dt = 0.05, decay and learning rates 1, input weights $W_{IB} \sim \mathrm{Exp}(0.2)$, lateral
  weights start at the floor, dense masks. A stage ends when the projected residual $\max|dw/dt| < 10^{-5}$ **and** the
  stage has lasted at least 100 time units. At every threshold change (tour stage 2 or a live θ change) every weight is
  multiplied by $1 + 10^{-6}\xi$, ξ ~ N(0,1) from the seeded stream, so that an exactly symmetric unstable state cannot
  persist (HebbianHarmonics F8: a small residual does not certify stability); the caption says so.
- **Stat tiles:** "clusters K" (populated clusters with ≥ max(2, 2% N) members, the old widget's convention) with their
  classes ("2 pairs", "4 wells", …); "parts that exist" (count and classes from the enumeration at the current
  $(\tau_s, \theta)$); "residual" $\max|dw/dt|$; "dead neurons"; "$\gamma\kappa_0$" (heuristic crossover).
- **Tours** (default first; outcomes recorded by the page's test, section 12):
  1. `wells`: $\tau_s = 0$, θ = `theta.wells0`, γ = 1, N = 96, seed 0, fresh. Note: "No trace: the neurons gather on
     the four wells."
  2. `pairs`: $\tau_s = 8$, θ = `theta.pairs8`, γ = 1, fresh. Note: "With a slow trace and a low threshold: the two
     pairs."
  3. `fresh-fine`: $\tau_s = 8$, θ = `theta.wells8`, γ = 1, fresh. Note: "A fresh network at a higher threshold: all
     four wells."
  4. `refine`: $\tau_s = 8$, γ = 1; stage 1 θ = `theta.pairs8` until the stage ends; stage 2 θ = `theta.wells8` until it
     ends. Note: "Learned the pairs first, then the threshold rose: each pair cluster moved as one body to one well."
  5. `refine-unbound` (**optional**: include only if the test finds the same class of outcome for seeds 0-2): as
     `refine` with γ = 0; note states the recorded outcome.
- **fallbackTour:** `wells` (the default), so the static image matches the first thing a reader sees; GIF from
  `refine` (stage change visible).
- **Caption:** *Plotted:* (a) contours of $V(x_1,x_2)$, wells $w_1..w_4$; squares: the 16 input place fields at their
  centres, coloured by well; circles: interior neurons at $\sum_b h_{ib}z_b$, the field centres averaged with weights
  given by each neuron's harmonic embedding, coloured by cluster class; dashed rings: stable parts at the current
  threshold and trace (exact enumeration); lines: strongest synapses; (b) voltage covariance $\mathcal H\Sigma_g
  \mathcal H^\top$, neurons sorted by cluster; (c) neurons per cluster against time. *Values:* inputs = centred place
  fields of the particle's position (centres on a 4 × 4 grid, $x_1 \in \{\pm0.5, \pm1.5\}$, $x_2 \in \{\pm0.3,
  \pm0.9\}$, widths 0.5 and 0.3), covariance under the equilibrium density, optionally trace-filtered with time
  $\tau_s$ (equation 6), scaled to mean variance 1; threshold rule with decay and learning rates 1, $w_{\min} =
  10^{-4}$, Euler dt = 0.05, mean-field; a relative $10^{-6}$ weight perturbation at each threshold change. Running
  example, face A (place-field features). `synthetic`.
- **Static fallback:** `assets/fallback/hebbian-fig-hero-wells.png`; PNGs for every tour; GIF
  `assets/fallback/hebbian-fig-hero.gif` (≈ 6 s of `refine` around the threshold change, ×16).
- **Accessibility:** alt text: "Neurons drawn over a four-well landscape gather into four clusters, one per well; a
  river chart shows how many neurons each cluster holds over time." Clusters are labelled with their class in text on
  hover and in the tile, so colour is not the only carrier.
- **Performance:** one Euler step at N = 96, B = 16 (Cholesky of $L_{II}$, products with $\Sigma_g$) ≈ 0.5-1 ms; steps
  per frame budgeted to ≤ 8 ms; convergence typically 300-2,600 steps (HH F9; slower near transitions). Clustering
  (`clustersAuto`) once per frame. Parity: none new (engine.js is parity-tested in HebbianHarmonics against
  `hebb/core.py`; keep that test with the copy).

### 5.2 `hebbian-fig-kirchhoff` "A neuron's embedding is where a random walk lands" (static, rendered by the page module; key `kc`)

- **Purpose:** conductances determine each neuron's harmonic embedding, a probability vector over the inputs.
- **Content:** a small fixed circuit: three inputs $g_1, g_2, g_3$ (squares at the corners of a triangle) and four
  interior neurons $n_1..n_4$ (circles at their barycentric positions). Conductances (fixed, in
  `data/hebbian/kirchhoff.json`): input edges $n_1g_1 = 1$, $n_2g_2 = 1$, $n_3g_3 = 1$, $n_4g_1 = 0.2$; lateral edges
  $n_1n_2 = 0.5$, $n_2n_3 = 0.5$, $n_3n_4 = 1$, $n_4n_1 = 0.5$. The module computes $\mathcal H$ live (4 × 3 solve),
  draws each edge with width ∝ conductance (ink), each input edge in its input's colour, and beside each neuron a
  three-segment bar of $h_i$ in input colours with the numbers. Hover a neuron: its row of $\mathcal H$ and the sentence
  "probability that a random walk from $n_i$, choosing edges in proportion to conductance, first reaches $g_1, g_2,
  g_3$". A toggle "clamp $g = (1, 0, 0)$" colours each neuron by its voltage $h_{i1}$ (`seq` map), showing $u =
  \mathcal Hg$.
- **Caption:** *Plotted:* a resistor network with three clamped inputs (squares) and four interior neurons (circles,
  placed at their harmonic embeddings); line width ∝ conductance; bars: rows $h_i$ of $\mathcal H = L_{II}^{-1}W_{IB}$.
  *Values:* conductances as drawn (illustrative, not learned).
- **Fig-sub:** *Each neuron's harmonic embedding is a probability vector over the inputs, fixed by the conductances: the
  chance that a random walk from the neuron reaches each input first.*
- **Fallback:** PNG `assets/fallback/hebbian-fig-kirchhoff-default.png` (captured like a widget with one tour).
  Alt text: "A small circuit of three input squares and four neuron circles, with bars showing each neuron's
  probabilities over the inputs."

### 5.3 `hebbian-fig-circuit` "Three inputs: clusters sit on parts" (live; key `ci`)

- **Purpose:** on three inputs, where every embedding is a point in a triangle, see collapse without pruning, parts at
  corners and edge midpoints, no cluster on a signed eigenvector, allocation that differs by seed, and collective
  binding.
- **Reuse:** HebbianHarmonics' old-rule widget: `ch_old.js` (UI) adapted as `p_hebbian_circuit.js` (ids, widget key
  prefix `ci_`, captions, neutral voice), `ch_old_model.js` imported **unchanged** (SPEC 6.2) with its `PRESETS`,
  `DEFAULTS`, `TOURS`, `createSim`, `analyse`, `runTour`; `engine.js` unchanged. Layout, panels, controls and
  encodings as in the original (triangle in `view3d` with optional height $\kappa\,h^\top\Sigma_g h$ and mesh; the
  covariance panel; the allocation river), with the side panel trimmed to: tours; inputs preset; θ (with the
  $\gamma\kappa_0$ line beneath it); γ. Advanced: the six $\Sigma_g$ sliders, $w_{\min}$, N, seed, view (height |
  flat).
- **Data:** live (engine.js mean-field on the preset covariance).
- **Controls (primary):** inputs preset (`indep` | `pair` | `pos` | `tilt` | custom); θ (−0.2 to 1.2); γ (0 | 0.5 | 1);
  transport. Advanced as above.
- **Default state (= first tour):** `neutral-identity` (the first entry of `ch_old_model.js` `TOURS`).
- **Tours:** exactly `ch_old_model.js` `TOURS`, in its order: `neutral-identity`, `corners-collective`,
  `three-corners`, `three-corners-s1`, `edge-midpoint`, `midpoint-splits`, `independent-tilt`; notes as in that file
  (they are neutral and match the engine; `runTour` checks them).
- **fallbackTour:** `edge-midpoint` (the page's main use; the default remains `neutral-identity`).
- **Stat tiles:** as the original: K, member spread, residual, dead, $\gamma\kappa_0$.
- **Caption:** the original's caption with "I"-free wording: *Plotted:* top: squares are the inputs $g_1, g_2, g_3$
  at the corners they define; circles are interior neurons at their harmonic embeddings (barycentric position),
  raised by $\kappa\,h_i^\top\Sigma_g h_i$ (or flat); colour mixes the input colours by $h_i$; grey: dead neurons; ink
  lines: synapses; below: (a) $\mathcal H\Sigma_g\mathcal H^\top$ sorted by cluster; (b) neurons per cluster against
  time. *Values:* B = 3, decay and learning rates 1, dt = 0.05, mean-field, paused when the residual < $10^{-5}$;
  defaults N = 90, $w_{\min} = 10^{-4}$, lateral weights at the floor, $W_{IB} \sim \mathrm{Exp}(0.2)$; tours set
  $\Sigma_g$, θ, γ and seed. HebbianHarmonics companion (not the running example). `synthetic Σ`.
- **Fig-sub:** *On three inputs, clusters land at corners or edge midpoints, the nonnegative parts of the shifted
  covariance, never at its signed eigenvector.*
- **Static fallback:** PNG per tour; GIF of `three-corners` (≈ 6 s at ×4).
- **Accessibility / performance:** as the original (DESIGN.md §§9-11; ≤ 4,000 synapses drawn).

### 5.4 `hebbian-fig-parts` "Parts versus eigenvectors, and the ladder of parts" (static, rendered by the page module; key `pt`)

- **Purpose:** in the running example, parts are nonnegative pieces (wells, pairs) while covariance eigenvectors are
  signed contrasts; and which parts exist is set by θ and $\tau_s$ together.
- **Content:** three panels from `p08.json`:
  (a) **eigenvectors**: for $\tau_s = 0$ and $\tau_s = 8$ (two rows), the top four eigenvectors of $\Sigma_g(\tau_s)$ as
  4 × 4 tiles laid out like the field grid (`div` map, symmetric range), each with its eigenvalue and the builder's
  label (pair contrast, within-pair contrasts, product);
  (b) **parts**: in the same two rows, the stable parts at the presets (row $\tau_s = 0$: `wells0`; row $\tau_s = 8$:
  `pairs8` and `wells8`) as 4 × 4 nonnegative tiles (`seq` map), each with c, its best single-eigenvector cosine, and
  the fraction of its norm in the span of the constant and the top-K eigenvectors (K = number of parts at that preset);
  (c) **ladder**: rows $\tau_s \in \{0, 0.5, 2, 8, 32\}$, x = θ from −0.6 to 1.0; each θ cell coloured by the class of
  the stable parts there (`one` `--c-other` dark; pairs `--c-pair-L` tint; wells `--c-well-4` tint; pieces lighter;
  mixed hatched; none blank), with the count printed in cells wide enough; preset markers.
- **Generation:** drawn by `p_hebbian.js` from the data (no interaction beyond hover), so it updates with the builder.
- **Caption:** *Plotted:* (a) eigenvectors of the place-field covariance $\Sigma_g(\tau_s)$ drawn on the 4 × 4 field grid,
  with eigenvalues; (b) stable parts (nonnegative eigenvectors of principal submatrices of $\Sigma_g(\tau_s) -
  \theta\mathbf 1\mathbf 1^\top$ passing the stability test) at the marked thresholds, with c, best eigenvector cosine,
  and norm fraction in the span of $\mathbf 1$ and the top-K eigenvectors; (c) class and number of stable parts against
  θ for five trace times. *Values:* as the hero; exact enumeration over all $2^{16} - 1$ supports. Running example,
  face A (place-field features). `synthetic`.
- **Fig-sub:** *Eigenvectors are signed contrasts; parts are nonnegative wells or pairs. Without a trace a threshold
  only finds wells; with a slow trace it finds pairs first, then wells.*
- **Fallback:** PNG `assets/fallback/hebbian-fig-parts-default.png`.

### 5.5 `hebbian-fig-readout` "Reading the input statistics back from the weights" (live, centrepiece; key `ro`)

- **Purpose:** the fixed-point equations of live synapses determine the contrast second moment under the distance rule
  with linear neurons once they span, fail when too few synapses live, become fragile when the network fuses; under the
  threshold rule they give a parts sketch.
- **Reuse:** HebbianHarmonics `ch_readout.js` `liveFigure` (adapted as `p_hebbian_readout.js`), its estimator
  `ch_readout_math.js` (copied verbatim as `p_hebbian_readout_math.js`), and the v2 engine `onsite_engine.js` (copied
  verbatim as `p_hebbian_onsite_engine.js`; see section 12 on placement); the threshold-rule readout uses `engine.js`
  `readoutState` (thetaMode `project`) and a parts-sum computed from `analyse`-style clusters. The original is
  hard-wired to B = 12; the adaptation takes B from the inputs (16 for the running example, 12 for the companion).
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view: a row of three heatmaps (a) target, (b) recovery,
  (c) recovery − target (fields grouped by well with band colours $w_1..w_4$; companion: inputs $g_1..g_{12}$; `div` map,
  one symmetric range), then a row of two charts: (d) singular values of the live-edge measurement operator (log y;
  dashed tolerances $10^{-8}$ and $10^{-4}$ of the largest; vertical line at the dimension of the target space), (e)
  training trace (1 − cos with the target, fixed-point error, projected residual, against step; orange: frame shown).
  Transport as the original (training animates; readout recomputed every 4 frames and at convergence).
- **Data:** inputs `running` (default): a bank of $n_s = 256$ equilibrium positions from `data/example/samples.json`
  (seed-0 set, first 256), features $g_b(x)$ centred by the population means and scaled as in `p08.json`; target for the
  distance rule $P_\perp\hat CP_\perp$ with $\hat C = G^\top G/n_s$; target for the threshold rule
  $P_\perp\Sigma_g(0)P_\perp$ (mean-field uses the population covariance). Companion `blocks`: HebbianHarmonics' four
  blocks of three (variances 2, 1, 0.5, 0.25, within 0.8), Gaussian bank of 256, seed as set. Attachments for the
  distance rule: s = 3 random inputs per neuron, Dirichlet shares, total conductance 1 (`makeNet`).
- **Controls (primary):**
  1. rule: `distance (linear neurons)` | `threshold`;
  2. plasticity scale: for the distance rule ζ (log slider 0.003-1, marks at the builder/test presets "few", "sweet",
     "fused"); for the threshold rule θ (slider −0.2 to 0.8, mark "wells"); the label and range switch with the rule;
  3. interior neurons N: `40` | `80`;
  4. weight noise ε: 0, 1e-6, 1e-5, 1e-4, 1e-3, 3e-3, 1e-2, 3e-2 (every weight × (1 + εξ), one fixed symmetric draw;
     the whole readout rebuilt from the noisy weights).
  Advanced: inputs (`running` | `blocks`); method (distance rule: ridge | ridge + dead-pair hinge; threshold rule:
  parts-sum | masked least squares); seed (attachments, bank; 0-9).
- **What changes:** rule, scale, N, inputs, seed retrain from scratch (W = 0 for the distance rule; the threshold rule's
  default start); ε and method act on the trained weights without retraining.
- **Stat tiles:** "live edges" (distance) or "active synapses" (threshold); "rank of what the weights measure" (distance:
  rank on the contrast space, out of $B(B-1)/2$; threshold: rank on all symmetric B × B matrices, out of $B(B+1)/2$,
  via `engine.measurementSpectrum`); "cos vs target" (Frobenius cosine after PSD projection); "cos vs population"
  (distance rule: against $P_\perp\Sigma_g(0)P_\perp$, limited by sampling); "fixed-point error"; "sampling error"
  (distance rule); "noise gain $2\alpha w/\mathcal D^2$" (median over live edges; distance rule); "clusters K"
  (threshold rule).
- **Tours** (default first; ζ presets found by the page's test script on the `running` bank and recorded in
  `data/hebbian/tours.json`: `few` = largest ζ on the grid with fewer live edges than half the target dimension;
  `sweet` = smallest ζ with full rank and ≥ 2 live-edge components; `fused` = smallest ζ with one component and every
  pair live):
  1. `sweet`: distance, running, ζ = sweet, N = 80, ε = 0.01, seed 1. Note: "Full rank while the network is still in
     several components: the contrast second moment is read exactly and survives 1% weight noise."
  2. `few`: distance, running, ζ = few, ε = 0. Note: "Too few live synapses: the rank is the number of live edges, and
     the readout is no better than a scaled identity."
  3. `fused`: distance, running, ζ = fused, ε = 0. Note: "One component, every pair live: exact."
  4. `fragile`: as `fused` with ε = 0.01. Note: "The same network with 1% weight noise: the readout collapses."
  5. `threshold`: threshold rule, running, θ = `theta.wells0`, γ = 1, N = 80. Note: "The threshold rule's weights
     measure only the populated parts: a low rank, and a sketch of the well blocks."
  6. `blocks`: distance, blocks, ζ = 0.05, ε = 0.01, N = 80, seed 1 (HebbianHarmonics' verified `sweet` tour). Note:
     "The project's own example: twelve inputs in four blocks."
- **fallbackTour:** `sweet`.
- **Caption:** *Plotted:* (a) the target: $P_\perp\hat CP_\perp$ ($\hat C = G^\top G/n_s$ over the training bank,
  $P_\perp = I - \mathbf 1\mathbf 1^\top/B$) for the distance rule, $P_\perp\Sigma_gP_\perp$ for the threshold rule;
  (b) the recovery from the (noisy) weights and attachments, after PSD projection; (c) recovery minus target; (d)
  singular values of the live-edge measurement operator, with rank tolerances; (e) during training: 1 − cos with the
  target, fixed-point error $\max_{\rm live}|2(\zeta - \alpha w) - \mathbf d^\top\hat C\mathbf d|$, projected residual.
  *Values:* running-example inputs: 16 centred place fields at 256 equilibrium positions (seed-0 sample set), scaled as
  in the hero; linear neurons (no on-site potential), s = 3 attachments per neuron of total conductance 1, α = 1,
  projected Euler dt = 0.5 from W = 0, stopped at $\max|\Delta w|/dt < 10^{-9}$ (distance rule); threshold rule as in
  the hero at $\tau_s = 0$. Companion: HebbianHarmonics' block covariance. Running example, face A (place-field
  features), or companion as set. `synthetic`.
- **Fig-sub:** *Each live synapse is one linear equation in the input second moment: with enough of them the contrast
  part is read exactly; too few, or too fused, and the readout fails.*
- **Static fallback:** PNG per tour; no GIF (training is shown in panel (e)).
- **Accessibility:** heatmap cells have numeric tooltips; tiles are text; tour notes announced.
- **Performance:** distance rule at N = 80, B = 16: training to $10^{-9}$ in ≤ 3 s with the engine's warm-started
  solver (status "training…", animated); measurement operator up to 3,160 live edges × 120 unknowns: QR + one-sided
  Jacobi SVD ≤ 300 ms, once per readout. Threshold rule: training as the hero; `measurementSpectrum` with ≤ 2,000
  active synapses × 136 unknowns ≤ 300 ms, once at convergence. Parity: the copied estimator and engine keep their
  HebbianHarmonics parity tests; add a test that the `blocks` tour reproduces the original page's `sweet` tile values
  (rank 66, cosine as recorded there).

## 6. Running example on this page

- **Face:** A, through features of position. Parameters exactly as SPEC 3.2 (κ = 0, D = 0.5); the page does not use
  the readout y or the symbols.
- **Place fields (defined here; binding for the builder per SPEC 3.6):** B = 16 Gaussian fields
  $g_b(x) = \exp\!\big(-\tfrac{(x_1 - z_{b,1})^2}{2\cdot0.5^2} - \tfrac{(x_2 - z_{b,2})^2}{2\cdot0.3^2}\big)$ with centres
  on the grid $z_{b,1} \in \{-1.5, -0.5, 0.5, 1.5\}$, $z_{b,2} \in \{-0.9, -0.3, 0.3, 0.9\}$, so each well sits at the
  centre of a 2 × 2 block of four fields. Order b = 1..16 by well ($w_1$'s four fields first, then $w_2$, $w_3$, $w_4$;
  within a well, inner-lower, inner-upper, outer-lower, outer-upper), and say so in the data file.
  Inputs are centred by their equilibrium means; one scale s₀ makes the mean variance of $\Sigma_g(0)$ equal to 1, and
  each $\Sigma_g(\tau_s)$ is rescaled to mean variance 1 as well (so θ is in units of mean input variance at every
  $\tau_s$; record both scales).
- **Precomputed** (`tools/build_example.py` → `site/data/hebbian/p08.json`, with config and assertions):
  - `fields` (centres, widths, order, well of each field), `means`, `scales`.
  - `Sigma[tau_s]` for $\tau_s \in \{0, 0.5, 2, 8, 32\}$ (16 × 16). Method: at κ = 0 the fields and the generator are
    separable, so $a_{ib}$ factor into 1-D projections; compute with ≥ 40 eigenpairs per axis from the 1-D generators,
    and $\Sigma_g(0)$ also directly as $\mathrm{Cov}_\pi$ on the grid. Cross-check against the 2-D grid (`grid.json`
    eigenpairs plus the exact $\Sigma_g(0)$) to $10^{-3}$ relative, and against a Monte Carlo estimate from pooled
    trajectories (exponentially traced features) within 3 standard errors.
  - `eig[tau_s]`: top 6 eigenpairs with labels (pair contrast, within-pair contrasts, product, other) by sign pattern on
    wells.
  - `parts[tau_s][theta]` on θ = −0.6:0.02:1.0: all stable parts by exact enumeration over the $2^{16} - 1$ supports
    (Perron vector of $Q_{SS}$ positive, c > 0, c strictly the top eigenvalue, strict negative off-support margin with
    tolerance $10^{-12}$), each with support bitmask, h (normalized to sum 1), c, energy $h^\top\Sigma_gh$, class
    (`classifyPart`), best eigenvector cosine, norm fraction in span(1, top-K). Vectorize by support size (batched
    symmetric eigensolves); budget ≤ 10 min.
  - `ranges[tau_s]`: min/max of $\Sigma_g$ entries within a well, between the wells of one pair, across pairs.
  - `kappa0[tau_s]`; `theta` presets: `wells0` (centre of the longest θ interval at $\tau_s = 0$ whose parts are
    exactly the four wells), `pairs8` (centre of the interval at $\tau_s = 8$ whose parts are exactly the two pairs,
    intersected with θ > γκ₀ + 0.05), `wells8` (a θ at $\tau_s = 8$ whose parts are exactly the four wells and with
    θ < γ·E_pair − 0.05, where E_pair is the pair part's energy at `pairs8`); `E_pair`, `E_well`.
  - `pair_level_first_tau`: smallest $\tau_s$ in the grid with any θ whose parts are exactly the two pairs.
  - **Assertions:** fields' mass on their own basin ≥ 0.9 (each field responds to its own well); at $\tau_s = 0$ some θ
    interval of width ≥ 0.2 has exactly the four wells as parts and no θ has exactly the two pairs; at $\tau_s = 8$
    intervals with exactly the two pairs and exactly the four wells both exist, the pairs' at lower θ; `wells8` exists
    (the window $\theta_{\rm wells} < \gamma E_{\rm pair}$ is non-empty). **If an assertion fails, stop and amend this
    spec; the fallback is the HebbianHarmonics block covariances (`hier8`, `#old` companion, SPEC 3.7).**
  - **Spec-time check (not for display; the builder's values replace these):** an independent computation with these
    fields (1-D spectra, 40 modes per axis) found, after per-$\tau_s$ normalization: at $\tau_s = 0$, within-well
    entries 0.49 to 0.89, same-pair other-well −0.29 to −0.10, across pairs −0.42 to −0.13; one part for θ ≤ −0.3,
    the four wells for θ from −0.1 to 0.5, pieces of wells from 0.6; at $\tau_s = 8$, same-pair other-well entries
    0.13 to 0.43, pairs for θ from −0.4 to 0.2, wells for 0.4 to 0.8, mixed six-field parts at 0.3; at $\tau_s = 2$ a
    narrow pair window (−0.3 to −0.1); at $\tau_s = 32$ pairs up to 0.6; $\kappa_0 \approx 0$ at every $\tau_s$;
    $E_{\rm pair} \approx 0.65$ at $\tau_s = 8$. So `wells8` should lie near 0.45-0.6.
- **Page test records** (`tests/test_tours_hebbian.mjs`, writes `data/hebbian/tours.json` in `--record` mode, asserts
  otherwise): for each hero tour and seeds 0-2: K, classes, sizes, final time; for `refine`, the well chosen per pair;
  the readout ζ presets and each readout tour's tiles. Expected: `wells` 4 wells; `pairs` 2 pairs; `fresh-fine` 4
  wells; `refine` 2 clusters, one well per pair, in at least 2 of 3 seeds. If `refine` does not show this, raise γ to
  1.5 (keeping θ < γE_pair) and re-record; if it still fails, replace the refinement example with HebbianHarmonics'
  `hier-pair-per-half` tour (hier8, θ = 0.4, γ = 1) and amend this spec.
- **Live:** all simulations; the Kirchhoff figure; nothing about the example is typed by hand.
- **Strain, and how the page states it:** the static covariance sees wells only; the pair level needs the trace, a
  modelling choice (3.3); the fields are placed by the site (3.3, caption); the threshold rule's clusters are clones,
  so a "population of neurons on a well" is one function repeated (3.2 disclosure).
- **Companions:** HebbianHarmonics' three-input presets (`hebbian-fig-circuit`); its block covariance (readout tour
  `blocks`).

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E10 | 4 Spectral clustering / 5 Sparsity | `=` | A clamped resistor network solves the graph Dirichlet problem: the harmonic embedding is harmonic label propagation with the inputs as labels; the same Laplacian's pseudo-inverse gives effective resistance (page 5). |
| E15 | 7 Neurons | `~` | Local rules compute spectral objects, each exactly for its own rule: PCA or principal subspaces, or CCA under stated objectives; this page's threshold rule has thresholded, nonnegative principal-submatrix eigenvectors as fixed points (of a lag-averaged covariance when a trace is added). No bound relates the rules' answers. |
| E23 | 4 Spectral clustering | `~` | Hebbian clustering and spectral clustering both threshold a spectral computation on a similarity matrix; no theorem says Hebbian learning finds a chosen Laplacian partition. |

Map card text: "Hebbian · thresholded Hebb rule on a resistor network · knob: threshold θ (and trace τ_s) · bound:
exact fixed-point characterization of parts; no bound on allocation or refinement."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The threshold-shifted input covariance $Q = \Sigma_g - \theta\mathbf 1\mathbf 1^\top$ (with a trace, $\Sigma_g(\tau_s)$, a lag-averaged covariance); parts are nonnegative eigenvectors of principal submatrices, $Q_{SS}h_S = c\,h_S$, $h_S > 0$, $(Qh)_{\bar S} \le 0$. No weighting beyond the input scale. |
| Knob | Pruning threshold θ; in this site's illustration the synaptic trace time $\tau_s$; the lateral gain γ affects which parts are populated, not which exist. |
| Discarded at r | Correlations below threshold (an input whose shifted covariance with a part is not positive falls outside its support); all sign structure (parts are nonnegative); with a trace, fast input modes, in proportion $1/(1+\nu_i\tau_s)$. |
| Bound | Exact fixed-point characterization of parts, with a sufficient stability test; for uniform block covariances block parts are stable iff $\rho_{\rm across} < \theta < \rho_{\rm within}$ (HebbianHarmonics `docs/v1/findings.md` F1; programme derivation, independently checked; `theorem` in that scope). Weight readout: for the distance rule with linear neurons, the weights and attachments determine the contrast second moment $P_\perp\hat CP_\perp$ exactly when live-edge outer products span the symmetric contrast space, never the common mode and never the input distribution (HebbianHarmonics `site/content/readout.html`; `theorem`, programme derivation); for the threshold rule, only the populated parts' sketch (F10). No approximation bound for population allocation or refinement order: `none` (history-dependent, shown by example). |
| From data | Mean-field (exact $\Sigma_g$) versus minibatch learning; sampling error of $\Sigma_g$ and of the readout's training bank ($\lVert P_\perp\hat CP_\perp - P_\perp\Sigma_gP_\perp\rVert/\lVert P_\perp\Sigma_gP_\perp\rVert$, shown live) — `standard`. |
| Running example | From the builder (`p08.json`): within-well, same-pair and across-pair covariance ranges at each $\tau_s$; θ presets selecting wells ($\tau_s = 0$, 8) and pairs ($\tau_s = 8$); the first $\tau_s$ with a pair level. From the page test (`tours.json`): populated clusters for `wells`, `pairs`, `fresh-fine`, `refine`; readout rank and cosine at `sweet`, `few`, `fragile`, `threshold`. |
| Budget line | — (this page supplies a mechanism, not a term). |

## 9. Things not to claim

Hebbian learning finds covariance eigenvectors, or does spectral clustering; clusters are "eigenmodes of the input";
the distance (v2) rule is the threshold (v1) rule's nonlinear extension; hierarchical refinement is guaranteed or set by
the equilibrium (it is history-dependent, shown by example); the trace is part of the HebbianHarmonics model (it is this
site's illustration); the parts nest in general (a check on this example only); weights reveal the input distribution,
or the full covariance, or the common mode; the threshold rule's weights recover $\Sigma_g$; members of a cluster form
a reservoir of distinct features (they are clones in every tested condition); the homeostatic parameters set an
allocation law (fits on tested families only); $\theta \approx \gamma\kappa_0$ is a phase boundary (it is a heuristic);
the network computes Koopman eigenfunctions (open); the pruning threshold is a spectral sparsifier (page 5's theorem is
about graph Laplacians, not about this rule).

## 10. Notation used

Global (SPEC appendix A): r (not used for parts; the page counts parts as K), $\nu_i$, $\lambda_i$ (only in the trace
disclosure, as $e^{-\nu_i\tau}$), $\mathcal L$, $\mathcal K_t$, τ, x, V, D, π, $w_1..w_4$, L/R pairs, L (graph Laplacian),
W (edge weights).
Page-local (SPEC appendix A allows HebbianHarmonics notation on this page; adjusted to avoid clashes, with a side note
at first use):
- B (number of inputs, 16 in the example; not the state-space B of page 2), N (interior neurons), g (clamped inputs;
  $g_b(x)$ the place fields), u (voltages), $W_{IB}$, $W_{II}$ (input and lateral conductances; the distance rule's
  fixed attachments are $W_{IB}$ too), $L_{II}$, $\mathcal H$ (harmonic extension, calligraphic to keep H for Hankel),
  $h_i$ (its rows), $z_b$ (field centres).
- $\Sigma_g$, $\Sigma_g(\tau_s)$, θ, γ, $w_{\min}$, $\omega = Nw_{\min}$, $\tau_s$, $Q$ (shifted covariance;
  HebbianHarmonics writes A, which this site reserves for state matrices), S (support), c (a part's eigenvalue = summed
  input conductance), q (other eigenvalues of $Q_{SS}$; HebbianHarmonics writes μ, which this site reserves for
  Laplacian eigenvalues), K (populated clusters), $n_k$, $\kappa_0$, $E_k = h_k^\top\Sigma_gh_k$, $a_{ib}$ (mode
  coefficients $\langle\tilde g_b, \phi_i\rangle_\pi$, with $\phi_i$ the generator eigenfunctions of SPEC 3.2).
- Distance rule: ζ (constant drive; HebbianHarmonics writes b, which clashes with the potential's b = 0.6), α
  (stiffness), $\mathcal D_{ij}$ (response distance; HebbianHarmonics writes D, which is the diffusion coefficient here),
  $\mathbf d_{ij} = h_i - h_j$, $F_i$ (response function), $\mathcal V_i$ (on-site potential; not the landscape V),
  $\hat C = G^\top G/n_s$ (training-bank second moment, $n_s$ = 256), $P_\perp = I - \mathbf 1\mathbf 1^\top/B$
  (contrast projector, as in SPEC 4.2; P is reserved for random walks).
- The decay and learning rates are set to 1 and not named (HebbianHarmonics' λ and η would clash with eigenvalues).

## 11. Sources

Cite as in SPEC appendix C (entries marked **new** were added to appendix C in SPEC v1.1).

- Zhu, X., Ghahramani, Z. & Lafferty, J. (2003). Semi-supervised learning using Gaussian fields and harmonic functions.
  *ICML*. [P]
- Doyle, P. G. & Snell, J. L. (1984). *Random Walks and Electric Networks*. Carus Mathematical Monographs 22, MAA.
  [**new**; W: bibliographic details; hitting-probability interpretation standard]
- Oja, E. (1982). A simplified neuron model as a principal component analyzer. *J. Math. Biol.* 15, 267-273. [P]
- Pehlevan, C., Hu, T. & Chklovskii, D. B. (2015). A Hebbian/anti-Hebbian neural network for linear subspace learning.
  *Neural Computation*. [A]
- Pehlevan, C., Zhao, X., Sengupta, A. M. & Chklovskii, D. (2020). Neurons as canonical correlation analyzers.
  *Front. Comput. Neurosci.* 14, 55. [P] (E15 card; page 7 states its scope)
- Stock, C. H., Harvey, S. E., Ocko, S. A. & Ganguli, S. (2022). Synaptic balancing. *PLoS Comput. Biol.* 18(9),
  e1010418. [P] (E10 bridge citation in SPEC; mention only in the E10 disclosure, as a plasticity rule with a
  Laplacian, not a Hebbian rule)
- Földiák, P. (1991). Learning invariance from transformation sequences. *Neural Computation* 3(2), 194-200. DOI
  10.1162/neco.1991.3.2.194. [**new**; W]
- Engel, K.-J. & Nagel, R. (2000). *One-Parameter Semigroups for Linear Evolution Equations*. GTM 194, Springer
  (resolvent as Laplace transform of the semigroup). [**new**; V]
- Programme sources (cite as the HebbianHarmonics project, not as literature): repository
  `/home/ubuntu/code/HebbianHarmonics` at commit `d528fa6`: `docs/note.md` (the original note), `docs/v1/findings.md`
  (F0, F1, F3, F4, F7, F8, F10), `docs/v1/review_corrections.md` (items 2, 3, 5, 6, 7, 8, 10; these override
  findings), `docs/v1/nonlin.md`, `docs/findings_v2.md`, `site/content/old.html`, `idea.html`, `readout.html`,
  `diversity.html:88-155`, `method.html:13` and `:40`; engines `site/js/engine.js` (+ `ENGINE.md`),
  `site/js/onsite_engine.js` (+ `ONSITE_ENGINE.md`), `site/js/ch_old_model.js`, `ch_old.js`, `ch_readout.js`,
  `ch_readout_math.js`. Archived v1 figures and data paths cited inside `docs/v1/` refer to commit `f613d68` and are
  not reusable assets.
- Data provenance: all running-example numbers from `tools/build_example.py` (`p08.json`, `samples.json`, `grid.json`)
  and the page's tour test (`tours.json`).

## 12. Implementation notes

- **Files (writer owns):** `site/content/hebbian.html`; `site/js/p_hebbian.js` (exports `init`, `widgets`; draws
  `hebbian-fig-parts` and `hebbian-fig-kirchhoff`); helpers `p_hebbian_model.js` (B-generic threshold-rule wrapper:
  `createSim({Sigma, B, N, seed, theta, gamma, wmin})`, `analyse(sim, prevLabels)` with cluster classes,
  `classifyPart(h, fields)`, `runProtocol(stages, opts)` for tours, adapted from `ch_old_model.js` with the
  symmetry-breaking perturbation and the stage rule of 5.1), `p_hebbian_hero.js`, `p_hebbian_circuit.js` (adapted
  `ch_old.js`), `p_hebbian_readout.js` (adapted `ch_readout.js` `liveFigure`), `p_hebbian_readout_math.js` and
  `p_hebbian_onsite_engine.js` (verbatim copies of `ch_readout_math.js` and `onsite_engine.js` with a header naming the
  source commit); data `site/data/hebbian/p08.json` (builder), `kirchhoff.json`, `tours.json` (page test),
  `widgets.json`.
- **Shared, copied unchanged by the design-system owner (SPEC 6.2):** `js/engine.js` + `ENGINE.md`,
  `js/ch_old_model.js`. The v2 engine and the readout estimator are copied verbatim, and `ch_old.js` and `ch_readout.js`
  adapted, by this page's writer under the page's own file names as above (SPEC 6.2 lists them).
- **Shared modules used:** `lib/example.js` (V for contours; loaders for `samples.json`), `charts.js` (heatmap,
  lineChart), `view3d.js` (circuit triangle), `palette.js` (well and pair tokens, `mixBary`), `ui.js`, `lib/rng.js`
  (the symmetry-breaking draw; the engines keep their own mulberry32 for parity with HebbianHarmonics).
- **Widget keys and URL state:** hero `hr` (`hr_ts`, `hr_theta`, `hr_gamma`, `hr_n`, `hr_seed`, `hr_wmin`, `hr_syn`,
  `hr_parts`, `hr_tour`); circuit `ci` (the original's keys prefixed: `ci_s`, `ci_v1..ci_v3`, `ci_r12`, `ci_r13`,
  `ci_r23`, `ci_theta`, `ci_gamma`, `ci_wmin`, `ci_n`, `ci_seed`, `ci_view`, `ci_tour`); readout `ro` (`ro_rule`,
  `ro_scale`, `ro_n`, `ro_eps`, `ro_in`, `ro_m`, `ro_seed`, `ro_tour`); static `kc`, `pt` (single tour `default`).
- **Manifest** `data/hebbian/widgets.json`: `hr` (wells, pairs, fresh-fine, refine[, refine-unbound]; fallback wells;
  animated), `ci` (the seven tours; fallback edge-midpoint; animated), `ro` (sweet, few, fused, fragile, threshold,
  blocks; fallback sweet), `kc`, `pt` (default).
- **Tests:** `tests/test_tours_hebbian.mjs` (record/assert hero and readout tours, section 6); `runTour` for every
  circuit tour (the original's check); the copied engines' parity tests; a Python check that `classifyPart` in JS and
  the builder agree on all enumerated parts.

## 13. Page-specific definition-of-done additions

- [ ] The distance rule is introduced as a different rule wherever it appears (3.5, 3.6, readout widget label), never
      as the threshold rule's nonlinear version.
- [ ] Every "the weights determine …" sentence names the rule, the neuron type and the spanning condition.
- [ ] The trace is labelled as this site's modelling choice wherever $\tau_s \ne 0$ is shown (hero caption, parts
      figure caption, 3.3).
- [ ] The hero's stable-part markers come from the builder's enumeration at the exact displayed $(\tau_s, \theta)$;
      screenshots at `wells`, `pairs` and `refine` show populated clusters on (a subset of) the markers.
- [ ] No bowtie on this page: SPEC 1.4 gives no page-8 labels and the page decomposes no past-to-future map with a
      truncation bound (budget line "—"); SPEC 1.4 records this and the map shows page 8 without a knot.
- [ ] Citations match SPEC appendix C, including the entries marked **new** in section 11; the copied and adapted
      HebbianHarmonics files are exactly those of SPEC 6.2's table.
- [ ] Statements of programme results say "the HebbianHarmonics project found/derived", with the file reference in
      Sources.

## Change log

- v1 (2026-11-17): first full spec. Main path restricted to the threshold (v1) rule plus the distance (v2) rule's
  readout and principle, as SPEC appendix D requires. Running-example place fields and trace defined here (SPEC 3.6
  lists the data without a layout) and checked at spec time (section 6). Template gap: support types "theorem
  (programme derivation)" and "cited empirical (programme)" used for the HebbianHarmonics project's derived and
  numerical results.
- v1.1 (2026-11-17): reconciled with SPEC v1.1, which records this page's place fields and Σ_g method as binding for
  the builder (3.6), no bowtie for page 8 (1.4), the reused HebbianHarmonics files (6.2), $P_\perp$ in the ledger
  draft (4.2), the page-local symbols (appendix A), the new bibliography entries (appendix C), and support types
  "theorem (programme derivation)" and "empirical (programme)" (template). E10 is now "4/5–8", so its row names
  page 5 as well (the text already pointed there).
- v1.2 (2026-11-17): round-1 review fix (SPEC v1.2). E15 is now `~`: the cited local rules each solve their own
  spectral problem exactly, but no bound relates their answers, so `≈` (approximation with a cited bound) was too
  strong. The E15 row and the 3.2 bullet keep every exact statement and add the section 8 hook to the comparison.
  Reviewer finding: math-7-10 9.
