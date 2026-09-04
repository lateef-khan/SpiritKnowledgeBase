---
id: f80-2026-error-code-list
title: Every console message the diagnosis guide lists
kind: spec
question: What error codes can a Sole F80-2026 treadmill show and what does each mean?
asked_as:
- list of error codes for my treadmill
- what do the e codes mean on a sole treadmill
- treadmill error code table
keywords:
- error code list
- e codes
- lube
- console message
- diagnosis guide
- fault
- meaning
- overview
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2026
  applies_to:
  - f80-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2026-lube-message
- f80-2026-e01-over-current
- f80-2026-e02-hall-mistake
- f80-2026-e03-hardware-current-too-large
- f80-2026-e04-phase-loss
- f80-2026-e05-undervoltage
- f80-2026-e06-overvoltage
- f80-2026-e3-incline-adjustment
- f80-2026-e22-led-control-board-communication
- f80-2026-e23-tft-led-communication
- f80-2026-e31-overtemperature
- f80-2026-error-tft-communication-failure
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-f80-2026-owners-manual
  locator: page 33, Service Checklist - Diagnosis Guide
  extracted_at: '2026-09-04'
---

**Read the look-alikes carefully: this manual prints both E3 and E03, and they are different faults.**

| Console shows | Meaning, as printed |
|---|---|
| LUBE | Reminder to check lubrication under walking deck |
| E01 | Over Current Protection. Treadmill over loaded, controller protection is activated. |
| E02 | Hall mistake |
| E03 | The hardware current is too large. |
| E04 | Phase loss |
| E05 | undervoltage |
| E06 | overvoltage |
| E3 | Incline adjustment error |
| E22 | Error in communication between the LED electronic watch and the control board |
| E23 | TFT electronic watch has communication error with LED electronic watch |
| E31 | overtemperature |
| ERROR | TFT electronic watch communication failure |

Twelve messages in all. Each has its own card with the full solution list.

**Two notes on this table.** The zero-padded codes E01 to E06 and the unpadded E3 sit in the same list, so
E03 and E3 are neighbours on the page and mean different things. And the last row's problem column is
printed as "Console ERROR" followed by a stray arrow glyph, which the text extraction rendered as
"ERROR<-"; the message itself is ERROR.

**These codes do not match the older F80 service manuals.** Those manuals define E1 through E7 with
different meanings - for example E2 is over current and E3 is an incline VR fault there. Those are different
machines; do not carry a meaning across.
