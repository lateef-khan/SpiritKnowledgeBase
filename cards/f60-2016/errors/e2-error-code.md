---
id: f60-2016-e2-error-code
title: 'E2 error: over current protection'
kind: troubleshooting
question: What does an E2 error mean on a Sole F60-2016?
asked_as:
- e2 error on my treadmill
- treadmill keeps tripping to e2
- over current error on my sole
keywords:
- e2
- e2 error
- over current
- overload
- silicone oil
- limit current
- lower controller
- 18a
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- f60-2016-e0-error-code
- f60-2016-e1-error-code
- f60-2016-incline-er-message
- f60-2016-e4-error-code
- f60-2016-e5-error-code
- f60-2016-e6-error-code
see_also:
- f60-2016-error-code-list
- f60-2016-belt-deck-lubrication
source:
  ref: sole-tm-f60-2016-service-manual
  locator: page 54, 8.4 Error Message E2
  extracted_at: '2026-09-04'
---

**This is E2, not E0 and not E6.** The incline fault on this machine is ER, not E2.

**Definition**: the lower controller has entered over current protection.

**Cause**: the motor is already overloading, so the lower controller supplies more and more voltage and current for it. Left alone, the lower controller would eventually be destroyed, so it limits its current to protect the whole system and itself.

**The current limits printed in this manual:**

| Supply | Limit |
|---|---|
| 220V | **18A** |
| 110V | **19A** |

| Possible cause | Things to check | Solution |
|---|---|---|
| Motor is overloading | Whether the treadmill limited load is exceeded | Do not overload |
| The running belt possibly has no lubricating oil | The friction between running belt and running board rises, so the current climbs | Add silicone oil |
| Lower controller or motor is bad | Lower controller circuit components may be bad, or the motor may be bad | Change the lower controller. Change the motor. |
