---
id: cu900ent-bluetooth-pairing
title: Pairing a phone or tablet over Bluetooth
kind: procedure
question: How do I pair a phone to a Spirit CU900ENT or CR900ENT bike over Bluetooth?
asked_as:
- how do i pair my phone to the spirit bike
- bike console will not connect over bluetooth
- how do i rename the bluetooth on the console
keywords:
- bt setup
- bluetooth
- pair mode
- deleted pair
- reset
- rename bt device
- ent console
- headphone volume
- pairing
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
- cu900ent-engineering-mode-menu
- cu900ent-console-layout
- cu900ent-maintenance-menu
- ct900ent-bluetooth-pairing
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: BT Setup, p. 37 (printed 37). The CR900ENT-2021 service manual, BT Setup,
    PDF p. 37 (printed 37), text.md lines 575-604, prints the same page word for word.
    The seven buttons, the "ENT console" pairing procedure and the headphone volume
    control are word for word.
  extracted_at: '2026-09-08'
---

**BT Setup** is the seventh Settings entry. Its buttons:

| Button | What it does |
|---|---|
| (version field) | Shows the version of the Bluetooth module |
| Clear | Clears all messages on the window |
| Pair Mode | The window displays "Enter pairing mode" and waits for a connection |
| Deleted Pair | The window displays "OK" and disconnects the Bluetooth connection |
| Reset | The window displays "Bluetooth device is power on" and Bluetooth turns on again |
| Rename BT Device | Modifies the name of the Bluetooth connection; press it again to enter the new name |
| (volume) | Headphone volume control |

**Pairing procedure:**

1. Press **Pair Mode**. The window shows "Enter pairing mode".
2. On the phone or tablet, turn Bluetooth on and search for devices. The display shows
   **"ENT console"**. Select it. Both the phone and the console then start the coding request; confirm
   on both and pairing completes.

The manual gives no PIN and no timeout. It does not say whether the console pairs for audio, for
heart rate, or for both.

**The owner's manual pairs from the home screen instead, and does not mention this screen.** The
CU900ENT owner's manual (p. 18) and the CR900ENT-2021 owner's manual (p. 20) say to press the **Blue
Tooth (BT) icon on the bottom left of the screen**, then **Pair Mode** in the pop-up, and that the
phone will show the console as **A2DP** - not as "ENT console". Audio then plays **through the
headphone port on the ENT console**: `ct900ent-bluetooth-pairing`.

**A2DP is an audio profile name, which settles what the link is for on that route** - the service
manual's own volume control on this screen is labelled headphone volume. Neither document says
whether the console pairs for heart rate as well.

**The CR900ENT-2021 service manual prints this page word for word** (its PDF p. 37), so this card
covers that machine too; its owner's manual never opens engineering mode.
