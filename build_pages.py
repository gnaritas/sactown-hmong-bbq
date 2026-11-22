#!/usr/bin/env python3
"""Sactown Hmong BBQ — template v2 T1 page generator (websites lane, 2026-11-22, t_779fdad1).
All copy comes from the verified-facts card body only; unknowns omitted, never guessed.
Output: public/*.html + sitemap.xml + robots.txt + favicon.svg. Canonical/OG pinned to the -demo host.
Facts provenance: SacBee article317734939 (story/hours), GBP pane 2026-11-22 (NAP/rating/phone),
abridged.org (origin story), hyperlikely (menu style), FB About tab 2026-11-22 (published email).
"""
import json, os

ORIGIN = "https://sactown-hmong-bbq-demo.up.railway.app"
SITE = "Sactown Hmong BBQ"
FB = "https://www.facebook.com/SACTOWNHMONGBBQ"
IG = "https://www.instagram.com/sactownhmongbbq"
MAIL = "hawjboi_916@yahoo.com"
PHONE_DISPLAY = "(916) 822-4344"
PHONE_TEL = "+19168224344"
GEO_LAT, GEO_LON = 38.52075, -121.47086  # OSM way 543067988, 5824 Franklin Blvd (Nominatim 2026-11-22)
MAPQ = "5824+Franklin+Blvd,+Sacramento,+CA+95824"
ADDR1, ADDR2 = "5824 Franklin Blvd", "Sacramento, California 95824"
HOURS = "Open every day — noon until it&rsquo;s sold out"
BUILT = "<!-- BUILT-2026-11-22 -->"
DATE = "2026-11-22"

MAP_EMBED = f'<iframe src="https://www.google.com/maps?q={MAPQ}&output=embed" title="Map: {SITE}, 5824 Franklin Blvd, Sacramento, CA 95824"></iframe>'
MAP_LINK = f"https://maps.google.com/maps?q={MAPQ}"

# 4.5 stars: 4 full + 1 half (GBP 2026-11-22: 4.5, 22 reviews)
STAR = ('<svg class="stars" viewBox="0 0 130 24" role="img" aria-label="Rated 4.5 out of 5 on Google, 22 reviews">'
        '<defs><linearGradient id="halffill"><stop offset="50%" stop-color="currentColor"/><stop offset="50%" stop-color="rgba(247,239,226,.22)"/></linearGradient></defs>'
        '<g fill="currentColor">'
        '<path d="M12 1.5l3.1 6.9 7.4.7-5.6 5 1.6 7.3L12 17.9l-6.5 3.5 1.6-7.3-5.6-5 7.4-.7Z"/>'
        '<path d="M38 1.5l3.1 6.9 7.4.7-5.6 5 1.6 7.3L38 17.9l-6.5 3.5 1.6-7.3-5.6-5 7.4-.7Z"/>'
        '<path d="M64 1.5l3.1 6.9 7.4.7-5.6 5 1.6 7.3L64 17.9l-6.5 3.5 1.6-7.3-5.6-5 7.4-.7Z"/>'
        '<path d="M90 1.5l3.1 6.9 7.4.7-5.6 5 1.6 7.3L90 17.9l-6.5 3.5 1.6-7.3-5.6-5 7.4-.7Z"/>'
        '<path d="M116 1.5l3.1 6.9 7.4.7-5.6 5 1.6 7.3L116 17.9l-6.5 3.5 1.6-7.3-5.6-5 7.4-.7Z" fill="url(#halffill)"/></g></svg>')

# Hmong-stitch diamond band — decorative cross-stitch motif (cultural ornament, not a factual claim)
STITCH = ('<svg class="stitch" viewBox="0 0 1200 46" preserveAspectRatio="none" aria-hidden="true">'
          '<defs><pattern id="st" width="120" height="46" patternUnits="userSpaceOnUse">'
          '<path d="M30 8l12 15-12 15-12-15Z" fill="none" stroke="#e0699b" stroke-width="3" stroke-linejoin="miter"/>'
          '<path d="M30 15l6 8-6 8-6-8Z" fill="#e5a63a"/>'
          '<path d="M90 8l12 15-12 15-12-15Z" fill="none" stroke="#3e9c5f" stroke-width="3" stroke-linejoin="miter"/>'
          '<path d="M90 15l6 8-6 8-6-8Z" fill="#d9481f"/>'
          '<path d="M0 38h8M10 38h8M20 38h8" stroke="#e5a63a" stroke-width="2.4" opacity=".55"/>'
          '<path d="M60 38h8M70 38h8M80 38h8" stroke="#e0699b" stroke-width="2.4" opacity=".55"/>'
          '<path d="M100 38h8M110 38h2" stroke="#3e9c5f" stroke-width="2.4" opacity=".55"/>'
          '</pattern></defs><rect width="1200" height="46" fill="url(#st)"/></svg>')

FLAME_MARK = ('<path d="M50 10c-7 9-13 16-13 24 0 8 6 13 13 13s13-5 13-13c0-8-6-15-13-24Z" fill="#d9481f"/>'
              '<path d="M50 22c-4 6-7 10-7 14 0 4.5 3 7.5 7 7.5s7-3 7-7.5c0-4-3-8-7-14Z" fill="#e5a63a"/>'
              '<path d="M31 6h38" stroke="#f7efe2" stroke-width="4" stroke-linecap="round" opacity=".9"/>')

def head(path, title, desc, og=True):
    canonical = ORIGIN + ("" if path == "/" else path)
    extra = ""
    if og:
        extra = (f'<meta property="og:title" content="{title}">\n'
                 f'<meta property="og:description" content="{desc}">\n'
                 f'<meta property="og:url" content="{canonical}">\n'
                 f'<meta property="og:image" content="{ORIGIN}/og.png">\n'
                 f'<meta property="og:type" content="website">\n'
                 f'<meta name="twitter:card" content="summary_large_image">\n')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{extra}<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

