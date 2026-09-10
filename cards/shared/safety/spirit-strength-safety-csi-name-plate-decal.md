---
id: spirit-strength-safety-csi-name-plate-decal
title: The i-Strength name plate says Made in Taiwan and For household use only, and its rating decal says Made in China
kind: fact
question: What is on the name plate of a Spirit i-Strength CSI-CPSP or CSI-LROW, and why does it contradict itself?
asked_as:
- what does the label on the i-strength machine say
- is the csi machine made in taiwan or china
- the label says household use but its a gym machine
- what standards does the csi machine meet
keywords:
- name plate
- rating decal
- dyaco
- made in taiwan
- made in china
- household use
- en 60335
- en iso 20957
- fcc
- load max
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-safety-serial-decal-fields-en-957-class-s-studio
see_also:
- spirit-strength-safety-user-weight-limit-350-lb
- spirit-strength-safety-csi-electrical-and-grounding-block
- spirit-strength-safety-product-labels-three-decals
- spirit-strength-safety-serial-decal-fields-en-957-class-s-studio
source:
  ref: spirit-strength-csi-cpsp-owners-manual
  locator: Rating decal and Name Plate Decal on PRODUCT LABELS, printed page 4 (PDF page 5) of the CSI-CPSP and CSI-LROW manuals, read from a 400 dpi render
  extracted_at: '2026-09-10'
---

The two i-Strength machines carry **four** labels where the rest of the range carries three, and the
two identity labels disagree with each other on three separate points.

**The name plate decal**, a bordered table:

| Field | CSI-CPSP | CSI-LROW |
|---|---|---|
| Company | Dyaco International Inc., 12F, No. 111, Songjiang Road., Taipei 10486, Taiwan. | same |
| Product | Chest Press / Shoulder Pres | Low Row |
| Trade Mark | SPIRIT | SPIRIT |
| Model | CSI-CPSP | CSI-LROW |
| Load max. | 160kg/360lb | 160kg/360lb |
| Rating | 110~220V | 110~220V |
| Standard | EN 60335-1, EN 55032, EN ISO20957-1 | same |
| Classes | Studio | Studio |
| Year of construction | 2025 | 2025 |
| | WARNING - Use the stationary training equipment in a supervised environment. | same |
| | Made in Taiwan | Made in Taiwan |

**The rating decal**, on the same page, says something different: `Model / Modèle: i-Strength`,
`Rating / Classement: 100-240V~ 50/60Hz 10A`, `Date code / Date du code: 2022.Q3`,
`Maximum Weight: 160KG`, `FCC ID: 2AHVL-CSI-PHA1`, `CLASS: SC (Gym)`,
`Test Standard: EN ISO 60335 / EN 55032 / 20957-1`, an Intertek mark, an FCC Part 15 statement, and
`For Consumer Use Only / For household use only`, `Made in China / Fabriqué en Chine`.

**The three disagreements, plainly:**

- **Country of origin.** Name plate says Made in Taiwan, rating decal says Made in China.
- **Class of use.** Rating decal says `CLASS: SC (Gym)` *and* `For household use only` on the same
  sticker; the name plate says `Classes: Studio`. The manual's own precautions page says the
  equipment is designed for a commercial or consumer environment. Treat the household-use line as a
  template leak from a residential product, not as a restriction on where the machine may be
  installed — but flag it if a warranty question turns on it.
- **Electrical rating.** 110~220V against 100-240V~ 50/60Hz 10A, with the safeguards text adding a
  third figure of 120 volts.

The date code, **2022.Q3**, is three years before the name plate's year of construction, 2025, and
four before the manual's own 2026 revision. It dates the label design, not the machine.

Both decals give the same weight, 160 kg, and both convert it to 360 lb, which the manual text does
not — the manual says 350 lb. See the weight-limit card.

All of this was read from a 400 dpi render of printed page 4; `pdftotext` returns almost nothing from
these labels.
