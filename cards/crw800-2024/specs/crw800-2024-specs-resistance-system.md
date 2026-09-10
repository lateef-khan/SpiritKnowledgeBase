---
id: crw800-2024-specs-resistance-system
title: A fan and flywheel braked by a gear motor, with the console running on two C
  cells
kind: spec
question: What kind of resistance does a Spirit crw800-2024 commercial rower use, and
  does it need batteries or an outlet?
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
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800h2o-outlines-part-names
- spirit-climber-2024-specs-resistance-system
- spirit-bike-specs-generator-brake-or-induction-brake
see_also:
- crw800-2024-specs-parts-list
- crw800-2024-specs-level-range-1-to-16
- spirit-crw800-specs-no-specification-table
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: Parts List printed pp. 36-37 (PDF pp. 38-39), items 22, 23, 24, 25, 29,
    35, 36-1 to 36-6, 43-06, 43-07, 74, 75, 76 and 77; battery note printed p. 14 (PDF
    p. 16); mains figure inside the troubleshooting table, printed p. 32 (PDF p. 34),
    read from the OCR supplement of a flat-image page
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

## Not the water rower, and not a bike

The repository's other Spirit rower is the **CRW800 H2O, a water rower** - a tank
and paddle, no fan, no flywheel, no gear motor and no resistance levels.
`crw800h2o-outlines-part-names` is not an answer for this machine.

**No flywheel weight, fan diameter, drag factor or watt figure is printed
anywhere.** The Watts window reports the work the rower is doing, not the
setting. See `spirit-crw800-specs-no-specification-table`.
