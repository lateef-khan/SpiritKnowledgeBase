---
id: spirit-bike-console-xic600-measuring-ranges
title: 'The console reads cadence to 240 RPM, speed to 96 km/h and pulse from 30 to 240 BPM'
kind: spec
question: 'What are the measuring ranges of the console on a Spirit XIC600 indoor cycle?'
asked_as:
- 'what is the top speed the indoor cycle console will show'
- 'how high does the rpm go on the spin bike display'
- 'what is the maximum time the bike console counts to'
- 'cadence bar graph range on the spirit indoor cycle'
keywords:
- 'console specification'
- 'measuring range'
- 'cadence bar graph'
- 'rpm range'
- 'speed range'
- 'pulse range'
- 'count up'
- 'count down'
- '240 rpm'
- '96 km/h'
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xic600-2018
  - xic600-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cic850-2022-console-measuring-ranges-and-ble40
see_also:
- spirit-bike-console-xic600-face-and-two-keys
- spirit-bike-console-xic600-display-windows
source:
  ref: spirit-bike-xic600-2021-owners-manual
  locator: XIC600-2021 printed p. 19 CONSOLE SPECIFICATION; XIC600-2018 printed p. 19 - identical
  extracted_at: '2026-09-09'
---

| Item | Range |
|---|---|
| Cadence bar graph | 0~200 rpm, **10 rpm per bar** |
| RPM | 0 ~ 240 RPM |
| Speed | 0 ~ 96 KM/H (0 ~ 60 mph) |
| Pulse | 30 ~ 240 BPM |
| Time, count down range | 1~99 minutes |
| Time, count up range | 00:01~99:59 |

**The manual publishes no Bluetooth protocol for this console** and no wireless data figure. The
only radio it describes is the coded link from the speed sensor transmitter and the built-in heart
rate receiver.

**These are not the CIC850's figures.** That bike's DT-3268F console tops out at **199** RPM with a
**0-199 RPM** cadence bar and **99 KM/H**, and publishes **BLE4.0**. Serving one set for the other
gives a rider a 41 RPM error at the top of the scale.
