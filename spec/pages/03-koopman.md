# Page spec 03: Nonlinear systems, Koopman and transfer operators

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 3 |
| id (hash, file stem) | `koopman` |
| tab label | Koopman |
| kicker | Page 3 · dynamical systems |
| title | Koopman operators: nonlinear dynamics, linear on functions |
| lede (one-sentence claim, ≤ 45 words) | A nonlinear or noisy system acts linearly on functions of its state. Subspaces of functions that the dynamics nearly maps into themselves give finite linear models; for noisy systems the best such subspaces are the top singular functions of that action, which past-future CCA estimates. |
| depends on | 1 (2 helps); readable alone |
| edges (SPEC 2.2) | E3, E4, E5, E6, E7, E13, E14, E19 |
| faces of the running example | A (positions, default; and the scalar signal y), C (the toy residual network), with the four-state chain A′ appearing as one EDMD dictionary |
| main-path words | 2,200-2,700 |
| spec status | v1.3, 2026-11-17 (round-2 review fix; change log) |

## 1. Reader outcome

After this page the reader can:

1. Say why page 2's machinery (impulse response, Hankel operator) needs linearity, and what delay embedding offers
   instead: Takens's theorem (reconstruction of a deterministic state from delays, with its hypotheses) and HAVOK (an
   SVD of a delay Hankel matrix, a linear model plus a forcing term).
2. Define the Koopman operator ($f \mapsto \mathbb E[f(X_\tau) \mid X_0 = \cdot\,]$) and the transfer operator (which
   pushes densities forward), explain why both are linear for any dynamics, and read the running example's slow
   eigenfunctions (constant, which pair, which well in the pair, their product) with $\lambda_i = e^{-\nu_i\tau}$.
3. Explain an invariant (closed) subspace of functions and why it gives an exact finite linear model; run EDMD
   (and DMD as its linear-dictionary case) and say what it converges to (the projection onto the dictionary's span);
   measure a dictionary's closure defect by a residual; place SINDy as a different finite view (a sparse vector field,
   not a subspace) and HAVOK's forcing as a closure defect.
4. Define the whitened (VAMP) singular value decomposition of a stochastic Koopman operator, say why it is past-future
   CCA, state its Eckart-Young bound and the variational property (any finite features give canonical correlations
   at or below the true singular values), and say when singular = eigen (reversible, equilibrium).
5. Read coherent sets off leading singular functions, both for the reversible particle and for a finite-time flow
   whose left and right singular functions differ (face C).
6. Use the lag τ as a resolution knob: say which resolution is well separated at a given lag (wells at short lags,
   pairs at long lags) and why gaps are not monotone in r.

What they see: a cloud of particles tumbling into the wells while four averages decay along exactly straight lines on
a log scale; a cubic dictionary producing biased eigenvalues while basin indicators and radial basis functions do
better, with residuals that say which; SINDy recovering four nonzero drift coefficients from short increments (and
failing when the samples do not excite the library); singular values sliding with the lag so that the gap after four
dominates at short lags and the gap after two at long lags; the four wells, then the two pairs, appearing as sets;
on the toy residual network, singular functions on the input layer that are the basins and singular functions on the
output layer that are four clumps.

## 2. Skim path

1. Lede (header).
2. Hero figure `koopman-fig-hero`: "Averages that decay at fixed rates". Fig-sub: *Particles fall into four wells and
   hop between them; averaged over the cloud, four special functions of position decay along straight lines on a log
   scale, each at its own rate, while position itself does not.*
3. Section headings (verbatim, these are the claims):
   - "Nonlinear systems lose the impulse response; delay windows still carry state"
   - "Every system acts linearly on functions of its state"
   - "Finite linear models are subspaces the dynamics nearly closes"
   - "For noisy dynamics the best subspaces come from past-future CCA"
   - "The lag decides which resolution is well separated"
4. Key-point callouts (one per section; gists in section 3).
5. Figure titles and fig-subs for `koopman-fig-delay`, `koopman-fig-edmd`, `koopman-fig-bowtie`, `koopman-fig-lag`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: nonlinear dynamics have no impulse response, but delays
and functions of the state still carry it; the Koopman operator is linear on functions for any dynamics, and its
eigenfunctions decay at fixed rates; a finite linear model is a subspace of functions the dynamics (nearly) maps into
itself, EDMD fits one from data, SINDy and HAVOK are different finite views; for noisy dynamics the right object is the
whitened SVD, which is past-future CCA, with an Eckart-Young bound; the lag is the resolution knob: short lags
separate the four wells, long lags only the two pairs; singular functions give coherent sets, also for a flow through
network layers.

## 3. Section outline

Section ids are `koopman-<slug>`; figure ids are `koopman-fig-<slug>` (SPEC 6.5). Word counts are main-path prose
only.

### 3.1 `koopman-problem` "Nonlinear systems lose the impulse response; delay windows still carry state" (≈ 400 words)

Placement: the hero sits between the lede and this heading; an "Arriving here first?" aside (≤ 80 words) at the top of
this section: "Page 1 arranges a process as a table of pasts by futures; page 2 shows that for a linear system the map
from past inputs to future outputs factors through a state and that its singular values rank the state's directions.
This page asks what replaces that map when the dynamics are not linear." Links `#hankel`, `#control`.
`koopman-fig-delay` sits after the fourth bullet.

- The running example in two sentences (link `#map/map-example`): the particle in four wells, drift $-\nabla V$ with
  cubic terms, noise of strength D. Its response to a large push is not the sum of responses to small ones (a push
  large enough to cross a barrier moves the particle to another well); there is no impulse response to factor, and
  page 2's linearizations are local (around one well) or describe only the ensemble's small-signal average.
- What survives is the past-to-future map itself. A classical route uses **delays**: stack the last m readings of one
  signal, $(y_t, y_{t-1}, \dots, y_{t-m+1})$, into a vector and treat it as the state. Takens 1981: for a smooth
  deterministic system on a compact m-dimensional manifold and a generic smooth scalar observable, $2m + 1$ delays give
  an embedding: the delay vector determines the state. This is a statement about reconstruction, **not** linearity.
- Stacking delay vectors side by side gives a trajectory (delay) Hankel matrix, constant along anti-diagonals like
  page 2's block Hankel. HAVOK (Brunton et al. 2017, "Hankel alternative view of Koopman") takes its SVD, fits a linear
  model to the leading delay coordinates, and finds that the last retained coordinate behaves like an intermittent
  forcing that fires during switching events (lobe switches of the Lorenz system). Link to the paper and its video;
  do not reproduce Lorenz.
- Running example (`koopman-fig-delay`): the readout $y = x_1 + x_2 + \xi$ as one signal, windows of 32 samples (8 time
  units). The delay matrix's singular values fall off quickly; the leading delay coordinates separate the four wells'
  levels; the builder's HAVOK-style forcing coordinate is shown against the true well changes, with the builder's
  correlation (quote it; do not promise that it is vivid).
- **Strain, stated here:** the running example is stochastic, so Takens's theorem does not literally apply (it is about
  deterministic systems; noise needs separate care), and HAVOK's forcing is less vivid than for Lorenz. Delay windows
  remain useful features; section 3.4 says what they estimate.

Key callout: "Delays reconstruct state; they do not make dynamics linear. Linearity comes from changing what is
evolved: functions of the state instead of the state."

Disclosures:
- "Hypotheses: Takens's theorem" (≤ 300 words): diffeomorphism of a compact m-manifold, $C^2$, generic pairs of map and
  observable, $2m+1$ delays; what "generic" means; nothing about linearity, finite data, or noise (appendix D). Point to
  Arbabi & Mezić 2017 for when long-trajectory Hankel DMD computes Koopman spectral quantities (ergodic, appropriate
  spectrum).
- "HAVOK in more detail" (≤ 400 words): delay Hankel → SVD → coordinates $q_1..q_r$ → linear regression of
  $\dot q_{1..r-1}$ on $q_{1..r}$, with $q_r$ treated as an input; why the forcing carries dynamics the linear part
  omits; Brunton et al.'s Lorenz example in words; the CoherentModes theory note's remark that delay-embedded past-future
  CCA and HAVOK share a trajectory matrix but are different estimators (`THEORY.md` §4.4, programme source).
- "In other fields: four tables called Hankel" (≤ 200 words): as on pages 1 and 2; glossary link.

### 3.2 `koopman-lift` "Every system acts linearly on functions of its state" (≈ 420 words)

Placement: refers back to the hero; no new figure.

