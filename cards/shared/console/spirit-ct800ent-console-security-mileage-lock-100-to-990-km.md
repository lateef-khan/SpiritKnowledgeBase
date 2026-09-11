---
id: spirit-ct800ent-console-security-mileage-lock-100-to-990-km
title: Locking the machine after 100 to 990 km with a four-digit password, and the
  2222 override
kind: procedure
question: How do I set or clear the mileage lock on a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill?
asked_as:
- how do i lock the treadmill after so many kilometres
- the console is locked and asking for a password
- what is the master password for the spirit ent console
- how do i unlock the mileage lock
keywords:
- security
- mileage lock
- lock mode
- accumulate mileage
- password
- '2222'
- kilometres
- unlock
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-security-distance-lock
- ce800ent-security-mileage-lock
- ct850-2016-mileage-lock
- ct900ent-console-security-distance-lock-100-to-9999-miles-password-2222
see_also:
- spirit-ct800ent-console-engineering-mode-seven-submenus
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT section 8-8 Engineering Mode Instructions, PDF p. 43 (printed
    43); text.md lines 853-862. The CT850ENT-2022 service manual prints the same page
    word for word on its PDF p. 44, text.md lines 872-881
  extracted_at: '2026-09-11'
---

Security in engineering mode sets a lock that trips at an accumulated mileage.

The screen carries **Lock Mode**, **Set Lock Accumulate Mileage** (the screenshot shows **100 - 990**
as the range beside the Mileage field), **Set Lock Password to Activate** and **Confirm Set Lock
Password to Activate**.

The instructions, word for word:

1. Set a four-digit number password and the number of kilometers you want to lock.
2. Can use the set password to unlock or use the password **2222** to unlock.

**So 2222 is a master unlock code on this console.** The mileage is in **kilometres**, and the
printed range is 100 to 990. The CU900ENT bike sets the same lock in **miles** with a range of 100 to
9999 (`cu900ent-security-distance-lock`); the CE800ENT elliptical prints no range
(`ce800ent-security-mileage-lock`). Both accept 2222 as well.

**The LED CT850 sets a mileage lock a completely different way** - three numeric keys held with the
safety key out, and no master password: `ct850-2016-mileage-lock`.

