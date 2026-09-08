---
id: ce800ent-machine-information
title: Machine Information - machine type, safety lock, odometer and versions
kind: fact
question: Where do I see the software version and total hours on a Spirit CE800ENT
  elliptical?
asked_as:
- where is the software version on the elliptical
- how do i zero the odometer on the elliptical
- what is the safety lock setting for
keywords:
- machine information
- machine type
- rpm detection
- safety lock
- zeroing
- odometer
- sw version
- fw version
- os version
- ems
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce800ent
  applies_to:
  - ce800ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-engineering-mode-menu
- ce800ent-engineering-mode-settings
- cu900ent-machine-information
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: Section 7-4 Engineering Mode Instructions, Machine Information, p. 33 (printed
    33). This page is a flattened image and was read from raw/page-33.png, not from
    the OCR text
  extracted_at: '2026-09-08'
---

| Control | What the manual says |
|---|---|
| Machine Type | Choose the exercise equipment. **This machine is CE800.** |
| RPM Detection | Shown ON. |
| Safety Lock | **Default OFF.** For an EMS system. |
| Zeroing | Click this key to clear all odometer. |

Read-only on the right of the same screen: **Distance**, **Hour**, **SW Version**, **FW Version**,
**OS Version**. The screenshot shows Distance 11.61 km, Hour 1.16 hr, SW Version `T29_20200312`,
FW Version `V1.0`, OS Version `V1.0` - those are the demonstration machine's values, not a spec.

**The RPM Detection description is wrong.** The manual glosses it as "Turns off the speaker so no
beeping sound is heard", which describes Beep Mode, not an RPM sensor setting. Beep Mode is a
separate control on the Engineering Mode screen. Treat the gloss as a copy-and-paste defect; the
manual says nothing else about what RPM Detection does.

The Engineering Mode Settings table promises this screen will also hold Touch sound, Sleep Mode and
Safety Mode. It does not.
