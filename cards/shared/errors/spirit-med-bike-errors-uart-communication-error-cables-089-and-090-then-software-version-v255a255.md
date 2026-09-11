---
id: spirit-med-bike-errors-uart-communication-error-cables-089-and-090-then-software-version-v255a255
title: UART Communication Error on the touchscreen bike is the two communication cables,
  then a software version reading V255A255 that wants an update, else both the LCB
  and the console
kind: troubleshooting
question: What does UART Communication Error mean on a Spirit Medical 8.0U or 8.5R
  bike?
asked_as:
- 8.0u says uart communication error
- rehab bike console lost contact with the lower board
- spirit medical bike uart error what to do
- v255a255 software version on the 8.5r
keywords:
- uart communication error
- communication cable
- cable 089
- cable 090
- v255a255
- software update
- lower control board
- lcb
- console
- touchscreen bike
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: errors
  code: uart-communication-error
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-errors-0xb2-uart-error-driver-board
- 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
see_also:
- 85ue-2025-errors-uart-communication-error-cables-then-software-version-v255a255
- 85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version
- spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: 8.0U (MU2000-SB036-01) service manual 5.2 UART Communication Error, steps
    1-2 and the Check Procedure flow chart, PDF p. 25; text.md lines 406-420 and the
    OCR supplement for page 25. 8.5R (MR2000-SB036-01) service manual 5.2, PDF p.
    24; text.md lines 302-311 and the OCR supplement for page 24 - word for word
  extracted_at: '2026-09-11'
---

**The message is the words `UART Communication Error`** - no code. It is the console and the lower control board (LCB) failing to talk over their serial link. It is not the CU1000ENT bike's `0xB2 UART Error` (`cu1000ent-2023-errors-0xb2-uart-error-driver-board`), which is a driver-board code with no printed remedy.

**Step 1.** Check if **cables #089 and #090** are properly connected (see the Electrical Wiring Diagram section). If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.

**Step 2.** Check if the software version shows **V255A255**. If it does, **update the software** (see the Maintenance Mode section). If not, **replace both the LCB and the console** (#091, #070).

**V255A255 is a placeholder, not a version.** A console that reports its firmware as all 255s has not been able to read a real version from the board it talks to - which is what a broken UART link produces - so the book treats that reading as "load the software again" rather than "the hardware is dead". The update is done from Maintenance Mode (tap the Wi-Fi icon once and the clock six times) with three files on a USB drive - `CS51009-01.bin`, `CS31003.bin` and `update.json` - and the Update buttons under Firmware and LCB; that procedure is carded under `section: console`.

**A real version number with the cables good means two boards.** The book does not say to try one before the other; it replaces both the LCB and the console together.

Cables #089 and #090 are the two halves of the communication run on the wiring diagram - console to inline connector, inline connector to LCB. Reseat both ends of both before reading the version. The 8.0U and 8.5R service manuals print the page identically; the 8.5UE prints the same two steps without cable numbers (`85ue-2025-errors-uart-communication-error-cables-then-software-version-v255a255`) and the 8.5S stepper with cables #103 and #104 (`85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version`).

