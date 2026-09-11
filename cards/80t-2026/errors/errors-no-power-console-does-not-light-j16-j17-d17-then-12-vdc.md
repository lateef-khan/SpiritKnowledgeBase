---
id: 80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc
title: 'No power on the touchscreen treadmill: wake it first, then mains at the lower
  board inlet, its indicator light and 12 volts out, then 12 volts at the console
  cable'
kind: troubleshooting
question: What do I check when a Spirit 80t-2026 treadmill has no power and the console
  does not light?
asked_as:
- 8.0t screen wont turn on
- no power on my medical treadmill
- treadmill console dead where are the breakers
- 8.0t lower board 12v test
keywords:
- no power
- console does not light
- lower control board
- lcb
- j16 j17
- d17
- 12 vdc
- circuit breaker
- filter
- medical treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: no-power
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
- mt200-2022-errors-no-power-console-does-not-light-five-steps
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
- 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
- 80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: 5. Troubleshooting, No power, console doesn't light, steps 1-4, PDF p.
    23-26, text.md lines 358-384, with the figure captions "Measured 110 VAC or 220
    VAC depending on the mains voltage" from the OCR supplement for page 23 and the
    Check Procedure for 110 VAC Model flow chart from the OCR supplement for page
    27 (lines 384-391)
  extracted_at: '2026-09-11'
---

**On this treadmill the LCB takes the mains directly - there is no separate 24 V power supply module** as on the 8-series bikes and the 8.5S stepper (`85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc`). The chain is mains, then 12 V out of the LCB, then 12 V at the console.

**Step 1.** Press any physical button on the console to wake up the system. If the system does not respond, proceed to the next step. *(The flow chart's first result: the system was in sleep mode.)*

**Step 2.** Measure the AC input voltage at connectors **J16 and J17 on the LCB** (#269). If no AC voltage is measured or the voltage is incorrect, check whether the **power switch** is turned on, whether **either of the two circuit breakers** has been triggered, measure the mains voltage, the voltage at the machine-side end of the power cable, and the voltage at the **input and output terminals of the filter**. If correct AC voltage is measured, proceed to the next step. The figure captions read *Measured 110 VAC or 220 VAC depending on the mains voltage*; the flow chart names the parts on that path as #260, 261, 262, 255, 265, 263.

**Step 3.** Check the **power indicator light D17** on the LCB, and measure **pins 1 and 2 on connector J3 of the LCB** to verify **12 VDC**. If no 12 VDC is measured, **replace the LCB**. If 12 VDC is measured, proceed to the next step.

**Step 4.** Measure **pins 1 and 2 on the J3 cable at the rear of the console** to verify 12 VDC. If no 12 VDC is measured, inspect the **inline connector cable** (#256, 275, 273 on the flow chart). If 12 VDC is measured, **replace the console** (#250).

**Two breakers and a filter are on the mains path**, and step 2 names them all before any measurement past the inlet. The circuit-board page says the LCB does the AC-to-DC conversion itself and also switches the inverter's AC for sleep mode, so an LCB with mains in and no 12 V out is condemned outright.

The flow chart page is headed *Check Procedure for 110 VAC Model*; the numbered steps are not marked as 110 V-only, and the captions allow 220 VAC.

