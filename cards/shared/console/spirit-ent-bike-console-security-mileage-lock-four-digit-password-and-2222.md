---
id: spirit-ent-bike-console-security-mileage-lock-four-digit-password-and-2222
title: Locking the bike after a set number of kilometres with a four-digit password,
  and the 2222 override
kind: procedure
question: How do I set or clear the mileage lock on a Spirit CR800ENT-2023 or CU800ENT-2022
  bike?
asked_as:
- how do i lock the ent bike after so many kilometres
- the bike console is locked and asking for a password
- what is the master password for the spirit bike touchscreen
- how do i unlock the mileage lock on the cr800ent
keywords:
- security
- mileage lock
- lock mode
- accumulate mileage
- password
- '2222'
- kilometres
- unlock
- engineering mode
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-security-distance-lock
- ce800ent-security-mileage-lock
- spirit-ct800ent-console-security-mileage-lock-100-to-990-km
see_also:
- spirit-ent-bike-console-engineering-mode-six-submenus
- ce800ent-security-mileage-lock
- cu900ent-security-distance-lock
source:
  ref: spirit-bike-cr800ent-2023-service-manual
  locator: CR800ENT section 7-4 Engineering Mode Instructions, Security, PDF p. 31
    (printed 31); text.md lines 492-501, screenshot read from the OCR supplement for
    PDF page 31. The CU800ENT-2022 service manual prints the same page word for word
    on its PDF p. 31, text.md lines 485-494
  extracted_at: '2026-09-11'
---

Security in engineering mode sets a lock that trips at an accumulated mileage.

The screen carries **Lock Mode** (shown ON), **Set Lock Accumulate Mileage** (shown at **100**),
**Set Lock Password to Activate** and **Confirm Set Lock Password to Activate**.

The instructions, word for word:

1. Set a four-digit number password and the number of kilometers you want to lock.
2. Can use the set password to unlock or use the password **2222** to unlock.

**So 2222 is a master unlock code on this console.** The mileage is in **kilometres**, and the book
prints no range - 100 is only the value in the screenshot.

**The CU900ENT sets the same lock in miles**, with a printed range of 100 to 9999
(`cu900ent-security-distance-lock`); the CT800ENT-2022 treadmill prints a range of 100 to 990 km
(`spirit-ct800ent-console-security-mileage-lock-100-to-990-km`); the CE800ENT elliptical prints
exactly this page (`ce800ent-security-mileage-lock`). All of them accept 2222.
