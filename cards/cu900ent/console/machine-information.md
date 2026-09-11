---
id: cu900ent-machine-information
title: Machine Information - machine type, GS mode, child lock, odometer and versions
kind: fact
question: How do I set the machine type on a Spirit CU900ENT or CR900ENT bike?
asked_as:
- how do i set the machine type on the bike console
- how do i clear the total distance on the bike
- how do i unlock the child lock on my spirit bike
keywords:
- machine information
- machine type
- gs mode
- child lock
- speaker
- distance hour
- sw version
- fw version
- os version
- update manager
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900ent-2021
  - cu900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-engineering-mode-menu
- cu900ent-security-distance-lock
- cu900ent-engineering-mode-settings
- ce800ent-machine-information
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Setting and Operation for Engineering Mode, p. 25 (printed 25) and p. 26
    (printed 26). Page 26 is a flattened image and was read from raw/page-26.png,
    not from the OCR text. The CR900ENT-2021 service manual, Machine Information,
    PDF pp. 24-25 (printed 24-25), text.md lines 272-316 and the OCR supplement for
    PDF page 25, prints the same page word for word. Same three machine types, same
    GS MODE, child lock and DISTANCE/HOUR reset, and the same demonstration values
    (SW VERSION V12 12/09/2015, OS VERSION ...1505271750).
  extracted_at: '2026-09-08'
---

Set this **first**, before anything else in engineering mode.

| Control | What it does |
|---|---|
| Machine Type | Three modes: **Treadmill / Elliptical / Bike**. The selection must match the actual machine or the machine will not operate properly. |
| GS MODE | **Treadmill mode only.** ON means the incline will not resume; OFF means the incline will resume. **Under Elliptical / Bike mode, set it OFF.** |
| Child lock | Set ON and the display and buttons lock and cannot be used. To unlock, **press and hold UP for 3 seconds** until it reads OFF. This is a one-time unlock. |
| SPEAKER | Volume control. ON shows it, OFF hides it. **The speaker is optional.** |
| DISTANCE / HOUR | To clear them, **press and hold UP for 3 seconds** while in Machine Information. |

Read-only version fields on the same screen: **SW VERSION** (screenshot shows `V12 12/09/2015`),
**JNI VERSION** (`V1.0`), **FW VERSION** (`0.49`), **OS VERSION** (`A0-R0.2-B01-1505271750`) and
**Update Manager** (`V1.2`). Those are the demonstration machine's values, not a spec.

The `JNI VERSION` field is a Java native-interface version; the OCR of this page reads it as
"UNI VERSION", which is wrong - the screenshot says JNI.

Two different things are both unlocked by holding UP for 3 seconds: the child lock here, and the
distance lock under Security.

**The CR900ENT-2021 service manual is this book with the model name changed.** Its engineering-mode chapter runs one PDF page earlier than the CU900ENT's and prints the page this card rests on word for word, so the card covers both machines. Same three machine types, same GS MODE, child lock and DISTANCE/HOUR reset, and the same demonstration values (SW VERSION V12 12/09/2015, OS VERSION ...1505271750).
