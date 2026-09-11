---
id: crw800-2024-specs-resistance-system
title: A fan and flywheel braked by a gear motor, with the console running on two C
  cells
kind: spec
question: What kind of resistance does a Spirit CRW800 commercial rower use, and does
  it need batteries or an outlet?
asked_as:
- is the spirit rower air or magnetic
- does the rower need batteries
- how does the resistance work on the spirit rowing machine
- does the rowing machine plug in
keywords:
- resistance
- air rower
- magnetic
- flywheel
- fan
- gear motor
- generator brake
- batteries
- c cell
- power
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2021
  - crw800-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800h2o-specs-six-water-fill-levels
- crw900-2021-specs-ten-level-tank-adjuster
- spirit-xrw600-specs-resistance-mechanism-never-named
- spirit-climber-2024-specs-resistance-system
- spirit-bike-specs-generator-brake-or-induction-brake
see_also:
- crw800-2024-specs-parts-list
- crw800-2024-specs-level-range-1-to-16
- spirit-crw800-specs-no-specification-table
- spirit-rower-specs-crw800-parts-list-2021-vs-2024
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: "Parts List printed pp. 36-37 (PDF pp. 38-39), items 22, 23, 24, 25, 29, 35, 36-1 to
    36-6, 43-06, 43-07, 74, 75, 76 and 77; battery note printed p. 14 (PDF p. 16); mains
    figure inside the troubleshooting table, printed p. 32 (PDF p. 34), read from the OCR
    supplement of a flat-image page. The CRW800-2021 parts list, printed pp. 41-42 (PDF pp.
    43-44), carries every one of those items with the same names and quantities, and its
    battery note is printed p. 13 (PDF p. 15). CRW800 (2020) service manual 800940 (spirit-
    rower-crw800-2021-service-manual): Unit Block Diagrams, PDF p. 24; 6-1-4 generator
    controller, PDF p. 29, text.md lines 385-404; circuit diagram, PDF p. 41; 11-10
    Batteries and 11-11 Generator motor replacement, PDF pp. 60-61, lines 917-936"
  extracted_at: '2026-09-10'
---

**The manual never uses the words *air*, *magnetic* or *damper*, and never states
a resistance rating.** The parts list is the only place the mechanism is named,
and it names both halves of it:

| Part | Item | What it tells you |
|---|---|---|
| **Fan** | 22 | there is an impeller in the housing |
| **Galvanized iron net (L)** and **(R)** | 76, 77 | a two-piece guard over that fan |
| **Flywheel** | 23 | on the same shaft |
| **Drive Belt** | 24 | driven from the handle chain |
| **Flywheel Pulley** and **Flywheel Pulley Axle** | 25, 13 | - |
| **Generator/Brake Controller** | 29 | the board that sets the brake |
| **Gear Motor** | 35, covered by 74 and 75 | the motor that moves the brake to the level you select |
| **Ribbon Roll** | 30 | the recoil for the handle strap |

**So it is a fan-and-flywheel rower whose resistance is set by a motor, not by a
damper lever.** There is no damper door, no damper number and no lever anywhere
in the parts list or the assembly chapter. The user sets a level on the console
instead - 1 to 16, see `crw800-2024-specs-level-range-1-to-16`.

**The level control is wireless.** Item 36 is a `Controller Assembly` with six
sub-items: `Top Handgrip Cap` (36-1), `Rear Handgrip Cap` (36-2), `Battery Cover`
(36-3), **`Resistance Button W/Cable+Faceplate` (36-4)**, **`RF Module` (36-5)**
and **`Battery` (36-6)**. The resistance buttons sit on the handle and talk to
the machine over RF, on their own battery.

## Batteries and mains, and where each is stated

**The console runs on two C cells.** Printed p. 14: *"The console operates on 2*C
batteries (not included). The battery compartment is on the back side of the
console."* The parts list backs this up with a `Battery case` (43-06) and a
`battery cover` (43-07) inside the console assembly. **Buy the cells; the box
does not contain them.**

