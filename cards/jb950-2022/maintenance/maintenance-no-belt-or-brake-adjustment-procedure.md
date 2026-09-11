---
id: jb950-2022-maintenance-no-belt-or-brake-adjustment-procedure
title: No belt tension or brake gap adjustment in the service manual; the belt is
  set at 100 to 110 lb only when replaced
kind: fact
question: How do I adjust the belt tension or the magnetic brake on a Spirit jb950-2022
  Johnny G bike?
asked_as:
- how do i tighten the belt on my johnny g bike
- brake gap adjustment jb950
- the jb950 belt is slipping
- can i adjust the magnetic brake on the johnny g spirit bike
keywords:
- belt tension
- 100 to 110 pounds
- magnetic brake
- no adjustment
- brake gap
- service technician
- drum brake
- generator belt
- flywheel belt
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: maintenance
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-air-bike-maintenance-weekly-vibration-and-flywheel-torque
see_also:
- jb950-2022-maintenance-weekly-check-toe-clips-and-service-tech
- jb950-2022-console-brake-test
- jb950-2022-console-calibration-do-not-enter
- spirit-cycle-specs-resistance-systems
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 'Absence, proved across the whole book. The 51-page service manual''s contents
    run Parts Replacement (six procedures: generator, generator drive belt, lower
    control board, belt, brake assembly, drum brake assembly), Electronic Parts, Electrical
    Configurations, Basic Connections and Wiring, Error Messages / Troubleshooting
    with the Maintenance Menu, and Console Update. Loose searches of text.md including
    its twelve OCR supplements for ''gap'', ''slip'', ''lubric'', ''grease'', ''clean'',
    ''wear'', ''brake pad'' and ''tension'' return only the two ''Adjust the belt
    tension between 100-110 pounds'' lines - 4. Belt Replacement step 12, PDF p. 14
    (printed 14), text.md line 190, and 5. Brake Assembly Replacement step 12, PDF
    p. 17 (printed 17), line 242 - plus the Maintenance Menu pages. Every page under
    25 native words was rendered by the sweep; none added maintenance text.'
  extracted_at: '2026-09-11'
---

**The service manual prints no maintenance chapter, no belt adjustment and no brake adjustment.**
Its mechanical content is six replacement procedures, and the only tension figure in the book sits
inside two of them: after the flywheel assembly goes back on (two M12 nylon nuts (169) and the M6
eye bolt (129), 19 mm open-end wrench), **'Adjust the belt tension between 100–110 pounds.'** That
is an install setting inside the belt and brake-assembly replacements, with no gauge named and no
procedure for tightening a belt in service.

**There is no brake gap to set.** The JB950's resistance is a motor-driven magnetic brake —
neodymium magnets, a gear motor to move them and a closed-loop encoder reporting brake position to
the console (`spirit-cycle-specs-resistance-systems`). Nothing in the book asks a technician to
measure a distance between magnet and flywheel. Brake position is handled electronically: the
Maintenance Mode **Brake Test** runs the motor from L-1 to L-20 and shows the encoder count and the
home / active-range / end sensor state (`jb950-2022-console-brake-test`), and **Calibration** holds
the factory offset that must be copied from an old console to a new one
(`jb950-2022-console-calibration-do-not-enter`). A brake that does not reach its home position is
the book's MOTOR ERROR, an errors matter.

**Two belts, one figure.** The book replaces the **generator drive belts** (#43, two of them, behind
the left crank arm) and the belt behind the flywheel assembly in separate procedures; the 100–110 lb
line appears only in the flywheel-belt and brake-assembly procedures. No figure is printed for the
generator belts.

The owner's manual's weekly check refers a vibrating flywheel and belt alignment to a service
technician (`jb950-2022-maintenance-weekly-check-toe-clips-and-service-tech`). This book gives that
technician the replacement steps and the 100–110 lb setting, and nothing else. The air bikes, by
contrast, have their owner torque the flywheel nuts weekly
(`spirit-air-bike-maintenance-weekly-vibration-and-flywheel-torque`).

