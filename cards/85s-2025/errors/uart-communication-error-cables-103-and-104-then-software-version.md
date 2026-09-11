---
id: 85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version
title: UART Communication Error is the two communication cables, then a software version
  reading V255A255 that wants an update, else both the LCB and the console
kind: troubleshooting
question: What does UART Communication Error mean on a Spirit 85s-2025 recumbent stepper?
asked_as:
- 8.5s says uart communication error
- stepper console lost contact with the lower board
- spirit rehab stepper uart error what to do
- v255a255 software version on the stepper
keywords:
- uart communication error
- communication cable
- cable 103
- cable 104
- v255a255
- software update
- lower control board
- lcb
- console
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: errors
  code: uart-communication-error
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- cu1000ent-2023-errors-0xb2-uart-error-driver-board
- spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode
see_also:
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
- 85s-2025-errors-console-shows-the-fault-and-a-suggested-fix
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 5. Troubleshooting (Electronic), 5-2 UART Communication Error, steps 1-2
    and the Check Procedure flow chart, PDF p. 19; text.md lines 266-278 and the OCR
    supplement for page 19 (lines 883-910)
  extracted_at: '2026-09-11'
---

**The message is the words `UART Communication Error`** - no code number. It is the console and the lower control board (LCB) failing to talk over their serial link. It is not the CU1000ENT bike's `0xB2 UART Error` (`cu1000ent-2023-errors-0xb2-uart-error-driver-board`), which is a driver-board code with no printed remedy.

**Step 1.** Check if **cables #103 and #104** are properly connected (see the Electrical Wiring Diagram section). If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.

**Step 2.** Check if the software version shows **V255A255**. If it does, **update the software** (see the Maintenance Mode section). If not, **replace both the LCB and the console**.

**V255A255 is a placeholder, not a version.** A console that reports its firmware as all 255s has not been able to read a real version from the board it talks to - which is exactly what a broken UART link produces - so the book treats that reading as "the software is missing or corrupt, load it again" rather than "the hardware is dead". The update is done from Maintenance Mode (tap the Wi-Fi icon once and the clock six times) with three files on a USB drive - `CS51009-01.bin`, `CS31003.bin` and `update.json` - and the Update buttons under Firmware and LCB; that procedure is carded under `section: console`.

**A real version number with the cables good means two boards.** The book does not say to try one before the other; it replaces both the LCB and the console together.

Cables #103 and #104 are the two halves of the communication run on the wiring diagram - console to inline connector, inline connector to LCB. Reseat both ends of both before reading the version.