- Koopman 1931: instead of evolving the state, evolve functions of it ("observables"; glossary link: "observable"
  means a function of state here, not page 2's observability). For deterministic dynamics with flow map $\Phi_\tau$:
  $\mathcal K_\tau f = f \circ \Phi_\tau$. For noisy (Markov) dynamics, the **stochastic Koopman operator**
  (one display equation): $(\mathcal K_\tau f)(x) = \mathbb E[f(X_\tau) \mid X_0 = x]$. It is linear in f whatever the
  dynamics: the expectation of a sum is the sum of expectations. The price is dimension: it acts on a space of
  functions.
- The **transfer operator** $\mathcal P_\tau$ pushes densities forward ($\rho_0 \mapsto$ density of $X_\tau$); it is
  the adjoint of $\mathcal K_\tau$, $\langle \mathcal P_\tau\rho, f\rangle = \langle \rho, \mathcal K_\tau f\rangle$.
  Koopman moves predictions backward from the future; transfer moves distributions forward from the past (edge E3:
  each entry of page 1's table is a transfer step followed by a Koopman step, restricted to words).
- Eigenfunctions: $\mathcal K_\tau\phi_i = \lambda_i\phi_i$ with $\lambda_i = e^{-\nu_i\tau}$, $\nu_i$ the rates of the
  generator $\mathcal L$ (the Kolmogorov backward operator). The average of an eigenfunction over any cloud of particles
  decays exactly as $e^{-\nu_it}$: this is the hero.
- Running example (builder values from `grid.json`, labels from the builder's sign checks): $\phi_1 = 1$ (rate 0);
  $\phi_2 \approx$ sign $x_1$, "which pair" (rate ≈ 0.028); $\phi_3 \approx$ sign $x_2$, "which well within the pair"
  (≈ 0.336); $\phi_4 \approx \phi_2\phi_3$, their product (≈ 0.364); then a gap to rates ≈ 8 (motion inside a well). The
  slow eigenfunctions are nearly constant on each well and change across barriers: they are smoothed well
  indicators. Hero tours `corner` and `saddle` (the pair mode is not excited from the between-pair saddle, where
  $\phi_2 \approx 0$).
- Position itself is not an eigenfunction: the cloud's mean $x_1$ is a mixture of many exponentials (hero, grey curve).

Key callout: "The Koopman operator is linear for any dynamics because it evolves averages of functions. Its
eigenfunctions are the functions whose averages decay at a single fixed rate."

Disclosures:
- "The maths: Koopman, transfer, generator" (≤ 500 words): definitions on $L^2(\pi)$; the generator $\mathcal Lf =
  -\nabla V\cdot\nabla f + D\Delta f$ and $\mathcal K_\tau = e^{\tau\mathcal L}$; adjointness; reversibility
  (detailed balance) makes $\mathcal K_\tau$ self-adjoint on $L^2(\pi)$, so eigenfunctions are orthogonal, eigenvalues
  real and in (0, 1], and the transfer operator's eigenfunctions are $\pi\phi_i$. Separability at κ = 0: eigenfunctions
  are products of 1-D ones, which is why the fourth is the product of the second and third.
- "In other fields: observable, transfer, mode" (≤ 200 words): observable (function of state vs control's
  observability); transfer operator vs transfer function (page 2) vs transfer learning; mode (eigenfunction here; a
  well elsewhere in the running example). Glossary links.

### 3.3 `koopman-closed` "Finite linear models are subspaces the dynamics nearly closes" (≈ 450 words)

Centrepiece: `koopman-fig-edmd` after the third bullet.

- A subspace of functions is **invariant** (closed) if the dynamics maps it into itself: then $\mathcal K_\tau$
  restricted to it is a finite matrix, and the model is exact. Spans of eigenfunctions are invariant; the running
  example's $\{1, \phi_2, \phi_3, \phi_4\}$ gives an exact four-dimensional linear model of the slow averages. This is
  page 1's closure (realization finds an invariant set of predictive directions) and page 2's state space, in function
  space. Glossary link: "closed / closure".
- What fails: position itself cannot be closed. The direct arguments for the running example (κ = 0), one per
  dynamics. *Deterministic drift:* the generator of the drift sends $x_1$ to $10x_1 - 10x_1^3$, and it sends any
  polynomial in $x_1$ of degree m with leading coefficient a to one of degree m + 2 with leading coefficient $-10ma
  \ne 0$; so $x_1$, its image, its image's image, … have degrees 1, 3, 5, … and are linearly independent, and no
  finite-dimensional subspace invariant under the flow (equivalently under its generator) contains $x_1$. *Noisy
  dynamics:* the running example's diffusion has reflecting walls, so its generator carries Neumann boundary
  conditions (zero normal derivative on ∂Ω), and $x_1$, whose normal derivative is ±1 on the walls $x_1 = \pm2.2$, is
  not in its domain; the degree argument does not apply there. Use instead: a finite-dimensional subspace invariant
  under the whole strongly continuous Koopman semigroup lies in the generator's domain (on it the semigroup is a
  matrix exponential, hence differentiable in t), so no such subspace contains $x_1$. One looks for closed
  eigenspaces instead of closing the state. (Do not cite the general claim that a finite invariant subspace containing
  the state requires a single isolated fixed point: it has counterexamples, e.g. $\dot x = 0, \dot y = -y$ with
  invariant span{x, y} and a line of fixed points; SPEC appendix D.)
- **EDMD** (Williams, Kevrekidis & Rowley 2015): choose a dictionary $\chi_1..\chi_k$, collect pairs $(x_n, x'_n)$ with
  $x'_n$ the state a lag τ after $x_n$, and solve the least-squares problem $\hat K = \hat C_{00}^{-1}\hat C_{0\tau}$
  (one display equation; $\hat C_{00}$ = dictionary covariance at time 0, $\hat C_{0\tau}$ = cross-covariance with time
  τ). DMD (Schmid 2010) is the case of a linear dictionary. As data grow, $\hat K$ converges to the orthogonal projection
  of $\mathcal K_\tau$ onto the dictionary's span (Korda & Mezić 2018; for samples from π, in $L^2(\pi)$); as the
  dictionary grows richly, to $\mathcal K_\tau$ in the strong operator topology, with eigenvalue convergence along
  subsequences.
- Running example (widget tours): `linear` (DMD) sees two slow modes, biased low; `cubic` does not do much better,
  because sign-like eigenfunctions are poorly approximated by cubics; `basins` (four basin indicators: the four-state
  chain A′ as a Markov state model) gets close; `rbf` closer; `oracle` (true eigenfunctions) exact. For reversible
  dynamics sampled at equilibrium, the projected eigenvalues are never above the true ones in the data limit
  (Rayleigh-Ritz; the variational principle of Noé & Nüske 2013), so a better dictionary can only raise them.
- **Closure defect**: for an estimated eigenpair $(\hat\lambda, \hat f)$, the residual $\|\mathcal K_\tau\hat f -
  \hat\lambda\hat f\|_\pi / \|\hat f\|_\pi$ measures how far the dictionary is from closing; for a self-adjoint operator
  some true eigenvalue lies within that residual of $\hat\lambda$ (standard). The widget computes it from the
  generator. In general the defect is not bounded a priori (status `conditional`).
- Two other finite views: **SINDy** (Brunton, Proctor & Kutz 2016) regresses the vector field on a library with
  sparsity; for a noisy system, the drift is estimated from short-time increments (Boninsegna, Nüske & Clementi 2018).
  Applying the generator to the coordinate functions gives the drift, which is why SINDy is a special case of
  generator EDMD (Klus et al. 2020). It finds a sparse vector field, not a closed subspace. **HAVOK's** forcing
  (section 3.1) is the closure defect of a delay dictionary, made visible as an input.

Key callout: "A finite linear model is a subspace of functions the dynamics maps into itself. EDMD finds the best one
in a chosen dictionary; the residual says how far the dictionary is from closing."

Disclosures:
- "The maths: EDMD as a projection" (≤ 500 words): Galerkin/least-squares equivalence; why samples from π give the
  $L^2(\pi)$ projection; eigenfunctions of $\hat K$ as functions $\hat f = \sum_j \hat v_j\chi_j$; the residual formula computed
  through the generator's eigenpairs (as the widget does); Ritz values ≤ true eigenvalues for self-adjoint operators;
  the residual bound $\mathrm{dist}(\hat\lambda, \mathrm{spec}\,\mathcal K_\tau) \le$ residual for self-adjoint (more
  generally normal) operators.
- "Hypotheses: what EDMD convergence does and does not promise" (≤ 300 words): Korda & Mezić 2018's setting (samples
  i.i.d. from a measure μ; convergence in $L^2(\mu)$; strong operator convergence as the dictionary grows; eigenvalues
  along subsequences; weak convergence of eigenfunctions when the weak limit is nonzero); nothing about the rate for a
  fixed dictionary; continuous spectrum and non-normality need separate care.
- "SINDy, increments and the generator" (≤ 400 words): the Kramers-Moyal estimate $(X_{t+\delta t} - X_t)/\delta t
  \approx$ drift, its bias $O(\delta t)$ and variance $2D/\delta t$; sequential thresholded least squares; why
  equilibrium samples near $x_1 = \pm1$ make $x_1$ and $x_1^3$ nearly collinear (the library is not excited; widget
  tour `sindy-eq`); Klus et al. 2020's generator EDMD, of which SINDy is the case $\psi = $ coordinates.

### 3.4 `koopman-svd` "For noisy dynamics the best subspaces come from past-future CCA" (≈ 460 words)

Placement: `koopman-fig-bowtie` after the second bullet.

- For a noisy system, measure functions of the present in $L^2(\pi_0)$ and functions of the future in $L^2(\pi_\tau)$
  (the state's distribution at the two times; both π here). The Koopman operator maps the second space to the first,
  and its **singular value decomposition** (one display equation): $\mathcal K_\tau = \sum_i \sigma_i\,
  \phi_i\,\langle\psi_i, \cdot\,\rangle$ with orthonormal present-side functions $\phi_i$ and future-side functions
  $\psi_i$. Wu & Noé 2020 (VAMP): the best rank-r linear model of the dynamics uses the top r singular pairs. (On this
  page $\psi_i$ always denotes future-side singular functions; dictionary functions are $\chi_j$. See section 10.)
- Why "whitened": in a finite dictionary on each side, the SVD of $C_{00}^{-1/2}C_{0\tau}C_{\tau\tau}^{-1/2}$ (one display
  equation) is exactly **canonical correlation analysis** between features of the present and of the future: whitening
  removes each side's own correlations, leaving only what one predicts of the other. With complete feature sets it is
  the Koopman SVD; with finite ones a Galerkin approximation (Klus et al. 2018; Wu & Noé 2020; edge E4). For
  linear-Gaussian processes this is Akaike's past-future CCA and stochastic balancing (page 2, E4); in the Gaussian case
  the past-future information bottleneck uses the same canonical directions, with its own β-dependent scales and
  noise (page 6, E13); for an Ornstein-Uhlenbeck process
  its leading nontrivial function is linear, which page 7 turns into a neuron (E14).
- Bound (one display equation): $\|\mathcal K_\tau - \mathcal K_{\tau,r}\|_{HS}^2 = \sum_{i>r}\sigma_i^2$, and for every
  f, $\|(\mathcal K_\tau - \mathcal K_{\tau,r})f\| \le \sigma_{r+1}\|f\|$ (Eckart-Young for compact operators; Hilbert-
  Schmidt for the first, true here for τ > 0). The variational property: canonical correlations computed from any finite
  features are, index by index, at most the true singular values (in the infinite-data limit), so a better feature set
  can only raise them.
- Reversible, equilibrium case: $\mathcal K_\tau$ is self-adjoint, singular = eigen, $\sigma_i = e^{-\nu_i\tau}$, and
  present and future functions coincide. **Strain, stated here:** the particle is reversible, so this page cannot show
  the difference on face A; the transfer and Koopman pictures also coincide up to the weight π.
- Face C (the toy residual network, link `#map/map-example`): twelve residual layers, each a step of the drift's flow
  (E19, depth as time). Following Froyland 2013's "diffuse, transport, diffuse" construction on the data points
  (identity transport, a Sinkhorn-balanced kernel at the first and last layer; the CoherentModes theory note §4.1,
  programme source), the operator $Q_\ell = P^{(\ell)}P^{(0)}$ is not symmetric: its right singular functions live on
  the input layer, its left ones on layer ℓ, and its eigenvalues differ from its singular values (`koopman-fig-lag`,
  tour `flow`). Expected: leading singular functions on layer 0 trace the basins and on layer 12 the clumps the points
  fall into; quote the builder's agreement with the basins and do not describe the block structure beyond it. (The input box of
  SPEC 3.5 is deliberately not symmetric about the basin boundaries, so quadrant-like functions at layer 0 are not a
  coincidence of the box.) Reading
  sets off singular functions with guarantees: pages 4 (E6, E7), 5 and 10 (E19).

Key callout: "Whiten both sides and the Koopman SVD is canonical correlation between present and future. Its top r
pairs are the best rank-r linear model, with an Eckart-Young bound."

Disclosures:
- "The maths: VAMP, CCA and the variational property" (≤ 600 words): covariance operators; $\mathcal K_\tau$ between
  $L^2(\pi_\tau)$ and $L^2(\pi_0)$; the whitened finite matrix; why CCA of finite features is a compression
  $\Pi_0\mathcal K_\tau\Pi_\tau$ by orthogonal projections, so its singular values are at most those of $\mathcal K_\tau$
  (s-number inequality); the VAMP-r score $\sum_{i\le k}\hat\sigma_i^r$ and its maximality (Wu & Noé 2020); for delay
  windows of a noisy readout, by the Markov property past and future windows interact only through the state, so their
  canonical correlations are also at most the state's singular values.
- "Coherent pairs for a flow" (≤ 400 words): Froyland 2013's normalized transfer operator and its singular vectors as
  coherent pairs; on samples with identity transport, $Q_\ell = P^{(\ell)}P^{(0)}$; THEORY §4.1's identity
  $1 - \|Qv\|^2 = (1 - \|P^{(0)}v\|^2) + (\|P^{(0)}v\|^2 - \|Qv\|^2)$: a singular value near 1 means the function is slow
  for both layers' geometries. Index shift note for CoherentModes (it writes $\sigma_0 = 1$ for the trivial value; this
  site counts it as $\sigma_1$). As noise vanishes, Froyland 2015's dynamic Laplacian (page 4, E7).
- "In other fields: coherent set, kernel" (≤ 150 words): glossary links.

### 3.5 `koopman-lag` "The lag decides which resolution is well separated" (≈ 380 words)

Centrepiece: `koopman-fig-lag`.

- The lag τ is the resolution knob. With $\sigma_i = e^{-\nu_i\tau}$, a short lag keeps many modes near 1, a long lag
  only the slowest. Quote the builder's values: at τ = 0.25, λ ≈ 1, 0.993, 0.920, 0.913, 0.13 (gap after four ≈ 0.78,
  after two ≈ 0.07); at τ = 4, λ ≈ 1, 0.89, 0.26, 0.23, ≈ 0 (gap after two ≈ 0.63). **Short lags certify the wells;
  long lags certify only the pairs.** Gaps are not monotone in r (widget panel (a)).
