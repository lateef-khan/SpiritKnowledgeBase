---
id: cic850-2022-console-measuring-ranges-and-ble40
title: 'The console reads cadence to 199 RPM, speed to 99 km/h and pulse from 30 to 240 BPM, over BLE4.0'
kind: spec
question: 'What are the measuring ranges and the Bluetooth protocol of the console on a Spirit cic850-2022 indoor cycle?'
asked_as:
- 'what bluetooth version does my indoor cycle console use'
- 'how high does the rpm read on the cic850'
- 'top speed shown on the spin bike display'
- 'what is the maximum countdown on the bike console'
keywords:
- 'console specification'
- 'measuring range'
- 'cadence bar graphic'
- '199 rpm'
- '99 km/h'
- '240 bpm'
- 'ble4.0'
- 'bluetooth low energy'
- 'count up'
- 'count down'
facets:
  brand:
  - spirit
  product_line: bike
  model: cic850-2022
  applies_to:
  - cic850-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-console-xic600-measuring-ranges
see_also:
- sole-spinner-dt3268-console-specification-2021
- sb900-2023-dt3268-console-specification
- cic850-2022-console-face-and-three-keys
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: CIC850-2022 printed p. 24, the specification block under the console drawing
  extracted_at: '2026-09-09'
---

| Item | Range |
|---|---|
| Cadence bar graphic | 0 - 199 RPM |
| RPM | 0 - 199 RPM |
| Speed | 0 - 99 KM/H |
| Pulse | 30 - 240 BPM |
| Time, count down range | 1 - 99 Minutes |
| Time, count up range | 00:01 - 99:59 |
| Protocol | **BLE4.0** |

**BLE4.0 is what the phone connects over.** It is the protocol behind the smartphone key, the Zwift
connection and the Kinomap connection.

**Speed is published in km/h only**, although the console will display MPH once the weight unit is
set to Lb - the manual notes that changing metric units to imperial affects the displayed units
MPH/KPH, Lb/KG and ML/KM.

**These are not the XIC600's figures.** That indoor cycle's console runs to **240 RPM** on a **0-200
rpm** cadence bar and **96 KM/H**, and publishes no Bluetooth protocol at all. Serving one set for
the other is a 41 RPM error at the top of the scale.

**The identical table is published by SOLE for the DT-3268 console** fitted to its SB900 indoor
cycles - same seven rows, same figures, same BLE4.0. It is the same console module sold under two
brands. That is a cross-brand look-alike, not a shared card: see
`sole-spinner-dt3268-console-specification-2021` and `sb900-2023-dt3268-console-specification`.
