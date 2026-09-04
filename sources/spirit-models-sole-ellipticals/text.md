# Sole elliptical and stepper model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-04.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM dbo.Models
    WHERE Brand = 'Sole' AND ModelType IN ('Elliptical', 'Stepper')
    ORDER BY ModelNumber

The last two digits of `ModelNumber` are the model year.

Rows for brand Sole, ModelType Elliptical or Stepper:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 520013 | SOLE E20 | Elliptical | Sole |
| 520014 | SOLE E20 2015 | Elliptical | Sole |
| 520016 | E20 | Elliptical | Sole |
| 520020 | SOLE E20 2020 | Elliptical | Sole |
| 520516 | SOLE SC200 | Stepper | Sole |
| 520517 | SC200 | Elliptical | Sole |
| 525010 | SOLE AE25 | Elliptical | Sole |
| 525012 | SOLE E25 | Elliptical | Sole |
| 525013 | SOLE E25 | Elliptical | Sole |
| 525016 | SOLE E25 | Elliptical | Sole |
| 525018 | Sole E25 2019 | Elliptical | Sole |
| 525022 | SOLE E25 2023 | Elliptical | Sole |
| 525081 | SOLE E25 | Elliptical | Sole |
| 525087 | SOLE VE25 2007 | Elliptical | Sole |
| 525088 | SOLE WE25 2008/2009 | Elliptical | Sole |
| 525113 | SOLE E25 | Elliptical | Sole |
| 525114 | SOLE E25 | Elliptical | Sole |
| 525116 | SOLE E25 2016 | Elliptical | Sole |
| 535010 | SOLE AE35 | Elliptical | Sole |
| 535012 | SOLE E35 | Elliptical | Sole |
| 535013 | SOLE E35 | Elliptical | Sole |
| 535014 | SOLE E35 | Elliptical | Sole |
| 535015 | SOLE E35 2015 | Elliptical | Sole |
| 535016 | SOLE E35 2016 | Elliptical | Sole |
| 535018 | SOLE E35 2019 | Elliptical | Sole |
| 535022 | SOLE E35 2023 | Elliptical | Sole |
| 535081 | SOLE E35 | Elliptical | Sole |
| 535087 | SOLE VE35 2007 | Elliptical | Sole |
| 535088 | SOLE WE35 2008/09 | Elliptical | Sole |
| 555010 | SOLE AE55 | Elliptical | Sole |
| 555013 | SOLE E55 2014 | Elliptical | Sole |
| 555014 | SOLE E55 | Elliptical | Sole |
| 555016 | SOLE E55 2016 | Elliptical | Sole |
| 555018 | Sole E55 2019 | Elliptical | Sole |
| 555081 | SOLE E55 | Elliptical | Sole |
| 555086 | SOLE E55 2006 | Elliptical | Sole |
| 555087 | SOLE VE55 2007 | Elliptical | Sole |
| 555088 | SOLE WE55 2008/09 | Elliptical | Sole |
| 575081 | SOLE E75 | Elliptical | Sole |
| 595010 | SOLE AE95 2011 | Elliptical | Sole |
| 595012 | SOLE E95 2013 | Elliptical | Sole |
| 595013 | SOLE E95 2014 | Elliptical | Sole |
| 595014 | SOLE E95 2015 | Elliptical | Sole |
| 595015 | SOLE E95 2016 | Elliptical | Sole |
| 595016 | SOLE E95 2016 | Elliptical | Sole |
| 595018 | SOLE E95 2019 | Elliptical | Sole |
| 595022 | SOLE E95 | Elliptical | Sole |
| 595081 | SOLE E95 | Elliptical | Sole |
| 595087 | SOLE VE95 2007 | Elliptical | Sole |
| 595088 | SOLE WE95 2008/09 | Elliptical | Sole |
| 595616 | SOLE E95S 2016 | Elliptical | Sole |
| 595618 | SOLE E95S 2019 | Elliptical | Sole |
| 595622 | SOLE E95s 2023 | Elliptical | Sole |
| 598012 | SOLE E98 | Elliptical | Sole |
| 598015 | SOLE E98 | Elliptical | Sole |
| 598016 | SOLE E98 | Elliptical | Sole |
| 598018 | SOLE E98 2019 | Elliptical | Sole |
| 598022 | SOLE E98 2023 | Elliptical | Sole |

Total: 58 rows.
