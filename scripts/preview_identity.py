"""
One-page rendered preview of the POC2 visual-identity PROPOSAL
(report_style.py), so the palette AND layout can be checked on an actual
printed page rather than only as a chat mockup. This is a proposal, not
an adopted identity and not a briefing note — Stage 4 (MeSH alignment)
hasn't run yet, so there is no final finding to report either. Exists
purely to get sign-off on the look before it's wired into a real
build_report_html.py once the briefing note is written.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from report_style import CSS, topband, pagefoot, pagehead  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent

page = f"""
<div class="page">
{topband(
    "Proposal: layout &amp; palette for review",
    "Not yet adopted. Stage 1&ndash;3 data collected, Stage 4 (MeSH alignment) and findings not yet run.",
)}
<div class="body-pad">
{pagehead("Layout check")}
<div class="disclaimer"><strong>This is a proposal, not an adopted identity or a briefing note.</strong> It uses a sidebar layout &mdash; a single main column plus a narrower right-hand rail &mdash; deliberately different from POC1's full-width two-column arrangement, in a distinct muted slate-teal palette, and a project name that does not reuse POC1's "radar" branding. Nothing on this page reflects a real finding.</div>

<h2 class="sec">Placeholder section heading</h2>
<div class="layout">
  <div class="main">
    <p><strong>This is where the opening key-message paragraph will sit once Stage 4 is complete.</strong> Single-column body copy, left-aligned rather than justified, with a rule-and-tab section heading instead of POC1's full-width underlined heading.</p>
    <p>Second paragraph placeholder, showing how a longer block of body copy reads in this palette at the same 10.6px base size used in POC1, but in one column instead of two.</p>
    <p>Third paragraph placeholder with a footnote marker<sup>1</sup> to check the sage superscript colour against the rest of the running text.</p>
  </div>
  <div class="rail">
    <div class="pullquote"><span class="label">Policy question</span><span class="q">Placeholder policy-question text, styled as a rule-bordered pull-quote rather than POC1's solid-fill banner.</span></div>
    <div class="stat"><div class="n">8</div><div class="l">Candidate topics</div></div>
    <div class="railbox">
      <div class="boxtitle">Box 1 &nbsp;Placeholder box title</div>
      <ul>
        <li><strong>Placeholder item:</strong> top-border rail-box styling check.</li>
        <li><strong>Placeholder item:</strong> sage top rule, light-teal fill.</li>
      </ul>
    </div>
    <div class="footnotes">
      <p>(1) Placeholder footnote, dotted top rule instead of POC1's solid one.</p>
    </div>
  </div>
</div>
</div>
{pagefoot(1, 1, "Proposal · pending review · not a briefing note")}
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Brain Health Priority Gap Project &mdash; Identity proposal</title>
<style>{CSS}</style>
</head>
<body>
{page}
</body>
</html>"""

out = ROOT / "briefing" / "identity_preview.html"
out.write_text(html, encoding="utf-8")
print(f"Saved {out}")
