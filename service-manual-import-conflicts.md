# Service manual import — merged conflicts report

Twelve extraction agents processed **55 Sole service manuals** and wrote **2,643 new cards**
(repository total after the run: 3,268 cards; `kb lint` clean, `undeclared_facet_values: {}`
in all twelve groups). Per-group card counts: G1 331, G2 274, G3 182, G4 133, G5 126, G6 49,
G7 258, G8 269, G9 268, G10 171, G11 286, G12 296. The reports carry roughly **520 distinct
conflicts**: about 90 model-number/SKU problems, 140 disagreements between manuals in the same
group, 220 self-contradictions inside a single manual, and 70 places where a new manual
contradicts a card already committed. No agent resolved a conflict, edited an existing card, or
touched `sources/`, `kb.yaml` or the manifest. Everything below is presented as printed, with
both sides intact.

---

# Part 1 — Cross-cutting findings

Anything two or more agents found independently, ranked by consequence. Independent agreement is
the evidence; a pattern found by six groups is a fleet-wide print defect, not a typo.

---

## 1.1 The 3-pin incline / position sensor connector is printed in two opposite pin orders

**Found by G4, G7, G8, G9 and G11** — five groups, not four. G10 and G12 print a consistent order
inside their own groups and so found no internal conflict, but their machines fall on one side of
the split and are included below. G11 found the two S77 manuals reversing it against each other;
G8 found the F80 2016 reversed against every other manual in its group; G9 found the F65 2023
reversed against the F80/F85/F89 2023; G7 found the F63 2016/2019 reversed against the F60 2016
and F63 2023; G4 found the E25 2026 reversed against five committed 2019 elliptical cards.

Every manual prints the same framing sentence: *"Console connector wiring, these connections are
the same on the incline board and at the console"*. Pin 2 is the position signal 0~5vdc in every
single case. Only pins 1 and 3 move.

| Machine | Source / card | Locator | Pin 1 | Pin 3 |
|---|---|---|---|---|
| e25-2019 | `cards/e25-2019/errors/incline-motor-test-procedure.md` | line 53 | ground | 5vdc |
| e35-2019 | `cards/e35-2019/errors/incline-motor-test-procedure.md` | line 53 | ground | 5vdc |
| e55-2019 | `cards/e55-2019/errors/incline-motor-test-procedure.md` | line 53 | ground | 5vdc |
| e98-2019 | `cards/e98-2019/errors/incline-motor-test-procedure.md` | line 53 | ground | 5vdc |
| e95s-2019 (stride) | `cards/e95s-2019/errors/stride-motor-test-procedure.md` | line 53 | ground | 5vdc |
| **e25-2026** | `sole-elliptical-e25-2026-service-manual` | lines 522-524 | **5vdc** | **ground** |
| f60-2016 | `sole-tm-f60-2016-service-manual` | p50, lines 897-899 | ground | +5V |
| **f63-2016** | `sole-tm-f63-2016-service-manual` | p59, lines 914-916 | **5vdc** | **ground** |
| **f63-2019** | `sole-tm-f63-2019-service-manual` | p59 | **5vdc** | **ground** |
| f63-2023 | `sole-tm-f63-2023-service-manual` | p28, lines 564-566 | ground | 5vdc |
| **f65-2016** | `sole-tm-f65-2016-service-manual` | lines 910-912 | **5vdc** | **ground** |
| **f65-2019** | `sole-tm-f65-2019-service-manual` | lines 907-909 | **5vdc** | **ground** |
| **f65-2023** | `sole-tm-f65-2023-service-manual` | §8.4 step 7, p29, lines 574-576 | **5VDC** | **Ground** |
| f80-2016 | `sole-tm-f80-2016-service-manual` | lines 761-763 | ground | 5vdc |
| **f80-2019** | `sole-tm-f80-2019-service-manual` | lines 716-718 | **5vdc** | **ground** |
| f80-2023 | `sole-tm-f80-2023-service-manual` | §8.4, p42, lines 686-688 | ground | 5vdc |
| f85-2023 | `sole-tm-f85-2023-service-manual` | §8.4, p43, lines 706-708 | ground | 5vdc |
| f89-2023 | `sole-tm-f89-2023-service-manual` | §8.4, p43, lines 707-709 | ground | 5vdc |
| f85-2016 / f85-2019 / f85-2021 | the three F85 manuals | nine-step incline test, all three | ground | 5 vdc |
| **s77-2019** | `sole-tm-s77-2019-service-manual` | p49 | **5vdc** | **ground** |
| s77-2016 | `sole-tm-s77-2016-service-manual` | p50 | ground | 5vdc |
| tt8-2016 / -2016-ac / -2019 / -2019-ac / -2023 | all five TT8 manuals | position sensor wiring | ground | 5 Vdc |

**The wire-colour legend splits the same way.** `sole-tm-f80-2016-service-manual` lines 715-718:
*"Black = 5vdc, White = Position signal, Red = Ground, (0~5v depending on incline position)"*.
`sole-tm-f65-2016-service-manual` lines 859-861, and the same in f65-2019 and f80-2019:
*"GND / SENSOR PIN (AD) / +5V VCC"*. Both S77 manuals give identical motor-end colours (black =
ground, white = signal, red = 5vdc), so colour cannot break the tie there (G11 §2.1).

**Decision forced:** ring out one connector on one machine of each family and declare a house
order, or accept that the order is genuinely per-model and require every card to name its own
manual. A technician using the F65 pinout on an F80 2016 reads 5 V as ground (G8 §2.6).

---

## 1.2 The E6 troubleshooting table prints the E4 remedy

**Found by G7, G8, G9, G10, G11 and G12** — six groups, across the whole DC treadmill range and
the 2023 TT8. E6 is defined as *"The lower controller component is fault, Like Transistor、IGBT、
control module…etc."* and its own table then reads **"Insert power wire of motor."**, which is E4's
remedy verbatim.

| Manual | Locator | E6 lower-controller cell |
|---|---|---|
| `sole-tm-f63-2016-service-manual` | p55 | `Insert power wire of motor.` |
| `sole-tm-f63-2019-service-manual` | p55 | `Replace Lower controller board.` |
| `sole-tm-f60-2020-service-manual` | p52 | `Insert power wire of motor.` |
| `sole-tm-f63-2023-service-manual` | p31 | `Insert power wire of motor.` |
| `sole-tm-f65-2016-service-manual` | line 1055 | `Insert power wire of motor.` |
| `sole-tm-f65-2019-service-manual` | line 1075 | `Replace Lower controller board.` |
| `sole-tm-f80-2016-service-manual` | line 865 | `Insert power wire of motor.` |
| `sole-tm-f80-2019-service-manual` | line 821 | `Replace Lower controller board.` |
| `sole-tm-f65-2023` / `-f80-2023` / `-f85-2023` / `-f89-2023` | §8.7 (F65 lines 643-645, F80 762-764, F85 782-784, F89 783-785) | `Controller \| Insert power wire of motor.` |
| `sole-tm-f85-2016-service-manual` | §8.6, p56 | `Insert power wire of motor.` |
| `sole-tm-f85-2019-service-manual` | §8.6, p73 | `Replace Lower controller board.` |
| `sole-tm-f85-ent-2021-service-manual` | §8.7, pp65-66 | `Insert power wire of motor.` |
| `sole-tm-s77-2016-service-manual` | p56 | `Insert power wire of motor.` |
| `sole-tm-s77-2019-service-manual` | p55 | `Replace Lower controller board.` |
| `sole-tm-tt8-2023-service-manual` | §8.7, p50 | `Insert power wire of motor.` |

**The 2019 manuals are the corrected ones** (G7 §2.14, G8 §2.5, G11 §2.2 all say so
independently), and the 2021 and 2023 books reverted to the broken text.

**The same defect at E4 and E5.** E4's lower-controller cell gains *"or Replace Lower controller
board"* only in the 2019 books (G7 §2.14, G8 §2.4, G11 §2.2). E5's table names a cable under the
heading of a board — *"Lower controller board | Replace main control wire."* — in all four 2023
manuals (G9 §2b.7: F65 §8.6 p31 lines 622-625, F80 738-741, F85 758-761, F89 759-762), in
f85-2016 §8.5 p55 and in f85-2021 §8.6 pp63-64 (G10 §2b.1.7, §2b.3.8).

**Decision forced:** does the KB print E6's remedy as the manual has it, or as the 2019 correction
has it? Every E6 card in 258 + 269 + 268 + 171 + 286 + 296 cards currently carries the printed text.

---

## 1.3 Existing shared error-code cards contradict the service manuals

**Found by G1, G5, G7, G8, G9, G10, G11 and G12** — eight groups, not four. Every one of these
shared cards is `authority: 2` or `3` with `applies_to: ['*']` or a wide list, so it already
answers for machines whose authority-3 service manual says something else.

| Shared card | What it says | What the manuals say | Groups |
|---|---|---|---|
| `cards/shared/errors/e7-external-voltage.md` (`sole-e7-error`) | "It should be about **120V AC** all the way to the motor controller." | "Use Multi-meter transform into AC 1000V to check wall outlet volt whether **110ACV or 220AC** or not." — f63-2016 p56, f65-2016 l.1092-1093, f80-2019 l.839-840, f65-2023 §8.8 p33 l.665-666, f80-2023 §8.8 p46 l.787-788, f85/f89-2023 p47 | G7 §3.7, G8 §3.6, G9 §3.1 |
| `cards/shared/errors/e8-controller-eeprom.md` (`sole-e8-error`, `applies_to: ['*']`) and `cards/shared/errors/dc-controller-error-code-list.md` | Claims an **E8** = "Controller EEPROM malfunction", and scopes itself "Applies to the F63, F65, F80, F85, F89 and TT8" | **No service manual in the batch prints E8.** F63 2016/2019/2023 list E0-E7 (p36/p36/p19); F65/F80/F85/F89 2023 list E1-E7 (F65 l.364-373, F80 l.462-472, F85 l.473-483, F89 l.474-484); all three F85 manuals stop at E7 (2016 p36, 2019 p53, 2021 p39) | G7 §3.1, G9 §3.2, G10 §3.6 |
| The same DC list | Omits **E0** entirely (has a "Safety Key" row instead) | E0 = "Safety keys dose not insert the safety module. Or safety module is broken." — printed as a code in F63 2016/2019/2023, F65 2023 l.365, all four G8 manuals, all three F85 manuals, both S77, TT8 2016/2019 | G7 §3.1, G8 §3.9, G9 §3.3, G10 §6.8 |
| `cards/shared/errors/e1-no-speed-signal.md` (`sole-e1-error`, authority 2) | "**the controller** read no signal from the speed sensor" | "E1 **Display board CPU** did not receive the RPM signal." — F65-2023 l.366, F80 l.465, F85 l.476, F89 l.477. Changes which board a technician suspects. | G9 §3.4 |
| `cards/shared/errors/e4-drive-motor-voltage.md` (`sole-e4-error`) | "abnormal **voltage** at the motor terminals, or a problem with the motor wiring" | "E4 Power wire of motor error." / cause: "Power wire of Motor does not insert lower controller." The manual never mentions voltage. | G8 §3.7 |
| `cards/shared/errors/ls-error.md` (`sole-ls-error`) | "This error only happens on **2016 and older** treadmills." | `sole-tm-f65-2019-service-manual` line 1427 prints "LS1/LOW SPEED" in a 2019 manual | G8 §3.4 |
| `cards/shared/errors/e2-overcurrent.md` + `e3-incline.md` | "This is E2 on a 2016 or newer machine. On a machine built before 2016 this same fault shows as E3" | Half-fails on `sole-tm-f60-2016-service-manual` p36, which has **no E3 at all**; its incline fault is `ER` — "The console didn't receive Incline feedback signal, ER will be appeared at incline window, but the treadmill able be operate." A customer saying "ER" reaches no card. Confirmed correct for G8 and G11's machines. | G7 §3.2 (contradiction); G8 §3.8, G10 §3.7, G11 §3.4 (confirmations) |
| `cards/shared/errors/e1-no-speed-signal.md`, `e2-overcurrent.md`, `e3-incline.md` (all `product_line: treadmill`, `model: '*'`, `applies_to: ['*']`) | E1 = no speed signal, E2 = overcurrent, E3 = incline motor | On the 2016 **ellipticals** E1 = EEPROM failure (replace the upper controller), E2 = tension motor does not move on a level key press, E3 = console board not detecting incline VR voltage / "RAMP ERROR" | G1 §3.5 |
| `cards/sole/errors/ac-inverter-error-code-list.md` (`sole-inverter-error-code-list`, authority 3, `applies_to: [st90, tt9]`) | `E-25H` "Check the 2-pin control cable is intact"; `E-06H` "replace inverter"; `E-21H` "follow inverter troubleshooting"; **`E3 red` = front incline, `E3 green` = rear incline**; carries `E-0CH, E-26H, E-27H, E-28H, E-41H, E-42H, E-53H` | ST90 manuals: `E-25H` "Safety key pulled, please attach safety key"; `E-06H` "Please check Braking resistor."; `E-21H` "Please lubricate running belt or check for bad bearing"; `E-3H` incline error, **no colour split**. TT8 AC manuals §8.1 pp36-38: `E-25H` "Check if the motor current is too high"; `E-53H` = **front** incline motor error, bare `E3` = **rear** incline motor error — the opposite binding to the card's red/green | G11 §3.1, G12 §3.1 |
| `cards/shared/errors/bike-eeprom-error.md` (`sole-bike-eeprom-error`, `model: '*'`) | "**Fix:** replace the upper controller." | "The EEPROM is abnormal, please replace the **Display Board** directly." — b94-2023 l.320, r92-2023 l.318, lcb-2023 l.281, lcr-2023 l.288, sb1200-2023 l.248 | G5 §3.3 |
| `cards/shared/errors/lwr-not-match.md` (`sole-lwr-not-match`, authority 2) | Fix = tap **Settings** repeatedly, scroll to **Machine Type**, select the correct model | §8.3/§7.3: "1. Check driver board controller number is **CS51005-11S** [E35/E95s] / **CS51005-21S** [E95/E98] / **CS51012** [LCB, LCR] / **CS51006-02** [SB1200]. 2. Replace upper controller." | G3 §3.6, G5 §1.3, §2.4 |
| `cards/shared/errors/safety-key-not-detected.md` | Carries `code: safety-key`, never mentions E0 | See E0 row above | G8 §3.9 |

**Decision forced:** the shared error cards were written from support notes and console tables, not
from service manuals. Either they are re-scoped by generation and controller family, or the
authority-3 per-model cards will lose to them on any query that does not filter by model year.

---

## 1.4 Shared cards misclassify which machines have touchscreens — and they are wrong in both directions

**Found by G3, G10 and G12.** This decides which Garmin pairing procedure a customer is given.
Verified in the repo: `cards/shared/console/garmin-pair-touchscreen.md` lists `f85-2019`,
`f85-2020`, `f85-2021`, `st90-2020`, `st90-2021`, `tt8-2019`, `tt8-2020` among others;
`cards/shared/console/garmin-pair-non-touchscreen.md` lists the year-less `e35`, `e95`, `e95s`,
`e98`, plus `f63-2026`, `f65-2026`, `f80-2026`, `f83-2026`.

| Machine | Currently filed as | Manual evidence | Should be | Group |
|---|---|---|---|---|
| e35-2023, e95-2023, e95s-2023, e98-2023 | not listed at all; the year-less `e35`/`e95`/`e95s`/`e98` sit on the **non**-touchscreen card, whose scope note reads *"The SOLE non-touchscreen cardio machines … because no source document enumerates the non-touchscreen fleet"* | identical line in all four: **"Console  Contain keys control and TFT LCD touch panel."** — e35 p6, e95 p6, e95s p7, e98 p6. §4.2 describes a Wi-Fi page, a brightness slider, media apps, a passcode; §8.5 is entered by pressing the word "Settings" ten times **on the screen** | **touchscreen** | G3 §3.5 |
| e25-2023 | as above | p5: **"Console  It is including keypad to control and LCD Display."** Error set is `E1 / E2 / E3`, not `EEPROM ERR / LWR not found / LWR not match` | **non-touchscreen** (correct as-is; must **not** gain the touchscreen cards) | G3 §3.5, §2.7 |
| **f85-2019** | on the **touchscreen** cards, and on `sole-media-apps-2020-touchscreen` as *"the first generation 2020 touchscreen … which run Android 6 … the F85 (SKU 585818)"* | `sole-tm-f85-2019-service-manual` §4, p32: **`10.1” TFT PANNEL`** — no "TOUCH". §4 READY/RUN MODE pp36-37 give **ENTER**, **PROGRAM**, FAST, SLOW, UP, DOWN, DISPLAY, FAN as physical buttons: *"PROGRAM KEY：Press PROGRAM keys (▲/▼) to choose"*. For contrast `sole-tm-f85-ent-2021-service-manual` p16 does say `10.1” TFT TOUCH PANNEL` and p20 *"Touch panel button"*, *"Touch FAST button"* | **unresolved — possibly non-touchscreen** | G10 §3.1 |
| **tt8-2019** | on the **touchscreen** cards and on `sole-media-apps-2020-touchscreen` | `sole-tm-tt8-2019-service-manual` p13 and `sole-tm-tt8-2019-ac-service-manual` p15 both document a **button console with a 10.1" TFT panel** and a physical **BLE** key (*"BLE button: When use the BLE wireless chest strap，in ready mode press one time and it will be turn on"*) — no touch input, no app menu, no pairing screen | **unresolved — possibly non-touchscreen** | G12 §3.3 |
| f85-2021 | on the touchscreen cards, and also reached by `cards/shared/console/engineering-menu-non-touchscreen.md` because that card is `applies_to: ['*']` | the 2021 manual is a touchscreen, so the non-touchscreen engineering card is wrong for it on two counts: it says sleep is "15 to 30 minutes" (manual: exactly **30 minutes**, p73) and that child lock unlocks with **Start and Enter** (manual §8.10 p73: **"press START & DISPLAY key within 2 seconds"**) | touchscreen, but the wildcard card must be excluded | G10 §3.5 |

**Note the disagreement between agents.** G3 wants four ellipticals **moved onto** the touchscreen
list; G10 and G12 want two treadmills **examined for removal** from it. Both may be right — the
lists were built by elimination, not from a source.

---

## 1.5 One model id per machine is not holding — in both directions

**Found by G1, G2, G5, G9, G10, G11 and G12.**

### Two ids, one machine

| Ids | Machine | Evidence | Group |
|---|---|---|---|
| `f85-2020` / `f85-2021` | SKU **585820** | Only unclaimed F85 SKU between 2019 and 2023 (`sources/spirit-models-sole-treadmills/text.md` lines 76-79). `cards/sole/console/software-2-0-to-2-4-update.md` (`f85-software-2-0-to-2-4-update`) already states *"Applies to the F85, SKU 585820, which is called both the 2020 and the 2021 machine"* and its `applies_to` is `[f85-2020, f85-2021]`. Before the run both ids carried an **identical** set of five cards; no fact is asserted of one and denied of the other. **G10's conclusion: merge, with `f85-2020` surviving.** | G10 §1.1 |
| `st90` / `st90-2020` / `st90-2021` | SKU **590820** | `sources/spirit-models-sole-treadmills/text.md` line 94: `\| 590820 \| SOLE ST90 2021 \|`; line 95 is `590822 SOLE ST90 2023`. There is no 590819 and no 590821. `cards/sole/console/media-apps-2020-touchscreen.md`: *"The machines are the F85 (SKU 585818), the ST90 (SKU 590820) and the TT8 (SKU 588818). **The ST90 is called both 2020 and 2021**"*. All five cards naming `st90-2020` also name `st90-2021`. Every part `st90-parts-and-wiring` names (2HP inverter, bearing seat, crawler belt with pedals/slats, filter, incline motor, key fast board covers) is in the 2021 manual, so the bare `st90` is very probably a third alias. | G11 §1.1, §3.2 |
| `sb1200` / `sb1200-2023` | SKU **512322** | `sources/spirit-models-sole-bikes/text.md` line 22 is the **only** SB1200 row. `kb.yaml` declares both ids (lines 98-99). Five existing cards name the bare `sb1200` in `applies_to` — `sole-garmin-pair-non-touchscreen`, `sole-plus-strava-sync`, `sole-lwr-not-match`, `sole-heart-rate-monitor-other-brands`, `sole-garmin-supported-watches-broadcast` — so a retrieval filtered on `sb1200-2023` misses all five. | G5 §1.3 |

`kb.yaml` lines 81-83, 98-99 and 109-112 declare all of these side by side.

### One SKU, two machines — the inverse, and more dangerous

| SKU | Two machines | Group |
|---|---|---|
| **588816** `SOLE TT8 2016` (treadmills line 86) | **ST925-YT021 (DC drive motor)** and **ST925A-YT030 (AC drive motor on an inverter)**. `sole-tm-tt8-2016-ac-service-manual` is UNRESOLVED — no second row exists. The two machines have **entirely different error code sets** (`E0…E7` vs `E-01H…E-53H`). A technician searching "TT8 2016" or "588816" cannot learn the drive type from the SKU. | G12 §1.1 |
| **588818** `SOLE TT8 2019` (line 87) | **ST928-YT035 (DC)** and **ST928A-YT037 (AC)**. Same problem. | G12 §1.2 |

### Two SKUs in the KB for one machine, only one of which exists

`f89-2023`: `cards/sole/console/start-button-grayed-2023.md` line 36 says *"Applies to the 2023
F85 (585822), F89 (**589822**) and TT8 (588822)"*. **`dbo.Models` has no 589822 row.** The database
F89 row is `sources/spirit-models-sole-treadmills/text.md` line 93: `| 589853 | SOLE F89 |`
(G9 §1.3). See Part 4.

### The SC200 is filed under two SKUs and two ModelTypes

`sources/spirit-models-sole-ellipticals/text.md` lines 23-24 (duplicated verbatim at
`sources/spirit-models-sole-climbers/text.md` lines 19-20):

```
| 520516 | SOLE SC200 | Stepper    | Sole |
| 520517 | SC200      | Elliptical | Sole |
```

Neither row carries a year, so `sc200-2016` = 520516 rests on the digits alone, `sc200-2019` is
UNRESOLVED, and the row that is typed `Elliptical` is 520517, whose digits say 2017 (G1 §1.4,
G2 §1.1). Both agents wrote `product_line: elliptical` as instructed and both objected — see
Part 2, decision 1.

---

## 1.6 "The last two digits of the model number are the model year" fails across nine groups

**Found by G1, G2, G3, G4, G5, G7, G9, G11 and G12.** The rule is asserted in
`sources/spirit-models-sole-bikes/text.md` line 51 and in the shared card
`sole-bike-service-manual-model-numbers`. It does not hold for the 2019 or 2023 model years at all.

| SKU | `ModelName` | Digits imply | Group |
|---|---|---|---|
| 525018 / 535018 / 555018 / 595618 / 598018 | Sole E25 2019 / E35 2019 / E55 2019 / E95S 2019 / E98 2019 | 2018, all five | G2 §1.2 |
| 563818 | SOLE F63 2019 | 2018 | G7 §1.3 |
| 563822 | SOLE F63 2023 | 2022 | G7 §1.4 |
| 555922 | SOLE SR550 2023 | 2022 | G4 §1.4 |
| 500918 | SR500 2019 | 2018 | G4 §1.4 |
| 577818 | SOLE S77 2019 | 2018 | G11 §1.2 |
| 590820 | SOLE ST90 2021 | 2020 | G11 §1.2 |
| 590822 | SOLE ST90 2023 | 2022 | G11 §1.2 |
| 588818 | SOLE TT8 2019 | 2018 | G12 §1.4 |
| 588822 | SOLE TT8 2023 | 2022 | G12 §1.4 |
| 565822 / 580822 / 585822 | SOLE F65 2023 / F80 2023 / F85 (no year) | 2022, all three | G9 §1.5 |
| **590321** | **SOLE SB900 2022** | 2021 — the reverse direction | G5 §1.4 |
| **589853** | SOLE F89 (no year) | **53 is not a year at all** | G9 §1.2 |

**And the ModelName is silent where the manual is not.** `595022 | SOLE E95` against cover
`E95(2023) SE698-SE040` (G3 §1.1); `594122 | SOLE B94` against cover `B94(2023)` (G5 §1.1);
`512322 | SB1200` with **no year in the database and none on the cover** (G5 §1.2);
`585822 | SOLE F85` against cover `F85(2023)` (G9 §1.4); `560816 | F60` bare, where every other
F60 row is named with a year (G7 §1.5); `598012 / 598015 / 598016` all named `SOLE E98`, so
nothing distinguishes the 2012, 2015 and 2016 machines by name (G1 §1.3).

**Decision forced:** the digits are the *release* year and `ModelName` the *model* year, or one of
the two is systematically wrong. Nine groups hit this; it is not per-model noise.

---

## 1.7 Most manuals never print their own Sole model name or six-digit SKU

**Found by G1, G7, G8, G9, G10 and G11.** The tie from PDF to SKU rests on the file name and the
manifest, not on the document.

| Group | Finding |
|---|---|
| G1 §1 | **No manual in the seven 2016 ellipticals prints a six-digit SKU anywhere.** Only factory codes: SE565S-SE016, SE575-SE017, SE585S-SE018, SE595-YE021, SE865-YE023, XE895A-YE022, XS110A-YS003. Two covers do not even name the machine: the E95S manual's ToC heads section 1 *"Elliptical Outlines"* and **no "E95S" string appears anywhere**; the SC200 manual's ToC heads it *"Outlines"* and **no "SC200" string appears anywhere**. |
| G7 §1.6 | Four of six manuals never name a Sole model or SKU: `f60-2016` = `AT90I-NT007`, `f60-2020` = `AT90P-NT038`, `f63-2016` = `ST125`, `f63-2019` = `ST128-YT043`. `sole-tm-f60-2020-service-manual` contains no "F60", no "560820" and no six-digit number in 1,384 lines. |
| G8 §1.1 | None of the four contains 565816, 565818, 580816 or 580818. The 2019 SKUs are corroborated only by `origin_uri`; the 2016 file names carry factory codes instead. |
| G9 §1.1 | `sole-tm-f89-2023-service-manual` prints **no six-digit SKU anywhere**. |
| G10 §1.3 | The strings "F85", "ENT" and "2021" appear **only in the file name** `ST538-YT056 (SOLE F85 ENT 2021) Service Manual.pdf`, never in the body. Every heading reads ST535 or ST538. |
| G11 §1.3 | Full-text scan: `sole-tm-s77-2016-service-manual` = **0 occurrences of "S77"** (`ST725` ×7, `ST535` ×1); `sole-tm-s77-2019-service-manual` = **0 occurrences of "S77"** (`ST728` ×6). The `YT020` and `YT034` codes in the manifest titles appear **nowhere** in either text. |

**Cover codes also disagree with their own bodies:** e25-2019 cover `SE665S-SE012` vs circuit
diagram line 811 `SE665S-SE016` (G2 §1.3); e98-2019 cover `SE855-YE029-01` vs ToC line 9
`1. SE865 Elliptical Outlines` (G2 §1.4); f65-2016 cover `ST155` vs ToC line 5
`1. ST125 Treadmill Outlines` (G8 §1.2); st90-2023 cover `ST8910-YT067` vs p10 heading
`6.1 INVERTER Component Locations (YT061)` — the previous ST90's code (G11 §1.4); s77-2016 p4
heading *"Special Note on **ST725** CE version"* over the sentence *"Besides normal version,
**ST535** treadmill is with a CE version"* (G11 §1.5), the identical fault in
`sole-tm-tt8-2016-service-manual` p4 (heading ST925, body ST535 — G12 §2b a) and in
`sole-tm-f85-ent-2021-service-manual` p4 (heading ST538, body ST535 — G10 §2b.3.1).

---

## 1.8 Belt tension is stated in four different units and the values do not reconcile

**Found by G1 and G5 as conflicts; G2, G4, G7, G8, G9, G10, G11 and G12 supply the rest of the
fleet picture.** There are four independent belt families and the numbers cross between them.

**Hz — ellipticals and light-commercial bikes**

| Machine | Locator | Printed |
|---|---|---|
| `sole-elliptical-e98-2016-service-manual` | §11-8 step 3, p86 | **"170HZ(±10)"** |
| e25 / e35 / e55 / e95 / e95s / sc200 2016 | §11.6/11-8/9-9 step 3 | **190 Hz (+/- 10)**, all six |
| `cards/e98-2019/specs/drive-belt-tension.md` | §11-8 step 3, p84 | **"190HZ(+/-10)"** |
| All five 2023 ellipticals + CC81 climber cards | — | **190 Hz (+/- 10 Hz)** |
| `sole-bike-lcb-2023-service-manual` | §9.8 step 4 p29 (l.499) and §10.2 step 2 p33 (l.564) | **"within the range of180~205HZ"** |
| `sole-bike-lcr-2023-service-manual` | §9.5 step 5, p29 (l.472) | **"within the range of180±10HZ"** |
| `cards/lcr-2016/specs/belt-tension.md`, `cards/lcb-2019/…`, `cards/lcb-2016/…` | — | **180 to 205 Hz** |

The E98 2016 is the only machine at **170 Hz**; every sibling and the 2019 E98 print 190. G1 §6.3:
*"reads like a typo … I did not change it."* 180 ± 10 Hz is 170-190; it overlaps 180-205 only
between 180 and 190 (G5 §2.1, §3.1). The LCB and LCR are the **same belt system** — J-bolt
tensioned idle arm, generator flywheel, audio tension gauge, M8 x 7T nut, 13 mm wrench.

**Newtons — bikes**

`cards/b94-2019/specs/belt-tension.md` and `cards/r92-2016/specs/belt-tension.md`: **450 Newton**.
`cards/sb700-2019/specs/belt-tension.md`: **700 to 750 Newton**. `cards/sb700-2020/…`: *"700 to
750 Newton is the standard setting. If the belt still slips after it has been set to 700 N, take it
up to **1000 N**."* `cards/sb900-2020/…`: **1000 Newton**. `b94-2023` line 624 and `r92-2023` line
640-641 both print **450N** with a dangling reference — *"(Remark)"* and *"(Note 1)"* — to a
paragraph that does not exist; the B94 **2016** manual's Remark gives **540 N for a brand new belt**
(G5 §2b(h),(i)).

**Pounds — spin bikes, new in 2023**

`sole-bike-sb1200-2023-service-manual` §8.4 STEP 3 p22 (l.398) and
`sole-bike-sb900-2023-service-manual` §6.4 STEP 3 p17 (l.369), identical: *"pay special attention
to ensuring that the belt tension is at **180 lbs**."* This is a **unit change**, not just a value
change: 180 lbf is about 800 N, between the SB700 figure and the SB900 2020 figure. Neither manual
names a gauge type and neither has a belt-slipping section (G5 §2.2, §3.2).

**Pounds — treadmills and rowers, stable**

