---
id: jb950-2022-console-brake-test
title: The Brake Test that runs the resistance motor from L-1 to L-20 and back, and
  the manual motor test behind it
kind: procedure
question: How do I test the magnetic resistance system on a Spirit jb950-2022 Johnny
  G Spirit Bike?
asked_as:
- how do i test the resistance on my johnny g bike
- the levels on my jb950 do not change
- motor test on the johnny g spirit bike
- brake test on my spin bike console
keywords:
- brake test
- motor test auto
- motor test manual
- level to 20
- l-1
- l-20
- encoder
- limit sensor
- home
- active range
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
- jb950-2022-console-limit-sensor-test
- jb950-2022-console-calibration-do-not-enter
- jb950-2022-console-reset
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: JB950-2022 printed p. 55 BRAKE TEST and MOTOR TEST MANUAL. JB950 service
    manual 5.3 BRAKE TEST, PDF p. 41 (printed 41), text.md lines 700-724
  extracted_at: '2026-09-09'
---

**Brake test controls are a sensitive setting for the bike's functionality. Proper training is
required for this setting.** Purpose: to test the magnetic resistance system.

**MOTOR TEST AUTO:**

1. Press the **Play Key** to enter Brake Test. **`MOTOR TEST AUTO`** is displayed.
2. Press **+ or -** to switch between **Motor Manual**, **Limit Sensor** and **Exit**.
3. Press the **Play Key**.
4. **`LEVEL TO 20`** displays. Press the Play Key.
5. The motor **auto-runs in a loop from L-1 to L-20 and back to L-1.**
6. Press the Play Key to end and revert to BRAKE TEST.

**MOTOR TEST MANUAL:**

- Use the **+ Key and - Key to move the motor**. Press Play to end and revert to BRAKE TEST.
- **`ENCODER`** displays - this is the encoder count, or digital value.
- **The upper right of the display shows the LIMIT SENSOR CONDITION:**

  | Reading | Meaning |
  |---|---|
  | **1** | HOME |
  | **2** | ACTIVE RANGE |
  | **3** | END |

- The **lower display shows the ENCODER SET VALUE**.
- **To exit, a Console Reset is required** - Play Key and + Key together for 3 seconds.

**Motor Test Manual is the one place in this menu you cannot leave with the Play Key.** Note it
before you enter, or you will be stuck pedalling and pressing.

**Limit Sensor is the third branch** of the same entry and is documented separately, because the
manual restricts it to occasions when a motor error has occurred -
`jb950-2022-console-limit-sensor-test`.

**Neither Brake Test nor Limit Sensor calibrates anything.** Calibration is a separate menu entry the
manual tells you not to enter - `jb950-2022-console-calibration-do-not-enter`.

**The service manual describes Motor Test Manual and Limit Sensor in more detail.** In Motor Test Manual,
**use + and - to set a target, press Play to move the brake to the target position, and press again to
return to zero**; **hold Play and + to reset the console and leave the test**. The ENCODER field is the
target encoder count "and is an important tool to know whether the encoder is functioning properly";
the lower display is the **Encoder Set Value** - where the brake should move to - while the encoder is
where it actually reaches. In Limit Sensor, + and - move the brake, the top left shows the home
sensor, the top right the end limit sensor, the bottom the encoder counts; **hold Play to end**. The
1 / 2 / 3 readings are the same.
