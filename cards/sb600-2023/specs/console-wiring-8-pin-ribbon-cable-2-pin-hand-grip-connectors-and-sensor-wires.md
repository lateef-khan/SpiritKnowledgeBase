---
id: sb600-2023-specs-console-wiring-8-pin-ribbon-cable-2-pin-hand-grip-connectors-and-sensor-wires
title: 'Console wiring: an 8-pin ribbon cable and 2-pin hand-grip connectors with
  press-to-release clips, two sensor wires up the support tube and a 600 mm DC wire'
kind: spec
question: How is the console wired on an Xterra sb600-2023 recumbent bike, and which
  wires and connectors does the service manual name?
asked_as:
- sb600 console cable connector
- how do i unplug the sb600 console ribbon cable
- sb600 sensor wire routing
- which wires go to the console on the sb600
keywords:
- ribbon cable
- 8-pin
- 2-pin
- hand grip connector
- clip
- sensor wire
- speed sensor
- dc wire
- computer cable
- no wiring diagram
facets:
  brand:
  - xterra
  product_line: bike
  model: sb600-2023
  applies_to:
  - sb600-2023
  section: specs
  code: '*'
  model_number:
  - '160113'
authority: 3
not_to_be_confused_with: []
see_also:
- sb600-2023-specs-main-parts-indication-thirty-callouts
- xterra-specs-external-power-adapter-with-no-rating-printed
- xterra-specs-resistance-set-from-the-console-by-a-gear-motor-on-a-magnetic-brake
source:
  ref: xterra-bike-sb600-2023-service-manual
  locator: '''Replacing the Console'' note, PDF p. 14, text.md lines 285-298 (OCR
    supplement lines 713-728); troubleshooting ''Screen remains blank'', ''No speed
    reading'', ''No heart rate reading'', PDF pp. 6-8 lines 104-157; parts list A1,
    A3, A4, A5, A6, A33, A34, A36, A45, A46, J1-1, J2-1, J4, S, PDF pp. 12-13 lines
    205-279. Owner''s manual (xterra-bike-sb600-2023-owners-manual) assembly step
    3 PDF p. 12 (printed 11) lines 297-298, step 4 p. 13 line 327, step 7 p. 15 (printed
    14) lines 364-373. The service manual prints no wiring diagram, block diagram
    or PCB drawing: its table of contents (PDF p. 2) runs General Information, Tools,
    Troubleshooting, Exploded View, Parts List, Parts Replacing Guide'
  extracted_at: '2026-09-11'
---

**Two connectors inside the console housing, and a clip on each.** "For both the **8-pin ribbon cable** and
**2-pin hand grip connectors**, always press the clip in the middle before disconnecting. Forcing the connector
without releasing the clip may cause wire damage." Once the clip pops up, pull the opposite end of the connector to
unplug it; four Phillips screws hold the console display.

**What runs where**, from the parts list and the assembly steps:

| Wire | Route |
|---|---|
| Sensor wires **A33** and **A34** (450 mm) | from the console's own pigtails down the Central Support Tube (D); at assembly they join **A4** (sensor wire 1100 mm) and **A36** inside the main frame, and the troubleshooting page calls the pair 'the computer cables (A33/A36)' |
| Sensor wire **A6** (700 mm) with the **magnet A45** | the speed sensor under the main chain covers; a test magnet across A6 proves which of the two is at fault |
| **J1-1** (550 mm) and **J2-1** | hand-pulse sensor wires from the left and right side handlebars (J1, J2) to the seat-tube wire **A3** (400 mm); the console end is the 2-pin hand-grip connector |
| **A46 DC wire 600 mm** | from the adaptor port at the rear of the main frame to the electronics; it has a retaining bracket under the chain cover that pulls out along a slot |
| Motor **A1** | the resistance gear motor, on a brace with a spring, under the chain covers |

The troubleshooting pages use those names: a blank screen means "verify that the console cable and computer cable are
securely connected", then measure the power output; no speed means inspect "the computer cables (A33/A36) and speed
sensor (A6)" and replace the sensor or the magnet; no heart rate means check the hand-grip connectors and test the
grip wiring for continuity (the errors section holds the three procedures).

**The service manual prints no wiring diagram, block diagram or board drawing** - it is a JKEXER-style book of
photographs and replacement steps - and no connector pin-out beyond the "8-pin" and "2-pin" counts. The Bluetooth radio and
FTMS are on the FCC card and the console section.

