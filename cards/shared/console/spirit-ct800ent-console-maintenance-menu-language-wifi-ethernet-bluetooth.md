---
id: spirit-ct800ent-console-maintenance-menu-language-wifi-ethernet-bluetooth
title: 'The Maintenance menu: thirteen default languages named, Wi-Fi, an Ethernet
  DHCP or Static IP page, Bluetooth pairing, Update App, Update OS and CTP Testing'
kind: procedure
question: What is in the Maintenance menu of a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill console?
asked_as:
- how do i put the treadmill on wifi
- how do i change the default language on the treadmill
- how do i pair bluetooth on the ent console
- where is the software update on the treadmill
keywords:
- maintenance menu
- default language
- wifi setup
- ethernet setup
- dhcp
- static ip
- bt setup
- bluetooth
- update app
- update os
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800ent-maintenance-menu
- cu900ent-maintenance-menu
- ct900ent-maintenance-menu-overview
see_also:
- spirit-ct800ent-console-engineering-mode-seven-submenus
- spirit-ent-console-wifi-setup
- spirit-ent-console-software-update
- ct800ent-2022-console-language-selection
- spirit-ent-console-bluetooth-pairing
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT section 8-8 Engineering Mode Instructions, PDF p. 46-50 (printed
    46-50); text.md lines 881-916. The CT850ENT-2022 service manual prints the same
    page word for word on its PDF p. 47-51, text.md lines 900-935. The Maintenance
    and Default language screens are flat images; they were rendered and read
  extracted_at: '2026-09-11'
---

The Maintenance entry of engineering mode is where the language, the network and the software
updates live. Its screen lists seven buttons, in this order: **Default Language Setup**,
**WiFi Setup**, **Etherent Setup** (printed that way), **BT Setup**, **Update App**, **Update OS**,
**CTP Testing**.

**Default language Setup** - "Choose a language as the starting language." The screen names all
thirteen: **English, Deutsch, Français, 繁體中文, Português, 한국어, Россия, Español, 日本語, Italiano,
简体中文, Nederlands, Norsk**. This is the list the owner's manual's language page counts but never
names (`ct800ent-2022-console-language-selection`).

**Set default Wi-Fi** - "When Wi-Fi is set to on, select a connectable network link." The screenshot
is a plain list of network names.

**Set default Ethernet** - "Choose a wired Ethernet connection." The screen shows Ethernet on/off, a
**DHCP Mode / Static IP Mode** choice, and read-only **Connect Info**: MAC Address, IP Address,
Gateway, DNS1, DNS2 and Mask Address. The screenshot's values (192.168.1.1 gateway, 255.255.255.0
mask) are the demonstration machine's, not settings to copy.

**Set default Bluetooth** - "When Bluetooth is set to On, select a connectable network link." The
screen shows Bluetooth on, a **Paired Device** list and an **Available Device** list ("No Bluetooth
device found nearby"), with the note that after Bluetooth is turned on nearby devices can detect the
console.

**Update App, Update OS and CTP Testing are named on the screen and nowhere else.** The manual's own
description of the menu says "USB update, update OS"; it gives no file name, no stick preparation
and no steps. The support note on connecting to the internet describes the over-the-network update
for these machines (`spirit-ent-console-software-update`), and the USB route is documented for the
CU900ENT bike (`cu900ent-usb-software-update`).

The elliptical in this console family prints the same seven buttons with **System & Apps** in place
of CTP Testing (`ce800ent-maintenance-menu`); the CU900ENT bike's Maintenance menu is a different
six (`cu900ent-maintenance-menu`).

