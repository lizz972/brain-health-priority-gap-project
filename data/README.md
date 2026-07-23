# Data Provenance

## Datasets

| File | Source | Purpose |
|---|---|---|
| google_trends_brain_health.csv | Google Trends (via pytrends) | Public search-interest signal for each candidate topic over time |
| openalex_brain_health.json | OpenAlex Works API | Raw scientific publication records for each candidate topic |
| mesh_terms_raw.json | NLM MeSH RDF API | Raw MeSH descriptor records used as the institutional recognition layer |
| mesh_terms_clean.csv | Derived from mesh_terms_raw.json | Cleaned MeSH descriptor list used for text-similarity matching |
| brain_health_text_corpus.csv | Derived from the above | Combined text corpus (Google Trends related queries + OpenAlex titles/abstracts) |
| digital_topic_signals.csv | Derived from the above | Unified per-item signal table used to score emergence |

## Why these sources

- **Google Trends** captures what the public is actively searching for — an early, low-cost signal of emerging concern.
- **OpenAlex** captures what researchers are actively producing — publication counts, growth rate and co-occurring concepts.
- **MeSH** (Medical Subject Headings, US National Library of Medicine) is a structured, publicly governed biomedical vocabulary with a free, no-authentication REST API: not a dictionary look-up, but a comparison instrument for measuring how closely an emerging topic already maps onto formally recognised terminology.

## Candidate topics

The eight candidate topics analysed (`data/taxonomy/candidate_topics.csv`) were chosen to span several distinct areas of women's brain health where lived-experience language often precedes formal clinical or institutional terminology: brain fog, ADHD in women, perimenopause and memory, executive function support, long COVID cognitive effects, adult-diagnosed neurodiversity, sleep and cognition, and postpartum cognitive changes.
