---
id: tr150-2021-errors-service-manual-prints-no-controller-led-debugging-table
title: The service manual has no Controller Indicator LED debugging table; its chapter
  6 ends at Driver Board Function
kind: fact
question: What do the LEDs on the lower controller mean on an Xterra tr150-2021 treadmill?
asked_as:
- tr150 controller led meaning
- lights on the tr150 motor control board
- xterra tr150 led debugging
keywords:
- controller led
- indicator led
- led debugging
- absence
- driver board
- motor control board
- two red leds
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: errors
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with: []
see_also:
- trx1400-2023-errors-controller-led-debugging-power-and-info-leds
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM Table of Contents, PDF p. 2; text.md lines 6-41 (chapter 6 lists
    6.1-6.5 and no LED section); 6.5 Driver Board function, PDF p. 28; text.md lines
    357-388; the text layer and the 22 OCR supplements searched for 'LED', 'indicator'
    and 'debug'. TR150 MCB wiring photo (authority 2), the labels SPD / 'If you have
    speed sensor, then it plugs here', 'M+ Red lead from drive motor', 'M- Black lead
    from drive motor'; text.md lines 1-40
  extracted_at: '2026-09-11'
---

The TR150 service manual (Dyaco GT65-NT014) is the one Dyaco book in this wave with **no *Controller Indicator LED debugging* table and no *Driver Board LED Indicator Locations* page**. Its chapter 6 runs 6.1 Display Board Wire Connections to 6.5 Driver Board Function, then chapter 7 is the safety pages. The word LED does not appear in the book's text layer or in any of its 22 OCR supplements outside the safety pages.

What exists instead is the annotated photograph of the TR150 / T500 motor control board, which shows **two red LEDs at the bottom edge near the AC terminals** but gives no meaning for either. Nothing in the knowledge base says what those two LEDs indicate on this board.

The TR260, TRX1400, TRX2500, TRX3500/TRX4500 and TRX5500 service manuals each print an LED table; see `tr260-2023-errors-controller-led-debugging-speed-led`, `trx1400-2023-errors-controller-led-debugging-power-and-info-leds`, `trx2500-2024-errors-controller-led-debugging-three-leds`, `xterra-trx-errors-controller-led-debugging-info-and-power-220-v`, `trx5500-2024-errors-controller-led-debugging-power-led-only`.
