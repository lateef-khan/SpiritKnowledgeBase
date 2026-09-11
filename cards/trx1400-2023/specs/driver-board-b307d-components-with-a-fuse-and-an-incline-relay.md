---
id: trx1400-2023-specs-driver-board-b307d-components-with-a-fuse-and-an-incline-relay
title: 'The driver board components: bridge, IGBT, a fuse on the AC input, filter
  capacitor, varistor, X safety capacitor, a relay and an incline relay, transformer,
  speed sensor, incline VR and main control line'
kind: spec
question: What are the components on the driver board of an Xterra trx1400-2023 treadmill
  and where are they?
asked_as:
- trx1400 controller components
- where is the fuse on the trx1400 driver board
- trx1400 incline relay
- what relay is on the trx1400 board
keywords:
- driver board
- components
- fuse
- bridge
- igbt
- incline relay
- relay
- transformer
- varistor
- x capacitor
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with: []
see_also:
- trx1400-2023-specs-driver-board-b307d-wire-connections
- trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
- tr150-2021-specs-driver-board-b426d-components-bridge-igbt-relay-and-transformer
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '6.7 Driver Board function', PDF p. 33 (printed
    31), lines 484-519; part markings read from the 110 dpi render
  extracted_at: '2026-09-11'
---

Section 6.7 is a photograph of the **B307D** board (this sample wears a 220V sticker; the drawing on the
wire-connections page has both 110V and 220V boxes) with red labels:

| Label | Where on the board |
|---|---|
| L / N | the ACN and ACL terminals, top left |
| FUSE | the glass fuse in a holder just below the AC terminals |
| Bridge | the black module at the top left, screwed to the heat-sink plate |
| IGBT | the black module at the top right, screwed to the plate |
| Filter capacitor | the large radial electrolytic in the centre, under a green "HI-POT TESTED" sticker |
| Varistor | the blue disc left of the X capacitor |
| X capacitor (Safety CAP.) | the yellow block capacitor |
| RELAY | a SONGLE **SLA-12VDC-SL-A** relay, centre left |
| INCLINE RELAY | a second SONGLE relay below it, by the UP and DOWN terminals |
| COM / UP / DOWN | the three incline terminals, left edge |
| TRANCEFORMER (so spelled) | the yellow **PEE19-005** part, centre |
| M- / M+ | the BLACK and RED terminals, right edge |
| SPEED SENSOR | the white 2-pin socket, right edge |
| INCLINE VR | the 3-pin socket, bottom right |
| MAIN CONTORL LINE (so spelled) | the 5-pin header, bottom right |

The fuse rating is not printed on the page and not legible in the photograph. The TR150's B426D has the same bridge,
IGBT, X capacitor, varistor, relay and transformer layout without the fuse label or the incline relay.
