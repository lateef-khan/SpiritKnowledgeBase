---
id: cu900ent-ftp-error-log-upload
title: FTP settings and uploading the error log
kind: procedure
question: How do I set up error log upload on a Spirit CU900ENT or CR900ENT bike?
asked_as:
- how do i send the error log from the console
- what is the ftp setting on the spirit console
- ftp upload test shows a red circle
keywords:
- ftp settings
- error log
- upload
- ftp ip address
- port 21
- account
- serial number
- path
- upload test
- feedback time
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr900ent-2021
  - cu900ent
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-maintenance-menu
- cu900ent-error-code-log
- cu900ent-wifi-ethernet-setup
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Maintenance / FTP Settings, p. 35 (printed 35). The CR900ENT-2021 service
    manual, FTP Settings, PDF pp. 34-35 (printed 34-35), text.md lines 513-541, prints
    the same page word for word. It prints the same IP address, port, account, password
    (again as "PASSEORD"), the same CR800-ENT example serial and the same green-or-red
    upload test.
  extracted_at: '2026-09-08'
---

FTP Settings uploads the console's error log to Dyaco service. The values printed in the manual:

| Field | Value as printed |
|---|---|
| FTP IP ADDRESS | 61.218.169.200 |
| FTP PORT | 21 |
| ACCOUNT | `dyaco_service` - lower case only |
| PASSWORD | 23751545 |
| SERIAL NUMBER | The machine serial number the error log is filed under, for example `CR800-ENT(5638880810000001)` |
| PATH | The customer name the log is filed under, for example `dyaco_service/SPIRIT FITNESS` |

There is a switch to turn the Error Log feedback function on or off, and a field to set the feedback
time.

**FTP Upload Test** uploads the information when you have finished. A **green circle means the
upload completed**; a **red circle means an error or a failed upload** - check the settings, and
check the network is on. The manual's own warning: when using the Error Log feedback function, be
aware of whether Wi-Fi is connected.

The password field is printed **`PASSEORD`** in the source. The example serial number is a `CR800-ENT`,
not a CU900ENT; the page block is reused across the range.

This uploads the same log that Diagnostics displays on the console.

**The CR900ENT-2021 service manual is this book with the model name changed.** Its engineering-mode chapter runs one PDF page earlier than the CU900ENT's and prints the page this card rests on word for word, so the card covers both machines. It prints the same IP address, port, account, password (again as "PASSEORD"), the same CR800-ENT example serial and the same green-or-red upload test.
