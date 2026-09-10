---
id: spirit-residential-bike-specs-no-specification-table
title: No specification table in fourteen residential bike owner's manuals, and the
  figures printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight and flywheel weight
  for a Spirit residential recumbent or upright bike?
asked_as:
- how much does the spirit recumbent bike weigh
- how big is the xbr55 when its built
- what is the shipping weight of the upright bike
- how heavy is the flywheel on this bike
keywords:
- specifications
- spec sheet
- assembled dimensions
- footprint
- machine weight
- shipping weight
- carton size
- flywheel weight
- q factor
- floor space
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2019
  - xbr25-2023
  - xbr55-2019
  - xbr55-2021
  - xbr55-2023
  - xbr55ent-2021
  - xbr95-2016
  - xbr95-2018
  - xbr95-2021
  - xbr95-2023
  - xbu55-2019
  - xbu55-2021
  - xbu55-2023
  - xbu55ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-no-specification-table
- spirit-cycle-specs-no-specification-table
- spirit-xe-specs-no-specification-table
- spirit-ce-specs-no-specification-table
see_also:
- spirit-residential-bike-specs-console-display-type
- spirit-residential-bike-specs-which-manuals-print-a-parts-list
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- spirit-residential-bike-specs-forty-resistance-levels
- spirit-residential-bike-specs-twenty-resistance-levels
source:
  ref: spirit-bike-xbr55-2023-owners-manual
  locator: 'Table of Contents printed p. 1 (PDF page 3) and whole document; the same
    absence was checked in all fourteen manuals - XBR95 2016, XBR95 2018, XBR25 2019,
    XBR55 2019, XBU55 2019, XBR55 2021, XBU55 2021, XBR95 2021, XBR55ENT 2021, XBU55ENT
    2021, XBR25 2023, XBR55 2023, XBR95 2023 and XBU55 2023, each at its own Table
    of Contents and across every page of its PDF'
  extracted_at: '2026-09-10'
---

**None of the fourteen Spirit residential recumbent and upright bike owner's
manuals contains a specification table.** All fourteen were checked. No table of
contents has a Specifications entry, and none of these figures is printed
anywhere in any of them:

- **assembled dimensions** - no length, width or height, in any unit. The word
  *dimension* appears **zero** times in all fourteen books.
- **machine weight**, shipping weight, gross weight or carton size. *Shipping*
  appears only in warranty terms; *carton* only in "remove all parts from the
  carton".
- **flywheel weight or diameter**, and no gear ratio. The word *flywheel* appears
  only in the six books that print a parts list, as an item name with a quantity
  of 1 and no measurement - see
  `spirit-residential-bike-specs-which-manuals-print-a-parts-list`.
- a **floor footprint** or a required operating area. *Footprint* and *floor
  space* appear zero times.
- a **resistance range in watts, newtons or kilograms**. Resistance is given only
  as a count of console levels.
- a **Q factor** or pedal-spacing measurement. The phrase appears zero times.

The word *specification* occurs in only three places in the whole range: warranty
boilerplate ("Product features or specifications ... subject to change"), the
operating-temperature safety line, and a note that the 5 kHz heart rate signal is
"an older specification". None of them is a machine figure.

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them. **Do not carry a figure across from one
printing to another, and never in from a Spirit commercial bike or from a Sole
bike.**

## What the fourteen books do print, and where each fact lives

| Figure | What is printed | Section |
|---|---|---|
| Resistance levels | **40** in the four XBR95 books; **20** in the other ten | specs |
| Console display | a Large Blue-LED Matrix Window in eight, an LCD Window in four, a Touchscreen in two - **and no size in any of them** | specs |
| Resistance unit | named only where there is a parts list - a **Gear Motor** in five and a **Generator/Brake Controller** in one; the other eight name no resistance part at all | specs |
| Exploded view and parts list | in **six** of the fourteen; none in the other eight | specs |
| User weight limit | **350 lb** in the four 2023 books and the two ENT books; the **eight older books print no weight limit at all** | safety |
| Operating temperature / humidity | 40 to 120 °F and 95% non-condensing in the older books; **three 2023 books print "40 degrees C" instead** | safety |
| Power source | a **built-in generator** on the four XBR95 books, which say the bike need not be plugged in; the other ten say the console powers up when the cord is connected | safety |

## This absence was proved from the PDFs, not only from the text extract

A missing specification table is exactly the claim a flat-image page fakes, so
every page of all fourteen PDFs was counted for extractable text, and **every page
under 25 native words that had no OCR supplement was rendered at 300 dpi and read
with `tesseract --psm 4`.** Fifty-seven such pages were rendered across the
fourteen books. Every one of them is a front cover, a blank page, a `NOTES` page,
a bare page number, a back cover, or the XBU55 2023 exploded-view drawing. **None
carries specification data.**

A word count alone is not enough, because a page can be half text and half
picture, so three whole books were also read twice over - every page rendered at
300 dpi and its OCR word count compared against its `pdftotext` count. The three
were **XBR95 2016** (the oldest layout), **XBR55 2023** (the newest and longest
non-touchscreen book) and **XBR55ENT 2021** (the touchscreen book, which has the
most imaged pages). No page in any of them hides text behind a picture beyond the
console and program artwork already carried in the OCR supplements.

Searching all fourteen extracts for dimension-shaped and weight-shaped figures -
`NN lbs`, `NN kg`, `NN" x NN" x NN"` - returns only fastener sizes from the parts
lists, the 350 lb user weight limit in six books, and a 155 lb example body weight
in the fitness-test chart.

**There is no specification table. Do not re-run this check.**

## The recumbent and the upright are not interchangeable here

The narrative specification facts really are shared between a recumbent book and
its upright twin - the resistance-level paragraph, the absence of a specification
table and the display description are word for word the same.

**Their parts lists are not.** Measured as the overlap of item names on the parts
pages alone, XBR55 2023 against XBU55 2023 shares **49.1%** of its part names, and
XBR55ENT 2021 against XBU55ENT 2021 only **43.0%** - against **91.8%** for XBR55
2023 against XBR95 2023, two recumbents. The recumbent carries a seat carriage, a
seat track, seat track wheels and a seat back frame that an upright has no
equivalent of. **Never answer a parts question for one from the other's list.**
