# Page spec 04: Spectral clustering as isoperimetry

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 4 |
| id (hash, file stem) | `cuts` |
| tab label | Spectral clustering |
| kicker | Page 4 · spectral graph theory |
| title | Spectral clustering: cutting where little crosses |
| lede (one-sentence claim, ≤ 45 words) | A good coarse-graining groups states so that little crosses between groups for their size. Finding the best such cut is hard, but it relaxes to an eigenproblem whose eigenvalues bracket the best cut from both sides; with dynamics, the same recipe finds coherent sets. |
| depends on | 3 for the dynamic half (section 3.5); the static half needs nothing |
| edges (SPEC 2.2) | E6, E7, E8, E9, E10, E12, E18, E23 |
| faces of the running example | A (equilibrium samples as a graph; generator eigenfunctions from `grid.json` as reference), C (the toy residual network) |
| main-path words | 2,200-2,600 (five sections, each ≤ 450) |
| spec status | v1.3, 2026-11-17 (round-2 review fixes; change log) |

## 1. Reader outcome

After this page the reader can:

1. Build a similarity graph on data points, compute its normalized Laplacian, run spectral clustering (eigenvectors, then rounding) and say exactly which set function it is approximately minimizing (conductance or normalized cut).
2. State the general recipe of the site in four steps (choose an energy and a size measure; define the best coarse-graining as the cut with the least energy for its size; relax indicators to functions, which gives an eigenproblem; bound the relaxation both ways) and say which steps are theorems and which are motivation.
3. Apply Cheeger's inequality (two-way, with the sweep cut as witness) and the higher-order Cheeger inequality to a computed spectrum, and say which side of each bound has an explicit constant.
4. Explain why the spectral gap after r, not r itself, decides which resolutions are certified, using Davis-Kahan for perturbations, the partition-residual bound for rounding, and the diffusion time or bandwidth as the knob that moves the gap.
5. Tell static coherence (metastability of a reversible process, recovered from equilibrium samples with α = 1/2 normalization) from dynamic coherence (sets that stay together under transport), and state what the dynamic Laplacian is, where it comes from (small-noise limit of a forward-backward transfer operator) and what its Cheeger inequality says.
6. Say what normalization ("which Laplacian") does: it chooses the measure of size, and in the sample limit it chooses which differential operator the graph approximates.

What they see: a cloud of equilibrium samples whose cheapest cut runs through the empty band between the two pairs of wells, then through the narrower bands inside each pair; a sweep along the second eigenvector whose conductance dips into the Cheeger bracket; a k = 3 cut that is arbitrary because there is no gap after 3; two gap curves that cross as the diffusion time grows, so the pair block and the well block take turns being the certified one; and a toy network on which three walks ask three questions of the same tracked inputs (which start close, which end close, which stay close across all layers), each labelling drawn at every layer beside its boundary cost layer by layer.

## 2. Skim path

1. Lede (header).
2. Hero figure `cuts-fig-hero`: "Cut where little crosses". Fig-sub: *Equilibrium samples of the four-well particle, joined to their nearest neighbours; the spectral cut runs through the sparse band between the pairs, and at four sets through the bands inside each pair.*
3. Section headings (verbatim, these are the claims):
   - "A good coarse-graining has a small boundary for its size"
   - "Every choice of energy defines its own best coarse-grainings"
   - "Relaxing the cut gives eigenvectors, with bounds both ways"
   - "The gap after r decides which resolutions are certified"
   - "With dynamics, coherent sets solve a moving cut problem"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `cuts-fig-recipe`, `cuts-fig-explorer`, `cuts-fig-scale`, `cuts-fig-dynamic`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: a coarse-graining is good when little crosses between its sets relative to their size (isoperimetry); choosing what "crossing" and "size" mean is choosing an energy, and the best coarse-graining for that energy is a graph cut; the cut problem is hard, but its relaxation is an eigenproblem whose k-th eigenvalue brackets the best k-way cut (Cheeger); eigenvectors are only as stable as the gap after r, and the scale knob (bandwidth, diffusion time) moves the gaps, so different resolutions are certified at different scales; for a reversible process, static clustering of equilibrium samples recovers the slow dynamics (with the right normalization); with transport, the same recipe applied to a time-averaged operator finds coherent sets, and the small-noise limit is the dynamic Laplacian.

## 3. Section outline

Section ids are `cuts-<slug>`; figure ids are `cuts-fig-<slug>` (SPEC 6.5). Word counts are main-path prose only. An "Arriving here first?" aside (≤ 80 words) sits at the top of section 3.5 (see there).

### 3.1 `cuts-isoperimetry` "A good coarse-graining has a small boundary for its size" (≈ 450 words)

Placement: the hero `cuts-fig-hero` sits between the lede and this heading.

- Open with the interpretability question in one sentence: given many data points (activations, states), which groupings deserve to be called objects? One answer, older than machine learning: a group is an object when little connects it to the rest compared with how much it contains. That is the isoperimetric idea (small boundary for the enclosed volume), here on a graph.
- Running example (two sentences, link to the map's description): equilibrium samples of the particle in the nested four-well potential, face A; N = 1000 points from `samples.json` (seed 0); each joined to its 15 nearest neighbours. Points crowd into the four wells and are scarce on the barriers, most scarce on the high barrier between the two pairs.
- Definitions, each glossed: edge weights $W_{xy} \ge 0$; degree $d_x = \sum_y W_{xy}$; volume $\mathrm{vol}(A) = \sum_{x\in A} d_x$; cut weight $\mathrm{cut}(A) = \sum_{x\in A, y\notin A} W_{xy}$. Displayed equation 1 (conductance):
  $$\phi(A) = \frac{\mathrm{cut}(A)}{\mathrm{vol}(A)},\qquad h(G) = \min_{\mathrm{vol}(A)\le \mathrm{vol}(G)/2}\phi(A).$$
  $h(G)$ is the graph's Cheeger constant (page-local symbol, SPEC appendix A). Link "conductance" to the glossary (it also means an edge's electrical conductance on page 8).
- The probabilistic reading, which is the one the rest of the site uses: if the random walk moves from x to y with probability $P_{xy} = W_{xy}/d_x$, its stationary distribution is proportional to degree, and $\phi(A)$ is exactly the probability that a walker started in A (in proportion to stationarity) leaves A in one step. Low conductance = metastable: a walker stays a long time. Cite Levin & Peres 2017 (bottleneck ratio).
- The hero shows the cheapest two-way cut (near $x_1 \approx 0$, between the pairs) and, at four sets, the within-pair cuts (near $x_2 \approx 0$). Quote the builder's locations and conductances (`p04.json`, `hero`), never the expectation. Say why the order is pair first: the between-pair barrier is higher ($h_x = 2.5$ against $h_y = 1.5$), so fewer samples sit on it and fewer edges cross.
- Scale-sensitivity, in two sentences: "small boundary" depends on how far an edge reaches (neighbour count, bandwidth) and, with dynamics, on how long one waits (lag). The answer to "what are the objects?" is therefore an answer at a scale; section 3.4 makes this precise.
- One sentence wrapped in the section 8 hook (`<span class="status" data-status="schematic">`): "Read this way, isoperimetry is a general, scale-sensitive way to define consistent objects: whatever the incoherence objective, the objects at a given scale are the sets that keep the most of it inside for their size." (Claim C4.4, support: motivation.)

Key callout: "A set is a good object when little leaves it compared with what it holds. On a graph this ratio is the conductance, and for a random walk it is the chance of leaving in one step."

Disclosures:
- "In other fields: isoperimetry, bottlenecks, metastability" (≤ 300 words): the classical isoperimetric problem (least perimeter for given area); Cheeger's original constant on manifolds (Cheeger 1970, named via Chung 1997); bottleneck ratio of a Markov chain (Levin & Peres 2017); metastable sets in molecular dynamics (link page 6, edge E12); conductance as edge conductance in resistor networks (page 8, glossary).

### 3.2 `cuts-recipe` "Every choice of energy defines its own best coarse-grainings" (≈ 450 words)

Placement: `cuts-fig-recipe` (static) after the third bullet.

This section carries the site's central general recipe. It must keep the proved steps and the schematic step visibly apart (section 4 marks which is which; the text says which in words, never with colour or chips).

- Generalize the hero: what made a cut "cheap" was a choice of two things. (i) An **energy**, which says how much it costs to separate two states: a nonnegative symmetric coupling $W$ and its quadratic energy (displayed equation 2)
  $$\mathcal E(f) = \tfrac12\sum_{x,y} W_{xy}\,(f_x - f_y)^2,$$
  so that $\mathcal E(\mathbf 1_A) = \mathrm{cut}(A)$. (ii) A **size measure** $m$ that says how big a set is. The incoherence of a set is $\mathcal E(\mathbf 1_A)/m(A)$.
- The recipe (four steps, as numbered in the figure):
  1. Choose the energy and the measure. When $m$ is the degree, the pair is exactly a reversible random walk ($P = \mathbf D^{-1}W$, stationary measure ∝ degree) and its Dirichlet form; conversely every reversible walk with stationary measure π gives $W_{xy} = \pi_xP_{xy}$. So "choosing an energy" and "choosing a reversible walk" are the same choice.
  2. Define the best coarse-graining into k sets as the one whose worst set (or whose sets in total) loses the least for its size: $\rho(k) = \min_{A_1..A_k}\max_j \phi(A_j)$ (k disjoint nonempty sets; page-local symbol $\rho_G(k)$) or the normalized cut $\mathrm{Ncut} = \sum_j \phi(A_j)$ over partitions. This is a graph-cut problem **by definition**, not by approximation: for any energy of this form, "optimal coarse-graining" and "minimum normalized cut" are the same object. Exact minimization is NP-hard in general (Shi & Malik 2000 note this for Ncut).
  3. Relax indicators to real functions (section 3.3).
  4. Bound what the relaxation loses, both ways (section 3.3), and then round and certify (section 3.4).
