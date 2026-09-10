---
id: spirit-strength-maintenance-no-torque-figure-for-any-fastener
title: Fasteners are inspected and re-tightened on a schedule, and no torque figure
  is printed for any of them
kind: fact
question: What torque should the bolts on a Spirit strength machine be tightened to,
  and how often are they checked?
asked_as:
- what torque do i tighten the bolts to
- how tight should the bolts be on a weight machine
- how often do i re-torque the fasteners
- is there a torque spec for spirit strength equipment
keywords:
- torque
- torque spec
- re-torque
- retighten
- fasteners
- nuts and bolts
- newton metres
- foot pounds
- hardware
- loose bolts
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
  section: maintenance
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-strength-maintenance-schedule-thirteen-actions-daily-to-bi-monthly
- spirit-strength-maintenance-schedule-with-a-bi-annual-column
- spirit-strength-st800-maintenance-schedule-with-commercial-and-home-columns
- spirit-strength-maintenance-owner-responsibility-and-repair-log
source:
  ref: spirit-strength-css-abdo-owners-manual
  locator: 'The interval is the MAINTENANCE row "Inspect: Fasteners", ticked Monthly - css-abdo
    printed p. 21 (PDF p. 22) and the same row in thirty-four of the thirty-six CS books; the
    ST800 books call the row "Inspect: All Nuts and Bolts, Tighten if needed" on their own
    schedule page, Weekly in a facility and 3 Months at home. The absence of a figure was
    established by extracting every page of all thirty-nine PDFs with pdftotext -layout and
    searching for torque, foot-pound, ft-lb, newton metre and N.m, and separately by searching
    each source''s text.md - native layer plus every appended OCR supplement - for the same
    terms. Zero hits in all thirty-nine. The eight machines whose maintenance pages were read
    from a 300 dpi render show no imaged torque table either'
  extracted_at: '2026-09-10'
---

**There is no torque figure in any of the thirty-nine Spirit strength owner's manuals.** Not in the
assembly chapters, not on the maintenance pages, not in the parts lists, not in any table. Searched
for *torque*, *foot-pound*, *ft-lb*, *newton metre* and *N.m* across every page of every book, in
both the PDF text layer and the OCR supplements: zero hits.

## What is printed instead

**An interval and a condition.**

| Manual family | Row | Interval |
|---|---|---|
| CSS, CSD, CSF (except CSF-UPRB), CSI | *Inspect: Fasteners* | **Monthly** |
| CSF-UPRB | — | **no fastener row at all** |
| ST800DR3, ST800FI, ST800FT | *Inspect: All Nuts and Bolts, Tighten if needed* | **Weekly** in a facility, **3 Months** at home |

The ST800FT adds the only narrative instruction in the range:

> Inspect all nuts and bolts for any loosening and tightening if needed. **Go through a
> re-tightening sequence periodically to ensure that all hardware is tensioned proper.**

No sequence is printed and no order is given.

## What to say when someone asks for a number

Say the manual does not give one. **Do not quote a figure from a Sole strength card, from a Spirit
treadmill card or from a general fastener table** — a wrong torque on a weight-stack frame is a
safety matter, and the number would not be Spirit's.

What the manuals do say is that a bolt is tightened *as much as possible* only in their cardio
range, which is a different set of machines; here the instruction is simply *tighten if needed*
against a monthly or weekly inspection.

## Why the interval still matters

The manuals put fastener inspection alongside cable inspection as an owner obligation, and the
repair log has to record it: `spirit-strength-maintenance-owner-responsibility-and-repair-log`. A
gym can build a compliant PM round from the intervals above without a torque figure — that is what
the books expect.