HEADER = f'''<header class="top"><div class="wrap"><a class="brand" href="/"><svg class="mark" viewBox="0 0 100 100" role="img" aria-label="{SITE} emblem: a flame above the grill inside a stitch diamond"><path d="M50 4l40 46-40 46-40-46Z" fill="none" stroke="#e5a63a" stroke-width="4" stroke-linejoin="miter"/><path d="M50 14l31 36-31 36-31-36Z" fill="#241a17"/>{FLAME_MARK}<path d="M35 52c-4 5-7 9-7 13M65 52c4 5 7 9 7 13" stroke="#f7efe2" stroke-width="3" stroke-linecap="round" opacity=".45" fill="none"/><path d="M20 88l6 8-6 8-6-8Z" fill="#e0699b"/><path d="M80 88l6 8-6 8-6-8Z" fill="#3e9c5f"/></svg><span class="word">{SITE}<small>Hmong barbecue · Franklin Blvd · Sacramento</small></span></a><nav class="main" aria-label="Main"><ul><li><a href="/menu">Menu</a></li><li><a href="/catering">Catering</a></li><li><a href="/visit">Visit</a></li><li><a class="btn" href="/contact">Contact</a></li></ul></nav></div></header>
<main id="main">
'''

FOOTER = f'''</main>

<footer class="site"><div class="wrap"><div class="nap"><p class="fbrand">{SITE}</p><address>{ADDR1}<br>{ADDR2}<br>Open every day — noon until sold out<br>Hmong barbecue restaurant</address><p class="tel"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></div><nav aria-label="Footer"><ul><li><a href="/menu">Menu</a></li><li><a href="/catering">Catering</a></li><li><a href="/visit">Visit</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy">Privacy</a></li></ul></nav><p class="socials"><a href="{FB}" rel="noopener">Facebook</a> <a href="{IG}" rel="noopener">Instagram</a></p><p class="footline">© 2026 {SITE} · Hmong barbecue · {ADDR1}, {ADDR2}</p></div></footer>
{BUILT}
'''

def ld(blocks):
    return '<script type="application/ld+json">\n' + json.dumps({"@graph": blocks}, indent=1, ensure_ascii=False) + '\n</script>\n</body>\n</html>'

def web_page(path, name, desc):
    return {
        "@type": "WebPage", "@id": ORIGIN + path, "name": name, "description": desc,
        "url": ORIGIN + path, "isPartOf": {"@id": ORIGIN + "/#restaurant"},
    }

def breadcrumb(path, crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + p}
        for i, (n, p) in enumerate(crumbs)]}

def service(sid, name, desc, path):
    return {
        "@type": "Service", "@id": ORIGIN + path + sid, "name": name, "description": desc,
        "url": ORIGIN + path, "serviceType": name,
        "provider": {"@id": ORIGIN + "/#restaurant"},
        "areaServed": {"@type": "City", "name": "Sacramento", "addressRegion": "CA"},
    }

RESTAURANT = {
    "@type": "Restaurant", "@id": ORIGIN + "/#restaurant", "name": SITE,
    "image": ORIGIN + "/og.png", "url": ORIGIN + "/",
    "telephone": "+1-916-822-4344",
    "servesCuisine": ["Hmong barbecue", "Texas-style smoked meats"],
    "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Sacramento",
                "addressRegion": "CA", "postalCode": "95824", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
    "hasMap": MAP_LINK,
    "sameAs": [FB, IG],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.5", "reviewCount": "22",
                        "bestRating": "5", "ratingSource": "Google Maps reviews"},
    "hasMenu": {"@id": ORIGIN + "/menu#bbq-menu"},
}

CTA_BAND = (f'<p class="heract"><a class="btn big" href="/menu">See the barbecue</a> '
            f'<a class="btn ghost" href="{MAP_LINK}" rel="noopener">Get directions</a></p>')

# ---------------------------------------------------------------- pages
PAGES = {}

