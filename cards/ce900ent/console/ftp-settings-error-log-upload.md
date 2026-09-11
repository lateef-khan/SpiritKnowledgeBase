---
id: ce900ent-console-ftp-settings-error-log-upload
title: FTP Settings uploads the error log to a Dyaco service server at 61.218.169.200,
  port 21, account dyaco_service
kind: procedure
question: How do I set up error log upload on a Spirit ce900ent elliptical?
asked_as:
- ce900ent ftp settings
- how do i upload the error log from the ce900ent
- ce900ent ftp upload test red circle
- dyaco service ftp address
keywords:
- ftp settings
- error log
- upload
- 61.218.169.200
- port 21
- dyaco_service
- password
- serial number
- auto upload
- ftp upload test
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
- ce900ent-console-wifi-ethernet-setup-dhcp-or-static-ip
- cu900ent-ftp-error-log-upload
- cu900ent-error-code-log
source:
  ref: spirit-elliptical-ce900ent-service-manual
  locator: Setting and Operation for Engineering Mode, FTP Settings, PDF pp. 35-36
    (printed 35-36); text.md lines 596-624, with the screenshots in the OCR supplements
    for PDF pages 35 and 36, lines 2025-2070
  extracted_at: '2026-09-11'
---

FTP Settings, the sixth Maintenance button, uploads the console's error log to Dyaco service. The
values printed in the manual:

| Field | Value as printed |
|---|---|
| FTP IP ADDRESS | 61.218.169.200 |
| FTP PORT | 21 |
| ACCOUNT | `dyaco_service` - lower case only |
| PASSWORD | 23751545 |
| SERIAL NUMBER | The machine serial number the error log is filed under, for example `CR800-ENT(5638880810000001)` |
| PATH | The customer name the log is filed under, for example `dyaco_service/SPIRIT FITNESS` |

There is a switch to turn the Error Log feedback function on or off (**AUTO UPLOAD ON/OFF**), and
Hour and Min fields to set the feedback time.

**FTP Upload Test** uploads the information when you have finished. A **green circle means the
upload completed**; a **red circle means an error or a failed upload** - "please verify for correct
setting or network is not turned on". The manual's own warning: when using the Error Log feedback
function, be aware of whether Wi-Fi is connected
(`ce900ent-console-wifi-ethernet-setup-dhcp-or-static-ip`).

The password field is printed **`PASSEORD`** in the source. The example serial number is a
`CR800-ENT`, not a CE900ENT; the page block is reused across the range, and the CU900ENT and
CR900ENT bike books print it word for word (`cu900ent-ftp-error-log-upload`).

This uploads the same log that Diagnostics displays on the console
(`ce900ent-console-engineering-mode-seven-settings-entries-machine-information-first`).
