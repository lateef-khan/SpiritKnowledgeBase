---
id: spirit-ct800ent-console-lube-setup-default-4000-hours
title: 'Lube Setup: the lube reminder defaults to 4000 hours, beside a cumulative
  distance, a cumulative time and a Zeroing key'
kind: fact
question: How is the lube reminder set on a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill console?
asked_as:
- how do i reset the lube reminder on the ent treadmill
- how many hours until the lube message
- where is the lube setting on the touchscreen
- how do i zero the cumulative time
keywords:
- lube setup
- lube suggest
- 4000 hours
- cumulative distance
- cumulative time
- zeroing
- lube reminder
- engineering mode
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
- ct900-engineering-mode-menu
- tt8-2023-lube-setup
- f80-2023-lube-setup
see_also:
- spirit-ct800ent-console-engineering-mode-seven-submenus
- spirit-ct800-maintenance-belt-deck-cleaning-4000-hours
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT section 8-8 Engineering Mode Instructions, PDF p. 52 (printed
    52); text.md lines 923-930. The CT850ENT-2022 service manual prints the same page
    word for word on its PDF p. 53, text.md lines 942-949
  extracted_at: '2026-09-11'
---

The Lube Setup entry of engineering mode has one line: **"Set Lube Suggest, the default is 4000Hrs."**

The screen shows **Cumulative Distance** (11.61 km in the screenshot), **Cumulative Time** (1.16 hr)
and a **Zeroing** key. The manual does not say what message the console shows when the figure is
reached, and gives no range for the setting.

**4,000 hours is also the rating of the deck** - the maintenance chapter of the same manuals
describes a belt/deck combination rated at 4,000 hours a side
(`spirit-ct800-maintenance-belt-deck-cleaning-4000-hours`) - so the default reminder falls due when
the deck is due to be flipped, not when the belt is due to be lubricated. The LED CT800 and CT850
consoles reset their lube message from an engineering-mode Maintenance entry and print no hours
figure (`ct900-engineering-mode-menu`).

The Sole touchscreen treadmills in the same Dyaco console family default their lube reminder to 90
hours; do not carry that figure here.

