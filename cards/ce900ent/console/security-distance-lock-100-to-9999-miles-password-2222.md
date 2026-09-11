---
id: ce900ent-console-security-distance-lock-100-to-9999-miles-password-2222
title: Security locks the machine when the accumulated distance reaches a set value
  of 100 to 9999 miles, and 2222 is the default unlock password
kind: procedure
question: How do I lock a Spirit ce900ent elliptical after a set distance, and what
  is the default password?
asked_as:
- how do i lock the ce900ent after so many miles
- ce900ent security password
- ce900ent console locked at a distance
- what is the default password on the ce900ent
keywords:
- security
- distance lock
- lock mode
- accumulate mileage
- 100 to 9999 miles
- password
- '2222'
- hold up three seconds
- unlock
- engineering mode
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: console
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with: []
see_also:
- ce900ent-console-engineering-mode-seven-settings-entries-machine-information-first
- ce900ent-console-machine-information-machine-type-gs-mode-child-lock-speaker-and-versions
- cu900ent-security-distance-lock
- ce800ent-security-mileage-lock
- ct850-2016-mileage-lock
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Security screen, PDF p. 27
    (printed 27); text.md lines 414-424, and the screenshot in the OCR supplement
    for PDF page 27, lines 1739-1763
  extracted_at: '2026-09-11'
---

Security in engineering mode sets a lock that trips at an accumulated distance.

| Control | What it does |
|---|---|
| LOCK MODE | Sets the distance locking function. When the distance reaches the set value the display and buttons lock and cannot be used. |
| SET LOCK ACCUMULATE MILEAGE | Sets the value of DISTANCE, **100 to 9999 Miles**. |
| SET LOCK PASSWORD TO ACTIVATE | Sets the password used to unlock DISTANCE. |

**To unlock:** press and hold **UP** for 3 seconds. "This is an unlock function once only."

> If password forgets, use default password 2222 to unlock the DISTANCE.

The distance is in **miles** here, with the range 100 to 9999 printed. The CE800ENT sets the same
lock in **kilometres** and prints no range at all (`ce800ent-security-mileage-lock`); the CT800ENT
family prints 100 to 990 km. All accept 2222.

**The child lock under Machine Information is a different lock with the same three-second UP-key
release**
(`ce900ent-console-machine-information-machine-type-gs-mode-child-lock-speaker-and-versions`).

**The CU900ENT and CR900ENT bikes print this screen word for word**
(`cu900ent-security-distance-lock`).
