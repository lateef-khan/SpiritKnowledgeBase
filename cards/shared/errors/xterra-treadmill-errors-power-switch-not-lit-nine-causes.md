---
id: xterra-treadmill-errors-power-switch-not-lit-nine-causes
title: 'The ON/OFF switch does not light at power-on: nine causes from an unplugged
  cord to a broken switch, with the breaker reset by its small red button'
kind: troubleshooting
question: Why does the power switch not light up when I turn on an Xterra treadmill,
  and what should I check?
asked_as:
- power switch not lit xterra treadmill
- treadmill completely dead no light on switch
- xterra breaker red button reset
keywords:
- no power
- on/off switch
- power cord
- outlet voltage
- breaker tripped
- small red button
- replace breaker
- replace ac switch
- connecting cable
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-tr-errors-jkexer-console-does-not-light-up
- xterra-ws-errors-treadmill-does-not-work-five-causes
see_also:
- tr260-2023-errors-err-code-troubleshooting-check-list
- xterra-treadmill-errors-display-does-not-light-five-checks-ac-outlet
- xterra-treadmill-errors-stops-or-shuts-off-by-itself-breaker-fuse-controller
- spirit-xt175-errors-no-power-to-console-nine-checks
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246; TR150 SM 8.11
    Troubleshooting procedure matrix, PDF pp. 49-50 (printed 57-58); text.md lines
    826-906; TR260 SM 8-13 Troubleshooting procedure matrix, PDF pp. 51-53; text.md
    lines 794-900; TRX1400 SM Troubleshooting procedure matrix, PDF pp. 61-63 (printed
    55-57); text.md lines 1102-1208; TR150 MCB wiring photo (authority 2), the labels
    SPD / 'If you have speed sensor, then it plugs here', 'M+ Red lead from drive
    motor', 'M- Black lead from drive motor'; text.md lines 1-40
  extracted_at: '2026-09-11'
---

The first row of the troubleshooting procedure matrix, identical in the TR150, TR260, TRX1400, TRX2500 and TRX3500/TRX4500 service manuals:

*Condition:* When turn on power, ON/OFF switch isn't lit.

| Reason | Solve |
|---|---|
| 1. Power cord isn't plugged into outlet | 1. Plug the power cord into outlet |
| 2. Power cord isn't plugged into unit | 2. Plug the power cord into unit |
| 3. The voltage of outlet is too low | 3. Check the voltage of outlet |
| 4. Plug or connector of power cord is open | 4. Replace power cord |
| 5. Connector of power cord is broken | 5. Replace power cord |
| 6. Connecting cable disconnected | 6. Check if wire is disconnected, connect it again |
| 7. Breaker tripped | 7. **Press the small red button** to return to original status |
| 8. Breaker is broken | 8. Replace breaker |
| 9. ON/OFF switch is broken | 9. Replace AC switch |

On the TR150 board the switch's two leads land on the spade terminals marked **AC N (white lead) and AC L (black lead)**, per the annotated board photo. The TR260 check list adds the fuse, varistor and relay-click checks for a console without power (`tr260-2023-errors-err-code-troubleshooting-check-list`). A switch that lights but a console that stays dark is the next row, split by book: `xterra-treadmill-errors-no-display-when-safety-key-inserted-5-pin-main-control-wires`, `tr260-2023-errors-no-display-when-safety-key-inserted-console-cable`, `xterra-trx-errors-no-display-when-safety-key-inserted-12-pin-computer-cable`. The owner's-manual version is `xterra-treadmill-errors-display-does-not-light-five-checks-ac-outlet`.
