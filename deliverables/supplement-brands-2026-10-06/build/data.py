"""Content for both deliverables.

Every number and statement here is taken from
reports/patterns/supplement-brands-2026-10-06.md, except the dated timeline
milestones and their evidence tags, which are copied from the timeline tables
in reports/brands/<brand>.md (all dated 2026-10-06). Nothing is estimated.
"""

REPORT_NAME = "supplement-brands-2026-10-06"
TITLE = "What five successful supplement brands have in common"
SUBTITLE = ("Cross-brand patterns: MaryRuth's, Free Soul, Novomins, Vida Glow, SmartyPants")
RUN_DATE = "6 October 2026"
SOURCE_LINE = "Source: Cross-brand pattern report, 2026-10-06 (brand-pattern-finder)"
SOURCE_SCORES = "Source: brand reports' scorecards, 2026-10-06 (1-5 scale); same scores in the pattern report's comparison matrix"
SOURCE_TIMELINE = "Source: timeline tables in the five brand reports, 2026-10-06; dates as reported (several approximate)"

BRANDS = ["MaryRuth's", "Free Soul", "Novomins", "Vida Glow", "SmartyPants"]
BRAND_KEYS = ["mr", "fs", "nv", "vg", "sp"]
BRAND_META = {
    "mr": {"name": "MaryRuth's", "home": "US", "founded": "2014"},
    "fs": {"name": "Free Soul", "home": "UK", "founded": "2017"},
    "nv": {"name": "Novomins", "home": "UK", "founded": "2020"},
    "vg": {"name": "Vida Glow", "home": "Australia", "founded": "2014"},
    "sp": {"name": "SmartyPants", "home": "US", "founded": "2010-11"},
}

CRITERIA = ["Story clarity", "Story-product fit", "Marketing-channel fit",
            "Sales-channel fit", "Overall coherence"]
SCORES = {  # order follows CRITERIA
    "mr": [4, 4, 5, 4, 4],
    "fs": [5, 4, 5, 4, 4],
    "nv": [4, 3, 3, 4, 3.5],
    "vg": [5, 4, 4, 4, 4],
    "sp": [4, 3, 4, 4, 4],
}

CAVEATS = [
    ("Evidence caveat", "All five brand reports were built from search-result snippets, because the "
     "network blocked direct page fetches (brand sites, Forbes, Lloyds, The Grocer, founder interviews "
     "and others). Exact figures, dates and wording have not been checked against full pages. Several "
     "success figures are self-reported (Vida Glow units, Novomins velocity, Free Soul revenue) or "
     "third-party estimates (MaryRuth's revenue from Forbes, SmartyPants revenue from databases). For "
     "this reason no pattern is rated higher than medium, even where all five brands support it."),
    ("Survivorship caveat", "All five brands are successes by their own measure. With no failed or "
     "stalled brands in the set, every shared trait is a correlation, not a proven cause."),
]

SUMMARY = ("All five brands started with a founder's personal problem, proved demand online (own site "
           "and/or Amazon) before entering physical retail, and sell mainly to women buying for themselves "
           "or their families. Within that, the clearest shared lever is a product format or hero that makes "
           "the founding promise visible at a glance (liquid, gummy, sachet, mango greens), which then suits "
           "the brand's lead channel, whether that is TikTok, Amazon thumbnails or a pharmacy or beauty shelf. "
           "Three routes reach success: a marketplace-and-creator mass engine (MaryRuth's, Free Soul, earlier "
           "SmartyPants), a pharmacy-shelf need-state block (Novomins) and prestige-beauty placement backed by "
           "celebrity launches (Vida Glow), with the last two each resting on one brand only. The same warning "
           "signs appear in all five: range sprawl into trend SKUs and claims that run ahead of evidence, which "
           "has already produced lawsuits at SmartyPants and is the main EU/UK exposure for the others. Because "
           "the evidence is snippet-based and the set has no failures, these are medium-confidence correlations; "
           "timing (TikTok Shop, the gummy boom), category growth and founder audiences explain part of the result.")

