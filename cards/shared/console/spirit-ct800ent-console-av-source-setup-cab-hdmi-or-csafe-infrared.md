---
id: spirit-ct800ent-console-av-source-setup-cab-hdmi-or-csafe-infrared
title: 'A/V Source Setup: CAB is an external HDMI TV box channel selection, C-SAFE
  is an infrared interface'
kind: fact
question: What does A/V Source Setup choose on a Spirit CT800ENT-2022 or CT850ENT-2022
  treadmill?
asked_as:
- what is cab mode on the treadmill
- how do i get the tv box to work with the treadmill
- what is the c-safe setting for
- how do i change the video source on the ent console
keywords:
- a/v source setup
- cab mode
- c-safe mode
- hdmi
- tv box
- infrared
- entertainment
- video source
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
authority: 3
not_to_be_confused_with:
- ce800ent-av-source-setup
- cu900ent-tv-switching-box-selection
see_also:
- spirit-ct800ent-console-engineering-mode-seven-submenus
- ct850-2020-c-safe-ports
source:
  ref: spirit-treadmill-ct800ent-2022-service-manual
  locator: CT800ENT section 8-8 Engineering Mode Instructions, PDF p. 51 (printed
    51); text.md lines 916-923. The CT850ENT-2022 service manual prints the same page
    word for word on its PDF p. 52, text.md lines 935-942
  extracted_at: '2026-09-11'
---

The A/V Source Setup entry of engineering mode has one sentence:

> The CAB mode is an external TV box (HDMI) channel selection / the C-SAFE mode is an infrared
> interface.

**So CAB drives an HDMI set-top box and C-SAFE drives an infrared interface.** The manual gives no
cable specification, no port location and no rule for which to pick.

The elliptical in this console family words the same two choices as protocols - "C-Safe protocol,
HDMI transfer to screen on TV" and "CAB protocol, connect a set-box" (`ce800ent-av-source-setup`) -
and the CU900ENT bike says only one of C-SAFE or CAB may be chosen
(`cu900ent-tv-switching-box-selection`). **These two treadmill books say infrared for C-SAFE, which
neither of those does.**

The physical POWER and COMM ports the C-SAFE feature uses are `ct850-2020-c-safe-ports`.

