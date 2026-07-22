# Optional. Collects raw OpenAlex data for each candidate topic in two
# passes:
#   (a) works-per-year counts for the last 6 years (via group_by), to
#       support a publication-growth calculation (trailing 3 years vs.
#       prior 3 years);
#   (b) the 50 most recent works, for the text corpus.
# OpenAlex requires no API key; a contact email in the User-Agent is
# recommended (polite pool) but not required.
#
# Requires: pip install requests pandas

import json
import time
import datetime
import requests
import pandas as pd

CANDIDATES = pd.read_csv("data/taxonomy/candidate_topics.csv")

HEADERS = {
    "User-Agent": "womens-brain-health-radar/1.0 (mailto:bonjour@atelierterridis.com)"
}

CURRENT_YEAR = datetime.date.today().year
YEARS = list(range(CURRENT_YEAR - 5, CURRENT_YEAR + 1))  # last 6 years inclusive

corpus_results = {}
yearly_counts = {}

def build_or_query(keywords):
    # OpenAlex's `search` parameter supports boolean OR with quoted phrases;
    # querying only the first keyword variant (as an earlier draft of this
    # script did) badly over-broadens topics like "Executive function
    # support" (whose first keyword, "executive function", is a huge
    # generic cognitive-science term). Querying all curated variants keeps
    # the search anchored to the specific phrasing candidate_topics.csv was
    # built to capture.
    return " OR ".join(f'"{kw}"' for kw in keywords)


for _, row in CANDIDATES.iterrows():
    topic = row["topic"]
    keywords = row["keywords"].split("|")
    query = build_or_query(keywords)

    # (a) works-per-year counts, last 6 years
    resp = requests.get(
        "https://api.openalex.org/works",
        params={
            "search": query,
            "group_by": "publication_year",
            "filter": f"publication_year:{YEARS[0]}-{YEARS[-1]}",
        },
        headers=HEADERS,
        timeout=30,
    )
    resp.raise_for_status()
    groups = resp.json().get("group_by", [])
    counts_by_year = {int(g["key"]): g["count"] for g in groups if g.get("key") is not None}
    yearly_counts[topic] = {year: counts_by_year.get(year, 0) for year in YEARS}
    time.sleep(1)

    # (b) 50 most recent works, for the corpus
    resp = requests.get(
        "https://api.openalex.org/works",
        params={
            "search": query,
            "per_page": 50,
            "sort": "publication_date:desc",
        },
        headers=HEADERS,
        timeout=30,
    )
    resp.raise_for_status()
    corpus_results[topic] = resp.json().get("results", [])
    time.sleep(1)

with open("data/openalex_brain_health.json", "w") as f:
    json.dump(corpus_results, f)

yearly_df = pd.DataFrame(yearly_counts).T
yearly_df.index.name = "topic"
yearly_df.to_csv("data/openalex_works_per_year.csv")

print(yearly_df)
counts = {k: len(v) for k, v in corpus_results.items()}
print(counts)
print("\nSaved data/openalex_brain_health.json and data/openalex_works_per_year.csv")
