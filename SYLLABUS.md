# Syllabus: one idea, many fields

A course outline meant to be handed to an AI tutor. It gives the big ideas, in a sensible order, and
trusts the tutor to fill in the rest at whatever depth the learner wants.

## For the learner

Give this whole file to your LLM and say something like:

> I'd like you to teach me from this syllabus. About me: *[your background, e.g. "I know logic and
> computability well, category theory somewhat, and very little applied maths or linear algebra"]*.
> Start with Module 0 unless I say otherwise. Go one big idea at a time, check my understanding with
> a question or a small exercise before moving on, and keep connecting back to the central picture.
> Work through small concrete examples by hand or in code. Tell me when something is a theorem and
> when it's an analogy.

Modules 1–3 are the core. After that, follow your interests; each module says what it relies on.

## For the tutor

- **The central picture, to return to constantly:** take a system that unfolds over time. Make a table
  whose rows are pasts, whose columns are futures, and whose entries say what happens for that past
  followed by that future (the *Hankel matrix*). States are what distinguishes rows. The number of
  independent rows (rank) is the size of the smallest model. The SVD ranks the directions of that
  state space by importance, so you can truncate with a guaranteed error. Every module is this
  picture with a different choice of table, of "past" and "future", and of how the two sides are
  weighted.
- Prefer small worked examples (a three-state machine, the Fibonacci sequence, a two-cluster graph, a
  noisy particle hopping between two wells) over general theory. Let the learner compute something in
  every module.
- Adapt to the learner's background. Logicians will like reaching linear algebra through
  Myhill–Nerode; category theorists through image factorizations; others through examples.
- Be precise about the status of each connection: theorem, approximation with a bound, or analogy.
  The "Keep it honest" list at the end gives common overstatements to avoid.
- [`docs/field-guide.md`](docs/field-guide.md) in this repo has exact statements and references
  if you need to check something.

---

## Module 0: Just enough linear algebra

**Big ideas.** A matrix is a linear map. Its *rank* is the dimension of its image, the smallest space
the map can be squeezed through. An *eigenvector* is a direction a map only stretches; for a map
applied repeatedly, eigenvectors are the independent "modes" and their eigenvalues are growth or
decay rates (near 1 means slow and persistent). The *singular value decomposition* writes any matrix
as a sum of rank-one pieces sorted by size. The *Eckart–Young theorem*: keeping the biggest *r* pieces
gives the best rank-*r* approximation, with a known error. What "biggest" means depends on the inner
products chosen on each side: choosing them is choosing what matters.

**Ask about:** rank as factorization; eigenvalues of a Markov chain's transition matrix; SVD as
"rotate, scale, rotate"; Eckart–Young; why changing the inner product changes the answer.

**Try:** the SVD of a small matrix by hand or in numpy; truncate it and measure the error.

---

## Module 1: States are rows (Myhill–Nerode)

**Big ideas.** For a language, build the 0/1 table "does prefix *u* followed by suffix *v* belong?".
Two prefixes are equivalent if their rows match. The language is regular iff there are finitely many
distinct rows, and the rows are the states of the minimal DFA. A state is *exactly* what you need to
remember about the past to predict the future, and you can define it from behaviour alone.

**Ask about:** Myhill–Nerode; residuals and Brzozowski derivatives; why non-regular languages (like
balanced brackets) have infinitely many rows; reachable versus distinguishable states.

**Try:** write the table for "binary numbers divisible by 3" and recover the 3-state machine.

**Relies on:** nothing.

---

## Module 2: From counting rows to rank (weighted automata and Hankel matrices)

**Big ideas.** Replace yes/no with numbers: a function from strings to numbers (a probability, a
count). A *weighted automaton* computes such a function with a vector, one matrix per letter, and
another vector. *Fliess's theorem*: the function comes from a finite weighted automaton iff its table
has finite rank, and the minimal number of states equals the rank. The automaton can be read off
from the table's factorization. The one-letter case is classical (*Kronecker*): a sequence has a
finite-rank Hankel matrix iff it satisfies a linear recurrence. Decision questions sit at an
interesting boundary: equivalence is easy (linear algebra); "does a linear recurrence ever hit zero?"
(the *Skolem problem*) is open; threshold questions for probabilistic automata are undecidable.

**Ask about:** weighted automata; Hankel matrices; Fliess's theorem; Kronecker's theorem; rational
power series (Kleene–Schützenberger); the Skolem problem and Skolem–Mahler–Lech; Rabin's
probabilistic automata and undecidability; why equivalence is decidable by linear algebra.

**Try:** the Hankel matrix of Fibonacci has rank 2; build the 2-state weighted automaton from it.

**Relies on:** 0, 1.

---

## Module 3: Keeping the important part (SVD truncation and its guarantees)

**Big ideas.** Real tables are noisy, infinite, or full rank. The SVD of the table ranks
state-space directions by how much the past-to-future map uses them. Truncating gives the best
rank-*r* table, with an error bound in terms of the discarded singular values. Subtlety: the best
rank-*r* table is not automatically a valid *r*-state machine of the same kind (it can produce
negative "probabilities"); separate results handle that.

