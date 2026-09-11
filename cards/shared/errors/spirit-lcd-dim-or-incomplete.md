---
id: spirit-lcd-dim-or-incomplete
title: The display backlight is dim, incomplete or imperfect
kind: troubleshooting
question: Why is the display dim or incomplete on a Spirit CT800-2016 or CT850-2016
  treadmill, CE850-2024 elliptical, CRS800S-2024 stepper or CVC800 climber?
asked_as:
- treadmill screen is dim
- display half lit on my spirit machine
- console backlight is faint
keywords:
- lcd
- dim display
- incomplete
- backlight
- power to console
- lower controller
- ac power
- faint
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce850-2024
  - crs800s-2024
  - ct800-2016
  - ct850-2016
  - cvc800
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-lcd-displays-dim-or-incomplete
- ct850-2020-led-dim-or-incomplete
see_also:
- spirit-lcd-displays-dim-or-incomplete
- ct850-2020-led-dim-or-incomplete
- ce800ent-tft-touch-panel-not-bright
- cu900ent-tft-not-bright
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Troubleshooting procedure matrix: CT850 2016 section 8.3 page 50; CVC800
    section 8-5 page 34; CT800 2016 service manual 8.4 Troubleshooting procedure matrix,
    PDF p. 56-59 (printed 55-58), text.md lines 1076-1215'
  extracted_at: '2026-09-08'
---

The CT850 2016 and CVC800 manuals print this row with the same causes, the same fixes and the same
voltage.

| Reason | Solve |
|---|---|
| LCD light is broken | Replace with new LCD or console |
| Power to console too low | Check AC power is 110-120V. Check power to console. Replace lower controller. |

The CVC800 manual writes the voltage as `110~120V`; the CT850 2016 manual writes it as `110-120V`.
Same figure.

**The CT850 2020 manual prints the same row about an LED rather than an LCD, and asks for 120V**:
see `ct850-2020-led-dim-or-incomplete`. The CE800ENT and CU900ENT manuals print a TFT version with
different causes again: `ce800ent-tft-touch-panel-not-bright` and `cu900ent-tft-not-bright`.

Dead segments rather than a dim backlight are the next row down:
`spirit-lcd-displays-dim-or-incomplete`.

**Two of the 2024 New Black machines print this row with the same causes, the same fixes and the
same 110-120V figure** - the CE850 2024 elliptical, on its printed page 38, and the CRS800S 2024
semi-recumbent stepper, on its printed page 35. Both pages are flat pictures with no text layer and
were read from the rendered page. The CRS800S 2024 writes the figure `110~120V` as the CVC800 does;
the CE850 2024 writes `110-120V` as the CT850 2016 does. Same figure.

**The CE850 2024 calls the display an LED**, not an LCD - `LED not bright, incomplete or imperfect`
and `Replace with new LED or console`. The figure and the four-step fix are otherwise identical, so
it belongs here rather than with the CT850 2020's LED version, which asks for **120V**
(`ct850-2020-led-dim-or-incomplete`). The noun changed; the number did not.

**Three other 2024 machines answer this same symptom with a different figure or none at all.** The
CE800 2024, CR800 2024 and CU800 2024 send the reader to the generator rather than to the wall
(`spirit-2024-errors-leds-not-bright-generator-power-connection`); the CS800 2024 stepper asks for
`220-240V or 110-120V` (`cs800-2024-errors-lcd-not-bright-220-240-or-110-120-volt`); the CRW800
2024 rower asks for `AC100 ~ 240V` in and `DC12V` out
(`crw800-2024-errors-lcd-display-does-not-shine`).

**The CT800 2016 service manual prints this row word for word**, `LCDs not bright, incomplete or imperfect`, the same two causes and `Check AC power is 110-120V`. The XT service manuals print the row without a voltage (`spirit-xt-errors-lcd-not-bright-connector-then-power`) or with 110V or 230V (`spirit-xt-2015-errors-lcd-not-bright-110-v-or-230-v`).
