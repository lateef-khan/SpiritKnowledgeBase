---
id: ct900ent-errors-controller-led-debugging-six-leds-110-120-v
title: Reading the six controller LEDs, power, incline up and down, start, fast and
  slow, against a 110 to 120 V supply
kind: troubleshooting
question: What do the LEDs on the lower controller mean on a Spirit ct900ent treadmill?
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
- 110-120v
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct1000ent-2023-errors-controller-led-debugging-six-leds-220-230-v
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- ct800-2016-errors-controller-led-debugging-90-to-110-v
see_also:
- ct900ent-errors-popping-sound-at-power-on-100-120-v
- spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: CT900ENT service manual Controller debugging, PDF p. 15, text.md lines
    191-209
  extracted_at: '2026-09-11'
---

The table the CT900ENT service manual prints under *Controller debugging*. Where the LEDs sit is a specs fact; this card is what each state means.

| LED | Function | Condition | Reason | Solve |
|---|---|---|---|---|
| POWER | Controller power | If AC voltage is normal, it would be always ON. If off, fault condition exists. | Voltage is not correct. Fuse is blown. Transformer is no good. | Check the supply voltage is 110~120V. Replace fuse. Replace controller. |
| UP | Motion of incline motor | Motion of incline motor is up. | Transistor was broken. Relay failed. | Replace controller. |
| DOWN | Motion of incline motor | Motion of incline motor is down. | Transistor was broken. Relay failed. | Replace controller. |
| START | START | No execution start | Check control cable plugged in | Replace controller. |
| FAST+ | FAST | No execution fast | Check control cable plugged in | Replace controller. |
| SLOW+ | SLOW | No execution slow | Check control cable plugged in | Replace controller. |

The three command LEDs - START, FAST+ and SLOW+ - light when the console's command reaches the board; one that stays dark on a key press means the control cable, and if the cable is seated, the controller. No speed-sensor or limit-current LED is listed, unlike the DC-controller XT boards (`spirit-xt-2023-errors-controller-led-debugging-five-leds`).

The CT1000ENT 2023 prints the same six rows against **220~230V** (`ct1000ent-2023-errors-controller-led-debugging-six-leds-220-230-v`). The CT900, whose driver board is the same VFD015TM12A inverter, prints no LED table at all.
