# Per-page spec template

Every per-page spec (`spec/pages/NN-<id>.md`) uses exactly the sections below, in this order, with these numbers and
headings. Write "n/a" rather than deleting a section. The spec writer fills it from `SPEC.md` (which wins on any
conflict) and the sources; the page writer builds the page from `SPEC.md` + this template + the per-page spec and
nothing else. A completed example, page 1, follows the template below and is also saved as `pages/01-hankel.md`.
Amended 17 November 2026 with SPEC v1.1: the support-type list (section 4), the map-card format and edge links
(section 7), named fallback tours (section 5) and SPEC 6.3's shared-module names (section 12).

A per-page spec is detailed enough when a writer who has read nothing else can build the page without asking a
question: every figure's data source, default state and fallback is named; every claim has its support and
hypotheses; every running-example number is assigned to the builder or a live computation.

---

## 0. Header

A table with: page number; id (hash and file stem, from SPEC 2.1); tab label; kicker; title; **lede** (the page's
one-sentence claim, ≤ 45 words, this exact text goes on the page); depends on (recommended prior pages); edges (the
E-ids from SPEC 2.2 touching this page, all of them); faces of the running example used; main-path word budget
(within SPEC 5.2); spec status and date.

## 1. Reader outcome

A numbered list: "After this page the reader can …" (3-6 items, each testable: a thing they could do or explain).
Then one short paragraph: what they *see* (the visual moments the widgets must deliver).

## 2. Skim path

The exact skim path (SPEC 5.1): lede; hero figure id, title and fig-sub (verbatim); every h2 heading verbatim
(written as a claim, ≤ 12 words); the list of figure ids whose titles and fig-subs are on the skim path; ledger;
connections. End with a "skim test": the five to eight statements a skim-only reader should come away with.

## 3. Section outline

One subsection per h2, in page order: `### 3.k <id> "<heading verbatim>" (≈ words)`. For each:

- placement of figures (which figure sits where);
- content bullets: what the prose must establish, in order, including the specific running-example moments, the
  definitions introduced, and pointers to other pages (with edge ids);
- **key callout** gist (≤ 2 sentences; one per section at most);
- **disclosures**: title and contents for each `details.more` (with a word cap), and an "In other fields" disclosure
  wherever a term has another meaning elsewhere (glossary, SPEC appendix B).

Section ids are `<page>-<slug>`. Always end with the three fixed sections: Connections, Ledger, Sources.

## 4. Claims in order

A table, one row per claim, in the order they appear:

| id | claim | support | source / where shown | hypotheses the page must state | section |

