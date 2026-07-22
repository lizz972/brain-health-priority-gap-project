# Combines OpenAlex titles/abstracts (inverted index) into one text corpus,
# one row per work, tagged with its candidate topic.
#
# Requires: pip install pandas

import json
import pandas as pd


def reconstruct_abstract(inverted_index):
    if not inverted_index:
        return ""
    positions = {}
    for word, idxs in inverted_index.items():
        for i in idxs:
            positions[i] = word
    return " ".join(positions[i] for i in sorted(positions))


with open("data/openalex_brain_health.json") as f:
    data = json.load(f)

rows = []
for topic, works in data.items():
    for w in works:
        title = w.get("title") or ""
        abstract = reconstruct_abstract(w.get("abstract_inverted_index"))
        rows.append({
            "topic": topic,
            "text": f"{title} {abstract}".strip(),
        })

df = pd.DataFrame(rows)
df.to_csv("data/brain_health_text_corpus.csv", index=False)

print(df.head())
print("\nDocuments extracted:", len(df))
print("Saved data/brain_health_text_corpus.csv")
