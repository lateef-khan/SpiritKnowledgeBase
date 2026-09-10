---
id: spirit-med-stepper-errors-programs-do-not-start-keypad-test
title: Console programs will not start, and a Key Test you cannot even reach is what
  proves the keypad dead
kind: troubleshooting
question: Why will the console programs not start on a Spirit recumbent stepper?
asked_as:
- my stepper wont start a program
- buttons do nothing on my spirit stepper
- stepper keypad not responding
- console lights up but nothing starts
keywords:
- programs do not start
- keypad
- key test
- membrane
- maintenance mode
- engineering mode
- unresponsive buttons
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-membrane-key-failure
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
see_also:
- spirit-med-stepper-errors-no-power-outlet-and-dc-wire
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- csc900-2024-errors-membrane-key-failure
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: 'Troubleshooting, "Console programs do not start", printed page 40 (PDF page
    42) of the 7.0S 2025 manual; the same text on printed page 42 (PDF page 44) of the
    7.5S 2025 manual and printed page 60 (PDF page 60) of the MS300 2021 manual, where
    the second bullet is missing from the text layer and was recovered from a 300 dpi
    render.'
  extracted_at: '2026-09-10'
---

The manual, word for word:

> - Perform Keypad test in Maintenance mode
> - If you cannot access the test, and the keys seem to have no affect when pressed, then the keypad
>   has malfunctioned.

**The diagnosis is the test being unreachable, not the test failing.** Maintenance mode is entered by
holding Start, Stop and Enter together, which is itself three key presses - so a keypad dead enough
to block that entry has already answered the question. If you get in and the Key Test runs, the
keypad is not the fault.

**The manual names no part number and no next step.** It stops at "the keypad has malfunctioned".

**The Maintenance / Engineering mode menu itself is carded under `section: console`**, with the entry
sequence and the full list of tests it holds. This card is only the fault use of it.

**On the MS300 2021 this bullet is invisible to a text extractor.** `pdftotext` returns the heading,
the first bullet and then jumps to the tail of the second one - "when pressed, then the keypad has
malfunctioned" - dropping "If you cannot access the test, and the keys seem to have no affect". The
printed page carries the whole sentence; it was read from a 300 dpi render. Anyone quoting the
extraction of that page is quoting a broken sentence.

The stair climbers answer the same symptom differently - a membrane keypad and its cable, with no
test mode at all (`csc900-2024-errors-membrane-key-failure`).
