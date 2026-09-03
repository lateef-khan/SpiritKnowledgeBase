---
id: cc81-tension-motor-console-output-check
title: "How the console drives the tension motor, and what it should put out"
kind: troubleshooting
question: "How does the console drive the tension motor on a Sole CC81 climber?"
asked_as:
- "what voltage should the climber console send to the resistance motor"
- "resistance motor does not move on my sole climber"
- "how does level up work on the cc81"
keywords:
- "tension motor"
- "console output"
- "drive board"
- "level up"
- "level down"
- "transformer"
- "data cable"
- "beep"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81
  applies_to:
  - cc81
  section: errors
  code: e2
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-tension-motor-voltage-test
- cc81-e2-tension-motor-failure
- cc81-tension-motor-spec
source:
  ref: sole-climber-cc81-service-manual
  locator: "Sections 7-4-1 Tension motor operation and 7-4-2 Tension motor troubleshooting"
  extracted_at: '2026-09-03'
---

**How it should work**

1. The key signal travels to the display. The main program IC then sends a command signal to the drive board.
2. The console controls the motor directly. **Level UP: +4 to 5 VDC. Level DOWN: -4 to 5 VDC.**

**How to check it**

1. If the key beeps when pressed, take it that the signal was sent.
2. Inspect the console power output to the motor. Level Up is **+4 to 5 VDC**, Level DOWN is **-4 to 5 VDC**.
   - Power reaches the motor but the motor does not run → **replace the motor**.
   - No power output → **inspect whether the transformer has power**.
3. Data cable: inspect the cable and the connections.

**The manual prints two different voltage figures for the same measurement.** This section says 4 to 5 VDC. The step-by-step test in section 7-4-3 says **5 to 6 VDC** as the normal reading at the drive board. The manual never says how the two relate. Both are recorded as printed — see the card `cc81-tension-motor-voltage-test` for the other half.
