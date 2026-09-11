---
id: ct1000ent-2023-errors-error-code-list-25-hex-codes
title: Every hex error code the console can show, twenty-five indexes carrying the
  inverter mnemonics
kind: spec
question: What error codes can a Spirit ct1000ent-2023 treadmill display and what
  does each one mean?
asked_as:
- list of error codes for my spirit ct1000ent
- what do the 0x codes mean on the ent treadmill
- spirit touchscreen treadmill error code table
keywords:
- error code
- error code table
- hex codes
- 0x
- inverter
- mcu board
- mnemonic
- list
- index
- ent
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct1000ent-2023
  applies_to:
  - ct1000ent-2023
  section: errors
  code: '*'
  model_number:
  - '210854'
authority: 3
not_to_be_confused_with:
- ct900ent-errors-error-code-messages-list
- ct850-2020-inverter-error-code-list
- ct900-error-code-table
see_also:
- ct1000ent-2023-errors-0x01-eeprom-error
- ct1000ent-2023-errors-0x02-ntcf
- ct1000ent-2023-errors-0x03-le1
- ct1000ent-2023-errors-0x04-oe
- ct1000ent-2023-errors-0x05-pfct
- ct1000ent-2023-errors-0x06-gf
- ct1000ent-2023-errors-0x07-oh
- ct1000ent-2023-errors-0x08-ol
- ct1000ent-2023-errors-0x09-ol1
- ct1000ent-2023-errors-0x0a-olo
- ct1000ent-2023-errors-0x0b-prer
- ct1000ent-2023-errors-0x0c-eer
- ct1000ent-2023-errors-0x0d-le
- ct1000ent-2023-errors-0x0e-esp
- ct1000ent-2023-errors-0x0f-drvf
- ct1000ent-2023-errors-0x10-lp
- ct1000ent-2023-errors-0x11-hp
- ct1000ent-2023-errors-0x12-ht
- ct1000ent-2023-errors-0x20-incline-error
- ct1000ent-2023-errors-0x31-uart-error
- ct1000ent-2023-errors-0x40-speed-error
- ct1000ent-2023-errors-0x41-short-circuit-error
- ct1000ent-2023-errors-0x42-motor-volt-error
- ct1000ent-2023-errors-0x43-controller-error
- ct1000ent-2023-errors-0x44-external-volt-error
- cu900ent-error-code-log
- spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter
source:
  ref: spirit-treadmill-ct1000ent-2023-service-manual
  locator: CT1000ENT 2023 service manual Error Code List, PDF p. 12, text.md lines
    270-306
  extracted_at: '2026-09-11'
---

Twenty-five codes, each with its own card; this table is only the index. It is printed once, in the service manual, with no solution column, and the only tool the chapter names is a multi-meter.

| Error Code | Description | Remarks Error |
|---|---|---|
| 0x01 | EEPROM Error | By Inverter Error |
| 0x02 | ntcF | By Inverter Error |
| 0x03 | LE1 | By Inverter Error |
| 0x04 | OE | By Inverter Error |
| 0x05 | PFCt | By Inverter Error |
| 0x06 | GF | By Inverter Error |
| 0x07 | OH | By Inverter Error |
| 0x08 | OL | By Motor Error |
| 0x09 | OL1 | By Inverter Error |
| 0x0A | OLO | By Inverter Error |
| 0x0B | PrEr | By Inverter Error |
| 0x0C | 0C:EEr | By Inverter Error |
| 0x0D | LE | By Inverter Error |
| 0x0E | ESP | By Inverter Error |
| 0x0F | drvF | By Inverter Error |
| 0x10 | LP | By Inverter Error |
| 0x11 | HP | By MCU Board Error |
| 0x12 | Ht | By MCU Board Error |
| 0x20 | Incline error | By incline motor Error |
| 0x31 | Uart error | By MCU Board Error |
| 0x40 | Speed error | By MCU Board Error |
| 0x41 | Short circuit error | By Inverter Error |
| 0x42 | Motor volt error | By motor line Error |
| 0x43 | Controller error | By Inverter Error |
| 0x44 | External volt error | By Inverter Error |

Three things to know before using it.

- **Codes 0x02 to 0x12 are the inverter's own mnemonics** - `ntcF`, `LE1`, `OE`, `GF`, `OH`, `OL`, `OL1`, `OLO`, `PrEr`, `EEr`, `ESP`, `LP`, `HP`, `Ht` - which the CTSBS900 owner's manual explains one by one with remedies (`ctsbs900-le1-inverter-low-voltage` and its siblings) and which the CT800 2020 service bulletin prints in brackets beside the CT850's `E-xxH` codes (`ct850-2020-inverter-error-code-list`). This book gives the letters and nothing else.
- **The CT900ENT, the other touch-screen AC treadmill, numbers the same faults differently** - two-digit hex, `01H` to `29H`, with plain-English descriptions (`ct900ent-errors-error-code-messages-list`). `0x03 LE1` here is `01H Low voltage trip` there.
- **`INCLINE ERR` is a message, not `0x20`.** It has its own section and check table (`spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter`), and the matrix's `INCLINE window displays "E3"` row is an XT leftover.

The Error Code Log in engineering mode stores these and clears with ten presses (`cu900ent-error-code-log`).
