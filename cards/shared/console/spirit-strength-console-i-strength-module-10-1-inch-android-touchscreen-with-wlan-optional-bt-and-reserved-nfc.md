---
id: spirit-strength-console-i-strength-module-10-1-inch-android-touchscreen-with-wlan-optional-bt-and-reserved-nfc
title: The Digital Resistance Module's console is a 10.1-inch capacitive Android 10
  touchscreen with Wi-Fi, optional Bluetooth 5.0, USB OTG for software upgrade and
  a reserved NFC
kind: spec
question: What is the console on the Spirit i-Strength CSI machines, and does it have
  Wi-Fi, Bluetooth or NFC?
asked_as:
- what screen is on the i-strength machines
- does the csi console have bluetooth
- is the i-strength console android
- can the i-strength console be updated over usb
keywords:
- console configuration
- digital resistance module
- 10.1 inch
- android 10
- capacitive touch
- wlan
- bluetooth 5.0
- usb otg
- nfc reserved
- allwinner
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-csi-console-nine-languages
- spirit-strength-csi-console-wifi-and-software-update
see_also:
- spirit-strength-csi-console-home-screen
- spirit-strength-csi-console-nine-languages
- spirit-strength-csi-console-wifi-and-software-update
- spirit-strength-csi-console-spirit-plus-connect-app
source:
  ref: spirit-strength-i-strength-resistance-module-maintenance-manual
  locator: Digital Resistance Module Maintenance Manual, Chapter 6 Specification of
    critical component, 1. Console configuration plan, PDF p. 23 (printed 23); text.md
    lines 490-547, checked against the OCR supplement lines 844-891. Chapter 2 Product
    Appearance, PDF p. 5, lines 125-136, for the Screen, Screen holder and Light strip
    call-outs
  extracted_at: '2026-09-11'
---

**The module the CSI owner's manuals list as part 72 carries the console**: its Product Appearance
drawing labels a **Screen** on a **Screen holder** above the upper cover, and a **Light strip** across
the front panel. The Console configuration plan is the screen's specification:

| Item | As printed |
|---|---|
| Main chipset | Allwinner R818; quad-core Cortex A53 at 1.5 GHz; GE8300 GPU at 500 MHz |
| Memory | DDR4 1 GB |
| OS | **Android 10** |
| Language | **Chinese/English** |
| LCM | TFT LCD, **10.1**, MIPI interface, max resolution **720 x 1280** |
| Touch panel | **Capacitive**, I²C |
| Audio in | 2 x AMIC, 100 Hz - 15 kHz at ±3 dB (1 kHz 0 dB reference) |
| Audio out | 2 x 3 W (4 Ω), THD+N < 10 % at 1 kHz (0.3 V rms input) |
| WLAN | 150 Mbps max; **2.4 GHz and 5 GHz**; IEEE 802.11 b/g/n/a/ac/ax |
| BT | **Optional**, BT 5.0 |
| USB | **OTG (software upgrade), HOST** |
| NFC | **Reserved** |

**Wi-Fi is fitted; Bluetooth is optional; NFC is a reserved footprint.** The owner's manuals name
Wi-Fi as the console's only network (`spirit-strength-csi-console-wifi-and-software-update`) and
never mention NFC, which agrees with this table - do not promise a CSI owner an NFC log-in on the
strength of the word "reserved".

**Two languages here, nine in the owner's manuals.** The owner's manuals say the console is
programmed with nine languages (`spirit-strength-csi-console-nine-languages`); this table prints
Chinese/English. Both are reproduced as printed and nothing reconciles them; the owner's manual is
the document the user sees.

**A USB upgrade path the owner's manuals do not describe.** They print no USB or offline update
route; the module's USB is specified as OTG "(software upgrade)" and HOST. The book gives no
procedure, file name or port location for it - only the capability.

**10.1 inches, portrait.** The 720 x 1280 resolution is taller than wide, which matches the Home
Screen the owner's manuals describe (`spirit-strength-csi-console-home-screen`). No screen size is
printed anywhere in the owner's manuals.

**The motor and controller table on the following pages, the internal cabling and the block diagram
are held with the specs cards**, and the module's fault list with the error cards.

