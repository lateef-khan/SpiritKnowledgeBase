---
id: ct1000ent-2023-errors-controller-led-debugging-six-leds-220-230-v
title: Reading the six controller LEDs, power, incline up and down, start, fast and
  slow, against a 220 to 230 V supply
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Spirit ct1000ent-2023
  treadmill?
asked_as:
- what do the lights on the treadmill controller mean
- start led on the lower board does nothing
- power led off on the controller
keywords:
- controller led
- indicator led
- power led
- up down led
- start led
- fast led
- slow led
- control cable
- fuse
- 220-230v
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct1000ent-2023
  applies_to:
  - ct1000ent-2023
  section: errors
  code: no-code
  model_number:
  - '210854'
authority: 3
not_to_be_confused_with:
- ct900ent-errors-controller-led-debugging-six-leds-110-120-v
- spirit-xt-2023-errors-controller-led-debugging-five-leds
see_also:
- spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter
- ct1000ent-2023-errors-error-code-list-25-hex-codes
source:
  ref: spirit-treadmill-ct1000ent-2023-service-manual
  locator: CT1000ENT 2023 service manual 4.3 Controller debugging, PDF p. 10, text.md
    lines 203-228
  extracted_at: '2026-09-11'
---

The table the CT1000ENT 2023 service manual prints under *4.3 Controller debugging*. Where the LEDs sit is a specs fact; this card is what each state means.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If AC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 220~230V. Replace fuse. Replace controller. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| START | START | No execution start | Check control cable plugged in | Replace controller. |
| FAST+ | FAST | No execution fast | Check control cable plugged in | Replace controller. |
| SLOW+ | SLOW | No execution slow | Check control cable plugged in | Replace controller. |

The three command LEDs - START, FAST+ and SLOW+ - light when the console's command reaches the board; one that stays dark on a key press means the control cable, and if the cable is seated, the controller. The book is the 230 V build - its safety page asks for a 230-volt 15-amp outlet and its circuit diagram is headed 230V - which is why the supply figure here is double the CT900ENT's (`ct900ent-errors-controller-led-debugging-six-leds-110-120-v`).
