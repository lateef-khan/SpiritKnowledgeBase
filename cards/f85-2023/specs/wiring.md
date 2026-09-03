---
id: f85-2023-wiring
title: Wiring and part numbers for the 2023 F85
kind: spec
question: How is the F85-2023 (585822) wired?
asked_as:
- wiring diagram for the 2023 f85
- which parts are in the f85 power path
keywords:
- wiring diagram
- '585822'
- rear incline controller
- filter
- computer cables
- motor controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2023
  applies_to:
  - f85-2023
  section: specs
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also:
- sole-start-button-grayed-2023
source:
  ref: sole-tm-f85-585822-2023-wiring-diagram
  locator: whole document
  extracted_at: '2026-09-03'
---

Model 585822. Full serial prefix seen in the source: 5858222401010453.

**Power path**

| Item | Part | Number | Notes |
|---|---|---|---|
| 50 | Power cord | E060001 | LT-202+511 SJT 14A/3C black 105D 2M |
| 43 | Power socket | F010007 | DB-14/15A/125VAC. White goes to the A/C switch, black goes to the breaker |
| 42 | Breaker | F020019 | |
| 45 | 100 mm connecting wire (black) | E010747 | Breaker to AC module |
| 44 | AC electronic module | F030008 | |
| 48 | 200 mm connecting wire (white) | E010752-01 | AC module to filter |
| 49 | 200 mm connecting wire (black) | E010753-01 | AC module to filter |
| 155 | Filter | F060117 | |
| 46 | 300 mm connecting wire (white) | E010754 | Filter to rear incline controller, then on to the motor controller |
| 47 | 300 mm connecting wire (black) | E010755 | Filter to rear incline controller, then on to the motor controller |
| 41 | Rear incline controller | D020621-02 | |
| 36 | Motor controller with bracket | CRD020087 | Also seen as CRD020087-01, and D020087-01 for the board alone. Bracket CRD020117-02 |

**Computer cables**

| Item | Part | Number |
|---|---|---|
| 152 | 950 mm 12-pin computer cable (upper) | E022105-01 |
| 153 | 1400 mm 12-pin computer cable (middle) | E022107 |
| 154 | 1200 mm 13-pin integration lower cable | E022854 |

The lower cable splits at the bottom and plugs into both the motor controller and the rear incline controller. A 6-pin connection from the MCB and a 7-pin connection from the rear incline controller join in one harness to meet the middle computer cable.

**Incline motor** (item 30, G150006) uses a 3-pin VR cable with Up, Com and Down.
