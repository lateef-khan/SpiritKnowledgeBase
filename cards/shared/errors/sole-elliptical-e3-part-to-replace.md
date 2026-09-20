---
id: sole-elliptical-e3-part-to-replace
title: 'E3 error on an elliptical: incline motor, controller or calibration'
kind: troubleshooting
question: What part do I replace when a Sole E20, E25, E35, E55, VE, AE or WE elliptical shows an E3 error?
asked_as:
- e3 error on my sole elliptical
- elliptical incline error what do i replace
- e3 after replacing the console on elliptical
- incline motor not moving on elliptical
keywords:
- e3
- incline error
- incline motor
- incline brake controller
- calibration
- computer cable
- display board
- pin test
facets:
  brand:
  - sole
  product_line: elliptical
  model: '*'
  applies_to:
  - ae25-2011
  - ae35-2011
  - ae55-2011
  - ae95-2011
  - e20-2013
  - e20-2014
  - e20-2015
  - e20-2016
  - e20-2020
  - e20-2026
  - e25-2007
  - e25-2013
  - e25-2014
  - e25-2015
  - e25-2016
  - e25-2026
  - e35
  - e35-2007
  - e35-2013
  - e35-2014
  - e35-2015
  - e35-2016
  - e35-2026
  - e55-2006
  - e55-2014
  - e55-2016
  - e75-2007
  - e95
  - e95-2007
  - e95-2013
  - e95-2014
  - e95-2015
  - e95-2019
  - e95-2023
  - e95-2026
  - e95s
  - e95s-2015
  - e95s-2023
  - e98
  - e98-2011
  - e98-2013
  - e98-2015
  - e98-2023
  - ve25-2007
  - ve35-2007
  - ve55-2007
  - ve95-2007
  - we25-2009
  - we25-2010
  - we35-2009
  - we35-2010
  - we55-2009
  - we55-2010
  - we95-2009
  - we95-2010
  section: errors
  code: e3
authority: 2
not_to_be_confused_with:
- sole-e3-error
see_also:
- sole-elliptical-e2-part-to-replace
- e35-2019-e3-ramp-error
- e35-2019-incline-calibration
source:
  ref: sole-el-e3-error-elliptical
  locator: whole document
  extracted_at: '2026-09-19'
---

**This is E3, the incline fault - not E2 (gear motor).**

E3 means the machine sees something wrong when driving the incline motor. It can appear after the console, the incline/brake controller or the incline motor was replaced without a recalibration afterwards, so always run a calibration first.

If the machine was recently assembled **and** it fails calibration, replace the **Computer Cable** and the **Incline Power Cords**.

1. Run a calibration.
   - Pass: press **Start**, then **Incline Up**. If it inclines and declines, it is fixed. If E3 comes back, go to step 2.
   - Fail, or E3 still present: go to step 2.
2. Ask whether the incline motor moved at all.
   - **Yes** - the signal back up to the console is interrupted.
     - 2016 or newer: replace the **Incline/Brake Controller** or the **Display Board**.
     - Older than 2016: run a pin test. Pass, replace the **Computer Cable** and the **Display Board**. Fail, replace the **Computer Cable** and the **Incline/Brake Controller**.
   - **No** - the signal down to the controller is interrupted.
     - 2016 or newer: replace the **Incline/Brake Controller** or the **Incline Motor**.
     - Older than 2016: run a pin test. Pass, replace the **Computer Cable** and the **Display Board**. Fail, replace the **Computer Cable** and the **Incline/Brake Controller**.
