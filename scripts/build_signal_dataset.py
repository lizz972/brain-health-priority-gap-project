# Builds a unified per-topic signal table from the Google Trends growth
# data and the OpenAlex works-per-year series, ahead of emergence scoring.
#
# Requires: pip install pandas

import pandas as pd

trends = pd.read_csv("data/google_trends_brain_health.csv")
trends_topic = trends[["topic", "trends_growth_pct_topic"]].drop_duplicates()

yearly = pd.read_csv("data/openalex_works_per_year.csv", index_col="topic")
year_cols = sorted(yearly.columns.astype(int))
recent_3yr_cols = [str(y) for y in year_cols[-3:]]
prior_3yr_cols = [str(y) for y in year_cols[-6:-3]]

yearly["recent_3yr_works"] = yearly[recent_3yr_cols].sum(axis=1)
yearly["prior_3yr_works"] = yearly[prior_3yr_cols].sum(axis=1)

signals = trends_topic.merge(
    yearly[["recent_3yr_works", "prior_3yr_works"]],
    left_on="topic",
    right_index=True,
    how="left",
)

signals.to_csv("data/digital_topic_signals.csv", index=False)
print(signals)
print("\nSaved data/digital_topic_signals.csv")