- Retained dimension at a threshold ϑ: the number of singular values above ϑ, $r_\vartheta(\tau) = \#\{i : \sigma_i >
  \vartheta\}$, is the smallest rank whose truncation error in operator norm is at most ϑ (Eckart-Young; the graph
  analogue is the CoherentModes register's S.10, programme source). Builder values at ϑ = 0.5 for τ ∈ {0.25, 4, 40}:
  expected 4, 2, 1 (one display equation at most).
- Sets read off the retained functions (widget panel (c)): at τ = 0.25 four sets, the wells; at τ = 4 two, the pairs.
  The rule used here is k-means with k = $r_\vartheta$ on the retained nontrivial singular functions scaled by their
  singular values; pages 4 and 5 give rounding rules with guarantees (Cheeger sweeps, SEBA).
- From data (estimate control): VAMP with a radial-basis dictionary from simulated pairs, and CCA of past and future
  delay windows of the readout y. Both give singular values at or below the truth (variational property), and the
  estimates scatter by an amount that shrinks like $1/\sqrt N$; a block is resolvable from data only once its gap
  exceeds that scatter (Weyl; subspaces by Davis-Kahan/Wedin, `conditional`). Smaller gaps need more data.
- Face C (tour `flow`): the knob is the end layer ℓ (depth as time). Quote the builder's singular values at ℓ = 12
  and which block is well separated with the shared face C graph; do not assert pairs or wells in advance (SPEC 3.5).

Key callout: "Finer resolution keeps more modes but is certifiable only where the spectrum has a gap; the lag moves
the gap, so it decides which resolution can be trusted."

Disclosure "The maths: retained dimension and the price of a small gap" (≤ 400 words): spectral Eckart-Young for
$r_\vartheta$; Weyl: estimated singular values within $\|\hat K - K\|$ of the truth; Wedin/Davis-Kahan: subspace angle
≤ error / gap; covariance estimation error ∝ $N^{-1/2}$ for bounded features (standard), hence $N \propto
\delta_r^{-2}$ for a fixed subspace accuracy (a scaling, not a theorem with constants here); pointer to page 10's
budget (S term).

### 3.6 `koopman-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.7 `koopman-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.8 `koopman-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C3.1 | The running example has no impulse response in the large: responses to large pushes do not superpose. | construction | 3.1 prose (barrier-crossing push) | — | 3.1 |
| C3.2 | Takens: for a smooth deterministic system on a compact m-manifold and a generic observable, 2m + 1 delays embed the state. It says nothing about linearity or noise. | theorem | Takens 1981, Thm 1 | $C^2$ diffeomorphism, compact manifold, generic pair, deterministic | 3.1 |
| C3.3 | HAVOK fits a linear model to leading delay-SVD coordinates with the last retained coordinate as an intermittent forcing; for Lorenz the forcing fires at lobe switches. | standard (described) | Brunton et al. 2017 | their delay and rank choices | 3.1 |
| C3.4 | For the running example's readout, the leading delay coordinates separate the wells' levels and the builder's HAVOK-style forcing correlates with well changes by the recorded amount. | builder values | `koopman-fig-delay`; `p03.json` `delay` | window 32, Δ = 0.25, r as recorded | 3.1 |
| C3.5 | Takens does not literally apply to the noisy running example. | construction | 3.1 prose | stochastic dynamics | 3.1 |
| C3.6 | The (stochastic) Koopman operator is linear for any dynamics; the transfer operator is its adjoint. | construction + standard | 3.2; Koopman 1931; Mezić 2005; Klus et al. 2018 | Markov dynamics; $L^2$ spaces as stated | 3.2 |
| C3.7 | Averages of an eigenfunction over any initial cloud decay exactly as $e^{-\nu_it}$. | construction + widget | hero tours `corner`, `well`, `saddle` | eigenfunction of the generator; Monte-Carlo error shown | 3.2 |
| C3.8 | The running example's slow eigenfunctions are 1, ≈ sign $x_1$, ≈ sign $x_2$, and their product, with rates ≈ 0, 0.028, 0.336, 0.364, then a gap to ≈ 8. | builder values + assertion | `grid.json`; builder sign-pattern checks | κ = 0; grid discretization (rates converged to 3 s.f.) | 3.2 |
| C3.9 | An invariant subspace gives an exact finite linear model; spans of eigenfunctions are invariant. | construction | 3.3 prose; EDMD tour `oracle` | — | 3.3 |
| C3.10 | For the running example, no finite-dimensional subspace invariant under the drift's flow contains $x_1$ (repeated generator application gives polynomials of strictly increasing odd degree with nonzero leading coefficients), and none invariant under the reflected diffusion's Koopman semigroup contains it (such a subspace lies in the generator's domain, whose functions satisfy the Neumann condition, which $x_1$ violates). | construction (direct proof on the page) | 3.3 prose; drift coefficients from `lib/example.js`; SPEC 3.2 (reflecting boundary) | κ = 0 (polynomial drift $10x_1 - 10x_1^3$); invariance for all times, equivalently under the generator for subspaces in its domain; reflected diffusion: strongly continuous semigroup, Neumann domain on the box; the general fixed-point-count statement of Brunton et al. 2016 is not used | 3.3 |
| C3.11 | EDMD's estimate converges, as data grow, to the $L^2(\mu)$-orthogonal projection of $\mathcal K_\tau$ onto the dictionary span; as the dictionary grows, to $\mathcal K_\tau$ in the strong operator topology, eigenvalues along subsequences. DMD is the linear-dictionary case. | theorem | Williams et al. 2015; Korda & Mezić 2018; Schmid 2010; Tu et al. 2014 | i.i.d. samples from μ; dictionary in $L^2(\mu)$; spectral convergence only along subsequences | 3.3 |
| C3.12 | For reversible dynamics sampled at equilibrium, data-limit EDMD eigenvalues are at most the true ones, index by index. | theorem | Noé & Nüske 2013; Rayleigh-Ritz (min-max) | self-adjoint $\mathcal K_\tau$ on $L^2(\pi)$; samples from π; infinite data | 3.3 |
| C3.13 | On the running example, linear and cubic dictionaries give biased slow eigenvalues; basin indicators and RBFs do better; the oracle is exact (builder values in the data limit). | widget + builder values | EDMD tours `linear`, `cubic`, `basins`, `rbf`, `oracle`; `p03.json` `galerkin` | τ as set; data limit or N as set | 3.3 |
| C3.14 | For a self-adjoint operator some true eigenvalue lies within the residual of any approximate eigenpair. | standard | Parlett 1998, §4.5 (or any spectral-theory text) | self-adjoint (normal) operator | 3.3 |
| C3.15 | SINDy recovers the drift's four nonzero cubic coefficients from short-time increments at the builder-recorded N (uniform start points); with equilibrium start points the library is poorly excited and recovery degrades. | widget + builder values | EDMD panel (d), tours `sindy`, `sindy-eq`; `p03.json` `sindy` | δt = 0.01; threshold 1.0; library monomials ≤ 3 | 3.3 |
| C3.16 | SINDy is a special case of generator EDMD (the generator applied to coordinate functions gives the drift); it finds a sparse vector field, not a closed subspace. | theorem (stated in source) | Klus et al. 2020; Brunton, Proctor & Kutz 2016; Boninsegna et al. 2018 | drift-diffusion SDE for the stochastic case | 3.3 |
| C3.17 | The whitened finite-dictionary SVD is CCA between present and future features; with complete features it is the Koopman SVD, with finite ones a Galerkin approximation; the top r pairs give the best rank-r model. | theorem (E4) | Wu & Noé 2020; Klus et al. 2018; Akaike 1975 | compact $\mathcal K_\tau$; feature covariances invertible | 3.4 |
| C3.18 | $\|\mathcal K_\tau - \mathcal K_{\tau,r}\|_{HS}^2 = \sum_{i>r}\sigma_i^2$ and $\|(\mathcal K_\tau - \mathcal K_{\tau,r})f\| \le \sigma_{r+1}\|f\|$. | theorem | Eckart-Young / Schmidt for compact operators | Hilbert-Schmidt for the first identity, compact for the second (both true here for τ > 0) | 3.4 |
| C3.19 | Canonical correlations from any finite features (including delay windows of a noisy readout) are at most the corresponding true singular values. | theorem (standard) | s-number inequality; Markov property; disclosure | infinite-data limit; centred features; Markov state | 3.4, 3.5 |
| C3.20 | For reversible equilibrium dynamics singular = eigen and $\sigma_i = e^{-\nu_i\tau}$. | standard | 3.4; disclosure in 3.2 | detailed balance; $\pi_0 = \pi_\tau = \pi$ | 3.4 |
| C3.21 | On face C, $Q_\ell = P^{(\ell)}P^{(0)}$ is non-symmetric; its singular values differ from its eigenvalue moduli; leading right singular functions on layer 0 approximate the basins (builder agreement value). | widget + builder values | lag widget tour `flow`; `p03.json` `flow` | shared face C kernel and bandwidth; N = 1000, seed 0; uncommitted band excluded from agreement | 3.4 |
| C3.22 | $Q_\ell$ is a sample realization of Froyland's diffuse-transport-diffuse construction with identity transport. | standard + programme source | Froyland 2013; CoherentModes `THEORY.md` §4.1 | smoothers are a choice (kernels), not canonical | 3.4 |
| C3.23 | At τ = 0.25 the gap after four dominates; at τ = 4 the gap after two; gaps are not monotone in r. | builder values | lag widget tours `wells`, `pairs`; `grid.json` | κ = 0 | 3.5 |
| C3.24 | $r_\vartheta = \#\{i : \sigma_i > \vartheta\}$ is the minimal rank with operator-norm truncation error ≤ ϑ; at ϑ = 0.5 it is 4, 2, 1 for τ = 0.25, 4, 40 (builder). | theorem + builder values | Eckart-Young; S.10 (graph analogue); lag widget panel (d) | — | 3.5 |
| C3.25 | k-means on the retained singular functions gives the wells at τ = 0.25 and the pairs at τ = 4 (builder agreement values). | widget + builder values | lag widget panel (c) | k = $r_\vartheta$; equilibrium samples N = 1000, seed 0 | 3.5 |
| C3.26 | Estimated singular values scatter by an amount shrinking like $N^{-1/2}$; resolving a block needs its gap to exceed the scatter. | standard (scaling) + widget | lag widget estimate `trajectories`; Weyl; Davis-Kahan/Wedin | bounded features; i.i.d. pairs; a scaling, not a constant-explicit theorem here | 3.5 |

Things not to claim on this page (SPEC appendix D and page-specific): Takens makes any time series a linear system; the
running example satisfies Takens's hypotheses; HAVOK's forcing is removable or that chaos has an exact finite linear
model; EDMD converges to the true spectrum for a fixed dictionary; linear CCA recovers the full Koopman SVD (it recovers
the linear sector; for OU only the leading nontrivial function is linear); the generator's slow modes are page 1's
instrument-table directions (the instrument decides that table's order); static clustering finds dynamics in general
(only in special cases, E6); finer resolution always has a smaller gap; HAVOK's "coherent regions" are transfer-operator
coherent sets; SINDy finds Koopman eigenfunctions; face C's block structure (pairs or wells) before the builder reports
it.

## 5. Figures and widgets

### 5.1 `koopman-fig-hero` "Averages that decay at fixed rates" (live, hero; key `hr`)

- **Purpose:** for nonlinear noisy dynamics, averages of eigenfunctions over a particle cloud decay exactly
  exponentially, each at its own rate; averages of position do not.
- **Layout:** `figure.fig.full.card`, two panels (stacked on phones): (a) contour map of V over Ω (ink contours, wells
  as ink-outlined circles labelled $w_1..w_4$), the particle cloud as small dots coloured by current basin (well
  colours), the start point as an accent cross; below (a), four mini-maps of $\phi_2..\phi_5$ (`div` map, symmetric
  range) labelled "which pair", "which well in the pair", "product", "inside a well" (labels from the builder);
  (b) log-linear chart: for i = 2, 3, 4, 5 the normalized cloud average $\overline{\phi_i}(t)/\phi_i(x_0)$ (dots, every
  0.25 time units, ±2 standard errors as a faint band), the exact line $e^{-\nu_it}$ (dashed, same colour), and in grey
  $\overline{x_1}(t)/x_{0,1}$ (labelled "position: not an eigenfunction"), t from 0 to 30, y from $10^{-2}$ to 1; points
  whose standard error exceeds their value are drawn hollow and labelled "below noise".
- **Data:** live: M = 1000 particles from `lib/example.js` (Euler-Maruyama, dt = 0.0025, seed in URL); eigenfunctions
  and rates from `data/example/grid.json` (display grid, bilinear interpolation); line colours: pair `--c-pair-L`,
  well-in-pair `--c-well-2`, product `--c-well-4`, inside-a-well `--c-other`, each also with a distinct dash pattern.
- **Controls:** transport (play/pause, speed ×1/×4/×16 = 1/4/16 time units per second), reset; start point (click on
  the map, or the select `corner` | `well` | `saddle`). Two primary controls.
- **Default state (= first tour):** `corner`, t = 0, autoplay when scrolled into view; reduced motion shows the
  `corner-late` still.
- **What changes:** time advances: the cloud falls into $w_4$ within a fraction of a time unit, spreads to $w_3$ over a
  few units and to the left pair over tens; in (b) the dots follow their straight lines until they reach the noise
  floor; the grey position curve bends (fast fall, then slow decay). A new start point resets the cloud and the
  theory lines (the dashed lines are scaled by $\phi_i(x_0)$; for $|\phi_i(x_0)| < 0.05\max|\phi_i|$ the series is
  hidden and labelled "not excited from here").
- **Tours:** `corner` (default; $x_0 = (1.7, 1.1)$, high on the wall above $w_4$, playing); `well` ($x_0 = w_4$);
  `saddle` ($x_0 = (0, 0.6)$, the between-pair saddle: the pair mode is not excited); `corner-late` (`corner` paused at
  t = 12).
- **fallbackTour:** `corner-late`.
- **Caption:** *Plotted:* (a) contours of $V(x_1,x_2)$, wells $w_1..w_4$, particles at time t coloured by basin, start
  point ×; mini-maps of the generator eigenfunctions $\phi_2..\phi_5$; (b) cloud averages of $\phi_i(X_t)$ divided by
  $\phi_i(x_0)$ (dots, ±2 s.e.), the prediction $e^{-\nu_it}$ (dashed), and the cloud average of $x_1$ divided by its
  initial value (grey), log scale. *Values:* M = 1000 particles, dt = 0.0025, D = 0.5, κ = 0, start point as set, seed
  0. Running example, face A. `synthetic`.
- **Static fallback:** `assets/fallback/koopman-fig-hero-corner-late.png` (and per tour); GIF
  `assets/fallback/koopman-fig-hero.gif` (≈ 6 s at ×4 from t = 0 on `corner`).
- **Accessibility:** alt text: "Particles fall into four wells; on a log scale four averaged quantities fall along
  straight dashed lines with different slopes, while the average position follows a bent curve." Series differ by dash
  pattern and are labelled at their right ends; the fig-sub carries the message without motion.
- **Performance:** 1000 particles × 100 substeps per 0.25 time units; at ×16 that is 6,400 substeps per particle per
  second ≈ 6.4 M steps/s; if a frame exceeds 12 ms, the step loop is chunked across frames and speed ×16 is
  throttled with a visible note. Eigenfunction evaluation: 4 bilinear lookups per particle per plotted point.

### 5.2 `koopman-fig-delay` "One noisy signal, stacked into delays" (static, rendered by the page module)

- **Purpose:** delay windows of one scalar readout carry the well structure; HAVOK's forcing coordinate is shown against
  the true well changes, as computed.
- **Data:** precomputed `data/koopman/p03.json` `delay`, from the shared `data/example/signal.json` (10⁵ samples of y at
  Δ = 0.25) and its true-basin labels: window m = 32; singular values of the centred delay matrix (top 20); the top 4
  right singular vectors (time profiles, 32 values each); the delay coordinates $q_1..q_r$ over a 2,000-sample excerpt
  (Float32); the builder's HAVOK fit (r chosen by the builder as the smallest r capturing 99 % of the delay matrix's
  energy, capped at 8; linear regression of $\Delta q_{1..r-1}/\Delta$ on $q_{1..r}$); the forcing $q_r$ over the
  excerpt; well-change times in the excerpt; the correlation between $|q_r|$ and an indicator of a well change within
  ±m/2 samples (over all 10⁵ samples).
- **Content:** four panels in a 2 × 2 grid: (a) y over the excerpt with the true-well strip beneath (well colours) and
  the bin lines at 0 and 1 faint; (b) singular values of the delay matrix (log y, index 1..20), r marked; (c) scatter of
  $(q_1, q_2)$ over the excerpt, dots coloured by true well, with the time profiles of the top two singular vectors as
  small insets; (d) the forcing $q_r$ over the excerpt with ticks at well changes, and a text line "corr($|q_r|$, well
  change) = <builder value>".
- **Generation:** drawn by `p_koopman.js` at fixed size from the data.
- **Caption:** *Plotted:* (a) readout $y_t$ and the true well (strip); (b) singular values of the matrix whose rows are
  the centred delay windows $(y_t, \dots, y_{t-31})$; (c) the first two delay coordinates, coloured by true well; (d) the
  r-th delay coordinate used as HAVOK's forcing, with well changes marked. *Values:* Δ = 0.25, m = 32, r as recorded,
  10⁵ samples, excerpt of 2,000. Running example, face A (signal y). `synthetic`.
- **Fallback:** PNG `assets/fallback/koopman-fig-delay-default.png` (key `dl`, single tour `default`).

### 5.3 `koopman-fig-edmd` "Pick functions, fit a linear model" (live, centrepiece; key `ed`)

- **Purpose:** EDMD's eigenvalues and eigenfunctions depend on the dictionary; the residual says how far a dictionary is
  from closing; SINDy, on the same library, finds a sparse drift instead.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view a 2 × 2 grid; side panel with tours, controls, tiles,
  legend.
  - (a) **Eigenvalues**: index i = 1..6 on x; true $e^{-\nu_i\tau}$ as ink ticks; estimated $\hat\lambda_i$ as dots
    (complex estimates shown by modulus, with a small marker if the imaginary part exceeds 1e-3); y from 0 to 1.
  - (b) **Eigenfunctions**: estimated $\hat f_2, \hat f_3, \hat f_4$ evaluated on the display grid (`div` maps, each
    normalized to unit $L^2(\pi)$ norm and sign-aligned with the true function), with the true $\phi_2..\phi_4$ as small
    maps beneath.
  - (c) **Closure residual**: bars for i = 2, 3, 4: relative residual $\|\mathcal K_\tau\hat f_i - \hat\lambda_i\hat
    f_i\|_\pi/\|\hat f_i\|_\pi$, computed through the generator's first 100 eigenpairs (stated in the caption).
  - (d) **SINDy**: two groups of bars (drift in $x_1$, drift in $x_2$) over the 10 monomials $1, x_1, x_2, x_1^2, x_1x_2,
    x_2^2, x_1^3, x_1^2x_2, x_1x_2^2, x_2^3$: true coefficients (outlined) and STLSQ estimates (filled); a tile
    "support recovered: yes/no". Active only for the `cubic` dictionary; otherwise shows "SINDy needs a library that
    contains the drift; select the cubic library."
- **Data:**
  - Live samples: N start points (equilibrium: drawn from π on the grid by inverse CDF over cells, uniform within a
    cell, seeded; the SINDy panel uses its own N uniform start points on Ω unless the advanced control says
    otherwise), each simulated forward by τ with `lib/example.js` (dt = 0.0025) for EDMD and by δt for SINDy.
  - Data limit (`N = ∞`): precomputed `data/koopman/p03.json` `galerkin[dict][tau]` = {C00, C0τ, eigenvalues,
    eigenvector coefficients, residuals} from the builder's full grid.
  - Dictionaries: `linear` {1, x₁, x₂}; `cubic` monomials of degree ≤ 3 (10); `basins` indicators of the four basins
    (quadrants) (4); `rbf` Gaussian radial basis functions on a 9 × 7 grid of centres over Ω, width 0.5, plus the
    constant (64); `oracle` $\phi_1..\phi_8$ from `grid.json` (8).
- **Controls (primary):**
  1. dictionary: `linear (DMD)` | `cubic` | `basins (four-state chain)` | `RBF` | `oracle` (select);
  2. data: segmented `500` | `2000` | `5000` | `∞`;
  3. lag τ: segmented `0.25` | `1` | `4`.
  Advanced: seed (0-2); SINDy increment δt (`0.01` default | `0.05` | `0.25`); SINDy threshold (0.1-5, default 1.0);
  SINDy start points (`uniform` default | `equilibrium`).
- **What changes when each control moves:** dictionary: all panels recompute ((d) activates for `cubic` only); data:
  resimulates (status "simulating…") or loads the data-limit values; τ: (a) ticks move to $e^{-\nu_i\tau}$, everything
  recomputes ((d) is unaffected: SINDy uses δt); seed: resamples; δt, threshold, start points: (d) only.
- **Stat tiles:** "$\hat\lambda_2$ vs $\lambda_2$" (both, 3 s.f.); "largest residual (i = 2..4)"; "dictionary size k";
  "SINDy coefficient error" ($\max|\hat\Xi - \Xi|$ over the 20 coefficients; cubic only).
- **Tours** (default first):
  1. `linear`: linear, ∞, τ = 0.25. Note: "DMD's linear dictionary sees two slow modes, biased low; it has no product
     function."
  2. `cubic`: cubic, ∞, τ = 0.25. Note: "Cubics approximate sign-like eigenfunctions poorly; residuals stay large."
  3. `basins`: basins, ∞, τ = 0.25. Note: "Four basin indicators: the four-state chain as a Markov state model."
  4. `rbf`: RBF, ∞, τ = 0.25. Note: "A rich local dictionary nearly closes the slow subspace."
  5. `oracle`: oracle, ∞, τ = 0.25. Note: "The true eigenfunctions span an invariant subspace: exact, zero residual."
  6. `fewdata`: RBF, 500, τ = 0.25, seed 0. Note: "With little data a rich dictionary overfits; compare with ∞."
  7. `sindy`: cubic, 2000, τ = 0.25, δt = 0.01, uniform starts. Note: "Same library, sparse drift regression: four
     nonzero coefficients." (If the builder finds support recovery fails at 2000, the tour uses the smallest N in
     {2000, 5000} at which it succeeds for seed 0; recorded as `tours.sindy`.)
  8. `sindy-eq`: as `sindy` with equilibrium starts. Note: "Samples near the wells barely excite the library; recovery
     degrades."
