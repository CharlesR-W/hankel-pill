# Page spec 07: Neurons as coherent-set detectors

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 7 |
| id (hash, file stem) | `neurons` |
| tab label | Neurons |
| kicker | Page 7 · neuroscience |
| title | Neurons as coherent-set detectors |
| lede (one-sentence claim, ≤ 45 words) | A neuron that filters its recent input with a past-future canonical direction and then rectifies reports which coherent set the input's history lies in. For an Ornstein-Uhlenbeck input this is exact; past-future CCA learns the filter from the input alone. |
| depends on | 3 (Koopman); 4 helps (coherent sets as spectral clustering) |
| edges (SPEC 2.2) | E14, E15, E22 |
| faces of the running example | A (the scalar readout $y_t$ and, for scoring only, the particle's positions); OU warm-up at $w_4$ (SPEC 3.4) as the analytic companion |
| main-path words | 2,100-2,500 |
| spec status | v1.2, 2026-11-17 (round-1 review fixes; first full spec checked numerically at spec time, see section 6; reconciled with SPEC v1.2) |

## 1. Reader outcome

After this page the reader can:

1. Define a coherent set (a pair of regions that the dynamics carries into each other with high probability over a
   lag) and say how the sign of a subdominant singular function of the stochastic Koopman operator (SKO) partitions
   state space into coherent sets.
2. Explain why, for an Ornstein-Uhlenbeck (OU) process, the leading nontrivial singular function is a linear
   projection of the state, so that "filter, then take the sign" computes coherent-set membership exactly; and why
   the next singular functions are Hermite polynomials that no linear filter reaches.
3. Derive the neuron's filter from data: build past and future delay windows, whiten their cross-covariance (a
   Hankel matrix of the input's autocovariance), and take its SVD (past-future CCA); state what is optimal about the
   result and relative to which dictionary.
4. Run this on the running example and predict what a linear filter can and cannot report (the pair, not the well),
   and what giving the neuron ON and OFF rectified channels adds (the inner/outer split, hence the well).
5. Weigh Pughe-Sanford et al.'s receptive-field evidence: what was measured, what the test assumes, and what it does
   not show.
6. Say what the neuron picture does and does not license for activation-space interpretability (a motivation, not a
   derivation).

What they see: a particle hopping between four wells while two rectifying "neurons" watching only its noisy readout
light up for the right pair and for the outer wells; a canonical filter that looks like a sustained low-pass and a
second that looks like a transient change detector; the OU's singular spectrum with the linear modes found by CCA
and the quadratic Hermite modes missed until quadratic features are added; canonical correlations falling as the lag
grows, until only the pair survives.

## 2. Skim path

1. Lede (header).
2. Hero figure `neurons-fig-hero`: "Two neurons read a noisy readout". Fig-sub: *A particle hops between four wells;
   two neurons see only its noisy readout, filter the last sixteen samples, and rectify: one reports the pair, the
   other the outer wells, and together they name the well.*
3. Section headings (verbatim, these are the claims):
   - "A coherent set is a region the dynamics keeps together"
   - "For Ornstein-Uhlenbeck input, the coherent-set function is linear"
   - "Past-future CCA learns the filter from the input alone"
   - "A linear filter reads the pair; rectified channels add the well"
   - "Receptive-field evidence fits the theory but does not prove it"
   - "Reading coherent sets motivates activation-space analysis; it does not derive it"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `neurons-fig-ou`, `neurons-fig-niels`, `neurons-fig-bowtie`,
   `neurons-fig-explorer` (page order).
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: coherent sets are regions the dynamics keeps together,
found as signs of singular functions of the stochastic Koopman operator; for OU input the relevant function is a
linear filter, so filter-and-rectify is set membership; the filter can be learned from the input by past-future CCA,
which is the Koopman SVD restricted to linear functions of a delay window; on the running example a linear filter
reports the pair and a filter on rectified ON/OFF channels adds the outer/inner split, giving the well; the
biological evidence is a consistency check on temporal filters, not a proof; none of this derives activation-space
methods for LLMs.

## 3. Section outline

Section ids are `neurons-<slug>`; figure ids are `neurons-fig-<slug>` (SPEC 6.5). Word counts are main-path prose
only.

Placement summary: hero between the lede and 3.1; `neurons-fig-ou` in 3.2; `neurons-fig-bowtie` and
`neurons-fig-niels` in 3.3; `neurons-fig-explorer` (centrepiece) in 3.4.

### 3.1 `neurons-sets` "A coherent set is a region the dynamics keeps together" (≈ 380 words)

Placement: the hero sits between the lede and this heading. The "Arriving here first?" aside goes at the top of this
section.

- "Arriving here first?" aside (≤ 80 words): a stochastic system acts linearly on functions of its state: the
  stochastic Koopman operator $\mathcal K_\tau$ maps a function f to its expected value τ later. Its singular
  functions, weighted by the state distribution, rank functions of the present by how well they predict functions of
  the future. Link page 3 (`#koopman`); coherent sets as spectral clustering, page 4 (`#cuts`).
- Introduce the running example in two sentences (link to the map): a particle in four wells (two pairs), readout
  $y = x_1 + x_2 + \xi$ every Δ = 0.25. The neuron on this page sees only $y_t$.
- Define a coherent pair of sets (Froyland 2013, as stated by Pughe-Sanford et al. 2025, §2): regions $\mathcal A$
  (now) and $\mathcal B$ (a lag τ later) with $\mathbb P[X_{t+\tau} \in \mathcal B \mid X_t \in \mathcal A] \approx
  1$, and equal probability, so that membership predicts the future and retrodicts the past. The best two-way split
  maximizes the sum of the two "stay" probabilities (inline; the full objective goes in the disclosure).
- Define the SKO as on page 3 (displayed equation 1): $(\mathcal K_\tau f)(x) = \mathbb E[f(X_{t+\tau}) \mid X_t =
  x]$, with inner products weighted by the state densities at t and t + τ. Its top singular pair is constant (the
  trivial set: everything). The **signs of the subdominant singular functions approximately solve the coherent-set
  problem**; this is spectral clustering of the transfer operator (pages 3 and 4; Froyland 2013; Klus & Djurdjevac Conrad 2024
  as cited by Pughe-Sanford et al.). "Approximately": the sign rounding of a relaxed problem, with the guarantees of
  page 4, not more.
- Running example: at short lag the coherent sets are the wells, at long lag only the pairs (SPEC 3.2: σ_i =
  e^{−ν_i τ}; quote the builder's λ values at τ = 0.25 and τ = 4 from `grid.json`, not typed). Link page 3 for the
  lag as resolution knob.
- The page's question: a neuron cannot compute a singular function of an operator it does not know. Pughe-Sanford et
  al. propose that sensory neurons do the next best thing: learn one from their input stream and report its sign.

Key callout: "A coherent set is defined by where the dynamics takes it, not by what it looks like now. The signs of
the leading nontrivial singular functions of the stochastic Koopman operator mark coherent sets."

Disclosures:
- "The maths: the coherent-set objective and its relaxation" (≤ 450 words): Pughe-Sanford et al.'s objective (their
  eq. 4: maximize $\mathbb P[X_{t+\tau}\in\mathcal B\mid X_t\in\mathcal A] + \mathbb P[X_{t+\tau}\in\mathcal
  B^c\mid X_t\in\mathcal A^c]$ subject to equal masses), rewritten as Rayleigh-type quotients of indicator functions
  under $\mathcal K_\tau$; replacing indicators by real functions gives the forward-backward operator $\mathcal
  F_\tau = \mathcal K_\tau\mathcal K_\tau^\dagger$ and its eigenfunctions (their eqs. 5-9). Left singular functions
  look forward (predictive sets), right ones backward (retrospective sets); for reversible dynamics such as the
  running example they coincide. Pointer to page 4 for what rounding by sign does and does not guarantee.
- "In other fields: 'coherent set' and 'receptive field'" (≤ 250 words): coherent set (finite-time, Froyland) vs
  almost-invariant / metastable set (autonomous) vs NCS coherent set (page 10) (glossary link); receptive field in
  neuroscience means the stimulus region or temporal filter that drives a cell, not a set; on this page a neuron's
  filter defines a direction and its rectified output a set.

### 3.2 `neurons-ou` "For Ornstein-Uhlenbeck input, the coherent-set function is linear" (≈ 420 words)

Placement: `neurons-fig-ou` after the third bullet.

- The OU process: $dx = Ax\,dt + \xi$, noise covariance $\mathbf D$; stationary covariance Σ solves
  $A\Sigma + \Sigma A^\top = -\mathbf D$ (Lyapunov). Pughe-Sanford et al. (§3) use it as a model of summed input to a
  neuron. Running-example instance (SPEC 3.4 warm-up): the linearization at $w_4$, $A = -\mathrm{diag}(20,
  33.\overline3)$, $\mathbf D = 2D\,I = I$, so Σ = diag(0.025, 0.015). It describes the particle's motion inside
  $w_4$ on time scales ≲ 0.1.
- The result (Pughe-Sanford et al. 2025, §3 and Supplement §3): the forward-backward operator has a family of
  eigenfunctions that are linear in the state, $v^\top x$, with $v$ an eigenvector of $e^{A^\top\tau}\Sigma^{-1}e^{A\tau}
  \Sigma$ (displayed equation 2); for attractive and repulsive dynamics the subdominant one belongs to this family; the
  others are constants or higher-degree polynomials with smaller singular values. So the leading nontrivial singular
  function is $v_1^\top x$, and its sign partitions state space by a hyperplane.
- At $w_4$ the closed form is explicit (reversible, diagonal A): singular values $e^{-\tau(20k_1 + 33.\overline3
  k_2)}$ over multi-indices $(k_1, k_2)$, eigenfunctions products of Hermite polynomials (Mehler; standard, e.g.
  Pavliotis 2014). The leading nontrivial function is $x_1 - 1$ (inward or outward along $x_1$); the next is $x_2 -
  0.6$; the **third nontrivial one is the quadratic Hermite polynomial in $x_1$** ($e^{-40\tau}$), which outranks the
  mixed term. Linear features see exactly the degree-1 sector. Show `neurons-fig-ou`, tours `linear` and
  `quadratic`.
- The neuron: store $v_1$ as synaptic weights, output $\mathbb 1[\pm v_1^\top x > 0]$ for a hard membership index,
  or the rectified $\max(0, \pm v_1^\top x)$ for a graded one. Two cells, ON and OFF, cover the two sets
  (Pughe-Sanford et al. §5.2 read the retina's ON/OFF split this way). Displayed equation 3: $r^\pm(t) = \max(0,
  \pm\, a^\top p_t)$.
- Scale honesty: at the running example's sampling interval Δ = 0.25 the within-well singular values are $e^{-5}
  \approx 0.007$ (tour `atDelta`): inside a well, coherence is gone long before the next sample. This is "detail
  inside a well" (SPEC 3.2).
- Saddles, in one paragraph: Pughe-Sanford et al.'s central case is a saddle point (their Fig. 1b,c), where the
  predictive set is set by the unstable direction and the retrospective set by the stable one, so predictive and
  retrospective neurons need different filters. The running example has saddles at $(0, \pm 0.6)$ (one unstable
  direction, which pair to fall into). The authors list linking the saddle analysis to the spectral-clustering
  framework as open (their Discussion, issues i-iii); the page describes this case and does not compute it.

Key callout: "For OU input, filter-and-sign is exact coherent-set membership: the leading nontrivial singular
function is linear. The next ones are Hermite polynomials, which no linear filter can represent."

Disclosures:
- "The maths: why the linear family closes" (≤ 500 words): the generator and its adjoint map linear functions to
  linear functions (Supplement §3.1: $\mathcal L^\dagger(\theta^\top x) = (A^\top\theta)^\top x$, and the reweighted
  forward operator gives $(\Sigma^{-1}A\Sigma\theta)^\top x$), so $\mathcal F_\tau$ restricted to linear functions is
  the matrix of equation 2; degree-k polynomials map to degree-k plus lower (their §3.3), so each degree contributes
  its own eigenvalues, products of degree-1 ones. For the reversible case at $w_4$, the Mehler/Hermite expansion gives
  the closed form above. State the scope: Pughe-Sanford et al. prove the subdominant function is linear for
  attractive and repulsive dynamics; their higher-degree analysis does not treat saddles.
- "Hypotheses: what 'exact' means here" (≤ 250 words): exact for the sets defined by the sign of the leading
  function; whether those sets are good coherent sets is the relaxation question of 3.1; at an attractive, nearly
  isotropic point the partition is not distinguished (Pughe-Sanford et al. §3), which is why the anisotropy 20 vs
  33.3 matters at $w_4$.

### 3.3 `neurons-cca` "Past-future CCA learns the filter from the input alone" (≈ 450 words)

Placement: `neurons-fig-niels` after the second bullet; `neurons-fig-bowtie` after the fourth.

- Galerkin projection (Pughe-Sanford et al. §4; Klus et al. 2018): restrict the SKO to the span of chosen features
  $\phi$; with covariances $\Sigma_0 = \mathbb E[\phi\phi^\top]$ and $\Sigma_\tau = \mathbb E[\phi(X_t)\phi(X_{t+\tau})^\top]$
  the matrix is $K_\tau = \Sigma_0^{-1}\Sigma_\tau$ and the forward-backward matrix is
  $\Sigma_0^{-1}\Sigma_\tau\Sigma_0^{-1}\Sigma_{-\tau}$ (displayed equation 4). Its eigenvectors are exactly the
  past-future CCA directions. For stable OU with linear features the Galerkin answer equals the analytic one
  (Supplement §6, Proposition 1).
- Delay windows as the features: a neuron with one input keeps a history. Past window $p_t = (y_t, y_{t-1}, \dots,
  y_{t-m+1})$ (most recent first), future window $f_t = (y_{t+g+1}, \dots, y_{t+g+m})$ (earliest first), gap g ≥ 0
  samples. Then $C_{pf}[i,j] = c(i+j+1+g)$, with c the autocovariance of y: **the past-future cross-covariance is a
  Hankel matrix** (displayed equation 5). Show `neurons-fig-niels`: the programme author's whiteboard of the same
  idea (a trajectory Hankel matrix whose columns predict the next column; "choose the weights based on the SVD").
- Whitening both sides and taking the SVD is CCA (displayed equation 6): $M = C_{pp}^{-1/2}C_{pf}C_{ff}^{-1/2} =
  \sum_i \sigma_i\, u_i w_i^\top$, past filters $a_i = C_{pp}^{-1/2}u_i$. Including the constant feature adds $\sigma_1
  = 1$; the nontrivial canonical correlations are $\sigma_2 \ge \sigma_3 \ge \dots$ (SPEC appendix A convention; say
  once). This is page 3's whitened Koopman SVD (VAMP) restricted to linear functions of the window (edge E4 lives on
  page 3; link, no card).
