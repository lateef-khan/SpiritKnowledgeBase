---
id: spirit-strength-errors-no-troubleshooting-page-printed
title: Eleven strength owner's manuals print no troubleshooting page, while the other twenty-eight print one that is two rows long
kind: fact
question: Does a Spirit strength owner's manual have a troubleshooting section or a list of error codes?
asked_as:
- where is the troubleshooting section in my spirit strength manual
- list of error codes for a spirit weight machine
- my spirit strength machine has no troubleshooting page
- what does the code on my spirit strength machine mean
keywords:
- troubleshooting
- error code
- fault table
- not printed
- diagnosis guide
- owner's manual
- strength
- absence
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
  - csi-cpsp
  - csi-lrow
  - st800dr3
  - st800fi
  - st800ft
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- srvo-error-code-table
- srvo-display-not-lighting-up
- srvo-wireless-switch-not-connecting
see_also:
- spirit-strength-errors-contents-heading-promises-troubleshooting
- spirit-strength-errors-resistance-box-cable-jam-over-8-kg
- spirit-strength-errors-no-mechanical-fault-remedy
- spirit-strength-errors-rep-counter-and-timer-does-not-turn-on
- spirit-strength-errors-rep-counter-turns-on-but-does-not-count
- spirit-xe-errors-no-error-codes-printed
- spirit-commercial-bike-errors-no-error-codes-printed
- spirit-climber-errors-no-error-codes-printed
- spirit-rower-errors-no-error-codes-printed
source:
  ref: spirit-strength-csf-aabb-owners-manual
  locator: 'Absence, checked across all 39 Spirit strength owner''s manuals. For the eleven named here (327 pages) the check was: a whole-word count of error, fault and troubleshoot over the full text; the contents page of each; and a 300 dpi tesseract --psm 4 render of the last seven pages of every one of the eleven, compared word for word against the same pages'' text layer.'
  extracted_at: '2026-09-10'
---

**The word *error* appears in exactly one of the thirty-nine Spirit strength owner's manuals, and the
word *fault* in none of them.** No machine in this range displays or prints an error code of any
kind. If a caller reports a code, it did not come from a Spirit strength manual - establish what is
actually on the screen before answering.

## Which machines have a troubleshooting page and which do not

| Family | Machines | Troubleshooting page? |
|---|---|---|
| **CSS** selectorized single station | 19 | **Yes** - one page, two rows, both about the rep counter |
| **CSD** dual station | 9 | **Yes** - the same page, word for word |
| **CSF** functional and bench | 6 | **No** |
| **CSI** | 2 | **No** |
| **ST800** | 3 | **No** |

The two rows the twenty-eight do print are
`spirit-strength-errors-rep-counter-and-timer-does-not-turn-on` and
`spirit-strength-errors-rep-counter-turns-on-but-does-not-count`. **Both are about the battery-powered
rep counter console and nothing else** - so even on a machine that *has* the page, it answers nothing
mechanical. That gap is `spirit-strength-errors-no-mechanical-fault-remedy`.

## Where the eleven contents pages stop

| Machine | Contents ends at |
|---|---|
| CSF-AABB, CSF-BEXT | Maintenance & Care 15, Exploded View 16, Warranty 17 |
| CSF-FUNT, CSF-HRAC | Maintenance & Care 17, Exploded View 18, Warranty 19 |
| CSF-LEGP | Maintenance & Care 15, Exploded View 16, Warranty 17 |
| CSF-UPRB | Maintenance & Care 14, Exploded View 15, Warranty 16 |
| CSI-CPSP | Maintenance & Care 45, Exploded View 46, Warranty 48 |
| CSI-LROW | Maintenance & Care 41, Exploded View 42, Warranty 44 |
| ST800DR3, ST800FI | General Maintenance 16, Warranty 18 |
| ST800FT | General Maintenance 27, Warranty 31 |

**On CSF-LEGP, CSI-CPSP and CSI-LROW the contents page heads that block "Warranty &
Troubleshooting" and then lists the warranty alone.** That heading is a trap, and it has its own
card: `spirit-strength-errors-contents-heading-promises-troubleshooting`.

## What these eleven print instead

- **CSI-CPSP and CSI-LROW carry one real fault and its remedy**, but it is on the assembly page, not
  in a troubleshooting chapter: pulling the steel cable harder than 8 kg before the resistance box
  and track are assembled can jam the cable inside the box
  (`spirit-strength-errors-resistance-box-cable-jam-over-8-kg`). These are the newest and longest
  books in the range - 48 and 56 pages, a touchscreen console, training modes and settings - and even
  so the words *error*, *err* and *fault* appear in neither of them, not once.
- **ST800FT prints the range's only general fault instruction**, in its pre-assembly section: *"After
  assembly, check all operations for ease of use. If any problems are experienced, first recheck the
  assembly instructions for possible errors made. If more help is needed, call your authorized
  dealer. Be sure to have your serial number ready."* This is the single occurrence of the word
  *error* in all thirty-nine manuals, and it means a mistake made during assembly, not a console
  code. ST800DR3 and ST800FI do not print even this.
- **A preventative maintenance schedule**, on all eleven - a clean/inspect/lubricate table by
  interval. It is an inspection rota, not a diagnosis guide, and it is carded under
  `section: maintenance`.
- **A safety rule about worn parts**, on all eleven - do not use equipment with worn, frayed or
  damaged components, and replace any cable or belt at the first sign of wear. That is a rule rather
  than a remedy, and it is carded under `section: safety`.

## How the absence was checked

Whole-word counts of *error*, *fault*/*faulty* and *troubleshoot\** over the full text of each of the
eleven returned zero, zero and zero, except *troubleshoot* twice each on CSF-LEGP, CSI-CPSP and
CSI-LROW - all four occurrences being the contents heading and its running header - and the one
*errors* on ST800FT quoted above. The last seven pages of every one of the eleven were then rendered
at 300 dpi and read with `tesseract --psm 4` and compared against the same pages' text layer: **no
page gained a table, and no render contains the words *Problem*, *Solution / Cause* or *Diagnosis*.**
The only page where the text layer held materially more than the render was an exploded-view diagram
whose callout numbers are live text.

**Not a single Sole SRVO code applies here.** The Sole strength range is a servo platform with
hexadecimal faults (`srvo-error-code-table`) and is a different brand; nothing filters it out at
retrieval time, so do not serve one to a Spirit strength caller.

The Spirit ellipticals, bikes, climbers and rowers have the same gap, at
`spirit-xe-errors-no-error-codes-printed`, `spirit-commercial-bike-errors-no-error-codes-printed`,
`spirit-climber-errors-no-error-codes-printed` and `spirit-rower-errors-no-error-codes-printed`.
