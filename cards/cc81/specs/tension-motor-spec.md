---
id: cc81-tension-motor-spec
title: "Tension motor rating and what it does"
kind: spec
question: "What is the tension motor spec on a Sole CC81 climber?"
asked_as:
- "what voltage is the resistance motor on the sole climber"
- "how many resistance levels does the cc81 have"
- "what changes the resistance on my climber"
keywords:
- "tension motor"
- "gear motor"
- "resistance"
- "brake"
- "steel cable"
- "working voltage"
- "levels"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81
  applies_to:
  - cc81
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-tension-motor-console-output-check
- cc81-tension-motor-voltage-test
- cc81-tension-motor-connector-pinout
- cc81-e2-tension-motor-failure
source:
  ref: sole-climber-cc81-service-manual
  locator: "Section 3 Electrical Configurations, part description table, and Section 4-3-4 LEVEL"
  extracted_at: '2026-09-03'
---

| Field | Value as printed |
|---|---|
| What it does | Increases or decreases the resistance level of the brake. |
| Working voltage | **DC 4.5 to 7.5 V** |
| Working resistance levels | 1 to 20 |
| Displayed level range | 0 to 99 |
| Drive | The motor pulls a steel cable. |

The console drives the motor directly. **The drive voltage the console puts out is a different figure from the working voltage above** — see [`cc81-tension-motor-console-output-check`](../errors/tension-motor-console-output-check.md).
