---
id: spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor
title: A tension motor working at DC 4.5 to 7.5 V and an AC incline motor with four
  wires, red up, black down, white common, green ground, plus a 3-pin position sensor
kind: spec
question: What does the electrical configuration page of the Spirit XS895 incline
  stepper service manual say about the tension motor and the incline motor?
asked_as:
- what voltage is the xs895 tension motor
- incline motor wires on the xs895
- which wire is up on the spirit stepper incline motor
- is the xs895 incline motor ac or dc
keywords:
- electrical configuration
- tension motor
- dc 4.5-7.5v
- incline motor
- ac motor
- red wire up
- black wire down
- white common
- green ground
- position sensor
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v
- spirit-crs800s-cs800-2021-specs-electrical-configuration-ecb-brake-with-no-voltage-printed
see_also:
- spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
- spirit-xe-2016-specs-tension-motor-working-voltage-dc-4-5-to-7-5-v
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 3. Electrical Configurations, PDF p. 9 (printed 8), text.md lines 114-146;
    the incline wire colours reappear on the circuit diagram, PDF p. 39, and the E2
    test page gives +5.5~6.0 V, PDF p. 30, lines 437-456
  extracted_at: '2026-09-11'
---

The only stepper book in this family with a **main controller that drives two motors**.

| Part | Description printed |
|---|---|
| CONSOLE | Interface that controls all functions of the Stepper |
| MAIN CONTROLLER | The circuit board consist of the DC power supply for console, incline driver and tension motor driver, link the console to output appropriate voltages for tension motor that control the Stepper functions |
| TENSION MOTOR | It can change to increase or decrease resistance level of brake |
| INCLINE MOTOR | This is an ac motor. User can to control variable elevation by console within main controller |

**General information**

- CONSOLE - Contains Key controls and LCD Display. Main controller Include power supply, motor
  driver control circuit and incline control circuit.
- TENSION MOTOR - **Work voltage: DC 4.5~7.5V.** Control resistance increases and decreases.
- INCLINE MOTOR - **This is a AC motor. Have four wires, red, black, white and green. Has one 3 pins
  cable of position sensor.**

| Incline wire | Function printed |
|---|---|
| **Red** | UP - "if there is AC voltage on the Red wire (UP) the incline motor will increase the incline" |
| **Black** | DOWN - AC voltage on the Black wire decreases the incline |
| **White** | COM - neutral |
| **Green** | ground |

**No mains voltage for the incline motor is printed** - only "AC voltage". The Spirit XE395
ellipticals print the same four colours with 120 or 115 V AC
(`spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor`); do not carry
that figure to the stepper. The 3-pin position sensor is the *INC VR* line of the 11-pin console
cable (`spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins`).

The E2 test expects **+5.5~6.0 V DC / -5.5~6.0 V DC** across the tension motor's blue and green
wires, inside the 4.5-7.5 V working range.

