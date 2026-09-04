---
id: st90-2023-does-not-start-when-start-pressed
title: Nothing happens when start is pressed
kind: troubleshooting
question: Why does the belt not move when I press start on a Sole ST90-2023 treadmill?
asked_as:
- i press start and nothing happens on my treadmill
- st90 will not start the belt
- treadmill start button does nothing
keywords:
- will not start
- start button
- motor wire
- motor broken
- controller shut down
- power cycle
- ac switch
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2023
  applies_to:
  - st90-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- st90-2023-stops-immediately-after-start
- st90-2023-err-after-pressing-start
see_also:
- st90-2023-stops-immediately-after-start
- st90-2023-drive-motor-replacement
- st90-parts-and-wiring
source:
  ref: sole-tm-st90-2023-service-manual
  locator: Troubleshooting procedure matrix, pages 17-18, and section 8.3, pages 28-30
  extracted_at: '2026-09-04'
---

**This manual prints its troubleshooting matrix twice**, once on pages 17-18 and again as section 8.3 on pages 28-30, and the two copies do not always agree. Where they differ this card gives both.

| Copy | Reasons | Solve |
|---|---|---|
| Pages 17-18 | 1 Motor wire isn't connected into right position. 2 Motor is broken. 3 Treadmill controller shut down and **TFT** would be ON. | Check and plug in again; replace the motor or check the wire and connector; turn off the AC switch and turn the power on again. |
| Section 8.3 | 1 Motor **M+ or M-** wire isn't connected into right position. 2 Motor is broken. 3 Treadmill controller shut down and **LED** would be ON. | Same three. |

**Section 8.3's wording does not fit this machine.** M+ and M- are the two motor terminals of a DC treadmill. This machine's drive motor lands on the inverter's three-phase AC MOTOR terminal, U red, V white and W black, and its console is a TFT screen with no controller LED. Read the pages 17-18 copy.

Reason 3 is the common one: the screen is alive but the inverter has latched off, and a full power cycle at the AC switch clears it.
