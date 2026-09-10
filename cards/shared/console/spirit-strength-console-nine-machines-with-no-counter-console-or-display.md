---
id: spirit-strength-console-nine-machines-with-no-counter-console-or-display
title: 'Nine strength machines carry no console, no rep counter and no display of any kind'
kind: fact
question: 'Do the Spirit CSF functional and bench units and the three ST800 units have a console, a rep counter or a display?'
asked_as:
- 'does the spirit functional trainer have a screen'
- 'where is the rep counter on my back extension bench'
- 'my flat incline bench has no display is that normal'
- 'does the dumbbell rack come with a counter'
keywords:
- 'no console'
- 'no display'
- 'no counter'
- 'no rep counter'
- 'no screen'
- 'no battery'
- 'no timer'
- 'functional trainer'
- 'dumbbell rack'
- 'bench'
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csf-aabb
  - csf-bext
  - csf-funt
  - csf-hrac
  - csf-legp
  - csf-uprb
  - st800dr3
  - st800fi
  - st800ft
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-console-rep-and-time-counter-two-windows-two-resets
- spirit-strength-csi-console-home-screen
see_also:
- spirit-strength-console-rep-and-time-counter-two-windows-two-resets
- spirit-strength-console-counter-runs-on-two-c-batteries
- spirit-strength-errors-no-troubleshooting-page-printed
source:
  ref: spirit-strength-csf-aabb-owners-manual
  locator: 'Whole manual, all nine books: CSF-AABB 21 pp., CSF-BEXT 24 pp., CSF-FUNT 24 pp., CSF-HRAC 24 pp., CSF-LEGP 23 pp., CSF-UPRB 23 pp., ST800DR3 24 pp., ST800FI 24 pp., ST800FT 36 pp. Contents pages carry no console or counter entry; every page of all nine was rendered at 200 dpi and read with tesseract --psm 4 on 2026-09-10.'
  extracted_at: '2026-09-10'
---

**None of these nine machines has a console.** No display, no rep counter, no timer, no battery and
no electrical connection of any kind is described anywhere in their manuals. Nothing on any of them
shows reps, time, weight moved or calories.

The nine are the six **CSF** functional and bench units - CSF-AABB adjustable ab bench, CSF-BEXT back
extension, CSF-FUNT functional trainer, CSF-HRAC half rack, CSF-LEGP leg press and CSF-UPRB upright
bench - and the three **ST800** units, ST800FI flat incline bench, ST800FT functional trainer and
ST800DR3 dumbbell rack.

## The absence was checked three ways

| Check | Result |
|---|---|
| Loose-word search of the extraction for console, display, monitor, counter, battery, LCD, LED, screen, Bluetooth | 0 hits on all nine |
| The same search allowing spaces between the letters, because `pdftotext` letter-spaces headings | 0 hits on all nine |
| Every page of all nine PDFs rendered at 200 dpi and read with `tesseract --psm 4`, then searched again | 0 hits on all nine; no page is a flattened image hiding a console section |
| Contents page | CSF books list Product Registration, Warning/Safety, Assembly, Maintenance & Care, Exploded View, Warranty and nothing else. No counter page, no cable routing diagram, no troubleshooting page |

The render sweep was run because these books do hide text in pictures elsewhere - it is how the
range prints its exercise instructions - so a word count alone would not have settled it.

## Two things that look like a contradiction and are not

**The warranty table on the CSF-FUNT and CSF-HRAC books names a "Counter-Timer" in its one-year
column.** That column is boilerplate shared with the CSD dual-station table; it names a part these
two machines do not have. Do not read it as evidence of a counter.

**The cover and the product registration page of every CSF book carry a QR code.** It is the
warranty registration code - *scan to quickly and easily register your new Spirit Fitness unit* - and
it is on the CSS, CSD and CSI books too; see `spirit-strength-warranty-registration`. It is not an
app, not a workout link and not a console feature. The three ST800 books print no QR code anywhere.

## Where a Spirit strength machine does have one

The nineteen CSS selectorized stations and the nine CSD dual stations carry a two-window battery rep
and time counter. The two CSI machines carry a full touchscreen. Neither belongs to any machine on
this card.