- `id` is `C<page>.<n>`.
- `support` is one of: **theorem** (cited, with theorem number when the source numbers it), **theorem
  (scope-limited)**, **construction** (built on the page), **widget** (demonstrated in a named widget state:
  give the widget id and tour), **builder values** (a number, label or assertion computed by the builder: give the
  file and key), **standard** (textbook, cited), **empirical (cited)** (a published measurement that the page
  describes but does not reproduce), **empirical (programme)** (a measurement from the programme's own studies, quoted
  by fact key or file and never described as established), **pointer** (supported on another page, named),
  **quotation** (attributed, not the site's claim), **motivation** (requires the SPEC section 8 hook).
- A parenthesized qualifier may narrow a type (`theorem (asymptotic)`, `theorem (programme derivation)` for a result
  derived in the programme's notes, `construction (argument)`); claims with several supports join types with " + ".
  Results from the programme's repositories are cited as such (SPEC 5.5) whatever their type.
- Every bound must list its hypotheses here and on the page.
- Any claim about the running example's numbers or the meaning of a spectral direction must be supported by a named
  builder output or assertion, never by an expectation from the generator alone (SPEC 3.2).

Then a one-line list of "things not to claim" from SPEC appendix D that are tempting on this page.

## 5. Figures and widgets

One subsection per figure, in page order: `### 5.k <figure-id> "<title>" (live | static | live, hero |
live, centrepiece; key <widget key>)`. Figure ids are `<page>-fig-<slug>` and never equal a section id; live widgets
have a two- or three-letter key used for URL state (`<key>_r`, `<key>_tour`) and capture (SPEC 6.5-6.6). Every figure
states:

- **Purpose** (the one thing the reader should see; this becomes the fig-sub);
- **Layout** (figure width class, panels, chart types from `charts.js` / `view3d.js` / shared components);
- **Data** (live computation via which `lib/` module, or precomputed file and key; seeds);
- **Controls**: primary (≤ 4) and advanced, each with range and default;
- **Default state** (must equal the first tour);
- **fallbackTour** (the tour captured as the static image; the first tour unless stated; always a named tour, so a
  representative still of an animation gets its own paused tour);
- **What changes when each control moves** (per control, per panel);
- **Stat tiles** (if any) with exact definitions;
- **Tours**: id, exact parameters, one-line note; default first;
- **Caption**: the full Plotted/Values text (definitional; no interpretation), stating the running-example face and
  marking synthetic data;
- **Static fallback**: PNG file names per tour (`assets/fallback/<figure-id>-<tour>.png`), GIF if animated
  (`assets/fallback/<figure-id>.gif`: what it shows, duration);
- **Accessibility**: alt text; anything the fig-sub must carry for users without motion or colour;
- **Performance**: expected cost per interaction; parity tests if the computation is shared.

Static figures state purpose, data, content, generation method, caption and fallback.

## 6. Running example on this page

Faces used; any parameter that differs from SPEC 3.2 (and why); exactly what is precomputed (file, keys, builder
assertions) and what is live; the strain on this page and how the page states it; companion examples and where they
appear.

## 7. Connections

A table with one row per edge (from the header's edge list): edge id, other page, relation symbol (identical to SPEC
2.2), and the text for the connections strip (≤ 35 words; may add detail, must not upgrade the relation). Edge chips
link to `#map/map-edge-e<n>` (SPEC 6.5). Then the map-card text for page 0, in the form "title · claim (≤ 25
words) · knob: … · bound: … (≤ 20 words)"; the map copies it verbatim.

## 8. Ledger

The seven rows of SPEC 4.1, in order, filled for this page. The "Running example" row names the builder outputs or
live computations that supply its numbers. Must agree with the draft in SPEC 4.2 (refine, do not contradict; if a
change is needed, amend SPEC).

## 9. Things not to claim

The appendix-D items relevant to this page, plus any page-specific ones.

## 10. Notation used

Global symbols used (SPEC appendix A) and page-local symbols with their definitions and any warnings about clashes.

## 11. Sources

Full citations as in SPEC appendix C, with check status, the specific theorem/section numbers used, and code or data
provenance notes.

## 12. Implementation notes

Files the writer owns; shared modules used and any functions they must expose (using SPEC 6.3's names and signatures
wherever they exist); data files and builder keys; URL keys (prefixed per widget); tests (parity and tour checks).

## 13. Page-specific definition-of-done additions

Checks beyond SPEC 9.2 that are specific to this page (visual checks on screenshots, assertions surfaced in the UI,
wording constraints).

## Change log

Dated entries for every revision of the spec, and any deviations the page writer made with reasons.

---

# Worked model: page 1 (identical to `pages/01-hankel.md`)

# Page spec 01: Hankel matrices and realization

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. -->

## 0. Header

| field | value |
|---|---|
| page | 1 |
| id (hash, file stem) | `hankel` |
| tab label | Hankel |
| kicker | Page 1 · realization theory |
| title | Hankel matrices: reading a machine off its behaviour |
| lede (one-sentence claim, ≤ 45 words) | Write down how often each past is followed by each future and you get a table whose rank is the size of the smallest linear machine that could have produced it; its singular vectors are predictive states, and cutting it to rank r keeps the most visible predictive distinctions first. |
| depends on | none (entry page) |
| edges (SPEC 2.2) | E1, E2, E3, E11, E16 |
| faces of the running example | A′ (four-state chain, default), A (particle) |
| main-path words | 2,000-2,400 |
| spec status | v1.3, 2026-11-17 (checked against SPEC v1.2; causal-state proof replaced after round-1 review; earlier: instrument bins, ordering computed, envelope wording, id conventions) |

## 1. Reader outcome

After this page the reader can:

1. Build the Hankel table $H[p,f] = P(pf)$ of a process from its word probabilities (or counts), and say what a row
   and a column mean.
2. Explain why an HMM or weighted automaton with n states gives rank ≤ n, and how a rank-d table gives back a
   d-state weighted automaton (realization from shifted blocks), possibly with negative weights.
3. Place a history in predictive-state space and explain why histories lie inside a simplex (the belief simplex).
4. State what rank-r truncation guarantees (Eckart-Young for the table; the singular-value-automaton ℓ² bound for a
   realizable machine) and what it does not (a valid stochastic machine; an optimal smaller machine except in the
   one-letter case).
5. Predict that finite data hide the smallest singular values first, and quantify it (Weyl).
6. Say why the table's ordering of distinctions reflects the instrument as well as the dynamics.

What they see: three symbols producing a rank-4 table; histories ending in the same symbol landing in different
places; a spectrum ordered "which pair", "which right-hand well", "which left-hand well (only history can tell)";
negative "probabilities" from a truncated machine; σ₄ sinking into the sampling floor as data shrink.

## 2. Skim path

1. Lede (header).
2. Hero figure `hankel-fig-hero`: "From particle to table". Fig-sub: *A particle hops between four wells; a coarse
   instrument reports only three symbols; counting which pasts precede which futures fills the table on the right.*
3. Section headings (verbatim, these are the claims):
   - "A process is a table of pasts by futures"
   - "The table's rank is the size of the smallest linear machine"
   - "Singular vectors are predictive states"
   - "Truncation keeps the most visible predictive distinctions first"
   - "Finite data blur the smallest singular values first"
   - "What rank does not tell you"
4. Key-point callouts (one per section; gist in section 3 below).
5. Figure titles and fig-subs for `hankel-fig-bowtie`, `hankel-fig-rank`, `hankel-fig-states`,
   `hankel-fig-explorer`.
6. Ledger.
7. Connections strip.

Skim test: a reader of only the above should come away with: table of pasts × futures; rank = smallest linear
machine; three symbols can need four dimensions because history disambiguates; singular vectors = predictive states;
truncation keeps the pair first and the history-only distinction last; it is optimal for the table but may not be a
valid machine; data hide small singular values; rank is not the number of causal states.

## 3. Section outline

Section ids are `hankel-<slug>`; figure ids are `hankel-fig-<slug>` (SPEC 6.5). Word counts are main-path prose only.

### 3.1 `hankel-table` "A process is a table of pasts by futures" (≈ 350 words)

Placement: the hero figure sits between the lede and this heading.

- Introduce the running example in two sentences (link to the map's description): a particle in four wells, two
  pairs; an instrument reads $y = x_1 + x_2$ plus noise every Δ = 0.25 and reports `a` ($y < 0$), `b`
  ($0 \le y \le 1$) or `c` ($y > 1$). Point out that both wells of the left pair read `a`.
- A stationary process assigns a probability $P(w)$ to every word $w$. Define $H[p,f] = P(pf)$: rows indexed by
  pasts (prefixes), columns by futures (suffixes). Give one concrete entry from the hero ("row `ca`, column `ab`").
- Why the table is the right object: everything an observer could ever predict is in it; a model is a compression of
  it. Realization theory asks for the smallest machine whose behaviour is a given table.
- The finite block used on the page: all words of length ≤ 3 (40 rows, 40 columns, the empty word included; the
  empty row lists future probabilities $P(f)$).
- The **conditional** table $P(f \mid p) = H[p,f]/H[p,\varnothing]$ (rows divided by their first entry) has the same
  rank.

Key callout: "The table is model-free: it lists what follows what. Every model of the process is a way of
compressing this table."

Disclosure "In other fields: four tables that are all called Hankel" (≤ 250 words): process Hankel (this page),
block Hankel of impulse responses (page 2), delay/trajectory Hankel of a time series (page 3), extended logit
matrix (page 9). Link the glossary entry.

### 3.2 `hankel-rank` "The table's rank is the size of the smallest linear machine" (≈ 450 words)

- A hidden Markov model with n states, written as a weighted automaton: $P(s_1\cdots s_k) = \alpha^\top A_{s_1}
  \cdots A_{s_k}\beta$ with $A_s = \mathrm{diag}(E_{\cdot s})\,T$ ("emit from the current state, then move"),
  $\alpha = \pi$, $\beta = \mathbf 1$. Use this convention everywhere on the page.
- Hence $H[p,f] = (\alpha^\top A_p)(A_f\beta)$: a row vector depending only on the past times a column vector
  depending only on the future, so $H = R\,O$ with inner dimension n and rank $H \le n$. Show `hankel-fig-bowtie`.
- Converse (realization): if rank H = d, a d-dimensional weighted automaton reproduces every word probability. It is
  read off H and the **shifted blocks** $H_s[p,f] = P(psf)$: with $H \approx U_d\Sigma_dV_d^\top$,
  $A_s = \Sigma_d^{-1/2}U_d^\top H_s V_d\Sigma_d^{-1/2}$, $\alpha^\top$ = the empty-prefix row of
  $U_d\Sigma_d^{1/2}$, $\beta$ = the empty-suffix column of $\Sigma_d^{1/2}V_d^\top$. Cite Fliess 1974 and Carlyle &
  Paz 1971 for the theorem, Hsu-Kakade-Zhang 2012 and Balle et al. 2014 for the spectral algorithm. Coordinates are
  defined only up to an invertible change of basis.
- The realized automaton may have negative weights: it is a weighted automaton, not necessarily an HMM.
- Running example: show `hankel-fig-rank`: the four-state chain's 40 × 40 table has exactly four nonzero singular
  values. Three symbols, rank four: **the table still separates the two wells that share the symbol `a`**, faintly.
  The instrument barely tells them apart ($w_2$ occasionally reads `b`; the two wells lead toward different
  right-hand wells), so the distinction is real but small. Make the point with the two pasts the builder selects
  (`p01.json`, `chain.contrast_pasts`: the two pasts of length ≤ 3, each with probability ≥ 0.005, whose conditional
  rows differ most along the fourth right singular vector): their conditional futures differ slightly, and that
  difference is what the fourth singular value measures. Do not narrate the difference as "which way the particle
  entered"; at these parameters misreadings dominate (the builder's beliefs after `ba` put most mass on $w_2$ and
  $w_3$).
- One sentence on closure: the span of the top d singular directions is mapped into itself by every $A_s$ exactly
  when d ≥ rank; this is the sense in which realization finds a *closed* set of macrostates.

Key callout: "Rank counts linearly independent predictive distinctions. Here three symbols need four dimensions:
`a` is shared by two wells, and the table still tells them apart, faintly."

Disclosures:
- "The maths: realization from shifted blocks" (≤ 600 words): derive $A_s$; the realized automaton reproduces all
  words when the block has full rank (a *complete* basis); a finite block gives a lower bound on rank and a generator
  gives an upper bound.
- "Why the weights can be negative" (≤ 300 words): weighted automata vs HMMs; positive realization is a different,
  harder problem.
- "In other fields: Ho-Kalman, observable operator models" (≤ 250 words): the same factorization for linear systems
  (page 2, edge E1); Jaeger's observable operator models.

### 3.3 `hankel-states` "Singular vectors are predictive states" (≈ 400 words)

- The row of the conditional table for past p is the vector of probabilities of every future given p: a
  **predictive state** (Littman, Sutton & Singh 2002; this site ignores actions). Two pasts with the same row are
  indistinguishable for any future purpose.
- Rows live in a d-dimensional space; projecting them on the top right singular vectors gives d coordinates per past
  (transformed predictive state representation, Boots, Siddiqi & Gordon 2011). Left singular vectors are the dual
  picture: which futures discriminate pasts.
- Show `hankel-fig-states`. For the four-state chain, each history's predictive state is an affine image of its
  belief over the four wells, so all of them lie **inside a tetrahedral envelope** whose corners are the futures of
  the four wells (the corners are hypothetical: no history makes the particle certainly in one well). Pasts with the
  same last symbol spread out along the envelope according to what came before (tour `two-a`).
- The `a-run` tour: `b a…a` and `c a…a` with growing runs move toward a common limit, each length at a different
  point: these finite histories never repeat a predictive state, so there are infinitely many distinct predictive
  states of finite histories, all within four dimensions. Say in one sentence that this is not yet a count of
  causal states, which condition on the whole infinite past (finite-history beliefs can multiply even when there are
  finitely many causal states); the disclosure proves that this instrument's causal states are infinitely many too.
  Forward pointers to page 6 (E11) and page 10 (belief geometry inside networks; Shai et al. 2024).
- The particle (tour `particle`): its histories are computed from the particle's own table; where they fall relative
  to the chain's envelope is reported as computed (expected: slightly spread, since the particle remembers position
  within a well). Do not promise a particular look.

