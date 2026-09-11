---
id: spirit-lcd-dim-or-incomplete
title: The display backlight is dim, incomplete or imperfect
kind: troubleshooting
question: Why is the display dim or incomplete on a Spirit CT800-2016 or CT850-2016
  treadmill, a CE850-2016, CE850-2020, CE850-2024, XE195-2016, XE295-2016, XE395-2016,
  XE395ENT-2021, XE895-2016 or XG400-2016 elliptical, CRS800S-2024 stepper, CVC800
  climber, or an XBR25-2016, XBR55-2016, XBU55-2016, XBR55ENT-2021 or XBU55ENT-2021
  bike?
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
  - ce850-2016
  - ce850-2020
  - ce850-2024
  - crs800s-2024
  - ct800-2016
  - ct850-2016
  - cvc800
  - xbr25-2016
  - xbr55-2016
  - xbr55ent-2021
  - xbu55-2016
  - xbu55ent-2021
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  - xg400-2016
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
- spirit-xb-2023-errors-lcd-not-bright-replace-generator-controller
- xbu55-2023-errors-lcd-not-bright-check-power-to-console
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Troubleshooting procedure matrix: CT850 2016 section 8.3 page 50; CVC800
    section 8-5 page 34; CT800 2016 service manual 8.4 Troubleshooting procedure matrix,
    PDF p. 56-59 (printed 55-58), text.md lines 1076-1215; XBR25 2016 service manual
    Troubleshooting procedure matrix, PDF p. 41, text.md lines 609-641; XBR55 2016
    service manual Troubleshooting procedure matrix, PDF p. 42, text.md lines 604-636;
    XBU55 2016 service manual Troubleshooting procedure matrix, PDF p. 41, text.md
    lines 608-640; XBR55ENT 2021 service manual Troubleshooting procedure matrix,
    PDF p. 33, text.md lines 416-445; XBU55ENT 2021 service manual Troubleshooting
    procedure matrix, PDF p. 33, text.md lines 412-442; CE850 2016 (XE898-SE011) service
    manual 8-7 Troubleshooting procedure matrix, PDF p. 56-57, text.md lines 973-1029;
    XE895 2016 (XE895-SE022) service manual 8-7 Troubleshooting procedure matrix,
    PDF p. 57-58, text.md lines 973-1029; CE850 (2020) service manual 8-7 Troubleshooting
    procedure matrix, PDF p. 49-50, text.md lines 852-909; XE195 2016 (XE509S-SE021-01)
    service manual Troubleshooting procedure matrix, PDF p. 42, text.md lines 652-685;
    XE295 2016 (XE519S-SE020-01) service manual Troubleshooting procedure matrix,
    PDF p. 42, text.md lines 653-686; XE395 2016 (XE539S-SE019-01) service manual
    Troubleshooting procedure matrix, PDF p. 57-58, text.md lines 966-1027; XE395ENT
    2021 (XE539S-SE025-01) service manual Troubleshooting procedure matrix, PDF p.
    46-47, text.md lines 656-709; XG400 2016 (SE551-SE023-01) service manual Troubleshooting
    procedure matrix, PDF p. 40, text.md lines 595-628'
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

**Five residential bike service manuals print this row word for word, `110-120V` included** - the XBR25 2016, XBR55 2016 and XBU55 2016, and the XBR55ENT 2021 and XBU55ENT 2021, whose matrices keep the LCD wording even though those two consoles are TFT touch panels. The XBR95 2016 of the same generation drops the voltage and is on `ce900-2025-errors-leds-not-bright-incomplete-or-imperfect`; the 2023 residential books replace the lower controller with a *generator controller* (`spirit-xb-2023-errors-lcd-not-bright-replace-generator-controller`) or stop before it (`xbu55-2023-errors-lcd-not-bright-check-power-to-console`).

**Eight elliptical service manuals print this row with the same two causes, the same four-step fix and `Check AC power is 110-120V`** - the CE850 2016 (XE898-SE011) and its residential twin the XE895 2016, the XE195, XE295, XE395 and XG400 2016, and the XE395ENT 2021, all about an LCD, and the CE850 (2020), which like the CE850 2024 says `LED not bright` and `Replace with new LED or console` around the same 110-120V figure. **The XE195 2016 alone adds a second figure**: its row reads `Check AC power is 110-120V. (or 220-230V)`, the only elliptical book of the eight to name the export voltage. The XE795 2016, XE795 2023 and CE900 drop the voltage (`ce900-2025-errors-leds-not-bright-incomplete-or-imperfect`); the CE800 2016 and CE800 (2020) send the reader to the generator (`spirit-2024-errors-leds-not-bright-generator-power-connection`); the CE900ENT and CE1000ENT 2023 print the TFT version (`cu900ent-tft-not-bright`).
