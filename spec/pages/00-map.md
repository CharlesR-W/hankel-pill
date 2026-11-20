# Page spec 00: Map

<!-- Follows PAGE_TEMPLATE.md. Section numbers below are the template's. The map is the skimmable entry point: it
summarizes, it does not argue; every substantive claim on it is a pointer to the page that supports it. -->

## 0. Header

| field | value |
|---|---|
| page | 0 |
| id (hash, file stem) | `map` |
| tab label | Map |
| kicker | Overview |
| title | One spectral framework, ten lenses: a map of spectral methods for interpretability |
| lede (one-sentence claim, ≤ 45 words) | Ten fields share one spectral framework: nine pages take the SVD of a map from what has happened to what happens next, with a resolution knob and an error budget, and the Hebbian page shows a learning rule that computes spectral decompositions itself. |
| depends on | none (entry page) |
| edges (SPEC 2.2) | all, E1-E23 (the map renders the full connection list; it is not itself an endpoint of any edge) |
| faces of the running example | all (A, A′, B, C), in miniature |
| main-path words | ≤ 900 (SPEC 5.2), excluding card text and the rendered edge list, which are data |
| spec status | v1.3, 2026-11-17 (round-2 review fix; change log) |

## 1. Reader outcome

After this page the reader can:

1. State the thesis in one sentence: a past-to-future map, factored through an r-dimensional state by an SVD, with a
   bound on what dropping the rest costs; recognize the bowtie diagram that every decomposing page reuses; and say
   how page 8 fits (a learning rule whose fixed points are spectral objects: a mechanism, not a decomposition with a
   bound).
