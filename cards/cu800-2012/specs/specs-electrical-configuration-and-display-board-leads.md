---
id: cu800-2012-specs-electrical-configuration-and-display-board-leads
title: A generator flywheel described in elliptical wording, an EMS BRAKE caption
  on the photo, and a display board with only a cooling fan and a key board called
  out
kind: fact
question: What electrical parts does the service manual name on a Spirit cu800-2012
  upright bike, and what plugs into its display board?
asked_as:
- what is the ems brake on the 2012 cu800
- does the xu878 have a generator
- cu800 2012 display board connections
- what electronic parts are in the 2012 cu800
keywords:
- electrical configuration
- generator flywheel
- ems brake
- main controller
- led display
- cooling fan
- thumb switch
- speed rpm sensor
- controller
- display board
facets:
  brand:
  - spirit
  product_line: bike
  model: cu800-2012
  applies_to:
  - cu800-2012
  section: specs
  code: '*'
  model_number:
  - '800343'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel
- sole-bike-ems-brake-spec
see_also:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram
- cu800-2012-specs-outline-part-names
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: Section 3 Electrical Configurations, PDF p. 11 (printed 11), text.md lines
    161-183; section 2 Electronic Parts, PDF pp. 8-9, lines 121-155; 'Display Board
    wire Connections', PDF p. 26, lines 399-410, photograph read from a 300 dpi render
  extracted_at: '2026-09-11'
---

**Section 3 is copied from an elliptical book.** As printed: the CONSOLE is "Interface that controls
all functions of the **Elliptical**"; the MAIN CONTROLLER "consist of the generator power supply
for console, link the console to output appropriate voltages for **tension motor** that control
the **elliptical** functions"; the **GENERATOR FLYWHEEL** "can change to increase or decrease
resistance level of brake". General information: key controls and an **LED display**; the
controller includes the generator power supply and driver control circuit.

**The chapter-2 photographs contradict it in one word.** The upper-controllers page captions the
flywheel unit **EMS BRAKE** (the parts it names are on `cu800-2012-specs-parts-electronic-parts-named`).
So the same unit is *generator flywheel* in the text, *EMS brake* on the photo and *Induction
Brake* on the skeleton drawing. **It is one part, and the schematic settles what it does**: a three-wire
generator output and a two-wire brake coil, exactly as on the 2020-version CU800 - see
`spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections`. There is no tension
motor on this bike, and no separate EMS controller of the kind the ENT-800 bikes carry.

**The display board (p. 26)** is photographed with only two call-outs: **COOLING FAN** (top) and
**KEY BOARD** (bottom). No other console lead is named and no pin table is printed for this
console.

**One more contradiction, in the Q&A.** Section 8-9 says "make sure power adaptor has been plug
in and DC connector is connected" - but nothing else in the book shows an adaptor, the block
diagram and schematic draw the generator as the only supply, and the owner's-manual card
`spirit-bike-safety-no-mains-outlet-needed` says the bike needs no outlet. Read that line as
another copy-paste, not as a hidden power supply.