**The machine still plugs in.** The maintenance page prints "UNPLUG ROWER BEFORE
PERFORMING ANY MAINTENANCE" in capitals, and the troubleshooting table, against a
dim or incomplete display, says to *"Check whether the AC power input is
AC100 ~ 240V"*. The gear motor and the generator/brake controller are what that
supply feeds.

**`AC100 ~ 240V` is the only mains figure in the book, and it is not a supply
specification.** It appears inside a troubleshooting step as a thing to measure,
not on the electrical safety page, which for this machine states no voltage, no
amperage and no circuit-breaker rating - unlike the CS800 and CRS800S stepper
books of the same range, which ask for a 110-volt, 15-amp outlet with a dedicated
5-amp breaker. Do not quote the stepper requirement for a rower.

## Both printings of the CRW800 say this, and neither ever uses the word "air"

The **2021** and **2024** parts lists carry all of the items above with the same
names and quantities, so this is one fact about one machine across two books. The
whole difference between the two lists is a washer thickness and one screw
quantity - `spirit-rower-specs-crw800-parts-list-2021-vs-2024`. The 2021 list even
heads itself with the factory drawing code **`CW800B-YR003-01 Part List_SPIRIT`**,
which is where the `CW800B` string hidden in the 2024 exploded view comes from.

## Not the water rowers, not the XRW600, and not a bike

The two Spirit **water** rowers are tank-and-paddle machines with no fan, no
flywheel and no gear motor: the `crw800h2o` is set by how much water is poured in
(`crw800h2o-specs-six-water-fill-levels`) and the `crw900-2021` by a knob on the
tank (`crw900-2021-specs-ten-level-tank-adjuster`). Nothing on this card applies to
either.

**The XRW600 is the one to be careful with.** It shares this console chapter almost
word for word and the same 1-16 level scale, but **its manual prints no parts list
and never names a mechanism** - so there is no evidence in that book that it has a
fan, and none that it has a magnet either. Do not answer an XRW600 from this card;
see `spirit-xrw600-specs-resistance-mechanism-never-named` - its **service** manual, unlike
its owner's manual, does name a fan, flywheel and gear motor
(`xrw600-2019-specs-service-manual-names-a-fan-flywheel-and-gear-motor`).

**No flywheel weight, fan diameter, drag factor or watt figure is printed
anywhere.** The Watts window reports the work the rower is doing, not the
setting. See `spirit-crw800-specs-no-specification-table`.

## What the 2020-version service manual adds

The CRW800 (2020) service manual (book 800940, the `crw800-2021` machine) confirms the mechanism
and names the power path the owner's manuals leave implicit:

- **The generator/brake controller is a generator controller.** Its block diagram runs GENERATOR
  -> GENERATOR CONTROLLER -> TENSION MOTOR -> display board, and its circuit diagram draws **no
  mains adapter, plug or switch** - the flywheel's generator is the machine's power source,
  rectified on an AE0076 board (`crw800-2021-specs-generator-controller-ae0076-connector-definition`,
  `crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control`). The book's own
  no-display checks say "check the battery" and "check the generator"; it never prints an AC
  figure. **So the "AC100 ~ 240V" line of the 2024 owner's-manual troubleshooting table is not
  corroborated by the service manual for this machine** - it is a template line, and the safest
  answer is that the 2020-version CRW800 draws its power from its own generator and the console
  from its batteries.
- The gear motor's working voltage is **DC 4.0-6.0 V**
  (`crw800-2021-specs-electrical-configuration-tension-motor-dc-4-0-to-6-0-v`).
- The wireless level control is confirmed as an **RF module in the handlebar** talking to a radio
  on the console board.

**The 2016 CRW800 was different**: its service manual (CW800-YR001, the `crw800-2016` machine)
draws a **12 V 1.5 A wall adapter into a DC jack** and no generator
(`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack`). That machine is
not on this card.
