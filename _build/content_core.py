# -*- coding: utf-8 -*-
"""Core page content for zonezeroventura.com. Hand-authored copy.
Binding rules: no em dashes; terminology triplet per page; local-first AHJ framing;
'Connect with a Licensed Contractor' never 'Find a Contractor' as visible copy.
Ventura throughlines: split-anchor doctrine (Mountain Fire 2024 = Camarillo only;
Thomas Fire 2017 = Ventura/Ojai/Santa Paula/Fillmore + Ojai Valley cluster);
City of Ventura has its OWN fire department and FHSZ mapping, distinct from VCFD;
county stats use the PARCEL basis only (59,000 of 86,000 parcels, 108% increase
vs 2010), never mixed with acreage-basis figures."""

PHONE_TEL = "+18055678416"
PHONE = "(805) 567-8416"

HARBOR_SVG = """<svg class="zz-hero-harbor" viewBox="0 0 1200 190" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<line x1="0" y1="120" x2="1200" y2="120" stroke="#1B4B4A" stroke-width="2" opacity="0.35"/>
<g fill="#7A6F63" opacity="0.55">
<rect x="120" y="96" width="9" height="70" rx="2"/><rect x="150" y="88" width="9" height="78" rx="2"/><rect x="180" y="100" width="9" height="66" rx="2"/>
<rect x="940" y="92" width="9" height="74" rx="2"/><rect x="970" y="102" width="9" height="64" rx="2"/><rect x="1000" y="94" width="9" height="72" rx="2"/>
</g>
<path d="M0,150 Q60,142 120,150 T240,150 T360,150 T480,150 T600,150 T720,150 T840,150 T960,150 T1080,150 T1200,150" stroke="#C9A66B" stroke-width="3" fill="none" opacity="0.7"/>
<path d="M0,168 Q60,161 120,168 T240,168 T360,168 T480,168 T600,168 T720,168 T840,168 T960,168 T1080,168 T1200,168" stroke="#1B4B4A" stroke-width="2" fill="none" opacity="0.3"/>
<path d="M0,182 Q60,176 120,182 T240,182 T360,182 T480,182 T600,182 T720,182 T840,182 T960,182 T1080,182 T1200,182" stroke="#C9A66B" stroke-width="2" fill="none" opacity="0.35"/>
</svg>"""

ZONE_DIAGRAM = """<figure class="zz-figure"><svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram of the 0 to 5 foot ember-resistant zone around a home">
<rect x="0" y="0" width="700" height="260" fill="#FFFDF7"/>
<rect x="40" y="200" width="620" height="20" fill="#E2D8C4"/>
<rect x="120" y="205" width="460" height="12" fill="#C9A66B" opacity="0.9"/>
<rect x="250" y="90" width="200" height="115" fill="#1B4B4A"/>
<polygon points="240,90 350,40 460,90" fill="#0F2E2E"/>
<rect x="330" y="140" width="40" height="65" fill="#C9A66B"/>
<line x1="120" y1="235" x2="250" y2="235" stroke="#7A5E2A" stroke-width="2"/>
<line x1="450" y1="235" x2="580" y2="235" stroke="#7A5E2A" stroke-width="2"/>
<text x="150" y="252" font-family="Mulish" font-size="13" fill="#23302E">0 to 5 ft: Zone 0</text>
<text x="470" y="252" font-family="Mulish" font-size="13" fill="#23302E">0 to 5 ft: Zone 0</text>
<text x="255" y="30" font-family="Mulish" font-size="13" fill="#23302E">The ember-resistant zone wraps the entire structure</text>
</svg><figcaption>Zone 0 is the first 5 feet out from every wall, deck, and attached structure. Under the April 2026 Board of Forestry draft, this ring must be kept free of combustible material.</figcaption></figure>"""

