# Combines Google Trends growth and OpenAlex publication growth into an
# emergence score per topic.
#
# Growth figures can be negative (declining interest/output). Both growth
# terms are clipped at zero before multiplying: a topic that is declining
# in one ecosystem should not register positive emergence just because it
# is also declining in the other (a literal signed multiplication would
# turn "both falling" into a spuriously positive product). This mirrors
# POC 1's emergence-formula rationale of requiring convergent, genuinely
# positive evidence across both ecosystems rather than letting one
# ecosystem's raw number dominate or distort the score.
#
# Requires: pip install pandas

import pandas as pd

signals = pd.read_csv("data/digital_topic_signals.csv")

signals["openalex_growth_pct"] = signals.apply(
    lambda r: ((r["recent_3yr_works"] - r["prior_3yr_works"]) / r["prior_3yr_works"] * 100)
    if r["prior_3yr_works"] > 0 else None,
    axis=1,
)

signals["trends_growth_clipped"] = signals["trends_growth_pct_topic"].clip(lower=0)
signals["openalex_growth_clipped"] = signals["openalex_growth_pct"].clip(lower=0)

signals["emergence_score"] = (
    signals["trends_growth_clipped"].fillna(0) *
    signals["openalex_growth_clipped"].fillna(0)
)

signals = signals.sort_values("emergence_score", ascending=False)

signals.to_csv("outputs/topic_radar.csv", index=False)

print(signals[[
    "topic", "trends_growth_pct_topic", "openalex_growth_pct", "emergence_score"
]])
print("\nSaved outputs/topic_radar.csv")
