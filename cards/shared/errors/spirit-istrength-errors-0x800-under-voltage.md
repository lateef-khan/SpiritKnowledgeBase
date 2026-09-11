---
id: spirit-istrength-errors-0x800-under-voltage
title: '0x800: Under-voltage on the digital resistance module'
kind: troubleshooting
question: What does fault code 0x800 mean on the Spirit i-Strength digital resistance
  module?
asked_as:
- what does 0x800 mean on my spirit strength machine
- i-strength module fault 0x800
- under-voltage on the resistance module
keywords:
- '0x800'
- under-voltage
- fault code
- hex code
- digital resistance module
- i-strength
- resistance box
- bit flag
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: errors
  code: '0x800'
authority: 3
not_to_be_confused_with:
- spirit-istrength-errors-0x80-fo-error-during-operation
- spirit-istrength-errors-0x80000-encoder-value-large-jump
- spirit-istrength-errors-0x800000-sampling-current-offset-calculation-error
see_also:
- spirit-istrength-errors-fault-code-checklist-twelve-bit-flag-codes
- srvo-error-0x800-low-voltage
source:
  ref: spirit-strength-i-strength-resistance-module-maintenance-manual
  locator: Chapter 7. Troubleshooting Checklist, PDF p. 26; text.md lines 661-711.
    The Fault Code column wraps each long code over two lines in the extraction (0x4000
    / 0 for 0x40000, and so on); the codes were read from a 200 dpi render of the
    page
  extracted_at: '2026-09-11'
---

**This is `0x800`, and it is not `0x80`, `0x80000`, `0x800000` - the same digit with a different number of zeroes, each a different fault.** Count the zeroes before you act.

| Fault Code | Fault Name | Possible Causes | Recommended Actions |
|---|---|---|---|
| `0x800` | Under-voltage | Insufficient input voltage to the drive | Power off and check input power connections. |

**This is the Digital Resistance Module's own code list** - the motorised resistance box that the CSI-CPSP and CSI-LROW owner's manuals list as part 72 - printed in the module's maintenance manual, not in either owner's manual. Neither owner's manual prints a code of any kind (`spirit-strength-errors-no-troubleshooting-page-printed`). **The manual does not say where the code is displayed**; the module carries a 10.1-inch touchscreen and the code is presumably shown there, but no screen, log or app page is named.

Every code in the list is a single bit of a hexadecimal word, which is why they run 0x40, 0x80, 0x100, 0x400 rather than counting up. The whole list is on `spirit-istrength-errors-fault-code-checklist-twelve-bit-flag-codes`.

Sole's SRVO resistance unit prints the same twelve codes, worded differently, in its own service manual: `srvo-error-0x800-low-voltage` is this code's Sole twin. That card describes a different brand's product and is linked for comparison only.
