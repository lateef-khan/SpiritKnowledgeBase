---
id: lcr-2026-sleep-mode-settings
title: The three sleep mode choices
kind: fact
question: How does sleep mode work on a Sole LCR-2026?
asked_as:
- my sole bike screen goes dark
- how do i stop the console going to sleep
- what is retail mode on the bike console
keywords:
- sleep mode
- energy saving
- retail mode
- demo video
- 15 minutes
- 3 minutes
- settings
- screen off
facets:
  brand:
  - sole
  product_line: bike
  model: lcr-2026
  applies_to:
  - lcr-2026
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- lcr-2026-power-up
- lcr-2026-home-screen
- lcr-2026-console-layout
source:
  ref: sole-bike-lcr-2026-owners-manual
  locator: page 12, Power Up - Sleep Mode
  extracted_at: '2026-09-04'
---

The console ships **in "Sleep mode"**, and the setting has three choices:

| Setting | What it does |
|---|---|
| **ON** | The unit goes into an **energy-saving state after 15 minutes of inactivity**. |
| **OFF** | The console **stays lit while the power is on**. |
| **RETAIL** | The console **runs the demo video after 3 minutes of inactivity**. |

**On TFT displays, click "Sleep Mode" under Settings to switch among the three.**

The manual does not say how to wake the console from the energy-saving state.

The repo's wildcard card `sole-sleep-mode-touchscreen` describes a different behaviour - sleep after **15 to 30 minutes**, waking with **Start**, and a **safety key** in place. That card reaches every model through its wildcard scope, but it was written from treadmill sources; this bike has no safety key. The figures above are what this machine's own manual prints.
