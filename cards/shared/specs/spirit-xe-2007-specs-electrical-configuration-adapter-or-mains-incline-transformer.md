---
id: spirit-xe-2007-specs-electrical-configuration-adapter-or-mains-incline-transformer
title: The three entry ellipticals of the 2007 dealer manual run from a plug-in adapter
  and the two incline ellipticals from a power cord, with an incline transformer 006096
  and an ALT-670100A incline controller
kind: fact
question: How are the 2007 Spirit XE100 to XE500 ellipticals powered, and which of
  them have an incline controller?
asked_as:
- does the xe300 use an adapter or a power cord
- xe500 incline transformer part
- which 2007 spirit ellipticals plug into the wall
- xe400 power supply
keywords:
- adapter
- power cord
- transformer
- 006096
- incline controller
- alt-670100a
- 9vdc
- 12vdc
- power supply
- electrical configuration
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe100-2007
  - xe200-2007
  - xe300-2007
  - xe400-2007
  - xe500-2007
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xe400-xe500-2007-specs-wiring-schematic
- spirit-xe400-xe500-2007-specs-incline-controller-alt-670100a-wiring
- spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3
- xe400-2007-specs-parts-list
- spirit-xe-specs-which-machines-have-a-power-incline
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: Repair Procedures, PROCEDURE 2 (adapter and harness), PDF p. 5, text.md
    lines 136-170; PROCEDURE 6 (incline controller) PDF p. 7, lines 202-243; XE400/XE500
    schematic PDF p. 9, lines 294-300; parts lists PDF p. 16 line 843, p. 20 line
    1029, p. 25 line 1409, pp. 30-37 lines 1073-1427 (Adaptor 1.5 Amp; 9V,DV,2.0A_Adaptor;
    Power Cord, Incline Adaptor (Transformer) 006096, Incline Controller ALT#670100A)
  extracted_at: '2026-09-11'
---

The dealer manual never prints an electrical-configuration page; the split falls out of its
procedures and parts lists.

| Machines | Supply | Incline |
|---|---|---|
| **XE100, XE200** | plug-in **Adaptor, 1.5 Amp** into the console's DC jack | none |
| **XE300** | plug-in **9 V DC, 2.0 A adaptor** | none |
| **XE400, XE500** | **Power Cord** into a fused inlet; an **Incline Adaptor (Transformer), 006096**, feeds the **Incline Controller ALT#670100A**, which powers the console through the main harness | powered, JS-15A motor |

Procedure 2 says the adapter is **labelled 9 VDC or 12 VDC** and reads "a few volts higher" when
metered unloaded, and that the console harness carries its power on **pins 1 and 3**, pin 1 marked
by a triangle on the connector (`spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3`).
The manual does not say which adapter voltage goes with which of the three adapter machines
beyond the XE300's parts-list line.

The incline machines' wiring is on `spirit-xe400-xe500-2007-specs-wiring-schematic` and the
controller's sockets on `spirit-xe400-xe500-2007-specs-incline-controller-alt-670100a-wiring`.
Part numbers for the adapters, cord and transformer are the parts cards' (`xe400-2007-specs-parts-list`
and its siblings).

