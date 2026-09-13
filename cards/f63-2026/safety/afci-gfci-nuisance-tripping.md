---
id: f63-2026-afci-gfci-nuisance-tripping
title: Nuisance tripping on arc fault and ground fault breakers
kind: troubleshooting
question: Why does my arc fault or ground fault breaker trip when I use a Sole F63-2026?
asked_as:
- my arc fault breaker trips when i run
- gfci keeps tripping with my treadmill
- what breaker should i use for my treadmill
keywords:
- afci
- gfci
- nuisance tripping
- inrush current
- surge suppressor
- eaton
- leviton
- schneider electric
- breaker
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f63-2019
  - f63-2023
  - f63-2025
  - f63-2026
  - f65-2019
  - f65-2023
  - f80-2019
  - f80-2023
  - f85-2019
  - f85-2020
  - f85-2021
  - f85-2023
  - f89-2023
  - s77-2019
  - st90-2020
  - st90-2021
  - st90-2023
  - td80-2019
  - tt8-2019
  - tt8-2020
  - tt8-2021
  - tt8-2023
  section: safety
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f60-2016-house-breaker-trips
- f63-2026-power-outlet-requirements
- f65-2016-gfci-and-circuit-breakers
source:
  ref: sole-tm-f63-2026-owners-manual
  locator: page 3, Important Electrical Instructions. Same page in the 2019-and-later A2 owner books (electrical page PDF p. 5).
  extracted_at: '2026-09-04'
---

**Avoid AFCI/GFCI circuit breakers if possible.** These breakers may trip occasionally during exercise because of the **high inrush currents of the treadmill drive electronics and motor**. This is an issue that affects all treadmill brands.

New laws in your area may require these breakers. If you have them and are experiencing nuisance tripping:

- Check whether **any other device is plugged into the same circuit**. Examples that may also cause tripping: fluorescent lights with electronic ballasts, a coffee maker, a space heater, a hair drier.
- **Optimally the treadmill should be the only device plugged into the circuit.**

Sole treadmills have **surge suppressors built in** to help avoid nuisance tripping. The brands tested with these products are **Eaton (Cutler Hammer Series)**, **Leviton (Smart lock pro)** and **Schneider Electric (Canadian home series)**. These breakers did not trip in testing when connected to a Sole treadmill, as long as no other devices were plugged into the same circuit.

**The two manuals disagree about GFCI outlets.** The service manual card `f63-2026-power-outlet-requirements` says never to use a ground fault circuit interrupt wall outlet with this treadmill. This owner's manual says to avoid AFCI/GFCI breakers if possible and names breakers that passed testing. Neither statement corrects the other.

The house breaker tripping while the treadmill's own breaker holds is a separate case; see `f63-2026-house-breaker-trips`.

The same page, word for word, appears in the 2019-and-later A2 owner books (the 21 machines named in applies_to): F63-2019/2023/2025, F65-2019/2023, F80-2019/2023, F85-2019/2020/2021/2023, F89-2023, S77-2019, ST90-2020/2021/2023, TD80-2019 and TT8-2019/2020/2021/2023. The disagreement note above still describes only the F63-2026 service manual.
