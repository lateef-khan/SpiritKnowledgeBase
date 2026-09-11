---
id: spirit-xt-errors-error-code-list-eight-codes
title: The eight numbered error codes the console can show, from a missing safety
  key to unstable input power
kind: spec
question: What error codes can a Spirit XT 2015 or XT 2023 treadmill display and what
  does each one mean?
asked_as:
- list of error codes for my spirit xt treadmill
- what do the e codes mean on the xt
- spirit treadmill error code table
keywords:
- error code
- error code table
- list
- index
- safety key
- rpm signal
- over current
- vr voltage
- input power
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt685-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-2024-errors-seven-code-table-with-no-hyphen
- ct850-2020-inverter-error-code-list
- f65-2023-error-code-list
see_also:
- spirit-xt-errors-e0-safety-key-loop
- xt-2023-errors-e1-motor-not-responsive
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor
- spirit-xt-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-2015-errors-e3-incline-vr-out-of-range
- spirit-xt-errors-e4-motor-power-wire-not-plugged
- spirit-xt-errors-e5-console-controller-communication-poor
- spirit-xt-errors-e6-lower-controller-component-fault
- spirit-xt-errors-e7-input-power-unstable
- xt485ent-2023-errors-error-code-list-nine-codes
- xt685ent-2023-errors-error-code-list-seven-codes
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2023 service manual Error Code List, PDF p. 18, text.md lines 346-369;
    XT285 2023 service manual Error Code List, PDF p. 19, text.md lines 348-371; XT385
    2023 service manual Error Code List, PDF p. 20, text.md lines 320-341; XT485 2023
    service manual Error Code List, PDF p. 20, text.md lines 320-341; XT685 2023 service
    manual Error Code List, PDF p. 19, text.md lines 353-376; XT185 2015 service manual
    Error code items, PDF p. 36, text.md lines 557-584; XT285 2015 service manual
    Error code items, PDF p. 37 (printed 36), text.md lines 626-653; XT385 2015 service
    manual Error code items, PDF p. 36, text.md lines 523-546; XT485 2015 service
    manual Error code items, PDF p. 36, text.md lines 522-545
  extracted_at: '2026-09-11'
---

Nine service manuals - the 2015 XT185, XT285, XT385 and XT485 and the 2023 XT185, XT285, XT385, XT485 and XT685 - print the same eight-row table word for word. Each code has its own card; this table is only the index.

| Code | Description |
|---|---|
| E0 | Safety keys dose not insert the safety module. Or safety module is broken. |
| E1 | Display board CPU did not receive the RPM signal. |
| E2 | Over current, over limit current of lower controller and motor. |
| E3 | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |
| E4 | Power wire of motor error. |
| E5 | Communication signal error. |
| E6 | Lower controller error. |
| E7 | Input power error. |

The only tool the chapter names is a **multi-meter**. The 2015 books head the table `Error code items` under `Error Messages / Troubleshooting for Electronic Issues`; the 2023 books head it `Error Code List`. The 2015 XT285 prints `E4 Power wires of motor error` with a plural.

**The XT685 2023 changes one heading and not the table.** Its section 8.1 is headed `Error Message: Display appears PLEASE REPLACE THE SAFETY KEY` rather than `E0`, and its E0 text says the display shows that message; the table above still lists `E0`. Both are on `spirit-xt-errors-e0-safety-key-loop`.

**The two ENT machines print different tables.** The XT485ENT adds `E9` and redefines `E7` as an incline calibration error (`xt485ent-2023-errors-error-code-list-nine-codes`); the XT685ENT stops at `E6` (`xt685ent-2023-errors-error-code-list-seven-codes`).

**The owner's manuals print none of this.** The XT owner's manuals name `E1` in one troubleshooting row and no other code (`xt-2023-errors-e1-motor-not-responsive`).
