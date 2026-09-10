---
id: spirit-strength-csi-console-auto-exit-two-minutes
title: 'The Auto Exit timer ends the session by itself after about two minutes without activity'
kind: fact
question: 'How long does the Spirit i-Strength console wait before ending a session on its own on the csi-cpsp and csi-lrow?'
asked_as:
- 'why did the i-strength machine end my workout'
- 'how long before the spirit touchscreen times out'
- 'the screen went back to the start while i was resting'
- 'auto exit on the i-strength what is it'
keywords:
- 'auto exit'
- 'timeout'
- 'idle'
- 'two minutes'
- 'session ends'
- 'no activity'
- 'screen reset'
- 'rest between sets'
- 'countdown'
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-strength-csi-console-summary-screen
- spirit-strength-csi-console-home-screen
source:
  ref: spirit-strength-csi-cpsp-owners-manual
  locator: 'TRAINING MODES - PURE CONTINUED, closing sentence of the Summary Screen page, printed p. 30 of the CSI-CPSP book (PDF p. 31) and p. 26 of CSI-LROW (PDF p. 27). The two books'' console chapters are identical at 99.2% word level from the PDF text layer, the only differences being the page numbers; every figure below was read from the native text layer of both PDFs and cross-checked against a 300 dpi tesseract --psm 4 render of the page.'
  extracted_at: '2026-09-10'
---

> The console includes an Auto Exit timer which will automatically end the session of the machine if
> there is **no activity for about 2 minutes**.

**Two minutes is the only figure the book gives, and it prints it once.** The Pure summary page
carries it in full. The Eccentric and Isokinetic summary pages repeat the same sentence but stop at
*if there is no activity* with no figure at all, and the Elastic summary page omits the sentence
entirely. That is a printing lapse rather than four different behaviours: it is one console and one
timer, described in full on the first of the four pages.

The Summary Screen header shows the timer running as an **AUTO EXIT IN** countdown, so a user resting
between sets can see how long is left before the machine returns itself to the Home Screen.

Anything counted as activity restarts it. The manual does **not** say what counts as activity, does
**not** say whether the timer runs on the Setup and Progress screens as well as the Summary screen,
and gives **no** way to change or disable it - it is not among the settings a facility can adjust.

Pressing **Repeat Set** before it expires starts another set with all measurements reset to zero.
