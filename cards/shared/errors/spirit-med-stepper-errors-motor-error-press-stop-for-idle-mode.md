---
id: spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode
title: Motor Error clears to idle mode when you press stop, and the machine still
  works with no resistance changes
kind: troubleshooting
question: What does Motor Error mean on a Spirit recumbent stepper, and can the machine
  still be used?
asked_as:
- my stepper says motor error
- what does motor error mean on the console
- stepper resistance wont change and shows an error
- can i keep using the machine with a motor error
keywords:
- motor error
- resistance motor
- idle mode
- press stop
- no resistance changes
- power cycle
- one minute
- stepper
- recumbent stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: motor-error
authority: 3
not_to_be_confused_with:
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cvc800-e-2-tension-motor-error
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
- ce850-2024-errors-err-tension-motor-failure
see_also:
- cs800-2024-errors-eeprom-error-replace-the-console
- crs800s-2024-errors-motor-error-tension-motor-signal-wrong
- cvc800-e-2-tension-motor-error
- spirit-med-stepper-errors-one-pedal-has-no-resistance-drive-cable
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: ERROR MESSAGE & TROUBLESHOOTING, printed page 40 (PDF page 42) of the 7.0S
    2025 manual; the same text on printed page 42 (PDF page 44) of the 7.5S 2025 manual
    and under the heading "Error messages" on printed page 59 (PDF page 59) of the
    MS300 2021 manual. Read from the native text layer of all three and confirmed
    against a 300 dpi render of the 7.0S page; 7.5S (RS9600-SS021) service manual
    5.2.2 Error messages, PDF p. 13, text.md lines 125-128, and 5.2.3 "Motor Error",
    PDF p. 18-19, text.md lines 189-201
  extracted_at: '2026-09-10'
---

**The message is the words `Motor Error`** - no code letter, no number.

The manual, word for word:

> Motor Error - Press stop to enter idle mode - This error means the motor that controls resistance
> did not respond as expected. If the error occurs press stop. The console will return to the idle
> mode. You can then use the console but there will be no resistance changes. You may try to
> disconnect the power to the machine for one minute and re-connect. This may solve the problem, but
> if it does not call service.

**The machine is still usable, and the manual says so.** Press stop, the console returns to idle, and
a workout can go on - at whatever resistance the machine is stuck at, because level changes will not
take. That is the only Spirit error message in the repository that comes with permission to keep
using the machine.

**The remedy in order:**

1. Press **stop**. The console returns to idle mode.
2. Disconnect the power for **one minute**, then reconnect.
3. If it comes back, call service.

**Do not read this card to a caller with a CRS800S, CS800 or CVC800.** Those machines print the same
two words - or the same sentence - and give a different answer:

| Machine | Message | What the manual says |
|---|---|---|
| CRS800S 2024 semi-recumbent stepper | `MOTOR ERROR` | The tension motor is abnormal or sending a wrong signal, and **no remedy is printed at all** (`crs800s-2024-errors-motor-error-tension-motor-signal-wrong`) |
| CVC800 vertical climber | `E-2` | The same sentence, plus a signal path, a voltage and a pass band (`cvc800-e-2-tension-motor-error`) |
| CS800 2024 stepper | `Err` in the LEVEL window | Tension motor feedback missing, cable checked first (`cs800-2024-errors-err-in-the-level-window-tension-motor-feedback`) |

**The page these five manuals print it on says `EEPROM Error` is "the only error message".** It is
not - this one is printed directly beneath it. See
`cs800-2024-errors-eeprom-error-replace-the-console`.

**The Spirit 7.0S is not the Dyaco 7.0S.** Dyaco MED sells a rehabilitation stepper under the same
`7.0S` name, in a manual that says Dyaco fourteen times and Spirit not once. Nothing in this card
came from that book.

## The 7.5S service manual defines the message in the same words and adds two resistance readings

*5.2.2 Error messages:* **Motor Error** - This error means the motor that controls resistance did not respond as expected. (It sits under the same `EEPROM Error ... (Note: this is the only error message)` line the owner's manuals print, so the contradiction is in the service manual too.)

*5.2.3 Motor Error*, the diagnosis the owner's manuals do not print:

> i. Make sure all the cables in the back of console are plugged in properly and there are no bent pins in the connector.
> ii. Use an ohm meter to measure between **pin 1 and pin 2 of the 14 pin cable** that connects to the console (check at the cable connector when it is unplugged from the console). The reading should be **about 2~3 ohm**; this is the motor armature measurement and tells you the motor is most likely good. Use the ohm meter to measure between **pin 3 and pin 5** of the 14 pin cable that connects to the console (check at the cable connector when it is unplugged from the console). The reading should be **about 5k ohm**; this is the motor position sensor. **Replace the console if the reading is correct.** Go to next step if the measurement is incorrect.
> iii. Open the left shroud and check the connection of the cable that connects to the motor. Replace the motor if the connection is good. Otherwise, replace the cable.

**Two resistances settle it, both read at the unplugged console end of the 14-pin cable.** About 2 to 3 ohms across pins 1 and 2 is the motor's armature; about 5 k ohms across pins 3 and 5 is its position sensor. Both correct means the motor and its cable are fine and the console is the fault; either wrong sends you to the motor's own connector under the left shroud, and then to the motor or the cable. This is the 7.5S book; its figures are printed for that machine.
