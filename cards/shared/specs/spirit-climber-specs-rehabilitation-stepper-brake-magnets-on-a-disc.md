---
id: spirit-climber-specs-rehabilitation-stepper-brake-magnets-on-a-disc
title: Four braking magnets swung against an aluminium brake disc by a gear motor
kind: spec
question: What kind of brake does a Spirit MS300, 7.0S or 7.5S rehabilitation recumbent
  stepper use?
asked_as:
- how does the resistance work on the rehab stepper
- what is the brake on the ms300
- is the 7.5s stepper magnetic
- what part changes the resistance on the 7.0s
keywords:
- brake
- braking magnet
- aluminum brake disc
- gear motor
- flywheel
- eddy current
- permanent magnet
- resistance
- magnet bracket
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-electromagnet-eddy-current-brake
- spirit-climber-2024-specs-resistance-system
- crw800-2024-specs-resistance-system
see_also:
- spirit-climber-specs-isokinetic-twenty-levels
- spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply
- spirit-climber-specs-which-manuals-print-a-parts-list
source:
  ref: spirit-climber-ms300-2021-owners-manual
  locator: Operating principle, printed p. 12, read from a 300 dpi render because the
    last line is not in the text layer; and the MS300 parts list printed pp. 49-56,
    items 11, 43, 44, 45, 48, 61, 62 and 64. The same prose is 7.0S-2025 printed p.
    9 and 7.5S-2025 printed p. 9, and the same item numbers are on the 7.0S parts list
    printed pp. 44-47 and the 7.5S parts list printed pp. 46-49
  extracted_at: '2026-09-10'
---

**A gear motor swings four permanent magnets closer to or further from an
aluminium disc on the flywheel.** All three manuals say so in the same sentence,
in their Operating Principle section:

> When the workload change is requested, a gear motor moves permanent magnets
> closer or further from the aluminum flywheel creating more or less resistance.

The parts list names every piece of it, with the **same item numbers in all three
books**:

| Item | Part |
|---|---|
| **11** | Brake Motor Bracket |
| **44** | Gear Motor |
| **45** | **Braking Magnet, quantity 4** |
| **61** | Aluminum Brake Disc |
| **62** | Magnet Bracket |
| 229 | Power Adapter (the MS300 calls it `Power adapter, 12vdc`) |

**Nothing is energised to brake.** The magnets are permanent; the only powered
part in the brake is the gear motor that moves them. That is why the machine runs
from a 30 watt supply - see
`spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply`.

## The MS300 names a flywheel and the 2025 pair name weight blocks

Item 43 is **`Flywheel mass`** on the MS300 and **`Curved weight Block`, quantity
3** on both the 7.0S and the 7.5S. The MS300 also carries a `Gear motor spring`
(48) and a `Gear motor cable` (64) that the 2025 books number differently. **The
rotating mass is built differently between the 2021 machine and the 2025 pair**,
even though the braking parts are identical. Order by the book in front of you.

## The 8.5S brakes a different way

The 8.5S energises an **electromagnet coil** and induces eddy currents in the
flywheel; there are no permanent magnets and no gear motor in its description.
See `spirit-climber-specs-electromagnet-eddy-current-brake`. **Never answer an
8.5S from this card**, and note that the 8.5S prints no parts list at all, so
these item numbers mean nothing on that machine.

## The commercial steppers use a similar idea and different parts

The CS800, CRS800S and CVC800 also move a magnet against a flywheel with a gear
motor, but their parts lists name a single `Magnet` and a `Flywheel` with
different item numbers, and they are not rehabilitation machines. See
`spirit-climber-2024-specs-resistance-system`. **Item 45 is a Braking Magnet on
this card and something else entirely on a CS800.**

## The MS300's Operating Principle line is cut off in the extraction

`pdftotext` returns the sentence as far as "a gear motor moves permanent magnets
closer or further from the" and stops. The last four words - "aluminum flywheel
creating more or less resistance" - are on the printed page and are readable only
from a 300 dpi render. **Read that page from a render**, and do not report the
sentence as truncated in the source.
