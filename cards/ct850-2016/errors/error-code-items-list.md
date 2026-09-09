---
id: ct850-2016-error-code-items-list
title: The two error messages the console can show
kind: spec
question: What error messages can a Spirit CT850-2016 treadmill display and what does
  each one mean?
asked_as:
- list of error messages for my spirit treadmill
- what errors can the ct850 show
- spirit treadmill error message list
keywords:
- error message
- error code
- low speed
- incline err
- list
- index
- rpm signal
- vr voltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-low-speed-error-message
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-during-incline-action
- ct850-2020-inverter-error-code-list
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Error code items table, page 29 (printed 28)
  extracted_at: '2026-09-08'
---

This manual names only **two** error messages. It has no numbered error-code table at all.

| Error Message | Explain |
|---|---|
| LOW SPEED | Display board CPU did not receive the RPM signal. |
| INCLINE ERR | The console board is not detecting the VR voltage value, or the voltage value has exceeded the range. |

The only tool the manual asks for to work through these is a **multi-meter**.

Two warnings about this table.

- The manual prints the low speed message under three different names in three places: `LOW SPEED`
  here, `LS1/LOW SPEED` in the section 8.1 flow charts, and `SPEED ERROR` in the summary on page 58.
- The manual defines `INCLINE ERR` **twice, with two different meanings**. The definition above is
  the first; the second, on page 43, says the display board CPU cannot read the VR value during
  incline action. Both are reproduced, one on each of the cards linked below.

The later CT850 2020 manual replaces this two-message list with a twenty-three row inverter code
table: see `ct850-2020-inverter-error-code-list`.
