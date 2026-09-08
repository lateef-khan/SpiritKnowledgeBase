---
id: ct850-2016-low-speed-check-rpm-sensor
title: Checking the RPM speed sensor after a LOW SPEED message
kind: procedure
question: How do I check the speed sensor after a LOW SPEED message on a Spirit CT850-2016
  treadmill?
asked_as:
- how to check the speed sensor on a spirit treadmill
- rpm sensor gap on a treadmill
- speed sensor adjustment ct850
keywords:
- rpm sensor
- speed sensor
- reed switch
- magnet
- gap
- front roller pulley
- sensor position
- low speed
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: low-speed
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-low-speed-solution-flow-chart
- ct850-2016-low-speed-troubleshooting-form
- ct850-2016-low-speed-error-message
- ct850-2016-speed-sensor-replacement
- ct850-2016-front-rear-roller-replacement
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 8.1, LOW SPEED solution follow chart - check RPM sensor device
    procedure, page 33 (printed 32), and Checking the speed sensor, page 34 (printed
    33). Page 33 is a flattened image and was read from raw/page-33.png
  extracted_at: '2026-09-08'
---

This is the branch the main flow chart sends you to when the belt **did** move after start.

1. **Is the sensor cable connected properly?** If not, connect it properly.
2. Move the roller so that the magnet is closest to the sensor.
3. **Make sure the gap between magnet and sensor is less than 3 mm.** If it is not, adjust the
   sensor position.
4. Replace the sensor with cable.
5. Turn the power back on, press "start" and count down. If it works, the problem is fixed.
6. If not, replace the computer cable. Turn the power back on, press "start" and count down. If it
   works, the problem is fixed.
7. If not, replace the console.

How to get at the sensor, from the facing page:

1. Remove the motor cover hood.
2. The speed sensor is on the **left side of the frame**, right next to the front roller pulley -
   the pulley with a belt around it that also goes to the motor. The sensor is small and black with
   a wire connected to it.
3. Make sure the sensor is as close as possible to the pulley without touching it. There is a magnet
   on the face of the pulley; make sure the sensor is aligned with the magnet. Loosen the screw that
   holds the sensor to adjust it, and re-tighten it when finished.

It is a **reed switch** RPM speed sensor device.

The 3 mm figure is the one printed in the flow chart and repeated in the troubleshooting form on
`ct850-2016-low-speed-troubleshooting-form`.

When the flow chart reaches `Replace the sensor with cable`, the removal procedure is on
`ct850-2016-speed-sensor-replacement`. The magnet this sensor reads sits on the face of the front
roller pulley, so a roller change disturbs it: `ct850-2016-front-rear-roller-replacement`.
