---
id: spirit-indoor-cycle-safety-no-mains-outlet-or-voltage
title: These bikes need no outlet, no voltage and no amperage, and run on AA or AAA
  batteries or on nothing at all
kind: fact
question: What outlet, voltage and amperage does a Spirit indoor cycle, air bike or
  Johnny G Spirit Bike need (ab900-2018, ab950-2024, cb900-2013, cic800-2021, cic850-2022,
  jb950-2022, xic600-2018 or xic600-2021)?
asked_as:
- does the indoor cycle need to be plugged in
- what outlet does the air bike need
- there is no power cord on my spin bike
- what voltage does the johnny g bike run on
keywords:
- outlet
- power cord
- plug
- voltage
- amperage
- grounding
- battery
- self powered
- no plug
- mains
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - ab900-2018
  - ab950-2024
  - cb900-2013
  - cic800-2021
  - cic850-2022
  - jb950-2022
  - xic600-2018
  - xic600-2021
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-safety-no-mains-outlet-needed
- spirit-ce850-safety-outlet-and-circuit-requirement
- spirit-ct800-safety-outlet-120-volt-15-amp
- spirit-xe-safety-no-outlet-figure-printed
see_also:
- spirit-bike-safety-no-mains-outlet-needed
- spirit-cic-safety-instructions-list
- spirit-xic600-safety-instructions-list
- ab950-2024-safety-instructions-list
- jb950-2022-console-power-and-wake-sequence
- jb950-2022-console-demo-mode
source:
  ref: spirit-bike-cic800-2021-owners-manual
  locator: 'Established by absence across all eight manuals - the words outlet, amp,
    power cord and extension cord appear in none of them, and the only occurrences
    of volt are battery voltage and the only occurrences of ground are the floor and
    the warranty conditions boilerplate. Service manuals: AB900 (AU800/AU800A) CONSOLE
    SETUP/Battery Installation, PDF p. 13 (printed 13), text.md line 161, and the
    block diagram `CONSOLE POWER AA * 4 PCS Batteries`, PDF p. 23, lines 412-413;
    CIC850 block diagram `LR03`, PDF p. 17 (printed 17), line 276, its OCR supplement
    for p. 18 (`LRO3 BATTERY`), and 9-3 Display Blank, PDF p. 26, line 388; JB950
    5.3 MAINTENANCE MENU, PDF p. 39 (printed 39), lines 610-613 and 633, the lower
    control board `External Power 9 V DC` / J5 `POWER 9 VIN`, PDF pp. 31-32, lines
    440-441 and 482-483, DEMO MODE, PDF p. 43, lines 801-803, and 1. Generator Replacement
    / 3 Electrical Configurations, PDF pp. 5 and 25, lines 50 and 350-351.'
  extracted_at: '2026-09-09'
---

**None of these eight manuals prints an outlet, a voltage, an amperage, a plug type, a circuit
rating, an extension-cord rule or a grounding page. There is no figure to give, because none of
these machines takes mains power.**

Searched across all eight books: `outlet` 0 hits, `amp` 0 hits, `power cord` 0 hits, `extension
cord` 0 hits. The word `volt` appears only as `When battery working voltage is low`, and `ground`
only as the floor the bike stands on and in the warranty conditions boilerplate `Proper connection
to a grounded power supply of sufficient voltage`, which is Spirit's standard warranty text and not
a requirement for these machines.

## What actually powers each console

| Machine | Console | Power |
|---|---|---|
| CB900-2013 | **none** | Nothing. The manual never mentions a console, monitor or computer |
| CIC800-2021 | **none** | Nothing. The manual never mentions a console, monitor or computer |
| XIC600-2018, XIC600-2021 | Cycling Monitor | 2 AAA in the console **and** 2 AAA in the speed sensor transmitter |
| CIC850-2022 | Console 110 | 2 AAA, plus a separate battery on the sensor board |
| AB900-2018, AB950-2024 | Air bike console | 4 x AA, **not included** |
| JB950-2022 | JB950 console | Self-powered; it wakes from sleep when the rider pedals |

- **The CB900 and the CIC800 are purely mechanical.** They have no electrical part at all, so there
  is nothing to power and nothing to fail electrically. That is an absence in the manual, not an
  omission by the extractor: neither book contains the words console, monitor, computer or battery
  anywhere.
- **The JB950 is the only one of the eight with a mains connection described anywhere**, and it is
  not for riding. Its Maintenance Mode DEMO MODE setting says `a plug-in cord would be required
  that can connect with the bikes electrical board. This setting is primarily used for manufacturer
  Trade Shows and requires access to electricity.` No cord is supplied, no voltage is given, and the
  bike is ridden without one.
- **The air bikes are fan-braked.** There is no generator, no brake controller and no resistance
  motor to power. The AB950's boxed safety callout asks the reader to review `the user weight
  restrictions of your new machine` where the commercial bike manuals ask for weight restrictions
  **and power requirements** - the power clause is dropped because there are none.

## This is not the same answer as the commercial bikes

The commercial CR and CU bikes also need no outlet, but for a different reason and with a different
sentence: they carry a built-in generator, and their manuals say so explicitly -
`spirit-bike-safety-no-mains-outlet-needed`. **None of the eight machines here has a generator**;
the word does not appear in any of the eight books. Do not answer an indoor cycle or air bike
question with the generator text, and do not tell an owner to pedal to wake a CB900 or CIC800
console that does not exist.

The battery types above are given so the outlet answer is complete. For fitting, replacing and
low-battery behaviour, see the assembly and console cards for each machine.

## The service manuals agree, and the JB950's names a generator and a 9 V adapter

- **AB900**: `The console operates on 4*AA batteries (not included)`, and the block diagram labels
  the console power `AA * 4 PCS Batteries`. No outlet, no adapter, no generator.
- **CIC850**: the block diagram shows an `LR03` (AAA) cell feeding the console and the speed
  transmitter, and the display-blank check is `Check the battery of console and transmitter`. No
  outlet, no adapter, no generator.
- **JB950**: the service manual says what the owner's manual does not - **the bike has a generator**.
  Its parts-replacement chapter opens with `1. Generator Replacement`, its electrical configuration
  says the lower controller `consists of the generator interface and switching power supply for the
  console and brake motor control circuitry`, and the lower board has a `GENERATOR POWER IN`
  connector. So the sentence above that none of the eight has a generator holds for the owner's
  manuals, not for this book. It is still self-powered - `PEDALING ABOVE 30 RPM IS ALL THAT IS NEEDED
  TO ILLUMINATE CONSOLE` - and still takes no outlet to ride. What the service manual adds is the
  adapter the owner's Demo Mode note hints at: `OR USE OPTIONAL 9V POWER ADAPTER TO POWER CONSOLE
  WITHOUT PEDALING. (Adapter available as a service part through your Spirit distributor)`, with a
  `POWER 9 VIN` socket on the lower control board labelled `External Power 9 V DC`. **9 V DC is the
  adapter's output; the book gives no outlet, mains voltage or current for it**, and no adapter is
  supplied with the bike.