# HOME --------------------------------------------------------------
PAGES["/"] = (head("/", "Sactown Hmong BBQ — Hmong Barbecue Restaurant, Sacramento CA",
    "Sacramento's first Hmong barbecue restaurant on Franklin Blvd — mesquite-smoked ribs, pork belly, grilled chicken, house-made Hmong sausage and kua txob hot sauce. Open every day, noon until sold out.")
+ HEADER + f'''
<section class="hero"><div class="wrap"><div class="herotext">
<p class="kick">Franklin Blvd · Sacramento, CA · first storefront opened Oct 2026</p>
<h1>Sacramento&rsquo;s first<br><em>Hmong barbecue.</em></h1>
<p class="herosub">Texas-style ribs and pork belly smoked over mesquite, house-made Hmong sausage and <span class="kd">kua txob</span> bird&rsquo;s-eye chili sauce — years of pop-ups and catering, now with a home on Franklin Boulevard.</p>
<p class="hourschip"><span class="dot" aria-hidden="true"></span>Open every day — <strong>noon until it&rsquo;s sold out</strong></p>
{CTA_BAND}
<p class="ratingline">{STAR}<span class="rt">4.5 on Google · 22 reviews</span></p>
</div><div class="heroart" aria-hidden="true"><svg viewBox="0 0 420 420"><path d="M210 12l158 182-158 182-158-182Z" fill="none" stroke="#e5a63a" stroke-width="5" stroke-linejoin="miter" opacity=".9"/><path d="M210 54l122 140-122 140-122-140Z" fill="#241a17"/><path d="M210 96c-27 34-50 61-50 92 0 30 22 50 50 50s50-20 50-50c0-31-23-58-50-92Z" fill="#d9481f"/><path d="M210 140c-16 21-29 37-29 54 0 17 12 29 29 29s29-12 29-29c0-17-13-33-29-54Z" fill="#e5a63a"/><path d="M210 178c-8 11-14 19-14 27 0 8 6 14 14 14s14-6 14-14c0-8-6-16-14-27Z" fill="#f7d98c"/><path d="M128 82h164" stroke="#f7efe2" stroke-width="10" stroke-linecap="round" opacity=".9"/><path d="M150 66c-10 12-16 22-16 30M270 66c10 12 16 22 16 30" stroke="#f7efe2" stroke-width="7" stroke-linecap="round" opacity=".35" fill="none"/><g fill="#e0699b"><path d="M84 300l12 15-12 15-12-15Z"/><path d="M336 300l12 15-12 15-12-15Z" fill="#3e9c5f"/></g></svg></div></div>{STITCH}</section>

<section class="block"><div class="wrap">
<h2>What comes off the smoke</h2>
<p class="lede">The whole grill runs on mesquite. When it&rsquo;s gone, it&rsquo;s gone — the kitchen closes as soon as the smoke case is empty.</p>
<div class="grid4">
<div class="mcard"><svg viewBox="0 0 100 100" aria-hidden="true"><path d="M18 30c26-10 48-8 64 4-8 22-28 36-52 36-4 0-8 4-12 10-4-18-2-36 0-50Z" fill="none" stroke="#d9481f" stroke-width="5"/><path d="M30 42h30M28 54h26M32 66h18" stroke="#e5a63a" stroke-width="4" stroke-linecap="round"/></svg><h3>Beef ribs</h3><p>Texas-style ribs, smoked over mesquite until the bark sets.</p></div>
<div class="mcard"><svg viewBox="0 0 100 100" aria-hidden="true"><rect x="20" y="34" width="60" height="34" rx="6" fill="none" stroke="#d9481f" stroke-width="5"/><path d="M32 42v18M46 42v18M60 42v18" stroke="#e5a63a" stroke-width="4"/><path d="M28 26c4-6 10-6 14 0M58 26c4-6 10-6 14 0" stroke="#f7efe2" stroke-width="3.4" opacity=".45" fill="none" stroke-linecap="round"/></svg><h3>Pork belly</h3><p>Slab pork belly put through the same mesquite smoke.</p></div>
<div class="mcard"><svg viewBox="0 0 100 100" aria-hidden="true"><path d="M40 26c18-8 34 2 34 18 0 22-14 38-34 42-6-14-8-40 0-60Z" fill="none" stroke="#d9481f" stroke-width="5"/><path d="M44 40c8-2 14 2 14 10" stroke="#e5a63a" stroke-width="4" fill="none" stroke-linecap="round"/></svg><h3>Grilled chicken</h3><p>Chicken straight over the coals to order.</p></div>
<div class="mcard"><svg viewBox="0 0 100 100" aria-hidden="true"><path d="M22 40c0-12 10-18 22-18s14 6 26 6 20 6 20 16-8 16-20 16-14 6-26 6-22-6-22-16c0-4 2-8 4-10Z" fill="none" stroke="#d9481f" stroke-width="5" transform="translate(3,4) scale(.9)"/><circle cx="38" cy="50" r="4" fill="#e5a63a"/><circle cx="62" cy="46" r="4" fill="#3e9c5f"/></svg><h3>Hmong sausage</h3><p>House-made sausage seasoned the Hmong way — the plate that built this shop&rsquo;s name at pop-ups.</p></div>
</div>
<div class="sauce"><div class="sauceglyph" aria-hidden="true"><svg viewBox="0 0 100 100"><path d="M50 14c16 12 26 26 26 42a26 26 0 0 1-52 0c0-16 10-30 26-42Z" fill="#d9481f"/><path d="M50 14c-6 12-6 24 0 34 6-10 6-22 0-34Z" fill="#e5a63a"/><circle cx="42" cy="58" r="3.4" fill="#f7d98c"/><circle cx="58" cy="54" r="3.4" fill="#f7d98c"/><circle cx="50" cy="68" r="3.4" fill="#f7d98c"/></svg></div><div class="saucetext"><h3>Kua txob — the house hot sauce</h3><p>Bird&rsquo;s-eye chili Hmong hot sauce, the condiment every table reaches for. Ask for it; heat is the point.</p></div></div>
<p class="blockact"><a class="btn" href="/menu">Full menu &amp; hours</a> <a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p>
</div></section>

<section class="story"><div class="wrap"><div class="storytext">
<h2>From Facebook Marketplace to Franklin Boulevard</h2>
<p>For years Sactown Hmong BBQ was the pop-up and catering kitchen — orders posted on Facebook Marketplace, weekend events, lines that kept growing. In October 2026 the shop opened its first storefront on Franklin Boulevard, and The Sacramento Bee called it Sacramento&rsquo;s first Hmong barbecue restaurant.</p>
<p class="src">Story details: The Sacramento Bee (Oct 22, 2026) and Abridged Press opening coverage.</p>
</div><div class="storyside">
<div class="chipcard"><p class="big">{STAR}</p><p class="bigt">4.5 out of 5 on Google</p><p class="sm">22 reviews and counting — the neighborhood found the place the first weekend.</p></div>
<div class="chipcard"><p class="bigt">13,000+ followers</p><p class="sm">The pop-up years built <a href="{FB}" rel="noopener">5.3k on Facebook</a> and <a href="{IG}" rel="noopener">8.1k on Instagram</a>. The smoke is the same — now there&rsquo;s an address to point people to.</p></div>
</div></div></section>

<section class="block mapband"><div class="wrap">
<h2>Find the smoke</h2>
<div class="mapgrid"><div class="mapcell">{MAP_EMBED}</div><div class="infocards">
<div class="infocard"><h3>Address</h3><address>{ADDR1}<br>{ADDR2}</address><p><a href="{MAP_LINK}" rel="noopener">Open in Google Maps →</a></p></div>
<div class="infocard"><h3>Hours</h3><p>Every day, from noon until the grill sells out. Some nights that means an early last plate — come by noon or early afternoon and you&rsquo;ll catch everything.</p></div>
<div class="infocard"><h3>Phone</h3><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> — the number on the shop&rsquo;s Google listing. Questions about what&rsquo;s on the smoke today? Call before you drive.</p></div>
</div></div>
</div></section>
''' + FOOTER + ld([RESTAURANT,
    web_page("/", SITE + " — Hmong Barbecue Restaurant", "Sacramento's first Hmong barbecue restaurant on Franklin Blvd — mesquite smoke, Hmong sausage, kua txob. Open daily noon till sold out."),
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "When does Sactown Hmong BBQ open?",
         "acceptedAnswer": {"@type": "Answer", "text": "Every day at noon, and the grill stays open until everything is sold out."}},
        {"@type": "Question", "name": "Where is Sactown Hmong BBQ located?",
         "acceptedAnswer": {"@type": "Answer", "text": "5824 Franklin Blvd, Sacramento, CA 95824 — the shop's first storefront after years of pop-ups and catering."}}]}])
)

