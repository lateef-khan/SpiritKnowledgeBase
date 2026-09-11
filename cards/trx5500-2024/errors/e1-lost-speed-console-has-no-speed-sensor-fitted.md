---
id: trx5500-2024-errors-e1-lost-speed-console-has-no-speed-sensor-fitted
title: 'E1 / Lost Speed: the console has a digital controller with no speed sensor,
  so a technician brings a sensor and fits it to calibrate'
kind: fact
question: Why is there no speed sensor on an Xterra trx5500-2024 treadmill, and what
  does that mean for an E1?
asked_as:
- trx5500 has no speed sensor
- trx5500 e1 lost speed calibration
- do i need a speed sensor to calibrate the trx5500
keywords:
- e1
- lost speed
- speed sensor
- no sensor
- digital controller
- calibration
- flywheel
- technician
- pre-set
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx5500-2024
  applies_to:
  - trx5500-2024
  section: errors
  code: e1
  model_number:
  - '155810'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-check-rpm-sensor-procedure
- trx5500-2024-errors-e9-speed-calibration-error
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: 'TRX5500 SM Checking the speed sensor, the two closing paragraphs, PDF
    p. 42 (printed 41); text.md lines 621-642; TRX5500 SM 7-4 Error Message: E1 /
    Lost Speed, PDF pp. 38-39 (printed 37-38); text.md lines 590-609'
  extracted_at: '2026-09-11'
---

The TRX5500 service manual ends its *Checking the speed sensor* page with two sentences no other Xterra book prints:

> The console display board comes with digital controller (speed detection according to input power), the parameters have been pre-set in controller and it is without a speed sensor to detect rotating of motor flywheel.
>
> So, for calibrating speed, technician will need to bring a speed sensor (w/its cable) then install nearby the motor flywheel to do the calibration as procedure listed here.

So on this machine E1 / Lost Speed during calibration can simply mean **no sensor is fitted**: the three-step sensor check (`xterra-treadmill-errors-e1-check-rpm-sensor-procedure`) presumes a sensor that a technician has brought and installed beside the motor flywheel. The E9 speed calibration error on the same machine says the same in its first step - "Install Speed Sensor to Calibrate Speed as ERROR E1 mentioned" (`trx5500-2024-errors-e9-speed-calibration-error`).

The parts replacement guide in the same book still carries a 9-8 Speed Sensor replacement section.
