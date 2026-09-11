---
id: 85ue-2025-specs-parts-list
title: The 297-row service-manual parts list, items 1 to 212 for the ergometer and
  501 to 618 for the shared seat, that decodes the owner's-manual drawings
kind: spec
question: What is the parts list for a Spirit 85ue-2025 upper body ergometer, and
  where is it printed?
asked_as:
- parts list for the 8.5ue
- what is item 204 on the 8.5ue exploded view
- the 8.5ue owners manual diagram has no list
- chain wheel sizes on the 8.5ue
keywords:
- parts list
- exploded view
- item number
- chain wheel
- chain
- reflective panel
- shared seat
- quantity
- spare parts
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 85r-2025-specs-parts-list
see_also:
- 85ue-2025-specs-exploded-view-with-no-parts-list
- 85r-2025-specs-parts-list
- 85s-2025-specs-parts-required-maintenance-tools-eighteen
- spirit-climber-specs-which-manuals-print-a-parts-list
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: '"9. 8.5UE Part List" PDF pp. 55-59 (text.md lines 611-612 - the five pages
    are flat images; each was rendered at 300 dpi, OCR-read in all four rotations
    and then read by eye against the render, so every row below was checked visually);
    "8. 8.5UE Exploded view drawing" PDF p. 53 (stamped MZ2000 2025/08/18) and PDF
    p. 54 (headed MR2000/MS2000/MZ2000 shared, stamped 2025/06/11), both flat images.
    Rows 501-618 compared row by row with the 8.5R service manual''s list'
  extracted_at: '2026-09-11'
---

**The owner's manual's two drawings have a list after all - in the service manual.** The MZ2000-SB036-01 service manual prints the ergometer drawing (stamped `MZ2000 2025/08/18`), the seat drawing headed `MR2000/MS2000/MZ2000` for the three machines that share it (stamped `2025/06/11`, the same date the owner's manual's second page carries), and five pages of list. **The five list pages are pictures, not text**: `pdftotext` returns nothing from them, so the table below was read from 300 dpi renders. No Spirit part number is printed.

**Two number series.** 185 rows run 1 to 212 (the ergometer: frame, pulleys, chain wheels, electronics, covers, hardware) and 112 rows run 501 to 618 (the rotating seat). 321 whole numbers are absent between 1 and 618, most of them the unused block 213 to 500. The owner's manual's sample balloons - `032`, `041`, `074`, `075`, `092`, `093`, `094`, `124`, `135`, `200` on the first page, `539`, `540`, `559`, `569`, `573`, `611`, `612`, `613` on the second - all resolve here: 32 `Steel Cable`, 41 `Buckle`, 74 `350L_Power Connecting Cable`, 75 `Switching Power Supply`, 92 `Rear Shroud`, 200 `Baffle Plate`, 539 `Steel Cable-B`, 611 `8mm_L Allen Wrench`. The assembly steps' `(537)` is the `Seat Back` and `(095)` is printed here as `Pedal Cover`.

**Item 89 `Ring Grip Button Cover` is printed with no quantity** - the cell is blank on the page.

## What the list names that the prose does not

- The drive: five `Chain Wheel` rows with their sizes - 204 `Ø40 × Ø23 × 23.2mm`, 205 `Ø37 × Ø30 × 15mm` (three of them), 206 `Ø44 × Ø37 × 36mm`, 207 `Ø44 × Ø37 × 36mm+Ø80 × 3mm`, 208 `Ø40 × Ø25 × 38.8mm` - and two chains, 209 `Chain(EGC35-59)` and 210 `Chain(EGC35-44)`; 35 `Drive Belt`; bearings 54 `6203`, 57 `UCP-20`, 58 `UCP-25`, 59 `6903ZZ` (six), 157 `6202`, 187 `6805`, 188 `Unidirectional Bearing`.
- Electronics: 61 `Console Assembly`, 62 `Resistance Button W/Cable`, 65 `Interface Board`, 70 `AC Electronic Module`, 75 `Switching Power Supply`, 78 `Hall Module`, 79 `Flywheel`, 84 `Generator/Brake Controller`, **85 `Reflective Panel`** (the target of the IR sensor), 110 `Power Cord (Optional)`, 211 `Magnet`; cables 63-69, 71-74, 76-77, 80-83, 86 by length and connector.
- The arm mechanism: 29 `Gas Cylinder`, 30 `Lift Adjustment`, 87 / 88 `Ring Grip (R)` / `(L)`, 154 `Crank Arm` (two), 165 `Handle`, 169 `Handle Link`, 181 `Slider`, 160 `Fixed slider base plate`.
- Tools packed as items: 174 `L Allen Wrench`, 175 `Phillips Head Screw Driver`, 611 `8mm_L Allen Wrench`, 612 `13/14mm_Wrench`, 613 `5 × 26 × 120L_L Allen Wrench`. The bench tools the book asks a technician for are a separate eighteen-row list (`85s-2025-specs-parts-required-maintenance-tools-eighteen`).

