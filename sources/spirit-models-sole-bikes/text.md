# Sole bike model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-03.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM Models
    WHERE Brand = 'Sole' AND ModelType = 'Bike'
    ORDER BY ModelName

Rows for brand Sole, ModelType Bike:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 511110 | LCB | Bike | Sole |
| 511112 | LCB | Bike | Sole |
| 511116 | LCB | Bike | Sole |
| 511118 | Sole LCB 2019 | Bike | Sole |
| 511122 | SOLE LCB 2023 | Bike | Sole |
| 512322 | SB1200 | Bike | Sole |
| 522110 | LCR | Bike | Sole |
| 522112 | LCR | Bike | Sole |
| 522116 | LCR | Bike | Sole |
| 522118 | LCR | Bike | Sole |
| 522122 | SOLE LCR 2023 | Bike | Sole |
| 570110 | Sole SB700 | Bike | Sole |
| 570116 | Sole SB700 2016 | Bike | Sole |
| 570119 | Sole SB700 2019 | Bike | Sole |
| 570120 | Sole SB700 2020 | Bike | Sole |
| 570121 | SB700 | Bike | Sole |
| 572115 | Sole R72 | Bike | Sole |
| 574115 | Sole B74 | Bike | Sole |
| 590314 | SOLE SB900 | Bike | Sole |
| 590316 | SOLE SB900 2016 | Bike | Sole |
| 590319 | SOLE SB900 2019 | Bike | Sole |
| 590320 | SOLE SB900 2020 | Bike | Sole |
| 590321 | SOLE SB900 2022 | Bike | Sole |
| 590322 | SOLE SB900 2023 | Bike | Sole |
| 592110 | SOLE R92 | Bike | Sole |
| 592112 | SOLE R92 2013 | Bike | Sole |
| 592116 | SOLE R92 2016 | Bike | Sole |
| 592118 | SOLE R92 2019 | Bike | Sole |
| 592122 | SOLE R92 2023 | Bike | Sole |
| 594112 | SOLE B94 2013 | Bike | Sole |
| 594116 | SOLE B94 2016 | Bike | Sole |
| 594118 | SOLE B94 2019 | Bike | Sole |
| 594122 | SOLE B94 | Bike | Sole |

The last two digits of the model number are the model year. Confirmed against
rows outside the bike range that carry the year in the name:

| ModelNumber | ModelName |
|---|---|
| 585812 | SOLE F85 2013 |
| 585816 | SOLE F85 2016 |
| 585818 | SOLE F85 2019 |
| 585820 | SOLE F85 2020 |
| 595015 | SOLE E95 2015 |
| 595018 | SOLE E95 2019 |

The SB700 and SB900 rows break that pattern: `570119` is named "Sole SB700 2019"
and `590319` is named "SOLE SB900 2019", so those two lines use 19 for 2019 while
the treadmills use 18.

Rows 511116 (LCB) and 522116 (LCR) carry no year in `ModelName`. They are the only
LCB and LCR rows whose model number ends in 16.