KEY_FINDINGS = [
    {
        "headline": "All five brands began with a founder's personal problem and proved demand online before physical retail.",
        "stat": "5 of 5", "stat_label": "brands with a founder-problem origin story",
        "conf": "Medium",
        "detail": ("Pill aversion (MaryRuth's), a family health scare (Free Soul), unfinished vitamin tubs "
                   "(Novomins), hair loss (Vida Glow) and a child who would not take vitamins (SmartyPants). "
                   "Story clarity scores 4-5 for every brand, the highest-scoring criterion. Four brands built "
                   "reviews, velocity or virality online first and used it to win retail; the gap between launch "
                   "and major retail was 2-7 years (P1, P3)."),
        "refs": "P1, P3",
    },
    {
        "headline": "The clearest shared lever is a format or hero that makes the promise visible at a glance.",
        "stat": "4 of 5", "stat_label": "brands where the format itself proves the story",
        "conf": "Medium",
        "detail": ("Liquid for 'no pills' (MaryRuth's), gummy for 'kids will take it' and 'easy to remember' "
                   "(SmartyPants, Novomins), a single 100%-collagen sachet (Vida Glow). It works in a 15-second "
                   "video, an Amazon thumbnail or a shelf facing without explanation. Free Soul is the exception: "
                   "it differentiates by audience (women-first), though it still needed a viral hero, Mango Greens "
                   "(17m+ servings), to break out (P2)."),
        "refs": "P2",
    },
    {
        "headline": "Three routes reach success: a mass engine, a pharmacy shelf block and prestige beauty.",
        "stat": "3 routes", "stat_label": "two of them rest on one brand each",
        "conf": "Medium / Early signal",
        "detail": ("Marketplace-and-creator mass engine: MaryRuth's, Free Soul, earlier SmartyPants (medium, 3 brands). "
                   "Pharmacy-shelf need-state block: Novomins (early signal, 1 brand). Prestige-beauty placement with "
                   "celebrity launches: Vida Glow (early signal, 1 brand). SmartyPants also shows a fourth outcome, "
                   "a strategic exit to Unilever (early signal)."),
        "refs": "Success models, P11, P12",
    },
    {
        "headline": "The same warning signs appear in all five: range sprawl and claims that run ahead of evidence.",
        "stat": "5 of 5", "stat_label": "brands with trend-SKU sprawl and claims escalation",
        "conf": "Medium (common) / Early signal (harm)",
        "detail": ("Story-product fit is the lowest or joint-lowest score for four of the five brands. SmartyPants "
                   "already faces two class actions aimed at its core promise (2021 'Complete', 2025 fiber). For the "
                   "other brands no ASA, FTC or court action was found; the risk is mainly that these claims block "
                   "or reshape EU/UK entry (W1, W2)."),
        "refs": "W1, W2",
    },
    {
        "headline": "Treat every pattern as a medium-confidence correlation, not a proven cause.",
        "stat": "0", "stat_label": "failed or stalled brands in the set",
        "conf": "Caveat",
        "detail": ("Evidence comes from search-result snippets, and some success figures are self-reported or "
                   "estimated. Timing (TikTok Shop, the gummy boom), category growth, funding and founder networks "
                   "explain part of the results. Adding failed brands and Spate category data would test the patterns."),
        "refs": "Caveats, Alternative explanations",
    },
]

