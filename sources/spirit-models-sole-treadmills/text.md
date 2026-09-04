# Sole treadmill model numbers, Spirit database

Source: `spiritwebdbTest`, table `dbo.Models`, columns `ModelNumber`, `ModelName`,
`ModelType`, `Brand`. Read on 2026-09-04.

Query:

    SELECT ModelNumber, ModelName, ModelType, Brand
    FROM dbo.Models
    WHERE Brand = 'Sole' AND ModelType IN ('Treadmill')
    ORDER BY ModelNumber

The last two digits of `ModelNumber` are the model year.

Rows for brand Sole, ModelType Treadmill:

| ModelNumber | ModelName | ModelType | Brand |
|---|---|---|---|
| 525003 | SOLE S75 | Treadmill | Sole |
| 526003 | SOLE TT6 | Treadmill | Sole |
| 527003 | SOLE TT7 | Treadmill | Sole |
| 560812 | SOLE F60 | Treadmill | Sole |
| 560813 | SOLE F60 2013 | Treadmill | Sole |
| 560814 | SOLE F60 2014 | Treadmill | Sole |
| 560816 | F60 | Treadmill | Sole |
| 560820 | Sole F60 2019 | Treadmill | Sole |
| 563810 | SOLE AF63 | Treadmill | Sole |
| 563812 | SOLE F63 2013 | Treadmill | Sole |
| 563814 | SOLE F63 2015 | Treadmill | Sole |
| 563816 | SOLE F63 2016 | Treadmill | Sole |
| 563818 | SOLE F63 2019 | Treadmill | Sole |
| 563822 | SOLE F63 2023 | Treadmill | Sole |
| 563881 | SOLE F SIX THREE | Treadmill | Sole |
| 563886 | SOLE UF63 2006 | Treadmill | Sole |
| 563887 | SOLE VF63 2007 | Treadmill | Sole |
| 563888 | SOLE WF63 2008/09 | Treadmill | Sole |
| 565810 | SOLE AF65 | Treadmill | Sole |
| 565812 | SOLE F65 | Treadmill | Sole |
| 565813 | SOLE F65 2014 | Treadmill | Sole |
| 565816 | SOLE F65 2016 | Treadmill | Sole |
| 565818 | SOLE F65 2019 | Treadmill | Sole |
| 565822 | SOLE F65 2023 | Treadmill | Sole |
| 570003 | SOLE S70 | Treadmill | Sole |
| 573881 | SOLE S73 | Treadmill | Sole |
| 573886 | SOLE US73 2006 | Treadmill | Sole |
| 573887 | SOLE VS73 2007 | Treadmill | Sole |
| 577003 | SOLE S77 | Treadmill | Sole |
| 577810 | SOLE AS77 | Treadmill | Sole |
| 577812 | SOLE S77 2013 | Treadmill | Sole |
| 577816 | SOLE S77 2016 | Treadmill | Sole |
| 577818 | SOLE S77 2019 | Treadmill | Sole |
| 577881 | SOLE S77 | Treadmill | Sole |
| 577886 | SOLE US77 2006 | Treadmill | Sole |
| 577887 | SOLE VS77 2007 | Treadmill | Sole |
| 577888 | SOLE WS77 2008/09 | Treadmill | Sole |
| 580003 | SOLE F80 | Treadmill | Sole |
| 580810 | SOLE AF80 | Treadmill | Sole |
| 580812 | SOLE F80 2013 | Treadmill | Sole |
| 580816 | SOLE F80 2016 | Treadmill | Sole |
| 580818 | SOLE F80 2019 | Treadmill | Sole |
| 580822 | SOLE F80 2023 | Treadmill | Sole |
| 580881 | SOLE F80 | Treadmill | Sole |
| 580886 | SOLE UF80 2006 | Treadmill | Sole |
| 580887 | SOLE VF80 2007 | Treadmill | Sole |
| 580888 | SOLE WF80 2008/09 | Treadmill | Sole |
| 580918 | SOLE Desk TD80 2019 | Treadmill | Sole |
| 583003 | SOLE F83 | Treadmill | Sole |
| 583810 | SOLE AF83 | Treadmill | Sole |
| 583881 | SOLE F83 | Treadmill | Sole |
| 583886 | SOLE UF83 2006 | Treadmill | Sole |
| 583887 | SOLE VF83 2007 | Treadmill | Sole |
| 583888 | SOLE WF83 2008/09 | Treadmill | Sole |
| 585003 | SOLE F85 | Treadmill | Sole |
| 585810 | SOLE AF85 2011 | Treadmill | Sole |
| 585812 | SOLE F85 2013 | Treadmill | Sole |
| 585816 | SOLE F85 2016 | Treadmill | Sole |
| 585818 | SOLE F85 2019 | Treadmill | Sole |
| 585820 | SOLE F85 2020 | Treadmill | Sole |
| 585822 | SOLE F85 | Treadmill | Sole |
| 585881 | SOLE F85 | Treadmill | Sole |
| 585886 | SOLE UF85 2006 | Treadmill | Sole |
| 585887 | SOLE VF85 2007 | Treadmill | Sole |
| 585888 | SOLE WF85 2008/09 | Treadmill | Sole |
| 588810 | SOLE ATT8 | Treadmill | Sole |
| 588812 | SOLE TT8 | Treadmill | Sole |
| 588816 | SOLE TT8 2016 | Treadmill | Sole |
| 588818 | SOLE TT8 2019 | Treadmill | Sole |
| 588822 | SOLE TT8 2023 | Treadmill | Sole |
| 588881 | SOLE TT8 | Treadmill | Sole |
| 588886 | SOLE UTT8 2006 | Treadmill | Sole |
| 588887 | SOLE VTT8 2007 | Treadmill | Sole |
| 588888 | SOLE WTT8 2008/09 | Treadmill | Sole |
| 589853 | SOLE F89 | Treadmill | Sole |
| 590820 | SOLE ST90 2021 | Treadmill | Sole |
| 590822 | SOLE ST90 2023 | Treadmill | Sole |
| 594714 | SOLE FT94 | Treadmill | Sole |
| 596715 | SOLE FT96 | Treadmill | Sole |
| 598715 | SOLE FT98 | Treadmill | Sole |
| 599818 | SOLE TT9 2019 | Treadmill | Sole |

Total: 81 rows.