- What is optimal (and relative to what): within the window dictionary, page 3's bounds hold: the rank-r truncation
  of M has operator-norm error $\sigma_{r+1}$, and the top-r directions maximize the VAMP-2 score among
  r-dimensional feature pairs built from the dictionary. For jointly Gaussian windows the canonical filter is also the
  one-dimensional summary of the past that carries the most information about the future window: mutual information
  $-\tfrac12\sum_i\log(1-\sigma_i^2)$ (Gel'fand & Yaglom), and the Gaussian information bottleneck's optimal projections lie along
  CCA directions, with β-dependent scales and noise (Chechik et al. 2005, cited by Pughe-Sanford et al. as the closest
  prior framework): the same directions, not the same compression. For non-Gaussian
  input, such as y here, the guarantee is about correlation, not information. Show `neurons-fig-bowtie`.
- Takens, in two sentences: delay windows are often justified by Takens's theorem, which gives a generic embedding of
  deterministic smooth dynamics; it says nothing about linearity and does not cover noise. Here the windows are
  simply a dictionary; for linear Gaussian processes, Akaike (1975) shows that canonical variables of the **whole**
  past and future form a minimal Markovian state, which is the exact version of the idea: finite-dimensional, but in
  general a function of the entire past, not of a fixed finite window.
- Learning it locally: the authors cite network models that compute CCA online with local plasticity (Lipshutz et al.
  2021; Pehlevan et al. 2020: multicompartment neurons, feedforward rules the authors call non-Hebbian, anti-Hebbian
  lateral connections; the CCA solution is a fixed point, convergence shown numerically for several channels). Link
  page 8 (edge E15) for a different local rule and what it computes instead.

Key callout: "The filter comes from the input's own statistics: whiten the past and future windows, take the SVD of
their cross-covariance. That is the Koopman SVD restricted to linear functions of the window."

Disclosures:
- "Why this holds: CCA is spectral clustering of time points" (≤ 500 words): with $X_p$, $X_f$ the stacked windows (a
  trajectory Hankel matrix and its shifted copy), the canonical variate $z = X_p a$ satisfies $\Pi_p\Pi_f z =
  \sigma^2 z$, with $\Pi_p = X_p(X_p^\top X_p)^{-1}X_p^\top$ the projection onto past features (standard CCA
  algebra; Hardoon, Szedmak & Shawe-Taylor 2004). So canonical variates are eigenvectors of a forward-backward
  similarity between time points, and their signs cluster the input patterns: this is the sense of the whiteboard's
  caption ("the SVD of the delay-embedding Hankel matrix is spectral clustering on input patterns"). Caveat stated:
  $\Pi_p\Pi_f$ is not a nonnegative graph, so this is spectral embedding by a product of projections, not Laplacian
  spectral clustering; the plain (unwhitened) SVD of the trajectory Hankel is PCA of windows, which ranks by variance,
  not by predictability.
- "Hypotheses: delay embeddings, Takens, and noise" (≤ 400 words): Takens (1981, Thm 1): generic smooth observable of a
  smooth diffeomorphism on a compact m-manifold, 2m + 1 delays; deterministic; no linearity (SPEC appendix D). For a
  stochastic process, keep three objects apart: the hidden state; a finite-dimensional filtering or predictive state
  (for an observable linear Gaussian state-space model, the Kalman-filter state, or Akaike's canonical variables of
  the whole past; their number equals the number of nonzero canonical correlations, Akaike 1975); and a finite window
  of raw observations, which is a dictionary and in general only approximates the predictive state. The predictive
  state is finite-dimensional but usually needs the entire past: a scalar readout of a multidimensional linear system
  is in general ARMA, not finite-order AR (Granger & Morris 1976). Example in one line: the sum of two independent
  stationary sampled OU coordinates with decay factors a ≠ b has covariance ∝ $a^{|k|} + b^{|k|}$; the positive-lag
  recurrence suggests AR coefficients a + b, −ab, but the lag-one Yule-Walker equation fails, so no two-lag window is an
  exact state. Pughe-Sanford et al.'s eqs. 19-21 state an exact finite lag-vector state for observable linear
  Gaussian systems; the page does not repeat that claim. For
  the running example (nonlinear, noisy readout) none of this applies exactly; the window dictionary is a modelling
  choice and the optimality statement is relative to it. Why the windows must not overlap: overlapping coordinates are
  perfectly correlated with themselves and give trivial canonical correlations of 1; the page uses g ≥ 0.
- "The maths: maximal predictiveness for Gaussian windows" (≤ 300 words): Gel'fand-Yaglom formula; the top canonical
  filter maximizes $I(a^\top p; f)$ over linear one-dimensional summaries a; Gaussian IB reduces to CCA (Chechik et
  al. 2005). Not true in general for non-Gaussian inputs.

### 3.4 `neurons-example` "A linear filter reads the pair; rectified channels add the well" (≈ 450 words)

Centrepiece: `neurons-fig-explorer`, placed after the first bullet.

- Run past-future CCA on the running example's readout (live from the precomputed long signal). Tour `pair` (linear
  windows, m = 16, g = 0): one strong nontrivial canonical correlation and a weak second (builder values; spec-time
  check: $\sigma_2 \approx 0.935$, $\sigma_3 \approx 0.14$, then ≈ 0.006). The first filter is a sustained,
  recency-weighted low-pass; its sign agrees with the pair label almost always (builder value; spec-time ≈ 0.99). The
  second is a transient filter contrasting recent with older samples. Point out that this sustained/transient pair is
  what Pughe-Sanford et al. found on their "dead leaves" stimulus (§5.1), here on a different signal.
