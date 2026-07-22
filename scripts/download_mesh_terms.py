# Optional. Collects raw MeSH descriptor records via the NLM MeSH RDF API
# (id.nlm.nih.gov/mesh). No authentication required.
#
# Requires: pip install requests pandas

import json
import time
import requests
import pandas as pd

CANDIDATES = pd.read_csv("data/taxonomy/candidate_topics.csv")

all_results = {}

for _, row in CANDIDATES.iterrows():
    topic = row["topic"]
    query = row["keywords"].split("|")[0]

    resp = requests.get(
        "https://id.nlm.nih.gov/mesh/lookup/descriptor",
        params={
            "label": query,
            "match": "contains",
            "limit": 20,
        },
        timeout=30,
    )
    resp.raise_for_status()

    all_results[topic] = resp.json()
    time.sleep(1)

with open("data/mesh_terms_raw.json", "w") as f:
    json.dump(all_results, f)

counts = {k: len(v) for k, v in all_results.items()}
print(counts)
print("\nSaved data/mesh_terms_raw.json")
