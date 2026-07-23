"""
Shared visual identity for the Brain Health as an Economic Input briefing
note (POC 2). Same muted, institutional register as the Hidden Skills
Radar (POC 1) template, but a distinct layout grammar as well as a
distinct palette, so the two documents are never mistaken for each other
even in black-and-white photocopy:

- POC1: masthead with logo-left/doclabel-right, full-width two-column
  justified body, inline boxes at full column width, dark solid-fill
  policy-question banner, bottom-of-page footnotes.
- POC2: full-width colour band header (not a slim masthead rule),
  single main column + a narrower right-hand rail that carries the
  policy question as a pull-quote, box call-outs and footnotes — a
  sidebar layout rather than an inline two-column one.

Palette: muted slate teal — deep teal-slate + sage accent, gender-neutral
and clinical in register (deliberately not a "women's health" pink),
matching POC1's institutional/Cedefop-style muted tone without reusing
its exact hues.

Naming note: this project is deliberately not called a "radar" — that
name belongs to POC1. Use BRAND_NAME below wherever the product name
appears in generated documents.

Status note: nothing built with this style module has been adopted yet.
Anything rendered with it should say "proposal" or "preview" somewhere
on the page until the user signs off on it.

Usage: import CSS, topband(), pagefoot() into a build_report_html.py for
this project once Stage 4 findings are final, the same way
scripts/build_report_html.py in POC1 assembles its pages.
"""

BRAND_NAME = "BRAIN HEALTH AS AN ECONOMIC INPUT"
BRAND_TAGLINE = "Independent sample proof-of-concept skills intelligence analysis"