- Why not the well: y adds $x_1$ and $x_2$, so a linear function of the window cannot separate "which well in the
  pair" from "which pair" (the inner wells read ±0.4, the outer ±1.6). The within-pair direction appears only weakly
  (the transient filter's correlation with the within-pair label is moderate; builder value). This is the
  linear-sector limitation of 3.2 in another guise.
- Tour `onoff`: give the neuron the ON and OFF rectified copies of its input, $\max(0, y)$ and $\max(0, -y)$, as
  upstream rectifying cells would, and run the same CCA on windows of both channels. A strong new direction appears
  (builder; spec-time $\sigma_3 \approx 0.77$): it separates the outer wells ($w_1, w_4$, $|y| \approx 1.6$) from the
  inner ones ($w_2, w_3$, $|y| \approx 0.4$), the running example's product mode. The pair neuron and this "outer"
  neuron jointly name the well (builder agreement; spec-time ≈ 0.95), by sign combination: two binary cells, four
  sets. This is the Galerkin route of 3.3 with a richer dictionary, and the hierarchical composition Pughe-Sanford et
  al. suggest (rectified outputs as features for the next cell).
- Make the instrument point (one paragraph): on position-space operators the order is pair, then the two within-pair
  splits (SPEC 3.2); through this readout the order is pair, then outer/inner, then a transient. **What a neuron can
  learn is set by its dictionary and its input, not only by the dynamics.** The builder labels each direction; the
  page uses the builder's labels.
- Tour `longlag` (gap 64 samples = 16 time units): the outer/inner correlation collapses and only the pair survives,
  as in SPEC 3.2 (short lags certify wells, long lags only pairs).
- Tour `reverse`: the future-side filters are the time-reverses of the past-side ones (tile: reflection residual).
  For a scalar stationary input with linear windows this is automatic (autocovariances are symmetric); with ON/OFF
  channels it holds here because the dynamics are reversible. **The running example cannot show predictive versus
  retrospective neurons;** that needs irreversible dynamics or the saddle case of 3.2.
- Tour `fewdata` (N = 10³ samples): canonical correlations are biased upward; the null floor (canonical correlations
  between windows 5,000 samples apart) shows the level below which nothing can be trusted. Sample CCA needs
  regularization when windows are long (ridge control).

Key callout: "Through this readout, one linear neuron can learn the pair but not the well. Feeding it rectified ON
and OFF channels lets a second neuron learn the outer/inner split, and the two signs together name the well."

Disclosures:
- "The maths: covariances of windows from one long signal" (≤ 300 words): stationarity gives Toeplitz $C_{pp}$,
  $C_{ff}$ and Hankel $C_{pf}$ from the auto- and cross-covariance functions of the channels; the explorer estimates
  those functions once per dictionary and assembles every (m, g) from them.
- "Why the well needs a nonlinear channel" (≤ 300 words): with $y = x_1 + x_2 + \xi$ and independent coordinates at
  κ = 0, $\mathrm{Cov}(y_{t-k}, \mathrm{sign}\,x_{2,t})$ and $\mathrm{Cov}(y_{t-k}, \mathrm{sign}\,x_{1,t})$ are both
  carried by the same linear window; the product mode $\mathrm{sign}\,x_1\,\mathrm{sign}\,x_2$ is a function of
  $|y|$, which $\max(0,y) + \max(0,-y)$ supplies linearly. Connect to 3.2's Hermite statement: the product mode is a
  degree-2 function of the two slow coordinates.

### 3.5 `neurons-evidence` "Receptive-field evidence fits the theory but does not prove it" (≈ 380 words)

No figure (third-party figures are linked, not embedded: SPEC 7.1). A small HTML table summarizes the evidence.

- What the theory predicts about neurons (Pughe-Sanford et al. §5): temporal filters are canonical directions of the
  neuron's input; responses are rectified (ON/OFF); there are predictive and retrospective cells, which at a 2-D
  saddle have filters orthogonal to the attracting (respectively repelling) direction. In lag coordinates, attracting
  modes are decaying exponentials and repelling modes growing ones, so the authors test each measured filter's cosine
  similarity with exponentials $e^{\alpha t}$ and look for the orthogonal one.
- The evidence, as reported (table, all from Pughe-Sanford et al. 2025): (1) synthetic "dead leaves" stimulus: CCA on
  10-sample windows gives a low-pass and a smoothed-derivative filter, qualitatively like sustained and transient
  bipolar cells (a salamander bipolar flash response, shared with the authors) and fly L1-L3 neurons; (2) 204
  tufted/mitral cells of the rat olfactory bulb, odour kernels fitted as Gabor functions: about half orthogonal to a
  decaying exponential (read as predictive), about 4% orthogonal to a growing one (retrospective), about a third to
  both; (3) 1,345 retinal ganglion cells (temporal component from a rank-1 SVD of each spatio-temporal receptive field,
  which captured about 60% of variance): most read as predictive, about 1% retrospective; (4) lagged and non-lagged
  cells of the lateral geniculate nucleus, compared qualitatively with published recordings. These are reanalyses of
  existing data, not new recordings.
- How to weigh it: the orthogonality test was derived for 2-D saddle dynamics; applying it to measured filters is an
  interpretation. The data show filters consistent with the predicted shapes; they do not show that the filters are
  the canonical directions of each cell's natural input, which would need the input statistics. The authors list
  their own open issues (unstable modes, data-driven estimation along unstable directions, more than two dimensions,
  feedback). Phrase every reading as a reading ("can be read as predictive").
- Local learnability: one paragraph pointing to 3.3's CCA network models and to page 8 (E15).

Key callout: "The evidence is that measured temporal filters have the shapes the theory predicts. It is not a
measurement that neurons compute canonical directions of their own inputs."

Disclosure "The orthogonal-exponential test, step by step" (≤ 350 words): normalized exponentials over the filter's
support, α swept over [−10, 10] (olfactory) or [−30, 30] (retina), cosine similarity, zero crossing = orthogonal
exponential, sign of the best-aligned α; kernel preprocessing (magnitudes below 0.005 set to zero, unit ℓ² norm).
Supplement §7 of the paper.

### 3.6 `neurons-limits` "Reading coherent sets motivates activation-space analysis; it does not derive it" (≈ 220 words)

- Beyond OU the neuron's filter is a Galerkin approximation: exact only within its dictionary, and the dictionary
  decides what can be seen (3.4). Stochasticity: no Takens theorem is used.
- The programme's step (SPEC 2.2 E22; Slouching post part III.b): if a neuron's receptive field is a coherent set of
  its input history, it is natural to look for coherent structure among data points in a network's activations
  (page 10's NCS). Mark this paragraph with the section 8 hook: `<span class="status"
  data-status="schematic">…</span>`. State plainly: a motivation, not a derivation; nothing on this page is about
  LLM neurons; expansion coding likewise motivates and does not derive (SPEC appendix D).
- Quote, with attribution to the programme's author and as their compression rather than the site's voice: "the
  receptive field of a neuron is a coherent set of its input-space" (Slouching post III.b), immediately followed by
  the scope sentence above.

Key callout: "Neurons that report coherent sets are a reason to look for coherent sets in activations, not evidence
that networks contain them."

### 3.7 `neurons-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.8 `neurons-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.9 `neurons-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C7.1 | A coherent pair of sets is a pair of regions the dynamics carries into each other with high probability over a lag; the signs of subdominant SKO singular functions approximately maximize the two-set coherence objective. | theorem (relaxation) | Froyland 2013; Pughe-Sanford et al. 2025 §2 (eqs. 4-9); page 4 for rounding | compact forward-backward operator; "approximately" = sign rounding of a relaxation | 3.1 |
| C7.2 | In the running example, coherent sets are wells at short lag and pairs at long lag. | builder values | `grid.json` eigenvalues at τ = 0.25, 4 (SPEC 3.2) | reversible dynamics, so singular = eigen | 3.1 |
| C7.3 | For an OU process the forward-backward operator has linear eigenfunctions $v^\top x$ with v solving equation 2; for attractive and repulsive dynamics the subdominant eigenfunction is in this family; the others are constants or higher-degree polynomials. | theorem | Pughe-Sanford et al. 2025 §3, Supplement §3 | stationary OU; real eigenvalues and eigenvectors of A; higher-degree analysis excludes saddles | 3.2 |
| C7.4 | At $w_4$ the SKO singular values are $e^{-\tau(20k_1+33.\overline3k_2)}$ with Hermite-product singular functions; the leading nontrivial one is linear; linear features recover exactly the degree-1 sector; adding quadratic features recovers the degree-2 sector. | standard (Mehler/Hermite) + widget | `neurons-fig-ou` tours `linear`, `quadratic`; Pavliotis 2014 | reversible OU (diagonal A, isotropic noise); finite-sample estimates | 3.2 |
| C7.5 | Filter-and-sign (or rectify) with the leading function computes membership of the sets defined by its sign, exactly for OU. | construction | 3.2; `neurons-fig-ou` panel (a) | sets defined by thresholding the leading function at its mean | 3.2 |
| C7.6 | At the running example's sampling interval, within-well coherence is negligible ($e^{-5}$). | widget (closed form) | `neurons-fig-ou` tour `atDelta` | local OU approximation of the well | 3.2 |
| C7.7 | Galerkin projection of the SKO on features φ gives $K_\tau = \Sigma_0^{-1}\Sigma_\tau$; the eigenvectors of the forward-backward matrix are past-future CCA directions; for stable OU with linear features this equals the analytic solution. | theorem | Pughe-Sanford et al. §4, Supplement §§5-6 (Prop. 1); Klus et al. 2018 | stationarity; finite dictionary (optimality relative to it) | 3.3 |
| C7.8 | The past-future cross-covariance of delay windows is a Hankel matrix of the autocovariance. | construction | 3.3 equation 5; `neurons-fig-niels` | stationarity; window ordering as defined | 3.3 |
| C7.9 | Within the window dictionary, rank-r truncation of the whitened cross-covariance has operator-norm error $\sigma_{r+1}$, and the top-r canonical pairs maximize the VAMP-2 score among r-dimensional dictionary feature pairs. | theorem | page 3 ledger; Wu & Noé 2020; Eckart-Young | relative to the dictionary; sample estimates add error (C7.17) | 3.3 |
| C7.10 | For jointly Gaussian windows the mutual information between past and future is $-\tfrac12\sum\log(1-\sigma_i^2)$ and the Gaussian information bottleneck's optimal projections lie along CCA directions (β-dependent scales and noise; same directions, not the same compression). | theorem (standard) | Gel'fand & Yaglom 1957/1959; Chechik et al. 2005 | Gaussianity (does not hold for y here) | 3.3 |
| C7.11 | Takens's theorem gives a generic embedding of deterministic smooth dynamics and says nothing about linearity or noise; for linear Gaussian processes, past-future canonical variables give a minimal Markovian state. | theorem (scope-limited) | Takens 1981 Thm 1; Akaike 1975 | Takens: compact manifold, smooth diffeomorphism, generic observable, 2m+1 delays; Akaike: finite-dimensional linear Gaussian | 3.3 |
| C7.12 | Network models compute CCA online with local plasticity (multicompartment neurons; feedforward rules the authors call non-Hebbian; anti-Hebbian lateral weights); the CCA solution is a fixed point, convergence shown numerically for several channels. | theorem (fixed point) + empirical (cited) | Pehlevan et al. 2020; Lipshutz et al. 2021 | linear neurons; centred inputs; their objectives | 3.3 |
| C7.13 | On the running example with linear windows (m = 16), one strong nontrivial canonical direction (sustained, ≈ pair) and one weak transient direction appear; the first filter's sign agrees with the pair label (builder value). | widget + builder values | `neurons-fig-explorer` tour `pair`; `p07.json` | stationarity; sample estimate from 10⁵ samples; labels for scoring only | 3.4 |
| C7.14 | A linear window of $y = x_1 + x_2 + \xi$ cannot represent the within-pair split separately from the pair; ON/OFF channels add an outer/inner direction (product mode); pair and outer neurons jointly give the well (builder agreement). | widget + builder values | explorer tour `onoff`; disclosure "Why the well needs a nonlinear channel" | κ = 0 (independent coordinates) for the disclosure argument; builder labels for meanings | 3.4 |
| C7.15 | At long lag only the pair direction keeps a large canonical correlation. | widget | explorer tour `longlag` | — | 3.4 |
| C7.16 | For a scalar stationary input with linear windows, future-side filters are time-reverses of past-side ones; with ON/OFF channels this holds here because the dynamics are reversible; so the example cannot show predictive versus retrospective cells. | construction + widget | 3.4; explorer tour `reverse` (reflection residual tile) | stationarity; reversibility for the multichannel case | 3.4 |
| C7.17 | Sample canonical correlations are biased upward at small N; a null floor shows the untrustworthy range; long windows need regularization. | standard + widget | explorer tour `fewdata`; standard CCA sampling theory | — | 3.4 |
| C7.18 | Pughe-Sanford et al. report: dead-leaves CCA filters resembling sustained/transient cells; among 204 olfactory tufted/mitral cells about half read as predictive, ≈ 4% retrospective, ≈ a third orthogonal to both; among 1,345 retinal ganglion cells most read as predictive, ≈ 1% retrospective; LGN lagged/non-lagged cells compared qualitatively. | empirical (cited) | Pughe-Sanford et al. 2025 §5, Supplement §7 | reanalysis of existing data; test derived for 2-D saddles; filters parametrized (Gabor) or rank-1 approximations (≈ 60% variance) | 3.5 |
| C7.19 | The evidence shows filter shapes consistent with the theory, not that neurons compute canonical directions of their own inputs. | construction (argument) | 3.5 | — | 3.5 |
| C7.20 | Neurons that read coherent sets motivate looking for coherent structure among data points in activation space; they do not derive it. | motivation (section 8 hook) | E22; Slouching post III.b | — | 3.6 |

Things not to claim on this page (SPEC appendix D): the singular functions of an OU process are linear / linear CCA
recovers the Koopman SVD; Takens makes any series linear with enough delays; expansion coding (or neurons reading
coherent sets) derives activation-space analysis; activation cells are coherent sets; coherent sets are a network's
computational states; the generator's slow modes are the readout-window table's singular directions.

## 5. Figures and widgets

### 5.1 `neurons-fig-hero` "Two neurons read a noisy readout" (live, hero; key `hr`)

- **Purpose:** filter-and-rectify units that see only a noisy scalar readout report coherent-set membership: one the
  pair, one the outer wells, together the well.
- **Layout:** `figure.fig.full.card`, three panels left to right (stacked on phones):
  (a) contour map of V over Ω (as page 1's hero: ink contours, wells as ink-outlined circles in `--c-well-k`,
  labelled $w_1..w_4$), the particle as a dot with a fading 2-time-unit trail;
  (b) the readout $y_t$ over the last 64 samples (line, x = sample index relative to now), with the last m = 16
  samples (the neuron's window) shaded; beneath it, aligned to the window, two small stem plots of the filters the
  neurons use (pair filter in ink; outer filter as two stems per lag, ON channel solid and OFF channel hollow);
  (c) four rectified outputs over the same 64 samples as filled traces: "pair ON" (`--c-pair-R`), "pair OFF"
  (`--c-pair-L`), "outer ON" and "outer OFF" (ink and `--c-other`); below them two thin strips: the true well
  (colour `--c-well-k`) and the well named by the two neurons' signs (same colours; mismatches outlined in accent).
- **Data:** live. Face A simulation from `lib/example.js` (Euler-Maruyama, dt = 0.0025, seed 0, readout noise drawn
  from the same seeded stream). Filters, channel means and orientation signs from `data/neurons/p07.json`
  (`hero.filters`: the builder's linear m = 16 direction 2 filter, and the ON/OFF m = 16 direction for the outer/inner
  split; each with the feature means to centre with and a sign so that positive means "right pair" / "outer wells").
- **Controls:** transport (play/pause, speed ×1/×4/×16), reset. Nothing else.
- **Default state (= first tour):** `default`, t = 0, autoplay when scrolled into view; under reduced motion the
  `frame-late` still is shown.
- **What changes:** the particle moves; y scrolls; the window slides; outputs rise and fall; the strips extend.
- **Tours:** `default` (t = 0, playing); `frame-switch` (16 samples after the first pair switch in the seed-0 run,
  so the pair neuron has just flipped); `frame-late` (after 4,000 samples). The builder records the seed-0 sample
  indices in `p07.json` (`hero.events`).
- **fallbackTour:** `frame-late`.
- **Caption:** *Plotted:* (a) contours of $V(x_1,x_2)$, wells $w_1..w_4$, the particle's last 2 time units of path;
  (b) readout $y_t = x_1 + x_2 + \xi_t$ against sample index (now = 0), the window of the last 16 samples shaded;
  below, the filter weights against lag (0 = most recent); (c) rectified outputs $\max(0, \pm z_t)$ of the pair unit
  ($z_t$ = filter · centred window of y) and the outer unit (filter · centred window of the channels $\max(0,y)$,
  $\max(0,-y)$); strips: true well and the well named by the two signs. *Values:* $h_x = 2.5$, $h_y = 1.5$, $b =
  0.6$, $D = 0.5$, $\sigma_y = 0.25$, Δ = 0.25, m = 16, filters from past-future CCA on $10^5$ samples (builder),
  seed 0. Running example, face A. `synthetic`.
- **Static fallback:** `assets/fallback/neurons-fig-hero-frame-late.png`; GIF `assets/fallback/neurons-fig-hero.gif`
  (≈ 6 s at ×4 from `frame-switch`).
- **Accessibility:** alt text: "A particle moving between four wells; its noisy readout; two rectifying units whose
  outputs follow which pair and whether the particle is in an outer well, with strips comparing the named well to the
  true one." Colour is not the only carrier: the strips carry $w_1..w_4$ labels on hover and a legend.
- **Performance:** ≤ 2 ms per frame (one particle, 100 substeps per sample at ×1; two dot products of length ≤ 32 per
  sample).

### 5.2 `neurons-fig-ou` "The OU singular spectrum, and what linear features see" (live; key `ou`)

- **Purpose:** for OU input the leading nontrivial singular function is linear and CCA on linear features finds the
  degree-1 sector exactly; the quadratic Hermite modes need quadratic features.
- **Layout:** `figure.fig.wide.card`, `ui.simLayout`: main view two panels side by side (stacked on phones), side
  panel with tours, controls, tiles.
  (a) **The sets:** the plane around $w_4$ in local coordinates $(x_1 - 1, x_2 - 0.6)$, axes ±0.5; stationary
  ellipses at 1 and 2 standard deviations (ink); 1,000 of the simulated points as dots coloured by the sign of the
  estimated leading canonical variate (ink for positive, `--c-other` for negative; well colours are not used, since
  both sets lie inside $w_4$); the estimated separating line (accent) and the analytic one (dashed ink).
  (b) **The spectrum:** analytic singular values $e^{-\tau(20k_1 + 33.\overline3k_2)}$ for all $(k_1,k_2)$ with
  $1 \le k_1 + k_2 \le 3$, sorted, as bars; bars coloured by degree (degree 1 ink, degree 2 `seq-3`, degree 3
  `seq-5`), labelled with the multi-index on hover ("$x_1$", "$x_2$", "$\mathrm{He}_2(x_1)$", "$x_1x_2$", ...);
  estimated canonical correlations from the chosen dictionary as open circles placed on the bars they match (by
  maximum correlation of the estimated variate with the analytic function, computed on the sample).
- **Data:** live. Exact discretization of the OU: $x_{t+\tau} = e^{A\tau}x_t + \eta_t$, $\eta_t \sim N(0, \Sigma -
  e^{A\tau}\Sigma e^{A^\top\tau})$, A and Σ from SPEC 3.4 (closed form), seeded by `lib/rng.js`; pairs $(x_t,
  x_{t+\tau})$ from one stationary chain sampled at interval τ; CCA by `lib/cca.js`.
- **Controls (primary):** lag τ (log slider 0.002-0.3, default 0.02, mark at 0.25 "Δ"); samples N (`10³` | `10⁴` |
  `10⁵`, default `10⁴`); dictionary (`linear` | `linear + quadratic`). Advanced: seed (0-2).
- **What changes:** τ rescales every analytic bar and resimulates; N resimulates (estimates scatter more at small N);
  dictionary adds the three quadratic monomials (centred) to both sides, so up to five circles appear (degree-1 and
  degree-2 bars matched).
- **Stat tiles:** "$\sigma_2$ analytic / estimated"; "angle between estimated and analytic leading filter" (degrees);
  "modes found" (count of circles within 0.05 of a bar); "persistence" = fraction of sample pairs whose sign of the
  leading analytic function is unchanged after τ (the coherence of the two sets, empirical).
- **Tours:** `linear` (default: τ = 0.02, N = 10⁴, linear; note "Linear features find the two degree-1 modes; the
  third bar, the quadratic Hermite mode in $x_1$, is missed."); `quadratic` (same, linear + quadratic; note "With
  quadratic features the degree-2 modes appear too."); `atDelta` (τ = 0.25, N = 10⁴, linear; note "At the running
  example's sampling interval the within-well singular values are below 0.01: no coherence left inside a well.");
  `fewdata` (τ = 0.02, N = 10³, linear; note "With 1,000 pairs the estimates scatter.").
- **fallbackTour:** `linear`.
- **Caption:** *Plotted:* (a) samples of the stationary OU process linearized at $w_4$, local coordinates, coloured by
  the sign of the estimated leading canonical variate; ellipses at 1 and 2 standard deviations of Σ; estimated
  (solid) and analytic (dashed) zero line of the leading singular function; (b) analytic SKO singular values
  $e^{-\tau(20k_1+33.\overline3k_2)}$, $1 \le k_1+k_2 \le 3$ (bars, colour = polynomial degree), and canonical
  correlations estimated from N sample pairs with the chosen features (circles). *Values:* $A = -\mathrm{diag}(20,
  33.\overline3)$, noise covariance $I$ ($D = 0.5$), Σ = diag(0.025, 0.015); τ, N, features and seed as set. OU
  warm-up of the running example at $w_4$ (SPEC 3.4). `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/neurons-fig-ou-<tour>.png`); not animated.
- **Accessibility:** alt text: "Scatter of points around a well split by a line into two coherent sets, and a bar
  chart of singular values in which linear features find the first two bars but not the third." Panel (b) bars carry
  text labels for degree.
- **Performance:** simulation of 10⁵ pairs plus CCA on ≤ 5 features: < 30 ms. Parity: `lib/cca.js` CCA against the
  builder's NumPy CCA on a fixed sample to 1e-10.

### 5.3 `neurons-fig-niels` "Niels the Neuron" (static image, reused with credit)

- **Purpose:** the programme author's whiteboard statement of the page's idea: a neuron predicting its next input
  from a weighted sum of past inputs, the trajectory Hankel matrix whose columns predict the next column, weights
  chosen by an SVD.
- **Data / content:** the image `niels-hankel.jpg` from `crw-blog` (`origin/main`,
  `assets/images/lw/Gradients-and-Circuits/niels-hankel.jpg`), copied to `site/assets/fig/neurons/niels-hankel.jpg`
  with a provenance note (`site/assets/fig/neurons/README.md`: source path, commit, licence as the blog's). SPEC 7.1
  permits this reuse with credit. Width: `figure.fig.narrow`.
- **Caption:** *Plotted:* whiteboard sketch: a neuron receives its input sequence $I(t - n\Delta t)$ and tries to
  predict $I(t+\Delta t) \approx \sum_n w_n I(t - n\Delta t)$; below, the trajectory Hankel matrix with rows $(I_1,
  I_2, \dots)$, $(I_2, I_3, \dots)$; "column n predicts column n+1"; "choose $w_n$ based on the SVD". *Credit:*
  whiteboard by the programme's author, from "Slouching Towards Interpretability" (Nov 2026), part III.b, after
  Pughe-Sanford et al. 2025.
- **Fig-sub:** *The neuron's filter comes from an SVD of its own input history arranged as a Hankel matrix; this page
  whitens both sides first, which turns the SVD into past-future CCA.*
- **Fallback:** the image itself; alt text: "Hand-drawn whiteboard: Niels the Neuron predicts its next input from a
  weighted sum of past inputs; a Hankel matrix of the input sequence; the weights are chosen from its SVD."

### 5.4 `neurons-fig-bowtie` "Delay windows to future observations" (static SVG; key `bw`)

- **Purpose:** the page's map is past window → future window through a knot whose bars are canonical correlations.
- **Data:** shared `bowtie` component (SPEC 1.4) with labels: left "delay windows of the input", left norm "whitened
  covariance", right "future observations", right norm "whitened covariance", knot bars = σ₁..σ₆ of the ON/OFF
  dictionary at m = 16, g = 0 (`p07.json`, `cca.onoff_m16_g0.sigmas`; σ₁ = 1 for the constant), r = 3, bound label
  "lost: σ_{r+1} (operator norm, within the window dictionary)".
- **Controls:** none required; if the component's draggable r is enabled, dragging r updates the hatching and label
  (no URL state).
- **Caption:** *Plotted:* schematic of $M = C_{pp}^{-1/2}C_{pf}C_{ff}^{-1/2}$ for windows of the channels
  $\max(0, y)$, $\max(0, -y)$; bars are its singular values (σ₁ = 1 is the constant function). *Values:* m = 16,
  g = 0, $10^5$ samples. Running example, face A.
- **Fig-sub:** *Past windows map to future observations through a few canonical directions; dropping the rest costs at
  most the next canonical correlation, within the window dictionary.*
- **Fallback:** the SVG; PNG export `assets/fallback/neurons-fig-bowtie-default.png`.

### 5.5 `neurons-fig-explorer` "Canonical filters of the running example's readout" (live, centrepiece; key `cx`)

- **Purpose:** what past-future CCA on delay windows learns from the readout, how that depends on the dictionary, the
  window, the lag and the data, and how well rectified outputs report pair, outer/inner and well.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view a 2 × 2 grid; side panel (320 px) with tours,
  controls, tiles, legend.
  - (a) **Filters:** the past-side filters $a_2, a_3, a_4$ against lag k = 0..m−1 (0 = most recent), one small line
    chart each; for the ON/OFF dictionary two lines per filter (ON solid, OFF dashed). Optional overlay (advanced
    toggle, and on in tour `reverse`): the future-side filters $b_i$ (dotted), drawn against distance from the present
    (k = 0 is the first future sample), so that a mirror-image filter lies on top of $a_i$. A short note under the
    panel says: a retrospective cell reading its own window (most recent first) would use $b_i$ reversed in time.
  - (b) **Spectrum:** σ₂..σ₉ as bars (σ₁ = 1 omitted; the axis says so), coloured by the builder's computed label for
    that direction under the current dictionary, m and g if available (labels: "pair" `--c-pair-R` tint, "outer/inner"
    `--c-well-4` tint, "transient" ink, "other" `--c-other`); for settings the builder did not label, the page labels
    live by the same rule (below) and marks the label "live". Dashed line: the null floor (largest canonical
    correlation between windows 5,000 samples apart, same N, m, dictionary).
  - (c) **Outputs:** a 200-sample stretch (advanced: start index): y (thin ink line), rectified outputs of directions
    2 and 3 ($\max(0,\pm z)$, filled, ON above the axis and OFF below), and two strips: true well and the well named
    by signs of directions labelled "pair" and "outer/inner" (blank if either is missing).
  - (d) **Agreement:** a 4 × 4 table, rows = true well, columns = named well, cells = counts over all N samples (`seq`
    map); shown only when both a "pair" and an "outer/inner" direction exist, otherwise a 2 × 2 table of the pair
    neuron's sign against the true pair.
- **Data:** `data/example/signal.json` (SPEC 3.6: $10^5$ samples of y, Float32, and the true basin label of each
  sample). Covariance functions of the chosen channels estimated live once per
  dictionary and N (`lib/cca.js`), windows assembled for each (m, g) by Toeplitz/Hankel indexing; CCA by whitening
  (eigendecomposition with ridge) and SVD. Labels: pair = sign $x_1$; within-pair = sign $x_2$; outer/inner = sign
  $x_1 \cdot$ sign $x_2$; well = quadrant. Direction labelling rule (builder and live): a direction is "pair",
  "outer/inner" or "within-pair" if the absolute correlation of its variate with that label exceeds 0.5 and is the
  largest of the three; "transient" if none exceeds 0.5 and its filter changes sign along the lag; else "other".
- **Controls (primary):**
  1. dictionary: `linear` (windows of y) | `on-off` (windows of $\max(0,y)$ and $\max(0,-y)$);
  2. window m: `4` | `8` | `16` | `32`;
  3. gap g (samples between windows): `0` | `4` | `16` | `64` (labels also in time units: 0, 1, 4, 16);
  4. data N: `10³` | `10⁴` | `10⁵`.
  Advanced: ridge (relative to the mean eigenvalue of $C_{pp}$; 0, 1e-6, 1e-4, 1e-2; default 1e-6); show future-side
  filters (toggle); stretch start for panel (c); data offset (which N-sample segment: 0, 1, 2).
- **What changes when each control moves:**
  - dictionary: everything recomputes; panel (a) shows one or two lines per filter; (d) switches between 4 × 4 and
    2 × 2.
  - m: windows rebuilt from the cached covariance functions; (a)-(d) update.
  - g: as m; σ's fall with g.
  - N: covariance functions re-estimated from the first N samples of the chosen segment; null floor recomputed.
  - ridge, overlay, start, offset: as named.
- **Stat tiles:** "σ₂, σ₃" (nontrivial canonical correlations); "null floor"; "pair agreement" (fraction of samples
  whose pair-direction sign equals the pair label, orientation fixed by the builder's sign or, if live-labelled, by
  the sign maximizing agreement, stated); "outer/inner agreement" (ON/OFF only); "well agreement" (ON/OFF only); 
  "reflection residual" = $\max_i \min_\pm \lVert b_i \mp a_i\rVert / \lVert a_i\rVert$ over i = 2, 3, with $a_i$
  indexed by lag into the past and $b_i$ by lag into the future (both counted from the present), i.e. the deviation
  from exact time-reversal symmetry.
- **Tours** (default first):
  1. `pair`: linear, m = 16, g = 0, N = 10⁵. Note: "One strong direction, a sustained filter whose sign is the
     pair; a weak transient second."
  2. `onoff`: on-off, m = 16, g = 0, N = 10⁵. Note: "Rectified channels add an outer/inner direction; with the pair
     it names the well."
  3. `longlag`: on-off, m = 16, g = 64, N = 10⁵. Note: "Sixteen time units apart, only the pair is still
     predictable."
  4. `reverse`: on-off, m = 16, g = 0, N = 10⁵, future-side filters shown. Note: "The future-side filters are the
     time-reversed past-side filters: reversible dynamics cannot separate predictive from retrospective cells."
  5. `fewdata`: linear, m = 32, g = 0, N = 10³, ridge 0. Note: "With 1,000 samples and 32-sample windows the
     canonical correlations rise above their true values; compare the null floor."
- **fallbackTour:** `onoff` (the page's main running-example result); the default remains `pair`.
- **Caption:** *Plotted:* (a) past-side canonical filters $a_i$ for i = 2, 3, 4 against lag (0 = most recent), per
  channel; (b) nontrivial canonical correlations σ₂..σ₉ of past and future windows (bars), null floor (dashed); (c)
  a stretch of the readout y, the rectified canonical variates of directions 2 and 3, the true well and the well
  named by the signs of the pair and outer/inner directions; (d) counts of true against named well (or pair) over all
  samples. *Values:* readout of the running example ($\sigma_y = 0.25$, Δ = 0.25); channels, m, g, N, ridge as set;
  windows $p_t = (y_t, \dots, y_{t-m+1})$, $f_t = (y_{t+g+1}, \dots, y_{t+g+m})$. Running example, face A (positions
  used only to score). `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/neurons-fig-explorer-<tour>.png`); GIF stepping g = 0, 4, 16,
  64 on the `onoff` settings (1 s per frame).
- **Performance:** covariance functions: two channels, lags up to 2·32 + 64 and the null offset, over 10⁵ samples:
  < 150 ms once per (dictionary, N, offset), status "estimating…"; each (m, g) change: window assembly and two
  eigendecompositions of ≤ 64 × 64 plus an SVD: < 20 ms; variates over 10⁵ samples: < 20 ms. Parity: `lib/cca.js`
  CCA against the builder on the `pair` and `onoff` tours (σ to 1e-6, filters to 1e-6 after sign alignment).
- **Accessibility:** each panel has an `aria-label`; tiles are text; tours announce their note; the agreement table is
  an HTML table with numbers, not only colours.

## 6. Running example on this page

- **Faces:** A (default; the scalar readout y; positions only to score), plus the OU warm-up at $w_4$ (SPEC 3.4) as the
  analytic companion. Parameters exactly as SPEC 3.2 ($h_x = 2.5$, $h_y = 1.5$, $b = 0.6$, κ = 0, $D = 0.5$, $\sigma_y
  = 0.25$, Δ = 0.25). No parameter differs.
- **Precomputed** (`tools/build_example.py` → `site/data/neurons/p07.json`, with config and assertions):
  - `cca`: for dictionary ∈ {linear, onoff} × m ∈ {4, 8, 16, 32} × g ∈ {0, 4, 16, 64}, from the full $10^5$-sample
    signal: σ₂..σ₉, past and future filters for directions 2-4, direction labels (rule in 5.5), correlations of each
    variate with the pair, within-pair and outer/inner labels, agreement scores (pair; outer/inner and well for onoff),
    null floor, and the same for N ∈ {10³, 10⁴} (first N samples, offsets 0-2) for the `fewdata` comparison.
  - `hero`: filters, channel means and orientation signs (5.1); seed-0 event indices.
  - `grid_lambda`: $\lambda_i = e^{-\nu_i\tau}$ for i ≤ 6 at τ = 0.25 and 4 (from `grid.json`), for 3.1.
  - **Assertions:** (i) the builder's long signal reproduces the separable closed-form autocovariance of y (from the
    1-D generators at κ = 0) to within 3 sampling standard errors at lags ≤ 40; (ii) for linear, m = 16, g = 0,
    direction 2 is labelled "pair" with pair agreement ≥ 0.95; (iii) for onoff, m = 16, g = 0, directions 2 and 3
    are labelled "pair" and "outer/inner" (either order). **If an assertion fails, stop and amend this spec; do not
    retune parameters silently.**
  - **Spec-time check (not for display; the builder's values replace these):** an independent computation (exact
    autocovariance from the 1-D generators, and a 400-chain simulation, $\approx 9\times10^5$ samples) gave, for m =
    16, g = 0: linear σ₂..σ₄ ≈ 0.935, 0.144, 0.006, direction 2 correlations with (pair, within-pair, outer/inner) ≈
    (0.87, 0.45, 0.02) in absolute value, pair-sign agreement ≈ 0.988, direction 3 ≈ (0.17, 0.35, 0); on-off σ₂..σ₄ ≈
    0.935, 0.769, 0.145, direction 3 ≈ outer/inner (|corr| 0.90, sign agreement 0.966), well agreement from the two
    signs ≈ 0.954; linear σ₂ ≈ 0.73 at g = 16 and ≈ 0.50 at g = 64. These numbers motivated the page's design and
    must not be typed into the page.
- **Example data (SPEC 3.6):** `signal.json` carries the basin label of each sample (uint8, quadrant at κ = 0; same
  seed and integrator as the signal), from which the explorer derives the pair, within-pair, outer/inner and well
  labels for scoring.
- **Live:** the hero's particle and readout; the OU simulation and closed form; all CCA in the explorer.
- **Strain, and how the page states it:** (1) stochastic, so Takens does not literally apply (3.3, disclosure); (2) the
  linear window of y cannot represent the within-pair split separately (3.4: an instrument effect, like pages 1, 6, 9;
  SPEC 3.2 "tables built from the instrument have their own ordering"); (3) reversible dynamics, so no
  predictive/retrospective dichotomy (3.4, tour `reverse`); (4) the OU companion lives on time scales ≪ Δ (3.2, tour
  `atDelta`).
- **Companions:** OU warm-up (Pughe-Sanford et al.'s attractive analytic case) in `neurons-fig-ou`; their
  receptive-field evidence described, not reproduced (3.5); their saddle case described (3.2).

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E14 | 3 Koopman | `≈` | For an OU process the leading nontrivial stochastic Koopman singular function is linear, so canonical filter plus sign is set membership; CCA estimates it. Hermite modes and non-OU inputs need richer features. |
| E15 | 8 Hebbian | `~` | Local rules compute spectral objects, each exactly for its own rule: PCA or principal subspaces (Hebbian/anti-Hebbian rules), canonical directions (the CCA networks' fixed points), thresholded nonnegative principal-submatrix eigenvectors (the resistor-network rule); no bound relates their answers. |
| E22 | 10 LLMs from inside | `~` | Neurons that read coherent sets, and expansion coding, motivate looking for coherent structure among data points in activation space; they do not derive it. |

Map card text: "Neurons · past-future CCA on a neuron's delay windows · knob: neurons r, window m, lag · bound: σ_{r+1}
within the window dictionary; exact set membership for OU input."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The whitened cross-covariance of past and future delay windows, $C_{pp}^{-1/2}C_{pf}C_{ff}^{-1/2}$: the stochastic Koopman SVD restricted to the span of the window dictionary (linear functions of y, or of its ON/OFF rectified channels). Whitened covariances on both sides. |
| Knob | Number of neurons r (retained canonical directions; ON/OFF cells per direction); window length m; lag (gap g between windows); the dictionary. |
| Discarded at r | Canonical directions with small correlation: fast, unpredictable components of the input; and everything outside the dictionary (for linear windows of this readout, the within-pair split and the outer/inner split). |
| Bound | Within the dictionary, page 3's bounds: $\lVert M - M_r\rVert = \sigma_{r+1}$, top-r canonical pairs maximize VAMP-2 (Wu & Noé 2020; `theorem`; optimality relative to the dictionary). For OU the leading nontrivial singular function is linear and higher ones are Hermite polynomials that linear CCA does not see (Pughe-Sanford et al. 2025; Mehler/Hermite; `theorem` for the leading function). Rectified output = set membership: `conditional` (exact for OU sets defined by the sign of the leading function, approximate otherwise). Local CCA networks: the CCA solution is a fixed point, convergence shown numerically (Pehlevan et al. 2020; Lipshutz et al. 2021; `conditional`). |
| From data | Sample CCA error (standard; upward bias at small N, regularize long windows); the null floor shown live — `standard`. |
| Running example | From the builder (`p07.json`): σ₂..σ₄ for linear and ON/OFF windows at m = 16, g = 0; σ₂ at g = 16 and 64; agreement of the pair unit with the pair label, of the outer unit with the outer/inner label, and of the two together with the well. |
| Budget line | S (sampling of the filter), I (reading a rectified output as set membership). |

## 9. Things not to claim

The singular functions of an OU process are linear, or linear CCA recovers the Koopman SVD (only the leading one is
linear; linear CCA gets the linear sector); Takens makes any time series linear with enough delays, or covers noisy
input; neurons have been shown to compute canonical directions of their inputs; the running example shows predictive
versus retrospective cells; a linear filter of this readout reports the well; reading coherent sets (or expansion
coding) derives activation-space analysis; activation cells are coherent sets; coherent sets are a network's
computational states; Pughe-Sanford et al. recorded new data (they reanalysed existing datasets); the CCA network
models are Hebbian in the classical sense (their feedforward rules are described by the authors as non-Hebbian).

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$ (σ₁ = 1 the constant; nontrivial canonical correlations σ₂, σ₃, …), $\lambda_i$,
$\nu_i$, $\mathcal K_\tau$, $\mathcal L$, τ, Δ, t, $x$, V, D, π, $y$, $\sigma_y$, $w_1..w_4$, L/R pairs.
Page-local: $\mathcal A, \mathcal B$ (a coherent pair of sets; not the alphabet $\mathcal A$ of page 1: say so in a
side note); $\mathcal F_\tau = \mathcal K_\tau\mathcal K_\tau^\dagger$ (forward-backward operator); A, Σ, $\mathbf D$ (OU
drift matrix, stationary covariance, noise covariance: A here is the OU drift, the same object as page 2's A for the
warm-up); $v_i$ (OU filter vectors); φ, $\Sigma_0$, $\Sigma_\tau$ (Galerkin features and their covariances, 3.3
only); m (window length), g (gap in samples), $p_t$, $f_t$ (past and future windows), c(k) (autocovariance of y),
$C_{pp}, C_{ff}, C_{pf}$, M (whitened cross-covariance), $a_i$ (past-side filter), $z_t$ (canonical variate), $r^\pm$
(rectified outputs), $\mathbb 1[\cdot]$ (indicator, used for the hard membership index; Pughe-Sanford et al. write
the Heaviside function as H, which this site reserves for Hankel tables). The OU noise covariance $\mathbf D$ is bold
to keep D the diffusion coefficient.

## 11. Sources

Cite as in SPEC appendix C (entries marked **new** were added to appendix C in SPEC v1.1).

- Pughe-Sanford, J. L., Ding, X., Moore, J. J., Sengupta, A. M., Epstein, C., Greengard, P. & Chklovskii, D. B.
  (2025). Neurons as detectors of coherent sets in sensory dynamics. *NeurIPS 38*. arXiv:2510.26955. [P: §§2-6 and
  Supplement §§3, 5, 6 (Proposition 1), 7 read for this spec, v1 HTML]
- Froyland, G. (2013). An analytic framework for identifying finite-time coherent sets in time-dependent dynamical
  systems. *Physica D* 250, 1-19. [V]
- Klus, S. & Djurdjevac Conrad, N. (2024). Dynamical systems and complex networks: a Koopman operator perspective.
  *J. Phys. Complexity* 5(4), 041001. [**new**; M, as cited by Pughe-Sanford et al.]
- Klus, S., Nüske, F., Koltai, P., Wu, H., Kevrekidis, I., Schütte, C. & Noé, F. (2018). Data-driven model reduction
  and transfer operator approximation. *J. Nonlinear Sci.* 28, 985-1010. [V]
- Wu, H. & Noé, F. (2020). VAMP. *J. Nonlinear Sci.* arXiv:1707.04659. [A]
- Akaike, H. (1975). Markovian representation of stochastic processes by canonical variables. *SIAM J. Control*
  13(1), 162-173. [A]
- Granger, C. W. J. & Morris, M. J. (1976). Time series modelling and interpretation. *J. R. Stat. Soc. A* 139(2),
  246-257 (sums of AR processes are ARMA). [V; delay-state disclosure only]
- Takens, F. (1981). Detecting strange attractors in turbulence. LNM 898, 366-381. [P, Thm 1]
- Pavliotis, G. A. (2014). *Stochastic Processes and Applications*. Texts in Applied Mathematics 60, Springer
  (OU spectrum, Hermite eigenfunctions). [**new**; V]
- Gel'fand, I. M. & Yaglom, A. M. (1957). Calculation of the amount of information about a random function contained
  in another such function. *Uspekhi Mat. Nauk* 12(1); English transl. *AMS Transl. (2)* 12 (1959). [**new**; V:
  the year and translation details were not confirmed; the formula is standard]
- Chechik, G., Globerson, A., Tishby, N. & Weiss, Y. (2005). Information bottleneck for Gaussian variables. *JMLR* 6,
  165-188. [**new**; W]
- Hardoon, D. R., Szedmak, S. & Shawe-Taylor, J. (2004). Canonical correlation analysis: an overview with application
  to learning methods. *Neural Computation* 16(12), 2639-2664. [**new**; V; used only for the standard CCA eigenproblem]
- Pehlevan, C., Zhao, X., Sengupta, A. M. & Chklovskii, D. (2020). Neurons as canonical correlation analyzers.
  *Front. Comput. Neurosci.* 14, 55. [P; checked for this spec: feedforward rules called non-Hebbian by the authors,
  lateral anti-Hebbian; fixed point = CCA; multichannel convergence numerical]
- Lipshutz, D., Bahroun, Y., Golkar, S., Sengupta, A. M. & Chklovskii, D. B. (2021). A biologically plausible neural
  network for multichannel canonical correlation analysis. *Neural Computation* 33(9), 2309-2352. DOI
  10.1162/neco_a_01414. arXiv:2010.00525. [**new**; W: abstract-level; "local non-Hebbian learning rules"]
- Oja, E. (1982). [P] and Pehlevan, Hu & Chklovskii (2015) [A]: named in the E15 card only.
- Programme sources (as such, not literature): "Slouching Towards Interpretability" (Nov 2026), part III.b, including
  the whiteboard `niels-hankel.jpg`.
- Data provenance: all running-example numbers from `tools/build_example.py` (`p07.json`, `signal.json`,
  `grid.json`).

## 12. Implementation notes

- **Files (writer owns):** `site/content/neurons.html`; `site/js/p_neurons.js` (exports `init`, `widgets`);
  helpers `site/js/p_neurons_hero.js`, `p_neurons_ou.js`, `p_neurons_explorer.js`; data
  `site/data/neurons/p07.json` (builder-written), `site/data/neurons/widgets.json`; figure asset
  `site/assets/fig/neurons/niels-hankel.jpg` + `README.md` (provenance).
- **Shared modules used:** `lib/example.js` (V, SDE step, readout, contour helper as on page 1, loaders for
  `signal.json`, `grid.json`), `lib/cca.js`, `lib/linalg.js` (eigh, svd), `lib/rng.js`, `lib/bowtie.js`,
  `charts.js`, `ui.js`, `palette.js`.
- **`lib/cca.js` must expose** (request to the shared-numerics owner; prototype in a page helper if late):
  `covFunctions(channels /* Float32Array[] */, maxLag, {offset = 0, n})` → `R[c][c'][ℓ]` for ℓ ∈ [−maxLag, maxLag]
  (means removed); `windowBlocks(R, m, g)` → `{Cxx, Cxy, Cyy}` (x = past window, y = future window; SPEC 6.3) with the ordering of 3.3
  (past most recent first, future earliest first; channels interleaved by lag); `cca(Cxx, Cxy, Cyy, {ridge})` →
  `{sigmas, A /* past filters */, B /* future filters */}` (sigmas of the centred problem: the page prepends σ₁ = 1); `ccaFromSamples(X, Y, {ridge})` for
  the OU widget; `variates(channels, A, m, means)` → Float32Array per direction.
- **Widget keys and URL state:** hero `hr` (`hr_speed`, `hr_tour`); OU `ou` (`ou_tau`, `ou_n`, `ou_dict`, `ou_seed`,
  `ou_tour`); explorer `cx` (`cx_dict`, `cx_m`, `cx_g`, `cx_n`, `cx_ridge`, `cx_future`, `cx_start`, `cx_off`,
  `cx_tour`); bowtie `bw` (single tour `default`).
- **Manifest** `data/neurons/widgets.json`: `hr` (tours default, frame-switch, frame-late; fallback frame-late;
  animated), `ou` (linear, quadratic, atDelta, fewdata; fallback linear), `cx` (pair, onoff, longlag, reverse, fewdata;
  fallback onoff), `bw` (default).
- **Tests:** parity of `lib/cca.js` against the builder (`pair`, `onoff`, OU fixed sample); a node test that each
  explorer tour's tiles match `p07.json` (σ to 1e-6; agreements to 1e-4); a test that the hero's filters applied to
  the builder's signal reproduce the builder's agreement scores.

## 13. Page-specific definition-of-done additions

- [ ] Every statement of what a canonical direction "means" uses the builder's labels (or, for unlabelled settings,
      the live label marked "live").
- [ ] The words "exact" and "optimal" appear only with their scope ("exact for OU sets defined by the sign of the
      leading function"; "optimal within the window dictionary").
- [ ] The evidence section phrases every classification as a reading and states that the data are reanalysed, not new.
- [ ] The E22 paragraph carries the section 8 status hook and is listed as "motivation" (C7.20).
- [ ] The E15 card (now `~`) carries the section 8 hook; each rule's exact result is stated outside it.
- [ ] No sentence says a finite window of y is an exact state of a partially observed linear Gaussian system.
- [ ] The `reverse` tour's reflection residual is below 0.05 at N = 10⁵ (builder-checked); if not, the page reports the
      value and drops the reversibility sentence pending review.
- [ ] Citations match SPEC appendix C, including the entries marked **new** in section 11.

## Change log

- v1 (2026-11-17): first full spec. Running-example design checked at spec time (section 6): linear windows of the
  readout yield the pair only (plus a weak transient), so SPEC 3.7's "rectified outputs track pair, then well" is
  realized here as "pair from linear windows; outer/inner from ON/OFF channels; the well from both signs", and the
  SPEC amendment is requested. Support type "cited empirical (literature)" used for C7.18, which the template's list
  lacks.
- v1.1 (2026-11-17): reconciled with SPEC v1.1, which adopts this page's running-example result (3.7), the corrected
  E15 and page-7 ledger wording on the CCA networks (2.2, 4.2), the `signal.json` basin labels (3.6), the new
  bibliography entries (appendix C) and the support type "empirical (cited)" (template), now used in C7.18. The
  `lib/cca.js` signatures follow SPEC 6.3 (`windowBlocks` and `cca` take and return x/y-named blocks; future filters
  are `B`).
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) The "Hypotheses: delay embeddings" disclosure no longer
  says an observable linear Gaussian state-space process has an exact finite lag-vector state (Pughe-Sanford et
  al.'s eqs. 19-21 assert it; it is false in general: a scalar readout is ARMA; two-OU example). It now separates the
  hidden state, the finite-dimensional predictive state (Kalman filter; Akaike's canonical variables of the whole
  past) and a finite window, which is a dictionary and generally an approximation; the Takens bullet says the same.
  (2) Gaussian IB: shares CCA's directions, not its compression (3.3, C7.10). (3) E15 is `~` (SPEC 2.2), with each
  rule's exact statement kept. Reviewer findings: math-7-10 6, 9; math-1-6 5 (Gaussian IB wording).
