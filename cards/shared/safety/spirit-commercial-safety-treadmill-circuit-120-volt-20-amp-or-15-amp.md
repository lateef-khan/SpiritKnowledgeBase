---
id: spirit-commercial-safety-treadmill-circuit-120-volt-20-amp-or-15-amp
title: Every treadmill takes power on its own 120 volt circuit, at 20 amps for five
  models and 15 amps for two
kind: spec
question: Which Spirit commercial treadmill needs a 120 volt, 20 amp circuit and which
  a 15 amp one, according to the Spirit Fitness power requirements sheet?
asked_as:
- what amp circuit does my spirit treadmill need
- does the treadmill need a 20 amp breaker
- which spirit treadmills run on a 15 amp circuit
- spirit commercial treadmill power requirements
keywords:
- power requirements
- 120 volt
- 20 amp
- 15 amp
- dedicated circuit
- isolated ground
- treadmill
- breaker
- electrical
- ct850ent
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ct800-2016
  - ct850-2018
  - ct900
  - ct900ent
  - mt200-2010
  - xt685-2015
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating
- spirit-treadmill-safety-outlet-220-volt-10-amp
see_also:
- spirit-commercial-safety-dedicated-circuit-and-isolated-ground-defined
- spirit-commercial-safety-treadmill-plug-nema-5-20p-into-a-5-20r-t-slot
- spirit-commercial-safety-non-treadmill-120-volt-15-amp-or-self-generating
- spirit-commercial-safety-non-treadmill-nema-5-15p-four-units-per-15-amp-circuit
- spirit-ct850-outlet-and-circuit-requirement
- spirit-ct800-safety-outlet-110-volt-15-amp
- spirit-ct800-safety-outlet-120-volt-15-amp
- xt-2015-safety-outlet-and-circuit-requirement
- spirit-mt200-safety-outlet-and-circuit-requirement
- ct900ent-electrical-requirements-gfci-breakers
- ct900ent-grounding-instructions
- ct900-grounding-instructions
- ct900-electrical-safety
- spirit-2026t-safety-outlet-and-circuit-requirement
- spirit-house-breaker-needs-a-high-inrush-type
- ct850-2016-trips-onboard-10-amp-circuit
- ct850-2020-trips-onboard-20-amp-circuit
source:
  ref: spirit-commercial-power-requirements-sheet-2019
  locator: TREADMILLS table and the four bullets under it, PDF p. 1, text.md lines
    1-45 (table lines 6-14, bullets lines 16-22). Both pages read from a 130 dpi render
    as well as the text layer; every X in the tables was checked against the render.
    Revision 03.06.2019, marked *For U.S. Markets.
  extracted_at: '2026-09-11'
---

**A 120 volt circuit for every treadmill on the sheet, and the sheet splits the amperage: 20 amps for five models, 15 amps for the CT800 and the XT685.** It is Spirit Fitness's own one-page statement, not a manual.

> All Spirit Fitness treadmills require power to operate regardless of console configuration.
> Circuits should be dedicated to each machine and require a non-looped (isolated) ground.

| Treadmill | 120V/20AMP | 120V/15AMP |
|---|---|---|
| CT900ENT | X | |
| CT900 | X | |
| CT850ENT | X | |
| CT850 | X | |
| CT800 | | X |
| XT685 | | X |
| MT200 | X | |

- **Regardless of console configuration** - an ENT touchscreen and a plain console draw from the same circuit rating; the ENT suffix changes nothing on this table.
- **Dedicated to each machine**, with a **non-looped (isolated) ground** - both terms are defined on the same page (`spirit-commercial-safety-dedicated-circuit-and-isolated-ground-defined`).
- **The plug is a NEMA 5-20P** on every treadmill but the two 15 amp ones (`spirit-commercial-safety-treadmill-plug-nema-5-20p-into-a-5-20r-t-slot`).
- **For U.S. markets** - the sheet says so in its footnote. It prints no 230 volt column; the 230 volt build of a Spirit treadmill has its own figure (`spirit-treadmill-safety-outlet-220-volt-10-amp`).

