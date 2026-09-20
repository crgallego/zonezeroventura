# -*- coding: utf-8 -*-
"""Locality page content for zonezeroventura.com.
Split-anchor doctrine (binding, Chris 2026-07-12): Mountain Fire = Camarillo ONLY;
Thomas Fire = Ventura, Ojai, Santa Paula, Fillmore + Ojai Valley cluster.
Moorpark/Simi Valley/Thousand Oaks: NO anchor fire, NO Woolsey claims, NO acreage
figures ([reconfirm]). Santa Paula/Fillmore: tier honestly caveated, not asserted.
City of Ventura: independent Ventura City Fire Department, own FHSZ mapping."""

VCFD = ("Ventura County Fire Department",
        "The Ventura County Fire Department (VCFPD / VCFD) is the Authority Having Jurisdiction here. Inside VCFPD, 2025 VCWUIC section 604.8.2 Zone 0 is Required now for new buildings, additions, new landscape, and refurbished landscape, effective March 1, 2025. Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies.")

L = []

def loc(slug, name, kind, tier, ahj, ahj_note, intro, fire_h2, fire, snaps, faqs, hero_em):
    L.append(dict(slug=slug, name=name, kind=kind, tier=tier, ahj=ahj, ahj_note=ahj_note,
                  intro=intro, fire_h2=fire_h2, fire=fire, snaps=snaps, faqs=faqs,
                  hero_em=hero_em))

# ============ MOUNTAIN FIRE ANCHOR (1) ============

loc("camarillo", "Camarillo", "city", "Very High",
    *VCFD,
    "Camarillo's hazard story changed in November 2024, and everyone here knows it. The city carries a real, current Very High designation on its hillside edges, the Camarillo Heights neighborhood above the valley floor most of all, and the Mountain Fire is the reason the maps and the community now read those hills the same way. The first five feet is the highest-leverage prevention on mapped parcels. Required now versus Proposed — not in force versus Recommended now depends on the fire authority and the work.",
    "The Mountain Fire, November 2024",
    "It started as a brush-clearing fire near Balcom Canyon Road north of Somis, believed out. A week later, Santa Ana winds found what remained and rekindled it. Over three weeks (November 6 to 27, 2024) the Mountain Fire burned 19,904 acres, destroyed 243 structures and damaged 127 more, and at least 83 of the destroyed homes stood in Camarillo Heights. Roughly 14,000 residents were under evacuation notices within a day; roughly 12,000 acres of avocado, citrus, and berry farmland were affected; at least 10 people were injured. The fire's mechanics are Zone 0's entire argument: wind-driven embers finding connected fuel at the house line. This story belongs to Camarillo, and this site keeps it here.",
    [("Very High", "confirmed, current hillside designation"), ("2024", "the Mountain Fire, the county's newest anchor event"), ("83+", "Camarillo Heights homes among 243 structures destroyed"), ("VCFD", "Ventura County Fire Department, contract city")],
    [("Is Camarillo in a Very High fire hazard zone?",
      "Yes, on its hillside edges, with Camarillo Heights the clearest case. Our verified sources don't pin an exact citywide acreage figure, so we describe the designation rather than invent a number. Check your specific parcel."),
     ("What did the Mountain Fire change for Camarillo homeowners?",
      "Practically: the 2025 remap and local attention that followed. At least 83 Camarillo Heights homes were among the 243 structures destroyed in November 2024, and the ember-driven mechanics of that fire are exactly what the Zone 0 ember-resistant zone addresses."),
     ("Who enforces Zone Zero in Camarillo?",
      "The Ventura County Fire Department, serving the city under contract, is the Authority Having Jurisdiction. Statewide Zone 0 is Proposed — not in force; local required versus recommended rules are named on this page.")],
    "the city the Mountain Fire rewrote"),

# ============ THOMAS FIRE ANCHOR (4) ============