- **fallbackTour:** `rbf`.
- **Caption:** *Plotted:* (a) eigenvalues of the EDMD matrix $\hat K = \hat C_{00}^{-1}\hat C_{0\tau}$ (dots) and of
  $\mathcal K_\tau$ (ticks); (b) estimated eigenfunctions $\hat f_2..\hat f_4$ and true $\phi_2..\phi_4$, normalized in
  $L^2(\pi)$; (c) relative residuals $\|\mathcal K_\tau\hat f - \hat\lambda\hat f\|_\pi/\|\hat f\|_\pi$ evaluated with
  the generator's first 100 eigenpairs; (d) drift coefficients over monomials of degree ≤ 3: true (outlined) and
  sequentially thresholded least squares on increments $(X_{t+\delta t} - X_t)/\delta t$ (filled). *Values:*
  dictionary, N, τ, δt, threshold and seed as set; start points from π (EDMD) or uniform on Ω (SINDy) unless stated;
  dt = 0.0025. Running example, face A (positions). `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/koopman-fig-edmd-<tour>.png`); no GIF.
- **Accessibility:** panel `aria-label`s; ticks vs dots also differ in shape; tiles are text; tours announce notes.
- **Performance:** simulation of N = 5000 pairs at τ = 4 (1,600 steps each) ≈ 8 M steps, target < 600 ms with
  "simulating…"; EDMD solve ≤ 64 × 64; residuals via 100 inner products per function on the display grid; SINDy 10 × 10
  normal equations per iteration. Parity: data-limit values are the builder's; live finite-N EDMD with fixed seeds is
  checked against the builder for `linear` and `basins` at N = 2000, τ = 0.25 (1e-6).

