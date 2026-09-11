---
id: crw800h2o-console-shows-no-data
title: The console shows no data
kind: troubleshooting
question: Why does the console show no data on a Spirit water rower?
asked_as:
- rower console is blank
- no numbers on my spirit rower display
- spirit water rower monitor not working
- screen is lit but nothing counts when i row
keywords:
- no data
- no display
- battery
- magnet
- mesh belt wheel
- wires
- computer lead
- console
- rower
- sensor gap
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800h2o
  - crw900-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- crw800h2o-console-shows-no-display
- spirit-water-rower-errors-inconsistent-split-time-and-stroke-rate
see_also:
- crw800h2o-console-shows-no-display
- crw800h2o-console-powers-on-by-itself
- crw800h2o-console-shows-no-pulse-data
- spirit-water-rower-errors-inconsistent-split-time-and-stroke-rate
- spirit-rower-errors-no-error-codes-printed
- crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets
source:
  ref: spirit-rower-crw800h2o-service-manual
  locator: CRW800H2O service manual, Section 2 Q&A, Console Error, page 21; and the
    TROUBLESHOOTING table row "The console screen illuminates, but does not register
    when rowing" in the CRW800H2O 2021 owner's manual printed page 34 and the CRW900
    2021 owner's manual printed page 53, both read from a 300 dpi render as well as
    the text layer; CRW900 service manual 1.3 Trouble with console, "The console screen
    illuminates, but does not register when rowing", PDF p. 14, text.md lines 95-101,
    and 1.1 Speed Sensor Troubleshooting, PDF p. 4-5, text.md lines 31-49
  extracted_at: '2026-09-08'
---

The service manual's answer, in its order. The question is printed as `The console without data` and
the answer opens `When there is no display, check as below`.

1. Check if batteries have enough power. If not, change new battery to try.
2. Check if wires are connected properly. If not, try to connect all the wires again.
3. Check if magnets are right in mesh belt wheel. If not, press a new magnet on hole of mesh belt
   wheel.
4. Check if wires have breakage. If yes, change new wire.
5. If all is OK, change a new console.

**The owner's manuals of both water rowers describe the same fault from the customer's side** -
`The console screen illuminates, but does not register when rowing` - and add a check the service
manual leaves out:

| Possible Cause | Instructions |
|---|---|
| Loose or failed connection | Check that the computer lead is connected properly. If it is connected then contact your local service center. |
| Sensor gap too wide | Check sensor gap. |

**The sensor gap is set with the console's own back cover**, used as a gap tool against the magnetic
ring - the same measurement the inconsistent-readings row asks for
(`spirit-water-rower-errors-inconsistent-split-time-and-stroke-rate`). Neither manual prints a gap
figure, so the cover is the only gauge there is.

**Work this list before the shorter one.** The service manual carries a second question that looks
like the same fault and answers it in two steps - `The console without display`, battery and then a
new console, on `crw800h2o-console-shows-no-display`. The magnet in the mesh belt wheel and the
sensor gap are the checks that short answer leaves out, and they are the ones a rower loses data
over.

These are **battery** consoles - both console chapters name 4 AA cells - so there is no mains supply
to check, and **neither water rower prints an error code anywhere**
(`spirit-rower-errors-no-error-codes-printed`).

The service manual covers the CRW800H2O only; the CRW900 contributes the owner's manual row.

**For the CRW900 the sensor gap does have a figure - in the service manual.** Its *Trouble with console* page repeats the owner's-manual row word for word (loose or failed connection; sensor gap too wide; check the computer lead, check the sensor gap), and its speed sensor page gives the checks in order: the gap between sensor and magnetic ring **2-3mm**, all **six** magnets present and flush, and the sensor head not receded more than a few millimetres into its hole (`crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets`). That figure is printed for the CRW900 only; the CRW800H2O service manual has no speed sensor page.
