"""
Short internal note reporting Stage 1-3 results for the Brain Health
Priority Gap Project (POC 2), per methodology.md Section 8's ask:
"not a full formatted briefing note... a short internal note (1-2 pages)
reporting the emergence score per topic, without yet claiming a
recognition gap". MeSH alignment (Stage 4) has not been run, so this
note reports emergence only and does not compute or claim the Priority
Gap Index.

Uses the sidebar visual-identity template from report_style.py. That
template was shared as a proposal and not yet formally signed off as a
permanent identity, but is used here to render the actual first
deliverable, consistent with the project's naming and layout decisions
made so far; the doclabel is set to "Internal note" rather than
"Proposal" since this page reports real, live-collected numbers.
"""

import base64
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from report_style import CSS, topband, pagefoot, pagehead, LOGO_SVG  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent
FIG = ROOT / "figures"


def b64(name):
    data = (FIG / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode()


FIG1 = b64("emergence_score_by_topic.png")

pages = []

# ============================================================== PAGE 1
pages.append(f"""
<div class="page">
{topband(
    "Emergence signal check: eight brain-health topics",
    "Stage 1&ndash;3 internal note &mdash; Google Trends and OpenAlex only, single collection round, 21&ndash;22 July 2026",
    doclabel="Internal note",
)}
<div class="body-pad">
{pagehead("Stage 1–3 results")}

<div class="disclaimer"><strong>This is not the briefing note.</strong> It reports emergence scores from the first Stage 1&ndash;3 collection pass only. It does not compute or claim a Brain Health Priority Gap Index &mdash; that requires MeSH alignment (Stage 4), which has not been run. Read this as a decision input for whether to proceed to Stage 4, not as a finding about recognition gaps.</p></div>

<div class="layout">
  <div class="main">
    <p><strong>All eight candidate topics show positive emergence on a single collection round; four show markedly higher emergence than the rest.</strong> Perimenopause and memory, long COVID cognitive effects, ADHD in women and neurodiversity (adult-diagnosed) combine rising Google Trends search interest with rising OpenAlex publication counts at the same time &mdash; the convergence the emergence-score formula is designed to require, per methodology.md Section 5. The remaining four topics are still growing on both signals, just less sharply.</p>
    <p>Emergence score is calculated exactly as pre-registered: clipped Google Trends growth (recent 3-month mean vs. prior 12-month mean) multiplied by clipped OpenAlex publication growth (trailing 3-year works vs. prior 3-year works from a 6-year series), both terms floored at zero before multiplying<sup>1</sup>. No window or formula choice was adjusted after seeing these numbers.</p>
    <p><strong>Executive function support is a known outlier, not a finding.</strong> Its OpenAlex counts (80,067 prior-period works, 97,559 recent) are an order of magnitude larger than every other topic's, because both of its keyword variants ("executive function", "executive function support") are generic clinical terms without a women's-health qualifier &mdash; flagged in methodology.md Section 6 as a candidate-definition limitation before this data was collected, not adjusted after the fact.</p>
  </div>
  <div class="rail">
    <div class="stat"><div class="n">8 / 8</div><div class="l">Topics with positive emergence</div></div>
    <div class="stat"><div class="n">4</div><div class="l">Topics scoring above 8,000</div></div>
    <div class="railbox">
      <div class="boxtitle">What this note does not show</div>
      <ul>
        <li>No MeSH alignment &mdash; Stage 4 not run.</li>
        <li>No Priority Gap Index &mdash; requires Stage 4.</li>
        <li>No trend line &mdash; one collection round only.</li>
      </ul>
    </div>
  </div>
</div>

<figure>
<figcaption class="figtitle">Figure 1&nbsp; Emergence score by candidate topic</figcaption>
<img src="{FIG1}" style="max-width:92%;">
<div class="src">Source: own analysis, Google Trends (pytrends) / OpenAlex Works API, 21&ndash;22 July 2026.</div>
</figure>

<div class="footnotes">
<p>(1) Both growth terms are clipped at zero before multiplying so that two co-declining signals cannot produce a false-positive emergence score &mdash; documented in calculate_topic_signals.py and methodology.md Section 5 before this data was collected.</p>
</div>
</div>
{pagefoot(1, 2, "Internal note · Stage 1–3 only · not a briefing note")}
</div>
""")

# ============================================================== PAGE 2
pages.append(f"""
<div class="page">
{topband(
    "Evidence table and decision ask",
    "Stage 1&ndash;3 internal note &mdash; continued",
    doclabel="Internal note",
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
    <p>Sleep and cognition has the single highest Trends growth figure (217.9%) but ranks near the bottom on emergence, because its OpenAlex growth is comparatively flat (7.8%) &mdash; the multiplicative formula is doing exactly what it was designed to do: reward convergence across both signals, not strength on either one alone. The same logic explains why postpartum cognitive changes (highest Trends growth of all eight, at 133.3%) still ranks fifth.</p>
    <p>This ranking is a prioritisation signal for a second collection round, not a settled result. A single snapshot cannot distinguish a genuine emerging pattern from short-term attention (e.g. a news cycle affecting search interest, or a conference cycle affecting publication counts in a given window).</p>
  </div>
  <div class="rail">
    <div class="railbox">
      <div class="boxtitle">Decision ask</div>
      <p style="margin:0;">Per methodology.md Section 8: proceed to Stage 4 (MeSH alignment) for the four highest-emergence topics, or hold all eight for a second collection round first. Both are defensible; this note does not recommend one over the other.</p>
    </div>
  </div>
</div>

<div class="citebox">
<div class="contactbrand">
  <div class="logomark" style="background:#2E4A45;">{LOGO_SVG}</div>
  <div><strong>BRAIN HEALTH PRIORITY GAP PROJECT</strong></div>
</div>
<p><strong>Internal note</strong> &mdash; Stage 1&ndash;3 results only, 21&ndash;22 July 2026. Not an official publication; not reviewed or endorsed by any institution.</p>
<div class="rule"></div>
<p><strong>Author:</strong> Eli Ifaturoti &nbsp;&middot;&nbsp; <strong>Email:</strong> liz.ifaturoti@gmail.com</p>
</div>
</div>
{pagefoot(2, 2, "Internal note · Stage 1–3 only · not a briefing note")}
</div>
""")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Brain Health Priority Gap Project — Stage 1-3 Internal Note</title>
<style>{CSS}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

out = ROOT / "briefing" / "stage1_3_internal_note.html"
out.write_text(html, encoding="utf-8")
print(f"Saved {out}")