loc("ventura", "City of Ventura", "city", "Very High",
    "Ventura City Fire Department",
    "The City of Ventura runs its own independent Ventura City Fire Department, not VCFD, with its own hazard-mapping process confirmed through the city's public FAQ. Inside city limits, the city's adopted maps and schedule control.",
    "The City of Ventura, San Buenaventura on the county seal, is the county seat and this site's namesake city, and it carries the county's heaviest single memory of wildfire loss. Its hillside neighborhoods hold real, current Very High designations under the city's own mapping process, administered by the independent Ventura City Fire Department rather than the county. The first five feet is the highest-leverage prevention within those zones, and the city's 2017 experience is why it reads differently here than almost anywhere in California. Statewide Zone 0 is Proposed — not in force.",
    "The Thomas Fire's worst night",
    "On December 4, 2017 the Thomas Fire ignited and ran at the coast with Santa Ana winds behind it, and before the first night ended more than 500 Ventura residences were destroyed, most in the hillside neighborhoods above downtown. The fire would eventually burn 281,893 acres across two counties, destroy 1,063 structures, and stand for a time as the largest wildfire in California history, but for this city the defining fact is the speed: one night, one wind event, five hundred homes. Embers arriving ahead of the flame front ignited fuel at the house line, which is precisely the five feet Zone 0 governs.",
    [("Very High", "hillside designations under the city's own mapping"), ("500+", "residences destroyed in the Thomas Fire's first night"), ("Independent", "Ventura City Fire Department, not VCFD"), ("2017", "the anchor event this city measures from")],
    [("Who enforces Zone Zero in the City of Ventura?",
      "The Ventura City Fire Department, the city's own independent agency with its own hazard-mapping process. If you're inside city limits, your requirements and schedule come from the city, not the county."),
     ("Is the City of Ventura in a Very High fire hazard zone?",
      "Its hillside areas hold real, current Very High designations under the city's own mapping. The city spans flat coastal neighborhoods outside the zones and hillside streets inside them, so check your specific parcel."),
     ("Why is the Thomas Fire so central to this city's page?",
      "Because more than 500 Ventura residences were destroyed in the fire's first night in December 2017, most in hillside neighborhoods. It remains the county's clearest local demonstration of ember-driven loss, the exact mechanism Zone 0 exists to interrupt.")],
    "one night in 2017, and the five feet that matter"),

loc("ojai", "Ojai", "city", "Very High",
    *VCFD,
    "Ojai sits in its oak-ringed valley almost entirely surrounded by wildland, and the 2025 remap treated it accordingly: the city's Very High acreage more than tripled, as reported by The Acorn. The Thomas Fire burned the valley's rim in 2017 and the town remembers watching the ridgelines glow. The first five feet is the highest-leverage prevention within the mapped zones, and in a town this canopied, the honest conversation is as much about what the rules don't require (removing healthy oaks) as what they do.",
    "Ringed by the Thomas Fire",
    "In December 2017 the Thomas Fire encircled the Ojai Valley, burning the surrounding ridges while the town itself was spared the worst structure loss that Ventura's hillsides suffered. The experience of being ringed by fire, evacuation routes limited to a few valley exits, is why Ojai's preparation culture runs deep and why the 2025 remap's tripling of the city's Very High acreage surprised few residents. The practical takeaway for Zone 0 is specific to this town: the first five feet at the structure is the controllable piece, and the oak canopy conversation belongs with VCFD, not with a chainsaw crew acting on a headline.",
    [("Very High", "acreage more than tripled in the 2025 remap"), ("2017", "the Thomas Fire burned the valley's rim"), ("Oak country", "healthy trees are a local-rules conversation, not a mandate"), ("VCFD", "Ventura County Fire Department, contract city")],
    [("Did Ojai's fire designation really triple?",
      "The city's Very High acreage more than tripled in the 2025 remap, as reported by The Acorn. For a town ringed by wildland on nearly every side, the updated modeling formalized what the geography always said."),
     ("Does Zone Zero mean removing Ojai's oaks?",
      "No. The withdrawn statewide draft is not in force, and it is not a mandate to remove healthy oaks. Inside VCFPD, local Zone 0 is Required now for new buildings, additions, and new or refurbished landscape. For existing homes the first five feet is Recommended now. Verify with VCFD before removing anything."),
     ("What did the Thomas Fire do to Ojai?",
      "It burned the valley's surrounding ridges in December 2017 and put the town through encirclement and evacuation, though Ojai was spared the concentrated structure loss Ventura's hillsides suffered. The memory shapes the valley's preparation culture to this day.")],
    "the valley the fire circled"),