# Comparison matrix (verbatim from report, lightly split into columns)
MATRIX = {
    "mr": {
        "label": "MaryRuth's (US, 2014)",
        "story": "Founder-problem: health coach whose clients could not take pills (\"liquids until lunch\"); family, clean, mother-founded",
        "hero": "Liquid Morning Multivitamin (sugar-free liquid); 2025 growth hero Liquid Multivitamin + Hair Growth (Lustriva, biotin)",
        "price": "Mid-premium mass (about $31-54 per bottle; deep Amazon deals)",
        "marketing": "Always-on creator programme (1,000+ creators) plus TikTok Shop 24/7 LIVE and Amazon ads",
        "first_sales": "Founder's coaching practice and Amazon (2014-15)",
        "sequence": ["Coaching practice", "Amazon", "DTC", "US natural and mass retail from 2021 (Whole Foods, 800+ Target, Walmart, Costco, Ulta, CVS)", "TikTok Shop from 2024"],
        "seq_note": "EU/UK grey-market only",
        "success": "Scale, profit and founder control: about $600M TTM revenue, about $125M EBITDA, at least $1.5B equity value (Forbes estimate, Aug 2026); family owns about 97%",
        "success_tag": "REPORTED (estimate)",
    },
    "fs": {
        "label": "Free Soul (UK, 2017)",
        "story": "Founder-problem: mother and son after a family health scare; \"female-first nutrition\", how women feel, not how they look",
        "hero": "Started with women's protein powders; viral hero Mango Greens powder (17m+ servings), 7-sachet retail packs",
        "price": "Masstige (about £15 multi, about £30 greens)",
        "marketing": "TikTok organic, LIVE and TikTok Shop (first UK brand with two Super Brand Days, Oct 2024 and Jan 2026)",
        "first_sales": "DTC Shopify with subscription, seeded by gym sampling",
        "sequence": ["DTC", "Amazon UK", "TikTok Shop (by 2024)", "UK mass retail 2024-25 (H&B, Boots, Tesco, Superdrug, Sainsbury's, Waitrose, Ocado)", "Ireland"],
        "seq_note": "No US",
        "success": "Founder-retained revenue growth: £35-42m (2025 to year to Apr 2026), Sunday Times 100 #10, reported EBITDA positive; one angel round",
        "success_tag": "REPORTED",
    },
    "nv": {
        "label": "Novomins (UK, 2020)",
        "story": "Founder-problem: clinician founders (dentist, pharmacologist) saw unfinished, expired vitamin tubs; \"make the healthy choice the obvious choice\"",
        "hero": "Gummy-only range (40+ SKUs); heroes Women's Bio-Balance, Collagen, Magnesium",
        "price": "Mass-premium (£19.99 per 60)",
        "marketing": "Trade and business press, reviews (Trustpilot 4.8, Amazon 5.0); social/creator activity not found",
        "first_sales": "DTC and Amazon UK (2020)",
        "sequence": ["DTC / Amazon", "Chemist Warehouse Ireland (Nov 2022)", "UK Boots, Superdrug, H&B (about 20,000 points claimed)", "Chemist Warehouse Australia (550 stores, c. 2025)", "DE/AT online"],
        "seq_note": "US thin",
        "success": "Bootstrapped growth (£70k savings, Lloyds debt): £3.5m in about 2 years (company figure), Sunday Times 100 #27 (Jun 2026); current revenue not found",
        "success_tag": "REPORTED",
    },
    "vg": {
        "label": "Vida Glow (Australia, 2014)",
        "story": "Founder-problem plus discovery: founder's hair loss, fixed with marine collagen found in Japan",
        "hero": "Natural Marine Collagen 3g sachets (powder); later Pro Collagen+, Collagen Liquid Advance",
        "price": "Prestige beauty (US$50 per 30 sachets)",
        "marketing": "Celebrity launch events per market, founder Instagram, glossy beauty press",
        "first_sales": "DTC Australia (2014)",
        "sequence": ["DTC", "AU health-food wholesale", "China demand (2017)", "2021 global rebrand", "US prestige (Revolve, Neiman Marcus, 2022)", "UK prestige (Harrods, Space NK, Cult Beauty, Sephora UK)", "Sephora AU"],
        "seq_note": "EU light",
        "success": "Units and footprint, mostly self-reported (\"one unit every four seconds\", \"world's No.1 marine collagen brand\"); revenue, funding, ownership not found",
        "success_tag": "Self-reported",
    },
    "sp": {
        "label": "SmartyPants (US, 2010-11)",
        "story": "Founder-problem: parent founders could not find a vitamin that was premium, tasty and affordable; \"all-in-one\"",
        "hero": "Kids multi + omega-3 + D3 gummy; later life-stage, organic, sugar-free gummies",
        "price": "Masstige list price, often value-tier paid price (Amazon deals)",
        "marketing": "Amazon reviews and search ranking; mom influencers; Vitamin Angels 1-for-1 cause",
        "first_sales": "DTC and Amazon (2010-11)",
        "sequence": ["DTC / Amazon", "Natural (Whole Foods, Sprouts)", "Mass and club (30,000+ doors by 2018: Target, Walmart, Costco)", "Unilever (2020)", "Walmart-specific line (2023)"],
        "seq_note": "No EU/UK",
        "success": "Exit: acquired by Unilever (Nov-Dec 2020, terms undisclosed); revenue estimates conflict ($52M 2017; \"over $100M\" pre-exit)",
        "success_tag": "CONFIRMED (exit) / REPORTED (revenue)",
    },
}