Key callout: "A past's predictive state is its row of the table. The SVD gives these rows coordinates, ordered by how
much they vary across pasts."

Disclosure "The maths: rows, beliefs, and why there are infinitely many causal states" (≤ 650 words):
1. For an HMM, $P(f \mid p) = b_p^\top P(f \mid \text{state})$ with $b_p$ the belief after p; rows are affine images
   of beliefs; hence the simplex envelope.
2. Injectivity: the four per-well future laws are linearly independent (that is rank 4), so distinct beliefs give
   distinct predictive states.
3. Finite histories (the `a-run` tour): reading symbol s updates the belief by the projective map
   $f_s(b)^\top = b^\top A_s/(b^\top A_s\mathbf 1)$. Every emission probability is positive (Gaussian readout noise) and
   every entry of $T_\Delta$ is positive, so $A_{\texttt a}$ is a strictly positive matrix; by Birkhoff's theorem
   $f_{\texttt a}$ is then a strict contraction of Hilbert's projective metric on the simplex (Birkhoff 1957; Seneta
   2006, ch. 3), with a unique fixed point $\eta^*_{\texttt a}$ (the Perron vector), and it is injective because
   $A_{\texttt a}$ is invertible. A periodic point of a strict contraction is its fixed point, so the iterates
   $f_{\texttt a}^n(f_{\texttt b}(\pi))$ along `b a^n` are pairwise distinct unless they start at $\eta^*_{\texttt a}$:
   infinitely many distinct predictive states of finite histories.
4. Why that is not yet a causal-state count: causal states condition on the semi-infinite past, and a process with
   finitely many causal states can have infinitely many finite-history beliefs before it synchronizes. Example (one
   sentence, no figure): the two-state unifilar machine with $A_{\texttt a} = \mathrm{diag}(0.8, 0.3)$,
   $A_{\texttt b} = \begin{pmatrix}0 & 0.2\\ 0.7 & 0\end{pmatrix}$ has two causal states, yet its beliefs after
   `b a^n` never repeat.
5. The causal states of the instrument are infinitely many. (i) By item 2, a causal state is the belief
   $\eta = P(\text{current well} \mid \text{infinite past})$, and reading s moves it to $f_s(\eta)$ exactly (Bayes'
   rule for the HMM). (ii) Suppose the stationary process visited only finitely many causal states, a set R. Each
   symbol has positive probability from every belief, so $f_s(R) \subseteq R$ for every s. (iii) $f_{\texttt a}$ is
   injective, so it permutes the finite set R; every point of R is then periodic for $f_{\texttt a}$, hence equal to
   $\eta^*_{\texttt a}$, so $R = \{\eta^*_{\texttt a}\}$. (iv) Then $f_{\texttt b}(\eta^*_{\texttt a}) = \eta^*_{\texttt a}$; but
   reading `b` after a long run of `a` moves the belief toward the right pair (builder: the ℓ¹ distance between
   $f_{\texttt b}(\eta^*_{\texttt a})$ and $\eta^*_{\texttt a}$ is large; ≈ 1.37 at κ = 0). Contradiction: no finite set of causal
   states carries the process, so its ε-machine is infinite. The builder checks and records every hypothesis: the
   smallest entry of $A_{\texttt a}$ (positive; ≈ 2e-8 at κ = 0, so the check uses exact emission integrals, not
   rounded tables), the smallest singular value of $A_{\texttt a}$, rank 4, and the distance in (iv). The page
   states this as a proof with those checked hypotheses, not as a sketch.

### 3.4 `hankel-truncate` "Truncation keeps the most visible predictive distinctions first" (≈ 450 words)

Centrepiece: `hankel-fig-explorer`.