## The seat series against the 8.5R's

The 501-618 rows are the 8.5R recumbent's seat list (`85r-2025-specs-parts-list`) with 12 rows worded or counted differently:

| Item | 8.5UE service manual | 8.5R service manual |
|---|---|---|
| 530 | Spring, 1 | Ø 13.5 × 60L_Spring, 1 |
| 532 | Spring, 1 | Ø 15.5×26.5L_Spring, 1 |
| 534 | POM wheel, 4 | Ø 31 × 9.5T_Nylon wheel, 4 |
| 535 | 608AB_Nylon wheel, 27 | Ø 31 × 16.2T_Nylon wheel, 27 |
| 566 | M5 × 4T_Nut, 1 | M5 × 4T_Nut, 2 |
| 567 | M5 × 5T_Nylon Nut, 6 | M5 × 5T_Nylon Nut, 5 |
| 587 | 3/8" × 1-3/4" × 34L_Socket Head Cap Bolt, 2 | 3/8" × 1-3/4"_Socket Head Cap Bolt, 2 |
| 591 | M12_Nylon Nut, 1 | M12 × P1.75 × 8T_Nylon Nut, 1 |
| 601 | Ø8 × 1.5T_Split Washer, 6 | Ø 8 × 1.5T_Split Washer, 2 |
| 602 | M8 × 35mm_Hex Head Bolt, 1 | M8 × 50mm_Hex Head Bolt, 1 |
| 611 | 8mm_L Allen Wrench, 1 | 8mm L Allen Wrench, 1 |
| 613 | 5 × 26 × 120L_L Allen Wrench, 1 | L Allen Wrench, 1 |

## The list