# Pattern support. Values: S = supports, X = exception / does not fit, U = not found or unconfirmed
PATTERNS = [
    {"id": "P1", "group": "Shared", "name": "Founder's personal problem is the origin story",
     "count": 5, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "S", "sp": "S"},
     "desc": "Every brand opens with a first-person problem, and the story stays the same for years. Story-clarity scores are 4-5 for all five, the highest-scoring criterion in the set.",
     "exceptions": "None in the set. But this is near-universal in the category, including in brands that fail, so it is probably necessary rather than distinctive."},
    {"id": "P2", "group": "Shared", "name": "Format or hero makes the promise visible at a glance",
     "count": 4, "conf": "Medium",
     "cells": {"mr": "S", "fs": "X", "nv": "S", "vg": "S", "sp": "S"},
     "desc": "The product itself is the proof of the story, so it can be shown in a 15-second video, an Amazon thumbnail or a shelf facing without explanation.",
     "exceptions": "Free Soul differentiates by audience (women-first), not by format; Mango Greens is a flavour and positioning win within an existing format. Partial: Novomins has no single hero, it has a format applied to a 40+ SKU range."},
    {"id": "P3", "group": "Shared", "name": "Demand proven online before physical retail",
     "count": 4, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "X", "sp": "S"},
     "desc": "Each brand built evidence of demand (reviews, sales velocity, social virality) online, then used it to win retail listings. The gap between launch and major retail was 2-7 years.",
     "exceptions": "Vida Glow moved into Australian health-food wholesale within two years of launch; its prestige retail push (2021-22) did follow years of DTC and China demand. Alternative explanation: this is the standard route for any small brand without retail funding."},
    {"id": "P4", "group": "Shared", "name": "Amazon was an early growth engine",
     "count": 3, "conf": "Medium",
     "cells": {"mr": "S", "fs": "U", "nv": "S", "vg": "X", "sp": "S"},
     "desc": "Amazon was a primary channel from the start; reviews and search rank served as both a sales channel and proof for retail buyers.",
     "exceptions": "Vida Glow (Amazon presence unclear, may be a reseller). Free Soul has a 'strong Amazon channel' but its start date is not found. Weakened by heavy Amazon discounting at MaryRuth's and SmartyPants: rank may partly be bought."},
    {"id": "P5", "group": "Shared", "name": "Creators and social commerce drive sales",
     "count": 3, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "U", "vg": "X", "sp": "S"},
     "desc": "The founder's voice is multiplied by creators who resemble the founder or buyer; in the two newest cases sales happen on the same platform (TikTok Shop). MaryRuth's was the #4 TikTok Shop seller in Jan 2025 with 1,000+ creators; Free Soul held two Super Brand Days; SmartyPants ran a mom-influencer programme (26M+ reach).",
     "exceptions": "Novomins: no social or creator evidence found (a gap, not evidence of absence). Vida Glow uses celebrities and founder Instagram instead. Timing explains part: TikTok Shop opened in the UK in 2021 and the US in late 2023."},
    {"id": "P6", "group": "Shared", "name": "Women buy; ranges follow life stages",
     "count": 5, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "S", "sp": "S"},
     "desc": "Every brand sells mainly to women, for themselves or for their families. Need-state naming maps onto how retail fixtures are organised.",
     "exceptions": "None, though SmartyPants and MaryRuth's address the mother as buyer for the family. Women are the majority supplement buyer, so this is close to a category trait."},
    {"id": "P7", "group": "Shared", "name": "Beauty-from-within is a growth extension",
     "count": 4, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "S", "sp": "X"},
     "desc": "Four brands started in or moved into hair, skin and collagen; in two cases that extension became a top seller (MaryRuth's Hair Growth liquid was the #2 TikTok Shop product in Jan 2025; Novomins Collagen gummies are a stated bestseller).",
     "exceptions": "SmartyPants (no beauty line found). Beauty claims carry the highest claim risk (see W2)."},
    {"id": "P8", "group": "Shared", "name": "A trust stack stands in for clinical trials",
     "count": 3, "conf": "Medium",
     "cells": {"mr": "S", "fs": "X", "nv": "S", "vg": "X", "sp": "S"},
     "desc": "None of the five has a published clinical trial on a finished product. Trust comes from certifications (B Corp, Clean Label Project, Vegan Society), contaminant testing, cause programmes, clinician founders or ingredient-supplier studies.",
     "exceptions": "Free Soul (Informed Sport page exists, SKUs unconfirmed; relies on customer surveys); Vida Glow (no certifications found; relies on brand-run, unpublished studies and celebrity)."},
    {"id": "P9", "group": "Shared", "name": "Founder-controlled, capital-light growth",
     "count": 3, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "U", "sp": "X"},
     "desc": "Brands grew on founder money, an angel or debt rather than venture equity: MaryRuth's bootstrapped to about $100M, took PE in 2021 and bought it back with debt in 2024; Free Soul self-funded with one angel round; Novomins used £70k savings plus Lloyds debt.",
     "exceptions": "SmartyPants (crowdfunding, then PE, then sale to Unilever). Vida Glow (funding not found). Profitable founders talk about bootstrapping more, so the trait may be over-reported among winners."},
    {"id": "W1", "group": "Warning", "name": "Range sprawl into trend SKUs",
     "count": 5, "conf": "Medium (common) / Early signal (harm)",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "S", "sp": "S"},
     "desc": "300+ SKUs vs 'make wellness simple' (MaryRuth's); Sculpt and 'glow' vs 'how women feel, not how they look' (Free Soul); NAD+, shilajit and libido vs 'established science' (Novomins); acne, sleep, topicals and a tea collaboration vs 'the marine collagen brand' (Vida Glow); sleep, fiber and pet SKUs vs 'all-in-one' (SmartyPants).",
     "exceptions": "No commercial damage documented yet for any brand. At SmartyPants, sprawl coincides with a post-acquisition period in which it is not named among Unilever's growth leaders (weak signal)."},
    {"id": "W2", "group": "Warning", "name": "Claims escalate beyond the evidence",
     "count": 5, "conf": "Medium (common) / Early signal (consequences)",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "S", "sp": "S"},
     "desc": "'Clinically shown' hair growth on an ingredient-supplier study plus 10,000 mcg biotin (MaryRuth's); survey percentages and 'hormone balance' (Free Soul); disease-adjacent naming such as 'Endo' (Novomins); 'clinically proven' and 'world's No.1' without published data (Vida Glow); 'Complete' and fiber claims (SmartyPants).",
     "exceptions": "SmartyPants faces two class actions (2021 'Complete', 2025 fiber). MaryRuth's had a 2021 infant probiotic recall (safety, not claims). For the other three, no ASA, FTC or court action was found."},
    {"id": "W3", "group": "Warning", "name": "'Premium' story vs deep discounting",
     "count": 3, "conf": "Medium (occurs) / effect not shown",
     "cells": {"mr": "S", "fs": "X", "nv": "S", "vg": "X", "sp": "S"},
     "desc": "List prices say premium while the price paid is often value-tier: MaryRuth's (50% off list on Amazon), SmartyPants (120 ct for $5-9 with coupons), Novomins (H&B 15-20% multibuys).",
     "exceptions": "Vida Glow (only 15% subscription discount found); Free Soul (25% first-order affiliate offers, not persistent). No measured effect on margin; MaryRuth's still reports about 20% EBITDA (Forbes estimate)."},
    {"id": "W4", "group": "Warning", "name": "'Global' story vs unmanaged international",
     "count": 4, "conf": "Medium",
     "cells": {"mr": "S", "fs": "S", "nv": "S", "vg": "X", "sp": "S"},
     "desc": "MaryRuth's (grey-market EU/UK), Free Soul ('4 million women globally', no US), Novomins (US push announced c. 2022, by 2026 only a third-party Amazon listing), SmartyPants (no EU/UK under Unilever).",
     "exceptions": "Vida Glow (official presence in AU, US, UK; EU light)."},
]

