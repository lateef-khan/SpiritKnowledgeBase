---
id: cu900ent-wifi-ethernet-setup
title: Wi-Fi and Ethernet setup
kind: procedure
question: How do I connect a Spirit CU900ENT bike to the network?
asked_as:
- how do i connect the bike to wifi
- how do i set a static ip on the console
- the bike console will not go online
keywords:
- wifi setup
- ethernet setup
- scan
- add network
- dhcp
- static ip
- netmask
- gateway
- dns
- mac address
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-maintenance-menu
- cu900ent-date-and-time-setup
- cu900ent-ftp-error-log-upload
- ce800ent-maintenance-menu
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Maintenance / WiFi/Ethernet Setup, p. 33 (printed 33, flattened image read
    from raw/page-33.png) and p. 34 (printed 34)
  extracted_at: '2026-09-08'
---

**WiFi/Ethernet Setup** offers two buttons: **WiFi** and **Ethernet**.

**WiFi.** The Wi-Fi Setting screen has **On**, **Scan** and **Add Network** across the top and lists
the networks it can see with their status.

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

Those values are the demonstration machine's, not settings to copy.

- Select **DHCP** and the network is found automatically.
- Select **Static IP** to set the four fields by hand, then **Save**.

Pressing **"Etherner Configuration"** ten consecutive times opens the Android setting mode, which is
where date and time are set.
