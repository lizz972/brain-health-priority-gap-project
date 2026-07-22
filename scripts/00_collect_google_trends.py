# Optional, rate-limited. Collects Google Trends interest-over-time for each
# candidate topic keyword via the unofficial pytrends client (no API key
# required, but Google may rate-limit repeated calls), and derives a growth
# metric: % change between mean weekly interest over the most recent 3
# months and mean weekly interest over the preceding 12 months.
#
# Requires: pip install pytrends pandas

import time
import pandas as pd
from pytrends.request import TrendReq

CANDIDATES = pd.read_csv("data/taxonomy/candidate_topics.csv")

pytrends = TrendReq(hl="en-US", tz=0)

rows = []

for _, row in CANDIDATES.iterrows():
    topic = row["topic"]
    keywords = row["keywords"].split("|")

    # pytrends allows at most 5 keywords per payload; these lists are all
    # well under that limit. "today 5-y" is requested (rather than a
    # shorter window) specifically because it returns *weekly* granularity
    # consistently, which the tail(13)/tail(65) slicing below assumes; a
    # shorter preset like "today 12-m" would return daily granularity and
    # break that slicing.
    pytrends.build_payload(keywords, timeframe="today 5-y", geo="")

    for attempt in range(3):
        try:
            interest = pytrends.interest_over_time()
            break
        except Exception as e:
            print(f"  retry {topic} ({e})")
            time.sleep(5)
    else:
        print(f"  FAILED: {topic}")
        continue

    if interest.empty:
        continue

    for kw in keywords:
        if kw not in interest.columns:
            continue

        series = interest[kw]

        # last 3 months ~ last 13 weeks; preceding 12 months ~ the 52 weeks
        # before that
        recent_3mo = series.tail(13)
        prior_12mo = series.iloc[-(13 + 52):-13] if len(series) >= 65 else series.iloc[:-13]

        recent_mean = recent_3mo.mean()
        prior_mean = prior_12mo.mean()

        if prior_mean and prior_mean > 0:
            growth_pct = (recent_mean - prior_mean) / prior_mean * 100
        else:
            growth_pct = None  # cannot compute growth from a zero/undefined base

        rows.append({
            "topic": topic,
            "keyword": kw,
            "recent_3mo_mean_interest": round(recent_mean, 2),
            "prior_12mo_mean_interest": round(prior_mean, 2),
            "trends_growth_pct": round(growth_pct, 1) if growth_pct is not None else None,
        })

    time.sleep(2)  # be polite to the unofficial endpoint

df = pd.DataFrame(rows)

# aggregate to one growth figure per topic (mean across its keywords)
topic_growth = (
    df.groupby("topic")["trends_growth_pct"]
    .mean()
    .round(1)
    .reset_index()
    .rename(columns={"trends_growth_pct": "trends_growth_pct_topic"})
)
df = df.merge(topic_growth, on="topic", how="left")

df.to_csv(
    "data/google_trends_brain_health.csv",
    index=False
)

print(df)
print("\nSaved data/google_trends_brain_health.csv")
