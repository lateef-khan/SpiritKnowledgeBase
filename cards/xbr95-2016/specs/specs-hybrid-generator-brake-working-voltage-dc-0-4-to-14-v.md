---
id: xbr95-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v
title: The hybrid generator brake works on DC 0.4 to 14 V, on the generator recumbent
  with a console, main controller and speaker
kind: spec
question: What is the working voltage of the generator brake on a Spirit xbr95-2016
  recumbent bike, and what electrical parts does the manual name?
asked_as:
- what voltage is the xbr95 brake
- hybrid generator brake spec
- what electronic parts are in the xbr95 2016
- xr829 electrical configuration
keywords:
- hybrid generator brake
- working voltage
- 0.4v
- 14v
- generator brake
- main controller
- lcd display
- speaker
- cooling fan
- speed sensor
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2016
  applies_to:
  - xbr95-2016
  section: specs
  code: '*'
  model_number:
  - '951115'
authority: 3
not_to_be_confused_with:
- spirit-xb-specs-gear-motor-working-voltage-dc-4-5-to-7-5-v
- sole-bike-ems-brake-spec
- xbr95-2023-specs-electrical-configuration-generator-brake
see_also:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
- spirit-residential-bike-specs-gear-motor-or-generator-brake
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: Section 3 Electrical Configurations, PDF pp. 11-12, text.md lines 153-178
    (OCR supplement lines 1238-1244 confirms the figure); section 2 Electronic Parts,
    PDF pp. 8-9, lines 114-147
  extracted_at: '2026-09-11'
---

**HYBRID GENERATOR BRAKE - Work voltage: DC 0.4 ~ 14 V.** "Control resistance increases and
decreases." That is the coil voltage the driver board puts across the brake as the level rises;
it is not a supply rating.

The rest of section 3: **CONSOLE** - controls all functions of the bike; key controls and an
**LCD display**. **MAIN CONTROLLER** - the DC power supply for the console, plus the driver control
circuit. **GENERATOR BRAKE** - increases or decreases the resistance level of the brake.

The chapter-2 photographs caption the flywheel unit **HYBRID GENERATOR** (the five parts they
name are on `xbr95-2016-specs-parts-electronic-parts-named`).

**This is the only XBR95 book that prints the brake voltage.** The 2023 book keeps the three-part
text and drops the figure (`xbr95-2023-specs-electrical-configuration-generator-brake`). The Sole
LCB/LCR "EMS brake" card gives DC 0-21 V for a different machine (`sole-bike-ems-brake-spec`); do
not carry either number across.

