---
id: spirit-ent-bike-console-machine-information-rpm-detection-safety-lock-zeroing
title: 'Machine Information: the machine type, an RPM Detection switch, a Safety Lock
  that defaults off, a Zeroing key and the version fields'
kind: fact
question: Where do I see the software version or zero the odometer on a Spirit CR800ENT-2023
  or CU800ENT-2022 bike?
asked_as:
- where is the software version on the ent bike
- how do i zero the odometer on the touchscreen bike
- what is the safety lock setting for on the cu800ent
- what does rpm detection do on the spirit bike
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
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800ent-machine-information
- cu900ent-machine-information
- spirit-ct800ent-console-machine-information-gs-beep-sleep-safety-zeroing
see_also:
- spirit-ent-bike-console-engineering-mode-six-submenus
- spirit-ent-bike-console-engineering-mode-units-beep-30-minute-sleep-and-5-minute-pause
- ce800ent-machine-information
source:
  ref: spirit-bike-cr800ent-2023-service-manual
  locator: CR800ENT section 7-4 Engineering Mode Instructions, Machine Information,
    PDF p. 33 (printed 33); text.md lines 508-518, screenshot read from the OCR supplement
    for PDF page 33. The CU800ENT-2022 service manual prints the same page on its
    PDF p. 33, text.md lines 501-511, with "this machine is CU800" in place of CR800
  extracted_at: '2026-09-11'
---

| Control | What the manual says |
|---|---|
| Machine Type | Choice exercise equipment. **This machine is CR800** in the CR800ENT book, **CU800** in the CU800ENT book. |
| RPM Detection | "Turns off the speaker so no beeping sound is heard." Shown ON. |
| Safety Lock | **The default is OFF.** For EMS system. |
| Zeroing | Click on this key to clear all odometer. |

Read-only on the right of the same screen: **Distance** (11.61 km), **Hour** (1.16 hr), **SW Version**
`T29_20200312`, **FW Version** `V1.0`, **OS Version** `V1.0`. Those are the demonstration machine's
values, not a spec.

**The screenshot is the elliptical's.** In both bike books the Machine Type field of the picture
reads **CE800**, while the sentence beside it says the machine is CR800 or CU800. The page was
lifted from the CE800ENT service manual (`ce800ent-machine-information`) and only the sentence was
edited. Set the type to the bike you are standing at, not to what the picture shows - the menu card
says the selection must match the actual machine.

**The RPM Detection description is wrong.** "Turns off the speaker" describes Beep Mode, which is a
separate control on the Engineering Mode screen. Treat the gloss as a copy-and-paste defect; the
manual says nothing else about what RPM Detection does.

The Engineering Mode Settings table promises this screen will also hold GS Mode, Touch sound and
Sleep Mode. It does not (`spirit-ent-bike-console-engineering-mode-six-submenus`).
