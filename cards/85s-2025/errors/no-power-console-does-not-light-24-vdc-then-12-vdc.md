---
id: 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
title: 'No power on the touchscreen stepper: wake it first, then mains at the power
  supply module, the board indicator, 24 volts out of the supply, 12 volts at the
  console cable'
kind: troubleshooting
question: What do I check when a Spirit 85s-2025 recumbent stepper has no power and
  the console does not light?
asked_as:
- 8.5s stepper screen wont turn on
- no power on my spirit rehab stepper
- stepper console dead where is the fuse
- 8.5s power supply 24v test
keywords:
- no power
- console does not light
- power supply module
- lower control board
- lcb
- 24 vdc
- 12 vdc
- fuse
- indicator light
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: errors
  code: no-power
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
- csc900-2024-errors-console-does-not-light-up-after-power-on
see_also:
- 85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version
- 85s-2025-errors-console-shows-the-fault-and-a-suggested-fix
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 5. Troubleshooting (Electronic), 5-1 No power, console doesn't light, steps
    1-5 and the Check Procedure flow chart, PDF p. 16-18; text.md lines 218-265, with
    the figure captions "Measured 110 VAC or 220 VAC depending on the mains voltage"
    and the flow chart from the OCR supplements for pages 16 and 18 (lines 810-880)
  extracted_at: '2026-09-11'
---

**This machine is mains-powered through an internal power supply module, not through the external adapter the 7.0S, 7.5S and MS300 use.** Their no-power row - outlet, adapter, DC wire - does not apply here (`spirit-med-stepper-errors-no-power-outlet-and-dc-wire`). The figures below are this book's.

**Step 1.** Press any physical button on the console to wake up the system. If the system does not respond, proceed to the next step. *(The flow chart's first result: the system was in sleep mode.)*

**Step 2.** Measure the AC input voltage at the cable connected to the **CN1** housing on the power supply module (#097). If no AC voltage is measured or the voltage is incorrect, check whether the **power switch** is turned on and the **fuse** is not blown. Then measure the mains voltage and the voltage at the machine-side end of the power cable. If correct AC voltage is present at CN1, proceed to the next step. The figure captions read *Measured 110 VAC or 220 VAC depending on the mains voltage*.

**Step 3.** Check the status of **power indicator light D5** on the LCB (the lower control board, #105). If the light is off, proceed to the next step. If the light is on, skip ahead to Step 5.

**Step 4.** Measure **pins 1 and 4 of connector CN100** on the power supply module to verify the presence of **24 VDC**. If 24 VDC is not measured, replace the power supply module. If 24 VDC is measured, replace the LCB.

**Step 5.** Measure **pins 1 and 2 on the J3 cable** at the rear of the console to verify **12 VDC**. If no 12 VDC is measured, inspect the inline connector cable (#089, #090 on the wiring diagram). If 12 VDC is measured, replace the console (#086).

**The chain is mains, then 24 V, then 12 V, and one LED splits it in half.** The circuit-board page of the same book says the power supply gives the LCB 24 VDC and the LCB converts it to 12 VDC for the console; the D5 indicator on the LCB is lit when the 24 V side is good, which is why a lit D5 lets you skip the 24 V measurement and go straight to the console cable. A dark D5 with 24 V present condemns the LCB; a lit D5 with no 12 V at J3 condemns the inline cable; 12 V at J3 with a dark screen condemns the console.

**A fuse and a switch are on this machine** - in the AC power entry module - and step 2 names them before any measurement past the inlet.

The CSC880 stair climber walks the same 24 V then 12 V chain with different connectors (`csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks`); do not carry its connector names here.