- The four-state chain's spectrum (tour `exact4`) is ordered: σ₂ "which pair", σ₃ "which well in the right pair"
  (the instrument sees it directly: `b` vs `c`), σ₄ "which well in the left pair" (the instrument barely separates
  them: $w_2$'s occasional `b`, and where each leads). Quote the builder's values (expected ≈ 1.99, 0.69, 0.35, 0.008). Rank 2 keeps the pair; rank 3 adds the
  right-hand wells; rank 4 the left-hand wells. The particle (tour `particle`) adds a tail: where in the well.
- Make the instrument point explicitly (one short paragraph): the dynamics separate pairs slowly and wells within a
  pair faster, symmetrically; the table's ordering is set by what the instrument shows as well as by the dynamics,
  which is why the two wells of the left pair come last. Which weights the table uses decides what counts as
  important; page 3 whitens both sides (CCA) and gets the same order here, with canonical correlations ≈ 0.93, 0.74,
  0.11 (builder values). This is the first instance of "find the right SVD".
- Eckart-Young: the rank-r truncation $H_r$ is the closest rank-r matrix to H in spectral and Frobenius norm, with
  errors $\sigma_{r+1}$ and $(\sum_{i>r}\sigma_i^2)^{1/2}$. The bowtie's hatched bar is this tail.
- What it does not promise: $H_r$ is generally not the table of any process; the automaton realized at rank r can
  assign negative "probabilities" to some words (tour `negative`; stat tile "negative mass").
- What does hold for a machine: Balle, Panangaden & Precup's **singular value automaton**: put the exact automaton in
  a balanced form (the automaton analogue of page 2's balanced truncation, edge E2) and drop states; the dropped
  states cost at most $\sum_{i>r}\sigma_i(H)^2$ in squared ℓ² error over all words, where the σ are singular values of
  the *infinite* table (expected ≈ 5.93, 1.27, 0.57, 0.14 for the chain). The explorer plots this bound against the
  actual error.
- AAK in one paragraph: the *best* approximation by a smaller machine in the table's spectral norm attains
  $\sigma_{r+1}$ and is constructive for linear systems (page 2) and for automata over a one-letter alphabet; for more
  letters it is open. Do not claim more.

Key callout: "Rank-r truncation is the best rank-r table and, in balanced form, a machine with a bounded ℓ² error.
It is not guaranteed to be a probability model."

Disclosures:
- "The maths: Eckart-Young and what it does not promise" (≤ 400 words).
- "Singular value automata and the ℓ² bound" (≤ 600 words): automaton Gramians (the series
  $G_p = \alpha\alpha^\top + \sum_s A_s^\top G_p A_s$, $G_f = \beta\beta^\top + \sum_s A_s G_f A_s^\top$, convergent
  when the spectral radius of $\sum_s A_s\otimes A_s$ is below 1: the builder checks this, expected ≈ 0.93 for the
  chain), Hankel singular values $\sigma_i = \sqrt{\lambda_i(G_pG_f)}$, the balanced form, Theorem 7.1 and its
  hypotheses (minimal automaton, rational and square-summable f).
- "AAK, and why one letter" (≤ 350 words): Hankel-norm optimality; Glover's state-space construction for linear
  systems; Balle et al. 2021 and Lacroce et al. 2023 for one letter; the noncommutativity obstruction for several
  letters.

### 3.5 `hankel-data` "Finite data blur the smallest singular values first" (≈ 300 words)

- From N symbols, estimate H by word frequencies (explorer "data" control). Weyl: every estimated singular value is
  within $\|\hat H - H\|_2$ of the truth, so singular values below that floor cannot be trusted; Wedin: singular
  subspaces move by at most $\|\hat H - H\|_2$ over the gap.
- Running example (tour `fewdata`): the builder records the smallest N at which σ₃ clears the floor and the smallest
  at which σ₄ does (both for seed 0 and as a 3-seed mean); the tour uses an N between them, so σ₃ is resolved and σ₄
  is not. Quote those N on the page. Because σ₄ is tiny, it may need the largest N offered or more; if the builder
  finds σ₄ below the floor at every offered N, the page says so (that is itself the point).
- Hsu, Kakade & Zhang 2012: polynomial sample complexity for HMM learning, depending on the smallest relevant
  singular value (conditioning), not only on the number of states.

Key callout: "The smallest retained singular value sets the price of resolution: the floor falls like $1/\sqrt N$,
so resolving a distinction half as large takes about four times the data."

Disclosure "The maths: Weyl, Wedin, and the $N^{-1/2}$ floor" (≤ 400 words); the "four times" is a rule of thumb from
the floor's scaling, not a theorem.

### 3.6 `hankel-not` "What rank does not tell you" (≈ 250 words)

- Rank is not the number of causal states: rank ≤ number of causal states when that is finite, and here the rank is
  4 while the causal states are infinitely many (the contraction argument of 3.3's disclosure; the `a-run` tour shows
  finite histories). Edge E11; page 6.
- A finite block only shows a lower bound on rank. The particle's table resolves more than four dimensions (the
  builder reports $\sigma_5..\sigma_8$ above numerical precision); whether its exact rank is infinite is not claimed.
  "Rank 4" is a statement about a resolution, not about the system.
- Low logit rank in language models concerns a different table (logs of conditional probabilities); page 9, E16.

Key callout: "Rank counts linear predictive dimensions, not states, not causal states, and not the size of a
probabilistic model."

### 3.7 `hankel-connections` Connections

Rendered with `ui.connections` (section 7 of this spec).

### 3.8 `hankel-ledger` Ledger

Rendered with `ui.ledger` (section 8 of this spec).

### 3.9 `hankel-sources` Sources

Section 11 of this spec.

## 4. Claims in order

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C1.1 | A stationary process over a finite alphabet defines the table $H[p,f] = P(pf)$; the conditional table has the same rank. | construction | hero; `hankel-fig-rank` | stationarity | 3.1 |
| C1.2 | An HMM or weighted automaton with n states gives $H = RO$ with inner dimension n, so rank H ≤ n. | construction | bowtie; disclosure | — | 3.2 |
| C1.3 | If rank H = d, a d-state weighted automaton reproducing all word probabilities exists and is read off H and its shifted blocks; its weights may be negative; it is unique up to change of basis. | theorem | Fliess 1974; Carlyle & Paz 1971; Balle et al. 2014; HKZ 2012 | the block must have full rank (complete basis) | 3.2 |
| C1.4 | The four-state chain gives a rank-4 table from three symbols; the builder's two contrast pasts have different conditional futures, by an amount of the size of σ₄. | widget | `hankel-fig-rank`; explorer tour `exact4` | builder assertion rank = 4 | 3.2 |
| C1.5 | Rows of the conditional table are predictive states; SVD coordinates give a d-dimensional predictive state representation. | theorem (standard) | Littman, Sutton & Singh 2002; Boots, Siddiqi & Gordon 2011 | uncontrolled setting | 3.3 |
| C1.6 | For an HMM, predictive states are affine images of beliefs, so they lie inside a simplex envelope. | construction | `hankel-fig-states` tour `simplex`; disclosure item 1 | — | 3.3 |
| C1.7 | For the chain, the beliefs after the finite histories `b a^n` (and `c a^n`) are distinct for every n (infinitely many finite-history predictive states in four dimensions), and the stationary process has infinitely many causal states. | theorem (proof in disclosure items 3-5) + builder checks | disclosure; tour `a-run` (finite histories only) | rank 4; $A_{\texttt a}$ strictly positive and invertible; $f_{\texttt b}(\eta^*_{\texttt a}) \ne \eta^*_{\texttt a}$ (all checked by the builder); Birkhoff contraction | 3.3 |
| C1.8 | $H_r$ is the closest rank-r matrix to H, with spectral error $\sigma_{r+1}$ and Frobenius error $(\sum_{i>r}\sigma_i^2)^{1/2}$. | theorem | Eckart & Young 1936 | — | 3.4 |
| C1.9 | The chain's table orders its distinctions pair, right-pair wells, left-pair wells; the particle adds a tail. | widget + builder assertion | explorer tours `exact4`, `particle`; builder sign-pattern check (below) | ordering is computed, not derived from the generator | 3.4 |
| C1.10 | The ordering depends on the instrument; whitening both sides (CCA) gives the same order here. | widget + builder values | explorer advanced view `whitened`; builder canonical correlations | — | 3.4 |
| C1.11 | $H_r$ need not be any process's table; the rank-r realized automaton can give negative values. | widget | tour `negative` | — | 3.4 |
| C1.12 | Singular-value-automaton truncation to r states has squared ℓ² error ≤ $\sum_{i>r}\sigma_i(H)^2$. | theorem | Balle, Panangaden & Precup 2019, Thm 7.1; explorer panel (c) | minimal automaton; f rational and square-summable (spectral radius of $\sum_s A_s\otimes A_s$ < 1, builder-checked); σ of the infinite table | 3.4 |
| C1.13 | Optimal Hankel-norm approximation by a smaller machine attains $\sigma_{r+1}$ and is constructive for linear systems and one-letter automata; open for several letters. | theorem (scope-limited) | Glover 1984; Balle et al. 2021; Lacroce et al. 2023 | one letter / LTI | 3.4 |
| C1.14 | Estimated singular values lie within $\|\hat H - H\|_2$ of the truth; subspaces move by at most that over the gap. | theorem | Weyl; Wedin 1972 | — | 3.5 |
| C1.15 | In the example σ₃ clears the sampling floor at a smaller N than σ₄ (values from the builder). | widget | tour `fewdata` | — | 3.5 |
| C1.16 | Spectral HMM learning has polynomial sample complexity depending on conditioning, not just state count. | theorem | Hsu, Kakade & Zhang 2012 | their rank and separation conditions | 3.5 |
| C1.17 | Rank ≤ number of causal states (when finite), often strictly; here rank 4 with infinitely many causal states. | theorem + pointer (C1.7) | Shalizi & Crutchfield 2001; Haslinger et al. 2010 App. C | finite causal states for the inequality | 3.6 |
| C1.18 | Finite blocks give lower bounds on rank; the particle's table resolves more than four dimensions. | construction + builder values | explorer tour `particle` | — | 3.6 |

Things not to claim on this page (SPEC appendix D): rank = number of causal states; truncation gives a smaller
stochastic machine; AAK for several letters or for language models; the four-state chain equals the particle; a
finite block certifies the rank of the process; the generator's slow modes are the table's singular directions; the
particle's table has infinite rank.

## 5. Figures and widgets

### 5.1 `hankel-fig-hero` "From particle to table" (live, hero; key `hr`)

- **Purpose:** a coarse three-symbol instrument on a four-well particle produces a stream whose past/future
  co-occurrences fill a table.
- **Layout:** `figure.fig.full.card`, three panels left to right (stacked on phones): (a) contour map of $V$ over Ω
  (ink contours, wells as ink-outlined circles coloured `--c-well-k`, labelled $w_1..w_4$, faint grey lines at the
  bin edges $x_1 + x_2 = 0$ and $x_1 + x_2 = 1$), the particle as a dot with a fading trail; (b) the readout $y_t$ as
  a scrolling trace over the last 40 samples with shaded bands for `a`/`b`/`c` and the symbol letters in monospace
  below each sample, the true well shown as a thin coloured strip under the letters; (c) the depth-2 Hankel table
  (13 × 13, words ≤ 2, rows and columns grouped by length) as a `heatmap` (`seq` map, fixed range), with the cell for
  (last two symbols, next two symbols) outlined in accent and its count incrementing.
- **Data:** live. Face A simulation (Euler-Maruyama, dt = 0.0025, seed 0) from `lib/example.js`; the table
  accumulates empirical counts from the live stream, normalized; a toggleable faint layer shows the exact depth-2
  table (`data/hankel/p01.json`, `particle.H2`) so the empirical one visibly converges.
- **Controls:** transport (play/pause, speed ×1/×4/×16), reset. Nothing else.
- **Default state (= first tour):** `default`, t = 0, autoplay when scrolled into view (centrepiece rule); under
  reduced motion, the `frame-late` still is shown instead.
- **What changes:** time advances; the particle hops (rarely between pairs); letters append; the outlined cell moves
  and the table sharpens.
- **Tours:** `default` (t = 0, playing); `frame-entry` (just after the particle enters the left pair from $w_4$, so
  the stream reads `…c a`); `frame-late` (after 10⁴ samples). The builder records the seed-0 sample indices of these
  events in `p01.json` (`hero.events`).
- **fallbackTour:** `frame-late`.
- **Caption:** *Plotted:* (a) contours of $V(x_1,x_2)$, wells $w_1..w_4$, the particle's last 2 time units of path,
  bin edges; (b) readout $y = x_1 + x_2 + \xi$ against sample index, bins $y < 0$ (`a`), $0 \le y \le 1$ (`b`),
  $y > 1$ (`c`), true well as the coloured strip; (c) $\hat H[p,f]$, frequency of past p followed by future f, words
  of length ≤ 2, current cell outlined. *Values:* $h_x = 2.5$, $h_y = 1.5$, $b = 0.6$, $D = 0.5$, $\sigma_y = 0.25$,
  Δ = 0.25, seed 0. Running example, face A. `synthetic`.
- **Static fallback:** `assets/fallback/hankel-fig-hero-frame-late.png`; GIF `assets/fallback/hankel-fig-hero.gif`
  (≈ 6 s at speed ×4 from `frame-entry`).
- **Accessibility:** alt text: "A particle moving between four wells, its noisy readout binned into symbols a, b, c,
  and a table of past and future symbol pairs filling in." The fig-sub carries the message without motion.
- **Performance:** ≤ 2 ms per frame (one particle, 100 substeps per sample at ×1); heatmap redraw throttled to every
  4 samples.

### 5.2 `hankel-fig-bowtie` "One table, two factors" (static SVG)

- **Purpose:** H factors as (past-side vector) × (future-side vector) through a small knot; the knot's width is the
  rank.
- **Data:** shared `bowtie` component with labels: left "pasts p (prefixes)", left norm "plain probabilities", right
  "futures f (suffixes)", right norm "plain probabilities", knot bars = the chain's σ₁..σ₆ from `p01.json` (four
  nonzero, two zero drawn as empty outlines), r = 4, bound label "lost: σ_{r+1} (spectral), (Σ_{i>r} σ_i²)^{1/2}
  (Frobenius)". Bars are drawn on a square-root scale (σ₄ would be invisible on a linear one); the caption says so.
