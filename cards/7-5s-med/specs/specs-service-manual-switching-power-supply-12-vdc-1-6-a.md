---
id: 7-5s-med-specs-service-manual-switching-power-supply-12-vdc-1-6-a
title: The service manual's wiring diagram draws a 90 to 260 VAC switching supply
  putting out 12 VDC at 1.6 A, not the 2.74 A Sinpro adapter of the owner's manual
kind: spec
question: What power supply do the Spirit 7-5s-med, 7.0S and 7.5S recumbent stepper
  service manuals specify, and does it match the owner's manual?
asked_as:
- what adapter does the 7.5s service manual show
- is the 7.5s power supply 1.6 amp or 2.74 amp
- 12 volt supply for the spirit rehab stepper
- 7.5s no power check adapter voltage
keywords:
- power supply
- switching power supply
- 12 vdc
- 1.6a
- 90-260 vac
- adapter
- dc jack
- sinpro
- 2.74a
- contradiction
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply
- spirit-climber-85s-specs-mains-power-supply
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
see_also:
- 7-5s-med-specs-wiring-diagram-j13-14-pin-with-wire-colours-and-sensor-cables
- spirit-climber-specs-fuse-rating
source:
  ref: spirit-stepper-7-5s-med-service-manual
  locator: '8. Wiring Diagram, the ''Switching Power Supply'' block, PDF p. 55 (printed
    55), text.md line 873 (OCR supplement 1212-1247 reads the block''s three lines);
    5.2.3 Troubleshooting ''No power'', PDF pp. 13-14, lines 125-146. 7.0S-2025 (spirit-stepper-70s-2025-service-manual):
    the same block on the MS7000 Wiring Diagram, PDF p. 56 (OCR supplement lines 1318-1320),
    and 5.2.3 No power, PDF p. 14, lines 150-164. 7.5S-2025 (spirit-stepper-75s-2025-service-manual):
    PDF p. 56 (OCR 900-902) and PDF pp. 13-14, lines 130-144'
  extracted_at: '2026-09-11'
---

**Two figures for one machine.** The 7.5S owner's manual specifies a **Sinpro HPU32A-105** 30 W
adapter, **12 VDC, 2.74 A**, with a 2MOPP medical rating
(`spirit-climber-specs-twelve-volt-dc-from-a-sinpro-supply`). The service manual for the same
machine, Dyaco's RS9600-SS021 book, draws on its wiring diagram a block captioned:

> Switching Power Supply - **90 ~ 260 VAC input** - **12 VDC output, 1.6A**

with a photograph of a desktop brick and a two-pin **Power** plug (Light Blue VIN 12V, Pink GND on
the cable; Red VIN, Black GND at the device). Its troubleshooting chapter checks "the A.C. outlet
has power (**90~240VAC**)" and "**12V DC at the DC plug of the adaptor**", then 12 V DC between
pins 10 and 11 of the console cable.

**What agrees and what does not.** The voltage is 12 V DC in both books and the input is a
universal mains range in both. The current does not agree - **1.6 A here, 2.74 A there** - and
the service manual names no maker, model or medical rating, while the owner's manual names all
three. The service manual's own two mains figures also differ (90-260 VAC on the diagram,
90-240 VAC in the text).

**Order the adapter from the owner's manual.** A 1.6 A supply is below the owner's-manual rating,
and the 2MOPP isolation the owner's manual specifies is a patient-safety requirement the service
manual's generic block does not carry. The service manual is evidence that the machine runs on
12 V DC and where to meter it; it is not the part specification.

The 8.5S is different again - a 24 V Mean Well module inside the machine
(`85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v`). The 7.5S has no user-replaceable
fuse (`spirit-climber-specs-fuse-rating`).

**The 7.0S and the 2025 7.5S service manuals print the identical block and the identical No power
procedure** - 90~240VAC at the outlet, 12V DC at the adaptor's plug, then pins 10 and 11 of the
14-pin console cable. The 7.0S owner's manual, like the 7.5S's, specifies the 12 V Sinpro adapter;
order from that, not from the 1.6 A block.

