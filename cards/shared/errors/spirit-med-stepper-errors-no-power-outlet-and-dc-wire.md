---
id: spirit-med-stepper-errors-no-power-outlet-and-dc-wire
title: No power on a stepper fed from a 90 to 240 VAC adapter, and three checks end
  at the connectors behind the console
kind: troubleshooting
question: What do I check when a Spirit recumbent stepper has no power at all?
asked_as:
- my stepper wont turn on
- no power to my spirit stepper
- stepper console is dead
- nothing happens when i plug the stepper in
keywords:
- no power
- dead console
- ac adapter
- dc power wire
- line cord
- connectors
- 90-240vac
- stepper
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: no-power
authority: 3
not_to_be_confused_with:
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
- csc900-2024-errors-console-does-not-light-up-after-power-on
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
see_also:
- spirit-med-stepper-errors-programs-do-not-start-keypad-test
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: Troubleshooting, "No power", printed page 40 (PDF page 42) of the 7.0S
    2025 manual; the same text on printed page 42 (PDF page 44) of the 7.5S 2025 manual
    and printed page 59 (PDF page 59) of the MS300 2021 manual. Read from the native
    text layer of all three and confirmed against a 300 dpi render of the 7.0S page;
    7.5S (RS9600-SS021) service manual 5.2.3 Troubleshooting and Problem Solving,
    "No power", PDF p. 13-14, text.md lines 132-146
  extracted_at: '2026-09-10'
---

Three checks, in the manual's order:

1. **Make sure the A.C. outlet has power (90~240VAC)** and the line cord is plugged in securely to
   the AC adapter.
2. **Check the connection of the DC power wire** from the adapter where it enters the machine.
3. **Make sure all connectors in back of the console are securely seated** in place.

**The machine takes 90 to 240 VAC at the wall and runs on DC from an external adapter.** So there are
two cables and two ends to each: mains into the adapter, DC out of the adapter into the frame. Both
are named, and the manual does not say which is more often at fault.

**No voltage is given for the DC side.** The specification page names the supply - a Sinpro
HPU32A-105 30 watt unit, input 100-240 V, **output 12 VDC 2.74 A** - but the troubleshooting page
asks only whether the wire is connected, not what should be on it.

**The 90~240VAC figure is a range, not a choice.** These are single-voltage-range machines; there is
no 110/220 switch to set, and no row in this table about setting one.

**The other Spirit climbers answer this symptom with voltages, and theirs are different.** The
CSC880 2025 stair climber steps 24 V down to 12 V and measures at three points
(`csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks`); the CSC900 2024 measures 24 V at
two (`csc900-2024-errors-console-does-not-light-up-after-power-on`). Neither figure belongs on a
stepper.

If the console lights but nothing starts, that is the keypad row:
`spirit-med-stepper-errors-programs-do-not-start-keypad-test`.

## The 7.5S service manual prints the same row with the voltage the owner's manuals leave out

Four steps instead of three, and the DC side gets its figure:

> i. Make sure the A.C. outlet has power (90~240VAC) and the line cord is plugged in securely to the AC adapter.
> ii. Make sure there is **12V DC at the DC plug of the adaptor** and plug into the DC jack of the stepper. Replace the adaptor if there is no 12V at the DC plug of the adaptor. Go to next step if there is 12V but still no power to the console.
> iii. Open the left shroud and check the connector of the DC power cable. Go to next step if there is still no power to the console.
> iv. Measure between **pin 10 and pin 11 of the 14 pin cable** that connects to the console for 12V DC. **Replace the console if 12V DC is measured. Replace the cable if there is no 12V DC.**

**So the chain is 12 V at the adapter plug, then 12 V at pins 10 and 11 of the console's 14-pin cable**, and the last measurement decides between the cable and the console. The wiring diagram in the same book rates the supply as a switching power supply, 90 to 260 VAC in, 12 VDC out at **1.6 A** - which does not agree with the 2.74 A Sinpro unit the owner's-manual specification page names (above). Both figures are printed; the 12 V is what the troubleshooting measures, and the current rating is a specs matter. This is the 7.5S book; the figures are printed for that machine, and the owner's manuals of the 7.0S, 7.5S and MS300 share only the three unmeasured steps above.

**The 8.5S is a different supply altogether** - mains into an internal power supply module, 24 V to the lower board, 12 V to the console - with its own procedure (`85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc`).