loc("santa-paula", "Santa Paula", "city", "designation under review on this site (tier not fully confirmed this pass)",
    *VCFD,
    "Santa Paula sits in the Santa Clara River valley on the Thomas Fire's historical path, served by the Ventura County Fire Department as a contract city. We include it because its fire history and service area are real and verified; we caveat it because this site could not fully confirm the city's current Fire Hazard Severity tier this research pass, and we don't assert what we haven't verified. What's confirmed is stated below; what isn't is labeled.",
    "On the Thomas Fire's path, told precisely",
    "The Thomas Fire ignited near Santa Paula on December 4, 2017 before running west and coastward, and regional coverage consistently places the city among the communities hit hard in the fire's opening hours. That history is verified and belongs here. What we have not confirmed this pass is Santa Paula's exact current FHSZ tier under the 2025 maps, so this page makes no claim about it. For a homeowner the practical path doesn't change: the parcel-level check is free, definitive, and the honest first step regardless of what a city-level summary would say.",
    [("Verified", "VCFD contract city in the Santa Clara River valley"), ("2017", "near the Thomas Fire's ignition, hit hard in its opening hours"), ("Unconfirmed", "current FHSZ tier not asserted on this site this pass"), ("Free check", "your parcel's actual mapped tier")],
    [("Is Santa Paula in a Very High fire hazard zone?",
      "We haven't confirmed the city's current tier with full certainty, so we won't assert it. What's verified: Santa Paula is a VCFD contract city near the Thomas Fire's 2017 ignition point. The definitive answer for your property is a free parcel-level check."),
     ("Why does this site include Santa Paula with a caveat?",
      "Because publishing what's verified with a clear label beats either excluding a fire-historied community or asserting an unconfirmed tier as fact. The caveat is the accuracy."),
     ("Who is Santa Paula's fire authority?",
      "The Ventura County Fire Department, serving the city under contract.")],
    "on the fire's path, stated precisely"),

loc("fillmore", "Fillmore", "city", "designation under review on this site (tier not fully confirmed this pass)",
    "Fillmore Fire Department",
    "Fillmore has its own fire department. VCFD Station 27 (133 C St., Fillmore) serves unincorporated areas near Fillmore and the central Santa Clara Valley and is a cooperator with the city's fire department. Do not treat Fillmore city limits as VCFPD family. Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies.",
    "Fillmore sits up the Santa Clara River valley from Santa Paula, citrus country against the Topatopa foothills. The city fire department is the AHJ inside city limits. VCFD Station 27 is real and nearby, but it covers unincorporated land and cooperates with the city; it is not Fillmore's municipal fire department. Like its downriver neighbor, the city is included here for verified fire history, and caveated because this site could not fully confirm the current Fire Hazard Severity tier this research pass.",
    "The valley the Thomas Fire ran through",
    "The Thomas Fire's December 2017 run moved through the Santa Clara River valley corridor, and regional coverage places Fillmore among the communities affected as the fire spread from its ignition area. That verified regional history is why the city is on this site. The city's exact current FHSZ tier under the 2025 maps is the piece we have not confirmed, and this page deliberately doesn't assert it. The foothill edge above town is the geography most worth checking at the parcel level, which is why the parcel-level check matters.",
    [("Verified", "Fillmore Fire inside city limits; Station 27 unincorporated/cooperator"), ("2017", "in the valley corridor of the Thomas Fire's spread"), ("Unconfirmed", "current FHSZ tier not asserted on this site this pass"), ("Foothills", "the Topatopa edge is the geography worth checking")],
    [("Is Fillmore in a Very High fire hazard zone?",
      "We haven't confirmed the city's current tier with full certainty, so we won't assert it. What's verified: Fillmore sits in the Thomas Fire's 2017 valley corridor. Fillmore Fire is the AHJ inside city limits; Station 27 covers unincorporated land nearby. The definitive answer for your property is a free parcel-level check."),
     ("Who is Fillmore's fire authority?",
      "Fillmore Fire Department inside city limits. VCFD Station 27 serves unincorporated areas near Fillmore and is a cooperator with the city's fire department. Ordinance 34 and VCFPD Zone 0 do not automatically apply inside Fillmore city limits."),
     ("What should a Fillmore homeowner actually do?",
      "Get the free parcel check. Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies. The first five feet is Recommended now: fence line first, then the rest of the five-foot ring.")],
    "citrus country against the foothills, stated precisely"),

