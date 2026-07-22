# Extracts per-work fields (venue, citation count, concepts, date) from the
# raw OpenAlex JSON, for the ecosystem map and for supplementary review.
#
# Requires: pip install pandas

import json
import pandas as pd

with open("data/openalex_brain_health.json") as f:
    data = json.load(f)

rows = []
for topic, works in data.items():
    for w in works:
        rows.append({
            "topic": topic,
            "title": w.get("title"),
            "venue": (w.get("primary_location") or {}).get("source", {}).get("display_name")
                if (w.get("primary_location") or {}).get("source") else None,
            "cited_by_count": w.get("cited_by_count", 0),
            "publication_date": w.get("publication_date"),
            "concepts": ";".join(c.get("display_name", "") for c in (w.get("concepts") or [])[:5]),
        })

df = pd.DataFrame(rows)
df.to_csv("outputs/openalex_topic_evidence.csv", index=False)

print(df.head())
print("\nSaved outputs/openalex_topic_evidence.csv")
