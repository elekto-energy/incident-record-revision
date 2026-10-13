# Can We Trust the Incident Record? - revised research version v4b

Revised research version (14 October 2026) of the report submitted to Track 2 of the AI Incident Response Sprint (Apart Research and CeSIA, 11-13 September 2026).

- **Historical competition entry:** [Can We Trust the Incident Record? | Apart Research](https://apartresearch.com/sprints/projects/can-we-trust-the-incident-record-w8t0)
- **Original repository (unchanged):** https://github.com/elekto-energy/incident-record-claim-matrix, commit [`d4e123c9b5df2e3e70e1332d3b92f006bc41a4c4`](https://github.com/elekto-energy/incident-record-claim-matrix/commit/d4e123c9b5df2e3e70e1332d3b92f006bc41a4c4)

The submitted report and its claim-evidence matrix are not changed by this revision. Corrections to them are listed in Appendix A of the revised report.

Author: Joakim Eklund, Organiq Sweden AB, Stockholm.

## Contents

| Path | What it is |
|---|---|
| `REPORT_v4b.pdf` | The revised report (9 pages). |
| `REPORT_v4b.md` | The Markdown text the PDF was rendered from. |
| `review/QUOTE_CHECK_2026-10-14.json` | Result of the quote check: 33 quotations, each with source, locus, match count and source SHA-256. |
| `review/norm.py` | Text extraction and normalisation used by the quote check. |
| `review/quotes.py` | The list of the 33 quotations. |
| `sources/<ID>/CAPTURE_<ID>.json` | Capture record per source: requested URL, HTTP status, time, tool, and SHA-256 of what was received. |
| `sources/<ID>/response_headers.txt` | HTTP response headers, for HF-27JUL, METR-26AUG and OAI-PDF only (see below). |
| `LICENSE` | Creative Commons Attribution 4.0 International (CC BY 4.0), legal code. |
| `LICENSE-MIT` | MIT License, for the two scripts in `review/`. |
| `SHA256SUMS.txt` | SHA-256 of every other file in this package. |

| File | SHA-256 |
|---|---|
| `REPORT_v4b.pdf` | `61db53ed180e9cc8b20d1ddbdec4fc5ff8d685fe93705b01142ad0996a3cc7fd` |
| `REPORT_v4b.md` | `ece412296f95dc07fb7d669bc030406c75d02b793d361949d63baf594a748cb3` |


## Approval status

Appendix D of the report says that the author's final approval is PENDING. That was the state when the text was written. The author approved this version for publication on 14 October 2026, with its stated research limitations. The report was not changed after approval, so its SHA-256 is the one given above.

## Sources

| ID | URL | Status on 2026-10-13 |
|---|---|---|
| HF-27JUL | https://huggingface.co/blog/agent-intrusion-technical-timeline | captured (HTTP 200) |
| OAI-21JUL | https://openai.com/index/hugging-face-model-evaluation-security-incident/ | not captured (HTTP 403, bot challenge) |
| OAI-26AUG | https://openai.com/index/hugging-face-incident-and-the-road-ahead/ | not captured (HTTP 403, bot challenge) |
| OAI-PDF | https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf | captured (HTTP 200) |
| METR-26AUG | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ | captured (HTTP 200) |

The captured source files themselves are third-party content and are not included. Each capture record gives the SHA-256 and size of the bytes received, so a copy fetched from the URL can be compared. A page that has changed since 13 October 2026 will not match.

The response headers of the two OpenAI blog requests are not included because they contain a cookie set by the site's bot protection. Their SHA-256 values remain in the capture records.

## Quote check

The 33 quotations in `review/quotes.py` were matched against text extracted from the preserved source copies and normalised as in `review/norm.py`:

- PDF: page text from pypdf 5.9.0.
- HTML: scripts and styles removed, tags replaced by spaces, entities decoded.
- In both: runs of whitespace, including U+00A0, collapsed to one space.

A quotation counts as matched only if it occurs exactly once in the normalised text. All 33 did. The method, script hashes and per-quotation results are recorded in `review/QUOTE_CHECK_2026-10-14.json`.

### Reproducibility

The package does not contain a complete, runnable pipeline for the quote check:

- `review/quotes.py` only defines the list of quotations, and `review/norm.py` only defines the extraction and normalisation functions.
- The short loop that counted occurrences and wrote the JSON was not kept as a file and is not included.
- `review/norm.py` contains a path constant `S` that points to the author's former working directory and has to be changed.
- The source copies are not included. Copies fetched today match the recorded SHA-256 only if the publications have not changed since 13 October 2026.
- The results depend on the text extraction of pypdf 5.9.0. The JSON records Python 3.13.16.

To repeat the check, a reader needs byte-identical copies of the three captured sources at the paths named in the JSON (`sources/<ID>/body.html` or `body.pdf`), the path constant changed, and a counting loop of their own that follows the rule recorded in the JSON. The JSON records the rule (a match is exactly one occurrence) and the locus convention (the page for the PDF, the character offset in the normalised text for HTML). It does not say whether PDF occurrences are counted per page or over the whole document; the test below counted over all pages.

While this package was being prepared, that procedure was tried once. It used byte-identical source copies, the two scripts unchanged except for `S`, and a counting loop of about fifteen lines. It reproduced all 33 recorded results (match count, locus and source) under Python 3.13.16 and pypdf 5.9.0. The loop used in that test is not part of this package.

What the check does not show: a match shows that the words occur in the identified source version. It does not show that they are true or that they were interpreted correctly. Section 2.2 of the report lists the two quoted passages that fall outside this check. The JSON refers to a separate review record for the semantic assessment, and that record is not part of this package.

Appendix B of the report refers to the author's research record. The parts of that record published here are `review/` and `sources/`.

## Limitations

The report states its own limits, chiefly in Section 6 and Appendix D:

- The claim states were assigned by one analyst with AI assistance.
- No independent human expert review has been performed.
- The section of OpenAI's blog post cited for C-10 was checked by an AI-assisted reading (GPT-6), which is not bound to preserved bytes. GPT-6 is developed by OpenAI, a party to the incident.
- Matrix rows other than those named in the report were not re-checked.

## Not included

- Raw copies of the sources.
- The author's internal working records and earlier drafts.
- The two OpenAI response-header files.

## License

- **Report and records.** CC BY 4.0, as for the original submission (see `LICENSE`). This covers the report (`REPORT_v4b.pdf`, `REPORT_v4b.md`), this README, `review/QUOTE_CHECK_2026-10-14.json` and `sources/*/CAPTURE_*.json`. Attribute to Joakim Eklund and link to this repository.
- **Scripts.** `review/norm.py` and `review/quotes.py` are under the MIT License (see `LICENSE-MIT`).
- **Not covered.** Neither licence covers third-party material:
  - Passages quoted from the primary sources, in the report, in `review/quotes.py` and in the JSON, remain the work of their authors and are reproduced as quotations.
  - The primary sources are not included, and no licence is claimed for them.
  - `sources/*/response_headers.txt` are responses from the source servers, and no licence is claimed for them.
