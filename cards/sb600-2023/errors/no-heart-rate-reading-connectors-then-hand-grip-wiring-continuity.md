---
id: sb600-2023-errors-no-heart-rate-reading-connectors-then-hand-grip-wiring-continuity
title: 'No heart rate reading from the hand sensors: the connectors, then the continuity
  of the hand-grip wiring'
kind: troubleshooting
question: Why does the screen show no heart rate while holding the hand sensors on
  an Xterra sb600-2023 recumbent bike?
asked_as:
- sb600 hand pulse not working
- xterra sb600 heart rate stays at zero
- recumbent bike grip sensors no reading
- sb600 hand grip wiring continuity
keywords:
- no heart rate
- hand pulse
- hand rate sensor
- connectors
- continuity
- multimeter
- hand grip wiring
- 2-pin
- recumbent
facets:
  brand:
  - xterra
  product_line: bike
  model: sb600-2023
  applies_to:
  - sb600-2023
  section: errors
  code: '*'
  model_number:
  - '160113'
authority: 3
not_to_be_confused_with: []
see_also:
- sb600-2023-errors-er-on-the-recovery-screen-heart-rate-undetected
- sb600-2023-errors-screen-remains-blank-console-cable-then-multimeter
- xterra-errors-heart-rate-not-displaying-pulse-wire-hand-pulse-grip-or-monitor
source:
  ref: xterra-bike-sb600-2023-service-manual
  locator: 'SB600 SM V1.0 Troubleshooting, NO HEART RATE READING APPEARS ON THE SCREEN,
    PDF p. 8; text.md lines 138-157; the connector note: Replacing the Console, PDF
    p. 14; lines 280-299'
  extracted_at: '2026-09-11'
---

*NO HEART RATE READING APPEARS ON THE SCREEN - Condition:* the screen displays normally, but the heart rate
remains at 0 or is not shown while holding the hand rate sensor.

1. First, check whether **all cable connectors between the console and the hand heart rate sensor** are
   properly connected (see images).
2. If all connectors are properly connected, **use a multimeter to test the continuity of the hand grip
   wiring.**

The grip wiring is the 2-pin hand-grip connector at the console - the book's console-replacement page warns
to press the clip in the middle of both the 8-pin ribbon cable and the 2-pin hand grip connector before
pulling, because forcing them can damage the wire. The grips are items J4 `HANDLE PULSE SENSOR` (2) on the
side handlebars, with sensor wires J1-1 and J2-1. An `ER` on the Recovery screen is the console failing to
hold a pulse for sixty seconds, not this fault
(`sb600-2023-errors-er-on-the-recovery-screen-heart-rate-undetected`).


The service manual closes its troubleshooting chapter with: *if the troubleshooting steps outlined above do not resolve the issue you are encountering, please contact the dealer for further assistance and resolution.* It prints no error codes; its four pages are symptom-based.