ROUTES = [
    {"id": "P10", "name": "Deep home market vs early internationalisation",
     "text": "Three brands scaled almost entirely in one home market and left international sales unmanaged: MaryRuth's (US), SmartyPants (US), Free Soul (UK plus Ireland). Two expanded early through a specific partner or demand pocket: Novomins (Ireland, Australia, Germany via Chemist Warehouse and online pharmacy), Vida Glow (China demand, then US and UK prestige).",
     "conf": "Medium (home market) / Early signal (international)"},
    {"id": "P11", "name": "Retail destination differs: mass/club, pharmacy or prestige beauty",
     "text": "The online-first start is shared, but the retail destination matches price tier and story: mass and club for a family staple (MaryRuth's, SmartyPants, Free Soul's grocery listings), pharmacy and health-store fixtures for a need-state gummy block (Novomins), prestige beauty for a US$50 sachet sold as beauty (Vida Glow).",
     "conf": "Medium (mass) / Early signal (pharmacy, prestige)"},
    {"id": "P12", "name": "Success by exit vs founder-retained scale",
     "text": "SmartyPants succeeded by selling to a strategic buyer; MaryRuth's, Free Soul and Novomins by growing while keeping control. Vida Glow is unknown.",
     "conf": "Early signal (exit route)"},
]

MODELS = [
    {"name": "Marketplace-and-creator mass engine",
     "how": "Visibly different format or positioning, proven on Amazon and/or DTC, scaled through creators and social commerce, then turned into mass, grocery and club listings.",
     "brands": "MaryRuth's (US), Free Soul (UK), SmartyPants (US, pre-TikTok version with Amazon and mom influencers)",
     "keys": ["mr", "fs", "sp"], "conf": "Medium (3 brands)"},
    {"name": "Pharmacy-shelf need-state block",
     "how": "One format (gummy) across many need-state SKUs at one price point, giving retailers a ready-made fixture block; clinician founders and B Corp reassure pharmacy buyers; growth funded by debt and retail partners across countries.",
     "brands": "Novomins (partly SmartyPants in its life-stage mass listings)",
     "keys": ["nv"], "conf": "Early signal (1 brand)"},
    {"name": "Prestige-beauty placement",
     "how": "Supplement sold as beauty: single-ingredient hero, giftable sachets, celebrity launch per market, beauty-retail doors at prestige prices.",
     "brands": "Vida Glow", "keys": ["vg"], "conf": "Early signal (1 brand)"},
    {"name": "Strategic exit",
     "how": "Staged capital (crowdfund, PE, growth equity) matched to staged channels, building a scaled US asset for a strategic buyer.",
     "brands": "SmartyPants", "keys": ["sp"], "conf": "Early signal (1 brand)"},
]

