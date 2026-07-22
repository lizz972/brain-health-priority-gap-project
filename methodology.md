# The Brain Health Priority Gap Project — Methodology

*Women's brain health as an input to the economy: a companion
proof-of-concept to the Hidden Skills Radar (POC 1), applying the same
recognition-gap method to a different policy domain.*

This is the canonical methodology document for POC 2. It mirrors POC 1's
three-layer architecture and pipeline structure, so that both projects
demonstrate the same underlying method — anticipatory policy intelligence
from open digital signals — applied to two independent policy domains.

This document is a pre-registration: it fixes the method, the data
sources, the two growth-window definitions, and the expected-result
reasoning (Section 6) before any data was collected, specifically so that
none of those choices could be adjusted after seeing the results to produce
a more favourable-looking finding. At the time this document was written,
no Google Trends, OpenAlex or MeSH data had yet been pulled; every script
below is described by what it is designed to do, not by output it has
already produced. A reader coming to this document with no other context
should be able to verify that claim directly: Sections 4 and 5 specify
every script, every data source and every formula in enough detail to
check, after the fact, that nothing was changed once real numbers arrived.

## 0. Scoping rationale and use case

This proof-of-concept was scoped as a project decision before it was
executed as an analysis: the candidate topic was chosen against explicit
selection criteria, sized for a low-cost first pass with a defined stop
condition, and tied to a specific decision a policy reader would actually
need to make. This section states that scoping explicitly, separately from
the method itself (Sections 1–7), so a reviewer evaluating whether this was
a well-chosen project can do so without first reading the full pipeline.

**Why this candidate.** Three criteria drove selection over other possible
topics: an existing institutional anchor to test against (OECD NAEC's
Brain Capital programme already treats brain health as economically
material, so this is not a case of manufacturing policy relevance from
nothing); a plausible recognition lag (the candidate conditions —
perimenopausal cognitive symptoms, adult-diagnosed ADHD, long-COVID
cognitive effects, postpartum cognitive change — are the kind of
combination-of-partially-recognised-elements case where POC 1 also found
its clearest signal, not isolated novel terms); and free, no-registration
data access for a first pass (Google Trends and OpenAlex), so the decision
to proceed past Stage 3 could be made on a week's effort rather than a
procurement cycle. A topic failing any of the three would not have cleared
this bar: no institutional anchor makes the "why does this matter" case
harder to write; no plausible lag makes a null result uninformative; paid
or gated data makes the first pass itself a commitment rather than a cheap
test.

**Effort and cost read.** Stages 1–3 (Google Trends and OpenAlex
collection, emergence scoring) require no paid API access and no
credentialing, and were completed end-to-end in the time it takes to run
eight topics through two free APIs — on the order of a day of analyst
time, not a week, once the scripts were written. Stage 4 (MeSH alignment)
adds a third free API and one additional alignment script; it was scoped
but deliberately not run in this pass. The only cost driver that would
change this picture is Section 7's future-work items — WHO/ICD-11
(registration required) and Reddit (a registered API app) — which is why
they are named explicitly as contingent future stages rather than folded
into the core pipeline's cost estimate.

**Decision gate.** Section 8 states the actual ask: approval to run
Stages 1–3 only, with a named stop condition (proceed to MeSH matching and
a full briefing note only if the emergence layer shows a meaningful
signal; otherwise report the negative result as a defensible finding on
its own). That gate is what makes this a scoping exercise rather than a
second finished report — the commitment size is explicitly matched to how
much has been validated so far.

**Use case.** This document is written for a reader deciding whether to
fund the next stage of a candidate analytics project, not for a reader
evaluating a finished result. The decision it supports is narrow and
concrete: whether an OECD-adjacent policy team should spend a few
additional days aligning these eight topics against MeSH and publishing a
short briefing note, or stop here on the strength of a negative result.
Sections 1–3 make the case for why this topic cleared the bar for a first
look; Sections 4–5 specify exactly what was built and measured so the
claim above is checkable; Section 6 states what would make the finding
uninteresting rather than burying that risk; Section 8 states the ask.

## 1. Policy question and context

Since 2021, the OECD's New Approaches for Economic Challenges (NAEC) unit
has run an active "Brain Capital" programme through its
Neuroscience-inspired Policy Initiative (NIPI) — treating brain health and
brain skills as a core economic asset — including seminars specifically on
sex and gender differences in neurological outcomes as part of OECD's own
gender-mainstreaming work. This proof-of-concept does not, therefore,
propose a new policy issue; OECD has already established that women's
brain health is economically material and worth institutional attention.