def build(write_page):
    # ---------------- HOME ----------------
    home_faqs = [
        ("Does Zone Zero apply to my Ventura County home?",
         "If your parcel sits in a Very High Fire Hazard Severity Zone, yes. The 2025 remap put roughly 59,000 of Ventura County's 86,000 mapped parcels in Very High, a 108% increase over 2010, spanning the Ojai Valley, the Camarillo hills, the City of Ventura's hillsides, and the eastern cities. Check your specific parcel rather than assuming."),
        ("Who enforces Zone 0 rules in Ventura County?",
         "Two different authorities, and the difference matters. The Ventura County Fire Department (VCFD) serves the contract cities (Camarillo, Ojai, Moorpark, Simi Valley, Thousand Oaks, Santa Paula) and unincorporated communities. The City of Ventura runs its own independent Ventura City Fire Department with its own hazard-mapping process."),
        ("When do I actually have to comply?",
         "Final state regulations are expected in late 2026. Existing homes get a phased runway, with Phase 1 estimated for 2027 to 2028 and Phase 2 set by your local authority, up to five years out. Two rules land immediately upon adoption: the combustible-fence restriction and requirements for new construction."),
    ]
    home_body = f"""<header class="zz-hero"><div class="zz-container"><div class="zz-hero-inner">
<h1>Zone Zero Requirements in <em>Ventura County</em></h1>
<p class="zz-hero-sub"><b>Two fires wrote this county's modern hazard map, and the 2025 remap more than doubled the parcels it covers.</b> Zone Zero (officially "Zone 0") is the ember-resistant zone: the first 5 feet around your home. Here's where it applies, which of the county's two fire authorities enforces it for you, and what your community's real story is.</p>
<div class="zz-hero-btns">
<a href="/find-contractor/" class="zz-btn zz-btn-sand">Get a free Zone 0 assessment</a>
<a href="/regulations/" class="zz-btn zz-btn-ghost">Read the requirements</a>
</div>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> California's Zone Zero law (AB 3074) requires an ember-resistant zone in the first 0 to 5 feet around homes in Very High Fire Hazard Severity Zones. The 2025 remap placed roughly 59,000 of Ventura County's 86,000 mapped parcels in Very High, a 108% increase over 2010. Enforcement runs through the Ventura County Fire Department for most cities, or the independent Ventura City Fire Department inside the City of Ventura. Final regulations are expected in late 2026, with phased deadlines from roughly 2027 to 2028.</div></div>
<div class="zz-trust"><div class="zz-container"><div class="zz-trust-grid">
<div class="zz-trust-item"><b>AB 3074</b><span>State law since 2020</span></div>
<div class="zz-trust-item"><b>59,000 parcels</b><span>of 86,000 mapped Very High in 2025</span></div>
<div class="zz-trust-item"><b>+108%</b><span>increase in Very High parcels vs. 2010</span></div>
<div class="zz-trust-item"><b>100% free</b><span>Assessments, no obligation</span></div>
</div></div></div>
<section class="zz-dark"><div class="zz-container">
<p class="zz-eyebrow">The county's record</p>
<h2 class="zz-h2">Two fires, one county</h2>
<p>Ventura County's hazard map isn't theoretical. It was written twice in seven years, in two different places, and this site keeps each story where it belongs.</p>
<div class="zz-twofires">
<div class="zz-fire-card">
<div class="zz-fire-year">November 2024</div>
<h3>The Mountain Fire</h3>
<p>19,904 acres. 243 structures destroyed, 127 damaged, at least 83 of those homes in Camarillo Heights. A rekindled brush-clearing fire, driven back to life by Santa Ana winds, put roughly 14,000 residents under evacuation notices within a day.</p>
<p><a href="/camarillo/">Camarillo's page</a> carries this story.</p>
</div>
<div class="zz-fire-card">
<div class="zz-fire-year">December 2017 to January 2018</div>
<h3>The Thomas Fire</h3>
<p>281,893 acres across Ventura and Santa Barbara counties, the largest California wildfire on record at the time. 1,063 structures destroyed, more than 500 Ventura residences in a single night, agricultural losses over $171 million.</p>
<p><a href="/ventura/">Ventura</a>, <a href="/ojai/">Ojai</a>, <a href="/santa-paula/">Santa Paula</a>, and <a href="/fillmore/">Fillmore</a> carry this one.</p>
</div>
</div>
</div></section>
<section><div class="zz-container">
<p class="zz-eyebrow">The harbor map</p>
<h2 class="zz-h2">Every community, grouped by its real story</h2>
<div class="zz-group-head"><span class="zz-dot zz-dot-mountain"></span>The Mountain Fire (2024)</div>
<p class="zz-group-note">The county's newest anchor event, and the reason Camarillo's hillsides read differently now.</p>
<div class="zz-chip-row">
<a class="zz-chip" href="/camarillo/">Camarillo</a>
</div>
<div class="zz-group-head"><span class="zz-dot zz-dot-thomas"></span>The Thomas Fire (2017)</div>
<p class="zz-group-note">The communities the largest fire in then-state history hit hardest, from the coast to the Santa Clara River valley.</p>
<div class="zz-chip-row">
<a class="zz-chip" href="/ventura/">City of Ventura</a>
<a class="zz-chip" href="/ojai/">Ojai</a>
<a class="zz-chip" href="/santa-paula/">Santa Paula</a>
<a class="zz-chip" href="/fillmore/">Fillmore</a>
</div>
<div class="zz-group-head"><span class="zz-dot zz-dot-valley"></span>The Ojai Valley</div>
<p class="zz-group-note">Unincorporated communities inside the valley's confirmed Very High zone, under the Ventura County Fire Department.</p>
<div class="zz-chip-row">
<a class="zz-chip" href="/meiners-oaks/">Meiners Oaks</a>
<a class="zz-chip" href="/oak-view/">Oak View</a>
</div>
<div class="zz-group-head"><span class="zz-dot zz-dot-vh"></span>Also Confirmed Very High</div>
<p class="zz-group-note">Eastern cities with real, current designations and significant 2025-remap footprints, each told without an invented fire story.</p>
<div class="zz-chip-row">
<a class="zz-chip" href="/moorpark/">Moorpark</a>
<a class="zz-chip" href="/simi-valley/">Simi Valley</a>
<a class="zz-chip" href="/thousand-oaks/">Thousand Oaks</a>
</div>
</div></section>
<section><div class="zz-container">
<p class="zz-eyebrow">What must I do?</p>
<h2 class="zz-h2">Zone 0: the first five feet</h2>
{ZONE_DIAGRAM}
<p><b>The rule is simple to state and hard to retrofit:</b> nothing combustible in the first 5 feet from any structure. Combustible fences and gates touching the house, bark mulch against the foundation, woody shrubs under windows, firewood on the deck. The Thomas and Mountain fires were both ember-driven events; Zone 0 removes the fuel where embers land. <a href="/regulations/">Read the full requirements</a>, or start with the two most common projects: <a href="/fences/">fences and gates</a> and <a href="/landscaping/">landscaping</a>.</p>
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">Who enforces it?</p>
<h2 class="zz-h2">Two fire authorities, one county</h2>
<p><b>Most of the county answers to the Ventura County Fire Department (VCFD):</b> the contract cities of Camarillo, Ojai, Moorpark, Simi Valley, Thousand Oaks, and Santa Paula, plus the unincorporated communities including Meiners Oaks and Oak View. Fillmore is served by the county fire protection district's Station 27, the same VCFD family.</p>
<p><b>The City of Ventura is the exception:</b> it runs its own independent Ventura City Fire Department and its own hazard-mapping process. If you're inside city limits, your requirements and schedule come from the city, not the county. Each community page names its authority. Enforcement under the April 2026 draft is education-first: inspections and correction notices before penalties.</p>
</div></section>
"""
    write_page("/", "Zone Zero Ventura County | Zone 0 Ember-Resistant Requirements, Community by Community",
               "Zone Zero (Zone 0) requirements for Ventura County: the Mountain Fire and Thomas Fire communities, the Ojai Valley, and the eastern Very High cities, with the county's two fire authorities explained.",
               home_body, [("Home", "/")], home_faqs, "Ventura County, California", cta_place="your Ventura County property", checker=True)

    # ---------------- FIND CONTRACTOR ----------------
    fc_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Connect with a Licensed Contractor</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Get a free Zone 0 assessment for your <em>Ventura County</em> home</h1>
