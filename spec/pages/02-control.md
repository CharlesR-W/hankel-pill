# Page spec 02: Linear control, balanced truncation and realization

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 2 |
| id (hash, file stem) | `control` |
| tab label | Linear control |
| kicker | Page 2 · control theory |
| title | Balanced truncation: keeping the states that are both easy to excite and easy to see |
| lede (one-sentence claim, ≤ 45 words) | For a linear system, the map from past inputs to future outputs is a Hankel operator. Balancing ranks its states by how easily they are excited and seen at once; dropping the weakest loses at most twice the sum of their Hankel singular values. |
| depends on | 1 (recommended; the page is readable alone) |
| edges (SPEC 2.2) | E1, E2, E4, E5 |
| faces of the running example | B (linear response of the ensemble, default), OU warm-up companion (SPEC 3.4) |
| main-path words | 2,200-2,600 |
| spec status | v1.2, 2026-11-17 (round-1 review fixes; change log) |

## 1. Reader outcome

After this page the reader can:

1. Write a linear time-invariant (LTI) system $(A, B, C)$, its impulse response $h(t) = Ce^{At}B$ and transfer function
   $G(s) = C(sI - A)^{-1}B$, and say why the response of the running example's ensemble to a small push is such a
   system (and why it describes an average, not a trajectory).
