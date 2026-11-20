# Field guide: the detailed version

This is the technical companion to the [README](../README.md): the same tour, field by field, with
the actual statements, names, dates and references. Read the README first; come here when a
section catches your interest and you want the precise version and something to read next.

---

## TL;DR

1. **Write down a table.** Rows are *pasts* (everything that has happened so far), columns are *futures*
   (everything that could happen next), and each entry says how the system responds to "this past,
   then that future". This is the **Hankel matrix** of the system.

2. **The state of a system is the factorization of that table.** Two pasts are "the same state" exactly
   when their rows agree. So the table factors as *past → state → future*, and the smallest possible
   state space is the image of that factorization. For a regular language with 0/1 entries, this *is*
   the Myhill–Nerode theorem: distinct rows are exactly the states of the minimal DFA. For real-valued
   entries, "number of distinct rows" becomes "**rank**", and the theorem becomes **Fliess's theorem**
   for weighted automata and the **Ho–Kalman** theorem for linear control systems.

3. **Linear algebra lets you approximate the state, with a guarantee.** The singular value
   decomposition (SVD) splits the table into pieces ranked by importance. Keep the top *r* and you get
   the best *r*-dimensional summary of the past *for predicting the future*, with error bounds stated
   in terms of the singular values you threw away.

4. **For dynamical systems, the same move is called the Koopman / transfer operator.** A nonlinear
   system acts *linearly* on functions of its state. Pull functions back along the dynamics and you
   get the Koopman operator; push probability distributions forward and you get its adjoint, the
   transfer operator. Their spectra find the slow, persistent, predictable parts of the system.
   For a hidden Markov model the Hankel matrix factors *exactly* as "transfer operator, then Koopman
   operator".

5. **For clustering, the same move is called spectral clustering.** Take a random walk on your data.
   Sets of points the walk rarely leaves (small boundary for their volume) show up as the leading
   eigenvectors of that walk, and the **Cheeger inequality** proves that the eigenvalue tells you
   how good the best cut is. Add time, and these become *coherent sets*: regions of a flowing system
   that move together.

6. **So one recipe recurs:** pick the map from *what has happened* to *what happens next*, choose how
   to weigh the two sides, take an SVD (or an eigendecomposition), truncate at a resolution *r*, and
   read off a state space with an error bar. Automata minimization, model reduction, Markov state
   models of protein folding, image segmentation, predictive-state RL, and (my current interest)
   finding the computational states inside neural networks all follow this recipe or a close
   relative of it. Each comes with its own theorem saying what the truncation costs.

One-line version: **the only thing that is truly interpretable is an SVD, so find the right SVD.**

---

## Contents