**Ask about:** singular value automata and approximate minimization (Balle, Panangaden & Precup);
why the choice of weights on pasts and futures matters; the difference between approximating a
table and approximating a machine.

**Try:** generate strings from a small hidden Markov model, estimate a finite Hankel block, and look
at its singular values. Where's the gap?

**Relies on:** 2.

---

## Module 4: Learning from the table

**Big ideas.** Angluin's L\* learns a DFA by asking membership and equivalence queries, maintaining a
finite piece of the table. *Spectral learning* replaces queries with estimated statistics and
exact row-matching with an SVD; it learns hidden Markov models and weighted automata consistently,
without local optima. *Predictive state representations* go further and define the state of a
partially observed system as a vector of predictions about future tests.

**Ask about:** L\*; observation tables; spectral learning of HMMs (Hsu, Kakade & Zhang) and of
weighted automata (Balle et al., "forward-backward perspective"); predictive state representations;
observable operator models; how this contrasts with EM.

**Try:** implement a minimal spectral learner for a 2-state HMM.

**Relies on:** 2, 3.

---

## Module 5: The categorical view

**Big ideas.** An automaton is both an algebra (start somewhere and read input) and a coalgebra
(observe, then step). The minimal machine is the image of the map from the initial algebra (all
input strings) to the final coalgebra (all behaviours). That map is the table. Reachability and
observability are dual, which explains Brzozowski's "reverse, determinize, reverse, determinize"
algorithm. Moving from sets to vector spaces turns "image" into "span" and gives Fliess's theorem.
The same duality is Kalman's controllability/observability duality in control theory (Module 6).

**Ask about:** universal coalgebra (Rutten); bisimulation; algebra–coalgebra duality in Brzozowski's
algorithm (Bonchi et al.); Arbib & Manes's "machines in a category"; precomposition (Koopman) vs
pushforward (transfer), Module 7, as contravariant vs covariant functors.

**Relies on:** 1, 2. Optional for most learners; a shortcut for category theorists.

---

## Module 6: Control theory (realization and model reduction)

**Big ideas.** A linear system has inputs, an internal state, and outputs. Its *Hankel operator*
maps past inputs to future outputs. Its rank is the minimal state dimension, and factoring it
recovers the system (*Ho–Kalman*). This is the same as Fliess with one letter and vector inputs.
*Balanced truncation* chooses coordinates in which each state direction is equally easy to reach
and to observe, then discards the weakest, with an error guaranteed to be at most twice the sum of
the discarded *Hankel singular values*.

**Ask about:** state-space models; controllability and observability (and their Gramians); Hankel
singular values; balanced truncation and its error bound; the Eigensystem Realization Algorithm;
AAK theory as the optimal version.

**Try:** balance-truncate a random stable system with `scipy`/`python-control` and check the bound.

**Relies on:** 0, 2 (3 helps).

---

## Module 7: Dynamical systems (Koopman and transfer operators)

**Big ideas.** Any dynamics, however nonlinear, acts *linearly* on functions of the state: the
*Koopman operator* sends a measurement to "that measurement, one step later". Its adjoint, the
*transfer operator*, moves probability distributions forward. The price is infinite dimensions;
the practical art is finding a finite set of functions the dynamics nearly preserves. Eigenvalues
near 1 are slow, persistent patterns. *Takens' theorem*: delays of a single measurement reconstruct
the state of a deterministic system, which is how you build the table from one time series. For
noisy systems, the SVD of the transfer operator is canonical correlation between past and future.
The hidden Markov model is where this meets Module 2: its table factors as "push the past forward,
then pull the future back".

**Ask about:** Koopman operator; Perron–Frobenius operator; von Neumann's mean ergodic theorem;
dynamic mode decomposition (DMD) and extended DMD; Takens' embedding theorem; Hankel-DMD and HAVOK;
VAMP and Markov state models in molecular dynamics; Mori–Zwanzig (what truncation costs you as
memory and noise).

**Try:** DMD on a simulated oscillator or the Lorenz system; Hankel-DMD from a single coordinate.

**Relies on:** 0 (2 and 6 make the connections visible).

---

## Module 8: Graphs and spectral clustering

**Big ideas.** The *graph Laplacian* measures how much a labelling disagrees across edges. Its
small eigenvalues correspond to labellings that are nearly constant on well-connected pieces, so its
eigenvectors find clusters. From the random-walk side: clusters are where the walker gets stuck.
The *Cheeger inequality* sandwiches the (hard) best-cut quality between functions of the (easy)
second eigenvalue: a relaxation with a two-sided guarantee. *Diffusion maps* build the walk from
data; for particles diffusing in a potential they recover the slow dynamics of Module 7. The
spectral gap also controls how fast random walks mix.

**Ask about:** Laplacian and normalized Laplacian; Fiedler vector and seriation; conductance and the
Cheeger inequality; higher-order Cheeger; normalized cuts; diffusion maps; mixing times; expander
graphs; for TCS fans: Reingold's SL = L, Dinur's PCP proof, approximate counting via rapid mixing,
spectral sparsifiers, Laplacian solvers.