# ============ OJAI VALLEY CLUSTER (2) ============

loc("meiners-oaks", "Meiners Oaks", "unincorporated community", "Very High (Ojai Valley zone)",
    *VCFD,
    "Meiners Oaks sits at the Ojai Valley's western end, an unincorporated community under the oaks that give it its name, inside the valley's confirmed Very High zone and served by the Ventura County Fire Department. The first five feet is the highest-leverage prevention here the same as in Ojai proper, and the community shares the valley's defining tension: the canopy is the identity, and the five-foot ring at the structure, not tree removal, is the requirement.",
    "The valley's shared 2017 memory",
    "When the Thomas Fire ringed the Ojai Valley in December 2017, Meiners Oaks shared the valley's encirclement and evacuation experience: limited routes out, ridgelines burning on the horizon. As an unincorporated community, its preparation path runs through VCFD, and the practical inheritance is the same as the valley's: the parcel-level five feet is what each household controls, starting with the fence line and the mulch bed, while the oak canopy conversation stays where it belongs, with the fire authority's local rules.",
    [("Very High", "inside the Ojai Valley's confirmed zone"), ("2017", "shared the valley's Thomas Fire encirclement"), ("Oak canopy", "identity preserved; the five-foot ring is the requirement"), ("VCFD", "Ventura County Fire Department, unincorporated area")],
    [("What Zone 0 rules apply in Meiners Oaks?",
      "Meiners Oaks sits inside the Ojai Valley's confirmed Very High zone under VCFPD. Local Zone 0 is Required now for new buildings, additions, and new or refurbished landscape. Statewide Zone 0 is Proposed — not in force. The first five feet is Recommended now for existing homes."),
     ("Will the rules require removing the community's oaks?",
      "No. Local rules may allow well-maintained trees, and draft statewide language scaled back blanket vegetation restrictions. The clear requirement is a noncombustible first five feet at each structure; verify tree specifics with VCFD."),
     ("What's the right first project on a Meiners Oaks parcel?",
      "The five-foot ring: firewood and stored fuel out, bark mulch swapped for gravel at the foundation, and the fence section touching the house evaluated. Then take the rest of the parcel in turn.")],
    "under the oaks, inside the zone"),