ALTERNATIVES = [
    ("Timing", "TikTok Shop launched in the UK (2021) and US (late 2023) with heavy platform support for early brands; MaryRuth's and Free Soul were early and visible. SmartyPants rode the 2010-2020 rise of gummies and clean label. Vida Glow launched in 2014 as ingestible collagen was emerging, and caught Chinese cross-border demand in 2017. Each brand's main channel or format was growing fast when it entered."),
    ("Category growth", "Gummy supplements grew 7.9% in 2025 (New Hope, US data, cited in the Novomins report); collagen, greens and women's health have been fast-growing need-states. Without Spate category data, brand share gain cannot be separated from category growth for any of the five."),
    ("Funding", "MaryRuth's took PE in 2021 at the point it entered mass retail; SmartyPants raised repeatedly before 30,000 doors; Novomins used Lloyds debt for international retail. Capital access, not strategy alone, may explain the speed of retail rollout."),
    ("Founder audience and networks", "MaryRuth's started with the founder's coaching clients; Vida Glow used the founders' celebrity and fashion network (Rita Ora, later a Typebea co-founder); Free Soul used diaspora and business press. These are hard to copy and could explain early traction as well as any strategy."),
    ("Measurement", "The success evidence is uneven: Forbes estimates (MaryRuth's), company-stated and press-ranked figures (Free Soul, Novomins), unverified unit claims (Vida Glow) and an undisclosed exit price (SmartyPants). Some 'successes' may be smaller than presented."),
]

IMPLICATIONS = [
    ("Choose a format or hero that proves the promise by itself.", "If the product needs a paragraph to explain why it is different, it will not travel on TikTok, Amazon or a retail shelf (P2). Free Soul shows the alternative is a sharp audience position, but it still needed a viral hero (Mango Greens) to break out."),
    ("Plan the online-proof-then-retail sequence on purpose.", "Collect reviews, velocity and repeat data in DTC and Amazon first, then take them to retail buyers (P3, P4). Design trial-size sachets or small packs for retail entry price points, as Free Soul and Vida Glow did (early signal)."),
    ("Match the retail destination to price and story.", "Mass and club for a family staple, pharmacy for need-state blocks, prestige beauty for a beauty-priced ingestible (P11). Mixing them (Vida Glow at Harrods and at Nasty Gal) creates price and positioning tension."),
    ("Build the trust stack early.", "With no finished-product clinical trial, certifications, testing and clinician or educator voices did the reassuring for three brands (P8). For a nutricosmetics launch, a finished-product study would be a real differentiator, since none of the five has one."),
    ("Write claims for the strictest target market from day one.", "All five brands' growth claims would need rework under EFSA/GB rules (W2). A brand planning UK/EU sales should build heroes around authorised nutrient claims (e.g. biotin, zinc, vitamin C for skin, hair and collagen formation) rather than adapting US claims later."),
    ("Set rules for line extension.", "Every brand drifted into trend SKUs (W1). A simple test: does the new SKU make the founding promise more tangible, or does it borrow a trend? Beauty extensions worked commercially for four brands (P7) but carry the highest claim risk."),
    ("Treat social commerce as a time-limited window.", "Early entry to a new platform (TikTok Shop) gave outsized reach to two brands; that advantage shrinks as the platform fills. A new brand should look for the next under-served channel rather than assume the same result."),
]

