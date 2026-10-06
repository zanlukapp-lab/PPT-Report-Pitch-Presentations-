# Learnings: design

One dated line per lesson: `- YYYY-MM-DD: ...`

- 2026-10-06: Keep all content in one build/data.py and generate both the .docx and the .html from it; numbers then cannot drift between deliverables.
- 2026-10-06: Word TOC: render to PDF with LibreOffice, read heading pages with pdftotext, and pre-fill the TOC field result (two passes). The TOC is correct on open and still updatable.
- 2026-10-06: python-docx tables ignore cell widths in LibreOffice unless tblGrid gridCol values and a fixed tblLayout are also set.
- 2026-10-06: Keep confidence tags out of heading text (put them in a "Confidence:" line below), or they leak into the TOC.
- 2026-10-06: Five key-finding callouts fit one A4 page at 9pt body with a stat column; 10pt overflowed.
- 2026-10-06: matplotlib subtitles: place with va="top" at 1 - 0.40in/fig height; a fixed 0.925 overlapped the title on shorter figures. Wrap long source lines.
- 2026-10-06: Pattern reports have no time series; good chart substitutes are "brands supporting each pattern" bars, a pattern-by-brand Yes/No/? heat map, and a milestone timeline from the brand reports' dated tables.
- 2026-10-06: Channel presence from text: show blank as "not listed (not proof of absence)", separate from a stated "No".
- 2026-10-06: HTML deck check: Playwright with executable_path=/opt/pw-browsers/chromium-*/chrome-linux/chrome (pip playwright revision differs); test 1440x900, 1024x768 and 390px, flag slides needing vertical scroll, and click-test every control.
- 2026-10-06: Inline grid-template-columns styles beat media queries; use a class for layout variants so phone layout collapses.
- 2026-10-06: Reset a detail panel when a filter tab changes, or it shows a hidden brand's item.
