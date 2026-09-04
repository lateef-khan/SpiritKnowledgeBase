---
id: f85-2019-display-mode-setting
title: The setting that decides whether the console shows a code when the key is pulled
kind: procedure
question: Why does my Sole F85-2019 treadmill show an error when I remove the safety
  key, and how do I change it?
asked_as:
- console shows a code when i pull the safety key
- how do i stop the display staying on without the key
- display mode setting on my treadmill
keywords:
- display mode
- safety key removed
- console stays on
- engineering mode
- functions menu
- power down
- software setting
- sleep
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2019-e0-safety-key-error
- f85-2019-engineering-mode-menu
source:
  ref: sole-tm-f85-2019-service-manual
  locator: 'section 8.1 Error Message: E0, Note before hardware checks, printed page
    55'
  extracted_at: '2026-09-04'
---

**Check this software setting before you check any hardware for an E0 complaint.**

1. Remove the safety key.
2. Press **STOP**, **START** and **ENTER** together and, at the same moment, insert the safety key. The display enters **ENGINEERING MODE**.
3. Press FAST/SLOW or UP/DOWN to find **"functions"**, press **ENTER** to reach **DISPLAY MODE**, then press **ENTER** again to choose on or off.

| Setting | Behaviour when the safety key is removed |
|---|---|
| Off | The display goes off. |
| On | The display stays on and shows **E0**. |

So an E0 on a machine with no other symptom can simply be this setting turned on.

**The same setting has a second effect, listed on a different page.** In the engineering mode menu it appears as Functions > Display Mode, where turning it off makes the console power down automatically after 30 minutes of inactivity. Do not confuse it with the separate top level menu item that is also called DISPLAY MODE and is only a display self test.
