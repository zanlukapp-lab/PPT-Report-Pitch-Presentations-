"""Build the self-contained HTML presentation. Run: python3 build_html.py"""
import os, json
import data as D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), D.REPORT_NAME + ".html")

payload = {
    "title": D.TITLE, "run_date": D.RUN_DATE, "source_line": D.SOURCE_LINE,
    "source_scores": D.SOURCE_SCORES, "source_timeline": D.SOURCE_TIMELINE,
    "brand_keys": D.BRAND_KEYS, "brand_meta": D.BRAND_META, "criteria": D.CRITERIA, "scores": D.SCORES,
    "key_findings": D.KEY_FINDINGS, "matrix": D.MATRIX, "patterns": D.PATTERNS, "routes": D.ROUTES,
    "models": D.MODELS, "alternatives": D.ALTERNATIVES, "implications": D.IMPLICATIONS,
    "gaps_evidence": D.GAPS_EVIDENCE, "gaps_brands": D.GAPS_BRANDS, "gaps_brands_note": D.GAPS_BRANDS_NOTE,
    "spate": D.SPATE, "sources": D.SOURCES, "sources_note": D.SOURCES_NOTE, "caveats": D.CAVEATS,
    "timeline": D.TIMELINE, "event_types": D.EVENT_TYPES,
    "channel_cols": D.CHANNEL_COLS, "channels": D.CHANNELS, "channel_notes": D.CHANNEL_NOTES,
}
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
js = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
html = tpl.replace("/*__DATA__*/null", js)
open(OUT, "w", encoding="utf-8").write(html)
print("saved", OUT, len(html), "bytes")
