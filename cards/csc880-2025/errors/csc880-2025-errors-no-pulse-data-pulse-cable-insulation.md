---
id: csc880-2025-errors-no-pulse-data-pulse-cable-insulation
title: No pulse data during use is the pulse cable, squeezed or pinched until the insulation
  breaks
kind: troubleshooting
question: Why does the console of a Spirit CSC880-2025 stair climber show no pulse
  data while the machine is in use?
asked_as:
- my stair climber wont read my heart rate
- no pulse showing on the csc880
- spirit stair climber heart rate not working
- pulse grips dead on my stair climber
keywords:
- pulse data
- heart rate
- hand pulse
- pulse cable
- wiring harness
- insulation
- pinched
- multimeter
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-heartbeat-not-sensed
- spirit-hand-pulse-not-working
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
see_also:
- csc880-2025-errors-error-code-table
- csc900-2024-errors-heartbeat-not-sensed
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, row 10 of the No./Problem/Causes/Solution table,
    printed page 34 (PDF page 36), read from the native text layer and confirmed against
    a 400 dpi render
  extracted_at: '2026-09-10'
---

**Problem:** When in use, the console does not display pulse data.
**Cause:** Pulse cable failure.

> Use a multimeter to measure the wiring harness. Generally, the wiring harness is squeezed or
> pinched, causing the insulation to break.

**One cause and one test.** The manual blames the cable and nothing else - not the grips, not the
board, not dry hands, not the user's grip. No pass figure is printed, and no cable route or pinch
point is named.

**The check is for broken insulation, not for continuity.** A conductor that is still joined but has
lost its insulation will pass an end-to-end continuity check and still be the fault, so measure the
harness rather than only buzzing it out.

**The CSC900 2024 book answers the same symptom with a different test** - a DC voltage reading at
the hand-held heartbeat seat (`csc900-2024-errors-heartbeat-not-sensed`). Same family, same fault,
two measurements; use the one printed in the caller's own book.

**Read the emergency stop row before you cut into this harness.** Row 11 of this same table says
that the handle pulse line and the emergency stop switch line can be **connected to each other's
positions**, and the symptom of that is the machine sitting in stop mode showing `Safe`
(`csc880-2025-errors-safe-in-the-display-emergency-stop-wiring`). A pulse fault and a stop-switch
fault on this machine share a wiring mistake.

**The manual prints no chest strap row.** A caller whose telemetric strap is not reading has nothing
in this table to work from.
