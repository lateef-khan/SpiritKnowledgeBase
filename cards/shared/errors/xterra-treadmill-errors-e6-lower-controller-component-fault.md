---
id: xterra-treadmill-errors-e6-lower-controller-component-fault
title: 'E6: a component inside the lower controller has failed, and the owner''s manuals
  that call it a power fault'
kind: troubleshooting
question: What does E6 mean on an Xterra treadmill, and what does each manual say
  to do?
asked_as:
- e6 on my xterra treadmill
- e6 controller malfunction
- e6 power malfunction trx
keywords:
- e6
- lower controller
- controller malfunction
- transistor
- igbt
- control module
- power malfunction
- power transistor
- replace controller
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr200-2021
  - tr260-2023
  - tr300-2021
  - tr65-2023
  - trx1000-2021
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: errors
  code: e6
authority: 3
not_to_be_confused_with:
- xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change
- xterra-ws-errors-e06-system-self-check-failed
- f63-2023-e6-error-code
see_also:
- xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
- tr260-2023-errors-err-code-troubleshooting-check-list
- spirit-xt-errors-e6-lower-controller-component-fault
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.7 Error Message: E6, PDF pp. 54-55 (printed 53-54); text.md
    lines 937-1010; TR150 SM 8.6 Error Message: E6, PDF p. 43; text.md lines 690-724;
    TR260 SM 8-9 Error Message: E6, PDF p. 45; text.md lines 692-713; TRX1400 SM 8.7
    Error Message: E6, PDF p. 56 (printed 55); text.md lines 996-1031; TRX3500/TRX4500
    SM 8.7 Error Message: E6, PDF p. 61 (printed 60); text.md lines 1017-1051; TRX5500
    SM 7-10 Error Message: E6, PDF p. 57 (printed 56); text.md lines 866-895; TR150
    OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md lines 619-677; TR200
    OM Service Checklist - Diagnosis Guide, PDF p. 21; text.md lines 648-706; TR260
    OM Service Checklist - Diagnosis Guide, PDF p. 20; text.md lines 812-870; TRX1000
    OM Service Checklist - Diagnosis Guide, PDF p. 18; text.md lines 662-720; TR300
    OM Error Messages, PDF p. 24 (printed 22); text.md lines 876-895; TR65 OM Troubleshooting,
    Error Code Guide, PDF p. 43 (printed 42); text.md lines 1431-1464; TRX1400 OM
    Troubleshooting, Error Code Guide, PDF p. 39 (printed 38); text.md lines 1285-1305;
    TRX2500 OM Error Messages, PDF p. 21 (printed 19); text.md lines 695-741; TRX3500
    OM Error Messages, PDF p. 23 (printed 21); text.md lines 818-866; TRX4500 OM Error
    Messages, PDF p. 24 (printed 22); text.md lines 901-948'
  extracted_at: '2026-09-11'
---

**This is E6 on the Dyaco-built Xterra treadmills, where it is a controller fault.** On the TR75H and TR95H E6 is an incline VR fault (`xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change`) and on the WS200/WS300 E06 is a failed self-check (`xterra-ws-errors-e06-system-self-check-failed`).

*Service manuals.* Definition: the lower controller component is at fault. Cause: a lower controller component such as a **transistor, IGBT or control module** has failed.

| Part | Troubleshooting |
|---|---|
| Lower controller | Insert power wire of motor |
| Display board | Only replace upper control board |

That table is printed the same way in all seven books, and it does not say "replace the lower controller" - the TR260 check list does (`tr260-2023-errors-err-code-troubleshooting-check-list`: "Controller component malfunction - Replace controller"). The **TR260 book's 8-9 definition of E6 is a copy of its E5 text** ("poor communication between the console and lower controller"); its code table (8-1) and check list both say lower control board.

*Owner's manuals disagree about what E6 is*

| Books | Printed meaning |
|---|---|
| TR150, TR200, TR260, TRX1000 | Controller Malfunction - Controller component failure |
| TR65 | Controller Malfunction - Controller component failure - Replace controller |
| TRX1400 | Power transistor failure |
| TR300, TRX2500, TRX3500, TRX4500 | **Power malfunction** |

The TRX2500, TRX3500 and TRX4500 service manuals list E6 as "Lower Control board possible broken" and reserve the power fault for **E7**; their owner's manuals print E6 as "Power malfunction" and no E7. Both are printed; a customer reading E6 off one of those consoles should be asked about the supply as well as the controller.