CSS = """
:root{
  --deep:#2E4A45;
  --sage:#4F7A72;
  --grey:#5A5F5B;
  --lightgrey:#EEF2F0;
  --rule:#CBD6D1;
  --text:#1A1A1A;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:#e9e9e9;}
body{font-family:Arial,Helvetica,"Segoe UI",sans-serif;color:var(--text);
     font-size:13.5px;line-height:1.5;}
@page{size:A4;margin:0;}
.page{
  width:210mm;height:297mm;background:#fff;margin:6mm auto;
  position:relative;
  box-shadow:0 0 6px rgba(0,0,0,.25);
}
@media print{
  body{background:#fff;}
  .page{margin:0;box-shadow:none;page-break-after:always;height:297mm;}
}

/* full-width colour band header, replacing POC1's slim logo-left masthead */
.topband{background:var(--deep);color:#fff;padding:9mm 14mm 7mm 14mm;}
.topband .row{display:flex;justify-content:space-between;align-items:flex-start;}
.topband .brandmark{width:30px;height:30px;background:rgba(255,255,255,.14);
  border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.topband .brandmark svg{width:18px;height:18px;}
.logomark{width:32px;height:32px;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.logomark svg{width:20px;height:20px;}
.topband .name{font-weight:800;font-size:14.5px;letter-spacing:.5px;margin-left:8px;}
.topband .tagline{font-size:10px;color:#CFE0DC;margin-left:8px;max-width:320px;}
.topband .brandblock{display:flex;align-items:center;}
.topband .doclabel{border:1px solid rgba(255,255,255,.55);border-radius:12px;
  padding:4px 12px;font-size:11px;text-transform:uppercase;letter-spacing:.6px;font-weight:700;}
.topband .doctitle{font-size:23px;font-weight:800;text-transform:uppercase;
  letter-spacing:.4px;margin:12px 0 5px 0;line-height:1.2;max-width:85%;}
.topband .subtitle{font-size:13.5px;font-style:italic;color:#DCEAE7;
  border-top:1px solid rgba(255,255,255,.35);padding-top:7px;max-width:88%;}

.body-pad{padding:6mm 14mm 11mm 14mm;}

.byline{font-size:11px;color:var(--grey);margin:0 0 10px 0;}
.byline strong{color:var(--deep);}

.disclaimer{font-size:10.5px;color:var(--grey);
  border:1px dashed var(--rule);padding:7px 10px;border-radius:2px;margin:0 0 11px 0;}

.pagehead{display:flex;justify-content:space-between;align-items:center;
  font-size:10px;color:var(--sage);text-transform:uppercase;letter-spacing:.4px;
  margin-bottom:8px;font-weight:700;}

h2.sec{color:var(--deep);font-size:15px;text-transform:uppercase;
  letter-spacing:.2px;margin:0 0 7px 0;position:relative;padding-left:12px;}
h2.sec::before{content:"";position:absolute;left:0;top:1px;bottom:1px;width:4px;background:var(--sage);}
h3.sub{color:var(--sage);font-size:14px;margin:8px 0 4px 0;font-weight:700;}

/* sidebar layout: main narrative column + a narrower right rail,
   replacing POC1's full-width two-column justified flow */
.layout{display:grid;grid-template-columns:1fr 0.4fr;gap:8mm;align-items:start;}
.main p{margin:0 0 5px 0;text-align:left;}
.rail{border-left:1px solid var(--rule);padding-left:8mm;}

.pullquote{border-top:2px solid var(--sage);border-bottom:2px solid var(--sage);
  padding:10px 0;margin:0 0 12px 0;}
.pullquote .label{display:block;font-size:10px;letter-spacing:.5px;text-transform:uppercase;
  color:var(--sage);margin-bottom:5px;font-weight:800;}
.pullquote .q{font-size:15px;font-weight:700;color:var(--deep);line-height:1.4;}

.railbox{background:var(--lightgrey);border-top:3px solid var(--sage);
  padding:9px 11px;margin:0 0 11px 0;font-size:12px;break-inside:avoid;}
.railbox .boxtitle{color:var(--deep);font-weight:800;font-size:11px;
  text-transform:uppercase;letter-spacing:.3px;margin-bottom:5px;}
.railbox ul{margin:4px 0 0 0;padding-left:15px;}
.railbox li{margin-bottom:4px;}

.stat{margin:0 0 11px 0;}
.stat .n{font-size:25px;font-weight:800;color:var(--deep);line-height:1.1;}
.stat .l{font-size:10.5px;color:var(--grey);text-transform:uppercase;letter-spacing:.3px;}

figure{margin:9px 0;break-inside:avoid;text-align:center;}
figcaption.figtitle{font-weight:800;font-size:11px;text-transform:uppercase;
  color:var(--deep);letter-spacing:.2px;margin-bottom:4px;text-align:left;}
figure img{max-width:100%;border:1px solid var(--rule);}
figure .src{font-size:10.5px;color:var(--grey);font-style:italic;margin-top:3px;text-align:left;}

table{border-collapse:collapse;width:100%;margin:8px 0 11px 0;font-size:12px;}
table caption{text-align:left;font-weight:800;font-size:11px;text-transform:uppercase;
  color:var(--deep);margin-bottom:4px;}
th{background:#fff;color:var(--deep);text-align:left;padding:5px 7px;font-size:11px;
   border-bottom:2px solid var(--deep);}
td{padding:5px 7px;border-bottom:1px solid var(--rule);vertical-align:top;}
tr:nth-child(even) td{background:var(--lightgrey);}

.footnotes{border-top:1px dotted var(--rule);padding-top:6px;margin-top:10px;
  font-size:10.5px;color:var(--grey);}
.footnotes p{margin:0 0 4px 0;}
sup{color:var(--sage);font-weight:700;}

.pagefoot{position:absolute;bottom:0;left:0;right:0;
  background:var(--deep);color:#fff;padding:6px 14mm;
  display:flex;justify-content:space-between;font-size:10px;
  text-transform:uppercase;letter-spacing:.3px;font-weight:700;}

.citebox{border-top:2px solid var(--deep);border-bottom:2px solid var(--deep);
  padding:7px 0;margin-top:6px;font-size:12px;}
.citebox p{margin:0 0 4px 0;}
.citebox .rule{border-top:1px solid var(--rule);margin:6px 0;}
.contactbrand{display:flex;align-items:center;gap:9px;margin-bottom:6px;}

.reftwo{column-count:2;column-gap:7mm;font-size:10px;}
.reftwo p{margin:0 0 4px 0;line-height:1.35;}
"""

LOGO_SVG = """<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="9" stroke="#fff" stroke-width="1.6"/>
<path d="M12 4 L12 12 L18 15" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round"/>
</svg>"""


def topband(doctitle, subtitle, doclabel="Proposal"):
    """Full-width colour-band header + title block (replaces POC1's slim masthead).

    doclabel defaults to "Proposal" rather than "Briefing note": nothing
    built with this identity has been adopted yet, so every page should
    say so upfront rather than only in a disclaimer paragraph.
    """
    return f"""
    <div class="topband">
      <div class="row">
        <div class="brandblock">
          <div class="name">{BRAND_NAME}</div>
        </div>
        <div class="doclabel">{doclabel}</div>
      </div>
      <div class="doctitle">{doctitle}</div>
      <div class="subtitle">{subtitle}</div>
    </div>
    """


def pagehead(section, doc_title="Brain Health as an Economic Input"):
    return f'<div class="pagehead"><span>{doc_title}</span><span>{section}</span></div>'


def pagefoot(page_no, total_pages, footer_text="POC draft research proposal"):
    return f'<div class="pagefoot"><span>{footer_text}</span><span>Page {page_no} of {total_pages}</span></div>'
