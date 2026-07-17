# zonezeroventura.com — Site Changelog

## 2026-07-17 — Full 22-page reconstruction build (original 2026-07-12 build files lost; zips never downloaded)

**Context:** Rebuilt fresh from surviving spec: `claude/ventura-kickoff.md` (Ventura Pier Harbor identity, Chris-approved 2026-07-12), the FHSZ identification doc, and network-config's resolved research. Third site in the reconstruction sequence (after OC and Riverside). Home H1 built to the keyword+locality standard.

**New pages (22):**
- Core (12): /, /find-contractor/, /deadlines/, /regulations/, /fences/, /landscaping/, /home-hardening/, /fire-history/, /assistance/, /resources/, /privacy/, /404.html
- Mountain Fire anchor (1): camarillo (2024 event: 19,904 ac, 243 structures, 83+ Camarillo Heights homes)
- Thomas Fire anchor (4): ventura (independent Ventura City Fire Dept + own FHSZ mapping, 500+ residences one night), ojai (VH acreage tripled per The Acorn), santa-paula (tier honestly caveated), fillmore (VCFPD Station 27, tier honestly caveated)
- Ojai Valley cluster (2): meiners-oaks, oak-view
- Also Confirmed VH, no anchor fire, no acreage figures (3): moorpark, simi-valley, thousand-oaks (no Woolsey claims per [reconfirm])

**New assets:**
- /css/site.css — Ventura Pier Harbor stylesheet: cream-dominant harbor-line hero (pier pilings + waves), piling-marker stat panel on waterline rule, 4-group harbor-map hub, "Two Fires, One County" dark section with paired fire cards, Domine + Mulish
- /js/site.js — shared scenario 5600808 webhook (real URL), reCAPTCHA v3, _event_id CAPI dedup, GA4 + Meta Lead events
- /sitemap.xml (21 URLs), /_redirects, staging robots.txt + robots-production.txt
- /_build/ — generators kept in-repo for disaster recovery

**Scripts / webhooks:**
- Webhook: https://hook.us2.make.com/mi0lks6grssbjq9hopp9pd0tdudexfgo, _site=zonezeroventura.com
- GA4 G-X43DDVCW9W, Meta Pixel 838658782511294 (per claude/network-tracking-ids.md)
- Phone (805) 567-8416 site-wide

**Verification (grep sweep, all passed):** 0 em dashes · triplet on all 22 · 0 "Find a Contractor" visible · 0 persona names · 1 H1/page · @graph everywhere · SPLIT-ANCHOR VERIFIED: 0 Thomas mentions on Camarillo, 0 Mountain mentions on the Thomas cluster (Moorpark's Mountain mention is the explicit non-borrowing disclaimer) · 0 Woolsey/borrowed fires · 0 acreage figures on Moorpark/Simi/Thousand Oaks per [reconfirm] · county stats parcel-basis only (59,000/86,000, +108%), 0 acreage-basis figures · Santa Paula/Fillmore tier explicitly not asserted · no Oxnard/Port Hueneme pages per anti-doorway exclusion

**Pending from this session:**
- Chris visual review; iterate on screenshots
- Netlify: link crgallego/zonezeroventura to site 96cc07e6-4299-4c9c-8172-cf03a82feb83 (Chris, ~1 min)
- Meta CAPI branch for pixel 838658782511294 in scenario 5600808 module 14
- robots.txt → production swap at launch; DNS (Chris)
- Optional future pass: verify Woolsey Fire reach into Thousand Oaks for a stronger anchor (per kickoff note; NOT asserted this build)
