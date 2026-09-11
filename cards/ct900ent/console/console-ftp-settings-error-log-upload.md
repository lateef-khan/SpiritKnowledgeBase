---
id: ct900ent-console-ftp-settings-error-log-upload
title: 'FTP Settings: the Spirit service server the error log uploads to, the auto-upload
  time, and the green or red circle on FTP Upload Test'
kind: procedure
question: How is the error log uploaded from a Spirit ct900ent treadmill and what
  are the FTP settings?
asked_as:
- how do i send the error log to spirit
- what are the ftp settings on the treadmill console
- ftp upload test shows a red circle
- what serial number goes in the ftp settings
keywords:
- ftp settings
- error log
- upload
- ftp ip address
- port 21
- dyaco_service
- serial number
- path
- auto upload
- ftp upload test
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- cu900ent-ftp-error-log-upload
see_also:
- ct900ent-maintenance-menu-overview
- ct900ent-wifi-ethernet-setup
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: Setting and Operation for Engineering Mode, Maintenance / FTP Settings,
    PDF pp. 41-42 (printed 41-42); text.md lines 615-661
  extracted_at: '2026-09-11'
---

FTP Settings, under Maintenance in engineering mode, uploads the console's error log to Dyaco
service. The values printed in the manual:

| Field | Value as printed |
|---|---|
| FTP IP ADDRESS | 61.218.169.200 |
| FTP PORT | 21 |
| ACCOUNT | `dyaco_service` - lower case only |
| PASSWORD | 23751545 (the manual misprints the label as PASSEORD) |
| SERIAL NUMBER | The machine serial number the error log is filed under, for example `CR800-ENT(5638880810000001)` |
| PATH | The customer name the log is filed under, for example `dyaco_service/SPIRIT FITNESS` |

**AUTO UPLOAD ON/OFF** turns the Error Log feedback function on or off, and the Hour and Min fields
beside it set the feedback time (12:00 in the screenshot).

**FTP Upload Test** uploads the information when you have finished. **A green circle means the
upload completed; a red circle means an error message or a failed upload** - verify the settings and
that the network is on. The manual's own warning: when using the Error Log feedback function, be
aware of whether WiFi is connected.

**The serial number example is a bike's**, CR800-ENT, in a treadmill manual; the field takes the
serial of the machine in front of you.

The owner's manual says only that FTP Settings "is the Spirit FTP site address where Error logs and
remote troubleshooting can be managed" (`ct900ent-maintenance-menu-overview`). The CU900ENT bike
prints these same values (`cu900ent-ftp-error-log-upload`).

