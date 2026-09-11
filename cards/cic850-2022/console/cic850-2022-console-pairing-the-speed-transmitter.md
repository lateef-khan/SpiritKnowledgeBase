---
id: cic850-2022-console-pairing-the-speed-transmitter
title: Re-pairing the console to the speed transmitter, and what 0 and Err mean
kind: procedure
question: How do I re-pair the speed transmitter to the console on a Spirit cic850-2022
  indoor cycle?
asked_as:
- my indoor cycle console shows no speed
- how do i pair the sensor to my spin bike display
- what does err mean on my cic850 console
- cadence jumping around on the spirit indoor cycle
keywords:
- pairing
- transmitter
- speed control pair key
- err
- console code
- cross-talking
- 10 seconds
- mode
- set
- unpaired
facets:
  brand:
  - spirit
  product_line: bike
  model: cic850-2022
  applies_to:
  - cic850-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cic850-2022-console-set-key-not-on-the-console
- cic850-2022-console-two-aaa-batteries
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: CIC850-2022 printed p. 17 and printed p. 29, PAIRING THE CONSOLE AND TRANSMITTER
    (the same block printed twice). CIC850 pairing process support tip (scanned, OCR
    only), PDF p. 1, text.md lines 5-29 of the OCR supplement; CIC850 service manual
    9-3 Display Blank or No Speed Displayed, PDF p. 26 (printed 25), text.md lines
    387-398
  extracted_at: '2026-09-09'
---

**All transmitters are paired with the console before shipping.** The manual's own note says these
steps should only be needed where the devices have been unpaired.

1. Hold **both MODE and SET keys** on the console for **3 seconds**.
2. On the speed transmitter, press the small **"SPEED CONTROL PAIR KEY"**.
3. The console should read **`0`** once a successful pairing has been established.
4. If the console reads **`Err`**, the pairing has failed. **Press the SET key** to repeat the steps.

**There is no SET key on this console.** It has three keys - MODE, a smartphone button and
PAGE/RECORD. Read SET as **PAGE/RECORD**; the wording is carried over from another console in the
same family. See `cic850-2022-console-set-key-not-on-the-console`.

**You have ten seconds.** If no action is taken within **10 seconds** the console automatically exits
pairing mode.

**When to run it.** After the sensor board battery is changed under the left chain guard, and when
the cadence number jumps high or low - the troubleshooting page's first cause for that is that two
bikes are paired to the same console code and are cross-talking, and its fix is to run the transmitter
pair stage again. Its second is to move the bike away from RF interference.

**The manual prints this block twice**, once in the assembly chapter and once in the console chapter,
word for word.

**A scanned support tip prints a different key sequence for the same pairing**, headed "New SB700/900
Console | CIC X50" - a technician's note (authority 2) rather than a manual:

1. Press **Mode** to highlight **DIST**.
2. Press and hold **Page** until you see a blinking **TIME**.
3. **Press and hold Mode and Page** until you see **PAIR** with three blinking lines.
4. **Start pedalling** until you see **ERR** or **0**.
5. **ERR** means the pairing failed - the transmitter battery may need changing, or the speed sensor
   is not aligned properly. **0** means it succeeded.

**No SET key and no button on the transmitter.** The tip's route enters through the Mode and Page keys
the console actually has, and it makes the rider pedal to give the transmitter a signal, where the
manual has you press a pair key on the transmitter. Both end at the same 0 or Err. The tip carries no
date and names the Sole SB700/SB900 console alongside the CIC; only the CIC850 side is carded here.

**The service manual's own no-speed advice ends "Each transmitter and console are matched one to
one"** - check the battery of console and transmitter, the sensor and magnet, the transmitter position -
which is why a swapped transmitter must be re-paired.
