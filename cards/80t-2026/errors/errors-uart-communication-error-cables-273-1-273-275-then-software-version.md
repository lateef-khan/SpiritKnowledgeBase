---
id: 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
title: UART Communication Error is the three console cables, then a software version
  reading V255A255 that wants an update, else both the LCB and the console
kind: troubleshooting
question: What does UART Communication Error mean on a Spirit 80t-2026 treadmill?
asked_as:
- 8.0t says uart communication error
- treadmill touchscreen lost contact with the lower board
- uart error on the medical treadmill
- v255a255 software version treadmill
keywords:
- uart communication error
- communication cable
- cable 273
- cable 275
- v255a255
- software update
- lower control board
- lcb
- console
- medical treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: uart-communication-error
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds
- cu1000ent-2023-errors-0xb2-uart-error-driver-board
see_also:
- 80t-2026-errors-inverter-error-code-table-48-rows
- 85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version
- 80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, Communication / Message row, PDF p. 22, text.md lines
    356-357; 5. Troubleshooting, UART Communication Error, steps 1-2 and the Check
    Procedure flow chart, PDF p. 32, text.md lines 452-466 and the OCR supplement
    for page 32
  extracted_at: '2026-09-11'
---

**The message is the words `UART Communication Error`** - no code. It is the console and the lower control board (LCB) failing to talk over their serial link. The error table lists it as a *Communication - Message* row with one line, *Check wiring between controller and console*; the troubleshooting chapter prints the procedure. It is not the drive-to-controller link, which fails as inverter code `conF` (`80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds`).

**Step 1.** Check if **cables #273-1, #273 and #275** are properly connected (see the Electrical Wiring Diagram section). If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.

**Step 2.** Check if the software version shows **V255A255**. If it does, **update the software** (see the Maintenance Mode section). If not, **replace both the LCB and the console** (#269, #250 on the flow chart).

**V255A255 is a placeholder, not a version.** A console that reports all 255s has not read a real version from the board it talks to - which is what a broken UART link produces - so the book treats that reading as "load the software again" rather than "the hardware is dead". The update runs from Maintenance Mode (tap the Wi-Fi icon once and the clock six times) with three files on a USB drive - `CS56018.bin`, `CS31003.bin` and `update.json` - and the Update buttons under Firmware and LCB; that procedure is carded under `section: console`. **Note the firmware file is `CS56018.bin` on this treadmill, not the `CS51009-01.bin` the 8-series bikes and the 8.5S stepper use.**

**A real version number with the cables good means two boards.** The book does not say to try one before the other; it replaces both the LCB and the console together.

The three cables are the console run on the wiring diagram - #273-1 and #273 are the two halves through the inline connector, #275 the short lead at the board. Reseat both ends of all three before reading the version. The 8.5S stepper prints the same two steps with its own cable numbers (`85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version`).

