---
id: spirit-istrength-errors-fault-code-checklist-twelve-bit-flag-codes
title: 'Every fault code the digital resistance module can report: twelve bit-flag
  hex codes from the power module to a motor overload'
kind: spec
question: What fault codes can the Spirit i-Strength digital resistance module report
  and what does each one mean?
asked_as:
- i-strength error code list
- spirit strength machine fault codes
- csi resistance module hex codes
- what do the 0x codes mean on the i-strength
keywords:
- fault code
- error code table
- hex code
- bit flag
- digital resistance module
- i-strength
- troubleshooting checklist
- list
- index
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- srvo-error-code-table
- cu1000ent-2023-errors-error-code-list-four-driver-board-codes
- ct1000ent-2023-errors-error-code-list-25-hex-codes
see_also:
- spirit-istrength-errors-0x40-ipm-fo-signal-stuck-low
- spirit-istrength-errors-0x80-fo-error-during-operation
- spirit-istrength-errors-0x100-ipm-over-temperature-alarm
- spirit-istrength-errors-0x400-over-voltage
- spirit-istrength-errors-0x800-under-voltage
- spirit-istrength-errors-0x40000-encoder-offset-error
- spirit-istrength-errors-0x80000-encoder-value-large-jump
- spirit-istrength-errors-0x400000-encoder-not-wired
- spirit-istrength-errors-0x800000-sampling-current-offset-calculation-error
- spirit-istrength-errors-0x4000000-uvw-wiring-error
- spirit-istrength-errors-0x10000000-regenerative-braking-overload
- spirit-istrength-errors-0x40000000-motor-overload
- spirit-strength-errors-no-troubleshooting-page-printed
- spirit-strength-errors-resistance-box-cable-jam-over-8-kg
- srvo-error-code-table
source:
  ref: spirit-strength-i-strength-resistance-module-maintenance-manual
  locator: Chapter 7. Troubleshooting Checklist, PDF p. 26; text.md lines 661-711.
    The Fault Code column wraps each long code over two lines in the extraction (0x4000
    / 0 for 0x40000, and so on); the codes were read from a 200 dpi render of the
    page
  extracted_at: '2026-09-11'
---

**The i-Strength owner's manuals print no code; the Digital Resistance Module's maintenance manual prints twelve.** They are the faults of the module's servo drive - the motor controller inside the resistance box the CSI-CPSP and CSI-LROW owner's manuals call part 72. Each code has its own card; this is the index.

| Fault Code | Fault Name | Possible Causes | Recommended Actions |
|---|---|---|---|
| `0x40` | IPM FO Signal Stuck Low | Power module failure or under-voltage | Restart the machine. If the fault persists, replace the module. |
| `0x80` | FO Error During Operation | Power module failure, under-voltage, or phase short-circuit | Power off, check input power and phase connections for integrity. Ensure no motor phase short-circuit. Replace module if fault recurs after reboot. |
| `0x100` | IPM Over-Temperature Alarm | Prolonged heavy load on power module or poor heat dissipation (loose module heat sink contact or failed fan) | Allow the system to cool down. If the fault persists, check fan connections. Replace module if fan is operational but fault recurs. |
| `0x400` | Over-voltage | Excessive input voltage to the drive | Power off and verify braking resistor connections. |
| `0x800` | Under-voltage | Insufficient input voltage to the drive | Power off and check input power connections. |
| `0x40000` | Encoder Offset Error | Encoder malfunction or poor contact | Power off and check encoder connections. |
| `0x80000` | Encoder Value Large Jump | Encoder malfunction or poor contact | Power off and check encoder connections. |
| `0x400000` | Encoder Not Wired | Encoder not connected or poor contact | Power off and check encoder connections. |
| `0x800000` | Sampling Current Offset Calculation Error | Drive phase current sampling circuit anomaly or unstable voltage at power-up | Restart the machine. If the fault persists, replace the drive. |
| `0x4000000` | UVW Wiring Error | Missing or loose motor phase connections | Power off and verify motor phase wiring. |
| `0x10000000` | Regenerative Braking Overload | Braking resistor overload | Restart and allow the braking resistor to cool down. Reduce load or extend cool-down time. |
| `0x40000000` | Motor Overload | Excessive motor load | Restart and allow the motor to cool-down. Reduce load or check mechanical constraints. |

**Three things to know before using the table.**

- **The codes are bits, and several differ only in the number of zeroes.** `0x40`, `0x400`, `0x40000`, `0x400000`, `0x4000000` and `0x40000000` are six faults; `0x80`, `0x800`, `0x80000` and `0x800000` are four; `0x100` and `0x10000000` are two. The manual's column is narrow enough that the long codes wrap over two lines in a text extraction (`0x4000` over `0`), which is how a reader ends up one zero short. Count them.
- **The manual does not say where a code is shown.** The module has a 10.1-inch Android touchscreen (the console specification chapter), but no screen, fault log or app page is named as the place the code appears, and nothing is said about two faults being reported together.
- **Five of the twelve end in a part.** The power module (`0x40`, `0x80`, `0x100`) and the drive (`0x800000`) are named for replacement; the disassembly chapter of the same manual takes out the controller module and the PFC module but prints no part number for either.

**What the controller protects against**, from its specification page: over-voltage, under-voltage, over-current, over-temperature, encoder fault, brake resistor fault, and a three-phase short of the motor during power loss - which is the list this table reports on.

**These are not the ENT consoles' hex codes.** The CU1000ENT and CE1000ENT bikes print `0xB0` to `0xB3` (`cu1000ent-2023-errors-error-code-list-four-driver-board-codes`) and the CT1000ENT treadmill `0x01` to `0x44` (`ct1000ent-2023-errors-error-code-list-25-hex-codes`); none of those is a bit-flag list and none overlaps this one.

**Sole's SRVO prints the same twelve codes with different wording** - `Power module low voltage` for `0x40`, `Braking control error` for `0x10000000` - in its own service manual (`srvo-error-code-table`). It is a different brand's unit; the per-code cards here link to its twins for comparison.

The only other fault either CSI owner's manual describes is a cable jammed in the resistance box by pulling it before assembly is complete (`spirit-strength-errors-resistance-box-cable-jam-over-8-kg`).
