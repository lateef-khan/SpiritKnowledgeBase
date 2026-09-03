---
id: sole-ftms-bluetooth-app-support
title: Machines that send workout data over Bluetooth FTMS
kind: spec
question: Which Sole machines send workout data to fitness apps over Bluetooth FTMS?
asked_as:
- does my machine work with zwift or kinomap
- can my treadmill send data to an app over bluetooth
- which sole machines have ftms
- my bike does not show up in the fitness app
keywords:
- ftms
- bluetooth
- fitness machine service
- third party app
- workout data
- no bluetooth function
- firmware
- sole bike
facets:
  brand:
  - sole
  product_line: '*'
  model: '*'
  applies_to:
  - '*'
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- sole-bluetooth-not-connecting
source:
  ref: sole-ftms-model-status-20210806
  locator: all six sheets
  extracted_at: '2026-09-03'
---

**Read the date first.** The only source for this is an engineering tracker dated **6 August 2021**. Any machine built after that date is not on it. Treat a machine that is absent as unknown, not as unsupported.

**Machines with no Bluetooth at all.** These can never send FTMS data.

| Line | Models |
|---|---|
| Treadmill | F60, TD80 |
| Elliptical | E20 |
| Bike | R52, R72, B54, B74 |
| Climbing | CC81 |
| Rower | SR500 |

**Machines that do send FTMS data**

| Line | Models | Note as printed |
|---|---|---|
| Treadmill | F63, F80, F65 | Running change. Done, mass production 3 Aug 2021. |
| Treadmill | F85-color TFT, S77-color TFT, TT8-color TFT | Older version FTMS. Non-Android consoles. |
| Treadmill | F85-ENT, ST90-ENT, S77-ENT, TT8-ENT | ENT console. Already on the new full FTMS protocol, "No Need". |
| Elliptical | E25, E35 | OK, May 2020. |
| Elliptical | E55, E95, E95S, E98 | Running change, priority 3. |
| Bike | R92, B94 | OK, May 2020. |
| Bike | LCB, LCR | Running change, priority 3. |
| Flywheel bike | SB700, SB900, SB910 (New) | Older version FTMS. Done. Shows up over Bluetooth as **SOLE BIKE**. |
| Climbing | SC200, SC300 | "No mass production" in every firmware column. |

**What each line is required to send**

| Line | Data required |
|---|---|
| Treadmill, elliptical, climbing | Speed (Instantaneous), Inclination (%), and Power (Watts) |
| Bike, flywheel bike | Cadence (RPM), Power (Watts), and Speed (Instantaneous) |

**What the new-version FTMS actually sends**

- **Treadmill (F63 row)**: Instantaneous Speed, Inclination, Total Energy, Total Distance, Elapsed Time, Remaining Time, Positive Elevation Gain, Heart Rate.
- **Elliptical (E55 row)**: Instantaneous Power, Resistance Level, Step per Minute, Inclination, Total Energy, Total Distance, Elapsed Time, Remaining Time, Instantaneous Speed, Positive Elevation Gain, Stride Count, Heart Rate.
- **Bike (LCB row) and climbing (SC200 row)**: Instantaneous Power, Resistance Level, Total Energy, Total Distance, Elapsed Time, Remaining Time, Instantaneous Speed, Heart Rate.

The old version sent far less: **Speed** only on the F63, and **Watt** only on the E55, LCB and SC200.

**Two notes copied from the sheet.** The E25 row is flagged "Incline resolution error". Most elliptical and bike rows are marked "New Order (after 2021/8/16)", so an older unit of the same model may still be on the old firmware.

The tracker also lists firmware and Bluetooth build identifiers for each model. Those are in the source, not here.
