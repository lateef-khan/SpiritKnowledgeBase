# Sole rower and recumbent model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-04.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM dbo.Models
    WHERE Brand = 'Sole' AND ModelType IN ('Rower', 'Recumbent')
    ORDER BY ModelNumber

The last two digits of `ModelNumber` are the model year.

Rows for brand Sole, ModelType Rower or Recumbent:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 500911 | SR500 | Rower | Sole |
| 500918 | SR500 2019 | Rower | Sole |
| 555922 | SOLE SR550 2023 | Rower | Sole |
| 598088 | SOLE WB48 | Recumbent | Sole |

Total: 4 rows.
