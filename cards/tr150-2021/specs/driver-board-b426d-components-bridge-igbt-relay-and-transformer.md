---
id: tr150-2021-specs-driver-board-b426d-components-bridge-igbt-relay-and-transformer
title: 'The lower controller components: bridge, IGBT, X safety capacitor, a 1000
  µF 200 V filter capacitor, varistor, relay and transformer, with the AC input labelled
  for 220 V on a 110 V board'
kind: spec
question: What are the components on the driver board of an Xterra tr150-2021 treadmill
  and where are they?
asked_as:
- tr150 controller board components
- where is the relay on the tr150 lower board
- tr150 filter capacitor rating
- what is the x capacitor on the treadmill controller
keywords:
- driver board
- lower controller
- components
- bridge
- igbt
- x capacitor
- filter capacitor
- varistor
- relay
- transformer
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with: []
see_also:
- tr150-2021-specs-driver-board-b426d-wire-connections
- trx1400-2023-specs-driver-board-b307d-components-with-a-fuse-and-an-incline-relay
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM (GT65-NT014) '6.5 Driver Board function', PDF p. 28 (printed 29),
    lines 357-388; capacitor rating read from the 110 dpi render
  extracted_at: '2026-09-11'
---

Section 6.5, "Driver Board function", is the same **B426D** photograph as the wire-connections page with red
component labels:

| Label | Where on the board |
|---|---|
| Bridge | the black module at the top left, screwed to the heat-sink plate |
| IGBT | the black module at the top right, screwed to the plate |
| X capacitor (Safety CAP.) | the yellow block capacitor beside the AC terminals |
| Filter Capacitor | the large radial electrolytic in the centre, marked **1000µF 200V** |
| Varistor | the blue disc below the X capacitor |
| RELAY | the black cube below the X capacitor |
| TRANCEFORMER (so spelled) | the yellow **EE22-1.2mH** part at the bottom left |
| SPEED SENSOR | the white 2-pin socket, bottom right |
| MAIN CONTORL WIRES (so spelled) | the black 5-pin header, bottom centre |
| AC220V INPUT N / AC220V INPUT L | the ACN and ACL spade terminals |
| M- / M+ | the BLACK and RED spade terminals, right edge |

**The AC terminals are labelled "AC220V INPUT" although the board photographed carries the 110V sticker** - the
labels were drawn for the 220 V version and reused. There is no fuse label on this page and no LED page in this book;
the annotated technician's photograph of the same board notes two red LEDs near the AC terminals, which this page
does not label. What an LED means when it lights is the errors section's subject; this book prints no
LED debugging table.