<p class="zz-hero-sub">Tell us where your property is. A licensed professional reviews your parcel's hazard designation, walks the ember-resistant zone requirements that apply, and gives you a straight answer on what needs to change. Free, no obligation.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Zone Zero work in the 0 to 5 foot ember-resistant zone often involves fencing, gates, hardscape, and vegetation changes. Fence and gate work in California requires a CSLB-licensed contractor (Class C-13 for fencing). The assessment below is free and connects you with licensed professionals who work in Ventura County, from the Ojai Valley to the Conejo Valley.</div></div>
<section><div class="zz-container" style="display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:start" id="zz-fc-grid">
<div>
<h2 class="zz-h2">What happens after you submit</h2>
<p><b>1. We check your parcel.</b> Your address is matched against CAL FIRE's 2025 Fire Hazard Severity Zone maps and your community's adopted local map. With 59,000 of the county's 86,000 mapped parcels now Very High, the answer is yes more often than most homeowners expect, and a parcel-level check beats a guess.</p>
<p><b>2. You get a plain-English rundown.</b> Which tier you're in, which Zone 0 requirements apply, what your fire authority (VCFD or the Ventura City Fire Department) will look for, and what the phased deadlines mean for you.</p>
<p><b>3. If work is needed, you're connected with a licensed contractor.</b> Fence and gate replacement in the 0 to 5 foot zone is the most common project. All referrals are CSLB-licensed. You choose who you hire, always.</p>
<p>Prefer to talk it through? Call <a href="tel:{PHONE_TEL}"><b>{PHONE}</b></a>
          <span class="zz-phone-disclosure">Calls are answered by an automated AI assistant and may be recorded and transcribed.</span>.</p>
