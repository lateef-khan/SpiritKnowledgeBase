---
id: sole-airplay-mirroring-apple
title: AirPlay screen mirroring from an Apple device
kind: troubleshooting
question: Why will AirPlay not mirror my iPhone or iPad to my Sole touchscreen machine?
asked_as:
- airplay wont work on my treadmill
- cant mirror my iphone to the screen
- treadmill asks for an airplay passcode
keywords:
- airplay
- screen mirroring
- iphone
- ipad
- passcode
- mdm
- control center
- same network
- mesh router
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f80-2023
  - f80-2026
  - f83-2026
  - f85-2020
  - f85-2021
  - f85-2023
  - f85-2026
  - f89-2023
  - st90-2020
  - st90-2021
  - st90-2023
  - tt8-2020
  - tt8-2023
  section: console
  code: '*'
authority: 2
not_to_be_confused_with:
- sole-screen-mirroring-android
see_also:
- sole-screen-mirroring-android
- sole-connect-wifi-touchscreen
- sole-update-software-touchscreen
source:
  ref: sole-tm-airplay-or-screen-mirroring-not-working
  locator: sections "Apple Devices" and "If customer using mesh router"
  extracted_at: '2026-09-03'
---

**First:** copyright protected content will never mirror. It shows a black, green or garbled screen, or refuses to start.

**Steps**

1. Put the machine and the Apple device on the **same network**.
2. Make sure both the Apple device and the machine are fully up to date, with no pending software updates.
3. Swipe down from the top right corner of the Apple device to open Control Center.
4. Tap the **AirPlay screen mirror** icon.
5. Pick the machine's name from the list.

**If the Apple device asks for a pin**

On the Apple device, open Settings, go to **AirPlay & Continuity**, set **Automatically AirPlay** to **Never**, and turn **AirPlay Receiver** off.

**If it still asks for a passcode, stop.** The device will not connect. This happens when a workplace Mobile Device Management (MDM) app controls the phone and forces stronger security. Our machines do not handle that and never show a pin to type. There is no workaround. The customer must use a different device that is not managed by an MDM.

**If the customer has a mesh router**

- Turn on **802.11r fast roam**. Google Nest has this on already.
- Turn off **AP Isolation**.