### 5.4 `koopman-fig-bowtie` "Functions now, functions later, whitened" (static SVG)

- **Purpose:** the stochastic Koopman operator factors through its top singular pairs; whitening on both sides makes
  the factorization CCA.
- **Data:** shared `bowtie` component. Labels (SPEC 1.4): left "points now / functions of the present", right
  "functions of the future", above the fans "whitened covariances"; knot bars $\sigma_i = e^{-\nu_i\tau}$ for i = 1..8
  at τ = 0.25 from `grid.json` (linear scale); r = 4; bound label "lost: σ_{r+1} per function; Σ_{i>r} σ_i² (HS)".
- **Controls:** none required; draggable r if enabled (no URL state).
- **Caption:** *Plotted:* schematic of $\mathcal K_\tau = \sum_i\sigma_i\phi_i\langle\psi_i,\cdot\rangle$: functions of the
  future ↦ functions of the present through r singular pairs; bars are the running example's $e^{-\nu_i\tau}$ at
  τ = 0.25; hatched: discarded at r = 4. *Values:* κ = 0, D = 0.5.
- **Fallback:** the SVG; PNG export `assets/fallback/koopman-fig-bowtie-default.png`.

### 5.5 `koopman-fig-lag` "The lag picks the resolution" (live, centrepiece; key `lg`)

