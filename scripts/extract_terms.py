# Diagnostic term-frequency scan over the corpus. Not read by any later
# pipeline stage; a sanity check on vocabulary before scoring.
#
# Requires: pip install pandas scikit-learn

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("data/brain_health_text_corpus.csv")
df = df[df["text"].fillna("").str.strip() != ""]

if df.empty:
    print("No text to analyse (corpus is empty).")
else:
    vectorizer = CountVectorizer(stop_words="english", ngram_range=(1, 3), min_df=2)
    X = vectorizer.fit_transform(df["text"])
    terms = vectorizer.get_feature_names_out()
    counts = X.sum(axis=0).A1

    results = pd.DataFrame({"term": terms, "frequency": counts})
    results = results.sort_values("frequency", ascending=False)
    results.to_csv("outputs/emerging_terms.csv", index=False)

    print(results.head(50))
    print("\nSaved outputs/emerging_terms.csv")
