---
id: spirit-ent-console-screen-mirroring-limits
title: Paid TV streaming apps will not screen mirror, and the device must share the console's WiFi
kind: fact
question: Why will Netflix not screen mirror to a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill console?
asked_as:
- why wont netflix show on the treadmill screen
- screen mirroring works but the video is black
- can i watch disney plus on the treadmill
- why cant i mirror my phone to the treadmill
keywords:
- screen mirroring
- netflix
- hbo
- disney plus
- drm
- paid streaming
- same wifi
- subscription
- black screen
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
authority: 2
not_to_be_confused_with: []
see_also:
- ct800ent-2022-console-screen-mirroring-ios
- ct800ent-2022-console-screen-mirroring-android
- spirit-ent-console-wifi-setup
- spirit-ent-console-wifi-bandwidth-for-a-facility
source:
  ref: spirit-ent-console-screen-mirroring-tip
  locator: '"Screen Mirroring", one page support note, revision 07.01.2024, p. 1, the
    three numbered notes at the foot of the page'
  extracted_at: '2026-09-09'
---

**Paid TV streaming apps do not allow wireless screen mirroring.** The note names **Netflix, HBO and
Disney+** as examples and says "etc." - it is the app that refuses, not the machine, so there is
nothing to configure on the console.

Two more conditions from the same note:

- **A subscription may be required to access some apps.**
- **The device MUST be connected to the same WiFi as the console** for screen mirroring to work at
  all.

**Ethernet is not a substitute.** The companion note on connecting to the internet says WiFi is
recommended because **Ethernet will prohibit use of the screen mirroring function** - a machine
wired to the network cannot be mirrored to. See `spirit-ent-console-wifi-setup`.

**Users also have to be able to join that WiFi**, which is a facility decision rather than a console
setting: `spirit-ent-console-wifi-bandwidth-for-a-facility`.

The note offers no workaround for the paid apps. The console's own **Internet** section runs those
services on the console instead of mirroring them - see `ct800ent-2022-console-internet-apps`.
