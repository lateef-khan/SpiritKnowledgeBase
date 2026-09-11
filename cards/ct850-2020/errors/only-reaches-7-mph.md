---
id: ct850-2020-only-reaches-7-mph
title: The belt only reaches about 7 mph while the display shows more, on the row
  that demands a minimum of 100 volt AC
kind: troubleshooting
question: Why does a Spirit CT800 2020, CT800ENT, CT850 2020, CT850ENT, 4.0T or 2024
  ENT treadmill only reach about 7 mph?
asked_as:
- treadmill will not go faster than 7 mph
- belt slower than the speed on the display
- spirit treadmill loses speed
keywords:
- 7 mph
- 10 kph
- extension cord
- gauge
- low voltage
- electrician
- speed shortfall
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 40t-2026
  - ct800-2020
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2020
  - ct850ent-2022
  - ct850ent-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ct850-2016-only-reaches-7-mph
- ct800-2020-errors-speed-caps-at-7-mph
see_also:
- ct850-2016-only-reaches-7-mph
- ct800-2020-errors-speed-caps-at-7-mph
- ct800-2016-errors-only-reaches-7-mph-120-volt-60-hz
- ct900ent-errors-only-reaches-7-mph-14-gauge-110-volt
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: 'Section 8-6 TROUBLESHOOTING, page 46 (printed 45); CT800 2020 service
    manual 8-5 TROUBLESHOOTING, PDF p. 45 (printed 44), text.md lines 631-660; CT800ENT
    2022 service manual 8-7 Troubleshooting, PDF p. 39, text.md lines 791-819; CT850ENT
    2022 service manual 8-7 Troubleshooting, PDF p. 40, text.md lines 810-838; 4.0T
    2026 service manual TROUBLESHOOTING, PDF p. 35 (printed 46), text.md lines 523-566;
    the 4.0T ST8700A-ST026-01 service manual (spirit-treadmill-40t-2026-service-manual-st8700a,
    88% the ST017 book) prints the same page one page later, word for word (compared
    with difflib on 2026-09-11): TROUBLESHOOTING at PDF p. 36 (printed 46), text.md
    lines 592-635'
  extracted_at: '2026-09-08'
---

The condition is printed as `Treadmill will only achieve approximately 7mph /10 kph but shows
higher speed on display`. The manual's answer, word for word:

> This indicates motor should be receiving power to operate. Do not use an extension cord. If an
> extension cord is required it should be as short as possible and heavy duty 16-gauge minimum, low
> voltage. Contact an electrician or your dealer. A minimum of 100 volt AC current is required.

Two numbers to hold on to: **16-gauge minimum** for an extension cord, and **100 volt AC minimum**
at the outlet.

**The CT850 2016 service manual prints different figures for the same fault** - 12 gauge and a
minimum of 110 volt AC, 60 Hz. See `ct850-2016-only-reaches-7-mph`.

**The CT850 2020 owner's manual contradicts this service manual for the same machine.** It prints
the row without the `/10 kph`, and demands **a minimum of 120 volt AC** rather than 100
(`ct800-2020-errors-speed-caps-at-7-mph`). Nothing in either document reconciles the two.

**The CT800ENT 2024 and CT850ENT 2024 owner's manuals print this row word for word**, on printed
page 59 of both books - the `/10 kph`, the 16-gauge minimum, the 100 volt AC minimum and even
`Contact an electrician or your dealer` rather than *your Spirit Fitness dealer*. Both pages are
flat pictures with no text layer and were read from the rendered page. So the figures that were only
in a service manual until now are printed in an owner's manual too.

**Their non-ENT siblings in the same 2024 family disagree with them.** The CT800 2024 and CT850 2024
print the same row without the `/10 kph` and demand **a minimum of 120 volt AC**
(`ct800-2020-errors-speed-caps-at-7-mph`) - and the same page of those books then names a **230 VAC**
outlet in its `Display does not light` row
(`spirit-2024-errors-display-does-not-light-230-vac-outlet`). Three supply figures across one
model year.

**The predecessors of the two ENT machines used 12 mph in this row**, not 7
(`ct800ent-2022-errors-speed-caps-at-12-mph`). The 2024 books dropped the threshold back to 7 mph
and say nothing about why.

**Four more service manuals print this row word for word** - `7mph /10 kph`, 16-gauge minimum, `A minimum of 100 volt AC current is required` - the CT800 2020, CT800ENT 2022, CT850ENT 2022 and 4.0T. Each contradicts its own owner's manual: the CT800 2020 owner's manual demands 120 volt (`ct800-2020-errors-speed-caps-at-7-mph`), the CT800ENT 2022 and CT850ENT 2022 owner's manuals put the threshold at 12 mph (`ct800ent-2022-errors-speed-caps-at-12-mph`), and the 4.0T owner's manual prints no voltage at all (`40t-2026-errors-speed-caps-at-7-mph`). The CT800 2016 service manual prints 120 volt AC at 60 Hz (`ct800-2016-errors-only-reaches-7-mph-120-volt-60-hz`) and the CT900ENT 110 volt with a 14 gauge cord (`ct900ent-errors-only-reaches-7-mph-14-gauge-110-volt`).
