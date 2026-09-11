---
id: xterra-errors-e2-computer-cannot-interface-with-the-eeprom-ic-chip
title: E2 means the computer cannot interface with its IC chip, an EEPROM fault, and
  the fix is a new monitor
kind: troubleshooting
question: What does error E2 mean on an Xterra recumbent bike or elliptical with a
  gear motor, and how is it fixed?
asked_as:
- xterra recumbent bike e2
- e2 error on my xterra elliptical
- sb250 shows e2 at power on
- sb240 error 2
keywords:
- e2
- error 2
- eeprom
- ic chip
- memory ic
- id code
- replace monitor
- console
- power on
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
  code: e2
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-no-speed-signal-for-10-seconds-owner-list
- xterra-treadmill-errors-e2-over-rated-current-for-3-seconds
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- xterra-tr-errors-e2-incline-position-error
- xterra-tr-errors-e3-incline-error-owner-checks
- e25-2023-e1-eeprom-failure
- e25-2023-e2-gear-motor-failure
- xg400-2016-errors-er1-eeprom-power-cycle-then-replace-console
see_also:
- xterra-errors-e1-monitor-cannot-read-the-gear-motor-signal
- xterra-errors-e3-gear-motor-did-not-leave-zero-within-4-seconds-of-start
- xterra-errors-monitor-does-not-display-adapter-then-computer-wires
source:
  ref: xterra-bike-sb150-2018-owners-manual
  locator: SB150 OM Trouble Shooting, PDF p. 24 (printed 22); text.md lines 711-777;
    SB250 OM Trouble Shooting, PDF p. 25 (printed 23); text.md lines 806-872; FS150
    OM (scan) Trouble Shooting, PDF p. 24 (printed 22), OCR supplement; text.md lines
    1001-1062; SB240 OM ERROR MESSAGES, PDF p. 41 (printed 40); text.md lines 1258-1281
  extracted_at: '2026-09-11'
---

**This is E2 on the SB150 / SB250 / SB240 recumbent bikes and the FS150 elliptical, which share one Dyaco
console family.** It is not the Xterra treadmill E2 (over-current), not the TR-series E2 (incline position), and
not the Sole E25 E2 (gear motor) - on this console the gear-motor faults are E1 and E3.

**What it means.** The SB150, SB250 and FS150 books: *E2 - The computer cannot interface with the IC chip.*
The SB240 book: *When the monitor reads the memory data, if the I.D. code is not correct or the memory IC is
damaged, the monitor will show E2 immediately at power on.*

**How it is fixed.** One row:

| Cause | Solution |
|---|---|
| EEPROM has a problem (EEPROM is installed incorrectly) | Replace monitor |

The monitor (console) is the part; nothing on the frame is involved. The SB240 book prints the definition
only, the other three the row only; it is one fault on one console, so both are here.

