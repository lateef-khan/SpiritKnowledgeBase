---
id: spirit-med-bike-errors-eeprom-err-start-stop-fan-three-seconds-then-console
title: 'EEPROM ERR on the generator bike: hold STOP three seconds, then hold Start,
  Stop and FAN together for three seconds to clear it, else a new console'
kind: troubleshooting
question: What does EEPROM ERR mean on a Spirit Medical 4.0R or 4.0U bike, and how
  is it cleared?
asked_as:
- 4.0r shows eeprom err
- eeprom error on my spirit medical bike
- how to reset eeprom err on the 4.0u
- bike screens all went off eeprom
keywords:
- eeprom err
- eeprom failure
- reset console
- start stop fan
- hold stop 3 seconds
- replace console
- medical bike
- self-powered
- generator bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40u-2025
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- spirit-med-bike-errors-eeprom-error-replace-the-console-only-message
- spirit-bike-errors-eeprom-err-replace-upper-controller
- spirit-xb-2023-errors-eeprom-err-replace-display-board
- cu900ent-eeprom-err
see_also:
- 40t-2026-errors-eeprom-err-hold-stop-then-start-stop-fan
- spirit-med-bike-errors-leds-not-bright-check-power-to-console-then-lower-controller
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: '4.0R (FR800-SB022-03) service manual 8-1 Error code items and Error Message:
    EEPROM ERR, PDF p. 28; text.md lines 305-330. 4.0U (FU800-SB022-03) service manual
    8-1 Error code items and Error Message: EEPROM ERR, PDF p. 28; text.md lines 337-360
    - the same page word for word'
  extracted_at: '2026-09-11'
---

**This is `EEPROM ERR`, the only error message the FR800 and FU800 service manuals define, and the two books print the page word for word.** It is not the 7.0R/7.0U `EEPROM error`, which has no key sequence and goes straight to a new console (`spirit-med-bike-errors-eeprom-error-replace-the-console-only-message`).

| Error Message | Explain |
|---|---|
| EEPROM ERR | EEPROM failure |

**When Error occurs, hold STOP Key for 3 seconds, Reset Console.**

*Definition:* All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show "EEPROM ERR".

*Troubleshooting:* **Press Start, Stop and FAN keys hold to clear EEPROM for 3 seconds at the same time**; if you still cannot rule out EEPROM anomalies, please replace the console directly.

**Two resets before the part.** The STOP hold is the console's ordinary full reset (the operation chapter says three seconds on STOP resets the console); the three-key hold is the EEPROM clear. Only after both is the console replaced - the book names no board inside it, and the only tool on the page is a multi-meter, which the procedure never uses.

**These are self-powered bikes.** The console only lives while someone pedals, so "hold for three seconds" means three seconds of holding the keys while the pedals keep the generator turning.

The 4.0T treadmill of the same year prints the identical procedure - STOP, then Start, Stop and FAN - (`40t-2026-errors-eeprom-err-hold-stop-then-start-stop-fan`). The older Spirit bikes that print this message give no key sequence at all: replace the upper controller (`spirit-bike-errors-eeprom-err-replace-upper-controller`) or the display board (`spirit-xb-2023-errors-eeprom-err-replace-display-board`).

The 4.0R and 4.0U 2025 owner's manuals print no error message and no troubleshooting page; this page exists only in the service manuals.

