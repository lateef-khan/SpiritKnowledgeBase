---
id: crw900-2021-errors-heart-rate-signal-drops-during-the-stroke
title: The heart rate signal drops out during the stroke, and the checks are a fresh
  belt battery, a 5.3 kHz transmitter and where the receiver sits
kind: troubleshooting
question: Why does the heart rate reading cut out while rowing on a Spirit crw900-2021
  water rower?
asked_as:
- heart rate keeps dropping out on my rowing machine
- pulse cuts in and out when i row
- what frequency chest strap does my spirit rower need
- rower loses my heart rate at the end of the stroke
keywords:
- heart rate
- chest belt
- transmitter
- 5.3 khz
- signal drops out
- receiver position
- interference
- fresh battery
- rowing stroke
facets:
  brand:
  - spirit
  product_line: rower
  model: crw900-2021
  applies_to:
  - crw900-2021
  section: errors
  code: no-code
  model_number: '900948'
authority: 3
not_to_be_confused_with:
- crw800h2o-console-shows-no-pulse-data
- spirit-wireless-chest-belt-no-pulse
see_also:
- crw800h2o-console-shows-no-pulse-data
- spirit-wireless-chest-belt-no-pulse
- spirit-rower-errors-no-error-codes-printed
source:
  ref: spirit-rower-crw900-2021-owners-manual
  locator: CRW900 HEART RATE INSTALLATION, printed page 31 (PDF page 31). The page
    was read from a 300 dpi render as well as the text layer, and the two agree, 5.3
    KHz included.
  extracted_at: '2026-09-10'
---

**The manual says a rower is a hard place to hold a heart rate signal**, and it says why:

> Maintaining a consistent signal on a rower can be a challenge due to the varying distances
> experienced during the rowing stroke between the receiver/transmitter.

That is the fault explained before it happens - the strap moves toward and away from the console
through every stroke, so a signal that would be steady on a bike breaks up here.

The three checks, in the manual's order:

1. **Make sure the batteries on your chest belt or other device are fresh.**
2. **Make sure the frequency of your transmitter is 5.3 KHz.**
3. **Move the heart rate receiver.** Environmental conditions and nearby machines interfere too, and
   the manual invites you to experiment with different receiver positions for best performance -
   the receiver is a separate part on this machine, installed with its own wiring and cable tie
   mounts.

**5.3 KHz is this machine's figure and no other Spirit rower prints it.** The CRW800H2O service
manual asks for a **5.0 KHz** chest belt (`crw800h2o-console-shows-no-pulse-data`) and the 8.5UE
ergometer says most transmitters at **5 kHz** will work. The XRW600 and CRW800 2021 owner's manuals
print no frequency at all. Quote the machine's own number; do not carry 5.0 onto a CRW900.

**No battery type is printed here.** The manual says "fresh" and stops. The Spirit commercial
machines that do name one say CR2032 (`spirit-wireless-chest-belt-no-pulse`), but this book does not,
so say so rather than assuming.

This is a signal that comes and goes. **A pulse that never appears at all**, or one displaying wild
random numbers, is a different question, and this manual prints no troubleshooting row for either -
its table has no heart rate row (`spirit-rower-errors-no-error-codes-printed`).
