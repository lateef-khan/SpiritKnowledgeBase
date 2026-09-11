---
id: spirit-med-70-bike-console-unit-type-recumbent-or-upright-and-the-model-codes-the-service-manual-names
title: Unit type selects Recumbent or Upright, which the service manuals name by their
  MU and MR model codes, and a wrong setting corrupts the symmetry reading
kind: procedure
question: What is the Unit type setting on a Spirit Medical 7.0 series bike and what
  should it be set to?
asked_as:
- what is unit type in the 7.0r maintenance menu
- should unit type be upright or recumbent on the 7.0u
- what is mu100 or mr100 on my spirit medical bike
- symmetry is wrong after a console swap
keywords:
- unit type
- recumbent
- upright
- mu100
- mr100
- factory settings
- symmetry
- console replacement
- maintenance mode
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration
- spirit-xb55ent-console-engineer-mode-factory-setting-machine-type-blename-and-an-incline-calibration
see_also:
- spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration
- spirit-med-70-bike-console-maintenance-mode-with-a-sleep-switch-a-keypad-lock-and-factory-settings
- ce900-2025-console-engineering-mode-unit-type
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: 'Unit type entry: 7.0R OM PDF p. 47 (printed 45), text.md lines 1325-1326;
    7.0U OM p. 45, lines 1282-1284; MED 7.0R p. 84, lines 2656-2657; 7.0R SM 5.2.1
    xiii, PDF p. 8, line 109; 7.0U SM PDF p. 8, line 160. Troubleshooting: 7.0R OM
    p. 48, lines 1330-1335; 7.0U OM p. 46, lines 1287-1292; MED 7.0R p. 85, lines
    2697-2700; 7.0R SM 5.2.4 item 4, p. 13, lines 159-162.'
  extracted_at: '2026-09-11'
---

**Unit type is the last item under Factory settings**, and the same console firmware serves both
bikes, so it has to be told which one it is on.

| Book | What it says to select |
|---|---|
| 7.0R 2025 owner's manual, Dyaco MED 7.0R | "Select on the console: **Recumbent**." |
| 7.0U 2025 owner's manual | "Select on the console: **Upright**." |
| Service manuals MR490-SB018-03 and MU470-SB018 | "Selects the corresponding model for the unit, **MU100 for the upright bike and MR100 for the recumbent bike**." |

**The model codes are the console's names, not the machines' part numbers.** The 7.0R book is
MR490 and the 7.0U book MU470; the menu still offers MU100 and MR100.

**A wrong Unit type shows up as a wrong Symmetry reading.** The troubleshooting pages: "Symmetry
measurement is incorrect - perform the sensor tests in Maintenance Mode; if sensors are functioning
then perform Crank Position Calibration; if calibration is ok then check the Unit Type"
(`spirit-med-70-bike-console-brake-test-to-512-sensor-test-angle-and-reed-and-crank-position-calibration`).
The service manuals put the Unit Type check first, before the sensor test.

**What the troubleshooting page tells you to check it against is wrong in two of the three owner's
manuals.** The 7.0R 2025 book says "check the Unit Type is set to **upright**" - on a recumbent bike
whose own menu page says Recumbent - and the Dyaco MED 7.0R says "set to **7.0R**", a value the menu
does not offer. The 7.0U book's "upright" is the only one that agrees with its menu page. **Set it to
the machine in front of you**, Recumbent or Upright, whatever the troubleshooting sentence says.

The 8-series touchscreen bikes make the same choice on a Machine Type page with six machines
(`spirit-med-80-bike-console-service-tab-machine-type-loopback-nfc-keypad-beacon-and-crank-calibration`);
the CE900/CR900/CU900 LED consoles pick Bike or Elliptical (`ce900-2025-console-engineering-mode-unit-type`).

