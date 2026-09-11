---
id: xterra-errors-e3-gear-motor-did-not-leave-zero-within-4-seconds-of-start
title: 'E3 means the gear motor did not leave its zero point within 4 seconds of Start:
  replace the gear motor'
kind: troubleshooting
question: What does error E3 mean on an Xterra recumbent bike or elliptical with a
  gear motor, and how is it fixed?
asked_as:
- xterra recumbent bike e3
- e3 error on my xterra elliptical after pressing start
- fs150 e3
- sb240 error 3
keywords:
- e3
- error 3
- gear motor
- zero point
- level one
- 4 seconds
- start button
- replace gear motor
- resistance
facets:
  brand:
  - xterra
  product_line: '*'
  model: '*'
  applies_to:
  - fs150-2016
  - sb150-2018
  - sb240-2023
  - sb250-2024
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list
- xterra-treadmill-errors-e2-over-rated-current-for-3-seconds
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- xterra-tr-errors-e2-incline-position-error
- xterra-tr-errors-e3-incline-error-owner-checks
- e25-2023-e3-ramp-error
- e25-2023-e2-gear-motor-failure
see_also:
- xterra-errors-e1-monitor-cannot-read-the-gear-motor-signal
- xterra-errors-e2-computer-cannot-interface-with-the-eeprom-ic-chip
- xterra-errors-no-tension-computer-wires-not-connected-properly
source:
  ref: xterra-bike-sb150-2018-owners-manual
  locator: SB150 OM Trouble Shooting, PDF p. 24 (printed 22); text.md lines 711-777;
    SB250 OM Trouble Shooting, PDF p. 25 (printed 23); text.md lines 806-872; FS150
    OM (scan) Trouble Shooting, PDF p. 24 (printed 22), OCR supplement; text.md lines
    1001-1062; SB240 OM ERROR MESSAGES, PDF p. 41 (printed 40); text.md lines 1258-1281
  extracted_at: '2026-09-11'
---

**This is E3 on the SB150 / SB250 / SB240 recumbent bikes and the FS150 elliptical, which share one Dyaco
console family.** It is not the Xterra treadmill E3 (incline VR out of range), not the TR-series E3 (incline error),
and not the Sole E25 E3 (ramp). These machines have no incline; their E3 is a gear-motor start-up check.

**What it means.** The SB240 book: *After 4 seconds by start mode, the computer detects the faulty motor did
not leave the zero point, then the LCD bar displays "E3".* The SB150, SB250 and FS150 books word the same
check as the cause:

| Cause | Solution |
|---|---|
| The gear motor cannot read the signal change from level one within 4 seconds after pressing the start button. | Replace gear motor |

E1 is the same motor failing to report *during* a workout or at power-on
(`xterra-errors-e1-monitor-cannot-read-the-gear-motor-signal`), and its cable-and-pin check is worth making
before a gear motor is ordered for an E3 as well; the books print no such step under E3.

