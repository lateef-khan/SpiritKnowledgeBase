---
id: spirit-ent-console-wifi-setup
title: Putting the console on WiFi from the Maintenance menu, and why Ethernet blocks mirroring
kind: procedure
question: How do I connect a Spirit CT800ENT-2022 or CT850ENT-2022 treadmill console to
  WiFi?
asked_as:
- how do i put the treadmill on wifi
- where are the network settings on the treadmill screen
- the treadmill apps say no internet
- should i use wifi or ethernet on the treadmill
keywords:
- wifi
- wireless
- network
- ethernet
- password
- maintenance menu
- home button ten times
- internet
- setup
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
authority: 2
not_to_be_confused_with:
- ct900ent-wifi-ethernet-setup
- cu900ent-wifi-ethernet-setup
- xt485ent-2023-console-wifi-first-time-setup
see_also:
- spirit-ent-console-enter-engineering-mode
- spirit-ent-console-software-update
- spirit-ent-console-screen-mirroring-limits
- ct800ent-2022-console-internet-apps
source:
  ref: spirit-ent-console-internet-connection-tip
  locator: '"Connecting to the Internet", one page support note, revision 07.01.2024,
    p. 1'
  extracted_at: '2026-09-09'
---

**To use the internet feature the machine must first be set up with WiFi.**

1. **Press the HOME button 10 times** to enter the **Maintenance** menu -
   `spirit-ent-console-enter-engineering-mode`.
2. **Choose WiFi** to continue setting up the connection.
3. **Choose the proper WiFi signal and enter the password if applicable.**

The note's screenshot of that menu shows **WiFi Setup**, **Ethernet Setup**, **BT Setup**, **Update
App(USB)** and **Update OS** as separate buttons. The first and last entries in the screenshot are
too damaged in the converted text to name, so the list above is not claimed to be complete; the same
console family's full Maintenance menu is at `ce800ent-maintenance-menu`.

**Use WiFi, not Ethernet, if anyone will screen mirror.** The note's own footnote says *"WiFi
connection is recommended as Ethernet will prohibit use of the screen mirroring function"*, and that
the machine and the user's phone must be on the **same** WiFi signal for mirroring to work. See
`spirit-ent-console-screen-mirroring-limits`.

**Once connected, check for software updates**: `spirit-ent-console-software-update`.

**This is a support note, not a manual.** It names no model, and neither the CT800ENT-2022 nor the
CT850ENT-2022 owner's manual prints any network setup at all - that gap is why this card exists. It
is scoped to those two because the note's screenshots show their Home Screen, with the
Entertainment, Program and Internet tabs and an incline readout. The CT900ENT, XT485ENT-2023 and
XT685ENT-2023 have different screens and their own network cards.
