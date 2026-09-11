---
id: spirit-xe-2007-errors-no-speed-distance-or-rpm-align-the-sensor-and-magnet
title: 'No speed, distance or RPM reading: the sensor must point straight at the large
  pulley and the pulley must carry its magnet'
kind: troubleshooting
question: Why does a Spirit XE100-2007, XE200-2007, XE300-2007, XE400-2007 or XE500-2007
  elliptical show no speed, distance or RPM?
asked_as:
- no rpm reading on my spirit xe300
- elliptical speed stays at zero
- xe200 distance not counting
- speed sensor magnet elliptical
keywords:
- no speed
- no rpm
- no distance
- speed sensor
- magnet
- pulley
- sensor alignment
- round disc cover
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe100-2007
  - xe200-2007
  - xe300-2007
  - xe400-2007
  - xe500-2007
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-rpm-shows-zero
see_also:
- ces880-2025-errors-rpm-shows-zero
- spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: XE100-XE500 2007 dealer service manual Troubleshooting Guide, ELECTRONIC
    SYSTEM, PDF p. 3, text.md lines 51-98; XE100-XE500 2007 dealer service manual
    Repair Procedures, PROCEDURE 3 and PROCEDURE 4, PDF p. 6, text.md lines 170-202
  extracted_at: '2026-09-11'
---

`No speed, distance, or RPM reading`
1. Check for proper alignment of speed sensor. (Procedure 4)
2. Check flywheel for magnet. (Procedure 4)

**Procedure 4 - alignment of speed sensor and magnet.**
1. Using a flat screwdriver or a knife, take off the **round disc cover on the left side** of the unit.
2. Turn the pedal so the bigger opening is at the top of the hole.
3. **The sensor should be pointing directly at the large pulley, and there should be a magnet on the pulley.**

**No gap figure is printed** - the 2007 book asks only that the sensor point at the pulley and that the magnet be there. The parts lists name the **300mm Sensor W/Cable (000184)**, its **Sensor Rack (022989)** and the **Magnet (010041)**; the XE200 to XE500 flywheels are listed as *with 6 magnets*, the XE100's flywheel entry names no count, and every list carries the magnet as a separate part. The CES880 2025 elliptical prints a 2 mm sensor-to-magnet gap for the same symptom (`ces880-2025-errors-rpm-shows-zero`); that figure is that machine's.

The row says *speed, distance, or RPM* because the console derives all three from the same pulse; a console that shows time and calories but none of those three is the sensor.