# MENU ------------------------------------------------------------
PAGES["/menu"] = (head("/menu", "Smoked Meats & Hmong Barbecue — Sactown Hmong BBQ, Sacramento CA",
    "The barbecue at Sactown Hmong BBQ in Sacramento: mesquite-smoked beef ribs, pork belly and grilled chicken, house-made Hmong sausage and kua txob chili hot sauce. Smoke starts at noon, ends at sold out.")
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">The menu</p>
<h1>Everything comes off mesquite smoke</h1>
<p class="bandsub">Ribs, belly, chicken and Hmong sausage, cooked the Texas-style-smoke way with Hmong seasoning. Portions run out daily — the case is done when it&rsquo;s empty.</p>
<p class="heract"><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> <a class="btn ghost" href="{MAP_LINK}" rel="noopener">Get directions</a></p>
</div></section>

<section class="block"><div class="wrap">
<div class="menusec">
<h2>From the smoke</h2>
<ul class="menu">
<li><span class="mname">Beef ribs</span><span class="mdots" aria-hidden="true"></span><span class="mdesc">Texas-style, smoked over mesquite.</span></li>
<li><span class="mname">Pork belly</span><span class="mdots" aria-hidden="true"></span><span class="mdesc">Slab belly, through the mesquite smoke.</span></li>
<li><span class="mname">Grilled chicken</span><span class="mdots" aria-hidden="true"></span><span class="mdesc">Over the coals, to order.</span></li>
<li><span class="mname">Hmong sausage</span><span class="mdots" aria-hidden="true"></span><span class="mdesc">House-made, seasoned the Hmong way — the item the pop-up years were built on.</span></li>
</ul>
</div>
<div class="menusec">
<h2>On the side</h2>
<ul class="menu">
<li><span class="mname">Kua txob</span><span class="mdots" aria-hidden="true"></span><span class="mdesc">House bird&rsquo;s-eye chili Hmong hot sauce. Ask for it — it was made for this food.</span></li>
</ul>
<p class="menunote">Plate combos and quantities change with the day&rsquo;s smoke. Ask what&rsquo;s up when you walk in — everything is cooked in one batch, and the day ends when it&rsquo;s gone. Coverage of the opening: The Sacramento Bee, October 2026.</p>
<p class="blockact"><a class="btn" href="/catering">Feeding a crowd? Catering</a> <a class="btn ghost" href="/contact">Ask about today</a></p>
</div>
</div></section>
''' + FOOTER + ld([
    {"@type": "Menu", "@id": ORIGIN + "/menu#bbq-menu", "name": "Barbecue Menu — " + SITE,
     "url": ORIGIN + "/menu", "inFoodService": {"@id": ORIGIN + "/#restaurant"},
     "hasMenuSection": [
        {"@type": "MenuSection", "name": "From the smoke", "headline": "From the smoke", "hasMenuItem": [
            {"@type": "MenuItem", "name": "Beef ribs", "description": "Texas-style, smoked over mesquite."},
            {"@type": "MenuItem", "name": "Pork belly", "description": "Slab belly, through the mesquite smoke."},
            {"@type": "MenuItem", "name": "Grilled chicken", "description": "Over the coals, to order."},
            {"@type": "MenuItem", "name": "Hmong sausage", "description": "House-made, seasoned the Hmong way."}]},
        {"@type": "MenuSection", "name": "On the side", "headline": "On the side", "hasMenuItem": [
            {"@type": "MenuItem", "name": "Kua txob", "description": "House bird's-eye chili Hmong hot sauce."}]}]},
    web_page("/menu", "Barbecue Menu", "Mesquite-smoked ribs, pork belly, grilled chicken, house-made Hmong sausage and kua txob at Sactown Hmong BBQ, Sacramento."),
    breadcrumb("/menu", [("Home", "/"), ("Menu", "/menu")])])
)

# CATERING --------------------------------------------------------
PAGES["/catering"] = (head("/catering", "Catering & Private Events — Sactown Hmong BBQ, Sacramento CA",
    "Sactown Hmong BBQ catering — years of pop-ups and catering before the storefront. Mesquite-smoked ribs, Hmong sausage and grilled chicken for events across Sacramento. Ask for a quote by phone or form.")
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">Catering &amp; events</p>
<h1>The catering years came first</h1>
<p class="bandsub">Before the storefront, this was a catering kitchen — orders posted on Facebook Marketplace, packed and smoked for parties and events. The pop-up playbook still runs: tell us the event and the headcount.</p>
<p class="heract"><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> <a class="btn ghost" href="/contact">Send the details</a></p>
</div></section>

<section class="block"><div class="wrap">
<h2>What to expect</h2>
<div class="cols">
<div class="col"><h3>Same smoke, bigger trays</h3><p>Ribs, pork belly, grilled chicken and house-made Hmong sausage — the same mesquite program the restaurant runs every day, scaled for a crowd. Kua txob travels with it.</p></div>
<div class="col"><h3>Book the way the pop-ups did</h3><p>Catering orders started here on Facebook Marketplace and grew by word of mouth. Calling or messaging the shop is still exactly how a date gets set — no portals, no forms-in-a-black-hole.</p></div>
<div class="col"><h3>Ask for the day&rsquo;s smoke</h3><p>Every menu follows what went up on the grill that week. Tell us the date and headcount and ask what&rsquo;s coming off the smoke — the answer is the menu.</p></div>
</div>
<div class="strip"><p>Feeding 20 or 200 — start with a call or a note, and the shop will answer with what it can smoke for your date.</p><a class="btn" href="/contact">Start your inquiry</a></div>
<p class="menunote">Event origin details: The Sacramento Bee and Abridged Press, October 2026.</p>
</div></section>
''' + FOOTER + ld([
    service("#catering", "Catering & private events", "Mesquite-smoked barbecue catering from Sactown Hmong BBQ, Sacramento — the catering program that ran for years before the storefront.", "/catering"),
    web_page("/catering", "Catering & Private Events", "Barbecue catering from Sactown Hmong BBQ in Sacramento — ribs, pork belly, chicken and Hmong sausage for events."),
    breadcrumb("/catering", [("Home", "/"), ("Catering", "/catering")])])
)

