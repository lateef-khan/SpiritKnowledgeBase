---
id: xterra-tr-errors-ls-no-speed-signal-for-8-seconds
title: 'LS: the treadmill has not received a speed signal for 8 seconds, and the belt
  that moves then stops is sent to calibration'
kind: troubleshooting
question: What does LS mean on an Xterra tr64-2024 or tr66-2021 treadmill, and what
  should I do?
asked_as:
- ls on my xterra treadmill
- tr66 shows ls after start
- belt moves then stops shows ls
keywords:
- ls
- lost speed
- speed signal
- 8 seconds
- calibration
- motor not responsive
- contact service
- owner's manual
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr64-2024
  - tr66-2021
  section: errors
  code: ls
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list
- f60-2016-ls-message
see_also:
- xterra-tr-errors-owner-error-messages-ls-console-memory-and-incline
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- sole-ls-error
- spirit-xt175-errors-ls-error-after-belt-moves
source:
  ref: xterra-treadmill-tr66-2021-owners-manual
  locator: TR6.6 OM Error Messages, PDF p. 30 (printed 28); text.md lines 1178-1206;
    TR6.6 OM Service Checklist - Diagnosis Guide, PDF p. 29 (printed 27); text.md
    lines 1117-1178; TR6.4 OM Error Messages, PDF p. 25 (printed 23); text.md lines
    919-947; TR6.4 OM Service Checklist - Diagnosis Guide, PDF p. 24 (printed 22);
    text.md lines 859-919
  extracted_at: '2026-09-11'
---

On the TR6.6 and TR6.4 the lost-speed message is **LS**, not E1. *Error Messages:* **LS: The treadmill hasn't received a speed signal for 8 seconds.**

The *Service Checklist* row *Motor is not responsive after pressing Start* tells the owner what to do with it:

1. If the belt moves but stops after a short time and the display shows "LS", **run calibration.**
2. If you press Start and the belt never moves, and then the display shows LS, **contact service.**

The calibration is the Engineering Mode procedure printed under the error list (Start and Speed 5 keys held 5 seconds while installing the safety key; wheel 63; 0.5 to 12.0 mph; incline 15) - a console card. On these two machines E1 is a console memory fault (`xterra-tr-errors-e1-console-memory-or-cpu-fault`). Every other Xterra treadmill reports lost speed as E1 (`xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`); the Sole books and Spirit XT175 use LS the same way as this one (`sole-ls-error`, `spirit-xt175-errors-ls-error-after-belt-moves`).
