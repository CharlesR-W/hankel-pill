# SpectralTutorial: site specification

Version 1.3, 17 November 2026 (round-2 review fixes on top of v1.2's round-1 fixes and v1.1's reconciliation; amendments listed at the end of this file).
This file and `PAGE_TEMPLATE.md` are the whole brief for anyone writing or building a page. A page writer receives
this file, the template, and one per-page spec (`pages/NN-<id>.md`); nothing else should be needed. Where this file
and a per-page spec disagree, this file wins until it is amended.

Contents

1. Purpose, reader, thesis
2. Pages, claims, dependencies, and the connection matrix
3. The running example
4. The ledger, and the page-10 error budget
5. Skimmability and length
6. Site architecture and design system
7. Inventory: what exists, what must be built
8. PLACEHOLDER: marking schematic or open links
9. Build order and definition of done

Appendices: A. Notation. B. Glossary of terms that mean different things in different fields. C. Master
bibliography with check status. D. Things never to claim.

---

## 1. Purpose, reader, thesis

### 1.1 Purpose

A pedagogical website that introduces mechanistic-interpretability researchers to the mathematics behind a family of
spectral methods, and shows that the family is one spectral framework seen from many sides: nine pages decompose a
map through an SVD, and one (page 8) shows a learning rule whose fixed points are spectral decompositions of their
own. The site has two aims, in order:

1. The reader comes to believe the approach is principled: there is a reason to take an SVD of a particular
   operator, and the reason comes with bounds.
2. The reader finds it credible that the specific methods developed in this programme (predictive states from
   input/output tables; neural coherent sets, NCS, from the flow of data points through layers) are principled,
   largely because of how many established theories they reduce to or relax.

The single result the site should leave most firmly in the reader's mind: **coherent-set and truncation methods,
applied to neural networks including LLMs, come with an error budget whose terms have names (truncation, sampling,
perturbation, sparsification, rounding, and an unbounded interpretation term); most terms are proved bounds with
checkable hypotheses, the rest are named gaps; and every term depends on a resolution knob, through the spectral gap
at the chosen resolution and the scale (lag, bandwidth) at which the operator is built.** Finer resolution lowers
truncation error but is certifiable only where the spectrum has a gap, and the data needed grow as that gap
shrinks. Page 10 assembles this budget; every other page contributes one line of it through its ledger (section 4).
The budget is a **ledger** (for each term, the strongest available result with its hypotheses, or the gap where
none exists); a **certificate** is what a particular run earns by checking those hypotheses and evaluating the
bounds. Skim paths must keep the two apart (4.3).

### 1.2 Reader

A mechanistic-interpretability researcher. Assume fluency with linear algebra, the SVD, PCA, probability, gradient
training, transformers and sparse autoencoders. Assume **no** background in control theory, dynamical systems,
stochastic processes beyond Markov chains, spectral graph theory, or computational mechanics. Each page therefore
introduces its topic from scratch before drawing connections. A reader may arrive at any page first.

### 1.3 Thesis (the paragraph every page may quote or paraphrase)

> Much of what interpretability wants to know is carried by a map from what has happened to what happens next:
> from a text prefix to its continuations, from past inputs to future outputs, from where a point is now to where it
> goes, from a layer's activations to the next layer's. Each such map factors through a state, and its singular
> value decomposition ranks the state's directions by how much the map uses them, with a bound on what is lost when
> the rest are dropped. Realization theory, balanced truncation, Koopman and transfer-operator analysis, spectral
> clustering, computational mechanics, and models of sensory neurons each apply this construction to a particular
> map measured in a particular norm. The interpretive question becomes which map to decompose and how to weigh its
> two sides; each answer brings an error budget whose terms grow as the resolution is made finer. Neural coherent
> sets apply the same construction to the flow of data points through a network.