- Examples of energies, one line each, each pointing to where the page or site uses it: a similarity graph of data points (this section; static clusters); the stationary flux $\pi_xP_{xy}$ of a reversible Markov chain (metastable sets; page 6 for when such sets behave as states, E12); the forward-backward composite of a transfer operator (coherent sets, section 3.5); the time average of energies along a flow (the dynamic Laplacian, section 3.5; NCS on page 10, E18); and an information-theoretic energy in which pasts are separated by how differently they predict the future (the information bottleneck, page 6). The last one is not a quadratic form; say in one sentence, inside the section 8 hook, that treating it as an instance of the same recipe is a motivating analogy (page 6, edge E13), and, outside the hook, the narrower exact fact: for Gaussian processes the information bottleneck's optimal projections lie along CCA directions, with β-dependent scales and noise, so it shares the spectral directions, not the solution.
- **Which Laplacian is a choice of scaling.** The unnormalized Laplacian $L = \mathbf D - W$ measures size by counting points (ratio cut); the random-walk Laplacian $L_{\rm rw} = I - \mathbf D^{-1}W$ and the symmetric normalized $L_{\rm sym} = I - \mathbf D^{-1/2}W\mathbf D^{-1/2}$ measure it by degree (conductance, Ncut). $L_{\rm rw}$ and $L_{\rm sym}$ have the same eigenvalues; their eigenvectors differ by the factor $\mathbf D^{1/2}$: the random-walk eigenvectors ("random-walk harmonics") are orthonormal in the degree-weighted inner product. Sinkhorn balancing (NCS, page 10) rescales the kernel so every degree is one, so all three coincide and size is counted uniformly. One more sentence: in the sample limit the normalization also decides which operator the graph approximates (disclosure "The α family").

Key callout: "Choose what it costs to separate two states and how to measure a set's size; the best coarse-graining is then, by definition, a minimum normalized cut. The hard part is computing it, not defining it."

Disclosures:
- "The α family: geometry, dynamics, or exaggerated clusters" (≤ 450 words). For samples from a density $p \propto e^{-U}$ and a Gaussian kernel of width ε, divide the kernel by $p_\varepsilon(x)^\alpha p_\varepsilon(y)^\alpha$ before forming the random walk (Coifman & Lafon 2006). As ε → 0 and N → ∞, the walk's generator acts on smooth functions as $\Delta\psi - 2(1-\alpha)\nabla U\cdot\nabla\psi$ (Nadler, Lafon, Coifman & Kevrekidis 2006, eq. (27)). So α = 0, the ordinary random-walk normalization used by most spectral clustering, gives the backward operator of a diffusion in potential 2U: the same wells at half the temperature, so clusters look more separated than the dynamics make them; α = 1/2 gives exactly the generator of the Langevin dynamics $dX = -\nabla U\,dt + \sqrt2\,dW$; α = 1 gives the Laplace-Beltrami operator, geometry with density removed. For the running example, $\pi \propto e^{-V/D}$ so $U = V/D$, and the generator $\mathcal L = D(\Delta - \nabla U\cdot\nabla)$ has the same eigenfunctions as the α = 1/2 limit with rates scaled by D. This is edge E6. Hypotheses to state: equilibrium samples, fixed-width Gaussian kernel, ε → 0 with N → ∞ at a suitable rate, smooth density; the result is a limit statement, not a finite-N bound. kNN graphs have a different (density-adaptive) limit; the page does not claim one.
- "Harmonic functions, voltages and effective resistance" (≤ 300 words). A function is harmonic for the walk at x when $f_x$ is the average of its neighbours, $(L_{\rm rw}f)_x = 0$. Clamp f on a set of boundary points and solve $Lf = 0$ elsewhere: this is the graph Dirichlet problem, the voltages of a resistor network with conductances $W_{xy}$ and clamped inputs, and harmonic label propagation (Zhu, Ghahramani & Lafferty 2003). Effective resistance between x and y, $R_{xy} = (e_x - e_y)^\top L^{+}(e_x - e_y)$, is the voltage drop for a unit current, the same Laplacian's pseudo-inverse; it reappears on page 5 as the sampling weight of a sparsifier and on page 8 as the resistor network of the Hebbian model. Edge E10.

### 3.3 `cuts-relax` "Relaxing the cut gives eigenvectors, with bounds both ways" (≈ 450 words)

Centrepiece: `cuts-fig-explorer` after the fourth bullet.

- Replace the indicator $\mathbf 1_A$ by any real function f. Its incoherence becomes the Rayleigh quotient $\mathcal E(f)/\sum_x d_xf_x^2$, minimized over f orthogonal (in the degree inner product) to the constant. The minimizers are eigenvectors of the generalized problem (displayed equation 3)
  $$Lf = \mu\,\mathbf Df,\qquad 0 = \mu_1 \le \mu_2 \le \dots,$$
  that is, eigenvectors of $L_{\rm rw}$, with $\mu_i$ the eigenvalues of $L_{\rm sym}$ (ascending, SPEC appendix A). Spectral clustering = compute the bottom k eigenvectors, then round them to k sets (here: k-means on the row-normalized embedding, Ng, Jordan & Weiss 2002).
