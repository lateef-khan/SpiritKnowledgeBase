---
id: spirit-mt200-errors-error-code-table
title: The 40 error messages, with the incline and decline faults numbered rather
  than named
kind: fact
question: What is the full list of error codes a Spirit MT200 treadmill can display?
asked_as:
- list of error codes for my treadmill
- what are all the e numbers on the display
- where do i find the error code table
- medical treadmill error code chart
keywords:
- error codes
- error code table
- fault codes
- e numbers
- troubleshooting chart
- console messages
- drive faults
- inverter faults
- medical treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - mt200-2010
  - mt200-2022
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-error-code-table
- ct900-e1-over-current
- ct850-2020-inverter-error-code-list
- ct850-2016-error-code-items-list
- cu900ent-error-code-messages-list
see_also:
- spirit-mt200-errors-e41-incline-err
- spirit-mt200-errors-e42-decline-err
- 70t-2026-errors-e1-over-current
source:
  ref: spirit-treadmill-mt200-2010-owners-manual
  locator: '"Error Codes, Messages and Solution/Cause", printed page 41, text.md lines
    1496-1541; the same table is "Error codes, messages and solution/cause" on printed
    pages 65-66 of the 2022 manual, text.md lines 2453-2522; 7.0T (MT200 2022) service
    manual 4.2.3 Error Codes: Messages, Cause and Solution, PDF p. 12-17, text.md
    lines 208-385; spirit-treadmill-mt200-error-codes-list, Error Codes List MT200
    - English, text.md lines 3-165 (a one-page 2024 leaflet)'
  extracted_at: '2026-09-09'
---

This is the index to the table. **Each code has its own card** - go to the card for the code
you are looking at, because several of these numbers mean something completely different on
other Spirit treadmills.

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
| E29 | I Signl Stop | Reset Power; Bad Drive |
| E30 | CPU Error | Electronic circuit fault |
| E31 | Fan | Drive Fan Bad |
| E32 | Analog In | Check Wiring; Bad Drive |
| E33 | Over Trque | Mechanical; Deck Lube; Brake; Bad Motor; Bad Drive |
| E34 | Thrm Ovrld 2 | Brake locked; Deck Lube; Bad Drive; Bad Motor |
| E35 | Motor Sel | Motor Wiring |
| E36 | LV Bus Run | Check AC Line V; Bad Drive |
| E37 | LV Bus | Check AC Line V; Bad Drive |
| E38 | Ext BB | Para Settings |
| E41 | Incline Err | none printed |
| E42 | Decline Err | none printed |

**The numbering has a gap.** The list runs E1 to E38 without a break, then jumps to E41 and
E42. Neither manual says what E39 or E40 would be, or whether they exist.

**Both MT200 manuals print this table identically** - the 2010 revision, effective July
2013, and the 2022 revision. Every code, every name and every cause is word for word the
same in the two, in the same order. Only the page layout differs: the 2010 manual sets it in
three columns on one page, the 2022 manual in three columns across two pages.

`Over Trque` (E33), `EPROM` (E12, E13) and `Thrm Ovrld 2` (E34) are the manual's own
spellings. The 2010 manual prints two rows without a space between the code and the name,
`E35Motor Sel` and `E37LV Bus`; the 2022 manual breaks `E35` onto its own line above
`Motor Sel`. They are the same two codes either way.

The table gives no description, no test procedure and no part number for any code - only the
name and the short cause or remedy words above.

**Do not read this table as the 7.0T's.** The Spirit 7.0T 2026 prints the same E1-E38 rows
with the same causes, but ends its table with two *unnumbered* messages, `ERR Incline Err`
and `ER2 Decline Err`, each marked "(Shows in Grade window)"
(`70t-2026-errors-error-code-table`). The MT200 numbers those two faults E41 and E42 and
prints no window note. Every other Spirit treadmill in this repository uses a different
family again - a CT900 E3 is IGBT Over Temp, where an MT200 E3 is Over V Decel.

**The 7.0T service manual prints the same forty codes with a description and numbered steps for each**, under 4.2.3 *Error Codes: Messages, Cause and Solution*; every code card now carries its row under *Service manual remedy*. It skips E39 and E40 exactly as the owner's manuals do.

**The 2024 MT200 error-codes leaflet prints the same forty codes with one line each** - and three of its names differ from the manuals': `E24 RS-485 Error` (manuals: PU Comm), `E38 External Brake` (manuals: Ext BB) and **`E42 Bad communication Error`** with a cable-inverter-console remedy, where every manual says `E42 Decline Err` (`spirit-mt200-errors-e42-decline-err`).
