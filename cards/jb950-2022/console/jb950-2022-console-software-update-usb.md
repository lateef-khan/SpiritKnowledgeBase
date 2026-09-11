---
id: jb950-2022-console-software-update-usb
title: Updating the console software from a blank USB stick in the port underneath
  the console
kind: procedure
question: How do I update the console software on a Spirit jb950-2022 Johnny G Spirit
  Bike?
asked_as:
- how do i update the software on my johnny g bike
- firmware update for the jb950
- where is the usb port on the johnny g spirit bike
- update fail on my spin bike console
keywords:
- update software
- usb
- memory stick
- bootloader
- update done
- search update
- update fail
- firmware
- port
- console reset
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
- jb950-2022-console-software-version
- jb950-2022-console-reset
- jb950-2022-console-screen-and-keys
- jb950-2022-console-gfit-bluetooth-module-update-with-nrf-connect-to-version-4-3
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: JB950-2022 printed p. 57 UPDATE SOFTWARE. JB950 service manual 5.3 UPDATE
    SOFTWARE, PDF p. 42 (printed 42), text.md lines 739-757, and 6.1 Console software
    update, PDF pp. 47-48 (printed 47-48), lines 874-901
  extracted_at: '2026-09-09'
---

**The USB port is underneath the console.** Updating requires a **blank USB memory stick** and a
computer, to transfer updates from the service website or an e-mail from customer service onto the
stick. **No other material besides the updates should be on the USB drive.**

1. **Insert the USB drive.**
2. Press the **Play Key** to display **`BOOTLOADER - OFF`**.
3. Press **+ or -** to switch to **`BOOTLOADER - ON`**.
4. Press the **Play Key** to advance out of the software update.
5. **Reset the console** - Play Key and + Key together for 3 seconds. **`CONSOLE RESET`** displays.
   - If successful, **`UPDATE DONE`** displays, flashing.
   - If unsuccessful, **`SEARCH UPDATE`** or **`UPDATE FAIL`** displays. **Check the USB for proper
     insertion and re-attempt.**
6. The console resets with **`JOHNNY G METHOD`** flashing.
7. **Remove the USB stick.**

**A stick with anything else on it is the commonest cause of failure**, because the manual is explicit
that only the update files should be present. Format the stick before copying.

**Check the version before and after.** The Software Version entry of the same menu displays what is
running, and the manual says knowing it is necessary for customer service when they provide updates -
`jb950-2022-console-software-version`.

**The port has no other use.** Nothing in this manual charges a phone, plays media or loads a video
from it.

**The service manual prints the update twice, in two different orders, and neither is quite this one.**

Its Maintenance Mode page: switch **BOOTLOADER** to ON, then **allow the console to power down and
wait until it has turned off** - "powering down could take up to 10 minutes if bike had been ridden
for a time" - then insert the USB drive, wait 1 to 2 minutes, and pedal to wake the console; it shows
SEARCH UPDATE, then UPDATE DONE or UPDATE FAIL.

Its Console Update chapter: download the .zip and extract **the two software update files** to the
root of a blank USB disk; plug the stick into the connector at the bottom of the console; enter
Maintenance Mode, go to UPDATE SOFTWARE and press Play; set Bootloader ON and press Play; hold Play
and + to reset - the console shows SEARCH UPDATE, and UPDATE DONE when finished, then returns to the
start-up screen.

**Two files, not one, and a stick inserted before or after the reset depending on which page you
read.** All three routes agree on Bootloader ON, a blank stick with nothing else on it, and the
SEARCH UPDATE / UPDATE DONE / UPDATE FAIL messages. **Update the GFIT Bluetooth module first** if a
module update is also due (`jb950-2022-console-gfit-bluetooth-module-update-with-nrf-connect-to-version-4-3`).
