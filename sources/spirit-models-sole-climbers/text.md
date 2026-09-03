# Sole climber and stepper model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-03.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM dbo.Models
    WHERE Brand = 'Sole'
      AND (ModelName LIKE '%SC200%' OR ModelName LIKE '%SC300%'
           OR ModelName LIKE '%CC81%' OR ModelType IN ('Climber', 'Stepper'))
    ORDER BY ModelNumber

Rows returned:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 520516 | SOLE SC200 | Stepper | Sole |
| 520517 | SC200 | Elliptical | Sole |
| 581519 | SOLE CC81 | Climber | Sole |

Notes on what the rows do and do not say:

- `581519` is the only row whose `ModelType` is `Climber`, and the only CC81 row.
  Its `ModelName` carries no model year.
- The SC200 appears twice under two different `ModelType` values, `Stepper` and
  `Elliptical`. Neither row carries a model year.
- A query for `ModelName LIKE '%SC300%'` returned no rows, so the SC300 named in
  the 2021 FTMS tracker has no row in this table.

The wider Sole convention is that the last two digits of the model number are the
model year, but the CC81 row does not confirm it, because the name has no year to
check the suffix against. Recorded as read, not interpreted.
