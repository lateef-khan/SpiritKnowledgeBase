---
id: spirit-elliptical-specs-drive-belt-tension-figure-by-service-manual
title: 'Which belt-tension figure each elliptical service manual prints: 190 Hz, 185
  to 210 Hz, 280 to 310 N, twin belts at 540 and 1000 N, or none'
kind: spec
question: What belt tension figure does the service manual print for each Spirit elliptical,
  and in what unit?
asked_as:
- what hz should the elliptical belt read
- belt tension for the ce900 in newtons
- does the ce850 service manual give a belt tension
- sonic meter reading for a spirit elliptical belt
keywords:
- belt tension
- drive belt
- poly-v
- 190 hz
- 280-310 n
- 185-210
- sonic belt tension meter
- hook screw
- j bolt
- pressure roller
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce1000ent-2023
  - ce800-2016
  - ce800-2021
  - ce850-2016
  - ce850-2020
  - ce900-2021
  - ce900ent
  - xe195-2016
  - xe295-2016
  - xe395-2016
  - xe395ent-2021
  - xe795-2016
  - xe795-2023
  - xe895-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cvc800-drive-belt-tension
- spirit-xbr95-specs-drive-belt-tension-180-hz-acoustic-gauge
- spirit-cr900-specs-drive-belt-tension-220-240-newtons
- cu900ent-drive-belt-tension
- e35-2016-drive-belt-tension
see_also:
- spirit-xe-2016-maintenance-belt-slipping-hook-screw-cap-13-mm-190-hz
- spirit-ce900-maintenance-belt-slips-or-falls-off-pressure-roller-280-to-310-n
- ce800-2021-maintenance-belt-drops-off-or-slips-j-bolt-nut-13-mm
- ce800ent-drive-belt-tension
- xg400-2016-assembly-drive-belt-replacement
- xg400-2016-specs-parts-gear-motor-and-belts-named-by-type
- ce850-2020-assembly-no-parts-replacement-chapter
source:
  ref: spirit-elliptical-xe395-2016-service-manual
  locator: 'XE395-2016: 11-8 Idler Wheel replacement step 3, PDF p. 93, text.md lines
    1493-1507. XE195 p. 74 (1106-1121); XE295 p. 76 (1120-1135); XE395ENT p. 82 (1169-1183);
    XE795-2016 p. 69 (955-971); XE795-2023 p. 25 (478-491); XE895 p. 105 (1705-1720);
    CE850-2016 p. 105 (1706-1721); CE800-2016 p. 61 (875-891). CE800-2021 10-7 step
    3, p. 48 (651-666). CE900-2021 6.11.2, p. 46 (826-849) and 7.1, p. 58 (1019-1036);
    CE900ENT p. 57 (1034-1057) and p. 69 (1227-1244); CE1000ENT 12.21, p. 26 (561-587)
    and p. 32 (730-762). XG400 step 4, p. 52 (869-895). CE850-2020: no belt figure
    anywhere in the book - its contents (PDF p. 2) have no replacement chapter, and
    a grep for HZ, Hz, N), newton and tension meter returns only the electrical pages'
  extracted_at: '2026-09-11'
---

No elliptical service manual prints a belt tension in a specification table; each prints its
figure inside a replacement or troubleshooting step. Four families of figure, one unit each:

| Figure | Unit | Set at | Machines |
|---|---|---|---|
| **190 Hz (plus or minus 10)** | frequency, sonic meter or "flick for a crisp sound" | nyloc nut M8x9T on the hook screws | CE800-2016, CE850-2016, XE195, XE295, XE395, XE395ENT, XE795-2016, XE795-2023, XE895 |
| **about 185 to 210**, printed "Khz" | frequency, sonic belt tension meter; read Hz - a kilohertz belt is impossible | nut on the J bolt, 13 mm wrench | CE800-2021 (and the CE800ENT, same figure) |
| **280 to 310 N** | force | the pressure roller (idler bracket) | CE900-2021, CE900ENT, CE1000ENT |
| **left belt 540, right belt 1000**, printed "NT" | force (newtons) | both idler wheels | XG400, which has two belts: PJ 8-rib left, PK 6-rib right, both 1000 mm |
| **none** | - | - | CE850-2020: the book has no replacement chapter and prints no belt figure |

The 190 Hz row is one sentence repeated across nine books: *tighten the nyloc nuts M8x9T on top
of the hook screws, flick the belt for crisp sound to check tightness or use a sound measuring
device to measure at 190HZ (plus or minus 10)*. The 280-310 N row is printed twice per book -
once at belt removal ("when the belt is installed in the middle of the belt, belt tension
maintained at 280 ~ 310N") and once under *Belt Slips/Falls off*.

**Do not carry a figure across a row.** A CE900 belt set to 190 of anything is wrong, and a
frequency and a force cannot be converted without the belt's span and mass, which no book gives.
The procedures that set each figure are the maintenance and assembly cards:
`spirit-xe-2016-maintenance-belt-slipping-hook-screw-cap-13-mm-190-hz`,
`ce800-2021-maintenance-belt-drops-off-or-slips-j-bolt-nut-13-mm`,
`spirit-ce900-maintenance-belt-slips-or-falls-off-pressure-roller-280-to-310-n`,
`xg400-2016-assembly-drive-belt-replacement`. The CVC800 climber (190 Hz, `cvc800-drive-belt-tension`)
and the XBR95 bike (180 Hz) are other product lines with their own cards.