loc("oak-view", "Oak View", "unincorporated community", "Very High (Ojai Valley zone)",
    *VCFD,
    "Oak View lines Highway 33 between Ojai and the coast, the valley's corridor community, unincorporated, inside the Ojai Valley's confirmed Very High zone, and served by the Ventura County Fire Department. The first five feet is the highest-leverage prevention here, and the community's corridor geography, homes stepping up from the highway toward brushy slopes on both sides, makes the parcel-level five feet an especially concrete conversation.",
    "The corridor's shared 2017 memory",
    "Oak View shared the Ojai Valley's Thomas Fire experience in December 2017: the fire burned the surrounding terrain while Highway 33, the corridor's lifeline, carried the valley's evacuations. For a community strung along one road between slopes, the lesson was about both preparation and egress, and the preparation half is what each parcel controls. The ember-resistant ring at every structure, house, garage, and outbuilding alike, is the requirement; the slopes beyond five feet fall under the broader defensible-space zones.",
    [("Very High", "inside the Ojai Valley's confirmed zone"), ("2017", "shared the valley's Thomas Fire experience"), ("Hwy 33", "the corridor community between Ojai and the coast"), ("VCFD", "Ventura County Fire Department, unincorporated area")],
    [("What Zone 0 rules apply in Oak View?",
      "Oak View sits inside the Ojai Valley's confirmed Very High zone under VCFPD. Local Zone 0 is Required now for new buildings, additions, and new or refurbished landscape. Statewide Zone 0 is Proposed — not in force. The first five feet is Recommended now for existing homes."),
     ("What makes Oak View's situation specific?",
      "Corridor geography: homes stepping from Highway 33 toward brushy slopes on both sides, with one main route through. The parcel-level five feet is the controllable half of that equation, and it starts with the fence line and the mulch bed."),
     ("Do outbuildings count under Zone 0?",
      "Yes. The ember-resistant zone wraps every structure: house, garage, sheds, and outbuildings each get the first-five-feet treatment.")],
    "the valley's corridor, prepared"),

# ============ ALSO CONFIRMED VERY HIGH (3) — no anchor fire, no acreage ============

loc("moorpark", "Moorpark", "city", "Very High",
    *VCFD,
    "Moorpark carries a real, confirmed Very High designation where the city meets the hills and canyons of eastern Ventura County, with the Ventura County Fire Department as its contract fire authority. We won't quote an acreage figure because our verified sources don't pin one; what's confirmed is the designation itself and the significant footprint the 2025 remap gave it, and for edge-of-town parcels that's where the first five feet earns the most.",
    "Designated by geography, framed honestly",
    "No single defining wildfire appears in this project's verified record for Moorpark, and this page won't borrow one: the Mountain Fire belongs to Camarillo, the Thomas Fire to the river valley and the coast. Moorpark's designation reflects its own terrain, canyon and hillside edges where homes meet chaparral, formalized by the 2025 remap that placed 59,000 of the county's 86,000 mapped parcels in Very High. The honest first step is parcel-level: the city spans flatland neighborhoods outside the zones and edges inside them.",
    [("Very High", "confirmed, current designation"), ("VCFD", "Ventura County Fire Department, contract city"), ("Canyon edges", "the designation tracks where homes meet chaparral"), ("Parcel check", "the city spans in-zone and out-of-zone areas")],
    [("Is Moorpark in a Very High fire hazard zone?",
      "Yes, on its hillside and canyon edges, with a significant footprint under the 2025 remap. Our verified sources don't pin an exact acreage figure, so we describe the designation rather than invent a number. Check your specific parcel."),
     ("Who enforces Zone Zero in Moorpark?",
      "The Ventura County Fire Department, serving the city under contract, is the Authority Having Jurisdiction. Statewide Zone 0 is Proposed — not in force; local required versus recommended rules are named on this page."),
     ("Does Moorpark have a defining fire event?",
      "Not in this site's verified record, and we don't invent one. The city's obligations follow its confirmed designation and terrain, not a borrowed story.")],
    "canyon edges, honestly framed"),

