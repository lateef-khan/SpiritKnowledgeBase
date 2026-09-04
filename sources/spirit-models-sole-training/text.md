# Sole training / strength model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-04.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM dbo.Models
    WHERE Brand = 'Sole' AND ModelType IN ('Training')
    ORDER BY ModelNumber

The last two digits of `ModelNumber` are the model year.

Rows for brand Sole, ModelType Training:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 578712 | SOLE SRB101 | Training | Sole |
| 578722 | SOLE SR260 | Training | Sole |

Total: 2 rows.
