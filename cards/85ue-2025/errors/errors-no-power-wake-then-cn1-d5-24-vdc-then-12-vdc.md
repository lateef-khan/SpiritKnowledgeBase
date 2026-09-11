---
id: 85ue-2025-errors-no-power-wake-then-cn1-d5-24-vdc-then-12-vdc
title: 'No power on the upper-body ergometer: wake it first, then mains at the power
  supply module, the board indicator, 24 volts out of the supply, 12 volts at the
  console cable'
kind: troubleshooting
question: What do I check when a Spirit 85ue-2025 upper body ergometer has no power
  and the console does not light?
asked_as:
- 8.5ue screen wont turn on
- no power on my spirit arm ergometer
- 8.5ue console dead where is the fuse
- ube power supply 24v test
keywords:
- no power
- console does not light
- power supply module
- lower control board
- lcb
- 24 vdc
- 12 vdc
- fuse
- d5 indicator
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: errors
  code: no-power
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
- spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply
see_also:
- spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc
- 85ue-2025-errors-uart-communication-error-cables-then-software-version-v255a255
- 85ue-2025-errors-no-revolutions-d13-then-hall-sensor-078-to-chain-wheel-208-at-2-to-3-mm
- 85ue-2025-errors-console-shows-the-message-and-the-fix
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 8.5UE (MZ2000-SB036-01) service manual 5.1 No power, console doesn't light,
    steps 1-5 and the Check Procedure flow chart, PDF p. 20-23; text.md lines 254-288,
    with the figure captions from the OCR supplement for page 21 and the flow chart
    from the OCR supplement for page 23; 4.4 Circuit Board, PDF p. 17-18, lines 227-233
  extracted_at: '2026-09-11'
---

**These bikes are mains-powered through an internal switching power supply**, unlike the 7.0R/7.0U whose chain ends at a fuse in the input module (`spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply`) and the generator-fed 4.0R/4.0U, which have no cord at all. The figures below are this book's; the 8.0U and 8.5R bikes print the same five steps with their own part numbers (`spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc`).

**Step 1.** Press any physical button on the console to wake up the system. If the system does not respond, proceed to the next step. *(The flow chart's first result: the system was in sleep mode.)*

**Step 2.** Measure the AC input voltage at the cable connected to the **CN1** housing on the power supply module (#075). If no AC voltage is measured or the voltage is incorrect, check whether the **power switch** is turned on and the **fuse** is not blown. Then measure the mains voltage and the voltage at the machine-side end of the power cable. If correct AC voltage is present at CN1, proceed to the next step. The figure captions read *Measured 110 VAC or 220 VAC depending on the mains voltage*.

**Step 3.** Check the status of **power indicator light D5** on the LCB (the lower control board, #084). If the light is off, proceed to the next step. If the light is on, skip ahead to Step 5.

**Step 4.** Measure **pins 1 and 4 of connector CN100** on the power supply module to verify the presence of **24 VDC**. If 24 VDC is not measured, replace the power supply module. If 24 VDC is measured, replace the LCB.

**Step 5.** Measure **pins 1 and 2 on the J3 cable** at the rear of the console to verify **12 VDC**. If no 12 VDC is measured, inspect the inline connector cable. If 12 VDC is measured, replace the console.

**The chain is mains, then 24 V, then 12 V, and one LED splits it in half.** The circuit-board page of the same book says the power supply gives the LCB 24 VDC and the LCB converts it to 12 VDC for the console and feeds the angle and magnet sensors; D5 is lit when the 24 V side is good, which is why a lit D5 lets you skip the 24 V measurement and go straight to the console cable. A dark D5 with 24 V present condemns the LCB; a lit D5 with no 12 V at J3 condemns the inline cable; 12 V at J3 with a dark screen condemns the console.

**A fuse and a switch are on this machine**, in the AC power entry module, and step 2 names them before any measurement past the inlet. The wiring is the *Generator/Brake Controller* on the parts list - the book's LCB - and a *Switching Power Supply*.

The 8.5UE flow chart names no part numbers; the wiring diagram gives the console as #061, the LCB as #084, the power supply as #075 and the AC power entry module with switch and fuse as #070.