2. Define the Hankel operator $\Gamma$ (past inputs ↦ future outputs), factor it as $\Gamma = \mathcal O\,\mathcal C$
   through the state at time 0, and explain why its rank is the minimal state dimension (the same factorization as
   page 1's table, edge E1).
3. Compute the controllability and observability Gramians $W_c, W_o$ of a small system, interpret them as the energy
   needed to reach a state and the output energy a state produces, and obtain Hankel singular values
   $\sigma_i = \sqrt{\lambda_i(W_cW_o)}$.
4. Perform balanced truncation, state its error bound $\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$
   with its hypotheses, and check it against the actual error on the running example; say what optimal Hankel-norm
   (AAK) approximation adds.
5. Recover a system from samples of its impulse response by Ho-Kalman / ERA, and say what noise does to the
   singular values (Weyl) and what finite-sample identification results add.
6. Explain why PCA of the state is not balancing (it ignores what the output sees), and why, with noise in place of
   inputs, balancing becomes past-future canonical correlation analysis (edge E4).

What they see: a push along the diagonal moves probability toward the upper-right well, the up/down part of the
excess relaxes in a few time units and the left/right part over tens; the output is a sum of two slow exponentials and
a fast tail; two Hankel singular values stand far above the rest and the product pattern (wells $w_1, w_4$ against
$w_2, w_3$) never appears; on the two-state warm-up, the reachable and observable ellipses are tilted differently and
balancing turns them into one; the actual truncation error sits between the lower bound $\sigma_{r+1}$ and the
$2\Sigma$-tail; ERA reads two slow rates off a noisy impulse response.

## 2. Skim path

1. Lede (header).
2. Hero figure `control-fig-hero`: "Push the ensemble, watch the mean". Fig-sub: *A small push along the diagonal
   shifts probability between wells; the mean readout relaxes on two slow time scales, and two Hankel singular
   values carry almost all of the input-output map.*
3. Section headings (verbatim, these are the claims):
   - "A linear system is a map from past inputs to future outputs"
   - "The Hankel operator factors through the present state"
   - "Gramians measure how hard a state is to reach and to see"
   - "Balanced truncation loses at most twice the discarded singular values"
   - "Ho-Kalman reads the state space off the impulse response"
   - "With noise in place of inputs, balancing becomes past-future CCA"
4. Key-point callouts (one per section; gists in section 3).
5. Figure titles and fig-subs for `control-fig-bowtie`, `control-fig-gramians`, `control-fig-explorer`,
   `control-fig-era`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: a linear system's past-to-future map is a Hankel
operator; it factors through the state, so its rank is the minimal state dimension, as on page 1; Gramians weigh
states by input cost and output energy, and Hankel singular values combine the two; balanced truncation drops states
weak in both, with error between $\sigma_{r+1}$ and $2\sum_{j>r}\sigma_j$; PCA of the state is half of this and can
rank states differently; Ho-Kalman/ERA builds the model from impulse-response samples, and noise hides the small
singular values; in the running example linear response sees two slow states, not three, and only the ensemble
average; with noise as the input the same construction is past-future CCA (page 3).

## 3. Section outline

Section ids are `control-<slug>`; figure ids are `control-fig-<slug>` (SPEC 6.5). Word counts are main-path prose
only.

### 3.1 `control-system` "A linear system is a map from past inputs to future outputs" (≈ 420 words)

Placement: the hero sits between the lede and this heading. An "Arriving here first?" aside (≤ 80 words) sits at the
top of this section: "Page 1 arranges a process's behaviour as a table of pasts by futures and shows that the table's
rank is the size of the smallest machine that could produce it. This page does the same for a system driven by an
input: the table becomes a map from past inputs to future outputs." Link `#hankel`.

- Define an LTI system in continuous time: $\dot x = Ax + Bu$, $z = Cx$, state $x \in \mathbb R^n$, input u, output
  z (scalar here; say "single-input single-output"). Stable means every eigenvalue of A has negative real part.
- Impulse response $h(t) = Ce^{At}B$; output is the convolution $z(t) = \int_{-\infty}^t h(t-s)u(s)\,ds$; transfer
  function $G(s) = C(sI-A)^{-1}B$, and $|G(i\omega)|$ is the gain at frequency ω. Name $(A, B, C)$ a *realization*
  of G (glossary link: "realization"); any invertible change of state coordinates $x \mapsto Tx$ gives another
  realization of the same G.
- Running example, face B (introduce in three sentences, link `#map/map-example` for the full description): the
  particle in four wells; push every copy of it with a small uniform force $u(t)$ along the diagonal $d = (1,1)/\sqrt2$,
  and read the ensemble's mean $z(t) = \mathbb E[x_1 + x_2]$. For small u the density's deviation from equilibrium
  obeys a linear equation (the linearized Fokker-Planck equation), so $u \mapsto z$ is an LTI system whose state is the
  density deviation. The builder discretizes it and keeps the 60 slowest modes (state the assertion: the neglected
  modes change the system's $H_\infty$ norm by less than $10^{-4}$, quoted from `response.json`).
- Hero commentary (tour `pulse`): a short push moves probability toward $w_4$ and away from $w_1$; the up/down part of
  the excess relaxes within a few time units, the left/right part over tens; z(t) is a sum of decaying exponentials,
  two of them slow. Quote the two slow rates from the builder (expected ≈ 0.028 and 0.336, SPEC 3.2).
- Strain, stated here in two sentences: this system describes the **ensemble average**, not one noisy trajectory (a
  single particle hops at random; the average relaxes smoothly). Linearity is exact for the density equation and
  approximate only in neglecting terms of order $u^2$.
- Warm-up companion: near the well $w_4$ the drift is linear, giving a two-state system (SPEC 3.4):
  $A = -\mathrm{diag}(20, 33.\overline3)$, $B = d$, $C = (1, 1)$. Used in section 3.3.

Key callout: "A linear system is completely described by its impulse response. Everything on this page is a way of
compressing that one function."

Disclosures:
- "The maths: why the ensemble's response is linear" (≤ 500 words): the Fokker-Planck equation $\partial_t\rho =
  \mathcal L^*\rho$ with $\mathcal L^*\rho = \nabla\cdot(\rho\nabla V) + D\Delta\rho$; adding the force $u\,d$ adds
  $-u\,\nabla\cdot(\rho\, d)$; writing $\rho = \pi + \delta\rho$ and dropping $u\,\delta\rho$ gives
  $\partial_t\delta\rho = \mathcal L^*\delta\rho + u\,B$ with $B = -\nabla\cdot(\pi d)$ and output
  $z = \langle x_1 + x_2, \delta\rho\rangle$. The total-mass mode is uncontrollable (B integrates to zero) and is
  removed. In the generator's eigenbasis the system is diagonal: $A = -\mathrm{diag}(\nu_k)$ over the slow modes. Note
  that the input operator B (as SPEC 3.4 writes it) is not the potential's width parameter $b = 0.6$. Removing the
  mass mode does not make the model minimal: with A diagonal and distinct rates, mode k is controllable iff $B_k \ne 0$
  and observable iff $C_k \ne 0$; fluctuation-dissipation gives $B_k = \frac{\nu_k}{D\sqrt2}C_k$, so both vanish
  together; at κ = 0 separability and parity make $C_k = 0$ for all but 9 of the 60 modes (modes that depend on only one
  coordinate and are odd in it). The minimal realization is the restriction to the visible modes, with the count and
  the numerical tolerance stated; modes invisible by symmetry (exactly zero) are distinguished from modes with small
  positive Hankel singular values. At κ = 0.3 symmetry no longer forces zeros, and the builder reports the numerical
  rank at its tolerance.
- "In other fields: realization" (≤ 150 words): in control and automata theory a realization is a state-space model
  reproducing given input-output behaviour; in probability a stochastic realization is a Markov model of a process;
  it never means "an instance". Glossary link.

### 3.2 `control-hankel` "The Hankel operator factors through the present state" (≈ 380 words)

Placement: `control-fig-bowtie` after the second bullet.

- Split time at 0. The **Hankel operator** maps an input applied in the past to the output it causes in the future:
  $(\Gamma u)(t) = \int_0^\infty h(t + s)\,u(-s)\,ds$ for $t \ge 0$. It is the part of the input-output map that must
  pass through the present.
- It factors: the past input determines the state $x(0) = \int_0^\infty e^{As}Bu(-s)\,ds =: \mathcal C u$ (the
  controllability map), and the state determines the future output $z(t) = Ce^{At}x(0) =: (\mathcal O x(0))(t)$ (the
  observability map). So $\Gamma = \mathcal O\,\mathcal C$, a map through $\mathbb R^n$, and rank $\Gamma \le n$, with
  equality exactly when the realization is minimal (every state reachable and every state visible in the output).
- Running example, one or two sentences: the 60-mode response model is **not** minimal. In modal coordinates a mode
  is reachable exactly when the push excites it and visible exactly when the readout sees it, and by the symmetry of
  the separable potential most modes are neither: the builder finds exactly 9 of the 60 visible at κ = 0 (quote it).
  Every realization-based step below (Gramians, balancing, the bound) uses the **minimal realization** made of those
  modes (Kalman's canonical decomposition, Kalman 1963; trivial here because A is diagonal); the full model is kept
  for playing back the density.
- Discrete-time version (needed in section 3.5): sampled Markov parameters $h_k = CA_d^{k-1}B_d$ fill a block Hankel
  matrix $\mathbf H[i,j] = h_{i+j-1}$, constant along anti-diagonals, which factors the same way as
  (observability matrix) × (controllability matrix).
- Connect to page 1 (edge E1): page 1's table $H[p,f] = P(pf)$ factors as (row vector after the past) × (column vector
  for the future), and its rank is the minimal automaton dimension. Same construction: the past is compressed to a
  state, the future read from it. For a one-letter alphabet the two coincide literally: $P(\texttt a^k) =
  \alpha^\top A^k\beta$ is a sequence of Markov parameters.
- The singular values of Γ are the **Hankel singular values** $\sigma_1 \ge \sigma_2 \ge \dots$; $\sigma_1$ is the
  Hankel norm (the largest future-output energy per unit past-input energy).

Key callout: "Whatever the past input was, its whole effect on the future passes through the n numbers of the present
state. The Hankel operator's rank counts how many of them matter."

Disclosure "The maths: rank, minimality and the shift" (≤ 400 words): rank Γ = n iff (A,B) controllable and (A,C)
observable (Kalman); the shift structure of the block Hankel ($\mathbf H^{\uparrow} = \mathcal O_d A_d\mathcal C_d$)
recovers $A_d$; two minimal realizations differ by a unique invertible T. Cite Ho & Kalman 1966 and any control
textbook (Zhou, Doyle & Glover 1996, ch. 3).

### 3.3 `control-gramians` "Gramians measure how hard a state is to reach and to see" (≈ 450 words)

Placement: `control-fig-gramians` after the fourth bullet.

- Controllability Gramian $W_c = \int_0^\infty e^{At}BB^\top e^{A^\top t}dt$; observability Gramian $W_o =
  \int_0^\infty e^{A^\top t}C^\top Ce^{At}dt$. Both solve Lyapunov equations, $AW_c + W_cA^\top + BB^\top = 0$ and
  $A^\top W_o + W_oA + C^\top C = 0$ (one display equation for the pair).
- Energy meanings (Rahn 2001; Moore 1981): the least input energy that steers the state from rest (in the far past)
  to $x_0$ is $x_0^\top W_c^{-1}x_0$; the output energy released from $x_0$ with no further input is
  $x_0^\top W_ox_0$. A state is important to the input-output map if it is cheap to reach **and** loud to observe.
- Hankel singular values from the Gramians: $\sigma_i = \sqrt{\lambda_i(W_cW_o)}$ (one display equation). These are the
  singular values of Γ, so they do not depend on the coordinates chosen.
- **Balanced coordinates** are those in which $W_c = W_o = \Sigma = \mathrm{diag}(\sigma_i)$: the i-th state costs
  $1/\sigma_i$ to reach and gives back $\sigma_i$ of output energy (per unit size). A balancing transformation exists
  for every stable minimal system (Moore 1981); it needs both Gramians positive definite, which is why the minimal
  realization is extracted first (3.2). With a non-minimal realization the Gramians are singular and the
  inverse-based construction fails.
- Warm-up (widget tours `ou`, `balanced`): the two-state system at $w_4$. Its Hankel singular values (closed form,
  computed live; expected ≈ 0.0279 and 0.00042) differ by a factor of about 66: the input and output both act along
  the diagonal, and both coordinates relax at similar rates, so one combination carries almost the whole map.
- **PCA is half of balancing** (tour `pca`): the stationary covariance of the noise-driven state is the controllability
  Gramian for the noise input, $D(-A)^{-1}$ here (expected diag(0.025, 0.015)); PCA ranks $x_1$ first with a ratio of
  only 0.6 and ignores what the output sees. Balancing uses both Gramians. High-variance states need not be important
  input-output states.

Key callout: "PCA keeps the states that vary most. Balancing keeps the states that are both cheap to excite and loud to
observe, which is what the input-output map uses."

Disclosures:
- "The maths: energy interpretations and the balancing transformation" (≤ 500 words): derive the minimum-energy
  formula by least squares on $\mathcal C$; derive the output-energy formula; the square-root algorithm (Cholesky
  factors $W_c = RR^\top$, SVD of $R^\top L$ where $W_o = LL^\top$) giving T, applied to the minimal realization (both
  Cholesky factors need positive definite Gramians).
- "In other fields: observable" (≤ 150 words): in control a state is *observable* if the output distinguishes it; in
  Koopman analysis and physics an *observable* is a function of the state (page 3). Glossary link.

### 3.4 `control-truncate` "Balanced truncation loses at most twice the discarded singular values" (≈ 450 words)

Centrepiece: `control-fig-explorer`.

- Balanced truncation: in balanced coordinates keep the first r states, i.e. partition $(A, B, C)$ conformally and keep
  $(A_{11}, B_1, C_1)$, giving $G_r$.
- The bound (one display equation): if the system is stable and minimal and $\sigma_r > \sigma_{r+1}$, then $G_r$ is
  stable and minimal and
  $$\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j,$$
  the sum running over the **distinct** discarded values. $\|\cdot\|_{H_\infty}$ is the worst-case gain over all
  frequencies, equivalently the largest output-error energy per unit input energy. Attribution: balancing, Moore 1981;
  stability of the truncation, Pernebo & Silverman 1982; the upper bound, Enns 1984 and Glover 1984. The lower bound
  holds for **every** order-r approximation, not only this one.
- Optimal Hankel-norm approximation (AAK; Glover 1984): among all stable systems of order r, the smallest achievable
  Hankel-norm error is exactly $\sigma_{r+1}$, and Glover's state-space formulas construct the minimizers. Balanced
  truncation is not optimal in either norm, but is within the factor of the bound (Rahn 2001). This optimality is
  constructive for linear systems and for one-letter automata only (page 1, edge E2); state it no more widely.
- Running example (tour `r2`): two Hankel singular values stand far above the rest, then a tail from motion inside the
  wells. Quote the builder's σ₁..σ₅. At r = 2 compare the actual $H_\infty$ error with $\sigma_3$ and
  $2\sum_{j>2}\sigma_j$ (builder values; the explorer's tiles).
- What the two balanced states are: the builder decomposes each balanced state on the generator's modes. Expected,
  from a two-mode estimate: the first is mostly the left/right (pair) mode with an admixture of the up/down mode, the
  second mostly up/down; quote the builder's loadings. Balanced states are input-output channels, not individual slow
  modes: under fluctuation-dissipation (section 3.6) a single mode's Hankel singular value depends on how much of the
  readout's variance it carries, not on how slow it is.
- **Strain, stated here** (tour `kappa`): the input and output each act on $x_1$ and $x_2$ separately (separable
  potential), so the product mode, which tells $w_1, w_4$ from $w_2, w_3$, has zero residue: **linear response sees two
  slow states, not three**. A four-well partition needs a nonlinear readout (page 1's symbols) to show its fourth set.
  The builder asserts the residue is below $10^{-8}$ at κ = 0; at κ = 0.3 (SPEC 3.2's tilt, which breaks the up/down
  mirror symmetry that made it vanish) it becomes small but
  nonzero (quote). So on this page "r = 2" keeps both slow axes, left/right and up/down; there is no slow third state to
  keep.
- Modal truncation for contrast (tour `modal3`): keeping the r slowest modes is a different rule; at r = 3 it keeps
  the invisible product mode and gains nothing, while balanced truncation adds the next most important channel.
  Slowness is not importance.

Key callout: "The error of dropping balanced states is at least the first dropped singular value and at most twice the
sum of all dropped ones. In the running example two states carry the map."

Disclosures:
- "Hypotheses: when the bound holds" (≤ 300 words): stable (Hurwitz A), minimal, $\sigma_r > \sigma_{r+1}$ (strict),
  distinct values counted once; continuous-time statement (a discrete-time analogue holds with the same form). The bound
  is a worst case over inputs; for a particular input the error can be far smaller. The explorer computes the
  $H_\infty$ norm on a frequency grid, which can only understate the true supremum (state the grid).
- "The maths: why the lower bound holds for any approximation" (≤ 300 words): Hankel norm ≤ $H_\infty$ norm; a
  rank-r Hankel operator cannot approximate Γ better than $\sigma_{r+1}$ (Eckart-Young / Schmidt for compact
  operators); AAK says the infimum over *Hankel* operators of rank r is the same $\sigma_{r+1}$.
- "AAK and Glover" (≤ 300 words): Adamyan-Arov-Krein 1971 for scalar Hankel operators; Glover 1984 for multivariable
  state space with all optimal solutions characterized. Glover also gives an $L_\infty$ error bound for a suitably
  chosen optimal Hankel-norm approximant in terms of the discarded tail: **the page writer quotes it only after
  checking the exact statement (constant term, distinct values) in Glover 1984 §9 or Zhou, Doyle & Glover 1996 ch. 8;
  otherwise omit it**. Pointer to page 1's one-letter results (Balle et al. 2021; Lacroce et al. 2023).

### 3.5 `control-realize` "Ho-Kalman reads the state space off the impulse response" (≈ 400 words)

Placement: `control-fig-era` after the third bullet.

- Ho & Kalman 1966: given exact Markov parameters $h_1, h_2, \dots$, form the block Hankel matrix, factor it as
  (observability) × (controllability) (e.g. by SVD, $\mathbf H = U\Sigma V^\top$, $\mathcal O_d = U\Sigma^{1/2}$,
  $\mathcal C_d = \Sigma^{1/2}V^\top$), read C from the first row block of $\mathcal O_d$, B from the first column block
  of $\mathcal C_d$, and $A_d$ from the shifted block: $A_d = \Sigma^{-1/2}U^\top\mathbf H^{\uparrow}V\Sigma^{-1/2}$.
  This is page 1's realization from shifted blocks, symbol for symbol (E1).
- The eigensystem realization algorithm (ERA; Juang & Pappa 1985) truncates the SVD at r first: a reduced model read
  off the leading singular directions, which in coordinates is approximately balanced (the factors split $\Sigma$
  evenly).
- Running example: sample face B's impulse response every Δ = 0.25 (builder: $h_1..h_{255}$, a 128 × 128 block),
  run ERA at r = 2, and convert the recovered discrete poles to rates $\hat\nu = -\log\hat\lambda/\Delta$. Quote the
  builder's recovered rates against the true slow rates.
- Noise: add independent measurement noise to the samples (the figure shows two levels). By Weyl's inequality every
  singular value moves by at most $\|E\|_2$, the spectral norm of the noise's Hankel matrix, so singular values below
  that floor are not identified (the same lesson as page 1's sampling section). Quote the builder's floors and which
  singular values clear them.
- Finite data in general: Oymak & Ozay 2019 bound the error of Markov parameters estimated from one input-output
  trajectory and show that Ho-Kalman is robust to such errors, giving non-asymptotic guarantees for recovering a
  balanced realization; their hypotheses (stability, random excitation, a margin on the r-th Hankel singular value)
  are stated in the disclosure. Status `conditional`.

Key callout: "Ho-Kalman is page 1's realization applied to an impulse response. Noise sets a floor, and the smallest
Hankel singular values are the first to fall below it."

Disclosures:
- "The maths: Ho-Kalman and ERA step by step" (≤ 500 words): the factorization, the shift, why the result is unique up
  to T, why ERA's split $\Sigma^{1/2}$/$\Sigma^{1/2}$ is close to balanced for a long block (the finite block's Gramians
  approach the infinite ones); sampled-data relation $A_d = e^{A\Delta}$, $B_d = A^{-1}(e^{A\Delta} - I)B$ (zero-order
  hold) and why discrete-time Hankel singular values differ from continuous ones (so the figure compares ERA with the
  sampled system, not with the explorer's continuous values).
- "Hypotheses: finite-sample identification" (≤ 300 words): Oymak & Ozay 2019's setting (single trajectory, Gaussian
  input, stable A, process and measurement noise), the $1/\sqrt{T}$ rate for Markov parameters, the robustness lemma
  for Ho-Kalman requiring a lower bound on the r-th singular value of the Hankel block. Mark status `conditional`; no
  numbers from their paper.
- "In other fields: four tables called Hankel" (≤ 200 words): process Hankel (page 1); block Hankel of Markov
  parameters (here); trajectory / delay Hankel of a time series (page 3, HAVOK); extended logit matrix (page 9).
  Different objects with different ranks. Glossary link.

### 3.6 `control-noise` "With noise in place of inputs, balancing becomes past-future CCA" (≈ 320 words)

No figure. One display equation at most.

- Replace the deterministic input by white noise: the output becomes a stationary random process. Its past and future
  are correlated only through the state. Akaike 1975 built Markovian state representations from the **canonical
  correlations** between past and future of such a process; Desai & Pal 1984 showed that, for linear-Gaussian
  processes, the canonical directions give a *stochastically balanced* realization, whose truncation is stochastic
  balanced truncation. This is the same construction with the two Gramians replaced by the past and future
  covariances (whitening on both sides). Edge E4, page 3, where the same CCA becomes the singular value decomposition
  of a Koopman operator for nonlinear Markov processes.
- Fluctuation-dissipation (edge E5): for the reversible running example the response to a small push is minus the
  time-derivative of an equilibrium correlation function divided by D, $h(t) = -\tfrac1D\tfrac{d}{dt}\,
  \mathbb E_\pi[(x_1+x_2)(t)\,(d\cdot x)(0)]$ (Kubo 1966). Expanding in generator modes, both have the same decay
  rates and the same mode-by-mode weights up to the factor $\nu_k/D$. So this page's response Hankel and page 3's
  correlation operator share their slow modes. Mode by mode, $B_k = \frac{\nu_k}{D\sqrt2}C_k$: proportional, but with a
  factor that changes with k, so the modal realization is **not** symmetric and its Gramians are not proportional.
  Rescaling mode k by $(D\sqrt2/\nu_k)^{1/2}$ leaves A diagonal and makes $B = C^\top$: a state-space-symmetric
  realization, in which the two Gramians are equal, so balancing reduces to diagonalizing one of them (on the visible
  modes).
- Close the page's argument: the response Hankel sees the slow dynamics only through the chosen push and readout;
  the next page removes that restriction by decomposing the dynamics' action on all functions of the state.

Key callout: "Driving with noise instead of a chosen input turns the Hankel operator into a cross-covariance between
past and future; whitening both sides makes balancing into canonical correlation analysis."

Disclosure "The maths: fluctuation-dissipation in two lines" (≤ 400 words): with $B = -\nabla\cdot(\pi d) =
-\pi\,\mathcal L(d\cdot x)/D$ and reversibility ($e^{t\mathcal L^*}(\pi f) = \pi e^{t\mathcal L}f$), $h(t) = \langle
x_1 + x_2, e^{t\mathcal L^*}B\rangle = -\tfrac1D\tfrac{d}{dt}\mathbb E_\pi[(x_1+x_2)\,\mathcal K_t(d\cdot x)]$; modal
form $h(t) = \tfrac{1}{D\sqrt2}\sum_k \nu_kc_k^2e^{-\nu_kt}$ with $c_k = \langle x_1+x_2, \phi_k\rangle_\pi$; the product
mode has $c_k = 0$ by separability.

### 3.7 `control-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.8 `control-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.9 `control-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C2.1 | An LTI system is determined (as an input-output map) by its impulse response $h(t) = Ce^{At}B$; realizations of the same G differ by state-coordinate changes. | standard | Zhou, Doyle & Glover 1996 | zero initial state; stable for the convolution over $(-\infty, t]$ | 3.1 |
| C2.2 | The ensemble's mean response to a small uniform force is an LTI system whose state is the density deviation; 60 modes reproduce it to $10^{-4}$ in $H_\infty$. | construction + builder assertion | disclosure "why the ensemble's response is linear"; `response.json` assertion | linearization in u (terms $O(u^2)$ dropped); mass mode removed | 3.1 |
| C2.3 | The response's slow decay rates are the generator's slow relaxation rates (expected ≈ 0.028 and 0.336). | widget + builder values | hero tour `pulse`; `response.json` rates | κ = 0 | 3.1 |
| C2.4 | Face B describes the ensemble average, not a single trajectory. | construction | 3.1 prose; hero (a) shows the density, not a particle | — | 3.1 |
| C2.5 | The Hankel operator factors as $\Gamma = \mathcal O\mathcal C$ through $\mathbb R^n$; rank Γ ≤ n with equality iff the realization is minimal. | theorem | Ho & Kalman 1966; Kalman's controllability/observability; bowtie | stable LTI | 3.2 |
| C2.6 | Page 1's process Hankel and this Hankel operator are the same construction; for one letter they coincide literally. | theorem (E1) | Ho & Kalman 1966; Fliess 1974; Carlyle & Paz 1971; Balle et al. 2014 | one-letter alphabet for literal coincidence | 3.2 |
| C2.7 | $x_0^\top W_c^{-1}x_0$ is the minimum input energy to reach $x_0$; $x_0^\top W_ox_0$ is the output energy from $x_0$. | standard | Moore 1981; Rahn 2001 | stable, controllable (for $W_c^{-1}$) | 3.3 |
| C2.8 | Hankel singular values are $\sqrt{\lambda_i(W_cW_o)}$, coordinate-independent, and equal the singular values of Γ. | standard | Rahn 2001; Glover 1984 | stable | 3.3 |
| C2.9 | Every stable minimal system has balanced coordinates with $W_c = W_o = \mathrm{diag}(\sigma_i)$. | theorem | Moore 1981 | stable, minimal | 3.3 |
| C2.9a | Face B's 60-mode model is not minimal: at κ = 0 exactly 9 modes are visible ($B_k = C_k = 0$ for the rest); balancing is applied to the minimal realization on the visible modes. | construction + builder assertion | Kalman 1963; FDT $B_k = \nu_kC_k/(D\sqrt2)$; `response.json` `minimal` | diagonal A with distinct rates; stated tolerance | 3.2-3.3 |
| C2.9b | In modal coordinates $B_k \propto C_k$ with a k-dependent factor; rescaling each mode gives a state-space-symmetric realization with equal Gramians. | construction | FDT (Kubo 1966); disclosure in 3.6 | reversible dynamics; visible modes | 3.6 |
| C2.10 | On the OU warm-up the two Hankel singular values differ by a factor of about 66 while PCA of the stationary state ranks the coordinates with ratio 0.6; PCA uses only the (noise) controllability Gramian. | widget (live closed form) | `control-fig-gramians` tours `ou`, `pca` | noise covariance 2D·I; output (1,1) | 3.3 |
| C2.11 | Balanced truncation of a stable minimal system with $\sigma_r > \sigma_{r+1}$ is stable and satisfies $\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$ (distinct values). | theorem | Enns 1984; Glover 1984; Pernebo & Silverman 1982 (stability); Rahn 2001 (statement) | stable, minimal, strict gap at r, distinct values counted once | 3.4 |
| C2.12 | No order-r system has $H_\infty$ (or Hankel-norm) error below $\sigma_{r+1}$; the optimal Hankel-norm error is exactly $\sigma_{r+1}$ and is attained constructively (AAK/Glover). | theorem | Adamyan, Arov & Krein 1971; Glover 1984 | stable; order-r competitors | 3.4 |
| C2.13 | Constructive AAK is established for LTI systems and one-letter automata only. | theorem (scope-limited) | Balle et al. 2021; Lacroce et al. 2023 | — | 3.4 |
| C2.14 | Face B has two Hankel singular values far above the rest, then an intra-well tail; at r = 2 the actual error lies between $\sigma_3$ and $2\sum_{j>2}\sigma_j$. | widget + builder assertion | explorer tour `r2`; `response.json` | κ = 0; $H_\infty$ on the stated frequency grid | 3.4 |
| C2.15 | The balanced states are mixtures of generator modes (expected: first mostly pair, second mostly up/down). | builder values | explorer advanced "loadings" table; `p02.json` `loadings` | — | 3.4 |
| C2.16 | The product mode has zero residue at κ = 0 (linear response sees two slow states); at κ = 0.3 its residue is small but nonzero. | construction + builder assertion | disclosure in 3.6 (separability); explorer tour `kappa`; tile "product-mode residue" | separable potential at κ = 0 | 3.4 |
| C2.17 | Keeping the slowest r modes is not balanced truncation; at r = 3 modal truncation keeps the invisible product mode. | widget | explorer tour `modal3` | κ = 0 | 3.4 |
| C2.18 | Ho-Kalman recovers a minimal realization from exact Markov parameters via factorization and shift; it is page 1's realization from shifted blocks. | theorem | Ho & Kalman 1966; Juang & Pappa 1985; page 1 | block large enough to have full rank n | 3.5 |
| C2.19 | ERA at r = 2 on face B's sampled impulse response recovers the two slow rates (builder values); with noise, singular values below $\|E\|_2$ are not identified (Weyl). | widget + theorem | `control-fig-era`; Weyl | noise level as stated; Δ = 0.25, 128 × 128 block | 3.5 |
| C2.20 | From a single noisy trajectory, Markov parameters and a balanced realization can be estimated with non-asymptotic error bounds. | theorem (conditional) | Oymak & Ozay 2019 | stability, random input excitation, noise model, margin on the r-th Hankel singular value | 3.5 |
| C2.21 | For linear-Gaussian processes, past-future CCA yields a stochastically balanced realization (Akaike; Desai & Pal). | theorem (E4) | Akaike 1975; Desai & Pal 1984 | stationary, linear-Gaussian, finite-dimensional | 3.6 |
| C2.22 | For the reversible example, the response kernel is $-\tfrac1D\tfrac{d}{dt}$ of an equilibrium correlation; both share decay rates and slow modes (E5). | theorem (standard) + construction | Kubo 1966; Risken 1989; disclosure derivation | reversible (gradient) dynamics; force is the gradient of a linear potential; equilibrium start | 3.6 |

Things not to claim on this page (SPEC appendix D and page-specific): balanced truncation is optimal; AAK applies to
multi-letter automata or language models; the balanced states are the generator's slow modes; linear response sees all
four wells; face B describes single trajectories; high-variance (PCA) states are the important ones; a finite or noisy
block certifies the system order; the $2\Sigma$ bound holds without stability, minimality or a strict gap.

## 5. Figures and widgets

### 5.1 `control-fig-hero` "Push the ensemble, watch the mean" (live, hero; key `hr`)

- **Purpose:** a small push along the diagonal shifts probability between wells; the mean readout relaxes on two slow
  time scales; two Hankel singular values carry the map.
- **Layout:** `figure.fig.full.card`, three panels left to right (stacked on phones):
  (a) **density deviation** $\delta\rho(x, t)/\pi(x)$ over Ω as a `heatmap` (`div` map, symmetric range fixed per tour
  at the maximum over the tour's time window), ink contours of V, wells as ink-outlined circles labelled $w_1..w_4$, an
  ink arrow along d labelled "push" that is drawn while $u(t) \ne 0$;
  (b) **traces**: input u(t) (thin, upper strip) and output z(t) (main axes), t from −5 to 120, with the accent "now"
  cursor; dashed grey: the two slowest modal contributions to z(t), each on its own;
  (c) **Hankel singular values** of the minimal realization, σ₁..σ₁₀ or as many as it has (9 at κ = 0; `barChart`, log y), r = 2 marked by an accent line and bars beyond it
  hatched. Static during the animation.
- **Data:** precomputed `data/example/response.json` (κ = 0): modal rates $\nu_k$, modal B and C (60 modes), the grid
  eigenfunction index of each mode (for drawing $\delta\rho/\pi = \sum_k a_k(t)\phi_k$ from `data/example/grid.json`
  display-grid eigenfunctions), Hankel singular values. Modal coefficients $a_k(t)$ evolve in closed form (diagonal A),
  so playback is exact at any frame rate.
- **Controls:** transport (play/pause, speed ×1/×4/×16 in model time units per second 2/8/32), reset; input shape
  (segmented: `pulse` = u = 1 for t ∈ [0, 1]; `step` = u = 1 for t ∈ [0, 60], then 0). Two primary controls.
- **Default state (= first tour):** `pulse`, t = −5, autoplay when scrolled into view (centrepiece rule); under reduced
  motion the `pulse-late` still is shown.
- **What changes:** time advances; in (a) the dipole patterns inside each well vanish within a fraction of a time unit,
  the up/down contrast fades over a few units, the left/right contrast over tens; (b) the cursor moves and z(t) draws
  in; input shape swaps u(t) and recomputes the traces.
- **Tours:** `pulse` (default; t = −5, playing); `pulse-early` (paused at t = 2: up/down and left/right contrasts both
  present); `pulse-late` (paused at t = 15: only the left/right contrast left); `step` (step input, paused at t = 60:
  the near-steady response).
- **fallbackTour:** `pulse-early`.
- **Caption:** *Plotted:* (a) relative density deviation $\delta\rho/\pi$ at the current time (blue negative, red
  positive), contours of V, wells $w_1..w_4$; (b) input u(t) and mean output $z(t) = \mathbb E[x_1+x_2] - \mathbb
  E_\pi[x_1+x_2]$ of the linearized ensemble, dashed: contributions of the two slowest modes; (c) Hankel singular values
  of the input-output system, log scale, r = 2 marked. *Values:* force along $d = (1,1)/\sqrt2$, 60 slowest modes,
  κ = 0, $h_x = 2.5$, $h_y = 1.5$, $b = 0.6$, D = 0.5. Running example, face B. `synthetic`. Amplitudes are per unit
  force (the system is linear).
- **Static fallback:** `assets/fallback/control-fig-hero-pulse-early.png` (and one PNG per tour); GIF
  `assets/fallback/control-fig-hero.gif` (≈ 6 s, `pulse` tour at ×16 from t = −5 to t = 90).
- **Accessibility:** alt text: "A heat map of the particle's probability shifting toward the upper-right well after a
  push, the mean readout rising and decaying on two time scales, and a bar chart with two tall bars and a short tail."
  The fig-sub carries the message without motion or colour; (a) has a text readout of the left/right and up/down
  contrasts at the cursor.
- **Performance:** per frame: 60 exponentials, a 88 × 60 sum over ≤ 60 modes (truncate to modes with $|a_k| > 10^{-6}$
  of the maximum) ≈ 1 ms.

### 5.2 `control-fig-bowtie` "Past inputs, a small state, future outputs" (static SVG)

- **Purpose:** Γ factors through an n-dimensional knot; balancing orders the knot's bars by Hankel singular value.
- **Data:** shared `bowtie` component. Labels: left "past inputs u(t), t < 0", left norm "input energy ($W_c$)", right
  "future outputs z(t), t > 0", right norm "output energy ($W_o$)"; knot bars: face B's σ₁..σ₈ from `response.json`
  (square-root scale, as on page 1, stated in the caption); r = 2; bound label "lost ≤ 2 Σ_{j>r} σ_j ($H_\infty$)"
  (SPEC 1.4). Above the fans: "Gramians".
- **Controls:** none required; if the component's draggable r is on, the hatching and the bound value follow r (no
  URL state).
- **Caption:** *Plotted:* schematic of $\Gamma = \mathcal O\,\mathcal C$: past input ↦ state $x(0)$ ↦ future output;
  bars are face B's Hankel singular values, square-root scale; hatched: discarded at r = 2. *Values:* as the hero.
- **Fallback:** the SVG itself; PNG export `assets/fallback/control-fig-bowtie-default.png`.

### 5.3 `control-fig-gramians` "Reachable and observable, then balanced" (live; key `gr`)

- **Purpose:** the two Gramians weigh state directions differently; balancing makes them one diagonal ellipse; PCA
  of the state uses only one of them.
- **Layout:** `figure.fig.wide.card`; left: state-plane view (square, 360 px); right: side panel with tours, controls,
  two small charts and tiles.
  - (a) **State plane** $(x_1, x_2)$ in current coordinates: the reachability ellipse $\{x : x^\top W_c^{-1}x = 1\}$
    (semi-axes $\sqrt{\lambda(W_c)}$; states reachable with unit input energy; `--c-pair-L` outline), the
    observability ellipse $\{x : x^\top W_o^{-1}x = 1\}$ (semi-axes $\sqrt{\lambda(W_o)}$; long where a state is loud;
    `--c-pair-R` outline), and, dashed grey, the stationary-covariance ellipse of the noise-driven state ($x^\top
    \Sigma_x^{-1}x = 1$, the PCA ellipse). Arrows for the input direction B and output direction $C^\top$. Axes and
    ellipses rescale so the largest semi-axis fills 80 % of the view; the scale is shown.
  - (b) **Bars**: $\sigma_1, \sigma_2$ (Hankel singular values) beside the PCA variances $\lambda_1(\Sigma_x),
    \lambda_2(\Sigma_x)$, each pair normalized to its first value, log y.
  - (c) **Impulse response** h(t) of the full system and of its r = 1 balanced truncation, t ∈ [0, 0.3].
- **Data:** live closed form via `lib/lti.js` (`gramians`, `balance`, `truncate`); 2 × 2 Lyapunov equations solved
  exactly.
- **Controls (primary):**
  1. input angle $\theta_B$ (slider 0°-180°, default 45°: $B = (\cos\theta_B, \sin\theta_B)$);
  2. output angle $\theta_C$ (slider 0°-180°, default 45°: $C = \sqrt2(\cos\theta_C, \sin\theta_C)$, so the default is
     (1, 1));
  3. stiffness ratio $a_2/a_1$ (slider 1-5 log, default 5/3, with $a_1 = 20$ fixed; $A = -\mathrm{diag}(a_1, a_2)$);
  4. coordinates (slider "original → balanced", 0-1, default 0): the view is drawn in coordinates $T(s)x$ with
     $T(s) = \exp(s\log T_{\rm bal})$ when $T_{\rm bal}$ has a real logarithm, otherwise $(1-s)I + sT_{\rm bal}$ (the
     helper checks invertibility along the path and falls back to a cross-fade if needed).
  Advanced: noise D (default 0.5; affects only the PCA ellipse).
- **What changes:** angles move the arrows and reshape both Gramian ellipses (and the bars, tiles, and (c)); the
  stiffness ratio reshapes all three ellipses; the coordinates slider morphs the view until the two Gramian ellipses
  coincide as one axis-aligned ellipse with semi-axes $\sqrt{\sigma_i}$ (the PCA ellipse is transformed too, and does
  not become axis-aligned).
- **Stat tiles:** "$\sigma_1, \sigma_2$" (3 s.f.); "$\sigma_2/\sigma_1$"; "PCA ratio $\lambda_2/\lambda_1$"; "angle
  between top balanced and top PCA directions" (degrees, measured in original coordinates).
- **Tours:**
  1. `ou`: defaults (θ_B = θ_C = 45°, ratio 5/3, s = 0). Note: "The two-state linearization at $w_4$. Two
     ellipses, tilted differently from the PCA ellipse."
  2. `balanced`: as `ou`, s = 1. Note: "In balanced coordinates both Gramians are the same diagonal ellipse; its
     axes are the Hankel singular values."
  3. `pca`: θ_B = θ_C = 80°, ratio 5/3, s = 0. Note: "Input and output act mostly on the stiff coordinate $x_2$. PCA
     still ranks $x_1$ first; balancing ranks the $x_2$-like direction first." (Expected angle between the top
     directions ≈ 78°; at the `ou` defaults it is already ≈ 38°.)
  4. `hidden`: θ_B = 45°, θ_C = 135°, ratio 5/3, s = 0. Note: "The output direction is perpendicular to the input:
     what the push excites is barely seen, so the largest Hankel singular value drops (by about a factor of three
     here) although nothing about the reachable states changed." (Expected σ ≈ 0.0085, 0.0014; live values shown.)
- **fallbackTour:** `ou`.
- **Caption:** *Plotted:* (a) in state coordinates (original or partly balanced), the sets $x^\top W_c^{-1}x = 1$
  (reachable with unit input energy), $x^\top W_o^{-1}x = 1$ (long where a state's output energy is large), and the
  stationary covariance ellipse of the noise-driven state (dashed); arrows B and $C^\top$; (b) Hankel singular values and
  PCA variances, each normalized by its largest; (c) impulse response $Ce^{At}B$ and its one-state balanced
  truncation. *Values:* $A = -\mathrm{diag}(20, 20\cdot\text{ratio})$, B, C as set, D = 0.5. Default: the Ornstein-
  Uhlenbeck linearization at $w_4$ (running example, OU companion). `synthetic`.
- **Static fallback:** PNG per tour `assets/fallback/control-fig-gramians-<tour>.png`; GIF
  `assets/fallback/control-fig-gramians.gif` (≈ 4 s: s from 0 to 1 on the `ou` tour).
- **Accessibility:** alt text: "Two tilted ellipses for the reachable and observable states and a dashed covariance
  ellipse; as the coordinates change, the two solid ellipses merge into one." Ellipses are distinguished by line style
  as well as colour (solid thin, solid thick, dashed) and labelled in the legend.
- **Performance:** closed form, < 1 ms per change.

### 5.4 `control-fig-explorer` "Balanced truncation of the running example" (live, centrepiece; key `ex`)

- **Purpose:** two Hankel singular values carry face B; the actual truncation error sits between $\sigma_{r+1}$ and
  $2\sum_{j>r}\sigma_j$; slowness is not importance; the product mode is invisible.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`; main view four linked panels in a 2 × 2 grid; side panel
  (320 px) with tours, controls, tiles, legend.
  - (a) **Spectrum**: σ₁..σ₁₂ (`barChart`, log y); bars coloured by the builder's label of each balanced state's
    dominant modal loading ("left/right (pair)" `--c-pair-L` tint; "up/down (well in pair)" `--c-well-2` tint;
    "product" `--c-well-4` tint; "inside a well" `--c-other`); r as an accent line, discarded bars hatched. In
    `modal` method, open circles mark the modes kept by modal truncation, placed at their own modal Hankel singular
    values (the Hankel singular value of each one-mode subsystem).
  - (b) **Frequency response**: $|G(i\omega)|$ (solid ink) and $|G_r(i\omega)|$ (`seq-5`) for ω from $10^{-3}$ to
    $10^{3}$ (log-log); below it, on its own log axis, the error $|G(i\omega) - G_r(i\omega)|$ with two horizontal
    references: $\sigma_{r+1}$ (dotted) and $2\sum_{j>r}\sigma_j$ (dashed).
  - (c) **Step response**: z(t) for a unit step at t = 0, full and reduced, t ∈ [0, 150].
  - (d) **Error against r**: r = 1..8 on x, log y. Series: "balanced truncation, $\|G-G_r\|_{H_\infty}$" (solid,
    dots); "bound $2\sum_{j>r}\sigma_j$" (dashed); "lower bound $\sigma_{r+1}$ (= optimal Hankel-norm error)" (dotted);
    "modal truncation (slowest r modes)" (grey, open dots). Cursor at the current r.
- **Data:** precomputed `data/example/response.json` for κ = 0 and κ = 0.3 (system, Gramians, Hankel singular values
  top 20, balancing transformation, reduced systems $(A_r, B_r, C_r)$ for r = 1..8, $H_\infty$ errors for balanced and
  modal truncation r = 1..8, product-mode residue) and `data/control/p02.json` (`loadings`: for each balanced state
  1..8, the squared loadings on pair, up/down, product and all other modes; `labels`). Frequency and step responses
  of full and reduced systems are computed live by `lib/lti.js` from the stored matrices (60 × 60 diagonal plus rank-
  one structure; cheap). OU model: live closed form as in 5.3.
- **Controls (primary):**
  1. model: `face B, κ = 0` | `face B, κ = 0.3` | `OU warm-up` (select);
  2. r: slider 1-8 (1-2 for OU) with marks at 2 ("two slow states");
  3. method: segmented `balanced` | `modal (slowest r)`.
  Advanced: show loadings table (toggle: a small table of `loadings` for the retained states); frequency-grid density
  (default 2,000 log-spaced points plus local refinement around the maximum).
- **What changes when each control moves:**
  - model: all panels recompute; the colour labels apply to face B only; r's range changes for OU.
  - r: (a) moves the line and hatching; (b) and (c) redraw the reduced curves and the error with its references; (d)
    moves the cursor; tiles update.
  - method: (b) and (c) use the modal truncation instead; (a) adds the open circles; (d) highlights the modal series;
    the bound references in (b) stay those of balanced truncation (the legend says the bound is for balanced
    truncation only).
- **Stat tiles:** "$\|G - G_r\|_{H_\infty}$" (max of the error curve over the grid, labelled "on grid"); "$\sigma_{r+1}$";
  "$2\sum_{j>r}\sigma_j$"; "error / bound" (ratio); "product-mode residue" (the residue of the product mode in z,
  $|C_kB_k|$ for that mode, from `response.json`; "0 (< 1e-8)" at κ = 0).
- **Tours** (default first):
  1. `r2`: face B κ = 0, r = 2, balanced. Note: "Two states carry the map; the error lies between $\sigma_3$ and the
     2Σ-tail."
  2. `r1`: face B κ = 0, r = 1, balanced. Note: "One state: the left/right channel alone. The up/down relaxation is
     lost."
  3. `modal3`: face B κ = 0, r = 3, modal. Note: "The third-slowest mode is the product mode, which the readout cannot
     see: modal truncation gains nothing from it."
  4. `kappa`: face B κ = 0.3, r = 2, balanced. Note: "With the tilt (upper wells switch pairs more readily) the product mode gets a small residue."
  5. `ou`: OU warm-up, r = 1, balanced. Note: "Two states, one nearly redundant: the bound and the error are both tiny."
- **fallbackTour:** `r2`.
- **Caption:** *Plotted:* (a) Hankel singular values $\sigma_i$ of the chosen system (log), coloured by the dominant
  generator mode of each balanced state; (b) gain $|G(i\omega)|$ of the full and reduced systems and the error
  $|G - G_r|$ against frequency, with $\sigma_{r+1}$ (dotted) and $2\sum_{j>r}\sigma_j$ (dashed); (c) unit-step responses;
  (d) $H_\infty$ error of balanced and modal truncation against r with the lower and upper bounds. $H_\infty$ norms are
  maxima over the stated frequency grid. *Values:* model, r and method as set; face B uses 60 slowest modes. Running
  example, face B (or OU companion). `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/control-fig-explorer-<tour>.png`); GIF
  `assets/fallback/control-fig-explorer.gif` stepping r = 1..6 on face B κ = 0 (1 s per frame).
- **Accessibility:** each panel has an `aria-label`; tiles are text; tours announce their note; the series in (d) differ
  by line style and marker as well as colour.
- **Performance:** frequency response of a diagonal-plus-rank-one 60-state system on 2,000 points ≈ 2 ms; reduced
  systems are ≤ 8 × 8. Parity: live $H_\infty$ errors match the builder's stored values to 1e-6 relative.

### 5.5 `control-fig-era` "Reading the system off a noisy impulse response" (static, rendered by the page module)

- **Purpose:** the block Hankel of sampled impulse responses has two dominant singular values; ERA at r = 2 recovers
  the two slow rates; measurement noise raises a floor that the small singular values sink below.
- **Data:** precomputed `data/control/p02.json` `era`: sampled impulse response $h_k$ of face B's zero-order-hold
  discretization at Δ = 0.25 (k = 1..255), the 128 × 128 block's singular values (top 20) for noise levels
  η ∈ {0, 10⁻⁴, 10⁻³} × max|h| (independent Gaussian noise added to each $h_k$, seed 0), the floor $\|E\|_2$ for each
  noisy level, the exact discrete-time Hankel singular values of the sampled system, and the rates recovered by ERA at
  r = 2, 3, 4 for each level.
- **Content:** left: heatmap of the top-left 40 × 40 corner of the noise-free block (`seq` map) with the anti-diagonal
  structure visible; middle: singular values (log y, index 1..20) for the three noise levels (markers distinguish
  levels) with each level's floor $\|E\|_2$ as a dashed line, and the exact discrete-time Hankel singular values as
  open circles; right: a dot plot of recovered rates $\hat\nu$ (log x) at r = 2 for each level against ticks at the true
  slow rates, with a small table beneath (r = 2, 3, 4; recovered rates to 3 s.f.).
- **Generation:** drawn by `p_control.js` at fixed size from the data (no interaction).
- **Caption:** *Plotted:* left, block Hankel matrix $\mathbf H[i,j] = h_{i+j-1}$ of face B's sampled impulse response
  (40 × 40 corner); middle, singular values of the 128 × 128 block with and without added noise, the noise floor
  $\|E\|_2$ (dashed) and the sampled system's Hankel singular values (circles); right, decay rates recovered by ERA at
  r = 2 and the true slow rates. *Values:* Δ = 0.25, noise as a fraction of $\max_k|h_k|$, seed 0. Running example,
  face B. `synthetic`.
- **Fallback:** PNG `assets/fallback/control-fig-era-default.png` (captured like a widget with one tour; key `er`,
  single tour `default`).

## 6. Running example on this page

- Faces: B (default), OU companion. Parameters exactly as SPEC 3.2 and 3.4: $h_x = 2.5$, $h_y = 1.5$, $b = 0.6$,
  κ = 0 (and κ = 0.3 in the `kappa` tour), D = 0.5, force along $d = (1,1)/\sqrt2$, output $z = \mathbb E[x_1+x_2]$,
  mass mode removed, K = 60 slowest modes.
- Notation on this page: the input density $B = -\nabla\cdot(\pi d)$ is the input operator B, as in SPEC 3.4; $b = 0.6$
  is the potential's width parameter. The page says so once, in the first disclosure.
- Precomputed by `tools/build_example.py`:
  - `site/data/example/response.json` (shared file; SPEC 3.6): for κ ∈ {0, 0.3}: modal rates $\nu_k$ (k = 1..60,
    mass mode excluded), modal B, C, the grid-eigenpair index of each mode, Gramians (60 × 60, Float32 base64),
    `minimal` (indices of the visible modes, their count, the tolerance $|C_k| > 10^{-10}\max_j|C_j|$, and which
    of the others vanish by symmetry), Hankel singular values of the minimal realization (all of them, up to 20),
    balancing transformation (first 8 columns), reduced systems r = 1..8 (or up to the minimal order),
    $H_\infty$ errors for balanced and modal truncation r = 1..8, product-mode residue, $H_\infty$ norm with K = 60 and
    with all grid modes.
  - `site/data/control/p02.json`: `loadings` and `labels` (5.4); `era` (5.5); `hero.range` (colour range per tour);
    config and assertions.
  - **Assertions:** neglected modes change $\|G\|_{H_\infty}$ by < 1e-4 (SPEC 3.4); product-mode residue < 1e-8 at κ = 0
    and > 1e-8 at κ = 0.3; Lyapunov residuals < 1e-10 (relative); reduced systems stable for r = 1..8; for every
    r = 1..8 with $\sigma_r > \sigma_{r+1}$, $\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$ (distinct
    values; tolerance 1e-9 relative); slow rates within 1 % of grid.json's $\nu_2$, $\nu_3$; $\sigma_3/\sigma_2 < 0.3$
    (expected ≈ 0.18: two independent checks of the minimal realization at grid spacings 0.05 and 0.005 gave
    σ ≈ 0.7205, 0.1414, 0.0259, 0.00093; this is the "two slow states" claim); exactly 9 visible modes at κ = 0,
    with $|C_k| < 10^{-12}\max_j|C_j|$ for the other 51; minimal-realization Gramians positive definite; balanced state 1's largest loading is the pair mode and
    balanced state 2's the up/down mode (if either fails, the page uses the builder's labels and this spec is amended);
    ERA at r = 2 on noise-free data recovers $\nu_2$, $\nu_3$ within 1 %. **If an assertion fails, stop and amend this
    spec; do not retune parameters silently.**
- Live: hero playback (closed-form modal evolution), all OU computations, frequency and step responses, $H_\infty$ of
  the displayed reductions (checked against stored values).
- Expected values (for checking only; the page always displays builder or live values): OU warm-up σ ≈ 0.0279,
  0.000421; OU stationary covariance diag(0.025, 0.015); OU $\|G\|_{H_\infty}$ = G(0) ≈ 0.0566. Face B: two-mode
  estimate of the first balanced state ≈ 85 % pair / 15 % up/down by squared loading.
- Strain, stated in 3.1 (ensemble, not trajectory) and 3.4 (product mode invisible; "two slow states, not three").
  Also note in 3.4 that the site-wide "r = 2 keeps the pair, r = 4 keeps the well" counts the constant mode and the
  product mode; here the constant (mass) mode is removed and the product mode is invisible, so r = 2 already keeps
  both visible slow axes.
- Companion: the OU warm-up (sections 3.1, 3.3; explorer tour `ou`).

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E1 | 1 Hankel | `=` | Page 1's table of pasts by futures and this page's Hankel operator are one construction: both factor through a state, rank is the minimal state dimension, and shifted blocks give the dynamics (Ho-Kalman). |
| E2 | 1 Hankel | `≈` | Singular-value-automaton truncation is the automaton analogue of balanced truncation, with an ℓ² bound $\sum_{i>r}\sigma_i^2$; optimal Hankel-norm (AAK) approximation is constructive here and for one-letter automata only. |
| E4 | 3 Koopman | `=` | With noise in place of inputs, past-future CCA of a linear-Gaussian process gives a stochastically balanced realization; for Markov processes generally, the whitened Koopman SVD is CCA of past and future features. |
| E5 | 3 Koopman | `=` | For the reversible running example the response to a push is the time-derivative of an equilibrium correlation (fluctuation-dissipation), so this page's response Hankel and page 3's correlation operator share slow modes. |

Map card text: "Linear control · the Hankel operator from past inputs to future outputs, weighted by input and output
energy · knob: number of balanced states r · bound: $\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The Hankel operator $\Gamma$: past inputs ↦ future outputs, $\Gamma = \mathcal O\,\mathcal C$ through the present state; weights: input energy and output energy ($L^2$ on both sides), i.e. the Gramians $W_c$, $W_o$; $\sigma_i = \sqrt{\lambda_i(W_cW_o)}$. |
| Knob | Number of retained balanced states r. |
| Discarded at r | States that are both hard to excite and hard to see: on face B, at r = 2, motion inside the wells; at r = 1, also the up/down relaxation. |
| Bound | $\sigma_{r+1} \le \|G - G_r^{\rm BT}\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$ (distinct values; stable minimal system, $\sigma_r > \sigma_{r+1}$; Moore 1981 for balancing, Enns 1984 and Glover 1984 for the bound; `theorem`). The lower bound holds for every order-r model; optimal Hankel-norm approximation attains $\sigma_{r+1}$ (AAK; Glover 1984; `theorem`). |
| From data | Ho-Kalman / ERA from a finite block of impulse responses; Weyl ($|\hat\sigma_i - \sigma_i| \le \|E\|_2$) and Wedin for noisy blocks; non-asymptotic identification from one trajectory (Oymak & Ozay 2019) — `conditional`. |
| Running example | From the builder (`response.json`, `p02.json`): the minimal order (9 visible modes of 60 at κ = 0) and its tolerance; face B's σ₁..σ₅ of the minimal realization; $\|G - G_2\|_{H_\infty}$ against $\sigma_3$ and $2\sum_{j>2}\sigma_j$; product-mode residue at κ = 0 (< 1e-8) and κ = 0.3; ERA-recovered slow rates and noise floors. |
| Budget line | T (truncation). |

## 9. Things not to claim

Balanced truncation is optimal (it is not, in either norm; it is within the factor of its bound); constructive AAK for
multi-letter automata or language models; the balanced states are the generator's slow modes (they are input-output
channels, mixtures of modes); linear response distinguishes all four wells (it sees two slow states); face B describes
single trajectories; PCA of the state finds the input-output-important states; a finite or noisy Hankel block
certifies the system's order; the $2\Sigma$ bound without its hypotheses (stability, minimality, strict gap); the
$H_\infty$ value shown is exact (it is a grid maximum); Glover's $L_\infty$ tail bound for Hankel-norm approximants
unless its statement has been checked (3.4 disclosure).

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, $(A, B, C)$, G, $W_c$, $W_o$, $\nu_i$, $\delta_r$ (only in passing), Δ, τ (not
used), x, V, D, π, $w_1..w_4$, L/R pairs, H (page 1's table, mentioned).
Page-local: u (input), z (output; not the readout y), h(t) and $h_k$ (impulse response and Markov parameters; never
$h_x$, $h_y$, which are barrier heights: say so in a side note), Γ (Hankel operator), $\mathcal C$, $\mathcal O$
(controllability and observability maps; calligraphic, to keep C for the output matrix), $\mathbf H$ (block Hankel
matrix, bold, to keep H for page 1's table), $\mathbf H^{\uparrow}$ (shifted block), $A_d, B_d$ (sampled system), T
(state transformation; not the chain $T_\Delta$), Σ (balanced Gramian), $\Sigma_x$ (stationary state covariance),
$G_r$, $G_r^{\rm BT}$, $\|\cdot\|_{H_\infty}$, $\theta_B$, $\theta_C$ (widget angles), $c_k$ (mode overlaps, disclosure
only), E (noise Hankel matrix), η (measurement-noise level, page-local per SPEC appendix A; not the partition
residual η of pages 4, 5 and 10).

## 11. Sources

Cite as in SPEC appendix C; check status there unless given here.

- Ho, B. L. & Kalman, R. E. (1966). Effective construction of linear state-variable models from input/output
  functions. *Regelungstechnik* 14, 545-548. [A]
- Moore, B. C. (1981). Principal component analysis in linear systems: controllability, observability, and model
  reduction. *IEEE TAC* 26(1), 17-32. [M]
- Pernebo, L. & Silverman, L. M. (1982). Model reduction via balanced state space representations. *IEEE TAC* 27(2),
  382-387. [V] (stability of balanced truncation)
- Enns, D. F. (1984). Model reduction with balanced realizations: an error bound and a frequency weighted
  generalization. *Proc. 23rd IEEE CDC*, 127-132. [W: attribution of the 2Σ bound confirmed in secondary sources;
  page range V]
- Glover, K. (1984). All optimal Hankel-norm approximations of linear multivariable systems and their L∞-error bounds.
  *Int. J. Control* 39(6), 1115-1193. [A]
- Adamyan, V. M., Arov, D. Z. & Krein, M. G. (1971). [M]
- Rahn, B. (2001). A balanced truncation primer. arXiv:quant-ph/0112066. [P; W: bound with distinct values, minimal and
  stable system, strict gap; energy interpretations]
- Zhou, K., Doyle, J. C. & Glover, K. (1996). *Robust and Optimal Control*. Prentice Hall (chs. 3, 7, 8). [V]
  (textbook reference for C2.1, C2.5, C2.11-12)
- Juang, J.-N. & Pappa, R. S. (1985). An eigensystem realization algorithm for modal parameter identification and
  model reduction. *J. Guidance* 8(5), 620-627. [A]
- Oymak, S. & Ozay, N. (2019). Non-asymptotic identification of LTI systems from a single trajectory. *Proc. ACC
  2019*, 5655-5661. arXiv:1806.05722. [W: venue and pages confirmed; theorem statements to be checked against the
  arXiv text before quoting hypotheses]
- Akaike, H. (1975). Markovian representation of stochastic processes by canonical variables. *SIAM J. Control* 13(1),
  162-173. [A]
- Desai, U. B. & Pal, D. (1984). A transformation approach to stochastic model reduction. *IEEE TAC* 29(12),
  1097-1100. [W]
- Kubo, R. (1966). The fluctuation-dissipation theorem. *Rep. Prog. Phys.* 29, 255-284. [V]
- Risken, H. (1989). *The Fokker-Planck Equation*, 2nd ed. Springer. [V]
- Fliess 1974 [V]; Carlyle & Paz 1971 [V]; Balle, Carreras, Luque & Quattoni 2014 [P] (for E1).
- Balle, Panangaden & Precup 2019 [P]; Balle et al. 2021 [P]; Lacroce et al. 2023 [P] (for E2).
- Weyl (1912) and Wedin (1972), as on page 1. [V]
- Code provenance: Gramians, balancing and truncation in `lib/lti.js` (square-root algorithm); no external code
  copied.

## 12. Implementation notes

- Files: `site/content/control.html`, `site/js/p_control.js`, helpers `site/js/p_control_hero.js`,
  `p_control_gramians.js`, `p_control_explorer.js`, `p_control_era.js`; data `site/data/control/p02.json`,
  `site/data/control/widgets.json`. Reads shared `site/data/example/response.json` and `grid.json`.
- Shared modules used: `lib/lti.js`, `lib/linalg.js`, `lib/example.js` (loaders), `lib/bowtie.js`, `charts.js`,
  `ui.js`, `palette.js`.
- `lib/lti.js` must expose: `lyap(A, Q)` (continuous Lyapunov, Bartels-Stewart or modal for diagonalizable A),
  `gramians({A,B,C})` → `{Wc, Wo}`, `hankelSV({A,B,C})`, `balance({A,B,C})` → `{T, Tinv, sigma, Ab, Bb, Cb}`,
  `truncate(sys, r)`, `modalTruncate(sys, r)` (slowest r), `freqResp(sys, omegas)` (complex), `hinf(sys, grid)`
  (grid maximum with local refinement), `stepResp(sys, ts)`, `impulseResp(sys, ts)`, `c2dZOH(sys, dt)`,
  `era(h, rows, cols, r)` → `{A, B, C, sigma}`.
- Widget keys and URL state: hero `hr` (`hr_shape`, `hr_speed`, `hr_tour`); Gramians `gr` (`gr_tb`, `gr_tc`,
  `gr_ratio`, `gr_s`, `gr_D`, `gr_tour`); explorer `ex` (`ex_model`, `ex_r`, `ex_meth`, `ex_load`, `ex_tour`); ERA
  figure `er` (single tour `default`); bowtie has no key.
- Tests: parity of `lyap`, `balance`, `truncate`, `hinf` against the builder on face B (1e-8 relative on Hankel
  singular values, 1e-6 on $H_\infty$) and against the OU closed form (1e-12); a node test that each explorer tour's
  tiles match `response.json`; a test that the Gramian widget's tiles satisfy $W_c$, $W_o$ Lyapunov residual < 1e-12.

## 13. Page-specific definition-of-done additions

- [ ] The explorer's bound check is surfaced: if for any r the grid $H_\infty$ error exceeds $2\sum_{j>r}\sigma_j$ or falls
      below $\sigma_{r+1}$ (beyond tolerance), the page shows an error banner, never a silent plot.
- [ ] Every statement of what σ₁ and σ₂ "are" uses the builder's loadings and the word "mostly", never "is the pair
      mode".
- [ ] The phrase "two slow states, not three" and the ensemble-not-trajectory caveat both appear on the main path.
- [ ] The word "optimal" appears only with its norm and competitor class ("optimal among order-r systems in Hankel
      norm").
- [ ] In the hero fallback (`pulse-early`) both the up/down and left/right contrasts are visible (check the
      screenshot); if not, the builder's colour range is adjusted, not the tour time.
- [ ] The Gramian widget's `pca` tour shows a top-direction angle tile above 30°; if not, the tour angles are adjusted
      and the change logged.

## Change log

- v1 (2026-11-17): first full spec.
- v1.1 (2026-11-17): reconciled with SPEC v1.1, which now records this page's exception to "r = 2 keeps the pair"
  (3.2), the input operator B (3.4), face B stored in full at κ = 0.3 (3.6), the 2Σ attribution and new bibliography
  entries (4.2, appendix C). Notes that requested those amendments updated; no change to the page's design.
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) The 60-mode response model is not minimal (at κ = 0 only 9
  modes are visible; checked at grid spacings 0.05 and 0.005), so its Gramians are singular and balancing cannot be
  applied to it: 3.2, its first disclosure, 3.3 and the balancing disclosure now extract the minimal realization
  first (Kalman 1963), the builder stores `minimal` and asserts the count, and C2.9a records it; expected Hankel
  singular values updated (σ₃/σ₂ ≈ 0.18, not 0.1). (2) 3.6's "$B \propto C^\top$, $W_c \propto W_o$ in modal
  coordinates" corrected: $B_k = \nu_kC_k/(D\sqrt2)$ has a k-dependent factor; a mode-wise rescaling gives a
  state-space-symmetric realization with equal Gramians (C2.9b). (3) The κ = 0.3 tour uses SPEC 3.2's new knob (the
  old one kept the mirror symmetry; the product-mode residue stays small but nonzero, overlap ≈ 0.031). Reviewer
  findings: math-1-6 1 (knob), 3.
