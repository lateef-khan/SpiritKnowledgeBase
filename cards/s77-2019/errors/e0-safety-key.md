---
id: s77-2019-e0-safety-key
title: 'E0: the console cannot see the safety key'
kind: troubleshooting
question: What does E0 mean on a Sole S77-2019 treadmill?
asked_as:
- e0 error on my treadmill
- s77 shows e0 when i take the key out
- what is error e zero
keywords:
- e0
- safety key
- safety module
- 12v loop
- main control wire
- display board
- display mode
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- s77-2019-e1-no-rpm-signal
- s77-2019-e2-over-current
- s77-2019-e3-incline-vr
- s77-2019-e4-motor-power-wire
see_also:
- s77-2019-error-code-list
- s77-2019-maintenance-menu
- sole-safety-key-not-detected
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.1 Error Message: E0, pages 36-37'
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no RPM signal) and not E2 (over current).**

**Meaning**: the console has no safety key fitted, or the safety module is broken, or a component of the upper control board or the lower controller is broken.

**Why it happens.** With no safety key the console cannot form the +12V safety switch loop, so E0 appears. The +12V comes up from the **lower controller**, through the S/W line of the main control wire, to the upper control board - so a broken main control wire or lower controller shows the same code.

**Check the software setting before the hardware.** E0 after the key is removed can be the console's Display Mode setting rather than a fault:

1. Remove the safety key.
2. Press **STOP, START and ENTER** together and, at the same time, insert the safety key. The display goes into engineering mode.
3. Use the FAST/SLOW or UP/DOWN keys to find **functions**, press Enter to reach **DISPLAY MODE**, then Enter to choose on or off.
4. **Off** means the display goes off after the key is removed. **On** means the display stays on and shows E0 after the key is removed.

**Then the hardware**

| Part | What to do |
|---|---|
| Safety module | Fit the safety key, then use a multimeter on continuity to check whether the safety module wires are shorted |
| Main control wires | Reseat the main control wire; replace it |
| Display board | Replace the upper control board |
