---
id: spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel
title: No adjustable resistance is worked through the handlebar controller and its
  RF module, then the console cables, then the gear motor, steel cable and flywheel
kind: troubleshooting
question: What do I check when the resistance will not adjust on a Spirit CRW800 rower?
asked_as:
- crw800 resistance wont change
- rower level button does nothing
- spirit rower stuck on one resistance
- rf module on the rower handle not working
keywords:
- no adjustable resistance
- controller assembly
- rf module
- calibration
- battery cover
- gear motor
- steel cable
- flywheel
- computer cable
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- xrw600-2019-errors-no-adjustable-resistance-8p-wires-then-console-then-flywheel
see_also:
- xrw600-2019-errors-no-adjustable-resistance-8p-wires-then-console-then-flywheel
- crw800-2024-errors-e2-cable-tension-communication-error
- crw800-2024-errors-rf-handheld-board-problem
- sr500-2016-no-adjustable-resistance
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: CRW800 2021 service manual 12-2 The Resistance Level can't adjust troubleshooting,
    PDF p. 65 (printed 64), text.md lines 978-996; CRW800 2016 (CW800-YR001) service
    manual 9-11 No Adjustable Resistance, PDF p. 66, text.md lines 767-786
  extracted_at: '2026-09-11'
---

**This is the CRW800 procedure, for the two books whose handlebar controller talks to the console by radio.** The XRW600's handle is wired, and its version of this page has no RF step (`xrw600-2019-errors-no-adjustable-resistance-8p-wires-then-console-then-flywheel`).

> Please check Controller Assembly (36) and Console Assembly (43) if there's no adjustable resistance separately. If it is the problem of Controller Assembly (36), please refer to step 1. If it is the problem of Console Assembly (43), please refer to step 3.

**Step 1 - the handlebar controller (36).** Follow the steps of the instruction manual or the message on the sticker to proceed the **calibration of the RF module**. If there is still no resistance, remove the one 3.5 x 12L sheet metal screw (112) from the Battery Cover (36~3) and check if the Controller Assembly (36) has power. If not, replace directly. If yes, remove the two screws (112) from the Controller Assembly (36) and check the connection of the Resistance Button W/Cable + Faceplate (36~4) and the RF Module (35). Or take out the four screws (112) from the console, open the cover and check the connections of cables on the Console Bottom Cover (43~2). *It is get easier to find the problem if you have RF Module (35).*

**Step 2.** Release the four screws (112) from the Console (43). Check the PCB board (43~4) and the 500 mm Computer Cable (Upper). Release the Chain Cover (R) (72) and check the Gear Motor (35) and the 500 mm Computer Cable (Lower) (45).

**Step 3 - the drive.** Release the Chain Cover (R) (72) and check the Drive Belt (24) and Flywheel (23). Check the connections with Gear Motor (35), Steel Cable (66) and Flywheel (23). The problems could be:

- **Gear Motor (35)** - check whether there is any noise while working. If yes, get the Steel Cable (66) to the maximum. If not, replace Gear Motor (35) directly.
- **Flywheel (23)** - check if the Steel Cable is broken or the Flywheel gets stuck. Check the troubleshooting step by step.

**Three things this page tells you that the E2 code does not.** The handlebar controller has its own battery, its own RF module and its own calibration (the sticker on the controller carries the routine); a silent gear motor is replaced, a noisy one is driven to full cable travel first; and a broken steel cable or a jammed flywheel shows as no resistance with nothing wrong electrically. **The book uses item number (35) for both the RF Module and the Gear Motor** on this page; it is how the page is printed.

`E2` on the console is the electrical half of this fault and has its own voltage test (`crw800-2024-errors-e2-cable-tension-communication-error`). Sole prints this page for its SR500: `sr500-2016-no-adjustable-resistance`.