- Lower bound, free from the relaxation: for every partition into k sets, $\mathrm{Ncut} \ge \mu_1 + \dots + \mu_k$ (the normalized indicators are one admissible choice in a minimization whose value is the sum of the k smallest eigenvalues; Ky Fan's principle; Shi & Malik 2000; von Luxburg 2007).
- Upper bound for two sets, which is the substance (displayed equation 4, Cheeger's inequality for graphs):
  $$\frac{\mu_2}{2} \le h(G) \le \sqrt{2\mu_2}.$$
  The right-hand side is constructive: sort the points by the second eigenvector and take the best prefix (the **sweep cut**); its conductance is at most $\sqrt{2\mu_2}$. Cite Chung 1997 and, for reversible chains, Levin & Peres 2017, Theorem 13.10. The square root is the price of relaxing; it is tight on some graphs (paths), and loose on well-clustered ones (Kwok et al. 2013: the sweep's conductance is at most $O(k)\,\mu_2/\sqrt{\mu_k}$ for every k ≥ 2, so a large higher eigenvalue makes the sweep nearly optimal).
- k sets (displayed equation 5, Lee, Oveis Gharan & Trevisan 2014, Theorems 1.1-1.2):
  $$\frac{\mu_k}{2} \le \rho_G(k) \le O(k^2)\sqrt{\mu_k},\qquad \rho_G(k) \le O\big(\sqrt{\mu_{2k}\log k}\big).$$
  Say plainly: $\rho_G(k)$ is a min over k-tuples of the **worst** set's conductance, so the lower bound says that every k disjoint sets have $\max_j\phi(A_j) \ge \mu_k/2$; it says nothing about each set (one endpoint of the three-vertex path and its complement have conductances 1 and 1/3, while $\mu_2/2 = 1/2$). The lower bound has an explicit constant; the upper bounds have universal constants the theorems do not make explicit, so a page can certify "no k-way coarse-graining is better than $\mu_k/2$" numerically but can only show the achieved value from above. Note the second bound uses $\mu_{2k}$, not $\mu_k$ (do not swap). The k sets are disjoint and need not cover every point.
- Running example in the explorer: tour `pair-cut` (k = 2: sweep conductance inside the bracket, builder values); tour `wells` (k = 4: the four achieved conductances, the worst of them against the lower bound $\mu_4/2$, and Ncut against $\mu_1 + \dots + \mu_4$); tour `no-gap` (k = 3: $\mu_3 \approx \mu_4$, so the third set is whichever within-pair split the rounding happens to pick; rerun with another k-means seed and it changes). The last point anticipates section 3.4.
- For Sinkhorn-balanced walks with holding probability (NCS), cite the CoherentModes theorem register, S.3: the two-way inequality holds as stated (with the index shift: the register's $\lambda_1$ is this site's $\lambda_2$; say so once on the page), and the higher-order upper bound needs an explicit loop-removal factor $d_{\max}/\sqrt{d_{\min}}$.

Key callout: "The k-th eigenvalue brackets the best k-way cut: in every k-way coarse-graining the worst set leaks at least $\mu_k/2$, and rounding the eigenvectors achieves a known function of $\mu_k$. The lower side is numeric; the upper side, beyond two sets, carries unspecified constants."

Disclosures:
- "Why this holds: Cheeger's inequality in a page" (≤ 450 words). The easy side (indicator of the best set, centred, as a test function in the Rayleigh quotient). The hard side (sweep): co-area identity $\sum_{x\sim y}W_{xy}|g_x - g_y| = \int \mathrm{cut}(\{g > t\})\,dt$, applied to $g = f^2$ for the positive part of the second eigenvector, then Cauchy-Schwarz. State that the ℓ¹ version of the relaxation is exact (the best ℓ¹ Rayleigh ratio equals h(G); graph Federer-Fleming, Chung 1997; Froyland 2015, Theorem 2.1 for manifolds), but it is not an eigenproblem; the ℓ² relaxation is an eigenproblem and pays the square root. This is the "choice of norm" in step 3 of the recipe: ℓ¹ is exact and hard, ℓ² is tractable and bounded.
- "Hypotheses: which graph, which conductance" (≤ 300 words): connected, undirected, nonnegative weights; conductance with degree volume; for sets that need not cover (ρ) versus partitions (Ncut); for self-loops/holding probabilities the S.3 conversion.

### 3.4 `cuts-gaps` "The gap after r decides which resolutions are certified" (≈ 450 words)

Placement: `cuts-fig-scale` (static) after the third bullet.

- Four approximation results turn "eigenvectors" into "sets with error bars". Introduce each in two or three sentences, with its hypothesis.
  1. **Good partitions lie near the eigenspace** (displayed equation 6). Let V hold the bottom k eigenvectors of $L_{\rm sym}$ and $g_j = \mathbf D^{1/2}\mathbf 1_{A_j}/\sqrt{\mathrm{vol}(A_j)}$ the normalized indicators of a partition. Then
     $$\eta^2 := \sum_j\big\|(I - VV^\top)g_j\big\|^2 \le \frac{\sum_j\phi(A_j)}{\mu_{k+1}}.$$
     A partition with small conductances, in a graph whose next eigenvalue is large, is nearly in the span of the eigenvectors (Peng, Sun & Zanetti 2017, Theorem 1.1, state it per set as $\|g_j - \hat f_j\|^2 \le \phi$-over-gap; the summed form is derived in the disclosure). The ratio $\mu_{k+1}/\rho_G(k)$ plays the role of a gap. This is what makes rounding certifiable: page 5's SEBA certificate (CoherentModes S.8) takes exactly this η as input (edge E9).
  2. **Perturbation** (displayed equation 7, Davis & Kahan 1970; CoherentModes register A.21): if the operator changes by e in operator norm and the block of r eigenvalues is separated from the rest by $\delta_r > 2e$, the block's subspace moves by at most
     $$\|\sin\Theta\|_{\rm op} \le \frac{e}{\delta_r - e}.$$
     The constant is 1; individual eigenvectors inside the block may rotate freely (A.28). Perturbations can be noise in the data, a different bandwidth, a sparsifier (page 5, edge E8).
  3. **Sampling**: a graph on N samples estimates an operator on the population. Normalized spectral clustering is consistent as N grows, under conditions that the unnormalized version can fail (von Luxburg, Belkin & Bousquet 2008); Laplacian eigenmaps converge to Laplace-Beltrami eigenfunctions with bandwidth shrinking at a suitable rate (Belkin & Niyogi 2007); for fixed-bandwidth Sinkhorn kernels the register gives explicit finite-N rates (A.43-A.44) whose constants are often vacuous at realistic N (page 10 shows them). All conditional.
  4. **Scale**: on a walk P with eigenvalues $\lambda_i = 1 - \mu_i$ (lazy, so in [0, 1]), running it for time t raises them to $\lambda_i^t$. The gap after r, $\lambda_r^t - \lambda_{r+1}^t$, rises then falls in t, with a single maximum (register S.10, which also shows the threshold-retained count $\#\{i: \lambda_i^t > \vartheta\}$ is the minimal rank with spectral error ≤ ϑ). Gaps are **not monotone in r**: at short times the four-well block is the well separated one, at long times the pair block (SPEC 3.2 says the same for the particle's own lag: τ = 0.25 certifies wells, τ = 4 only pairs).
- `cuts-fig-scale` shows (a) the two gap curves crossing on the running example's graph, with the crossing time from the builder; (b) Davis-Kahan: actual subspace angle against the bound for the pair block and the well block under positional jitter.
- Conclude: truncation error falls as r grows, but subspace certificates (Davis-Kahan) divide by the gap at the chosen r; eigenvalue and operator-error bounds do not, and the gap decides whether those errors are small enough to distinguish the block; rounding to sets by SEBA additionally needs a small partition residual and a positive threshold margin (page 5), while the Cheeger sweep bound involves eigenvalues only. The scale knob decides which r has a gap. This is page 4's line in the page-10 budget (R from rounding, P from perturbation).

Key callout: "Eigenvectors are only as trustworthy as the gap after r. Change the scale and a different resolution gets the gap: here the wells at short times, the pairs at long ones."

Disclosures:
- "The maths: why good partitions are near the eigenspace" (≤ 300 words): expand $g_j = \sum_i c_{ij}f_i$ in the orthonormal eigenvectors $f_i$ of $L_{\rm sym}$; $g_j^\top L_{\rm sym}g_j = \phi(A_j) = \sum_i\mu_ic_{ij}^2 \ge \mu_{k+1}\sum_{i>k}c_{ij}^2$; sum over j. No gap condition is needed for the inequality; a large $\mu_{k+1}$ relative to the conductances is what makes it small. Peng, Sun & Zanetti also prove the converse direction (each eigenvector near a combination of indicators) under $\mu_{k+1}/\rho_G(k) = \Omega(k^2)$.
- "Hypotheses: Davis-Kahan as used here" (≤ 300 words): symmetric matrices on the same space; contiguous isolated block; e < δ/2; compare eigenspaces only on the same sites (never raw eigenvectors of graphs on different samples; SPEC 4.3).
- "In other fields: spectral gap" (≤ 200 words): mixing-time gap $1 - \lambda_2$ (Markov chains) versus the gap after r (this page) versus SNS's ratio-based "gap" (page 6); glossary link.

### 3.5 `cuts-dynamic` "With dynamics, coherent sets solve a moving cut problem" (≈ 450 words)

Aside at the top, "Arriving here first?" (≤ 80 words): "A transfer operator pushes a distribution of points forward by the dynamics, possibly with noise; its adjoint (the Koopman operator) pulls functions back. Page 3 introduces both. Here we need only that composing 'push forward, then pull back' gives a symmetric operator whose top singular vectors mark sets that land mostly on one image set." Link page 3.

Placement: `cuts-fig-dynamic` after the fourth bullet.

- Static first. The particle is reversible, so its slow sets are the metastable ones, and those are a static isoperimetric problem on its equilibrium distribution: with the α = 1/2 normalization, the graph on equilibrium samples recovers the generator's eigenfunctions in the large-sample, small-bandwidth limit (edge E6; disclosure in 3.2). The explorer's tour `dmap` shows the agreement on the running example (correlations with the reference eigenfunctions from `grid.json`, builder values).
- Dynamic. When the flow carries sets somewhere (non-autonomous, finite-time, or simply not reversible), a coherent set is one that stays compact while it moves: small boundary both at the start and after transport. Froyland 2013: with noise, the leading singular vectors of the transfer operator relax the problem "find a set A and image set B such that most of A's mass lands in B and most of A's complement in B's complement" (Theorem 2; in the register's finite form, A.5 with the bipartite rounding S.4).
- Small noise. Let the noisy transfer operator be $\mathcal L_\epsilon$ (diffuse, move, diffuse). As ε → 0 (displayed equation 8; Froyland 2015, Theorem 5.1),
  $$\frac{\mathcal L_\epsilon^*\mathcal L_\epsilon - I}{\epsilon^2} \to 2c\,\Delta^D,\qquad \Delta^D = \tfrac12\big(\Delta + \mathcal P^*\Delta\mathcal P\big),$$
  (c the noise covariance coefficient; the source writes the limit as $c(\Delta + \mathcal P^*\Delta\mathcal P)$, C4.25; the factor 2 matters for rates, not for eigenfunctions),
  the **dynamic Laplacian**: the average of the Laplacian now and the Laplacian after transport, pulled back. Its eigenfunctions obey a dynamic Cheeger inequality $h^D \le 2\sqrt{-\lambda_2^D}$ (Theorem 3.2; Froyland writes Laplacians nonpositive: note the sign convention, SPEC appendix A), where $h^D$ averages the boundary length of a set before and after the flow over its volume. For several steps, average the pulled-back Laplacians over all steps (Corollary 3.5). Hypotheses: flat compact manifold, smooth volume-preserving maps; Froyland & Kwok 2017 extend to non-volume-preserving dynamics and weighted manifolds (face C's gradient flow is contractive, so it is in their setting, not the 2015 one).
- From data. Banisch & Koltai 2017 build a graph walk on each time slice of trajectory data and average the walks over time; as the number of trajectories grows, this averaged walk converges to the time-averaged forward-backward transfer operator (their Theorem 3, pointwise at fixed bandwidth, up to $O(\epsilon^2)$), and $(Q_\epsilon - I)/\epsilon$ approximates a density-weighted dynamic Laplacian (their Remark 4). This is the precedent for doing the same with the flow of data points through a network's layers: NCS averages Sinkhorn-balanced walks over layers, $\bar M$, and $I - \bar M$ is a finite-graph analogue of the dynamic Laplacian (edge E18; page 10). Two exact facts hold for $\bar M$ itself: the conductance of a set under $\bar M$ is the average of its conductances under the layer walks (cut weight is linear in the matrix), and Cheeger's inequality applies to $\bar M$ as to any symmetric doubly stochastic walk (S.3). What has no theorem is the limit: wrap in the section 8 hook "that NCS's Sinkhorn-normalized layer average converges to a dynamic Laplacian of the network's layer maps" (claim C4.29, motivation).
- Face C in `cuts-fig-dynamic`: on the toy residual network (each layer a step of the particle's drift; SPEC 3.5), three walks on the same tracked inputs answer three questions. The input layer's walk asks which inputs **start** close (a uniform cloud; quote whether it has a gap after 4); the output layer's walk asks which inputs **end** close (four clumps, which are the basins because the flow ends in wells); the layer-averaged walk asks which inputs **stay** close, since a set's conductance under $\bar M$ is the average of its per-layer conductances (C4.28). Every labelling can be drawn at every layer (the inputs are tracked), so the page does not say that only the average shows where points end up; it shows each labelling's boundary cost layer by layer and its agreement with the basins, and quotes the builder's numbers whichever way they come out (`p04.json` `facec`). The input box (SPEC 3.5) is deliberately not symmetric about the basin boundaries, so a layer-0 cut that followed the quadrants could not be a coincidence of the box; say so in one sentence.
- Close the section with two forward pointers: a metastable partition is approximately a Markov chain on its own, with a bound (page 6, edge E12); and the Hebbian model of page 8 performs a related thresholded spectral computation, without a theorem tying it to a chosen cut (edge E23, wrapped in the section 8 hook).

Key callout: "For transport, the energy is the cost of a set's boundary averaged over the flow. In the small-noise limit that is the dynamic Laplacian, with its own Cheeger inequality; averaging graph walks over layers is its finite, data-point version."

Disclosures:
- "The maths: coherent pairs and the forward-backward operator" (≤ 400 words): Froyland 2013's balanced coherence score and its relaxation to $\sigma_2$ of the normalized transfer operator; the register's exact finite identity (A.5: the balanced two-set retention score equals $\langle Tf_A, f_B\rangle \le \sigma$ for centred normalized indicators) and the bipartite Cheeger rounding (S.4: the witness exists for $\sigma > 1/2$, the trimmed transport bound is positive only for $\sigma > 17/18$; register indexing shifted by one). State that these are finite-site theorems for doubly stochastic products, not the manifold theorems.
- "Hypotheses: what the dynamic Cheeger theorems assume" (≤ 300 words): Theorem 3.2 (flat compact $C^\infty$ manifold, $C^\infty$ volume-preserving diffeomorphism, Neumann-type boundary condition (17)); Corollary 3.5 (sequence of such maps, averaged operator); Theorem 5.1 ($C^3$ map and function, isotropic compactly supported noise with covariance cI); Froyland & Kwok 2017 for weights and non-volume-preserving maps; Banisch & Koltai Theorem 3 (deterministic trajectories, fixed ε, pointwise, m → ∞). None is a theorem about a Sinkhorn-normalized kNN graph on network activations.
- "In other fields: coherent set" (≤ 200 words): Froyland's finite-time coherent set; almost-invariant / metastable set (autonomous case); NCS coherent set (a SEBA set of a data-point walk); glossary link.

### 3.6 `cuts-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.7 `cuts-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.8 `cuts-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C4.1 | Conductance $\phi(A) = \mathrm{cut}(A)/\mathrm{vol}(A)$; for the walk $P = \mathbf D^{-1}W$ it is the probability of leaving A in one step from stationarity within A. | construction + standard | Levin & Peres 2017 (bottleneck ratio) | undirected, nonnegative weights; stationary measure ∝ degree | 3.1 |
| C4.2 | On face A samples the minimum-conductance two-way cut lies near $x_1 \approx 0$ and the four-way partition adds cuts near $x_2 \approx 0$. | widget + builder values | hero tours `pairs`, `wells`; `p04.json` `hero` | builder locations, not the expectation | 3.1 |
| C4.3 | The isoperimetric ratio, and hence the best coarse-graining, depends on the graph's scale and, with dynamics, on the lag. | construction + widget | explorer scale control; `cuts-fig-scale` | — | 3.1 |
| C4.4 | Isoperimetry is a general, scale-sensitive way to define consistent objects under an incoherence objective. | motivation (section 8 hook) | — | — | 3.1 |
| C4.5 | For an energy that is the Dirichlet form of a reversible walk, the optimal k-coarse-graining (min max conductance, or min Ncut) is by definition a minimum (normalized) graph cut of $W_{xy} = \pi_xP_{xy}$; choosing the energy and choosing the reversible walk are the same choice. | construction | text; `cuts-fig-recipe` | reversibility; size measured by the stationary measure | 3.2 |
| C4.6 | Exact Ncut minimization is NP-hard in general. | standard | Shi & Malik 2000 | — | 3.2 |
| C4.7 | Treating information-theoretic energies (information bottleneck) as instances of the same recipe is a motivating analogy; in the Gaussian case the IB shares CCA's directions (exact), not its solution. | motivation (section 8 hook) + theorem pointer for the Gaussian fact | page 6, E13; Chechik et al. 2005 | Gaussian case: directions only | 3.2 |
| C4.8 | $L_{\rm rw}$ and $L_{\rm sym}$ share eigenvalues; eigenvectors differ by $\mathbf D^{1/2}$; the unnormalized L corresponds to counting measure (ratio cut); Sinkhorn balancing makes all degrees one. | standard | von Luxburg 2007; register A.1 | connected graph, positive degrees | 3.2 |
| C4.9 | As ε → 0, N → ∞, the α-normalized diffusion-map generator acts as $\Delta - 2(1-\alpha)\nabla U\cdot\nabla$: α = 0 is potential 2U, α = 1/2 the Langevin generator, α = 1 Laplace-Beltrami. | theorem (asymptotic) | Nadler et al. 2006, eq. (27); Coifman & Lafon 2006; disclosure | equilibrium samples from $e^{-U}$; Gaussian kernel; limit statement | 3.2 |
| C4.10 | Voltages with clamped inputs solve the graph Dirichlet problem (harmonic label propagation); effective resistance is $(e_x - e_y)^\top L^+(e_x - e_y)$. | standard | Zhu, Ghahramani & Lafferty 2003; disclosure | connected graph | 3.2 |
| C4.11 | Minimizing the degree-weighted Rayleigh quotient gives the generalized eigenproblem $Lf = \mu\mathbf Df$; spectral clustering rounds its bottom k eigenvectors. | standard | Ng, Jordan & Weiss 2002; von Luxburg 2007 | — | 3.3 |
| C4.12 | For every k-partition, $\mathrm{Ncut} \ge \sum_{i\le k}\mu_i$. | theorem | Ky Fan principle via Shi & Malik 2000; von Luxburg 2007 | partitions covering all points | 3.3 |
| C4.13 | $\mu_2/2 \le h(G) \le \sqrt{2\mu_2}$, the upper bound attained by a sweep of the second eigenvector. | theorem | Chung 1997; Levin & Peres 2017, Thm 13.10; register S.3 | connected undirected graph; degree volume; for the register's form, index shift | 3.3 |
| C4.14 | The sweep cut has conductance $O(k)\,\mu_2/\sqrt{\mu_k}$ for every k ≥ 2. | theorem | Kwok et al. 2013 | constants not explicit | 3.3 |
| C4.15 | $\mu_k/2 \le \rho_G(k) \le O(k^2)\sqrt{\mu_k}$ and $\rho_G(k) \le O(\sqrt{\mu_{2k}\log k})$; the lower bound is on the worst set, $\max_j\phi(A_j) \ge \mu_k/2$, not on each set. | theorem | Lee, Oveis Gharan & Trevisan 2014, Thms 1.1-1.2 | disjoint nonempty sets (need not cover); upper constants not explicit; holding kernels need S.3's conversion factor | 3.3 |
| C4.16 | On the running example the sweep conductance lies in the Cheeger bracket; at k = 4 the worst set's conductance lies above $\mu_4/2$ (individual sets need not) and Ncut above $\sum_{i\le4}\mu_i$; at k = 3 the third set changes with the rounding seed. | widget + builder values | explorer tours `pair-cut`, `wells`, `no-gap` | builder values | 3.3 |
| C4.17 | The best ℓ¹ relaxation ratio equals h(G) (exact, not an eigenproblem); the ℓ² relaxation pays a square root. | standard + construction | Chung 1997; Froyland 2015, Thm 2.1; disclosure (co-area derivation) | — | 3.3 |
| C4.18 | $\sum_j\|(I - VV^\top)g_j\|^2 \le \sum_j\phi(A_j)/\mu_{k+1}$ for any k-partition. | theorem (derived on the page; per-set form in the source) | Peng, Sun & Zanetti 2017, Thm 1.1; disclosure; explorer tile | normalized indicators $\mathbf D^{1/2}\mathbf 1_A/\sqrt{\mathrm{vol}A}$; V = bottom k eigenvectors of $L_{\rm sym}$ | 3.4 |
| C4.19 | An operator-norm perturbation e < δ_r/2 moves an isolated block by $\|\sin\Theta\| \le e/(\delta_r - e)$; vectors inside the block are not individually stable. | theorem | Davis & Kahan 1970; register A.21, A.28; `cuts-fig-scale` (b) | symmetric, same sites, contiguous isolated block | 3.4 |
| C4.20 | Normalized spectral clustering is consistent; Laplacian eigenmaps converge; fixed-β Sinkhorn kernels have explicit (often vacuous) finite-N rates. | theorem (conditional) | von Luxburg, Belkin & Bousquet 2008; Belkin & Niyogi 2007; register A.43-A.44 | i.i.d. samples; bandwidth schedules; constants | 3.4 |
| C4.21 | The gap $\lambda_r^t - \lambda_{r+1}^t$ is unimodal in t; gaps are not monotone in r; the retained count at threshold ϑ is the minimal rank with spectral error ≤ ϑ. | theorem | register S.10; `cuts-fig-scale` (a) | PSD walk (lazy) | 3.4 |
| C4.22 | On the running example's graph the gap after 4 exceeds the gap after 2 at short diffusion times and the reverse at long ones (crossing time from the builder). | widget + builder values | `cuts-fig-scale` (a); `p04.json` `scale` | builder values | 3.4 |
| C4.23 | For the reversible particle, α = 1/2 graph eigenvectors on equilibrium samples approximate the generator's eigenfunctions (large N, small bandwidth). | theorem (asymptotic) + widget | E6; Nadler et al. 2006; explorer tour `dmap` | as C4.9; finite-N agreement is shown, not certified | 3.5 |
| C4.24 | The leading singular vectors of a noisy transfer operator relax the balanced coherent-pair problem; finite doubly stochastic version with bipartite rounding. | theorem | Froyland 2013, Thm 2; register A.5, S.4 | Froyland's Assumptions 1-2; finite version: bistochastic factors; S.4 thresholds | 3.5 |
| C4.25 | $\epsilon^{-2}(\mathcal L_\epsilon^*\mathcal L_\epsilon - I) \to c(\Delta + \mathcal P^*\Delta\mathcal P) = 2c\,\Delta^D$. | theorem (scope-limited) | Froyland 2015, Thm 5.1 | flat compact manifold, $C^3$ volume-preserving map, isotropic noise with covariance cI | 3.5 |
| C4.26 | Dynamic Cheeger $h^D \le 2\sqrt{-\lambda_2^D}$; multistep average version; extension to non-volume-preserving maps. | theorem (scope-limited) | Froyland 2015, Thm 3.2, Cor 3.5; Froyland & Kwok 2017 | as stated in the disclosure; nonpositive sign convention | 3.5 |
| C4.27 | Time-averaged graph walks on trajectory data converge to the time-averaged forward-backward transfer operator; $(Q_\epsilon - I)/\epsilon$ approximates a weighted dynamic Laplacian. | theorem (scope-limited) | Banisch & Koltai 2017, Thm 3 and Remark 4 | deterministic trajectories; fixed ε, pointwise, m → ∞, $O(\epsilon^2)$; their normalization | 3.5 |
| C4.28 | A fixed set's conductance under $\bar M$ is the layer average of its conductances; a labelling's worst-set conductance under $\bar M$ is at most the layer average of its per-layer worst-set conductances (the maximum over sets does not commute with the average); Cheeger's inequality applies to $\bar M$. | construction + theorem | linearity of cut weight; register S.3 | $\bar M$ symmetric, nonnegative, doubly stochastic | 3.5 |
| C4.29 | NCS's Sinkhorn-normalized layer average converges to a dynamic Laplacian of the network's layer maps. | motivation (section 8 hook) | E18 text ("finite-graph analogue") only | — | 3.5 |
| C4.30 | On face C, the input layer's, the output layer's and the layer-averaged walk's sets answer "start close", "end close" and "stay close across the block"; each is drawn at every layer with its per-layer boundary cost, its block cost (worst-set conductance under $\bar M$, bounded above by the mean of the per-layer worst-set values; C4.28) and its agreement with the basins, as computed; no ordering is claimed in advance. | widget + builder values | `cuts-fig-dynamic` tours; `p04.json` `facec` | builder values; uncommitted band excluded from agreement | 3.5 |
| C4.31 | A metastable partition is approximately lumpable, with a bound. | pointer (theorem on page 6) | E12; Sarich, Noé & Schütte 2010 | page 6 | 3.5 |
| C4.32 | Hebbian clustering and spectral clustering are both thresholded spectral computations on a similarity matrix; no theorem connects them. | motivation (section 8 hook) | E23 | — | 3.5 |

Things not to claim on this page (SPEC appendix D and page-specific): static clustering of activations finds the dynamics (only E6's special case); finer resolution always has a smaller gap; spectral sparsification prunes networks safely; the sweep cut is the optimal cut; k eigenvectors always give k meaningful clusters; the higher-order upper bound has a known constant; the dynamic Laplacian theorems apply directly to NCS's graph operator; kNN-graph Laplacians converge to the same operator as α = 0 Gaussian kernels; coherent sets are the network's computational states.

## 5. Figures and widgets

All face A figures use `samples.json` (N = 1000, seed 0 unless a control says otherwise) and draw the potential's contours (ink, thin), the four wells as ink-outlined circles labelled $w_1..w_4$. Sets are coloured with the hierarchy tokens (SPEC 6.4): at k = 2 `--c-pair-L/R`, at k = 4 `--c-well-1..4`, matched to the builder's ground-truth basin labels by Hungarian matching on overlap; unmatched or extra sets (k = 3, 5, 6) use the categorical palette after the matched ones. Edges crossing between sets are drawn in accent.

### 5.1 `cuts-fig-hero` "Cut where little crosses" (live, hero; key `hr`)

- **Purpose:** the spectral cut runs through the regions where samples (and therefore edges) are scarce: first between the pairs, then inside each pair.
- **Layout:** `figure.fig.full.card`; two panels (stacked on phones). (a) Map (≈ 2/3 width): contours, the 1000 samples as dots coloured by set, kNN edges at 6 % opacity, edges crossing between sets in accent at full opacity. (b) Bar panel: for each set, its conductance $\phi(A_j)$ as a horizontal bar in the set's colour, the largest marked "worst set", with a dashed vertical line at the lower bound $\mu_k/2$ labelled "bound on the worst set" (individual bars may fall below it; a one-line legend says so) and, at k = 2, a second dashed line at $\sqrt{2\mu_2}$ labelled "sweep cut ≤".
- **Data:** live, `lib/graph.js`: union-symmetrized kNN graph ($k_{\rm nn}$ = 15, unit weights), $L_{\rm sym}$ bottom 6 eigenpairs by Lanczos, k = 2 by the Fiedler sweep (minimum-conductance prefix), k = 4 by k-means++ on the row-normalized bottom-4 embedding (NJW; 10 restarts, seed 0, lowest within-cluster sum of squares).
- **Controls:** one segmented control "sets: 2 | 4". Nothing else.
- **Default state (= first tour):** `pairs` (k = 2).
- **What changes:** colours, crossing edges, bars and the dashed lines.
- **Tours:** `pairs` (k = 2; note "The cheapest cut separates the two pairs."); `wells` (k = 4; note "At four sets the cuts run through the narrower bands inside each pair.").
- **fallbackTour:** `wells`.
- **Caption:** *Plotted:* (a) contours of $V(x_1,x_2)$; equilibrium samples coloured by spectral-clustering set; nearest-neighbour edges (faint) and edges between sets (accent); (b) conductance $\phi(A) = \mathrm{cut}(A)/\mathrm{vol}(A)$ of each set, the largest marked, with the lower bound $\mu_k/2$ on the largest and, for two sets, the sweep bound $\sqrt{2\mu_2}$. *Values:* N = 1000 samples from $\pi \propto e^{-V/D}$, D = 0.5, $h_x = 2.5$, $h_y = 1.5$, b = 0.6, κ = 0, seed 0; 15 nearest neighbours, unit weights. Running example, face A. `synthetic`.
- **Static fallback:** `assets/fallback/cuts-fig-hero-pairs.png`, `assets/fallback/cuts-fig-hero-wells.png`.
- **Accessibility:** alt text: "Dots in four clusters around the wells of a potential, joined by faint edges; a few highlighted edges cross the sparse band between the left and right clusters." Sets also labelled by text ("left pair", "$w_1$" …) in the bar panel; colour is not the only carrier.
- **Performance:** graph + Lanczos + rounding once per tour change, < 150 ms; cached.

### 5.2 `cuts-fig-recipe` "One recipe: energy, cut, relaxation, bound" (static SVG, with the shared bowtie)

- **Purpose:** the general recipe in one picture, and where the page's bound sits in the site's bowtie.
- **Content:** top row, four boxes joined by arrows, each with a one-line formula and its source in small type (no colour coding of status; SPEC section 8):
  1. "Choose an energy and a size" — $\mathcal E(f) = \frac12\sum W_{xy}(f_x - f_y)^2$, size $\mathrm{vol}$ — "a reversible walk";
  2. "Best coarse-graining = smallest boundary for its size" — $\rho_G(k)$, Ncut — "isoperimetry; NP-hard";
  3. "Relax sets to functions" — $Lf = \mu\mathbf Df$ — "eigenvectors";
  4. "Bound both ways, then round" — $\mu_k/2 \le \rho_G(k) \le O(k^2)\sqrt{\mu_k}$; sweep; η, Davis-Kahan — "Cheeger; Lee et al.; Davis-Kahan".
  Under box 1, a small fan of four labels: "similarity graph", "reversible chain (metastable)", "transfer operator / dynamic Laplacian (coherent)", "information bottleneck (page 6)"; the last label is followed by "analogy (Gaussian case: same directions as CCA, not the same solution)" in small type.
  Bottom row: the shared `bowtie` with left "points at time 0", right "points at time T", left and right norm "degree / Sinkhorn", knot bars = lazy-walk eigenvalues $\lambda_1..\lambda_8$ of the hero's graph (from `p04.json`, `hero.lambda`), r = 4, bound label "best k-way cut ≥ μ_k/2; sweep ≤ √(2μ₂)".
- **Generation:** SVG built by `p_cuts.js` with `bowtie.js` from data (so it updates with builder output).
- **Caption:** *Plotted:* schematic of the recipe; bars are eigenvalues $\lambda_i = 1 - \mu_i/2$ of the lazy walk on the hero's graph. *Values:* as the hero.
- **Fallback:** `assets/fallback/cuts-fig-recipe-default.png` (captured with a single tour `default`; key `rc`).
- **Accessibility:** alt text: "Four boxes: choose an energy, define the best cut, relax to eigenvectors, bound both ways; below, a bowtie diagram from points at time 0 to points at time T through eight bars."

### 5.3 `cuts-fig-explorer` "Cheeger's bracket, live" (live, centrepiece; key `ex`)

- **Purpose:** the eigenvalues bracket the best cut; the sweep attains the two-way upper bound; at k without a gap the rounding is arbitrary; the normalization changes which operator the graph approximates.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`: main view 2 × 2 panels; side panel (320 px): tours, controls, stat tiles, legend.
  - (a) **Map:** samples coloured by the k sets; accent crossing edges (kNN graph only; for dense kernels draw only edges with weight > 1 % of the maximum).
  - (b) **Spectrum:** $\mu_1..\mu_{12}$ (bars, linear y), k marked by an accent line; the gap $\mu_{k+1} - \mu_k$ shaded; reference ticks for the generator's rates rescaled to match $\mu_2$ (only for `gauss-dm`, from `grid.json`; legend "generator, rescaled").
  - (c) **Bracket:** for k = 2, the sweep curve: conductance of the prefix sets $\{x: f_2(x) > t\}$ (volume ≤ half) against the prefix volume fraction, minimum marked, horizontal dashed lines at $\mu_2/2$ and $\sqrt{2\mu_2}$; for k ≥ 3, per-set conductance bars with the worst set marked and the dashed line at $\mu_k/2$ labelled "bound on the worst set", and a second marker for Ncut against $\sum_{i\le k}\mu_i$.
  - (d) **Eigenvector:** $f_k$ (the k-th eigenvector of $L_{\rm rw}$) on the points, `div` map, symmetric range.
- **Data:** live, `lib/graph.js` + `lib/linalg.js` (Lanczos). Samples: `samples.json`. Reference eigenfunctions for correlation tiles: `grid.json` (bilinear interpolation of $\phi_2..\phi_4$ at the sample points).
- **Controls (primary):**
  1. graph: `knn` (union kNN, unit weights) | `gauss-rw` (Gaussian kernel $e^{-\|x-y\|^2/(2s^2)}$, α = 0) | `gauss-dm` (same kernel, α = 1/2 diffusion-map normalization) | `sinkhorn` (same kernel, Sinkhorn-balanced, degree one);
  2. k: slider 2-6;
  3. scale: $k_{\rm nn}$ 5-40 (default 15) for `knn`; bandwidth s 0.08-0.5 (default 0.2) for the kernels (one slider whose meaning follows the graph; label updates);
  4. N: 500 | 1000 | 2000 (prefixes of the seeded sample set).
  Advanced: rounding seed (0-9); edge drawing on/off.
- **What changes when each control moves:** graph/scale/N: everything recomputes ("computing…" over 200 ms); k: (a), (c), (d), tiles; seed: (a) and (c) for k ≥ 3 (the eigenvectors do not change; the rounding may).
- **Stat tiles:**
  - "μ₂" and "gap after k": $\mu_{k+1} - \mu_k$.
  - "Cheeger bracket" (k = 2): "$\mu_2/2$ ≤ h ≤ $\sqrt{2\mu_2}$" with the sweep's conductance; (k ≥ 3): "lower bound $\mu_k/2$; worst set achieved".
  - "Ncut vs Σμ": achieved Ncut of the rounded partition and $\sum_{i\le k}\mu_i$.
  - "Partition residual": $\eta^2$ of the rounded partition (normalized indicators, bottom-k eigenvectors of $L_{\rm sym}$) and its bound $\sum_j\phi(A_j)/\mu_{k+1}$.
  - "Agreement with generator" (only `gauss-dm`, `gauss-rw`, `sinkhorn`): absolute correlations $|\mathrm{corr}(f_i, \phi_i)|$ for i = 2..min(k, 4), where $\phi_i$ are the reference generator eigenfunctions; for i = 3, 4 (a nearly degenerate pair at κ = 0) report the principal-angle cosine of the 2-D spans instead, labelled "span of 3-4".
- **Tours** (default first):
  1. `pair-cut`: knn, k = 2, $k_{\rm nn}$ = 15, N = 1000. Note: "The sweep's conductance sits inside the Cheeger bracket."
  2. `wells`: knn, k = 4. Note: "Four sets: the worst set's conductance is above μ₄/2, as the theorem requires; single sets may be below it."
  3. `no-gap`: knn, k = 3, seed 0 (and the note invites seed 1). Note: "No gap after 3: the third set is whichever within-pair split the rounding picks."
  4. `dmap`: gauss-dm, k = 4, s from the builder (`p04.json`, `tours.dmap.s`, the bandwidth in {0.1, 0.15, 0.2, 0.3} maximizing the span-of-2-4 agreement at N = 2000), N = 2000. Note: "With α = 1/2 the eigenvectors track the particle's slow functions (E6)."
  5. `rw-scale`: gauss-rw, same s and N as `dmap`, k = 4. Note: "α = 0: same shapes, but the spectrum is that of potential 2U: compare μ₃/μ₂ with dmap's." The tile shows both ratios (builder values) and the generator's $\nu_3/\nu_2$.
  6. `sinkhorn`: sinkhorn, k = 4, s = 0.2, N = 1000. Note: "Degree one: sizes are counts, and the residual bound applies directly to page 5's SEBA."
- **fallbackTour:** `wells`.
- **Caption:** *Plotted:* (a) samples coloured by the k sets from the bottom k eigenvectors (k-means on the row-normalized embedding; for k = 2 the minimum-conductance sweep), edges between sets; (b) eigenvalues $\mu_i$ of $L_{\rm sym}$; (c) conductance of sweep sets with the bounds $\mu_2/2$ and $\sqrt{2\mu_2}$, or per-set conductances with $\mu_k/2$, a lower bound on the largest of them; (d) the k-th eigenvector of $L_{\rm rw}$. *Values:* graph, scale, k and N as set; samples from $\pi \propto e^{-V/D}$, D = 0.5, seed 0. Running example, face A. `synthetic`.
- **Static fallback:** PNG per tour; GIF stepping k = 2..6 on the `knn` graph (1 s per frame).
- **Accessibility:** panels have `aria-label`s; tiles are text; tour notes are announced; sets named in the legend.
- **Performance:** knn N = 2000: graph < 60 ms, Lanczos (12 pairs) < 150 ms; dense kernels at N = 2000: matvec 4·10⁶, Lanczos ≈ 60 iterations, < 600 ms (status shown); Sinkhorn (damped iteration, tolerance 1e-10 on row sums) < 200 ms at N = 1000. Parity: graph construction, Sinkhorn and Lanczos eigenvalues match the builder to 1e-8 relative (SPEC 6.7).

### 5.4 `cuts-fig-scale` "The scale decides which block has the gap" (static, rendered by the page module; key `sc`)

- **Purpose:** (a) the gap after 2 and the gap after 4 cross as the diffusion time grows; (b) the better-separated block is the one that resists perturbation, and Davis-Kahan says by how much.
- **Data:** precomputed by the builder (`p04.json`, `scale`), for the hero's graph (knn, $k_{\rm nn}$ = 15, N = 1000, seed 0) and its lazy walk $M = I - L_{\rm sym}/2$ (symmetric form; eigenvalues $\lambda_i = 1 - \mu_i/2 \in [0,1]$):
  - (a) $g_2(t) = \lambda_2^t - \lambda_3^t$ and $g_4(t) = \lambda_4^t - \lambda_5^t$ on a log grid t ∈ [1, 10⁴] (200 points); the crossing time $t_\times$; each curve's maximizer $t^* = \log(\log b/\log a)/\log(a/b)$ (S.10);
  - (b) positional jitter: for σ_j ∈ {0.005, 0.01, 0.02, 0.04, 0.08} and seeds 0-2, rebuild the graph on the jittered positions **of the same sites with the same neighbour sets** (so only weights would change; with unit weights, rebuild neighbours and accept that the edge set changes, the builder records which), compute $e = \|L'_{\rm sym} - L_{\rm sym}\|_2$, the actual $\|\sin\Theta\|_{\rm op}$ for the bottom-2 and bottom-4 blocks, and the bound $\min(1, e/(\delta - e))$ when $e < \delta/2$ (else "vacuous"). To keep edge sets fixed, the builder uses the Gaussian-weighted version of the kNN graph for panel (b) (weights $e^{-\|x-y\|^2/(2s^2)}$ on the fixed union-kNN edge set, s = median kNN distance); the caption says so.
- **Content:** (a) line chart, log x, two series in `--c-pair-L` ("gap after 2") and `--c-well-4` ("gap after 4"), vertical dashed line at $t_\times$; (b) scatter, log-log, x = e, y = sine of the angle; actual (filled dots, two colours for the two blocks), bound (open circles, same colours), vacuous points drawn at y = 1 with an "×".
- **Caption:** *Plotted:* (a) gaps $\lambda_2^t - \lambda_3^t$ and $\lambda_4^t - \lambda_5^t$ of the lazy walk against diffusion time t; (b) for positional jitter of the samples, operator-norm change e of the normalized Laplacian against the sine of the largest principal angle between the bottom-2 (and bottom-4) eigenspaces before and after, with the Davis-Kahan bound $e/(\delta - e)$. *Values:* hero graph (panel (b): Gaussian weights on the same edges); jitter σ_j as listed, seeds 0-2. Running example, face A. `synthetic`.
- **Fallback:** `assets/fallback/cuts-fig-scale-default.png`.
- **Accessibility:** alt text: "Two curves that rise and fall, crossing once: the gap after four is larger at short times, the gap after two at long times. Beside it, dots for actual angles lie below circles for the bound."

### 5.5 `cuts-fig-dynamic` "Where inputs start, where they end, and what stays together" (live; key `dy`)

- **Purpose:** on the toy residual network, three walks ask three questions of the same tracked inputs: which start close (input layer), which end close (output layer), which stay close across the block (layer average). Every labelling is drawn at every layer; a strip shows each labelling's boundary cost at each layer. No walk is presented as the only one that shows where inputs go.
- **Layout:** `figure.fig.wide.card`; main: (a) the points at the displayed layer coloured by the chosen operator's sets, uncommitted-band points drawn with a ring; (b) small multiples: the same sets drawn at layers 0, 4, 8, 12 (four mini-maps). Side: controls, (c) spectrum $\lambda_1..\lambda_{10}$ of the chosen operator with the gaps after 2 and after 4 labelled, tiles. Under (b), a **boundary-cost strip**: the worst-set conductance under each layer's walk $M^{(\ell)}$, ℓ = 0..12, for the chosen operator's sets (solid) and for the other two labellings (faint: input layer, output layer, average), with two marks at the right end of each line: the labelling's worst-set conductance under $\bar M$, computed under $\bar M$ itself (solid), and the line's mean over layers (dashed, labelled "upper bound"). Each fixed set's conductance under $\bar M$ is exactly the mean of its per-layer conductances (C4.28), but the worst set can change from layer to layer and the maximum over sets does not commute with the average, so the mean of the worst-set line is only an upper bound on the worst-set conductance under $\bar M$.
- **Data:** live, face C (`lib/example.js` flow: RK4, ≥ 8 substeps per layer, T = 0.3, 12 layers; N = 1000 inputs uniform on the input box, seed 0). Per layer ℓ = 0..12: union-symmetrized kNN graph on $x^{(\ell)}$ (SPEC 3.5's binding face C graph: union of directed kNN graphs, $k_{\rm nn}$ = 15, weight 1 on edges and a floor $10^{-6}$ on every other pair so Sinkhorn scaling exists, diagonal 0; register A.1), Sinkhorn-balanced $P^{(\ell)}$, lazy $M^{(\ell)} = (I + P^{(\ell)})/2$. Dynamic operator $\bar M = \frac1{13}\sum_\ell M^{(\ell)}$. Sets: k-means on the row-normalized top-r eigenvectors (as in the hero). Ground truth: input basins (quadrants at κ = 0); uncommitted band per SPEC 3.5. This is page 10's implemented NCS operator on positions (page 10 adds the lift); pages 3, 4 and 10 share it.
- **Controls (primary):**
  1. operator: `dynamic` (layer average: "stay close") | `static` (one layer's $M^{(\ell)}$: "close at layer ℓ"; ℓ = 0 is "start", ℓ = 12 "end");
  2. layer ℓ: 0-12 (for `static`, the operator's layer; in both modes, the layer at which panel (a) draws the points);
  3. r: 2 | 4;
  4. $D_{\rm flow}$: 0-0.05 (default 0; Froyland's small-noise regime).
  Advanced: $k_{\rm nn}$ (5-40); seed.
- **What changes:** operator/layer (static)/r/$D_{\rm flow}$/seed recompute sets and spectrum; layer in dynamic mode only redraws (a).
- **Stat tiles:** "agreement with basins" (Hungarian-matched Jaccard averaged over sets, excluding the uncommitted band; also the fraction of points excluded) for the chosen operator and, in smaller type, for the other two labellings; "gap after r" ($\lambda_r - \lambda_{r+1}$ of the chosen operator); "worst set conductance under $\bar M$" for all three labellings, computed under $\bar M$, with the note "≤ the average over layers of the worst-set values; each single set's conductance under $\bar M$ equals its own layer average" (C4.28). Tiles show the builder's values whichever labelling scores best.
- **Tours** (default first):
  1. `dynamic`: dynamic, ℓ = 0, r = 4, $D_{\rm flow}$ = 0. Note: "The layer-averaged walk: sets whose boundaries are cheap across all layers; the strip shows their cost at each layer."
  2. `static-0`: static, ℓ = 0, r = 4. Note: "The input layer alone: which inputs start close, in a uniform cloud." (Add the gap statement only as the builder found it; 13.)
  3. `static-12`: static, ℓ = 12, r = 4. Note: "The output layer alone: four clumps. Drawn at layer 0, they show where each input ends up, because the flow ends in wells; the strip shows what their boundaries cost at earlier layers."
  Comparative notes ("…matches the basins better/worse than…") are written from `p04.json` `facec` after the builder runs, never in advance.
  4. `pairs`: dynamic, r = 2. Note: "Two sets: the pairs."
  5. `noise`: dynamic, r = 4, $D_{\rm flow}$ = 0.05. Note: "With diffusion in the flow the sets blur at their edges."
- **fallbackTour:** `dynamic`.
- **Caption:** *Plotted:* (a) the N points at layer ℓ of the toy residual network, coloured by the sets from the chosen operator's top r eigenvectors, points still in the uncommitted band ringed; (b) the same sets at layers 0, 4, 8, 12; (c) eigenvalues of the chosen operator (one layer's lazy Sinkhorn walk, or their average over layers 0-12); strip: worst-set conductance of each labelling's sets under each layer's walk, with the worst-set conductance under the layer average (solid mark) and the strip's mean over layers (dashed mark), an upper bound on it. *Values:* T = 0.3, 12 layers, $D_{\rm flow}$ as set, N = 1000 inputs uniform on the input box, seed 0; 15 nearest neighbours. Running example, face C. `synthetic`.
- **Static fallback:** PNG per tour; GIF of `dynamic` stepping ℓ = 0..12 (0.5 s per frame).
- **Accessibility:** alt text: "Points of a toy network at one layer, coloured into four sets; four small maps show the same sets at layers 0, 4, 8 and 12; below, three lines of boundary cost against layer." Sets labelled by basin in the legend.
- **Performance:** flow of 1000 points ≈ 30 ms; 13 kNN graphs + Sinkhorn ≈ 250 ms (the $10^{-6}$ floor applied as a rank-one-plus-diagonal correction, never stored densely); Lanczos on $\bar M$ (≈ 2·10⁵ nonzeros) < 100 ms; full recompute < 500 ms with "computing…".

## 6. Running example on this page

- Faces: A (equilibrium samples; default), C (dynamic section). Parameters exactly as SPEC 3.2 and 3.5: $h_x = 2.5$, $h_y = 1.5$, b = 0.6, κ = 0, D = 0.5; face C T = 0.3, 12 layers, $D_{\rm flow}$ = 0 default.
- **Face C input box (SPEC 3.5):** $[-1.4, 2.6]	imes[-1.0, 1.4]$, adopted in SPEC from this page's analysis. Reason, stated once on the page: a box symmetric about $x_1 = 0$ and $x_2 = 0$, such as $[-2,2]	imes[-1.2,1.2]$, gives the uniform input cloud first nontrivial Neumann modes ≈ sign $x_1$, sign $x_2$ and their product (box eigenvalues in ratio 0.62 : 1.71 : 2.33 : 2.47 for modes (1,0), (0,1), (1,1), (2,0)), so static clustering of layer 0 at r = 4 would reproduce the quadrants (the basins) by coincidence, with no gap after 4 (2.33 vs 2.47). The asymmetric box breaks the coincidence; its layer-0 modes change sign at the box's centre lines, not at the basin boundaries.
- Precomputed (`tools/build_example.py` → `site/data/cuts/p04.json`, with config and assertions):
  - `hero`: for the default knn graph (N = 1000, seed 0, $k_{\rm nn}$ = 15): $\mu_1..\mu_{12}$; lazy-walk $\lambda_1..\lambda_8$; sweep cut conductance and its set's mean $x_1$ (and the $x_1$ range of crossing edges); k = 4 sets (labels), their conductances and mean positions; Ncut and $\sum_{i\le4}\mu_i$; η² and bound at k = 2 and k = 4.
  - `tours.dmap.s` (bandwidth choice rule above); for `dmap` and `rw-scale`: $\mu_3/\mu_2$, span-agreement values, and the generator's $\nu_3/\nu_2$ from `grid.json`.
  - `scale`: as in 5.4.
  - `facec`: for SPEC 3.5's box, seed 0, N = 1000, $D_{\rm flow}$ ∈ {0, 0.05}: eigenvalues $\lambda_1..\lambda_{10}$ of $\bar M$, $M^{(0)}$, $M^{(12)}$; for each of the three labellings (sets of $M^{(0)}$, $M^{(12)}$, $\bar M$) at r = 2, 4: agreement with basins, worst-set and mean conductance under each $M^{(\ell)}$ and under $\bar M$; band fraction. Also the same at N = 8000 as the SPEC 3.6 numerical reference (eigenvalues and agreements only).
  - **Assertions** (if one fails, stop and amend this spec; do not retune parameters silently): kNN graph connected; sweep conductance within $[\mu_2/2, \sqrt{2\mu_2}]$; the k = 2 sweep set separates the samples with $x_1 < 0$ from $x_1 > 0$ with ≥ 95 % agreement (else the page's "between the pairs" sentence changes to what is computed); η² ≤ bound for k = 2, 4; all Davis-Kahan actual angles ≤ bounds whenever $e < \delta/2$; for every set of every labelling, its conductance under $\bar M$ equals the mean of its per-layer conductances to 1e-12 (C4.28; checks the code), and each labelling's worst-set conductance under $\bar M$ is at most the mean of its per-layer worst-set conductances (+1e-12; equality not asserted). No assertion orders the three labellings: the page reports what the builder finds.
- Live: everything drawn in the hero, explorer and dynamic widget (graphs, eigenvectors, rounding, sweeps, flow).
- Strain stated on the page: face A is reversible, so its coherence is metastability and static clustering of equilibrium samples suffices (E6); face C is where transport matters. The double gyre (the standard coherent-set example) is named in one sentence in 3.5 with a link to Froyland 2015, not built. Face C is a contracting gradient flow, outside Froyland 2015's volume-preserving hypotheses (inside Froyland & Kwok 2017's).
- Companions: none built; the double gyre is text only.

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E6 | 3 Koopman | `=` | For the reversible particle, α = 1/2 diffusion-map eigenvectors on equilibrium samples converge to the generator's eigenfunctions: static clustering of samples recovers the slow dynamics. |
| E7 | 3 Koopman | `≈` | With transport, coherent sets are leading singular vectors of a noisy transfer operator; as noise vanishes the forward-backward composite tends to the dynamic Laplacian, which has its own Cheeger inequality. |
| E8 | 5 Sparsity | `≈` | A spectral sparsifier keeps every cut and Laplacian eigenvalue of this page's graphs to within 1 ± ε; conductances move by at most the degree ratio; eigenvectors follow where there is a gap. |
| E9 | 5 Sparsity | `≈` | SEBA rotates this page's eigenvectors into sparse set indicators; the partition residual η bounded here is the input to its conditional rounding certificate. |
| E10 | 8 Hebbian | `=` | Clamped voltages on a resistor network solve this page's graph Dirichlet problem: harmonic label propagation; effective resistance is the same Laplacian's pseudo-inverse. |
| E12 | 6 Comp. mechanics | `≈` | A partition with small conductance and a large gap is approximately lumpable: the induced chain reproduces the slow dynamics with an error bounded by step-function approximation of eigenfunctions and the spectral ratio. |
| E18 | 10 LLMs from inside | `=` | NCS operators are Sinkhorn-balanced kernel walks on data points; their layer average is a finite-graph analogue of the dynamic Laplacian, and every bound here applies with the register's hypotheses. |
| E23 | 8 Hebbian | `~` | Hebbian clustering and spectral clustering both threshold a spectral computation on a similarity matrix; no theorem says Hebbian learning finds a chosen Laplacian partition. |

Map card text: "Spectral clustering · cut where little crosses for its size · knob: number of sets k and the graph's scale · bound: μ_k/2 ≤ best k-way cut; sweep ≤ √(2μ₂)."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The normalized Laplacian (equivalently the random walk) of a similarity graph on data points, weighted by degree (or Sinkhorn-balanced to degree one); with dynamics, the forward-backward transfer operator, its small-noise limit the dynamic Laplacian, or the layer average $\bar M$ of graph walks. |
| Knob | Number of sets k (= r); the graph's scale ($k_{\rm nn}$ or bandwidth s, β); diffusion time t or lag τ. |
| Discarded at r | The integrality of sets (indicators relaxed to real functions) and every mode beyond k: at k = 2 the within-pair split, at k = 4 detail inside a well. |
| Bound | Relaxation: $\mathrm{Ncut} \ge \sum_{i\le k}\mu_i$ and $\mu_k/2 \le \rho_G(k)$ (`theorem`). Rounding: $h(G) \le \sqrt{2\mu_2}$ by sweep (Cheeger; `theorem`); $\rho_G(k) \le O(k^2)\sqrt{\mu_k}$, $\rho_G(k) \le O(\sqrt{\mu_{2k}\log k})$ (Lee, Oveis Gharan & Trevisan 2014; `theorem`, constants not explicit); partition residual $\eta^2 \le \sum_j\phi(A_j)/\mu_{k+1}$ (Peng, Sun & Zanetti 2017; `theorem`). Dynamic: $h^D \le 2\sqrt{-\lambda_2^D}$ (Froyland 2015, Thm 3.2, nonpositive sign convention; flat manifold, volume-preserving; `theorem (scope-limited)`). |
| From data | Davis-Kahan $\|\sin\Theta\| \le e/(\delta_r - e)$ for $e < \delta_r/2$ (register A.21; `theorem`); consistency of normalized spectral clustering (von Luxburg, Belkin & Bousquet 2008), graph-to-manifold convergence (Belkin & Niyogi 2007), α = 1/2 limit (Nadler et al. 2006), finite-N Sinkhorn rates (A.43-A.44) — `conditional`. |
| Running example | From the builder (`p04.json`): $\mu_2..\mu_5$ of the knn graph; sweep conductance against $[\mu_2/2, \sqrt{2\mu_2}]$; location of the k = 2 and k = 4 cuts; η² and its bound at k = 2, 4; crossing time $t_\times$ of the gap curves; face C agreement and gaps for $\bar M$, $M^{(0)}$, $M^{(12)}$. |
| Budget line | R (Cheeger and partition-residual rounding), P (Davis-Kahan perturbation). |

## 9. Things not to claim

Static clustering of activations finds the dynamics (only E6's reversible, density-normalized case); finer resolution always has a smaller gap, or gaps are monotone in r; spectral sparsification prunes networks safely; the sweep cut is the minimum-conductance cut (it is within the Cheeger bound of it); the higher-order Cheeger upper bound has an explicit constant; the k-th gap certifies k semantic clusters; Froyland's theorems apply directly to NCS's Sinkhorn kNN graph or to face C (face C is not volume-preserving; the graph is not a manifold); NCS's layer average provably converges to a dynamic Laplacian; kNN graphs and α = 0 Gaussian graphs have the same limit; coherent sets are the network's computational states; activation cells are coherent sets.

## 10. Notation used

Global (SPEC appendix A): r, k (used as r for sets), $\lambda_i$, $\mu_i$ (ascending, $\mu_1 = 0$), $\delta_r$, P, M (lazy walk), L, W, β, $k_{\rm nn}$, ε (only in the dynamic section, as Froyland's noise scale: a side note says it is not the sparsifier accuracy of page 5), $\mathcal P$, $\mathcal L$ (here the noisy transfer operator $\mathcal L_\epsilon$ follows Froyland; a side note says it is not the generator $\mathcal L$ of SPEC 3.2), $x, V, D, \pi$, $w_1..w_4$, L/R, $x^{(\ell)}, P^{(\ell)}, \bar M$, ϑ.
Page-local: $\mathbf D = \mathrm{diag}(d_x)$ (degree matrix, bold; plain D is the diffusion coefficient D = 0.5, which appears in the α-family disclosure and captions: a side note at first use), $h(G)$ (Cheeger constant), $\rho_G(k)$ (k-way conductance), $\phi(A)$ (conductance), $d_x$, $\mathrm{vol}$, $\mathrm{cut}$, $\mathcal E$ (energy), m (size measure), $L_{\rm rw}$, $L_{\rm sym}$, $f_i$ (eigenvectors), $g_j$ (normalized indicators), η, s (kernel bandwidth; a side note relates it to β = 1/(2s²) for Gaussian kernels on positions), α (diffusion-map normalization exponent; not a Hankel weight), U (potential of the sampled density, U = V/D here), $\Delta^D$, $h^D$, $\lambda_2^D$ (Froyland's nonpositive dynamic Laplacian eigenvalue), $t_\times$. Index shift when quoting CoherentModes (S.3, S.4, S.10, A.5): their $\lambda_1$ is this site's $\lambda_2$; say so once.

## 11. Sources

Cite as in SPEC appendix C; status there unless noted.

- Chung, F. R. K. (1997). *Spectral Graph Theory*. CBMS 92, AMS. (Cheeger inequality for graphs; co-area/Federer-Fleming form.) [V]
- Levin, D. A. & Peres, Y. (2017). *Markov Chains and Mixing Times*, 2nd ed., AMS, Theorem 13.10. [M; as cited in CoherentModes `SPARSITY.md`]
- Shi, J. & Malik, J. (2000). Normalized cuts and image segmentation. *IEEE TPAMI* 22(8), 888-905. [M]
- von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing* 17(4), 395-416. [M]
- Ng, Jordan & Weiss 2002.
- Lee, Oveis Gharan & Trevisan 2014, Theorems 1.1-1.2.
- Kwok, Lau, Lee, Oveis Gharan & Trevisan 2013.
- Louis, Raghavendra, Tetali & Vempala 2012 (in the hypotheses disclosure only, as the many-sparse-cuts variant).
- Peng, R., Sun, H. & Zanetti, L. (2017). Partitioning well-clustered graphs: spectral clustering works! *SIAM J. Comput.* 46(2), 710-743; COLT 2015; arXiv:1411.2021. Theorem 1.1 (structure theorem; part 1: $\|g_i - \hat f_i\|^2 \le 1/\Upsilon$, $\Upsilon = \lambda_{k+1}/\rho(k)$). [P: Theorem 1.1 checked in arXiv v2 during this spec]
- Davis & Kahan 1970.
- von Luxburg, Belkin & Bousquet 2008; Belkin & Niyogi 2003, 2007.
- Coifman & Lafon 2006 [V].
- Nadler, Lafon, Coifman & Kevrekidis 2006, eq. (27) and the three α cases (checked in arXiv:math/0503445 during this spec: α = 0 gives potential 2U, "best suited for spectral clustering"; α = 1/2 the backward Fokker-Planck operator with potential U; α = 1 Laplace-Beltrami). [P]
- Zhu, Ghahramani & Lafferty 2003.
- Froyland 2013, Theorem 2 [V; as checked in CoherentModes `SPARSITY.md`, S.4 notes].
- Froyland 2015: Definition 2 ($h^D$), eq. (15) (dynamic Laplacian), Theorem 2.1 (Federer-Fleming), Theorem 3.2 (dynamic Cheeger), Corollary 3.5 (multistep), Theorem 5.1 (small-diffusion limit). [P: numbers checked in arXiv:1411.7186v4 during this spec]
- Froyland & Kwok 2017 (non-volume-preserving, weighted manifolds) [P per appendix C; abstract re-checked].
- Froyland 2024, tutorial (further reading link).
- Banisch, R. & Koltai, P. (2017), *Chaos* 27, 035804; arXiv:1603.04709. Theorem 3 and Remark 4. [P: checked during this spec]
- Sarich, Noé & Schütte 2010 (pointer only; page 6).
- CoherentModes theorem register (programme source): `THEOREMS.md` A.1 (`:72-136`), A.5 (`:209-258`), A.21 (`:570-602`), A.28 (`:933`), A.43-A.44 (`:1158-1246`); `SPARSITY.md` S.3 (`:62-85`), S.4 (`:87-115`), S.8 (`:157-171`, pointer), S.10 (`:184-198`).
- Code provenance (not citations): Sinkhorn and Lanczos follow `lib/graph.js`/`lib/linalg.js` (parity with `CoherentModes/viz/toy.py`).

## 12. Implementation notes

- Files: `site/content/cuts.html`, `site/js/p_cuts.js`, helpers `site/js/p_cuts_hero.js`, `p_cuts_explorer.js`, `p_cuts_dynamic.js`, `p_cuts_round.js` (k-means++ with restarts on row-normalized embeddings; may move to `lib/graph.js` if page 10 needs it); data `site/data/cuts/p04.json`, `site/data/cuts/widgets.json`.
- Shared modules used: `lib/example.js` (V, contours, face C flow, sample loader, basin labels), `lib/graph.js`, `lib/linalg.js`, `lib/rng.js`, `lib/bowtie.js`, `charts.js`, `ui.js`.
- `lib/graph.js` must expose: `knnGraph(X, k, {weights: "unit"|"gauss", s})` (union-symmetrized, CSR; face A), `knnUnion(X, k, {metric: "euclidean", floor: 1e-6})` (face C, SPEC 3.5), `gaussKernel(X, s, {alpha})` (dense or thresholded, with α normalization), `sinkhorn(K, {tol, maxIter, addDiagonal})`, `normalizedLaplacian(W)`, `lazyWalk(P)`, `bottomEigs(Lsym, k)` (via Lanczos on $I - L_{\rm sym}/2$), `sweepCut(W, f)` → `{set, conductance, curve}`, `conductance(W, labels)`, `ncut(W, labels)`. Request any missing function from the shared-numerics owner; prototype in `p_cuts_*.js` first.
- Widget keys and URL state: hero `hr` (`hr_k`, `hr_tour`); explorer `ex` (`ex_graph`, `ex_k`, `ex_scale`, `ex_N`, `ex_seed`, `ex_tour`); scale figure `sc` (tour `default`); recipe figure `rc` (tour `default`); dynamic `dy` (`dy_op`, `dy_layer`, `dy_r`, `dy_D`, `dy_knn`, `dy_seed`, `dy_tour`).
- Tests: parity of kNN graph, Sinkhorn, Lanczos eigenvalues and sweep conductance against the builder (1e-8 relative; sweep set identical); a node test that each explorer tour's tiles match `p04.json`; a test that `cuts-fig-scale` reads only builder data.

## 13. Page-specific definition-of-done additions

- [ ] The words "optimal" and "best" appear only with the set function and the class of competitors ("the minimum-conductance two-way cut", "the best k-way coarse-graining in max-conductance").
- [ ] Every higher-order Cheeger statement says its upper constant is not explicit; no figure plots an upper k-way bound with an invented constant.
- [ ] The sign convention note for Froyland's nonpositive Laplacian is present wherever $\lambda_2^D$ appears.
- [ ] The section 8 hook wraps C4.4, C4.7, C4.29, C4.32 exactly; nothing else on the page uses it.
- [ ] On the `no-gap` tour, changing the rounding seed visibly changes the third set (check two screenshots); if it does not at the builder's seed pair, pick the seed pair from the builder (`p04.json`, `tours.nogap.seeds`).
- [ ] The `static-0` note matches what the builder found.
- [ ] No sentence, note or caption says that only the layer-averaged walk shows where points end up or came from; comparative statements quote `p04.json` `facec`.
- [ ] Every display of $\mu_k/2$ against per-set conductances labels it as a bound on the worst set.
- [ ] Whole page including disclosures ≤ 6,000 words (main ≈ 2,250 + disclosure caps ≈ 3,500).
- [ ] Dense-kernel recomputes at N = 2000 stay under 1 s in headless Chrome; otherwise cap N at 1000 for the kernel graphs and record it.

## Change log

- v1 (2026-11-17): first full spec. Theorem numbers for Froyland 2015 (Thm 3.2, Cor 3.5, Thm 5.1), Nadler et al. (eq. 27), Peng-Sun-Zanetti (Thm 1.1) and Banisch-Koltai (Thm 3, Remark 4) checked against the papers. Page-local `shifted` input box added for face C (reported for a SPEC 3.5 amendment).
- v1.1 (2026-11-17): reconciled with SPEC v1.1. SPEC 3.5 adopted the asymmetric input box as face C's default, so the `shifted` option, tour and assertion qualifier are dropped and section 6 keeps the reason; the face C graph is SPEC 3.5's binding construction (floor $10^{-6}$, zero diagonal, replacing the unit diagonal); E10 now also touches page 5 (no change to this page's E10 row); the in-text pointer to the motivation claim corrected from C4.27 to C4.29; bibliography requests removed (now in appendix C). The degree matrix is written $\mathbf D$ (bold) to keep D for the diffusion coefficient, which the α-family disclosure also uses.
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). (1) Higher-order Cheeger: $\mu_k/2$ is a lower bound on the
  worst set's conductance, not on each set (path counterexample stated); hero bar panel, explorer panel (c), the
  `wells` tour note, the 3.3 callout, C4.15 and C4.16 now compare it with the worst set. (2) Displayed equation 8 now
  has the limit $2c\,\Delta^D$, consistent with C4.25 and Froyland 2015, Thm 5.1. (3) Face C: the claim that the
  output layer's walk cannot trace inputs back is removed; the three walks are presented as start / end / stay close,
  each labelling drawn at every layer with a per-layer boundary-cost strip; widget renamed; the assertion that the
  average beats the input layer is replaced by the mean-conductance identity; comparisons are quoted from the builder
  whichever way they come out. (4) Information bottleneck: the Gaussian case is stated as sharing CCA's directions,
  not its solution (recipe figure label, 3.2, C4.7; E13 is now `~`). Reviewer findings: design 3, math-1-6 5, 7, 10.
- v1.3 (2026-11-17): round-2 review fixes (SPEC v1.3). (1) `cuts-fig-dynamic`: a fixed set's conductance under
  $\bar M$ is the mean of its per-layer conductances, but the strip plots the worst set per layer and the maximum over
  sets does not commute with the average (only ≤ holds). Option chosen: keep the worst-set strip, mark the worst-set
  conductance computed under $\bar M$, and mark the strip's mean as an upper bound on it (layout, tile note, caption,
  C4.28, C4.30, builder assertion). (2) 3.4's conclusion no longer says every certificate divides by the gap: subspace
  certificates do; eigenvalue and operator-error bounds are compared with the gap; rounding also needs η and c.
  Reviewer findings: round 2, items 3 and 6.
