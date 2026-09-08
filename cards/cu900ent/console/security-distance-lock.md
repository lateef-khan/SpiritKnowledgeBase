---
id: cu900ent-security-distance-lock
title: Locking the machine after a set distance
kind: procedure
question: How do I lock a Spirit CU900ENT bike after a set distance?
asked_as:
- how do i lock the bike console
- bike console is locked and wants a password
- what is the default password on the spirit bike
keywords:
- security
- lock mode
- set lock accumulate mileage
- distance lock
- password
- '2222'
- unlock
- 9999 miles
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800ent-security-mileage-lock
see_also:
- cu900ent-engineering-mode-menu
- cu900ent-machine-information
- ce800ent-security-mileage-lock
- ct850-2016-mileage-lock
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Security screen, p. 27 (printed 27). This page is a flattened image and
    was read from raw/page-27.png, not from the OCR text
  extracted_at: '2026-09-08'
---

Security in engineering mode sets a lock that trips at an accumulated distance.

| Control | What it does |
|---|---|
| LOCK MODE | Sets the distance locking function. When the distance reaches the set value the display and buttons lock and cannot be used. |
| SET LOCK ACCUMULATE MILEAGE | Sets the value of DISTANCE, **100 to 9999 Miles**. |
| SET LOCK PASSWORD TO ACTIVATE | Sets the password used to unlock DISTANCE, entered on the on-screen keypad. |

**To unlock:** press and hold **UP** for 3 seconds. This is a one-time unlock.

> If password forgets, use default password 2222 to unlock the DISTANCE.

The distance is in **miles** here, with the range 100 to 9999 printed. The elliptical in the same
console family sets the same lock in **kilometres** and prints no range at all. Both accept 2222.

The child lock under Machine Information is a different lock with the same three-second UP-key
release.