**70-75 LBS** in the white zone with a **14 mm open end wrench** and a tension measuring device —
identical in all six G7 manuals, all four G8 manuals, all four G9 manuals, all three G10 manuals
and both S77 manuals. **Exception:** `sole-tm-f63-2026-service-manual` p58 uses a **13 mm wrench**
for the same 70-75 lbs (G7 §2.12). Both rowers: `6PJ-787L` (part 24) at **70~80BLS** — SR500
l.635-636, SR550 l.473-474 (G4 §2.6).

**Unit confusion inside one manual:** `r92-2023` §10.2 l.840 — *"turn M8×7T Nyloc Nut (88)
clockwise until **sound wave frequency** falls between **450N**"*, a frequency reading with a force
unit, reprinting the identical defect the `r92-2016-belt-tension` card already records.
`lcr-2023` §10.2 l.687 does the same (G5 §2b(j),(y)).

---

## 1.9 The drive motor M- wire is white in one paragraph and black three lines later

**Found by G7, G8, G9, G10, G11 and G12** — six groups. The paragraph names three wires and then
uses a fourth colour.

| Manual | Locator | Printed |
|---|---|---|
| `sole-tm-f63-2016-service-manual` | p11, l.179 | *"Requires three wire connection: red, black, and green."* then **"The White wire is inserted into M-."** |
| `sole-tm-f63-2019-service-manual` | p11, l.171 | **"The Black wire is inserted into M-."** |
| `sole-tm-f63-2023-service-manual` | p6, l.97 | **"The White wire is inserted into M-."** — while p40 says `Red to M+ / Black to M-` |
| `sole-tm-f65-2016` and `-f65-2019` | l.169-171 | *"red, black and green. The Red wire is inserted into M+. The **White** wire is inserted into M-."* |
| `sole-tm-f80-2016-service-manual` | l.190 | *"If there is DC voltage on the **Red (white)** wire (M+)"* |
| `sole-tm-f65-2023-service-manual` | p6, l.102-105 | *"three wire connection: red, black, and green. / The Red wire is inserted into M+. / The **White** wire is inserted into M-."* |
| `sole-tm-f80-2023` / `-f85-2023` / `-f89-2023` | p6/7, l.100-101 | *"DC voltage on the **Red (white)** wire (M+) … Black wire (M-)"* |
| `sole-tm-f85-2016-service-manual` | §3, p13 | *"Red (white) wire (M+)"* against pp78, 81, 83 *"(red M+, black M-)"* |
| `sole-tm-s77-2016-service-manual` | p13 | *"Red (white) wire (M+)"*, motor *"Have three wires red, black and green"*, §11-3 p75 *"motor wire (+) red"* / *"(-) black"* |
| `sole-tm-tt8-2016-ac-service-manual` | p13 vs §12-3 p58-59 | p13: AC motor, *"three wires **red, white and black** for power … green wire is grounding"*. §12-3 step 4: *"(**red M+, black M-**)"* — **M+/M- do not exist on this motor as described** |
| `sole-tm-tt8-2019-ac-service-manual` | p13 vs §11-3 pp56-57 | identical fault |

**Every replacement procedure in every manual says red = M+, black = M-.** Only the General
Information paragraph says white.

**And the incline motor wire count contradicts itself the same way** — four wires or five for the
same four colours (G8 §2.13, G9 §2.3, G10 §2b.2.1, G11 §2.5):

- `sole-tm-f80-2016-service-manual` l.188-197 / `f85-2016` §3 p13 / `s77-2016` p13:
  *"Have **four wires**, red, black, white and green."*
- `f65-2016` l.169-178 / `f65-2019` / `f80-2019` l.142-150 / `f65-2023` p6 l.109 / `f85-2019`
  §3 p30 / `s77-2019` p12: *"All of **five wire connection**: red, black, white, green, and has one
  of 3 pins cable for position sensor."* — **five claimed, four named.**

---

## 1.10 The incline motor stroke / zeroing figure has ten values across the fleet

**Found by G1, G2, G3, G4, G7, G8, G9, G10, G11 and G12** — all but G5 and G6. This is a
fit-critical number: set it wrong and the motor will not install.

**Treadmills — "Incline Range must be adjusted to X minimum prior to installation"**

| Value | Machines | Locator |
|---|---|---|
| **195 mm** | f60-2016 (p84), f60-2020 (p79), f63-2023 (p43), f80-2023 (§9.9 p61 l.1118) | *"The zeroing distance is 195mm."* / *"To adjust spare Incline motor to lower (195mm)."* |
| **200 mm** | f63-2026 (p64) | *"Set the incline motor to the lowest stroke position: 200 mm (Operating range: 200–300 mm)"* |
| **205 mm** | f85-2023 §9.10 p64 l.1162, f89-2023 l.1163 — **rear** incline motor | |
| **210 mm** | tt8-2016-ac §12-10 p69, tt8-2019 §11-10 p85, tt8-2019-ac §11-10 p67 — **rear** incline motor | |
| **220 mm** | tt8-2023 §9.10 p68 — **rear** incline motor | |
| **225 mm** | f63-2016 (pp67, 79), f63-2019 (pp66, 80), f65-2016 l.1461-1462, f65-2019, f80-2016, f80-2019 l.1239, f65-2023 §9.9 p44 l.935, f85-2023 §9.9 p62 l.1138, f89-2023 l.1139, f85-2016/2019/2021 (all three), s77-2016, s77-2019 (twice each), tt8-2016-ac **§11 p53**, tt8-2023 §9.9 p66 | |
| **235 mm** | tt8-2016 §10 p72, tt8-2016-ac **§12-9 p67**, tt8-2019 §10 p69, tt8-2019-ac §10 p51 | |

`sole-tm-tt8-2016-ac-service-manual` prints **both 225 mm (§11 p53) and 235 mm (§12-9 step 2 p67)**
for the same motor, with matching diagram callouts (G12 §2b a).

**Ellipticals — the zeroing distance between the two hole sites**

| Value | Machines | Locator |
|---|---|---|
| **207 ± 1 mm** | e35-2016 §9-7 step 2 p72, e95-2016 §9-7 step 2 p71, e98-2016 §9-7 step 2 p64, e25-2019 l.1448, e35-2019 l.1067-1068, e98-2019 l.885-887, e25-2023 §9.11 STEP 8 p35, **and e95-2023 §10.6 b) p39 and e98-2023 §10.6 b) p39** | *"rotate the incline barrel clockwise to the end and then rotate the same barrel counterclockwise in **one and a half circle**. Make sure the distance of two holes sites is 207±1mm."* |
| **206 ± 1 mm** | e35-2023 §9.11 STEP 8 p31, **e95-2023 §9.13 STEP 8 p33**, **e98-2023 §9.12 STEP 8 p33**, e25-2026 l.812-813 | |
| **245 ± 1 mm** | e95s-2016 (step 3 p64), e95s-2019 l.1023-1024, e95s-2023 §10.6 c) p59 — a **stride** mechanism, *"two and half circles"* | |
| **not printed at all** | e25-2016, e55-2016, e55-2019 | genuine absence |

**The E95 and E98 2023 manuals each print both 206 and 207 for the same operation**, in §9.x and
§10.6, one millimetre apart with a ±1 mm tolerance, so the two windows only just touch (G3 §2b.3).
The E25 and E35 2023 manuals are otherwise byte-identical through the whole of section 9, and
**this figure is the only substantive difference between them** (G3 §2.1). The e25-2026's 206 mm
also contradicts the committed `cards/e25-2019/assembly/incline-motor-replacement.md` at 207 mm,
and `cards/e35-2019/…` and `cards/e98-2019/maintenance/incline-motor-not-working.md` at 207 ± 1 mm
(G4 §3.3, G3 §3.7).

---

## 1.11 Sleep mode: two settings, opposite polarity, 15 minutes or 30

**Found by G3, G4, G5, G9, G10, G11 and G12** — seven groups. Two independently named switches
claim to govern the same behaviour, and the manual states the polarity both ways.

| Manual | The two statements |
|---|---|
| `sole-elliptical-e25-2023-service-manual` | Window Display Mode p6: *"it will enter sleep mode if there is no key press for **15 minutes**"* / §8.5 p28: *"III. Sleep Mode - **Turn off** to have the console power down automatically after **30 minutes** of inactivity."* |
| `sole-elliptical-e25-2026-service-manual` | p9 l.181-182: *"**ON** The unit goes energy-saving state after 15 minutes of inactivity. **OFF** The console will stay lit"* / §8.5 p38 l.613-614: *"【F5】Sleep Mode - **Turn off** to have the console power down automatically after 15 minutes of inactivity. 0: OFF / 1: ON"*. **One says ON sleeps, the other says OFF sleeps.** The same item is **P5** on p9 l.184 and **F5** on l.613. |
| `sole-bike-b94-2023` / `-r92-2023` | §4 l.101-102: *"When set to **on** … it will enter sleep mode if there is no key press for **15 minutes**"* / §8.4 item C.III (b94 l.400 p21, r92 l.396 p20): *"III. Sleep Mode - **Turn off** to have the console power down automatically after **30 minutes**."* |
| `sole-tm-f80-2023` / `-f85-2023` / `-f89-2023` | §4.5 item 3 (F80 l.245-249): *"When Sleep Mode is **OFF**: removing the SAFETY KEY will not turn off the screen and there is no Sleep Mode. When Sleep Mode is **ON**: … no operation … for **15 minutes** … Default: OFF"* / §8.10 Machine Information (F80 l.850-854): *"**Display Mode** Default: **ON** … When the setting is ON, the console won't power down if the users remove the SAFETY KEY. When the setting is OFF, the console will power down … after **30 minutes**."* |
| `sole-tm-st90-2023-service-manual` | p22: *"The unit goes to energy save state after **15 minutes** of inactivity"* / p25: *"the display will turn off … automatically after **30 minutes** of inactivity"* |
| `sole-tm-tt8-2023-service-manual` | §4.5 p15 "Sleep Mode" (Default OFF; ON = safety key removal turns the screen off; **15 minutes**) / §8.10 p55 "Display Mode" (Default ON; ON = console will *not* power down on safety key removal; OFF powers down after **30 minutes**) |
| `sole-tm-f85-2016` / `-2019` / `-ent-2021` | all three say **30 minutes** exactly (p60, p77, p73) |

**Against the committed cards:** `cards/shared/console/engineering-menu-non-touchscreen.md` line 48
and `cards/sole/console/sleep-mode-2023.md` line 43 both say *"**15 to 30 minutes**"*, and
`cards/shared/console/sleep-mode-touchscreen.md` repeats the range. G9 §3.5 warns that the two
exact figures belong to **two different switches**, so replacing "15 to 30" with either single
number alone would be wrong. G9 §3.6 also notes `sole-sleep-mode-2023-f63-f65` gives an F65 button
combination (*"hold **Stop** and **Enter**, press **Display**"*) that appears **nowhere** in
`sole-tm-f65-2023-service-manual`, whose only route is §8.11 l.693 *"Press and hold the Start, Stop
and Enter key at the same time"* → Functions → **Display Mode**, a switch whose polarity is
inverted relative to one named "Sleep Mode".

---

## 1.12 The child lock unlock gesture is stated three ways, including on the console's own screen

**Found by G9, G10, G11 and G12.**

| Gesture | Where |
|---|---|
| *"press and hold the **START and ENTER** buttons for 3 seconds"* | f85-2016 §8.9 p60, f85-2019 §8.9 p77, f65-2023 §8.11 D p35 l.705-707, all four 2016/2019 TT8 manuals; and `cards/shared/console/engineering-menu-non-touchscreen.md` |
| *"press and hold both the **START & STOP** buttons for **3 seconds**"* | f80-2023 §4.5 l.235, tt8-2023 §4.5 p14, st90-2023 p22; and `cards/shared/console/engineering-menu-touchscreen.md` |
| *"press **START & STOP** key **within** 3 seconds"* | f80-2023 §8.10 l.858-860, tt8-2023 §8.10 p55, st90-2023 p25 |
| *"press **START & DISPLAY** key **within 2 seconds**"* | f85-2021 §8.10 Machine Information p73 |
| **The message the console itself displays** | f80/f85/f89-2023 §8.10 and tt8-2023 p55, quoted in the manual: *"**Press Start and Display** to enable operation"* — a third pair of keys, printed on screen while the prose beside it names Start and Stop |

"Hold for 3 seconds" and "press within 3 seconds" are different actions. G9 §3.7 records that the
two shared cards each match one manual and neither is wrong, *"so nobody 'fixes' one into the
other."*

---

## 1.13 The supply voltage contradicts itself inside almost every manual

**Found by G1, G2, G3, G4, G7, G8, G9, G10, G11 and G12** — ten groups. §7.1 (the outlet), §7.3
(the nominal circuit), §3 (the motor), and the troubleshooting matrix rarely agree.

| Manual | The contradiction |
|---|---|
| `sole-elliptical-e25-2016` | §7.1 p38 *"**115-volt**, 15-amp grounded outlet"* / §7.3 p38 *"nominal **230-volt** circuit"*. Every sibling prints 115-volt in §7.3. |
| `sole-elliptical-e25-2019` | l.509 *"**115-volt**, 15-amp"* / l.528 *"nominal **230-volt** circuit"*. E35/E55/E98/E95s 2019 all print 115-volt. |
| `sole-elliptical-sc200-2016` | §7-3 p33 *"nominal **120-volt**"*, §7-1 p33 *"**120-volt**, 15-amp"* where every elliptical says 115 |
| `sole-elliptical-sc200-2019` | l.438 *"120-volt, 15-amp"* / l.458 *"nominal 120-volt"* / matrix l.605 *"Check AC power is **220~230V**"* |
| all five 2023 ellipticals | §7.1 **120-volt, 15-amp** — against the committed 2019 cards' **115-volt** |
| `sole-elliptical-e98-2023` | §3 p6 *"115(220V)-volt AC motor"* / §7.1 and §7.3 p15 *"**120-volt**"* |
| `sole-elliptical-e95s-2016` | §7-1 p38 *"115-volt, 15-amp **(for 220V is 10-amp)**"* / §8-7 matrix p57 *"110-120V.**(or 220-230V)**"* / §7-3 p38 *"nominal **115-volt**"* only |
| `sole-elliptical-e25-2026` | §7.1 l.303 **120-volt**, §7.3 l.332 **120-volt**, Operation l.166-167 *"**115 VAC**"*, §3 l.144 *"**115 volt** AC motor"*, §8.7 matrix l.646 *"**110-120V**"*. **This edition fixes the 2019 230-volt defect** (G4 §3.5). |
| `sole-tm-f63-2016` / `-f63-2019` | §7.1 p34 *"**230-volt, 10-amp (110-volt, 15-amp)**"* / §7.3 p34 *"nominal **230-volt**"* / p64 *"**110 VAC** wall outlet. (for 220V model is **220 VAC**)"* / p64 *"A minimum of **220 volt** AC current, 50 hz"* |
| `sole-tm-f60-2016` | §7.3 p34 l.522, damaged: **"This product is for use on a nominal       -volt 230-volt circuit"** — a number has dropped out |
| `sole-tm-f60-2020` | §7.1 p30 *"**230-volt, 10-amp**"* with **no 110V alternative**, unlike every other manual / matrix p55 *"Check the voltage of power is **120V (230V)**"* / cover l.4 *"(110~120V & 220~230V)"* |
| `sole-tm-f65-2016` / `-f65-2019` | §7.1 *"**230-volt, 10-amp (110-volt, 15A)**"*; matrix l.1175 *"110V or **230V**"*; guide l.1390 *"110 VAC … (for 220V model is **220** VAC)"* — 220 and 230 for one supply |
| `sole-tm-f80-2016` / `-f80-2019` | §7.1 *"**220-volt, 10-amp** … 【120Vac electronic power system is 110-volt, 15-amp】"* |
| all four 2023 F65/F80/F85/F89 | §7.1 *"**220-volt, 10-amp** … 【120VAC electronic power system is **110-volt**, 15-amp】"* / §7.3 *"nominal **220-volt** (on 120VAC … need **110VAC**)"*. F80 has **no CE note**, so 220-volt is its only unqualified figure. |
| `sole-tm-f85-2016` | Special Note p3 *"110AC … versus **230VAC** for CE version"* / §7.1 p34 *"**220-volt**, 10-amp"* / §7.3 p34 *"nominal **220-volt**"* |
| `sole-tm-f85-2019` | §7.1 p51 *"**220-volt**, 10-amp"* / §7.3 p51 *"nominal **230-volt**"* |
| `sole-tm-s77-2016` | §3 drive motor *"0-180 DC volts"*, §7.1 *"220-volt, 10-amp"*, §8.7 *"whether **110ACV or 220AC**"*, E3 test p49 *"~ **110VAC (230VAC)**"* |
| `sole-tm-st90-2023` | p16 *"A minimum of **110-volt** AC current is required"* / p28 *"Check the voltage of power is **220V**"* |
| `sole-bike-sb1200-2023` | §4 p5 *"DC 12V/3.3A … supplied by the power pack … connected to **115 VAC**"* / §7.6 matrix p19 *"Check AC power is **110-120V**"*. **No safety or grounding section at all.** |

G6 §2b.12 records the same shape on the SRVO and explains it: the power module input is
**90-130 V** (the wall) and the motor is **220 V** (the bus), with a PFC output of **0 v-330 v** —
consistent, but *"the exact shape of the 115/230 V trap"*.

---

## 1.14 Lubrication and belt tracking: the shared cards describe a different job from the manuals

**Found by G7, G8, G10 and G11.**

**Lubrication interval and method.** `cards/shared/maintenance/lubricate-running-belt.md`
(authority 2, source `sole-tm-how-lubricate-treadmill-belt`) line 35: *"**How often**: every 3
months, or every 90 hours of use."* Line 37: *"**What you need**: 2 ounces of 100% silicone based
lubricant, preferably a gel, and a **5mm or 6mm** Allen wrench."* Its steps: *"2. Turn both bolts
counter-clockwise **10 full turns**. 3. Lift the belt. 4. Lay the lube down in an "S" pattern …
5. Tighten both rear roller bolts clockwise 10 full turns."*

| Manual | Locator | Printed |
|---|---|---|
| f63-2016 / f63-2019 | p63, l.1391 | *"every **90 hours** of use or if you notice that the deck is dry"* |
| f65-2016 l.1362-1371 / f65-2019 l.1385-1394 / f85 ×3 §10.1 (pp69/86/84) / both S77 §9.1 | | *"every **90 hours** … reach between the belt and deck to verify there is lubrication present, **every other month**"* then *"Measure **18"** from the edge of the motor cover; reach under the belt approximately **4-6"** from one edge. Squirt a line of lubricant about **1/8" wide x 15" long** in an "S" pattern … Repeat on the opposite side … **Walk on the belt at a moderate speed for five minutes**"* |
| **f60-2016 p69 l.1389-1390 / f60-2020 p64** | | *"1. After the first **25 hours** of use (2-3 months) apply **one half bottle** of lubricant. 2. Every **50 hours** of use (5-8 months) apply one half bottle."* plus *"ONLY USE HALF THE BOTTLE OF LUBRICANT PER APPLICATION"* |
| `sole-tm-f85-ent-2021` | §8.10 Lube Setup p74 | the reminder is now adjustable: *"default time is **90 hours** … Setting range: **90~200 hours**"* — the same on tt8-2023 §8.10 p56 |

**The manuals never loosen the rear roller bolts to lubricate**, give no lubricant quantity, and
never say "every 3 months" (G8 §3.1). The F60 pair uses a completely different interval, quantity
and method (G7 §2.5, §2.6).

**Belt tracking.** `cards/shared/maintenance/running-belt-tracking.md`: *"2. Run the machine at low
speed, **no more than 2**, and watch the belt walk across."* All four G8 manuals (f65-2016 l.1329,
f65-2019 l.1352, f80-2016 l.1116-1117, f80-2019 l.973-974), both F63 manuals p62 l.1358, all three
F85 manuals §10.1, both S77 manuals and all four 2016/2019 TT8 manuals: *"A **10 mm** Allen wrench
is provided to adjust the rear roller. Make tracking adjustments from the **left side only**. Set
belt speed at approximately **3 to 5 kph**."* **Exception:** `sole-tm-f60-2016` p68 l.1353 and
`-f60-2020` p63 — *"A **6 mm** Allen wrench (97) is provided … Set belt speed at **3 mph**."*
The shared card also adds *"Counter-clockwise moves it left"*, which no manual states, and carries
neither the wrench size nor the warranty exclusion (G8 §3.2). G7 §2.4 notes a **10 mm Allen wrench
is an unusual size for a treadmill rear roller bolt** and may be a typo, quoted as printed.

**Belt tension.** `cards/shared/maintenance/running-belt-tensioning.md` says *"Turn both bolts the
same number of turns"*; the manuals specify *"in increments of **1/4 turn each** … **DO NOT
OVERTIGHTEN** - Over tightening will cause belt damage and premature bearing failure"* plus
*"DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING / TENSION ADJUSTMENTS IS NOT COVERED
UNDER THE WARRANTY"* (f65-2016 l.1311-1316, l.1345-1347). Not a contradiction — the shared card is
missing the number and the warranty line (G8 §3.3).

**Drive belt tension.** `cards/shared/maintenance/drive-belt-tension.md` (authority 2, derived from
photographs) describes *"four plate bolts"* plus *"a threaded tensioner stud that runs up through a
cross bracket behind the motor"* and gives **no target tension**. Every treadmill manual in the
batch gives **70-75 LBS**. G7 §3.8, G8 §3.5 and G10 §3.4 all raise it independently. G8 adds that
the fasteners differ too: F65 loosens *"**1 belt tension screw**"* with a **14mm open end** wrench
(l.1517), F80 loosens *"**a side tension screw as well as a rear drive belt tension screw**"* with
a **14mm T-shaped socket** wrench (l.1282).

---

## 1.15 The console-to-driver cable is 6-pin in the wiring section and 12-pin in the matrix

**Found by G7, G8, G9, G10 and G11.** The same row of the same matrix names a different cable from
the rest of the manual.

| Manual | Matrix says | Rest of the manual says |
|---|---|---|
| `sole-tm-f60-2020` p55 l.931/933 | *"3.**12 PIN** Computer connector not plugged in properly. / 4.**12 PIN** computer cable is broken."* — with the solution *"4 Replace **5-PIN** computer cable."* | pin table p45: `1. SW 2.+12V 3.TXD 4.RXD 5.GND` — a **5-pin** main control wire |
| `sole-tm-f80-2016` l.938-940 | *"**12 PIN** Computer connector … 12 PIN computer cable is broken."* | l.581 *"Send and receive speed signal via TX/RX of **6-pin** Main wire"* |
| `sole-tm-f65-2016` l.1154-1156 / `-f65-2019` l.1177-1179 | *"3 **6-PIN** Main control wire … 4 **6-PIN** Main control wire is broken."* | consistent |
| `sole-tm-f65-2023` §8.12 p36 l.721-723 | *"**6 PIN** Computer connector"* | consistent |
| `sole-tm-f80-2023` p53 / `-f85-2023` p54 / `-f89-2023` | *"**12 PIN** Computer connector … 12 PIN computer cable is broken."* | — |
| `sole-tm-f85-2016` §8.10 p61 / `-ent-2021` §8.11 p75 | *"**12 PIN**"* | f85-2021 §8.2 p43 callout: *"via TX/RX of **6-pin** Main wire"* |
| `sole-tm-f85-2019` §8.10 p78 | *"**6-PIN** Main control wire"* | consistent |
| `sole-tm-st90-2023` §8.3 (copy 2) | *"**12 PIN** Computer connector / 12 PIN computer cable"* | copy 1 of the same matrix, pp17-18: *"console connectors not plugged in properly / console cable is broken"* |
| `sole-elliptical-e55-2019` l.677-679, l.747-749 | row **label** says `6-pin cable`, row **text** says *"Inspect whether the **14-PIN** cable is connected well"* | E25 and E35 2019 print 14-pin throughout the identical tables |

Elliptical variant: `sole-elliptical-e95-2016` blames an **11-pin cable** at E3 case 1 p47 and a
**14-pin cable** at case 2 p53, while the console connector drawn in that manual has **11 pins**
(G1 §2b, §2.18).

---

## 1.16 Section 8 is numbered 8.2 twice, so every later number is one behind the table of contents

**Found by G7, G8, G10, G11 and G12** — the whole DC treadmill family.

The body prints `8.2 Error Message：E1` and then `8.2 Error Message：E2/OVER CURRENT`, so the ToC's
`8.9 Circuit Diagram / 8.10 Calibration Procedure / 8.11 Maintenance Menu` becomes the body's
`8.8 Circuit diagram / 8.9 Calibration procedure / 8.10 Troubleshooting procedure matrix`, and the
troubleshooting matrix has **no ToC entry at all**.

Confirmed in: f63-2016 and f63-2019 (G7 §2b.3, §2b.4); f65-2016 l.670/l.779, f65-2019 l.664/l.773,
f80-2016 l.572/l.659, f80-2019 l.522/l.609 (G8 §2b.8); f85-2016 p39/p45 (G10 §2b.1.3), f85-2019
(G10 §2b.2.6); s77-2016 and s77-2019 (G11 §2b); tt8-2016 (G12 §2b b), tt8-2019.

**Consequence: every card locator in these manuals points at a section number the reader will not
find where the ToC says.** Cross-references inside the manuals inherit the fault — *"(See section
**8.1** on Error Message: E1)"* when 8.1 is E0, in tt8-2016 p68, tt8-2019 p66 and tt8-2019-ac p48
(G12 §2b f/d/a); and *"(See section 8.2 on Error Message: LS1/LOW SPEED)"* in f63-2016/2019 p64 and
f65-2016 l.1404 / f65-2019 l.1427, where **LS1/LOW SPEED is never defined anywhere in either
manual** — grep-verified (G7 §2b.6, §6.1; G8 §2b.7).

Two further ToC failures: `sole-tm-f80-2016` ToC lines 30-36 lists 8.1 E1 through 8.7 E7 but the
body starts at `8.1 Error Message：E0` (G8 §2b.9); `sole-tm-f85-2016` ToC **never lists E7 at all**
although the p36 table and a full p57 section cover it (G10 §2b.1.3).

---

## 1.17 "5 preset buttons" listing seven values

**Found by G8, G10, G11 and G12.** Printed twice in each manual, for speed and for incline.

| Manual | Locator | Printed |
|---|---|---|
| `sole-tm-f80-2016` | l.322-323 | *"SPEED RAPID button: **5 preset buttons** for rapid speed: 2，3，4，5，7，9，12"* and *"INCLINE RAPID button: **5preset buttons** … 1，3，5，7，9，12，15"*. The console drawing at l.290-293 labels **seven** of each. |
| `sole-tm-f85-2016` | §4 READY MODE p19 | identical |
| `sole-tm-f85-2019` | p36 vs p37 | *"5 preset buttons"* on p36, *"total **7** buttons"* on p37 |
| `sole-tm-f85-ent-2021` | §4 p20 | *"**7** preset buttons"* — corrected |
| `sole-tm-s77-2016` | p19 | identical to f80-2016 |
| `sole-tm-s77-2019` | p18 vs p19 | *"5 preset buttons"* then *"total 7 buttons"* |
| `sole-tm-tt8-2016` | p19 | *"5 preset buttons … 2，3，4，5，7，9，12"* and *"GRADE RAPID: 5preset … -4，-2，2，4，6，9，12"* |
| `sole-tm-tt8-2019` | p17 | *"5 preset buttons … 2，3，4，5，7，9，12 (Note: On 22.0kph spec is 3, 6, 9, 12, 15, 18, 22)"* |
| `sole-tm-tt8-2019-ac` | p19 | *"5 preset buttons … 3，6，9，12，15，18，22"* |

Related, same family: `sole-tm-f63-2026` p20 READY MODE says *"SPEED RAPID button:
**Non-functional**. INCLINE RAPID button: **Non-functional**."* while p21 RUN MODE lists
*"4 preset buttons for rapid speed: 3，6，9，12 MI"* and *"4preset buttons for rapid incline:
0/5/10/15"* (G7 §2b.21).

---

## 1.18 The console range tables contradict the quick keys and the RUN MODE text

**Found by G7, G8, G9, G10, G11 and G12.**

**Maximum incline, 12 or 15, inside one manual**

| Manual | Function table | RUN MODE | Quick keys |
|---|---|---|---|
| `sole-tm-f60-2016` | — | p20 l.289 *"the maximum incline position is **10**"* | p19 l.272 *"6 preset buttons: 2, 4, 6, 8, **10 and 12**"*; p60 l.1128 *"Incline level is set at 10 for level 10 or **12** for level 12"* |
| `sole-tm-f63-2023` | p8 l.134-136 *"from **0 to 10** … WORK range is 0 to 10"* | p10 l.206 *"maximum incline position is **15**"* | p10 l.209 *"1/3/5/7/9/12/**15**"*; p27 l.540 *"**15** for max incline"* |
| `sole-tm-f80-2016` | l.241-244 *"0 to **15**"* | l.341 *"maximum incline position is **12**"* | l.344 *"1，3，5，7，9，12，15"* |
| `sole-tm-f85-2016` | p16 *"0 to **15**"* | p20 *"maximum incline position is **12**"* | p18 *"1/3/5/7/9/12/15"* |
| `sole-tm-s77-2016` | p16 *"0 to 15"* | p20 *"maximum incline position is **12**"* | p16, up to 15 |
| `sole-tm-f85-2023` | §4.2 p8 l.148-151 *"from 0 to 15 … WORK range is **0 to 15**"* | — | §4.4 p10 l.198 *"7preset buttons: **-4/-2**/2/4/6/9/12"* — **the machine declines and §4.2 says it does not**; §9.10 p64 is *"Replacing the **Rear Incline Motor**"* |
| `sole-tm-f89-2023` | §4.2 l.148-151 *"GRADE Display the incline position from **0 to 15** … (INCLINE & DECLINE) DISPLAY range is 0 to 99 … WORK range is **-6 to 15** … preset value is -6 to 15"* — **the same cell says both** | — | l.199, reaches only **-4** |
| `sole-tm-tt8-2023` | §4.2 p8 *"WORK range is **0 to 15**"*, *"**DISPLAY range is 0.**"* (upper bound lost) | — | §4.4 p10 *"7preset buttons: **-4/-2**/2/4/6/9/12"* |
| all four 2016/2019 TT8 | Operation *"WORK range is **-6 to 15**"* | *"the minimum incline position is **0**"* | -4，-2，2，4，6，9，12 |

And **§8.4's E3 test procedure still reads "15 for max incline, **0** for lowest incline" in every
one of the four 2023 manuals, including the two that decline to -6** (G9 §2b.15, §2b.19).

**Maximum speed — the metric figure moves, the mile figure never does**

