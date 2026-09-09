---
id: spirit-mt200-safety-outlet-and-circuit-requirement
title: Requires a 115 volt AC, 60 Hz, 20 amp grounded outlet with nothing else on the circuit
kind: policy
question: What outlet and circuit does a Spirit MT200 rehabilitation treadmill need?
asked_as:
- what outlet does this rehab treadmill need
- does the mt200 need its own circuit
- what amp breaker for a rehabilitation treadmill
- can i plug anything else into the same socket
keywords:
- outlet
- 115 volt
- 20 amp
- 60 hz
- dedicated circuit
- grounded outlet
- flat level surface
- circuit breaker
- mains supply
- protective earth
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - mt200-2010
  - mt200-2022
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-2026t-safety-outlet-and-circuit-requirement
- spirit-ct850-outlet-and-circuit-requirement
- xt-2015-safety-outlet-and-circuit-requirement
- cvc800-outlet-and-circuit-requirement
see_also:
- spirit-product-must-be-grounded
- spirit-2026t-safety-extension-cord-12-awg-or-larger
- spirit-mt200-safety-instructions-list
source:
  ref: spirit-treadmill-mt200-2010-owners-manual
  locator: Important Safety Instructions, page 4, and the Specifications page, page 42; the
    2022 owner's manual prints the same WARNING on its Important safety instructions page,
    page 5, and the same specification row on its page 67
  extracted_at: '2026-09-09'
---

Both MT200 owner's manuals state it as the WARNING header of their safety instructions page:

> To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on
> a flat level surface with access to a 115 volt AC, 60 Hz, 20-amp grounded outlet. [...] The
> treadmill should be the only appliance in the electrical circuit. Do not attempt to disable the
> grounded plug by using improper adapters, or in any way modify the cord set; a serious shock or
> fire hazard may result along with computer malfunctions.

| What | Figure |
|---|---|
| Voltage | 115 volt AC |
| Frequency | 60 Hz |
| Circuit | 20 amp, grounded |
| Sharing | nothing else on the circuit |
| Surface | flat and level |

- **115 volt, 60 Hz, 20 amp, grounded.** The 2022 manual writes `115-volt AC` with a hyphen; the
  figures are the same.
- **Nothing else on that circuit.** The manual says the treadmill should be the only appliance in
  it.
- **Never defeat the grounding pin** with an adapter and never modify the cord set. Unlike the XT
  and CT850 manuals, **these manuals give no permission for a temporary grounding adapter at all** -
  see `spirit-product-must-be-grounded`.
- The safety page adds the rule these manuals state in the same breath -
  `To avoid risk of electric shock, this equipment must only be connected to a supply main with
  protective earth`.

**The specifications page states the supply a second time**, as `Power: 115 Volts A.C., 20 Amps,
60 Hz.`, and gives the machine's own protection: a thermal circuit breaker rated **AC 125V, 20A**
with a breaking capacity of 1000A at 125 VAC, and a **1A** fuse on the inverter. The two pages
agree on the supply.

**No other Spirit machine in this knowledge base asks for 115 volt.** Do not answer an MT200 from
another family's figure, or the reverse:

| Machine | Circuit | Card |
|---|---|---|
| MT200 | 115 volt, 60 Hz, 20 amp | this card |
| 2026 4.0T, 7.0T, 8.0T | 120 volt, 60 Hz, dedicated 20 amp, NEMA 5-20P | `spirit-2026t-safety-outlet-and-circuit-requirement` |
| CT850 | 120 volt, 20 amp | `spirit-ct850-outlet-and-circuit-requirement` |
| 2015 XT treadmills | 110 volt, 15 amp | `xt-2015-safety-outlet-and-circuit-requirement` |
| CVC800 climber | 120 volt, 15 amp | `cvc800-outlet-and-circuit-requirement` |

The extension cord rule printed in the same sentence is 12 awg or larger with one outlet on the
end: `spirit-2026t-safety-extension-cord-12-awg-or-larger`.
