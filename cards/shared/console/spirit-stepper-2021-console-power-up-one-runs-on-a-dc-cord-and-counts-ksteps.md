---
id: spirit-stepper-2021-console-power-up-one-runs-on-a-dc-cord-and-counts-ksteps
title: One stepper powers up from a DC cord and shows total ksteps, the other from an AC cord and shows total steps
kind: fact
question: What does a Spirit stepper or semi-recumbent stepper console show when it is switched on?
asked_as:
- what are the numbers when my stepper powers up
- what does ksteps mean on my stepper
- where is the software version on the spirit stepper
- does the stepper plug into the wall or a power brick
keywords:
- power on
- self test
- software version
- ver 1.0
- total hours
- ksteps
- steps
- odometer
- dc power cord
- ac power cord
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - cs800-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-console-power-up-self-test
see_also:
- spirit-ce-console-led-console-face
- ct850-2020-c-safe-ports
- spirit-stepper-console-led-data-windows-steps-and-vertical-distance
source:
  ref: spirit-climber-cs800-2021-owners-manual
  locator: CS800-2021 printed p. 17, POWER; the CRS800S-2021 owners manual prints the same paragraph on its printed p. 18.
    CRS800S (2020 ver.) service manual Operation / POWER, PDF p. 12 (printed 12), text.md lines 137-143; CS800 (2020) service manual 4-2-1 POWER, PDF p. 14 (printed 13), lines 227-233
  extracted_at: '2026-09-10'
---

**The paragraph is identical apart from two words, and both of them matter.**

1. **The console powers up on its own** when the power cord is connected.
2. It runs an **internal self-test**; all the lights turn on.
3. When the lights go off, the **Dot Matrix Message Center** shows the **software version**
   (i.e. `VER 1.0`).
4. The **LED Data Display Window** shows the **total hours of use** and a **total step count**.
5. The **odometer stays up for only a few seconds**, then the console goes to the start-up display -
   the Dot Matrix scrolls the program profiles and the start-up message.

| | Cord it names | Step total it names |
|---|---|---|
| **CS800-2021** | "When the **AC power cord** is connected to the Stepper" | total **steps** |
| **CRS800S-2021** | "When the **DC Power cord** is connected to the equipment" | total **ksteps** |

**The CRS800S is the one with an external power adapter**, which is why its own console chapter says
DC. **Do not tell a CRS800S owner to look for a mains cord at the console, or a CS800 owner that
their machine takes a power brick.**

**`ksteps` means thousands of steps and the manual never says so.** It expands the abbreviation
nowhere, gives no rollover behaviour and no maximum, and the CS800 book counting plain **steps**
means the two odometers are not read the same way.

**The CRS800S book also misspells the window "LED Data Diplay Window"** here and three more times on
the next two pages. It is a misprint in that book, not a different part.

**Neither console has a power switch in this instruction.** Neither paragraph mentions one.

**The service manuals swap the two words the owner's manuals split on.** The CS800 (2020) service
manual says *"When the **AC power cord** is connected to the Stepper"* and then *"the total hours of
use and total **ksteps**"*; the CRS800S (2020 ver.) service manual says *"When the **DC Power cord** is
connected to the equipment"* and *"total hours of use and total **steps**"*. So the cord word follows
the machine - AC on the CS800, DC on the CRS800S, in both documents of each - but **ksteps and steps
do not**: each machine's owner's manual prints one and its service manual the other. Treat the step
total's unit as unsettled for both machines rather than a difference between them. The CS800 book
also writes "Message Center" where the owner's manual writes "Dot Matrix Message Center", and both
service manuals spell "LED Data Display Window" correctly.