| Value | Machines |
|---|---|
| `1.0~16.0KM or 0.5~12Mile` | f63-2016 p16 l.236 |
| `1.0~18.0 kmph (0.5 ~ 12.0 mph)` | f80-2016 l.238, f85-2016 §4 p16, s77-2016 p16, tt8-2016-ac p16, tt8-2019 p14 |
| `1.0~18.0KM` | f63-2023 p8 l.132 |
| `1.0~20.0KM or 0.5~12Mile` | f63-2019 p16 l.224, f80-2019 l.194, f65-2023 l.138, f80-2023 l.135 |
| `1.0~22.0KM` / `1.0~22.0 km/h (0.5 ~ 12.0 mph)` | f85-2019 §4 p33, f85-2021 §4 p17, f85-2023 l.146, f89-2023 l.146, s77-2019 p15, tt8-2019-ac p16, tt8-2023 §4.2 p8 |
| `0.5~12Mile` only, no kilometre figure | f63-2026 p16 l.214 |
| `1.0~16.0KM or 0.5~12Mile` | f65-2016 l.226, f65-2019 l.224 |

**16.0 / 18.0 / 20.0 / 22.0 km/h are not consistent conversions of 12 mph (19.3 km/h)** — G7 §2.10,
G8 §2.1, G9 §2.10, G10 §2.1 and §2b.1.12, G11 §2.3, G12 §23. `sole-tm-tt8-2019` p14 prints both in
one sentence: *"WORK range is 0.5 ~ 12.0 mph (**1.0~18.0 kmph**) Note: Specific spec has
**22.0kph** of maximum speed."* `sole-tm-f85-ent-2021` §4 p17 has a malformed range with a stray
quote: *"DISPLAY range is 1.0 to 22.0 km MAX or for MILE is "0.5 to12.0 MAX"*.
`sole-tm-st90-2021` p47: *"The default setting is **12MPH / 22KPH**"* — 12 mph is 19.3 kph — while
the Min. Speed on the same row, `0.5MPH / 0.8KPH`, converts correctly (G11 §2b).

**Calibration maximum contradicts the work range.** `sole-tm-f85-2023` §4.2 p8 gives
*"WORK range is 1.0~**22.0** km/h"* but §8.10 p50 l.833 gives *"the Metric range: Max. (**20.0**);
Min. (1.0)"*. The otherwise-identical F89 manual prints **22.0** at l.834 (G9 §2.12, §2b.13).
`sole-tm-tt8-2023` has the same split: §4.2 p8 and §4.4 p10 give 22.0, §8.10 step 1 p54 gives
**20.0** (G12 §2b d).

**Pulse work range:** `60 to 220` (f60-2016 p17), `50 to 220` (f60-2020 p14), `40 to 220 BPM`
(f63-2016/2019/2023, f65-2016/2019/2023, f85-2019), `50 to 200 BPM` (f80-2016/2019, f80/f85/f89-2023,
f85-2016, f85-2021), `60 to 200 BPM` with a **3-second** rather than 8-second timeout (f63-2026 p17).
The no-signal display is `---` (f60-2016), `P` (f60-2020) or `0` (everything else).

---

## 1.19 "The settings page has 8 sub-menu modes", followed by ten of them

**Found by G3, G9 and G12.** Word for word, in nine manuals:

> *"there are **8 sub-menu modes** on the settings page, namely: 1)Unit System, 2)Speed Display
> [2)Child Lock on treadmills], 3)Sleep Mode, 4)Screen Brightness, 5)Date & Time, 6)Wi-Fi,
> 7)Language, 8)Software, **9)Media Apps, and 10)Passcode**."*

- Ellipticals: e35-2023 p8, e95-2023 p8, e95s-2023 p9, e98-2023 p8 (G3 §2b.12)
- Treadmills: f80-2023 §4.5 p11 l.210-212, f85-2023 l.221-223, f89-2023 l.222-224 (G9 §2b.12)
- tt8-2023 §4.5 p12 (G12 §2b a)

**Related:** the engineering menu lists six functions and documents four. **"Diagnostics" and
"Maintenance" are named and never described** — f80-2023 l.804, f85-2023 l.824, f89-2023 l.825
(G9 §6.2); f85-2021 §8.10 p70 (G10 §2b.3.14); st90-2023 p23 and st90-2021 (whose Key Test is
listed as one of six sub-functions and never described, and is absent from the ToC) (G11 §2b);
tt8-2023 §8.10 p53 (G12 §6.2).

---

## 1.20 The troubleshooting matrix is structurally broken in every manual in the batch

**Found by all twelve groups.** Four distinct defects, each reproduced as printed because no agent
would guess a mapping.

**(a) The incline-cable reason is printed three times with three separate "Replace the cable"
fixes.** G1 §5.5 (all seven 2016 ellipticals, 8.7/8.6/unnumbered), G2 §5.13 (all six 2019
ellipticals, e.g. e25 l.892-902: *"The connector of INCLINE CABLE or INCLINE ADJUSTMENT SWITCH
CABLE got damage / got damage / damaged"*), G3 §2b.16 (all five 2023 ellipticals, four
restatements), G4 §6.3 (e25-2026 l.654-671, **six** numbered reasons of which 3, 5 and 6 are
near-identical). *"The duplication is in the source, not the conversion"* (G2).

