"""
Draft research document reporting emergence-score results for Brain
Health as an Economic Input (POC 2), per methodology.md Section 8's ask:
a short document (1-2 pages) reporting the emergence score per topic,
without yet claiming a recognition gap. The MeSH comparison step has not
been run, so this document reports emergence only.

Written for a reader with no prior context on the project (this is an
interview writing sample): opens with the policy question and why the
project exists, before any numbers, the same convention used throughout
POC1. The "what's still missing" explanation is given in plain terms
right before the decision ask, rather than as an upfront "Stage 1-3"
label a first-time reader would not recognise.

Uses the sidebar visual-identity template from report_style.py. That
template was shared as a proposal and not yet formally signed off as a
permanent identity, but is used here to render the actual first
deliverable.
"""

import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from report_style import CSS, topband, pagefoot, pagehead  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent
FIG = ROOT / "figures"


def b64(name):
    data = (FIG / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode()


FIG1 = b64("emergence_score_by_topic.png")
FIG2 = b64("wordcloud_and_trend.png")
FIG3 = b64("trends_recent_vs_prior.png")

TOTAL_PAGES = 5
pages = []

# ============================================================== PAGE 1
pages.append(f"""
<div class="page">
{topband(
    "The case for further exploring the link between women's brain health and the economy",
    "Evidence from informal and academic datasets, 22 July 2026",
    doclabel="POC draft research proposal",
)}
<div class="body-pad">
{pagehead("Evidence")}

<p class="byline"><strong>Eli Ifaturoti</strong> &nbsp;&middot;&nbsp; eli.ifaturoti@oecd.org</p>

<p>Interest in women's brain health and its correlation with labour have soared since 2021: across eight related topics, public search interest rose by an average of 115% and academic publishing on the same topics grew by an average of 65%, comparing a recent snapshot against the prior period.</p>

<p>A Google Trends keyword combination search revealed particularly sharp growth for specific terms: "postpartum memory" search interest is up 251.5%, "sleep deprivation cognition" up 235.7%, "post covid cognitive" up 213.7%, and "perimenopause memory" up 191.0%, each comparing the recent 3-month mean against the prior 12-month mean.</p>

<p>The graphic below shows that evolution in interest and users' search, comparing the recent 3-month mean against the prior 12-month mean for each topic.</p>

<figure>
<figcaption class="figtitle">Figure 1&nbsp; Google Trends search interest, recent vs. prior period, by topic</figcaption>
<img src="{FIG3}" style="max-width:92%;">
<div class="src">Source: own analysis, Google Trends (pytrends), 22 July 2026.</div>
</figure>

</div>
{pagefoot(1, TOTAL_PAGES, "POC draft research proposal")}
</div>
""")

# ============================================================== PAGE 2
pages.append(f"""
<div class="page">
{topband(
    "Academic publishing evidence: the OpenAlex query",
    "Continued",
    doclabel="POC draft research proposal",
)}
<div class="body-pad">
{pagehead("Evidence")}

<p>An OpenAlex query also revealed a matching rise in academic output: publications on Long Covid cognitive effects grew from 18 in 2021 to a peak of 236 in 2024; work on neurodiversity in adults rose every year, from 13 in 2021 to 62 already in the partial 2026 count; and perimenopause-and-memory publications more than tripled, from 7 in 2021 to 25 so far in 2026. The word cloud and publication trend below are drawn from that same OpenAlex corpus.</p>

<figure>
<figcaption class="figtitle">Figure 2&nbsp; Most frequent terms in the OpenAlex corpus, and publication growth for the four fastest-growing topics</figcaption>
<img src="{FIG2}" style="max-width:100%;">
<div class="src">Source: own analysis, OpenAlex works corpus (word cloud) and OpenAlex Works API by year (trend lines), 22 July 2026. 2026 figures are partial-year.</div>
</figure>

</div>
{pagefoot(2, TOTAL_PAGES, "POC draft research proposal")}
</div>
""")

# ============================================================== PAGE 3
pages.append(f"""
<div class="page">
{topband(
    "Premise: why this proposal, and what it tests",
    "Continued",
    doclabel="POC draft research proposal",
)}
<div class="body-pad">
{pagehead("Premise")}

<div class="pullquote"><span class="label">Policy question</span><span class="q">Does discourse from public and unconventional datasets amplify academic evidence of female brain health being economically material?</span></div>

<div class="layout">
  <div class="main">
    <p>OECD has already made the case that women's brain health is economically material: its New Approaches for Economic Challenges unit has run Brain Capital, a programme treating brain health as a core economic asset, since 2021, including work on sex and gender differences in neurological outcomes<sup>1</sup>. What is not yet tested is whether public, unconventional data, search interest, publishing activity, amplifies that case: gives it earlier, cheaper, independently observable evidence than the institutional argument alone provides.</p>
    <p>The labour-market cost that argument points to is already measured: menopausal symptoms are linked to higher sick leave and lower work productivity<sup>2</sup>, adult ADHD to comparably large productivity loss<sup>3</sup>, and Long Covid to higher odds of leaving employment the longer symptoms persist<sup>4</sup>. If unconventional public data tracks the same conditions, it gives policymakers a faster, cheaper signal on top of the institutional case, not a competing one.</p>
    <p>This proposal tests a narrower, answerable version of that question: for eight topics spanning the female lifespan, perimenopause and memory, adult ADHD in women, long COVID cognitive effects and others, is public search interest and academic publishing growing fast enough to count as that kind of evidence. The previous page reported that first check, using two free data sources, Google Trends and OpenAlex. It does not yet run the medical-recognition check itself, against MeSH, the step that would show whether a topic already has a formal classification.</p>
    <p>Working hypothesis: these eight topics are gaining public and research attention faster than they are gaining formal medical recognition. The eight were chosen because each names a phase of the female lifespan or a related cognitive condition already raised in OECD's Brain Capital seminars, not because they scored highest in a broader keyword sweep.</p>
  </div>
  <div class="rail">
    <div class="stat"><div class="n">8 / 8</div><div class="l">Topics with positive emergence</div></div>
    <div class="stat"><div class="n">4</div><div class="l">Topics scoring above 8,000</div></div>
    <div class="railbox">
      <div class="boxtitle">Objective, this round</div>
      <p style="margin:0;">Confirm, from this single 22 July 2026 data pull, whether at least half of the eight topics show positive growth on both signals, enough to justify running the MeSH comparison next round.</p>
    </div>
    <div class="railbox">
      <div class="boxtitle">Limitations</div>
      <ul>
        <li>No comparison against existing medical terminology yet.</li>
        <li>No combined priority score, only the emergence half.</li>
        <li>No trend line beyond the years shown here, one collection round only.</li>
      </ul>
    </div>
  </div>
</div>

<div class="footnotes">
<p>(1) Eyre et al. (2021), <em>Neuron</em>. (2) O'Neill, Jones &amp; Reid (2023), <em>Occupational Medicine</em>. (3) Joseph et al. (2019), <em>Journal of Attention Disorders</em>. (4) Ayoubkhani et al. (2024), <em>European Journal of Public Health</em>. Full citations on page 5.</p>
</div>

</div>
{pagefoot(3, TOTAL_PAGES, "POC draft research proposal")}
</div>
""")

# ============================================================== PAGE 4
pages.append(f"""
<div class="page">
{topband(
    "What the two data sources show",
    "Continued",
    doclabel="POC draft research proposal",
)}
<div class="body-pad">
{pagehead("Findings")}

<h2 class="sec">All eight topics are growing; four stand out</h2>
<p>Perimenopause and memory, long COVID cognitive effects, ADHD in women and neurodiversity (adult-diagnosed) combine rising Google Trends search interest with rising OpenAlex publication counts at the same time, exactly the kind of convergence the emergence-score formula was designed to reward rather than either signal rising on its own. The remaining four topics are still growing on both signals, just less sharply.</p>
<p>Emergence score is calculated exactly as pre-registered: clipped Google Trends growth (recent 3-month mean vs. prior 12-month mean) multiplied by clipped OpenAlex publication growth (trailing 3-year works vs. prior 3-year works from a 6-year series), both terms floored at zero before multiplying<sup>1</sup>. No window or formula choice was adjusted after seeing these numbers.</p>

<h2 class="sec">Executive function support is a known outlier</h2>
<p>Its OpenAlex counts (80,067 prior-period works, 97,559 recent) are an order of magnitude larger than every other topic's, because both of its keyword variants ("executive function", "executive function support") are generic clinical terms without a women's-health qualifier. That risk was written down as a limitation before the data was collected, not adjusted after seeing the numbers.</p>

<figure>
<figcaption class="figtitle">Figure 1&nbsp; Emergence score by candidate topic</figcaption>
<img src="{FIG1}" style="max-width:88%;">
<div class="src">Source: own analysis, Google Trends (pytrends) / OpenAlex Works API, 22 July 2026.</div>
</figure>

<div class="footnotes">
<p>(1) Both growth terms are clipped at zero before multiplying, a rule fixed before this data was collected, so that two co-declining signals cannot produce a false-positive emergence score.</p>
</div>
</div>
{pagefoot(4, TOTAL_PAGES, "POC draft research proposal")}
</div>
""")

# ============================================================== PAGE 5
pages.append(f"""
<div class="page">
{topband(
    "Evidence table and what happens next",
    "Continued",
    doclabel="POC draft research proposal",
)}
<div class="body-pad">
{pagehead("Evidence and next step")}

<h2 class="sec">Evidence summary</h2>
<table>
<caption>Emergence components by topic, ranked by emergence score</caption>
<tr><th>Topic</th><th>Trends growth %</th><th>OpenAlex growth %</th><th>Emergence score</th></tr>
<tr><td>Perimenopause and memory</td><td>117.8</td><td>134.4</td><td>15,829</td></tr>
<tr><td>Long COVID cognitive effects</td><td>121.7</td><td>82.8</td><td>10,078</td></tr>
<tr><td>ADHD in women</td><td>100.1</td><td>96.0</td><td>9,610</td></tr>
<tr><td>Neurodiversity (adult-diagnosed)</td><td>67.6</td><td>124.6</td><td>8,426</td></tr>
<tr><td>Postpartum cognitive changes</td><td>133.3</td><td>21.1</td><td>2,806</td></tr>
<tr><td>Executive function support</td><td>105.0</td><td>21.8</td><td>2,294</td></tr>
<tr><td>Sleep and cognition</td><td>217.9</td><td>7.8</td><td>1,704</td></tr>
<tr><td>Brain fog</td><td>53.1</td><td>31.8</td><td>1,689</td></tr>
</table>

<div class="layout">
  <div class="main">
    <h2 class="sec">Reading the ranking correctly</h2>
    <p>Sleep and cognition has the highest Trends growth (217.9%) but ranks near the bottom on emergence because its OpenAlex growth is flat (7.8%): the multiplicative formula rewards convergence across both signals over strength on either one alone. The same logic explains why postpartum cognitive changes, the highest Trends growth of all eight at 133.3%, still ranks fifth.</p>
    <h2 class="sec">What's still missing</h2>
    <p>The medical-recognition check has not been run yet. This page compares public search interest against academic publishing only, not yet against MeSH, the US National Library of Medicine's controlled vocabulary, which would show whether a topic already has formal recognition. Adding that comparison would produce a single priority score per topic; without it, these numbers describe attention and publishing activity only.</p>
  </div>
  <div class="rail">
    <div class="railbox">
      <div class="boxtitle">Decision ask</div>
      <p style="margin:0;">Two options: add the medical-terminology comparison now for the four strongest-growth topics, or first repeat the count for all eight to confirm the ranking holds. The first is faster but rests on one data pull; the second costs a delay but checks against a one-off spike. Neither is clearly better, so the choice is left open here.</p>
    </div>
  </div>
</div>

<h2 class="sec">References</h2>
<div class="reftwo">
<p><strong>Academic</strong> &mdash; Eyre et al. (2021). Building brain capital. <em>Neuron</em>, 109(9).</p>
<p>O'Neill, Jones &amp; Reid (2023). Impact of menopausal symptoms on work and careers. <em>Occupational Medicine</em>, 73(6).</p>
<p>Joseph et al. (2019). Health-related quality of life and work productivity of adults with ADHD. <em>Journal of Attention Disorders</em>, 23(12).</p>
<p>Ayoubkhani et al. (2024). Employment outcomes of people with Long Covid symptoms. <em>European Journal of Public Health</em>, 34(3).</p>
<p><strong>Institutional</strong> &mdash; OECD NAEC Unit, Neuroscience-inspired Policy Initiative, Brain Capital programme.</p>
<p><strong>Data sources</strong> &mdash; Google Trends (pytrends); OpenAlex Works API, 22 July 2026.</p>
</div>

<div class="citebox">
<p><strong>BRAIN HEALTH AS AN ECONOMIC INPUT</strong> &nbsp;&middot;&nbsp; POC draft research proposal, 22 July 2026.</p>
<div class="rule"></div>
<p><strong>Author:</strong> Eli Ifaturoti &nbsp;&middot;&nbsp; <strong>Email:</strong> eli.ifaturoti@oecd.org</p>
</div>
</div>
{pagefoot(5, TOTAL_PAGES, "POC draft research proposal")}
</div>
""")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Brain Health as an Economic Input — Draft Research Document</title>
<style>{CSS}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

out = ROOT / "briefing" / "stage1_3_internal_note.html"
out.write_text(html, encoding="utf-8")
print(f"Saved {out}")
