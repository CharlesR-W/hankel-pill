# hankel-pill

There is one simple idea that turns up, under a different name, in logic, engineering, physics,
statistics, computer science, pure mathematics, neuroscience and machine learning. Once you see it,
you keep seeing it. This page is the version I'd send you after getting you excited about it in
conversation.

- **New to all of this?** Read this page. It has no formulas.
- **Want to actually learn it?** Point an AI tutor at [`SYLLABUS.md`](SYLLABUS.md). It is a list of
  big ideas in a sensible order, written for an LLM to teach from, at whatever depth you like.
- **Want the precise statements and references?** See [`docs/field-guide.md`](docs/field-guide.md).

---

## The idea

**1. Make a table of pasts and futures.** Take any system that unfolds over time: a machine reading
input, a language, a planet, a market, a neural network. Make a big table. Each row is a possible
*past* (what has happened so far). Each column is a possible *future* (what could happen next). Each
entry records what happens when that past is followed by that future: yes or no, a probability, a
measurement.

**2. The state is whatever makes rows different.** If two pasts have identical rows, they lead to
exactly the same futures, so nothing distinguishes them that will ever matter. They are the same
*state*. So the number of genuinely different rows is the number of states the system needs, and
the state of a system *is* "what you need to remember about the past to predict the future". You
can work this out from behaviour alone, without opening the box.

**3. With numbers, "different rows" becomes "independent rows".** When the entries are numbers,
some rows are blends of others and add nothing new. The number of independent rows (the *rank*
of the table) is the size of the smallest machine that reproduces the behaviour. And there is a
standard procedure from linear algebra that builds that machine from the table.

**4. Rank things by importance and keep the top few.** Real tables are noisy and huge, so in
practice nothing is exactly finite. A second standard tool, the *singular value decomposition*
(SVD), breaks the table into ingredients sorted from most to least important. Keep the top *r* and
you get the best *r*-dimensional summary of the past *for predicting the future*, plus a receipt:
a guarantee of how much you lost by dropping the rest.

That's it. **Table of pasts by futures → its rows are states → keep the important directions,
with a guarantee.** The rest of this page is the same three steps in different clothes.

---

## The same idea under different names

Each entry: what the field calls it, what it studies, and what the table, the states and the
"keep the important part" step turn into there.

**Logic and automata: the Myhill–Nerode theorem.** Studies which languages a finite machine can
recognize. The table says which endings complete which beginnings into a valid word. Distinct rows
are exactly the states of the smallest possible machine; a language is recognizable by a finite
machine exactly when there are finitely many distinct rows. Replace "yes/no" with numbers and you
get *weighted automata*, where the number of states is the rank of the table (Fliess's theorem).
Surprisingly simple questions about these machines are still open: whether a sequence defined by a
linear recurrence ever hits zero (the *Skolem problem*) is not known to be decidable.

**Machine learning theory: learning automata from questions.** Studies how to learn a hidden
machine by experimenting with it. Angluin's L\* algorithm learns a finite machine by filling in a
small corner of the table, asking "is this string accepted?". *Spectral learning* does the same
with statistics from data instead of questions and an SVD instead of exact bookkeeping. It learns
hidden Markov models without getting stuck in bad local optima, as iterative training can.

**Category theory: minimal realization as a factorization.** The table is a map from pasts to
futures. Any machine factors that map as "past → state → future", and the minimal machine is the
smallest thing that fits in the middle. *Reachable* states (the past side) and *observable*
differences (the future side) are mirror images, the algebra/coalgebra duality, and this is why
Brzozowski's odd-looking "reverse it twice" minimization algorithm works.

**Control theory: realization theory and model reduction.** Studies how to rebuild the inside of a
black box (an aircraft wing, a circuit) from input–output measurements, then simplify it. The table
maps past inputs to future outputs; its rank is the size of the smallest internal state that
explains it (the Ho–Kalman theorem). *Balanced truncation* ranks internal states by how easy they
are both to push and to see, discards the weak ones, and guarantees the simplified model is
close. Engineers use this every day.

**Dynamical systems: the Koopman operator.** Studies how things move: fluids, planets, weather.
The motion of points can be very nonlinear, but the way *measurements* of the system change over
time is always linear. Koopman's trick is to track the measurements instead of the points. The
table maps "now" to "later"; the important directions are the slow, persistent patterns (modes)
that outlast the noise. In fluid dynamics this is *dynamic mode decomposition*. *Takens' theorem*
says a single measurement recorded over a window of time is enough to reconstruct the state, which
is exactly how you build the table from one time series.

**Probability: hidden Markov models.** Studies systems whose real state is hidden and seen only
through noisy signals. The table is the probability of each past followed by each future, and the
hidden state is the bottleneck in the middle: given it, past and future are independent. The
standard forward and backward algorithms are the two halves of the factorization.

**Physics of complexity: causal states and ε-machines.** Studies how much memory a process really
has. Group pasts by the future they predict; the groups are *causal states*, and the resulting
minimal predictor is the *ε-machine*. This is Myhill–Nerode for random processes, and it gives a
principled measure of how complex a process is.

**Statistics: canonical correlation analysis (CCA).** Studies which aspects of one dataset
correlate most strongly with which aspects of another. Apply it to (past, future) and you get the
most predictive summaries of the past, ranked. For many processes this is exactly the SVD of the
table, with the right normalization.

**Graphs and data: spectral clustering.** Studies how to split a network or a dataset into natural
groups. Imagine a random walker on the data. Groups are places where it gets stuck for a long
time. The table is "where the walker is now → where it is a few steps later", and its top
directions mark the groups. Finding the best split is computationally hard; the *Cheeger
inequality* says this easy linear-algebra version is provably close. The same mathematics powers
*expander graphs* in theoretical computer science, and with them results like the logspace
algorithm for undirected connectivity and a combinatorial proof of the PCP theorem.

**Moving data: coherent sets.** Studies regions that move together in a flowing system, like an
ocean eddy that carries the same water for months. The table maps where things are now to where
they are later. Its top directions find the regions that hold together while everything around
them mixes. This is spectral clustering with time added in, and it is the version I care most
about.

**Pure mathematics and physics: spectra and trace formulas.** A deep end, as a teaser. Quantum
mechanics can evolve either the states or the measurements (the Schrödinger and Heisenberg
pictures); those are exactly the "move the distributions" and "move the measurements" views
from the Koopman entry above. In geometry, the "sound" (spectrum)
of a surface encodes its closed loops, in a formula with the same shape as the one linking the
zeros of the Riemann zeta function to the primes. "Can you hear the shape of a drum?" asks how much
of a shape its spectrum determines.

**Brains and neural networks.** Simple learning rules for neurons (Hebbian learning) compute
related decompositions, such as principal components. A language model's predictions form exactly this table (beginnings of
text by continuations), and it turns out to be approximately low-rank. Transformers trained on
data from a hidden process have been found to represent the hidden state internally, the same
"state" as above.