**(b) "After pressing START the treadmill stops immediately" is printed twice with different
answers.** G8 §2b.11 (f65-2016 l.1185-1191, f65-2019 l.1208-1214), G9 §2b.5 (f65 l.766-775, f80
l.949-958, f85 l.969-978, f89 l.970-979), G10 §2b.1.10/§2b.2.9/§2b.3.13 (all three F85s), G12 §2b h
(tt8-2016 p63, tt8-2019 p60, tt8-2023 p59). Row 1: *"Controller **is** broken"* → two steps
(*"Turn off the AC switch and turn on power again. 2 Replace controller and calibrate it"*).
Row 2, a few rows later: *"Controller **was** broken"* → one step (*"Replace with new controller and
calibrate it"*).

**(c) The dim-display condition is printed twice, once as LCD and once as TFT LCD, on machines
that have only one of the two.** G9 §2b.6: `sole-tm-f65-2023` l.743-748 prints *"LCD not bright,
incomplete, or imperfect"* (4 causes, ending *"Replace lower controller"*) **and** *"**TFT** LCD
displays not bright … Replace with new console"* — on a machine with no TFT panel. F80/F85/F89 print
both rows as "TFT LCD". G5 §2b(p): both `b94-2023` and `r92-2023` carry *"LCDs not bright…"* and
*"LCD displays not bright…"* with different fixes.

**(d) Columns are offset, numbered wrong, or split across a page break.** G8 §2b.13: f65-2016
l.1152-1160, eight reasons and eight solves, but *"solve 1 is printed against reason 1 and the
remaining solves are shifted one row down, so reason 8 ('Other components are faulty') has no solve
and solve 8 ('Replace console') sits against reason 7."* G8 §2b.12: the incline-switch solve column
runs 1, 2, 3, 4, **6** against five reasons. G9 §2b.9: the Reason column runs 1-4 and the Solve
column runs 1, 2, **2**, 3 — in all four 2023 manuals. G10 §2b.2.10: the wireless heart rate row
lists three causes and the solutions run *"1. … 2. … Replace with new lithium battery type is
CR2032"* with **no number 3**. G9 §2b.10 and G10: the chest belt row breaks across a page footer so
the condition reads *"Chest belt too close to the"* … footer `- 37 -` … *"treadmill."* — no verb, no
stated symptom. G3 §2b.16: the chest belt row's condition and reason do not match at all —
*"Chest belt too close to the Elliptical | **Weak battery** | Replace with new lithium battery with
type CR2032."* G8 §2b.19: *"Treadmill with noises"* item 1 is an **unfinished sentence** —
*"1. If the noise is coming from the rollers, ."* — in all four manuals (f65-2016 l.1426,
f65-2019 l.1449, f80-2016 l.1197, f80-2019 l.1053).

---

## 1.21 Boilerplate carries the wrong machine noun

**Found by G1, G2, G3, G4, G5 and G7.** Whole safety and console sections are pasted between
product lines without changing the subject.

| Manual | Printed |
|---|---|
| `sole-elliptical-sc200-2016` and `-sc200-2019` | **Climber**: §3 p11 *"CONSOLE: Interface that controls all functions of the **Climber**"*; p24 *"**CLIMBER** Configuration"*; p42 *"**CLIMBER** CIRCUIT DIAGRAM"*; matrix *"chest belt in use around **climber**"*. **Bike**: the whole of §7 pp32-33 *"disconnect your **bike**", "install the **bike** on a flat level surface", "If the **bike** should malfunction"*; READY MODE p21 *"Pressing START button to start **bike**"*; RUN MODE p22 *"press STOP button to stop **bike**"*; PULSE p19 *"if the **bike** doesn't have a signal for 8 seconds"*. **The 2016 and 2019 manuals carry the identical self-contradiction.** |
| `sole-elliptical-e25-2023` | §4 Function pp7-8: *"PULSE … if the **treadmill** doesn't have a signal for 8 seconds"* |
| `sole-rower-sr500-2016` | §3 l.79: *"Console: Interface that controls all functions of the **Elliptical**."* |
| `sole-rower-sr550-2023` | every safety section: l.88-90 *"power is connected to the **fitness bike** … the line cord plugs into the unit on the front of the **bike**"*; l.268-272 §7.1; l.275-282 §7.2 *"Route the power cord away from any moving part of the **bike** including the **elevation mechanism and transport wheels**"* — **a rower has no elevation mechanism**; l.286 §7.3 |
| `sole-bike-b94-2023` / `-r92-2023` | §4 Function PULSE: *"if the **treadmill** doesn't have a signal for 8 seconds"* |
| `sole-bike-lcb-2023` l.330-333 / `-lcr-2023` l.337-340 | *"Erratic pulse display. \| 1. Another chest belt in use around **Elliptical**. \| … 2. Change the position or direction of **Elliptical**."* — the next row of the same table says *"Chest belt too close to the **Bike**"*. The 2016 and 2019 LCB/LCR manuals say Bike throughout. |
| `sole-bike-lcb-2023` l.107 / `-lcr-2023` l.112 | *"Resistance in SLEEP MODE: **Incline =1**, Cooling Fan off."* — neither bike inclines |
| `sole-bike-sb1200-2023` l.280 | *"Test configuration: **Incline motor** control function relate parts location."* — a spin bike with a magnetic brake on a push rod |
| `sole-elliptical-e95s-2016/2019/2023` | §8.x headed *"Case of **RAMP ERROR**"* and a whole matrix of **INCLINE CABLE** / **INCLINE ADJUSTMENT SWITCH** rows on a **stride** machine with no ramp. e95s-2023 p7 goes further: *"**Incline Motor** This is an AC motor. User can control **Stride** length by console"* beside *"If there is AC voltage on the red wire (UP) the **incline** motor will increase the **incline**."* |
| `sole-tm-st90-2023` §8.3 (copy 2, pp28-30) | *"Motor **M+ or M-** wire isn't connected"*, *"**LED** would be ON"*, *"**12 PIN** computer cable"* — the exact strings the DC S77 manuals use, on a machine with a **Rhymebus AC inverter**, a three-wire U/V/W motor terminal (§6.1 *"AC MOTOR W(black) V(white) U(red)"*) and a TFT touch console |
| `sole-tm-f63-2026` p52 l.730 | *"Noise under motor cover. 1. **Worn brushes** or bearings on motor."* — p12 l.150 says *"**Brushless** motor with variable speed range 0-90 or (0-180) volt"* |
| `sole-tm-f85-ent-2021` p4 / `sole-tm-tt8-2016` p4 / `sole-tm-s77-2016` p4 | CE note heading names ST538 / ST925 / ST725; the sentence under it names **ST535** in all three |
| `sole-elliptical-e98-2016` §10-1 p66 | lists *"a steel cable and a magnetic flywheel"* on a machine whose §9-3 p57 calls the brake an **Inductive Flywheel** with electric cables and no cable adjustment |
| `sole-elliptical-e98-2023` §10.3 p36 | *"the most case will be improper **steel cable** adjustment … Follow procedures for replacing flywheel for steel cable adjustment."* — this machine has an **EMS Brake** (§3 p6) and §9.9 has no cable step |

---

## 1.22 Cross-references point at sections that do not exist

**Found by G1, G2, G3, G4, G5, G7, G11 and G12.** Two distinct causes: the 2019 generation's
`11-x` numbering left in a manual renumbered to `9.x`, and plain wrong numbers.

| Manual | Locator | Printed | Reality |
|---|---|---|---|
| e25-2023 §9.9 p34, e35-2023 §9.9 p30, e95-2023 §9.11 p32, e98-2023 §9.10 p32 | STEP 4 | *"Follow procedures **11-2, 11-5 and 11-3, 11-4** to return Pedal Arm and Connecting Arm."* | **none of these manuals has a section 11** |
| `sole-elliptical-e25-2026` l.787 | §9.9 step 4 | same `11-2, 11-5, 11-3, 11-4` | this manual numbers them 9.2-9.5 |
| `sole-elliptical-e25-2026` l.784 | §9.9 step 1 | *"Follow procedures **9.2 and 9.3** to take apart Connecting Arm, Pedal Arm, left and right-Side Cases, Cross Bar and the Belt."* | 9.2/9.3 remove only the arms; the rest are 9.4, 9.5, 9.6 |
| `sole-elliptical-sc200-2016` | 9-3 step 1 p51, 9-4, 9-8 step 1 p61, 9-9 step 1 p62 | *"(Refer to step **11.2**)"*, *"(Refer to step **11.4**)"*, *"Remove the Linked Assembly. (Refer to step **9-8**)"* | **Section 11 in this manual is "Q & A"**; 9-8 is the crank arm, the linked assembly is 9-4. Identical in sc200-2019 (l.741, 883, 904). |
| `sole-bike-b94-2023` §9.7 step 4 l.579-580 and `-lcb-2023` §9.7 | | *"Follow step **2.1** to resume Cranks and Pedals"* | there is no section 2.1; cranks and pedals are 9.6 |
| `sole-bike-r92-2023` §10.3 l.869-870 and `-lcr-2023` §10.3 l.710-711 | | *"Follow the instructions outlined in **Section 9.10** … to resolve"* | 9.10 is Rear Shrouds and Harness; the seat carriage is 9.11 |
| `sole-bike-lcr-2023` §10.2 l.694 | | *"follow … **Section 9.7** … to properly install the Drive Belt"* | 9.7 is Replacing the Induction Brake; the drive belt is 9.5 |
| `sole-tm-s77-2016` p80 and `-s77-2019` p80, §11-7 step 1 | | *"Follow procedures **12-6** to Front/ Rear Roller Replacement."* | there is no section 12; the rollers are 11-6 |
| `sole-tm-tt8-2016` p81, `-tt8-2019` p79, `-tt8-2019-ac` p61, §11-7 step 1 | | same `12-6` | same |
| `sole-tm-f63-2026` p62 l.883 | procedure (H) | *"Follow procedure **(F)** to remove front and rear rollers"* | (F) is *Replace AC Power Switch*; the rollers are **(G)** |
| `sole-elliptical-e55-2016` §11-11 step 1 p90 | | *"Follow the procedures to take Rail Base Assembly apart."* | **no rail base assembly procedure exists in this manual** |
| `sole-tm-tt8-2016` p69 and p64 | | *"See General Maintenance section on **Belt/Deck Lubrication**"* and *"See treadmill belt lubrication"* | **there is no lubrication section in this manual** |
| `sole-tm-tt8-2023` §8.11 p60 | | *"See treadmill belt adjustment"* / *"See treadmill belt lubrication"* | **no General Maintenance chapter**; §8.11 is followed directly by §9 |
| both ST90 manuals §7-2 | | refers to a *"General Maintenance section on Tread-belt Tension"* | **neither ST90 manual contains one** |

---

## 1.23 Fasteners are removed at one size or count and refitted at another

**Found by G1, G2, G3, G4 and G5.**

| Manual | Locator | Removal | Refit |
|---|---|---|---|
| e25-2016 §11.8 p85 | flywheel | loosen `3/8"-UNF26x9T` | tighten `3/8"-UNF26 x **9T**` |
| e55-2016 §11-8 p86 | flywheel | loosen `3/8"-UNF26x**11T**` | tighten `3/8"-UNF26 x **9T**` |
| e25-2019 l.1345/1353 | §11.7 flywheel | loosen `3/8"-UNF26x**9T**` | tighten `3/8"-UNF26 x **11T**` |
| e55-2019 l.1265/1272 | §11-8 flywheel | loosen `3/8"-UNF26x**11T**` | tighten `3/8"-UNF26 x **9T**` |
| e25-2023 §9.8 p33, e35-2023 §9.8 p29, e95-2023 §9.10 p31 | flywheel | loosen `3/8"-UNF26x**9T**` | tighten `3/8"-UNF26 x **11T**`, then adjust `3/8"-UNF26 x **4T**` — **three thread counts for one fastener** |
| e25-2026 §9.8 l.772-775 | flywheel | `3/8”-UNF26x**9T**` | `**11T**`, belt centring `**4T**` — *"inherited from the 2019 manual"* |
| `sole-elliptical-sc200-2016` §9-9 pp62 | idler wheel | loosen nyloc nut `**M8x7T**` | tighten `**M8x9T**` at 190 Hz |
| e98-2016 §11-9 p87 | flywheel | release `**4pcs**` 1/4" spring washers and 1/4"x13x1T flat washers | refit `4pcs` bolts with `**3pcs**` spring washers and `**3pcs**` flat washers |
| e98-2019 l.1203/1210-1211 | | identical `4pcs` out, `3pcs` back | |
| e95s-2016 §11-3 p79/p80 and e95s-2023 §9.3 STEP 5/6 p33 | same bolt, two steps apart | `Ø 8.5 × Ø 26 × **2.0T**_Flat Washer` | `flat washer ψ8.5x26x**1.5T**` |
| e25-2016 §11.11 pp89 | incline motor, same bolt | step 3 `nyloc nut **3/8"x7T**` | step 4 `nyloc nut **M10 x 8T**` |
| e25-2026 §9.5 l.736-741 | cross bar | `Socket Head Cap Bolt **M8 × 25mm** with **one** Nut M8x6.3T` | `**M8x40** socket head cap screw together with **two** M8x6.3T nuts` at 500 Kg-cm |
| e25-2026 §9.4 l.720/726 | right side case | `9pcs of 3.5x16 self-tapping screws and 3pcs of **5x19 x 3** tapping screws` | `9pcs of 3.5x16 … and 3pcs of **5x16** tapping screws` |
| `sole-bike-b94-2023` §9.7 l.565-566/579-580 | chain cover | `nine Ø3.5 × **16**m/m Sheet Metal Screw` | `9pcs of 3.5x**12**mm Self Tapping Screws` |
| `sole-bike-r92-2023` §9.2 l.470-474 and `-lcr-2023` §9.2 l.388-392 | | `**4pcs** of 5/16" × 18 × 1.5T flat Washer (76)` | `**6pcs** of 5/16"×18×1.5T Flat Washers (76)` |
| `sole-tm-tt8-2016-ac` §12-6 pp61-62 | roller, same four screws | step 3 `**19mm** T-shaped socket wrench` | step 4 `**14mm** T-shaped socket wrench` |
| `sole-rower-sr500-2016` §8-4 steps 4/5 l.617-624 and `-sr550-2023` §9.4 steps 4/5 l.457-461 | Attaching Plate (8R) | `M5 × 10L_Phillips Head Screw (86)**x3pcs**` | then again `…(86)**x2pcs**` — the plate is removed twice |
| `sole-elliptical-e95-2023` §9.9 p31 | idler wheel | STEP 2 `M8 x 20 carriage **bolts**` | STEP 3 `M8x20 carriage **bolt**` |

**Cross-manual size differences on the same job:** cylinder screw on the deck replacement — `12mm`
(f80-2016 l.1341, f65-2016 l.1575, f65-2019 l.1599) vs `13mm` (f80-2019 l.1199, f85-2019 §12-7 p100,
f85-2021 §12-7 p98) (G8 §2.10, G10 §2.20). Incline motor assembly — `M6,M8 L wrench and #14`
(f80-2016 l.1394, f85-2016 §12-9 p85) vs `M8 L wrench and 14 mm` (f80-2019 l.1250, f85-2019,
f85-2021, f65-2016 l.1628, f65-2019 l.1653, f65-2023 §9.9 l.940) vs `14mm open-end wrench` alone
(f80/f85/f89-2023 §9.9) (G8 §2.11, G9 §2.6, G10 §2.21). Console mast cover — **six** sheet metal
screws in 2016 (f63-2016 p70 l.1518, f65-2016 l.1490, f80-2016 l.1255, s77-2016 §11-2, tt8-2016) vs
**four** in 2019 (f63-2019 p70 l.1501, f65-2019 l.1512, f80-2019 l.1111, s77-2019 §11-2, tt8-2019),
with the 2019 books also naming an `M6 L Allen wrench` where 2016 names none (G7 §2.13, G8 §2.9,
G11 §2.7, G12 §49). J-bolt nut — `M8 x 9T` (e25/e35/e95-2023) vs `M8 x **7T**` (e98-2023 §9.8 p30)
(G3 §2.4). Pulley bolt part **105** — `3/8" × UNC16 × **1-1/4"**_Button Head Socket Bolt` on the
SR500 §8-8 vs `3/8" × UNC16 × **32mm**` on the SR550 §9.8 — **same part number, different part**
(G4 §2.4).

---

## 1.24 Whole sections are image-only, so the content is unrecoverable without re-OCR

**Found by all twelve groups.** Every source in the batch is `pdftotext -layout` output of a
picture-heavy PDF. The consistent loss, in every manual: §1 Outlines and exploded views, §2
Electronic Parts, §5 Unit Block Diagrams, §6.1-6.8 (display board wire connections, PCB component
locations top and bottom, interface/amplifier board, driver board wiring and component locations,
driver board function, gear-motor connector definition), the Circuit Diagram, every "Configuration:"
figure under an error code, and every Action Flow Chart.

**The consequences that matter, not the inventory:**

1. **No part numbers.** G1 §5.2: *"There are no part numbers, so no parts-list cards could be
   built."* G9 §6.2: *"**No part number appears anywhere in the extracted text of any of the four
   manuals**."* G10 §6.6: *"No parts list, exploded view or part number appears in any of the three
   manuals."* G7 §6.3: *"No parts numbers anywhere in this batch."*
2. **Pinouts that used to be text are now pictures.** G3 §5.1: *"The 2019 pilot could write
   `e25-2019-console-to-driver-board-pinout` … **The 2023 PDFs have no recoverable pinout at all**."*
   G5 §5: no console-to-driver pinout card exists for any of the six 2023 bikes, although
   `b94-2019-console-to-driver-board-pinout`, `r92-2016-console-to-driver-board-pinout`,
   `lcb-2019-driver-board-cable` and `sole-bike-7-pin-console-cable-pinout` exist for the earlier
   ones. G4 §5.2: *"the E25 2026 and SR550 2023 gear motor connector pinouts are unrecoverable"* —
   `cards/e25-2019/specs/tension-motor-connector-pinout.md` (5 pins: M+, M-, +5V, VR, GND) has no
   2026 counterpart. G8 §5.3 and G10/G11: the page survives only as `1, 2, 3, 4, 5, 6,` — **no agent
   copied a sibling manual's pin names across.**
3. **LED debugging tables lost on exactly the machines where the thresholds live.** No LED card
   exists for `f80-2019` (G8 §5.1), `f60-2020` (G7 §5.5), `f80-2023`, `f85-2023`, `f89-2023`
   (G9 §5.2) or `tt8-2023` (G12 §5.2) — *"not because the machine lacks the LEDs."*
4. **Nine consecutive pages of the F63 2026 error chapter are gone.** See Part 5.

Full inventory and re-OCR priority in **Part 5**.

---

# Part 2 — Decisions needed

The worklist. One line each, in rough order of consequence.

## Safety and repair correctness

1. **Incline / position sensor pinout** — is pin 1 ground and pin 3 5vdc, or the reverse? Options: (a) ring out one connector per family (DC treadmill, 2023 treadmill, elliptical, S77) and declare a house order; (b) accept it as genuinely per-model and require every card to name its own manual and refuse to generalise. See 1.1.
2. **E6 remedy** — does the KB print E6's remedy as the manuals mostly have it ("Insert power wire of motor", the E4 remedy) or as the 2019 manuals corrected it ("Replace Lower controller board")? Options: (a) print as-is with a warning on every E6 card; (b) adopt the 2019 wording fleet-wide and note the deviation. See 1.2.
3. **E98 belt tension** — is the E98 2016 really **170 Hz** while every sibling and the E98 2019 are **190 Hz**, or is 170 a typo? Options: (a) confirm 170 for that generation; (b) declare it a print error and re-source. G1 §6.3 did not change it. See 1.8.
4. **LCR 2023 belt tension** — is **180 ± 10 Hz** (§9.5 step 5 p29) a real spec change for the LCR, or a typing error for **180 ~ 205 Hz**, which the LCB 2023 and the 2016/2019 LCB/LCR cards all print? See 1.8.
5. **SB900 / SB1200 2023 belt tension** — is "**180 lbs**" the real unit, and what gauge reads it? The whole prior spin-bike range is in Newtons (700-750 N, 1000 N). 180 lbf ≈ 800 N. Neither manual names a gauge type or has a belt-slipping section. See 1.8.
6. **B94 / R92 2023 dangling belt figures** — `b94-2023` §9.8 step 7 says "450 N **(Remark)**" and `r92-2023` §9.7 step 8 says "450N. **(Note 1)**"; neither Remark nor Note exists in either manual. The B94 **2016** Remark gives **540 N for a brand new belt**. Options: (a) supply the missing Remark from the 2016 manual; (b) leave the reference dangling on the card.
7. **Incline motor stroke** — 195 / 200 / 205 / 210 / 220 / 225 / 235 mm. Which value belongs to which chassis, and is `sole-tm-tt8-2016-ac-service-manual`'s internal 225 (§11 p53) vs 235 (§12-9 p67) a print error? See 1.10.
8. **Elliptical zeroing distance** — 206 mm or 207 mm? The E95 2023 and E98 2023 manuals each print **both**, one millimetre apart with a ±1 mm tolerance. The E25/E35 2023 manuals are byte-identical through section 9 **except** this figure (207 vs 206). See 1.10.
9. **Belt tracking wrench** — is the **10 mm** Allen wrench in the F63/F65/F80/F85/S77/TT8 manuals real, or a typo? G7 §2.4: "an unusual size for a treadmill rear roller bolt." The F60 pair says **6 mm** at **3 mph**; the shared card says **5 mm or 6 mm** and "no more than 2". See 1.14.
10. **Lubrication method** — the shared card loosens both rear roller bolts **10 full turns** and lays lube toward the centre; the manuals never loosen anything and squirt **1/8" x 15"** S-patterns **18"** from the motor cover, **4-6"** in from each edge. Which one is service telling customers? And is the interval "every 3 months or 90 hours" (card), "90 hours, check every other month" (most manuals), or "25 hours then every 50 hours, half a bottle" (F60 2016/2020)? See 1.14.
11. **SRVO parts-replaceable policy — the most consequential single decision in the batch.** `sole-srvo-service-manual` (authority 3) is a part-level service manual: **sixteen orderable part numbers** on p28 (including `004.039.0052708` motor, `004.057.0054583` power module, `004.057.0055008` display control, `004.039.0050054` fan), **eleven numbered disassembly steps** with tool sizes and screw counts on pp12-22, error `0x40` "Restart machine. **Replace module** if issue not resolved", error `0x800000` "Restart machine. **Replace motor control board** if issue is not resolved". Four committed cards say the opposite: `srvo-parts-replacement-policy` (authority **2**), `srvo-display-not-lighting-up` (authority **3**), `srvo-cables-not-retracting` (authority 2) and `srvo-cable-stuck-back-cover` (authority **3**) all state "**Individual parts are not replaced on the SRVO. When an SRVO needs a repair, a new SRVO is sent to the customer.**" Authority does not break the tie. Options G6 §3.1 sets out: (a) the policy is a **consumer-channel** rule and the manual is for an authorised service channel or the factory — both true, scoped differently; (b) the policy predates the manual and is superseded; (c) the manual is a Dyaco/OEM document never adopted by Sole service. If the policy wins, G6 recommends **re-scoping** the 13 disassembly cards and the part-number card rather than deleting them, since the manual is still the only source for tool sizes and connector pinouts.
12. **SRVO RS485 wiring** — `sole-srvo-service-manual` p37 §8-2-3 prints controller CN6 pin 3 as Name `RS485_B` / Description `RS485_A` and pin 4 as Name `RS485_A` / Description `RS485_B`; the far end of the same bus, display main board CN5 on p31, is consistent. G6: "**the entry most likely to cause a real field failure of anything in this manual**." Ring the pair out and say which column is right.
13. **SRVO power board output** — p41 §8-3-2 calls CN1-1/CN1-2 "**DC output** positive/negative terminal" with pin names L1/N1; p35 §8-2-1 heads the controller port it feeds "**AC port**" with L/N. Which is it?
14. **SRVO cooling fan screw count** — p22 step 11: "remove the **four** screws in the circle. (**Four** on the left end cap and **two** on the right end cap.)" Four or six?
15. **C80 wildcard hazard** — `c80-2026` is `product_line: treadmill` but is a **manual curved treadmill with no drive motor, no incline, no safety key, no mains cord and no error codes**. Should any `model: '*'` + `product_line: treadmill` card (belt lubrication, motor error codes, incline calibration, speed calibration, safety keys, mains wiring) be allowed to reach it? G4 §3.6: "the C80 is the one machine in this batch where extending a wildcard card is more likely to be wrong than right."
16. **Wildcard treadmill error cards vs ellipticals** — `cards/shared/errors/e1-no-speed-signal.md`, `e2-overcurrent.md` and `e3-incline.md` carry `product_line: treadmill`, `model: '*'`, `applies_to: ['*']`, so they match a brand-and-`applies_to` query about a 2016 elliptical, where E1/E2/E3 mean something else entirely. Filter on `product_line`, or narrow `applies_to`?

## Model identity

17. **SC200 product line — climber, elliptical, stepper or bike?** G1 and G2 both found the manual calling itself all of these. Climber: §3 p11 "controls all functions of the **Climber**", p24 "**CLIMBER** Configuration", p42 "**CLIMBER** CIRCUIT DIAGRAM", matrix "chest belt in use around **climber**". Bike: the whole of §7, READY MODE "start **bike**", RUN MODE "stop **bike**", PULSE "if the **bike** doesn't have a signal". Database: `520516 | SOLE SC200 | **Stepper**` and `520517 | SC200 | **Elliptical**`. `kb.yaml` declares `climber` and `cc81-2020` already uses it. Both agents wrote `elliptical` as assigned and objected; **if it becomes `climber`, 38 cards on `sc200-2019` and 38 on `sc200-2016` need their `product_line` changed.**
18. **SRVO product line** — the assignment table said `rower`; G6 wrote **`strength`** on all 49 cards to match the 36 pre-existing srvo cards. Confirm `strength`. (`kb.yaml` declares both, and lint does not check `product_line` against the model, so `rower` would have passed silently and split the srvo set across two product lines.)
19. **Merge `f85-2020` and `f85-2021`?** G10 §1.1 concludes they are one machine, SKU **585820**, and recommends `f85-2020` survives. Caveat: `sole-tm-f85-ent-2021-service-manual` documents **two console generations in one book**, named by Android version (§6.1-6.3 pp25-30: separate display-board wiring for "For Android 6" and "For Android 10", separate PCB bottom pages, an amplifier board page marked "**Only for Android 6**"). If 585818 is the Android 6 console and 585820 the Android 10 one, ST538-YT056 may cover both SKUs. Confirm which SKU the manual was issued against before merging.
20. **Merge `st90`, `st90-2020` and `st90-2021`?** G11 §1.1 concludes all three are SKU **590820**. `st90-parts-and-wiring` (`model: st90`) is the only source of ST90 part numbers in the repo and does not reach `st90-2021` or `st90-2023` in a facet-filtered query.
21. **Merge `sb1200` and `sb1200-2023`?** One database row, `512322`. Five committed cards name the bare `sb1200` in `applies_to`. Options: (a) collapse the ids; (b) add `sb1200-2023` alongside `sb1200` in those five lists.
22. **Split the TT8 SKUs, or accept two machines per SKU?** `588816` covers **ST925-YT021 (DC)** and **ST925A-YT030 (AC)**; `588818` covers **ST928-YT035 (DC)** and **ST928A-YT037 (AC)**. Their error code sets share nothing (`E0…E7` vs `E-01H…E-53H`). `tt8-2016-ac` and `tt8-2019-ac` are UNRESOLVED. Is `588810 SOLE ATT8` one of them? G12 §1.5 warns the leading letter is a **generation** marker in that table (`UTT8 2006`, `VTT8 2007`, `WTT8 2008/09`), not "AC".
23. **F89 2023 SKU — 589853 or 589822?** `cards/sole/console/start-button-grayed-2023.md` line 36 says **589822**; `dbo.Models` has only **589853** (`SOLE F89`, no year, and `53` is not a year). Which is right? See Part 4.
24. **`sc200-2019` SKU** — UNRESOLVED. Neither `520516` nor `520517` has year digits of 19 and no SC200 2019 row exists. Which ModelNumber does the 2019 service manual belong to?
25. **`sc200-2016` SKU** — `520516` is typed **Stepper** while the manual sits in the Ellipticals folder, and neither SC200 row carries a year, so 520516 = 2016 rests on the digits alone.
26. **`e25-2026` SKU** — UNRESOLVED. There is **no row whose ModelNumber ends in 25 or 26** and no row named "E25 2026".
27. **`sr500-2016` SKU** — UNRESOLVED. The rowers extract has four rows total; the candidate is **500911** ("SR500", no year, digits 11) but nothing in the manual confirms it. The manual's own code is `CW800A-YR001`.
28. **`c80-2026` SKU** — UNRESOLVED. `grep -i "c80\|curve\|tk700"` over all six `spirit-models-sole-*` extracts returns nothing. **Caveat from G4 §1.5: those extracts are filtered by `ModelType`** (the training extract queries only `ModelType IN ('Training')`, 2 rows). A manual curved treadmill could sit under a ModelType none of the six extracts queried. **Absence from these files is not proof of absence from `dbo.Models`.**
29. **`f63-2026` SKU** — UNRESOLVED, no 2026 treadmill row. Unlike the other UNRESOLVED cases the manual names the model on its cover: `GT88-YT088-01 / (F63 2026) / Service Manual`, so only the SKU is missing.
30. **`f60-2020` — CONFLICT.** `| 560820 | Sole F60 **2019** | Treadmill |`. Digits say 2020, name says 2019, and **the manual names neither a Sole model nor a SKU** (cover: `AT90P-NT038 / Treadmill Service Manual / (110~120V & 220~230V)`; no "F60" or six-digit number in 1,384 lines). Is the DB name stale or the folder year wrong?
31. **`f60-2016` year** — `| 560816 | F60 |` is the only F60 row with no year in the name; the id's year rests entirely on the digits, with no confirmation in the manual.
32. **`f85-2021` SKU** — UNRESOLVED; see decision 19.
33. **`e98-2016` year** — `598012`, `598015` and `598016` are all named `SOLE E98` with no year, so nothing in the database distinguishes the 2012, 2015 and 2016 machines by name.
34. **`e25-2016` — what is `525016`?** Its digits say 2016 and its ModelName says nothing; the assignment took `525116` ("SOLE E25 2016"), the only E25 row whose name carries the year. `525113` and `525114` are also bare "SOLE E25".
35. **`e95-2023` / `b94-2023` / `sb1200-2023` — should the database rows gain their years?** `595022 | SOLE E95`, `594122 | SOLE B94` and `512322 | SB1200` carry no year while every neighbouring row does. **`512322` carries no year anywhere — not in the database and not on the manual cover**, which prints only `SB1200` where its five siblings print `LCB(2023)`, `LCR(2023)`, `R92(2023)`, `B94(2023)`, `SB900(2023)`.
36. **`590321 | SOLE SB900 2022`** — digits say 21, name says 2022, and **no card in the repo covers it**. It sits between `sb900-2020` and `sb900-2023`. Is it a real machine that needs a model id?
37. **SRVO SKUs — one product or two?** `srvo-overview` (authority 3, `sole-srvo-seminar` p3) says "The SRVO is sold under two SKUs: **578712** and **578722**." The database gives them **two different ModelNames**: `578712 SOLE SRB101` and `578722 SOLE SR260`. The manual cover names **SR260 only**; the strings `SRB101` and `578712` appear **nowhere** in it. G6's unconfirmed reading: `SRB101` looks like the **SRVO Multi-Angle Bench** part code (the repo already carries `srvo-bench-overview` and `srvo-bench-warranty`), in which case 578712 is the bench and **this manual covers none of it**.
38. **The "last two digits are the model year" rule** — retire it, or restate it? It fails on at least 15 SKUs across nine groups (1.6), including three of the six rows that `sources/spirit-models-sole-bikes/text.md` prints to *prove* it. The shared card `sole-bike-service-manual-model-numbers` states it and is also six rows short (see decision 44).
39. **`tt8-2023` chassis code** — the cover reads `ST738-YT066`, not an ST925/ST928 series code like every other TT8. Confirm ST738-YT066 really is 588822's chassis.
40. **`e25-2026` and `sr500-2016` manifest codes** — the manifest titles carry a `-01` suffix (`SE668SA-SE052-01`, `CW800A-YR001-01`) that neither document prints; the suffix comes from the origin filename. Which is authoritative? Same question for `ST278-YT071-01`, `ST378-YT078-01` (F85/F89 2023 covers print no `-01`) and `ST538-YT056`.

## Card scope and retrieval

41. **Touchscreen lists** — move `e35-2023`, `e95-2023`, `e95s-2023`, `e98-2023` onto the touchscreen Garmin cards (G3), and examine `f85-2019` (G10) and `tt8-2019` (G12) for **removal** from them. Keep `e25-2023` non-touchscreen. Exclude `f85-2021` (a touchscreen) from `cards/shared/console/engineering-menu-non-touchscreen.md`, which reaches it via `applies_to: ['*']`. See 1.4.
42. **E0 shared card** — write one? E0 ("Safety keys dose not insert the safety module. Or safety module is broken") is printed as a code in eleven manuals and `cards/shared/errors/dc-controller-error-code-list.md` has no E0 row. Raised independently by G8, G9 and G10.
43. **E8 shared card** — `cards/shared/errors/e8-controller-eeprom.md` (`applies_to: ['*']`) claims a code **no service manual in the batch prints**, and the DC list scopes itself to "the F63, F65, F80, F85, F89 and TT8". Re-scope it to the controller generation its own source describes, or delete it?
44. **`sole-bike-service-manual-model-numbers`** is six rows short. Add: B94 2023 / 594122 / SU415A-SB025; LCB 2023 / 511122 / SU615A-SB026; LCR 2023 / 522122 / SR625A-SB026; R92 2023 / 592122 / SR425A-SB025; SB900 2023 / 590322 / SB910-3268T; SB1200 2023 / 512322 / SB950-SB027. Its "how to read the number" paragraph needs the `594122 SOLE B94`, `512322 SB1200` and `590321 SOLE SB900 2022` exceptions.
45. **`sole-inverter-error-code-list` `applies_to`** — extend from `[st90, tt9]` to reach `st90-2021`, `st90-2023`, `tt8-2016-ac` and `tt8-2019-ac`? G12 §3.2 warns that doing so **puts the card's `E3 red` = front / `E3 green` = rear reading in front of TT8 AC technicians alongside per-code cards that bind the bare `E3` to the **rear** motor and `E-53H` to the **front**.** Resolve the E3 front/rear question first.
46. **The 2016/2019 bike console cards must not simply gain the 2023 ids.** G5 §6b: the sleep timer (30→15 min), the END timeout (3→5 min on LCD bikes), the exercise-scan list (gained a `SPEED XX.X RPM` line; `WATT XXX.X` lost its decimal) and the engineering-mode entry method (Start+Stop+Enter for 5 s → "Press 10 times on 'Settings'") all changed. `sole-bike-lcd-console-modes`, `-buttons`, `-data-ranges`, `sole-bike-engineering-mode-lcd-consoles` and their four TFT equivalents must stay separate from the 2023 cards.
47. **`code` facet values** — the facet is open (no `values:` list in `kb.yaml`), so lint cannot check it. New or contested values introduced this run: **`eer`** for "EEPROM ERR" (G3 reused it from `ctsbs900`, whose console literally prints `EER`; if `code` is the exact printed string these want their own value); **`eeprom-err`**, new (G5, deliberately split from `e1` because those three bikes never print E1); **`lwr`** for both "LWR not found" and "LWR not match", two distinct faults with two distinct fixes sharing one value; **`e0`**, new (G9, G10); **`incline-er`** and **`no-power`**, new (G7); **`please-replace-the-safety-key`** (G12); and G6's **eighteen** SRVO values — twelve hex fault codes `0x40, 0x80, 0x100, 0x400, 0x800, 0x40000, 0x80000, 0x400000, 0x800000, 0x4000000, 0x10000000, 0x40000000` plus six connector names `cn1, cn2, cn3, cn5, cn6, cn7`, which stretch the facet "from fault code to identifier".
48. **Merge the boilerplate, or keep it per-model?** Rule 4 forced every group to write the same fact once per machine. The largest candidates: the GFCI prohibition + 16 AWG single-outlet extension cord + grounding text; the high-inrush house breaker with **Grainger part 1D237** and **www.squared.com part QO120HM** and "not a warranty defect" (G4 notes **44 existing cards already carry this per-model**, so the house convention is per-model); the CR2032 chest belt battery + 3-foot receiver range + 8-second timeout; the "both grips" hand pulse row; the 70-75 LBS drive belt tension; the 3 mm speed sensor gap. G4 §6.1 flags one genuine two-machine card the rules forbade: drive belt `6PJ-787L` at `70~80BLS` on **both** rowers.
49. **`sole-lwr-not-match` vs the manuals** — the shared card's fix (console **Machine Type**) and the manual's fix (check driver board controller number, replace upper controller) address different causes and neither document mentions the other. Should the shared card carry both routes?
50. **The SB900 2023 Smart Tension knob** — `sb1200-2023` §8.3 "Replacing the Bluetooth Wireless Knob and Brake Assembly" is **word for word** the SB900's §6.3, part numbers included (21, 22, 24, 78, 83, 85, 86, 87, 104, 105), but **the SB1200 manual never mentions pairing or calibrating the knob** and calibrates resistance from the console's Engineer Mode instead. Are they the same part? Decide before the four SB900 knob cards are widened.
51. **`sole-spinner-console-spec`** names the console "**DT-3268**", a part number the SB900 2023 manual never prints. G5 wrote a per-machine `sb900-2023-console-spec` rather than extend it. Confirm.
52. **SC200 `SPM` unit** — `sole-elliptical-sc200-2019` line 276: "SPM / Display the current speed in **mile per minute**"; the 2016 manual p18: "**SPM** — Display the current speed in **mile per hour**. DISPLAY range is 0 to 888, WORK range is 0~120", and p19 "**VERTICAL** — Display the current vertical in **Mile**". On a climber SPM is normally steps per minute, and the same table already has TOTAL STEPS in steps. What does the console actually show?
53. **E98 2019/2023 E2** — `sole-elliptical-e98-2019-service-manual` line 518 has `| E2 | Tension motor is failure |` in its error table, but the ToC lists only E1 and E3 and **no E2 section exists**; the machine has an EMS brake and no tension motor. Does an E2 procedure exist elsewhere for this machine? The 2016 manual has the identical gap.
54. **E95s "crisp sound" belt check** — `sole-elliptical-e95s-2019` l.1678-1680: "flick belt with a **crisp sound** **or** use sonic device measured at 190HZ(±10)". Is the subjective check acceptable in the field?
55. **`c80-2026` 608 bearing** — the heading and step 2 of "Replacing the Limit Wheel and 608 Bearing" name a **608 bearing**; the parts list names only `16 Bearing 120`, `25 6203_Bearing 2`, `27 6001_Bearing 2`. Which part number is the 608?
56. **`c80-2026` "the 10 pedals"** — p12 step 2: "Remove the **10** pedals by following the above procedure"; parts list line 110: `19 Pedal **60**`. G4's reading is that these are the 10 slats that must come off to free the rear roller; the manual does not say so.
57. **`c80-2026` part names** — item **7** is "**Foot Pad**" on the page-3 photograph and "**Handle**" in the parts list; "Foot Pad" is callout **7 and 12** on the same photograph; the wheel is "Moving Wheel" on the photograph and "Transportation Wheel" in the list. Which numbering is authoritative?
58. **`e95s` axle dimension** — `sole-elliptical-e95s-2023` §9.6 STEP 2 p42: "remove 5/16"x1/2"hex head bolt and 5/16"x23x1.5T flat washer from **Bψ178x41L** Rotate Axle". A 178 mm diameter axle retained by a 5/16" bolt is not plausible; the same manual's other axles are "Ø 17 × 34L" and "ψ17x108L". G3 transcribed 178 as printed. Someone with the machine should confirm.
59. **`sr500-2016` voltage test step 2** — §7.2 lines 441-448 are numbered `1. 3. 4. 5. 6. 7.`; **step 2 is absent from the printed list**, not from the extraction. What was it?
60. **`sr500-2016` "Q With a sequence of displays:"** — §8-10 line 751 asks a troubleshooting question and **never says what the symptom looks like**. Carded as `sr500-2016-console-display-sequence-fault` with the ambiguity stated.
61. **`srvo` — where is an error code displayed?** The manual names no console readout, no app screen, no LED and no debug output. All thirteen error cards say so explicitly; if a human knows the answer they each want one added line.
62. **`srvo` duplicate part numbers** — `004.049.0052894` appears on **rows 5, 7 and 14** of p28 with two different descriptions (row 5 a low-voltage PFC output power cable, rows 7 and 14 an identical "PC260 Power &485 communication cable & Fan"). And two **different** part numbers, `004.028.0052625` (row 9) and `004.057.0054999` (row 11), carry **word-for-word identical** speaker descriptions with nothing to say which is left and which is right. Do not order from the table without checking.
63. **`srvo` PC260** — a third model-number-shaped string on p28 rows 7, 13, 14, never explained. Supplier code, project code, or SKU?
64. **`s77-2019` E2 video link** — `https://www.youtube.com/watch?v=ak_raMb_6vY&t=1s` is printed in the manual and is on `s77-2019-e2-over-current`. Nobody has checked it still resolves.
65. **`f63-2026` HIIT program** — the manual says "**9 programs** (Manual, Hill, Fat Burn, Cardio, Strength, **HIIT**, Interval, User*2, HRC*2)" and then gives LED codes for eight of them: `Manual-P1, Hill-P2, Fat Burn-P3, Cardio-P4, Strength-P5, Interval-P6, User*2-U1~U2, HRC*2–H1~H2`. **HIIT has no code.** The same sentence counts User*2 and HRC*2 twice.
66. **`f63-2026` hand pulse** — the troubleshooting matrix has four causes and four solutions for "Hand pulse lost its function", but the console parts list (p4), the console description (p12) and the display board socket list (p25) name **no hand pulse grips and no hand pulse socket**. Is it fitted?
67. **`f63-2026` motor ground** — p12: "Requires **three** wires connection: red, black and white" assigned to U, V, W, with **no grounding wire named**, unlike every other manual; p58: "**Reconnect ground wire** and motor wires (W/U/V)".
68. **`f63-2026` E3 twice** — the error table lists `E3 Incline error, displaying in Incline window` (p47) and `E3 Calibration error` (p48), with different names and different step counts. One fault or two?
69. **`sb1200-2023` calibration control** — §7.5 item 4: "After pressing the **START** button, the resistance system's G-sensor calibration process will begin", then step 1: "Click '**start**' to calibrate resistance level". Same control or two?
70. **`sb900-2023` knob sleep timer** — **15 seconds** (§5.2 "How to pair" item 2, p11) or **20 seconds** (§5.2 "Other Instructions", p12)?
71. **`sb900-2023` knob battery** — "Remove **both sides' screws** … To open turn counterclockwise" (§5.2 p12) or "**three M3×6L hex screws** from the socket under the knob, 2.5mm hex key" (§6.1 STEP 3 p15)? These are not the same job. G5 marked §6.1 as the working description.
72. **`c80-2026` parts list numbering** — **item 1 appears twice** (`1 Frame Welding` and `1 Main frame right side`), **there is no item 14**, and **there is no item 55**. Every following frame item may be one out from the exploded view.

## Housekeeping

73. **`groups/G6.md` says "Model id srvo already carries 74 cards."** The repository held **36** before the run (85 after). Correct the assignment source.
74. **`sole-elliptical-e25-2016` "nominal 230-volt circuit"** — G1 §6.3 believes it is a typo for 115-volt (all five siblings print 115, and the same manual's §7.1 says 115). Not changed. Confirm or correct.
75. **`sole-tm-f60-2016` p34 damaged grounding sentence** — "This product is for use on a nominal `      -volt` 230-volt circuit". A number dropped out. Supply it or leave the damage quoted.
76. **Collapse the repeated incline-cable matrix reasons?** G4 §6.3 kept all six on `cards/e25-2026/errors/incline-buttons-not-working.md` with one sentence saying the table repeats itself. If the house preference is to collapse, that is the card to edit.
77. **`sole-tm-f63-2026` braking resistor** — `cards/sole/maintenance/controller-braking-resistor-2026.md` documents drilling two 3.5 mm holes 140 mm from the front of the right main frame tube and fitting a braking resistor with the new controller. The service manual's `(A) Replace Lower Controller` (p53) says only "remove the motor cover, disconnect all wiring related to the lower controller, replace the component, and then reconnect the wiring" — **no resistor, no bracket, no drilling.** A technician following only the manual would omit it.
78. **`sole-tm-f63-2026` calibration screen** — `cards/sole/console/calibration-2026-non-touchscreen.md` says the screen shows "**F1**" and that there are "3 buttons under the Start button sticker — use the left or the right one, the centre button does not work"; the manual p50 says hold Start + Speed 3 while replacing the safety key "until the window displays '**Factory settings**'", then navigate with a **Rotary Switch incline▲/▼** key and a **Grade return** step the card does not mention. The Start + Speed 3 combination agrees; nothing else does. Different firmware, or one is wrong?

---

# Part 3 — Per-group detail

Everything each group found that is not already in Part 1. Numbers, part numbers, tool sizes and
quotes are exact.

---

## G1 — seven 2016 Sole ellipticals (331 cards)

`e25-2016` 50, `e35-2016` 50, `e55-2016` 50, `e95-2016` 50, `e98-2016` 48, `e95s-2016` 45,
`sc200-2016` 38. Factory codes: SE565S-SE016, SE575-SE017, SE585S-SE018, SE595-YE021, SE865-YE023,
XE895A-YE022, XS110A-YS003.

**Between manuals**

| Fact | Values |
|---|---|
| Poly-V belt "falls off" high-speed test | `-e25-` §9.4 item 1 p63 **"100-200RPM"**; `-e35-` 9-4 p66, `-e55-` 9-4 p64, `-e95-` 9-4 p64, `-e98-` 9-4 p58, `-sc200-` 10-3 p68 **"100-120RPM"** |
| Tension motor voltage test, probe colours | `-e25-` 8.2 p43, `-e35-` 8-2 p45, `-e55-` 8-2 p43: **"Red probe in brown wire, Black probe in black wire"**. `-e95-` 8-2 p43, `-e95s-` p43, `-sc200-` 8-2 p38: **"Red probe in blue wire, Black probe in green wire"** |
| Meter setting / normal reading | e25/e35/e55/e95/e95s: **20VDC**, "+5~6.0VDC … -5~6.0VDC". `-sc200-` 8-2 p38: **12VDC**, "+5.5~6.0VDC … -5.5~6.0VDC" |
| Tension motor connector | `-e25-` 6.10 p36, `-e35-` 6-10 p38, `-e55-` 6-10 p36 — **5 pins**: `1.M+ 2.M- 3.+5V 4.VR 5.GND`. `-e95-` 6-10 p36, `-e95s-` p36, `-sc200-` p41 — **8 pins**: `1.VIN 2.M+ 3.M- 4.COUNT 5.ZERO 6.3V 7.GND 8.SPEED`, plus a 2-pin speed sensor. `-e98-`: **no tension motor section at all** (EMS brake) |
| Controller indicator LED table | `-e25-` 6.8 p34, `-e35-` 6-8 p36, `-e55-` 6-8 p34: **D5 POWER** (check 110~120V), **D2** = incline up, **D4** = incline down. `-e95-` p34, `-e95s-` p34: **LED1 = motion up, LED2 = down**, no power row. `-e98-` 6-8 p35: **LED1 = down, LED2 = up** — the opposite way round. `-sc200-`: no table |
| Swing arm bearing | `-e25-` 9.5 item 2 p65, `-e55-` 9-5 item 2 p66: *"If the noise is emitting from the bottom bracket, then the **6203 bearings** needs to be replaced."* `-e35-` 9-5 item 1 p68, `-e95-` p66, `-e98-` p60: *"add crease or thick lubricant on **ψ25x296L** console mast shaft … If noises come from **6005 bearing**, replace"*. **Two different bearings at two different places, both printed as "the swing arm noise fix"** |
| Flywheel nut | `-e25-` 11.8 p85 **`3/8"-UNF26x9T`**; `-e35-` 11-9 p96, `-e55-` 11-8 p86, `-e95-` 11-9 p96, `-e95s-` 11-8 step 7 p107 **`3/8"-UNF26 x 11T`**; `-sc200-` 9-10 p63 **`3/8" -UNF26 x 9T x 2 nuts`** |
| Slip / tightening figures | `-e35-` 10-2 pp76-77, `-e55-` 10-2 p72, `-e95-` 10-2 pp75-76, `-e98-` 10-2 pp67-68: bushing housing **"500~600 lbs of force suggested"**, cross bar **"550~600 lbs"**. `-e25-` 10.2 p71: same three joints, **no force figures at all**. `-e95s-` 10-2 p68: two situations, no figure; instead **"torque wrench to up to 550lb"** (11-5 step 14) and **"150lbs"** (11-6 step 13). `-sc200-` 11-2 p73: crank arm bolt only, **"550 Lbs"** in 9-8 step 4 |
| Sleep mode resistance line | `-e25-` 2.4 p16 *"Incline =1, **FAN system OFF**"*; `-e35-` 2.5 p18, `-e55-` 2.5 p16 *"Incline =1"* (no fan); the rest *"Incline =1，Fan off"* |
| Sleep mode quick key | `-e25-` has **none**; every other manual: *"In IDLE MODE press and hold **ENTER+STOP+DISPLAY** keys 2 seconds"* |
| Incline / level work range | `-e25-` p18, `-e35-` p20, `-e55-` p18 **"0 to 20"**; `-e95-` p19, `-e98-` p19 **"1 to 20"**; `-e95s-` p18 stride **"18 to 24 … each increment and decrement is 0.5"**; `-sc200-` p18 level only, **"1 to 20"** |
| Engineering Mode menu | `-e25-` p55, `-e35-` p57, `-e55-` p56, `-sc200-` p43: lettered **A to F** with a nested Functions submenu (ODO Reset, Units, Display Mode, Motor Test, Manual, Pause Mode, Key Tone) + D. Security, E. Factory Set, F. Exit. `-e95-` p55, `-e95s-` p55: flat **A to G** (KEY TEST, UNIT MODE, **MANUAL TEST**, DISPLAY MODE, PAUSE MODE, KEY TONE, CHILD LOCK) — **no ODO Reset, no Factory Set**. `-e98-` p49: same A-G but **C is BRAKE TEST – Testing of the EMS brake** |
| Error code strings | E1: `-e25-` 8.1 p41 and `-sc200-` 8-1 p36 print **"E-1"**; the other five print **"E1"**. E2: `-e95-` 8-2 p42 heads it **"E-2"**; every other manual prints E2 |
| Console-to-driver connector | `-e25-` p48 list **stops at "10.INC -"** beside a drawing numbered 1-11. `-e35-` p50, `-e55-` p49, `-e95-` p48, `-e95s-` p48: 11 entries ending `11.INC VR`. `-e98-` p42: 11 entries, a **completely different signal set** — `1.+12V 2.GND 3.VCC+5V 4.PWM 5.AD 6.SPD 7.P/C 8.INC+ 9.INC- 10.INC VR 11.NA`. `-sc200-`: none |
| E3 first-case cable | `-e25-` p47, `-e35-` p49, `-e55-` p48 **14-pin**; `-e95-` p47, `-e95s-` p47 **11-pin**; `-e98-` no first case |
| Display size | 6.5" LCD (e25 p14) · 7.5" LCD (e35 p16, sc200 p14) · 9" LCD (e55 p14) · 10.1" TFT (e95 p16, e98 p16, e95s p15) |
| §9-4 missing fourth item | e25, e35, e95, e98, sc200 all end *"If the Poly-V Belt worn or damaged, replace with new part."* **`-e55-` 9-4 p65 stops after item 3 and never says it** |

**Inside one manual (beyond Part 1)**

- **e25-2016**: ToC 11.2 Swing Arm / 11.3 Connecting Arm / 11.9 Bushing Housing vs body 11.2 Connecting Arm / 11.3 Pedal Arm / 11.9 Drive Pulley — **there is no swing arm removal procedure in the manual at all**. 11.9 is headed "Drive Pulley Replacement" and every step removes and refits the **bushing housing**; no drive pulley part is named. ToC 9.8 "Tension Motor Problem" vs body 9.8 "Controller & Incline Motor Problem" — **no tension motor troubleshooting section exists**. 9.7 headed "Controller & Incline Motor & Slide Wheel Problem" but all four steps are the linked structure and slide wheels. **ENTER key**: READY MODE p21 *"pressing ENTER key can modify DM display"* vs RUN MODE p22 *"**ENTER button: non-functional.**"* — also in the E35, E55 and E98 manuals.
- **e35-2016**: cross bar torque in two units — 11-7 step 4 p94 *"tighten M8x40 socket head cap screw together with two M8x6.3T nuts until it reaches **500 Kg-cm**"* vs 10-2 item 3 p77, same screw, *"**550~600 lbs** of force suggested"* (also E55, E95, E98). ToC 9.8 "Tension Motor Problem" vs body "9-8 Gear Motor". 11-7 step 1 p93 begins *"…and both Side Cases. **ake off** the Round Disk Cover"* — reproduced as "Take off".
- **e55-2016**: 11-4 step 3 p79 releases the **right** side case; step 4 p80 removes screws securing the **left** Side Case then *"take **right** Side Case apart"*. 11-3 steps 1 and 2 are **the same sentence twice** (p78). ToC 11.6 "Flywheel & Poly-V Belt Replacement" vs body "11-6. Poly-V Belt Replacement"; ToC 9.7 "Controller & Incline Motor & Slide Wheel Problem" vs body "9-7 Connecting Arm and Rail Tube Problem". Circuit diagram p55 has **no section number** (ToC says 8.4), then jumps to "8-5 CALIBRATION PROCEDURE". **Page 47 is blank** but for the footer.
- **e95-2016**: **the same 11-pin plug is labelled two ways on consecutive pages** — p48 `1.SPEED 2.GND 3.VCC+5V 4.VR 5.GND 6.M- 7.M+ 8.VIN 9.INC+ 10.INC- 11.INC VR`; p49 `1.SPEED 2.GND 3.VCC+5V 4.ZERO 5.COUNT 6.MOTOR- 7.MOTOR+ 8.VIN 9.INC UP 10.INC DOWN 11.INC VR`. Section 6 numbering **skips 6-6** (body: 6-5, then 6-7, then 6-8; ToC: 6.5, 6.6, 6.7). 9-6 item 4 p69 **repeats 9-7 word for word**. **11-8 and 11-9 carry the same heading**, "Flywheel & Poly-V Belt Replacement" (pp95, 96); 11-8 is the idler wheel procedure. Circuit diagram p54 has no section number.
- **e98-2016**: **the error table lists a fault the machine cannot have** — p40 "E2 — Tension motor is failure", but §3 p14 describes an **EMS BRAKE, Work voltage: DC 0 ~23V**, with no tension motor, and **no E2 section exists**. LED table p35 vs the 6-7 drawing p34, which lists INCLINE MOTOR UP first. E3 section carries **no number** (ToC says 8.2). ToC 11.8 Idler Wheel / 11.9 Flywheel & Poly-V Belt vs body 11-8 "Flywheel & Poly-V Belt Replacement" (idler wheel steps) / 11-9 "Flywheel Replacement". §10-1 Noise p66 lists **a steel cable and a magnetic flywheel** on an Inductive Flywheel machine. RUN MODE p23 *"START button: LEVEL & INCLINE PROFILE. ENTER button: non-functional"* — the E95 assigns those two the other way round. 9-6 item 4 p62 repeats 9-7. **Pages 59 and 88 are blank.**
- **e95s-2016**: **four sections named in the ToC do not exist** — 9.5 Swing Arm, 9.6 Connecting Arm, 9.7 Controller & Incline Motor, 9.8 Tension Motor; the body runs 9-1, 9-2, 9-3, then an **unnumbered** section headed *"Controller , Incline Motor,Tension Motor **Problem Problem**"* (p64), then 9-4. The heading "**6-2**" is used **twice** — "6-2 Display Board PCB Component Locations" (p27) and "6-2 Driver Board PCB Component Locations" (p32); four further section-6 pages carry no number. **Stride range contradicts itself**: p18 *"from **18 to 24** … each increment and decrement is 0.5"* vs Test Procedure p50 *"**20 for max stride, 0 for lowest stride**"*. **The same motor has two names**: p13 "**STRIDE MOTOR**", but the LED table p34, the parts drawings p7 and §11-7 p98 head it "**Incline Motor**", and the E3 section p46 is headed "Case of **RAMP ERROR**". §11-5 step 6 p89 removes an **"Inclinable Rail Assembly"**, a part the machine's own parts drawings do not list. **Motor comes off at 21" and goes back on at 18"** — §11-7 step 2 p98 *"use console to adjust program to **21”**"* vs step 17 p104 *"…to **18”**"*. §11-4 step 6 p85 is **printed twice, once in Chinese and once in English** (the two agree). READY MODE p21 still lists "INCLINE PROFILE" on a stride machine.
- **sc200-2016**: **unit definitions that cannot be right** — p18 *"**SPM** — Display the current speed in **mile per hour**. DISPLAY range is 0 to 888, WORK range is 0~120"*; p19 *"**VERTICAL** — Display the current vertical in **Mile**. DISPLAY range is 00000 to 99999"*. Sleep mode p16 names *"**Incline =1**, fan off"* on a machine with no incline. §9-6 step 1 p59: **"First remove the Console Mast."** — the console mast procedure starts by removing the console mast, and **no fasteners between mast and frame are named anywhere**. **Two different covers are both labelled "Stabilizer Cover (L)"** in the p5 parts drawing. §8 stops numbering after 8.2; the circuit diagram, maintenance menu and troubleshooting matrix (pp42-44) carry no section numbers.

**Against committed cards**

- `cards/e25-2019/maintenance/swing-arm-noise.md` says **6003 bearings**; the 2016 manual §9.5 item 2 p65 says **6203**. *"A one-digit difference on a part number, on the same machine line, one generation apart."*
- `cards/e25-2019/assembly/flywheel-replacement.md` loosens 9T and tightens **11T**, with its own note that this is internally inconsistent; the 2016 manual loosens 9T and tightens **9T** and is self-consistent.
- `cards/e35-2019/maintenance/poly-v-belt-falls-off.md` says **100-200 RPM**, and the e55-2019 and e98-2019 cards carry the note *"The E25 and E35 manuals of the same year say 100-200 RPM"*. In **2016 only the E25 says 100-200**; the E35 says 100-120. The 2019 note is correct for 2019 and wrong read as a statement about the E35 generally.
- `cards/e55-2019/specs/incline-motor-spec.md`: *"The E35 and E98 manuals of the same year print 207 +/- 1mm"* — in 2016 **the E95 manual prints it too**, and the E55 and E25 still print nothing.
- `cards/e98-2019/errors/e3-incline-vr-error.md` names a **6-pin cable**; the 2016 E98 names an **11-pin cable** for the same row.

**Absences that are the answer**: every manual names the program buttons (Manual, Hill, Fat Burn, Strength, Interval, 2 User, 2HR; Cardio and User 1&2 / HR1&2 on the SC200) but **never says what any program does** — no profile, no target, no duration. No `section: programs` card exists for any of the seven. Each error chapter's "Prepare:" table has one row, "Multi-meter".

**Merge candidates identical across all seven**: E1 = EEPROM failure, all screens off, replace the upper controller · the nine-step incline/stride motor and potentiometer test (relay click, ~115VAC, 5vdc black-red, **4.5~4.7Vdc** red-white, pin 3/2/1) [all but sc200] · chest belt within **3 feet**, **CR2032** · hand pulse two hands, HANDPULSE W/WIRE · GFCI warning + **Grainger 1D237 / squared.com QO120HM**, "not a warranty defect" · Engineering Mode entry: hold **Start + Stop + Enter about 5 seconds** · **FUSE 5A** on the motor controller [all but sc200, which has no fuse section] · round disk swing displacement **"within 3 mm prior to shipping"** [e25 as "+/-3mm" with a quiet-room test] · swing arm size tolerance **0.05mm~0.07mm** · incline motor **115 volt AC**, four wires red/black/white/green, 3-pin position sensor, red=UP black=DOWN white=COM green=ground · tension motor work voltage **DC 4.5~7.5V** · cross bar **7x7x25L Woodruff key, M8x40 socket head cap screw, two M8x6.3T nuts, 500 Kg-cm** · console mode timings 30-minute / 5-minute / 3-minute / 2-second.

---

## G2 — six 2019 Sole ellipticals (274 cards)

`e25-2019` 46 (525018), `e35-2019` 50 (535018), `e55-2019` 48 (555018), `e98-2019` 47 (598018),
`e95s-2019` 45 (595618), `sc200-2019` 38 (UNRESOLVED).

**Between manuals** (beyond Part 1)

| Fact | Values |
|---|---|
| Connecting-arm rod end bearing nut | e25 l.1175 §11.2: *"Hex Head Bolt 5/16" x1-1/4", flat washer 5/16" x 20 x 1.5T and nut **5/16" x 7T** which secure the Rod End Bearing."* e55 l.1111 §11-2: identical sentence, **`5/16" x 9T`** |
| Poly-V high-speed test | E25 l.984 and E35 l.973 **"100-200RPM"**; E55 l.946, E98 l.817, SC200 l.984 **"100-120RPM"** |
| Slip torque | E35 l.1123/1132, E55 l.1046/1052-1053, E98 l.920/927: **500~600 lbs** and **550~600 lbs**. E25 l.1113-1116: same two joints, **no force figure**. E95s l.1078: one joint, no force; its figure is in assembly l.1443 *"torque wrench to up to **550lb**"* |
| Tension motor drive voltage | E25 l.595 / E35 l.613 / E55 l.618 / E95s l.641: *"Level UP:**+5VDC**;Level DOWN:**-5VDC**"*, meter **+5~6.0VDC / -5~6.0VDC**. SC200 l.523-524: *"Level UP:**+2.5VDC**;Level DOWN:**-2.5VDC**"*, meter **+2.2~2.7VDC / -2.2~2.7VDC**; work voltage **DC 4~5.5V** against **DC 4.5~7.5V** on the ellipticals. E98 l.155: **EMS BRAKE Work voltage: DC 0 ~23V** — no tension motor, no steel cable. *"the single most likely place for a retriever to serve the wrong number"* |
| Tension motor connector | E25 l.491-495 / E35 l.508-512 / E55 l.512-516 `1.M+ 2.M- 3.+5V 4.VR 5.GND`; E95s l.753-760 `1.MT- 2.MT+ 3.VCC 4.VR 5.GND`; SC200 l.420-424 `1.M- 2.M+ 3.VR1 4.VR2 5.GND`. **Pins 1 and 2 are reversed** between the E25 family and the other two, and the SC200 has **two VR pins** where the ellipticals have a +5V |
| Console-to-driver connector | E25 l.668-681 and E35 l.686-704: an **11-pin** analogue harness (RPM IN, GND, +5V, MOTO AD, GND, MOTO DN, MOTO UP, VIN, INC_UP, INC_DN, INC_AD). E95s l.717-722: a **6-pin serial link** (GND, RXD, TXD, VIN0, S/W, S/W). SC200 l.581-590: a **10-pin** connector (GND, GND, +12V, SPEED, GND, GND, VR IN, +5V, M-, M+). E55 and E98 print the heading with **no readable pin list** |
| Engineering Mode | E25 l.834-848, E35 l.811-825, E55 l.792-806, SC200 l.644-658: lettered **A-F** with a Functions submenu. E98 l.672-680: **A-G** with **BRAKE TEST**, no ODO Reset. E95s l.870-878: the same A-G with **MANUAL TEST** in place of BRAKE TEST |
| Work range | E25 l.247-254, E35 l.266-273, E55 l.329-336 **"0 to 20"**; E98 l.263-270, E95s l.348-355 **"1 to 20"** |
| Pause-mode resting position | E25 l.217, E35 l.232, E55 l.295, E98 l.234 *"The ramp incline level should back to **"1"**"*; E95s l.317 *"The **STRIDE** should back to **"18"**"* |

**Inside one manual**

- **E25**: two sections are both numbered **11.7** (l.1319 "11.7 Idler Wheel Replacement", l.1336 "11.7 Flywheel Replacement"); the ToC numbers them 11.7 and 11.8.
- **E55**: **"11-9. Drive Pulley Replacement"** (l.1289) whose steps are the bushing housing; the ToC calls 11.9 "Bushing Housing Replacement". ToC l.54 calls 11.6 "Flywheel & Poly-V Belt Replacement" but body 11-6 (l.1219) is the belt only; the flywheel is 11-8 (l.1257). **END MODE paragraph is misnumbered** — l.299-309 run 5.5, 6.1, 6.1.1, 6.2 where the siblings run 6.1, 6.2, 6.2.1, 6.3.
- **E98**: **"11-8. Flywheel & Poly-V Belt Replacement"** (l.1180) whose steps are the idler wheel and belt tension; the flywheel is 11-9 (l.1196). l.354 RUN MODE, **untranslated Chinese**: `ENTER button: 切換 LEVEL 和 INCLINE PROFILE`. Its console-to-driver page (l.547) is a heading over a lost figure, so **no pinout card exists for the E98**.
- **E95s**: tension motor probe colour contradicts itself one page later — l.659-660 *"(Red probe in **blue** wire, Black probe in **green** wire)"* vs l.668 *"(Red probe in blue wire, Black probe in **brown** wire)"*. **The LEVEL entry of the function table is a copy of the STRIDE entry** — l.351-356 *"LEVEL / Display the **stride** position from 1 to 20 … Press "UP" or "DOWN" to adjust **stride**"*. l.1018 heading: *"9-4 Controller , Incline Motor,Tension Motor **Problem Problem**"*, with §248 calling the same part the STRIDE MOTOR. l.682 heads a stride VR fault *"Case of **RAMP ERROR**"*.
- **SC200**: same blue/green vs blue/Brown probe contradiction (l.542-543 vs l.551).
- **E55 has no controller LED table and no console-to-driver pinout**, so no card exists for either on that machine. **The SC200 has no calibration procedure and no fuse replacement section** — both are in all five elliptical manuals; its only power-loss guidance is l.547 *"If there is no voltage, check the transformer, if there is no output, replace it."*

**Coverage gap, not a contradiction.** `cards/` holds **122** cards with `model: '*'`. Five list the
**unyeared** elliptical ids in `applies_to` — `sole-garmin-pair-non-touchscreen`,
`sole-plus-strava-sync`, `sole-lwr-not-match`, `sole-heart-rate-monitor-other-brands`,
`sole-garmin-supported-watches-broadcast` — carrying `e35`, `e95`, `e95s`, `e98` and **never**
`e25-2019`, `e35-2019`, `e55-2019`, `e95s-2019`, `e98-2019` or `sc200-2019`. `applies_to` is checked
for membership, not completeness, so **`kb lint` cannot see this**.

**Nothing was lost in table rebuilding.** G2 §5.14: every table with recoverable columns was rebuilt
as Markdown; no fenced "unrecoverable" block was needed.

---

## G3 — five 2023 Sole ellipticals (182 cards)

`e25-2023` (525022), `e35-2023` (535022), `e95-2023` (595022), `e95s-2023` (595622),
`e98-2023` (598022). Covers: SE668S-SE038, SE678S-SE039, SE698-SE040, SE895B-SE041, SE868-SE042.
Two PDFs existed for the E35 (a factory issue and a SOLE-branded one) with **byte-identical
extracted text**; one source was kept.

**Between manuals**

| Fact | Values |
|---|---|
| Driver board controller number, §8.3 "LWR not match" | e35 p18 and e95s p20 **`CS51005-11S`**; e95 p18 and e98 p17 **`CS51005-21S`**. *"Every other word of section 8.3 is identical in the four."* |
| Resistance setting before releasing the steel cable | e25 §9.8 STEP 2 p33 and e35 §9.8 STEP 2 p29 *"adjust the resistance to **level 20**"*; e95 §9.10 STEP 2 p31 *"adjust the resistance to **level MAX**"* |
| Resistance hardware | e25 p5, e35 p6, e95 p6, e95s p7 *"**Gear Motor** Work voltage: **DC 4.5~7.5V**"*; e98 p6 *"**EMS Brake** Work voltage: **DC 0~21V**"* |
| Incline motor supply | e25/e35/e95/e95s *"This is a **115-volt** AC motor."*; e98 p6 *"This is a **115(220V)-volt** AC motor."* |
| Console and error set | e25 p5 *"keypad to control and **LCD Display**"*, errors `E1 / E2 / E3`. e35/e95/e95s/e98 *"Contain keys control and **TFT LCD touch panel**"*, errors `EEPROM ERR / LWR not found / LWR not match`. **A single answer about "the 2023 Sole elliptical console" is wrong for one half of the range whichever half it is written from.** |
| Fuse section | e35 §8.7 p24, e95 p24, e95s p26, e98 p23 carry "Replacing the Fuse". **The e25 manual has none**; its only fuse mention is §8.2 step 5 p21 *"If there is no voltage, inspect the power socket and the holder FUSE."* **No manual gives a fuse rating or a part number.** |

**Inside one manual**

- **The four touchscreen manuals list an error code they do not define.** Each prints exactly three error codes and then a matrix row: *"**INCLINE ERR**, INCLINE window shows "**E3**" error code. | Position sensor value of incline motor is wrong. | 1 Turn off the AC switch and turn on power again. 2. Follow 8.6 Calibration procedure to calibrate the incline motor."* — e35 matrix p25 / list p17, e95 p25 / p17, e95s p27 / p19, e98 p24 / p16. **E3 exists only in the E25 manual of the same year**, where it is the ramp error.
- **e98 §9.9 is headed "Replacing the Flywheel" and never removes a flywheel** (p31): *"STEP 2: First, disconnect the wires which connecting the induction brake… STEP 3: use an **11mm** wrench to unscrew the **1/4" x 3/4"** carbon steel hex screws that secure it. There are **four** screws in total… STEP 4: To reinstall, start by placing the induction brake back onto the flywheel mounting plate."* **The flywheel itself is never removed anywhere in the manual.**
- **e95s cannot decide whether the motor sets stride or incline** (both quotes on p7): *"**Incline Motor** This is an AC motor. User can control **Stride** length by console"* and *"If there is AC voltage on the red wire (UP) the **incline** motor will increase the **incline**."* Its matrix (p27) carries INCLINE CABLE and INCLINE ADJUSTMENT SWITCH rows and its calibration page is "Incline Calibration".
- **e95s §9.7 sets the console to two stride lengths for one job**: STEP 2 p45 *"adjust program to **21"**"*; STEP 17 p49 *"adjust program to **18"**, and then fasten socket head cap bolt (**M8x40L**) which fixed on spring."*
- **e95s torque figures have no length unit**: §9.5 STEP 14 p41 *"using the torque wrench to up to **550lb**"*; §9.6 STEP 12 p44 *"lock **M8 × 20L**_Socket Head Cap Bolt to **150lbs**"*. Compare the properly dimensioned cross bar step: *"tighten M8x40 socket head cap screw together with two M8x6.3T nuts until it reaches **500 Kg-cm**"* (e25 §9.5 STEP 5 p32).
- **e95s §9.2 STEP 6 p31 prints its last clause twice**: *"…and then it can remove the Side Case (L) and then it can remove the Side Case (L)."* STEP 1 p30 calls a part the **"Seat Handlebar"** on a machine with no seat.
- **"Chain Covers" and "Side Cases" are the same part, named both ways**: e25 §9.6 STEP 1 p32 *"Follow procedures 9.2,9.3, 9.4 and 9.5 to take apart Connecting Arm, Pedal Arm, both **Chain Covers** and the Cross Bar"* — but 9.4 is titled *"Replacing the **Side Case** (R/L)"*. Same in e35 §9.6 p28, e95 §10.2 p35, e98 §10.2 p35.
- **e25 Function table, pp7-8**: *"**RPM**  Display the current speed in **mile per hour**. DISPLAY range is 0 to 888. WORK range is 0~120"* — the row is headed RPM and described as mph.
- **e95 §9.9 p31 says bolts then bolt** for the same fastener: STEP 2 *"release **M8 x 20 carriage bolts**"*, STEP 3 *"tighten **M8x20 carriage bolt**"*.
- **§10.5 d) and §10.6 a) are word-for-word duplicates** in e95 (pp38, 39), e95s (pp58, 59, lightly reworded) and e98 (pp38, 39): *"If the incline motor does not function, first check the proper connection of the cables then the damage of the incline controller, the transformer, and the console."*
- **e25 sleep timer**: p6 *"it will enter sleep mode if there is no key press for **15 minutes**"* vs §8.5 p28 *"III. Sleep Mode - Turn off to have the console power down automatically after **30 minutes**"*.