GAPS_EVIDENCE = [
    "All five brand reports rest on search-result snippets because direct fetches were blocked. Rerunning brand-analyst with full page access (brand sites, Forbes, Lloyds, The Grocer, Sunday Times 100, Unilever releases) would let several patterns move from medium to high confidence. Priorities: Free Soul and Novomins revenue (Companies House, Sunday Times 100 entries), Vida Glow revenue and ownership (ASIC), SmartyPants post-2020 performance.",
    "Channel revenue mix (Amazon vs DTC vs retail vs TikTok Shop) was not found for any brand. This is the single biggest gap for P4 and P5.",
    "Novomins social and creator activity was not found; checking it would confirm or break P5.",
]
GAPS_BRANDS = [
    ("Care/of", "US personalised vitamin packs, Bayer-owned; reported closed in 2024: DTC subscription model with no retail-first proof; a test of P3."),
    ("Sugarbear", "US influencer-led hair gummies: celebrity and influencer demand without a trust stack; a test of P5 and P8."),
    ("Goli Nutrition", "US ACV gummies, viral c. 2020, reported financial difficulties later: a format-led hero that rode a trend; a test of P2 and of the timing explanation."),
    ("SmartyPants after 2020", "Already in the set: a possible stall under corporate ownership, which could be tested with Unilever segment data and Spate brand search."),
    ("Comparable survivors", "Bears With Benefits and Vitabiotics gummies (UK pharmacy model, alongside Novomins), Absolute Collagen or The Beauty Chef (prestige ingestible beauty, alongside Vida Glow), Women's Best (women-first, alongside Free Soul), Olly (US gummy mass, alongside SmartyPants)."),
]
GAPS_BRANDS_NOTE = "These are candidates from general category knowledge, not from the brand reports; their status should be checked by a brand-analyst run before use."
SPATE = [
    ("\"gummy vitamins\" / \"gummies supplements\"", "US, UK, AU", "Category tailwind behind SmartyPants and Novomins (P2, timing)"),
    ("\"liquid vitamins\" / \"liquid multivitamin\"", "US, UK", "Whether MaryRuth's grew with or ahead of its format"),
    ("\"marine collagen\" / \"collagen supplement\" / \"liquid collagen\" / \"collagen sachets\"", "US, UK, AU", "Collagen tailwind for Vida Glow, Novomins and Free Soul; format shifts"),
    ("\"greens powder\" / \"mango greens\"", "UK, US", "Whether Free Soul rode or created the greens wave"),
    ("\"supplements for women\" / \"women's multivitamin\" / \"perimenopause supplements\"", "UK, US", "Size and growth of the women's need-state all five target (P6)"),
    ("\"hair growth supplement\" / \"biotin\" / \"hair vitamins\"", "US, UK", "The beauty-extension pattern (P7)"),
    ("\"creatine for women\" / \"magnesium gummies\" / \"magnesium glycinate\"", "UK, US", "Trend SKUs and the timing of entry"),
    ("\"kids vitamins\" / \"prenatal vitamins\"", "US, UK", "Life-stage demand behind MaryRuth's and SmartyPants"),
    ("Brand-name searches for all five brands, side by side", "US, UK, AU, DE", "Relative brand trajectories; whether TikTok Shop events, retail listings and celebrity launches lifted search; whether SmartyPants stalled after 2020"),
]

SOURCES = [
    ("reports/patterns/supplement-brands-2026-10-06.md", "Cross-brand pattern report (brand-pattern-finder), run 2026-10-06. The source of every finding in this document."),
    ("reports/brands/maryruths.md", "MaryRuth's brand strategy report, 2026-10-06. Scorecard and timeline dates."),
    ("reports/brands/freesoul.md", "Free Soul brand strategy report, 2026-10-06. Scorecard and timeline dates."),
    ("reports/brands/novomins.md", "Novomins brand strategy report, 2026-10-06. Scorecard and timeline dates."),
    ("reports/brands/vida-glow.md", "Vida Glow brand strategy report, 2026-10-06. Scorecard and timeline dates."),
    ("reports/brands/smartypants.md", "SmartyPants brand strategy report, 2026-10-06. Scorecard and timeline dates."),
]
SOURCES_NOTE = ("Each brand report lists its own primary sources (for example Forbes, BusinessWire, TikTok Newsroom, "
                "Lloyds, The Grocer, NutraIngredients, Unilever and Morgan Stanley releases, retailer listings), all "
                "accessed 2026-10-06, mostly through search-result extracts. No Spate export was in inputs/category/ "
                "and Revuze was not used. No new research was done for these deliverables.")