- **Controls:** none required; if the component's draggable r is enabled, dragging r updates the hatching and bound
  label (no URL state).
- **Caption:** *Plotted:* schematic of $H = R\,O$: rows of R are $\alpha^\top A_p$, columns of O are $A_f\beta$;
  bars are the singular values of the four-state chain's table (words ≤ 3), square-root scale. *Values:* as the hero.
- **Fallback:** the SVG itself; PNG export `assets/fallback/hankel-fig-bowtie-default.png` for cross-posting.

### 5.3 `hankel-fig-rank` "Three symbols, rank four" (static, rendered by the page module)

- **Purpose:** the chain's 40 × 40 table has exactly four nonzero singular values, and two pasts that end alike
  differ by a small, real amount.
- **Data:** exact chain table (`p01.json`, `chain.H3`).
- **Content:** left: heatmap of H (rows and columns: words ≤ 3 grouped by length, `seq` map, colour bar "$P(pf)$"),
  the two contrast pasts (`chain.contrast_pasts`) marked by side ticks; middle: bar chart of the difference of their
  conditional rows over the 40 futures (`div` colours, own symmetric scale, labelled "difference, note the scale"); right: bar chart of
  σ₁..σ₁₀ on a log axis with the numerical zero floor (1e-15) as a dashed reference line.
- **Generation:** drawn by `p_hankel.js` at fixed size from the data (no interaction), so it updates if the builder
  data change.
- **Caption:** *Plotted:* left, $H[p,f] = P(pf)$ for all words p, f of length ≤ 3 over {a, b, c} (40 × 40, empty word
  first); middle, the difference of the conditional rows for the two marked pasts; right, singular values $\sigma_i$ of
  H, log scale. *Values:* four-state chain at Δ = 0.25 (face A′).
- **Fallback:** PNG `assets/fallback/hankel-fig-rank-default.png` (captured like a widget with one tour).