**Against committed cards**

- **EMS brake voltage**: `cards/e98-2019/specs/ems-brake-spec.md` (from the 2019 manual, General Information p14) *"**Work voltage: DC 0 ~ 23V.**"* vs `sole-elliptical-e98-2023-service-manual` p6 *"EMS Brake  Work voltage: **DC 0~21V**"*.
- **E25 incline range and readout name — the sharpest same-model-different-year trap in the set.** `cards/e25-2019/console/console-data-ranges.md`: `| INCLINE | 0 to 99 | 0 to 20 | position shown 1 to 20 |` and `| SPEED | 0.0 to 99.9 | 0.0~99.9 | miles per hour |`. The 2023 manual pp7-8: *"INCLINE  DISPLAY range is 0 to 99. **WORK range is 1 to 15**."* and the speed row is now headed *"**RPM**  DISPLAY range is 0 to 888. WORK range is 0~120"*. **"What is the max incline on a Sole E25" returns 20 from the 2019 card and 15 from the 2023 card.**
- **E1 sends you to a different board**: `cards/e25-2019/errors/e1-eeprom-failure.md` *"**replace the upper controller**. The manual gives no other step for E1."* vs 2023 §8.1 p19 *"The EEPROM is abnormal, please replace the **Display Board** directly."*

**Agreements worth recording so nobody "fixes" them**: belt tension **190 Hz (+/- 10 Hz)** identical
in all five, in every 2019 elliptical card and the CC81 climber cards · e95s stride zeroing **245 +/-
1 mm with two and a half circles** identical in `cards/e95s-2019/specs/stride-motor-spec.md` and the
2023 manual §10.6 c) p59 · the GFCI and high-inrush breaker paragraphs (Grainger 1D237 / QO120HM)
word for word between 2019 and 2023.

**Extraction damage specific to the E95s**: "N of 60" page furniture leaves content-free lines
(l.129 "4 of 60", l.350 "15 of 60"), and tokens run together where the PDF had no space —
`twoψ3x20 Tapping Screws`, `smallerψ17`, `use3.5x16self tapping screw`, `Bψ178x41LRotate Axle`,
`than ψ25 and hit`. Split by hand in the card bodies with the numbers kept exactly. Its part-number
references (`#137`, `#176`, `#165`, `#16`, `J4FM-1719-09`, `WFM-2528-21`, `WFM-1719-12`) point at an
exploded diagram **not in this document**, so no parts-list card was written.

---

## G4 — E25 2026, SR500 2016, SR550 2023, C80 2026 (133 cards)

`e25-2026` 34, `sr500-2016` 43, `sr550-2023` 38, `c80-2026` 18. **The first rower cards in the
repository** — `grep -rl "rower" cards/` previously returned exactly one file.

**Between manuals**

| Fact | SR500 2016 (`CW800A-YR001`) | SR550 2023 |
|---|---|---|
| Resistance motor work voltage | §3 l.95 *"**Tension motor** / Work voltage:**DC 4.5~7.5V**"* | §3 p5 l.76 *"**Gear Motor** / Work voltage: **DC 4.5~5.5V**"* |
| Meter setting | §7.2 **12VDC** | §8.1 p17 **20VDC** |
| Red probe on | **blue wire** | **brown wire** |
| Black probe on | **green wire** | **black wire** |
| Level UP normal | **+5.5 ~ 6.5VDC** | **+5~6.0 VDC** |
| Level DOWN normal | **-5.5 ~ 6.0VDC** | **-5~6.0 VDC** |
| Error codes | l.396-397 `E1 Console (Electronic Desk) EEPROM failure` / `E2 Cable tension communication error` ("MOTOR ERROR", all functions stopped) | l.308 `E2 Gear motor is failure` — **and that is the whole list. The SR550 documents no E1 at all.** The two E2s are not the same fault: SR500 E2 is a *communication* failure, SR550 E2 is "the motor does not move" on a Level key press |
| Seat/track pulley | §8-8 steps 5-6 l.707-710: **two** bolts, `3/8" × UNC16 × **1-1/4"**_Button Head Socket Bolt(105)` and `3/8" × UNC16 × 4-1/4"_Socket Head Cap Bolt(104)`, each with `3/8" × 11T_Nyloc Nut(106)` and `Pulley(54)` | §9.8 step 5 l.527-528: **one** bolt, `3/8" × UNC16 × **32mm**_Button Head Socket Bolt (105)` with `3/8" x 19 x 1.5T_Flat washer (109)`, `3/8" x 21 x 2T_Flat washer (130)`, `3/8" × 11T_Nyloc Nut (106)`, `Pulley (54)` |
| Chain cover foam | l.570 *"must aim at the **hole**"* | l.414-415 *"must aim at the **groove**"* |

The SR550's wire colours and meter setting **match the E25 2026 elliptical** (l.424: 20VDC, red
probe in brown, black probe in black). **The SR500's blue/green pair is the odd one out across the
whole group.**

**Agreement**: drive belt `6PJ-787L` (24) at `70~80BLS` in **both** rowers (SR500 l.635-636, SR550
l.473-474); the Grainger 1D237 / QO120HM paragraph is word-for-word identical in the E25 2026
(l.318) and SR550 2023 (l.282).

**Inside one manual**

- **e25-2026**: **the Distance window or the Incline window?** §8.3 step 4 l.507-509 *"The **Distance window** will display the computer incline setting … is a counter that is showing the actual position sensor output. If the motor is moving and there is no count occurring in the **Distance window**…"*; step 8 l.527 *"…but no count in **Incline window** when motor is moving then there is a problem with the console."* **ToC omits four sections that exist in the body** — 8.4 Circuit Diagram (l.594), 9.2 Replacing the Connecting Arm (l.695), 9.3 Replacing the Pedal Arm (l.706), 9.7 Replacing the Idler Wheel Assembly (l.758); **9.2 and 9.3 are the entry point for nearly every other procedure**. §9.6 step 1 l.749 names *"both **Chain Covers**"* — procedure 9.4 is "Replacing the Side Case (R/L)" and there is no chain cover section. Circuit diagram sheet l.581 misspelled `ELLIPICAL CIRCUIT DIAGRAM`.
- **sr500-2016**: **E1's meaning and its on-screen message disagree** — l.396 `E1 Console (Electronic Desk) EEPROM failure` vs §7.1 l.411 *'When the screen displays "E1" "**RAM ERROR**" message, it means that the system console EEPROM failure'*. **Section number 7.5 is used twice for unrelated content** — l.100 inside "4. CW800A-YR001 Product Operation": *"7.5 Function Description"*; l.482 inside section 7: *"7.5 Troubleshooting Quick Lookup Table"*. **Part (35) has two names** — "**RF Module(35)**" in §8-11 l.768 and "**Gear Motor(35)**" in §8-6 and §8-11 (l.667, 758, 778), described as different components doing different jobs. l.233 *"The default distance is **1:00**"* in the Time program — 1:00 is a time, and this is §IV item 4, the count-down mode. **Duplicate sub-numbering**: l.123-124 print "5.1" twice; l.251-252 print "5-3." twice. **Figure captions repeat**: *"Fig. 2-1, Fig. 2-2, **Fig. 2-2**"* (l.230), *"Fig. 4-1, Fig. 4-2, **Fig. 4-2**"* (l.259), *"Fig. 6-1, Fig. 6-2, **Fig. 6-2**"* (l.284) — the third should be -3 each time. **Roman-numeral sections start at III** (l.151 "III. Key button Function", l.184 "IV. Operating Instruction"); there is no I or II.
- **sr550-2023**: the gear motor's **work range is below the manual's own "normal" test reading** — l.76 *"Work voltage: DC **4.5~5.5V**"* vs l.346-347 *"The normal reading should be **+5~6.0 VDC** / **-5~6.0 VDC**"*. **Console-drives-motor vs drive-board-drives-motor**: l.329 *"**Console directly controls the motor.** Level UP: +5VDC; Level DOWN: -5VDC"* and l.335-336 *"Inspect **console power output** to the motor"* against l.343-344 *"place the probes on the motor control wire … on the **drive board**"* and l.363 *"The **console to driver board** connector pin define function."* **Transformer or power pack**: l.337-338 *"inspect whether the **transformer** has power"* vs l.89 *"supplied by the **power pack** that is connected to 115 VAC"*. **Part (47) has two names** — "Seat **Up/Down** Adjustment Knob (47)" §9.9 step 4 l.542 vs "Seat **Folding** Adjustment Knob (47)" §10.4 item 3 l.646; the SR500 calls the same number the Seat Up/Down knob. **The upper computer cable is described three ways** — §9.2 l.423 *"**11P** upper Computer cable (44)"*, l.424 *"11P Computer Cable (Upper) (44)"* with *"**8P** Computer Cable (Lower) (45)"*, §10.1 l.565 *"**500mm** Computer Cable (Upper) (44)"*. **There is no console key map anywhere in the manual**: the physical START key (l.189-190) is mentioned once and never described.
- **c80-2026**: **the main-parts photograph and the parts list use unrelated numbering and disagree on a name.** Photograph (p3): `1 Console`, `2 Gear Shift Assembly`, `6 Moving Wheel`, `7 Foot Pad`, `12 Foot Pad`, `13 Handle`. Parts list: `47 Console Assembly`, `40 Gear Shift Assembly`, `9 Transportation Wheel`, `8 Foot Pad (qty 4)`, `7 Handle`. **Item 7 is "Foot Pad" on the photograph and "Handle" in the parts list**, and "Foot Pad" is callout **7 and 12** on the same photograph. **Two body sections are missing from the ToC** — *"Replacing the Magnetic Resistance Assembly, Flywheel, and Belt"* (p13, l.276) and *"Replacing the Limit Wheel and 608 Bearing"* (p15, l.338); the first is **the main drivetrain procedure on this machine**. The ToC entry "Replacing the Flywheel Pulley," ends in a stray comma. The manual is **361 lines for 17 pages**, roughly half parts list, with **no safety section, no warranty text, no maintenance schedule and no assembly instructions** — that is the document, not the extraction. Revision History (p17): *"Version 1.0 / 2026/6/10: Initial release"*.

**Extraction risk to audit.** `sole-c80-2026-service-manual` **pages 8-15 are letter-spaced** —
every step arrives like l.160: `St ep 1: U si n g a P h il li p s scre wd ri ve r, r e mo ve th e
fo u r M5 × 12 L p an he ad Ph il l ip s scre ws`. G4 rebuilt all ten procedures by removing the
intra-word spacing; **no number, size, quantity or step order was changed**, but *"anyone auditing
should re-read pages 8-15 against my cards; this is the source in my group most likely to have a
transcription slip."*

**One table was recoverable and rebuilt**: the SR500's tension motor connector definition
(l.362-392) survived as loose label/value pairs across a drawing; the three sockets and their pin
numbers are unambiguous. **Pin 2 of the power socket is printed as a bare `/` and was left as
printed.**

**Against committed cards** (beyond Part 1): the incline position readout **changed window and
scale** — `cards/e25-2019/errors/incline-motor-test-procedure.md` *"The **INCLINE window** shows the
computer incline setting after speed calibration ends; **20 for max incline, 0 for lowest
incline**"* vs 2026 l.507-508 *"The **Distance window** will display the computer incline setting;
The **AD value** corresponding to the maximum Incline is approximately **40**, and the AD value
corresponding to the minimum Incline is approximately **924**."* — **different window, different
scale, and the 2026 scale runs backwards**. Incline calibration changed too:
`cards/e25-2019/console/incline-calibration.md` *"Press the **Incline UP key and the Start key** …
hold them down for **5 seconds**"* vs 2026 §8.6 l.634-636 *"Press the **Start key and the FAN key**
… Hold them down for **3 seconds**."*

**No conflict, recorded so the sweep is safe**: `cards/shared/specs/ftms-bluetooth-app-support.md`
line 49 lists `| Rower | SR500 |` under "Machines with no Bluetooth at all"; the SR500 2016 manual
describes only an RF module and a wireless heart-rate receiver. The SR550 2023 postdates that 2021
tracker and **does** sync to SOLE+ over its Android console, so the tracker's silence about the
SR550 is expected.

---

## G5 — six 2023 Sole bikes (126 cards)

`b94-2023` 21 (594122, SU415A-SB025), `r92-2023` 23 (592122, SR425A-SB025), `lcb-2023` 21
(511122, SU615A-SB026), `lcr-2023` 23 (522122, SR625A-SB026), `sb1200-2023` 22 (512322,
SB950-SB027), `sb900-2023` 16 (590322, SB910-3268T).

**Between manuals** (beyond Part 1)

| Fact | Values |
|---|---|
| Seat back procedure, the two recumbents | `lcr-2023` §9.8 step 2 p31 l.510: *"Use Phillips Head Screwdriver to unscrew Seat Back Cover, **4pcs of M5×15m/m** Phillips Head Screws as shown in figure 2."* `r92-2023` §9.8 p31 l.658-663: **no equivalent step** — straight from the frame bolts to *"Use Combination **M5 Allen Wrench** to release **M8×15m/m** Button Head Socket Bolt (**179**) to take Seatback Cushion (**63**) apart."* Either the R92 has no seat back cover or a step was dropped; the R92 version also numbers its parts and the LCR version does not |
| Controller number and cable | `lcb-2023` and `lcr-2023` §8.2/8.3 p18: **CS51012**, **6 PIN** computer cable. `sb1200-2023` §7.2/7.3 p15: **CS51006-02**, **7 PIN** computer cable |
| EEPROM label | `b94-2023` l.300 and `r92-2023` l.301: `E1 \| EEPROM failure`, detail page displays "E1". `lcb-2023` l.264, `lcr-2023` l.271, `sb1200-2023` l.228: `EEPROM ERR \| EEPROM failure`, detail page displays "EEPROM ERR" — the reason the two LCD bikes use `code: e1` and the three touchscreen bikes use `code: eeprom-err` |

**Inside one manual**

