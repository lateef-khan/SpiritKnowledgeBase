---
id: spirit-xe400-xe500-2007-specs-wiring-schematic
title: 'Incline elliptical schematic of the 2007 dealer manual: fused inlet, red 300
  mm mains leads, transformer plugs, a JS-15A incline motor on black down, red up,
  white common and ground, a 3-pin VR cable, and a 10-pin 1000 mm and 7-pin 1450 mm
  console loom'
kind: spec
question: What does the wiring schematic of a Spirit XE400-2007 or XE500-2007 elliptical
  show?
asked_as:
- xe500 wiring diagram
- xe400 schematic
- which wire is up on the xe500 incline motor
- how long is the console cable on the xe400
keywords:
- schematic
- wiring diagram
- incline controller
- jk1 jk2 jk5 jk6 jk7
- js-15a incline motor
- transformer
- fuse
- 10 pin 1000mm
- 7 pin 1450mm
- gear motor 5 pin
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe400-2007
  - xe500-2007
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xe400-xe500-2007-specs-incline-controller-alt-670100a-wiring
- spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer
- spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller
- xe400-2007-specs-parts-list
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: XE400/XE500 schematic, PDF p. 9, text.md lines 294-300; the page is a flattened
    drawing read from a 300 dpi render (OCR supplement lines 1510-1570). Only the
    two incline machines have a schematic in this book
  extracted_at: '2026-09-11'
---

The only wiring drawing in the dealer manual, and it covers the two incline machines alone.

**Mains.** Plug -> female connector -> **inlet with FUSE** -> two **RED 300 mm** leads to **AC1** and
**AC2** on the incline controller.

**Transformer.** Two leads to the controller: a **4-pin plug on JK2** and a **3-pin plug on JK6**.

**Incline motor - JS-15A.** Four wires from the controller: **DOWN black, UP red, COM white, and
GROUND**; plus a **3 PIN INCLINE VR CABLE** from the motor's position sensor to **JK1**.

**Console loom.** From **JK5** on the controller, a **10 PIN, 1000 mm** cable up the mast that
becomes a **7 PIN, 1450 mm** cable into the console.

**Gear motor.** A **5-pin** plug on the loom; a **2-pin SENSOR** (speed) plug; and a **3-pin plug
marked NO USE**.

The controller's socket names are the ones photographed in Procedure 6
(`spirit-xe400-xe500-2007-specs-incline-controller-alt-670100a-wiring`), and the wire colours the
ones the troubleshooting row tells the dealer to match at the rail joint - black to black, red to
red, white to white (`spirit-xe-2007-errors-incline-does-not-work-check-the-incline-wires-and-controller`).
**No pin-by-pin definition of the 10-pin or 7-pin cable is printed**; the lengths are the only
figures. The XE100-XE300 have no schematic in the book - they run from an adapter with no
controller (`spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer`).

