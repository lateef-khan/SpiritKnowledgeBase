---
id: spirit-strength-st800fi-maintenance-wipe-the-sweat-path-after-each-workout
title: Wipe the sweat path with a damp cloth after each workout, and the half-sentence
  about squeaks that the page breaks off
kind: fact
question: What should I do to the Spirit ST800FI flat incline bench after each workout,
  and what does the broken sentence on its maintenance page mean?
asked_as:
- how do i clean the bench after a workout
- my bench squeaks what do i do
- the maintenance page on my bench does not make sense
- what does spirit say to do after using the bench
keywords:
- sweat path
- damp cloth
- after each workout
- squeak
- thump
- clicking
- broken sentence
- printing error
- bench care
facets:
  brand:
  - spirit
  product_line: strength
  model: st800fi
  applies_to:
  - st800fi
  section: maintenance
  code: '*'
  model_number:
  - '808039'
authority: 3
not_to_be_confused_with:
- ct800-2016-maintenance-squeak-thump-or-clicking
- cu900ent-general-maintenance
see_also:
- spirit-strength-st800-maintenance-schedule-with-commercial-and-home-columns
- spirit-strength-maintenance-owner-responsibility-and-repair-log
- ct900-sanitizing-equipment
source:
  ref: spirit-strength-st800fi-owners-manual
  locator: 'GENERAL MAINTENANCE, printed p. 16 (PDF p. 18), the intro paragraph above the
    schedule table. Read from the PDF text layer and then from a 300 dpi render of the same page
    with tesseract --psm 4, specifically to establish whether the broken clause is an extraction
    artefact or is on the paper. It is on the paper: the render shows three printed lines reading
    "Wipe down all areas in the sweat path with a damp cloth after each workout. If a squeak,
    thump, clicking or For best performance, Spirit recommends the following maintenance
    schedule." The ST800DR3, whose table is otherwise identical, prints the same paragraph
    without the first sentence and without the broken clause, which is how the join was located'
  extracted_at: '2026-09-10'
---

**The instruction is one sentence, and the sentence after it is broken on the printed page.**

> **Wipe down all areas in the sweat path with a damp cloth after each workout.** If a squeak,
> thump, clicking or For best performance, Spirit recommends the following maintenance schedule.
> Check the integrity and function of the following parts. Replace all worn components immediately.

## What to tell a customer

**Wipe the sweat path with a damp cloth after every workout.** That is the whole of the
after-workout instruction in this book, and it is genuine — it is the first sentence of the
paragraph and it is complete.

**Then the schedule table** — daily upholstery cleaning, weekly decal, bolt and anti-skid
inspection, six-monthly wax — `spirit-strength-st800-maintenance-schedule-with-commercial-and-home-columns`.

## The broken clause is a printing defect, and it is on the paper

*"If a squeak, thump, clicking or"* stops mid-sentence and the next words are the opening of a
different paragraph. **This was checked on a 300 dpi render of the page, not only in the
extraction**: the join is printed, not an artefact of pdftotext.

The **ST800DR3**, whose maintenance table is identical row for row, prints the same paragraph
**without** the wipe-down sentence and **without** the broken clause. So the ST800FI page is the one
that was edited, and the edit cut a sentence in half.

## Where the missing half comes from, and why you must not supply it

The lost clause is the opening of Spirit's cardio *GENERAL MAINTENANCE* block: *"If a squeak,
thump, clicking or rough feeling develops the main cause is most likely one of two reasons..."*,
which continues into the loose-hardware paragraph, the 90%-of-service-calls figure, the crank arm
nut and the two rear-stabiliser levelling pads adjusted with a 14 mm wrench
(`ct800-2016-maintenance-squeak-thump-or-clicking`).

**Do not complete the sentence for an ST800FI owner.** None of those remedies is printed in this
book, and two of them do not exist on the machine: a flat/incline bench has **no crank arm** and its
manual gives **no levelling pad count and no wrench size**. The bench manual's own answer to a loose
bolt is the schedule row — *Inspect: All Nuts and Bolts, Tighten if needed*, weekly in a facility and
every 3 months at home — and *Replace all worn components immediately*.

`cu900ent-general-maintenance` is the bike version of the same block and is likewise not this
machine's answer.

## Sanitizing is on the next page

Spirit's four sanitizing bullets — **75% isopropyl alcohol** on hard plastics, a conditioner after
sanitizing on upholstery — are printed in full on printed p. 17: `ct900-sanitizing-equipment`.