- **b94/r92 (§4, 8.1, 8.2, 8.4, 8.5 are word for word identical)**: **the Enter button is dead and the data-scan key in the same section** — IDLE and EXERCISE tables *"Enter Button   Non-function."* vs the Display key row *"When in the exercise state, press the **Enter** key to switch the display of exercise data. If the message is to display the last data, press the Enter key again to display the data scan…"*. **RPM labelled as speed**: *"RPM   Display the current speed in **mile per hour**. DISPLAY range is 0 to 888. WORK range is 0~120"*.
- **b94-2023 §10.3 heading vs its problem line** (l.739-740): heading *"10.3 Troubleshooting for the **Noise** during pedaling"*, first line *"Problem: The drive belt is **slipping** when pedaling."* The steps under it are the noise steps. `r92-2023` gets it right (l.864: *"Problem: The Bike is making noise when pedaling."*).
- **b94-2023 §9.3 step 3 releases a part that was already removed** (l.484-485): *"Using **12 wrench** to release **7pcs of 5/16" × 5/8"**_Hex Head Bolt, **6pcs of 5/16" × 18mm ×1.5T**_Flat Washer and **1pcs of 5/16" × 19 ×1.5T**_Curved Washer and the **Handlebar** can be released."* The handlebar came off in §9.2 and step 4 refits these same bolts to the **console mast**. **Same defect in `lcb-2023` §9.3 step 3** (l.391-392).
- **r92-2023 §10.2 names a part this bike does not have** (l.854-855): *"inspect and potentially replace the Drive Pulley (**20**), Idler Wheel Assembly (**10**), or **Generator/Brake (55)**."* §9.7 calls part **55** the **Flywheel**, and the R92 brakes with a gear motor and a steel cable, not a generator. **The sentence is copied from the LCR 2023 manual**, which does use a generator flywheel.
- **r92-2023 contents page is missing its first line** — it begins at "2.Electronic Parts" (l.11); section 1 Outlines is printed on p3 (l.53).
- **r92-2023 §9.1 step 4 runs two screw sizes together** (l.445): *"release **four M5 3.5×12mm** Phillips Head Screws then remove the PAD holder."* **Same in `lcr-2023` §9.1 step 4** (l.366).
- **§9.11 heading misspelled "Replacing the **Sear** Carriage"** in both `r92-2023` (l.728) and `lcr-2023` (l.576). **§9.12** heading says "Aluminum Rail and **Stabilizer Cover**", step 2 says "take apart the **Step Cover**", in both.
- **lcb/lcr idle arm fastener named two ways, and the removal step ends mid-phrase.** `lcb-2023` §9.8 l.487-494: step 2 *"unscrew **3pcs of M6x7T** Phillips Head Screws on Idle Arm (9)"* — **M6 x 7T is a nut description, not a screw length**; step 3 *"Unscrew 3pcs of **M6x15** Phillips Head Screws (56) with 3pcs ofø1/4" Split Washers (73) and 3pcs of 1/4”x13x1T."* — **the sentence stops with no part name**; step 4 completes it, *"3pcs of 1/4”x13x1T Flat Washers (69)"*. **The same three defects appear in `lcr-2023` §9.5 steps 3-5** (l.464-473).
- **Part 20 has two names in `lcb-2023`**: §9.8 step 4 l.495 *"secure the **Generator Flywheel (20)**"*; §9.9 step 2 l.505 *"Unplug electric wires connected to the **Induction Brake (20)**"*. In `lcr-2023` the same part gets **three** names — heading 9.7 "Replacing the **Induction Brake**", step 2 "**Generator Flywheel**", §10.2 "**Generator/Brake (55)**".
- **lcb-2023 §10.2 names a bearing housing this bike does not have** (l.573): *"Try to replace the drive pulley, **Bearing Housing** or flywheel."* The LCB uses a J-bolt tensioned idle arm; the sentence is copied from the B94 manual.
- **lcb-2023 §9.10 step 1 removes only chain cover L to reach the drive pulley** (l.516), while §9.7 puts the drive pulley behind the **right** side case and §9.8 removes both covers.
- **sb1200-2023 has no safety section, no belt-slipping answer, no noise section and no grounding or outlet instructions.** Its Engineer Mode names four pages (*"FUNCTION, SERVICE, FACTORY SETTING, and CALIBRATION"*) and **prints only the FUNCTION page's contents**.
- **Part 83 is a cap nut in one section and a nylon nut in another**: `sb1200-2023` §8.3 STEP 1 l.375-376 *"use a **10mm ratchet wrench** to remove the **cap nut - M6×6T (83)**"* vs §8.5 STEP 1 l.408 *"remove the **nylon nut - M6×6T (83)**"*. **Same in `sb900-2023` §6.3 and §6.5.**
- **sb900-2023 MODE key cycle listed two ways**: §4 p8 l.116 *"Press 'MODE' key to select **TIME, DIST, KCAL**"*; §5.1 Situation 2 p10 l.178 *"Press 'MODE key' repeatedly to toggle between **SPEED (SPD), DISTANCE (DIST), TIME (TIME) and CLOCK (CLK)**"*. The shared card `sole-spinner-quick-start-and-mode` **already records this same disagreement** for the SB700 2020 / SB900 2020 manuals; it is reprinted here unchanged.
- **sb900-2023 quick-release lever 38 does two different jobs**: §6.7 STEP 2 l.413-414 detaches the **Sliding Handlebar Mount (7)**; §6.8 STEP 2 l.427-428 detaches the **dumbbell rack assembly (27)** and the **Sliding Seat Mount (6)**.
- **sb900-2023 describes a connection message as a calibration result**: §5.2 step 1 l.229-230 *"Confirm that the console is connected to Smart Tension. **When the calibration is successful**, the LEVEL symbol on the console will flash rapidly for 2 seconds, indicating the Smart Tension **connection**."* Calibration has not started at that point.
- **sb900-2023 has no belt-slipping answer and no noise section.** The only belt figure in the whole manual is the 180 lbs line in §6.4 STEP 3.

**Against committed cards** (beyond Part 1)

- **END mode timeout changed on the LCD bikes**: `sole-bike-lcd-console-modes` *"With no key press for **3 minutes** it returns to idle mode"* vs b94-2023 l.132-133 / r92-2023 l.133-134 *"…it will automatically return to idle mode in **5 minutes**."* The 2023 **TFT** manuals still say 3 minutes.
- **The exercise data scan list gained an entry**: `sole-bike-lcd-console-buttons` *"cycles every four seconds through: LAPS XX, SPEED XX.X MPH, L XX MAX LV XX (program mode only), **WATT XXX.X**, SEG TIME XX:XX"* vs b94-2023 l.211-217 / r92-2023 l.212-217 — `LAPS XX`, `SPEED XX.X MPH`, **`SPEED XX.X RPM`** (new), `L XX MAX LV XX`, **`WATT XXX`** (lost its decimal), `SEG TIME XX:XX`.
- **The touchscreen console lost physical keys**: `sole-bike-tft-console-buttons` tables list STOP, START, LEVEL UP / LEVEL DOWN, FAN, DISPLAY, ENTER; lcb-2023 l.173-186 and lcr-2023 l.180-193 list only **Stop, Start, Fan, Display**.
- **No conflict, recorded so the sweep is safe**: `sole-bike-power-outlet-requirements` says the LCB 2016 and B94 2019 manuals print only the 120 V / 15 A figure and four others add a 220 V / 10 A line. **All four 2023 upright and recumbent manuals print only 120 V / 15 A** — none has the 220 V line. `sole-bike-breaker-trips-or-gfci` matches word for word, Grainger 1D237 and QO120HM included.

**The SB1200 2023 and SB900 2023 share a frame.** §8.2-8.6 of the SB1200 and §6.2-6.6 of the SB900
are **word for word identical**, with the same part numbers: 34, 79, 80, 47, 48, 32, 33, 66, 72, 70,
73, 67, 65, 74, 89, 71, 15, 77, 28, 62, 75, 17, 68, 30, 53, 49, 50, 83, 21, 22, 24, 78, 85, 86, 87,
104, 105, 16. Only the handlebar sections differ (the SB1200 has a screen rack and screen rotation
assembly). Five procedures and the 180 lbs belt tension are **one fact each across two machines**,
written twice as the rules require.

**One deliberate exception G5 wrote rather than lean on a shared card**: `sb900-2023-speed-sensor-pairing-note`,
because the SB900 2023 now has **two** pairing procedures that both start by holding **MODE and
PAGE** — the speed sensor transmitter (§5.3) and the new Smart Tension knob (§5.2). Without a
machine-specific `not_to_be_confused_with`, a technician following the shared card runs the wrong one.

---

## G6 — SRVO service manual (49 cards, one source, 44 pages / 687 lines)

All `model: srvo`, `product_line: strength` (see decision 18). Pre-existing srvo cards: **36**, not
the 74 the assignment claimed. Two further cards name `srvo` in `applies_to` only —
`cards/shared/console/sole-plus-strava-sync.md` and
`cards/shared/specs/heart-rate-monitor-other-brands.md`.

**Findings beyond Part 2's decisions 11-14, 37, 61-63**

- **Motor power port pins are numbered 1, 3, 5** — p36 §8-2-2: `1 \| U`, `3 \| V`, `5 \| W`. **Pins 2 and 4 are absent from the table with no note.** Preserved as printed.
- **Two different boards share one section heading.** p34 `8-2 Controller module` → CN3 AC, CN2 Motor power, CN6 RS485, CN7 Encoder. p39 `8-3 Controller module` → CN3 AC input, CN1 DC output, CN2 DC output. **Section 8-3 is the full range power board** — p17 step 6 calls it "full range PFC power board", p5 "Full Range Power Supply", p10 row 19 "Full range board" — not a third controller. **The table of contents repeats the wrong heading.**
- **Six CN numbers mean different things on different boards inside one machine** — the look-alike trap this manual introduces:

| Connector | Display main board | Controller module | Full range power board |
|---|---|---|---|
| CN1 | Debug port | — | DC output |
| CN2 | — | Motor power (UVW) | DC output |
| CN3 | — | AC port, 2 pins, no PE | AC input, 3 pins with PE |
| CN5 | RS485 + 12V | — | — |
| CN6 | Left speaker | RS485 interface | — |
| CN7 | Right speaker | Encoder port | — |

  Every pinout card names its board in the first body line and lists the other board's
  same-numbered connector in `not_to_be_confused_with`. **If these cards are ever merged or
  shortened, that cross-linking is the part that must survive.**
- **"Multiple power cords" against a one-cord parts list.** p8: *"the device may have multiple power cords. To completely power off the device, make sure all power cords are disconnected."* p10 explosive view row 18: `Power cord | 1`; the key component list holds one mains cord (row 1).
- **A battery safety section for a machine with no battery.** p8 devotes two of its four "Matters need attention" items to batteries (*"Please use the same battery when replacing battery"*, *"Heating the battery to more than 100°C (212°F)"*). Neither the explosive view (24 rows) nor the key component list (16 rows) contains a battery. The only battery on the product is the coin cell in the wireless switch, **which this manual never mentions**.
- **The explosive view has no servo motor.** p10 lists 24 parts and no motor; p5 calls out "13 Servo Motor Module" and p13 is a whole step for removing two of them. The motor appears only in the key component list, row 12.
- **Ambiguous bolt count** — p18 step 7: *"Use a **4mm** Allen wrench to remove the **four** bolts in the upper circle of the **two** electronic control components **respectively**"* — reads as four each, eight total, but no total is printed.
- **Not a contradiction but it will look like one**: row 12 rates the motor at **220V** while row 6 rates the power module input at **90 to 130V**. Consistent, because the PFC module's stated output is **0 v-330 v** — the 90-130 V is the wall supply and 220 V is the motor bus.

**Against committed cards** (beyond decision 11)

- **What "number 4 on the controller module" is.** `srvo-encoder-location` (authority **3**, `sole-srvo-seminar` PDF p49): *"The encoder is on the controller module. The seminar marks it as **number 4** in its diagram."* The manual (authority **3**, p34) makes **number 4 = CN7 = Encoder port**, and p38 §8-2-4 gives CN7 an 8-pin pinout — `ENC_Z-`, `ENC_Z+`, `ENC_B-`, `ENC_B+`, `ENC_A-`, `ENC_A+`, `ENC_5V`, `ENC_GND`. *"A differential quadrature output with its own 5 V and ground is the signature of a sensor mounted on the motor and cabled back."* Both authority 3; the two documents are probably describing **two different diagrams** that happen to share the number 4. If a human confirms the encoder is on the motor, that card's first sentence needs a rewrite, **not a delete** — its "two controllers" claim is independently confirmed by the manual (p10 row 10, `Controller | 2`).
- **One speaker or two.** `srvo-parts-layout` (authority 3, seminar p20): *"**Speaker** - plays the audible announcements"*, singular, no count. The manual: p10 row 13 `Speaker | 2`, row 14 `Speaker bracket | 1`; p30 §8-1 `CN6 | Left Speaker port` and `CN7 | Right Speaker port`; p33 L+/L-/R+/R- pinouts; p28 two speaker part numbers. **The SRVO has two.**
- **A gap the manual closes.** `srvo-cable-stuck-back-cover` ends *"The seminar gives no torque figures and no Allen key size, and no warranty guidance for opening the unit."* The manual supplies the size and counts — p12 step 1 *"first unscrew the **four shock pads** in the four-corner frame counterclockwise, and then use a Phillips screwdriver to remove the **14 screws**"*; p13 step 2 *"Use a **6mm Allen wrench** to remove the four screws (**8 in total for two motors**)"*. **The other two halves stay true: the manual prints no torque figure anywhere, no warranty guidance for opening the unit, and no reassembly sequence at all — eleven removal steps, zero refit steps.**
- **The manual answers nothing about** the four safety features, the three training modes, the app, the bench or the warranty. It contains **no** mention of static safety, tilt safety, drop safety, the resistance stop point, Standard/Eccentric/Isokinetic mode, the wireless switch, the phone app, the bench, warranty terms, resistance range or user weight capacity. It never contradicts those 36 cards because it never touches them. The one near-miss, p42 §8-4 *"Wireless control module"*, has **no body text at all**.

**Text damage repaired**, all in the p28 key component list: `3 C ores` → `3 Cores`,
`full f requency` → `full frequency`, `PHS-5Y T O` → `PHS-5Y TO`, `4 000rpm` → `4000rpm`,
`M CU:ESP32` → `MCU:ESP32`, `YD. ESP32` → `YD.ESP32`; `24N×m` kept; the two-line wrap on rows 5, 7,
12 and 14 rejoined. **One piece not repaired** — p32 §8-1-2, CN1 pin 5: `5 | GPIO0 | Enter 0BOOT
mode`. `0BOOT` is almost certainly `BOOT` with a stray leading zero (GPIO0 is the ESP32's normal
boot-select pin) but the printed string was not silently corrected.

**Untranslated or unexplained strings in the p28 key component list**, preserved verbatim: motor
row 12 carries a bare **`5`** between `6:1` and `80%` with no unit or label, and the phrase
**`optical brining`**; display control row 8 has `digital tube`, `KG and LBS soft cutting`,
`power station`; power board row 6 says **`without firmware`** and the manual never says where
firmware comes from or how it is loaded; row 1 carries certificate codes
`A12-0127-AC2+A12-0120-AC2`; supplier codes `BS`, `YQ`, `GXD`, `SH`, `SK`, `TDA`, `QL`, `LCJD`
appear as row suffixes **with no legend**.

**Merge candidates**: only p7's connect/disconnect ordering and electric-shock bullet list, and p8's
battery rules — *"generic IBM-style safety boilerplate, not SRVO-specific"*. If the same block
appears in other Dyaco service manuals, `srvo-connect-disconnect-order` and
`srvo-service-electrical-safety` should probably become one shared card.

---

## G7 — F60 2016/2020, F63 2016/2019/2023/2026 (258 cards)

`f60-2016` 44, `f60-2020` 42, `f63-2016` 48, `f63-2019` 47, `f63-2023` 40, `f63-2026` 37.
OEM codes: `AT90I-NT007`, `AT90P-NT038`, `ST125`, `ST128-YT043`, `GT98-YT068`, `GT88-YT088-01`.

**The single biggest wrong-answer risk in the batch.** `sole-tm-f63-2026-service-manual` uses a
**different error code family entirely**: pages 47-48 list **E3, E01, E02, E03, E04, E05, E06, E3,
E22, E31**, where every other manual lists **E0 to E7** (or E0, E1, ER, E2, E4, E5, E6 for the F60
2016). *"The two families share the strings "E3", and nothing else. **`E01` is not `E1`, `E02` is not
`E2`, `E03` is not `E3`**."* The 2026 machine also uses a **brushless DC motor with U/V/W terminals
and a Hall sensor**, where the others use a brushed motor with M+/M- and a reed switch. Every 2026
card opens with a look-alike warning.

**The incline fault is not the same code on every machine**

| Manual | Locator | Code |
|---|---|---|
| `sole-tm-f60-2016` | p36 | **`ER`** — *"The console didn't receive Incline feedback signal, ER will be appeared at incline window, but the treadmill able be operate."* **This manual has no E3 at all.** |
| `sole-tm-f60-2020` | p32 | `E3` |
| `sole-tm-f63-2016` / `-2019` / `-2023` | p36 / p36 / p19 | `E3` |
| `sole-tm-f63-2026` | p47 | `E3`, in the different family above |

**A customer with a 2016 F60 reporting "ER" will not match an E3 card.** `f60-2020` §8.x p46
l.731-732 still carries the older wording: heading `Error Message： INCLINE E3`, definition *"During
incline action, the display board CPU cannot read the VR value, so **INCLINE ER** appears."* —
**this manual has no ER code.**

**"Belt does not move after 10 seconds" is a different string per manual**

| Manual | Locator | Printed |
|---|---|---|
| `sole-tm-f60-2016` | p61 l.1180 | *"running belt isn't running and window displays **"LS"** error message after 10 seconds"* |
| `sole-tm-f60-2020` | p56 l.959 | *"…displays **"E1"** error message after 10 seconds"*, and adds *"the **Shut-D light will be always bright**"* |
| `sole-tm-f63-2016` / `-2019` | p64 l.1433 | *"display shows **"LS1/LOW SPEED"**, run calibration"* |

**Other cross-manual differences**

| Fact | Values |
|---|---|
| E4 lower-controller row | f63-2016 p53 *"Insert power wire of motor."*; f63-2019 p53 *"Insert power wire of motor **or Replace Lower controller board**."* |
| Lubrication interval and method | see 1.14 — the F60 pair is 25 h then every 50 h with half a bottle poured under the centre and a 3-5 minute walk; the F63 pair is 90 h with the 18" / 4-6" / 1/8" x 15" S-pattern and a five-minute walk |
| Drive belt wrench | 14 mm in F60 2016/2020 and F63 2016/2019/2023; **13 mm** in f63-2026 p58 — *"Adjust belt tension using a **13 mm** wrench / Use a belt tension gauge and adjust to **70–75 lbs (white zone)**"* |
| Tracking wrench | f63-2016/2019 p62 l.1358 **10 mm** Allen, left side only, **3 to 5 kph**; f60-2016 p68 l.1353 / f60-2020 p63 **6 mm** Allen wrench **(97)**, left side bolt, **3 mph**. **f63-2023 and f63-2026 have no tracking section at all.** |

**Inside one manual** (beyond Part 1)

- **f63-2016 / f63-2019 — the 6-pin pin table numbers two rows "Pin 5"** (p47, l.840-845): `Pin 1 GND` / `Pin 2 TXD` / `Pin 3 RXT` / `Pin 4 VCC` / `Pin 5 SW` / **`Pin 5 N/A`**. The drawing beneath is labelled `1, 2, 3, 4, 5, 6`. Reproduced verbatim rather than renumbered.
- **f63-2016 / f63-2019 — the printed page numbers go backwards.** In the E3 test section the footers run 47, 49, then **59**, then 50, 51, 52; the "page 59" footer sits on a page physically between 49 and 50. Later, §8.9 CALIBRATION and MAINTENANCE MENU are footed **54**, after §8.8 Circuit diagram was footed 57-58. **Card locators quote the printed page number, so a reader following them will hit this.**
- **f63-2023 — the Run Mode table puts the Display key description in the Fan key row** (p10, l.210-219): the `Fan key` row carries the whole *"select the profile of SPEED or INCLINE by pressing DISPLAY key"* paragraph, and a separate `Display key` row follows with a one-line description. **The fan key has no description of its own.**
- **f63-2026 — the motor has three wires and no ground, but a ground wire is reconnected.** p12 l.150: *"**Brushless** motor with variable speed range 0-90 or (0-180) volt … Requires three wires connection: red, black and white"*, assigned red→U, black→V, white→W, and **unlike every other manual it names no grounding wire**. p58 l.822: *"**Reconnect ground wire** and motor wires (W/U/V)"*.

**Against committed cards** (beyond Part 1): the shared drive belt tension card carries no number
while every manual gives *"Use **14mm open end wrench** to adjust belt tension using tension
measuring device. Adjust to **white LBS area between 70-75LBS**."* (f63-2016 p72).

**Absences that are the answer**

- **`f63-2023` and `f63-2026` have no general maintenance content at all** — no tread belt and deck section, no belt tension adjustment, no belt tracking, no lubrication, no folding or transport, **though both troubleshooting matrices point at them** (*"See treadmill belt adjustment"*, *"See treadmill belt lubrication"*). No cleaning, tension, tracking, lubrication or folding cards were written for those two models. The four older manuals' figures conflict with each other, **so copying any of them across would be wrong.**
- **No parts numbers anywhere in this batch.** The only numbered items are the F63 2026 outline list and the F60 tracking wrench, referred to as "(97)".
- **Bluetooth, USB and NFC hardware is shown but never explained.** f63-2016/2019 show a `BULETOOTH` block on the Treadmill Configuration diagram with no text; f60-2020 shows `USB (Only Charge)` and `BLUETOOTH`; f63-2026 shows a `USB TYPE C` socket, a `Connection with NFC GEM4` socket and an `NFC reader` label. **None of the six manuals says what any of these do, how to pair, or how to update firmware.** No pairing or firmware cards were written.
- **Two f60-2016 display board sockets are labels only** (p25): a `2 pins MP3 Power Socket` and a `Write Program Socket`, mentioned nowhere else. Not carded.
- **The f63-2016/2019 amplifier board** (§6.3, p27) is a heading and an image; the only surviving detail is a display-board callout, *"Connection with 4-pin of the amplifier wire"*. Not carded.

---

## G8 — F65 2016/2019, F80 2016/2019 (269 cards)

`f65-2016` 74 (565816, ST155), `f65-2019` 73 (565818, ST158-YT044), `f80-2016` 69 (580816, ST525),
`f80-2019` 53 (580818, ST528-YT033). **The f80-2019 count is 20 lower because its troubleshooting
matrix is images** — see Part 5.

**Between manuals** (beyond Part 1)

| Fact | Values |
|---|---|
| Drive motor and incline motor descriptions | f80-2016 l.188-197: *"variable speed on **0-180 volt** DC motor. (**0-90** volts DC motor on 120Vac electronic power system)"* and *"This is a **230 volt AC motor**. (**115** volts AC motor on 120Vac…) Have **four wires**, red, black, white and green."* f65-2016 l.169-178, f65-2019, f80-2019 l.142-150: *"DC motor with variable speed range **0-90 or (0-180)** volt"* and *"This is a **110 or 230 volt** AC motor. All of **five wire connection**…"* — **four wires vs five, and the primary/secondary voltage stated the opposite way round** |
| Driver board LED table | f65-2016 l.503-516 / f65-2019 l.497-510: **two rows** — POWER and Limit current, **no current figure**, *"Check the supply voltage is 110VAC or 230VAC."* f80-2016 l.438-461: **five rows** — POWER / LIMIT / UP / DOWN / SPEED, with *"When current of motor exceed **18A**, the LCD will turn on. ( on **220Vac** electronic power system)"* and *"exceed **28A** … (on **120Vac** electronic system)"*, POWER row *"Check the supply voltage is 220Vac. (on 120Vac … need 110Vac)"*. **f80-2019 §6.7 exists but contains no text at all.** The 18A / 28A thresholds exist in exactly one of the four manuals |
| Drive belt loosening | f65-2016 l.1517 / f65-2019 l.1542: *"use **14mm open end** wrench to loosen **1 belt tension screw**"*. f80-2016 l.1282 / f80-2019 l.1140: *"use **14mm T-shaped socket** wrench to loosen **a side tension screw as well as a rear drive belt tension screw**"*. Final figure identical in all four: *"Adjust to white LBS area between **70-75LBS**"* |
| "Treadmill stops or shuts off by itself" | f65-2016 l.1168-1171 / f65-2019 l.1191-1194: **four** causes including *"3 Treadmill controller **fuse** is broken. → 3. Replace with new fuse"*. f80-2016 l.956-961: **three** causes, **no fuse row**, and adds *"3. **Belt / deck lubrication**."* |
| Lubrication section | f65-2016 l.1362-1378 / f65-2019 l.1385-1401: the **full** procedure plus the four-step lube-message reset. f80-2016 l.1147-1148 / f80-2019 l.1003-1004: the section **ends** at *"reach between the belt and deck to verify there is lubrication present, every other month."* — **no numbered application steps and no reset steps.** The "every 90 hours" interval is identical in all four |
| CE note wording | f65-2016 l.57-60: *"**ST155** treadmill is with a **CE/GS** version … 110AC for normal version versus 230VAC for **CEGS** version"*. f80-2016 l.61-64: *"**ST525** treadmill is with a **CE** version … versus 230VAC for **CE** version"*. **Absent from both 2019 manuals.** |

**Sections present in some manuals and absent in others**

| Content | f65-2016 | f65-2019 | f80-2016 | f80-2019 |
|---|---|---|---|---|
| CE / CEGS special note | yes (l.57-60) | no | yes (l.61-64) | no |
| Console-to-driver pin names | Pin 1-5 (l.834-838) | Pin 1-6 (l.828-833) | image only | image only |
| Driver board socket labels JK50/60/80/90 | yes (l.455-472) | yes (l.449-466) | image only | image only |
| Transport wheels paragraph | yes (l.1267-1270) | yes (l.1290-1293) | no | no |
| Program list (6 + USER1/2 + THR) | yes (l.326-327) | yes (l.321-322) | **no** | yes (l.292-293) |
| Metric speed presets 3,6,9,12,15,18,20 | no | no | no | yes (l.285, 311) |
| Troubleshooting matrix 8.10 text | yes | yes | yes | **image only** |

The `Pin 6 = N/A` row exists **only** in f65-2019 (l.833).

**Inside one manual** (beyond Part 1)

- **f65-2016 explains E3 as E2.** Under the heading *"Error Message：E3 / INCLINE ERR"* (l.923), the explanation at l.939-940 reads: *"If there is no VR value change to the CPU, the incline is not operating, and then appear **E2** appears on the display."* Every heading, definition and troubleshooting row around it says E3, and f65-2019 l.946 prints *"**E3** appears on the display"* in the same sentence.
- **f80-2016 merges two different switches into one matrix row** (l.988-999): the condition cell reads *"**FAST/SLOW** button of SPEED ADJUSTMENT SWITCH can't be used."* and *"**UP/DOWN** button of INCLINE ADJUSTMENT SWITCH can't be used."*, but **every reason names only "SPEED CABLE", "SPEED ADJUSTMENT SWITCH" and "SPEED ADJUSTMENT SWITCH/W/CABLE"**. The incline-buttons card says so rather than substituting the word "incline".
- **f65-2016 page numbering jumps mid-section**: §8.3's Test Procedure page is footed **59** (l.922) while the pages before and after are 47, 49, 50, 51, 52. Same in f65-2019 (l.919). **f80-2019 page footers repeat**: RUN MODE ends on a page footed **20** (l.328) after pages already footed 31-37, then continues 21, 22, 23.
- **f80-2019 E3 driver-board cell is overprinted** (l.646-649): *"Driver board | 3. 3. Replace / Replace the wires / the driver and test again. / board."* — two table cells collided. Read as "Replace the driver board", matching the other three manuals.
- **The E1 troubleshooting form's header row is printed twice** in all four manuals and the cells interleave with the "E1 message / The motor cannot move" spanning cell (f65-2016 l.739-773). Rebuilt as a three-column table; the duplicated header was dropped.

**Against committed cards** (beyond Part 1): `sole-safety-key-not-detected` covers the symptom but
carries `code: safety-key` and never mentions E0; the four new `e0-safety-key-error` cards supply
the code, the **+12V safety-switch-loop** explanation, and **the engineering-mode DISPLAY MODE
setting that decides whether the console shows E0 or goes dark when the key is pulled**
(f65-2016 l.664-667). **No existing card holds that setting.**

**Content in the manuals that no card covers**

- **Display board wire-connection labels differ between the years.** f65-2016 l.386-419 has *"Connection with **2-pin of AMP Line**"*; f65-2019 l.381-415 instead has *"Connection the **USB** wire"* and *"Connection the **Bluetooth speaker** wire"*. **This looks like a real console hardware change**, but the source is a scatter of photo callouts with no wiring table, so no card asserts a USB port.
- **"BULETOOTH" in the configuration block diagram**: f65-2016 l.374, f65-2019 l.369, f80-2019 l.340 and l.344 (printed twice). **f80-2016 does not contain the string at all** — grep-verified for both spellings. The display board photo reinforces it (f65-2016 l.391 and f65-2019 l.389 both label a "Bluetooth Module"; f65-2019 l.391 adds a "Bluetooth speaker wire"). That would mean Bluetooth on the F65 pair and the F80 2019 but not the F80 2016. **A misspelled diagram label with no supporting text, so no card claims it.**
- **§6.8 driver board component list** (f65-2016 l.522-556): Bridge, IGBT, X capacitor (Safety CAP.), Varistor, Filter capacitor, FUSE, TRANSFORMER, RELAY, INCLINE RELAY, Main IC, INCLINE VR, MAIN CONTROL, SPEED SENSOR. Folded into `specs/driver-board-connectors` **for the F65 pair only** — the F80 manuals' 6.8 is an image.
- **The word "cycle" in READY mode** (*"the message window will show program profile name and cycle"*, all four) is **never defined anywhere in the manuals**. Quoted, not explained.

**Merge candidates identical across all four**: the E0-E7 table (byte-identical, f65-2016 l.610-617,
f80-2019 l.470-477) · drive belt **70-75 LBS** with a **14 mm open end wrench** · *"Incline Range
must be adjusted to **225mm** minimum prior to installation"* (f65-2016 l.1461-1462, f80-2019 l.1239)
· incline motor wiring **Red to UP, White to COM, Black to DOWN** · the engineering mode menu (Key
Test / Display Test / Functions I-V / Security / Exit, **30 minutes** inactivity, **5 minutes**
pause, **Start+Enter for 3 seconds** to unlock) · the calibration procedure — **identical in three
of four; f80-2016 alone names the keys "START and FAST (Speed ▲)" and the unit selector "UP/DOWN
(▲/▼)"** · belt tracking 10 mm / left side only / 3-5 kph / 1/4 turn · GFCI and **Grainger 1D237 /
www.squared.com QO120HM** · chest belt **CR2032**, **3 feet**, **8 second** timeout · belt and deck
cleaning (monthly wipe, monthly vacuum, yearly hood removal, **water only**) · speed sensor gap
**"less than 3 mm"**, located *"on the left side of the frame, right next to the front roller
pulley"*.

**G8 §6.3: nothing else was dropped.** No numbered procedure, error definition, matrix row, spec
value or safety instruction in any of the four manuals is missing from the cards, except the
image-only material and the items above.

---

## G9 — F65/F80/F85/F89 2023 (268 cards)

`f65-2023` (565822, ST168), `f80-2023` (580822), `f85-2023` (585822, ST278-YT071),
`f89-2023` (589853, ST378-YT078). *"`diff` between the F85 and F89 text files is 12 hunks, of which
only five are substantive"* — cover, console size, GRADE row, calibration metric max, special note
code.

**Between manuals** (beyond Part 1)

