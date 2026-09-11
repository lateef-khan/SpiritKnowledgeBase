# Xterra (step 3b) plan — decided 2026-09-11

Survey files: `xterra-survey.tsv`, `xterra-ids.tsv` (stamp / © / effective / SKU rows per PDF).
Before the first wave: add `xterra` to `kb.yaml` `facets.brand.values` and a `models: xterra:` list.
Ids: `<model>-<year>`; year = the back-cover revision stamp, else the © year confirmed by the
warranty-effective date, else the dbo.MODEL name; scans with no date get the table's year.
Every card `brand: [xterra]`; never extend a Spirit or Sole card with an Xterra id.

## X1 — treadmills (19 OMs + 8 SMs + 2 videos)
tr150-2021 (OM Rev 04.13.2021; SM "TR150 (GT65-NT014)" 2019 — same machine? measure vs OM, else its own id from the code year), tr200-2021, tr300-2021, tr64-2024, tr65-2023 (Rev 09.28.23), tr66-2021, tr75-2024 (Rev 06.07.24), tr75h-2025 (Rev 08.19.25; SM V1.0 20260127), tr85-2024, tr95h-2024 (©2023, eff Jan 3 2024, Rev 01.19.24; SM "JKEXER 337" 2024), trx1000-2021 (Rev 3.0, eff Mar 13 2021), trx1400-2023 (Rev 05.09.23; SM T3-NT053-01 2023), trx2500-2024 (OM eff Jun 7 2024; SM GT90B-NT022 2018 — probably the earlier generation: own id from the table FP 6/19/2017 → trx2500-2017?), trx3500-2024 / trx4500-2024 (OMs; SM GT90CD 2019 covers both → earlier generation, same question), trx5500-2024 (OM eff Mar 20 2024; SM GT90D-NT041 2021), tr260-2022 (©2022 eff Aug 24 2022, Rev 4.0; SM GT75A-NT050 2022), ws200-2023, ws300-2023 (Rev 10.09.23). Videos: "How to assemble the wire WS200-300.mp4", "TR95H Track the belt demo.mp4" — frame-describe as with the XS895 video. "TR150 T500 MCB wiring.jpg" — a photo; describe by eye.
SKUs: 100819 TRX1000, 112084 TRX1200 (no manual), 125817 TRX2500, 135817 TRX3500, 145817 TRX4500, 140082 TRX1400, 160083 TR600, 165873 TR65, 175825 TR75H, 175873 TR75, 185873 TR85, 195813 TR95H, 164583 TR6.45, 165811 TR6.55 2012, 166583 TR6.65 2013, 166813 TR6.6 2013, 168813 TR6.8, 162811 TR6.2 2012, 163812 TR6.3 2013, 170086 TR700, 180814 TR800, 250809 TR250, 430518 Intrepid i300, 138013/138014 TR3.0. The TR64/TR65/TR66 names look like successors of the TR6.45/6.55/6.65 — do NOT map by name; the OMs' own SKUs decide.

## X2 — bikes, ellipticals, climber (21 + 9 + 2 OMs, 4 small SMs, the app QA)
Bikes: air350-2019, air650-2020 (SM 2-page "AIR650 _165710_ SM"), fb150-2021, fb160-2019 (SM 3-page service document 2019), fb180-2025 (two SKUs 115425 / 118425(NS)), fb350-2021, fb360-2019, mb500 (scan; year from OCR/table), mb550-2018, mbx2500-2018, sb120-2022 (SM 4-page service doc 2019), sb150-2018, sb240-2023, sb250-2019, sb25r-2020, sb4500-2021, sb45r-2012 (scan; table "SB4.5r 2012"), sb500-2014 (scan; 150314 FP 8/1/2014) and sb500-2020 (©2018, eff Jul 6 2020 — measure the two), sb600-2023 (+ SM V1.0 2025 from the Spirit folder), ub120-2023.
Ellipticals: eu100-2018, eu150-2024, fs150 (scan), fs15-2019, fs25-2020, fs30-2018, fs35-2020, fs58e-2013 (scan; 158012), fs59e-2014 (scan; 159003).
Climber: rsx1500-2021 (+ an older scan RSX1500_OM_115518: OCR, date it).
XTERRA APP QA EN.pdf: a 2-page 2018 Q&A about the app — policy/console cards, product_line '*', brand xterra.

## X3 — rowers, strength (11 + 4 OMs, 2 SMs + 4 Spirit-folder ERG SMs + the ERG750W OM)
er800w-2023, erg160-2020 (+ SM V1.0 2025), erg180-2023 (+ SM V1.0 2025; two identical OM copies), erg220-2019 (©2019, no effective line — read the page), erg400-2014 (scan; 140914 FP 8/18/2014), erg500-2018, erg550w-2023 (©2022, eff Jan 1 2023; SM 2022), erg600w-2021 (SM 2019), erg650w-2021 (©2021, eff Mar 4 2020 — read), erg700-2022, erg750w-2025 (OM Rev 11.12.2025 in the Spirit folder; SM 2026), erg800w (OM? none — SM V1.0 2025 "ERG800W_R80"; the ER800W OM 2023 may be it: measure). Strength: adb12-5pr-2022, adb25-2022, adb55-2022, dbstand-2022 (four near-identical dumbbell books).