- **Purpose:** the lag moves the gaps: short lags separate four wells, long lags two pairs; sets are read off the
  retained singular functions; estimates from data sit at or below the truth; for a flow through layers, left and right
  singular functions differ.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view a 2 × 2 grid; side panel with tours, controls, tiles,
  legend.
  - (a) **Spectrum against the knob**: particle: $\sigma_i(\tau) = e^{-\nu_i\tau}$, i = 1..8, against τ on a log axis
    from 0.05 to 100 (lines coloured by the builder's labels: pair, well-in-pair, product, inside a well); accent cursor
    at τ; at the cursor, shaded bars showing the gap after 2 ($\sigma_2 - \sigma_3$) and after 4 ($\sigma_4 -
    \sigma_5$), labelled with their values; a horizontal line at ϑ; with an estimate selected, estimated values at the
    snapped lags as dots with min-max whiskers over seeds 0-2. Flow: singular values of $Q_\ell$ against ℓ = 1..12, with
    the moduli of its eigenvalues at the cursor as open circles.
  - (b) **Singular functions** at the cursor: particle: $\phi_2..\phi_5$ maps (`div`), each labelled with $\sigma_i$,
    faded if $\sigma_i \le \vartheta$; flow: right singular vectors $v_2..v_4$ on layer-0 points and left singular vectors
    $u_2..u_4$ on layer-ℓ points (two rows of scatters, `div` colours).
  - (c) **Sets read off**: points coloured by k-means (k = $r_\vartheta$, k-means++ seeded, 20 restarts) on the
    retained nontrivial singular functions scaled by $\sigma_i$; colours: if k = 2, pair colours matched to the majority
    pair; if k = 4, well colours matched by majority; otherwise categorical. Particle: the 1,000 equilibrium samples of
    `samples.json` (seed 0); flow: layer-0 points, uncommitted-band points (SPEC 3.5) drawn in `--c-other`.
  - (d) **Retained dimension** $r_\vartheta$ against the knob (step plot), cursor marked.
- **Data:**
  - particle, exact: rates and eigenfunctions from `grid.json` (σ_i exact for each τ); singular-function values at the
    sample points by bilinear interpolation.
  - particle, `trajectories`: live VAMP with the RBF dictionary of 5.3 on N = 2000 simulated pairs per lag, lags
    snapped to {0.25, 0.5, 1, 2, 4, 8, 16}, seeds 0-2 (cached per lag).
  - particle, `delay windows`: live CCA (`lib/cca.js`) between past windows $(y_{t-m+1}..y_t)$ and future windows
    $(y_{t+k}..y_{t+k+m-1})$ with $k = \tau/\Delta$, m = 8, from `signal.json` (10⁵ samples), lags snapped to multiples
    of Δ in {0.25, 0.5, 1, 2, 4, 8, 16}; the trivial value 1 is prepended (CCA is centred); seed-free (one long signal),
    so no whiskers; sets in (c) are not shown for this estimate (the functions live on windows, not positions; (c) says
    so).
  - flow: face C points (N = 1000, seed 0) computed live with `lib/example.js` (RK4 flow, SPEC 3.5); kernel walks
    $P^{(\ell)}$ by `lib/graph.js` with **SPEC 3.5's face C graph**, binding for pages 3, 4 and 10 (union of directed
    kNN graphs on the positions $x^{(\ell)}$, $k_{\rm nn} = 15$, weight 1 on edges and floor $10^{-6}$ elsewhere,
    diagonal 0, Sinkhorn-balanced; register A.1), so the three pages show one operator family;
    $Q_\ell = P^{(\ell)}P^{(0)}$; top 8 singular triplets by Lanczos on
    $Q_\ell^\top Q_\ell$ (matrix-free); eigenvalues of $Q_\ell$ by Arnoldi (top 8 moduli). Reference values for ℓ = 1..12
    precomputed in `p03.json` `flow` for parity.
- **Controls (primary):**
  1. system: segmented `particle` | `flow (face C)`;
  2. knob: particle: lag τ (log slider 0.05-100, default 0.25); flow: end layer ℓ (slider 1-12, default 12);
  3. threshold ϑ (slider 0.1-0.9, default 0.5);
  4. estimate (particle only): `exact` | `trajectories (RBF, N = 2000)` | `delay windows of y (m = 8)`.
  Advanced: N for trajectories (500 | 2000 | 5000); window m (4-16); flow $k_{\rm nn}$ (8-30, default 15); flow
  noise $D_{\rm flow}$
  (0-0.05, default 0).
- **What changes when each control moves:** system swaps the meaning of every panel (labels and axes change; the
  caption states both); the knob moves the cursor and redraws (b)-(c); ϑ moves the line, changes $r_\vartheta$, fades
  functions and re-runs k-means; estimate adds dots/whiskers to (a), replaces (b) by estimated functions (`trajectories`)
  or hides (b)-(c) with a note (`delay windows`).
- **Stat tiles:** "gap after 2" and "gap after 4" (at the cursor; particle exact or estimated); "$r_\vartheta$"; "agreement
  with ground truth" (fraction of points whose set matches the majority-matched pair (k = 2) or well (k = 4) label;
  "n/a" otherwise; flow excludes the uncommitted band); flow only: "max |σ − |λ||" over the top 8 (non-normality).
- **Tours** (default first):
  1. `wells`: particle, τ = 0.25, ϑ = 0.5, exact. Note: "At a short lag four singular values sit near 1 and the gap
     after four is large: four sets, the wells."
  2. `pairs`: particle, τ = 4, ϑ = 0.5, exact. Note: "At a longer lag only two survive: two sets, the pairs."
  3. `one`: particle, τ = 40, ϑ = 0.5, exact. Note: "At a very long lag only the constant remains above ϑ."
  4. `data`: particle, τ = 1, ϑ = 0.5, trajectories N = 2000. Note: "Estimates from 2000 simulated pairs: at or below
     the truth, with scatter."
  5. `delays`: particle, τ = 1, ϑ = 0.5, delay windows. Note: "Canonical correlations of delay windows of one noisy
     readout sit below the state's singular values."
  6. `flow`: flow, ℓ = 12, ϑ = 0.5. Note: "A finite-time flow: input-layer singular functions trace the basins,
     output-layer ones the clumps; singular values differ from eigenvalue moduli."
- **fallbackTour:** `wells`.
- **Caption:** *Plotted:* particle: (a) singular values $\sigma_i = e^{-\nu_i\tau}$ of the Koopman operator against lag
  τ (lines), estimates (dots, min-max over seeds), threshold ϑ, gaps at the cursor; (b) singular functions at the cursor;
  (c) equilibrium samples coloured by k-means on the retained singular functions; (d) number of $\sigma_i > \vartheta$
  against τ. Flow: (a) singular values of $Q_\ell = P^{(\ell)}P^{(0)}$ against end layer ℓ, with eigenvalue moduli at the
  cursor (circles); (b) right singular vectors on layer-0 points, left on layer-ℓ points; (c) layer-0 points coloured by
  k-means sets, uncommitted band grey; (d) as above against ℓ. *Values:* κ = 0, D = 0.5; estimate, N, m, $k_{\rm nn}$, seeds
  as set. Running example, face A (positions; signal y for the delay estimate) or face C. `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/koopman-fig-lag-<tour>.png`); GIF
  `assets/fallback/koopman-fig-lag.gif` (≈ 6 s: τ swept from 0.1 to 40 on a log scale, exact, ϑ = 0.5).
- **Accessibility:** panel `aria-label`s; lines in (a) differ by dash pattern; set colours also given as labels on
  hover ("set 1 ↔ $w_4$", majority match); tiles are text.
- **Performance:** exact particle mode: closed form plus k-means on 1,000 points in ≤ 4 dimensions, < 20 ms; trajectories:
  2,000 pairs × lag/dt steps (≤ 6,400) ≈ 13 M steps at τ = 16, < 1 s with "simulating…", cached per (lag, seed); delay CCA:
  covariance of 2m-dimensional windows over 10⁵ samples ≈ 25 M multiply-adds, < 150 ms, cached; flow: RK4 ≈ 30 ms, two
  sparse Sinkhorn kernels and Lanczos per ℓ, target < 400 ms, cached per (ℓ, $k_{\rm nn}$). Parity: flow singular values vs
  `p03.json` `flow` to 1e-6 relative.

## 6. Running example on this page