2. For each page, name the map being decomposed, the weights on its two sides, the knob, and the kind of bound
   (from the cards and the hero's page selector).
3. Describe the running example (a noisy particle in four wells grouped in two pairs; a three-symbol instrument; the
   linear response; the toy residual network) and say which face each page uses.
4. Say why the resolution knob has a price: truncation error falls as r grows, but a resolution is certifiable only
   where the spectrum has a gap, and the scale (lag, bandwidth) decides where the gaps are (wells at short lags, pairs
   at long ones).
5. Read the relation symbols `=`, `≈`, `~` and find any cross-page link in the connection list.
6. Choose a reading route suited to their background.

What they see: one bowtie that relabels itself page by page (prefixes and suffixes; past inputs and future outputs;
functions now and later; points at layer ℓ′ and ℓ) with the running example's own singular values in the knot; the
four-well particle, its symbol stream, its ensemble response and its flow through twelve layers; a card per page with
a miniature of that page's hero; two curves of spectral gap crossing as the lag grows; a graph of the pages joined by
solid, dashed and dotted links.

## 2. Skim path

1. Lede (header).
2. Hero figure `map-fig-hero`: "One bowtie, nine maps and a mechanism". Fig-sub: *Nine pages decompose a map from
   what has happened to what happens next through a small knot of singular values, and choosing one changes the
   labels, the weights and the bound; page 8 has no knot: it shows a learning rule whose fixed points are spectral
   decompositions of their own.*
3. Section headings (verbatim, these are the claims):
   - "Nine pages factor a past-to-future map through a small state"
   - "One noisy particle in four wells runs through every page"
   - "The lenses differ in map and weights; one supplies a mechanism"
   - "Finer resolution is trustworthy only where the spectrum has a gap"
   - "Each link is a theorem, a bounded approximation, or an analogy"
4. Key-point callouts (one per section; gists in section 3).
5. Figure titles and fig-subs for `map-fig-faces`, `map-fig-gaps`, `map-fig-graph`; the card grid's card titles and
   claim lines.
6. Ledger (the generic ledger, 8).
7. Connections (the full edge list).

Skim test: a reader of only the above should come away with: one spectral framework (SVD of a past-to-future map
through an r-dimensional state, with a bound) under many names, plus one page (8) showing a learning rule that
produces spectral decompositions rather than decomposing a map; the running example and its four faces; each page's map,
weights, knob and bound; truncation error falls with r, but certification needs a gap, gaps are not monotone in r, and
the lag or bandwidth decides which resolution is well separated; the error budget's named terms (T, S, P, Z, R, I) are
assembled on page 10; links are marked as theorems (=), bounded approximations (≈) or analogies (~).

## 3. Section outline

Section ids are `map-<slug>`; figure ids are `map-fig-<slug>` (SPEC 6.5). Word counts are main-path prose only.

### 3.1 `map-thesis` "Nine pages factor a past-to-future map through a small state" (≈ 300 words, of which ≈ 150 quoted)

Placement: the hero sits between the lede and this heading.

- One paragraph (≤ 90 words) in the site's voice: interpretability often wants to know what a system keeps from its
  past in order to act on its future; any such map factors through a state; the SVD orders the state's directions by
  how much the map uses them and bounds the cost of dropping the rest (Eckart-Young). Then the two aims of the site
  (SPEC 1.1) in one sentence each.
- The thesis paragraph of SPEC 1.3, quoted verbatim as a block quote (it is the site's own text; no attribution
  needed beyond "the site's thesis").
- The programme author's compression, quoted with attribution and a link to the "Slouching Towards Interpretability"
  post (part III): "the only thing that is truly interpretable is an SVD, so we need to find the right SVD", followed
  by one sentence of the author's reason, paraphrased: the SVD is the way to say that one thing approximates another
  in an importance-sensitive way, with bounds. Mark it as the author's stance, not the site's claim.
- One sentence on the tenth page: page 8 decomposes no map; it shows that a local learning rule (Hebbian, with a
  pruning threshold, on a resistor network) settles on nonnegative eigenvectors of thresholded covariance
  submatrices, a mechanism that produces spectral decompositions of its own, with no truncation bound (its budget line
  is "—").
- How to read a page (≤ 60 words): the lede, the hero, headings written as claims, one key point per section, a ledger
  box with the same seven rows on every page, and a connections strip; derivations live in "The maths" disclosures.

Key callout: "Nine pages differ in which map they decompose and how they weigh its two sides; the interpretive question
is which map, and which weights. Page 8 shows a learning rule that arrives at spectral decompositions by itself."

Disclosure "The bowtie, read row by row" (≤ 250 words): left fan (pasts), knot (singular values; dial r; faint bars
discarded), right fan (futures), the hatched bar under the knot (the page's bound), the two norms above the fans
(weights). Why the weights matter: the same table whitened or not can order its directions differently (page 1's
instrument; page 2's PCA versus balancing).

### 3.2 `map-example` "One noisy particle in four wells runs through every page" (≈ 220 words)

Placement: `map-fig-faces` after the first bullet. This section is the running example's canonical description;
other pages link to it as `#map/map-example`.

- The particle: overdamped Langevin dynamics in a two-dimensional potential with four wells $w_1..w_4$ at
  $(\pm1, \pm0.6)$, grouped in a left and a right pair by a high central barrier, the wells in each pair separated by a
  lower one; noise D = 0.5. Time scales (builder values): pair switching ≈ 36, hops within a pair ≈ 3, relaxation in a
  well ≈ 0.12. Colours: blue for the left pair, orange for the right, dark for the lower well, light for the upper (say
  so once; colour is never the only carrier).
- The four faces, one sentence each, with the pages that use them: **A** the particle itself, observed as positions,
  as the scalar readout $y = x_1 + x_2 + $ noise, or as symbols `a`, `b`, `c` from uneven bins (pages 1, 3-9);
  **A′** the four-state chain on the wells, an idealization that forgets position inside a well (pages 1, 6);
  **B** the ensemble's linear response to a small push along the diagonal (page 2); **C** a twelve-layer toy residual
  network whose layers are steps of the particle's drift, through which 1,000 input points flow into the wells
  (pages 3, 4, 10).
- One sentence: the two wells of the left pair both read `a`, so the instrument barely tells them apart; that is
  deliberate (page 1).
- All data are synthetic and computed by the site's reference builder; every number on every page comes from it or
  from a live computation.

Key callout: "Two pairs of two wells: at a coarse resolution the particle is left or right, at a finer one it is in
one of four wells, and everything finer is motion inside a well."

Disclosure "The running example's definition" (≤ 400 words): SPEC 3.2's potential $V_\kappa$, dynamics, generator,
readout and bins, emission probabilities (builder values), the asymmetry knob κ (pages 2 and 6: it lowers the
between-pair barrier on the upper side, so the upper wells switch pairs more readily and the pair label stops being
exactly lumpable), face C's layer map and
uncommitted band; why this example and not a one-dimensional four-well or a double gyre (one sentence each, from SPEC
3.1).

### 3.3 `map-pages` "The lenses differ in map and weights; one supplies a mechanism" (≈ 150 words, plus the card grid)

Placement: the card grid (component, not a figure) after the first bullet.

- One sentence introducing the grid: each card names the page's map, its knob and its bound, with a miniature of the
  page's hero (the running example under that lens).
- Card grid: `ui.mapCard` for pages 1-10 and a smaller card for the Reference tab, in page order, two columns on
  desktop, one on phones. Card content in section 7 below (and in `data/map/cards.json`).
- Reading routes (≤ 80 words, a short list): new to all of it: 1 → 3 → 4 → 10; from control or signal processing:
  2 → 1 → 3; from spectral clustering: 4 → 5 → 10; from computational mechanics: 1 → 6 → 9; interpretability results
  first: 10, then 9 and 4. Every page is readable alone ("Arriving here first?" boxes).

Key callout: "Pages 1-3 decompose maps of a process or system; 4-5 relax partition problems on graphs; 6-7 read the
same structure as states and neurons, and 8 shows a learning rule that produces such decompositions; 9-10 apply it to
language models from outside and inside."

No disclosure.

### 3.4 `map-knob` "Finer resolution is trustworthy only where the spectrum has a gap" (≈ 200 words)

Placement: `map-fig-gaps` after the second bullet.

- The site's single main result in plain words (SPEC 1.1): coherent-set and truncation methods, applied to neural
  networks, come with error bounds whose terms have names: truncation (T), sampling (S), perturbation (P),
  sparsification (Z), rounding (R), and an interpretation term with no bound (I). Each page's ledger supplies one line;
  page 10 assembles them.
- Every term depends on the resolution: truncation error falls as r grows, but subspace certificates divide by the
  spectral gap at the chosen r; eigenvalue and operator-error bounds do not, and the gap decides whether those errors
  are small enough to distinguish a block (rounding to sets also needs a small partition residual and a positive
  threshold margin); and gaps are **not monotone** in r. In the running example (builder values) at lag
  0.25 the gap after four is far larger than the gap after two; at lag 4 the reverse. Short lags certify the wells;
  long lags only the pairs. The lag (or a kernel's bandwidth) is the knob that decides which resolutions can be trusted.
- The data needed grow as the gap shrinks (roughly as one over its square for a single operator; page 10 states the
  hypotheses).

Key callout: "Truncation error falls as r grows; certification needs a gap at r. The scale knob decides where the gaps
are."

No disclosure (page 10 holds the budget).

### 3.5 `map-links` "Each link is a theorem, a bounded approximation, or an analogy" (≈ 120 words)

Placement: `map-fig-graph` after the first bullet; the full edge list follows in the Connections section.

- The three symbols: `=` identity or theorem-level equivalence under stated hypotheses; `≈` a relaxation or
  approximation controlled by a cited bound; `~` a motivating analogy with no theorem behind it. Every page's
  connections strip uses the same symbols, and a page may add detail but never upgrade a symbol.
- Analogies are marked as such: the information bottleneck as an energy (E13), comparisons between learning rules
  (E15), depth as time in real networks (E19), and the links between neural-network coherent sets and computational
  states, activation plateaus, neurons, and Hebbian learning (E17, E20-E23) are currently `~`, wrapped in the SPEC
  section 8 hook; each `~` edge states its exact special cases (the Gaussian bottleneck's directions, each rule's
  fixed points, the toy network's flow) as such.

Key callout: "Solid links are theorems, dashed links come with bounds, dotted links are analogies that motivate but do
not prove."

No disclosure.

### 3.6 `map-connections` Connections

The full connection list, rendered from `data/map/edges.json` (a verbatim transcription of SPEC 2.2): one entry per
edge with id, the two page names (linked), the relation symbol (large), the statement, and the bridge and citation.
Entry ids `map-edge-e1` … `map-edge-e23`; every page's connections strip links its edge chips to
`#map/map-edge-e<n>` (`ui.connections` generates this link; URL scheme of SPEC 6.5). On arrival by such a link the
entry is scrolled into view and briefly outlined in accent. Statements of `~` edges are wrapped in
`<span class="status" data-status="schematic">…</span>` (SPEC 8). A filter row (chips: all | `=` | `≈` | `~` | by page)
filters the list without changing URL state beyond `map_edgefilter`.

### 3.7 `map-ledger` Ledger

The generic ledger (section 8), rendered with `ui.ledger`, titled "How to read every page's ledger". It doubles as the
legend for the seven rows and the budget letters.

### 3.8 `map-sources` Sources

Section 11 of this spec; a pointer to the Reference tab for the full bibliography.

## 4. Claims in order

The map makes few claims of its own; each is either the site's framing or a pointer to the page that supports it.

| id | claim | support | source / where shown | hypotheses the page must state | section |
|---|---|---|---|---|---|
| C0.1 | Each page except 8 decomposes a past-to-future map through an r-dimensional state, with weights on both sides and a bound on what is dropped; page 8 shows a learning rule whose fixed points are spectral objects. | construction (site framing) | hero (page 8 chip and fig-sub); each page's ledger | "where a theorem allows"; page 8's ledger has no approximation bound | 3.1 |
| C0.2 | The SVD's truncation is optimal for a given norm with error given by the discarded singular values (Eckart-Young). | theorem | Eckart & Young 1936 (pages 1, 3) | the norm and the competitor class (rank-r matrices / operators) | 3.1 |
| C0.3 | "The only thing that is truly interpretable is an SVD, so we need to find the right SVD." | quotation (author's stance) | "Slouching Towards Interpretability", part III | attributed to the programme's author, not stated as the site's claim | 3.1 |
| C0.4 | The running example's time scales are ≈ 36 (pair switching), ≈ 3 (hops within a pair), ≈ 0.12 (relaxation in a well). | builder values | `data/example/grid.json` rates | κ = 0, D = 0.5 | 3.2 |
| C0.5 | Both left-pair wells read `a`. | construction + builder emission table | `data/example/chain.json` | bins as SPEC 3.2 | 3.2 |
| C0.6 | Error budgets have named terms T, S, P, Z, R and an unbounded I, assembled on page 10. | pointer | page 10; SPEC 4.3 | — | 3.4 |
| C0.7 | At lag 0.25 the gap after four dominates; at lag 4 the gap after two; gaps are not monotone in r. | builder values | `map-fig-gaps` from `grid.json` | κ = 0; gaps of $e^{-\nu_i\tau}$ | 3.4 |
| C0.8 | The data needed grow as the gap shrinks (≈ $\delta^{-2}$ for a single operator). | pointer (theorem on page 10, conditional) | page 10; CoherentModes A.44 (programme source) | page 10's hypotheses; a scaling, not a constant | 3.4 |
| C0.9 | Each cross-page link is `=`, `≈` or `~`, exactly as in SPEC 2.2. | construction | `map-fig-graph`; edge list; parity test against SPEC 2.2 | — | 3.5, 3.6 |
| C0.10 | The information bottleneck as an energy, comparisons between learning rules, depth as time in real networks, and links to activation plateaus, computational states, neurons-as-motivation and Hebbian clustering are analogies. | motivation (section 8 hook) | E13, E15, E19, E17, E20-E23 | wrapped in the schematic hook; exact special cases stated outside it | 3.5 |

Things not to claim on this page: every page decomposes a map or has a bound (page 8 supplies a mechanism, not a decomposition with a bound); the lenses differ only in map and weights; the
methods recover "the same features"; coherent sets are the network's computational states; finer resolution always
has a smaller gap; the error budget is one inequality; anything from SPEC appendix D in condensed card text (cards are
the most likely place for an over-compressed claim; see 13).

## 5. Figures and widgets

### 5.1 `map-fig-hero` "One bowtie, ten lenses" (live, hero; key `hr`)

- **Purpose:** every decomposing page is the same picture with different labels, weights and bound; page 8, visibly different, is the mechanism.
- **Layout:** `figure.fig.full.card`; the shared `bowtie` component (SPEC 1.4) centred, ≈ 900 × 380 px on desktop,
  full width on phones; above it a chip row: `generic`, `1 Hankel`, `2 Linear control`, …, `10 LLMs from inside`, with the page-8 chip always
  labelled `8 Hebbian · mechanism` and drawn with a dashed outline (so the exception is visible without clicking); to
  the right (below on phones) a small text box with the selected page's one-line map card text and a link "go to the
  page".
- **Data:** labels per page from SPEC 1.4 (left, right, norms, bound label), stored in `data/map/cards.json`
  (`bowtie` field per page); knot bars per page from `cards.json` `sigmas`, filled during build step 9 with exactly
  the knot bars of that page's own bowtie figure, whose spec names them (page 1 `hankel-fig-bowtie`: the chain's
  σ₁..σ₆ at depth 3; page 2 `control-fig-bowtie`: face B's σ₁..σ₈; page 3 `koopman-fig-bowtie`: $e^{-\nu_i\tau}$ at
  τ = 0.25; page 4 `cuts-fig-recipe`: lazy-walk eigenvalues of the hero's graph; page 5 `sparsity-fig-chain`: the
  dense Sinkhorn walk's eigenvalues; page 6 `compmech-fig-norms`: the instrument's canonical correlations; page 7
  `neurons-fig-bowtie`: the ON/OFF dictionary's σ₁..σ₆; page 9 `logits-fig-bowtie`: the chain block's σ₁..σ₈; page
  10 `ncs-fig-bowtie`: face C's $\bar M$ eigenvalues), and the same labels, norms and bound text. **Page 8 has no
  bowtie** (SPEC 1.4): its chip shows the fans without a knot, greyed, with the text "page 8 supplies a mechanism
  (a learning rule's fixed points), not a decomposition with a bound". If a page's `sigmas` is absent, the bars are
  drawn as a generic decreasing sequence with the label "schematic bars" under the knot. Generic view: labels "what has happened" / "what happens next", norms "weights", bound "lost ≤ tail of
  discarded σ", schematic bars.
- **Controls (primary):** page (chips); r (drag on the knot's dial, 1-8; default 2). Advanced: none.
- **Default state (= first tour):** `generic`, r = 2.
- **What changes:** the page chip swaps labels, norms, bars, bound label and the text box, with a 300 ms cross-fade
  (none under reduced motion); dragging r moves the dial, fades and hatches bars beyond r, and updates the hatched
  bar's proportion (the fraction of the page's chosen tail measure discarded, computed from `sigmas`).
- **Stat tiles:** none.
- **Tours:** `generic` (default; r = 2); `p1` (page 1, r = 4); `p2` (page 2, r = 2); `p3` (page 3, r = 4); `p10`
  (page 10, r = 4). Tours for the other pages are reachable by chip but not listed.
- **fallbackTour:** `generic`.
- **Caption:** *Plotted:* the thesis diagram: items on the left (pasts) and right (futures) joined through a knot of r
  bars (singular values, descending; bars beyond r faint); under the knot, kept versus discarded (hatched) with the
  page's bound; above the fans, the weights on each side. *Values:* bars from each page's running-example output, or
  schematic where marked. Running example, all faces. `synthetic`.
- **Static fallback:** `assets/fallback/map-fig-hero-generic.png` and one PNG per tour; GIF `assets/fallback/map-fig-
  hero.gif` (≈ 6 s cycling `generic` → `p1` → `p2` → `p3` → `p10`, 1.2 s each).
- **Accessibility:** alt text: "A bowtie diagram: many lines from past items converge on a small stack of bars and
  fan out to future items; labels change with the selected page." The chips are buttons with the page names; the text
  box states the map in words.
- **Performance:** SVG relabel only, < 5 ms.

### 5.2 `map-fig-faces` "The running example's four faces" (live; key `fx`)

- **Purpose:** one system seen four ways: a particle with a symbol readout, a four-state chain, an ensemble response,
  a flow through layers.
- **Layout:** `figure.fig.wide.card`; a segmented control A | A′ | B | C above one view area (≈ 900 × 320 px) and a
  one-line description under it naming the pages that use the face.
  - **A:** contour map of V with wells (labelled, well colours), one particle with a fading trail (live), and to the
    right a scrolling strip of the last 40 readouts $y_t$ with the bin lines and the symbols `a`/`b`/`c` in monospace.
  - **A′:** a four-node diagram of the chain at the wells' positions, arrows with widths ∝ $T_\Delta[j,k]$ (self-loops
    as labels), and small bar charts of each state's emission probabilities over `a`, `b`, `c`.
  - **B:** the hero of page 2 in miniature: the mean output z(t) after a short push (two slow exponentials), no density
    map.
  - **C:** three scatter panels of the 1,000 points at layers 0, 6 and 12, coloured by input basin (well colours),
    uncommitted band grey.
- **Data:** A: live simulation (`lib/example.js`, seed 0) and live readout; A′: `data/example/chain.json`; B:
  `data/example/response.json` (modal form, closed-form response); C: live flow (`lib/example.js`, N = 1000, seed 0).
- **Controls (primary):** face (segmented); play/pause (A only; autoplay when visible; reduced motion shows a still).
- **Default state (= first tour):** `A`, playing.
- **What changes:** face swaps the view and the description line.
- **Tours:** `A` (default), `Aprime`, `B`, `C`.
- **fallbackTour:** `A` (captured at the builder-recorded frame used for page 1's `frame-late`, or at t = 50 if that is
  unavailable; the capture mode pauses there).
- **Caption:** *Plotted:* A, contours of $V$, wells $w_1..w_4$, one simulated particle, and its readout $y_t$ binned to
  `a` ($y < 0$), `b` ($0 \le y \le 1$), `c` ($y > 1$); A′, transition probabilities $T_\Delta$ between wells and
  emission probabilities $E[k, s]$; B, mean readout after a unit push of length 1 along $(1,1)/\sqrt2$, linear response;
  C, positions $x^{(\ell)}$ of 1,000 inputs at layers 0, 6, 12 of the toy residual network, coloured by input basin.
  *Values:* $h_x = 2.5$, $h_y = 1.5$, b = 0.6, κ = 0, D = 0.5, $\sigma_y = 0.25$, Δ = 0.25, T = 0.3, seed 0. Running
  example, faces A, A′, B, C. `synthetic`.
- **Static fallback:** PNG per tour (`assets/fallback/map-fig-faces-<tour>.png`); GIF `assets/fallback/map-fig-
  faces.gif` (≈ 6 s of face A at ×4).
- **Accessibility:** alt text per face (the description line); wells labelled $w_1..w_4$ in every view.
- **Performance:** A ≤ 2 ms per frame; C flow ≈ 30 ms once, cached.

### 5.3 `map-fig-gaps` "Which resolution is well separated depends on the lag" (static, rendered by the page module)

- **Purpose:** the gap after two and the gap after four cross as the lag grows: wells are certifiable at short lags,
  only pairs at long lags.
- **Data:** `data/example/grid.json` rates $\nu_1..\nu_6$.
- **Content:** left: $\lambda_i(\tau) = e^{-\nu_i\tau}$ for i = 2..6 against τ (log axis 0.05-100), lines labelled by
  meaning (pair, well in pair, product, inside a well; labels from page 3's builder output `p03.json` `labels`, or
  "mode i" if unavailable); right: the two gaps $\lambda_2 - \lambda_3$ ("after 2: pairs") and $\lambda_4 - \lambda_5$
  ("after 4: wells") against τ, with markers and values at τ = 0.25 and τ = 4.
- **Generation:** drawn by `p_map.js` at fixed size from the data (no interaction).
- **Caption:** *Plotted:* left, eigenvalues $e^{-\nu_i\tau}$ of the running example's Koopman operator at lag τ; right,
  the gap after the second and after the fourth eigenvalue, against τ. *Values:* κ = 0, D = 0.5; rates from the
  builder's grid generator. Running example, face A. `synthetic`.
- **Fallback:** PNG `assets/fallback/map-fig-gaps-default.png` (key `gp`, single tour `default`).

### 5.4 `map-fig-graph` "How the pages connect" (static SVG, rendered by the page module)

- **Purpose:** the pages form one connected web; each link is marked by what supports it.
- **Data:** `data/map/edges.json` (SPEC 2.2 transcribed).
- **Content:** nodes for pages 1-10 placed on two arcs (upper: 1, 2, 3, 6, 9; lower: 4, 5, 7, 8, 10, in an order that
  keeps the drawing planar where possible; the writer may adjust), plus one external node "Janiak et al. (stable
  regions)" for E20; edges drawn `=` solid ink, `≈` dashed ink, `~` dotted grey, each labelled with its E-id at the
  midpoint; E10 ("4/5–8") and E18 ("4/5–10") each drawn as two edges, from 4 and from 5, sharing one label. Hover on an edge shows its statement
  (tooltip); click goes to `#map/map-edge-e<n>`. Node click goes to the page.
- **Generation:** SVG by `p_map.js` (no physics simulation; fixed coordinates in `edges.json` `layout`).
- **Caption:** *Plotted:* pages (nodes) and the links between them listed in the connection list (edges): solid,
  identity or theorem-level equivalence; dashed, approximation with a cited bound; dotted, analogy. *Values:* none.
- **Fallback:** PNG `assets/fallback/map-fig-graph-default.png` (key `cg`, single tour `default`).
- **Accessibility:** line styles carry the relation (not colour alone); the full list below is the text equivalent.

## 6. Running example on this page

- Faces: all, in miniature (5.2) and through the cards' thumbnails (each page's hero fallback).
- Precomputed (shared files only): `grid.json` (rates for 5.3 and time scales in 3.2), `chain.json` (A′),
  `response.json` (B). Live: face A particle, face C flow.
- Page data: `data/map/cards.json` and `data/map/edges.json` (written by the map writer, not the builder).
- Card thumbnails: each card's thumbnail is the page's hero fallback PNG (`assets/fallback/<id>-fig-hero-<fallbackTour>.png`;
  every page's hero is `<id>-fig-hero`, SPEC 6.5; fallback tours as named in the page specs: 1 `frame-late`, 2
  `pulse-early`, 3 `corner-late`, 4 `wells`, 5 `eps05`, 6 `instrument-late`, 7 `frame-late`, 8 `wells`, 9
  `frame-still`, 10 `dynamic`), optionally cropped by `cards.json` `crop: [x, y, w, h]` (in source
  pixels) to the panel that best shows the running example under that lens; crops are chosen during build step 9 by
  inspecting each fallback. No new computation for thumbnails.
- No strain to state; the example's strains are stated on the pages.

## 7. Connections

The map is not an endpoint of any edge; its Connections section is the full list of E1-E23 (3.6), transcribed verbatim
from SPEC 2.2 (statement and bridge columns), with the same symbols.

Card content (`data/map/cards.json`, one entry per page). Fields: `title`, `claim` (≤ 25 words), `knob`, `bound`
(≤ 20 words). **Each page spec's section 7 "map card text" is authoritative; the map writer copies it at build step 9.**
The entries below are transcribed from the page specs' section 7 as of 17 November 2026 (all ten pages); re-check
them at build step 9, since page specs may have been revised since.

| page | title | claim | knob | bound |
|---|---|---|---|---|
| 1 | Hankel | The table of pasts by futures. | rank r | σ_{r+1} for the table, Σ_{i>r} σ_i² for a balanced machine |
| 2 | Linear control | The Hankel operator from past inputs to future outputs, weighted by input and output energy. | number of balanced states r | $\sigma_{r+1} \le \|G - G_r\|_{H_\infty} \le 2\sum_{j>r}\sigma_j$ |
| 3 | Koopman | The dynamics' action on functions, whitened on both sides (past-future CCA). | r and the lag τ | σ_{r+1} per function, Σ_{i>r} σ_i² in Hilbert-Schmidt norm |
| 4 | Spectral clustering | Cut where little crosses for its size. | number of sets k and the graph's scale | μ_k/2 ≤ best k-way cut; sweep ≤ √(2μ₂) |
| 5 | Sparsity | Thin the graph, keep every cut; read sparse sets out of an eigenspace. | ε and the SEBA threshold μ | (1 ± ε) on every energy; 2√2η/c for an aligned readout (existence) |
| 6 | Comp. mechanics | Pasts merged by equal futures; macro-variables that are states of their own. | tolerance, horizon, β_IB | rank ≤ n_c; MSM error ≤ min[2, C(δ, η, k)]λ₂^k |
| 7 | Neurons | Past-future CCA on a neuron's delay windows. | neurons r, window m, lag | σ_{r+1} within the window dictionary; exact set membership for OU input |
| 8 | Hebbian | Thresholded Hebb rule on a resistor network. | threshold θ (and trace τ_s) | exact fixed-point characterization of parts; no bound on allocation or refinement |
| 9 | LLMs from outside | The extended logit table. | logit rank r = ISAN dimension | mean KL ≤ Σ_{i>r} σ_i² / (2\|H\|\|F\|) for the table; none for the machine |
| 10 | LLMs from inside | Walks on the same inputs, layer after layer. | r, bandwidth β (or k), block of layers | a ledger of named terms: finite-site e_F/(δ_r − e_F); eigenvalues end to end ≤ e_F + E_N (one analysed layer); rounding 2√2η/c (existence); truncation exact; interpretation unbounded |
| R | Reference | Notation, glossary, every ledger in one table, bibliography. | — | — |

## 8. Ledger

The map's ledger is the **generic ledger**: the thesis filled into the seven rows, so the box doubles as the legend
for every page's ledger. Title on the page: "How to read every page's ledger".

| row | content |
|---|---|
| Decomposed | A map from what has happened to what happens next (a table, an operator, a walk), and the weights put on each side; the decomposing pages differ mainly here. Page 8's row names a learning rule and its fixed points instead (a mechanism). |
| Knob | The resolution r (states, modes or sets kept), and the continuous scale that moves it: lag, bandwidth, threshold, horizon or ε. |
| Discarded at r | What the rank-r description cannot distinguish; in the running example, at r = 2 which well within a pair, at r = 4 where inside a well. |
| Bound | The guarantee on what is lost, its hypotheses, its source, and a tag: `theorem`, `theorem (scope-limited)`, `conditional`, `standard`, `none`. For a plain SVD, Eckart-Young: the error is the discarded singular values. |
| From data | What finite samples or perturbations add: estimated singular values move by at most the error's norm (Weyl), subspaces by error over gap (Davis-Kahan, Wedin). |
| Running example | The page's numbers for the running example, all from the builder or computed live. Here: the gap after 2 and after 4 at τ = 0.25 and τ = 4 (`map-fig-gaps`). |
| Budget line | The page-10 term the page supplies: **T** truncation, **S** sampling, **P** perturbation, **Z** sparsification, **R** rounding, **I** interpretation (no bound), or "—". |

## 9. Things not to claim

Every page has an approximation bound (page 8 does not); the methods find "the same features" or "the true features";
coherent sets are the network's computational states (E21: candidates; closure untested); activation plateaus are
coherent sets (E20: analogy); static clustering of activations finds the dynamics in general (E6 only); finer
resolution always has a smaller gap; the error budget is one inequality; AAK or optimal smaller machines for language
models; Hankel rank equals the number of causal states. In card text, avoid "optimal", "recovers" and "proves" unless
the page's own map-card text uses them.

## 10. Notation used

Global (SPEC appendix A): r, $\sigma_i$, $\lambda_i$, $\nu_i$, $\delta_r$, τ, Δ, x, V, D, π, y, $\sigma_y$, $s_t$,
$w_1..w_4$, L/R pairs, $x^{(\ell)}$, T S P Z R I. Page-local: none. The map uses as little notation as possible: symbols
appear in the caption of `map-fig-gaps`, in the running example's disclosure, and in card text only.

## 11. Sources

- The site's thesis: SPEC 1.3 (the site's own text).
- Programme author's stance: "Slouching Towards Interpretability" (Nov 2026), part III.c-III.d, published at
  `charlesr-w.github.io/crw-blog` (link the published post; the local copy is
  `crw-blog/_posts/2026-11-14-Gradients-and-Circuits.md`). Programme source, cite as such.
- Eckart, C. & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika* 1(3),
  211-218. [V]
- Everything else by pointer to the pages and to the Reference tab's bibliography (SPEC appendix C).

## 12. Implementation notes

- Files: `site/content/map.html`, `site/js/p_map.js`, helpers `site/js/p_map_faces.js`, `p_map_graph.js`; data
  `site/data/map/cards.json`, `site/data/map/edges.json`, `site/data/map/widgets.json`.
- `cards.json`: `[{page, id, title, claim, knob, bound, thumb: {figureId, tour, crop|null}, bowtie: {left, right,
  leftNorm, rightNorm, bound}, sigmas|null}]`. `edges.json`: `{edges: [{id, pages: [a, b], rel, statement, bridge}],
  layout: {nodes: {...}}}`.
- Shared modules used: `lib/bowtie.js` (hero), `lib/example.js` (face A simulation, face C flow, loaders), `ui.js`
  (`mapCard`, `ledger`, `connections` styles), `charts.js`, `palette.js`.
- Deep links: section anchors `#map/<section-id>`; edge entries `#map/map-edge-e<n>`. The router scrolls to the
  element after the fragment loads (SPEC 6.5, binding URL scheme).
- Widget keys and URL state: hero `hr` (`hr_page`, `hr_r`, `hr_tour`); faces `fx` (`fx_face`, `fx_tour`); gaps `gp`
  and graph `cg` (single tour `default`); edge-list filter `map_edgefilter` (not a widget).
- Tests: a node test parsing SPEC.md's section 2.2 table and checking that `edges.json` has the same ids, page pairs
  and relation symbols (statements compared after whitespace normalization); a test that every `cards.json` entry's
  thumbnail file exists after `capture.sh`; a test that every page's connections strip edge ids are a subset of
  `edges.json` and touch that page.

## 13. Page-specific definition-of-done additions

- [ ] Main-path prose ≤ 900 words (card text and the rendered edge list excluded and counted separately: cards ≤ 50
      words each including knob and bound).
- [ ] Every card's text matches its page spec's section 7 map-card text (or the page's final version).
- [ ] The edge list equals SPEC 2.2 (test above); `~` statements carry the schematic hook.
- [ ] The quotation from the programme's author is attributed and linked, and not repeated as the site's claim.
- [ ] Thumbnails legible at card size on desktop (inspect at 1440 × 900); on phones (390 × 844) cards stack and
      thumbnails are full card width.
- [ ] The gap values in 3.4 and the ledger come from `grid.json` (expected ≈ 0.78 vs ≈ 0.07 at τ = 0.25; ≈ 0.63 after two
      at τ = 4; checks only).
- [ ] `#map/map-example` and `#map/map-edge-e<n>` links from other pages land on the right element.

## Change log

- v1 (2026-11-17): first full spec. Ledger: SPEC 4.2 drafts none for page 0; this spec defines a generic ledger used
  as the legend (reported for SPEC amendment). Card text for pages 6, 7, 8 and 10 is provisional; pages 4, 5 and 9 copied from
  their specs as of 2026-11-17.
- v1.1 (2026-11-17): reconciled with SPEC v1.1. SPEC 4.2 now drafts this generic ledger, and SPEC 6.5 makes the
  `#map/<element-id>` URL scheme binding. Cards for pages 6, 7, 8 and 10 rewritten from those pages' section 7 (no
  card is provisional now). Hero knot bars taken from each page's own bowtie figure; page 8 shown without a knot (it
  has no bowtie); E10 drawn like E18; thumbnails' hero fallback tours listed (page 6's is now `instrument-late`).
- v1.2 (2026-11-17): round-1 review fixes (SPEC v1.2). The unity is stated as a shared spectral framework with page 8
  as a mechanism that produces spectral decompositions, in the title, lede, hero title and fig-sub, two headings, the
  3.1 and 3.3 callouts, the skim test, C0.1, the generic ledger's Decomposed row and the hero's page-8 chip (labelled
  "mechanism" and outlined, visible without clicking). The analogies list adds E13, E15 and E19 (now `~`). Page 10's
  card follows its new ledger wording; the running-example disclosure describes SPEC 3.2's new asymmetry knob.
  Reviewer findings: design 4; math-7-10 9; math-1-6 1 (knob description).
- v1.3 (2026-11-17): round-2 review fix (SPEC v1.3). 3.4's resolution bullet no longer says each certificate divides
  by the gap: subspace certificates do; eigenvalue and operator-error bounds are compared with the gap; rounding also
  needs a small partition residual and a positive threshold margin. Reviewer finding: round 2, item 3.