## Which machine each name is

The sheet names models without years. The ids on this card are the ones dated 2019 or earlier at the sheet's own date, or year-less where that is the only id:

| Name on the sheet | Id on this card | Why |
|---|---|---|
| CT900ENT, CT900 | `ct900ent`, `ct900` | the only ids, year-less |
| CT850 | `ct850-2018` | latest CT850 id dated 2019 or earlier (2016, 2018, 2020 exist) |
| CT800 | `ct800-2016` | latest CT800 id dated 2019 or earlier (2012, 2016, 2020 exist) |
| XT685 | `xt685-2015` | latest XT685 id dated 2019 or earlier (2010, 2015, 2023 exist) |
| MT200 | `mt200-2010` | the only MT200 id dated 2019 or earlier (2010, 2022 exist) |
| CT850ENT | **none** | the only ids are `ct850ent-2022` and `ct850ent-2024`, both later than the sheet |

**CT850ENT is on the sheet and on no id here.** Do not read this row across to a `ct850ent-2022` or `ct850ent-2024`: their own books say 120 volt at 20 amps for the 2022 machine and 15 amps for the 2024 (`spirit-ct850-outlet-and-circuit-requirement`, `spirit-ct800-safety-outlet-120-volt-15-amp`), which is a change the sheet predates.

## Where the sheet and the manuals disagree

**The amperage agrees with every manual but one.** The CT850-2018 owner's manual asks for a nominal 110-volt, **15 amp** dedicated circuit and a dedicated 15 amp breaker (`spirit-ct800-safety-outlet-110-volt-15-amp`); this sheet puts the CT850 at 120 volt, **20 amps**, as the 2016 and 2020 CT850 books do (`spirit-ct850-outlet-and-circuit-requirement`). The sheet is one more voice for 20 amps on a CT850 and it does not mention the 2018 printing; say both figures and which document each comes from.

**The voltage agrees with almost none of them.** The sheet says 120 volts throughout. The CT900ENT and CT900 owner's manuals say a nominal **110** volt circuit (`ct900ent-grounding-instructions`, `ct900-grounding-instructions`), the CT800-2016 and the 2015 XT685 say **110** volt at 15 amps (`spirit-ct800-safety-outlet-110-volt-15-amp`, `xt-2015-safety-outlet-and-circuit-requirement`), and the MT200-2010 says **115** volt AC, 60 Hz, 20 amps (`spirit-mt200-safety-outlet-and-circuit-requirement`). Nothing reconciles 110, 115 and 120; on a North American supply they describe the same socket, and the amperage is the figure that decides the breaker.

**The MT200 is on this sheet at 20 amps, and its manual agrees**: 20 amps in both. **The CT900ENT manual agrees on 20 amps as well** (`ct900ent-electrical-requirements-gfci-breakers`). The CT900 owner's manual prints no amp figure at all, and its service manual's only outlet sentence is the 220-volt, 10-amp one for the 230 volt build (`spirit-treadmill-safety-outlet-220-volt-10-amp`), so this sheet is the only Spirit document that gives a 120-volt CT900 a circuit rating.

**The onboard breaker is a different figure.** The 10 amp and 20 amp circuits the CT850 service manuals say the treadmill trips are the machine's own breaker, not the wall circuit on this sheet (`ct850-2016-trips-onboard-10-amp-circuit`, `ct850-2020-trips-onboard-20-amp-circuit`). A house breaker that trips while the treadmill's does not is `spirit-house-breaker-needs-a-high-inrush-type`.

**The 2026 4.0T, 7.0T and 8.0T are not on the sheet** - it predates them - but their manuals ask for the same thing this sheet asks of the five 20 amp treadmills: 120 volts, a dedicated 20 amp circuit and a NEMA 5-20P (`spirit-2026t-safety-outlet-and-circuit-requirement`).