loc("simi-valley", "Simi Valley", "city", "Very High",
    *VCFD,
    "Simi Valley carries a real, confirmed Very High designation along its rim: the city floor sits ringed by the Santa Susana range and rocky hills where neighborhoods climb into chaparral. The Ventura County Fire Department serves the city under contract. We won't quote an acreage figure because our verified sources don't pin one; the designation and its significant 2025-remap footprint are the confirmed facts, and rim-neighborhood parcels are where the first five feet earns the most.",
    "A ringed valley, framed honestly",
    "No single defining wildfire appears in this project's verified record for Simi Valley, and this page won't borrow one from elsewhere in the county. The city's exposure is structural: a valley floor surrounded by wildland slopes, with hillside neighborhoods pressed against the fuel. The 2025 remap, which more than doubled the county's Very High parcels versus 2010, formalized that geometry. For homeowners the picture splits cleanly by elevation: valley-floor streets largely outside the zones, rim streets inside them, and the free parcel check settles which side you're on.",
    [("Very High", "confirmed, current designation along the rim"), ("VCFD", "Ventura County Fire Department, contract city"), ("Ringed", "a valley floor surrounded by wildland slopes"), ("Parcel check", "elevation largely decides which side of the line you're on")],
    [("Is Simi Valley in a Very High fire hazard zone?",
      "Yes, along its rim and hillside neighborhoods, with a significant footprint under the 2025 remap. Our verified sources don't pin an exact acreage figure, so we describe the designation rather than invent a number. Check your specific parcel."),
     ("Who enforces Zone Zero in Simi Valley?",
      "The Ventura County Fire Department, serving the city under contract, is the Authority Having Jurisdiction. Statewide Zone 0 is Proposed — not in force; local required versus recommended rules are named on this page."),
     ("Which Simi Valley homes are most likely affected?",
      "Rim and hillside neighborhoods where streets climb toward the Santa Susana range and the surrounding chaparral. Valley-floor streets are more often outside the zones, but the parcel-level check is the definitive answer.")],
    "the ringed valley, honestly framed"),

loc("thousand-oaks", "Thousand Oaks", "city", "Very High",
    *VCFD,
    "Thousand Oaks carries a real, confirmed Very High designation across its wildland edges: the Conejo Valley's signature open-space ring, the very thing that defines the city's planning identity, is also its fuel interface. The Ventura County Fire Department serves the city under contract. We won't quote an acreage figure because our verified sources don't pin one; the designation and its significant 2025-remap footprint are the confirmed facts, and open-space-adjacent parcels are where the first five feet earns the most.",
    "The open-space ring, framed honestly",
    "No dedicated anchor fire is asserted on this page: this site states only what its verified record supports, and Thousand Oaks' entry rests on its confirmed designation rather than an event narrative. The city's famous greenbelt planning, neighborhoods laced with preserved open space, produces more wildland-urban interface per resident than almost any city its size, and the 2025 remap read that interface accordingly. The practical translation: if your street backs onto the open-space ring, assume the parcel check matters, and the first five feet at your structure is where compliance starts.",
    [("Very High", "confirmed, current designation on the wildland edges"), ("VCFD", "Ventura County Fire Department, contract city"), ("Greenbelt", "the open-space ring is also the fuel interface"), ("Parcel check", "open-space-adjacent streets are the ones to verify")],
    [("Is Thousand Oaks in a Very High fire hazard zone?",
      "Yes, across its wildland and open-space edges, with a significant footprint under the 2025 remap. Our verified sources don't pin an exact acreage figure, so we describe the designation rather than invent a number. Check your specific parcel."),
     ("Who enforces Zone Zero in Thousand Oaks?",
      "The Ventura County Fire Department, serving the city under contract, is the Authority Having Jurisdiction. Statewide Zone 0 is Proposed — not in force; local required versus recommended rules are named on this page."),
     ("Why is the greenbelt relevant to Zone 0?",
      "Because preserved open space threading through neighborhoods means an unusual amount of home-to-wildland edge. Streets backing onto the ring are exactly where the ember-resistant first five feet earns its keep.")],
    "where the greenbelt meets the fence line"),

PHONE_TEL = "+18055678416"
PHONE = "(805) 567-8416"