- [0. A two-minute linear algebra primer (for people who know eigenvalues mostly from category theory)](#0-a-two-minute-linear-algebra-primer)
- [1. Automata, logic and computability](#1-automata-logic-and-computability)
- [2. Category theory and coalgebra](#2-category-theory-and-coalgebra)
- [3. Control theory: realization and model reduction](#3-control-theory-realization-and-model-reduction)
- [4. Dynamical systems: Koopman and transfer operators](#4-dynamical-systems-koopman-and-transfer-operators)
- [5. Graphs: Laplacians, Cheeger, spectral clustering](#5-graphs-laplacians-cheeger-spectral-clustering)
- [6. Statistics and information: CCA, predictive states, ε-machines](#6-statistics-and-information)
- [7. Physics and pure mathematics: the deep end](#7-physics-and-pure-mathematics-the-deep-end)
- [8. Brains and neural networks](#8-brains-and-neural-networks)
- [9. Why I think this is deep, natural and practical](#9-why-i-think-this-is-deep-natural-and-practical)
- [10. Where I'm taking it](#10-where-im-taking-it)
- [Reading paths by background](#reading-paths-by-background)
- [Common overclaims to avoid](#common-overclaims-to-avoid)

---

## 0. A two-minute linear algebra primer

Skip this if you already think in SVDs.

- A **linear map** $T: V \to W$ between vector spaces. Its **rank** is the dimension of its image:
  the smallest $k$ such that $T$ factors as $V \to \mathbb{R}^k \to W$. (Categorically, the
  epi-mono / image factorization in $\mathsf{Vect}$. Rank is "how big must the middle object be".)
- An **eigenvector** of $T: V \to V$ is a direction $T$ only rescales: $Tv = \lambda v$. The scale
  $\lambda$ is its **eigenvalue**. Eigenvectors of a map that is applied over and over (a dynamics,
  a random walk) are the "modes" that evolve independently, each growing or decaying at its own rate
  $\lambda^t$. Eigenvalues near 1 are the slow, persistent parts.
- The **singular value decomposition (SVD)** works for any matrix, even a rectangular one (and for
  compact operators between Hilbert spaces, which covers most of the infinite tables below once
  you fix the right spaces): $T = \sum_i \sigma_i\, u_i v_i^\top$ with orthonormal $v_i$
  (inputs), orthonormal $u_i$ (outputs), and $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$. Read it as:
  "$T$ is a sum of rank-one maps, ranked by importance". The number of nonzero $\sigma_i$ is the rank.
- **Eckart–Young theorem:** chopping the sum after $r$ terms gives the *best* rank-$r$
  approximation, and the error is exactly $\sigma_{r+1}$ in operator norm (or
  $\sqrt{\sum_{i>r}\sigma_i^2}$ in Frobenius norm). This is the prototype of the "with a bound"
  results below, though each field needs its own theorem: the best rank-$r$ *table* is not
  automatically the best $r$-state *machine*.
- The catch, and the whole art: the SVD depends on the **inner products** you put on the input and
  output spaces. Choosing those weights is choosing what "important" means. Many of the named
  methods below differ *only* in this choice.

Good references: Trefethen & Bau, *Numerical Linear Algebra* (lectures 4–5); Gilbert Strang's
*Linear Algebra and Learning from Data*; Axler, *Linear Algebra Done Right* if you want it basis-free.

---

## 1. Automata, logic and computability

**This is where I'd start if you know Myhill–Nerode.** The whole subject is Myhill–Nerode with the
Booleans replaced by a field.

### The construction

For a language $L \subseteq \Sigma^*$ define the infinite 0/1 matrix $H_L[u, v] = 1$ iff $uv \in L$,
rows indexed by prefixes $u$, columns by suffixes $v$. Row $u$ is the residual language
$u^{-1}L$ (the Brzozowski derivative). Myhill–Nerode: $L$ is regular iff $H_L$ has finitely many
distinct rows, and the minimal DFA's states *are* those rows.

Now let $f: \Sigma^* \to \mathbb{R}$ be any function on strings (a probability, a count, a weight), with
$H_f[u,v] = f(uv)$. A **weighted automaton** of dimension $n$ is an initial vector $\alpha$, one $n\times n$
matrix $A_\sigma$ per letter and a final vector $\beta$, computing
$f(\sigma_1\cdots\sigma_k) = \alpha^\top A_{\sigma_1}\cdots A_{\sigma_k}\beta$.

**Fliess's theorem (1974; also Carlyle & Paz 1971):** $f$ is computed by a weighted automaton iff
$\operatorname{rank} H_f < \infty$, and the minimal number of states is *exactly* that rank. The
factorization $H = (\text{pasts} \to \text{state})(\text{state} \to \text{futures})$ hands you the
automaton: the $A_\sigma$ are read off from "shifted" sub-blocks $H_\sigma[u,v] = f(u\sigma v)$.

That's the "Hankel trick": **finite rank of the past-by-future table = finite-state, and you can
build the machine by linear algebra.**

### Threads to pull

- **Kronecker (1881).** The one-letter case. A sequence $a_0, a_1, \dots$ has a finite-rank Hankel
  matrix $[a_{i+j}]$ iff it satisfies a linear recurrence, iff its generating function is rational.
  Fibonacci has Hankel rank 2.
- **The Skolem problem.** Given an integer linear recurrence (equivalently, a one-letter weighted
  automaton over $\mathbb{Q}$), does it ever hit 0? *Decidability is open*, which is remarkable for such
  a simple object. The Skolem–Mahler–Lech theorem says the zero set is eventually periodic, but the
  proof is non-effective ($p$-adic). Survey: Ouaknine & Worrell, "Decision problems for linear
  recurrence sequences" (2012); Ouaknine & Worrell, "Positivity problems for low-order linear
  recurrence sequences" (SODA 2014).
- **Equivalence is easy, thresholds are not.** Equivalence of weighted automata over the rationals
  is decidable in polynomial time by linear algebra (Schützenberger 1961; Tzeng 1992 for probabilistic
  automata). But for Rabin's probabilistic automata (1963), "is there a word accepted with
  probability $> 1/2$?" is *undecidable* (Paz 1971; Condon & Lipton 1989 give a clean proof). The
  linear-algebraic structure buys you exactly the questions that are about the span of rows.
- **Kleene–Schützenberger.** Rational power series (weighted regular expressions) = weighted automata
  = finite Hankel rank over a field. Berstel & Reutenauer, *Noncommutative Rational Series with
  Applications* (2011), is the book.
- **Learning theory.** Angluin's **L\*** algorithm (1987) learns a DFA from membership and
  equivalence queries by filling in an "observation table": a finite submatrix of $H_L$. Beimel et al.
  (2000) generalize to weighted ("multiplicity") automata, with rank playing the role of distinct rows.
  The *spectral* versions replace exact queries with statistics estimated from samples and the exact
  factorization with a truncated SVD: Hsu, Kakade & Zhang, "A spectral algorithm for learning hidden
  Markov models" (2009/2012); Bailly, Denis & Ralaivola (2009); the best overview is **Balle,
  Carreras, Luque & Quattoni, "Spectral learning of weighted automata: a forward-backward perspective"
  (*Machine Learning*, 2014).** These come with PAC-style guarantees and avoid EM's local optima.
- **Approximate minimization.** If the rank is too large, truncate: for square-summable series,
  Balle, Panangaden & Precup, "Singular value automata and approximate minimization" (2019) put the
  automaton in an SVD-adapted basis and drop the weakest states, with error
  $\|f - \hat f\|_2^2 \le \sum_{i>r}\sigma_i^2$: the automaton analogue of balanced truncation.
- **Beyond regular.** Context-free languages have infinite Hankel rank in general, so this lens is
  natively "finite-state". How much of a context-free or Turing-complete process you can capture at
  a given rank, and at what error, is the quantitative question. See my
  [Mori–Zwanzig and context-free memory](https://charlesr-w.github.io/crw-blog/Mori-Zwanzig-Hankel-Geometry-and-Context-Free-Memory/)
  note.

---

## 2. Category theory and coalgebra

If your relationship to eigenvalues is mainly through category theory, this is the bridge.

- **States are a factorization.** A deterministic automaton is both an *algebra* (start in a state,
  read letters: $1 + Q \times \Sigma \to Q$) and a *coalgebra* (from a state, observe and step:
  $Q \to 2 \times Q^\Sigma$). The reachable part is the image of the initial algebra $\Sigma^*$;
  the observable quotient is the image in the final coalgebra $2^{\Sigma^*}$ (all languages). The
  minimal automaton is the image of the composite $\Sigma^* \to Q \to 2^{\Sigma^*}$, which is
  exactly the Hankel matrix viewed as a map. Now move from $\mathsf{Set}$ to $\mathsf{Vect}_k$: the
  linear map $k^{(\Sigma^*)} \to k^{\Sigma^*}$ from the free vector space on words, sending a word
  $u$ to its row $(f(uv))_v$, has image the span of the rows, and its dimension is the minimal
  weighted automaton: Fliess's theorem.
- **Brzozowski's minimization algorithm** (reverse, determinize, reverse, determinize) looks like
  magic until you read it as this duality: reachability and observability swap under reversal.
  Bonchi, Bonsangue, Hansen, Panangaden, Rutten & Silva, "Algebra-coalgebra duality in Brzozowski's
  minimization algorithm" (*ACM TOCL*, 2014).
- **Kalman's duality.** In control theory, "reachable" and "observable" are dual under transposition,
  and minimal realization = reachable + observable. Arbib & Manes, "Machines in a category" (1974
  onwards; survey in *J. Pure Appl. Algebra* 1980) and Goguen (1972) put DFAs and linear systems in
  one categorical framework precisely because of this.
- **Universal coalgebra.** Rutten, "Universal coalgebra: a theory of systems" (2000). For deterministic
  automata, bisimilarity of two states is "same row of the Hankel matrix" (equal residual
  languages).
- **Koopman as a functor.** A map of spaces $T: X \to X$ gives a linear map on functions by
  precomposition, $f \mapsto f\circ T$ (contravariant), and a linear map on measures by pushforward
  (covariant). These are the Koopman and transfer operators of §4. Turning a nonlinear map on points
  into a linear map on functions is the same "go to the algebra of observables" move as Gelfand duality
  (a heuristic analogy, not a theorem I know of in this setting).
- What the SVD adds to the categorical picture is a *metric* on the middle object: not just "the
  minimal state space" but "these directions of state space matter more than those, by this much".

---

## 3. Control theory: realization and model reduction

Engineers found the same thing independently and made it industrial.

- **Ho–Kalman (1966).** Given the impulse response of a linear system $x_{t+1} = Ax_t + Bu_t$,
  $y_t = Cx_t$ (the "Markov parameters" $CA^kB$), stack them into a block Hankel matrix. Its rank is the
  minimal state dimension, and factoring it as observability × reachability gives $A, B, C$. This is
  Fliess's theorem for a one-letter alphabet with vector inputs and outputs.
- **The Hankel operator.** It maps past inputs to future outputs. Its singular values, the **Hankel
  singular values**, measure how much each state direction is *simultaneously* easy to reach and
  easy to observe.
- **Balanced truncation** (Moore 1981): for a stable, minimal system, change coordinates so the
  reachability and observability Gramians are equal and diagonal, then delete the weak directions.
  The error bound (Glover 1984; Enns 1984):
  $\|G - G_r\|_{\mathcal{H}_\infty} \le 2\sum_{i>r}\sigma_i$. You know in advance how much you lose.
- **AAK theory** (Adamyan, Arov & Krein 1971; Glover 1984) gives *optimal* Hankel-norm approximation.
  A beautiful piece of operator theory (Nehari's theorem, Hardy spaces).
- **Practical:** model reduction of large finite-element models and circuits; the Eigensystem
  Realization Algorithm (Juang & Pappa 1985), developed at NASA to identify vibrating space structures
  from measured data, is Ho–Kalman with an SVD.
- **Book:** Antoulas, *Approximation of Large-Scale Dynamical Systems* (2005). For a gentler start,
  the system identification chapters of Brunton & Kutz, *Data-Driven Science and Engineering*
  (2nd ed. 2022, free videos online).

---

## 4. Dynamical systems: Koopman and transfer operators

The "linearize by going to functions" trick, applied to nonlinear and chaotic systems.

- **Koopman (1931)**, "Hamiltonian systems and transformation in Hilbert space". Given dynamics
  $T: X\to X$, the operator $K f = f \circ T$ is linear on functions even when $T$ is wildly
  nonlinear. Von Neumann used it to prove the mean ergodic theorem (1932), with Birkhoff's
  pointwise theorem following within months: this is the original operator-theoretic view of
  dynamics. The price is that the function space is infinite-dimensional.
- **Transfer (Perron–Frobenius) operator:** the adjoint, acting on densities. Its fixed points are
  invariant measures. For noisy (or coarse-grained) systems, eigenvalues just below 1 give the
  slowly mixing, metastable parts. (For purely deterministic invertible dynamics the operator is
  unitary, and you need noise, a finite time window or coarse-graining to get a useful ranking.)
- **Modern revival:** Mezić (2005), "Spectral properties of dynamical systems, model reduction and
  decompositions"; Budišić, Mohr & Mezić, "Applied Koopmanism" (2012); Schmid (2010) and Rowley et al.
  (2009) on **Dynamic Mode Decomposition (DMD)**, now standard in fluid dynamics; Williams, Kevrekidis
  & Rowley (2015) on extended DMD.
- **Delay embedding.** **Takens (1981)**: for a generic smooth system on an $m$-dimensional manifold
  and a generic observable, $2m+1$ delays $(y_t, y_{t-1}, \dots, y_{t-2m})$ reconstruct the state
  (up to a smooth change of coordinates) (Sauer, Yorke &
  Casdagli, "Embedology", 1991). Stack delays into a matrix and you have built a Hankel matrix from a
  time series. **HAVOK** (Brunton et al., "Chaos as an intermittently forced linear system", 2017)
  takes its SVD and finds a nearly-linear model of the Lorenz attractor driven by a rare forcing term.
  Arbabi & Mezić (2017): Hankel-DMD.
- **Stochastic systems and CCA.** For a Markov process, the SVD of the (suitably whitened) transfer
  operator from now to time $\tau$ later is **canonical correlation analysis between past and future
  features**: Wu & Noé, "Variational approach for learning Markov processes from time series data"
  (VAMP, 2020); Klus et al. (2018). This is how **Markov state models** of protein folding are built
  from molecular-dynamics simulations (Prinz et al. 2011; Noé's group).
- **Coherent sets.** For time-dependent flows (ocean eddies, the polar vortex), the leading singular
  vectors of a slightly noisy transfer operator over a time window pick out regions that stay together and
  exchange little mass with their surroundings: Froyland, "An analytic framework for identifying
  finite-time coherent sets" (2013); Froyland, "Dynamic isoperimetry and the geometry of Lagrangian
  coherent structures" (2015), which proves a *dynamic* Cheeger inequality (§5).
- **Coarse-graining.** The Mori–Zwanzig projection formalism (Zwanzig 1961; Mori 1965): project the
  Koopman dynamics onto the observables you keep, and what you threw away comes back as memory and
  noise. This is what "truncate at rank $r$" costs you, made explicit.

**The hidden Markov model is the meeting point.** For an HMM with hidden states $x$,
$H[\text{past}, \text{future}] = \sum_x P(\text{past}, x) \cdot P(\text{future} \mid x)$, because
the hidden state at the boundary screens off past from future. The first factor is a distribution
over hidden states pushed forward through the observed past (transfer-operator style: the forward
algorithm); the second is a function of the hidden state pulled back through the future
(Koopman style: the backward algorithm), each step using the observation-labelled transition
matrices. So the Hankel factorization of §1 is "forward, then backward", the same
reachability-times-observability split as in control (Jaeger 2000; Balle et al. 2014, §4).

---

## 5. Graphs: Laplacians, Cheeger, spectral clustering

The same mathematics for static data, and a fully developed theory of *why* eigenvectors find
clusters.

- **The graph Laplacian** $L = D - W$ (degree minus adjacency). Its quadratic form
  $x^\top L x = \tfrac12\sum_{i,j} w_{ij}(x_i - x_j)^2$ measures how much a labelling $x$ disagrees across
  edges. Small eigenvalues are labellings that are nearly constant on well-connected pieces.
- **Fiedler (1973)**: the second eigenvalue ("algebraic connectivity") is zero iff the graph is
  disconnected; its eigenvector (the **Fiedler vector**) orders vertices so that the graph is
  roughly "cut in the middle". When a consistent ordering exists (the similarity matrix is
  "Robinson"), sorting by it solves *seriation*, the problem behind ordering archaeological graves
  by date from their artefacts (Atkins, Boman & Hendrickson, "A spectral algorithm for
  seriation and the consecutive ones problem", 1998).
- **Cheeger's inequality** (Cheeger 1970 for manifolds; Alon & Milman 1985, Alon 1986, Sinclair &
  Jerrum 1989 for graphs): with $\phi$ the conductance (the best ratio of cut edges to volume) and
  $\lambda_2$ the normalized Laplacian's second eigenvalue,
  $\lambda_2/2 \le \phi \le \sqrt{2\lambda_2}$. Finding the best cut is NP-hard; the eigenproblem is
  easy and provably not far off. Higher-order version for $k$ clusters: Lee, Oveis Gharan & Trevisan
  (2012/2014).
- **Spectral clustering**: Shi & Malik, "Normalized cuts and image segmentation" (2000); Ng, Jordan &
  Weiss (2001); the tutorial to read is **von Luxburg, "A tutorial on spectral clustering" (2007)**.
  It is the random-walk view of the same thing: clusters are sets the walk rarely leaves.
- **Diffusion maps** (Coifman & Lafon 2006) build the walk from a kernel on data; Nadler, Lafon,
  Coifman & Kevrekidis (2006) show that for a particle diffusing in a potential (a reversible
  Langevin system), the suitably normalized walk on equilibrium samples has eigenvectors converging
  to the slow eigenfunctions of the *dynamics*. Static clustering of samples recovers dynamics: §4 and §5
  are the same section.
- **PageRank** is the stationary eigenvector of a random walk on the web: the simplest relative, keeping only the top mode.

### Threads for the theoretical computer scientists

- **Expanders** are graphs with a large spectral gap, i.e. no sparse cuts. Hoory, Linial & Wigderson,
  "Expander graphs and their applications" (*Bull. AMS*, 2006). They power
  **Reingold's SL = L** (undirected connectivity in logspace, 2005/2008) and **Dinur's combinatorial
  proof of the PCP theorem** (2007), as well as error-correcting codes and derandomization.
- **Mixing time and counting.** Conductance bounds the mixing time of a reversible Markov chain
  (Sinclair & Jerrum 1989), which is how approximate counting works, up to the polynomial-time approximation of
  the permanent (Jerrum, Sinclair & Vigoda 2004). Levin & Peres, *Markov Chains and Mixing Times*
  (2nd ed. 2017), is free online.
- **The Laplacian paradigm.** Spielman & Teng's nearly-linear-time Laplacian solvers (2004) and
  **spectral sparsifiers** (Spielman & Srivastava 2011: every graph has a reweighted subgraph with
  $O(n\log n/\varepsilon^2)$ edges preserving every cut to $1\pm\varepsilon$, found by sampling edges
  by effective resistance). Electrical-flow methods built on these (Christiano, Kelner, Mądry,
  Spielman & Teng 2011) started the line of work that reached almost-linear-time max-flow (Chen et
  al. 2022). Spielman's lecture notes *Spectral and Algebraic Graph Theory* are free and excellent.
- **Book:** Chung, *Spectral Graph Theory* (1997).

---

## 6. Statistics and information

- **Canonical correlation analysis** (Hotelling 1936) finds the pairs of directions in two
  datasets that are most correlated. It is the SVD of the whitened cross-covariance. Applied to
  (past, future) it is **Akaike's (1975)** stochastic realization: the canonical directions are
  the predictive state of a linear-Gaussian process.
- **Predictive state representations** (Littman, Sutton & Singh 2002) and **observable operator
  models** (Jaeger 2000): represent the state of a partially observed system *as* predictions of
  future tests. A state is a row of the Hankel matrix normalized to conditional probabilities
  ($P(\text{future}\mid\text{past})$), written in a basis of "core" tests. Boots, Siddiqi & Gordon
  (2011) learn them spectrally for reinforcement learning.
- **Computational mechanics** (Crutchfield & Young 1989; Shalizi & Crutchfield 2001): the **causal
  states** of a stationary process are the classes of pasts with the same conditional future, and the
  **ε-machine** is the minimal unifilar predictor built on them. This is Myhill–Nerode for stochastic
  processes. Relation to rank: rank ≤ number of causal states, often strictly (a process can have
  finite Hankel rank and infinitely many causal states). My
  [ε-machines post](https://charlesr-w.github.io/crw-blog/Computational-Mechanics-and-Epsilon-Machines/)
  is an introduction.
- **Information bottleneck** (Tishby, Pereira & Bialek 1999) and Bialek, Nemenman & Tishby,
  "Predictability, complexity, and learning" (2001): compress the past while keeping information
  about the future. Same question, measured in bits instead of a norm. For Gaussian variables its
  solutions point along the CCA directions (Chechik et al. 2005).
- **Lumpability** (Kemeny & Snell 1960): when can you merge states of a Markov chain and still have a
  Markov chain? Metastable sets found by spectral methods are approximately lumpable, with an error
  you can bound (Deuflhard & Weber 2005, PCCA+; Sarich, Noé & Schütte 2010).

---

## 7. Physics and pure mathematics: the deep end

None of this is needed for the applications, but it is the strongest evidence that the idea is
fundamental rather than a trick.

- **Quantum mechanics is the original example.** The Heisenberg picture evolves observables, the
  Schrödinger picture evolves states. Those are the Koopman and transfer pictures, and Koopman's 1931
  paper was written in exactly that spirit, as von Neumann's Hilbert-space methods were being
  applied to classical mechanics.
- **Thermodynamic formalism.** Ruelle's transfer operators $\mathcal{L}_\phi f(x) = \sum_{Ty=x}
  e^{\phi(y)}f(y)$: for nice (e.g. uniformly expanding) maps, the leading eigenvalue is $e^{P(\phi)}$
  with $P$ the pressure (a free energy), the leading eigenfunction times the dual eigenmeasure gives
  the equilibrium state (Gibbs measure), and the spectral gap gives exponential decay of
  correlations.
  Ruelle, *Thermodynamic Formalism* (1978); Baladi, *Positive Transfer Operators and Decay of
  Correlations* (2000).
- **Spectra and closed geodesics.** The **Selberg trace formula** (1956) equates a sum over the
  Laplace eigenvalues of a hyperbolic surface with a sum over its closed geodesics.
  The Ruelle zeta function does the same for periodic orbits of chaotic maps: *spectrum ↔ periodic
  orbits* is a theme, and the transfer operator is its engine.
- **Can you hear the shape of a drum?** (Kac 1966.) How much of a geometry is determined by its
  Laplace spectrum? Not all of it: Gordon, Webb & Wolpert (1992) built isospectral, non-congruent
  drums. Cheeger's inequality (§5) is the quantitative positive half: the spectrum knows the
  bottlenecks.

---

## 8. Brains and neural networks

- **Hebbian learning computes PCA.** Oja (1982): a single neuron with a normalized Hebbian rule
  converges to the top principal component of its inputs. Pehlevan, Chklovskii and collaborators
  extend this to principal subspaces and CCA with local learning rules.
- **Neurons as predictive filters.** Recent work (Pughe-Sanford et al. 2025) argues that a
  filter-and-rectify neuron whose filter is a past-future canonical direction reports membership in a
  coherent set of its input history: stochastic Koopman analysis in one cell.
- **Language models from the outside.** Golowich, Liu & Shetty (2025) show that a language model's
  (centred) *logit* table (histories × continuations) is Hankel-like and approximately low-rank in
  trained models, and that its rank is exactly the dimension of the smallest simple time-varying,
  input-switched linear model (with a softmax readout) that reproduces the model.
- **Language models from the inside.** Shai et al., "Transformers represent belief state geometry in
  their residual stream" (2024): trained on data from a hidden Markov model, transformers linearly
  encode the Bayesian belief over hidden states, i.e. the predictive state of §6.

---

## 9. Why I think this is deep, natural and practical

**Deep.** The same construction is a theorem in automata theory (Myhill–Nerode, Fliess), in control
(Ho–Kalman), in ergodic theory (Koopman–von Neumann), in spectral geometry (Cheeger), in statistics
(Akaike's CCA realization) and in stochastic processes (causal states). It touches open decidability
problems (Skolem), the PCP theorem and quantum mechanics. Ideas that show up
independently in this many places are usually tracking something real.

**Natural.** It answers the most basic modelling question, "what about the past matters for the
future?", in the most basic way: by writing down the past-to-future map and asking for its image.
Everything else is a choice of weights and a choice of resolution. There is no architecture to
design, and most of the methods have no free parameters beyond the rank and the time lag.

**Practical.** These are not just existence theorems. They are SVDs, which run in seconds on
millions of points, come with error bars, and avoid the local optima of EM and gradient descent.
They are used daily in aerospace system identification, circuit model reduction, fluid dynamics
(DMD), molecular dynamics (Markov state models), climate science (coherent sets), image segmentation
and web search.

**The honest caveat.** The SVD tells you the best *linear* summary in the norm you chose. Choosing
the map and the norm is where the thinking happens, and a truncated table is not always a valid
smaller machine of the same kind (it can have negative "probabilities").

---

## 10. Where I'm taking it

My research applies this to interpretability: if you want to find the *computational states* of a
neural network, write down the right past-to-future map (prefixes to continuations from the outside;
activations at one layer to the next from the inside), take the right SVD, and track what the error
budget does as you change the resolution. The working name for the inside version is **neural
coherent sets**: Froyland-style coherent sets for the flow of data points through a network's layers.
The error budget currently has proved terms and named gaps; it is a research programme, not a
finished result.

Posts, roughly in reading order (these are AI-assisted research notes; treat them as drafts):

- [Computational Mechanics and Epsilon-Machines](https://charlesr-w.github.io/crw-blog/Computational-Mechanics-and-Epsilon-Machines/)
- [Characterizing Predictive Salience via Hankel Spectra](https://charlesr-w.github.io/crw-blog/Characterizing-Predictive-Salience-via-Hankel-Spectra/)
- [The Spectral Structure of Natural Data](https://charlesr-w.github.io/crw-blog/The-Spectral-Structure-of-Natural-Data/)
- [A Spectral Theory of Computation](https://charlesr-w.github.io/crw-blog/A-Spectral-Theory-of-Computation/) (MATS 9.0 report)
- [Mori–Zwanzig, Hankel Geometry and Context-Free Memory](https://charlesr-w.github.io/crw-blog/Mori-Zwanzig-Hankel-Geometry-and-Context-Free-Memory/)
- [Dynamic Spectral Geometry for Identifying Computations](https://charlesr-w.github.io/crw-blog/Dynamic-Spectral-Geometry-for-Identifying-Computations/)
- [Hankel HMM reconstruction widget](https://charlesr-w.github.io/crw-blog/Hankel-HMM-Reconstruction-Widget/) (interactive)

The [`spec/`](../spec/) folder is the plan for a ten-page interactive site that walks through §§1–8 with one
running example (a noisy particle hopping between four wells) seen through every lens.

---

## Reading paths by background

| If you like… | Start with | Then |
|---|---|---|
| Logic, automata, computability | §1: Fliess's theorem, Balle et al. 2014 | Skolem problem survey; §2; §6 causal states |
| Category theory | §2: Bonchi et al. 2014 on Brzozowski | §0, then §1 and §3 (Kalman duality) |
| Theoretical CS | §5: von Luxburg, then Hoory–Linial–Wigderson | Spielman's notes; Lee–Oveis Gharan–Trevisan |
| Dynamics, physics | §4: Budišić–Mohr–Mezić "Applied Koopmanism" | Froyland 2013; §7 |
| Engineering, control | §3: Antoulas, or Brunton & Kutz | §4 DMD and HAVOK |
| Statistics, ML | §6: CCA and predictive states | Hsu–Kakade–Zhang; Wu & Noé (VAMP) |
| Pure maths | §7: Selberg, Ruelle, Kac | Baladi; §5 Cheeger |

If you read only three things: **von Luxburg's spectral clustering tutorial**, **Balle et al.'s
spectral learning of weighted automata**, and **Brunton & Kutz's chapters on DMD and Koopman**.

---

## Common overclaims to avoid

The connections are real, but they are easy to overstate. A few corrections I care about:

- Hankel rank ≠ number of causal states. Rank ≤ causal states, often strictly.
- A rank-$r$ truncation of a table is the best rank-$r$ *table*, not necessarily a valid smaller
  automaton or HMM.
- Takens' theorem gives an *embedding* of deterministic smooth dynamics. It says nothing about the
  embedded dynamics being linear, and noise needs separate treatment.
- Static clustering finds dynamics only in special cases (reversible dynamics with the right kernel
  normalization). In general you need the transfer operator over time.
- Spectral sparsification is a theorem about undirected graph Laplacians with nonnegative weights,
  not a licence to prune signed, directed neural network weights.
- Hebbian learning computes *some* spectral object for each rule; it is not generically "doing
  spectral clustering".

The full list, with the precise versions, is Appendix D of [`spec/SPEC.md`](../spec/SPEC.md).