# VISIT -----------------------------------------------------------
PAGES["/visit"] = (head("/visit", "Visit — Franklin Blvd, Sactown Hmong BBQ, Sacramento CA",
    "Visit Sactown Hmong BBQ at 5824 Franklin Blvd, Sacramento CA 95824. Open every day from noon until the grill sells out. Call (916) 822-4344 before you drive.")
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">Visit</p>
<h1>Noon to sold out, seven days a week</h1>
<p class="bandsub">The storefront is on Franklin Boulevard — {ADDR2}. Smoke starts at noon; the day ends whenever the case is empty. Early afternoons catch the fullest board.</p>
<p class="heract"><a class="btn" href="{MAP_LINK}" rel="noopener">Get directions</a> <a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p>
</div></section>

<section class="block mapband"><div class="wrap">
<h2>The corner of the smoke</h2>
<div class="mapgrid"><div class="mapcell">{MAP_EMBED}</div><div class="infocards">
<div class="infocard"><h3>Address</h3><address>{ADDR1}<br>{ADDR2}</address><p><a href="{MAP_LINK}" rel="noopener">Open in Google Maps →</a></p></div>
<div class="infocard"><h3>Hours</h3><p>Every day, noon until sold out. The sold-out sign goes up whenever the smoke case is empty — it can be earlier some days.</p></div>
<div class="infocard"><h3>Phone</h3><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> — call ahead to ask what&rsquo;s on the grill today.</p></div>
<div class="infocard"><h3>Good to know</h3><p>The shop opened its first storefront in October 2026 after years of pop-ups and catering, and reviews started the same week — 4.5 stars across 22 Google reviews so far.</p></div>
</div></div>
<p class="blockact"><a class="btn" href="/menu">See the barbecue</a> <a class="btn ghost" href="/catering">Catering</a></p>
</div></section>
''' + FOOTER + ld([
    service("#visit", "Dine-in visit", "Visit Sactown Hmong BBQ on Franklin Blvd, Sacramento — open daily from noon until sold out.", "/visit"),
    web_page("/visit", "Visit", "Address, hours and directions for Sactown Hmong BBQ, 5824 Franklin Blvd, Sacramento CA 95824."),
    breadcrumb("/visit", [("Home", "/"), ("Visit", "/visit")])])
)

# CONTACT ---------------------------------------------------------
PAGES["/contact"] = (head("/contact", "Contact — Sactown Hmong BBQ, Sacramento CA",
    "Contact Sactown Hmong BBQ in Sacramento — send a note through the form, email hawjboi_916@yahoo.com, or call (916) 822-4344. 5824 Franklin Blvd, open daily noon till sold out.")
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">Contact</p>
<h1>Send the shop a note</h1>
<p class="bandsub">Catering dates, questions about the smoke, or a plate you want cooked for a party — this lands in the shop&rsquo;s own inbox.</p>
<p class="heract"><a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> <a class="btn ghost" href="{FB}" rel="noopener">Message on Facebook</a></p>
</div></section>

<section class="block"><div class="wrap">
<div class="mapgrid"><div><form class="cform" method="post" action="/contact" accept-charset="utf-8"><h2>Leave a note</h2><div class="fields"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div><div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div><div class="field full"><label for="f-email">Email <span class="opt">(optional — so we can answer)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div><div class="field full"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div><button class="btn big" type="submit">Send note</button></div><p class="fineprint">Notes go straight to the shop&rsquo;s inbox — no newsletter, no list, just a reply.</p></form></div><div><div class="infocards" style="margin-top:0"><div class="infocard"><h3>Email</h3><p><a href="mailto:{MAIL}">{MAIL}</a> — the published inbox on the shop&rsquo;s Facebook page.</p></div><div class="infocard"><h3>Phone</h3><p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> — the number on the Google listing.</p></div><div class="infocard"><h3>Social</h3><p>Menus, dates and the day-to-day land on <a href="{FB}" rel="noopener">Facebook</a> and <a href="{IG}" rel="noopener">Instagram</a> first.</p></div><div class="infocard"><h3>The shop</h3><p>{ADDR1}, {ADDR2} — open every day, noon until sold out.</p><p><a href="{MAP_LINK}" rel="noopener">Open in Google Maps →</a></p></div></div></div></div>
</div></section>
''' + FOOTER + ld([
    web_page("/contact", "Contact", "Contact Sactown Hmong BBQ Sacramento — form, published email, phone and social pages."),
    breadcrumb("/contact", [("Home", "/"), ("Contact", "/contact")])])
)

