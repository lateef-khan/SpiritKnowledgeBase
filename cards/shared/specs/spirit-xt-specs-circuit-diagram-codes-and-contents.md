---
id: spirit-xt-specs-circuit-diagram-codes-and-contents
title: The schematic sheet codes of every XT service manual, their voltage variants,
  and what each sheet draws
kind: spec
question: Which circuit diagram sheet belongs to which Spirit XT treadmill service
  manual, and what does each draw?
asked_as:
- what is the schematic number for the xt385
- wiring diagram for the xt485 2023
- is there a 220 volt circuit diagram for the xt185
- xt685 ent schematic
keywords:
- circuit diagram
- schematic
- wiring diagram
- sheet code
- cegs
- 220v
- 110v
- filter
- choke
- computer cable
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct800-2020-specs-circuit-diagram
- spirit-xt-2007-specs-controller-and-wiring-diagram
see_also:
- spirit-xt-specs-console-cable-6-pin-pinout
- spirit-xt-ent-specs-console-cable-5-pin-pinout
- spirit-xt-specs-electrical-part-descriptions
- spirit-dc-treadmill-specs-unit-block-diagram
- spirit-xt-assembly-breaker-replacement
source:
  ref: spirit-treadmill-xt385-2015-service-manual
  locator: XT185-2015 PDF pp. 57-58 (text.md line 1081; render); XT285-2015 pp. 58-59
    (line 1151; OCR lines 2680, 2746); XT385-2015 p. 58 (line 894; render) and the
    CEGS sheet on p. 4; XT485-2015 p. 59 (line 905); XT185-2023 pp. 32-33 (line 659;
    OCR 1880-1982); XT285-2023 pp. 33-34 (line 661); XT385-2023 p. 34 (line 598; render);
    XT485-2023 p. 34; XT685-2023 p. 33 (line 664; render); XT485ENT p. 57 (line 856;
    render); XT685ENT p. 37 (line 626; render). All are flat drawings
  extracted_at: '2026-09-11'
---

| Machine | Sheet code | Where | Variants |
|---|---|---|---|
| XT185-2015 | **XT125-YT024** | pp. 57-58 | 110V sheet, then 220V CEGS sheet |
| XT285-2015 | **XT135-YT025** | pp. 58-59 | 220V CEGS sheet and 110V sheet |
| XT385-2015 | **XT625-YT022** | p. 58, and a CEGS sheet as the section 1 opener on p. 4 | - |
| XT485-2015 | **XT625-YT023** | p. 59 | - |
| XT185-2023 | **XT126-YT072** | pp. 32-33 | 110V, then CEGS with "CE PARTS: FILTER, CHOKE" |
| XT285-2023 | **XT136-YT073** | pp. 33-34 | same pair |
| XT385-2023 | **XT626-YT074** | p. 34 | - |
| XT485-2023 | **XT626-YT075** | p. 34 | - |
| XT685-2023 | **XT816-YT076** | p. 33 | - |
| XT485ENT | **#XT625-NT042** | p. 57 | - |
| XT685ENT | **#XT816-NT052** | p. 37 | - |

**What the sheets draw.** All of them: the console; the computer cable in three lengths (UPPER / MIDDLE /
LOWER, 6-pin on the non-ENT machines, 5-pin on the ENT); INPUT POWER plug, connector, INLET, BREAKER and
On/Off SWITCH wired black / white; a FILTER (and, on the CEGS sheets, a CHOKE); the CONTROLLER with its L
/ N (ENT: ACL / ACN), the 3-pin VR cable, UP red / COM white / DOWN black to the INCLINE MOTOR, M+ red and
M- white-or-black to the DC MOTOR; grounding wires to the main and base frames.

**Sheet-by-sheet differences.** The XT185-2015 and XT385-2015 sheets print a 6-pin colour table (the
XT185's names the controller plugs JK60, JK90, JK50 and the DOWN / UP / COM block; the XT385's names JK51
for the speed sensor and JK90 for the cable). The 2023 XT185 / XT285 sheets repeat the colour table; the
2023 XT385 / XT485 / XT685 sheets have no table and name only JK51 SPEED SENSOR and JK90. The XT685-2023
sheet adds the AC FAN on FAN121 / FAN120 and **draws one incline motor although the book describes a
decline motor**. The ENT sheets print the 5-pin table, JK11, and **no speed sensor**.

No XT sheet prints a breaker rating, motor model, fan voltage or cable length; the CT sheets do.
