---
id: spirit-ct800ent-console-machine-information-gs-beep-sleep-safety-zeroing
title: 'Machine Information: GS Mode and Safety Mode default off, Beep on, a 30-minute
  Sleep Mode, a Zeroing key and the version fields'
kind: fact
question: What is on the Machine Information screen of a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill?
asked_as:
- how do i turn off the touch sound on the treadmill
- how do i stop the console going to sleep
- how do i zero the mileage on the ent console
- where do i find the software version
keywords:
- machine information
- machine type
- gs mode
- beep mode
- touch sound
- sleep mode
- safety mode
- zeroing
- sw version
- os version
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800ent-machine-information
- cu900ent-machine-information
- ct900ent-console-machine-information-machine-type-gs-mode-child-lock
see_also:
- spirit-ct800ent-console-engineering-mode-seven-submenus
- ct900ent-sleep-mode-auto-shutoff
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT section 8-8 Engineering Mode Instructions, PDF p. 45 (printed
    45); text.md lines 868-881. The CT850ENT-2022 service manual prints the same page
    word for word on its PDF p. 46, text.md lines 887-900
  extracted_at: '2026-09-11'
---

The Machine Information entry of engineering mode sets **Machine type, GS Mode, Beep Mode, Sleep
Mode, Safety Mode and Zero mileage**. The five numbered lines, word for word:

| Setting | What the manual says |
|---|---|
| GS Mode | The default is **OFF**. |
| Beep Mode | Touch sound; the default is **ON**. |
| Sleep Mode | The default is **OFF**. When set ON, "the electronic watch" goes to sleep after **30 minutes** without any operation. Press any key to wake it. |
| Safety Mode | The default is **OFF**. |
| Zeroing | Click this key to clear all mileage. |

Read-only on the right of the screenshot: **Machine Type**, **Distance** (11.61 km), **Hour**
(1.16 hr), **SW Version** `T29_20200312`, **FW Version** `V1.0`, **OS Version** `V1.0`. Those are the
demonstration machine's values, not a spec. The screen also carries a **Safety Lock** switch.

**GS Mode is not explained here.** On the CU900ENT bike, and on every LED Spirit treadmill that
prints it, GS Mode is the grade return - ON means the incline does not go back to zero on pause
(`cu900ent-machine-information`, `ct900-engineering-mode-menu`). These two books give no definition.

**Safety Mode is not explained either.** The same manuals' error table lists a **SAFETY LOCK**
message - "Children's Safety mode is on. Press and hold Incline ▲ key to relieve this mode" - which
is the message this switch produces; that message is held with the error cards.

"The electronic watch" is the source's own term for the console throughout the Dyaco manuals.

The elliptical in this console family lists RPM Detection instead of GS Mode and Beep on its version
of this screen (`ce800ent-machine-information`).

