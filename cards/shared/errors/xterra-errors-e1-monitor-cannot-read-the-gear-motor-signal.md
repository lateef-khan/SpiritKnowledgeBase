---
id: xterra-errors-e1-monitor-cannot-read-the-gear-motor-signal
title: 'E1 means the monitor cannot read the signal from the gear motor: cables and
  pins, then the gear motor, then the motor wire length'
kind: troubleshooting
question: What does error E1 mean on an Xterra recumbent bike or elliptical with a
  gear motor, and how is it fixed?
asked_as:
- xterra recumbent bike e1
- e1 error on my xterra elliptical
- sb150 shows e1 and resistance wont change
- sb240 e1 error 1
keywords:
- e1
- error 1
- gear motor
- level change
- resistance
- count signal
- 4 seconds
- tension motor
- motor wire
- replace gear motor
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
  code: e1
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
see_also:
- xterra-errors-e2-computer-cannot-interface-with-the-eeprom-ic-chip
- xterra-errors-e3-gear-motor-did-not-leave-zero-within-4-seconds-of-start
- xterra-errors-no-tension-computer-wires-not-connected-properly
source:
  ref: xterra-bike-sb150-2018-owners-manual
  locator: SB150 OM Trouble Shooting, PDF p. 24 (printed 22); text.md lines 711-777;
    SB250 OM Trouble Shooting, PDF p. 25 (printed 23); text.md lines 806-872; FS150
    OM (scan) Trouble Shooting, PDF p. 24 (printed 22), OCR supplement; text.md lines
    1001-1062; SB240 OM ERROR MESSAGES, PDF p. 41 (printed 40); text.md lines 1258-1281
  extracted_at: '2026-09-11'
---

**This is E1 on the SB150 / SB250 / SB240 recumbent bikes and the FS150 elliptical, which share one Dyaco
console family.** It is not the Xterra treadmill E1 (no speed signal), not the TR-series E1 (console memory), and
not the Sole E25 E1 (EEPROM) - on this console the EEPROM fault is E2.

**What it means.** The SB150, SB250 and FS150 books print it as *E1 - Monior* [sic] *cannot read the signal
change (level change or level change cannot reach target position) from the gear motor*. The SB240 book
defines it more precisely, in two states:

- *Normal state:* during a workout, when the monitor did not get the count signal from the gear motor for
  more than **4 seconds**, checked **3 successive times**, the LCD shows E1.
- *Power on state:* the gear motor returns to zero automatically; when the motor signal cannot be detected
  for more than 4 seconds the gear motor's driver is cut off immediately and E1 shows. All other digits and
  function marks go blank and the output signals are cut off too.

**How it is fixed.** The cause-and-solution rows, from the SB150, SB250 and FS150 books:

| Cause | Solution |
|---|---|
| Monitor has a problem | Replace monitor |
| The connection cables from monitor to gear motor are damaged or disconnected. Pins of the connector are bent or not fixed well. | Check all computer plugs and wires are connected firmly. |
| Gear motor damage, or the circuit on the gear motor is abnormal. | Replace gear motor |
| Wire cable from gear motor to magnetic system is too short to drive the magnetic system, or its position is not correct. | Adjust the length of the motor wire to make sure there is enough space to drive the motor. |

The SB240 book prints the definition and no remedy table; the other three print the table and no
definition. They describe one fault on one console, so both halves are here, and the plug-and-pin check
is the sensible first step before any part is ordered. "Monior" is the books' misprint of "Monitor".