### 5.4 `hankel-fig-states` "Predictive-state space" (live, 3-D; key `st`)

- **Purpose:** histories become points inside a tetrahedral envelope whose corners are the wells' futures; histories
  ending in the same symbol but entered differently land in different places.
- **Layout:** `figure.fig.wide.card`, `view3d` on the left (height 440), side panel (tours, controls, legend, two stat
  tiles) on the right.
- **Data:** chain: computed live from the automaton (all histories of length 1..L, conditional rows over the 40
  suffixes of length ≤ 3, beliefs by the forward filter). Particle: precomputed conditional rows (`p01.json`,
  `particle.states`, histories ≤ 6, Float32 base64) with the chain's filter beliefs as an approximate colouring
  (stated in the caption).
- **Coordinates:** centre the conditional rows (weighted by $P(p)$), take the top three right singular vectors of the
  $P(p)^{1/2}$-weighted centred table, project. Anchors: the four per-well future laws $P(f \mid w_k)$ projected the
  same way, drawn as labelled ink-outlined markers in well colours, hull edges on (the envelope). The legend calls
  them "pure-well futures (envelope corners; not reachable histories)".
- **Encoding:** point colour = `mixBary(belief, wellColours)`; size ∝ $P(p)^{1/2}$ (clamped 2-7 px); hover shows the
  history string, P(p), belief over $w_1..w_4$.
- **Controls (primary):** model (`chain` | `particle`); max history length L (slider 1-6, default 4); colour by
  (`belief` | `last symbol` | `pair`). Advanced: show anchors/hull (toggle, on); point size scale.
- **What changes:** model swaps point sets; L adds longer histories (more points, filling toward edges); colour-by
  re-colours (last symbol: `a` dark ink, `b` mid grey, `c` light grey with outlines; pair: `--c-pair-L/R` by the most
  probable pair).
- **Stat tiles:** "distinct predictive states shown" (count after merging points closer than 1e-9); "dimension of
  their span" (numerical rank of the centred rows; 3 for the chain, i.e. 4 including the constant).
- **Tours:** `simplex` (default: chain, L = 4, belief); `two-a` (chain, L = 3, colour by last symbol, rings and
  labels on the builder's contrast pasts); `a-run` (chain, L = 6, highlight `b a^n` and `c a^n` for n = 1..5 joined by thin lines,
  labels at n = 1 and 5); `particle` (particle, L = 4, belief).
- **fallbackTour:** `simplex`.
- **Caption:** *Plotted:* each dot is a past p (all words of length 1..L), placed at the projection of its predictive
  state $P(f \mid p)$ (f over words of length ≤ 3) onto the top three weighted principal directions; markers $w_k$ are
  the pure-well futures $P(f \mid w_k)$, joined as the envelope; colour mixes well colours by the belief
  $P(w_k \mid p)$ (for the particle, the chain's belief, an approximation); size ∝ $P(p)^{1/2}$. *Values:* face A′ or
  A, Δ = 0.25.
- **Fallback:** PNG per tour from a fixed camera (yaw −0.6, pitch 0.9); GIF of a slow rotation for `simplex`.
- **Performance:** ≤ 1,093 points; recomputation on L change < 20 ms.

### 5.5 `hankel-fig-explorer` "Rank, truncation and data" (live, centrepiece; key `ex`)

- **Purpose:** the spectrum decides what survives truncation; truncation is optimal for the table and bounded for a
  balanced machine but can produce non-probabilities; data hide the small singular values first.
- **Layout:** `ui.simLayout` in `figure.fig.full.card`: main view = four linked panels in a 2 × 2 grid; side panel
  (320 px) = tours, controls, stat tiles, legend.
  - (a) **Table**: heatmap of H (or $\hat H$) for words ≤ 3 (40 × 40), grouped by word length, fixed colour range per
    model.
  - (b) **Spectrum**: σ₁..σ₁₂ (log y). For the chain and the particle, bars are coloured by the **computed** meaning
    of each direction (the builder labels directions 2-4 by the sign pattern of the pure-well futures on each right
    singular vector: "pair" `--c-pair-L` tint, "right-pair wells" `--c-well-4` tint, "left-pair wells" `--c-well-2`
    tint; σ₅+ `--c-other` "within well"); if the builder's labels differ from this expected order, the page uses the
    builder's. r is a vertical accent line, discarded bars hatched. With sampled data: a dashed line at the sampling
    floor $\|\hat H - H\|_2$ (mean over 3 seeds) and the exact σ as open circles behind the bars. For the particle,
    infinite-table σ as small ticks.
  - (c) **Error vs r**: r = 1..8 on x; y log. Series: "spectral learning from this table" (ℓ² error over all words
    of length ≤ 6; solid ink, dots); "balanced (SVA) truncation of the exact machine" (ℓ² over words ≤ 8; `seq-5`);
    "SVA bound $(\sum_{i>r}\sigma_i^2)^{1/2}$" (dashed `seq-5`). The SVA series are exact-model quantities and do not
    change with the data control (the legend says so). The ℓ² over words ≤ 8 can only understate the full ℓ² error;
    the caption says so.
  - (d) **Word probabilities at r**: scatter of true vs reconstructed $P(w)$ for the 729 words of length 6 (log-log;
    negative reconstructed values drawn in accent along a "< 0" band at the bottom).
- **Data:** chain and catalogue models: live (exact tables from the automaton; sampled tables from live simulation,
  seeds 0-2). Particle: precomputed exact depth-3 blocks and shifted blocks, exact word probabilities ≤ 8,
  infinite-table σ (top 12), SVA errors r = 1..8, sampled counts for N ∈ {10³, 10⁴, 10⁵, 10⁶} × seeds 0-2
  (`p01.json`). Catalogue models: Golden Mean, Zero-One-Random, Mess3 (matrices ported from
  `crw-blog/assets/widgets/hankel-hmm-src/build.py:27-70`); their tables and SVA data computed live.
- **Controls (primary):**
  1. model: `chain` | `particle` | `golden` | `z1r` | `mess3` (select; labels "four-state chain", "particle",
     "Golden Mean", "Zero-One-Random", "Mess3");
  2. r: slider 1-8 (marks at 2 "pair" and 4 "all wells" for chain and particle);
  3. data: segmented `exact` | `10³` | `10⁴` | `10⁵` | `10⁶`.
  Advanced: seed (0-2); table view (`joint` | `conditional` | `whitened`: canonical-correlation matrix of past and
  future windows of length 3, $D_p^{-1/2}JD_f^{-1/2}$); error metric for panel (c) (ℓ² | ℓ¹ on length-6 words after
  clipping and renormalizing, as in the crw-blog widget).
- **What changes when each control moves:**
  - model: all panels recompute; the meaning colours and r marks apply only to chain and particle.
  - r: (b) moves the accent line and hatching; (c) moves the cursor; (d) redraws the scatter for the rank-r
    reconstruction; tiles update.
  - data: (a) shows the empirical table; (b) shows sampled σ as bars, exact σ as circles, and the floor line; (c)'s
    spectral-learning series recomputes from the sampled table; SVA series unchanged.
  - seed: resamples (data ≠ exact only).
  - table view: (a) and (b) show the chosen table and its spectrum (the caption names which); (c) and (d) always use
    the joint table, because realization needs it (the legend says so).
- **Stat tiles:** "numerical rank" (exact: count of σ_i > 1e-10 σ₁; sampled: count above the floor, labelled "above
  floor"); "$\sigma_{r+1}/\sigma_1$"; "ℓ² error at r"; "negative mass at r" (sum of $\max(0, -\hat P(w))$ over
  length-6 words).
- **Tours** (default first):
  1. `exact4`: chain, exact, r = 4. Note: "Four nonzero singular values; at r = 4 the reconstruction is exact to
     rounding."
  2. `pairs`: chain, exact, r = 2. Note: "Two dimensions keep which pair the particle is in."
  3. `negative`: model and r chosen by the builder as the case with the largest negative mass among r < rank over
     chain, particle and Mess3 (recorded in `p01.json`, `tours.negative`). Note: "The truncated machine assigns
     negative values to some words."
  4. `particle`: particle, exact, r = 4. Note: "Beyond four, a tail: where in the well. The SVA bound sits above the
     actual error."
  5. `fewdata`: chain, N and seed recorded by the builder (σ₃ above the floor, σ₄ not), r = 4. Note: "σ₄ is below the
     sampling floor at this N."
  6. `mess3`: Mess3, exact, r = 3. Note: "Rank 3, yet infinitely many causal states (page 6)."
- **fallbackTour:** `exact4`.
- **Caption:** *Plotted:* (a) $H[p,f]$, or $\hat H$, or $P(f \mid p)$, or the whitened window table; (b) singular
  values of the shown table (bars), exact values (circles), infinite-table values (ticks, particle only), sampling
  floor $\|\hat H - H\|_2$ (dashed), retained r (line); (c) ℓ² error between true and reconstructed word probabilities
  against r, for spectral learning from the joint table and for SVA truncation of the exact machine (words ≤ 8, a
  lower estimate of the full ℓ² error), with the SVA bound; (d) true vs rank-r reconstructed probabilities of the 729
  words of length 6. *Values:* model, data and seed as set; Δ = 0.25.
- **Static fallback:** PNG per tour (`assets/fallback/hankel-fig-explorer-<tour>.png`); GIF stepping r = 1..6 on the
  `particle` tour (1 s per frame).
- **Performance:** exact tables: SVD of 40 × 40 and evaluation of ≤ 9,841 words at r ≤ 8 in < 30 ms; live sampling of
  10⁶ symbols < 150 ms (status "sampling…"). Parity: realization and metrics match the builder to 1e-9 on exact
  tables.
- **Accessibility:** each panel has an `aria-label`; tiles are text; tours announce their note.

## 6. Running example on this page

- Faces: A′ (default), A (particle). Parameters exactly as SPEC 3.2: $h_x = 2.5$, $h_y = 1.5$, $b = 0.6$,
  $\kappa = 0$, $D = 0.5$, $\sigma_y = 0.25$, Δ = 0.25, bins `a` $y < 0$, `b` $0 \le y \le 1$, `c` $y > 1$.
- Automaton convention: $A_s = \mathrm{diag}(E_{\cdot s})\,T$, $\alpha = \pi$, $\beta = \mathbf 1$.
- Precomputed (`tools/build_example.py` → `site/data/hankel/p01.json`, with config and assertions):
  - chain: T, E, π; exact H and shifted blocks (depth 3, and depth 2 for the hero); infinite-table σ via Gramians; SVA
    truncations r = 1..8 and their ℓ² errors over words ≤ 8; direction labels for σ₂..σ₄; whitened window spectrum
    (`chain.whitened`: canonical correlations of past and future windows of length 3; page 6 reads it);
    `contrast_pasts`;
    `tours.negative`; `tours.fewdata` (N, seed); `a-run` checks (pairwise distinctness of the finite-history beliefs
    for n ≤ 50) and `causal` checks (smallest entry and smallest singular value of $A_{\texttt a}$; fixed point
    $\eta^*_{\texttt a}$; ℓ¹ distance from $f_{\texttt b}(\eta^*_{\texttt a})$ to $\eta^*_{\texttt a}$; assert all three positive).
  - particle: 60-mode spectral automaton (assert word-probability error ≤ 1e-8 vs the full grid on words ≤ 4);
    exact H and shifted blocks (depth 2 and 3); exact probabilities of words ≤ 8; infinite-table σ (top 12); SVA
    errors r = 1..8; direction labels; sampled word counts (words ≤ 7) for N ∈ {10³, 10⁴, 10⁵, 10⁶} × seeds 0-2
    (pooled stationary chains, Euler-Maruyama dt = 0.0025); predictive-state rows for histories ≤ 6; hero event
    indices.
  - assertions: chain rank = 4 (tol 1e-10); $T = T^x\otimes T^y$ at κ = 0 (1e-10); emission table within 0.02 of
    SPEC 3.2's expected values; direction 2 separates the pairs (pure-well futures of $w_1, w_2$ on one side, $w_3,
    w_4$ on the other) for both chain and particle; ordering σ₂ > σ₃ > σ₄ with σ₄/σ₃ < 0.1 (chain); spectral radius of
    $\sum_s A_s\otimes A_s$ < 1 (both); SVA error ≤ bound for r = 1..8 (both). **If an assertion fails, stop and amend
    this spec; do not retune parameters silently.**
