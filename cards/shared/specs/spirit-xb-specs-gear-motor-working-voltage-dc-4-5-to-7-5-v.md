---
id: spirit-xb-specs-gear-motor-working-voltage-dc-4-5-to-7-5-v
title: The resistance gear motor works on DC 4.5 to 7.5 V, on every gear-motor residential
  bike from 2016 to 2023
kind: spec
question: What is the working voltage of the resistance gear motor on a Spirit XBR25,
  XBR55, XBU55, XBR55ENT or XBU55ENT bike?
asked_as:
- what voltage does the xbr55 resistance motor run on
- tension motor spec spirit recumbent
- gear motor voltage xbu55
- what electronic parts are in the xbr25
keywords:
- gear motor
- tension motor
- working voltage
- 4.5v
- 7.5v
- resistance
- electrical configuration
- lcd display
- cooling fan
- speed sensor
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbr55-2016
  - xbr55-2023
  - xbr55ent-2021
  - xbu55-2016
  - xbu55-2023
  - xbu55ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xbr95-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v
- sole-bike-ems-brake-spec
see_also:
- spirit-xb-specs-gear-motor-connector-5-pin-definition
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- sole-bike-tension-motor-spec
- spirit-xb-ent-2021-specs-electrical-configuration-with-incline-motor-text
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55-2023: section 3 Electrical Configurations, PDF p. 5, text.md lines
    72-83, and 2.1/2.2 Electronic Parts, PDF p. 4 (OCR supplement lines 771-800).
    XBU55-2023: PDF p. 5, lines 69-80; PDF p. 4 (OCR 625-648). XBR55-2016: PDF pp.
    11-12, lines 145-170; parts PDF pp. 8-9, lines 119-138. XBR25-2016: PDF pp. 10-11,
    lines 138-163; pp. 7-8, lines 112-131. XBU55-2016: PDF pp. 10-11, lines 132-157;
    pp. 7-8, lines 105-125. XBR55ENT-2021: PDF p. 9, lines 71-92; pp. 5-7, lines 22-62.
    XBU55ENT-2021: PDF p. 9, lines 66-89; pp. 5-7, lines 22-58'
  extracted_at: '2026-09-11'
---

**Work voltage: DC 4.5 ~ 7.5 V.** Seven books print exactly that line, under *Tension motor* in
the 2016 and ENT books and *Gear Motor* in the 2023 books - two names for the one part, which
"can change to increase or decrease resistance level of brake" by pulling a steel cable that
moves the magnet on the flywheel.

What else the electrical-configuration page says:

| Books | Console | Main controller |
|---|---|---|
| 2016 (XBR25, XBR55, XBU55) | key controls and an **LCD display** | "power supply and motor driver control circuit" |
| 2023 (XBR55, XBU55) | key controls and an **LCD display** | not listed as a part at all |
| ENT 2021 (XBR55ENT, XBU55ENT) | key controls and a **TFT LCD touch panel** | "DC power supply for console, incline driver and tension motor driver" - see the ENT card |

**The chapter-2 photographs caption the same part TENSION MOTOR (2016, ENT) or Gear Motor (2023)**;
what else they name is on `spirit-xbr-xbu-2016-specs-parts-electronic-parts-named`,
`spirit-xbr55ent-xbu55ent-specs-parts-electronic-parts-named` and
`spirit-xbr55-xbu55-2023-specs-parts-electronic-parts-named`. There is no lower controller board
to photograph on the 2023 bikes: the motor is driven straight from the console over the computer
cable.

The Level Up / Level Down drive voltage the drive board puts out, +5 V and -5 V, is a test figure
and lives with the E2 / "- -" error cards. The Sole B94 and R92 print the same 4.5-7.5 V motor
(`sole-bike-tension-motor-spec`) - a different brand, not the same machine.

