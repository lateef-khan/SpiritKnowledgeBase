---
id: xterra-treadmill-specs-parts-display-board-part-numbers-on-the-pcb-stickers
title: Part numbers printed on the display-board stickers and silkscreens photographed
  in the service manuals
kind: fact
question: What part number, description and programming number are printed on the
  display board (upper control board) of an Xterra TR260, TRX1400, TRX2500, TRX3500,
  TRX4500, TRX5500, TR75H or TR95H treadmill?
asked_as:
- what is the part number of the xterra display board
- console board part number
- programming number on the pcb sticker
- which firmware is on my treadmill console
keywords:
- display board
- console board
- upper control board
- PCB
- part number
- programming number
- firmware
- sticker
- silkscreen
- A001010
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - tr75h-2025
  - tr95h-2024
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-treadmill-specs-parts-service-manual-outlines-and-electronic-parts-named
- xterra-treadmill-specs-parts-which-manuals-print-an-exploded-view-and-parts-list
- trx1400-2023-specs-parts-list-items-001-to-121
- trx5500-2024-specs-parts-list-items-1-to-188
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/4500 SM PDF p. 27 lines 398-404 and p. 30 lines 446-480; TR260
    SM p. 20 lines 307-313 (sticker also on p. 18); TRX1400 SM p. 28 lines 404-410;
    TRX2500 SM p. 24 lines 365-371; TRX5500 SM p. 25 lines 376-382; TR150 SM p. 25
    lines 313-319; TR75H SM p. 13 lines 264-286; TR95H SM p. 15 lines 193-209. All
    read from pdftoppm renders at 300-400 dpi, stickers cropped and rotated upright;
    the OCR supplements hold the TR260 and TRX3500/4500 stickers only partially.
  extracted_at: '2026-09-11'
---

The service manuals photograph the console's display board for their socket maps, and the board carries a factory sticker (*Part Number / Description / ProgrammingNumber / Speed*) and a silkscreen revision. **These are the only part numbers printed anywhere in the Xterra service manuals.** They were read from 300-400 dpi renders of the photographs, not from the text layer, and the illegible characters are marked.

| Machine (service manual) | Sticker: Customer Model / Part Number / Description / Programming Number / Speed / barcode | Silkscreen | Page |
|---|---|---|---|
| TR260 (GT75A-NT050) | Customer Model **GT75A-NT050** / Part Number **A001010728** / Description **INC-A3404J5** / ProgrammingNumber **A340401_C05A17V20_22071202.hex** / Speed **10km** / 04220719A00009 | A3404-V61 2020-04-15 | PDF p. 20 (printed 20), PCB Board Bottom |
| TRX1400 (T3-NT053-01) | 料號 (part number) **A0010101?1** - one digit hidden by a smudge - / 品名 (name) **INC-A0127H3** / 程式編號 (program) **T3_A0127_S309_80424.hex** / 04210301A00021 | A0127-V14 2017-01-03 | PDF p. 28 (printed 26), PCB Board Bottom |
| TRX2500 (GT90B-NT022) | Part Number **A001010420** / Description **INC-A0463A0** / ProgrammingNumber **CT80_A0463_S505_70529.hex** / Speed **16KM** / 04170623A001 | A0463_V11 2017-6-8 | PDF p. 24 (printed 23), PCB Board Bottom |
| TRX3500 (GT90C-NT023) | Part Number **A001010421** / Description **INC-A0464A0** / ProgrammingNumber **NT023_A0464_S102_70623.mot** / Speed **12KM** / 04170623A011 | A0464_V10 20170609 | PDF p. 27 (printed 26), PCB Board Bottom for GT90C-NT023 |
| TRX4500 (GT90D-NT024) | Part Number **A001010422** / Description **INC-A0465A0** / ProgrammingNumber **NT024_A0465_S102_70622.mot** / Speed **12KM** / 041706... (hidden by a call-out) | A0465_V10 20... (hidden by a call-out) | PDF p. 30 (printed 29), the socket map for GT90D-NT024 |
| TRX5500 (GT90D-NT041) | Customer Model **TRX5500** / Part Number **A0010106?4** / Description **INC-A8802F0?** / ProgrammingNumber **C006_TRX5500_1?0018 ... release 2020.11.13-12** - the photograph is too soft to read every character | - | PDF p. 25 (printed 24), 6-1-2 PCB BOARD BOTTOM |
| TR75H and TR95H (JKEXER) | a small label **JKM-337藍牙 AB / DPCB-3370000108 / P01-224043** on the board | **JKM-337-MB / JKM-655-MB / 2023-09-19_V1.3**, ASTEK logo | TR75H SM PDF p. 13, TR95H SM PDF p. 15, *Display board PCB sockets* - the same photograph in both books |
| TR150 (GT65-NT014) | no sticker in the photograph | A0439_V11 2014-4-22 | PDF p. 25 (printed 26), PCB Board Bottom |

**How to read a sticker.** *INC-Axxxx* is Dyaco's board description, *Part Number A00101xxxx* the orderable part, and *ProgrammingNumber* the firmware file flashed to it - so the TRX3500 and TRX4500 boards are two different part numbers (A001010421 / A001010422) carrying two different firmware files (`..._70623.mot` / `..._70622.mot`) on the same A046x hardware, which is why the two consoles in the shared service manual are photographed separately (`xterra-treadmill-specs-parts-service-manual-outlines-and-electronic-parts-named`). The *Speed* line is the firmware's top speed in km/h: 10 km on the TR260 board, 16 km on the TRX2500, 12 km on the TRX3500 and TRX4500. The TRX1400 sticker is in Chinese (料號 part number, 品名 name, 程式編號 program number) with the same three fields.

**The board photographed in the two JKEXER books is one board**: the TR75H manual re-uses the TR95H photograph, silkscreened JKM-337-MB (337 being the JKEXER number for the TR95H) with an alternative JKM-655-MB name, revision 2023-09-19 V1.3. Whether the TR75H's own board carries a different number the book does not say.

None of these numbers appears in an owner's-manual parts list, which name the board only as *Console Display Board* (`xterra-treadmill-specs-parts-which-manuals-print-an-exploded-view-and-parts-list`). The socket and wiring maps these photographs illustrate are on the wiring cards, not here.