The open question this proof-of-concept investigates is narrower, and
directly measurable: has public and research discourse caught up to that
institutional reframing, or does it still treat women's brain health the
way a recent industry newsletter described it — puberty, pregnancy,
motherhood, perimenopause and ageing discussed as separate problems, rather
than as parts of one neurological lifespan?

That framing question motivates the analysis but is not, on its own, what
this pipeline measures. What the pipeline directly tests is the narrower
and immediately computable version of it: for each of eight candidate
topics spanning the female lifespan, is there a coverage gap between
emerging public/research signal and formal biomedical recognition
(MeSH) — the same structure POC 1 applied to ESCO and AI skills? Whether
discourse is becoming more integrated across these topics — the sharper
lifespan-silo question above — is related but distinct, and this pipeline
does not yet measure it directly. It is flagged as the natural next stage
in Section 7, once the per-topic layer is validated.

The economic framing here ("brain capital," labour-force participation) is
the "why it matters" case that connects this analysis to existing OECD
priorities, mirroring how POC 1 connected AI skills detection to
labour-market policy. It sits alongside, not in place of, the intrinsic
case for closing gender gaps in brain-health recognition — the economic
argument is a complement to that case, not a replacement for it.

Conditions such as perimenopausal cognitive symptoms, adult-diagnosed
ADHD, long-COVID cognitive effects and postpartum cognitive change
plausibly affect female labour-force participation and productivity, yet
are inconsistently represented in formal biomedical classification systems
— creating a recognition question directly analogous to the
skills-recognition question in POC 1.

## 2. Three-layer architecture and why each source was chosen

| Layer | Source | Role | Why this source (vs. alternatives considered) |
|---|---|---|---|
| Public information-seeking ecosystem | Google Trends (via `pytrends`) | What the public is beginning to search for | No API key required; free; widely cited in public-health surveillance research. Considered Reddit instead (richer lived-experience language), but Reddit requires a registered API app; Google Trends can be collected immediately and still captures rising public attention, which is the same function YouTube played in POC 1. |
| Research production ecosystem | OpenAlex Works API | What researchers are actively publishing — volume, growth rate, co-occurring concepts | Free, no key required, comprehensive open scholarly index; plays the same role GitHub played in POC 1 (a production/output signal, not just discussion). |
| Institutional recognition layer | MeSH (Medical Subject Headings, US National Library of Medicine) | Whether an emerging topic already maps onto a formally recognised biomedical concept | Free, no-authentication REST API returning structured descriptor records — the closest available analog to how ESCO was used in POC 1 (a queryable, publicly governed concept taxonomy, not a dictionary look-up). WHO/ICD-11 was considered and is more immediately recognisable to policymakers, but its API requires registering a client id/secret before any data can be pulled; MeSH lets the pipeline run today. WHO/ICD-11 is kept as a named next-development-stage comparison layer (see Section 7), exactly how POC 1 kept O*NET/OpenAlex as future work rather than pretending it was already implemented. |

The three layers feed a single indicator, the **Brain Health Priority Gap
Index** — the direct analog of POC 1's Capability Recognition Gap Index.

## 3. Candidate topics, not just single search terms

Following the same logic as POC 1's "capability configurations" concept,
several candidates are not single symptoms but combinations of
already-partially-recognised elements (e.g. "ADHD in women" combines a
recognised diagnostic category with an under-studied population; "long
COVID cognitive effects" combines a novel condition with an established
cognitive-science vocabulary). Eight candidate topics were selected to
span distinct life stages — the same life stages the newsletter trigger
for this POC described as commonly discussed in isolation from one
another — where lived-experience language plausibly precedes formal
clinical terminology (full list and keyword patterns in
`data/taxonomy/candidate_topics.csv`):

1. Brain fog
2. ADHD in women
3. Perimenopause and memory
4. Executive function support
5. Long COVID cognitive effects
6. Neurodiversity (adult-diagnosed)
7. Sleep and cognition
8. Postpartum cognitive changes

## 4. Analytical pipeline — file by file

The pipeline mirrors POC 1's five conceptual stages and verified script
order. **Scripts and their inputs/outputs are described below as they will
work once run — none have been executed yet.**

### Stage 1 — Collect public digital traces

