---
id: 70t-2026-errors-error-code-table
title: The 38 numbered error codes plus ERR and ER2, and the causes printed against
  each
kind: fact
question: What is the full list of error codes a Spirit 7.0T treadmill can display?
asked_as:
- list of error codes for my treadmill
- what are all the e numbers on the display
- where do i find the error code table
- treadmill error code chart
keywords:
- error codes
- error code table
- fault codes
- e numbers
- err
- er2
- troubleshooting chart
- console messages
- drive faults
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2025
  - 70t-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- ct900-e1-over-current
- ct850-2020-inverter-error-code-list
- ct850-2016-error-code-items-list
- cu900ent-error-code-messages-list
see_also:
- spirit-mt200-errors-error-code-table
- 70t-2026-errors-e1-over-current
- 70t-2026-errors-e29-i-signl-stop
- 70t-2026-errors-err-incline-err
- 70t-2026-errors-er2-decline-err
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    lines 1474-1505; 7.0T 2025 owner's manual (Rev 01.10.25, spirit-treadmill-70t-2025-owners-manual)
    prints the same table word for word, ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48
    (printed 46), text.md lines 1478-1513 (compared with difflib on 2026-09-11)
  extracted_at: '2026-09-09'
---

This is the index to the table. **Each code has its own card** - go to the card for the
code you are looking at, because several of these numbers mean something completely
different on other Spirit treadmills.

| Code | Name, as printed | Causes and remedies, in printed order |
|---|---|---|
| E1 | Over Current | Deck Lube; Bad Drive or Motor; Check Brake |
| E2 | Over Volt | Check AC line V |
| E3 | Over V Decel | Check AC line V; Check Brake |
| E4 | Ground Fault | Check wiring; Replace Drive |
| E5 | IGBT Fault | Check wiring; Replace Drive |
| E6 | Drive Ovrload | Deck Lube; Brake locked; Bad Drive; Bad Motor |
| E7 | Thrm Ovrload | Brake locked; Deck Lube; Bad Drive; Bad Motor |
| E8 | Over Torque | Brake locked; Deck Lube; Bad Drive; Bad Motor |
| E9 | Over I Speed | Check Brake; Deck Lube; Bad Drive; Bad Motor |
| E10 | Over I Accel | Deck Lube; Bad Drive; Bad Motor |
| E11 | Over I Decel | Deck Lube; Bad Drive; Bad Motor |
| E12 | EPROM RD | Check AC Line V; Reset Power; Bad Drive |
| E13 | EPROM WR | Check AC Line V; Reset Power; Bad Drive |
| E14 | Ext Fault | Reset Power |
| E15 | U Phase I | Reset Power; Bad Drive |
| E16 | W Phase I | Reset Power; Bad Drive |
| E17 | HW Fault | Reset Power; Bad Drive |
| E18 | IGBT O-Heat | Bad Drive Fan; Dirty Heat Sink |
| E19 | Ambient Temp | Air Vent Blocked; Bad Fan |
| E20 | Inrush Fault | Reset Power; Bad Drive |
| E21 | In Sig Lost | Check Wiring; Bad Drive |
| E22 | RS-485 Flt | Check Wiring |
| E23 | PID Error | Check Wiring; Chk Para Setting |
| E24 | PU Comm | Bad Drive |
| E25 | Auto Tune | Chk Motor wires; Reset Power |
| E26 | Bk Chopper | Reset Power; Bad Drive |
| E27 | PG Error | Check Motor |
| E28 | Phase Loss | Check Wiring; Bad Drive |
| E29 | I Signl Stop | Reset Power; Bad Drive (see the note below) |
| E30 | CPU Error | Electronic circuit fault |
| E31 | Fan | Drive Fan Bad |
| E32 | Analog In | Check Wiring; Bad Drive |
| E33 | Over Trque | Mechanical; Deck Lube; Brake; Bad Motor; Bad Drive |
| E34 | Thrm Ovrld 2 | Brake locked; Deck Lube; Bad Drive; Bad Motor |
| E35 | Motor Sel | Motor Wiring |
| E36 | LV Bus Run | Check AC Line V; Bad Drive |
| E37 | LV Bus | Check AC Line V; Bad Drive |
| E38 | Ext BB | Para Settings |
| ERR | Incline Err | none printed; shows in the Grade window |
| ER2 | Decline Err | none printed; shows in the Grade window |

The list runs E1 to E38 with no gaps. E37 is printed as `E37LV Bus`, with no space
between the code and the name. `Over Trque` (E33) and `EPROM` (E12, E13) are the
manual's own spellings.

**How this table was rebuilt.** The manual prints it in five narrow columns and the PDF
text extraction reads across all five, so a single extracted line such as
`E1 Over Current   Check Brake   Bad Drive Fan   E30 CPU Error   ERR Incline Err`
holds five fragments belonging to five different codes. Each column was read
top-to-bottom on its own; every column but the fourth begins with a code heading and
every column ends at a code's last cause, so the split is unambiguous.

**The one thing that was not, and what settled it.** The fourth column opens with a bare
`Bad Drive` line under no code heading, and the third column ends with `E29 I Signl Stop /
Reset Power`. From this manual alone that line could not be proved to belong to E29:

```
E29 I Signl Stop      <- column 3, second-to-last row
Reset Power           <- column 3, last row
Bad Drive             <- column 4, first row, no code heading
```

**Both Spirit MT200 owner's manuals print the same table in a different column layout, and
in them E29, `Reset Power` and `Bad Drive` are three consecutive rows inside one column with
no break between them.** `Bad Drive` is E29's second remedy. See
`spirit-mt200-errors-error-code-table` and `70t-2026-errors-e29-i-signl-stop`.

The table gives no description, no test procedure and no part number for any code - only
the name and the short cause or remedy words above.

**A Spirit machine that shares this table.** Both MT200 owner's manuals print E1 to E38 with
the same names and the same causes, in the same order. They differ only at the tail: the
MT200 numbers the incline and decline faults `E41` and `E42` where this manual prints `ERR`
and `ER2`, and it prints no Grade-window note (`spirit-mt200-errors-error-code-table`).

**The 7.0T 2025 owner's manual (Rev 01.10.25) prints the same table word for word**, so the list holds for the previous model year as well (added 2026-09-11).

