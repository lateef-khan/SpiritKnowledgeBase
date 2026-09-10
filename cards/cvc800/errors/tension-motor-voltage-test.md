---
id: cvc800-tension-motor-voltage-test
title: Measuring the tension motor drive voltage
kind: procedure
question: How do I test the tension motor voltage on a Spirit CVC800 climber?
asked_as:
- how to test the tension motor on a spirit climber
- climber resistance motor voltage test
- multimeter test for climber tension motor
keywords:
- tension motor
- voltage test
- multi-meter
- 20vdc
- level up
- level down
- drive board
- transformer
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: errors
  code: e2
  model_number: '800440'
authority: 3
not_to_be_confused_with: []
see_also:
- cvc800-e-2-tension-motor-error
- e25-2016-tension-motor-voltage-test
- sole-bike-tension-motor-voltage-test
source:
  ref: spirit-climber-cvc800-service-manual
  locator: Tension Motor Voltage Test Procedure, page 31
  extracted_at: '2026-09-08'
---

Five steps, in the manual's order. This is the test the E-2 section sends you to.

1. Put the multi-meter to the **20 VDC** setting. Place probes on the motor control wire (**red probe
   in blue wire, black probe in green wire**) on the drive board.
2. Turn on unit power. The display lights up.
3. Press **LEVEL UP**. Normal reading: **+4 to 5.5 V DC**. Motor operates, resistance increases.
4. Press **LEVEL DOWN**. Normal reading: **-4 to -5.5 V DC**. Motor operates, resistance decreases.
5. If there is no voltage, check the transformer; if there is no output, replace it.

| Part | Troubleshooting |
|---|---|
| Display board | Inspect the 9-pin cable connections. |
| 9-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Tension Motor | Inspect the display board 5-pin connections. |

**The page names two different pairs of wires for the same probes.** Step 1 says red on the **blue**
wire and black on the **green** wire. The caption under the photograph on the same page says
`Place probes on the motor control wire (Red probe in palm wire, Black probe in black wire)`. Both
are reproduced here because the manual gives no way to decide between them; the photograph shows the
probes on a multi-way connector at the drive board. Identify the motor control pair from the
connector pin map in section 8-4 before probing.

The E-2 section on the previous page quotes two further voltages, +/-2.5 VDC and +/-4.5 VDC, that
do not agree with the +4 to 5.5 V band above. See `cvc800-e-2-tension-motor-error`.

Sole's ellipticals and bikes carry the same procedure with their own numbers; those cards are
linked below and are for different machines.
