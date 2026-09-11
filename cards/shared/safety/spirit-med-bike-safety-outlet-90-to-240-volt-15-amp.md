---
id: spirit-med-bike-safety-outlet-90-to-240-volt-15-amp
title: A 90 to 240 volt AC, 50/60 Hz, 15-amp grounded outlet with a 16awg cord, for
  a bike whose supply is universal and fused at 5 amps
kind: spec
question: What outlet, circuit and extension cord does a Spirit Medical 7.0R or 7.0U
  rehabilitation bike (70r-2025, 70u-2025) or the Dyaco MED 7.0R (70r-2021) need?
asked_as:
- what outlet does the 7.0r need
- can i plug the 7.0u into a normal socket
- can i use an extension cord with the 7.0r
- what voltage does the 7.0u run on
keywords:
- outlet
- voltage
- amperage
- 90 to 240 volt
- 50/60 hz
- 15 amp
- extension cord
- 16awg
- dedicated circuit
- universal power supply
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-med-bike-safety-outlet-100-to-240-volt-15-amp
- spirit-climber-safety-outlet-100-to-240-volt-15-amp
- 85ue-2025-safety-outlet-100-to-240-volt-50-60-hz-15-amp
- spirit-bike-safety-no-mains-outlet-needed
- spirit-ct800-safety-outlet-120-volt-15-amp
see_also:
- spirit-product-must-be-grounded
- spirit-med-bike-safety-instructions-list-plug-in-with-emergency-brake-lever
- spirit-med-bike-safety-operating-environment-iec-60601
- spirit-extension-cord-16-awg-or-better
- xt-2023-safety-supply-voltage-variation
- 70r-2021-safety-packaging-symbols-ce-mdd-class-im-and-type-b-applied-parts
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: 'SAFETY INSTRUCTIONS item 2, PDF p. 6 (printed 4), text.md lines 108-143;
    ELECTRICAL SAFETY, PDF p. 8 (printed 6), lines 171-203; Plugging in & Starting
    Operation, PDF p. 23 (printed 21), lines 618-647; SPECIFICATIONS, PDF p. 49 (printed
    47), lines 1377-1413. 7.0U: item 2 PDF p. 6, lines 112-151; p. 8, lines 177-208;
    p. 21, lines 580-607; p. 47, OCR supplement at line 2358, in spirit-bike-70u-2025-owners-manual.
    Dyaco MED 7.0R: Warning bullets PDF p. 5, lines 80-117; Important electrical information
    PDF p. 15, lines 486-517; Connecting to A.C. power PDF p. 37, lines 1109-1151;
    Specifications PDF p. 86, lines 2730-2775; labeling symbols PDF p. 90, lines 2911-2941,
    in spirit-bike-70r-2021-owners-manual'
  extracted_at: '2026-09-11'
---

> To reduce the risk of burns, fire, electric shock, or injury to persons, install the 7.0R on a
> flat level surface with access to a **90 to 240-volt AC, 50/60 Hz, 15-amp grounded outlet**. Do
> not use an extension cord unless it is **16awg or larger**, with only one outlet on the end. The
> 7.0R should be the only appliance in the electrical circuit. Do not attempt to disable the
> grounded plug by using improper adapters, or in any way modify the cord set; a serious shock or
> fire hazard may result along with computer malfunctions.

| Requirement | Figure |
|---|---|
| Nominal supply | **90 to 240 volt AC** - a range, not one voltage |
| Frequency | **50/60 Hz** |
| Circuit | **15 amp**, and the bike the only appliance on it |
| Outlet | grounded (`spirit-product-must-be-grounded`) |
| Extension cord | **16awg or larger**, one outlet on the end |
| Surface | flat and level |

**The machine draws far less than 15 amps.** The specification page prints the load - `90-240V ~:
50/60 Hz: 1.76-0.71A` - so 1.76 A at 90 V falling to 0.71 A at 240 V. The 15 amp figure is the
circuit the manual requires, not the current the bike takes; both are printed and never side by
side.

**The supply is universal and fused.** The setting-up page says:

> The 7.0R has a built-in universal power supply. You can plug the 7.0R into any A.C. power source
> from 90 to 240 volts, 50 to 60 Hz. The A.C. input is located in the front of the 7.0R. The input
> module has an input connector for the line cord, a power switch and a 5 amp fuse. Turn the power
> switch to off when the 7.0R is not in use.

The specification page adds the fuse to fit: `Replace with only 5A, 250V glass fuse. Fast acting
5.2 x 20 mm.` **No NEMA plug type is printed anywhere** in either book, and no breaker paragraph.

**The tolerance rule is on the electrical page.** `If voltage varies by 10% or more outside the
specified range (90 to 240V), the performance of your 7.0R may be affected. Such conditions are not
covered under your warranty` (`xt-2023-safety-supply-voltage-variation`).

**The 7.0U prints every figure the same.** Its safety item 2, electrical page, setting-up page and
specification page carry the same 90 to 240 V, 50/60 Hz, 15 amp, 16awg, 5 amp fuse and 1.76-0.71 A.

## The Dyaco MED 7.0R of 2021 prints 90 to 240 volt too, and its symbol page says 50 Hz

**The Dyaco edition prints the same outlet sentence** (as a bullet), the same 10 % tolerance
paragraph, the same `Connecting to A.C. power` paragraph with the 5 amp fuse, and the same
`90-240V ~: 50/60 Hz: 1.76-0.71A` on its specification page. **Its packaging-and-labeling symbol page
reads `AC power 90-240 Volt, 15Amps, 50Hz`** - 50 Hz alone, and 15 amps as if it were the machine's
rating rather than the circuit's. Both are printed; the 50/60 Hz of the safety page is the figure
the specification page agrees with
(`70r-2021-safety-packaging-symbols-ce-mdd-class-im-and-type-b-applied-parts`).

**The 8.0U and 8.5R ask for 100 to 240 volt**, not 90
(`spirit-med-bike-safety-outlet-100-to-240-volt-15-amp`), as do the 8.5UE ergometer and the
steppers. The 4.0R and 4.0U need no outlet at all (`spirit-bike-safety-no-mains-outlet-needed`).
