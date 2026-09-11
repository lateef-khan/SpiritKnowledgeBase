---
id: crw800-2024-errors-e2-cable-tension-communication-error
title: E2 on the rower is a cable tension communication error, shown with MOTOR ERROR,
  and the service manuals add the checks and a voltage test
kind: troubleshooting
question: What does E2 mean on a Spirit CRW800 or XRW600 rower?
asked_as:
- my spirit rower says e2
- what does e2 mean on a rowing machine console
- rower showing e2
keywords:
- e2
- cable tension
- tensioner
- communication error
- console
- rower
- resistance
- error message code
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - xrw600-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- crw800-2024-errors-e1-console-eeprom-failure
- spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt
- cvc800-e-2-tension-motor-error
see_also:
- crw800-2024-errors-e1-console-eeprom-failure
- crw800-2024-errors-lcd-display-does-not-shine
- cvc800-e-2-tension-motor-error
- spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter
- crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller
- spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel
- sr500-2016-e2-motor-error
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: ERROR CODES, printed page 34. That page is a flat picture with no text
    layer and was read from the rendered page; CRW800 2021 (800940) service manual
    7-1 Error Codes, PDF p. 31 (printed 30), text.md lines 412-421, and 7-3 Error
    Message, PDF p. 33-34 (printed 32-33), text.md lines 437-483; CRW800 2016 (CW800-YR001)
    service manual 8. Error Messages / Troubleshooting, PDF p. 31-33, text.md lines
    398-445; XRW600 (DW400-YR002) service manual 8. Error Messages / Troubleshooting,
    PDF p. 31-33, text.md lines 390-445
  extracted_at: '2026-09-10'
---

| Error Message Code | Problem Description |
|---|---|
| E2 | Cable tension communication error |

**That is the whole of what this manual says.** No definition, no troubleshooting column and no part
to replace.

**The cable tensioner is the part this machine resists you with**, and it is also the part the
manual's display row asks about: the LCD row on the previous page says to check whether the *cable
tensioner* is putting out **DC12V**, and to replace it if not
(`crw800-2024-errors-lcd-display-does-not-shine`). That is the only measurement printed anywhere in
this book against the tensioner, and it is the nearest thing to a check for this code. **The manual
does not connect the two**, so say plainly that the DC12V test comes from the display row rather
than from the code.

Look-alike codes: `E2` on the 2024 treadmills is a drive motor over-current answered with belt
lubricant (`spirit-2024-errors-e2-motor-overcurrent-lubricate-the-belt`), and `E-2` on the Spirit
CVC800 climber is a tension motor fault with a full voltage test of its own
(`cvc800-e-2-tension-motor-error`).

## Three service manuals print the code with a symptom, a signal path and a fix

**The CRW800 2016 (`CW800-YR001`), the CRW800 2021 (`800940`) and the XRW600 (`DW400-YR002`) service manuals all print `E2 | Cable tension communication error`** (the XRW600 shortens it to `communication error`) and then:

> Error code: E2. When the "E2" "MOTOR ERROR" message is displayed, the communication with the cable tensioner is abnormal and all functions are stopped.

So **the console shows the words `MOTOR ERROR` beside `E2`**, and everything stops. (The XRW600 book says "the communication with the cable is abnormal" and calls the part a *tension motor*.)

**Cable tensioner operation**

| Device | Description |
|---|---|
| Console | When you press the UP or DOWN key while in program mode, the LEVEL value displayed on the console display increases or decreases. At the same time send a command signal to the cable tensioner action. |
| Cable tensioner | Receives the command signal from the console and actuation. *The 2016 and XRW600 books add:* supply the console DC12V power. |

**Troubleshooting**

| Device | Troubleshooting |
|---|---|
| Console | 1. Check the connection of motherboard's 8-pin cable. 2. When UP or DOWN is pressed, a beep sound is generated, if yes that it is determined that the signal has been sent. |
| 8-pin Cable | 1. Check the cable connections. 2. Check if the cable is broken or curled. 3. Replace the cable and retest. |
| Cable tensioner | Check the 8-pin cable connection. |

**The tensioner feeds the console on the adapter-powered machines.** The 2016 and XRW600 books say so in the operation table - *supply the console DC12V power* - which is what the 2024 owner's manual's LCD row was getting at with its `DC12V` check (`crw800-2024-errors-lcd-display-does-not-shine`). The 2021 generator-powered book drops that clause.

**The voltage test follows, and its figures differ by book:** 5.5 to 6.5 V and a power adapter on the 2016 CRW800 and the XRW600 (`spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter`), 4 to 6 V and a generator controller on the 2021 CRW800 (`crw800-2021-errors-cable-tensioner-voltage-test-4-to-6-vdc-then-the-generator-controller`). The mechanical half of a resistance that will not change - the handlebar controller, the steel cable and the flywheel - is the Q&A chapter (`spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel`).

Sole's SR500 2016 prints the same code and tables for its own rower: `sr500-2016-e2-motor-error`.