| Item | Description | Qty |
|---|---|---|
| 1 | Main Frame | 1 |
| 2 | Pedal | 2 |
| 3 | Back Plate(A) | 1 |
| 4 | Back Plate(B) | 1 |
| 5 | Rotating Structure Assembly(Top) | 1 |
| 6 | Rotating Structure Assembly(Bottom) | 1 |
| 7 | Console Transfer Bracket | 1 |
| 8 | Pulley Axle-A | 1 |
| 11 | Pulley-E | 1 |
| 12 | Sheet Metal Axis-A | 1 |
| 13 | Axle-A | 1 |
| 14 | Axle-B | 1 |
| 15 | Adjustment Axis-B | 2 |
| 19 | Sheet Metal | 1 |
| 20 | Fixing Bracket | 1 |
| 21 | Sheet Metal | 1 |
| 22 | Connecting Plate | 1 |
| 23 | Transfer Sheet | 1 |
| 27 | Console Bracket | 1 |
| 29 | Gas Cylinder | 1 |
| 30 | Lift Adjustment | 1 |
| 32 | Steel Cable | 1 |
| 35 | Drive Belt | 1 |
| 37 | Spring | 2 |
| 38 | Rubber Foot | 2 |
| 39 | Transportation Wheel | 2 |
| 40 | Adjustment Foot | 4 |
| 41 | Buckle | 10 |
| 42 | Snap seat | 10 |
| 43 | O-ring | 6 |
| 44 | Pedal Mat | 1 |
| 45 | Nylon Washer | 2 |
| 46 | Pad | 2 |
| 47 | Isolation Column | 4 |
| 49 | Round Cap | 1 |
| 54 | 6203_Bearing | 2 |
| 57 | Bearing(UCP-20) | 2 |
| 58 | Bearing(UCP-25) | 2 |
| 59 | 6903ZZ_Bearing | 6 |
| 60 | Cantilever | 1 |
| 61 | Console Assembly | 1 |
| 62 | Resistance Button W/Cable | 1 |
| 63 | 1300mm_Connecting Wire | 1 |
| 64 | 550mm_Connecting Wire(PHP-6) | 1 |
| 65 | Interface Board | 1 |
| 66 | 1700mm_Connecting Wire(PHP-9) | 1 |
| 67 | 550mm_Connecting Wire(PHP-9) | 1 |
| 68 | 1700mm_Connecting Wire(XHP-4) | 1 |
| 69 | 550mm_Connecting Wire(XHP-4) | 1 |
| 70 | AC Electronic Module | 1 |
| 71 | 80mm_Connecting Wire (White) | 1 |
| 72 | 80mm_Connecting Wire (Black) | 1 |
| 73 | 500mm_Ground Wire | 1 |
| 74 | 350L_Power Connecting Cable | 1 |
| 75 | Switching Power Supply | 1 |
| 76 | 300L_Ground Wire | 1 |
| 77 | 250mm_Power Connecting Cable | 1 |
| 78 | Hall Module | 1 |
| 79 | Flywheel | 1 |
| 80 | 250mm_Wire Brake Coil Harness(Red) | 1 |
| 81 | 200mm_Wire Brake Coil Harness(Red) | 1 |
| 82 | 950mm_Connecting Wire(XHP-6) | 1 |
| 83 | 550mm_Connecting Wire(XHP-6) | 1 |
| 84 | Generator/Brake Controller | 1 |
| 85 | Reflective Panel | 1 |
| 86 | 250mm_Connecting Wire(XHP-4) | 1 |
| 87 | Ring Grip (R) | 1 |
| 88 | Ring Grip (L) | 1 |
| 89 | Ring Grip Button Cover | (blank) |
| 90 | Ring Grip Plug | 1 |
| 91 | Release Lever | 1 |
| 92 | Rear Shroud | 1 |
| 93 | Front Upper Cover | 1 |
| 94 | Front Lower Cover | 1 |
| 95 | Pedal Cover | 1 |
| 96 | Top Cover | 1 |
| 97 | Rear Tube Cover | 1 |
| 98 | Inner Ring Positioning Lining | 8 |
| 99 | Handle Bar Cover | 2 |
| 100 | Round Disk | 2 |
| 103 | Ø25_C Ring | 4 |
| 104 | Ø5 × 16L_Tapping Screw | 14 |
| 105 | M10 × 80mm_Socket Head Cap Bolt | 8 |
| 106 | Ø10 × Ø25 × 1.5T_Flat Washer | 9 |
| 107 | M10 × 8T_Nylon Nut | 8 |
| 108 | M4 × P0.7 × 10L_Socket Head Cap Bolt | 2 |
| 109 | Ø5 × Ø12 × 1.0T_Flat Washer | 11 |
| 110 | Power Cord (Optional) | 1 |
| 111 | 1/4" × UNC20 × 3/4"_Hex Head Bolt | 4 |
| 112 | Ø1/4" × 13 × 1.0T_Flat Washer | 7 |
| 113 | Ø1/4"_Split Washer | 7 |
| 114 | M8 × 1.25 × 40mm_Socket Head Cap Bolt | 2 |
| 115 | M8 × P1.25 × 6T_Nylon Nut | 3 |
| 116 | 5/16" × 1-3/4"_Button Head Socket Bolt | 2 |
| 117 | 5/16" × 6T_Nylon Nut | 2 |
| 118 | Ø17_C Ring | 4 |
| 119 | M8 × P1.25 × 20L_Button Head Socket Bolt | 2 |
| 120 | M6 × 40mm_Socket Head Cap Bolt | 8 |
| 121 | M5 × 15mm_Socket Head Cap Bolt | 12 |
| 122 | M5 × 12mm_Phillips Head Screw | 21 |
| 123 | Ø10_Star Washer | 8 |
| 124 | 3.5 × 12mm_Sheet Metal Screw | 10 |
| 125 | 4 × 12mm_Sheet Metal Screw | 10 |
| 126 | 4 × 16mm_Sheet Metal Screw | 1 |
| 127 | Ø8.5 × Ø18 × 1.5T_Flat Washer | 4 |
| 129 | M10 × P1.25 × 10T_Nut | 2 |
| 130 | M6 × 6T_Nylon Nut | 6 |
| 131 | M5 × 15mm_Phillips Head Screw | 1 |
| 133 | Woodruff Key | 1 |
| 134 | M3 × 8mm_Flat Head Socket Screw | 2 |
| 135 | M4 × 8mm_Phillips Head Screw | 7 |
| 136 | M3 × 6mm_Phillips Head Screw | 4 |
| 137 | M4 × 3.5T_Nut | 4 |
| 138 | Wire Clamp | 2 |
| 139 | M5 × 5mm_Slotted Set Screws | 5 |
| 140 | M5 × 10mm_Slotted Set Screws | 2 |
| 141 | 1/4" × 1/2"_Carriage Bolt | 2 |
| 142 | 1/4" × 5.5T_Nylon Nut | 2 |
| 143 | Washer | 2 |
| 144 | M5 × 10mm_Phillips Head Screw | 2 |
| 145 | M10 × P1.5 × 15L_Button Head Socket Bolt | 2 |
| 146 | Ø17 × 3T-M8 × 37L_Flat Head Socket Screw | 2 |
| 147 | M4 × P0.7 × 6mm_Flat Head Socket Screw | 4 |
| 148 | Ø3/8" × 25 × 3.0T_Flat Washer | 2 |
| 149 | 5 × 10L_Woodruff Key | 2 |
| 150 | E4_E-Clip | 16 |
| 151 | Wear Plate | 16 |
| 152 | Ø8 × Ø18 × 3T_Nylon Washer | 2 |
| 154 | Crank Arm | 2 |
| 155 | Axle | 2 |
| 156 | Circular Ring | 2 |
| 157 | 6202_Bearing | 4 |
| 158 | Crank Axle Sleeve | 2 |
| 159 | Crank retaining sleeve | 2 |
| 160 | Fixed slider base plate | 2 |
| 161 | Handgrip Anchor | 2 |
| 162 | Handgrip Anchor | 2 |
| 163 | Anchor | 2 |
| 164 | Anchor | 2 |
| 165 | Handle | 2 |
| 166 | Fixing Axle-C | 2 |
| 167 | Fixing Axle-D | 4 |
| 168 | Spring | 2 |
| 169 | Handle Link | 2 |
| 170 | 3.5 × 10mm_Sheet Metal Screw | 2 |
| 171 | M5 × 5mm_Slotted Set Screws | 6 |
| 172 | M5 × 10mm_Phillips Head Screw | 4 |
| 173 | M5 × 12mm_Phillips Head Screw | 8 |
| 174 | L Allen Wrench | 1 |
| 175 | Phillips Head Screw Driver | 1 |
| 176 | Locating Ring | 2 |
| 177 | Bushing | 2 |
| 178 | M5_Star Washer | 1 |
| 179 | Ø14 × 10 × 25L_Podwer metallurgy Sleeve | 1 |
| 180 | M5 × 25mm_Flat Head Socket Screw | 2 |
| 181 | Slider | 1 |
| 182 | Fixing Bracket | 1 |
| 183 | Idler Bracket-A | 1 |
| 184 | Idler Bracket-B | 1 |
| 185 | Steel Cable | 1 |
| 186 | Tension Spring | 1 |
| 187 | 6805_Bearing | 4 |
| 188 | Unidirectional Bearing | 2 |
| 190 | Round Cap | 1 |
| 191 | Ø5 × 1.5T_Split Washer | 1 |
| 192 | Ø10_C Ring | 1 |
| 193 | Ø17 × Ø23.5 × 1.0T_Flat Washer | 2 |
| 194 | M6 × 57L_Idle Wheel Screw | 1 |
| 195 | M6 × P1.0 × 5.0T_Nut | 2 |
| 197 | Ø15 × 0.3mm_Wave Washer | 2 |
| 198 | Console Rear Trim | 1 |
| 199 | Sleeve | 1 |
| 200 | Baffle Plate | 2 |
| 201 | 3 × 6mm_Sheet Metal Screw | 8 |
| 202 | M10 × 100mm_Socket Head Cap Bolt | 2 |
| 203 | 7 × 7 × 20mm_Woodruff Key | 1 |
| 204 | Chain Wheel(Ø40 × Ø23 × 23.2mm) | 1 |
| 205 | Chain Wheel(Ø37 × Ø30 × 15mm) | 3 |
| 206 | Chain Wheel(Ø44 × Ø37 × 36mm) | 1 |
| 207 | Chain Wheel(Ø44 × Ø37 × 36mm+Ø80 × 3mm) | 1 |
| 208 | Chain Wheel(Ø40 × Ø25 × 38.8mm) | 1 |
| 209 | Chain(EGC35-59) | 1 |
| 210 | Chain(EGC35-44) | 1 |
| 211 | Magnet | 1 |
| 212 | Foam | 2 |
| 501 | Seat Rotation | 1 |
| 502 | Seat Carriage | 1 |
| 503 | Releasing Latch | 1 |
| 504 | Cantilever Anchor Assembly | 1 |
| 505 | Seat Rotation Release Lever | 1 |
| 506 | Rail Assembly | 1 |
| 507 | Seat Release Lever | 1 |
| 508 | Seat Back Fixed Bracket | 1 |
| 509 | Seat Back Bracket | 1 |
| 510 | Cup Holder Sheet Metal | 1 |
| 511 | Adjusting Lever | 1 |
| 512 | Bottom Plate | 2 |
| 513 | Seat Track Sheet Metal(L) | 1 |
| 514 | Seat Track Sheet Metal(R) | 1 |
| 515 | Seat Back Adjustment Sheet Metal | 1 |
| 516 | Adjusting Lever Rotate Axle(L) | 2 |
| 517 | Adjusting Lever | 1 |
| 518 | Steel Cable Sliding Axis | 1 |
| 519 | Handlebar | 1 |
| 520 | Adjusting Rod | 1 |
| 521 | Rack | 1 |
| 522 | Back Plate | 1 |
| 523 | Sheet Metal | 1 |
| 524 | Transportation Wheel Fixing Plate | 1 |
| 525 | Seat Position Latch | 1 |
| 526 | Sheet Metal-A | 2 |
| 527 | Sheet Metal-B | 2 |
| 528 | Gas Cylinder | 1 |
| 529 | Rotate Disk | 1 |
| 530 | Spring | 1 |
| 531 | Constrict Spring | 2 |
| 532 | Spring | 1 |
| 533 | Seat Front Read Adjusting | 2 |
| 534 | POM wheel | 4 |
| 535 | 608AB_Nylon wheel | 27 |
| 536 | Handgrip | 1 |
| 537 | Seat Back | 1 |
| 538 | Seat | 1 |
| 539 | Steel Cable-B | 1 |
| 540 | Steel Cable | 1 |
| 542 | 15.9 × 22mm_Podwer metallurgy Sleeve | 8 |
| 543 | Ø12 × Ø18 × 8L_Podwer metallurgy Sleeve | 2 |
| 544 | Spacer for Stopper Axle | 2 |
| 546 | Buckle | 10 |
| 547 | Snap seat | 10 |
| 548 | Plastic flaps | 2 |
| 549 | Pad | 4 |
| 550 | Beverage Holder | 1 |
| 551 | Hinge Cover | 1 |
| 552 | Seat Back Cover | 1 |
| 553 | Lower Plastic Cover | 1 |
| 554 | Turntable cover (R) | 1 |
| 555 | Turntable cover (L) | 1 |
| 559 | 5/16" × UNC18 × 3/4"_Hex Head Bolt | 9 |
| 560 | M6 × 15mm_Button Head Socket Bolt | 31 |
| 561 | M8 × P1.25 × 25L_Hex Head Bolt | 2 |
| 562 | M6 × 12mm_Socket Head Cap Bolt | 2 |
| 563 | M6 × 38mm_Socket Head Cap Bolt | 3 |
| 564 | M8 × P1.25 × 20L_Socket Head Cap Bolt | 2 |
| 565 | M8 × 20mm_Hex Head Bolt | 10 |
| 566 | M5 × 4T_Nut | 1 |
| 567 | M5 × 5T_Nylon Nut | 6 |
| 568 | M6 × 6T_Nylon Nut | 9 |
| 569 | 5/16" × 6T_Nylon Nut | 11 |
| 570 | M6 × 19L_Nut | 24 |
| 571 | M8 × 1.25 × 6.5T_Square Nut | 18 |
| 572 | Ø6 × Ø16 × 1.0T_Flat Washer | 26 |
| 573 | Ø8.5 × Ø18 × 1.5T_Flat Washer | 21 |
| 574 | Ø16_C Ring | 6 |
| 575 | M5 × 12mm_Flat Head Socket Screw | 4 |
| 576 | M6 × P1.0 × 50L_Button Head Socket Bolt | 1 |
| 577 | M10 × 20mm_Button Head Socket Bolt | 1 |
| 578 | 3/8" × 19mm_Hex Head Bolt | 3 |
| 579 | Ø3/8" × Ø30 × 3T_Flat Washer | 2 |
| 580 | M8 × P1.25(10L × 16L)_Bolt | 1 |
| 581 | M6 × 25mm_Socket Head Cap Bolt | 4 |
| 582 | M6 × P1.0 × 40L_Socket Head Cap Bolt | 3 |
| 583 | Ø5/16" × 19 × 1.5T_Curved Washer | 8 |
| 584 | M5 × P0.8 × 70L_Socket Head Cap Bolt | 1 |
| 585 | M12 × P1.75 × 120L_Socket Head Cap Bolt | 1 |
| 586 | 5/16" × UNC18 × 5/8"_Hex Head Bolt | 2 |
| 587 | 3/8" × 1-3/4" × 34L_Socket Head Cap Bolt | 2 |
| 588 | Ø3/8" × Ø25 × 2.0T_Flat Washer | 2 |
| 589 | M8 × 30mm_Flat Head Socket Screw | 6 |
| 591 | M12_Nylon Nut | 1 |
| 592 | E5_E-Clip | 1 |
| 593 | M5 × 12mm_Phillips Head Screw | 14 |
| 594 | 3.5 × 12mm_Sheet Metal Screw | 10 |
| 595 | M5 × 10mm_Button Head Socket Bolt | 4 |
| 596 | M10 × 70mm_Socket Head Cap Bolt | 1 |
| 597 | M10 × 8T_Nylon Nut | 1 |
| 598 | Ø8.5 × Ø26 × 2.0T_Flat Washer | 2 |
| 599 | 5/16" × 1-1/4"_Hex Head Bolt | 1 |
| 600 | Ø6.6 × Ø12 × 1.5T_Flat Washer | 2 |
| 601 | Ø8 × 1.5T_Split Washer | 6 |
| 602 | M8 × 35mm_Hex Head Bolt | 1 |
| 603 | M8 × P1.25 × 15L_Button Head Socket Bolt | 2 |
| 604 | M8 × 10mm_Button Head Socket Bolt | 1 |
| 605 | M8 × 20mm_Flat Head Countersink Bolt | 4 |
| 606 | M8 × 60mm_Flat Head Countersink Bolt | 2 |
| 607 | M8 × 7T_Nylon Nut | 2 |
| 608 | Ø8.5 × Ø26 × 2.0T_Flat Washer | 2 |
| 609 | M8 × P1.25 × 20L_Button Head Socket Bolt | 4 |
| 610 | 3/8" × 7T_Nylon Nut | 2 |
| 611 | 8mm_L Allen Wrench | 1 |
| 612 | 13/14mm_Wrench | 1 |
| 613 | 5 × 26 × 120L_L Allen Wrench | 1 |
| 614 | M6 × P1.0(Ø8 × 20L)_Bolt | 2 |
| 615 | M6 × 12mm_Socket Head Cap Bolt | 4 |
| 616 | M5 × 15mm_Phillips Head Screw | 4 |
| 617 | Ø6 × 25L × M5 × P0.8_Bolt | 1 |
| 618 | Fixing Base | 1 |

