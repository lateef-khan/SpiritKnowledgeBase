---
id: ct850-2016-incline-err-vr-out-of-range
title: INCLINE ERR raised because the incline VR voltage is out of range
kind: troubleshooting
question: What does INCLINE ERR mean at power on on a Spirit CT850-2016 treadmill?
asked_as:
- incline err on my spirit treadmill at startup
- what is incline err
- treadmill incline error when i turn it on
keywords:
- incline err
- vr voltage
- potentiometer
- out of range
- display board
- 12 pin cable
- incline board
- power on
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-during-incline-action
see_also:
- ct850-2016-incline-err-during-incline-action
- ct850-2016-incline-err-test-procedure
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2016-error-code-items-list
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Error Message: INCLINE ERR, pages 36-38 (printed 35-37). Page 36 is a
    flattened image and was read from raw/page-36.png'
  extracted_at: '2026-09-08'
---

**This manual defines `INCLINE ERR` twice, with two different meanings, and never says so.** This
card holds the first definition; `ct850-2016-incline-err-during-incline-action` holds the second.
Read both before condemning a part.

This one is the reading being out of range, and it appears **at power on**:

> The console board is not detecting the VR voltage value, or the voltage value has exceeded the
> range. "ERR" appears on the display.

Cause, from the facing page:

> Incline VR value exceeds the range. INCLINE Err appears on the display. Incline motor isn't
> operation up or down, making the VR value exceed the range. After turning on the unit, the display
> board detects that the incline VR voltage exceeds the range, so INCLINE Err appears.

| Part | Troubleshooting |
|---|---|
| Incline VR | 1. Reconnect VR wires. 2. Inspect whether the incline wires are broken or disconnected. |
| Display board | 1. Inspect the incline wire and 12-pin cable connections. 2. Test whether the VR voltage varies at the incline wire terminal. |
| 12-pin cable | 1. Inspect the wire connections. 2. Inspect whether wires are broken or crimped. 3. Replace the wires and test again. |
| Incline board | Inspect the display board 12-pin connections. |

The signal path drawn on the page: the incline motor's `INCLINE VR SET` sends incline VR voltage to
the driver board, which carries it to the display board on the 12-pin cable. The driver board has an
`INCLINE DOWN LED` and an `INCLINE UP LED`.

The CT850 2020 manual gives this same definition a code of its own, `E3`: see
`ct850-2020-e3-incline-motor-cannot-work`.
