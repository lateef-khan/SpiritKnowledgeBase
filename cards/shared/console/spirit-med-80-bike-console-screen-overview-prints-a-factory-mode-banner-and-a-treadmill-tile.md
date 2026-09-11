---
id: spirit-med-80-bike-console-screen-overview-prints-a-factory-mode-banner-and-a-treadmill-tile
title: The console overview page prints a screenshot still in Factory Mode, its heart
  rate call-out points at the wrong thing, and its programs tile promises incline
  changes
kind: fact
question: What is on the home screen of a Spirit Medical 8 series bike, and what is
  the Factory Mode message in the manual?
asked_as:
- what is exit the factory mode on my 8.0u
- what are the icons at the top of the 8.5r screen
- my spirit medical bike says factory mode
- why does the bike screen say incline change
keywords:
- console screen
- home screen
- status bar
- factory mode
- banner
- log out
- settings icon
- bluetooth device
- wifi
- heart rate sensor
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- 85ue-2025-console-screen-overview-and-status-bar
see_also:
- spirit-med-80-bike-console-login-by-qr-code-nfc-or-pin-or-as-a-guest
- spirit-med-80-bike-console-settings-menu-and-the-four-viewing-modes-with-close-up-mode
- spirit-med-80-bike-console-wifi-ble-ftms-and-ant-plus
- spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times
- 85s-2025-console-screen-overview-prints-a-factory-mode-banner
- 80t-2026-console-home-screen-icons
source:
  ref: spirit-bike-80u-2025-owners-manual
  locator: 8.0U OM CONSOLE SCREEN - OVERVIEW, PDF p. 22 (printed 20), text.md lines
    562-592, read from a 130 dpi render and the OCR supplement; CONSOLE SCREEN - HOME
    SCREEN, PDF p. 27 (printed 25), lines 717-735. 8.5R OM PDF p. 27 (printed 25),
    lines 723-753, same screenshot; PDF p. 32 (printed 30), lines 878-896.
  extracted_at: '2026-09-11'
---

**The page labels five things in the status bar and two buttons at the foot of the screen:**

| Call-out | What it points at |
|---|---|
| **Log Out** | Left-most icon |
| **Settings** | The gear icon |
| **Bluetooth Device** | The Bluetooth icon |
| **WiFi Connection** | The Wi-Fi icon and the clock (**12:15** in the screenshot) |
| **Heart Rate Sensor Connection** | *see below* |
| **Press Timer to start the Timer program** | The **Timer** button |
| **Press Start to begin the exercise session** | The **Start** button |

**The body of the screen is a Welcome carousel** with **Age, Height (cm) and Weight (kg)** pickers -
the screenshot shows 30, 165 and 75 - under the line "To get more accurate results, please provide your
physical data". **"Swiping from left to right to see more and then select the wanted item to start"**;
the next card in the carousel is **Pattern Programs**. The HOME SCREEN page five pages later shows
the same carousel headed by the **user name** once someone has logged in.

**Three defects on this page, visible only in a render** (`pdftotext` returns the call-outs alone):

- **The screenshot was taken with the machine still in Factory Mode.** A grey toast under the status
  bar reads **`Exit the Factory Mode once the testing is over.`** with an **X** to dismiss it. It is a
  factory test banner never cleared before the photograph, **not** a message an owner should see.
- **The Heart Rate Sensor Connection leader line lands on that toast's X**, not on a status-bar icon.
  The heart-rate icon is the **third** icon, the waveform between the gear and the Bluetooth symbol.
- **The Pattern Programs tile reads "Programs with incline change"** - a treadmill screenshot in a bike
  book. These bikes have no incline; the tile's text is the 8.0T's.

**The same screenshot, banner and all, is printed in the 8.5S stepper book**
(`85s-2025-console-screen-overview-prints-a-factory-mode-banner`) and again on the maintenance-mode
page of both bikes' service manuals
(`spirit-med-80-bike-console-maintenance-mode-on-the-wifi-icon-once-and-the-clock-six-times`), where
the Wi-Fi icon and the clock are the entry gesture. The 8.5UE's page labels its status bar without
the banner (`85ue-2025-console-screen-overview-and-status-bar`).

