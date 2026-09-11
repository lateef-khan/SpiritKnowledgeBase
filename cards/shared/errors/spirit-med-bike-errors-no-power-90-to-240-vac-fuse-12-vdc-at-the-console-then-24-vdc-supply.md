---
id: spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply
title: 'No power on the mains-fed rehabilitation bike: outlet, connectors and the
  input-module fuse for the owner, then 12 volts at the console cable and 24 volts
  from the switching supply for the technician'
kind: troubleshooting
question: What do I check when a Spirit Medical 7.0R or 7.0U bike has no power and
  the console does not light?
asked_as:
- 7.0r wont turn on
- no power on my spirit rehab bike
- where is the fuse on the 7.0u
- 7.0r console dead 12v test
keywords:
- no power
- console does not light
- fuse
- input module
- 90-240vac
- 12v dc
- 24v dc
- switching power supply
- control board
- rehabilitation bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: no-power
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
- spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
see_also:
- spirit-med-bike-errors-eeprom-error-replace-the-console-only-message
- spirit-med-bike-errors-programs-do-not-start-key-test-then-keypad
- spirit-med-bike-errors-no-data-when-pedaled-angle-sensor-5-volts-3-mm-and-reed-sensor-5-mm
source:
  ref: spirit-bike-70r-2025-service-manual
  locator: '7.0R (MR490-SB018-03) service manual 5.2.4 Troubleshooting, 1. No Power,
    steps i-vii, PDF p. 8-11; text.md lines 113-141. 7.0U (MU470-SB018) service manual
    5.2.4 Troubleshooting, 1. No Power, PDF p. 8-11; text.md lines 164-192 - the same
    seven steps word for word. Owner''s manual row: ERROR MESSAGE & TROUBLESHOOTING,
    PDF p. 48 (printed 46); text.md lines 1328-1377; 7.0U 2025 owner''s manual ERROR
    MESSAGE & TROUBLESHOOTING, PDF p. 46 (printed 44); text.md lines 1285-1329; Dyaco
    MED 7.0R 2021 owner''s manual (Rev. 1.2.1) Error messages and Troubleshooting,
    PDF p. 84-85; text.md lines 2642-2730'
  extracted_at: '2026-09-11'
---

**This bike plugs into the wall and has a fuse; the 4.0R/4.0U do not** (they are pedal-generator bikes with no cord). The 7.0S/7.5S steppers run from an external adapter and their no-power row is different again (`spirit-med-stepper-errors-no-power-outlet-and-dc-wire`).

## The owner's manual row - three checks

> - Make sure the A.C. outlet has power (**90~240VAC**), the line cord plugged in securely and the power switch is on.
> - **Check the fuse in the Input module** (located between the power switch and line cord input).
> - Make sure all connectors in back of the console are securely seated in place.

The 7.0R 2025, 7.0U 2025 and the Dyaco MED 7.0R 2021 owner's manuals print these three bullets word for word. The fuse rating is on the specification page, not here: the 2021 book says *replace with only 5A, 250V glass fuse, fast acting 5.2 x 20 mm* (carded under `section: specs`).

## The service manual procedure - seven steps

1. Make sure the A.C. outlet has power (90~240VAC), the line cord plugged in securely and the power switch is on.
2. Make sure all connectors in back of the console are securely seated in place. Go to next step if there is still no power on the bike.
3. Measure **pin 1/pin 6 and pin 3/pin 6 of the 6 pin cable** that connected to the console for **12V DC**. Replace the console if the 12V DC was measured. Go to next step if there is no voltage.
4. Open the cover and measure **pin 3 and pin 6 of the 6 pin connector at the control board** for 12V DC. Replace the cable if the voltage was measured at the control board but not at the cable. Otherwise, go to next step.
5. Measure the input voltage at the control board at the **4 pin connector for 24V DC**. Replace the control board if the voltage was measured. Go to next step if there is no voltage.
6. Measure the input (**2 pin** connector) and output (**8 pin** connector) voltage of the **switching power supply**. You should measure the same AC voltage with step 1 at input, 24V DC at the output. Replace the cable that connects the control board and power supply if the 24V DC was measured. Replace the power supply if the input AC voltage was measured but no output voltage. Go to next step if both voltage was measured.
7. Check the **fuse in the Input module** (located between the power switch and line cord input). Use the meter to check the fuse, the fuse should be short. Make sure there is nothing short in the whole system and replace the fuse if the fuse was open.

**The chain is mains, then 24 V out of the switching supply, then 12 V out of the control board to the console.** Twelve volts at the console cable with a dark screen condemns the console; 12 V at the board but not at the cable condemns the cable; 24 V into the board with no 12 V out condemns the board; mains into the supply with no 24 V out condemns the supply. The fuse is last in the service order and second in the owner's order - the owner has no meter for the rest.

The 7.0R (MR490) and 7.0U (MU470) service manuals print the seven steps in the same words. The 8.0U and 8.5R of the same range walk a similar 24 V then 12 V chain with different connectors and an LED on the board (`spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc`); do not carry those pin numbers here.

