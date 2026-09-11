---
id: ct900ent-console-machine-information-machine-type-gs-mode-child-lock
title: 'Machine Information: set the machine type first, GS Mode, a child lock and
  a distance reset that both take a 3-second hold on UP, and five version fields'
kind: fact
question: What is on the Machine Information screen of a Spirit ct900ent treadmill
  and why must it be set first?
asked_as:
- how do i unlock the child lock on the ct900ent
- how do i reset the distance and hours on the touchscreen
- what is gs mode on the treadmill
- where do i find the software version on the ent console
keywords:
- machine information
- machine type
- treadmill elliptical bike
- gs mode
- child lock
- speaker
- distance hour reset
- sw version
- os version
- update manager
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-machine-information
- spirit-ct800ent-console-machine-information-gs-beep-sleep-safety-zeroing
see_also:
- ct900ent-settings-menu-access
- ct900ent-console-engineering-mode-settings-max-speed-12-or-20-and-incline-only-calibration
- ct900ent-console-security-distance-lock-100-to-9999-miles-password-2222
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Machine Information, PDF pp.
    25-26 (printed 25-26); text.md lines 347-398
  extracted_at: '2026-09-11'
---

**Set this first.** The manual is explicit: after entering engineering mode (Home pressed ten times -
`ct900ent-settings-menu-access`) the first priority is Machine Information, to set the machine type.
"There are three modes: Treadmill / Elliptical / Bike. The selection must match the actual machine
otherwise it will be unable to operate the machine properly."

| Control | What it does |
|---|---|
| MACHINE TYPE | Treadmill / Elliptical / Bike. Must match the machine. |
| GS MODE | Treadmill mode only. **ON: the incline will not resume. OFF: the incline will resume.** Under Elliptical / Bike mode set it OFF. |
| Child lock | Set ON and the display and buttons lock. **To unlock, press and hold UP for 3 seconds** until it reads OFF. "This is an unlock function once only." |
| SPEAKER | Volume control: ON shows it, OFF hides it. The speaker is optional. |
| DISTANCE / HOUR | To reset them, **press and hold UP for 3 seconds** while in Machine Information. |

Read-only on the same screen: **SW VERSION**, **JNI VERSION**, **FW VERSION**, **OS VERSION**
(the screenshot's value ends in `-1505271750`; its leading characters did not survive extraction)
and **Update Manager** (`V1.2`). Those are the demonstration
machine's values, not a spec.

**Two locks share the three-second UP release**: the child lock here and the distance lock under
Security (`ct900ent-console-security-distance-lock-100-to-9999-miles-password-2222`).

**The owner's manual never opens this screen.** It names Machine Information in the Settings list and
says to refer to the service manual (`ct900ent-settings-menu-access`).

The CU900ENT bike prints this screen word for word (`cu900ent-machine-information`); the
CT800ENT-2022 treadmill's version carries Beep, Sleep and Safety Mode switches instead
(`spirit-ct800ent-console-machine-information-gs-beep-sleep-safety-zeroing`).

