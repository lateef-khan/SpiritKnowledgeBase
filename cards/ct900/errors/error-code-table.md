---
id: ct900-error-code-table
title: Which fault and warning codes this machine can show, and where each is printed
kind: fact
question: What error codes can a Spirit ct900 treadmill display?
asked_as:
- what error codes does this treadmill have
- list of fault codes for the ct900
- where do i find the error code table
- what do the inverter warning codes mean
keywords:
- error codes
- fault codes
- warning codes
- inverter
- vfd-tm
- ac motor drive
- code table
- index
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900
  applies_to:
  - ct900
  section: errors
  code: '*'
  model_number:
  - '900825'
authority: 3
not_to_be_confused_with:
- ctsbs900-troubleshooting-common-problems
- 70t-2026-errors-error-code-table
see_also:
- ct900-electrical-power-requirements
- ct900-errors-incline-e33-no-vr-change-during-incline-action
source:
  ref: spirit-treadmill-ct900-owners-manual
  locator: printed pages 42-49, ERROR CODES and ERROR CODES - AC MOTOR DRIVE INVERTER;
    CT900 service manual Error code items, PDF p. 29-30, text.md lines 366-426; CT900
    service manual AC MOTOR DRIVER INVERTER VFD-TM Error and Warning Codes, List of
    Error Codes, PDF p. 40-43, text.md lines 579-841; CT900 service manual List of
    Warning Codes, PDF p. 44-45, text.md lines 841-947
  extracted_at: '2026-09-09'
---

**This machine is the exception among Spirit commercial treadmills: its owner's
manual carries a full inverter code table.** No CT800 or CT850 owner's manual does —
those print only `LS`. The CTSBS900 has a table but a completely different family
(`LE1`, `NTCF`, `OC`, `OE`, `GF`, `OH`, `OL`, `LF`, `DBUP`, `PRER`, `EER`, `LP`,
`ESP`, `HT`), and the CT900ENT owner's manual has no error-code section at all.

Three families are printed, each with its own card:

- **Fault codes `E1`-`E34`** (`E15` is not printed). Inverter and console faults —
  over current, over voltage, IGBT over temp, motor overload, EEPROM errors,
  communication timeouts, incline errors.
- **Communication warnings `cE1`-`cE4` and `cE10`**, plus `AuE`, `SE1`, `SE2`,
  `ocSt`, `oL2`, `oSL`, `oSP`, `PGEr`, `tHL`, `toH`, `LC`. Press RESET to clear a
  warning code.
- **Incline codes `Inc1`, `Inc2`, `Inc3`** and the plain-language `Stop` row.

**Provenance, because it matters here.** These pages are printed as images; a text
extraction of the PDF returns them blank. They were recovered by rendering the source
PDF at 300 dpi and reading it with `tesseract --psm 4`. **50 of the 52 codes the
knowledge base holds for this machine were confirmed word-for-word against that
recovered text.**

**Two codes were not found in this owner's manual** and rest on another source:
`E34` (console EEPROM error) and `oSL` (over-slip warning). Treat those two as less
firmly attested than the rest, and check a service manual before quoting them.

The manual also defers twice, at `E31` and `E32`, to the **VFD-TM Error and Warning
codes** table of the AC motor drive inverter, which it does not reproduce.

**The service manual prints all three families and, unlike the owner's manual, the VFD-TM fault table itself** - thirty-one faults numbered 1 to 32 with 15 missing, each with the inverter keypad's mnemonic, a description and corrective actions; every `E` card now carries its row under *Service manual remedy*. It also prints `E34 CONSOLE EEPROM ERROR - Replace the console`, so the two codes recorded above as unconfirmed are confirmed for E34 and, for `oSL`, confirmed as warning #12 with two corrective actions. The service manual's `E33` gets two full sections of its own (`ct900-e33-incline-err`, `ct900-errors-incline-e33-no-vr-change-during-incline-action`).