# PRIVACY ---------------------------------------------------------
PAGES["/privacy"] = (head("/privacy", "Privacy Policy — Sactown Hmong BBQ, Sacramento CA",
    "Privacy policy for sactownhmongbbq site pages: what the contact form collects, hosting, map embed, and no cookies or trackers on this site.")
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">Privacy</p>
<h1>What this site knows about you</h1>
<p class="bandsub">Short version: nothing tracks you here. The only information this site collects is what you type into the contact form.</p>
<p class="heract"><a class="btn" href="/contact">Contact the shop</a></p>
</div></section>

<section class="block"><div class="wrap prose">
<h2>Contact form</h2>
<p>The form on the contact page collects the name, phone, email and message you enter. The note is delivered to Sactown Hmong BBQ&rsquo;s own email inbox so the shop can answer. Nothing is sold, shared or added to a marketing list.</p>
<h2>Cookies &amp; tracking</h2>
<p>This site sets no cookies and runs no analytics or advertising scripts. There is no visitor counter and no third-party tracker.</p>
<h2>Google Maps</h2>
<p>The visit and home pages show a Google Maps embed. When those pages load, Google receives standard request data (IP address, browser information) as part of delivering the map. See Google&rsquo;s own privacy policy for details on that request.</p>
<h2>Hosting</h2>
<p>Pages are served from a standard hosting provider, which logs ordinary web requests (page, time, approximate location) for reliability.</p>
<h2>Questions</h2><p>Ask the shop directly — same form, or <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
<p class="blockact"><a class="btn" href="/">Back to the front page</a></p>
</div></section>
''' + FOOTER + ld([
    web_page("/privacy", "Privacy Policy", "Privacy policy for the Sactown Hmong BBQ site: form data, map embed, no cookies."),
    breadcrumb("/privacy", [("Home", "/"), ("Privacy", "/privacy")])])
)

# 404 -------------------------------------------------------------
PAGES["/404"] = (head("/404", "Page not found — Sactown Hmong BBQ", "This page is gone — or sold out. Head back to the front page or the menu.", og=False)
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">404</p>
<h1>That plate&rsquo;s gone</h1>
<p class="bandsub">This page isn&rsquo;t here — much like the last tray of ribs after a Friday. The menu and the front page are both still up.</p>
<p class="heract"><a class="btn" href="/">Front page</a> <a class="btn ghost" href="/menu">See the barbecue</a></p>
</div></section>
''' + FOOTER + "</body>\n</html>")

# THANKS ----------------------------------------------------------
PAGES["/thanks"] = (head("/thanks", "Note sent — Sactown Hmong BBQ", "Your note is on its way to Sactown Hmong BBQ's inbox.", og=False)
+ HEADER + f'''
<section class="pageband"><div class="wrap">
<p class="kick">Sent</p>
<h1>Note on its way</h1>
<p class="bandsub">Your message went straight to the shop&rsquo;s inbox. The sooner you call {PHONE_DISPLAY}, the sooner you get an answer — but the reply will come.</p>
<p class="heract"><a class="btn" href="/menu">While you wait: the menu</a> <a class="btn ghost" href="/">Back to the front page</a></p>
</div></section>
''' + FOOTER + "</body>\n</html>")

