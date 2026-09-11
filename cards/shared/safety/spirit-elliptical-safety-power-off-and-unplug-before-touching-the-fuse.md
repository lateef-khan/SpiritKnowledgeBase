---
id: spirit-elliptical-safety-power-off-and-unplug-before-touching-the-fuse
title: Turn the power switch off and unplug the elliptical before you touch the fuse
  on the motor controller
kind: policy
question: Do I have to unplug a Spirit CE850, XE395, XE395ENT or XE895 elliptical
  (ce850-2016, ce850-2020, xe395-2016, xe395ent-2021 or xe895-2016) before replacing
  the fuse on its motor controller?
asked_as:
- elliptical lost power is it the fuse
- can i change the fuse with the elliptical plugged in
- where is the fuse on the elliptical
- what fuse does the ce850 take
keywords:
- fuse
- fuse holder
- motor controller
- unplug
- power switch
- electric shock
- danger
- no power
- 5 amp
- 10 amp
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-treadmill-safety-power-off-before-the-repair-procedures
- xt-2023-safety-remove-a-cover-only-with-ac-disconnected
see_also:
- spirit-disconnect-from-the-outlet-before-cleaning-or-service
- xt-2023-safety-remove-a-cover-only-with-ac-disconnected
- spirit-xe-safety-outlet-115-volt-15-amp
- spirit-ct800-safety-outlet-120-volt-15-amp
- spirit-ce850-safety-outlet-and-circuit-requirement
- spirit-house-breaker-needs-a-high-inrush-type
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016 (XE898-SE011) service manual: 8-6 Fuse replacement, PDF p.
    55 (printed 55); text.md lines 957-971 (FUSE 5A). CE850 (2020) service manual:
    8-6 Fuse replacement, PDF p. 48 (printed 48); lines 836-849 and OCR supplement
    lines 1659-1674 (FUSE 10A). XE395-2016 (XE539S-SE019-01) service manual: Fuse
    replacement, PDF p. 56 (printed 56); lines 950-963 (FUSE 5A). XE395ENT-2021 (XE539S-SE025-01)
    service manual: Fuse replacement, PDF p. 45 (printed 45); lines 641-654 (FUSE
    5A). XE895-2016 (XE895-SE022) service manual: 8-6 Fuse replacement, PDF p. 56
    (printed 56); lines 957-970 and supplement lines 2567-2584 (FUSE 5A). The Tension
    Motor Voltage Test step 5, `inspect power socket the holder FUSE`, is CE850-2016
    PDF p. 43, line 721; CE850 (2020) PDF p. 35, line 617; XE395-2016 PDF p. 43, line
    712; XE395ENT PDF p. 28, line 370; XE895-2016 PDF p. 43, line 720; and, in books
    with no fuse page, XE195-2016 PDF p. 37, line 577; XE295-2016 PDF p. 37, line
    581; XG400-2016 PDF p. 35, line 518.'
  extracted_at: '2026-09-11'
---

**Power switch off, then unplug, before the fuse holder comes out.** Five Spirit elliptical service
manuals print the same fuse-replacement page, and its one safety line is a DANGER:

> If your elliptical loses power or will not start, check the fuse located on the motor controller.
> DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric
> shock. Remove FUSE holder. Remove and replace the fuse on the holder.

- **Two actions, in that order**: the machine's own power switch off, and the plug out of the wall.
  The general rule elsewhere in these books asks only for the disconnection
  (`spirit-disconnect-from-the-outlet-before-cleaning-or-service`); this page asks for both.
- **The fuse is on the motor controller**, under the chain covers, in a holder. The page shows a
  photograph of the holder and the fuse and prints no part number for either.
- **The symptom that sends you there is no power or no start.** The same books' Tension Motor Voltage
  Test says, when there is no motor voltage, `inspect power socket the holder FUSE. If broke replace
  it` - the fuse holder sits at the power socket on the driver board.

**The rating printed on the page differs between books, and one book prints twice the others'
figure:**

| Service manual | Photograph caption |
|---|---|
| CE850-2016 (XE898-SE011) | `FUSE 5A` |
| CE850 (2020) | `FUSE 10A` |
| XE395-2016 (XE539S-SE019-01) | `FUSE 5A` |
| XE395ENT-2021 (XE539S-SE025-01) | `FUSE 5A` |
| XE895-2016 (XE895-SE022) | `FUSE 5A` |

That is the caption on the picture, not a specification sentence; the books print no fuse type, no
voltage rating and no part number. The CE850 (2020) book's 10 A sits in a book that also prints a
`nominal 115-volt circuit (or 220-volt circuit)` and draws two driver boards, one labelled 110 V and
one 220 V, so which fuse a given machine carries is a question for the label on the holder. Quote
the caption with the book it comes from.

**The XE195-2016, XE295-2016 and XG400-2016 service manuals print no fuse page.** They carry the
same `inspect power socket the holder FUSE` line in their tension-motor test and nothing else - no
rating, no photograph, no DANGER. The XE795-2016 and XE795-2023 service manuals mention no fuse at
all; those machines are generator-powered (`spirit-xe795-console-power-up-by-pedalling`). Do not
carry a rating onto any of the five from this table.

**This DANGER is the only warning printed at the head of a procedure in any of the sixteen
elliptical service manuals.** The disassembly chapters start straight into screw sizes; the
CE850-2016 and XE895-2016 books even say `Plug in the power supply before remove Incline Motor` so
that the stride can be driven to a set length first, and only then `cut off the power`. Treat this
page's DANGER as the rule for every job on the motor controller, and the chapter-7 disconnect
sentence as the rule for everything else (`xt-2023-safety-remove-a-cover-only-with-ac-disconnected`
for the owner's-manual version).