</div>
<form id="zz-find-contractor" class="zz-form" data-webhook="" novalidate>
<h2 class="zz-h3" style="font-size:22px">Request my free assessment</h2>
<label for="first_name">First name</label>
<input id="first_name" name="first_name" type="text" autocomplete="given-name" required>
<label for="last_name">Last name</label>
<input id="last_name" name="last_name" type="text" autocomplete="family-name" required>
<label for="email">Email</label>
<input id="email" name="email" type="email" autocomplete="email" required>
<label for="phone">Phone</label>
<input id="phone" name="phone" type="tel" autocomplete="tel">
<label for="address">Property address</label>
<input id="address" name="address" type="text" autocomplete="street-address" required>
<label for="city">City or community</label>
<input id="city" name="city" type="text" autocomplete="address-level2" required>
<label for="message">Anything specific you want checked? (optional)</label>
<textarea id="message" name="message" rows="3"></textarea>
<label class="zz-consent">
<input type="checkbox" name="consent" required>
<span><strong>Yes — connect me with a contractor.</strong> I am asking Zone Zero Property Inspections to share my name, phone number, email address, and property address with an independent CSLB-licensed contractor so that contractor can contact me about a Zone 0 assessment. I agree that contractor and Zone Zero Property Inspections may call or text me at the number I provided, including using an automated dialing system or an artificial, prerecorded, or AI voice. <strong>I am not required to agree to this in order to use this site or its information, and agreeing is not a condition of purchasing anything.</strong> Message and data rates may apply. See our <a href="/privacy/">Privacy Policy</a>.</span>
</label>
<button type="submit">Request my free assessment</button>
<p class="zz-form-note">Your request goes to our team for review.</p>
<p class="zz-form-status" role="status"></p>
<p class="zz-disclosure">Disclosure: this network's operator also owns a fence contracting company, and fence inquiries may be referred to it. You are never obligated to use it, and you're free to choose any licensed contractor. This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy">Privacy Policy</a> and <a href="https://policies.google.com/terms">Terms of Service</a> apply.</p>
</form>
</div></section>
<style>@media (max-width:767px){{#zz-fc-grid{{grid-template-columns:1fr !important}}}}</style>
"""
    write_page("/find-contractor/", "Free Zone 0 Assessment | Connect with a Licensed Contractor | Zone Zero Ventura",
               "Free Zone Zero assessment for Ventura County homes. Parcel hazard check, ember-resistant zone requirements, and connections to CSLB-licensed contractors.",
               fc_body, [("Home", "/"), ("Connect with a Licensed Contractor", "/find-contractor/")],
               recaptcha=True, cta_place=None)

    # ---------------- DEADLINES ----------------
    dl_faqs = [
        ("What is the actual Zone Zero deadline for existing Ventura County homes?",
         "There is no single date yet. Final state regulations are expected in late 2026. Phase 1 for existing homes is currently estimated for 2027 to 2028, and Phase 2 is set by your local fire authority, which can extend up to five years. In this county that means VCFD's adopted schedule for most cities, or the City of Ventura's own schedule inside city limits."),
        ("Which requirements take effect immediately?",
         "Two, upon adoption of the final regulations: the restriction on combustible fences attached to structures, and Zone 0 requirements for new construction. If you're building or replacing a fence in a Very High zone, plan for the ember-resistant standard now."),
        ("Does the City of Ventura follow the county's schedule?",
         "Not automatically. The city runs its own independent fire department and its own hazard-mapping process, so its adopted Zone 0 schedule can differ from VCFD's. Inside city limits, the city's timeline controls."),
    ]
    dl_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Deadlines</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Zone Zero deadlines: what's set, what's estimated, and <em>who decides</em></h1>
<p class="zz-hero-sub">The compliance timeline for the ember-resistant zone runs in phases, and in Ventura County one of two fire authorities controls your specifics.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Final Zone 0 regulations are expected in late 2026. New construction and the combustible-fence restriction take effect immediately upon adoption. Existing homes follow: Phase 1 is estimated for 2027 to 2028, and Phase 2 is set by your local Authority Having Jurisdiction, up to five years out. In Ventura County that authority is the Ventura County Fire Department, or the Ventura City Fire Department inside the City of Ventura.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">The timeline</p>
<h2 class="zz-h2">Phased compliance under the April 2026 draft</h2>
<figure class="zz-figure"><svg viewBox="0 0 720 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Zone 0 compliance timeline from 2026 through roughly 2031">
<line x1="40" y1="95" x2="690" y2="95" stroke="#23302E" stroke-width="2"/>
<circle cx="90" cy="95" r="8" fill="#BF0A30"/>
<text x="90" y="65" text-anchor="middle" font-family="Mulish" font-size="13" font-weight="700" fill="#1B4B4A">Late 2026</text>
<text x="90" y="130" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">Final regs adopted;</text>
<text x="90" y="145" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">fences + new builds</text>
<text x="90" y="160" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">immediate</text>
<circle cx="300" cy="95" r="8" fill="#C9A66B"/>
<text x="300" y="65" text-anchor="middle" font-family="Mulish" font-size="13" font-weight="700" fill="#1B4B4A">2027 to 2028 (est.)</text>
<text x="300" y="130" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">Phase 1:</text>
<text x="300" y="145" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">existing homes begin</text>
<circle cx="520" cy="95" r="8" fill="#83460D"/>
<text x="520" y="65" text-anchor="middle" font-family="Mulish" font-size="13" font-weight="700" fill="#1B4B4A">Up to +5 years</text>
<text x="520" y="130" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">Phase 2: schedule set</text>
<text x="520" y="145" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">by your local authority</text>
<circle cx="665" cy="95" r="6" fill="#1B4B4A"/>
<text x="665" y="130" text-anchor="middle" font-family="Mulish" font-size="11.5" fill="#23302E">Full compliance</text>
</svg><figcaption>Dates beyond adoption are estimates from the April 17, 2026 Board of Forestry draft and are subject to change. Your jurisdiction sets the specifics.</figcaption></figure>
<table class="zz-timeline">
<tr><th>Requirement</th><th>Status</th><th>Applies</th></tr>
<tr><td>Zone 0 for new construction</td><td><span class="zz-badge zz-badge-imm">Immediate</span></td><td>Upon adoption of final regulations, expected late 2026</td></tr>
<tr><td>Combustible fence restriction (attached to structures)</td><td><span class="zz-badge zz-badge-imm">Immediate</span></td><td>Upon adoption; plan replacements to the ember-resistant standard now</td></tr>
<tr><td>Existing homes, first wave</td><td><span class="zz-badge zz-badge-p1">Phase 1</span></td><td>Estimated 2027 to 2028</td></tr>
<tr><td>Existing homes, local schedule</td><td><span class="zz-badge zz-badge-p2">Phase 2</span></td><td>Set by your AHJ, up to 5 years after adoption</td></tr>
<tr><td>Voluntary early compliance</td><td><span class="zz-badge zz-badge-bp">Best practice</span></td><td>Any time; the county's two anchor fires were both wind-driven ember events</td></tr>
</table>
<p style="margin-top:22px"><b>Your jurisdiction sets the specifics.</b> VCFD's adopted schedule covers the contract cities and unincorporated communities; the City of Ventura's own department sets the schedule inside city limits. With the 2025 remap placing 59,000 of 86,000 mapped parcels in Very High, confirm your parcel's tier first, then track your authority's adoption.</p>
</div></section>
"""
    write_page("/deadlines/", "Zone Zero Deadlines for Ventura County | Phase 1, Phase 2 &amp; Immediate Requirements",
               "Zone 0 compliance timeline for Ventura County: what takes effect immediately, Phase 1 estimates for 2027 to 2028, and how VCFD and the Ventura City Fire Department set Phase 2.",
               dl_body, [("Home", "/"), ("Deadlines", "/deadlines/")], dl_faqs,
               "Ventura County, California", cta_place="your property")

    # ---------------- REGULATIONS ----------------
    reg_faqs = [
        ("What laws actually create Zone Zero?",
         "AB 3074 (2020) created the ember-resistant zone requirement in state law. SB 504 (2024) and AB 1455 (2025) refined the framework, and the Board of Forestry's April 17, 2026 draft is the most current regulatory text. Final regulations are expected in late 2026."),
        ("Is Zone 0 the same thing as defensible space?",
         "Zone 0 is the newest and strictest part of defensible space. California already required Zones 1 and 2 (5 to 30 feet, and 30 to 100 feet). Zone Zero adds the 0 to 5 foot ember-resistant ring, because post-fire research shows embers igniting material right against the structure is how most homes are lost. The Thomas Fire's single-night destruction of 500+ Ventura residences is the local case study."),
        ("What happens if I don't comply?",
         "Under the April 2026 draft, enforcement is education-first: your fire authority inspects, notifies, and works with you on corrections before penalties come into play. In this county that's VCFD or, inside the City of Ventura, the city's own department."),
    ]
    reg_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Regulations</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>The Zone Zero regulations, translated into <em>plain English</em></h1>
<p class="zz-hero-sub">What AB 3074 and the April 2026 Board of Forestry draft actually require in the ember-resistant zone, and how Ventura County's two fire authorities apply it.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> AB 3074 requires an ember-resistant zone (Zone 0) in the first 0 to 5 feet around structures in Very High Fire Hazard Severity Zones. The April 17, 2026 Board of Forestry draft is the current text: no combustible materials in that ring, with immediate rules for new construction and attached combustible fences, and phased deadlines for existing homes enforced by your local fire authority.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">The framework</p>
<h2 class="zz-h2">Three laws, one draft, and your local enforcer</h2>
<p><b>AB 3074 (2020)</b> created Zone 0 in statute, using the term "ember-resistant zone." <b>SB 504 (2024)</b> and <b>AB 1455 (2025)</b> refined how it's implemented and funded. The <b>April 17, 2026 Board of Forestry draft</b> is the most current regulatory language, and final regulations are expected in late 2026.</p>
<p><b>Then it goes local, and Ventura County goes local twice.</b> The Ventura County Fire Department applies the framework for the contract cities and unincorporated communities; the City of Ventura's independent department applies it inside city limits, on the city's own mapping. Local adoption also matters for vegetation: the state draft scaled back blanket tree restrictions after widespread public concern, and local rules may allow well-maintained trees. In the oak-shaded Ojai Valley especially, verify with your own authority before removing anything.</p>
{ZONE_DIAGRAM}
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">In the zone</p>
<h2 class="zz-h2">What Zone 0 restricts in the first five feet</h2>
<ul class="zz-list">
<li><b>Combustible fencing and gates</b> attached to or within 5 feet of the structure. This is the immediate-effect item and the most common retrofit. <a href="/fences/">See the fences guide.</a></li>
<li><b>Combustible mulch</b> such as bark and wood chips against the foundation. Hardscape, gravel, and stone are the replacements. <a href="/landscaping/">See the landscaping guide.</a></li>
<li><b>Woody shrubs and flammable plantings</b> under eaves and windows.</li>
<li><b>Stored combustibles:</b> firewood, lumber, trash bins, and furniture cushions in the ring.</li>
<li><b>Attachments matter too:</b> decks, stairs, and trellises within the zone face material requirements. <a href="/home-hardening/">See home hardening.</a></li>
</ul>
<p>The science behind the rule comes from IBHS ember research: wind-driven embers, not the flame front, ignite most homes. Both of this county's anchor fires, the Thomas Fire and the Mountain Fire, were Santa Ana wind events that proved the point locally.</p>
</div></section>
"""
    write_page("/regulations/", "Zone Zero Regulations Explained | AB 3074 &amp; the 2026 Draft | Zone Zero Ventura",
               "Plain-English guide to Zone 0 regulations for Ventura County: AB 3074, SB 504, AB 1455, the April 2026 Board of Forestry draft, and how VCFD and the Ventura City Fire Department enforce the ember-resistant zone.",
               reg_body, [("Home", "/"), ("Regulations", "/regulations/")], reg_faqs,
               "Ventura County, California", cta_place="your property")

    # ---------------- FENCES ----------------
    fence_faqs = [
        ("Do I have to replace my whole fence?",
         "Usually no. The requirement targets the portion attached to or within 5 feet of the structure. Many homeowners replace the last section with a noncombustible panel or gate and keep the rest. An assessment tells you exactly how much of your run is affected."),
        ("What fence materials count as ember-resistant?",
         "Noncombustible materials: steel, aluminum, masonry, and certain composites rated for the application. Standard wood fencing attached to the house is exactly what the immediate-effect restriction targets."),
        ("Who can legally do fence work in California?",
         "A CSLB-licensed contractor. Fencing is Class C-13. Any referral through this site is licensed, and the free assessment is how to start."),
    ]
    fence_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Fences &amp; Gates</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Your fence is the <em>first thing</em> the new rules touch</h1>
<p class="zz-hero-sub">The combustible-fence restriction takes effect immediately when final Zone Zero regulations are adopted. Here's what that means for Ventura County fence lines, from hillside neighborhoods to valley ranchettes.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Under the April 2026 draft, combustible fences attached to structures in Very High hazard zones are restricted immediately upon adoption of the final Zone 0 regulations, expected late 2026. The fix is a noncombustible section or gate in the first 5 feet of the ember-resistant zone. Fence work in California requires a CSLB Class C-13 licensed contractor.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">Why fences first</p>
<h2 class="zz-h2">A wood fence is a fuse connected to your house</h2>
<p><b>Ember research shows the mechanism plainly:</b> embers land in a wood fence line, the fence ignites, and the flame walks the fence straight to the wall. In the neighborhoods the Thomas Fire burned through in a single December night, and in Camarillo Heights during the Mountain Fire, house-to-house spread through connected fuels was part of how the losses compounded. That's why the fence rule is one of only two provisions that take effect immediately, alongside new construction.</p>
<p><b>The common retrofit is smaller than people fear.</b> Replace the final 5 feet where the fence meets the structure with a noncombustible panel or metal gate, and the rest of the run can stay. Hillside parcels in Ventura and Ojai often have the added wrinkle of fencing that steps down a slope toward wildland; the assessment maps which sections actually sit in the zone.</p>
<p>Costs vary by material and run length, and any quote should come from a licensed contractor after seeing the property. The <a href="/find-contractor/">free assessment</a> is the honest starting point: it tells you how many linear feet are actually in the zone before anyone talks price.</p>
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">Beyond the fence</p>
<h2 class="zz-h2">Gates, and what Zone 0 means for them</h2>
<p><b>Gates get the same treatment as fencing</b> where they sit in the ember-resistant zone: noncombustible materials in the first 5 feet. A metal pedestrian gate at the house corner is often the single cheapest compliance win on the property. Statewide fencing guidance lives at <a href="https://zonezerofences.com">zonezerofences.com</a>; this page covers how it lands in Ventura County.</p>
</div></section>
"""
    write_page("/fences/", "Zone Zero Fence &amp; Gate Requirements | Ventura County | Immediate-Effect Rules",
               "The combustible-fence restriction under Zone 0 takes effect immediately upon adoption. What Ventura County homeowners need to know about ember-resistant fencing, gates, and CSLB-licensed work.",
               fence_body, [("Home", "/"), ("Fences", "/fences/")], fence_faqs,
               "Ventura County, California", cta_place="your fence line")

    # ---------------- LANDSCAPING ----------------
    land_faqs = [
        ("Do I have to remove my trees?",
         "In most cases, no. The April 2026 draft scaled back blanket vegetation restrictions after widespread public concern about mature trees and shade, and local rules may allow well-maintained trees. In the oak-canopied Ojai Valley this distinction matters enormously. What Zone 0 clearly targets is combustible ground cover and shrubs in the first 5 feet. Verify specifics with your own fire authority before removing anything."),
        ("What replaces bark mulch in Zone 0?",
         "Noncombustible ground cover: gravel, decomposed granite, pavers, stone, and concrete. The 5-foot ring converts to hardscape without losing the planting design further out."),
        ("Does drought-tolerant automatically mean fire-safe?",
         "No. Some drought-tolerant plants are resinous and burn readily. In the ember-resistant zone the standard is noncombustible, not just low-water."),
    ]
    land_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Landscaping</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Zone 0 landscaping: what stays, what goes, and <em>what about the oaks</em></h1>
<p class="zz-hero-sub">The ember-resistant zone rewrites the first 5 feet of your yard. It does not require scorched-earth landscaping, and in a county of oak valleys, citrus country, and coastal hillsides, the honest version has range.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Zone Zero requires noncombustible ground cover in the 0 to 5 foot ember-resistant zone: no bark mulch, no woody shrubs against the wall. The April 2026 draft scaled back blanket vegetation rules amid concern over mature trees and shade, and local authorities may allow well-maintained trees. Your Ventura County fire authority sets the specifics.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">The redesign</p>
<h2 class="zz-h2">The five-foot ring, replanted</h2>
<p><b>Out:</b> bark and wood-chip mulch, juniper and other resinous shrubs, climbing vegetation on walls, and plantings under eaves and vents.</p>
<p><b>In:</b> gravel and decomposed granite, pavers and stone, low succulents in noncombustible beds where your authority allows plantings, and clean hardscape paths that double as access.</p>
<p><b>On trees, honestly:</b> homeowners across California pushed back on early drafts precisely because mature trees provide needed shade, and the state responded. The current draft is more permissive than the headlines suggested, and local rules may allow well-maintained trees near the home. In Ojai, Meiners Oaks, and Oak View, where the oak canopy is the valley's identity, do not preemptively remove a healthy tree; verify with the Ventura County Fire Department first. Inside the City of Ventura, ask the city's own department.</p>
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">Beyond five feet</p>
<h2 class="zz-h2">Where landscaping meets wildland</h2>
<p>On the hillsides above Ventura, along the Ojai Valley's edges, and on the Camarillo hills, Zone 0 is only the innermost ring: Zones 1 and 2 (5 to 30 and 30 to 100 feet) still govern the broader property. The <a href="/find-contractor/">free assessment</a> covers all three zones, so wildland-edge homeowners see the full picture, not just the first five feet.</p>
</div></section>
"""
    write_page("/landscaping/", "Zone Zero Landscaping Rules | Trees, Mulch &amp; the 5-Foot Ring | Ventura County",
               "Zone 0 landscaping for Ventura County: noncombustible ground cover in the ember-resistant zone, the truth about tree removal under the 2026 draft, and oak-valley considerations.",
               land_body, [("Home", "/"), ("Landscaping", "/landscaping/")], land_faqs,
               "Ventura County, California", cta_place="your yard")

    # ---------------- HOME HARDENING ----------------
    hh_faqs = [
        ("Is home hardening the same as Zone Zero?",
         "They're partners. Zone 0 removes fuel in the first 5 feet; home hardening upgrades the structure itself: vents, eaves, roofing, decks, and windows. IBHS research treats them as one system, because embers exploit whichever weakness exists."),
        ("What's the highest-value hardening upgrade?",
         "Ember-resistant vents are consistently the best cost-to-protection ratio. Embers entering attic and crawlspace vents ignite homes from the inside, and vent retrofits are far cheaper than roofing or window replacement."),
        ("Do hardening upgrades have deadlines like Zone 0?",
         "New construction in Very High zones already follows Chapter 7A building standards. For existing homes, most hardening beyond Zone 0 is best practice rather than mandate, which makes it the smart thing to do while retrofitting the ember-resistant zone anyway."),
    ]
    hh_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Home Hardening</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Zone 0 clears the fuel. <em>Hardening</em> closes the openings.</h1>
<p class="zz-hero-sub">The ember-resistant zone and home hardening are one system. Here's the structure side, prioritized by what actually saves homes in wind-driven ember events.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Home hardening upgrades the structure against embers: ember-resistant vents, enclosed eaves, Class A roofing, noncombustible gutters, and deck upgrades. Zone Zero handles the first 5 feet of ground; hardening handles the building. Together they address how homes were actually lost in the Thomas and Mountain fires: wind-driven embers finding fuel and openings.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">Priority order</p>
<h2 class="zz-h2">Hardening upgrades, ranked by protection per dollar</h2>
<ul class="zz-list">
<li><b>1. Ember-resistant vents.</b> The cheapest high-impact upgrade. Embers entering attic vents ignite homes from inside, which is how houses burn down hours after the front passes.</li>
<li><b>2. Gutter guards and debris control.</b> Leaf and needle litter in gutters is a rooftop fuel bed waiting for a Santa Ana night.</li>
<li><b>3. Enclosed or boxed eaves.</b> Open eaves trap rising embers against wood.</li>
<li><b>4. Deck surfaces and under-deck screening</b> where decks sit in or near the ember-resistant zone, a common hillside configuration above Ventura and in the Ojai Valley.</li>
<li><b>5. Class A roofing</b> at replacement time. If your roof is due anyway, this is when.</li>
<li><b>6. Dual-pane, tempered-glass windows</b> on exposures facing fuel.</li>
</ul>
<p>The Thomas Fire took more than 500 Ventura residences in one night; the Mountain Fire took at least 83 homes in Camarillo Heights in 2024. Hardening plus Zone 0 is what survivability looks like when the next wind event comes. The <a href="/find-contractor/">free assessment</a> covers both.</p>
</div></section>
"""
    write_page("/home-hardening/", "Home Hardening Guide | Vents, Eaves, Roofing &amp; Decks | Zone Zero Ventura",
               "Home hardening for Ventura County: the structure-side companion to Zone 0. Ember-resistant vents, eaves, Class A roofing, and deck upgrades, ranked by protection per dollar.",
               hh_body, [("Home", "/"), ("Home Hardening", "/home-hardening/")], hh_faqs,
               "Ventura County, California", cta_place="your home")

    # ---------------- FIRE HISTORY ----------------
    fh_faqs = [
        ("What are Ventura County's defining modern wildfires?",
         "Two, seven years apart. The Thomas Fire (December 2017 to January 2018): 281,893 acres across Ventura and Santa Barbara counties, 1,063 structures destroyed, more than 500 Ventura residences in a single night. And the Mountain Fire (November 2024): 19,904 acres, 243 structures destroyed, at least 83 homes in Camarillo Heights."),
        ("Why does this site assign each fire to specific cities?",
         "Because that's what happened. The Mountain Fire's losses centered on Camarillo; the Thomas Fire hit Ventura, Ojai, Santa Paula, and Fillmore. Borrowing a fire's story for a city it didn't burn would be exactly the kind of interchangeable content this network refuses to publish."),
        ("How much did the 2025 remap change Ventura County?",
         "Substantially: roughly 59,000 of the county's 86,000 mapped parcels are now Very High, a 108% increase over 2010. Two major fires in seven years reshaped how the modeling reads this county."),
    ]
    fh_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Fire History</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Ventura County's fire record: <em>two fires, seven years apart</em></h1>
<p class="zz-hero-sub">The Thomas Fire rewrote the coast and the valleys in 2017. The Mountain Fire rewrote the Camarillo hills in 2024. Together they explain the 2025 map.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> The Thomas Fire (2017 to 2018) burned 281,893 acres, destroyed 1,063 structures, and took more than 500 Ventura residences in a single night; it remains the anchor event for Ventura, Ojai, Santa Paula, and Fillmore. The Mountain Fire (November 2024) burned 19,904 acres and destroyed 243 structures, at least 83 in Camarillo Heights. The 2025 remap that followed placed roughly 59,000 of the county's 86,000 mapped parcels in Very High, driving where Zone 0 (Zone Zero) applies.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">The record</p>
<h2 class="zz-h2">The numbers, kept where they belong</h2>
<div class="zz-pilings">
<div class="zz-piling-item"><div class="zz-piling-val">281,893 ac</div><div class="zz-piling-label">Thomas Fire, Dec 2017 to Jan 2018, then the largest wildfire in California history</div></div>
<div class="zz-piling-item"><div class="zz-piling-val">500+</div><div class="zz-piling-label">Ventura residences destroyed in a single night, of 1,063 structures lost overall</div></div>
<div class="zz-piling-item"><div class="zz-piling-val">19,904 ac</div><div class="zz-piling-label">Mountain Fire, November 2024, in the hills above Camarillo and Somis</div></div>
<div class="zz-piling-item"><div class="zz-piling-val">243</div><div class="zz-piling-label">structures destroyed in 2024, at least 83 of them homes in Camarillo Heights</div></div>
</div>
<p style="margin-top:22px"><b>The Thomas Fire</b> ignited December 4, 2017 and burned into January, crossing into Santa Barbara County and forcing a generation of coastal and valley residents through evacuation. Its worst single night belonged to the City of Ventura's hillside neighborhoods. Agricultural losses exceeded $171 million across citrus, avocado, and berry country. It is the shared anchor for <a href="/ventura/">Ventura</a>, <a href="/ojai/">Ojai</a>, <a href="/santa-paula/">Santa Paula</a>, and <a href="/fillmore/">Fillmore</a>, and by extension the <a href="/meiners-oaks/">Ojai Valley communities</a>.</p>
<p><b>The Mountain Fire</b> ignited November 6, 2024 near Balcom Canyon Road north of Somis: a brush-clearing fire believed extinguished, rekindled a week later by Santa Ana winds. Within a day roughly 14,000 residents were under evacuation notices, and by containment on November 27 it had destroyed 243 structures and damaged 127 more, with roughly 12,000 acres of avocado, citrus, and berry farmland affected and at least 10 people injured. Its story belongs to <a href="/camarillo/">Camarillo</a>, and this site keeps it there.</p>
<p><b>The 2025 remap read both events</b> and more than doubled the county's Very High parcel count versus 2010: roughly 59,000 of 86,000 mapped parcels. That's the map your obligations follow.</p>
</div></section>
"""
    write_page("/fire-history/", "Ventura County Fire History | The Thomas Fire &amp; the Mountain Fire",
               "Ventura County's fire record: the Thomas Fire (281,893 acres, 500+ Ventura homes in one night) and the Mountain Fire (2024, Camarillo Heights), and the 2025 remap they drove.",
               fh_body, [("Home", "/"), ("Fire History", "/fire-history/")], fh_faqs,
               "Ventura County, California", cta_place="your property")

    # ---------------- ASSISTANCE ----------------
    as_faqs = [
        ("Is there financial help for Zone Zero compliance?",
         "Programs exist and are growing as the deadlines approach. California has funded defensible-space and home-hardening grant pilots, and AB 1455 (2025) touches implementation funding. Availability is program-by-program and changes often, so verify current openings through the official resources on this page before planning around a grant."),
        ("Where should Ventura County homeowners start?",
         "With your fire authority: VCFD for most of the county, the Ventura City Fire Department inside city limits. Then CAL FIRE's grant channels at fire.ca.gov, and the county's fire-safe community organizations. The Thomas and Mountain fire recovery periods both built local support infrastructure worth asking about."),
        ("What if I can't afford compliance work right now?",
         "Start with the free assessment so you know your actual scope: many properties need less than feared, and the highest-impact items (clearing stored combustibles from the 5-foot ring, swapping mulch for gravel) cost little. Phased deadlines mean existing homes have runway, and education-first enforcement credits progress."),
    ]
    as_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Assistance</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Help paying for Zone 0 compliance <em>exists</em>. Here's how to find it.</h1>
<p class="zz-hero-sub">Grant channels, agency guidance, and low-cost first steps for Ventura County homeowners.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> Assistance for Zone Zero work comes through state grant channels, your fire authority's programs, and free assessments. Program availability changes frequently: verify current openings through official channels before planning around any grant.</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">Where to look</p>
<h2 class="zz-h2">Assistance channels, in order</h2>
<ul class="zz-list">
<li><b>Your fire authority first.</b> The Ventura County Fire Department serves the contract cities and unincorporated communities with defensible-space guidance; City of Ventura homeowners start with the city's own department.</li>
<li><b>State programs.</b> CAL FIRE administers defensible-space and home-hardening grant funding as it's appropriated. Check current cycles at fire.ca.gov.</li>
<li><b>Community fire-safe organizations.</b> The recovery periods after the Thomas and Mountain fires built local support networks; ask your fire authority what's currently active in your area.</li>
<li><b>The free assessment.</b> Knowing your real scope is itself financial protection: it stops you from over-buying work you don't need. <a href="/find-contractor/">Request one here.</a></li>
<li><b>Low-cost first moves.</b> Rehoming stored firewood beyond the 5-foot ring and swapping bark mulch for gravel are weekend projects that close the biggest ember pathways.</li>
</ul>
<p><b>A note on honesty:</b> we don't list specific dollar amounts or name grant programs we haven't verified as currently open, because funding cycles close. The <a href="/resources/">resources page</a> links the official sources that stay current.</p>
</div></section>
"""
    write_page("/assistance/", "Zone Zero Assistance Programs | Grants &amp; Support | Ventura County",
               "Financial assistance for Zone 0 compliance in Ventura County: fire authority programs, state grant channels, community organizations, and low-cost first steps.",
               as_body, [("Home", "/"), ("Assistance", "/assistance/")], as_faqs,
               "Ventura County, California", cta_place="your property")

    # ---------------- RESOURCES ----------------
    res_body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; Resources</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Official Zone Zero resources for <em>Ventura County</em></h1>
<p class="zz-hero-sub">The primary sources: statutes, hazard maps, both fire authorities, and ember science. When our pages and a fresh official source ever disagree, the official source wins.</p>
</div></div>{HARBOR_SVG}</header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> The authoritative sources on Zone 0 are the Board of Forestry (regulatory text), CAL FIRE (hazard maps and the ember-resistant zone FAQ), the Ventura County Fire Department and the Ventura City Fire Department (local enforcement), and IBHS (the ember research behind the rules).</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">Primary sources</p>
<h2 class="zz-h2">Where the rules actually live</h2>
<ul class="zz-list">
<li><b>Board of Forestry and Fire Protection</b> (bof.fire.ca.gov): the Zone 0 regulatory drafts, including the April 17, 2026 text.</li>
<li><b>CAL FIRE</b> (fire.ca.gov): Fire Hazard Severity Zone maps, the official Zone 0 FAQ, and defensible space guidance. The 2025 county remap lives here.</li>
<li><b>OSFM FHSZ viewer</b>: look up your exact parcel's tier, the decisive check in a county where 59,000 of 86,000 mapped parcels are now Very High.</li>
<li><b>Ventura County Fire Department</b> (vcfd.org): the AHJ for the contract cities and unincorporated communities.</li>
<li><b>Ventura City Fire Department</b>: the independent AHJ inside the City of Ventura, with the city's own hazard-mapping process.</li>
<li><b>IBHS</b> (ibhs.org): the ember-intrusion research underlying the ember-resistant zone standard.</li>
<li><b>Statewide context:</b> <a href="https://zonezerocalifornia.com">Zone Zero California</a>, the network's statewide guide and zone checker.</li>
</ul>
<p><b>Regulations move.</b> Final Zone Zero rules are expected in late 2026, and local adoptions continue. Anything time-sensitive on this site should be verified against these sources before you make decisions.</p>
</div></section>
"""
    write_page("/resources/", "Official Resources | Statutes, Maps &amp; Fire Authorities | Zone Zero Ventura",
               "Primary sources for Zone 0 in Ventura County: Board of Forestry drafts, CAL FIRE hazard maps, VCFD and the Ventura City Fire Department, and IBHS ember research.",
               res_body, [("Home", "/"), ("Resources", "/resources/")], None,
               "Ventura County, California", cta_place="your property")

    # ---------------- PRIVACY ----------------
    # Body, <title>, and meta description below reproduce the committed/served
    # privacy/index.html verbatim (authoritative text per the 2026-09-18 legal-copy
    # backport) rather than the generator's earlier "Effective July 2026" draft.
    # The structured-data name/description in base_ld() are intentionally left
    # pointing at the pre-hand-edit title/desc strings via meta_title/meta_desc
    # below, matching the served page's own ld+json, which was never re-run.
    priv_body = f"""<main>
<header class="zz-hero" style="padding:0">
  <div class="zz-container">
    <div class="zz-hero-inner" style="padding:56px 0">
      <span class="zz-eyebrow-light">Zone Zero Ventura County</span>
      <h1 class="zz-h1" style="font-size:clamp(30px,4vw,44px)">Privacy Policy</h1>
    </div>
  </div>
</header>
<section style="padding:72px 0">
  <div class="zz-container zz-prose" style="max-width:800px">
    <p><em>Effective date: August 21, 2026</em></p>
    <h2>Who we are</h2>
    <p>This site is operated by Zone Zero Property Inspections ("we," "us"). This policy describes what we collect on this site and how we use it.</p>
    <h2>What we collect</h2>
    <p>When you use our forms, compliance checker, or phone line, we may collect: your name, email address, phone number, property address or city, and information you provide about your property. Our phone line is answered by an automated AI assistant; calls may be recorded and transcribed. We also collect standard usage data through cookies and similar technologies, including via Google Analytics and the Meta (Facebook) pixel.</p>
    <h2>How we use it</h2>
    <p>We use this information to operate the site, respond to your requests, provide the compliance guide, and — when you ask us to — connect you with an independent CSLB-licensed local contractor for an assessment. We may receive compensation for those connections.</p>
    <h2>Who we share it with</h2>
    <p>If you request a contractor connection, we share your contact and property information with the contractor(s) who will follow up. We also use service providers (hosting, analytics, advertising, and workflow automation) that process data on our behalf. We do not sell your personal information to unrelated third parties.</p>
    <h2>Your choices</h2>
    <p>You can browse this site without submitting any personal information. You can control cookies through your browser settings. California residents may request access to or deletion of their personal information via the contact form on this site; we will respond as required by applicable law.</p>
    <h2>Do Not Track</h2>
    <p>This site does not currently respond to browser Do Not Track signals.</p>
    <h2>Changes</h2>
    <p>If we change this policy, we will post the updated version on this page with a new effective date.</p>
    <h2>Contact</h2>
    <p>Questions about this policy: use the contact form on this site.</p>
  </div>
</section>
</main>

"""
    write_page("/privacy/", "Privacy Policy | Zone Zero Ventura",
               "Privacy policy for zonezeroventura.com: what we collect through the assessment form and analytics, and how it's used.",
               priv_body, [("Home", "/"), ("Privacy", "/privacy/")], None, cta_place=None,
               meta_title="Privacy Policy | Zone Zero Ventura County",
               meta_desc="Privacy policy for Zone Zero Ventura County: what we collect, how we use it, and your choices.'s used.")

    # ---------------- 404 ----------------
    nf_body = f"""<section style="padding:100px 0"><div class="zz-container" style="text-align:center;max-width:640px">
<h1 class="zz-h2" style="font-size:44px">This page drifted off the pier</h1>
<p>The page you're looking for isn't here. Everything on Zone Zero, Zone 0, and the ember-resistant zone for Ventura County is still one click away.</p>
<p style="margin-top:26px"><a href="/" class="zz-btn zz-btn-sand">Back to the home page</a></p>
<p style="margin-top:18px"><a href="/regulations/">Regulations</a> &middot; <a href="/deadlines/">Deadlines</a> &middot; <a href="/find-contractor/">Connect with a Licensed Contractor</a></p>
</div></section>
"""
    write_page("/404.html", "Page Not Found | Zone Zero Ventura",
               "The page you're looking for isn't here. Find Zone Zero Ventura guides on regulations, deadlines, fences, and more.",
               nf_body, [("Home", "/")], None, cta_place=None)
