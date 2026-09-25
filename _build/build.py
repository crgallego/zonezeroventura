#!/usr/bin/env python3
"""Zone Zero Ventura static build generator.
Hand-authored content in content_*.py; this file holds shared chrome only.
Output: plain HTML files, no build tooling shipped in repo (script is repo-local dev aid)."""
import json, os, re

DOMAIN = "https://www.zonezeroventura.com"
SITE_NAME = "Zone Zero Ventura"
FOOTER_GEOGRAPHY = "Ventura County homeowners, from the Ojai foothills to the coast"
PHONE_TEL = "+18055678416"
PHONE_DISPLAY = "(805) 567-8416"
GA4 = "G-X43DDVCW9W"
PIXEL = "838658782511294"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Zone checker widget (hosted on zone-zero-checker-api.netlify.app; nothing
# bundled here). Home page only. Values match this site's entry in
# zone-zero-checker-api's config/network-site-checker.json.
CHECKER_CSS_HREF = "https://zone-zero-checker-api.netlify.app/zz-checker.css"
CHECKER_JS_SRC = "https://zone-zero-checker-api.netlify.app/zz-checker.js"
CHECKER_API_URL = "https://zone-zero-checker-api.netlify.app/api/zone-checker/v2"
CHECKER_CITY_DISPLAY_NAME = "Ventura County"
CHECKER_CTA_HREF = "/request-inspection/#zz-request-inspection"
CHECKER_CTA_LABEL = "Request an inspection"
CHECKER_LA_COUNTY_OVERLAY_APPLIES = False

def checker_section():
    overlay_clause = (
        " For Los Angeles County properties, the county’s 2025 overlay takes precedence over the statewide map."
        if CHECKER_LA_COUNTY_OVERLAY_APPLIES else
        " County-level overlays take precedence over the statewide map where one applies."
    )
    return f"""
<!-- ================= ZONE CHECKER ================= -->
<section style="background:#fff" aria-labelledby="zone-checker-heading">
  <div class="zz-container">
    <div class="zz-center zz-reveal" style="margin-bottom:36px">
      <span class="zz-eyebrow">Check Your Address</span>
      <h2 class="zz-h2" id="zone-checker-heading">Which fire department covers this {CHECKER_CITY_DISPLAY_NAME} parcel?</h2>
      <p class="zz-body" style="margin:0 auto;max-width:56ch">Enter your address to check it against the CAL FIRE Fire Hazard Severity Zone map. The same check helps show whether you sit in VCFPD, the City of Ventura, or another municipal fire department.{overlay_clause}</p>
    </div>
    <div data-zz-checker
         data-api-url="{CHECKER_API_URL}"
         data-cta-href="{CHECKER_CTA_HREF}"
         data-cta-label="{CHECKER_CTA_LABEL}"
         data-default-city="{CHECKER_CITY_DISPLAY_NAME}"></div>
  </div>
</section>"""

FONTS = "https://fonts.googleapis.com/css2?family=Domine:wght@400;500;600;700&family=Mulish:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap"

def head(title, desc, path, ld, recaptcha=False, depth=1, checker=False, meta_title=None, meta_desc=None):
    pre = "../" * depth if depth else ""
    url = DOMAIN + path
    mt = meta_title if meta_title is not None else title
    md = meta_desc if meta_desc is not None else desc
    rc = ('<script src="https://www.google.com/recaptcha/api.js?render='
          '6Lfh4U4tAAAAALuYKhSwIpggriOhdKqEsj6XBFo6"></script>\n') if recaptcha else ""
    checker_css = f'<link rel="stylesheet" href="{CHECKER_CSS_HREF}">\n' if checker else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{mt}</title>
<meta name="description" content="{md}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{mt}">
<meta property="og:description" content="{md}">
<meta property="og:site_name" content="{SITE_NAME}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{pre}css/site.css">
<!-- Analytics and ads, loaded by /js/zz-consent.js (on by default, off with GPC or opt-out) -->
<meta name="zz-ga4" content="{GA4}"><meta name="zz-pixel" content="{PIXEL},3477703075702797">
<script defer src="/js/zz-consent.js"></script>
{rc}<script type="application/ld+json">
{json.dumps(ld, indent=1, ensure_ascii=False)}
</script>
<style id="zz-transparency">
.zz-phone-disclosure{{display:block;font-size:12px;line-height:1.45;margin-top:6px;font-weight:400;letter-spacing:0;text-transform:none;max-width:46ch;opacity:.9}}
.zz-cta-btns .zz-phone-disclosure{{flex-basis:100%;margin-top:10px}}
.zz-footer .zz-phone-disclosure{{margin-top:4px;opacity:.8}}
.zz-operator-line{{margin-bottom:10px}}
</style>
{checker_css}</head>
<body>
"""

LOGO_SVG = """<svg class="zz-logo-mark" viewBox="0 0 34 34" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect x="6" y="8" width="4" height="18" rx="1" fill="#C9A66B"/><rect x="15" y="5" width="4" height="21" rx="1" fill="#E3C68A"/><rect x="24" y="10" width="4" height="16" rx="1" fill="#C9A66B"/><path d="M2 28 Q6 25 10 28 T18 28 T26 28 T34 28" stroke="#E3C68A" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>"""

def nav():
    return f"""<nav class="zz-nav" aria-label="Main">
<div class="zz-nav-inner">
<a href="/" class="zz-logo">{LOGO_SVG}<span class="zz-logo-text">Zone Zero<small>Ventura</small></span></a>
<button class="zz-nav-toggle" aria-expanded="false" aria-label="Menu">&#9776;</button>
<ul class="zz-nav-links">
<li><a href="/regulations/">Regulations</a></li>
<li><a href="/deadlines/">Deadlines</a></li>
<li><a href="/fences/">Fences</a></li>
<li><a href="/fire-history/">Fire History</a></li>
<li><a href="/resources/">Resources</a></li>
<li><a href="/request-inspection/" class="zz-nav-cta">Request an inspection</a></li>
</ul>
</div>
</nav>
"""

def cta(place="your Ventura County property", trackc=False):
    if trackc:
        return f"""<section class="zz-cta zz-cta-trackc">
<div class="zz-container">
<h2 class="zz-cta-title">Support is available for {place}</h2>
<p>Grant programs and free defensible-space guidance exist for mountain communities. Verify current openings through official channels before spending.</p>
<a href="/assistance/" class="zz-btn">See assistance programs</a>
<p style="margin-top:18px;margin-bottom:0">Questions? Call <a class="zz-cta-tel" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or <a class="zz-cta-tel" href="/request-inspection/">get in touch</a>
          <span class="zz-phone-disclosure">Calls are answered by an automated AI assistant and may be recorded and transcribed.</span>.</p>
</div>
</section>
"""
    return f"""<section class="zz-cta">
<div class="zz-container">
<h2 class="zz-cta-title">Find out what {place} needs</h2>
<p>Submit your address and we will follow up about which local rules apply to your parcel, what your fire authority will look for, and what to fix first.</p>
<a href="/request-inspection/" class="zz-btn">Request an inspection</a>
<p style="margin-top:18px;margin-bottom:0">Prefer to talk? Call <a class="zz-cta-tel" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <span class="zz-phone-disclosure">Calls are answered by an automated AI assistant and may be recorded and transcribed.</span></p>
</div>
</section>
"""

def footer(checker=False):
    checker_script = f'<script src="{CHECKER_JS_SRC}" defer></script>\n' if checker else ""
    return f"""<footer class="zz-footer">
<div class="zz-container">
<div class="zz-footer-grid">
<div class="zz-footer-about">
<h4>Zone Zero Ventura</h4>
<p>Plain-English guidance on wildfire home hardening and local Zone 0 rules for {FOOTER_GEOGRAPHY}. Independent educational resource. Not a government agency.</p>
</div>
<div>
<h4>Guides</h4>
<ul>
<li><a href="/regulations/">The regulations</a></li>
<li><a href="/deadlines/">Deadlines</a></li>
<li><a href="/fences/">Fences &amp; gates</a></li>
<li><a href="/landscaping/">Landscaping</a></li>
<li><a href="/home-hardening/">Home hardening</a></li>
<li><a href="/assistance/">Assistance programs</a></li>
</ul>
</div>
<div>
<h4>Communities</h4>
<ul>
<li><a href="/ventura/">City of Ventura</a></li>
<li><a href="/ojai/">Ojai</a></li>
<li><a href="/camarillo/">Camarillo</a></li>
<li><a href="/thousand-oaks/">Thousand Oaks</a></li>
<li><a href="/fire-history/">County fire history</a></li>
</ul>
</div>
<div>
<h4>Network</h4>
<ul>
<li><a href="https://zonezerocalifornia.com">Zone Zero California</a></li>
<li><a href="https://www.zonezerolosangeles.com">Zone Zero Los Angeles</a></li>
<li><a href="https://www.zonezerosandiego.com">Zone Zero San Diego</a></li>
<li><a href="/resources/">Official resources</a></li>
<li><a href="/privacy/">Privacy</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/terms/">Terms of Use</a></li>
</ul>
</div>
</div>
<div class="zz-footer-bottom">
      <p class="zz-operator-line">Zone Zero Ventura County is published by Zone Zero Property Inspections. It is an independent informational resource and is not affiliated with, endorsed by, or operated by any government agency, including the City of Ventura County, the County, CAL FIRE, or any fire department. Zone Zero Property Inspections is not a contractor.</p>
<p>&copy; 2026 Zone Zero Ventura. Educational information, not legal advice. Regulations change: verify requirements with your local fire authority before making decisions. Questions? Call {PHONE_DISPLAY}.</p>
</div>
</div>
</footer>
<script src="/js/site.js"></script>
{checker_script}</body>
</html>
"""

def base_ld(title, desc, path, crumbs, faqs=None, area=None, service=False):
    graph = [
        {"@type": "Organization", "@id": "https://zonezerocalifornia.com/#org",
         "name": "Zone Zero California", "url": "https://zonezerocalifornia.com",
         "description": "An independent educational resource on wildfire home hardening and local Zone 0 rules in California."},
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/",
         "name": SITE_NAME, "publisher": {"@id": "https://zonezerocalifornia.com/#org"}},
    ]
    page = {"@type": "WebPage", "@id": DOMAIN + path + "#webpage",
            "url": DOMAIN + path, "name": title, "description": desc,
            "isPartOf": {"@id": DOMAIN + "/#website"}}
    if area:
        page["areaServed"] = {"@type": "Place", "name": area}
    if service:
        page["about"] = {"@id": DOMAIN + "/#service"}
    graph.append(page)
    if service:
        served = {"@type": "Place", "name": area} if area else {"@type": "AdministrativeArea", "name": "Ventura County, California"}
        graph.append({
            "@type": "Service",
            "@id": DOMAIN + "/#service",
            "name": "Zone Zero information",
            "serviceType": "Wildfire home hardening information",
            "provider": {"@id": "https://zonezerocalifornia.com/#org"},
            "areaServed": served,

        })
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p}
             for i, (n, p) in enumerate(crumbs)]
    graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if faqs:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in faqs]})
    return {"@context": "https://schema.org", "@graph": graph}

def faq_html(faqs, heading):
    out = [f'<section><div class="zz-container"><p class="zz-eyebrow">Questions</p><h2 class="zz-h2">{heading}</h2>']
    for q, a in faqs:
        out.append(f'<details class="zz-faq-item"><summary class="zz-faq-q">{q}</summary><div class="zz-faq-a"><p>{a}</p></div></details>')
    out.append('</div></section>')
    return "\n".join(out)

def write_page(path, title, desc, body, crumbs, faqs=None, area=None, recaptcha=False, cta_place=None, trackc=False, checker=False, meta_title=None, meta_desc=None, service=False):
    """path like '/deadlines/' -> deadlines/index.html ; '/' -> index.html ; '/404.html' special.
    checker=True inserts the zone-checker widget right after this page's own
    </header> — home page only, mirrors zone-zero-checker-api's patch().
    meta_title/meta_desc override only the visible <title>/meta tags, letting
    the structured-data name/description stay pinned to title/desc — needed
    where the served page's head tags and its ld+json were hand-edited apart."""
    ld = base_ld(title, desc, path, crumbs, faqs, area, service=service or path == "/request-inspection/")
    depth = 0 if path in ("/", "/404.html") else 1
    if checker:
        if body.count("</header>") != 1:
            raise ValueError(f"checker=True on {path} expected exactly one </header> in body, found {body.count('</header>')}")
        body = body.replace("</header>", "</header>\n" + checker_section(), 1)
    html = head(title, desc, path, ld, recaptcha, depth, checker, meta_title, meta_desc) + nav() + body
    if faqs:
        html += faq_html(faqs, f"Quick answers")
    if cta_place is not None:
        html += cta(cta_place, trackc)
    html += footer(checker)
    if path == "/":
        fp = os.path.join(OUT, "index.html")
    elif path == "/404.html":
        fp = os.path.join(OUT, "404.html")
    else:
        d = os.path.join(OUT, path.strip("/"))
        os.makedirs(d, exist_ok=True)
        fp = os.path.join(d, "index.html")
    with open(fp, "w") as f:
        f.write(html)
    print("wrote", fp)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import content_core, content_localities
    content_core.build(write_page)
    content_localities.build(write_page)
    print("done")
