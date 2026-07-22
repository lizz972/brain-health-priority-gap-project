# Aggregates OpenAlex evidence per candidate topic (work count, total
# citations), the production-ecosystem analog of
# build_skill_ecosystem_map.py in POC 1.
#
# Requires: pip install pandas

import pandas as pd

df = pd.read_csv("outputs/openalex_topic_evidence.csv")

agg = df.groupby("topic").agg(
    openalex_works=("title", "count"),
    openalex_total_citations=("cited_by_count", "sum"),
).reset_index()

agg.to_csv("outputs/openalex_topic_ecosystem_map.csv", index=False)

print(agg.sort_values("openalex_total_citations", ascending=False))
print("\nSaved outputs/openalex_topic_ecosystem_map.csv")