The user's own compression of the stance, which pages may quote with attribution to the programme's author (not as
the site's voice): "the only thing that is truly interpretable is an SVD, so we need to find the right SVD", because
the SVD is the way to say that one thing approximates another in an importance-sensitive way, with bounds.

### 1.4 The thesis diagram ("the bowtie")

One SVG, built once as a shared component (`js/lib/bowtie.js`, section 6.5) and reused with different labels on
every page and on the map.

- **Left fan:** many thin lines converging from a column of labelled items on the left ("pasts"). Generic label:
  *what has happened*. Page labels: prefixes (1), past inputs (2), points now / functions of the present (3),
  points at time 0 (4), points (graph vertices) (5), histories (6), delay windows of the input (7), histories /
  prefixes (9), functions of the inputs at layer ℓ′ (10).
- **Knot:** a small vertical stack of r bars of decreasing length (the singular values), labelled *state*,
  with a dial beside it labelled *r* (resolution). Bars beyond r are drawn faint and labelled *discarded*.
- **Right fan:** lines diverging to a column of items on the right ("futures"). Generic label: *what happens next*.
  Page labels: suffixes / continuations (1), future outputs (2), functions of the future (3), points at time T (4),
  points (5), future observations (6, 7), (continuation, next token) pairs (9), functions of the inputs at layer ℓ
  (10).
- **Under the knot:** a thin bar split into a solid part (kept) and a hatched part (lost), labelled with the page's
  bound (for example "lost ≤ 2 Σ_{j>r} σ_j" on page 2; "Z: ≤ 2ε/(1+ε); R: ≤ 2√2η/c (existence)" on page 5).
- **Above the fans:** the two norms the page uses to weigh pasts and futures (for example "probabilities, plain" on
  page 1; "Gramians" on page 2; "whitened covariances" on page 3; "degree / Sinkhorn" on page 4; "degree one
  (Sinkhorn)" on page 5; "uniform weight on every input (Sinkhorn)" on page 10).

The exact labels, bars and bound text of each page's bowtie are in that page's spec (its bowtie figure). **Page 8 has
no bowtie**: it supplies a mechanism (a learning rule's fixed points), not a past-to-future decomposition with a
truncation bound (its budget line is "—"); the map's hero shows page 8 without a knot (page 0 spec, 5.1).

The diagram's one message: every page that decomposes a map does so through an r-dimensional knot, and those pages
differ in which map and which weights. The map's skim path states the page-8 exception without requiring a click
(page 0 spec, 2 and 5.1).

---

## 2. Pages, claims, dependencies, connections

### 2.1 Page list

Tab ids are fixed (they are URL hashes and file names). "Depends on" lists *recommended* prior pages; every page must
still be readable alone (section 5.4 gives the "arriving here first" box).

| # | id | tab label | one-sentence claim | after this page the reader can | depends on |
|---|---|---|---|---|---|
| 0 | `map` | Map | Ten fields share one spectral framework: nine pages take the SVD of a past-to-future map, with a resolution knob and an error budget, and the Hebbian page shows a learning rule whose fixed points are spectral decompositions of their own. | Name, for each decomposing page, the map, the knob, and the bound, and for page 8 the mechanism; see the running example under every lens. | none |
| 1 | `hankel` | Hankel | Arranging a process's behaviour as a table of pasts by futures turns "find the hidden machine" into a rank problem; singular vectors are predictive states and truncation at r is optimal for the table, though not always a valid smaller machine. | Build a Hankel table, read its rank, realize a weighted automaton from it, place histories in predictive-state space, and state what rank-r truncation does and does not guarantee. | none |
| 2 | `control` | Linear control | For a linear input-output system the past-input-to-future-output map is a Hankel operator; balancing ranks states by how reachable and observable they are at once, and truncation loses at most twice the discarded singular values. | Compute Gramians and Hankel singular values, perform balanced truncation, and check the 2Σ-tail bound against the actual error; relate Ho-Kalman/ERA to page 1's realization. | 1 |
| 3 | `koopman` | Koopman | A nonlinear or noisy system acts linearly on functions of its state; looking for subspaces of functions the dynamics nearly closes gives finite linear models, and for stochastic systems the singular functions of that action are exactly past-future CCA. | Explain Koopman and transfer operators, delay embedding, EDMD, HAVOK and SINDy as different finite views; compute a VAMP/CCA decomposition and read coherent sets off it. | 1 (2 helps) |
| 4 | `cuts` | Spectral clustering | Finding sets with small boundary for their size (isoperimetry) is hard combinatorially but relaxes to an eigenproblem with two-sided Cheeger bounds; with dynamics, the same recipe gives coherent sets and, at small noise, the dynamic Laplacian. | Run spectral clustering and say what it optimizes; apply Cheeger and k-way Cheeger; state the general recipe (energy, cut, relaxation, bound); tell static from dynamic coherence; use eigengap/perturbation results. | 3 for the dynamic half |
| 5 | `sparsity` | Sparsity | Sparsity can be earned rather than imposed: spectral sparsifiers keep every cut and energy of a graph to within (1 ± ε) on O(n log n / ε²) edges, and SEBA turns an eigenspace into a few sparse set indicators under stated conditions. | Sample a sparsifier by effective resistance and check that the cuts survive; run SEBA and know when its output is guaranteed. | 4 |
| 6 | `compmech` | Comp. mechanics | Causal states are the exact classes of pasts with the same future; their coarse-graining analogues (the υ-machine and computational closure) say when a macro-variable is a self-contained state, and coherent sets are the approximate, spectral version. | Define causal states and the ε-machine, compare with Hankel rank, define υ-machines and closure, bound the error of treating a metastable partition as a Markov chain, and place the information bottleneck as one choice of energy. | 1, 4 |
| 7 | `neurons` | Neurons | A filter-and-rectify neuron whose filter is a past-future canonical direction reports membership of a coherent set of its input history; this is data-driven stochastic Koopman analysis in one cell. | Derive the neuron's filter from past-future CCA, see it detect coherent sets in a signal, and weigh the receptive-field evidence. | 3 (4 helps) |
| 8 | `hebbian` | Hebbian | On a resistor network, Hebbian learning with a pruning threshold produces clusters that are nonnegative eigenvectors of principal submatrices of the threshold-shifted covariance; the harmonic embedding is the natural coordinate for reading them. | Read a neuron's harmonic embedding, predict which parts a threshold allows, see refinement depend on history, and know what the weights do and do not reveal about the inputs. | 4, 7 |
| 9 | `logits` | LLMs from outside | A language model's extended logit matrix is a Hankel-like table; its rank is exactly the dimension of a time-varying input-switched affine network that reproduces the model; trained models' tables are approximately low rank, with structure that survives nonsense inputs (shared low-rank column spaces under nonsense continuations; generation from nonsense histories' logits). | Build an extended logit matrix, relate logit rank to ISAN dimension, distinguish it from probability-Hankel rank, and state what Golowich et al. showed and did not show. | 1 (6 helps) |
| 10 | `ncs` | LLMs from inside | Neural coherent sets decompose the flow of data points through a network's layers; the result is a candidate coarse-graining with an error budget of named terms (proved bounds where hypotheses hold, named gaps elsewhere), all of which scale with the resolution r. | Run NCS on a toy network, read real results (ViT, Mamba, Pythia, ResNet), read the budget as a ledger and as a run's certificates, and say what the budget does not cover. | 4, 5, 9 (3 helps) |
| R | `ref` | Reference | (Not a numbered page.) Notation, glossary, every page's ledger in one table, and the bibliography. | Look anything up. | none |

Kickers (in `index.html`): "Page N · <field>", e.g. "Page 1 · realization theory", "Page 4 · spectral graph theory",
"Page 6 · computational mechanics", "Page 10 · interpretability". The map's kicker is "Overview".

### 2.2 Connection matrix

Relation symbols (used in the matrix, on every page's connections strip, and on the map):

- `=` **identity or theorem-level equivalence** under stated hypotheses;
- `≈` **relaxation or approximation with a bound** (one object relaxes, estimates, or approximates the other, and a
  cited result controls the gap);
- `~` **schematic**: a motivating analogy or a link with no theorem behind it. All `~` links fall under the
  placeholder of section 8.

Each edge has an id (E1...) that per-page specs cite. A page's connections section must list every edge that touches
it, with the same symbol and wording core; it may add detail, not upgrade a symbol.

| id | pages | rel. | statement | bridge and citation |
|---|---|---|---|---|
| E1 | 1–2 | `=` | The process Hankel of a weighted automaton and the Hankel operator of a linear system are the same construction: the table factors as reachability × observability, its rank is the minimal state dimension, and shifted blocks recover the dynamics. For one-letter alphabets the two coincide literally. | Ho & Kalman 1966; Fliess 1974; Carlyle & Paz 1971; Balle et al. 2014 (forward-backward). |
| E2 | 1–2 | `≈` | Singular-value-automaton truncation is the automaton analogue of balanced truncation, with an ℓ² bound Σ_{i>r} σ_i²; optimal Hankel-norm (AAK) approximation is constructive for LTI systems and one-letter automata only. | Balle, Panangaden & Precup 2019, Thm 7.1; Glover 1984; Balle et al. 2021; Lacroce et al. 2023. |
| E3 | 1–3 | `=` | For a hidden Markov model, H[p,f] = α_p · β_f: α_p is the (unnormalized) state distribution after past p, propagated by the transfer operator; β_f(x) = P(f | x) is a function of state, propagated by the Koopman operator. The Hankel SVD is the SVD of "transfer then Koopman" restricted to words. | Balle et al. 2014; Jaeger 2000 (observable operator models). |
| E4 | 2–3 | `=` | For linear-Gaussian processes, past-future canonical correlation analysis yields a stochastic balanced realization; for general Markov processes, the whitened Koopman/transfer SVD is CCA of past and future features (VAMP), exactly in the limit of complete feature sets and as a Galerkin approximation for finite ones. | Akaike 1975; Desai & Pal 1984; Klus et al. 2018; Wu & Noé 2020. |
| E5 | 2–3 | `=` | For reversible diffusions (the running example), the fluctuation-dissipation theorem makes the linear-response kernel the time-derivative of an equilibrium correlation function, so page 2's response Hankel and page 3's correlation operator share their slow modes. | Kubo 1966; Risken 1989 (Fokker-Planck). |
| E6 | 3–4 | `=` | For reversible Langevin dynamics, the eigenfunctions of the generator are the large-sample limit of α = 1/2 diffusion-map (density-normalized graph Laplacian) eigenvectors built on equilibrium samples: static spectral clustering on samples recovers the slow dynamics. | Nadler, Lafon, Coifman & Kevrekidis 2006; Coifman & Lafon 2006. |
| E7 | 3–4 | `≈` | For non-autonomous or finite-time dynamics, coherent sets are leading singular vectors of a (noisy) transfer operator; as noise vanishes, the rescaled forward-backward composite converges to the dynamic Laplacian, whose eigenfunctions obey a dynamic Cheeger inequality. | Froyland 2013; Froyland 2015, Thm 5.1 (small-noise limit), Thm 3.2 (dynamic Cheeger), Cor 3.5 (multistep), for flat manifolds and volume-preserving maps; Froyland & Kwok 2017 (weighted manifolds, non-volume-preserving maps, which covers face C's contracting flow); Banisch & Koltai 2017, Thm 3 and Remark 4 (time-averaged graph walks on trajectory data converge to the forward-backward operator; data-driven dynamic Laplacian). |
| E8 | 4–5 | `≈` | A spectral sparsifier preserves every value of the Laplacian quadratic form to (1 ± ε), hence every cut weight and every Laplacian eigenvalue to that factor; conductances change by at most the extra ratio of degree factors unless the original degrees are kept (for a degree-one walk such as NCS's, the register's stochastic surrogate has cut/energy factors in [(1−ε)/(1+ε), 1]); eigenvectors follow when there is a gap. | Spielman & Srivastava 2011; Batson, Spielman & Srivastava 2012; CoherentModes `SPARSITY.md` S.2. |
| E9 | 4–5 | `≈` | SEBA rotates and soft-thresholds a leading eigenspace into sparse set indicators; recovery is exact from an aligned start in the exact-indicator regime and controlled near it, not guaranteed from arbitrary starts. | Froyland, Rock & Sakellariou 2019; Froyland & Rock 2025 (Props 3.8, 3.20); CoherentModes S.6-S.8. |
| E10 | 4/5–8 | `=` | The voltages of a resistor network with clamped inputs solve the graph Dirichlet problem: the harmonic embedding is harmonic label propagation; effective resistance (page 5) is the same Laplacian's pseudo-inverse. | Zhu, Ghahramani & Lafferty 2003; HebbianHarmonics `docs/note.md`; Stock et al. 2022 for a plasticity rule with this Laplacian. |
| E11 | 1–6 | `=` | Causal states are the classes of equal rows of the *conditional* Hankel table. Consequence: the ε-machine is a realization, so Hankel rank ≤ number of causal states, with strict inequality possible (finite rank, infinitely many causal states). | Shalizi & Crutchfield 2001; Haslinger, Klinkner & Shalizi 2010 (App. C); CoherentModes `THEOREMS.md` B.7-B.8. |
| E12 | 4–6 | `≈` | A metastable (coherent) partition is approximately lumpable: the induced chain reproduces the slow dynamics with an error controlled by how well the slow eigenfunctions are approximated by piecewise-constant functions and by the spectral gap; exact closure holds for exactly lumpable partitions such as modular random walks. | Sarich, Noé & Schütte 2010; Deuflhard & Weber 2005 (PCCA+); Rosas et al. 2024, §IV.4. |
| E13 | 3–6 | `~` | The past-future information bottleneck can be read as one choice of energy in page 4's recipe; no bound relates its merged states to a spectral truncation in general. Exact special cases, stated as such: it recovers the causal states as the compression penalty vanishes; for Gaussian processes its optimal projections lie along the CCA directions, with β-dependent scales and added noise (same directions, not the same compression). | Still, Crutchfield & Ellison 2010; Creutzig, Globerson & Tishby 2009; Chechik, Globerson, Tishby & Weiss 2005. |
| E14 | 3–7 | `≈` | For an Ornstein-Uhlenbeck process the leading nontrivial stochastic Koopman singular function is a linear projection (the full operator also has higher-degree Hermite modes; linear CCA recovers only the linear sector), so a filter-and-rectify neuron with a canonical filter encodes membership of the corresponding coherent sets; past-future CCA estimates the filter from data. Beyond OU this is an approximation. | Pughe-Sanford et al. 2025. |
| E15 | 7–8 | `~` | Local learning rules compute spectral objects, each exactly for its own rule: Hebbian/anti-Hebbian rules reach PCA and principal subspaces (proved under stated objectives); multicompartment networks whose feedforward rules their authors call non-Hebbian, with anti-Hebbian lateral weights, have the CCA solution as a proved fixed point (multichannel convergence shown numerically); the resistor-network v1 rule's fixed points are thresholded, nonnegative principal-submatrix eigenvectors. No bound relates the answers of these rules to one another. | Oja 1982; Pehlevan, Hu & Chklovskii 2015; Pehlevan et al. 2020; Lipshutz et al. 2021; HebbianHarmonics `docs/v1/findings.md`. |
| E16 | 1–9 | `=` | The extended logit matrix (histories × (continuation, next token), entries centred log-probabilities) is a Hankel-like table; its rank is at most d exactly when a time-varying ISAN of dimension d reproduces the model. Its rank is not the probability-Hankel rank (logs intervene). | Golowich, Liu & Shetty 2025, Thm 4.3; Foerster et al. 2017. |
| E17 | 9–10 | `~` | Outside view (logit rank, predictive states of the token process) and inside view (coherent sets of activations, kernel past-future CCA on activations) are two estimates of predictive structure; in idealized settings the inside scores span the beliefs, but a belief-sufficient layer can have infinite context rank. | CoherentModes `THEORY.md` §sequence contexts; `THEOREMS.md` A.47-A.48, B.2-B.9, B.12 (Mess3); Shai et al. 2024. |
| E18 | 4/5–10 | `=` | NCS operators are Sinkhorn-balanced kernel walks on data points; the block average I − M̄ is a finite-graph analogue of the dynamic Laplacian; NCS sets are SEBA readouts. Every bound of pages 4 and 5 applies with the hypotheses in `THEOREMS.md`/`SPARSITY.md`. | CoherentModes `THEORY.md`; `THEOREMS.md` A.1-A.7, A.21-A.27, A.43-A.44; `SPARSITY.md` S.2-S.8. |
| E19 | 3–10 | `~` | Depth plays the role of time: a residual layer x ↦ x + f(x) resembles one step of a flow, and data points moving through layers have transfer operators as page 3's dynamics do. Exact for face C, whose layers are by construction time-T/12 maps of a gradient flow; for general residual networks no bound ties layers to a flow (a residual map can fail to be injective, a flow map cannot). | CoherentModes `THEORY.md:109-136`; this site's face C (section 3.5). |
| E20 | 10–(Janiak) | `~` | Stable regions / activation plateaus (regions where the output barely changes, separated by sensitive boundaries) motivate coherent sets of data-point flow and harmonic label propagation as a relaxation; no theorem identifies the two. | Janiak et al. 2024; Heimersheim & Mendel 2024; Shinkle & Heimersheim 2025; CoherentModes `explore/cifar_coherent/site/content/overview.html:56-66`. |
| E21 | 6–10 | `~` | Coherent sets of data-point flow are candidate coarse-grained computational states; calling them states would require (approximate) closure, which has not been tested for networks. | Rosas et al. 2024 (closure definitions); CoherentModes `explore/cifar_coherent/site/content/overview.html:116-121` (analogy disclaimer). |
| E22 | 7–10 | `~` | "Neurons read coherent sets" and expansion coding motivate looking for structure among data points in activation space; they do not derive it. | Pughe-Sanford et al. 2025; the programme's "Slouching" post, part III. |
| E23 | 4–8 | `~` | Hebbian clustering and spectral clustering are both thresholded spectral computations on a similarity matrix; no theorem says generic Hebbian learning finds a chosen Laplacian partition. | HebbianHarmonics `site/content/method.html:13`; literature digest gap list. |

Pages with no direct edge between them (for example 2 and 9) are connected through the bowtie, not through a
claimed bridge; writers must not invent edges. A new edge needs an amendment to this table. An entry "4/5–x" (E10,
E18) is one edge touching three pages: pages 4, 5 and x all list it, and the map draws it as two lines sharing one
label.

---

## 3. The running example

### 3.1 Choice, and why

**A noisy particle in a nested four-well potential**, as the brief proposed, with three refinements: the potential
is two-dimensional and separable by default (so the nesting is exact and several quantities are known in closed form
or by product structure); the coarse readout has three symbols for four wells (so the hidden state is not the
current symbol, which is the whole point of page 1); and "depth as time" is made literal by a residual network whose
layers are steps of the particle's drift (face C), which also provides the genuinely non-reversible, finite-time
flow that pages 3, 4 and 10 need.

Considered and rejected: a 1-D four-well (pictures of graphs, sparsifiers and SEBA on a line are uninformative, and a
1-D chain makes the within-pair modes nearly degenerate with no product structure); a rotating potential (rigid
rotation is an isometry, so its dynamic Laplacian equals the static one and shows nothing); the double gyre
(standard for coherent sets but useless for pages 1, 2, 6, 8, 9; it may be mentioned in text on page 4).

The example has four **faces**. Every widget names the face it uses in its caption ("running example, face A").

### 3.2 Common definitions

State $x = (x_1, x_2) \in \Omega = [-2.2, 2.2] \times [-1.5, 1.5]$, reflecting boundary.

Potential (default $\kappa = 0$):
$$V_\kappa(x) = \big(h_x - \kappa\,x_2/b\big)(x_1^2 - 1)^2 + h_y\big((x_2/b)^2 - 1\big)^2,\qquad h_x = 2.5,\ h_y = 1.5,\ b = 0.6.$$

- Wells (minima, $V = 0$): $w_1 = (-1, -0.6)$, $w_2 = (-1, +0.6)$, $w_3 = (+1, -0.6)$, $w_4 = (+1, +0.6)$, **for every
  κ** (the κ term and its gradient vanish where $x_1 = \pm1$).
- **Pairs:** left $\{w_1, w_2\}$, right $\{w_3, w_4\}$. Within-pair saddles $(\pm 1, 0)$, height $h_y = 1.5$ (low
  barrier), for every κ. At κ = 0: between-pair saddles $(0, \pm 0.6)$, height $h_x = 2.5$ (high barrier); hilltop
  $(0,0)$, height 4. For κ > 0 the between-pair saddles stay on $x_1 = 0$ but move to $x_2 = b u_\pm$ with
  $u_\pm \approx \pm1 + \kappa/(8h_y)$, heights $\approx h_x \mp \kappa - \kappa^2/(16h_y)$ (κ = 0.3: $(0, 0.614)$ at
  2.196 and $(0, -0.584)$ at 2.796), and the hilltop moves to $(0, \approx -\kappa b/(4h_y))$ (κ = 0.3: $(0, -0.030)$,
  height 4.008); the builder computes them exactly (roots of $\partial_{x_2}V$ on $x_1 = 0$).
- **Basins** of the gradient flow at $\kappa = 0$: the four open quadrants $B_k$ (exact, because the flow
  decouples). For $\kappa \neq 0$ the builder computes basins numerically, on a grid with no node on a basin
  boundary (cell-centred, so no node lies on $x_1 = 0$), because ties broken by index create spurious asymmetries of
  order $10^{-5}$ in the four-state chain.
- $\kappa \in [0, 0.5]$ is the **asymmetry knob**, used only on pages 2 and 6 (and in advanced controls elsewhere): it
  lowers the between-pair barrier on the **upper** side ($x_2 > 0$) and raises it on the lower side, so the upper
  wells $w_2, w_4$ switch pairs more readily than the lower wells $w_1, w_3$: the rate of leaving a pair depends on
  which well of the pair the particle is in, and the pair label stops being exactly lumpable. (The previous knob,
  $(h_y + \kappa x_1)$ on the second term, kept the reflection $x_2 \mapsto -x_2$, which swaps the two wells of each
  pair and preserves the pair label; so it left the pair label exactly lumpable for every κ. Replaced in v1.2.) The
  new knob keeps the reflection $x_1 \mapsto -x_1$, so the up/down label stays exactly lumpable at every κ; pages
  may say so. Verified (grid spacing 0.05, cell-centred; the builder recomputes and asserts): pair-label
  lumpability defect $\max_{B,C}\max_{j,j'\in C}|T[j,B] - T[j',B]|$ = 0 (< 1e-13) at κ = 0, ≈ 0.0014, 0.0042,
  0.0075 at κ = 0.1, 0.3, 0.5; the hierarchy survives over the whole range (rates ν₂..ν₅ ≈ 0.031, 0.337, 0.368, 7.4 at
  κ = 0.3; 0.036, 0.336, 0.372, 6.8 at κ = 0.5); page 1's instrument ordering survives (depth-3 process Hankel
  σ ≈ 1.956, 0.697, 0.343, 0.0104 at κ = 0.3, directions still pair / right-pair wells / left-pair wells); the
  product mode's readout overlap $\langle x_1 + x_2, \phi_4\rangle_\pi$ is 0 at κ = 0 and ≈ 0.031 at κ = 0.3
  (page 2's "small but nonzero").

Dynamics (overdamped Langevin): $dX_t = -\nabla V(X_t)\,dt + \sqrt{2D}\,dW_t$, $D = 0.5$. Equilibrium density
$\pi(x) \propto e^{-V(x)/D}$.

Generator $\mathcal L f = -\nabla V\cdot\nabla f + D\Delta f$ (backward Kolmogorov); Koopman operator
$\mathcal K_\tau = e^{\tau\mathcal L}$; relaxation rates $0 = \nu_1 < \nu_2 \le \dots$ with
$\mathcal K_\tau \phi_i = e^{-\nu_i\tau}\phi_i$.

**Expected spectrum** (from 1-D computations at these parameters; the builder recomputes in 2-D and asserts):
$\nu \approx 0,\ 0.028,\ 0.336,\ 0.364,\ 8.2,\dots$ The four slow functions at $\kappa = 0$ are $1$,
$\phi^x_2(x_1)$ (≈ sign $x_1$: which pair), $\phi^y_2(x_2)$ (≈ sign $x_2$: which well within the pair), and their
product. Time scales: pair switching ≈ 36, within-pair hopping ≈ 3, relaxation inside a well ≈ 0.12. Separation ratios
$\nu_2/\nu_3 \approx 0.08$, $\nu_4/\nu_5 \approx 0.04$.

This is the source of the site's "r = 2, then r = 4" for **operators on position space** (Koopman, transfer, graphs,
flows; pages 2-5, 7, 8, 10): **r = 2 keeps the pair, r = 4 keeps the well, and everything beyond is detail inside a
well.** Which of the two blocks is *well separated* depends on the lag, and this is the example's resolution knob:
at $\tau = \Delta = 0.25$, $\lambda_i = e^{-\nu_i\tau} \approx 1,\ 0.993,\ 0.920,\ 0.913,\ 0.13$, so the gap after 4
(≈ 0.78) is far larger than the gap after 2 (≈ 0.07); at $\tau = 4$, $\lambda \approx 1,\ 0.89,\ 0.26,\ 0.23,\ 0$,
and the gap after 2 (≈ 0.63) dominates. Short lags certify the wells; long lags certify only the pairs. Gaps are not
monotone in r; no page may say they are.

The count includes the constant mode and the product mode. **Exception, page 2 (face B):** the linear response removes
the mass (constant) mode and its product mode has zero residue (section 3.4), so on page 2 r = 2 already keeps both
visible slow directions (left/right and up/down) and there is no slow third state; page 2 says so. Its balanced states
are input-output channels that mix generator modes (the builder reports the loadings), not the modes themselves.

Tables built from the *instrument* (pages 1, 6, 9) have their own ordering, set by what the instrument sees, not by
the generator. The builder computes it and pages quote the computed ordering (expected values below).

Sampling interval for discrete-time processes: $\Delta = 0.25$. Lag $\tau$ is a control on pages 3 and 4 (default
$\tau = \Delta$).

Readout (the "coarse noisy instrument"): $y = x_1 + x_2 + \xi$, $\xi \sim N(0, \sigma_y^2)$ independent per sample,
$\sigma_y = 0.25$. Symbol $s \in \mathcal A = \{\texttt a, \texttt b, \texttt c\}$ from **unevenly placed bins**:
`a` if $y < 0$, `b` if $0 \le y \le 1$, `c` if $y > 1$. Noise-free readouts at the wells: $w_1 \to -1.6$ (`a`),
$w_2 \to -0.4$ (`a`), $w_3 \to +0.4$ (`b`), $w_4 \to +1.6$ (`c`). Expected emission probabilities (four-state chain,
from 1-D computations): $w_1$: a 1.00; $w_2$: a 0.88, b 0.12; $w_3$: a 0.12, b 0.84, c 0.04; $w_4$: b 0.08, c 0.92.
**The two wells of the left pair share the symbol `a`**: the instrument sees the pair and sees the right pair's two
wells, but barely tells the left pair's wells apart ($w_2$ occasionally reads `b`, and the two wells lead toward
different right-hand wells), so the table separates them only faintly.

Expected instrument-table spectra (four-state chain; the builder recomputes and asserts the ordering):
- process Hankel, words ≤ 3: $\sigma \approx 1.99,\ 0.69,\ 0.35,\ 0.008$, rank 4. Direction 2 separates the pairs,
  direction 3 separates $w_3$ from $w_4$, direction 4 separates $w_1$ from $w_2$;
- infinite process Hankel (automaton Gramians): $\sigma \approx 5.93,\ 1.27,\ 0.57,\ 0.14$;
- whitened (canonical correlations of past and future windows of length 3): $1,\ 0.93,\ 0.74,\ 0.11$, same order of
  directions.

So the instrument tables also give "r = 2 keeps the pair"; their r = 3 adds the right pair's wells and r = 4 the left
pair's. The rejected alternative (bins at ±1, sharing `b` between $w_2$ and $w_3$) ranks "is it `b`" above "which
pair", which is a fine lesson on its own but breaks the site's nesting; it is recorded here so nobody reintroduces
it by accident.

### 3.3 Face A and A′: the particle and the four-state chain

- **Face A, the particle.** The stationary process above, observed as the scalar signal $y_t$ (pages 3, 7, 8) or the
  symbol stream $s_t$ (pages 1, 6, 9), at interval $\Delta$; or as 2-D positions (pages 3, 4, 5).
- **Face A′, the four-state chain.** The Markov state model on the basins: $T_\Delta[j,k] = P_\pi(X_\Delta \in B_k
  \mid X_0 \in B_j)$, emissions $E[k, s] = P_\pi(s \mid X \in B_k)$ (integrating position within the basin and the
  readout noise). This is an HMM with four hidden states and three symbols. At $\kappa = 0$,
  $T_\Delta = T^{x}_\Delta \otimes T^{y}_\Delta$ exactly (product of two 2-state chains; the builder asserts this to
  1e-10). It is an idealization of face A: it forgets where in a basin the particle is. Pages say so.

### 3.4 Face B: the response (page 2)

The ensemble's linear response to a small uniform force $u(t)$ along $d = (1,1)/\sqrt2$ (drift becomes
$-\nabla V + u\,d$), with output $z(t) = \mathbb E[x_1 + x_2]$ (no readout noise). Linearizing the Fokker-Planck
equation about $\pi$ gives an LTI system whose state is the density deviation:
$\dot\rho = \mathcal L^*\rho + u\,B$, $B = -\nabla\cdot(\pi d)$ (the input operator, written B as in $(A, B, C)$;
not the potential's width b = 0.6), $z = \langle x_1 + x_2, \rho\rangle$, with the mass mode removed (it is
uncontrollable). Discretized on the builder's grid and reduced by exact modal truncation to
K = 60 slow modes (assert: the neglected modes change the H∞ norm by < 1e-4). **This 60-mode model is not minimal**:
removing the mass mode is not enough. In modal coordinates A is diagonal with distinct rates, so mode k is
controllable iff $B_k \neq 0$ and observable iff $C_k \neq 0$, and fluctuation-dissipation gives
$B_k = \frac{\nu_k}{D\sqrt2}C_k$ (both vanish together). At κ = 0, separability and parity make exactly **9 of the 60**
nonconstant modes visible (verified at grid spacings 0.05 and 0.005); the other 51 have $B_k = C_k = 0$ exactly. So
the full Gramians are singular and balancing cannot be applied to the 60-mode realization. The builder therefore
(i) keeps the full 60-mode model for density playback and modal-truncation comparisons, and (ii) **extracts a
minimal realization before balancing**: the modes with $|C_k| > 10^{-10}\max_j|C_j|$ (Kalman decomposition, trivial
here because A is diagonal), recording the count and the tolerance and distinguishing modes invisible by symmetry
(exactly zero overlap) from small positive Hankel singular values. At κ = 0.3 symmetry no longer forces zeros
(every mode is visible), but many weights are tiny; the builder balances on the modes above the same tolerance and
reports the numerical rank. Expected positive Hankel singular values at κ = 0 (two independent checks):
$\sigma \approx 0.7205,\ 0.1414,\ 0.0259,\ 0.00093$, so $\sigma_3/\sigma_2 \approx 0.18$. Builder computes, **in
full for both κ = 0 and κ = 0.3**, on the minimal realization: Gramians, Hankel singular values, balancing
transformations, balanced truncations for r = 1..8 (or up to the minimal order, if smaller), their H∞ errors (and
those of modal truncation on the full model), and the product-mode residue; frequency and step responses are
computed live from the stored matrices (page 2 spec, section 6). Because $B_k/C_k = \nu_k/(D\sqrt2)$ varies with k,
the modal realization is **not** state-space symmetric; rescaling mode k by $(D\sqrt2/\nu_k)^{1/2}$ makes $B = C^\top$
with A unchanged and diagonal, and in those coordinates the two Gramians are equal (page 2, 3.6).

**Strain, stated on page 2:** by separability, the input and output act on $x_1$ and $x_2$ separately, so the product
mode (which tells $w_1, w_4$ from $w_2, w_3$) has zero residue: **linear response sees two slow states, not three**;
the four-well partition needs a nonlinear readout (page 1's symbols) to show its fourth set. The builder asserts the
product-mode residue < 1e-8 at $\kappa = 0$; with $\kappa > 0$ it becomes small but nonzero (the knob of 3.2 breaks
the $x_2$-reflection that made it vanish; expected overlap ≈ 0.031 at κ = 0.3). Also: the LTI system describes the
ensemble average, not a single noisy trajectory.

**Warm-up companion (pages 2 and 7):** the local Ornstein-Uhlenbeck linearization at $w_4$:
$A = -\nabla^2 V(w_4) = -\mathrm{diag}(8h_x, 8h_y/b^2) = -\mathrm{diag}(20, 33.\overline3)$, $B = d$,
$C = (1, 1)$, noise $\sqrt{2D}$. Two states; Gramians in closed form. This is also Pughe-Sanford et al.'s analytic
case (page 7).

### 3.5 Face C: the flow, a toy residual network (pages 3, 4, 10)

- Inputs: $N = 1000$ points $x^{(0)}$ uniform on $\Omega_{\rm in} = [-1.4, 2.6] \times [-1.0, 1.4]$ (seed 0; N is
  a control on page 10, range 250-1000 live, to keep within the 1 s budget of 6.7; larger N only through the builder's
  precomputed reference). **The box is deliberately not symmetric about the basin boundaries** $x_1 = 0$, $x_2 = 0$:
  on a symmetric box such as $[-2,2]\times[-1.2,1.2]$ the uniform cloud's own leading graph modes are ≈ sign $x_1$,
  sign $x_2$ and their product, so static clustering of layer 0 would reproduce the quadrants (the basins) by
  coincidence (page 4 spec, section 6). The flow is defined on all of $\mathbb R^2$; inputs with $x_1 > 2.2$ lie
  outside Ω and are drawn as such.
- Layers $\ell = 1, \dots, 12$: $x^{(\ell)} = \Phi_{T/12}(x^{(\ell-1)}) + \sqrt{2D_{\rm flow}T/12}\,\zeta_\ell$,
  where $\Phi_t$ is the time-$t$ flow of $\dot x = -\nabla V(x)$ (RK4, ≥ 8 substeps per layer), $T = 0.3$,
  $D_{\rm flow} = 0$ by default (control: 0 to 0.05, Froyland's small-diffusion regime).
- Each layer is a residual block $x \mapsto x + f(x)$ with $f = \Phi_{T/12} - \mathrm{id}$. **This is a real (tiny)
  residual network**, not an analogy; the analogy is only in claiming LLM layers behave similarly.
- **Lift** (page 10 only; **on by default there**, raw positions an advanced option): activations $a^{(\ell)} =
  \tanh(W_{\rm lift} x^{(\ell)} + c_{\rm lift})$, $W_{\rm lift} \in \mathbb R^{64\times2}$ with entries $N(0,
  1.5^2)$, $c_{\rm lift} \sim U(-1, 1)$ entrywise, seed 7, then centred and row-normalized, so NCS runs on 64-wide
  normalized activations as in a network. **Centring differs by construction.** The implemented construction (`kNN`)
  centres by the mean over the current probe set, as on real networks. The theory construction (`sphere`) centres by
  a stored vector $m_\ell$: a **fixed quadrature estimate of the population mean** of the lifted activations at
  layer ℓ, computed once by the builder (midpoint quadrature on a 400 × 240 grid of the input box pushed through the
  noise-free flow; `p10.json` `faceC.popmean`), so that each normalized view $\hat\phi_\ell(x) = (a^{(\ell)}(x) -
  m_\ell)/\|a^{(\ell)}(x) - m_\ell\|$ is a fixed function of the input, fixed before any sites are drawn, and the
  i.i.d. inputs give i.i.d. views as A.40-A.44 require. The population target $P_{\star,\rm ref}$ (4.3) is defined
  with this same stored vector, so the quadrature error never enters a bound; it only means that "population-centred"
  is centring by an estimate of the population mean, not by the exact mean. Probe centring would make every row depend on all N inputs and change the feature map with N. Reason for
  the lift default: the register's sampling and view results (A.24-A.25, A.40-A.44) need normalized views, and
  normalizing raw 2-D positions would keep only their angle. (Subscripts keep $W$ for edge weights and $c$ for S.8's
  margin.)
- **The face C graph (binding for pages 3, 4 and 10):** the implemented NCS construction. At each layer ℓ = 0..12,
  on the layer's representation (2-D positions with Euclidean distance on pages 3 and 4; on page 10 the lifted
  activations with cosine distance by default), the union of the directed $k_{\rm nn} = 15$ nearest-neighbour graphs
  with weight 1 on its edges and a floor $10^{-6}$ on every other off-diagonal pair, diagonal 0 (the floor makes
  Sinkhorn scaling exist and unique: a symmetric matrix with positive off-diagonal entries and zero diagonal has
  total support and is fully indecomposable for N ≥ 3, since every off-diagonal position lies on a derangement;
  Sinkhorn & Knopp 1967, with the symmetric scaling by Csima & Datta 1972. Register A.1 and A.23 do **not** cover
  it: both assume strictly positive entries, and A.1's alternative needs a positive diagonal. The floor is stored as
  a rank-one-plus-diagonal correction, never as a dense matrix); symmetric
  Sinkhorn balancing to a doubly stochastic $P^{(\ell)}$; fixed-lazy $M^{(\ell)} = (I + P^{(\ell)})/2$; the dynamic
  operator is the block average $\bar M = \frac1{13}\sum_{\ell=0}^{12} M^{(\ell)}$; ordered products use the
  $P^{(\ell)}$ (page 3's $Q_\ell = P^{(\ell)}P^{(0)}$). The theory construction of the register (dense sphere kernel,
  products) is page 10's advanced option `sphere β_ref`. A page that changes $k_{\rm nn}$ or the block does so only as
  an advanced control and labels it.
- Ground truth: the basin of each input (quadrant at $\kappa = 0$). Points within the "uncommitted band"
  ($|x^{(12)}_1| < 0.5$ or $|x^{(12)}_2| < 0.3$) have not yet fallen into a well by the last layer; they are the
  toy's sensitive boundary, the analogue of a plateau boundary.
- What it shows: three operators on the same tracked inputs answer three different questions. Layer 0's walk asks
  which inputs **start** close (initial geometry: a uniform cloud, whose sets follow the box's shape); layer 12's
  walk asks which inputs **end** close (final geometry: four tight clumps, which on this toy are the basins, because
  the flow ends in wells); the layer-averaged walk $\bar M$ asks which inputs **stay** close across the block
  (neighbourhood persistence: a set is cheap for $\bar M$ when its boundary is cheap at every layer on average, since
  a set's conductance under $\bar M$ is the mean of its per-layer conductances; for a labelling's **worst** set only
  an inequality holds, $\max_j \phi_{\bar M}(A_j) \le \frac1{13}\sum_\ell \max_j \phi_{M^{(\ell)}}(A_j)$, because the
  maximum over sets does not commute with the average). Because the inputs are tracked, any
  labelling can be drawn at every layer; in particular layer 12's labels drawn at layer 0 do show where each input
  ends, so the toy does **not** show that only the average recovers origins, and no page may say so. What the pages
  show instead, for each of the three labellings: its per-layer boundary cost (conductance under each $M^{(\ell)}$),
  its block cost (conductance under $\bar M$), and its matched Jaccard with the basins, all computed by the builder,
  with no ordering asserted in advance (an independent check on the lifted kNN construction found matched Jaccard
  ≈ 0.74, 0.91, 0.87 for layer 0, layer 12 and the average, so the final layer can match the basins better). The
  real-network contrast between one layer and a block is the programme's ResNet-20 comparison (page 10, 3.2).
  Whether pairs or wells are the well-separated block depends on the bandwidth; the builder and the live widget
  compute face C's actual gaps. (THEOREMS B.33's closed-form two-level hierarchy does **not** apply to face C: it
  assumes replicated identical sites and equal prototype inner products. Page 10 uses it only through the labelled
  ideal companion of section 3.8.)

### 3.6 Precomputed versus live

Python reference builder `tools/build_example.py` (NumPy/SciPy, run with `uv run --with numpy --with scipy`) writes
`site/data/example/*.json`; each file carries its full config and the builder's assertions. A JS port of the
example (`site/js/lib/example.js`) runs the live parts; parity tests compare the two (section 6.7).

| quantity | where | notes |
|---|---|---|
| Grid generator (square-root approximation of rates, spacing ≤ 0.05), its first 100 eigenpairs, π | precomputed | `example/grid.json` (eigenvalues, eigenfunctions subsampled to a 88×60 display grid as Float32 base64). Assert rates converge to 3 s.f. under halving spacing. |
| Four-state chain T_Δ, E, stationary distribution | precomputed (also re-derivable live from 1-D chains) | `example/chain.json` |
| Process Hankel blocks (words ≤ 3) for chain and particle; infinite-Hankel singular values via automaton Gramians | precomputed | particle via a 60-mode spectral WFA (error ≤ e^{−ν_61 Δ}, asserted < 1e-8) |
| Sampled symbol streams / Hankels for the particle at N ∈ {10³,10⁴,10⁵,10⁶}, 3 seeds | precomputed | pooled stationary chains, Euler-Maruyama dt = 0.0025 |
| Sampled streams for the chain | live | seeded RNG; 10⁶ symbols in < 100 ms |
| Particle trajectories for animation (a few particles) | live | Euler-Maruyama, seeded; matches builder's integrator |
| Equilibrium samples (N up to 2000) for graphs | precomputed (seeded sets) | `example/samples.json` |
| kNN / kernel graphs on ≤ 2000 points, Laplacian eigenvectors (k ≤ 12), Cheeger sweeps, effective resistances, sparsifier sampling, SEBA | live | Lanczos / subspace iteration; < 500 ms at N = 1000 |
| Linear-response system (face B), for κ = 0 **and** κ = 0.3: full 60-mode modal (A,B,C); the minimal realization (visible modes, count, tolerance); on it, Gramians, Hankel SVs, balancing transformation, balanced truncations r = 1..8 with H∞ errors; modal truncations of the full model; product-mode residue | precomputed | `example/response.json` (keys per κ; page 2 spec, section 6) |
| OU warm-up Gramians | live | closed form |
| Face C flow: layers for N ≤ 2000 | live | RK4; ≈ 30 ms |
| Face C numerical reference (N = 8000): eigenvalues and gaps, basin labels; the stored quadrature estimates $m_\ell$ of the lift's population mean per layer | precomputed | a numerical reference, not population truth; drawn with its own seed (1), independent of the live inputs (seed 0), so that choices made on it ($\beta_{\rm ref}$) are fixed relative to the live sites; compared with live runs only through eigenvalues (comparable across N) and basin labels, never through raw eigenvectors |
| B.33 ideal companion: eigenvalues vs β | live (closed form) | section 3.8 |
| Delay-window covariances / CCA for the signal y (window ≤ 32) | live from a precomputed long signal | `example/signal.json`: 10⁵ samples of y (Float32) **and the true basin label of each sample** (uint8, quadrant at κ = 0; same seed and integrator), so pages 3 and 7 can score agreement with pair, within-pair, outer/inner and well labels |
| Place-field features and their (time-filtered) covariances Σ_g(τ_s) for page 8 | precomputed | `hebbian/p08.json`; τ_s ∈ {0, 0.5, 2, 8, 32}; field layout (16 Gaussian fields on a 4 × 4 grid, centred and scaled) and the separable 1-D-spectral method with its cross-checks are **binding as written in the page 8 spec, section 6** |
| Extended logit matrix of the exact predictor (page 9) | chain live; particle from precomputed word probabilities | `logits/p09.json`: the particle's word probabilities for all words ≤ 8 (from the 60-mode spectral WFA), time-indexed tables up to length T = 5 for both models, and the derived spectra and KLs (page 9 spec, section 6) |
| Page-specific builder outputs | precomputed | `site/data/<id>/pNN.json` (`hankel/p01.json` … `ncs/p10.json`), each written by `tools/build_example.py` with config and assertions **exactly as the page's spec lists them in its section 6**; the example owner implements them, the page spec defines them |

### 3.7 Per-page use, strain, and companions

| page | face | what the example shows | where it strains | companion used alongside |
|---|---|---|---|---|
| 0 map | all | one thumbnail per lens | — | — |
| 1 hankel | A′, A (symbols) | rank 4 from 3 symbols; spectrum ordered pair, right-pair wells, left-pair wells (the last only through history); predictive states lie inside a tetrahedral envelope (belief simplex); the particle resolves more than four dimensions | A′ is an idealization; the instrument, not the generator, sets the table's ordering | crw-blog Hankel widget's processes (Golden Mean, Zero-One-Random, Mess3) as alternative models |
| 2 control | B, OU | two slow Hankel singular values + intra-well tail; balanced truncation to r = 2, which already keeps both visible slow axes (3.2's exception); balanced states are mixtures of modes (builder loadings) | linear response is blind to the product mode; ensemble, not trajectory | OU warm-up (2 states) |
| 3 koopman | A (positions, y), C | Koopman eigenfunctions = pair, well, product; σ_i = e^{−ν_i τ}; lag as resolution knob; EDMD/VAMP from trajectories; SINDy, given drift estimates from short-time increments, recovers the cubic drift's few nonzero coefficients (accuracy depends on data and is shown); delay embedding of y | reversible, so singular = eigen and transfer ≈ Koopman; HAVOK forcing less vivid than Lorenz | face C for a genuinely non-normal (finite-time) SVD; Lorenz/HAVOK described with link to Brunton et al. |
| 4 cuts | A (equilibrium samples; the grid generator's eigenfunctions as reference), C | Cheeger cut = central barrier (k = 2), then the within-pair barriers (k = 4); diffusion maps (α = 1/2) on samples recover generator eigenfunctions; dynamic vs static on face C | face A is reversible: its coherence is metastability | face C for transport-coherence; double gyre named in text |
| 5 sparsity | A (dense Gaussian kernel graph on N = 600 samples; kNN truncation only as the uncertified contrast) | resistance sampling protects every bottleneck collectively: the leverages of the edges crossing any cut sum to at least 1, so each barrier receives samples and its few surviving edges are reweighted heavily; individual crossing edges of the dense graph have tiny weights and mostly small leverages, and most are dropped (an independent check: mean leverage ≈ 0.0002 for crossing edges against ≈ 0.006 overall); SEBA yields four well indicators (two at r = 2) | at N = 600 the edge savings are modest; the graph has no single bridges | planted SEBA examples of register S.7 |
| 6 compmech | A′, A (symbols), κ | noiseless well readout: 4 causal states = rank 4; the instrument: rank 4 but infinitely many causal states (proof in `pages/01-hankel.md` 3.3: the symbol matrices are strictly positive and invertible, so a finite set of causal beliefs would be permuted by a contraction; hypotheses checked by the builder); the hero's rising count is of distinct finite-history predictive distributions, not of causal states; pair label exactly lumpable at κ = 0 (closed, υ = ε), not for κ > 0 (3.2's knob), approximately for the particle | the IB / Markov-blanket links are not exercised numerically | Golden Mean and Even processes (small exact ε-machines); Mess3 (fractal mixed states); Rosas et al.'s modular random walk |
| 7 neurons | A (signal y), OU | CCA filters of delay windows: the pair from linear windows of y; the outer/inner split from ON/OFF rectified channels; the well from the two signs together; at long lags only the pair | stochastic, so Takens' theorem does not literally apply; y = x₁ + x₂ makes the within-pair split invisible to linear filters; reversible, so no predictive/retrospective dichotomy | OU warm-up (Pughe-Sanford's analytic case); their receptive-field evidence described, not reproduced |
| 8 hebbian | A (place-field features) | place fields (page 8 spec, section 6); without a trace the parts are wells (never pairs); with a slow synaptic trace (τ_s = 8) pairs at low threshold and wells at higher threshold; refinement depends on history | static covariance mostly sees wells; pair structure needs the trace (a modelling choice, labelled) | HebbianHarmonics block-covariance examples (`#old`) if the builder's checks fail |
| 9 logits | A (symbol process as a "language") | exact predictor's extended logit matrix; logit rank vs probability-Hankel rank; ISAN of dimension d from a rank-d factorization; nonsense histories | tiny alphabet, no learned model | Golowich et al.'s results on real LMs (described with numbers, linked) |
| 10 ncs | C (lift on by default) | live NCS on the toy residual network; start, end and persistence labellings compared by per-layer and block boundary cost (no winner asserted); the budget as a ledger and as the certificates a live run earns, with actual errors | contractive 2-D flow ending in wells, so the last layer already sorts inputs by basin; LLM layers are not gradient flows | real NCS results: DINOv2 ViT-S/14, Mamba-130m, Pythia-160m, ResNet-20/CIFAR-10 (precomputed figures and facts), including ResNet-20's one-layer-against-block comparison |

### 3.8 The ideal companion for page 10 (THEOREMS B.33)

A labelled synthetic dataset, not the running example: G = 2 coarse groups ("pairs") × $b_f$ = 2 fine clusters
("wells") × n identical normalized sites per cluster, prototypes $\sqrt{1-d_c}\,e_0 + \sqrt{d_c - d_f}\,e_g
+ \sqrt{d_f}\,e_{g,j}$ with $d_f = 0.2$, $d_c = 0.9$ (defaults; sliders on page 10). The register writes δ and Δ for
$d_f$ and $d_c$; the site renames them because δ is the spectral gap and Δ the sampling interval. B.33
(`THEOREMS.md:2650-2663`) gives the walk's eigenvalues exactly: $1$; $\lambda_c = 1 - Gb_fz_c/Z$ (G − 1 times);
$\lambda_f = (1 - z_f)/Z$ (G($b_f$ − 1) times); 0 otherwise, with $z_f = e^{-\beta d_f}$, $z_c = e^{-\beta d_c}$,
$Z = 1 + (b_f-1)z_f + b_f(G-1)z_c$. Page 10 plots the gap after the coarse block and after the fine block against β,
to show exactly how the bandwidth decides which resolution is certifiable. Pages may not summarize the coarse gap
as simply closing with β: at the defaults the coarse gap $\lambda_c - \lambda_f$ opens
(0.03 at β = 0.1, 0.31 at β = 1), peaks (≈ 0.575 near β ≈ 3.3) and then closes (0.17 at β = 12, 0.04 at β = 20),
while the fine gap $\lambda_f$ keeps opening (0.005 at β = 0.1, 0.83 at β = 12). Every figure using it carries the tag
"ideal companion (B.33), not the running example".

---

## 4. The ledger, and the page-10 error budget

### 4.1 Ledger format

Every page ends with a ledger box (component `ui.ledger`, section 6.5). Seven rows, always in this order, each one or
two sentences on the page (the per-page spec may be longer):

| row | content |
|---|---|
| **Decomposed** | The table or operator, as a map from what to what, and the weights on each side. |
| **Knob** | The resolution r, and the continuous scale that moves it (lag τ, bandwidth β, threshold θ, horizon, ε). |
| **Discarded at r** | What the rank-r description throws away, in words. |
| **Bound** | The bound on what is lost, its hypotheses, its source, and a status tag: `theorem`, `theorem (scope-limited)`, `conditional` (holds under checkable assumptions), `standard` (textbook, cited), `none`. |
| **From data** | The finite-sample or perturbation counterpart, if any. |
| **Running example** | The numbers on the example (filled from builder output; never typed by hand). |
| **Budget line** | Which page-10 term this supplies: **T** truncation, **S** sampling/estimation, **P** perturbation, **Z** sparsification, **R** rounding, **I** interpretation (unbounded), or "—". |

The Reference tab collects all ledgers into one table. Status tags here are not the claim-status scheme of section 8;
they only say what kind of bound sits in the row.

### 4.2 Drafted ledgers

Bracketed items `[builder: …]` name a number the builder must compute and the page must display. Each page spec's
section 8 refines its draft below; the two must not contradict (PAGE_TEMPLATE section 8).

**Page 0, map: the generic ledger.** Titled "How to read every page's ledger"; it doubles as the legend for the seven
rows and the budget letters.
- Decomposed: a map from what has happened to what happens next (a table, an operator, a walk), and the weights put
  on each side; the decomposing pages differ mainly here. Page 8 decomposes nothing: its row names the learning rule
  whose fixed points are spectral objects (a mechanism, budget line "—").
- Knob: the resolution r (states, modes or sets kept), and the continuous scale that moves it: lag, bandwidth,
  threshold, horizon or ε.
- Discarded: what the rank-r description cannot distinguish; in the running example, at r = 2 which well within a
  pair, at r = 4 where inside a well.
- Bound: the guarantee on what is lost, its hypotheses, its source and a status tag; for a plain SVD, Eckart-Young.
- From data: estimated singular values move by at most the error's norm (Weyl), subspaces by error over gap
  (Davis-Kahan, Wedin).
- Running example: $[builder$: the gap after 2 and after 4 at τ = 0.25 and τ = 4, from `grid.json`$]$.
- Budget line: the legend of the letters T S P Z R I and "—".

**Page 1, Hankel.**
- Decomposed: the process Hankel $H[p,f] = P(pf)$, prefixes × suffixes (finite block: words of length ≤ 3;
  infinite: all words). Plain probabilities on both sides.
- Knob: rank r; also block depth and sample size.
- Discarded: distinctions between pasts that change future-word probabilities only by the small singular values.
- Bound: finite block, Eckart-Young: $\|H - H_r\|_2 = \sigma_{r+1}$, $\|H - H_r\|_F^2 = \sum_{i>r}\sigma_i^2$, optimal
  over all rank-r matrices (`theorem`; but $H_r$ need not be a Hankel matrix of any process). Realizable truncation:
  singular value automaton, $\|f - \hat f_r\|^2_{\ell^2(\mathcal A^*)} \le \sum_{i>r}\sigma_i(H_f)^2$ for a minimal
  automaton computing a square-summable f (Balle, Panangaden & Precup 2019, Thm 7.1; `theorem`). Optimal
  Hankel-norm (AAK) approximation: `theorem (scope-limited)`, one-letter alphabets only.
- From data: $|\hat\sigma_i - \sigma_i| \le \|\hat H - H\|_2$ (Weyl); subspace angle $\le \|\hat H - H\|/\text{gap}$
  (Wedin); Hsu, Kakade & Zhang 2012 for HMM learning under conditioning assumptions.
- Running example: chain: rank 4, $\sigma_5 = 0$, ordering pair / right wells / left wells (expected
  1.99, 0.69, 0.35, 0.008 at depth 3); $[builder$: the same for the particle and its $\sigma_5..\sigma_8$; ℓ² error
  and SVA bound at r = 2, 4; negative mass at the `negative` tour; the N at which σ₃ and σ₄ clear the sampling
  floor$]$.
- Budget line: T, S.

**Page 2, linear control.**
- Decomposed: the Hankel operator $\Gamma$: past inputs ↦ future outputs, $\Gamma = \mathcal O\mathcal C$;
  weights: input and output energy ($L^2$); $\sigma_i = \sqrt{\lambda_i(W_c W_o)}$.
- Knob: number of retained balanced states r.
- Discarded: states that are both hard to excite and hard to see.
- Bound: $\sigma_{r+1} \le \|G - G_r^{\rm BT}\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$ (distinct values; stable minimal
  system, $\sigma_r > \sigma_{r+1}$, so balancing is applied to a minimal realization extracted first (3.4);
  balancing Moore 1981; stability of the truncation Pernebo & Silverman 1982; the
  upper bound Enns 1984 and Glover 1984; `theorem`). The lower bound holds for every order-r model. Optimal
  Hankel-norm approximation attains $\sigma_{r+1}$ (AAK, Glover 1984; `theorem`). Glover's $L_\infty$ tail bound for
  Hankel-norm approximants is quoted only after its exact statement has been checked in the paper (page 2 spec,
  3.4); otherwise omitted.
- From data: Ho-Kalman/ERA from a finite block of impulse responses; Weyl and Wedin for noisy blocks; non-asymptotic
  identification from one trajectory (Oymak & Ozay 2019) — `conditional`.
- Running example: $[builder$: number of visible modes (minimal order) and its tolerance; Hankel singular values;
  $\|G - G_2\|_{H_\infty}$ vs $\sigma_3$ and $2\sum_{j>2}\sigma_j$;
  product-mode residue at κ = 0 and κ = 0.3; loadings of the balanced states on generator modes; ERA-recovered slow
  rates and noise floors$]$.
- Budget line: T.

**Page 3, Koopman.**
- Decomposed: the stochastic Koopman operator $\mathcal K_\tau: L^2(\pi_\tau) \to L^2(\pi_0)$ ($\pi_0, \pi_\tau$ the
  state's distributions at times 0 and τ; both π at equilibrium), $(\mathcal K_\tau f)(x)
  = \mathbb E[f(X_\tau) \mid X_0 = x]$, whitened on both sides (VAMP); equivalently CCA between functions of the
  present and of the future. For reversible dynamics, eigen = singular.
- Knob: r and lag τ (diffusion time); dictionary size for EDMD.
- Discarded: functions of state that decorrelate faster than $e^{-\nu_{r+1}\tau}$.
- Bound: Hilbert-Schmidt Eckart-Young: $\|\mathcal K_\tau - \mathcal K_{\tau,r}\|_{HS}^2 = \sum_{i>r}\sigma_i^2$; for any
  f, $\|(\mathcal K_\tau - \mathcal K_{\tau,r})f\| \le \sigma_{r+1}\|f\|$; the top-r VAMP-2 score is maximal over all
  r-dimensional feature pairs (Wu & Noé 2020; `theorem`; needs $\mathcal K_\tau$ compact, and Hilbert-Schmidt for the
  first identity, both true here for τ > 0).
  Retained dimension at threshold ϑ is the minimal rank with error ≤ ϑ (spectral Eckart-Young; CoherentModes S.10
  for the graph analogue).
- From data: EDMD converges to the Galerkin projection on the dictionary span (Williams et al. 2015; Korda & Mezić
  2018); closure defect of the dictionary is not bounded in general (`conditional`).
- Running example: $\sigma_i = e^{-\nu_i\tau}$; $[builder$: retained dimension at ϑ = 0.5 for τ ∈ {0.25, 4, 40},
  expected 4, 2, 1; gaps after 2 and 4 at τ = 0.25 and 4; data-limit EDMD eigenvalues per dictionary; face C singular
  values at ℓ = 12$]$.
- Budget line: T, S.

**Page 4, spectral clustering.**
- Decomposed: the normalized Laplacian (or random walk) of a similarity graph; with dynamics, the transfer operator
  or dynamic Laplacian. Weights: degree (or Sinkhorn) normalization, which is what makes eigenvectors relax
  conductance.
- Knob: number of sets k (= r); graph scale (bandwidth β or k_nn); lag / diffusion time.
- Discarded: the integrality constraint (indicators relaxed to real vectors) and modes beyond k.
- Bound: Cheeger $\mu_2/2 \le h(G) \le \sqrt{2\mu_2}$ (sweep cut attains the upper bound); k-way
  $\mu_k/2 \le \rho_G(k) \le O(k^2)\sqrt{\mu_k}$ and $\rho_G(k) \le O(\sqrt{\mu_{2k}\log k})$ (Lee, Oveis Gharan &
  Trevisan 2014; upper constants not explicit); all `theorem`; partition residual $\eta^2 \le
  \sum_j\phi(A_j)/\mu_{k+1}$ (Peng, Sun & Zanetti 2017; `theorem`); dynamic Cheeger $h^D \le 2\sqrt{-\lambda_2^D}$
  (Froyland 2015, Thm 3.2, nonpositive sign convention; flat manifold, volume-preserving maps; `theorem
  (scope-limited)`).
- From data: Davis-Kahan $\|\sin\Theta\| \le \|E\|/\delta$; consistency of normalized spectral clustering (von
  Luxburg, Belkin & Bousquet 2008); graph-to-manifold convergence (Belkin & Niyogi 2007) — `conditional`.
- Running example: $[builder$: $\mu_2, \dots, \mu_5$ of the kNN graph; sweep-cut conductance vs Cheeger bounds at
  k = 2; location of the cuts (expected $x_1 \approx 0$, then $x_2 \approx 0$)$]$.
- Budget line: R (Cheeger rounding), P (Davis-Kahan).

**Page 5, sparsity.**
- Decomposed: the Laplacian quadratic form $x^\top L x$ (all cuts and energies at once); for SEBA, a leading
  eigenspace.
- Knob: ε (edge budget $O(n\log n/\varepsilon^2)$); SEBA threshold μ; r.
- Discarded: edges (survivors reweighted); for SEBA, the dense mixing of sets across eigenvectors.
- Bound: $(1-\varepsilon)L \preceq \tilde L \preceq (1+\varepsilon)L$ w.h.p. (Spielman & Srivastava 2011);
  deterministic $(1-\varepsilon)^2 L \preceq \tilde L \preceq (1+\varepsilon)^2 L$ with $O(n/\varepsilon^2)$ edges
  (BSS 2012) — `theorem`. This preserves cut weights and Laplacian eigenvalues; normalized quantities (conductance,
  normalized eigenvalues) pick up the ratio of degree factors unless the original degrees are kept; for a
  degree-one walk the register's surrogate $P_* = I - \hat{\mathcal L}/(1+\varepsilon)$ has cut/energy factors in
  $[(1-\varepsilon)/(1+\varepsilon), 1]$ and $\|P_* - P\|_2 \le 2\varepsilon/(1+\varepsilon)$ (S.2). kNN truncation is
  not a sparsifier. SEBA: exact recovery from an aligned start in the exact-indicator regime (S.7); for a candidate
  partition H with $\eta = \|(I - VV^\top)H\|_F$, if $0 < \mu < \min_j n_j^{-1/2}$ and $\sqrt2\eta < c =
  \min_j(1 - \mu\sqrt{n_j})$, an aligned frame's threshold step has error $\le 2\sqrt2\eta/c$ (S.8); Froyland & Rock
  2025 — `conditional`.
- From data: n/a (sparsification is itself a controlled perturbation).
- From data (sparsifier side): a drawn sparsifier's accuracy is certified only by a verified check of both Loewner
  inequalities at a stated ε (page 5, 3.2 and 5.2: Rump 2006's floating-point Cholesky criterion, Cor. 2.7, with the
  rounding in forming the two test matrices included); a Lanczos estimate of the extreme generalized eigenvalues is an
  estimate.
- Running example: $[builder$: edges kept at ε = 0.3, 0.5; certified ε; max relative error of $\mu_2..\mu_5$; total
  leverage across the between-pair and within-pair cuts (each ≥ 1) and mean leverage per crossing edge against all
  edges; fraction of crossing edges kept and the cut weights before and after$]$.
- Budget line: Z, R.

**Page 6, computational mechanics.**
- Decomposed: the conditional Hankel (pasts × future laws) under predictive equivalence; for a coarse-graining
  Z = g(X), micro-pasts by macro-futures (υ-machine).
- Knob: number of retained predictive classes (approximate merging threshold), horizon, information-bottleneck
  trade-off $\beta_{\rm IB}$.
- Discarded: predictive distinctions below threshold; for υ, micro detail irrelevant to the macro future.
- Bound: exact: rank H ≤ number of causal states; the ε-machine is the minimal prescient history-based
  representation (Shalizi & Crutchfield 2001; `theorem`). Merging: lost predictive information = expected KL
  (identity; `standard`), computed from the actual merge. Three operations are kept apart: exact row equivalence
  (causal states), discrete quantization into K groups (a merge), and linear rank reduction (SVD of the whitened
  table). The discarded tail $\sum_{i>r}\sigma_i^2$ is the exact χ² error of the best rank-r projection, not the loss
  of a merge; for a K-group merge it is only a lower bound on the χ² loss, $\ge \sum_{i>K}\sigma_i^2$ (σ₁ = 1
  trivial), with equality only if the top-K block is spanned by group indicators (`standard`). Approximate closure of a metastable partition: $E(k) = \|QT^kQ - (QTQ)^k\| \le \min[2,
  C(\delta, \eta, k)]\,\lambda_2^k$, with δ the projection error of the dominant eigenfunctions onto step functions
  and η the spectral ratio (Sarich, Noé & Schütte 2010, Thm 3.1, quoted on page 6 with its assumptions (7), (8), (12),
  (13); reversible; full partition; `theorem`). Closure definitions
  and implications: Rosas et al. 2024, Thms 1-3 (`theorem`), with their hypotheses stated per direction: the
  weak-lumpability and computational-closure directions assume a stationary process; the strong-lumpability and
  informational-closure directions additionally assume the micro ε-machine irreducible and aperiodic; and the
  lumpability in Theorem 3 is of the micro ε-machine's causal states, not of arbitrary micro states (they coincide for
  a chain observed directly with distinct rows, as on page 6). "Coherent sets as approximate Markov blankets": `none`
  (schematic, section 8).
- From data: CSSR-type reconstruction consistency (Shalizi & Klinkner 2004) — `conditional`.
- Running example: $[builder$: four causal states and rank 4 for the well readout; rank 4 for the instrument, with
  rising counts of distinct finite-history predictive distributions and the checked hypotheses of page 1's
  infinitely-many-causal-states argument; lumpability defect of the pair label at κ = 0 (expected 0 for the chain)
  and κ = 0.3 (expected ≈ 0.004, 3.2); SNS δ, η, bound and actual error for pairs and wells at τ = 0.25, 1, 4$]$.
- Budget line: I (closure is what would license calling a coarse-graining a state), T.

**Page 7, neurons.**
- Decomposed: the whitened cross-covariance of past and future delay windows,
  $C_{pp}^{-1/2}C_{pf}C_{ff}^{-1/2}$: the stochastic Koopman SVD restricted to the span of the window dictionary
  (linear functions of the window of y, or of its ON/OFF rectified channels).
- Knob: number of neurons r; window length m; lag.
- Discarded: canonical directions with small correlation (fast, unpredictable components of the input).
- Bound: within the window dictionary, page 3's bounds hold (optimality is relative to that dictionary);
  for OU the leading nontrivial singular function is linear, while higher ones are higher-degree Hermite modes that
  linear CCA does not see (Pughe-Sanford et al. 2025; Mehler/Hermite expansion; `theorem` for the leading function);
  that the rectified output equals set membership is `conditional` (exact for OU sets defined by thresholding the
  leading function, approximate otherwise). Local CCA networks (Pehlevan et al. 2020; Lipshutz et al. 2021;
  feedforward rules their authors call non-Hebbian, anti-Hebbian lateral weights): the CCA solution is a proved fixed
  point, multichannel convergence shown numerically (`conditional`).
- From data: sample CCA error (standard; regularize when windows are long) — `standard`.
- Running example: $[builder$: top canonical correlations for linear and ON/OFF windows at m = 16; agreement of the
  pair unit with the pair label, of the outer unit with the outer/inner label, and of the two signs with the well$]$.
- Budget line: S, I.

**Page 8, Hebbian.**
- Decomposed: the threshold-shifted input covariance $Q = \Sigma_g - \theta\mathbf 1\mathbf 1^\top$; parts are
  nonnegative eigenvectors of principal submatrices, $Q_{SS}h_S = c\,h_S$, $h_S > 0$, $(Qh)_{\bar S} \le 0$.
- Knob: pruning threshold θ (and, in this site's illustration, the synaptic trace time $\tau_s$).
- Discarded: correlations below threshold.
- Bound: exact fixed-point characterization; for uniform block covariances parts are stable iff
  $\rho_{\rm across} < \theta < \rho_{\rm within}$ (HebbianHarmonics `docs/v1/findings.md`; derived). Weight readout
  (distance rule, linear neurons) recovers the contrast second moment $P_\perp\hat C P_\perp$ ($P_\perp = I -
  \mathbf 1\mathbf 1^\top/B$, the contrast projector) when live-edge outer products span the symmetric contrast space,
  never the common mode or the input distribution (HebbianHarmonics `site/content/readout.html`); for the threshold
  rule only a sketch of the populated parts. No approximation bound for population
  allocation or refinement order: `none` (history-dependent, shown by example).
- From data: mean-field (exact Σ_g) vs minibatch; sampling error of Σ_g — `standard`.
- Running example: $[builder$: within/across correlations for wells and pairs at each τ_s; θ presets that select
  wells and pairs$]$.
- Budget line: — (this page supplies a mechanism, not a term).

**Page 9, LLMs from outside.**
- Decomposed: the extended logit matrix $\Lambda[h,(f,s)] = \log P(s \mid hf) - \frac1{|\mathcal V|}\sum_{s'}\log
  P(s' \mid hf)$, histories h × (continuation f, next token s). (Λ, not L: L is the graph Laplacian and t is time.)
- Knob: logit rank r = ISAN dimension d.
- Discarded: logit directions beyond r.
- Bound: exact: rank ≤ d iff a time-varying ISAN of dimension d reproduces the (fixed-length) model (Golowich, Liu &
  Shetty 2025, Thm 4.3; `theorem`, exact-rank hypothesis on complete time-indexed matrices). Approximate, on a sampled
  block: Eckart-Young gives $\|\Lambda - \Lambda_r\|_F^2 = \sum_{i>r}\sigma_i^2$, and summed over rows
  $\sum_{h,f}\mathrm{KL}(p_{hf}\,\|\,\mathrm{softmax}\,\Lambda_r[h,(f,\cdot)]) \le \tfrac12\sum_{i>r}\sigma_i^2$
  (Golowich et al. 2025, Fact A.2; it composes directly with Eckart-Young); per row also $\mathrm{KL} \le
  2\|\delta_{hf}\|_\infty$ (log-softmax is 2-Lipschitz from ℓ∞ to ℓ∞; `standard`). Learning guarantees from logit queries for approximately low-logit-rank models:
  Golowich, Liu & Shetty 2025b (`conditional`, abstract-level check only).
- From data: finite blocks do not certify the universal rank condition — `none`.
- Running example: $[builder$: logit singular values of the exact predictor (chain and particle), typical vs
  scrambled ("nonsense") histories; numerical ranks and ISAN dimension; mean KL of rank-r reconstruction and its bound
  at r = 2, 4, 6$]$.
- Budget line: T (outside view).

**Page 10, NCS.**
- Decomposed: Sinkhorn-balanced kernel walks $P^{(\ell)}$ on N data points at each layer; the block average
  $\bar M$ (or ordered product Q); leading eigen/singular functions; SEBA sets.
- Knob: r; kernel bandwidth β (or k_nn); block of layers; diffusion time.
- Discarded: modes beyond r; detail within each set.
- Bound: the ledger of section 4.3, term by term: finite-site chain F (perturbation, sparsification, layer
  combination by the triangle inequality for averages; then a subspace bound; any construction, a posteriori); the
  end-to-end scalar chain for spectral values (Weyl on the same sites plus A.44's eigenvalue comparison; single
  sphere-kernel layer walks); sampling (single sphere-kernel walks, A.44; two-layer products, A.55; no theorem for the
  layer average or kNN graphs); rounding (S.8, an existence statement; S.3); exact truncation (A.6, S.10); and an
  unbounded interpretation term; each entry names the construction it covers. Products of layers are covered in
  prose (singular blocks, A.22, A.55, S.4), not in the live widget.
- Running example: the budget widget evaluates every ledger entry on a live face C run (lift on) and reports, per
  entry, the certificate obtained ("certified", "vacuous", "unavailable" or "no theorem") beside the observed
  quantity and the N = 8000 reference. No real-network run has a certificate yet (no reference operator or candidate
  partition was computed for them); the page says so.
- Budget line: all.

### 4.3 The page-10 error budget

All theorem numbers refer to `/home/ubuntu/code/CoherentModes/THEOREMS.md` (A.x, B.x) and
`/home/ubuntu/code/CoherentModes/SPARSITY.md` (S.x); those files index nontrivial modes from 1 (appendix A explains
the shift). **Quote hypotheses with every bound.** The budget is not one inequality: its terms live on different
spaces, and the page presents them as separate entries, combined only where a theorem allows.

**Ledger and certificate.** The budget is a **ledger**: for each term, the strongest available result, its
hypotheses and the construction it covers, or the word "gap" where none exists. A **certificate** is what a
particular run earns when those hypotheses are checked on it and the bound is evaluated, with one of four statuses:
`certified` (hypotheses hold, bound informative), `vacuous` (hypotheses hold, bound no better than trivial),
`unavailable` (a hypothesis fails, e.g. $e_F \ge \delta_r/2$), `no theorem` (the ledger entry is a gap for this
construction). Pages write "the ledger has …" for the first and "this run is certified …" for the second, and never
say that sets "carry" a certificate without naming the run. Present status, which page 10's skim path states: on the
toy network every ledger entry is evaluated live and several are certified; the real-network results quoted on page
10 have **no run certificate yet** (no reference operator or candidate partition was computed for them), and the
sampling theorems do not cover the construction that produced them.

**Two constructions; every result names the one it covers.** The *theory construction* is the register's: a dense
sphere kernel $K_\beta[i,j] = \exp(\beta\langle\hat\phi_i,\hat\phi_j\rangle)$ on normalized views that are fixed
functions of the input (on face C, population-centred: 3.5), diagonal kept, symmetric Sinkhorn P; ordered products Q
in the register. The *implemented construction* is what produced every real-network result and is face C's default
graph (section 3.5): probe-centred views, union kNN with a $10^{-6}$ floor, zero diagonal, Sinkhorn, fixed-lazy M,
block average $\bar M$. Coverage:
- both: A.2-A.3 once the scaling exists; A.6; A.21 a posteriori (with a measured difference on the same sites);
  S.3 (through its proof's hypotheses, a symmetric bistochastic chain); S.6-S.8; S.10 (P is PSD in the theory
  construction, and the lazy $\bar M$ is PSD);
- theory construction only: A.1 and A.23 (both need strictly positive entries), A.24-A.25 (sphere kernels), S.2
  (dense PSD bistochastic P), and every sampling result (A.41-A.45, A.55-A.56: fixed views, i.i.d. sites);
- implemented construction: existence and uniqueness of the scaling follow from total support (3.5; Sinkhorn &
  Knopp 1967, Csima & Datta 1972), **not** from A.1; **A.23 does not apply** (its entry range $[e^{-b}, e^b]$ excludes
  the zero diagonal), so the implemented construction has no a priori Sinkhorn-stability constant here, only A.21 a
  posteriori. (Were the kernel changed to keep a positive diagonal floor $10^{-6}$, A.23 would apply with joint range
  $[10^{-6}, 1]$: rescale kernel **and kernel difference** by $10^3$, so $b_K = \tfrac12\log10^6 \approx 6.9$ and
  $\|P'-P\|_F \le 10^3\min(10^{12}/N, 707)\,\|K'-K\|_F$: vacuous at practical N.) kNN truncation is not a sparsifier.
The page-10 spec's coverage table (its section 6.3) is the detailed version.

**Objects.** N sampled sites (data points). On those same sites: $P^{\rm used}$, the operator actually computed
(chosen kernel and bandwidth, possibly sparsified, possibly with noisy activations, a single layer or a layer
average), and $P^{\rm ideal}_N$, the reference operator on the same N sites: the same construction at its reference
scale (page 10: the builder's $\beta_{\rm ref}$, or $k_{\rm nn} = 15$), dense (not sparsified) and noise-free
($D_{\rm flow} = 0$). Separately, $P_{\star,\rm ref}$, the **reference population operator**: the population
(infinite-sample) operator of the same reference construction, i.e. the noise-free fixed view (on face C centred by
the stored vector $m_\ell$, 3.5) at the reference scale $\beta_{\rm ref}$. It is the operator that $P^{\rm ideal}_N$
samples, it acts on functions on the data distribution, not on $\mathbb R^N$, and it is the only population target
the budget names (not the population operator at whatever bandwidth $P^{\rm used}$ happens to use). A resolution r and
the external gap $\delta_r$ of the top-r block: of $P^{\rm ideal}_N$ for chain F; for sampling statements the gap of
$P_{\star,\rm ref}$, which is never known and enters only through a lower bound proved on the same event (below).

**Chain F: finite-site certificate (everything on $\mathbb R^N$, the same sites; symmetric operators).**

| term | bound | hypotheses | source |
|---|---|---|---|
| **P** kernel / bandwidth / view perturbation | Sinkhorn Lipschitz: for kernels with joint entry range $[m, M]$, $b_K = \tfrac12\log(M/m)$ and $\|P'-P\|_F \le \min(e^{4b_K}/N, e^{b_K}/\sqrt2)\,(mM)^{-1/2}\|K'-K\|_F$ (the rescaling by $(mM)^{-1/2}$ applies to the difference too; for sphere kernels $mM = 1$; the register writes b, the site $b_K$, since b = 0.6 is the potential's width); propagation of view and temperature changes (A.24-A.25); a posteriori, A.21 with a computed upper bound on $\|P^{\rm used} - P^{\rm ideal}_N\|_{op}$ (verified: page 5's floating-point positive-definiteness test (Rump 2006, Cor. 2.7, with the formation radius) passed by $sI \mp E$, or the Frobenius norm with a stated rounding inflation; a Lanczos value is only a lower estimate) | strictly positive symmetric kernels (A.23; not the zero-diagonal implemented kernel); unit views, same sites, sphere kernel (A.24-A.25); a posteriori: none beyond same sites | A.23 (`THEOREMS.md:655-719`, scale-relative statement at `:661`), A.24-A.27 (`:797-931`) |
| **Z** sparsification | for $\mathcal L = I - P$ and a sparsifier $\hat{\mathcal L}$ at certified accuracy ε: $(1-\varepsilon)(1-\lambda_i) \le \hat\mu_i \le (1+\varepsilon)(1-\lambda_i)$, relative on $1 - \lambda_i$, not on $\lambda_i$; after rescaling to the walk $P_* = I - \hat{\mathcal L}/(1+\varepsilon)$, the eigenvalues of $I - P_*$ lie within factors $[(1-\varepsilon)/(1+\varepsilon), 1]$ of $1 - \lambda_i$ (cuts and energies likewise), and $\|P_* - P\|_2 \le 2\varepsilon/(1+\varepsilon)$ | dense PSD bistochastic P, normalized before sparsifying; resistance sampling or BSS; ε certified for the drawn graph by page 5's verified test (5.2: Rump 2006, Cor. 2.7, including matrix-formation error), not estimated; kNN truncation not covered | S.2 (`SPARSITY.md:19-50`) |
| layer combination | averages: $\|\bar M' - \bar M\| \le \frac1m\sum_\ell e_\ell$ (triangle inequality; the implemented construction averages). Products (prose only on page 10): error ≤ sum of layer errors (A.26) | same sites; contractions (finished Sinkhorn); sparsified factors as in S.2 | triangle inequality; A.26 (`:869-893`); S.2 (`SPARSITY.md:29`, proof `:44`) |
| → subspace | with $e_F = e_P + e_Z$ (+ layer mean) in operator norm: if $e_F < \delta_r/2$, $\|\sin\Theta\|_{op} \le e_F/(\delta_r - e_F)$. Singular blocks of products: $(1+\sqrt2)e_F/(\delta_r - e_F)$ for left and right subspaces separately (A.22; prose only) | isolated block with gap $\delta_r$ of $P^{\rm ideal}_N$ | A.21 (`:570-602`), A.22 (`:604-653`) |

Adding $e_P$, $e_Z$ and layer errors is legitimate here because all are operator-norm errors of matrices on the same
$\mathbb R^N$ (triangle inequality).

**Scalar chain: an end-to-end budget for spectral values (named terms, limited target).** For one sphere-kernel
layer: the reference $P^{\rm ideal}_N$ is the noise-free fixed view at $\beta_{\rm ref}$ on the N sites, and the used
operator may differ from it in any way chain F measures (bandwidth, noise, sparsifier). On the event of A.44 for the
reference construction at $\beta_{\rm ref}$ (probability ≥ $1 - \eta_{\rm fail}$ after the selection accounting
below), for every i at once,
$$|\lambda_i(P^{\rm used}_N) - \lambda_i(P_{\star,\rm ref})| \;\le\; \underbrace{e_F}_{\text{P, Z: chain F}} \;+\; \underbrace{E_N(\beta_{\rm ref})}_{\text{S: A.44}},\qquad e_F \ge \|P^{\rm used}_N - P^{\rm ideal}_N\|_{op}:$$
Weyl on the same sites (whatever bandwidth $P^{\rm used}$ uses), then A.44's ordered eigenvalue comparison between
$P^{\rm ideal}_N$ and $P_{\star,\rm ref}$, both at $\beta_{\rm ref}$ (their nonzero spectra are those of their lifts).
$E_N$ is evaluated at $\beta_{\rm ref}$ ($B_0 = e^{4\beta_{\rm ref}}$ and A.44's t at $\beta_{\rm ref}$), never at
the used operator's β: the sampling theorem compares the reference with its own population, and a used bandwidth
other than $\beta_{\rm ref}$ is a finite-site perturbation inside $e_F$. **Target, stated with it:** the eigenvalues of
the declared reference population operator, hence its gaps (which resolutions are separated), not its
eigenfunctions, not sets, and not the population operator at the bandwidth in use. On the same event Weyl also gives
the **population-gap lower bound** $\delta_r(P_{\star,\rm ref}) \ge \delta_{\rm lb} := \delta_r(P^{\rm ideal}_N) -
2E_N(\beta_{\rm ref})$, which is the justified gap a projector certificate needs: if $E_N(\beta_{\rm ref}) \le
\delta_{\rm lb}/4$, A.44's lifted projector error between the blocks of $P^{\rm ideal}_N$ and $P_{\star,\rm ref}$ is
at most $4E_N(\beta_{\rm ref})/\delta_{\rm lb}$. Because all of this holds simultaneously for every i on one event, r
may be chosen after looking (no union over r). For an ordered product of two layers the same chain holds for singular
values with $E_Q$ (A.55; prose only). For the layer average and for kNN graphs there is no scalar chain, because there
is no sampling theorem.

**Sampling (S): three displays, never merged.**
1. **Theorem certificate**: the A.43/A.44/A.55/A.56 bound evaluated at the reference bandwidth $\beta_{\rm ref}$
   with the universal constant $B_0 = e^{4\beta_{\rm ref}}$ (no population quantity needed), on a view fixed before
   the sites are drawn (on face C, centring by the stored vector $m_\ell$, which also defines $P_{\star,\rm ref}$;
   probe centring breaks this), with the population gap replaced by $\delta_{\rm lb}$. Status `certified`, `vacuous`
   or `unavailable`. **Selection accounting** (one rule, used wherever a sampling certificate appears): (i)
   $\beta_{\rm ref}$ is chosen on the independent reference sample (3.6), so conditionally on that sample it is fixed
   relative to the live sites and needs no union bound over the β grid; (ii) every other choice a reader can make
   after seeing results that changes which sampling event is invoked is covered by splitting $\eta_{\rm fail}$ over the
   whole selectable family (page 10: 13 layers × 3 sample sizes, so A.44 is applied at $\eta_{\rm fail}/39$ per event);
   (iii) choices that change only $P^{\rm used}$ (its bandwidth, noise, sparsifier) are deterministic chain-F terms and
   need no probability; (iv) no union over r is needed, since every i holds on one event. $\eta_{\rm fail}$ itself is
   declared before looking.
2. **Plug-in calculation**: the same formulas at $\beta_{\rm ref}$ with $S_{\max}$ estimated from the reference
   sample and the reference's gap in place of the population's; labelled "plug-in calculation, not a certificate".
3. **Empirical comparison**: the observed $\max_{i\le r+1}|\lambda_i^{(N)} - \lambda_i^{(8000)}|$ against the
   N = 8000 numerical reference, labelled "empirical; the reference is not population truth".

| operator | bound | hypotheses | source |
|---|---|---|---|
| single unnormalized kernel | lifted covariance error $\le b_K\,h_N(\eta_{\rm fail})$, $h_N(\eta_{\rm fail}) = (1 + \sqrt{2\log(1/\eta_{\rm fail})})/\sqrt N$, with probability ≥ $1 - \eta_{\rm fail}$ (the register writes η for this failure probability; the site writes $\eta_{\rm fail}$ because η is S.8's residual), $b_K = e^\beta$ for the sphere kernel; eigenvalues within the same; isolated-block lifted projector error $\le 4b_Kh_N/\delta$ if $b_Kh_N \le \delta/4$ | i.i.d. sites; view and β fixed before sampling; bounded feature map | A.43 (`:1158-1177`) |
| single Sinkhorn-normalized walk | eigenvalue error $\le E_N$; lifted projector error $\le 4E_N/\delta$ if $E_N \le \delta/4$ (δ the population gap, or $\delta_{\rm lb}$); in the small-error regime $E_N \le (12e^{2\beta}+7)e^{4\beta}h_N$ (population-sensitive $O(S_{\max}^2 e^{3\beta}h_N)$) | i.i.d. sites; normalized views fixed before sampling; β fixed independently of the sites (on face C, $\beta_{\rm ref}$ from the independent reference sample; union bound over the post-hoc selectable layers and sample sizes, as in display 1); regime conditions stated in A.44 | A.44 (`:1179-1246`; fixed-view requirement `:1100`) |
| ordered product of two layer walks | singular values within $E_Q = O(N^{-1/4})$; lifted singular projectors $8E_Q/\delta$ if $E_Q \le \delta/4$, sample requirement carrying $\delta^{-4}$; root-N only for finitely supported views | i.i.d. sites carrying both fixed views | A.55 (`:1581-1629`) |
| block average $\bar M$ of layer walks, and any kNN construction | **no sampling theorem in the register.** Per-layer A.44 bounds plus the triangle inequality in A.55's common site space are a plausible route; the page states this as an open gap, not a certificate | — | gap; section 8 hook |
| documents with dependent positions | replace statistical N by the number of documents D | i.i.d. documents | A.56 (`:1631-1642`) |

**What cannot be combined.** Subspace certificates in different lifts cannot be summed without a common
identification: chain F's subspace bound compares two blocks in $\mathbb R^N$; the sampling projector bound compares
lifted projectors in A.44's RKHS (A.55's common site space for products). Nothing in the register identifies the two,
so there is no end-to-end subspace or set certificate from a finite run to the population; the scalar chain above is
the end-to-end statement that exists, and pages say so in those words (not "the chains cannot be added").
Comparisons across sample sizes use **eigenvalues** (comparable across N) or Nyström-extended functions (A.45,
`:1250`), never raw eigenvectors of different-size matrices.

**Rounding (R): from subspace to sets.** For a candidate partition with normalized indicator matrix H (on face C, the
full ground-truth basin partition of all inputs, because S.8 is stated for a partition of all sites; agreement on the
uncommitted band is reported only as an observation):
- decompose the candidate residual: $\eta = \|(I - VV^\top)H\|_F \le \eta_{\rm ideal} + \sqrt r\,\|VV^\top -
  V_0V_0^\top\|_{op}$, where $V_0$ spans the top-r block of $P^{\rm ideal}_N$, $\eta_{\rm ideal} = \|(I -
  V_0V_0^\top)H\|_F$ is how well the ideal block represents the partition at all (not zero on face C: the basins are
  not exactly an eigenspace), and the second term comes from chain F;
- SEBA (S.8, `SPARSITY.md:157-171`): if $0 < \mu < \min_j n_j^{-1/2}$ **and** $\sqrt2\eta < c = \min_j(1 -
  \mu\sqrt{n_j})$, an aligned frame exists whose threshold step has error $\le 2\sqrt2\eta/c$. If either condition
  fails, the widget shows "rounding certificate unavailable". This is an **existence** statement about an aligned
  frame, not a guarantee for a given SEBA run (S.6-S.7; the default threshold recovered planted sets in only 43/200
  starts, `SPARSITY.md:151`); the run's own error against H is reported beside it as an observation;
- two-way Cheeger rounding (S.3, `SPARSITY.md:62-85`): sweep sets with conductance $\le \sqrt{2(1 - \lambda_2)}$
  (site indexing), for symmetric walks; higher-order bounds only with the explicit loop-removal factors stated there;
  for products, S.4's coherent-pair rounding (source and image sets; witness for $\sigma > 1/2$, trimmed transport
  bound positive only for $\sigma > 17/18$; prose only).

**Truncation (T).** Exact identity $\|F - \Pi_r F\|_F^2 = \sum_{i>r}\|F^\top\psi_i\|^2$ for any feature matrix F (A.6,
`:262-279`); spectrally, for a symmetric PSD walk, the retained count $\#\{i : \lambda_i^t > \vartheta\}$ is the
minimal rank of an approximation to $P^t$ with spectral error ≤ ϑ (S.10, `SPARSITY.md:184-188`). S.10 does not
apply to products: in general $\sigma_i(Q^t) \ne \sigma_i(Q)^t$.

**Interpretation (I).** No bound. Belief-sufficient layers need not have rank k − 1; a perfectly belief-sufficient
Mess3 layer has infinite context rank under a universal kernel (B.10-B.12, `THEOREMS.md:1946-2115`). Section 8 hook.

**How the resolution knob enters** (the page's key point and a figure):
- Truncation error falls as r grows.
- Subspace certificates divide by the gap at the chosen r (A.21's $e_F/(\delta_r - e_F)$, A.44's
  $4E_N/\delta_{\rm lb}$); eigenvalue and operator-error bounds (chain F's $e_F$, the scalar chain's $e_F + E_N$) do
  not, and the gap decides whether those errors are small enough to distinguish the block (an error below $\delta_r/2$
  separates it); rounding additionally needs a small partition residual η and a positive threshold margin c (S.8).
  Gaps are **not monotone in r**: in the running example at lag $\tau = 0.25$ the block of 4 is far better separated
  than the block of 2, and at $\tau = 4$ the reverse (section 3.2). The knob (lag, diffusion time t, or bandwidth β)
  decides which resolutions are certifiable.
- For a fixed target accuracy, a sampling block certificate needs $N \propto 1/\delta_r^2$ for a single walk (A.44's
  condition $E_N \le \delta_r/4$ and $E_N \propto N^{-1/2}$) and $N \propto \delta_r^{-4}$ for an ordered product
  (A.55).
- The bandwidth is itself a resolution knob with a price: larger β resolves finer clusters (the ideal companion,
  section 3.8: the fine gap keeps opening as β grows, while the coarse gap opens, peaks and closes) but A.44's
  constant grows like $e^{3\beta}$ to $e^{6\beta}$.

**Vacuity.** Universal constants often make sampling certificates vacuous (a sine bound ≥ 1, or a condition such as
$E_N \le \delta/4$ failing) at realistic N; A.44's worst case is the usual culprit (`THEOREMS.md:1235-1246`). The
widget displays vacuous terms as such ("bound vacuous at this N", with the N that would be needed) and never hides
them. On the toy, chain F and the rounding certificate are usually informative.

**The outside view's budget** (pages 1 and 9) has only T and S in this sense; page 10 shows it next to the inside
view's and says no theorem yet ties them (E17).

---

## 5. Skimmability and length

### 5.1 The skim path

A page's skim path is exactly these elements, and reading only them must give a simplified but true account:

1. kicker, title, and the **lede**: the page's one-sentence claim (≤ 45 words), set as `p.lede`;
2. **the picture**: a hero figure showing the running example under this page's lens, with a one-line `fig-sub`
   saying what to see;
3. **section headings written as claims** (sentences, ≤ 12 words), not topics ("Rank counts the machine's states",
   not "Rank");
4. at most one **key-point callout** per section (≤ 2 sentences);
5. every figure's title and `fig-sub` line (the "one thing to see");
6. the **ledger** box;
7. the **connections strip** (cards to other pages, each with its relation symbol).

The writer checks the skim path by reading only these elements aloud; if a claim depends on unread prose, fix the
heading or the callout, not the prose.

### 5.2 Length budgets

| item | budget |
|---|---|
| main-path prose (outside disclosures) | 1,800-2,800 words (map: ≤ 900) |
| h2 sections | 4-6 plus "Connections" and "Ledger"; each ≤ 450 words of main-path prose |
| figures on the main path | hero + ≤ 2 live widgets + ≤ 2 static figures |
| displayed equations on the main path | ≤ 8; every symbol glossed at first use on the page |
| a disclosure (`details.more`) | ≤ 800 words; any number of them |
| whole page including disclosures | ≤ 6,000 words |
| captions | Plotted/Values convention; ≤ 90 words |

### 5.3 Layers of depth

- **L0 skim** (5.1).
- **L1 main prose**: the argument, with every claim either supported in place or pointed to its support.
- **L2 disclosures** titled "The maths: …", "Why this holds: …", "Hypotheses: …", "In other fields: …". Derivations,
  proof sketches, full hypothesis lists, and the alternative conventions of other fields go here. A disclosure must
  never be needed to understand the main path.
- **L3 sources**: a "Sources" section at the end (full citations, links, and which theorem numbers were used).

### 5.4 Self-completeness

Each page introduces its topic from scratch. If a page relies on another page's idea, it includes an
"Arriving here first?" aside (≤ 80 words) glossing the idea in plain language with a link. Pages may not say "as we
saw" without a link.

### 5.5 Voice and style

- **Neutral expository voice.** No first person singular; "we" only in the inclusive mathematical sense ("we can
  write…"), sparingly. This overrides HebbianHarmonics `DESIGN.md` §3.
- British spelling (as in the reused design system).
- No hype words ("powerful", "remarkable", "crucially", "delve"); no decorative bold. Bold is for the one phrase in a
  paragraph the skimmer must catch.
- Captions are definitional and do not interpret (HebbianHarmonics `DESIGN.md` §3 rules apply).
- Every result is attributed. Results from the programme's own repositories are described as such ("the
  CoherentModes theorem register, A.21"), not as established literature.
- Interpretive readings of empirical results are marked as readings ("the sets can be read as…").

---

## 6. Site architecture and design system

### 6.1 Decisions (fixed)

A standalone static GitHub Pages site, modelled on HebbianHarmonics: no build step, native ES modules, vendored KaTeX
and fonts, Canvas/SVG widgets, hash-routed pages, served over HTTP (not `file://`). Nothing from a CDN; no tracking.

### 6.2 Reused from HebbianHarmonics (copy, then adapt)

Source: `/home/ubuntu/code/HebbianHarmonics/site/`. Read its `DESIGN.md` for the API; this section lists only the
differences.

| file | reuse | changes |
|---|---|---|
| `index.html` | shell: banner, masthead, sticky tabs, one `<section>` per page | new title/subtitle; 12 tabs (`map`, `hankel`, `control`, `koopman`, `cuts`, `sparsity`, `compmech`, `neurons`, `hebbian`, `logits`, `ncs`, `ref`); banner: "Explanatory site · widgets run in your browser · the running example is synthetic" |
| `css/tokens.css` | all tokens | add the hierarchy tokens of 6.4 |
| `css/site.css`, `css/ui.css` | as is | add styles for `ledger`, `connections`, `map-card`, `fallback`, `status` hook (unstyled; section 8) |
| `js/main.js` | router, lazy loading, maths, side notes, ctx | module naming: `js/p_<id>.js` instead of `ch_<tab>.js`; otherwise unchanged |
| `js/ui.js` | all components | `tabsMeta` for 12 tabs; add `ledger`, `connections`, `mapCard` (6.5) |
| `js/charts.js`, `js/view3d.js`, `js/palette.js` | as is | palette exports hierarchy colours |
| `js/engine.js` (v1 engine), `js/ch_old_model.js` | page 8 only, imported unchanged (copy with `ENGINE.md`) | none |
| `js/onsite_engine.js` (v2 engine, with `ONSITE_ENGINE.md`), `js/ch_readout_math.js` (readout estimator) | page 8 only; copied verbatim by the page writer as `js/p_hebbian_onsite_engine.js` and `js/p_hebbian_readout_math.js`, with a header naming the source commit | none |
| `js/ch_old.js` (three-input widget), `js/ch_readout.js` (readout figure) | page 8 only; adapted by the page writer as `js/p_hebbian_circuit.js` and `js/p_hebbian_readout.js` (page 8 spec, section 12); a new B-generic threshold-rule wrapper `js/p_hebbian_model.js` is written from `ch_old_model.js`, which is hard-wired to three inputs | keys prefixed per SPEC 6.5 |
| `vendor/` (KaTeX 0.16, Source Serif 4, Inter, JetBrains Mono) | as is | none |
| DESIGN.md §§2, 4-11 | binding (component APIs, captions, interaction conventions, performance, hand-in checks) | §3 voice replaced by 5.5; ids prefixed with the page id (`hankel-explorer`) |

### 6.3 File layout

```
SpectralTutorial/
  spec/                  SPEC.md, PAGE_TEMPLATE.md, pages/NN-<id>.md            (spec owners)
  site/
    index.html
    css/{tokens,site,ui}.css
    js/{main,ui,charts,palette,view3d}.js                                       (design system)
    js/lib/rng.js        seeded PRNG + normal/categorical sampling              (shared numerics owner)
    js/lib/linalg.js     dense: matmul, eigh (start from HebbianHarmonics engine.js), svd (via eigh of Gram
                         for small, one-sided Jacobi ≤ 80×80), lstsq/pinv, expm (small); sparse: CSR, matvec,
                         Lanczos (top-k), conjugate gradient
    js/lib/example.js    the running example: V, ∇V, SDE step, readout, symbols, flow map, loaders for
                         data/example/*.json
    js/lib/hankel.js     word enumeration, Hankel blocks from probabilities or counts, spectral WFA
                         realization, word-probability evaluation, metrics (port of crw-blog build.py)
    js/lib/graph.js      kNN/kernel graphs (incl. face C's union kNN with floor, 3.5), Laplacians, Sinkhorn
                         balancing, lazy walks, Cheeger sweep, effective resistance, spectral-sparsifier
                         sampling, matrix-free Lanczos SVD
    js/lib/seba.js       SEBA (port of CoherentModes explore/cifar_baselines/variants.py:seba_mu)
    js/lib/lti.js        Gramians (Lyapunov via Bartels-Stewart or modal), balanced truncation, H∞ on a
                         frequency grid, step/impulse responses
    js/lib/cca.js        delay windows and covariance functions, CCA / VAMP / EDMD (API below)
    js/lib/bowtie.js     the thesis diagram (1.4)
    js/p_<id>.js         page module; helpers js/p_<id>_*.js                     (page writer)
    content/<id>.html    page prose fragment                                    (page writer)
    data/example/*.json  running-example data (tools/build_example.py)          (example owner)
    data/<id>/...        page-specific data                                     (page writer)
    assets/fig/<id>/...  static figures (PNG/SVG) with provenance notes
    assets/fallback/<figureId>-<tour>.png, <figureId>.gif                       (generated, 6.6)
    vendor/
  tools/
    build_example.py     Python reference for the running example (asserts; writes site/data/example)
    capture.sh           fallback capture with playwright-cli + ffmpeg (6.6)
  tests/
    parity_*.mjs / test_parity_*.py   JS vs Python parity for lib/ and example.js
```

Ownership: a page writer edits only `content/<id>.html`, `js/p_<id>*.js`, `data/<id>/`, `assets/fig/<id>/`. Shared
modules have one owner; a writer who needs a shared change requests it (and may prototype it in a page helper first).
The builder-written files `data/<id>/pNN.json` are produced by the example owner from the page spec's section 6 (3.6).

**Shared-module API (binding where pages overlap).** Each page spec's section 12 lists the functions it needs; the
owner implements their union. Where two pages need the same thing, these names and signatures are binding:
- `lib/cca.js`: `delayWindows(signal, m, lag)`; `covariances(X, Y)` → `{Cxx, Cxy, Cyy}`; `covFunctions(channels,
  maxLag, {offset, n})` → `R[c][c'][ℓ]`; `windowBlocks(R, m, g)` → `{Cxx, Cxy, Cyy}` (past most recent first, future
  earliest first); `cca(Cxx, Cxy, Cyy, {ridge})` → `{sigmas, A, B}` (canonical correlations of the centred problem,
  descending, without the trivial 1, which pages prepend; A past/left filters, B future/right filters, columns
  aligned); `ccaFromSamples(X, Y, {ridge})` (same return); `variates(channels, A, m, means)`; `vamp(X0, Xt, {ridge})`
  → `{sigmas, A, B}`; `edmd(X0, Xt, {ridge})` → `{K, eigvals, eigvecs}`.
- `lib/graph.js`: `knnUnion(Z, k, {metric: "euclidean"|"cosine", floor = 1e-6})` (the face C graph of 3.5; diagonal
  0); `knnGraph(X, k, {weights: "unit"|"gauss", s})` (face A graphs, page 4); `gaussKernel(X, s, {alpha, floor})`;
  `sphereKernel(Z, beta)`; `sinkhorn(K, {tol, maxIter})` → `{P, v, residual}`; `lazy(P)`; `normalizedLaplacian(W)`;
  `bottomEigs`, `sweepCut`, `conductance`, `ncut`, `effectiveResistances`, `sampleSparsifier`, `knnTruncate`,
  `measureEps`, `sparseSurrogate` as named in pages 4 and 5; `lanczosSVD(matvec, rmatvec, n, k)`.
- `lib/linalg.js`: adds `arnoldi(matvec, n, k)`, `opNormSym(A)`, `sinTheta(V, W)`, `hungarian(C)`, Procrustes, and
  `verifyPD(A, R)` (Rump 2006, Cor. 2.7 with bound I: true only if every symmetric X with $|X - A| \le R$ is proved
  positive definite; specified on page 5, 5.2; used by pages 5 and 10).
- `lib/example.js`: adds `samplePi(n, rng)`, `driftCoefficients(kappa)`, basin labels, the face C flow and lift.
- `lib/lti.js` and `lib/seba.js`: as listed in pages 2 and 5 (sole users of their full APIs; page 10 uses `seba`).

### 6.4 Colour and shape semantics added

The running example's hierarchy gets fixed colours, used on every page whenever wells or pairs are shown:

| token | role | proposed value |
|---|---|---|
| `--c-pair-L`, `--c-pair-R` | left / right pair (r = 2 colouring) | blue `#2a78d6`, orange `#eb6834` (= cat-0, cat-1) |
| `--c-well-1`, `--c-well-2` | $w_1$ (lower left), $w_2$ (upper left) | dark blue `#184f95`, light blue `#6da7ec` |
| `--c-well-3`, `--c-well-4` | $w_3$ (lower right), $w_4$ (upper right) | dark orange `#b8460f`, light orange `#f4a37f` |
| `--c-other` | unassigned / uncommitted / below threshold | as HebbianHarmonics |

Lightness encodes the within-pair split (lower = dark, upper = light) and hue the pair, so an r = 2 picture and an
r = 4 picture of the same points are visibly nested. Validate with the dataviz skill's palette validator
(adjacent CVD ΔE ≥ 9) before use and adjust shades if needed. Symbols `a`, `b`, `c` are always set in monospace text,
never colour-coded. Data points are dots; wells are drawn as small ink-outlined circles at their minima; graph edges
use the ink map (opacity ∝ weight). Signed eigenfunctions use the `div` map with a symmetric range.

### 6.5 New shared components

- `ui.ledger({decomposed, knob, discarded, bound, fromData, example, budget, parent})`: a card with the seven rows of
  4.1; `example` accepts a function filled after data load; `budget` renders letter chips (T S P Z R I).
- `ui.connections({items: [{page, rel: "=" | "≈" | "~", text, edge}], parent})`: a strip of cards linking to other
  pages; the relation symbol is large; `edge` (E-id) shown small and linking to the map's connection list entry
  `#map/map-edge-e<n>`. Exactly
  three relation values exist; an inequality such as E11's is stated in the text, not in `rel`.
- `ui.mapCard({page, title, claim, thumb, knob, bound})` for page 0.
- `bowtie(el, {left, right, leftNorm, rightNorm, sigmas, r, bound, onR?})`: SVG per 1.4; interactive variant lets
  r be dragged.
- **URL scheme (binding).** `#<page>` opens a tab; `#<page>/<element-id>` opens it and scrolls to the element with
  that id (a section, a figure, or a map entry such as `map-edge-e7` or the section `map-example`), outlining it
  briefly in accent; widget state follows as a query, `#<page>[/<element-id>]?<key>_<param>=…`. The router in
  `main.js` supports all three forms. Pages link to the running example's canonical description as
  `#map/map-example` and to an edge as `#map/map-edge-e<n>`.
- **Ids.** Section ids are `<page>-<slug>` (`hankel-states`); figure ids are `<page>-fig-<slug>`
  (`hankel-fig-states`); the two namespaces never collide. Every widget also has a two- or three-letter **key**
  (`ex`, `st`, `hr`) used for its URL state.
- **Widget mount contract** (every live figure):
  ```js
  // in js/p_<id>.js
  export async function init(panel, ctx) { const w = await mountExplorer(ctx.slot("explorer"), ctx, "ex"); ... }
  // a widget returns
  { key, figureId, tours: [{id, label, note, params}], fallbackTour, apply(params), state(), destroy() }
  ```
  URL keys are prefixed by the widget key (`ex_r=4`); the widget's tour is `<key>_tour` (`ex_tour=particle`) and wins
  over its individual keys. The **default state equals the first tour**. The **fallback image** is the first tour
  unless the per-page spec names a different `fallbackTour` (e.g. a hero whose default is "start playing" but whose
  representative still is a later frame). The fallback must be a named tour (capture loads tours only), so a
  representative frame gets its own paused tour. Every page's hero is `<id>-fig-hero` (the map's card thumbnails use
  its fallback PNG).
- Each page module exports `widgets()` returning the list above, and the page writes a manifest
  `site/data/<id>/widgets.json` (`[{key, figureId, tours: [ids], fallbackTour, animated}]`) for the capture tool.
- When all widgets on a page have rendered their current state, the page sets `document.body.dataset.ready = "1"`.

### 6.6 Static and GIF fallbacks (every widget)

- Each live figure's HTML contains, inside its slot, `<img class="fallback" src="assets/fallback/<figureId>-<fallback
  tour>.png" alt="…">`; the module replaces it only after a successful mount, so a widget whose `init` throws, or a
  browser without the needed features, still shows the picture and caption. (Reading the site with JavaScript
  disabled is **not** a requirement: the inherited shell loads page fragments with JavaScript. Fallbacks exist for
  cross-posting and for failures.)
- `tools/capture.sh <id>` serves the site on loopback, reads `site/data/<id>/widgets.json`, and for each widget key
  and tour runs `playwright-cli open "http://127.0.0.1:<port>/#<id>?<key>_tour=<tour>&capture=<key>"`, waits for
  `document.body.dataset.ready === "1"`, and screenshots the element `#<figureId>` at 1440 px width and device scale 2
  to `assets/fallback/<figureId>-<tour>.png`. `capture=<key>` hides transport chrome and hover hints and pauses
  animation at the tour's state. Animated widgets also get `assets/fallback/<figureId>.gif` assembled from their
  tour sequence (or ≤ 6 s of frames) with `ffmpeg` (palettegen/paletteuse, ≤ 2 MB).
- Cross-posting (LessWrong, blog): the fallback PNG/GIF plus the caption text is the cross-post figure. Captions must
  therefore make sense without the controls ("at r = 4" rather than "move the slider").

### 6.7 Performance, correctness and accessibility

- Load: ≤ 1.5 MB per page excluding fonts and fallbacks; JSON lazily fetched in `init`; Float32 arrays stored as
  base64 when > 50 kB.
- Interaction: ≤ 100 ms per control change typical; ≤ 1 s for heavy recomputes, with a "computing…" status; never
  block during animation. Measure in headless Chrome without GPU (HebbianHarmonics `DESIGN.md` §9 method).
- All animation visibility-gated (`ui.transport`, `ui.animate`); respect `prefers-reduced-motion`.
- Determinism: every random draw comes from `lib/rng.js` with a seed in the URL state; the same seed gives the same
  picture in the builder and the browser (parity tests: example dynamics, Hankel blocks, Sinkhorn, Lanczos
  eigenvalues to 1e-8 relative; SEBA labels exactly on fixed inputs).
- Accessibility: keyboard-operable controls (ui.js), visible focus, alt text for every image and fallback, a
  text statement of the one thing to see (`fig-sub`), colour never the only carrier (wells also labelled
  $w_1..w_4$ on hover and in legends), WCAG AA contrast for text.
- Zero console errors; screenshots at 1440 × 900 and 390 × 844 inspected (HebbianHarmonics `DESIGN.md` §11).

### 6.8 Notation and glossary

Appendix A (notation) and appendix B (glossary) are binding. The Reference tab renders them.

---

## 7. Inventory

### 7.1 Existing assets to reuse

| asset | path | use |
|---|---|---|
| Site shell, components, vendor | `/home/ubuntu/code/HebbianHarmonics/site/` (`index.html`, `css/`, `js/{main,ui,charts,palette,view3d}.js`, `vendor/`) | the whole design system (6.2) |
| v1 Hebbian engine + model wrapper | `/home/ubuntu/code/HebbianHarmonics/site/js/engine.js`, `ENGINE.md`, `js/ch_old_model.js`; reference `hebb/core.py` | page 8 live simulation |
| v2 engine and sweeps | `/home/ubuntu/code/HebbianHarmonics/site/js/onsite_engine.js`, `site/data/sweeps2/*.json` | page 8 aside on the different (v2) principle; quote numbers only from these files |
| Hebbian theory | `/home/ubuntu/code/HebbianHarmonics/docs/v1/findings.md`, `docs/v1/review_corrections.md`, `site/content/old.html`, `site/content/readout.html` | page 8 claims |
| Hankel-HMM widget | `/home/ubuntu/code/crw-blog/assets/widgets/hankel-hmm.html`, builder `hankel-hmm-src/build.py` | page 1: port the realization and metrics code into `lib/hankel.js` and the builder; reuse its Golden Mean / Zero-One-Random / Mess3 catalogue |
| Davis-Kahan widget | `/home/ubuntu/code/crw-blog/assets/widgets/davis-kahan.html` (D3) | design reference for the perturbation figure on pages 4 and 10; reimplement with `charts.js` (no D3) |
| Epsilon-machine post | `/home/ubuntu/code/crw-blog/_posts/2026-01-21-Computational-Mechanics-and-Epsilon-Machines.md` | page 6 content reference (Golden Mean, Even process, mixed states); correct its overgeneralized minimality claim, and do not follow its use of "upsilon machine" for the mixed-state presentation (appendix D) |
| Programme post, part III | published at `charlesr-w.github.io/crw-blog` ("Slouching Towards Interpretability", Nov 2026); local copy `crw-blog/_posts/2026-11-14-Gradients-and-Circuits.md` on `origin/main` | quotation on pages 0/10; whiteboards `niels-hankel.jpg`, `spectral-receptive-fields.jpg`, `towards-spectral-interp.jpg` (under `assets/images/lw/Gradients-and-Circuits/`) may be reused on pages 7 and 10 with credit; the ResNet teaser `image-1.png` is **not** used (it is a ResNet-18 run that matches no study quoted on page 10) |
| NCS theorem register | `/home/ubuntu/code/CoherentModes/THEOREMS.md`, `SPARSITY.md`, `THEORY.md` | pages 4, 5, 10 bounds (cite by number and line) |
| NCS joint report (ViT/Mamba/Pythia) | `/home/ubuntu/code/CoherentModes/explore/ncs_report/site/assets/fig/{hero_vit,hero_mamba,view_vit-*,view_m-*}.png` (+ `phone/`); facts `site/assets/ncs.json` (`facts` keys); live report `site/index.html`; viewer `viewer/site/` (36 MB: link to the published report, do not copy) | page 10 results; quote numbers only via their fact keys |
| Mamba study | `/home/ubuntu/code/CoherentModes/explore/mamba_coherent/` (`page/content/findings.html`, `page/build/m130/fig/`) | page 10 detail and negative results |
| Pythia study | `/home/ubuntu/code/CoherentModes/explore/lm_coherent/` (`SPEC.md`, `data/p160t/`) | page 10 (the published numbers are `o.py.*` in `ncs.json`: matched Jaccard to sources 0.17-0.24 at step 0, 0.68-0.79 at step 512, 0.65-0.84 at the end; both come from one stored array, `explore/lm_coherent/data/p160t/blocks_143000.npz` `reading_src_jacc[:, 1]`: `o.py.final` covers all six layers, while the superseded Pythia page's `rd.sj.L4_12` (0.79-0.84) covers layers 4-12 only; the ranges near `ncs_report/NOTES.md:76-78` are from the Mamba v1 study, not Pythia — quote the fact keys) |
| ResNet/CIFAR study | `/home/ubuntu/code/CoherentModes/explore/cifar_coherent/site/assets/fig/{hero,step1..step5,seba,avgprod,static_dynamic,q_when,q_carry}.png`, `site/assets/questions.json`, `site/FINDINGS_NOTES.md` | page 10 (static vs dynamic; average vs product), page 5 (SEBA figure) |
| NCS method diagrams | `/home/ubuntu/code/CoherentModes/viz/diagrams/D1..D7.{svg,png}` | page 10 method figures |
| Planted toy | `/home/ubuntu/code/CoherentModes/pages/toy.html`, `viz/toy.py` (Sinkhorn, eigenbasis, isolated blocks) | reference implementation for `lib/graph.js` parity |
| SEBA (Python) | `/home/ubuntu/code/CoherentModes/explore/cifar_baselines/variants.py:261` (`seba_mu`), `sources.py:186` | port to `lib/seba.js`. The original `gfroyland/SEBA` (MATLAB/Julia) has no clear licence file; do not copy it |
| Literature digest | `/home/ubuntu/.t3/scratch/2026-11-17-i-want-to-write-a-3446692a/digests/literature.md` | citation checks and gap list (appendix C marks what was checked) |

Not to be used as sources or linked: the programme's "analogue computation" sequence
(`/home/ubuntu/code/BootlegInkhaven/analogue-computation/`) and the Laplacian post drafts and figures
(`/home/ubuntu/code/BootlegInkhaven/posts/`, `figures/`). Their ideas may inform design; do not copy files, quote,
or link them.

Third-party figures (Janiak et al., Zhu et al., Golowich et al., Pughe-Sanford et al.): link and describe; redraw a
schematic if needed; do not embed their images.

### 7.2 To be built

| item | owner | notes |
|---|---|---|
| Ported shell with 12 tabs, ledger/connections/mapCard components, bowtie | design system | section 6 |
| `tools/build_example.py` + `site/data/example/*.json` | example owner | section 3; assertions listed there |
| `js/lib/*` numerics + parity tests | shared numerics owner | 6.3, 6.7 |
| `tools/capture.sh` | design system | 6.6 |
| 11 pages (content + modules + page data) | page writers | per-page specs |
| Reference tab (notation, glossary, ledgers, bibliography) | design system | rendered from appendices |

---

## 8. PLACEHOLDER: marking schematic or open links

**To be specified by the programme's author.** This section will define how pages mark claims and links that are
schematic, open, or conjectural.

Until then, and only so that nothing is lost:
- the relation symbols `=`, `≈`, `~` of the connection matrix (2.2) are the only status markers on the site;
- a writer who states a `~` link, or any claim whose support is a motivation rather than a theorem, construction or
  widget demonstration, wraps the sentence in `<span class="status" data-status="schematic">…</span>` (no visible
  styling yet) and lists it in the per-page spec's "Claims" table with support type "motivation";
- no other claim-status machinery (verdict chips, confidence levels, colour codes) is to be built.

---

## 9. Build order and definition of done

### 9.1 Build order

1. **Design system port** (6.2-6.5) with placeholder pages; `capture.sh`. Gate: every tab loads, zero console
   errors.
2. **Running example**: `build_example.py` (all assertions pass), `lib/example.js`, `lib/rng.js`, parity tests.
   Gate: section 3.2's expected spectrum confirmed or the spec amended with the computed values.
3. **Shared numerics**: `lib/linalg.js`, `lib/hankel.js`, `lib/graph.js`, `lib/seba.js`, `lib/lti.js`, `lib/cca.js`
   with parity tests.
4. **Page 1** (the worked model). Gate: it meets 9.2; the template is amended with anything it revealed.
5. **Pages 3 and 4** (the spectral core used by 5, 7, 10).
6. **Pages 2, 5, 6** (parallel).
7. **Pages 7, 8, 9** (parallel).
8. **Page 10** (needs every ledger).
9. **Page 0 and Reference** (need thumbnails, ledgers, and the final connection list).
10. **Consistency pass**: notation, ledger numbers from builder output, connection symbols identical across pages,
    fallbacks regenerated, accessibility and phone screenshots.

Steps 5-7 can run in parallel once 1-3 are done. A cross-family review (a GPT reviewer for Claude-written pages, and
vice versa) of each page's claims table against its sources is part of step 10.

### 9.2 Definition of done for a page

- [ ] Follows its per-page spec; deviations recorded in the spec's change log.
- [ ] Skim path (5.1) reads as a true, simplified account; headings are claims.
- [ ] Length within 5.2; no disclosure needed for the main path.
- [ ] Every claim in the spec's claims table appears with its support; every cited bound states its hypotheses.
- [ ] Nothing from appendix D is claimed; every `~` link carries the section 8 hook.
- [ ] Running example used as specified; its face named in captions; strain stated where the spec says.
- [ ] Every number about the running example comes from builder output or a live computation, never typed by hand.
- [ ] Every figure: title, `fig-sub`, Plotted/Values caption, alt text; synthetic data labelled.
- [ ] Every live widget: ≤ 4 primary controls, tours, URL state, default = first tour, entry in
      `data/<id>/widgets.json`, fallback PNG (+ GIF if animated) generated by `capture.sh` and shown if the widget
      fails to mount (test by forcing `init` to throw).
- [ ] Connections strip lists exactly the matrix edges touching the page, with the same symbols.
- [ ] Ledger present, seven rows, numbers filled.
- [ ] Notation per appendix A; page-local symbols introduced on the page.
- [ ] Sources section complete; citations match appendix C.
- [ ] Zero console errors; screenshots at 1440 × 900 and 390 × 844 inspected; performance budgets met; keyboard
      operable; reduced motion respected.

---

## Appendix A. Notation (binding)

Global symbols (same meaning on every page):

| symbol | meaning |
|---|---|
| r | resolution: number of retained modes, states or sets |
| $\sigma_i$ | singular values, descending, $\sigma_1$ the largest; the trivial (constant) mode is included and counted |
| $\lambda_i$ | eigenvalues of a Markov / transfer / Koopman / walk operator, descending, $\lambda_1 = 1$ trivial |
| $\mu_i$ | Laplacian eigenvalues, ascending, $\mu_1 = 0$; $\mu_i = 1 - \lambda_i$ for walks |
| $\nu_i$ | relaxation rates of a generator, $\lambda_i = e^{-\nu_i\tau}$ |
| $\delta_r$ | spectral gap separating the top-r block from the rest |
| $H$, $H_r$ | Hankel table / operator and its rank-r truncation |
| $p, f$ | a past (prefix) and a future (suffix); $\mathcal A$ the alphabet, $\mathcal A^*$ all words |
| $\mathcal K_\tau, \mathcal P_\tau, \mathcal L$ | Koopman operator, transfer operator, generator |
| $\tau, \Delta, t$ | lag, sampling interval, time |
| $(A, B, C)$, $G$ | state-space system and its transfer function; $W_c, W_o$ controllability and observability Gramians |
| $P, M, L, W$ | graph random walk (Sinkhorn-balanced in NCS), lazy walk $(I+P)/2$, graph Laplacian, edge weights |
| β, $k_{\rm nn}$ | kernel inverse bandwidth, nearest-neighbour count |
| ε | spectral sparsifier accuracy |
| $x, V, D, \pi$ | particle state, potential, diffusion coefficient, equilibrium density |
| $y, \sigma_y, s_t$ | readout, its noise std, symbols in $\{\texttt a,\texttt b,\texttt c\}$ |
| $w_1..w_4$; L, R | wells; left and right pairs |
| $x^{(\ell)}, P^{(\ell)}, \bar M$ | layer-ℓ points/activations, layer-ℓ walk, block-averaged walk (NCS) |
| $n_c$ | number of causal states |
| d | hidden / ISAN dimension |
| T S P Z R I | budget terms (4.3) |

Shared by several pages (same meaning wherever used; each page introduces them):

| symbol | meaning | pages |
|---|---|---|
| ϑ, $r_\vartheta$ | retention threshold; number of retained modes above it (S.10) | 3, 4, 10 |
| η | the S.8 / partition residual $\|(I - VV^\top)H\|_F$ (page 4: its square bounded by conductances) | 4, 5, 10 |
| c | S.8's threshold margin $\min_j(1 - \mu\sqrt{n_j})$ | 5, 10 |
| μ (no index) | SEBA threshold; with an index, $\mu_i$ is always a Laplacian eigenvalue | 5, 10 |
| $\eta_{\rm fail}$ | failure probability of a sampling bound (the register writes η) | 10 (and 4.3) |
| $b_K$ | kernel log-range in A.23 (the register writes b) | 10 (and 4.3) |
| $d_f$, $d_c$ | the ideal companion's fine and coarse prototype distances (the register's δ, Δ; 3.8) | 10 |
| $W_{\rm lift}$, $c_{\rm lift}$ | face C's lift (3.5) | 10 |
| s | Gaussian kernel bandwidth on positions; β = 1/(2s²) | 4, 5 |
| H (S.8) | a candidate partition's normalized indicator matrix; a side note says it is not the Hankel H | 4 (as $g_j$ columns), 5, 10 |
| $\pi_0, \pi_\tau$ | the state's distributions at times 0 and τ (both π at equilibrium) | 3 (and 4.2) |

Page-local symbols (allowed only on the named page, introduced there, with a side note wherever they collide with a
symbol above or on another page):
- page 2: d = (1,1)/√2 (the push direction of 3.4; not the ISAN dimension d), u, z (input, output), h(t), $h_k$, Γ, $\mathcal C$, $\mathcal O$, $\mathbf H$, $A_d$, $B_d$, T (state
  transformation), Σ, $\Sigma_x$, E (noise Hankel), η (measurement-noise level, page 2 only), B for face B's input
  operator (3.4);
- page 3: $\phi_i$, $\psi_i$ (present- and future-side singular functions), $\chi_j$ (dictionary), $\hat K$, $\hat
  C_{00}$, $\hat C_{0\tau}$, $Q_\ell$, $u_i$, $v_i$, μ (a sampling measure in EDMD convergence statements only);
- page 4: $\mathbf D = \mathrm{diag}(d_x)$ (degree matrix, bold to keep D for diffusion), $h(G)$, $\rho_G(k)$, $\phi(A)$ (conductance), $L_{\rm rw}$, $L_{\rm sym}$, α (diffusion-map exponent),
  U, $\mathcal L_\epsilon$ and ε (Froyland's noisy transfer operator and noise scale), $\Delta^D$, $h^D$, $t_\times$;
- page 5: $\tilde L$, $P_*$, $\hat\varepsilon$, $R_{xy}$, $w_e$, q, $p_e$, R and S (SEBA rotation and output), $n_j$,
  $\eta_*$, $e_Z$;
- page 6: $\beta_{\rm IB}$, $C_\mu$, X and Z (micro and macro processes), Q (step projector), E(k), and the
  Sarich-Noé-Schütte δ (projection error) and η (spectral ratio), $r_{\rm SNS}$, $\Delta_{\rm SNS}$ — δ and η glossed at
  every use, never written $\delta_r$, never confused with η above;
- page 7: $\mathcal A, \mathcal B$ (a coherent pair; not the alphabet), $\mathcal F_\tau$, $\mathbf D$ (OU noise
  covariance), m, g, $C_{pp}, C_{pf}, C_{ff}$, M (whitened cross-covariance), $a_i$, $r^\pm$;
- page 8: HebbianHarmonics notation, adjusted: $B$, $N$, $g$, $u$, $\mathcal H$ for the harmonic extension with rows
  $h_i$ (calligraphic to keep $H$ for Hankel), $\Sigma_g$, $\Sigma_g(\tau_s)$, θ, $w_{\min}$, γ, $\tau_s$, Q (the
  shifted covariance; HebbianHarmonics writes A), S, c (a part's eigenvalue), q (HebbianHarmonics' μ), K, ζ
  (HebbianHarmonics' b), $\mathcal D_{ij}$ (HebbianHarmonics' D), $P_\perp$ (contrast projector), $\hat C$;
- page 9: Λ (extended logit table), h, f, s (history, continuation, next token), T (sequence length), $q_t$, $A_{s,t}$,
  $B_t$ (ISAN), α (power-law exponent);
- page 10: THEOREMS notation ($S_{\max}$, $B_0$, $h_N$, $E_N$, $E_Q$, $\ell_N$), $\alpha_{\rm tol}$ (A.43-A.44's α), the
  4.3 objects $P^{\rm used}$, $P^{\rm ideal}_N$, $P_{\star,\rm ref}$ (reference population operator), $e_F$,
  $\delta_{\rm lb}$ (population-gap lower bound), Q (ordered product), V, $V_0$, F, $\psi_i$; $m_\ell$ (stored
  quadrature estimate of the lift's population mean, 3.5).
- page 1: $A_s$, α, β (automaton weights; this β is not the kernel bandwidth), $H_s$, R, O, $b_p$.

**Index shift when quoting CoherentModes:** `THEOREMS.md` and `SPARSITY.md` write $\lambda_1$ for the top
*nontrivial* eigenvalue and $\mu_1 = 1 - \lambda_1$. On this site that is $\lambda_2$, $\mu_2$. Quote with the shift
and say so once per page.

Sign convention: Laplacians are positive semidefinite on this site; Froyland writes a nonpositive dynamic Laplacian
($h^D \le 2\sqrt{-\lambda_2^D}$); quote with a note.

## Appendix B. Glossary: terms that change meaning between fields

Each page's first use of these terms links to this glossary (Reference tab).

| term | meanings to keep apart |
|---|---|
| state | hidden state of a generator (HMM); predictive state (vector of future-test probabilities, PSR); belief state (posterior over hidden states); causal state (class of pasts with equal future law); state-space vector of an LTI system; a coherent set read as a "computational state" (candidate only) |
| Hankel matrix | probability Hankel of a process $P(pf)$; conditional Hankel $P(f \mid p)$; block Hankel of Markov parameters $CA^{i+j}B$ (control); trajectory / delay Hankel of a time series (HAVOK); extended logit matrix (Golowich et al.). Different objects, different ranks |
| rank | exact matrix rank; numerical rank at a tolerance; Hankel rank (minimal linear realization); logit rank; effective rank / participation ratio; "context rank" (CoherentModes) |
| realization | a state-space or automaton model reproducing given input-output behaviour (control, automata); a stochastic realization (Markovian representation of a process); not "an instance" |
| minimal | fewest states among linear realizations (Hankel rank) vs fewest among prescient predictive representations (ε-machine) vs fewest nonnegative HMM states; these differ |
| observable | a function of state (Koopman, physics); observability of a state from outputs (control) |
| closed / closure | invariant subspace (Koopman, realization: the dynamics maps it into itself); closed macro-variable (computational mechanics: information, causal, computational closure); "closed form" |
| coherent set | finite-time set that stays together under transport (Froyland); almost-invariant / metastable set (autonomous case); NCS coherent set (a SEBA set of a data-point walk) |
| mode | eigenfunction / singular function; a vibration mode (ERA); a well in the example; a v2 Hebbian population mode |
| kernel | null space; similarity function (kernel methods); memory kernel (Mori-Zwanzig); transition kernel |
| conductance | cut weight over set volume (graph theory); electrical conductance of an edge (resistor networks, page 8) |
| transfer | transfer operator (pushes densities forward); transfer function (control, Laplace domain); transfer learning (ML) |
| spectral | of eigen/singular values (linear algebra); of frequency content (signal processing) |
| sparse | sparse code / SAE activations; sparse graph (few edges); sparse regression (SINDy); sparse eigenvectors (SEBA) |
| temperature | physical noise level (here D); kernel inverse bandwidth β (NCS); softmax temperature |
| cell | activation cell / stable region (Janiak et al.); Voronoi cell; grid cell of a discretization |
| plateau | activation plateau (output insensitive to small perturbations); loss plateau in training |
| site | (CoherentModes) an observation / data point; (exploratory CoherentModes pages) a layer location |
| retention | Rayleigh quotient $f^\top M f/\|f\|^2$ (NCS), not memory |
| causal | causal state (predictive equivalence) vs causal intervention / causal graph |
| Markov blanket | statistical: a set making the inside conditionally independent of the outside (Pearl); the free-energy literature's usage; on this site only schematic |

## Appendix C. Master bibliography

Check status from the literature digest: **P** paper text checked; **A** abstract checked; **M** metadata only;
**W** checked by web search during this spec or a page spec; **V** to verify before publication. Per-page specs copy
entries from here.

General linear algebra and perturbation
- Schmidt, E. (1907). Zur Theorie der linearen und nichtlinearen Integralgleichungen. *Math. Ann.* 63, 433-476
  (best low-rank approximation of compact operators). [V]
- Eckart, C. & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika* 1(3),
  211-218. [V]
- Weyl, H. (1912). Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen.
  *Math. Ann.* 71, 441-479 (eigenvalue perturbation inequality). [V]
- Wedin, P.-Å. (1972). Perturbation bounds in connection with singular value decomposition. *BIT* 12, 99-111. [V]
- Stewart, G. W. & Sun, J.-G. (1990). *Matrix Perturbation Theory*. Academic Press (optional; as cited in the
  register). [M]
- Parlett, B. N. (1998). *The Symmetric Eigenvalue Problem*. SIAM Classics (residual bound, §4.5). [V]
- Birkhoff, G. (1957). Extensions of Jentzsch's theorem. *Trans. AMS* 85, 219-227 (strictly positive matrices
  contract Hilbert's projective metric); textbook form: Seneta, E. (2006). *Non-negative Matrices and Markov Chains*,
  rev. ed., Springer, ch. 3 (Birkhoff's contraction coefficient). [V] (page 1's causal-state argument)
- Sinkhorn, R. & Knopp, P. (1967). Concerning nonnegative matrices and doubly stochastic matrices. *Pacific J. Math.*
  21(2), 343-348 (scaling exists iff total support; unique for fully indecomposable matrices). [V; as cited in
  CoherentModes `SPARSITY.md` S.2]
- Csima, J. & Datta, B. N. (1972). The DAD theorem for symmetric non-negative matrices. *J. Combin. Theory A* 12,
  147-152. [V; as cited in CoherentModes `SPARSITY.md` S.2]
- Rump, S. M. (2006). Verification of positive definiteness. *BIT Numer. Math.* 46, 433-452. Theorem 2.3 and
  Corollaries 2.4 and 2.7: if floating-point Cholesky (rounding to nearest, any evaluation order, underflow allowed)
  runs to completion on the symmetric floating-point matrix A with its diagonal lowered by $c + r$, where $c \ge
  \gamma_{n+1}(1-\gamma_{n+1})^{-1}\mathrm{tr}(A) + 3n(2n + \max_i a_{ii})\,\mathtt{eta}$ (bound I of §3; $\gamma_k =
  ku/(1 - ku)$, $\mathtt{eta} = 2^{-1074}$) and $r \ge \|R\|_2$ for an entrywise radius R, then every symmetric X with
  $|X - A| \le R$ is positive definite; the lowered diagonal is formed without directed rounding by Lemma 2.5 /
  (2.11). [V: read 17 Nov 2026 (author's PDF, tuhh.de/ti3/paper/rump/Ru06c.pdf)] (page 5's certified ε; page 10's
  verified $e_P$)
- Engel, K.-J. & Nagel, R. (2000). *One-Parameter Semigroups for Linear Evolution Equations*. GTM 194, Springer
  (resolvent as Laplace transform of the semigroup; page 8). [V]

Realization, automata, predictive states
- Ho, B. L. & Kalman, R. E. (1966). Effective construction of linear state-variable models from input/output
  functions. *Regelungstechnik* 14, 545-548. [A]
- Fliess, M. (1974). Matrices de Hankel. *J. Math. Pures Appl.* 53, 197-224. [V]
- Carlyle, J. W. & Paz, A. (1971). Realizations by stochastic finite automata. *J. Comput. Syst. Sci.* 5, 26-40. [V]
- Jaeger, H. (2000). Observable operator models for discrete stochastic time series. *Neural Computation* 12(6),
  1371-1398. [V]
- Littman, M. L., Sutton, R. S. & Singh, S. (2002). Predictive representations of state. *NIPS 14*. [P]
- Hsu, D., Kakade, S. M. & Zhang, T. (2012). A spectral algorithm for learning hidden Markov models. *JCSS* 78(5),
  1460-1480. arXiv:0811.4413. [A]
- Boots, B., Siddiqi, S. M. & Gordon, G. J. (2011). Closing the learning-planning loop with predictive state
  representations. *IJRR*. [A]
- Balle, B., Carreras, X., Luque, F. M. & Quattoni, A. (2014). Spectral learning of weighted automata: a
  forward-backward perspective. *Machine Learning* 96, 33-63. [P]
- Balle, B., Panangaden, P. & Precup, D. (2019). Singular value automata and approximate minimization. *MSCS* 29(9),
  1444-1478. arXiv:1711.05994. [P, Thm 7.1]
- Balle, B., Lacroce, C., Panangaden, P., Precup, D. & Rabusseau, G. (2021). Optimal spectral-norm approximate
  minimization of weighted finite automata. *ICALP*, LIPIcs 198, 118. arXiv:2102.06860. [P]
- Lacroce, C., Balle, B., Panangaden, P. & Rabusseau, G. (2023). Optimal approximate minimization of one-letter
  weighted finite automata. arXiv:2306.00135. [P]

Control
- Moore, B. C. (1981). Principal component analysis in linear systems: controllability, observability, and model
  reduction. *IEEE TAC* 26(1), 17-32. [M] (introduced balancing)
- Kalman, R. E. (1963). Mathematical description of linear dynamical systems. *J. SIAM Control A* 1(2), 152-192
  (canonical decomposition into controllable/observable parts; minimal realization). [V] (page 2's minimal
  realization step)
- Pernebo, L. & Silverman, L. M. (1982). Model reduction via balanced state space representations. *IEEE TAC* 27(2),
  382-387. [V] (stability of balanced truncation)
- Enns, D. F. (1984). Model reduction with balanced realizations: an error bound and a frequency weighted
  generalization. *Proc. 23rd IEEE CDC*, 127-132. [W: attribution of the 2Σ bound; page range V]
- Zhou, K., Doyle, J. C. & Glover, K. (1996). *Robust and Optimal Control*. Prentice Hall (chs. 3, 7, 8). [V]
- Glover, K. (1984). All optimal Hankel-norm approximations of linear multivariable systems and their L∞-error
  bounds. *Int. J. Control* 39(6), 1115-1193. [A] (the 2Σ bound, with Enns 1984; its L∞ tail bound for
  Hankel-norm approximants is quoted only after checking the exact statement)
- Adamyan, V. M., Arov, D. Z. & Krein, M. G. (1971). Analytic properties of Schmidt pairs for a Hankel operator and
  the generalized Schur-Takagi problem. [M]
- Juang, J.-N. & Pappa, R. S. (1985). An eigensystem realization algorithm. *J. Guidance* 8(5), 620-627. [A]
- Rahn, B. (2001). A balanced truncation primer. arXiv:quant-ph/0112066. [P]
- Desai, U. B. & Pal, D. (1984). A transformation approach to stochastic model reduction. *IEEE TAC* 29(12),
  1097-1100. DOI 10.1109/TAC.1984.1103438. [W: abstract-level; links CCA and balanced stochastic realization]
- Oymak, S. & Ozay, N. (2019). Non-asymptotic identification of LTI systems from a single trajectory. *Proc. ACC
  2019*, 5655-5661. arXiv:1806.05722. [W: venue and pages; check theorem statements in the arXiv text before quoting
  hypotheses]
- Kubo, R. (1966). The fluctuation-dissipation theorem. *Rep. Prog. Phys.* 29, 255-284. [V]
- Risken, H. (1989). *The Fokker-Planck Equation*, 2nd ed. Springer. [V]

Koopman, transfer operators, delays
- Koopman, B. O. (1931). Hamiltonian systems and transformation in Hilbert space. *PNAS* 17(5), 315-318. [V]
- Mezić, I. (2005). Spectral properties of dynamical systems, model reduction and decompositions. *Nonlinear Dynamics*
  41, 309-325. [V]
- Tu, J. H., Rowley, C. W., Luchtenburg, D. M., Brunton, S. L. & Kutz, J. N. (2014). On dynamic mode decomposition:
  theory and applications. *J. Comput. Dyn.* 1(2), 391-421. [W]
- Brunton, S. L., Brunton, B. W., Proctor, J. L. & Kutz, J. N. (2016). Koopman invariant subspaces and finite linear
  representations of nonlinear dynamical systems for control. *PLoS ONE* 11(2), e0150171. [W: the paper does state
  that a finite invariant subspace containing the state requires a single isolated fixed point, but the statement
  has counterexamples without further qualification ($\dot x = 0, \dot y = -y$; rotation on a circle); the site cites
  the paper for Koopman invariant subspaces and control, and does **not** rely on that statement (page 3 uses a direct
  polynomial-degree argument for the drift and a generator-domain (Neumann) argument for the reflected diffusion)]
- Boninsegna, L., Nüske, F. & Clementi, C. (2018). Sparse learning of stochastic dynamical equations. *J. Chem.
  Phys.* 148, 241723. [W]
- Klus, S., Nüske, F., Peitz, S., Niemann, J.-H., Clementi, C. & Schütte, C. (2020). Data-driven approximation of the
  Koopman generator: model reduction, system identification, and control. *Physica D* 406, 132416. [W: SINDy as a
  special case of generator EDMD]
- Noé, F. & Nüske, F. (2013). A variational approach to modeling slow processes in stochastic dynamical systems.
  *Multiscale Model. Simul.* 11(2), 635-655. arXiv:1211.7103. [W; journal details V]
- Klus, S. & Djurdjevac Conrad, N. (2024). Dynamical systems and complex networks: a Koopman operator perspective.
  *J. Phys. Complexity* 5(4), 041001. [M, as cited by Pughe-Sanford et al.]
- Pavliotis, G. A. (2014). *Stochastic Processes and Applications*. Texts in Applied Mathematics 60, Springer (OU
  spectrum, Hermite eigenfunctions). [V]
- Akaike, H. (1975). Markovian representation of stochastic processes by canonical variables. *SIAM J. Control*
  13(1), 162-173. [A]
- Granger, C. W. J. & Morris, M. J. (1976). Time series modelling and interpretation. *J. R. Stat. Soc. A* 139(2),
  246-257 (a sum of independent AR processes is ARMA, not finite-order AR). [V] (page 7's delay-state disclosure)
- Schmid, P. J. (2010). Dynamic mode decomposition. *J. Fluid Mech.* 656, 5-28. [A]
- Williams, M. O., Kevrekidis, I. G. & Rowley, C. W. (2015). A data-driven approximation of the Koopman operator
  (EDMD). *J. Nonlinear Sci.* 25, 1307-1346. [A]
- Korda, M. & Mezić, I. (2018). On convergence of extended dynamic mode decomposition to the Koopman operator.
  *J. Nonlinear Sci.* 28, 687-710. [V]
- Brunton, S. L., Brunton, B. W., Proctor, J. L., Kaiser, E. & Kutz, J. N. (2017). Chaos as an intermittently
  forced linear system (HAVOK). *Nat. Commun.* 8, 19. [A]
- Brunton, S. L., Proctor, J. L. & Kutz, J. N. (2016). Discovering governing equations from data (SINDy). *PNAS*
  113(15), 3932-3937. [A]
- Takens, F. (1981). Detecting strange attractors in turbulence. LNM 898, 366-381. [P]
- Arbabi, H. & Mezić, I. (2017). Ergodic theory, DMD, and computation of spectral properties of the Koopman
  operator. *SIADS*. [A]
- Klus, S., Nüske, F., Koltai, P., Wu, H., Kevrekidis, I., Schütte, C. & Noé, F. (2018). Data-driven model reduction
  and transfer operator approximation. *J. Nonlinear Sci.* 28, 985-1010. [V]
- Klus, S., Husic, B. E., Mollenhauer, M. & Noé, F. (2019). Kernel methods for detecting coherent structures in
  dynamical data. arXiv:1904.07752. [A]
- Wu, H. & Noé, F. (2020). Variational approach for learning Markov processes from time series data (VAMP).
  *J. Nonlinear Sci.* arXiv:1707.04659. [A]

Spectral graph theory, coherent sets, sparsity
- Froyland, G. (2013). An analytic framework for identifying finite-time coherent sets in time-dependent dynamical
  systems. *Physica D* 250, 1-19. [V; Thm 2 as recorded in CoherentModes `SPARSITY.md` S.4 notes]
- Froyland, G. (2015). Dynamic isoperimetry and the geometry of Lagrangian coherent structures. *Nonlinearity* 28,
  3587-3622. arXiv:1411.7186. [P: Def. 2, eq. (15), Thm 2.1 (Federer-Fleming), Thm 3.2 (dynamic Cheeger), Cor 3.5
  (multistep), Thm 5.1 (small-diffusion limit); flat manifold, volume-preserving maps]
- Froyland, G. & Kwok, E. (2017). A dynamic Laplacian for identifying Lagrangian coherent structures on weighted
  Riemannian manifolds. *J. Nonlinear Sci.* [P]
- Froyland, G. (2024). A tutorial on the dynamic Laplacian. arXiv:2408.04149. [P]
- Froyland, G., Rock, C. P. & Sakellariou, K. (2019). Sparse eigenbasis approximation (SEBA). *CNSNS* 77, 81-107.
  arXiv:1812.02787. [P]
- Froyland, G. & Rock, C. P. (2025). Higher Cheeger ratios of features in Laplace-Beltrami eigenfunctions. *ACHA* 74,
  101710. arXiv:2308.04850. [P]
- Chung, F. R. K. (1997). *Spectral Graph Theory*. CBMS 92, AMS (Cheeger inequality; co-area form). [V]
- Cheeger, J. (1970). A lower bound for the smallest eigenvalue of the Laplacian. In *Problems in Analysis*,
  Princeton, 195-199 (named only). [M]
- Levin, D. A. & Peres, Y. (2017). *Markov Chains and Mixing Times*, 2nd ed. AMS (bottleneck ratio; Thm 13.10). [M]
- Shi, J. & Malik, J. (2000). Normalized cuts and image segmentation. *IEEE TPAMI* 22(8), 888-905. [M]
- von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing* 17(4), 395-416 (incl.
  Prop. 2). [M]
- Peng, R., Sun, H. & Zanetti, L. (2017). Partitioning well-clustered graphs: spectral clustering works! *SIAM J.
  Comput.* 46(2), 710-743; arXiv:1411.2021. [P: Thm 1.1]
- Foster, R. M. (1949). The average impedance of an electrical network. In *Contributions to Applied Mechanics
  (Reissner Anniversary Volume)*, 333-340. [V; may be cited via Spielman & Srivastava 2011]
- Spielman, D. A. & Teng, S.-H. (2011). Spectral sparsification of graphs. *SIAM J. Comput.* 40(4), 981-1025
  (further reading). [M]
- Doyle, P. G. & Snell, J. L. (1984). *Random Walks and Electric Networks*. Carus Mathematical Monographs 22, MAA.
  [W]
- Lee, J. R., Oveis Gharan, S. & Trevisan, L. (2014). Multiway spectral partitioning and higher-order Cheeger
  inequalities. *J. ACM* 61(6), 37. [P]
- Louis, A., Raghavendra, P., Tetali, P. & Vempala, S. (2012). Many sparse cuts via higher eigenvalues. *STOC*. [A]
- Kwok, T. C., Lau, L. C., Lee, Y. T., Oveis Gharan, S. & Trevisan, L. (2013). Improved Cheeger's inequality. *STOC*.
  [A]
- Spielman, D. A. & Srivastava, N. (2011). Graph sparsification by effective resistances. *SIAM J. Comput.* 40(6),
  1913-1926. [A]
- Batson, J., Spielman, D. A. & Srivastava, N. (2012). Twice-Ramanujan sparsifiers. *SIAM J. Comput.* 41(6),
  1704-1721. [P]
- Ng, A. Y., Jordan, M. I. & Weiss, Y. (2002). On spectral clustering. *NIPS 14*. [A]
- Davis, C. & Kahan, W. M. (1970). The rotation of eigenvectors by a perturbation III. *SIAM J. Numer. Anal.* 7(1),
  1-46. [A]
- von Luxburg, U., Belkin, M. & Bousquet, O. (2008). Consistency of spectral clustering. *Ann. Stat.* 36(2),
  555-586. [A]
- Belkin, M. & Niyogi, P. (2003, 2007). Laplacian eigenmaps; Convergence of Laplacian eigenmaps. [A]
- Coifman, R. R. & Lafon, S. (2006). Diffusion maps. *ACHA* 21(1), 5-30. [V]
- Nadler, B., Lafon, S., Coifman, R. R. & Kevrekidis, I. G. (2006). Diffusion maps, spectral clustering and
  reaction coordinates of dynamical systems. *ACHA* 21(1), 113-127. arXiv:math/0503445. [P: eq. (27); α = 0 gives
  potential 2U, α = 1/2 the Langevin generator, α = 1 Laplace-Beltrami]
- Banisch, R. & Koltai, P. (2017). Understanding the geometry of transport: diffusion maps for Lagrangian trajectory
  data unravel coherent sets. *Chaos* 27, 035804. arXiv:1603.04709. [P: Thm 3, Remark 4]
- Zhu, X., Ghahramani, Z. & Lafferty, J. (2003). Semi-supervised learning using Gaussian fields and harmonic
  functions. *ICML*. [P]
- Deuflhard, P. & Weber, M. (2005). Robust Perron cluster analysis in conformation dynamics. *Linear Algebra Appl.*
  398, 161-184. [V]
- Sarich, M., Noé, F. & Schütte, C. (2010). On the approximation quality of Markov state models. *Multiscale Model.
  Simul.* 8(4), 1154-1177. DOI 10.1137/090764049. [P: Thm 3.1 (eqs (27)-(32)), assumptions (7), (8), (12), (13),
  Thm 3.3, §4.1; quoted on page 6]

Computational mechanics, information
- Crutchfield, J. P. & Young, K. (1989). Inferring statistical complexity. *PRL* 63, 105. [M]
- Shalizi, C. R. & Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and
  simplicity. *J. Stat. Phys.* 104, 817-879. [P]
- Shalizi, C. R. & Klinkner, K. L. (2004). Blind construction of optimal nonlinear recursive predictors (CSSR).
  *UAI*. [M]
- Haslinger, R., Klinkner, K. L. & Shalizi, C. R. (2010). The computational structure of spike trains. *Neural
  Computation* 22(1), 121-157. [P, App. C]
- Tishby, N., Pereira, F. C. & Bialek, W. (1999). The information bottleneck method. *Proc. 37th Allerton
  Conference*, 368-377; arXiv:physics/0004057. [V]
- Slonim, N. & Tishby, N. (2000). Agglomerative information bottleneck. *NIPS 12*, 617-623. [V]
- Chechik, G., Globerson, A., Tishby, N. & Weiss, Y. (2005). Information bottleneck for Gaussian variables. *JMLR* 6,
  165-188. [W]
- Greenacre, M. J. (1984). *Theory and Applications of Correspondence Analysis*. Academic Press. [M]
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann (Markov blanket). [M]
- Marzen, S. E. & Crutchfield, J. P. (2017). Nearly maximally predictive features and their dimensions. *Phys. Rev.
  E* 95, 051301(R). [V: candidate original source of the Mess3 process; check which paper introduced Mess3 before
  attributing it]
- Still, S., Crutchfield, J. P. & Ellison, C. J. (2010). Optimal causal inference. *Chaos* 20(3), 037111. [A]
- Creutzig, F., Globerson, A. & Tishby, N. (2009). Past-future information bottleneck in dynamical systems. *PRE*
  79, 041925. [A]
- Rosas, F. E., Geiger, B. C., Luppi, A. I., Seth, A. K., Polani, D., Gastpar, M. & Mediano, P. A. M. (2024).
  Software in the natural world: a computational approach to hierarchical emergence. arXiv:2402.09090. [W: υ-machine
  §III.1 and Def. 2; informational closure Def. 4; causal closure Def. 3 (ε- and υ-machines equivalent);
  computational closure Def. 5; lumpability Def. 7; Thms 1-3; modular random walk §IV.4; Hopfield §IV.6]
- Kemeny, J. G. & Snell, J. L. (1960). *Finite Markov Chains* (lumpability). [M]

Neurons and Hebbian learning
- Pughe-Sanford, J. L., Ding, X., Moore, J. J., Sengupta, A. M., Epstein, C., Greengard, P. & Chklovskii, D. B.
  (2025). Neurons as detectors of coherent sets in sensory dynamics. *NeurIPS 38*. arXiv:2510.26955. [P]
- Oja, E. (1982). A simplified neuron model as a principal component analyzer. *J. Math. Biol.* 15, 267-273. [P]
- Pehlevan, C., Hu, T. & Chklovskii, D. B. (2015). A Hebbian/anti-Hebbian neural network for linear subspace
  learning. *Neural Computation*. [A]
- Pehlevan, C., Zhao, X., Sengupta, A. M. & Chklovskii, D. (2020). Neurons as canonical correlation analyzers.
  *Front. Comput. Neurosci.* 14, 55. [P: feedforward rules called non-Hebbian by the authors, lateral anti-Hebbian;
  the CCA solution is a fixed point; multichannel convergence shown numerically]
- Lipshutz, D., Bahroun, Y., Golkar, S., Sengupta, A. M. & Chklovskii, D. B. (2021). A biologically plausible neural
  network for multichannel canonical correlation analysis. *Neural Computation* 33(9), 2309-2352. arXiv:2010.00525.
  [W: "local non-Hebbian learning rules"]
- Hardoon, D. R., Szedmak, S. & Shawe-Taylor, J. (2004). Canonical correlation analysis: an overview with application
  to learning methods. *Neural Computation* 16(12), 2639-2664. [V]
- Gel'fand, I. M. & Yaglom, A. M. (1957). Calculation of the amount of information about a random function contained
  in another such function. *Uspekhi Mat. Nauk* 12(1); English transl. *AMS Transl. (2)* 12 (1959). [V: year and
  translation details]
- Földiák, P. (1991). Learning invariance from transformation sequences. *Neural Computation* 3(2), 194-200. [W]
- Stock, C. H., Harvey, S. E., Ocko, S. A. & Ganguli, S. (2022). Synaptic balancing. *PLoS Comput. Biol.* 18(9),
  e1010418. [P]

Language models and activations
- Foerster, J. N., Gilmer, J., Sohl-Dickstein, J., Chorowski, J. & Sussillo, D. (2017). Input switched affine
  networks. *ICML*, PMLR 70, 1136-1145. [P]
- Golowich, N., Liu, A. & Shetty, A. (2025). Sequences of logits reveal the low rank structure of language models.
  arXiv:2510.24966 (v1, the only version); *ICLR* 2026. [P: Thm 4.3; Fact A.2; §§3.1-3.3. They report no rank
  measurement on nonsense histories; check figure numbering (Fig. 4 vs "Fig. 5" in the HTML text) against the
  camera-ready]
- Golowich, N., Liu, A. & Shetty, A. (2025b). Provably learning from modern language models via low logit rank.
  arXiv:2512.09892. [A]
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A. & Riechers, P. M. (2024). Transformers represent
  belief state geometry in their residual stream. arXiv:2405.15943. [W: authors]
- Janiak, J., Karwowski, J., Mangat, C. S., Giglemiani, G., Petrova, N. & Heimersheim, S. (2024). Characterizing
  stable regions in the residual stream of LLMs. arXiv:2409.17113. [P]
- Heimersheim, S. & Mendel, J. (2024). [Interim research report] Activation plateaus & sensitive directions in GPT2.
  LessWrong, 5 July 2024. [W]
- Shinkle, M. & Heimersheim, S. (2025). Activation plateaus: where and how they emerge. LessWrong, 17 Oct 2025
  (lesswrong.com/posts/WMfSbt7AAcJdHzysB; authors listed as Matthew Shinkle and "StefanHex"). [W]
- Ferreira da Silva, F. & Heimersheim, S. (2026). Evidence for feature-specific error correction in LLMs.
  arXiv:2606.24964. [A]

Programme sources (cite as the programme's own work, not as literature)
- CoherentModes theorem register: `THEORY.md`, `THEOREMS.md`, `SPARSITY.md` (repository; Lean-checked portions listed
  in `lean/README.md`).
- NCS reports: ResNet-20/CIFAR-10; joint DINOv2 ViT-S/14 + Mamba-130m report (`explore/ncs_report`).
- HebbianHarmonics site and notes.
- "Slouching Towards Interpretability" (Nov 2026), part III.

## Appendix D. Things never to claim

Use the right-hand version.

| do not claim | claim instead |
|---|---|
| Hankel rank = number of causal states | rank ≤ number of causal states (when finite); strict inequality is common; with noisy readout the running example has rank 4 and infinitely many causal states |
| distinct beliefs after finite words prove infinitely many causal states; or the hero's rising count is a causal-state count | finite-history predictive distributions from the stationary prior can multiply even for finite ε-machines (a two-state unifilar example does); causal states condition on infinite pasts; the instrument's infinitely many causal states follow from page 1's argument (strictly positive, invertible symbol matrices contract projectively, so no finite set of causal beliefs is closed under the symbol updates) |
| a rank-r truncation of a table is a smaller machine of the same kind | it is the best rank-r table; a realizable rank-r automaton follows from singular-value-automaton truncation with an ℓ² bound; it may not be a stochastic model (negative weights) |
| AAK gives optimal smaller automata / language models | constructive AAK is proved for LTI systems and one-letter automata; multi-letter is open |
| Hebbian learning finds covariance eigenvectors / does spectral clustering | v1 clusters are nonnegative eigenvectors of principal submatrices of the threshold-shifted covariance; the v2 energy/distance rule is a different learning principle; hierarchical refinement is history-dependent (shown by example) |
| weights reveal the input distribution | weights recover the contrast second moment under stated spanning conditions |
| predictive states predict logits across models on nonsense inputs; low logit rank was measured on nonsense histories | trained models' logit tables are approximately low rank; low-rank column spaces overlap between real and nonsense *continuations* and across models; generation from a target prompt works using linear combinations of nonsense *histories'* logits within a model (LINGEN); Golowich et al. report no rank measurement on nonsense histories; logit rank ≤ d ⟺ time-varying ISAN of dimension d; cross-model coefficient transfer is proposed future work |
| activation cells are polytopes / are coherent sets | activation cells are the stable regions / plateaus of Janiak et al. and the plateau reports; they are not polytopes; linking them to coherent sets and harmonic label propagation is a motivating relaxation |
| expansion coding derives activation-space analysis | it motivates looking in activation space |
| SEBA recovers the true sets | SEBA's guarantees are conditional (aligned start, exact-indicator regime, alignment existence) |
| coherent sets are the network's computational states | they are candidate coarse-grainings; closure has not been tested |
| Takens: enough delays make any time series a linear system | Takens gives a generic embedding of deterministic smooth dynamics; it says nothing about linearity, and noise needs separate care |
| spectral sparsification prunes networks safely | it is a theorem about undirected nonnegative graph Laplacians, not about pruning signed directed weights |
| resistance sampling keeps the edges that cross a barrier / crossing edges have the largest leverages | the leverages across any cut sum to at least 1, so every bottleneck is sampled and its few surviving edges are reweighted heavily; in a dense kernel graph most individual crossing edges have tiny weights and small leverages and are dropped |
| a Lanczos estimate of a sparsifier's ε is a certificate | an estimate; a certificate needs a verified check of both Loewner inequalities at a stated ε in Rump's sense (2006, Cor. 2.7: his shift plus a radius for the rounding in forming the test matrices); a Cholesky check with an ad hoc shift is a numerical check, not a certificate |
| resistance sampling always keeps a bridge | a bridge has the maximum leverage, 1, and is kept with high probability at the stated budget (it is missed with probability $(1 - 1/(n-1))^q > 0$); every successful sparsifier with ε < 1 must contain every bridge |
| every certificate divides by the gap at r | subspace certificates do; eigenvalue and operator-error bounds do not, and the gap decides whether those errors are small enough to distinguish a block; rounding also needs a small partition residual and a positive threshold margin |
| a labelling's worst-set conductance under the layer-averaged walk is the mean of its per-layer worst-set conductances | each fixed set's conductance under $\bar M$ is the mean of its per-layer conductances; for the worst set only ≤ holds (the maximum over sets does not commute with the average) |
| static clustering of activations finds the dynamics | only in special cases (reversible dynamics with density-normalized kernels, E6); otherwise one layer's operator measures geometry at that layer and a block operator measures neighbourhood persistence across the block: different questions, compared on face C by boundary cost |
| only the layer-averaged operator shows where tracked inputs end up (or came from) | the inputs are tracked, so any labelling, including the last layer's, can be drawn at every layer; on face C the last layer's sets already mark the basins; the average's sets are the ones whose boundaries are cheap across the whole block |
| every set of a k-way partition has conductance at least μ_k/2 | the higher-order Cheeger lower bound is on the worst set: $\max_j\phi(A_j) \ge \rho_G(k) \ge \mu_k/2$; individual sets can lie below it (Ncut ≥ Σ_{i≤k} μ_i is the separate sum bound) |
| finer resolution always has a smaller spectral gap, so bounds always worsen with r | truncation error falls with r; certificates depend on the gap at the chosen r, which is not monotone; the scale knob (lag, bandwidth) decides which r is well separated |
| the singular functions of an OU process are linear / linear CCA recovers the Koopman SVD | the leading nontrivial one is linear; higher ones are Hermite polynomials; linear CCA recovers the linear sector |
| an observable linear-Gaussian state-space process has an exact finite lag-vector state | its optimal predictive state is finite-dimensional, but in general it depends on the whole past through a filter (a scalar readout of a multidimensional linear system is ARMA, not finite-order AR); a finite window of raw observations is a dictionary, generally an approximation |
| a finite Koopman-invariant subspace containing the state needs a single isolated fixed point | that general statement (Brunton et al. 2016) has counterexamples ($\dot x = 0, \dot y = -y$; rotations); for the running example use the direct arguments: under the deterministic drift, repeated generator application to $x_1$ gives polynomials of strictly increasing degree; under the reflected diffusion, a finite-dimensional subspace invariant under the strongly continuous Koopman semigroup lies in the generator's domain, whose functions satisfy the Neumann boundary condition, which $x_1$ violates (the degree argument alone does not apply there) |
| the Gaussian information bottleneck is CCA; SVD truncation solves K-state merging; the tail Σσ² is the loss of merged states | Gaussian IB shares CCA's directions, with β-dependent scales and noise; a K-group merge is quantization, an SVD is rank reduction; the tail is the projection error and only a lower bound on a merge's χ² loss |
| the error budget is one inequality adding sampling, perturbation and sparsification; or, conversely, the chains can never be added | finite-site errors add on the same sites; for spectral values of a single sphere-kernel walk there is an end-to-end chain (Weyl on the same sites plus A.44's eigenvalue comparison) with a stated, limited target; subspace certificates in different lifts cannot be summed without a common identification; the layer average and kNN graphs have no sampling theorem yet |
| the real-network NCS sets are certified, or carry an error budget | the budget is a ledger of the guarantees and gaps that apply to them; no real-network run has a certificate yet (no reference operator or candidate partition was computed), and the sampling theorems do not cover the implemented construction |
| SEBA's rounding bound certifies the returned sets | S.8 proves that an aligned frame with a small threshold-step error exists; whether a given SEBA run is near it is observed, not certified |
| the generator's slow modes are the instrument-table's singular directions | the instrument decides the table's ordering; it must be computed (here it happens to give pair first) |
| ε-machines are minimal among all generative models | minimal among prescient history-based (unifilar) predictors; nonunifilar generators can be smaller |
| the υ-machine is the mixed-state presentation (the programme's 2026 epsilon-machine post uses "upsilon machine" that way) | on this site υ-machine means only Rosas et al.'s Definition 2: micro pasts grouped by the law they give the macro future; the mixed-state presentation is called that |
| local CCA networks are Hebbian, or provably converge for several channels | their feedforward rules are called non-Hebbian by their authors (lateral rules anti-Hebbian); the CCA solution is a proved fixed point; multichannel convergence is shown numerically |
| the balanced states (page 2) are the generator's slow modes | they are input-output channels that mix modes; the builder reports the loadings |

## Amendment log

- v1.1 (17 November 2026), reconciliation with the eleven page specs and the four page writers' reports:
  page 9's claim (2.1) and appendix D's nonsense-history row follow what Golowich et al. measured; page 8 has no
  bowtie and pages 5 and 10 have bowtie labels (1.4); E7 cites the checked Froyland theorems, Froyland & Kwok and
  Banisch & Koltai; E10 is "4/5–8"; E15 states the CCA networks' rules and convergence as their authors do; E20's
  Shinkle & Heimersheim; page 2's exception to "r = 2 keeps the pair" (3.2); face B's input operator is B (3.4) and is
  stored in full at κ = 0.3; face C's input box is asymmetric, its graph is the implemented NCS construction for pages
  3, 4 and 10, the lift is on by default on page 10 (renamed $W_{\rm lift}$, $c_{\rm lift}$) and page 10's live N is
  250-1000 (3.5); builder outputs for `signal.json` basin labels, page 8's place fields, page 9's tables and the
  per-page `pNN.json` files (3.6); 3.7 rows for pages 2, 4, 5, 7, 8, 10; the ideal companion's $d_f$, $d_c$ (3.8);
  a page-0 ledger and updated drafts for pages 2, 3, 6, 7, 8, 9, 10 (4.2); the budget's construction coverage,
  reference operator, layer-combination row, $\eta_{\rm fail}$, $b_K$ and rounding candidate (4.3); page 8's reused
  HebbianHarmonics files (6.2); shared-module APIs (6.3); URL scheme and fallback tours (6.5); Pythia provenance and
  the unused ResNet teaser (7.1); notation (appendix A), bibliography (appendix C) and appendix D rows.
- v1.2 (17 November 2026), round-1 review (design; mathematics of pages 1-6; mathematics and citations of pages 7-10;
  23 findings, all resolved or answered):
  - **Ledger versus certificate** (1.1, 4.2 page 10, 4.3, appendix D): the budget is a ledger of results with
    hypotheses and named gaps; a certificate is what a checked run earns; the real-network runs have none yet. 1.1's
    headline result is restated as the strongest true form (named terms, most of them proved bounds, the rest named
    gaps, all resolution-dependent).
  - **4.3 rewritten**: construction coverage corrected (A.1 and A.23 need strictly positive entries, so they do not
    cover the zero-diagonal implemented kernel, whose scaling exists by total support; A.23's scale-relative form);
    the Z row distinguishes the sparsifier's $(1\pm\varepsilon)$ from the rescaled walk's
    $[(1-\varepsilon)/(1+\varepsilon), 1]$ and requires a certified ε; a new **end-to-end scalar chain** for
    eigenvalues (Weyl on the same sites plus A.44) with its limited target and a population-gap lower bound on the
    same event; sampling shown as theorem certificate, plug-in calculation and empirical comparison; "the chains
    cannot be added" replaced by "subspace certificates in different lifts cannot be summed without a common
    identification"; products confined to prose (A.22, A.26, A.55, S.4; S.10 does not transfer); S.8 is an
    existence statement.
  - **Face C (3.5, 3.6, 3.7)**: the static-versus-dynamic claim is replaced by start / end / stay-close questions
    compared by per-layer and block boundary cost, with no ordering asserted (an independent check found layer 12's
    sets closer to the basins than the average's); the `sphere` construction's views are population-centred and the
    N = 8000 reference has its own seed, so A.40-A.44's fixed-view and fixed-β hypotheses hold; scaling existence for
    the floor kernel by total support (Sinkhorn & Knopp 1967; Csima & Datta 1972).
  - **Asymmetry knob (3.2)**: $V_\kappa = (h_x - \kappa x_2/b)(x_1^2-1)^2 + h_y((x_2/b)^2-1)^2$ replaces the old tilt,
    which kept the $x_2$ reflection and left the pair label exactly lumpable; verified pair-label defect ≈ 0.0042 at
    κ = 0.3 with the pair-then-well hierarchy and page 1's instrument ordering intact; stationary-point statements
    corrected (wells and within-pair saddles fixed for every κ; between-pair saddles and hilltop move); basin grids
    must avoid ties. Pages 0, 2 and 6 follow; pages 1 and 4 (κ = 0 only) need no change of numbers.
  - **Face B (3.4, 3.6, 4.2 page 2)**: the 60-mode model is not minimal (9 visible modes at κ = 0); balancing is
    applied to an extracted minimal realization; expected Hankel singular values 0.7205, 0.1414, 0.0259, 0.00093;
    $B_k = \nu_kC_k/(D\sqrt2)$ has a k-dependent factor, so the modal realization is not symmetric until rescaled.
  - **3.8**: the companion's coarse gap opens, peaks (≈ 0.575 near β ≈ 3.3) and closes; the fine gap opens.
  - **Connection matrix (2.2)**: E13, E15 and E19 are `~`, each with its exact special cases stated as such (Gaussian
    IB shares CCA's directions; each local rule's fixed points; face C's layers are flow steps by construction).
  - **Page list (2.1), 1.1, 1.4, 4.2 page 0**: the unity is a shared spectral framework, with page 8 as a mechanism
    that produces spectral decompositions, stated on the map's skim path.
  - **4.2 pages 5 and 6; 3.7 rows 5, 6**: resistance sampling protects every cut collectively (summed leverage ≥ 1),
    not every crossing edge; sparsifier ε must be certified; Rosas et al. Theorem 3's hypotheses per direction;
    merging, projection and exact equivalence kept apart; the instrument's infinitely many causal states proved by a
    contraction argument (page 1), the finite-history count described as such.
  - **Appendix C**: Birkhoff 1957 / Seneta 2006, Sinkhorn & Knopp 1967, Csima & Datta 1972, Rump 2006, Kalman 1963,
    Granger & Morris 1976 added (all [V]); Brunton et al. 2016's fixed-point statement annotated as not relied on.
  - **Appendix D**: rows added or revised for the static/dynamic claim, the budget (both directions), real-network
    certification, SEBA's existence bound, finite-history versus causal-state counts, crossing-edge leverage, Lanczos
    ε, finite-delay states, the fixed-point obstruction, Gaussian IB and merging, and the worst-set Cheeger bound.
- v1.3 (17 November 2026), round-2 review (nine corrections of statement or definition; each checked against its
  argument or counterexample before adoption):
  - **4.3 population target and bandwidth** (item 1): the finite reference was at $\beta_{\rm ref}$ while $E_N$ used the
    selected β and was subtracted from the reference gap. The target is now defined as $P_{\star,\rm ref}$, the
    population operator of the noise-free fixed view at $\beta_{\rm ref}$ (Objects), and $E_N$ is evaluated at
    $\beta_{\rm ref}$ in both $|\lambda_i(P^{\rm used}_N) - \lambda_i(P_{\star,\rm ref})| \le e_F + E_N(\beta_{\rm ref})$ and
    $\delta_r(P_{\star,\rm ref}) \ge \delta_r(P^{\rm ideal}_N) - 2E_N(\beta_{\rm ref})$; a used bandwidth other than
    $\beta_{\rm ref}$ is a chain-F term. The reference-bandwidth design was chosen over retargeting to the current β.
    Appendix A follows; page 10's whiskers are intervals for the declared reference population.
  - **4.3 selection accounting** (item 2): one rule in sampling display 1. $\beta_{\rm ref}$ is chosen on the
    independent reference sample, so sampling statements are conditional on it (no union over the β grid); the
    remaining post-hoc choices (page 10: 13 layers × 3 sample sizes) are covered by a union bound, A.44 at
    $\eta_{\rm fail}/39$ per event ($h_N(\eta_{\rm fail}/78)$ with A.44's internal halving); no union over r;
    $\eta_{\rm fail}$ declared before looking. **3.5**: $m_\ell$ is a fixed midpoint-quadrature estimate of the
    population mean, and $P_{\star,\rm ref}$ is defined with the same stored vector (3.6 row and appendix A follow).
  - **4.3 "How the resolution knob enters"** (item 3): "every certificate divides by the gap" replaced: subspace
    certificates divide by the gap at r; eigenvalue and operator-error bounds do not, and the gap decides whether those
    errors distinguish a block; rounding also needs a small partition residual and a positive threshold margin. Pages
    0, 4 and 10 follow; appendix D row added.
  - **Page 10, ResNet retentions** (item 4): Rayleigh retentions of signed eigenfunctions (.94 on b1's walk, .73 on the
    pool walk; block mode .83 and .96), not mass fractions (page only).
  - **Verified positive definiteness** (item 5): page 5's former check (Cholesky after subtracting $10\,n\,u\|L\|_1$,
    attributed to Rump 2006) was not Rump's criterion, whose shift scales with $\gamma_{n+1}\mathrm{tr}(A)$ (larger by
    a factor of about 5.7 on the reviewer's test graph and ≈ 19 on an independent four-cluster Gaussian graph at
    n = 600), and it ignored matrix-formation error. Rump 2006 was read (Theorem 2.3, Corollaries 2.4 and 2.7, Lemma
    2.5, Algorithm 1); page 5 now specifies a faithful in-browser implementation of Cor. 2.7 with bound I and an
    entrywise formation radius, so "certified" stays. The same routine (`lib/linalg.js` `verifyPD`, 6.3) replaces page
    10's "dense eigensolve plus $10\,Nu\|E\|_F$" for the measured perturbation norm (4.3 chain F row P), with a
    rounding-inflated Frobenius norm as the labelled cruder bound. 4.2 page 5, 4.3 row Z, appendix C (Rump entry,
    now with the criterion stated) and appendix D follow.
  - **Worst-set conductance** (item 6): 3.5 now says that each fixed set's conductance under $\bar M$ is the mean of its
    per-layer conductances, while a labelling's worst-set conductance under $\bar M$ is only bounded above by the mean
    of the per-layer worst-set values. Pages 4 and 10 keep their worst-set strips and mark that mean as an upper bound
    beside the worst-set conductance computed under $\bar M$; appendix D row added.
  - **Koopman obstruction for the reflected diffusion** (item 7): the running example's diffusion has reflecting walls,
    so its generator has Neumann conditions and $x_1$ is not in its domain; the degree argument is kept for the
    deterministic drift, and the diffusion case uses the generator-domain argument (appendix C Brunton annotation,
    appendix D row, page 3).
  - **χ² versus KL** (item 8): page 6's 3.3 callout and related labels say the spectral tail bounds a merge's χ² loss,
    not its KL information loss (4.2 and appendix D already said χ²).
  - **Bridges** (item 9): not "always kept" under sampling with replacement (missed with probability
    $(1 - 1/(n-1))^q > 0$); maximum leverage, kept with high probability, and contained in every successful sparsifier
    with ε < 1 (page 5; appendix D row added).
