---
id: cu900ent-error-code-log
title: Reading and clearing the error code log
kind: procedure
question: Where do I find the logged error codes on a Spirit CU900ENT, CR900ENT-2021
  or CU1000ENT-2023 bike, a CT900ENT or CT1000ENT-2023 treadmill, or a CE900ENT or
  CE1000ENT-2023 elliptical?
asked_as:
- where is the error log on my spirit bike
- how to clear the error log on the console
- diagnostics screen on a cu900
keywords:
- error code log
- diagnostics
- engineering mode
- clear errors
- fault history
- console
- technician
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce1000ent-2023
  - ce900ent
  - cr900ent-2021
  - ct1000ent-2023
  - ct900ent
  - cu1000ent-2023
  - cu900ent
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-error-code-messages-list
- cu900ent-eah-ucb-does-not-match-lcb-device
- ce800ent-error-code-log
- ct900ent-errors-error-code-messages-list
- ct1000ent-2023-errors-error-code-list-25-hex-codes
- cu1000ent-2023-errors-error-code-list-four-driver-board-codes
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Diagnostics, page 27. This page is a flattened image and was read from
    raw/page-27.png, not from the OCR text; CT900ENT service manual Error Code Log
    under Setting and Operation for Engineering Mode, PDF p. 29, text.md lines 443-453;
    CT1000ENT 2023 service manual Service table, Error Code Log row, PDF p. 19, text.md
    lines 428-473; CR900ENT 2021 service manual Diagnostics / Error Code Log, the
    screen read from the render, PDF p. 26-27, text.md lines 330-362; CU1000ENT 2023
    service manual Service table, Error Code Log row, a picture read from the render,
    PDF p. 16, text.md lines 287-296; CE900ENT service manual Diagnostics / Error
    Code Log, the screen read from the render, PDF p. 28, text.md lines 429-446; CE1000ENT
    2023 service manual Service table, Error Code Log row, a picture read from the
    render, PDF p. 16, text.md lines 313-319
  extracted_at: '2026-09-08'
---

**Diagnostics** in engineering mode holds the console's fault history.

> Diagnose and save malfunction error messages for technician to inspect the machine and
> troubleshooting.
> Press "Error Code Log" button 10 consecutive repetitions to clear the error message.

So: **press the `Error Code Log` button ten times in a row to clear the log.** When it is empty the
screen shows a `Deleted All Error Log` button.

Each logged line carries a code, a description and a timestamp. The worked example in the manual
reads `0xea  UCB No Match LCB Device  2015-12-16 11:04:14`.

Two things to note.

- The log writes codes as `0x` values, while the error code table writes the same code as `EAH`.
  They are the same code.
- The log spells the entry `No Match`, which confirms that `Is Not Math` in the code table is a
  misprint.

To reach engineering mode, press the `Home` button ten times in a row. Diagnostics is the third
entry in the Settings list.

The CE800ENT elliptical has the same console family and the same Diagnostics screen, but its manual
does not print the ten-press clearing instruction: `ce800ent-error-code-log`.

**The CT900ENT and CT1000ENT 2023 treadmill service manuals print the same two sentences** - *Diagnose and save malfunction error messages for technician to inspect the machine and troubleshooting. Press "Error Code Log" button 10 consecutive repetitions to clear the error message.* The CT1000ENT prints them in its engineering-mode Service table; the CT900ENT on a page of its own. Neither prints a worked example, so the `0x` log format above is the bike's page. The codes those logs hold are the treadmill lists on `ct900ent-errors-error-code-messages-list` and `ct1000ent-2023-errors-error-code-list-25-hex-codes`, both of which also write their codes as hex.

**The CR900ENT 2021 recumbent service manual prints the same Diagnostics page** - the two sentences above and the same `Error Code Log` screen, reached the same way, ten presses on `Home`. **The CU1000ENT 2023 upright prints the two sentences in its engineering-mode Service table**, beside the key, NFC, communication, brake and sensor tests, and its engineering mode is entered with ten presses on `Welcome` rather than `Home`. The codes the CU1000ENT's log can hold are its own driver-board list, `0xB0` to `0xB3` (`cu1000ent-2023-errors-error-code-list-four-driver-board-codes`), which the console already writes in `0x` form.

**The CE900ENT elliptical service manual prints the same Diagnostics page** - the two sentences above and the same `Error Code Log` screen under `Settings > Engineering Mode > Diagnostics`, engineering mode entered with ten presses on `Home`. **The CE1000ENT 2023 elliptical prints the two sentences in its engineering-mode Service table** beside Key Test, NFC Test, Brake Test and Sensor Tests, its engineering mode entered with ten presses on `Welcome`; the codes its log can hold are the four driver-board codes `0xB0` to `0xB3` (`cu1000ent-2023-errors-error-code-list-four-driver-board-codes`).
