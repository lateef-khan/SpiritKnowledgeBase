---
id: erg700-2022-specs-power-adapter-ac-100-to-240-v-in-dc-12-v-out-feeding-the-console-and-tension-motor
title: An external adapter rated AC 100 to 240 V in and DC 12 V out, printed only
  on the troubleshooting page, feeding the console and the tension motor over an 8-pin
  cable
kind: spec
question: What power supply does an Xterra erg700-2022 rower use, what is the adapter
  rated, and what does it feed?
asked_as:
- erg700 power adapter voltage
- what adapter does the xterra erg700 rower use
- erg700 tension motor 12v
- erg700 8 pin cable
keywords:
- adapter
- adaptor
- power supply
- dc 12v
- 12 volt
- 100-240v
- tension motor
- 8-pin cable
- power jack
- rating
facets:
  brand:
  - xterra
  product_line: rower
  model: erg700-2022
  applies_to:
  - erg700-2022
  section: specs
  code: '*'
  model_number:
  - '170918'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-specs-external-power-adapter-with-no-rating-printed
- fs30-2018-specs-power-adaptor-rated-9-v-1000-ma
- xterra-specs-resistance-has-16-levels
- spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack
- xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
- sb1200-2023-power-supply
source:
  ref: xterra-rower-erg700-2022-owners-manual
  locator: '''Power'', PDF p. 4 (printed 1), text.md lines 51-88 (''This product uses
    an external power supply. The power supply must first be plugged into the power
    jack on the unit''); Troubleshooting table, PDF p. 26 (printed 23), lines 794-856
    (''Check whether the AC power input is AC100 ~ 240V and the output is DC12V'',
    ''Has the tension motor output DC12V, if not, please replace the new tension motor'');
    Error Codes page, PDF p. 25 (printed 22), lines 770-794 (''Check the connection
    of motherboard''s 8-pin cable'', ''Tension Motor - Check the 8-pin cable connection'')'
  extracted_at: '2026-09-11'
---

**The Power page prints no rating; the troubleshooting page does: input AC 100 to 240 V, output DC 12 V.** The
Power paragraph says only "This product uses an external power supply. The power supply must first be plugged into
the power jack on the unit. Next, plug the power supply into the appropriate wall outlet", unplug it when not in
use, and let a cold machine warm to room temperature before plugging in. No current (A), polarity or plug size is
printed anywhere, so a replacement adapter is matched to the label on the original.

The rating appears in the "LCD display does not shine" row: "Check whether the AC power input is AC100 ~ 240V and
the output is DC12V", then "Check the power of the console", then "Has the tension motor output DC12V, if not,
please replace the new tension motor." So the adapter feeds a **tension motor** that sets the sixteen resistance
levels (`xterra-specs-resistance-has-16-levels`), and the motor passes power on to the console.

The wiring the book names: an **8-pin cable** between the console and the "motherboard", which the E2 page says
is the communication cable ("When the screen displays E2, it means that the communication with the cable is
abnormal ... Check the connection of motherboard's 8-pin cable ... Check if the cable is broken or curled ...
Replace the cable and retest"), and the same 8-pin connection at the tension motor. A **light sensor** reads the
stroke ("Check the light point and the receiving point for dust obstruction"). The E1 and E2 codes and the
troubleshooting rows are the errors section's.

Cross-brand: the Spirit XRW600 and 2016 CRW800 rowers use a 12 V 1.5 A adapter
(`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack`) and carry an 8-pin tension-motor
plug (`xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor`); the current figure is theirs, not
this book's. The other adapter-fed Xterra rowers (ERG400, ERG800W) print no rating at all
(`xterra-specs-external-power-adapter-with-no-rating-printed`).

