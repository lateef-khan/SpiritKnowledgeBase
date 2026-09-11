---
id: spirit-ct-2020-errors-e-08h-ground-failed
title: 'E-08H: a ground fault on the drive, printed only in a service bulletin'
kind: troubleshooting
question: What does E-08H mean on a Spirit CT800-2020 or CT850-2020 treadmill?
asked_as:
- what does e-08h mean on my treadmill
- treadmill showing e-08h
- ground fault code on the ct850
keywords:
- e-08h
- e08h
- ground fault
- gf
- inverter
- transformer
- wiring
- error code
- service bulletin
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct850-2020
  section: errors
  code: e-08h
authority: 3
not_to_be_confused_with:
- ct850-2020-e-0ah-motor-overcurrent
- ct900-e13-ground-fault
- ctsbs900-gf-inverter-ground-fault
- 70t-2026-errors-e4-ground-fault
see_also:
- ct850-2020-inverter-error-code-list
- ct850-2020-e-50h-console-controller-communication-abnormal
- ctsbs900-gf-inverter-ground-fault
source:
  ref: spirit-treadmill-ct800-2020-e50h-service-bulletin
  locator: spirit-treadmill-ct800-2020-e50h-service-bulletin, TRANSCRIPT, PDF PAGE
    2 (AC list, "For A/C Transforming System")
  extracted_at: '2026-09-11'
---

**This is E-08H, and no CT800 or CT850 manual prints it.** It is not E-0AH, E-0BH or E-0CH, the three overload codes beside it in the same list, and not the CT900's E13 GROUND FAULT or the CTSBS900's GF, which are other machines' codes for the same kind of fault.

The only document that lists it is the photographed error card in the Spirit service bulletin `spirit-treadmill-ct800-2020-e50h-service-bulletin`, headed *ERROR MESSAGE of New CT800&CT850(2020) - For A/C Transforming System*:

| Field | Value |
|---|---|
| Code | E-08H |
| Label, word for word | (GF) Ground failed. |
| Solution, printed once for the whole list | all above are related with transformer error, so please check the wiring first before replace a new transformer. |

`GF` is the inverter's own mnemonic for a ground fault - the same letters the CTSBS900 owner's manual explains as an inverter ground fault (`ctsbs900-gf-inverter-ground-fault`) - and "transformer" is the bulletin's word for the inverter. So: check the motor and inverter wiring for a short to ground before replacing the drive.

The twenty-three codes the manuals do print are on `ct850-2020-inverter-error-code-list`. The bulletin's heading is the only thing that puts an inverter code on the CT800 2020, whose service manual describes a DC-motor controller; on that machine treat this code as the bulletin's claim, not the manual's.
