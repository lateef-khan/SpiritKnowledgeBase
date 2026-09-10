---
id: jb950-2022-console-limit-sensor-test
title: 'The Limit Sensor test, run only after a motor error, and the fifteen-minute stand it can demand'
kind: procedure
question: 'How do I test the limit sensor after a motor error on a Spirit jb950-2022 Johnny G Spirit Bike?'
asked_as:
- 'motor error on my johnny g bike'
- 's1 s2 test on the jb950'
- 'limit sensor test on the johnny g spirit bike'
- 'resistance stuck on my spin bike'
keywords:
- 'limit sensor'
- 's1'
- 's2'
- 'home sensor'
- 'encoder wheel count'
- 'motor error'
- '15 minutes'
- 'memory clear'
- 'flag'
- 'brake test'
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- jb950-2022-console-brake-test
- jb950-2022-console-rpm-sensor-test
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: JB950-2022 printed p. 56 LIMIT SENSOR
  extracted_at: '2026-09-09'
---

**The Limit Sensor test checks the proper movement of the flag that moves between the home sensor
(S1) and the limit sensor (S2).** The manual restricts it: **this test is performed only when a motor
error has occurred.**

It is reached from **Brake Test**, by pressing + or - at the `MOTOR TEST AUTO` screen until Limit
Sensor is shown.

1. The display reads **`S1 OFF, S2 OFF`**, and the bottom number is the **encoder wheel count (0)**.
2. Using the **+ and - Keys**, adjust the motor to try to change **S1 to ON**.
3. **Pedalling resistance should change as the keys are pressed.** That is the sign the motor is
   moving the flag.
4. **If S1 goes ON, stop pedalling immediately.** Allow the console to turn off and **let the bike
   stand for 15 minutes minimum for memory to clear** before trying it again.
5. **EXIT** reverts to the setting screen. Press **+** for the next screen, or reset the console to
   exit Maintenance Mode.

**Step 4 is the whole point of the procedure and it is easy to miss.** A technician who keeps
pedalling through an S1 ON reading does not clear the memory, and the bike comes back with the same
fault. Fifteen minutes is a minimum, not a target.

**Resistance that does not change as the keys are pressed** points at the motor or its wiring rather
than at the sensors - Motor Test Manual in `jb950-2022-console-brake-test` is where the encoder count
is read.