| Script | What it does | Source | Why |
|---|---|---|---|
| `00_collect_google_trends.py` | Pulls interest-over-time via `pytrends` and derives a growth metric: % change between mean weekly interest over the most recent 3 months and mean weekly interest over the preceding 12 months | Google Trends via `pytrends` | Public attention signal, no key needed; a defined trailing-window comparison, not just a raw interest score |
| `download_openalex.py` | Pulls OpenAlex works per candidate topic in two passes: (a) works-per-year counts for the last 6 years, to support a growth calculation, and (b) the 50 most recent works, for the text corpus | OpenAlex Works API | Research production signal, no key needed. Separating the corpus pull from the growth-series pull makes "publication growth" an actual computable quantity — a gap identified and fixed before data collection, not after |
| `download_mesh_terms.py` | Pulls matching MeSH descriptor records per candidate topic | NLM MeSH RDF API | Institutional recognition signal, no key needed |

### Stage 2 — Extract terminology and build the signal base

| Script | What it does | Why |
|---|---|---|
| `build_text_corpus.py` | Combines OpenAlex titles/abstracts into one text corpus | Mirrors `build_text_corpus.py` in POC 1; feeds diagnostic term extraction |
| `extract_terms.py` | Diagnostic term-frequency scan over the corpus (not read downstream) | Sanity check on vocabulary before scoring |
| `build_signal_dataset.py` | Builds a unified per-item signal table from Trends + OpenAlex data | Direct analog of POC 1's `build_signal_dataset.py` |

### Stage 3 — Score emergence

| Script | What it does | Why |
|---|---|---|
| `calculate_topic_signals.py` | Combines Google Trends growth (recent 3-month mean vs. prior 12-month mean) and OpenAlex publication growth (trailing 3-year works count vs. prior 3-year works count) into an emergence score per topic | Direct analog of `calculate_skill_signals.py`; same mentions x ecosystems logic, with both growth windows explicitly defined ahead of data collection |
| `extract_openalex_evidence.py` | Extracts per-work fields (venue, citation count, concepts, date) | Analog of `extract_github_evidence.py` |
| `build_topic_ecosystem_map.py` | Aggregates OpenAlex evidence per candidate topic | Analog of `build_skill_ecosystem_map.py` |

### Stage 4 — Compare against MeSH and compute the recognition gap

| Script | What it does | Why |
|---|---|---|
| `process_mesh.py` | Cleans raw MeSH JSON into a flat descriptor table | Analog of `process_esco.py` |
| `extract_topic_mentions.py` | Diagnostic MeSH-term mention count (not read downstream) | Sanity check, mirrors `extract_skill_mentions.py` |
| `mesh_alignment.py` | Matches each candidate to the closest MeSH descriptor by text similarity; **the zero-similarity tie-break fix from POC 1 is built in from the start** (a zero score is reported as no match, not an arbitrary nearest label) | Direct analog of `esco_alignment.py` — this is the step that produced a real, hard-to-spot bug in POC 1, so it is being written correctly the first time here |
| `create_final_evidence_table.py` | Merges emergence + MeSH + OpenAlex evidence into one table | Analog of `create_final_evidence_table.py` |
| `build_mesh_recognition_layer.py` | Classifies each candidate's MeSH recognition status (initial labels) | Analog of `build_esco_recognition_layer.py` |
| `update_mesh_labels.py` | Relabels recognition categories to final naming | Analog of `update_esco_labels.py` |
| `update_mesh_interpretations.py` | Attaches final interpretation text per category | Analog of `update_esco_interpretations.py` |

### Stage 5 — Combine into the index and publish

| Script | What it does | Why |
|---|---|---|
| `build_priority_index.py` | Computes the Brain Health Priority Gap Index | Analog of `build_hidden_skill_index.py` |
| `build_final_topic_radar.py` | Assembles the full combined radar table | Analog of `build_final_skill_radar.py` |
| `create_policy_radar.py` | Policy-facing subset of the MeSH recognition table | Analog of `create_policy_radar.py` |
| `create_policy_table.py` | Policy-facing subset of the topic radar | Analog of `create_policy_table.py` |
| `create_policy_summary.py` | Summary statistics for a policy audience | Analog of `create_policy_summary.py` |
| `create_priority_matrix.py` | Optional standalone chart, not used in the briefing note | Analog of `create_hidden_skill_matrix.py` |
| `generate_report_figures.py` | Generates the 5 figures for the briefing note | Analog of POC 1's figure generator |
| `build_report_docx.js` / `build_report_html.py` | Build the Word and HTML/PDF versions of the final briefing note | Same toolchain as POC 1 |

### Kept as future work only (not run, not claimed as implemented)

| Script | What it would do | Why it's not core |
|---|---|---|
| `comparison/build_who_comparison.py` | Optional WHO/ICD-11 comparison layer, requiring a registered API client | Exactly how POC 1 kept O*NET/OpenAlex as an optional, clearly-labelled future-work comparison rather than presenting it as validated core methodology |

