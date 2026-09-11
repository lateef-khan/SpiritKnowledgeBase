---
id: spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack
title: A 12 V 1.5 A adapter into a DC jack on the chain cover, with the tension motor
  passing 12 V on to the console
kind: spec
question: What power supply does a Spirit CRW800 (2016) or XRW600 rower use according
  to its service manual?
asked_as:
- what adapter does the xrw600 rower use
- power supply for the 2016 crw800
- is the spirit rower 12 volt
- where is the dc jack on the xrw600
keywords:
- power adapter
- ac adapter
- 12v
- 1.5a
- dc jack
- dc12v output
- ac100-240v
- dc power cord
- power supply
- console power
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - xrw600-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crw800-2021-specs-generator-controller-ae0076-connector-definition
- crw800-2024-specs-resistance-system
see_also:
- spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
- xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
- xrw600-console-no-power-source-is-named
source:
  ref: spirit-rower-crw800-2016-service-manual
  locator: 'CW800-YR001: circuit diagram adapter block ''12V/1.5A'' and DC JACK, PDF
    p. 35 (printed 34), read at 300 dpi; 8.2 E2 ''supply the console DC12V power'',
    PDF p. 32, text.md lines 415-433; 8.5 quick lookup ''AC power input is AC100 ~
    240V and the output is DC12V'' and ''Has the cable tensioner output DC12V'', PDF
    p. 38, lines 487-510; 8.6 ''the adapter is correctly inserted into the DC jack'',
    PDF p. 39, lines 511-537; 9-1 step 3 ''Remove the Nut of DC Power Cord'', PDF
    p. 43, lines 568-576. DW400-YR002 (XRW600): the same items at PDF pp. 35, 32,
    38, 39 and 43, lines 446, 406-424, 478-501, 502-529 and 544-553'
  extracted_at: '2026-09-11'
---

**These two rowers plug into a wall adapter; the 2020-version CRW800 does not**
(`crw800-2021-specs-generator-controller-ae0076-connector-definition`).

| | |
|---|---|
| Adapter | **12V/1.5A** on the circuit-diagram block; **AC100 ~ 240V** input, **DC12V** output on the troubleshooting page |
| Lands on | a **DC jack** held by a nut in the chain cover (the chain-cover procedure removes "the Nut of DC Power Cord" with a 15 mm wrench) |
| Then | the **tension motor**, which "supply the console DC12V power" |

**The console is fed through the motor, not from the jack.** Both books say so twice - in the E2
table ("Cable tensioner: receives the command signal from the console and actuation, supply the
console DC12V power") and in the no-display checks ("Has the cable tensioner output DC12V, if
not, please replace the new cable tensioner"). The XRW600 block diagram draws exactly that:
adapter -> motor -> J13 on the console
(`xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13`). A dead console with a good
adapter can therefore be a dead motor.

**No part number, plug type or wattage is printed** for the adapter, and no fuse. The owner's
manuals name no power source at all (`xrw600-console-no-power-source-is-named`); this figure
exists only in the service books.

**Not the batteries.** The CRW800's *Battery Cover (36~3)* in the same books belongs to the
handlebar controller with the RF module, not to the console.

