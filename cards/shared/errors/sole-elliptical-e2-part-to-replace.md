---
id: sole-elliptical-e2-part-to-replace
title: 'E2 error on an elliptical: gear motor, incline/brake controller or induction brake'
kind: troubleshooting
question: What part do I replace when a Sole E20, E25, E35 or E55 elliptical shows an E2 error?
asked_as:
- e2 error on my sole elliptical
- elliptical says e2 what part do i replace
- e2 code after moving my elliptical
- gear motor issue on elliptical
keywords:
- e2
- gear motor
- incline brake controller
- induction brake
- computer cable
- display board
- pin test
- elliptical
facets:
  brand:
  - sole
  product_line: elliptical
  model: '*'
  applies_to:
  - e20-2013
  - e20-2014
  - e20-2015
  - e25-2007
  - e25-2013
  - e25-2014
  - e25-2015
  - e35-2007
  - e35-2013
  - e35-2014
  - e35-2015
  - e55-2006
  - e55-2014
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
  code: e2
authority: 2
not_to_be_confused_with:
- sole-e2-error
see_also:
- sole-rower-e1-part-to-replace
- sole-rower-e2-part-to-replace
source:
  ref: sole-el-e2-error-elliptical
  locator: whole document
  extracted_at: '2026-09-19'
---

**This is E2, not E1 (the EEPROM / display-board fault).**

E2 means the machine sees something wrong with the gear motor, or cannot talk to it.

1. Ask whether the machine has recently been assembled, disassembled or moved.
   - **Yes** - replace the **Computer Cable**.
   - **No** - replace the **Gear Motor**, if the machine has one.
2. If the gear motor was replaced and did not fix it, or the machine has no gear motor, replace the **Incline/Brake Controller**.
3. If E2 is still present, replace the **Display Board**.
4. On a machine with an induction brake, if E2 is still present after that, replace the **Induction Brake**.

**Older than 2016, there is a pin test.** Pass, replace the Display Board. Fail, replace the **Computer Cables**, the **Incline/Brake Controller** and the **Gear Motor**.

(The source scrambles one sentence across a line break - "the machine d[oes not]..." - the reading above follows the rower note's word order for the same step.)
