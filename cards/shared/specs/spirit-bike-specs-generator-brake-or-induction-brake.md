---
id: spirit-bike-specs-generator-brake-or-induction-brake
title: Two different resistance units - a generator brake on most commercial bikes,
  an induction brake with an EMS controller on three of them
kind: spec
question: What kind of resistance or brake does a Spirit commercial upright or recumbent
  bike use?
asked_as:
- how does the resistance work on the spirit commercial bike
- is this bike magnetic resistance
- what is the brake part on a cu800ent
- does the bike generate its own power
keywords:
- resistance
- brake
- generator
- induction brake
- ems controller
- magnetic
- eddy current
- brake controller
- power adaptor
- self powered
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cr800-2023
  - cr800ent-2023
  - cr900-2025
  - cu800-2021
  - cu800ent-2022
  - cu800ent-2024
  - cu900-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cycle-specs-resistance-systems
see_also:
- spirit-bike-specs-no-specification-table
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-ce-specs-forty-resistance-levels
source:
  ref: spirit-bike-cr800-2021-owners-manual
  locator: 'Parts List p. 41, items 43 and 55; also CR800-2023 p. 41, CU800-2021
    p. 41 items 20 and 21, CR900-2025 p. 37 items 69 and 70, CU900-2025 p. 36 items
    49 and 50, CR800ENT-2023 p. 47 items 047, 048, 049, 055 and 195, CU800ENT-2022
    p. 47 items 20, 21, 27, 31 and 32, CU800ENT-2024 p. 53 items 20, 21, 27, 31 and
    32'
  extracted_at: '2026-09-09'
---

The manuals never state a resistance rating in watts, newtons or kilograms.
**What they do tell you is which resistance unit is fitted, and it is not the
same part on every machine.** The parts lists name it.

| Machines | Resistance unit named in the parts list | Its controller |
|---|---|---|
| CR800-2021, CR800-2023 | **Generator/Brake** (item 55) | Generator/Brake Controller (43) |
| CU800-2021 | **Generator/Brake** (item 20) | Generator/Brake Controller (21) |
| CR900-2025 | **Generator/Resistance** (item 69) | Generator/Brake Controller (70) |
| CU900-2025 | **Generator/Resistance** (item 49) | Generator/Brake Controller (50) |
| CR800ENT-2023 | **Induction Brake** (item **055**) | **EMS Controller** (**049**) |
| CU800ENT-2022, CU800ENT-2024 | **Induction Brake** (item 20) | **EMS Controller** (21) |

**A CR800 and a CR800ENT do not share a brake.** The generator machines brake
against the same unit that powers the console; the ENT-800 machines have a
separate induction brake driven by an EMS controller, and take their power from a
wall adaptor instead.

## The supporting parts follow the same split

The generator bikes list an **AC Input Module** and a **TV Adapter (5C2V)**. The
ENT-800 bikes list an **AC Electronic Module**, a **Power Adaptor** and a
**Control Power Board** instead, plus the HDMI and network wiring the touchscreen
needs. Asking for "the brake controller" on an ENT-800 and getting a
Generator/Brake Controller quoted is the wrong part.

**The same part has a different item number on the recumbent and the upright.**
The CR800ENT-2023 numbers its electrical parts in a three-digit padded series of
its own - Power Adaptor **047**, Control Power Board **048**, EMS Controller
**049**, Induction Brake **055**, AC Electronic Module **195**. The two CU800ENT
books number the identical parts **31, 32, 21, 20 and 27**. Quote an item number
only from the book for the machine in front of you. **Both numbering schemes were
re-read from the parts-list pages rendered at 300 dpi**, not only from the text
extract.

## Five of the thirteen manuals cannot answer this question

The CR900-2018, CR900ENT-2021, CU800-2012, CU900-2018 and CU900ENT-2021 owner's
manuals print no parts list at all, so **they name no brake part**. The CR900-2018,
CU800-2012 and CU900-2018 console chapters say the machine has a built-in generator
and turns on when you pedal; the CR900ENT-2021 and CU900ENT-2021 books instead say
to plug in the power cord. Either way that is a power statement, not a part. Do not infer a Generator/Brake item number for those five
from a book that covers a different machine - see
`spirit-bike-specs-which-manuals-print-a-parts-list`.

## Where the power supply itself is answered

Whether the machine needs an outlet, and at what voltage and amperage, is a
safety question and lives in the `safety` section, not here. In outline: the
**eight LED-console machines** run off the built-in generator and need no outlet;
**all five touchscreen machines plug in**. The CR900ENT-2021 and CU900ENT-2021
books simply say to plug in the power cord at the front base and never use the
word *generator* at all; the CR800ENT-2023 and CU800ENT-2022 ask for a 110-volt,
5-amp grounded circuit; and **the CU800ENT-2024 asks for a 120-volt, 15-amp
circuit instead** - the same machine family, a different requirement, so check the
printing in front of you.

## No resistance figure is printed anywhere

Level 1 to 40 is a console scale, not a physical rating. **No Spirit commercial
bike manual prints a level-to-watts table**, and the Watts readout on the console
reports the work the rider is doing, not the setting. See
`spirit-bike-specs-no-specification-table`.
