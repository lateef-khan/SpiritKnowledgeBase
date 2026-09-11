---
id: ce900ent-console-machine-information-machine-type-gs-mode-child-lock-speaker-and-versions
title: Machine Information sets the machine type, a treadmill-only GS mode, a child
  lock released by holding Up for three seconds, the speaker, and clears the odometer
kind: procedure
question: How do I set the machine type, release the child lock or reset the odometer
  on a Spirit ce900ent elliptical?
asked_as:
- how do i unlock the child lock on the ce900ent
- how do i reset the odometer on the ce900ent
- ce900ent machine type setting
- what is gs mode on the ce900ent
keywords:
- machine information
- machine type
- gs mode
- child lock
- hold up three seconds
- speaker
- distance hour reset
- odometer
- sw version
- os version
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: console
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with: []
see_also:
- ce900ent-console-engineering-mode-seven-settings-entries-machine-information-first
- ce900ent-console-security-distance-lock-100-to-9999-miles-password-2222
- cu900ent-machine-information
- ce800ent-machine-information
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Machine Information, PDF pp.
    25-26 (printed 25-26); text.md lines 351-399, with the screenshots in the OCR
    supplements for PDF pages 25 and 26, lines 1648-1707, and a 100 dpi render of
    page 26
  extracted_at: '2026-09-11'
---

Set this **first**, before anything else in engineering mode
(`ce900ent-console-engineering-mode-seven-settings-entries-machine-information-first`).

| Control | What it does |
|---|---|
| Machine Type | Three modes: **Treadmill / Elliptical / Bike**. The selection must match the actual machine or the machine will not operate properly. |
| GS MODE | **Treadmill mode only.** ON means the incline will not resume; OFF means the incline will resume. **Under Elliptical / Bike mode, set it OFF.** |
| Child lock | Set ON and the display and buttons lock and cannot be used. To unlock, **press and hold UP for 3 seconds** until it reads OFF. "This is an unlock function once only." |
| SPEAKER | Volume control. ON shows it, OFF hides it. **The speaker is optional.** |
| DISTANCE / HOUR | To clear them, **press and hold UP for 3 seconds** while in Machine Information. |

Read-only version fields on the same screen: **SW VERSION** (screenshot shows `V12 12/09/2015`),
**JNI VERSION** (`V1.0`), **FW VERSION** (`0.49`), **OS VERSION** (`A0-R0.2-B01-1505271750`) and
**Update Manager** (`V1.2`). Those are the demonstration machine's values, not a spec.

**GS mode has nothing to drive on this elliptical.** It is a treadmill incline setting printed in
every book of this console family; the instruction that matters here is the one to leave it OFF.

**Two different things are both unlocked by holding UP for 3 seconds**: the child lock here, and
the distance lock under Security
(`ce900ent-console-security-distance-lock-100-to-9999-miles-password-2222`).

**This page is printed word for word in the CU900ENT and CR900ENT bike books**
(`cu900ent-machine-information`), with the same demonstration values. The CE800ENT's version of the
screen is `ce800ent-machine-information`.