- Live: chain and catalogue tables, sampling of the chain, all reconstructions, the hero simulation, the
  predictive-state projection for the chain.
- Strain: the four-state chain is an idealization (it forgets position inside a well); 3.1 says so and the particle
  is the corrective. The instrument, not the generator, sets the table's order; 3.4 says so.
- Companion: the catalogue processes are available in the explorer; the main path uses only Mess3 (tour `mess3`).

## 7. Connections

| edge | other page | rel. | text for the connections strip (≤ 35 words) |
|---|---|---|---|
| E1 | 2 Linear control | `=` | The same factorization, past inputs × future outputs, for linear systems: Ho-Kalman realization is this page's realization from shifted blocks, and Hankel rank is minimal state dimension. |
| E2 | 2 Linear control | `≈` | Balanced truncation is the linear-systems version of singular-value-automaton truncation; AAK's optimal approximation is constructive there and for one-letter automata only. |
| E3 | 3 Koopman | `=` | Each table entry is (state distribution after the past) · (probability of the future from each state): a transfer operator followed by a Koopman operator. |
| E11 | 6 Comp. mechanics | `=` | Causal states are the classes of equal rows of the conditional table; their number bounds the rank from above, and can be infinite when the rank is 4. |
| E16 | 9 LLMs from outside | `=` | A language model's extended logit matrix is a Hankel-like table of log-probabilities; its rank equals the dimension of an input-switched affine network that reproduces the model. |

Map card text: "Hankel · the table of pasts by futures · knob: rank r · bound: σ_{r+1} for the table, Σ_{i>r} σ_i² for
a balanced machine."

## 8. Ledger

| row | content |
|---|---|
| Decomposed | The process Hankel table $H[p,f] = P(pf)$, pasts × futures, plain probabilities on both sides (finite block: words ≤ 3; infinite: all words). |
| Knob | Rank r; also block depth and sample size N. |
| Discarded at r | Distinctions between pasts that change future probabilities only through the small singular values: at r = 2, which well; at r = 3, which well in the left pair (the one only history reveals); at r = 4 (particle), where within a well. |
| Bound | Table: $\|H - H_r\|_2 = \sigma_{r+1}$, $\|H - H_r\|_F^2 = \sum_{i>r}\sigma_i^2$, optimal over rank-r matrices (Eckart-Young; `theorem`; $H_r$ need not be a process). Machine: SVA truncation, $\|f - \hat f_r\|_{\ell^2}^2 \le \sum_{i>r}\sigma_i(H)^2$ (Balle, Panangaden & Precup 2019, Thm 7.1; minimal automaton, square-summable f; `theorem`). Optimal smaller machine (AAK): `theorem (scope-limited)`, one letter only. |
| From data | $|\hat\sigma_i - \sigma_i| \le \|\hat H - H\|_2$ (Weyl); subspace angle ≤ $\|\hat H - H\|_2$/gap (Wedin); HKZ 2012 sample complexity under conditioning. |
| Running example | From the builder: chain σ₁..σ₄ and their direction labels; particle σ₂..σ₈; ℓ² error and SVA bound at r = 2, 3, 4; the N at which σ₃ and σ₄ clear the floor. |
| Budget line | T (truncation), S (sampling). |