# Timeline milestones (from brand-report timeline tables). type: online | retail | social | capital | marker
# year is the plotting position; 'when' is the date as written in the source.
TIMELINE = {
    "mr": [
        (2014.75, "Fall 2014 (or 2015)", "First 90 bottles of Liquid Morning Multivitamin, sold in the practice and on Amazon", "online", "REPORTED"),
        (2021.3, "April 2021", "Whole Foods launch; Whole Foods Rookie Supplier of the Year", "retail", "REPORTED"),
        (2021.5, "2021", "800+ Target stores", "retail", "REPORTED"),
        (2021.6, "5 Aug 2021", "Butterfly (PE) invests; founder keeps a significant stake", "capital", "CONFIRMED"),
        (2024.6, "15 Aug 2024", "Butterfly sells most of its stake back to the founder family", "capital", "CONFIRMED"),
        (2025.05, "Jan 2025", "#4 on TikTok Shop US, $5.3M monthly sales; Hair Growth liquid the #2 product", "social", "REPORTED"),
        (2026.65, "27 Aug 2026", "Forbes: about $600M TTM revenue, at least $1.5B value", "marker", "REPORTED (estimate)"),
    ],
    "fs": [
        (2017.0, "2017 (brand says; sources say 2016-2018)", "Founded by Rohini and Arjun Sofat after a family health scare; self-funded; gym sampling", "online", "CONFIRMED / conflict noted"),
        (2021.0, "2021", "Seven-figure investment from Sonny Arora (angel), who joins the board", "capital", "REPORTED"),
        (2024.8, "22-25 Oct 2024", "First TikTok Shop Super Brand Day", "social", "CONFIRMED"),
        (2024.5, "2024-25 (date not found)", "Wider UK retail: Boots, Tesco, Superdrug, Sainsbury's, H&B; greens and CreaGlow in Ocado and Waitrose", "retail", "REPORTED"),
        (2026.02, "5-11 Jan 2026", "Second Super Brand Day; Sculpt protein launched first on TikTok Shop", "social", "CONFIRMED"),
        (2026.3, "Year to Apr 2026", "£42m sales; 10th in Sunday Times 100", "marker", "REPORTED"),
    ],
    "nv": [
        (2020.0, "2020", "Founded with £70k of savings; DTC launch", "online", "REPORTED"),
        (2022.9, "24 Nov 2022", "Ireland launch: full range in Chemist Warehouse IE", "retail", "REPORTED"),
        (2023.4, "May 2023", "B Corp certified (score 88.1)", "marker", "REPORTED"),
        (2024.0, "c. 2023-2025", "UK listings at Boots, Superdrug, H&B (exact dates not found)", "retail", "REPORTED"),
        (2025.05, "c. Jan 2025", "Chemist Warehouse Australia listings; 550 stores", "retail", "REPORTED"),
        (2026.45, "Jun 2026", "Sunday Times 100, #27", "marker", "REPORTED"),
    ],
    "vg": [
        (2014.0, "2014", "Launched with Natural Marine Collagen (Sydney, DTC)", "online", "REPORTED"),
        (2015.0, "~2014-2016", "Wholesale to Australian health-food stores begins", "retail", "REPORTED"),
        (2017.0, "2017", "Breakthrough with Chinese consumers; brand 'goes global'", "marker", "REPORTED"),
        (2021.4, "May 2021", "'Vida Glow 2.0' global rebrand and launch, Sydney (Rita Ora et al.)", "marker", "CONFIRMED / REPORTED"),
        (2022.15, "23 Feb 2022", "US launch event; US retail at Revolve, Shen Beauty, Carbon Beauty", "retail", "REPORTED"),
        (2022.85, "Nov 2022", "One-month pop-up at Harrods Knightsbridge", "retail", "REPORTED"),
    ],
    "sp": [
        (2010.8, "Fall 2010", "First products on sale", "online", "REPORTED"),
        (2013.6, "Aug 2013", "Raises $2.59M on CircleUp", "capital", "REPORTED"),
        (2015.55, "Jul 2015", "North Castle Partners invests", "capital", "REPORTED"),
        (2018.1, "Feb 2018", "30,000+ stores incl. Target, Walmart, Costco, Whole Foods", "retail", "REPORTED"),
        (2020.9, "25 Nov / 23 Dec 2020", "Unilever announces and completes acquisition", "capital", "CONFIRMED"),
        (2021.55, "Jul 2021", "'Complete' class action filed", "marker", "REPORTED"),
        (2023.4, "5 Jun 2023", "Gelatin-free multis at Walmart, $13.98", "retail", "CONFIRMED"),
        (2025.95, "Dec 2025", "Fiber class action", "marker", "REPORTED"),
    ],
}
EVENT_TYPES = {
    "online": "Online launch",
    "retail": "Physical retail",
    "social": "Social commerce",
    "capital": "Funding / ownership",
    "marker": "Other milestone",
}

# Sales-channel presence, as listed in the pattern report's "channel expansion sequence" and
# "first sales channel" columns. F = first channel, Y = listed, N = stated as absent/unofficial, "" = not listed.
CHANNEL_COLS = ["DTC site", "Amazon", "TikTok Shop", "Natural / health store", "Mass, grocery, club", "Pharmacy", "Prestige beauty", "Official international"]
CHANNELS = {
    "mr": ["Y", "F", "Y", "Y", "Y", "Y", "", "N"],
    "fs": ["F", "Y", "Y", "Y", "Y", "Y", "", "Y"],
    "nv": ["F", "F", "", "Y", "", "Y", "", "Y"],
    "vg": ["F", "", "", "Y", "", "", "Y", "Y"],
    "sp": ["F", "F", "", "Y", "Y", "", "", "N"],
}
CHANNEL_NOTES = {
    "mr": "Started in the founder's coaching practice and on Amazon; CVS for pharmacy; EU/UK grey-market only.",
    "fs": "H&B (health store), Boots and Superdrug (pharmacy), Tesco, Sainsbury's, Waitrose, Ocado (grocery); international = Ireland; no US.",
    "nv": "H&B (health store); Boots, Superdrug and Chemist Warehouse (pharmacy); international = Ireland, Australia, DE/AT online; US thin.",
    "vg": "AU health-food wholesale; Revolve, Neiman Marcus, Harrods, Space NK, Cult Beauty, Sephora; official in AU, US, UK; EU light. Amazon presence unclear.",
    "sp": "Whole Foods and Sprouts (natural); Target, Walmart, Costco (30,000+ doors by 2018); no EU/UK.",
}