## 5. Indicators (planned)

| Indicator | Definition |
|---|---|
| Google Trends growth | % change, mean weekly interest (recent 3 months) vs. mean weekly interest (prior 12 months) |
| OpenAlex publication growth | % change, works count (trailing 3 years) vs. works count (prior 3 years), from a 6-year works-per-year series |
| Emergence score | Google Trends growth x OpenAlex publication growth |
| MeSH alignment | Text similarity to closest MeSH descriptor (0-1) |
| Recognition gap | 1 minus MeSH alignment |
| Brain Health Priority Gap Index | Emergence score x (1 + recognition gap) |

Both growth windows are defined here, before any data collection, so that
neither can be adjusted after the fact to produce a more favourable
result.

In plain terms, before any data has been seen: a **high** Priority Gap
Index would mean a topic is growing fast in public search interest and
research output at the same time, while still mapping poorly onto an
existing MeSH descriptor — the signature of a real, currently
under-recognised gap. A **low** score would mean either the topic isn't
actually gaining attention (low emergence, whatever the MeSH result), or
it is gaining attention but already has a close formal descriptor
(low recognition gap) — i.e., a symptom that discourse has already caught
up with the classification system on. Both outcomes are informative;
neither is presupposed by the formula.

## 6. Anticipated limitations (to validate once data is collected)

- **Construct validity** — search growth and publication growth may
  reflect attention rather than genuine emerging need, exactly as in
  POC 1.
- **Snapshot bias** — a single collection date, not a trend line, unless
  repeated.
- **Platform dependence** — Google Trends and OpenAlex both skew toward
  English-language, digitally engaged, research-literate populations; may
  under-represent exactly the populations most affected by
  under-recognised brain health conditions.
- **MeSH coverage, reframed as an expected result rather than a threat to
  the finding** — MeSH is a broad, mature vocabulary, so most individual
  candidate topics likely already have a reasonably close descriptor,
  unlike POC 1's finding of near-total ESCO non-alignment for AI
  capabilities. That is the anticipated outcome here, not a null result:
  the interesting gap in this domain is not expected at the level of
  individual, already-medicalised symptoms, but at the level of lifespan
  integration — whether any single institutional or public framing
  connects these topics as one continuous trajectory, the way NAEC's own
  Brain Capital initiative already argues for (Section 1). This pipeline,
  as scoped, measures the former (per-topic recognition); it does not yet
  measure the latter (cross-topic integration) — see Section 7.

## 7. Next development stages

1. Longitudinal monitoring of the Priority Gap Index over repeated
   collection rounds.
2. WHO/ICD-11 as an additional institutional recognition layer, once API
   credentials are registered.
3. Reddit as a richer public-experience layer alongside or instead of
   Google Trends.
4. Validation against later MeSH revisions.
5. A lifespan-integration indicator: testing whether discourse and
   publication co-occurrence across the eight candidate topics increases
   over time — i.e. whether topics are discussed together, under a shared
   "brain capital"/lifespan frame — rather than only measuring each
   topic's individual recognition gap in isolation. This would directly
   test the fragmentation question raised in Section 1, which the current
   per-topic pipeline motivates but does not yet measure.

## 8. Proposed next step and ask

**What this document is asking for:** approval to run a first, low-cost
data-collection pass — Google Trends and OpenAlex layers only (Stages 1–3,
no MeSH yet) — across the eight candidate topics.

**Timeline:** both APIs require no authentication; a first pass across
eight topics is a matter of days, not weeks. Collection and emergence
scoring could be complete within one working week.

**Output at that stage:** not a full formatted briefing note. A short
internal note (1–2 pages) reporting the emergence score per topic, without
yet claiming a recognition gap — the MeSH layer (Stage 4) would follow
only if the emergence results justify the additional step.

**Decision point after that:** if the emergence layer surfaces a
meaningful signal, proceed to MeSH matching and the full Priority Gap
Index (Stages 4–5), and publish as a short briefing note comparable in
scope to POC 1. If not, the negative result is itself useful — it would
suggest women's brain health topics are not currently under-tracked in
public/research discourse relative to formal recognition, which is a
defensible, reportable finding on its own rather than a failed pilot.

**What this is not asking for, yet:** WHO/ICD-11 integration, longitudinal
monitoring, or the lifespan-integration indicator (Section 7, items 1, 2
and 5). Those remain future-stage work, contingent on this first pass
justifying further investment.
