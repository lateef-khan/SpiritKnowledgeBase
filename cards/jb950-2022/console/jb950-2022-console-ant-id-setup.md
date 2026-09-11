---
id: jb950-2022-console-ant-id-setup
title: Giving each bike a unique number for a leaderboard, where zero is not a valid
  number
kind: procedure
question: How do I number the bikes for a leaderboard on a Spirit jb950-2022 Johnny
  G Spirit Bike?
asked_as:
- how do i set up spivi with my johnny g bikes
- how do i number the bikes in my studio
- ant id setup on the jb950
- two bikes showing as the same on the leaderboard
keywords:
- ant+ id setup
- bike number
- leaderboard
- spivi
- myzone
- unique
- '1000'
- zero not valid
- studio
- maintenance mode
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: console
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with: []
see_also:
- jb950-2022-console-ant-bluetooth-ftms-and-apps
- jb950-2022-console-maintenance-mode-entry-and-menu
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: JB950-2022 printed p. 58 ANT+ ID SETUP; leaderboard compatibility from
    printed p. 31. JB950 service manual 5.3 BIKE ID SETUP, PDF p. 42 (printed 42),
    text.md lines 767-777
  extracted_at: '2026-09-09'
---

**Purpose: to allow numbering of the bike when using leaderboard software, such as Spivi or similar.**

1. Press the **Play Key** to change the setting.
2. The console displays **`ANT+ ID SETUP`**, with **1 flashing on the lower console.**
3. Press the **+ Key or - Key** to adjust the bike number to the number you want. **Over 1,000 are
   available.**
4. **Set each bike to a unique number.** The number **must be set to 1 or above - 0 is not a valid
   number.**
5. Press the **Play Key** to accept. The bike number stops flashing momentarily, then turns off,
   indicating it is set.
6. Press **+** for the next screen, or reset the console to exit Maintenance Mode.

**Zero is the trap.** A bike left on 0 will not appear correctly on the leaderboard, and the console
gives no error to say so - it simply accepts the value.

**Duplicates are the other trap.** Two bikes on the same number collide on the board and neither rider
gets a reliable position. Walk the room and write the numbers down.

**Each bike has to be pedalled to be set.** The console is powered by the rider above 30 RPM, so
numbering a studio of bikes is a per-bike job with someone on the cranks.

**The bike is compatible with leaderboards such as those from MyZone or Spivi**, and carries both an
ANT+ and a Bluetooth FTMS chip - `jb950-2022-console-ant-bluetooth-ftms-and-apps`.

**The service manual calls this entry BIKE ID SETUP and gives the range as 1 to 999**, not "over 1,000".
Its purpose line names "a Leaderboard software with ANT+ transmission, such as Performance IQ or
similar", and adds that the number **also sets the name in the Bluetooth search list** - so a phone
scanning for the bike sees this number. The console displays BIKE ID with 1 flashing; the keys and the
accept step are the same as above.
