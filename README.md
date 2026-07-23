# Brain Health as an Economic Input

A companion proof-of-concept to the Hidden Skills Radar (POC 1), applying
the same recognition-gap method to a different policy domain: whether
public and unconventional digital datasets amplify the case that women's
brain health is economically material, ahead of and independent of a
formal medical-recognition check.

This is a sample proof-of-concept analysis that simulates how a policy
research unit might scope and pre-register a data-driven anticipatory
intelligence exercise. It is an independent prototype exercise and not an
output of, or endorsed by, any institution.

## Policy question

Does discourse from public and unconventional datasets amplify academic
evidence of female brain health being economically material?

OECD's own New Approaches for Economic Challenges (NAEC) unit has already
made the case that brain health is economically material through its Brain
Capital programme, including work on sex and gender differences in
neurological outcomes. What is not yet tested is whether public search
interest and unconventional publishing-activity signals amplify that case:
whether they give policymakers an earlier, cheaper, independently
observable signal than the institutional argument alone. The economic
argument itself — labour-market costs tied to menopausal symptoms, adult
ADHD and long COVID cognitive effects — is not new; this project tests
whether open digital signals track it.

## Method

Two evidence layers feed a single emergence score, benchmarked (in a later
stage, not yet run) against MeSH as the institutional recognition layer:

| Layer | Source | Role |
|---|---|---|
| Public search interest | Google Trends (pytrends) | Informal, real-time public attention |
| Academic publishing | OpenAlex Works API | Growth in scientific output |
| Institutional recognition layer (not yet run) | MeSH (US National Library of Medicine) | Whether a topic already has a matching, formally recognised biomedical term |

For each of eight candidate topics, an emergence score is computed by
multiplying clipped Google Trends growth (recent 3-month mean vs. prior
12-month mean) by clipped OpenAlex publication growth (trailing 3-year
works vs. prior 3-year works from a six-year series), with both growth
terms floored at zero before multiplying so that two co-declining signals
cannot produce a false-positive score. This mirrors the Hidden Skills
Radar's approach of treating emergence as convergence across two
independent ecosystems rather than strength on either signal alone.

The eight candidate topics were chosen to span areas of women's brain
health where lived-experience language often precedes formal clinical
terminology: brain fog, ADHD in women, perimenopause and memory, executive
function support, long COVID cognitive effects, adult-diagnosed
neurodiversity, sleep and cognition, and postpartum cognitive changes.

See `methodology.md` for the full pre-registered methodology, including
the scoping rationale, effort/cost read, formulas, and the MeSH-alignment
stage that has been scoped but not yet run.

## Repository structure

```
data/                   Raw and derived data (Google Trends, OpenAlex, MeSH terms, taxonomy)
scripts/                Pipeline scripts, run in filename/stage order
scripts/comparison/     Optional multi-system recognition comparison layer (not part of the core pipeline)
outputs/                Generated CSVs at each pipeline stage
figures/                Generated chart images used in the briefing note
briefing/               Internal note / research proposal (.html, .pdf) and long-form methodology (.docx, .pdf)
appendix/               Supplementary evidence tables
```

## Running the pipeline

Stages 1–3 (Google Trends and OpenAlex collection, emergence scoring) have
been run; Stage 4 (MeSH alignment) is scoped in `methodology.md` but has
not yet been executed.

```
python scripts/00_collect_google_trends.py
python scripts/download_openalex.py
python scripts/extract_openalex_evidence.py
python scripts/build_text_corpus.py
python scripts/build_signal_dataset.py
python scripts/extract_terms.py                  # diagnostic: term-frequency scan
python scripts/build_topic_ecosystem_map.py
python scripts/calculate_topic_signals.py
python scripts/build_internal_note.py
```

`scripts/download_mesh_terms.py` collects the MeSH descriptor list for the
not-yet-run recognition-comparison stage. `scripts/report_style.py` and
`scripts/preview_identity.py` are shared styling/preview utilities, not
pipeline stages.

The final report is built separately, in either or both formats:

```
python scripts/build_internal_note.py
node scripts/build_methodology_docx.js
```

## Limitations

The two collected signals (Google Trends, OpenAlex) were captured on a
single day (22 July 2026); every figure is a point-in-time snapshot, not a
trend line. The medical-recognition check against MeSH has not yet been
run, so current results describe public attention and academic publishing
activity only, not a measured gap against formal biomedical recognition.
See the briefing note's "What's still missing" section for the full
discussion.

## References

**Academic**

- Eyre, H. A. et al. (2021). Building brain capital. *Neuron*, 109(9).
- O'Neill, T., Jones, K., & Reid, S. (2023). Impact of menopausal symptoms on work and careers. *Occupational Medicine*, 73(6).
- Joseph, S. et al. (2019). Health-related quality of life and work productivity of adults with ADHD. *Journal of Attention Disorders*, 23(12).
- Ayoubkhani, D. et al. (2024). Employment outcomes of people with Long Covid symptoms. *European Journal of Public Health*, 34(3).

**Institutional and policy**

- OECD NAEC Unit. Neuroscience-inspired Policy Initiative, Brain Capital programme.

**Data sources**

- Google Trends (pytrends).
- OpenAlex Works API.
- MeSH RDF API (National Library of Medicine) — scoped, not yet queried in this pass.

## Author

Eli Ifaturoti — eli.ifaturoti@oecd.org
