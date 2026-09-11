---
id: spirit-xt-errors-e1-check-rpm-sensor-procedure
title: 'Checking the RPM speed sensor after an E1: cable, magnet, a gap under 3 mm,
  then sensor, cable and console'
kind: procedure
question: How do I check the speed sensor after an E1 on a Spirit XT 2015, XT 2023
  or XT ENT treadmill?
asked_as:
- how to check the speed sensor on my spirit xt
- rpm sensor gap for e1
- speed sensor magnet alignment treadmill
keywords:
- e1
- rpm sensor
- speed sensor
- reed switch
- magnet
- gap
- 3 mm
- front roller pulley
- computer cable
- replace console
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- ct850-2016-low-speed-check-rpm-sensor
see_also:
- spirit-xt-errors-e1-solution-flow-chart
- xt-2023-errors-e1-motor-not-responsive
- xt-2023-maintenance-adjusting-the-speed-sensor
- xt-2015-errors-calibration-does-not-pass
source:
  ref: spirit-treadmill-xt485-2023-service-manual
  locator: XT185 2023 service manual E1 solution follow chart - check RPM sensor device
    procedure, and Checking the speed sensor, PDF p. 22-23, text.md lines 428-475;
    XT285 2023 service manual E1 solution follow chart - check RPM sensor device procedure,
    and Checking the speed sensor, PDF p. 23-24, text.md lines 430-477; XT385 2023
    service manual E1 solution follow chart - check RPM sensor device procedure, and
    Checking the speed sensor, PDF p. 24-25, text.md lines 391-434; XT485 2023 service
    manual E1 solution follow chart - check RPM sensor device procedure, and Checking
    the speed sensor, PDF p. 24-25, text.md lines 391-434; XT685 2023 service manual
    E1 solution follow chart - check RPM sensor device procedure, and Checking the
    speed sensor, PDF p. 23-24, text.md lines 435-480; XT185 2015 service manual check
    RPM sensor device procedure, and Checking the speed sensor, PDF p. 41-42, text.md
    lines 662-689; XT285 2015 service manual check RPM sensor device procedure, and
    Checking the speed sensor, PDF p. 42-43 (printed 41-42), text.md lines 731-758;
    XT385 2015 service manual check RPM sensor device procedure, and Checking the
    speed sensor, PDF p. 42-43, text.md lines 620-638; XT485 2015 service manual check
    RPM sensor device procedure, and Checking the speed sensor, PDF p. 42-43, text.md
    lines 620-638; XT485ENT 2023 service manual check RPM sensor device procedure,
    and Assembling the speed sensor, PDF p. 38-39, text.md lines 535-553; XT685ENT
    2023 service manual check RPM sensor device procedure, and Checking the speed
    sensor, PDF p. 25-26, text.md lines 401-427
  extracted_at: '2026-09-11'
---

This is the branch the E1 flow chart sends you to when the belt moved after start. The chart is a picture in every book; it was read from the rendered page.

1. **Is the sensor cable connected properly?** No -> connect it properly.
2. Move the roller so that the magnet is closest to the sensor.
3. **Make sure the gap between magnet and sensor is less than 3 mm.** No -> adjust the sensor position.
4. Replace the sensor with cable.
5. Turn the power back on, press "start" and count down. **Is the function OK?** Yes -> problem fixed.
6. No -> replace the computer cable. Turn the power back on, press "start" and count down. Yes -> problem fixed.
7. No -> replace the console.

How to reach the sensor, from the page that follows (*Checking the speed sensor* in the 2015 and 2023 books, *Assembling the speed sensor* in the XT485ENT):

1. Remove the motor cover hood.
2. The speed sensor is on the **left side of the frame**, right next to the front roller pulley - the pulley with a belt around it that also goes to the motor. The sensor is small and black with a wire connected to it.
3. Make sure the sensor is as close as possible to the pulley without touching it. There is a magnet on the face of the pulley; align the sensor with it. One screw holds the sensor; loosen it to adjust and re-tighten it when finished.

The books call it a **reed switch** RPM speed sensor device.

The main E1 chart prints **2 mm** for the same gap (`spirit-xt-errors-e1-solution-flow-chart`); this chart and the troubleshooting form print **less than 3 mm**. The owner's-manual alignment page prints no figure at all (`xt-2023-maintenance-adjusting-the-speed-sensor`). The sensor's own replacement steps are a parts procedure and not on this card.
