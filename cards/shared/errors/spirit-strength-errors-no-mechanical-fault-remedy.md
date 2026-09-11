---
id: spirit-strength-errors-no-mechanical-fault-remedy
title: No strength manual prints a remedy for a sticking stack, a frayed cable, a
  noisy pulley or a pin that will not seat
kind: fact
question: What does a Spirit strength owner's manual say to do about a sticking weight
  stack, a frayed or slipping cable, a noisy pulley or a selector pin that will not
  seat?
asked_as:
- my weight stack is sticking what do i do
- cable is fraying on my spirit weight machine
- pulley is squealing on my strength machine
- selector pin wont go into the weight stack
keywords:
- weight stack
- selector pin
- frayed cable
- pulley noise
- guide rod
- sticking
- slipping
- no remedy printed
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csd-acbe
  - csd-bcte
  - csd-cpsp
  - csd-itot
  - csd-lelc
  - csd-lpce
  - csd-lpsr
  - csd-pfrd
  - csd-puda
  - csf-aabb
  - csf-bext
  - csf-funt
  - csf-hrac
  - csf-legp
  - csf-uprb
  - csi-cpsp
  - csi-lrow
  - css-abdo
  - css-bcur
  - css-bext
  - css-delt
  - css-glut
  - css-latp
  - css-latr
  - css-lext
  - css-lrow
  - css-prlc
  - css-scex
  - css-scpr
  - css-shpr
  - css-slgc
  - css-slgp
  - css-sqsc
  - css-srow
  - css-text
  - css-trot
  - st800dr3
  - st800fi
  - st800ft
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- srvo-error-code-table
see_also:
- spirit-strength-errors-no-troubleshooting-page-printed
- spirit-strength-errors-rep-counter-and-timer-does-not-turn-on
- spirit-strength-errors-rep-counter-turns-on-but-does-not-count
- spirit-strength-errors-resistance-box-cable-jam-over-8-kg
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: 'Absence, checked across all 39 Spirit strength owner''s manuals: the full
    text of each, the one-page TROUBLESHOOTING Diagnosis Guide on the 28 that print
    one, and the maintenance and safety pages of all 39. The CSS-SROW manual has no
    text layer on any page and was read from a 300 dpi tesseract --psm 4 render; the
    CSS-DELT 2026 revision and the CSD-CPSP May 2025 update were checked the same
    way on 2026-09-11 (full text, the OCR supplement of every page, and the TROUBLESHOOTING
    page) and print nothing more'
  extracted_at: '2026-09-10'
---

**Not one of the thirty-nine Spirit strength owner's manuals prints a symptom, a cause and a remedy
for any mechanical part.** There is no answer in the book to a sticking weight stack, a cable that
frays or slips, a pulley that squeals or rumbles, a guide rod that binds, or a selector pin that will
not seat. This is a real gap, not a gap in the search - state it plainly rather than reading an
inspection rule back as though it were a fix.

## Even the twenty-eight machines that have a troubleshooting page do not cover this

The CSS and CSD books print one page headed `TROUBLESHOOTING`, subtitled *Service Checklist Diagnosis
Guide*, with a `Problem` column and a `Solution/ Cause` column. **It is two rows long and both rows
are the battery-powered rep counter console** -
`spirit-strength-errors-rep-counter-and-timer-does-not-turn-on` and
`spirit-strength-errors-rep-counter-turns-on-but-does-not-count`. Nothing on that page touches the
stack, the cables, the pulleys, the pins or the frame. The other eleven machines print no such page
at all (`spirit-strength-errors-no-troubleshooting-page-printed`).

## What the manuals print about these parts instead, and why it is not a remedy

Two things, and neither one diagnoses anything:

- **An inspection rota** in the maintenance section - inspect belts and cables weekly, fasteners,
  handgrips, upholstery and labels monthly, pulleys and the main frame bi-monthly, lubricate the
  guide rods monthly. It tells you *when to look*, never what a symptom means. Carded under
  `section: maintenance`.
- **A safety rule about worn parts** - *"Cables and belts pose an extreme liability if used when
  frayed. Always replace any cable or belt at first sign of wear"*, and do not use a machine whose
  components are worn, frayed or damaged. That is a prohibition and a replace-on-sight instruction,
  not a fault tree. Carded under `section: safety`.

So the printed answer to "the cable looks frayed" is **take the machine out of service and replace
the cable** - a safety instruction. There is no printed answer at all to "the stack sticks", "the
pulley is noisy" or "the pin will not seat": no cause list, no adjustment, no lubricant, no torque
figure, no clearance.

## The one exception, and it is narrow

The two CSI machines print a single mechanical fault with a remedy, and it applies only during
assembly: pulling the steel cable harder than 8 kg before the resistance box and track are fully
assembled can jam or damage the cable inside the box, and the remedy printed is to open the rear
cover and follow after-sales guidance
(`spirit-strength-errors-resistance-box-cable-jam-over-8-kg`). It says nothing about a stack, a
pulley or a pin, and it does not apply to a fully assembled machine in service.

## How the absence was checked

Every one of the thirty-nine manuals was searched for the loose words *problem*, *fault*,
*malfunction*, *diagnos\**, *checklist*, *frayed*, *slipp\**, *stick\**, *noise*, *squeak*, *grind*
and *rattle*, spacing-tolerantly as well, because this extractor letter-spaces headings - it renders
*Service Checklist* as `Service Checklis t` on the CSS-DELT book. Every hit outside the CSS and CSD
troubleshooting page resolved to the safety instruction list, the maintenance rota, the warranty
text, or a parts table naming a pulley or a cable as a component. The CSS-SROW manual carries no text
layer on any of its twenty-seven pages and was read entirely from a 300 dpi render.

**Do not fill this gap with a Sole answer.** The Sole strength range is a different brand on a servo
platform (`srvo-error-code-table`), and nothing filters a brand back out at retrieval time.