| Fact | Values |
|---|---|
| Incline motor zeroing | F65 §9.9 p44 l.935 *"To adjust spare Incline motor to lower (**225mm**)"*; F80 §9.9 p61 l.1118 *"(**195mm**)"*; F85 l.1138 and F89 l.1139 *"(**225mm**)"*; **rear** incline motor F85 §9.10 p64 l.1162 and F89 l.1163 *"(**205mm**)"* |
| Incline motor refit tooling | F65 §9.9 l.940 *"Install Incline motor back with **M8 L-Allen wrench and 14mm open-end wrench**"*; F80 l.1124, F85 l.1144, F89 l.1145 *"**14mm open-end wrench**"* only |
| Safety key fault | F65 p20 l.365 *"**E0** Safety keys dose not insert the safety module. Or safety module is broken."* F80/F85/F89 l.463-464 *"**PLEASE REPLACE THE SAFETY KEY** \| The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed."* — **E0 exists only in the F65 manual** |
| Incline quick keys, and whether the machine declines | F65 l.192 and F80 l.187 *"7preset buttons for rapid incline: **1，3，5，7，9，12，15**"*; F85 l.198 and F89 l.199 *"**-4/-2/2/4/6/9/12**"* |
| Console hardware | F65 l.99 *"Contains keys、 **LCD Display**、Speaker、Fan、. Hand Pulse Grip、Safety key, etc."*; F80 l.95 `TFT 10.1” TFT TOUCH PANNEL`; F85 l.106 `TFT 15.6”`; F89 l.106 `TFT 21.5”` — **the only hardware fact that separates the three touchscreen manuals** |
| CE special note | F65 p3 l.58-62 *"Special Note on **ST168 CEGS** version"*, *"the power input is **110AC** for normal version"*; F85 p4 l.65-69 *"Special Note on **ST278 CE** version"*, *"**110VAC** for normal version"*; F89 p4 l.65-69 *"**ST378 CE**"*. **`sole-tm-f80-2023-service-manual` has no such note at all** — whether the F80 has no CE variant or the note was left out, the manual does not say. **No `f80-2023-ce-version` card was written.** |

**Inside one manual** (beyond Part 1)

- **F65 names the safety key fault two ways.** §3 p6 l.87-88: *"Safety Key … The display will show **"Please Replace the Safety Key"**."* §8 error list p20 l.365: *"**E0** Safety keys dose not insert the safety module."* §8.1's own note l.413 confirms the code: *"…which is display on and appear **E0** after removed safety key."* **§3 in the F65 is boilerplate copied from the touchscreen manuals.**
- **F65 has two different ways into ENGINEERING MODE.** §8.1 note p21 l.410-411: *"**Remove safety key**, press STOP & START & ENTER keys, and **at the same time insert the safety key**."* §8.11 p35 l.693-694: *"Press and hold the Start, Stop and Enter key at the same time, until the display shows "ENGINEERING MODE MENU PRESS ENTER" (it may say maintenance menu, depending on version)."* — **no safety key step.**
- **F85/F89's §8.1 note describes a console this machine does not have.** F85 p34 l.528-533 / F89 l.529-534 print the F65's *"Remove safety key, press STOP & START & **ENTER** keys … Press **FAST/SLOW or UP/DOWN** keys, to find "functions""*, while §4.4 (F85 l.192-196) replaces the Enter Key row with a **"Touch panel"** row — **this console has no ENTER key** — and §8.10 p49 l.823 gives the real route, *"Press 10 times on "Settings" letter to enter engineering mode."* **The F80 manual does not carry this note at all.**
- **"DISPLAY range is 0."** — not a range — in both F80 and F85 §4.2.

**Against committed cards** (beyond Part 1): `cards/f85-2023/specs/wiring.md` (`f85-2023-wiring`,
authority 2) names item 41 *"Rear incline controller **D020621-02**"*; the manual's §9.10 p64
confirms a rear incline motor on its own control board. **The two agree**, and the manual adds the
205 mm zeroing length and the removal steps the wiring card lacks.

**Extraction damage specific to this group**

- **Touch panel glyphs are blank runs.** F80 l.182, F85 l.193, F89 l.194: *`Press “                 ” button to change each function.`* Same for the gear icon (F80 l.210 *"Press the gear icon    above the screen"*), the unit toggle (l.220), the WIFI connected/disconnected icons (l.276) and the media apps update button (l.320-321). **The cards say "the touch panel" rather than naming a button.**
- **Page breaks inside table rows.** In F85/F89 the `-8-` footer lands between *"COUNT DOWN setup range is 10:00 to 99:00."* and *"When TIME is set, the count will go to zero."* (F85 l.157-159). Rebuilt by reading across the break; **values unchanged**.
- **`sole-tm-f80-2023-service-manual` page 20 is nothing but its footer** — l.328 is `- 20 -` alone between the Media Apps text and the Passcode heading. A full page of screenshots produced no text. F85 l.339 and F89 l.340 are the same.

**Content in the manuals that no card covers**: the F65's *"Special Note on ST168 CEGS version"*
mentions *"an additional **Filter Choke** circuit … as shown in the circuit diagram on next page"* —
the diagram is an image, so the card can only say the circuit exists. The F65's §4 Program Key
prints **"TH60 PCT"** (l.203) where "THR60 PCT" is obviously meant; **the typo was kept and flagged,
not silently corrected**. **Screen Brightness** (F80 l.257) is one sentence, folded into
`<model>-settings-menu`.

**Deliberate overlap with shared cards.** `<model>-wifi-setup`, `<model>-software-update` and
`<model>-media-apps-update` duplicate `sole-connect-wifi-touchscreen`,
`sole-update-software-touchscreen` and `sole-update-media-apps-touchscreen` (all `applies_to: ['*']`,
authority 2), **because the manuals add three facts the shared cards do not have**: the Wi-Fi failure
state is the word **"Saved"** with no connection (F80 l.272-273), and both update flows carry an
explicit warning that **interrupting the power supply may damage the system permanently** (F80
l.297-298 and l.321-322). *"If a reviewer disagrees, these three per model are the first six to
drop."*

---

## G10 — F85 2016, F85 2019, F85 ENT 2021 (171 cards)

`f85-2016` 54 (585816, **ST535**), `f85-2019` 59 (585818, **ST538-YT034**), `f85-2021` 58
(UNRESOLVED, **ST538-YT056**). **`ST538` is not a model year** — the Dyaco platform code covers at
least two model years and the suffix after the dash identifies the build.

**Between manuals** (beyond Part 1) — every row is the same field with a different value

| Field | f85-2016 | f85-2019 | f85-2021 |
|---|---|---|---|
| Metric speed quick keys | none printed (§4 p19) | *"( For metric is **3，6，9，12，15，18，20**)"* (p36) | *"(**3/6/9/12/15/18/22**KM)"* (p20) |
| Incline motor voltage | *"**230 volt** AC motor. (**115 volts** AC motor on 120Vac…)"* (§3 p13) | *"This is a **110 or 230 volt** AC motor."* (§3 p30) | same as 2016 (§3 p14) |
| Drive motor voltage | *"To control the **0 – 180 DC volts**（To control **0-90** DC voltages on 120Vac…）"* (§3 p12) | *"Control the **0 –90 (or 0-180)** voltages from the main controller"* (§3 p29) | *"variable speed on **0-180 volt** DC motor on 230V. (**0-90** volts DC motor on 120Vac…)"* (§3 p14) |
| POWER LED supply check | *"Check the supply voltage is **220Vac**. (on 120Vac … need **110Vac**)"* (§6.7 p31) | *"Check the supply voltage is **110VAC or 230VAC**"* (§6.7 p48) | same as 2016 (§6.7 p34) |
| E3 incline cable troubleshooting | two steps only (§8.3 p47) | adds *"**3. Replace the wires and test again.**"* (§8.3 p64) | adds the same step (§8.4 p54) |
| "Treadmill stops by itself", 3rd cause | *"3 Treadmill controller shut down and LED would be ON."* → *"3. **Belt / deck lubrication**."* (§8.10 p61) | *"3 Treadmill controller **fuse** is broken."* → *"3. Replace with new fuse"* (§8.10 p78) | same as 2016 (§8.11 p75) |
| "After removing safety key, treadmill can't stop" | **three** solutions: safety key device, controller, console (§8.10 p62) | **one**: *"1. Replace with new safety key device."* (§8.10 p78) | three, same as 2016 (§8.11 p76) |
| Speed / incline switch failure | **one merged row**, causes all about the SPEED CABLE connectors (§8.10 p62) | **two separate rows** — speed = *"Maybe keys stuck / upper control / lower control"*; incline = *"The incline VR or incline power wires not connected properly"* (§8.10 p79) | one merged row, same as 2016 |
| "LCD not bright" first cause | *"1. Connector fall off. → 1. Check connector again."* (§8.10 p61) | **that cause is absent**; instead adds *"2. Check AC power is **110V or 230V**."* (§8.10 p78) | same as 2016 |
| Incline motor refit wiring list | printed: *"Red wire Connect to "UP" / White wire Connect to "COM" / Black wire Connect to "DOWN""* (§12-9 step 4 p86) | printed, identical (§12-9 step 4 p104) | **step 4 prints no wiring list at all** (§12-9 step 4 p102) |
| LAPS window | present, *"DISPLAY range is 0 to 99. WORK range is 0 to 99."* (§4 p17) | present, identical (§4 p33) | **absent**; the function list runs SPEED, Incline, TIME, DISTANCE, CALORIES, PULSE |
| DISPLAY key readouts in RUN mode | *"LAP XXX / VERTICAL XXXX M / SEGMENT TIME X：XX / MAX SPEED XX.X"* (§4 p20) | *"PROGRAM NAME LAPS XX / VERT XXX **FT** / SEG TIME XX：XX / MAX SPEED XX：XX"*, plus *"the system will scan and display automatically **every four seconds**"* (§4 p37) | no text readouts; *"It can change the **three training diagrammatic**"*, and in READY mode *"DISPLAY KEY: **Non-function**."* |
| Engineering / maintenance menu | flat **A KEY TEST, B DISPLAY MODE, C PAUSE MODE, D LUBE MESSAGE RESET, E KEY TONE, F CHILD LOCK** (§8.9 p60) | **A KEY TEST, B DISPLAY MODE, C Functions {Display Mode, Pause Mode, Maintenance, Units, Key Tone}, D Security, E Exit** (§8.9 p77) | touchscreen: *"Press 10 times on "Settings" letter"*, six functions — **Engineering Mode, Diagnostics, Machine Information, Maintenance, Lube Setup, Key Test** (§8.10 p70) |
| Calibration entry | *"Press and hold down the **START and FAST (Speed ▲)** buttons and replace the Safety Key"* (§8.9 p60) | same, plus *"(The maximum speed value is displayed in the speed window, and the maximum elevation value is displayed in the incline window.)"* (§8.9 p77) | *"Press 10 times on "Settings" letter"*, then *"Press Engineering Mode to enter Calibration"* (§8.10 pp70-71) |
| Grade return | calibration step 4, with *"**For sale in Europe, EU standards require this to be off**"* (§8.9 p60) | identical note (§8.9 p77) | a Machine Information setting, *"**GR Mode: Grade Return，Default: ON**"*, nine behaviours listed, **no EU note** (§8.10 pp72-73) |
| Lube interval | *"every **90 hours** of use"*, fixed (§10.1 p69) | fixed (§10.1 p86) | *"default time is **90 hours** … Setting range: **90~200 hours**"*, adjustable (§8.10 Lube Setup p74) |
| Console panel type | `10.1” TFT PANNEL` (§4 p15) | `10.1” TFT PANNEL` (§4 p32) | `10.1” TFT **TOUCH** PANNEL` (§4 p16) |
| CE version note | present, *"Special Note on **ST535** CE version"* (p3) | **absent**; instead *"The 220V (or CEGS) of Lower Controller Area has **Filter and Chock**."* (§3 p30) | present but **mislabelled** — heading "Special Note on **ST538** CE version", body "Besides normal version, **ST535** treadmill is with a CE version" (p4) |
| Workout program list | not enumerated | *"**6 programs** (Manual, Hill, fat burn, Cardio, Strength and Interval), and also has USER1, USER2, **TH60 PCT**, and **THR80 PCT**"* (§4 p36) | not enumerated; adds a **"Fitness tests"** category **with no tests named** (§4 p20) |
| "ON/OFF switch not lit" matrix row | absent | present, **nine causes** (§8.10 first row, p78) | absent |

**Inside one manual** (beyond Part 1)

- **f85-2016 §6.7 p31 calls an LED an LCD**: *"When current of motor exceed **18A**, the **LCD** will turn on."* — in a table headed "Indicator LED", for the LIMIT indicator on the driver board. **Same wording in f85-2021 §6.7 p34** and in `sole-tm-s77-2016` p31, where the same row then says *"the LIMIT **LED** will turn on"*.
- **f85-2016 has two paths to DISPLAY MODE**: §8.9 p60 lists *"B. DISPLAY MODE"* as a top-level item; §8.1 Note p38 reaches it via *"Press FAST/SLOW or UP/DOWN keys, to find "functions", and press Enter key into "DISPLAY MODE""*.
- **f85-2016 §4 p16 speed conversion does not hold**: *"WORK range is **1.0~18.0 kmph (0.5 ~ 12.0 mph)**"* — 18.0 kmph is 11.2 mph and 1.0 kmph is 0.62 mph.
- **f85-2019 has two menu items called Display Mode** (§8.9 p77): *"**B. DISPLAY MODE** - Tests all the display functions."* and *"C. Functions … **I. Display Mode** - Turn off to have the console power down automatically after 30 minutes of inactivity"*.
- **f85-2019 metric quick key top speed is below the console's own limit**: §4 p33 *"WORK range is 1.0~**22.0**KM"* vs §4 p36 metric quick keys ending at **20**.
- **f85-2021's E0 section is titled by a message and bodied by a code**: ToC p1 lists *"8.1 Error Message: **E0**"*; the body heading p40 is *"8.1 Error Message：Display appears「**PLEASE REPLACE THE SAFETY KEY**」on the Message Window"*, and the text under it says *"Cause of **E0** … So display will be appeared E0."*
- **f85-2021 numbering inside §8.10 restarts and collides** (pp70-75): *"1. Engineering Mode"* then *"1. Press 10 times on "Settings""*, then *"2. Press Engineering Mode to enter Calibration"*, then *"2. Machine Information"*, *"3. Lube Setup"*, *"4. Key Test"* — **two different things numbered 1 and two numbered 2**.
- **f85-2021 typo**: §4 p17 *"Press START button or **TOPCH PANNEL** "START WORKOUT""*.

**Extraction damage specific to this group**

- **f85-2021 §4 p17: *"Incline … DISPLAY range is 0."*** — the upper figure is absent. **Written as printed and flagged rather than guessing 99.**
- **f85-2021 §4 p17: *"DISPLAY range is 1.0 to 22.0 km MAX or for MILE is "0.5 to12.0 MAX"*** — unbalanced quote, "to12.0" unspaced.
- **f85-2021 §4 p20: *"Touch panel button: Press "       " button to change each function"*** — the glyph was an image.
- **f85-2021 §4 p21: *"DISPLAY KEY：It can change the three training diagrammatic, from [image] to [image] then to this [image]."*** — the card can say there are three and cannot say what they are.
- **f85-2016 §8.3 p53: one troubleshooting cell is garbled to `t lb d`** where the 2019 and 2021 manuals read *"replace upper control board"*. The readable wording was used and said so on the card.
- **f85-2016 §8.3 p48 and f85-2021 §8.4 p55: the console-to-driver pinout survives only as `1, 2, 3, 4, 5, 6,`.** **The 2019 pin names were not copied across**; the 2016 and 2021 cards say the page is unlabelled and point at the 2019 card.

**No table was abandoned.** The error code tables, LED debugging tables, E0-E7 troubleshooting
tables, §8.10/8.11 matrices, §10.2 diagnosis guides and console function ranges were all recoverable.

**Content no card covers**: **no parts list, exploded view or part number appears in any of the
three manuals** — absence is the answer to "what is the part number for X" on these machines from
these sources. Nothing in the three covers Bluetooth pairing, Wi-Fi, apps, Garmin, Sole+, software
updates or the touchscreen UI beyond the engineering menu; those already have shared cards.

**Merge candidates word-for-word identical in all three**: §7.1/7.2/7.3 in full (the **220 volt
10 amp** outlet, the **16 AWG** extension cord rule, the GFCI prohibition, the high-inrush breaker
with **Grainger part 1D237** and **www.squared.com part QO120HM**, and the whole grounding and
temporary adapter text) · §10.1 in full (belt and deck cleaning, the **10 mm** Allen wrench tracking
from the **left side only at 3 to 5 kph**, the **1/4 turn** tension procedure, lubrication and the
warranty warning) · §9 folding and unfolding · **70 to 75 LBS** drive belt tension with a **14 mm**
open end wrench, in three separate procedures each · the **3 mm** speed sensor gap and the **8
second** no-signal timeout · the nine-step incline motor and potentiometer bench test including the
**4.5 to 4.7 Vdc at lowest position** figure · the E0 to E7 code set · the **225 mm** minimum incline
range · the §10.2 diagnosis guide rows (black particles, thumping belt, noise at lowest incline,
static shutdown on a cold day, the **10 kph** low voltage symptom, the on-board **15 amp** breaker
friction symptom).

---

## G11 — S77 2016/2019, ST90 2021/2023 (286 cards)

`s77-2016` 62 (577816, ST725), `s77-2019` 49 (577818, ST728), `st90-2021` 92 (590820, YT061),
`st90-2023` 83 (590822, ST8910-YT067).

**The two ST90 manuals**

| Value | 2021 | 2023 |
|---|---|---|
| Engineering menu slot 5 | **`Belt Setup`**, default off, **100-1000 hrs**, message `CHECK BELT PRESS START/STOP TO RESET CHECK MESSAGE` (p51) | **`Lube Setup`**, default **90 hrs**, **90-200 hrs**, message `LUBE DECK PRESS STOP TO RESET LUBE MESSAGE` (p26) |
| Settings page | **11 entries** incl. Bluetooth, Wired network, Display mode (p36) | **9 entries** incl. Language, Sleep Mode (pp19-22) |
| Language | Engineering menu > Maintenance, **13 languages** (p50) | Settings page, **no list printed** (p22) |
| Sleep | **30 min** (p43) | **15 min** + retail demo after **3 min** (p22) |
| Date/time | Date and Time separate, AM/PM or 24h (p39) | `Date & Time`, **24h only** (p20) |
| Brightness | **11 levels, 0-10** (p43) | red slider bar (p21) |
| Max speed | range **12.0-13.0 MPH / 20.0-22.0 KPH** (p47) | English max **12.0**, metric max **20.0** (p24) |
| Bearing seat | full ruler alignment, **0.5 mm**, **3 bolts** (pp66-67) | **2 steps, no alignment** (p37) |
| Incline window on an incline fault | *"INCLINE window displays **"INCLINE ERR""*** (p33) | **"INCLINE ERR"** on p17, **"E3"** in §8.3 p29 |
| E-09H description | `Converter overheat` (p29) | `Converters overheat` (p15) |
| Popping sound check | *"Check the voltage of power is **120V**"* (p32) | **120V** on p17, **220V … (On 120Vac … need 110V)** in §8.3 p28 |
| Incline motor | *"This is a **110 volt** AC motor."* (p12) | *"This is a **110 voltage** AC motor. (**220 volts** AC motor on 230Vac electronic power system)"* (p6) |
| Console | *"CONSOLE Contains Key controls and **LCD Display**."* (p12) | *"key controls and **TFT TOUCH PANNEL** display."* (p6) |
| Quick start speed | **0.5 mph** (p15) | **0.5 mph(1.0KMPH)** (p7) |
| Pad holder screws | *"**5 screws (3.5*12mm)**"* (p55) | *"**3.5 x 16mm** umbrella head self-tapping screws"* (p31) |
| Belt/roller gap on refit | **`15~18mm`**, both sides equal (p64) | **not printed** |
| Bearing seat alignment | **50 cm ruler, 0.5 mm, 3 bolts**, *"if it not necessary don't do the replacement"* (pp66-67) | **not printed** |
| Resonant noise Q&A | **not present** | *"paste foam with **1~2 mm** thickness in the middle"* (p40) |

**Everything the 2023 manual dropped (belt alignment notes, bearing seat alignment, roller gap) is
still needed to service the machine.** The 2023 cards say so and point at the earlier manual's
figures.

**`sole-tm-st90-2023-service-manual` prints its troubleshooting matrix twice with different
content.** Copy 1 is unnumbered on pp17-18; copy 2 is §8.3 on pp28-30.

| Row | Copy 1 (pp17-18) | Copy 2 (§8.3) |
|---|---|---|
| Popping sound | *"Check the voltage of power is **120V**."* | *"Check the voltage of power is **220V** … (On 120Vac electronic power system need 110V)"* |
| No display with key | *"console connectors not plugged in properly"* / *"console cable is broken"* | *"**12 PIN** Computer connector"* / *"**12 PIN** computer cable"* |
| START does nothing | *"**Motor wire** isn't connected"* / *"**TFT** would be ON"* | *"**Motor M+ or M-** wire isn't connected"* / *"**LED** would be ON"* |
| Stops by itself | adds *"Treadmill controller **fuse** is broken"* / *"Replace with new fuse"* | adds *"**Belt / deck lubrication**"* |
| Can't stop after key removed | **one** remedy | **three** remedies (device, controller, console) |
| Screen dim | *"TFT light is broken"* / *"Check AC power is 120V"* | adds *"Connector fall off"*, **drops the 120V line** |
| INCLINE ERR | window shows **`INCLINE ERR`** | window shows **`E3`** |
| ON/OFF switch not lit | present, **9 causes** | **absent** |
| Belt speed vs display | **absent** | present, *"Controller is not calibrated"* |
| Incline switch row | own row, own causes | **folded into the speed row, speed causes only** |

**Copy 2 describes a DC treadmill, not this machine** — see 1.21. Both copies are on the affected
cards, with a statement of which one fits.

**Other ST90 internal contradictions**

- **Both ST90 manuals**, main controller (2021 p12, 2023 p6): *"…link the console to output appropriate voltages for **DC control Board** that controls the Treadmill functions."* **There is no DC control board on this machine.**
- **st90-2023 p25, GR Mode OFF**: *"-Press START to begin; the incline should be at **zero or at the current set level**."* Both answers for one case.
- **st90-2021 p12**: *"CONSOLE Contains Key controls and **LCD Display**"* against p15 *"**Touch-control screen** is installed for operating the treadmill"* and the p23 heading *"6-4 **TFT** CONSOLE CABLE FUNCTION"*.
- **st90-2021 p47 engineering mode table: the row name `Max. Incline` is used twice** — once for the incline percentage (*"The range is **10 to 15%**"*) and once for the incline AD value (*"The maximum of incline AD value"*).
- **st90-2021 ToC lists 8-2-1 to 8-2-7 with no Key Test entry**, while p45 says the engineering page has **6 sub-functions including `Key Test`**. **Key Test is never described.**

**Against committed cards** (beyond Part 1)

- **`sole-inverter-error-code-list` E-21H.** The manuals answer a flash-memory fault (`Abnormal PrEr Flash`) with *"**Please lubricate running belt or check for bad bearing**"*, **which is the line printed against E-0AH and E-0BH directly above it and is almost certainly a copy error in the manual.** The existing card's answer (follow inverter troubleshooting, replace inverter) is the sensible one. The manual's text was recorded faithfully on `st90-2021-e-21h-abnormal-prer-flash` and `st90-2023-e-21h-abnormal-prer-flash` with the mismatch flagged in the body.
- **`sole-lubricate-running-belt`**: the shared card says lubricate **every 3 months**; both S77 manuals §9.1 say **check every other month**. *"Not a hard contradiction, but the two numbers will read as one to a retriever."*
- **`sole-safety-key-not-detected` and `sole-no-display`** both carry an unscoped closing paragraph *"On a TT9 or ST90, …"* with `applies_to: ['*']`. Their ST90 advice (check the safety key wiring **including the 2-pin inverter wire**; replace console then inverter) **does not contradict** the manuals, but that branch is not year-scoped and now competes with 10 per-model cards.

**Two tables rebuilt with a caveat, one refused**

- **Rebuilt with a caveat**: st90-2021 §6-1 p20 — the inverter terminal block survived as a bare column of labels with no connecting lines, so it was written as a **terminal list, not a pin-by-pin map**, keeping the wire colours printed beside `AC IN` and `AC MOTOR` and **making no claim about physical position**.
- **Rebuilt with a caveat**: st90-2021 §6-2 and §6-3 pp21-22 — connector names and pin counts survived, positions did not; written as lists.
- **Refused**: s77-2016 p48 *"Test configuration. The console to driver board connector pin define function"* is followed only by `1,` `2,` `3,` `4,` `5,` `6,`. **No mapping was invented and no card was written.** The same page in the 2019 manual (p47) is equally empty.

**Content no card covers**: st90-2021 §1/§2 callouts are readable (Console, PAD holder, Cup holder,
Handle Button, Upright, Upright Cover, Front and back cover, Transportation Wheel, Foot Rail, Pedal,
Foot Pad, Console Support, Drink Bottle Holder, Bearing seat, Front roulette wheel, **2HP Inverter**,
Incline motor, Roller SET, Filter, Drive Motor) but **duplicate the existing `st90-parts-and-wiring`
card**, so no second parts list was written. **st90-2021 §8-1-8 "Wired Network" is one sentence** —
*"Set the wired network."* — carded anyway, because *"does my machine have an ethernet port"* is a
real question and the answer is yes. **Both ST90 manuals' §7-2 merges two symptoms into one row**
("Tread-belt does not stay centered / Treadmill belt hesitates when walked/run on") and refers to a
General Maintenance section neither manual contains; split into a tracking card and a hesitation
card, both saying the referenced section is absent and pointing at the 2021 manual's §10-6.

---

## G12 — TT8 2016 DC/AC, TT8 2019 DC/AC, TT8 2023 (296 cards)

`tt8-2016` 50 (ST925-YT021), `tt8-2016-ac` 68 (ST925A-YT030), `tt8-2019` 51 (ST928-YT035),
`tt8-2019-ac` 67 (ST928A-YT037), `tt8-2023` 60 (588822, ST738-YT066). **No AC card and DC card share
a file; every card names its drive type in the first body line; every AC/DC pair answering the same
question is linked both ways with `not_to_be_confused_with`.**

**AC vs DC of the same year — the main deliverable** (beyond Part 1)

### 2016: DC (ST925-YT021) vs AC (ST925A-YT030)

| Thing | DC manual | AC manual |
|---|---|---|
| Error code set | "Error code items" p37: `E0 … E7` | §8.1 pp36-38: `E-01H … E-53H` plus a bare `E3` |
| What **`E3`** means | p37: *"The console board is not detecting the VR voltage value, or the voltage value has exceeded the range."* | p38: *"**Machine (rear) incline motor error**"* |
| On-board breaker rating | §9.2 p69: *"Treadmill trips on board **15 amp** circuit"* | §10.2 p51: *"…on board **10 amp** circuit"* |
| Roller replacement socket | §11-6 step 3 p79: *"use **14mm** T-shaped socket wrench to loosen 4 screws"* | §12-6 step 3 p61: *"use **19mm** T-shaped socket wrench"* |
| Main controller | p12: *"…DC power supply for console、incline driver and **DC motor driver**…"* | p12: *"…and **AC motor driver**…"* |
| Incline motor on a 120 Vac system | p13: *"230 volt AC motor. **(115 volts AC motor on 120Vac electronic power system)**"* | p13: *"This is a 230 volt AC motor."* — **no 120 Vac figure at all** |
| Console display wording | p13: *"key controls and **LCD display**"* | p13: *"key controls and **TFT LCD display**"* |
| Driver board LED table | §6.7 p32: full table (POWER / LIMIT / UP / DOWN / SPEED) incl. **18A** / **28A** | **absent** — §6.6 is "Driver Board Component Locations", an image only |
| Speed sensor gap spec | §6.7 p32 and E1 form p45: *"To keep the gap-distance **less than 3 mm**."* | **not stated anywhere in the manual** |
| "No display when safety key inserted" | §8.10 p62: **8** causes incl. *"3 **12 PIN** Computer connector … 4 12 PIN computer cable is broken / 5 **Fuse** on controller is blown / 6 **Varistor** on controller is blown"* | §8.4 p41: **5** causes — *"3 Computer cable is broken. 4 Safety device is broken. (open) 5 Other components are faulty."* |
| "After removing safety key, treadmill can't stop" | p62: *"2. Replace **controller**."* | p41: *"2. Replace **controller or power board**."* |
| Popping sound at power on | p62: *"Check the voltage of power is 220V. Replace controller. **(on 120Vac electronic power system need 110V)**"* | p41: same **without** the 110 V note |
| "Motor is not responsive after pressing start" | §9.2 p68: *"If the **belt** moves, but stops after a short time and the display shows **"E1"**, run calibration"* | §10.2 p50: *"If the **incline** moves, but stops after a short time and the display shows **"E52H"**, check incline motor then calibration again."* |
| "Incline position doesn't match console" | p63: *"1 Calibrate the console."* | p42: *"1 Calibrate the console. **2 replace incline motor.**"* |
| Belt/deck lubrication section | **absent** — §9 covers cleaning, tension and tracking only | §10.1 p49: *"…**every 90 hours of use**"* |
| Folding / unfolding section | **absent** | §9 p45: *"TO FOLD THE TREADMILL — Make certain the treadmill is at minimum incline…"* |
| Rear incline motor replacement | **absent** — §11 ends at 11-9 | §12-10 p69: *"Rear incline motor be adjusted to **210 mm** minimum prior to installation."* |

### 2019: DC (ST928-YT035) vs AC (ST928A-YT037)

Rows 21-32 repeat the same pattern (error code set, E3 meaning, main controller, 120 Vac figure,
console wording, LED table + 3 mm gap absent from the AC manual, CE note absent from the DC manual)
and add:

| Thing | DC | AC |
|---|---|---|
| Speed work range | p14: *"0.5 ~ **12.0 mph** (1.0~**18.0** kmph) Note: Specific spec has **22.0kph** of maximum speed."* | p16: *"1.0~**22.0** kmph (0.5 ~ **13.0 mph**)"* |
| Speed quick keys | p17: *"2，3，4，5，7，9，12 (Note: On 22.0kph spec is **3, 6, 9, 12, 15, 18, 22**)"* | p19: *"**3，6，9，12，15，18，22**"* |
| Incline preset label | p14: *"**INCLINE** preset value is -6 to 15."* | p16: *"**GRADE** preset value is -6 to 15."* |
| Maintenance menu STOP key | p58: *"Use the STOP key to **return to previous menu selection**."* | p40: *"Use the STOP key to **exit to engineering mode**."* |

### The two AC manuals also differ from each other

| Thing | 2016 AC | 2019 AC |
|---|---|---|
| `E-08H` row | p36: *"GF grounding failure — 1.**更換變頻器** Replace the inverter"* (untranslated Chinese left in) | p36: *"GF grounding failure — 1. Replace the inverter"* |
| "Motor is not responsive after pressing start" | §10.2 p50: names **"E52H"** and the **incline** | §9.2 p48: names **"E1"** and the **belt** — but **this manual's code table has no E1 at all** |
| On-board breaker | p51: **10 amp** | p49: **15 amp** |
| Speed work range | p16: **1.0~18.0 kmph (0.5 ~ 12.0 mph)** | p16: **1.0~22.0 kmph (0.5 ~ 13.0 mph)** |
| Power board section heading | §6.5 p29: *"Power Driver Board Component Locations"* | §6.5 p29: *"Power Driver Board **(STANDBY BOARD)** Component Locations"* |
| Roller socket | §12-6 step 3 p61: **19mm** | §11-6 step 3 p59: **14mm** |
| Calibration entry word | §8.3 p40: *'until the window displays "**Factory settings**", then press the **ENTER** key'* | §8.3 p40: *'until the window displays "**CALIBRATION MODE**"'* |
| Folding section | §9 p45: present | **absent** |