- Faces: A (positions; and the signal y for the delay figure and the delay estimate), C (the toy residual network, in
  the lag widget's `flow` mode); A′ appears as the `basins` dictionary. Parameters exactly as SPEC 3.2 and 3.5: κ = 0,
  D = 0.5, Δ = 0.25, $\sigma_y = 0.25$; face C with N = 1000, seed 0, T = 0.3, 12 layers, $D_{\rm flow} = 0$.
- Precomputed by `tools/build_example.py`:
  - shared: `data/example/grid.json` (rates, eigenfunctions, π); `data/example/samples.json` (equilibrium samples,
    N = 1000, seed 0); `data/example/signal.json` (10⁵ samples of y at Δ, **with the true basin label of each sample**, SPEC 3.6).
  - `data/koopman/p03.json`: `labels` (builder's meaning of $\phi_2..\phi_5$ from sign checks); `galerkin[dict][tau]`
    for the five dictionaries × τ ∈ {0.25, 1, 4} (C00, C0τ, eigenvalues, eigenvector coefficients, residuals of
    $\hat f_2..\hat f_4$); `sindy` (STLSQ results for N ∈ {500, 2000, 5000} × seeds 0-2, δt ∈ {0.01, 0.05, 0.25},
    uniform and equilibrium starts: coefficients and support-recovery flags); `tours.sindy`; `delay` (5.2); `lag`
    (retained dimension at ϑ = 0.5 for τ ∈ {0.25, 4, 40}; gaps after 2 and 4 at τ ∈ {0.25, 4}; k-means agreement with
    wells at τ = 0.25 and pairs at τ = 4 on `samples.json`); `flow` (singular values and eigenvalue moduli of $Q_\ell$ for
    ℓ = 1..12 with SPEC 3.5's face C graph, agreement of k-means sets with basins at ℓ = 12, which block (2 or 4) has
    the larger gap at ℓ = 12).
  - **Assertions:** rates within 1 % of SPEC 3.2's expected values (else amend SPEC per its 9.1 gate); $\phi_2$'s sign
    separates the pairs, $\phi_3$'s the wells within each pair, $\phi_4 \approx \phi_2\phi_3$ (correlation > 0.99);
    retained dimensions at ϑ = 0.5 are 4, 2, 1 for τ = 0.25, 4, 40; data-limit Ritz values ≤ true eigenvalues for every
    dictionary (C3.12; tolerance 1e-9); oracle residuals < 1e-6; residual of the true $\phi_i$ in the first-100-mode
    evaluation < 1e-8; $e^{-\nu_{101}\cdot 0.25} < 10^{-3}$ (the 100-mode residual evaluation is adequate at τ ≥ 0.25);
    SINDy support recovered at the `tours.sindy` setting for seed 0; delay-window canonical correlations ≤ $\sigma_{i+1}$
    of the corresponding nontrivial index at every snapped lag (C3.19, tolerance 0.02 for finite-sample error).
    **If an assertion fails, stop and amend this spec; do not retune parameters silently.**
- Live: hero simulation; finite-N EDMD and SINDy; VAMP from trajectories; delay CCA; face C flow and its operators.
- Expected values (for checking; the page displays builder or live values): λ at τ = 0.25: 1, 0.993, 0.920, 0.913,
  0.13; at τ = 4: 1, 0.89, 0.26, 0.23, ≈ 0; retained dimension at ϑ = 0.5: 4, 2, 1 for τ = 0.25, 4, 40. True drift
  coefficients at κ = 0: drift₁ = $10x_1 - 10x_1^3$; drift₂ = $\tfrac{4h_y}{b^2}x_2 - \tfrac{4h_y}{b^4}x_2^3 \approx
  16.67x_2 - 46.30x_2^3$ (the builder writes the exact values into `p03.json` `sindy.true`).
- Strain: stochastic, so Takens does not literally apply (3.1); reversible, so singular = eigen and transfer ≈ Koopman on
  face A (3.4), which is why face C is used for the non-normal case; HAVOK's forcing less vivid than Lorenz (3.1, quoted
  as the builder's correlation).
- Companions: face C (lag widget tour `flow`); Lorenz/HAVOK described with a link to Brunton et al. 2017 (3.1).
- Face C uses SPEC 3.5's (asymmetric) input box and graph; no page-local variant.

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E3 | 1 Hankel | `=` | Each entry of page 1's table for a hidden Markov model is (state distribution after the past) · (probability of the future from each state): a transfer step, then a Koopman step, restricted to words. |
| E4 | 2 Linear control | `=` | Past-future CCA of a linear-Gaussian process gives a stochastically balanced realization; for Markov processes generally, the whitened Koopman SVD is CCA of past and future features, exactly with complete features. |
| E5 | 2 Linear control | `=` | For the reversible running example the response to a push is the time-derivative of an equilibrium correlation (fluctuation-dissipation), so page 2's response Hankel and this page's correlation operator share slow modes. |
| E6 | 4 Spectral clustering | `=` | For reversible Langevin dynamics, density-normalized graph Laplacian (diffusion map, α = 1/2) eigenvectors on equilibrium samples converge to this page's generator eigenfunctions: static clustering recovers the slow dynamics. |
| E7 | 4 Spectral clustering | `≈` | For finite-time flows, coherent sets are leading singular vectors of a noisy transfer operator; as noise vanishes the rescaled construction tends to the dynamic Laplacian, which has a dynamic Cheeger inequality. |
| E13 | 6 Comp. mechanics | `~` | The past-future information bottleneck can be read as one choice of energy among spectral relaxations. Exact cases: it recovers the causal states without compression, and for Gaussian processes it uses this page's CCA directions (not its truncation). |
| E14 | 7 Neurons | `≈` | For an Ornstein-Uhlenbeck process the leading nontrivial Koopman singular function is linear, so a neuron with a canonical filter reports coherent-set membership; higher modes, and processes beyond OU, are approximations. |
| E19 | 10 LLMs from inside | `~` | Depth plays the role of time: a residual layer resembles one step of a flow, and data points moving through layers have transfer operators as here. Exact for face C by construction; for real networks an analogy with no bound. |

Map card text: "Koopman · the dynamics' action on functions, whitened on both sides (past-future CCA) · knob: r and the lag
τ · bound: $\sigma_{r+1}$ per function, $\sum_{i>r}\sigma_i^2$ in Hilbert-Schmidt norm."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The stochastic Koopman operator $\mathcal K_\tau: L^2(\pi_\tau) \to L^2(\pi_0)$, $(\mathcal K_\tau f)(x) = \mathbb E[f(X_\tau) \mid X_0 = x]$, whitened on both sides (VAMP); equivalently CCA between functions of the present and of the future. For reversible dynamics at equilibrium, eigen = singular. |
| Knob | r and the lag τ (diffusion time); on face C, the end layer ℓ; dictionary size for EDMD. |
| Discarded at r | Functions of state that decorrelate faster than $e^{-\nu_{r+1}\tau}$: at r = 4 (τ = 0.25), motion inside a well; at r = 2 (τ = 4), which well within a pair. |
| Bound | $\|\mathcal K_\tau - \mathcal K_{\tau,r}\|_{HS}^2 = \sum_{i>r}\sigma_i^2$; for any f, $\|(\mathcal K_\tau - \mathcal K_{\tau,r})f\| \le \sigma_{r+1}\|f\|$; the top-r VAMP-2 score is maximal over all r-dimensional feature pairs (Wu & Noé 2020; Eckart-Young; `theorem`; needs $\mathcal K_\tau$ compact, and Hilbert-Schmidt for the first identity, both true here for τ > 0). Retained dimension at threshold ϑ is the minimal rank with error ≤ ϑ (spectral Eckart-Young; CoherentModes S.10 for the graph analogue). |
| From data | EDMD converges to the projection onto the dictionary span (Williams et al. 2015; Korda & Mezić 2018); for reversible equilibrium sampling its eigenvalues are lower bounds in the data limit (Noé & Nüske 2013); finite features give canonical correlations at or below the truth; the closure defect of a dictionary is not bounded in general (`conditional`). |
| Running example | $\sigma_i = e^{-\nu_i\tau}$ from `grid.json`; from the builder (`p03.json`): retained dimension at ϑ = 0.5 for τ ∈ {0.25, 4, 40} (expected 4, 2, 1); gaps after 2 and 4 at τ = 0.25 and 4; data-limit EDMD eigenvalues per dictionary; face C singular values at ℓ = 12. |
| Budget line | T (truncation), S (sampling). |

## 9. Things not to claim

Takens: enough delays make any time series a linear system (it gives a generic embedding of deterministic smooth
dynamics; nothing about linearity; noise needs separate care); the running example satisfies Takens's hypotheses;
HAVOK yields an exact closed linear model or removes the forcing; EDMD finds the true spectrum for a fixed dictionary;
the singular functions of an OU process are linear / linear CCA recovers the Koopman SVD (only the leading nontrivial
one is linear; linear CCA recovers the linear sector); static clustering of samples finds the dynamics in general
(only for reversible dynamics with density-normalized kernels, E6); finer resolution always has a smaller gap; the
generator's slow modes are the instrument table's singular directions (page 1; the instrument decides that order);
SINDy finds Koopman eigenfunctions or a closed subspace; HAVOK's coherent regions are transfer-operator coherent
sets; face C's well-separated block is pairs (or wells) before the builder reports it; coherent sets of face C are
"computational states" (E21's caution applies on page 10).

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, $\lambda_i$, $\nu_i$, $\delta_r$, $\mathcal K_\tau$, $\mathcal P_\tau$,
$\mathcal L$, τ, Δ, t, x, V, D, π, y, $\sigma_y$, $w_1..w_4$, L/R pairs, $x^{(\ell)}$, $P^{(\ell)}$, $k_{\rm nn}$.
Page-local: $\phi_i$ (eigenfunctions / present-side singular functions; SPEC 3.2 already uses $\phi$), future-side
singular functions (SPEC's ledger uses no symbol; **$\psi_i$ on this page**), dictionary functions **$\chi_1..\chi_k$**
(not ψ, to avoid the clash noted in 3.4), $\hat K$, $\hat C_{00}$, $\hat C_{0\tau}$, $\hat C_{\tau\tau}$ (EDMD/VAMP
matrices), $\hat\lambda$, $\hat f$ (estimated eigenpair), $\pi_0, \pi_\tau$ (state distributions at times 0 and τ, as
in SPEC 4.2's ledger and appendix A; both equal π at equilibrium, and the page writes π wherever both are the
equilibrium), μ (a sampling measure, only in the EDMD convergence statements of 3.3 and C3.11; a side note says it is
not a Laplacian eigenvalue $\mu_i$ or the SEBA threshold of pages 5 and 10), $\Phi_\tau$ (flow map),
$q_1..q_r$ (delay coordinates), m (window length), Θ, Ξ (SINDy library and coefficients), δt (increment interval),
$Q_\ell$, $u_i$, $v_i$ (face C operator and its left/right singular vectors, as in CoherentModes THEORY §4.1), ϑ
(retention threshold; shared with pages 4 and 10, SPEC appendix A),
$r_\vartheta$.

## 11. Sources

Cite as in SPEC appendix C; check status there unless given here.

- Koopman, B. O. (1931). Hamiltonian systems and transformation in Hilbert space. *PNAS* 17(5), 315-318. [V]
 
- Mezić, I. (2005). Spectral properties of dynamical systems, model reduction and decompositions. *Nonlinear Dynamics*
  41, 309-325. [V]
- Takens, F. (1981). Detecting strange attractors in turbulence. LNM 898, 366-381. [P, Thm 1]
- Arbabi, H. & Mezić, I. (2017). Ergodic theory, DMD, and computation of spectral properties of the Koopman operator.
  *SIADS*. [A]
- Brunton, S. L., Brunton, B. W., Proctor, J. L., Kaiser, E. & Kutz, J. N. (2017). Chaos as an intermittently forced
  linear system (HAVOK). *Nat. Commun.* 8, 19. [A]
- Schmid, P. J. (2010). Dynamic mode decomposition. *J. Fluid Mech.* 656, 5-28. [A]
- Tu, J. H., Rowley, C. W., Luchtenburg, D. M., Brunton, S. L. & Kutz, J. N. (2014). On dynamic mode decomposition:
  theory and applications. *J. Comput. Dyn.* 1(2), 391-421. [W: DMD eigenvalues equal ERA poles from the same data]
  (used only in the HAVOK disclosure and C3.11)
- Williams, M. O., Kevrekidis, I. G. & Rowley, C. W. (2015). EDMD. *J. Nonlinear Sci.* 25, 1307-1346. [A]
- Korda, M. & Mezić, I. (2018). On convergence of extended dynamic mode decomposition to the Koopman operator.
  *J. Nonlinear Sci.* 28, 687-710. [W: projection limit; strong operator convergence; eigenvalues along subsequences;
  weak eigenfunction convergence when the limit is nonzero]
- Brunton, S. L., Brunton, B. W., Proctor, J. L. & Kutz, J. N. (2016). Koopman invariant subspaces and finite linear
  representations of nonlinear dynamical systems for control. *PLoS ONE* 11(2), e0150171. [W: its single-isolated-fixed-point
  statement is in the paper but has counterexamples; cited for Koopman invariant subspaces only, not for that statement]
- Brunton, S. L., Proctor, J. L. & Kutz, J. N. (2016). SINDy. *PNAS* 113(15), 3932-3937. [A]
- Boninsegna, L., Nüske, F. & Clementi, C. (2018). Sparse learning of stochastic dynamical equations. *J. Chem. Phys.*
  148, 241723. [W: asymptotic correctness in the infinite-data limit; cross-validation for sparsity]
- Klus, S., Nüske, F., Peitz, S., Niemann, J.-H., Clementi, C. & Schütte, C. (2020). Data-driven approximation of the
  Koopman generator: model reduction, system identification, and control. *Physica D* 406, 132416. [W: SINDy as a
  special case; gEDMD]
- Noé, F. & Nüske, F. (2013). A variational approach to modeling slow processes in stochastic dynamical systems.
  *Multiscale Model. Simul.* 11(2), 635-655. arXiv:1211.7103. [W: variational principle; journal details V]
- Klus, S., Nüske, F., Koltai, P., Wu, H., Kevrekidis, I., Schütte, C. & Noé, F. (2018). Data-driven model reduction
  and transfer operator approximation. *J. Nonlinear Sci.* 28, 985-1010. [V]
- Klus, S., Husic, B. E., Mollenhauer, M. & Noé, F. (2019). Kernel methods for detecting coherent structures in
  dynamical data. arXiv:1904.07752. [A]
- Wu, H. & Noé, F. (2020). VAMP. *J. Nonlinear Sci.* arXiv:1707.04659. [A; W: abstract states the best linear model
  comes from the top singular components and that VAMP holds for non-reversible processes]
- Akaike, H. (1975). [A]; Desai & Pal 1984 [W] (E4).
- Froyland, G. (2013). An analytic framework for identifying finite-time coherent sets in time-dependent dynamical
  systems. *Physica D* 250, 1-19. [V]; Froyland 2015 [P] (E7, pointer only).
- Banisch, R. & Koltai, P. (2017) [A] (pointer: diffusion maps on trajectory data).
- Nadler, Lafon, Coifman & Kevrekidis 2006 [W]; Coifman & Lafon 2006 [V] (E6).
- Creutzig, Globerson & Tishby 2009 [A] (E13); Pughe-Sanford et al. 2025 [P] (E14).
- Jaeger 2000 [V]; Balle et al. 2014 [P] (E3).
- Kubo 1966 [V] (E5).
- Eckart & Young 1936 [V]; Schmidt, E. (1907) for compact operators [V]; Parlett, B. N. (1998). *The Symmetric
  Eigenvalue Problem*. SIAM (residual bound) [V].
- Davis & Kahan 1970 [A]; Wedin 1972 [V]; Weyl [V].
- Programme sources (cite as such): CoherentModes `THEORY.md` §4.1 (the product $Q = P^{L'}P^{L}$ as a finite-state
  realization of Froyland's construction) and §4.4 (delay CCA vs HAVOK); `SPARSITY.md` S.10 (retained dimension, graph
  analogue).
- Code provenance: EDMD/VAMP/CCA in `lib/cca.js`; STLSQ in the page helper; no external code copied (PyKoopman and
  PySINDy may be linked as further reading, not copied).

## 12. Implementation notes

- Files: `site/content/koopman.html`, `site/js/p_koopman.js`, helpers `site/js/p_koopman_hero.js`,
  `p_koopman_delay.js`, `p_koopman_edmd.js`, `p_koopman_lag.js`; data `site/data/koopman/p03.json`,
  `site/data/koopman/widgets.json`. Reads shared `data/example/grid.json`, `samples.json`, `signal.json`.
- Shared modules used: `lib/example.js` (SDE step, flow map, π sampler, loaders), `lib/cca.js`, `lib/graph.js`,
  `lib/linalg.js`, `lib/rng.js`, `lib/bowtie.js`, `charts.js`, `ui.js`, `palette.js`.
- `lib/cca.js` must expose: `delayWindows(signal, m, lag)`, `covariances(X, Y)` → `{Cxx, Cxy, Cyy}`,
  `cca(Cxx, Cxy, Cyy, {ridge})` → `{sigmas, A, B}`, `vamp(X0, Xt, {ridge})` → `{sigmas, A, B}` (SPEC 6.3),
  `edmd(X0, Xt, {ridge})` → `{K, eigvals, eigvecs}`.
- `lib/example.js` must expose a π sampler on the grid (`samplePi(n, rng)`) and `driftCoefficients(kappa)` (true
  monomial coefficients, for SINDy).
- `lib/graph.js` must expose the face C graph (`knnUnion(points, 15, {metric: "euclidean"})`, SPEC 3.5 and 6.3),
  `sinkhorn(K)`, and a matrix-free `lanczosSVD(matvec, rmatvec, n, k)`; `linalg.js` an `arnoldi(matvec, n, k)` for the
  eigenvalue moduli of $Q_\ell$.
- STLSQ lives in `p_koopman_edmd.js` (page-local): least squares, zero coefficients below the threshold, refit on the
  support, repeat ≤ 10 times.
- Widget keys and URL state: hero `hr` (`hr_start`, `hr_x0`, `hr_speed`, `hr_seed`, `hr_tour`); delay figure `dl`
  (single tour `default`); EDMD `ed` (`ed_dict`, `ed_n`, `ed_tau`, `ed_seed`, `ed_dt`, `ed_thr`, `ed_start`,
  `ed_tour`); lag `lg` (`lg_sys`, `lg_tau`, `lg_l`, `lg_th`, `lg_est`, `lg_n`, `lg_m`, `lg_knn`, `lg_dflow`,
  `lg_tour`); bowtie has no key.
- Tests: parity of `edmd`, `vamp`, `cca` against the builder (1e-8 on fixed inputs); the data-limit tours' tiles match
  `p03.json`; face C singular values vs `p03.json` `flow` (1e-6 relative); a test that every data-limit Ritz value is
  ≤ the true eigenvalue (surfaced in the UI, 13 below).

## 13. Page-specific definition-of-done additions

- [ ] The Ritz check is surfaced: if any data-limit EDMD eigenvalue exceeds the true one beyond 1e-9, the EDMD widget
      shows an error banner, never a silent plot.
- [ ] The words "pair", "well" and "product" are attached to eigenfunctions only through the builder's labels.
- [ ] The Takens disclaimer ("reconstruction, not linearity"; "noise needs separate care") is on the main path.
- [ ] The hero's `saddle` tour visibly hides the pair series with the "not excited from here" label (check the
      screenshot).
- [ ] In the `flow` tour, the statement of which block (2 or 4) is well separated is the builder's, quoted, and the
      graph is SPEC 3.5's face C construction; the page never says "pairs" or "wells" for face C without that value.
- [ ] Ledger's Running-example row and the gap statements in 3.5 use builder values (expected 0.78/0.07 and 0.63 are
      checks only).
- [ ] "Optimal"/"best" always comes with its sense ("best rank-r approximation in Hilbert-Schmidt norm", "maximal
      VAMP-2 score").
- [ ] The E13 and E19 cards (now `~`) are wrapped in the section 8 hook, with their exact cases stated outside it;
      3.3's obstruction is the direct degree argument, with no fixed-point-count theorem cited.

## Change log

- v1 (2026-11-17): first full spec.
- v1.1 (2026-11-17): reconciled with SPEC v1.1. Face C: SPEC 3.5's asymmetric input box is now the default, so the
  `shifted` option and its caveat are dropped; the graph is SPEC 3.5's binding face C construction (kNN union with a
  $10^{-6}$ floor and zero diagonal, replacing the unit diagonal). $\mu_0, \mu_\tau$ renamed $\pi_0, \pi_\tau$ (SPEC
  4.2, appendix A); `lib/cca.js` return names follow SPEC 6.3; `signal.json` basin labels, ϑ and the bibliography are
  now in SPEC, so the corresponding requests are removed.
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) 3.3's obstruction no longer rests on Brunton et al.'s
  "single isolated fixed point" statement, which has counterexamples; it is replaced by the direct argument for the
  running example (generator iterates of $x_1$ have strictly increasing odd degree), which also covers the noisy
  generator (C3.10; SPEC appendix C annotation and appendix D row). (2) E13 and E19 are `~` (SPEC 2.2), with exact
  cases stated: the Gaussian information bottleneck shares CCA's directions, not its truncation; face C's layers are
  flow steps by construction. Reviewer findings: math-1-6 8; math-7-10 9.
- v1.3 (2026-11-17): round-2 review fix (SPEC v1.3). 3.3's obstruction for the noisy dynamics was wrong: the
  running example's diffusion has reflecting boundaries, so its generator has Neumann conditions and $x_1$ is not in
  its domain, and "the diffusion term lowers degree" does not apply. The degree argument now covers only the
  deterministic drift; for the reflected diffusion the page uses that a finite-dimensional subspace invariant under
  the strongly continuous Koopman semigroup lies in the generator's domain, which $x_1$ (normal derivative ±1 on the
  walls $x_1 = \pm2.2$) is not in (3.3, C3.10; SPEC appendix C annotation and appendix D row). Reviewer finding:
  round 2, item 7.
