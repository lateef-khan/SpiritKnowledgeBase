---
id: ce800ent-no-resistance
title: The machine gives no resistance, and the control board is the first part to
  replace
kind: troubleshooting
question: Why is there no resistance on a Spirit CE800-2024, CE800ENT or CE800ENT-2024
  elliptical or a CR800-2021, CR800-2024, CR800ENT-2023, CR800ENT-2024, CU800-2012,
  CU800-2021, CU800-2024, CU800ENT-2022 or CU800ENT-2024 bike?
asked_as:
- no resistance on my spirit elliptical
- pedals feel loose with no load
- elliptical will not add resistance
keywords:
- no resistance
- control board
- generator brake
- resistance voltage wire
- driver ic
- console
- induction brake
- elliptical
- bike
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce800-2024
  - ce800ent
  - ce800ent-2024
  - cr800-2021
  - cr800-2024
  - cr800ent-2023
  - cr800ent-2024
  - cu800-2012
  - cu800-2021
  - cu800-2024
  - cu800ent-2022
  - cu800ent-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-no-resistance
see_also:
- cvc800-e-2-tension-motor-error
- ces880-2025-errors-no-resistance
- cu800-2012-errors-no-resistance-check-the-brake-coil-harness
- spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: CE800ENT service manual section 7-3 Troubleshooting procedure matrix, page
    27; CU800ENT 2024 owner's manual TROUBLESHOOTING, printed page 50 (that page is
    a flat picture and was read from the rendered page); CU800ENT 2020-ver book (cu800ent-2022)
    service manual 7-3 Troubleshooting procedure matrix, PDF p. 27, text.md lines
    418-452; CR800ENT 2020-ver book (cr800ent-2023) service manual 7-3 Troubleshooting
    procedure matrix, PDF p. 27, text.md lines 425-459; CU800 2020-book (cu800-2021)
    service manual 7-5 Troubleshooting procedure matrix, PDF p. 27 (printed 26), text.md
    lines 420-451; CR800 2020-book (cr800-2021) service manual 7-5 Troubleshooting
    procedure matrix, PDF p. 27 (printed 26), text.md lines 398-429; CU800 2012 (XU878)
    service manual Troubleshooting procedure matrix, PDF p. 35, text.md lines 541-573
  extracted_at: '2026-09-08'
---

| Reason | Solve |
|---|---|
| Control board are broken | Replace with new Control board |
| Generator brake resistance voltage wire shedding | Please re-install wire |
| Driver IC broken | Replace the new console |

The CE800ENT elliptical service manual and the CU800ENT 2024 bike owner's manual print this row
word for word. On the bike the whole troubleshooting page is a flat picture with no text layer.

Note the split: the manuals blame the **control board** for the first cause but the **console** for
the third, because the driver IC they name sits in the console.

Both machines brake with a generator and an induction brake rather than a tension motor, so the
tension-motor tests written for the CVC800 climber do not apply here.

**The CES880 2025 elliptical answers the same symptom with a different list** - resistor, then
controller, then console: `ces880-2025-errors-no-resistance`. Do not carry one part order to the
other machine.

**Five of the 2024 New Black machines print these three causes and three fixes word for word** -
the CE800 2024 and CE800ENT 2024 ellipticals, the CR800 2024 and CR800ENT 2024 recumbent bikes and
the CU800 2024 upright bike.

**On the CR800 2024 and the CU800 2024 the row is printed under the wrong condition.** Both of
those manuals label it `Wireless lost its function.` - the label belonging to the chest-belt row
above it - and neither prints the words `No resistance` anywhere in the table. The CE800 2024
elliptical, whose table is otherwise identical, labels the same three causes `No resistance`. The
rendered page was checked on the CR800 2024 to be sure this is the printed page and not an
extraction fault. Answer a CR800 2024 or CU800 2024 caller who has no resistance from this row
anyway, and do not look for a `No resistance` heading in their book.

**Five more bike service manuals print this row.** The CU800ENT "2020 ver." (`cu800ent-2022`) and CR800ENT "2020 Ver." (`cr800ent-2023`) books print it word for word under `No resistance`. The CU800 2020-book (`cu800-2021`) and the CR800 2020-book (`cr800-2021`) print the three causes and three fixes under the slipped label `Wireless lost its function.` - the same defect the 2024 CR800 and CU800 carry, so it is inherited from these two. **The CU800 2012 (XU878) book prints the row under `No resistance` with only the first two causes and the first two fixes** - control board / replace control board, resistance-voltage wire shedding / re-install wire - and no `Driver IC broken` line at all; its Q&A chapter adds a brake-coil harness check instead (`cu800-2012-errors-no-resistance-check-the-brake-coil-harness`). The XBR25/XBR55 2007 dealer manual answers the same symptom with a DC-voltage test at the controller: `spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller`.