def build(write_page):
    for d in L:
        path = f"/{d['slug']}/"
        title = (f"Zone Zero in {d['name']}, CA | {d['ahj']} | Zone Zero Ventura"
                 if "Fillmore" in d["ahj"] else
                 f"Zone Zero in {d['name']}, CA | {d['ahj']} Requirements | Zone Zero Ventura")
        if "Fillmore" in d["ahj"]:
            desc = ("Zone Zero (Zone 0) status for Fillmore: Fillmore Fire is the AHJ inside city limits. VCFD Station 27 is unincorporated/cooperator only. Statewide Zone 0 is Proposed — not in force.")
        else:
            desc = (f"Zone Zero (Zone 0) status for {d['name']}: {d['ahj']} is the AHJ. Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies.")
        snaps = "\n".join(
            f'<div class="zz-piling-item"><div class="zz-piling-val">{v}</div><div class="zz-piling-label">{l}</div></div>'
            for v, l in d["snaps"])
        is_vh = d["tier"].startswith("Very High")
        if "Fillmore" in d["ahj"]:
            qa_tail = ("Fillmore Fire is the AHJ inside city limits. VCFD Station 27 serves unincorporated areas near Fillmore as a cooperator, not as Fillmore's city fire department. Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies. The first five feet is Recommended now.")
        elif "Ventura City" in d["ahj"]:
            qa_tail = ('Ventura City Fire is the AHJ inside city limits. No citywide existing-home Zone 0 ordinance is cited here. Statewide Zone 0 is Proposed — not in force. Existing defensible space (PRC section 4291 and Government Code section 51182) still applies. The first five feet is Recommended now.')
        elif is_vh:
            qa_tail = ('Inside VCFPD, Zone 0 is Required now for new buildings, additions, new landscape, and refurbished landscape (2025 VCWUIC section 604.8.2 / 604.8.2.1, effective March 1, 2025). Statewide Zone 0 is Proposed — not in force. Existing defensible space still applies. The first five feet is Recommended now for existing homes.')
        else:
            qa_tail = "This site states the city's verified fire history and service area while deliberately not asserting an unconfirmed hazard tier; a free parcel-level check gives the definitive answer for your property. Statewide Zone 0 is Proposed — not in force."
        body = f"""<div class="zz-container"><p class="zz-crumb"><a href="/">Home</a> &rsaquo; {d['name']}</p></div>
<header class="zz-hero" style="padding-bottom:104px"><div class="zz-container"><div class="zz-hero-inner">
<h1>Zone Zero in {d['name']}: <em>{d['hero_em']}</em></h1>
<p class="zz-hero-sub">What the ember-resistant zone rules mean for this {d['kind']}, under its actual designation and its actual fire authority.</p>
<div class="zz-hero-btns">
<a href="/find-contractor/" class="zz-btn zz-btn-sand">Check my parcel, free</a>
<a href="tel:{PHONE_TEL}" class="zz-btn zz-btn-ghost">Call {PHONE}</a>
          <span class="zz-phone-disclosure">Calls are answered by an automated AI assistant and may be recorded and transcribed.</span>
</div>
</div></div></header>
<div class="zz-container"><div class="zz-quick-answer"><b>Quick answer:</b> {qa_tail}</div></div>
<section><div class="zz-container">
<p class="zz-eyebrow">The local snapshot</p>
<h2 class="zz-h2">Where {d['name']} stands</h2>
<p>{d['intro']}</p>
<div class="zz-pilings zz-snap">{snaps}</div>
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">The local record</p>
<h2 class="zz-h2">{d['fire_h2']}</h2>
<p>{d['fire']}</p>
</div></section>
<section style="padding-top:0"><div class="zz-container">
<p class="zz-eyebrow">Who enforces it</p>
<h3 class="zz-h3">{d['ahj']}</h3>
<p>{d['ahj_note']} The deadlines page names what is Required now versus Proposed — not in force; <a href="/deadlines/">your jurisdiction sets the specifics</a>, and this page names yours. For the requirements themselves, start with <a href="/regulations/">the regulations guide</a>, <a href="/fences/">fences and gates</a>, and <a href="/landscaping/">landscaping</a>.</p>
</div></section>
"""
        write_page(path, title, desc, body,
                   [("Home", "/"), (d["name"], path)],
                   d["faqs"], f"{d['name']}, California",
                   cta_place=f"your {d['name']} property")
