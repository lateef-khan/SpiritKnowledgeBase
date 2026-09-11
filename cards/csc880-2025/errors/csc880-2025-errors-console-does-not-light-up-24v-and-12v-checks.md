---
id: csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
title: The console does not light after power on, and the chain is 24 V out of the
  adapter then 12 V out of the controller
kind: troubleshooting
question: What do I check when the console of a Spirit CSC880-2025 stair climber does
  not light up after the power is turned on?
asked_as:
- my stair climber console is dead
- csc880 screen wont turn on
- stair climber has power but no display
- nothing lights up on my spirit stair climber
keywords:
- console does not light
- no display
- dead console
- power adapter
- controller
- 24v
- 12v
- indicator light
- wiring harness
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: no-display
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-console-does-not-light-up-after-power-on
- cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt
- cvc800-screen-does-not-light
see_also:
- csc880-2025-errors-error-code-table
- csc900-2024-errors-console-does-not-light-up-after-power-on
- csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, row 9 of the No./Problem/Causes/Solution table,
    printed page 34 (PDF page 36), read from the native text layer and confirmed against
    a 400 dpi render; CSC880 service manual (Magnetic), 5. Troubleshooting, "CSC880
    electrical malfunction Troubleshooting" table row 9, PDF p. 8 - the page is a
    flat picture (text.md lines 123-128 hold only the heading; OCR supplement lines
    428-505) and was read from a 200 dpi render
  extracted_at: '2026-09-10'
---

**Problem:** After turning on the power, the console does not light up.

**Causes named, in the manual's order:** 1. Power adapter failure. 2. Controller failure.
3. Connection cable failure. 4. Console failure.

> Use a multimeter to measure and check problems one by one.
>
> 1. Check whether the indicator light on the adapter is on and measure whether there is a
>    **DC 24V** output.
> 2. Check whether the indicator light on the controller is on and measure whether there is a
>    **DC 12V** output.
> 3. Measure whether there is a **DC 12V** output at the terminals of the wiring harness connected
>    to the console.

**Three measurements for four causes.** The console is the fourth cause and gets no measurement - it
is what is left when the other three pass.

**The voltage steps down inside the machine: 24 V from the adapter, 12 V from the controller
onwards.** Measuring 24 V at the console end is as wrong an answer as measuring nothing.

**Two indicator lights are part of the test** - one on the adapter, one on the controller - and each
is checked before its voltage. A dark indicator narrows the fault without a meter.

**These are not the same figures the CSC900 2024 book prints for the same symptom.** That machine's
row reads 24 V at the adapter and 24 V *into the lower control*, with no 12 V anywhere
(`csc900-2024-errors-console-does-not-light-up-after-power-on`). The two are separate cards because
the numbers differ; quoting one at the other machine sends a technician looking for a voltage that
is not supposed to be there.

**This machine runs from an external DC adapter, not from a mains supply into the frame.** Do not
carry the 110-120 V or 220-240 V checks written for the mains-powered Spirit consoles onto it.

If the screen lights but a key does nothing, that is the membrane keypad row instead:
`csc900-2024-errors-membrane-key-failure`.

**The CSC880 service manual prints this row word for word**, as row 9 of the eleven-row table on its page 8. Owner's manual and service manual carry the same table; the service manual adds nothing to this row.