**Try:** spectrally cluster two noisy blobs; watch the eigenvalue gap; check Cheeger numerically.

**Relies on:** 0.

---

## Module 9: Coherent sets (clustering things that move)

**Big ideas.** For a flowing system over a time window, the transfer operator from start to end (with
a little noise) has leading singular vectors that mark *coherent sets*: regions that move together
and mix little with their surroundings, like ocean eddies. There is a dynamic Cheeger inequality.
This joins Modules 7 and 8: spectral clustering with time in it. Coherent sets are approximately
*lumpable*: merging them gives a reduced Markov model with a controlled error.

**Ask about:** finite-time coherent sets (Froyland); the dynamic Laplacian; metastability; PCCA+;
lumpability (Kemeny & Snell); SEBA for turning eigenvectors into sparse sets.

**Try:** find the coherent sets of a double-gyre flow, or of a noisy particle in a four-well potential.

**Relies on:** 7, 8.

---

## Module 10: Prediction and information (causal states, CCA, information bottleneck)

**Big ideas.** *Computational mechanics*: group pasts by their conditional distribution of futures.
The groups are *causal states*; the minimal predictor built on them is the *ε-machine*; its entropy
measures how much memory the process needs (statistical complexity). Relation to rank: the Hankel
rank is at most the number of causal states, and can be strictly smaller, even finite when the
causal states are infinite. *CCA* between past and future gives linear predictive summaries; the
*information bottleneck* asks the same question measured in bits.

**Ask about:** causal states, ε-machines, statistical complexity, excess entropy; unifilarity;
Akaike's stochastic realization; predictive information (Bialek, Nemenman & Tishby); information
bottleneck.

**Try:** compute causal states for the "even process" or the "golden mean process".

**Relies on:** 1, 2 (7 helps).

---

## Module 11: The deep end (spectra, periodic orbits, number theory, quantum)

**Big ideas.** A tour, not a course. Quantum mechanics evolves states (Schrödinger) or observables
(Heisenberg): transfer versus Koopman. *Thermodynamic formalism*: Ruelle's transfer operators turn
chaotic dynamics into statistical mechanics, with the leading eigenvalue giving the pressure and the
spectral gap giving decay of correlations. *Trace formulas* equate sums over a spectrum with sums
over periodic orbits. The *Selberg trace formula* relates Laplace eigenvalues of a hyperbolic
surface to its closed geodesics, in a formula with the same shape as the one linking zeta zeros to
primes. *Can one hear the shape of a drum?*: the spectrum determines a lot of geometry, but not all.

**Ask about:** Heisenberg vs Schrödinger pictures; Ruelle transfer operators and zeta functions;
Selberg trace formula and the prime geodesic theorem; explicit formulas in number theory; the
Hilbert–Pólya idea; Weyl's law; Kac's drum and isospectral domains.

**Relies on:** 7, 8. Purely for enrichment.

---

## Module 12: Neural networks

**Big ideas.** Hebbian learning rules make neurons compute principal components (Oja). A language
model's next-token predictions, arranged by context and continuation, form a Hankel-like table that
is approximately low-rank in trained models. Transformers trained on data from a hidden Markov model
represent the belief over hidden states linearly in their activations. The research frontier (my own
interest): treat the flow of data points through a network's layers as a dynamical system, find its
coherent sets (Module 9), and track what is guaranteed as the resolution gets finer.

**Ask about:** Oja's rule; logit rank of language models (Golowich, Liu & Shetty 2025); belief-state
geometry in transformers (Shai et al. 2024); residual networks as discretized flows; stable regions
in activation space.

**Relies on:** 3, 7, 9 (10 helps).

---

## Capstone

Ask the tutor to help you fill in this table from memory, then check it:

| Field | What is "past"? | What is "future"? | What is the state? | What does truncation give? | What's the guarantee? |
|---|---|---|---|---|---|
| Automata | | | | | |
| Control | | | | | |
| Koopman / dynamics | | | | | |
| HMMs | | | | | |
| Spectral clustering | | | | | |
| Coherent sets | | | | | |
| Computational mechanics | | | | | |
| Language models | | | | | |

Then ask: in each case, what plays the role of the *weights* on pasts and futures, and how would the
answer change with a different choice?

---

## Keep it honest (for the tutor)

Common overstatements to avoid:

- Hankel rank ≤ number of causal states, not equal; the gap can be infinite.
- A truncated table is the best low-rank *table*, not necessarily a valid smaller machine.
- Takens' theorem gives an embedding of deterministic smooth dynamics; it does not make the dynamics
  linear, and noise needs separate care.
- Static clustering of samples recovers dynamics only in special cases (reversible diffusions with
  the right kernel normalization).
- For purely deterministic invertible dynamics the transfer operator is unitary; ranking modes needs
  noise, a finite time window, or coarse-graining.
- Spectral sparsification is about undirected graphs with nonnegative weights, not about pruning
  neural network weights.
- Hebbian rules each compute *some* spectral object; they don't generically do spectral clustering.
- Analogies (quantum pictures, trace formulas and primes, neural networks as flows) are analogies
  unless a specific theorem is named.
