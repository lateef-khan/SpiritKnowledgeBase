---
id: spirit-strength-specs-i-strength-module-motor-43-n-m-2000-w-and-foc-controller-rs485
title: 'Motor and controller specification of the digital resistance module: a 43
  N m, 2000 W, 435 rpm DC servo motor with a magnetic encoder, and an FOC controller
  on RS-485 at 115200 bps accurate to 5% plus or minus 0.12 N m'
kind: spec
question: What are the motor and controller specifications of the Spirit i-Strength
  digital resistance module?
asked_as:
- how much torque does the i-strength motor make
- i strength motor specs
- what is the controller accuracy on the csi machines
- is the i-strength motor ip rated
keywords:
- motor specification
- controller specification
- 43 n-m
- 2000 w
- 435 rpm
- foc
- rs485
- '115200'
- magnetic encoder
- ip42
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-specs-no-weight-stack-rating-printed
see_also:
- spirit-strength-specs-i-strength-module-electronic-system-block-diagram
- spirit-strength-specs-i-strength-has-no-weight-stack
- spirit-strength-specs-machine-weight-and-overall-dimensions
source:
  ref: spirit-strength-i-strength-resistance-module-maintenance-manual
  locator: Chapter 6. Specification of critical component, 2. Motor and Controller
    configuration plan, PDF pp. 24-25 (printed 24-25), text.md lines 552-660, native
    tables (OCR supplement 894-941 confirms the p. 25 figures)
  extracted_at: '2026-09-11'
---

The only rating anywhere in the i-Strength books for what the machine can resist. The owner's
manuals print no weight-stack figure because there is none
(`spirit-strength-specs-i-strength-has-no-weight-stack`,
`spirit-strength-specs-no-weight-stack-rating-printed`); the module's maintenance manual rates the
motor instead.

**Controller**

| Item | Printed |
|---|---|
| Heat dissipation | Natural cooling via bottom aluminum plate |
| Communication | **RS485**, baud rate **115200 bps** |
| Control accuracy | **5% +/- 0.12 N-m** |
| Service life | **5000 hours** |
| Ambient temperature | **-10 C to 45 C** |
| Control method | **FOC (Field-Oriented Control)** |
| Functions | Single-motor drive |
| Protection | Over-voltage, under-voltage, over-current, over-temperature, encoder fault, brake resistor fault, and three-phase short-circuit of the motor during power loss |

**Motor**

| Item | Printed |
|---|---|
| Type | **DC servo inner rotor motor**, 3-phase, **12 slots, 10 poles** |
| Position feedback | **Magnetic encoder**; rotation CW/CCW |
| Duty cycle | **S3** (IEC 60034-1); insulation **class H (180 C)** |
| Rated torque / peak torque | **43 N-m** / **>= 43 N-m** |
| Rated speed / peak speed | **435 rpm** / **651 rpm** |
| Rated power / efficiency | **2000 W** / **> 83%** |
| No-load current | **< 0.3 A @ 435 rpm** |
| Insulation resistance | 500 VDC / >= 50 megohm |
| Withstand voltage | 1800 VAC / 1 s / <= 5 mA (IEC 60664-1) |
| Protection degree | **IP42** (IEC 60529) |
| No-load noise | <= 60 dB @ 435 rpm (ISO 3745) |
| Dimensions (L x W x H) | **219.5 x 100 x 120 mm** |
| Weight | **6.2 +/- 0.1 kg** |
| Salt spray | 48 hours (ISO 9227) |

**43 N-m is torque at the motor shaft**, not a pull at the handle - the rope reel and any
pulleys between change it, and the book gives no rope-force figure. "Three-phase short-circuit of
the motor during power loss" is the braking that holds the load if the power fails. The block
diagram places this motor on a 320 V DC bus behind an IPM drive
(`spirit-strength-specs-i-strength-module-electronic-system-block-diagram`).