## 9. Things not to claim

Rank = number of causal states; distinct beliefs after finite words prove infinitely many causal states (they do not; item 4 of 3.3's disclosure); a rank-r table is a smaller stochastic machine; AAK for several letters or for
language models; the four-state chain equals the particle; a finite block certifies the rank of the process; the
generator's slow modes are the table's singular directions; the particle's table has infinite rank; predictive states
"fill" the tetrahedron.

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, H, $H_r$, p, f, $\mathcal A$, $\mathcal A^*$, Δ, $w_1..w_4$, L/R pairs,
$s_t$, $y$, $\sigma_y$, π, $n_c$, d.
Page-local: $A_s$ (symbol operators; s a symbol, never σ), α, β (initial and final weights; this β is not the kernel
bandwidth: say so in a side note), $H_s$ (shifted block), $R$, $O$ (past and future factors), $G_p, G_f$ (automaton
Gramians, disclosure only), $b_p$ (belief after p), J, $D_p$, $D_f$ (window table and its marginals, advanced view
only).

## 11. Sources

Cite as in SPEC appendix C; check status there.

- Ho & Kalman 1966; Fliess 1974 [V]; Carlyle & Paz 1971 [V].
- Jaeger 2000 [V].
- Littman, Sutton & Singh 2002; Boots, Siddiqi & Gordon 2011.
- Hsu, Kakade & Zhang 2012.
- Balle, Carreras, Luque & Quattoni 2014.
- Balle, Panangaden & Precup 2019 (Theorem 7.1).
- Balle, Lacroce, Panangaden, Precup & Rabusseau 2021; Lacroce, Balle, Panangaden & Rabusseau 2023.
- Glover 1984; Adamyan, Arov & Krein 1971.
- Eckart, C. & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika* 1(3),
  211-218. [V]
- Weyl (eigenvalue perturbation, 1912) and Wedin, P.-Å. (1972). Perturbation bounds in connection with singular
  value decomposition. *BIT* 12, 99-111. [V]
- Shalizi & Crutchfield 2001; Haslinger, Klinkner & Shalizi 2010 (App. C).
- Birkhoff, G. (1957), Trans. AMS 85; Seneta, E. (2006), *Non-negative Matrices and Markov Chains*, ch. 3 (projective
  contraction of strictly positive matrices). [V]
- Shai et al. 2024 (pointer only).
- Code provenance (not a citation): the realization and metrics code is ported from the programme's Hankel-HMM
  widget, `crw-blog/assets/widgets/hankel-hmm-src/build.py`.

## 12. Implementation notes

- Files: `site/content/hankel.html`, `site/js/p_hankel.js`, helpers `site/js/p_hankel_hero.js`,
  `p_hankel_states.js`, `p_hankel_explorer.js`; data `site/data/hankel/p01.json`, `site/data/hankel/widgets.json`.
- Shared modules used: `lib/example.js` (simulation, readout), `lib/hankel.js` (words, blocks, realization, SVA,
  metrics), `lib/linalg.js` (SVD, eigh), `lib/rng.js`, `lib/bowtie.js`, `charts.js`, `view3d.js`, `ui.js`.
- `lib/hankel.js` must expose: `words(alphabetSize, maxLen)`, `hankelFromProbs(probFn, prefixes, suffixes)`,
  `hankelFromCounts(counts, prefixes, suffixes)`, `shiftedBlocks(...)`, `realize(H, Hs, r)` → `{A[], alpha, beta}`,
  `wordProbs(wfa, words)`, `gramians(wfa)` → `{Gp, Gf}`, `svaTruncate(wfa, r)`, `metrics(pTrue, pHat)`.
- Widget keys and URL state: hero `hr` (`hr_speed`, `hr_tour`); states `st` (`st_model`, `st_L`, `st_col`,
  `st_tour`); explorer `ex` (`ex_model`, `ex_r`, `ex_n`, `ex_seed`, `ex_view`, `ex_err`, `ex_tour`). The rank figure
  has key `rk` with the single tour `default`.
- Tests: parity of `realize` and `svaTruncate` against the builder on the chain and Mess3 (1e-9); a node test that
  each tour's stat tiles match the builder's recorded values.

## 13. Page-specific definition-of-done additions

- [ ] The contrast-pasts difference panel of `hankel-fig-rank` is legible at default size (check the screenshot) and its
      scale label is visible.
- [ ] The SVA bound lies above the SVA error at every r for chain and particle (builder assertion surfaced: if
      violated, the page shows an error, never a silent plot).
- [ ] The `negative` tour shows nonzero negative mass in the tile.
- [ ] The word "optimal" appears only with its norm and its class of competitors ("optimal among rank-r matrices in
      spectral norm").
- [ ] Every statement of the spectrum's meaning on the page uses the builder's direction labels.

## Change log

- v1 (2026-11-17): first full spec; worked model for `PAGE_TEMPLATE.md`.
- v1.1 (2026-11-17): after cross-family review. Bins moved to $y<0$, $0\le y\le1$, $y>1$ (the left pair shares `a`),
  because with bins at ±1 the table ranked "is it `b`" above "which pair"; contrast pasts chosen by the builder
  (an "entry history" narrative was checked and found wrong at these parameters); spectrum meanings computed and
  asserted by the builder; "fill a tetrahedron" → "inside a tetrahedral envelope"; infinite-states claim given an
  argument with checked hypotheses; particle's infinite rank no longer claimed; ids and tour keys follow SPEC 6.5.
- v1.2 (2026-11-17): checked against SPEC v1.1 (reconciliation of all page specs). Changes: the whitened window
  spectrum gets the key `chain.whitened` (read by page 6); claims-table support types written in the template's
  amended vocabulary (`builder values`, `pointer`). No change to content, figures or the ledger.
- v1.3 (2026-11-17): round-1 review fix (SPEC v1.2). The old argument (beliefs after `b a^n` never repeat) proved
  infinitely many predictive states of **finite** histories from the stationary start, not infinitely many causal
  states: a two-state unifilar machine has the same finite-history behaviour. The `a-run` tour is kept and described
  as finite histories; the disclosure now proves the causal-state claim for the instrument (strictly positive,
  invertible $A_{\texttt a}$ contracts Hilbert's metric, so a finite set of causal beliefs closed under the symbol
  updates would collapse to $\eta^*_{\texttt a}$, which `b` moves); C1.7, 3.6, section 6's builder checks, section 9
  and the sources (Birkhoff; Seneta) follow. The ordering of the instrument's singular values is unchanged under SPEC
  v1.2's new asymmetry knob (checked at κ = 0.1, 0.3, 0.5; this page uses κ = 0). Reviewer finding: math-1-6 2.
