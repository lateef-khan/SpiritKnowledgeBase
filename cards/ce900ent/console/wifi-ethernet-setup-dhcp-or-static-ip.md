---
id: ce900ent-console-wifi-ethernet-setup-dhcp-or-static-ip
title: WiFi/Ethernet Setup offers a Wi-Fi scan and an Ethernet configuration with
  DHCP or a static IP
kind: procedure
question: How do I connect a Spirit ce900ent elliptical to the network?
asked_as:
- how do i connect the ce900ent to wifi
- ce900ent ethernet static ip
- ce900ent network setup
- ce900ent wifi not connecting
keywords:
- wifi
- ethernet
- network setting
- dhcp
- static ip
- ip address
- netmask
- gateway
- dns
- mac address
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce900ent
  applies_to:
  - ce900ent
  section: console
  code: '*'
  model_number:
  - '900050'
authority: 3
not_to_be_confused_with: []
see_also:
- ce900ent-console-maintenance-menu-six-buttons-and-twelve-languages
- ce900ent-console-date-and-time-via-ten-presses-on-etherner-configuration
- ce900ent-console-ftp-settings-error-log-upload
- cu900ent-wifi-ethernet-setup
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Setting and Operation for Engineering Mode, WiFi/Ethernet Setup, PDF pp.
    33-34 (printed 33-34); text.md lines 549-575, with the screenshots in the OCR
    supplements for PDF pages 33 and 34, lines 1921-1989
  extracted_at: '2026-09-11'
---

**WiFi/Ethernet Setup** offers two buttons: **WiFi** and **Ethernet**.

**WiFi.** "Please hit WiFi button to proceed WiFi setting." The Wi-Fi Setting screen has **On**,
**Scan** and **Add Network** across the top and lists the networks it can see with their status.

**Ethernet.** The Ethernet Configuration screen shows the current **IP Address** and **MAC Address**
read-only, and an **Ethernet Configuration / Configure Ethernet devices** row that opens the network
setting mode.

The Network Setting screen holds:

| Field | Screenshot value |
|---|---|
| Ethernet Devices | eth0 |
| Connection Type | DHCP or Static IP |
| IP address | 192.168.192.28 |
| NetMask | 255.255.255.0 |
| Gateway address | 192.168.192.1 |
| DNS address | 10.10.2.66 |

Those values are the demonstration machine's, not settings to copy; the MAC on the screenshot is
00:18:70:91:48:7F.

- Select **DHCP** and "the network will automatically search for the connection".
- Select **Static IP** to set the four fields by hand.

Pressing **"Etherner Configuration"** ten consecutive times opens the Android setting mode, which is
where date and time are set
(`ce900ent-console-date-and-time-via-ten-presses-on-etherner-configuration`).

**The CU900ENT and CR900ENT bike books print these pages word for word**
(`cu900ent-wifi-ethernet-setup`).
