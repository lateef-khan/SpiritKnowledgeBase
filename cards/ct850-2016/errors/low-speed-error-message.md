---
id: ct850-2016-low-speed-error-message
title: What the LOW SPEED message means
kind: troubleshooting
question: What does LOW SPEED mean on a Spirit CT850-2016 treadmill?
asked_as:
- what does low speed mean on my spirit treadmill
- treadmill display says low speed
- ls1 low speed error
keywords:
- low speed
- ls1
- speed error
- rpm sensor
- rpm signal
- display board
- motor does not turn
- drive board
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: low-speed
  model_number:
  - '850845'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-low-speed-solution-flow-chart
- ct850-2016-low-speed-check-rpm-sensor
- ct850-2016-low-speed-troubleshooting-form
- ct850-2016-low-speed-after-eight-seconds
- ct850-2016-error-code-items-list
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Section 8.1 Error Message: LOW SPEED, pages 29-31 (printed 28-30); pages
    30 and 31 are flattened images and were read from raw/page-30.png and raw/page-31.png.
    The summary on page 58 (printed 57) prints a third name for the same message'
  extracted_at: '2026-09-08'
---

**This manual prints three different names for this one message, and never says they are the same
message.** Anyone searching for only one of them will miss the other two.

| Where | The string the manual prints |
|---|---|
| Error code items table, page 29 | `LOW SPEED` |
| Section 8.1 definition and flow charts, pages 30-35 | `LS1/LOW SPEED` |
| Summary page 58 | `SPEED ERROR` |

Definition, from section 8.1:

> Display board CPU did not receive the RPM signal.

Cause, from the following page:

> The motor doesn't turn: LS1/LOW SPEED appears.
> The drive board did not sent voltage to the motor, so the motor didn't operate. And the display
> board didn't receiver the RPM sensor signal.

The page 58 summary states the timing the other two do not:

> If under the start, when successive 8 seconds speed signal, MW display "SPEED ERROR".

The signal path the manual draws is: RPM sensor -> driver board -> display board over the 12-pin
cable, with the driver board sending motor voltage out on a 2-pin connector.

Work the fault with `ct850-2016-low-speed-solution-flow-chart`. The matrix row that lists eight
parts to change is `ct850-2016-low-speed-after-eight-seconds`.
