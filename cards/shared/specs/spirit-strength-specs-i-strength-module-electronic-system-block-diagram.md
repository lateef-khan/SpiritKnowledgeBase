---
id: spirit-strength-specs-i-strength-module-electronic-system-block-diagram
title: 'Electronic system block diagram of the digital resistance module: an Allwinner
  R818 console over RS-485 to an AT32F403 motor-control motherboard with an IPM drive,
  a 300 W brake resistor and DC 320 V from the PFC supply'
kind: spec
question: What does the electronic system block diagram of the Spirit i-Strength digital
  resistance module show?
asked_as:
- i-strength block diagram
- how is the digital resistance module wired
- what voltage runs the i strength motor
- what is the pfc module in the csi machines
keywords:
- block diagram
- digital resistance module
- motor control motherboard
- rs-485
- ipm
- dc 320v
- pfc
- brake resistor
- servo motor
- light strip
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-strength-specs-i-strength-module-motor-43-n-m-2000-w-and-foc-controller-rs485
- spirit-strength-console-i-strength-module-10-1-inch-android-touchscreen-with-wlan-optional-bt-and-reserved-nfc
- spirit-strength-specs-parts-digital-resistance-module-internal-cable-list
- spirit-strength-specs-i-strength-module-product-appearance-part-names
source:
  ref: spirit-strength-i-strength-resistance-module-maintenance-manual
  locator: Chapter 5. Electronic system block diagram, PDF p. 22 (printed 22), text.md
    lines 483-488; the diagram is a flattened image read from a 200 dpi render (OCR
    supplement 797-839 is partial and rotated)
  extracted_at: '2026-09-11'
---

One sheet, two halves.

**Console (upper half)**

- **SOC: R818, Quad-core Cortex A53** at the centre, with a **10.1 Inch 1280*800** screen on
  **MIPI 1280*800**.
- **AD52050C IC Audio AMP, Class D, 10Wx2** driving two speakers marked **2x3W (4 ohm)**.
- **SKI.WB800DS2 MODULE** for **BT5.0** and **WIFI 2.4&5G**.
- **UART TTL** out of the SOC into a **UART TO 485 MODULE** - the console's only link downward.

**Motor control motherboard (lower half)**

- **UM3483EESA RS-485** transceiver receiving the console's line.
- **AT32F403AVGT7 MCU, 240MHz, 32bit** at the centre.
- **Motor Drive IPM Module 6MBP35XSF060** driving the **Left 3P Servo Motor**.
- **Fan Control Unit** for two **12V 0.35A** fans.
- **Brake Unit** switching a **300W, 40ohm Resistance** - two finned resistors.
- **Light strip unit** driving the front light strip.
- **DC320V INPUT** from the PFC power module, which takes **AC 100-240V** through the **AC
  Switch**.

**What it means for a technician.** The module runs its servo motor from a **320 V DC bus**, not
from the mains directly and not from a low-voltage adapter - the PFC module (the "power panel" of
the cable list) makes it. Braking energy is dumped into the 300 W 40-ohm resistor pack, which is
why the fault list has a *Regenerative Braking Overload* code and the disassembly guide calls it
the cement resistor. The console and the motherboard speak RS-485 at 115200 bps
(`spirit-strength-specs-i-strength-module-motor-43-n-m-2000-w-and-foc-controller-rs485`); the
console's own specification is on
`spirit-strength-console-i-strength-module-10-1-inch-android-touchscreen-with-wlan-optional-bt-and-reserved-nfc`.

**The screen is 1280*800 here and 720*1280 on the specification table** of the next chapter - the
same panel quoted in two orientations. The physical cables between these blocks are the fourteen
numbered items of chapter 4 (`spirit-strength-specs-parts-digital-resistance-module-internal-cable-list`).