### Cross-year within one drive type

| Thing | Values |
|---|---|
| Calibration entry word | 2016 DC §8.9 p61 and 2016 AC §8.3 p40: *"Factory settings", then press the ENTER key*. 2019 DC §8.10 p58 and 2019 AC §8.3 p40: *"CALIBRATION MODE"* with **no ENTER**. 2023 §8.10 p54: press **Settings** ten times, then Engineering Mode → Calibration |
| Safety key fault | 2016/2019 (all four): *"**E0** — Safety keys dose not insert the safety module."* 2023 p34: *"**PLEASE REPLACE THE SAFETY KEY**"*. **There is no E0 on the 2023.** |
| `E2` definition | 2016/2019 DC: *"When lower board detect over current … First, check whether smear **Silicone oil** or not."* 2023 §8.3 p41: a different, longer text about a dry or worn running belt raising friction, ending *"**replacing the controller should be the first option to consider**"* |
| Belt speed mismatch reason | 2016/2019: *"**Console** is not calibrated."* 2023 §8.11 p58: *"**Controller** is not calibrated, or the parameters of the controller are incorrect."* |
| Motor cover fasteners | 2016 DC/AC: *"the **2 Phillips Head Screw and 2 tapping screws** on motor cover"*. 2019 DC/AC: *"the **5 tapping screws**"*. 2023 §9.3: *"Loose **5 Motor cover front locking screws**"* |
| Console removal | 2016 DC/AC: *"L Allen wrench … **6 button head socket bolts** from the upright cover"* + 4 from the console support. 2019 DC/AC: *"**M5 L Allen Wrench** … **4 Sheet Metal Screw** … console mast cover"* + *"**M6 L Allen wrench** … 4 button head socket bolts"*. 2023 §9.2: *"**4 Phillips head screws**"* |
| Deck wax run-in step | 2016 DC §11-7 p83 and 2016 AC §12-7 p64: *"walk **S type for 1km and square type for 3km** around 10 minutes, so that the wax will evenly on the running deck."* 2019 DC/AC and 2023: **no such step** |
| Lube interval | 2016 AC / 2019 DC / 2019 AC: *"every **90 hours**"*. 2023 §8.10 p56: *"default time is **90 hours** … Setting range: **90~200 hours**"* — **and 2023 has no printed maintenance chapter to put it in** |
| BLE button | 2016 DC/AC: not present. 2019 DC p17 and 2019 AC p19: *"**BLE button**: When use the BLE wireless chest strap，in ready mode press one time and it will be turn on."* 2023: no BLE button, a touch panel instead |

**Inside one manual** (beyond Part 1)

- **tt8-2016-ac §12-3 p58, DC wording on an AC motor**: p13 describes an AC motor with *"three wires red, white and black for power"* and no polarity; step 2 reads *"Remove motor grounding wire (greenish yellow), **motor wire (+)and motor wire (-) black.red**"* (the colour words transposed by the conversion) and step 4 *"(**red M+, black M-**)"*. **The M+/M- pair does not exist on this machine's motor as described on p13.** Identical fault in tt8-2019-ac §11-3 pp56-57.
- **tt8-2016-ac ToC vs body headings**: ToC p2 *"6.5 **Power Board** Component Locations"* vs body p29 *"6.5 **Power Driver Board** Component Locations"*; ToC p3 *"12.7 Running Deck/ Belt & Cushion Replacement"* vs body p63 *"12-7 Running Deck/ Belt/ Cushion **and running deck wax** replacement"*.
- **Code punctuation**: the table prints **`E-53H`** and the matrix row prints **`GRADE window displays "E53H"`** — tt8-2016-ac p37-38 vs p42, tt8-2019-ac p38 vs p42.
- **tt8-2023 invalid clock values**, §4.2 p9: *"TIME … DISPLAY range is **0:00:00 to 9:99:99**. WORK range is 00:00 to **9:99:59**."*
- **tt8-2016 §8.3 E3 troubleshooting table, p54, last display-board cell is corrupt**: *"If no values, please check keys weather keys stuck or not, or replace upper"* / `    t lb d`. **tt8-2019 p52 prints the same cell intact** as *"… or replace upper control board."* That reading was used, and nothing the 2016 manual does not support was written.
- **Uncaptioned dimension `175`**: tt8-2016 p83 and tt8-2016-ac p64 both print a bare `175` beside a "deck wax" diagram, **with no unit and no sentence**. Not carded.
- **The `235`, `225`, `210` and `220` incline figures appear twice each** — once as an image callout and once in a sentence. **The sentences only were taken.**

**Against committed cards**: `cards/sole/console/start-button-grayed-2023.md` (`applies_to` includes
`tt8-2023`) blames a *"rear incline controller"*; `sole-tm-tt8-2023-service-manual` §9.10 p68
confirms a separate **"rear incline control board"** exists. **No contradiction — the two agree.**
**No existing card mentions `tt8-2016`, `tt8-2016-ac` or `tt8-2019-ac` at all**; those three ids had
zero cards before this batch.

**Scope warnings for the merge sweep**: a shared **E0-E7** card **must not reach `tt8-2016-ac` or
`tt8-2019-ac`**, which have no E0-E7 at all, and **must not reach `tt8-2023`**, which has no E0. The
AC inverter set `E-01H`-`E-53H` plus `E3` is shared with the TT9 and ST90; **if those card sets are
merged, the E3 front/rear disagreement has to be resolved first.**

---

# Part 4 — Data defects in the repository itself

Facts that are wrong in already-committed files, not in the manuals. Every line below was verified
against the working tree; nothing was edited.

## 4.1 `sources/spirit-models-sole-bikes/text.md` line 60 — the wrong value is what makes the rule look true

**Verified by the reader against the live database.** Line 60 reads:

```
| 595015 | SOLE E95 2015 |
```

The live database says **`595015 | SOLE E95 2016 | Elliptical`**, which is also what
`sources/spirit-models-sole-ellipticals/text.md` **line 62** says:

```
| 595015 | SOLE E95 2016 | Elliptical | Sole |
```

The row sits inside the table headed (line 51) *"The last two digits of the model number are the
model year. Confirmed against rows outside the bike range that carry the year in the name"*, so the
wrong value **is what makes that rule look true**. With the real value, `595015` and `595016` are
**both** named "SOLE E95 2016" and the rule breaks. Editing the file would break its manifest
sha256, so it has not been touched. G1 §1.2 and G3 §1.2 both found the two dumps disagreeing and
flagged it *"because another agent may lean on that table."*

**The same six-row table contains three further rows that break the rule it is printed to prove:**

| Line | Row | Digits imply | Name says |
|---|---|---|---|
| 56 | `\| 585812 \| SOLE F85 2013 \|` | 2012 | **2013** |
| 58 | `\| 585818 \| SOLE F85 2019 \|` | 2018 | **2019** |
| 61 | `\| 595018 \| SOLE E95 2019 \|` | 2018 | **2019** |

With line 60 corrected, only **two** of the six rows (`585816 → 2016`, `585820 → 2020`) actually
confirm the rule. See Part 2, decision 38.

## 4.2 `sources/manifest.yaml` line 589 — the F89 2023 manual carries the F85's SKU

```yaml
- id: sole-tm-f89-2023-service-manual
  title: Sole F89 2023 service manual (ST378-YT078-01)
  origin_uri: file://F89(2023)_585822_ST378-YT078-01_Service manual.pdf
```

**`585822` is the F85's SKU** — `sources/manifest.yaml` line 559 embeds the same number in the F85
manual's `origin_uri`, and `sources/spirit-models-sole-treadmills/text.md` line 79 gives
`| 585822 | SOLE F85 | Treadmill | Sole |`. The ST code in the F89 file name (`ST378-YT078-01`) is
the F89's own and matches its cover, so **only the six-digit number was copied from the F85**
(G9 §1.1). The F89 manual's own text prints no six-digit SKU anywhere.

## 4.3 `cards/sole/console/start-button-grayed-2023.md` line 36 — an F89 SKU that is not in the database

```
Applies to the 2023 F85 (585822), F89 (589822) and TT8 (588822).
```

**`dbo.Models` has no `589822` row.** `grep -rn "589822" sources/` finds it only inside
`sources/sole-tm-f85-f89-tt8-585822-589822-588822-start-button-grayed/` and the three manifest lines
naming that source. The database F89 row is `sources/spirit-models-sole-treadmills/text.md` line 93,
`| 589853 | SOLE F89 | Treadmill | Sole |`. Its neighbours do exist: `588822 = SOLE TT8 2023`
(line 88) and `585822 = SOLE F85` (line 79). **The knowledge base now carries two different F89 2023
SKUs, 589822 and 589853, and only 589853 is in the database** (G9 §1.3).

## 4.4 `cards/srvo/specs/overview.md` line 58 — two SKUs asserted as one product

```
The SRVO is sold under two SKUs: **578712** and **578722**.
```

`sources/spirit-models-sole-training/text.md` lines 19-20 give the two SKUs **two different
ModelNames**, not two SKUs for one product:

```
| 578712 | SOLE SRB101 | Training | Sole |
| 578722 | SOLE SR260 | Training | Sole |
```

`sole-srvo-service-manual`'s cover (line 1) reads ` SRVO SR260` — **SR260 only, which is 578722**.
The strings `SRB101` and `578712` appear **nowhere** in the 687-line manual, and every page of it is
the cable trainer (two servo motors, two reels modules, a rope hatch, a footboard). G6's unconfirmed
reading: `SRB101` looks like the **SRVO Multi-Angle Bench** part code, and the repository already
treats the bench as a separate product under the same model id
(`cards/srvo/specs/bench-overview.md`, `cards/srvo/warranty/bench-warranty.md`). **If that is right,
578712 is the bench and this manual covers none of it.** G6 wrote no bench card from it, because it
contains no bench content at all.

## 4.5 `kb.yaml` declares three sets of duplicate model ids

Verified at `kb.yaml` lines 81-83, 98-99 and 109-112:

```
81:    - f85-2020        98:    - sb1200        109:    - st90
82:    - f85-2021        99:    - sb1200-2023   110:    - st90-2020
83:    - f85-2023                               111:    - st90-2021
```

Each set is one machine by the evidence in 1.5 — SKUs 585820, 512322 and 590820 respectively. The
duplication silently splits retrieval: five committed cards name the bare `sb1200`, and
`st90-parts-and-wiring` (the only source of ST90 part numbers in the repo) is scoped to the bare
`st90` and does not reach `st90-2021` or `st90-2023` in a facet-filtered query.

## 4.6 `sources/manifest.yaml` titles carry a `-01` suffix the documents never print

- `title: Sole E25 2026 service manual (SE668SA-SE052-01)` — the manual prints `SE668SA-SE052`
  **three times and never `-01`** (cover line 4, circuit diagram sheet line 580, console line 586).
  The `-01` comes from the origin filename `E25(2026)_SE668SA-SE052-01 Service  Manual.pdf` (G4 §1.2).
- `sole-rower-sr500-2016-service-manual` — origin filename
  `SR500 2016 (CW800A-YR001-01_CW800A)  Service Manual.pdf`; the document prints `CW800A-YR001`
  (line 1 and every section heading) (G4 §1.3).
- `Sole F85 2023 service manual (ST278-YT071-01)` and `Sole F89 2023 service manual (ST378-YT078-01)`
  — **the covers print `ST278-YT071` and `ST378-YT078` with no `-01`** (G9 §1.6).

**And the manifest is inconsistent within one group**: `Sole F65 2023 service manual (565822)` and
`Sole F80 2023 service manual (580822)` name the **SKU**; the F85 and F89 titles name the **ST code**
instead (G9 §1.6).

## 4.7 `sources/spirit-models-sole-ellipticals/text.md` and `-climbers/text.md` duplicate the SC200 rows

Lines 23-24 of the ellipticals dump and lines 19-20 of the climbers dump carry **the same two rows**,
verbatim:

```
| 520516 | SOLE SC200 | Stepper    | Sole |
| 520517 | SC200      | Elliptical | Sole |
```

The climbers dump's own notes say *"The SC200 appears twice under two different `ModelType` values,
`Stepper` and `Elliptical`. Neither row carries a model year."* One machine is filed under two SKUs,
two ModelTypes and two product-line extracts, with no year on either row (G1 §1.4, G2 §1.1).

## 4.8 The assignment file for G6 states a card count that is wrong by a factor of two

`groups/G6.md` states *"Model id srvo already carries 74 cards."* The repository held **36** before
the run — `grep -rl "^  model: srvo" cards/` → 36 files, and `kb vocab`'s `card_ids` matching
`srvo-` → 36 ids. (Two further cards name `srvo` in `applies_to` only, giving 38 at the most generous
count.) After G6's 49 new cards, `find cards/srvo -name '*.md'` returns **85**, which is 36 + 49
exactly. The same file's `product_line` column says `rower`; the machine is a two-cable servo
strength trainer and all 36 pre-existing cards use `strength` (G6 §1.4, §3.6).

## 4.9 `cards/shared/errors/dc-controller-error-code-list.md` scopes itself to machines whose manuals contradict it

Line 35: *"Applies to the F63, F65, F80, F85, F89 and TT8, which use the DC digital controller."*
Its table runs E1 to E8. **No service manual for any of those six machines prints E8**, and every one
of them prints **E0**, which the table omits. Its companion
`cards/shared/errors/e8-controller-eeprom.md` carries `applies_to: ['*']`. The E8 card's own source
is `sole-tm-console-error-code-list`, **not a service manual** (G7 §3.1, G9 §3.2, G10 §3.6). See
Part 2, decisions 42-43.

## 4.10 Coverage gaps that `kb lint` structurally cannot see

`applies_to` is checked for **membership, not completeness**, so a shared card that omits a machine
lints clean. Three were found independently:

- **122 cards carry `model: '*'`.** Five of them list the **year-less** elliptical ids (`e35`, `e95`,
  `e95s`, `e98`) and none of the six 2019 ids or five 2023 ids: `sole-garmin-pair-non-touchscreen`,
  `sole-plus-strava-sync`, `sole-lwr-not-match`, `sole-heart-rate-monitor-other-brands`,
  `sole-garmin-supported-watches-broadcast` (G2 §3.3, G3 §6.2).
- **`sole-bike-service-manual-model-numbers`** is six rows short — see Part 2, decision 44 (G5 §3.10).
- **`sole-inverter-error-code-list`** (`applies_to: [st90, tt9]`) does not reach `st90-2021`,
  `st90-2023`, `tt8-2016-ac` or `tt8-2019-ac`, all of which use that inverter's code set
  (G11 §3.2, G12 §3.2).

## 4.11 Lint noise during the run was cross-agent, not damage

Every group reported transient `dangling-link` problems in other agents' in-flight directories —
`cards/st90-2021/`, `cards/st90-2023/`, `cards/s77-2016/`, `cards/s77-2019/` — `see_also` ids that did
not exist yet (for example `cards/s77-2016/errors/e4-motor-power-wire.md: [dangling-link] see_also
points at unknown id 's77-2016-motor-replacement'`). Counts climbed from 9 to 19 mid-run and
**cleared by the end: the final state is 0 problems in 3,268 cards**. Per rule 6 no agent touched
another agent's files.

---

# Part 5 — Re-OCR candidates

Every source with image-only sections, what was lost, and the agent's estimate of cards recoverable.
Only G11 gave a numeric estimate; the rest are marked "no estimate given" rather than invented.

## Priority 1 — content that exists and is completely absent from the KB

| Source | What is lost | Cards recoverable |
|---|---|---|
| `sole-tm-s77-2019-service-manual` | **§8.10 Troubleshooting procedure matrix, pages 60, 61 and 62 — three blank pages** carrying nothing but the running footer (text.md lines 900-906). The whole matrix is images. Everything the ST725 matrix covers is absent from this source: dead start with no code, popping sound at power-up, no display with the key in, treadmill running with no key, stops by itself, will not stop when the key is pulled, TFT dim or incomplete, speed or incline not matching the display, INCLINE ERR, stops immediately after start, erratic pulse, rapid keys dead, hand pulse dead, chest belt dead. **No cards were written from it.** | **~15 cards** (G11's estimate) |
| `sole-tm-f80-2019-service-manual` | **§8.10 Troubleshooting procedure matrix (lines 884-890)** — heading, then "61 Service Manual" and "62 Service Manual" and nothing else. **17 troubleshooting cards that exist for the other three G8 models could not be written for this one** — the reason `f80-2019` has 53 cards where `f65-2016` has 74. Also **§6.7 Controller Indicator LED debugging (lines 411-416)**, heading followed by a page footer, where the f80-2016 equivalent carries the **18A / 28A** thresholds. **No LED card was written for f80-2019.** | ~17 troubleshooting + 1 LED |
| `sole-tm-f63-2026-service-manual` | **14 pages produced no extractable text**: printed pages **7, 8, 9, 18, 19 and 38 to 46**. The footer sequence jumps 6→10, 17→20, 37→47. Pages 7-9 are the tail of §1.3 Lower Controller and Driver; pages 18-19 are Function Button Locations; **pages 38-46 are nine consecutive pages sitting inside §7 Treadmill Error Messages (p36) before §7.1 Error Message/Troubleshooting (p47)** — almost certainly error flow charts or diagnostic diagrams. The code table on pp47-48 did extract, so every code is held; **nine pages of whatever supports them are not.** | no estimate given |
| `sole-srvo-service-manual` | **§5 Circuit Diagrams (pp23-24)** and **§6 Block diagram (pp25-26)** — pure images, **zero extracted text**; two of the nine numbered sections of the manual, and exactly what a board-level technician wants. **§8-4 Wireless control module (p42)** — a heading with **no body text whatsoever**, the only mention of the wireless switch in the entire manual; the existing `srvo-pair-wireless-switch` and `srvo-wireless-switch-not-connecting` cards already note that the seminar's flashing-sequence chart is an unextractable image, and **p42 may be that chart's engineering counterpart.** | no estimate given |
| `sole-tm-st90-2023-service-manual` | **§1, §2.1-2.3, §5, §6.1-6.8 — headings only, no labels survived.** The 2021 manual's equivalents kept their labels, which is why `inverter-terminal-layout`, `console-rack-connectors`, `transfer-pcb-connectors`, `tft-console-cable` and `lower-controller-plugs` exist for `st90-2021` and **not for `st90-2023`**. The two share the §6.1 heading `(YT061)`, so the layouts may be the same — **but that was not assumed.** | 5 spec cards |

## Priority 2 — pinouts that were text in an earlier generation and are images now

| Source | What is lost | Consequence |
|---|---|---|
| All five 2023 ellipticals (`e25`, `e35`, `e95`, `e95s`, `e98`) | §6.1-6.6 in full (display board wire connections, PCB top and bottom, interface board, driver board wiring, driver board function, **gear motor connector definition**), §8.4 Circuit Diagram, both "Test configuration" pages, §8.5 Engineer Mode screenshots | **"The 2023 PDFs have no recoverable pinout at all"** — the 2019 pilot could write `e25-2019-console-to-driver-board-pinout` and `e25-2019-tension-motor-connector-pinout`. **No pinout card exists for any of the five 2023 machines.** |
| All six 2023 bikes (`b94`, `r92`, `lcb`, `lcr`, `sb1200`, `sb900`) | §1, §2.1, §2.2, §5, §6.1-6.6 including **§6.6 Brake Controller Functions** (lcb, lcr — heading only, no text at all) and **§6.5 Driver Board PCB Component Locations & function** (sb1200 — heading only); Test Configuration; Circuit Diagram; Function Button Locations; sb900's console layout and **§2.2 RPM Sensor / Transmitter** | **No console-to-driver-board pin-out card exists for any of the six**, although `b94-2019-console-to-driver-board-pinout`, `r92-2016-console-to-driver-board-pinout`, `lcb-2019-driver-board-cable` and `sole-bike-7-pin-console-cable-pinout` exist for the earlier bikes. **A 2023 bike technician has no pin-out in the knowledge base.** |
| `sole-elliptical-e25-2026-service-manual` | §1.1, §1.2, §2.1, §2.2, §4 drawing, §5, **§6.1-6.6 including 6.6 Gear Motor connector definition function**, §8.2/§8.3 Configuration drawings, both Action Flow Charts, §8.4 Circuit Diagram | **The E25 2026 gear motor connector pinout is unrecoverable**; the committed `cards/e25-2019/specs/tension-motor-connector-pinout.md` (5 pins: M+, M-, +5V, VR, GND) has **no 2026 counterpart and could be neither confirmed nor contradicted.** |
| `sole-rower-sr550-2023-service-manual` | §1 Outlines, §2.1 Console, §2.2 Controller and Driver parts, §5, **§6.1-6.4 including Gear Motor connector definition function**, §8.2 Circuit Diagram, all numbered figures | Same — **no SR550 gear motor pinout.** |
| `sole-tm-f80-2016` and `-f80-2019` | *"Test configuration. The console to driver board connector pin define function"* followed only by `6, 5, 4, 3, 2, 1` (f80-2016 l.706, f80-2019 l.660). Also §6.1-6.5 and §6.8 (display board wire connections, PCB component locations, amplifier board, driver board wiring and function) are photographs with **no recovered labels** | **No pinout card written for either F80**, and `specs/driver-board-connectors` exists **only for the F65 pair**, whose manuals label the same drawings (JK50 / JK60 / JK80 / JK90, Com/UP/DOWN, M+/M-). **The F65 pinout was not copied across.** |
| `sole-tm-f85-2016` and `-f85-ent-2021` | The console-to-driver pinout survives only as `1, 2, 3, 4, 5, 6,` (f85-2016 §8.3 p48; f85-2021 §8.4 p55). f85-2021 additionally loses **§6.1 both the Android 6 and Android 10 pages**, §6.2 both PCB pages, **§6.3 amplifier board**, §6.4, §6.5, §8.9 circuit diagram p69, and **every engineering mode, calibration, Machine Information, Lube Setup and Key Test screenshot (pp70-75)** | **The 2019 pin names were not copied across.** `f85-2019-display-board-connections` and `f85-2019-driver-board-sockets` exist **only** because that one manual's callout labels survived. |
| `sole-tm-s77-2016` p48 and `-s77-2019` p47 | The same page, followed only by `1,` `2,` `3,` `4,` `5,` `6,` | **No mapping invented, no card written.** |
| `sole-tm-f63-2023-service-manual` | **p26 console-to-driver pin table is an image** (heading `Test configuration:` / `The console to driver board connector pin define function.` then nothing) — the equivalent table is text in the 2016, 2019 and F60 manuals. **p14 §6.3 Patching Board Wire Connections** shows a `Console patching board` and a `Console outer cover patching board` **with no readable connector names** | **No console-to-controller pinout card for `f63-2023`** — only the 3-pin incline connector, which is text on p28. The two patching boards are recorded as existing, with their connections marked drawings-only. |

## Priority 3 — bulk loss, uniform across a group

| Group / sources | Sections lost |
|---|---|
| **G1** — seven 2016 ellipticals | Every wiring and PCB page in all seven (§6.1-6.7), §5 unit block diagrams and "Elliptical Configuration", the circuit diagram, the "Configuration:" image under each error section, every Action Flow Chart. The only surviving text is floating labels: POWER, INCLINE MOTOR UP, INCLINE MOTOR DOWN, RPM SENSOR, TENSION MOTOR, SYSTEM WIRE, AC POWER INPUT, TRANSFORMER AC POWER INPUT/OUTPUT. **Every parts drawing (§1 Outlines) is an image; only the callout labels survive, so there are no part numbers and no parts-list cards.** LCD Layout pages (E25 p15, E35 p17, E55 p15, SC200 p15) are images only — **no card can describe the screen layout.** Blank pages carrying only the footer: **E55 p47, E98 pp59 and 88.** Specific damage: **SC200 p31** — the tension motor connector plug is numbered **1 to 8 with no signal names**, and the speed sensor is drawn with two pins but labelled `2. GND / 3. SPEED` (the E95/E95S manuals print that plug as 1.GND, 2.SPEED); the fragment was reproduced in a fenced block and **no mapping was invented**. **E95S p85** §11-4 step 6 begins with an untranslated Chinese sentence, `用外六角板手 M5 將固定踏板滑軌…`, followed by the English; the English was used. |
| **G2** — six 2019 ellipticals | §1 (Outlines / plastic and steel parts), §2 (Electronic Parts, Upper Controllers, Lower Controller and Driver), §5 (Unit Block Diagrams), §6 (Display Board PCB Component Locations, PCB Top / Bottom, Amplifier Board Wire Connections, Driver Board Wire Connections, Driver Board LED Indicator Locations) and the circuit diagram pages survive as a heading, a page number and nothing else. **E98 lines 76-78 are literally three consecutive "N Service Manual" lines where pages 5, 6 and 7 used to be.** The E55 and E95s parts drawings **did** keep their part-name callouts (E55 l.75-144, E95s l.64-172); those names are in the two `model-overview` cards. **Rebuilding the exploded views and board layouts needs the PDFs, not the text dump.** |
| **G7** — six F60/F63 manuals | Every wiring diagram, PCB layout, block diagram and circuit diagram in all six is an image; the extracted text carries only floating callout labels, and often not their positions — **which is why the driver board and display board socket cards read as lists rather than diagrams.** The circuit diagrams (§8.8 / §8.9 / §7.2) yielded **nothing at all**. The `E1 solution follow chart`, `E1 solution follow chart – check RPM sensor device procedure` and the `Action Flow Chart` blocks under E3 / INCLINE ER are headings with no content; the prose test procedures beside them did extract. |
| **G8** — four F65/F80 manuals | §8.8 / §8.9 circuit diagram pages carry **no text at all** (f65-2016 l.1102-1108). All flow charts are images (f65-2016 l.706-717, l.809-813, l.941-945). §1, §2, §2.1, §2.2 and §5 yield only stray labels — "Speed Sensor", "Lower Controller Area", "Driving Motor", "BULETOOTH" — **not enough for a card.** |
| **G9** — four 2023 F65/F80/F85/F89 | §1 Outlines and §2 Electronic Parts (**the exploded views — so no part numbers were recoverable from any of the four**), §4.3 Function Button Locations, §5 Unit Block Diagrams, §6.1-6.7 in full, §8.9 Circuit Diagram in all four **and the CE/CEGS filter-choke diagram the special note points at**, the "Configuration:" block under every error code and the Action Flow Chart under E3, the E1 solution flow chart and its "check RPM sensor device procedure" chart (F65 pp23-24, F80 pp35-36, F85/F89 pp36-37), the E3 "Test configuration" and "Incline motor control function relate parts location" drawings (**only the three pin definitions in the prose survived**), every §9 photograph, and the §8.10/8.11 settings screenshots. **§6.8 Controller Indicator LED debugging survived as text only in the F65** — the other three machines have **no LED debugging card**. |
| **G10** — three F85 manuals | 2016: §1, §2/2.1/2.2, §5, §6.1-6.5 and §6.8, §8.8 circuit diagram (pp58-59), the E1 solution flow charts (pp41-42), the E3 action flow charts (pp46, 52), §11 incline motor installation drawing (pp72-73), every §12 step photograph. 2019: §1, §2, §5, §6.2, §6.5, §8.8 circuit diagram (pp75-76), E1 and E3 flow charts, §11 drawing, §12 photographs — **§6.1, §6.4 and §6.8 survive as callout labels only.** 2021: as Priority 2 above. |
| **G11** — S77 and ST90 | ST90 2021: §5 Unit Block Diagrams, §9 Circuit diagram, every figure in §10. ST90 2023: §5 and every figure in §9. S77 2016 and 2019: §6.1-6.6 board photographs and PCB component locations, §8.8 circuit diagram, the E1 and E3 "solution follow chart" flowcharts, §10 incline motor installation figures, every figure in §11. **S77 §7.3 grounding adapter illustration** — the text says *"a grounding plug that looks like the plug illustrated below"* and the illustration is an image. |
| **G12** — five TT8 manuals | §1 Outlines, §2.1/§2.2 electronic parts, §3 Electrical Configurations diagram, §5 Unit Block Diagrams, §6.1-§6.6 (display board wire connections, PCB component locations top and bottom, amplifier board, driver board wiring and component locations), §6.8 Driver Board function, the Circuit Diagram, the E1 and E3 solution flow charts, and every "Configuration:" image under an error code. **`sole-tm-tt8-2023-service-manual` §6.8 "Controller Indicator LED debugging" (p32) is a heading with nothing under it** — the 2016 and 2019 DC manuals print that table as text, so `tt8-2016-driver-board-led-debugging` and `tt8-2019-driver-board-led-debugging` exist and **there is no `tt8-2023` equivalent, not because the machine lacks the LEDs.** G12 §6.1: *"A technician asking 'which pin on the display board is the safety key' cannot be answered from these sources as ingested; the answer is only in the images."* |
| **G4** — C80 2026 | Exploded view (p5), **Console Display Layout (p16)**, Unit Block Diagrams (p16), every "(See figure)". **The biggest single loss is the Console Display Layout: there is no console card for that machine** beyond speed/RPM. Also **pages 8-15 are letter-spaced** and were rebuilt by hand — see G4 above; audit those ten procedures against the PDF. |
| **G6** — SRVO | Beyond Priority 1: pp3-5 the three outline drawings the 16 numbered parts point at (`srvo-exterior-parts-identification` gives names, not positions, and **its View column is inferred from row grouping and says so**); p9 the explosive view drawing (names and quantities only); **pp12-22, all eleven disassembly figures showing the screw or nut positions — every disassembly card gives the count and the tool, never the pattern**; pp30, 34, 39 the board photographs the No/Port tables key into, so the connector-map cards give the mapping and not the physical location. |

## What re-OCR will not fix

Two losses are in the documents, not the conversion, and OCR will not recover them:

- `sole-tm-tt8-2016-service-manual` p83 and `-tt8-2016-ac` p64 print a bare **`175`** beside a "deck
  wax" diagram with **no unit and no sentence**.
- `sole-rower-sr500-2016-service-manual` §7.2 lines 441-448 are numbered `1. 3. 4. 5. 6. 7.` —
  **step 2 is absent from the printed list**, not from the extraction.

And three documents are simply thin: `sole-c80-2026-service-manual` has **no safety section, no
warranty, no maintenance or cleaning schedule, no assembly instructions, no specifications table and
no error code list**; `sole-bike-sb1200-2023-service-manual` has **no safety section, no grounding or
outlet instructions, no belt-slipping answer and no noise section**;
`sole-bike-sb900-2023-service-manual` has **no belt-slipping answer and no noise section**. Those are
the documents, not the extraction, and **absence is the answer**: a technician asking "what is error
E1 on a C80" must be told the machine has no error codes, not given a treadmill's list.
