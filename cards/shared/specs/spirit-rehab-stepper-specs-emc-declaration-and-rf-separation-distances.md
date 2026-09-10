---
id: spirit-rehab-stepper-specs-emc-declaration-and-rf-separation-distances
title: The electromagnetic compatibility declaration, and how far a radio or phone must stay from
  the machine
kind: spec
question: What electromagnetic compatibility declaration does a Spirit rehabilitation recumbent
  stepper carry, and how close may a phone or radio be?
asked_as:
- can i use a mobile phone near the rehab stepper
- is the recumbent stepper emc tested
- how far away must a two way radio be from the stepper
- what is the immunity rating of the ms300
keywords:
- electromagnetic compatibility
- emc
- cispr 11
- immunity
- separation distance
- radiated rf
- electrostatic discharge
- iec 61000
- interference
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - ms300-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- 70t-2026-specs-emc-declaration
- xt-2023-safety-rf-exposure-separation-distance
see_also:
- spirit-climber-specs-medical-certification-list
- spirit-climber-safety-operating-environment-iec-60601
- spirit-rehab-stepper-programs-erratic-heart-rate-seven-sources-and-a-one-metre-rule
source:
  ref: spirit-climber-7-0s-med-owners-manual
  locator: 'Guidance and manufacturer''s declaration - electromagnetic compatibility, printed and
    PDF pp. 69-70 of the 7.0S MED book and pp. 72-73 of the 7.5S MED book; the same two pages in
    the MS300 book at printed pp. 62-64. The ESD test levels are missing from the MED books'' PDF text
    layer and were read from a 300 dpi render; the MS300''s text layer has them'
  extracted_at: '2026-09-10'
---

## Emissions

| Test | Compliance | What it means |
|---|---|---|
| RF emissions **CISPR 11** | **Group 1** | The machine uses RF energy only internally, so its emissions are very low and unlikely to disturb nearby electronics |
| RF emissions **CISPR 11** | **Class B** | Suitable for use in all establishments, **including domestic ones** |

## Immunity

| Test | IEC 60601 test level | Compliance level |
|---|---|---|
| Electrostatic discharge, **IEC 61000-4-2** | **6 kV contact, 8 kV air** | the same |
| Power frequency (50/60 Hz) magnetic field, **IEC 61000-4-8** | **3 A/m** | **3 A/m** |
| Radiated RF, **IEC 61000-4-3** | **3 V/m**, 80 MHz to 2.5 GHz | **3 V/m** |
| Electrical fast transient / burst, **IEC 61000-4-4** | **±2 kV** power supply lines, **±1 kV** input/output lines | the same |

**Floors should be wood, concrete or ceramic tile**, and if they are covered with synthetic
material the relative humidity should be **at least 30%**. Mains quality and magnetic fields should
be those of a typical commercial or hospital environment.

## How far a transmitter must stay away

Recommended separation distance in metres, by the transmitter's maximum output power:

| Transmitter (W) | 150 kHz - 80 MHz | 80 - 800 MHz | 800 MHz - 2.5 GHz |
|---|---|---|---|
| 0,01 | 0,12 | 0,12 | 0,23 |
| 0,1 | 0,38 | 0,38 | 0,73 |
| 1 | 1,2 | 1,2 | 2,3 |
| 10 | 3,8 | 3,8 | 7,3 |
| 100 | 12 | 12 | 23 |

**Decimal commas are the manual's**, not a typo. For an unlisted power, d = 1,2 √P below 800 MHz and
d = 2,3 √P above it.

**In practice: a mobile phone at about 1 watt belongs 1.2 to 2.3 metres away**, and a handheld
two-way radio at 5 watts about 2.7 to 5.1 metres. At 80 MHz and 800 MHz the higher frequency range
applies. The manual notes these guidelines may not apply in all situations, because absorption and
reflection from structures, objects and people change propagation.

## What interference looks like

> If the device is interfered by power or signal cable, **image quality may be reduced or abnormally
> displayed**. Such interference images could be easily identified and differentiated from the
> physiological characteristics of the patient... but wouldn't have any diagnostic accuracy issue.
> If there is a certain frequency of image interference, there is a need of isolation or filtering
> of the RF signal.

That note is printed in the 2025 books too, on their condensed specification page.

**A wild heart rate reading is a different problem with its own list** -
`spirit-rehab-stepper-programs-erratic-heart-rate-seven-sources-and-a-one-metre-rule`.

## The 6 kV and 8 kV figures are not in the MED books' text layer

On both MED books `pdftotext` returns the ESD row as
`Electrostatic discharge (ESD) IEC 61000-4-2` followed by the word `contact` alone, dropping both
test levels. They are on the printed page and were read from a 300 dpi render. **Do not report this
row as blank.** The MS300's own text layer prints `6 kV contact` in full, which is how the render
was confirmed.
