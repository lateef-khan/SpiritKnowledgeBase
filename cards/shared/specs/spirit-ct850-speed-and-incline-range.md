---
id: spirit-ct850-speed-and-incline-range
title: Speed range 0.5 to 12 mph and incline 0 to 15 on the commercial treadmills, and the figures that disagree
kind: spec
question: What is the speed range and the incline range of a Spirit CT850, CT800, CT800ENT
  or CT850ENT treadmill?
asked_as:
- how fast does the spirit ct850 go
- what is the max incline on a ct850
- top speed of the commercial spirit treadmill
- incline levels on the ct850
keywords:
- speed range
- incline range
- max speed
- min speed
- elevation
- mph
- levels
- work range
- treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - ct800-2020
  - ct800ent-2022
  - ct850-2016
  - ct850-2020
  - ct850ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-electrical-part-descriptions
- ct850-2020-electrical-part-descriptions
- spirit-ct850-specs-no-specification-table
- spirit-ct800-specs-no-specification-table
- spirit-ct800ent-console-engineering-mode-speed-and-incline-defaults-wheel-2-98
- ct800-2016-console-calibration-in-kph-with-potentiometer-readings-235-to-22
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: CT850-2016 p. 15 (printed 14) and p. 19 (printed 18); CT850-2020 p. 45
    (printed 44) section 8-5; the owner's-manual figures below are from the CT850-2016
    owner's manual p. 38 and the CT850-2020 owner's manual p. 38. CT800-2016 service manual
    p. 14 (printed 13) Function, text.md lines 207-218, and p. 19 RUN Mode, line 330;
    CT800-2020 service manual p. 43 (printed 42) section 8-4 Factory and Acceleration
    Settings, lines 603-630; CT800ENT-2022 p. 42, Engineering Mode, lines 843-852;
    CT850ENT-2022 p. 43, lines 862-870
  extracted_at: '2026-09-08'
---

| | Speed | Incline |
|---|---|---|
| Working range | **0.5 to 12 mph** | **0 to 15** |
| Step | 0.1 mph per press | 1 per press |
| Display range | 0.0 to 99.9 | 0 to 99 |

The 2020 manual's factory settings agree and add the adjustment limits: **MIN SPEED** default
0.5 mph, adjustable 0.3 to 0.5; **MAX SPEED** default 12.0 mph, adjustable 10.0 to 12.0;
**MAX ELEVATION** default 15, adjustable 10 to 15.

**The CT800 books print the same figures.** The CT800-2016 service manual's Function list gives
the speed WORK range as **0.8~20.0 kph (0.5~12 mph)** and the incline WORK and preset range as
**0 to 15**, with the same 0.1 and 1 steps and display ranges. The CT800-2020 book has no
Function list but its factory settings are the CT850-2020's exactly: min 0.5 (0.3 to 0.5), max
12.0 (10.0 to 12), max elevation 15 (10 to 15), wheel 2.98. The CT800ENT and CT850ENT books print
0.5 to 12.0 mph and incline 15 as their engineering-mode defaults, with the same 2.98 wheel.

**The 2016 manuals contradict themselves on the incline.** The CT850-2016 function list on p. 15
gives the incline work range and preset range as **0 to 15**, but its RUN MODE description on p.
19 says "the maximum incline position is **12**" - and the CT800-2016 book prints the same pair,
0 to 15 on p. 14 and "maximum incline position is 12" on p. 19. A machine set to the factory default reaches 15;
treat the 12 as an error in the source, and check the console's own MAX ELEVATION setting if a
particular machine stops short.

**The owner's manuals for these same two machines say 15.0 mph, not 12.0.** The CT850-2016 and
CT850-2020 owner's manuals both give a Calibration Procedure whose step 6 reads "Adjust the
maximum speed (if needed) to 15.0", and the 2016 console carries Direct Access Speed Buttons
numbered 1 through 15. Their minimum-speed steps disagree with each other too - 0.5 in the 2016
book, 0.3 in the 2020 book. Neither owner's manual states a working range at all, so the 0.5 to
12 mph above remains the only *rated* figure; but a machine calibrated from the owner's manual
will accept a higher maximum than this card's range. Check the console's own MAX SPEED setting
before quoting either. The full four-manual picture, including the CT850-2018 and the
CT850ENT-2022, is in `spirit-ct850-specs-no-specification-table`.

No Spirit CT850 manual prints a motor horsepower, a running-surface size or a machine weight.
The **service** manuals print no maximum user weight either; all four owner's manuals do print
one, on their safety pages rather than in any spec table.