# ---------------------------------------------------------------- assets
CSS = ''':root{--ink:#181110;--coal:#241a17;--cream:#f7efe2;--paper:#fbf6ec;--ember:#d9481f;--emberhot:#f2711c;--gold:#e5a63a;--pink:#e0699b;--green:#3e9c5f;--disp:'Avenir Next Condensed','Futura','Helvetica Neue',Arial,sans-serif;--body:Georgia,'Iowan Old Style','Times New Roman',serif}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--cream);color:#2b211c;font-family:var(--body);font-size:17px;line-height:1.65}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:var(--gold);color:var(--ink);padding:8px 14px;z-index:9;border-radius:6px}
a{color:#a93b16;text-underline-offset:3px}
h1,h2,h3{font-family:var(--disp);font-weight:800;letter-spacing:.02em;line-height:1.06}
h1{font-size:clamp(38px,6vw,64px);text-transform:uppercase}
h2{font-size:clamp(26px,3.6vw,38px);text-transform:uppercase;margin-bottom:14px}
h3{font-size:19px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px}
p{margin:0}
.stars{height:22px;width:auto;color:var(--gold);display:inline-block;vertical-align:middle}
/* header */
.top{background:var(--ink);color:var(--cream);border-bottom:3px solid var(--gold)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--cream)}
.brand .mark{width:52px;height:52px;flex:none}
.brand .word{font-family:var(--disp);font-weight:800;font-size:22px;letter-spacing:.06em;text-transform:uppercase;line-height:1.05;display:flex;flex-direction:column}
.brand .word small{font-family:var(--body);font-weight:400;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:rgba(247,239,226,.68);margin-top:4px}
nav.main ul{display:flex;gap:20px;list-style:none;align-items:center;flex-wrap:wrap}
nav.main a{color:var(--cream);text-decoration:none;font-family:var(--disp);font-weight:700;font-size:15px;letter-spacing:.12em;text-transform:uppercase;padding:8px 2px;border-bottom:2px solid transparent}
nav.main a:hover{border-color:var(--ember)}
.btn{display:inline-block;background:var(--ember);color:#fff!important;border:2px solid var(--ember);border-radius:10px;padding:11px 20px;font-family:var(--disp);font-weight:800;font-size:15px;letter-spacing:.09em;text-transform:uppercase;text-decoration:none;transition:background .15s}
.btn:hover{background:var(--emberhot);border-color:var(--emberhot)}
.btn.ghost{background:transparent;color:var(--gold)!important;border-color:var(--gold)}
nav.main .btn.ghost{}
.btn.big{padding:14px 26px;font-size:16px}
/* hero */
.hero{background:radial-gradient(700px 420px at 82% 18%,rgba(217,72,31,.28),transparent 62%),radial-gradient(520px 320px at 8% 96%,rgba(229,166,58,.14),transparent 58%),linear-gradient(165deg,#120c0b,#241a17 62%,#2e201a);color:var(--cream);position:relative}
.hero .wrap{display:flex;align-items:center;gap:36px;padding-top:52px;padding-bottom:52px}
.herotext{flex:1 1 520px;min-width:0}
.kick{font-family:var(--disp);font-weight:800;font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
.hero h1 em{font-style:normal;color:var(--emberhot)}
.herosub{margin-top:16px;font-size:18.5px;line-height:1.6;color:rgba(247,239,226,.92);max-width:560px}
.kd{color:var(--gold);font-style:italic}
.hourschip{display:inline-flex;gap:10px;align-items:center;margin-top:20px;background:rgba(247,239,226,.08);border:1.5px dashed rgba(229,166,58,.7);border-radius:999px;padding:9px 18px;font-size:15.5px;color:var(--cream)}
.hourschip strong{color:var(--gold)}
.dot{width:10px;height:10px;border-radius:50%;background:var(--green);box-shadow:0 0 0 3px rgba(62,156,95,.25)}
.heract{margin-top:22px;display:flex;gap:12px;flex-wrap:wrap}
.ratingline{margin-top:22px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.rt{font-size:15px;letter-spacing:.04em;color:rgba(247,239,226,.85)}
.heroart{flex:0 0 320px;display:flex;justify-content:center}
.heroart svg{width:min(320px,46vw);height:auto}
.stitch{display:block;width:100%;height:46px}
/* page bands */
.pageband{background:radial-gradient(560px 320px at 88% 0%,rgba(217,72,31,.32),transparent 60%),linear-gradient(160deg,#120c0b,#241a17);color:var(--cream);padding:44px 0;border-bottom:3px solid var(--gold)}
.pageband h1{margin:6px 0 12px}
.bandsub{max-width:640px;color:rgba(247,239,226,.9);font-size:17.5px}
.pageband .heract{margin-top:18px}
.pageband .btn.ghost{color:var(--gold)!important}
/* blocks */
.block{padding:56px 0}
.block>p+p,.prose>p+p,.col+p{margin-top:14px}
.lede{font-size:19px;max-width:700px;margin-bottom:26px}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:26px 0 8px}
.mcard{background:var(--paper);border:1.5px solid #e4d5bd;border-top:4px solid var(--ember);border-radius:14px;padding:22px 20px}
.mcard svg{width:58px;height:58px;display:block;margin-bottom:12px}
.mcard p{font-size:15.5px;line-height:1.55;color:#4a3a31}
.sauce{display:flex;gap:18px;align-items:center;background:var(--coal);color:var(--cream);border-radius:16px;padding:22px 26px;margin:26px 0 4px}
.sauceglyph svg{width:64px;height:64px;display:block;flex:none}
.saucetext h3{color:var(--gold);margin-bottom:4px}
.saucetext p{font-size:16px;color:rgba(247,239,226,.9)}
.blockact{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap}
/* story */
.story{background:var(--paper);border-top:1.5px solid #e4d5bd;border-bottom:1.5px solid #e4d5bd;padding:56px 0}
.story .wrap{display:flex;gap:34px;align-items:flex-start}
.storytext{flex:1 1 560px;min-width:0}
.storytext p{margin-top:14px;max-width:640px}
.src{font-size:13.5px;color:#8a7463;letter-spacing:.02em;font-style:italic}
.storyside{flex:1 1 300px;display:flex;flex-direction:column;gap:14px;min-width:260px}
.chipcard{background:var(--cream);border:1.5px solid #e4d5bd;border-radius:14px;padding:20px}
.chipcard .big{margin-bottom:6px}
.bigt{font-family:var(--disp);font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:16px}
.sm{font-size:15px;color:#4a3a31;margin-top:6px}
/* map */
.mapband{padding-top:48px}
.mapgrid{display:grid;grid-template-columns:1.15fr 1fr;gap:18px;margin-top:18px}
.mapcell{min-width:0}
.mapcell iframe{width:100%;height:340px;border:1.5px solid #e4d5bd;border-radius:14px;background:#efe6d6;display:block}
.infocards{display:flex;flex-direction:column;gap:14px}
.infocard{background:var(--paper);border:1.5px solid #e4d5bd;border-left:4px solid var(--gold);border-radius:12px;padding:16px 18px}
.infocard address{font-style:normal}
.infocard p+p{margin-top:8px}
/* menu lists */
.menusec{margin-top:8px}
.menusec+.menusec{margin-top:40px}
ul.menu{list-style:none;border-top:1.5px dashed #cbb896;margin-top:6px}
ul.menu li{display:flex;align-items:baseline;gap:14px;padding:14px 2px;border-bottom:1.5px dashed #cbb896;flex-wrap:wrap}
.mname{font-family:var(--disp);font-weight:800;text-transform:uppercase;letter-spacing:.05em;font-size:19px;flex:none}
.mdots{flex:1 1 40px;border-bottom:2px dotted #cbb896;transform:translateY(-4px);min-width:20px}
.mdesc{flex:1 1 240px;color:#4a3a31;font-size:15.5px}
.menunote{font-size:14px;color:#8a7463;margin-top:18px;font-style:italic}
/* cols/strip */
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.col{background:var(--paper);border:1.5px solid #e4d5bd;border-top:4px solid var(--gold);border-radius:14px;padding:22px 20px;font-size:15.5px;line-height:1.6}
.strip{margin-top:26px;background:var(--coal);color:var(--cream);border-radius:16px;padding:22px 26px;display:flex;gap:18px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.strip p{font-size:16.5px;flex:1 1 340px}
/* form */
.cform{background:var(--paper);border:1.5px solid #e4d5bd;border-radius:16px;padding:26px}
.cform h2{margin-bottom:16px}
.fields{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.field{display:flex;flex-direction:column;gap:7px}
.field.full{grid-column:1/-1}
.opt{font-weight:400;text-transform:none;letter-spacing:0;font-family:var(--body);font-size:13.5px;color:#8a7463}
label{font-family:var(--disp);font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
input,textarea{font:inherit;font-size:16px;padding:11px 13px;border:1.5px solid #cdbb9d;border-radius:9px;background:#fffdf8;color:#2b211c}
input:focus,textarea:focus{outline:2.5px solid var(--ember);outline-offset:1px}
textarea{min-height:130px;resize:vertical}
.cform .btn{margin-top:18px}
.fineprint{font-size:13.5px;color:#8a7463;margin-top:12px}
/* prose */
.prose{max-width:760px}
.prose h2{margin-top:34px}
.prose h2:first-of-type{margin-top:0}
/* footer */
footer.site{background:var(--ink);color:rgba(247,239,226,.85);border-top:3px solid var(--gold);padding:44px 0 34px}
footer.site .wrap{display:grid;grid-template-columns:1.3fr 1fr;gap:26px}
.fbrand{font-family:var(--disp);font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);font-size:18px;margin-bottom:10px}
footer.site address{font-style:normal;line-height:1.7}
footer.site .tel{margin-top:10px}
footer.site .tel a{color:var(--cream);font-family:var(--disp);font-weight:800;letter-spacing:.06em;text-decoration:none}
footer.site nav ul{list-style:none;display:flex;flex-direction:column;gap:8px}
footer.site nav a{color:rgba(247,239,226,.85);text-decoration:none;font-size:15px}
footer.site nav a:hover{color:var(--gold)}
.socials{grid-column:1/-1;margin-top:6px}
.socials a{color:var(--gold);font-family:var(--disp);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:13.5px;text-decoration:none;margin-right:16px}
.footline{grid-column:1/-1;margin-top:18px;font-size:13px;color:rgba(247,239,226,.55)}
/* responsive */
@media (max-width:900px){.hero .wrap{flex-direction:column}.heroart{flex:none;order:-1}.heroart svg{width:min(240px,60vw)}footer.site .wrap{grid-template-columns:1fr}.mapgrid{grid-template-columns:1fr}.mapcell iframe{height:280px}}
@media (max-width:620px){.top .wrap{flex-direction:column;align-items:flex-start}.brand .word{font-size:19px}nav.main{width:100%}nav.main ul{gap:14px}.fields{grid-template-columns:1fr}.sauce{flex-direction:column;align-items:flex-start}.block{padding:40px 0}.story .wrap{flex-direction:column}}
'''

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M50 4l40 46-40 46-40-46Z" fill="#241a17" stroke="#e5a63a" stroke-width="5" stroke-linejoin="miter"/><path d="M50 14c-13 17-22 30-22 41 0 13 9 21 22 21s22-8 22-21c0-11-9-24-22-41Z" fill="#d9481f"/><path d="M50 34c-7 9-11 15-11 21 0 6.5 4.5 11 11 11s11-4.5 11-11c0-6-4-12-11-21Z" fill="#e5a63a"/><path d="M33 62c-3 4-5 7-5 10M67 62c3 4 5 7 5 10" stroke="#f7efe2" stroke-width="4" stroke-linecap="round" opacity=".5" fill="none"/></svg>'''

def write(name, text):
    with open(os.path.join("public", name), "w") as f:
        f.write(text)
    print("wrote", name, len(text.encode()), "bytes")

os.makedirs("public", exist_ok=True)
SITEMAP = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f'<url><loc>{ORIGIN}{p}</loc><lastmod>{DATE}</lastmod></url>\n' for p in ["/", "/menu", "/catering", "/visit", "/contact", "/privacy"])
    + "</urlset>\n")

for path, html in PAGES.items():
    fname = "index.html" if path == "/" else path[1:] + ".html"
    write(fname, html)
write("style.css", CSS)
write("favicon.svg", FAVICON)
write("sitemap.xml", SITEMAP)
write("robots.txt", f"User-agent: *\nDisallow: /thanks\nDisallow: /404\n\nSitemap: {ORIGIN}/sitemap.xml\n")
print("done:", sorted(os.listdir("public")))