---

## Why I think this is deep, natural and practical

**Deep.** The same construction is a theorem in automata theory, control, ergodic theory,
geometry, statistics and the theory of random processes, and it touches open problems in
decidability, the PCP theorem, quantum mechanics and number theory. When an idea is discovered
independently in this many places, it is usually tracking something real.

**Natural.** It answers the most basic modelling question, "what about the past matters for the
future?", in the most direct way: write down the past-to-future map and look at what it actually
uses. The only choices are what counts as past and future, how to weigh them, and how much detail to
keep.

**Practical.** It is linear algebra, so it runs fast on large data, comes with error bars, and has
none of the local optima of iterative training. It is used routinely in aerospace, circuit design,
fluid dynamics, protein-folding simulation, climate science, image segmentation and web search.

**The honest caveat.** The SVD gives the best summary *in the sense you chose*; choosing the table
and the weights is where the thinking happens. And a simplified table isn't always a valid smaller
machine of the original kind.

---

## Where I'm taking it

My research uses this to look inside neural networks: write down the right past-to-future table for
the network (from the outside, prompts to continuations; from the inside, activations at one layer to
the next), find its coherent sets, and keep track of exactly what is guaranteed and what isn't as you
zoom in. Notes so far (AI-assisted drafts):

- [Computational Mechanics and Epsilon-Machines](https://charlesr-w.github.io/crw-blog/Computational-Mechanics-and-Epsilon-Machines/)
- [Characterizing Predictive Salience via Hankel Spectra](https://charlesr-w.github.io/crw-blog/Characterizing-Predictive-Salience-via-Hankel-Spectra/)
- [The Spectral Structure of Natural Data](https://charlesr-w.github.io/crw-blog/The-Spectral-Structure-of-Natural-Data/)
- [A Spectral Theory of Computation](https://charlesr-w.github.io/crw-blog/A-Spectral-Theory-of-Computation/)
- [Mori–Zwanzig, Hankel Geometry and Context-Free Memory](https://charlesr-w.github.io/crw-blog/Mori-Zwanzig-Hankel-Geometry-and-Context-Free-Memory/)
- [Dynamic Spectral Geometry for Identifying Computations](https://charlesr-w.github.io/crw-blog/Dynamic-Spectral-Geometry-for-Identifying-Computations/)
- [Hankel HMM reconstruction widget](https://charlesr-w.github.io/crw-blog/Hankel-HMM-Reconstruction-Widget/) (interactive)

---

## What's in this repo

| File | What it is |
|---|---|
| [`SYLLABUS.md`](SYLLABUS.md) | A course outline to hand to an AI tutor: big ideas, in order, with what to ask about. |
| [`docs/field-guide.md`](docs/field-guide.md) | The detailed version of this page: precise statements, names and references. |
| [`spec/`](spec/) | Plans for an interactive tutorial site on this material (work in progress, written for interpretability researchers). |
