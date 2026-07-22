"""
Shared visual identity for the Brain Health Priority Gap Project briefing
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

BRAND_NAME = "BRAIN HEALTH PRIORITY GAP PROJECT"
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
     font-size:10.6px;line-height:1.45;}
@page{size:A4;margin:0;}
.page{
  width:210mm;min-height:297mm;background:#fff;margin:6mm auto;
  position:relative;
  box-shadow:0 0 6px rgba(0,0,0,.25);
}
@media print{
  body{background:#fff;}
  .page{margin:0;box-shadow:none;page-break-after:always;}
}

/* full-width colour band header, replacing POC1's slim logo-left masthead */
.topband{background:var(--deep);color:#fff;padding:9mm 14mm 7mm 14mm;}
.topband .row{display:flex;justify-content:space-between;align-items:flex-start;}
.topband .brandmark{width:24px;height:24px;background:rgba(255,255,255,.14);
  border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.topband .brandmark svg{width:14px;height:14px;}
.logomark{width:26px;height:26px;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.logomark svg{width:16px;height:16px;}
.topband .name{font-weight:800;font-size:11.5px;letter-spacing:.5px;margin-left:8px;}
.topband .tagline{font-size:7.6px;color:#CFE0DC;margin-left:8px;max-width:260px;}
.topband .brandblock{display:flex;align-items:center;}
.topband .doclabel{border:1px solid rgba(255,255,255,.55);border-radius:11px;
  padding:3px 10px;font-size:8.6px;text-transform:uppercase;letter-spacing:.6px;font-weight:700;}
.topband .doctitle{font-size:18px;font-weight:800;text-transform:uppercase;
  letter-spacing:.4px;margin:10px 0 4px 0;line-height:1.2;max-width:85%;}
.topband .subtitle{font-size:10.4px;font-style:italic;color:#DCEAE7;
  border-top:1px solid rgba(255,255,255,.35);padding-top:6px;max-width:88%;}

.body-pad{padding:6mm 14mm 15mm 14mm;}

.disclaimer{font-size:8px;color:var(--grey);
  border:1px dashed var(--rule);padding:5px 8px;border-radius:2px;margin:0 0 9px 0;}

.pagehead{display:flex;justify-content:space-between;align-items:center;
  font-size:7.8px;color:var(--sage);text-transform:uppercase;letter-spacing:.4px;
  margin-bottom:9px;font-weight:700;}

h2.sec{color:var(--deep);font-size:12.5px;text-transform:uppercase;
  letter-spacing:.2px;margin:0 0 8px 0;position:relative;padding-left:10px;}
h2.sec::before{content:"";position:absolute;left:0;top:1px;bottom:1px;width:4px;background:var(--sage);}
h3.sub{color:var(--sage);font-size:10.8px;margin:9px 0 4px 0;font-weight:700;}

/* sidebar layout: main narrative column + a narrower right rail,
   replacing POC1's full-width two-column justified flow */
.layout{display:grid;grid-template-columns:1fr 0.4fr;gap:9mm;align-items:start;}
.main p{margin:0 0 7px 0;text-align:left;}
.rail{border-left:1px solid var(--rule);padding-left:8mm;}

.pullquote{border-top:2px solid var(--sage);border-bottom:2px solid var(--sage);
  padding:8px 0;margin:0 0 10px 0;}
.pullquote .label{display:block;font-size:7.6px;letter-spacing:.5px;text-transform:uppercase;
  color:var(--sage);margin-bottom:4px;font-weight:800;}
.pullquote .q{font-size:12px;font-weight:700;color:var(--deep);line-height:1.35;}

.railbox{background:var(--lightgrey);border-top:3px solid var(--sage);
  padding:7px 9px;margin:0 0 9px 0;font-size:9.2px;break-inside:avoid;}
.railbox .boxtitle{color:var(--deep);font-weight:800;font-size:8.4px;
  text-transform:uppercase;letter-spacing:.3px;margin-bottom:4px;}
.railbox ul{margin:3px 0 0 0;padding-left:13px;}
.railbox li{margin-bottom:3px;}

.stat{margin:0 0 9px 0;}
.stat .n{font-size:19px;font-weight:800;color:var(--deep);line-height:1.1;}
.stat .l{font-size:8px;color:var(--grey);text-transform:uppercase;letter-spacing:.3px;}

figure{margin:7px 0;break-inside:avoid;text-align:center;}
figcaption.figtitle{font-weight:800;font-size:8.6px;text-transform:uppercase;
  color:var(--deep);letter-spacing:.2px;margin-bottom:3px;text-align:left;}
figure img{max-width:100%;border:1px solid var(--rule);}
figure .src{font-size:7.8px;color:var(--grey);font-style:italic;margin-top:2px;text-align:left;}

table{border-collapse:collapse;width:100%;margin:6px 0 9px 0;font-size:8.4px;}
table caption{text-align:left;font-weight:800;font-size:8.6px;text-transform:uppercase;
  color:var(--deep);margin-bottom:3px;}
th{background:#fff;color:var(--deep);text-align:left;padding:3.5px 5px;font-size:8px;
   border-bottom:2px solid var(--deep);}
td{padding:3.5px 5px;border-bottom:1px solid var(--rule);vertical-align:top;}
tr:nth-child(even) td{background:var(--lightgrey);}

.footnotes{border-top:1px dotted var(--rule);padding-top:5px;margin-top:8px;
  font-size:7.4px;color:var(--grey);}
.footnotes p{margin:0 0 3px 0;}
sup{color:var(--sage);font-weight:700;}

.pagefoot{position:absolute;bottom:0;left:0;right:0;
  background:var(--deep);color:#fff;padding:4px 14mm;
  display:flex;justify-content:space-between;font-size:7.6px;
  text-transform:uppercase;letter-spacing:.3px;font-weight:700;}

.citebox{border-top:2px solid var(--deep);border-bottom:2px solid var(--deep);
  padding:8px 0;margin-top:8px;font-size:8.4px;}
.citebox p{margin:0 0 3px 0;}
.citebox .rule{border-top:1px solid var(--rule);margin:5px 0;}
.contactbrand{display:flex;align-items:center;gap:7px;margin-bottom:5px;}

.reftwo{column-count:2;column-gap:7mm;font-size:8px;}
.reftwo p{margin:0 0 5px 0;}
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
          <div class="brandmark">{LOGO_SVG}</div>
          <div>
            <div class="name">{BRAND_NAME}</div>
            <div class="tagline">{BRAND_TAGLINE}</div>
          </div>
        </div>
        <div class="doclabel">{doclabel}</div>
      </div>
      <div class="doctitle">{doctitle}</div>
      <div class="subtitle">{subtitle}</div>
    </div>
    """


def pagehead(section, doc_title="The Brain Health Priority Gap Project — Technical Briefing"):
    return f'<div class="pagehead"><span>{doc_title}</span><span>{section}</span></div>'


def pagefoot(page_no, total_pages, footer_text="Sample POC · Not an official publication"):
    return f'<div class="pagefoot"><span>{footer_text}</span><span>Page {page_no} of {total_pages}</span></div>'
