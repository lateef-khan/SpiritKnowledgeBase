---
id: xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller
title: 'E3 on the JKEXER console: poor communication between the upper and lower controllers
  over their connection cable'
kind: troubleshooting
question: What does E3 mean on an Xterra tr75h-2025 or tr95h-2024 treadmill, and what
  should I check?
asked_as:
- e3 on my tr95h
- tr75h e3 cable
- xterra e3 communication error
keywords:
- e3
- communication
- upper controller
- lower controller
- connection cable
- control box
- console
- driver board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e3-incline-vr-out-of-range
- xterra-tr-errors-e3-incline-error-owner-checks
- xterra-treadmill-errors-e5-console-controller-communication-poor
- xterra-ws-errors-e01-poor-communication
see_also:
- xterra-tr-errors-jkexer-error-messages-e1-e3-e6-and-dashes
- xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
- xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: TR95H SM 11. Explanation and troubleshooting of error messages, PDF pp.
    16-17; text.md lines 209-258; TR75H SM 12. Explanation and troubleshooting of
    error messages, PDF pp. 16-17; text.md lines 346-421; TR95H OM Troubleshooting,
    PDF p. 53 (printed 52); text.md lines 1920-1939; TR75H OM Troubleshooting, PDF
    p. 49 (printed 48); text.md lines 1845-1864
  extracted_at: '2026-09-11'
---

**On the TR75H and TR95H, E3 is a communication fault.** On the Dyaco-built Xterra treadmills E3 is the incline VR fault (`xterra-treadmill-errors-e3-incline-vr-out-of-range`) and communication is E5.

*Owner's manual:* E3 (Error 3) shows when the cable from the computer to the control box is not well connected or is damaged. If the cable works well, check whether the computer or the control box is damaged.

*Service manual:* cause - poor communication between upper and lower controllers. Troubleshooting: (a) check whether the upper and lower controller connection cable is connected, or damaged; (b) console or driver board failure - replace.

The cable in question is the 7-pin *upper and lower controller connection cable* at the driver board and the 6-pin socket at the display board (the books list both an AC-system and a DC-system socket); those callouts are specs facts.
