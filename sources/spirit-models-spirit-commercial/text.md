# Spirit commercial model numbers, CustService database

Source: SQL Server `CustService` on the Spirit Server, table `dbo.MODEL`, columns
`MODELNO`, `MODEL`, `FG`, `DESC`, `Brand`, `SOLE`, `Commercial`, `VERSION`. Read
on 2026-09-08 as `SpiritReadOnlyUser`.

This is **not** the same table as the Sole lookups already in this repo. Those read
`dbo.Models` in the Azure database `spiritwebdbTest`. This one reads `dbo.MODEL` in
the on-premise `CustService` database. The column names differ and the two tables
are not known to agree.

Query:

    SELECT MODELNO, MODEL, FG, [DESC], Brand, SOLE, Commercial, VERSION
    FROM dbo.MODEL
    WHERE MODEL LIKE '%CE800%' OR MODEL LIKE '%CRW800%' OR MODEL LIKE '%CT850%'
       OR MODEL LIKE '%CU900%' OR MODEL LIKE '%CVC800%'
       OR MODELNO LIKE '%CE800%' OR MODELNO LIKE '%CRW800%' OR MODELNO LIKE '%CT850%'
       OR MODELNO LIKE '%CU900%' OR MODELNO LIKE '%CVC800%'
       OR FG LIKE '%CE800%' OR FG LIKE '%CRW800%' OR FG LIKE '%CT850%'
       OR FG LIKE '%CU900%' OR FG LIKE '%CVC800%'
    ORDER BY MODEL, VERSION

## Machine rows

Accessory and spare-part rows are listed separately below.

| MODELNO | MODEL | FG | DESC | Commercial |
|---|---|---|---|---|
| 800025 | CE800 | ELLIPTICAL | SPIRIT, ELLIPTICAL CE800 | |
| 800042 | Spirit CE800 | Elliptical | Elliptical Spirit CE800 | |
| 800049 | CE800 | ELLIPTICAL | FG, SPIRIT, CE800 2009 ELLIPTICAL | 1 |
| 800043 | CE800 CSAFE | ELLIPTICAL | FG, SPIRIT, CE800 2009 ELLIPTICAL | 1 |
| 800044 | CE800 2014 | ELLIPTICAL | FG, SPIRIT, CE800 2014 ELLIPTICAL | 1 |
| 800045 | Spirit CE800 2016 | ELLIPTICAL | Elliptical Spirit CE800 2016 | 1 |
| 800040 | Spirit CE800 2020 | Elliptical | Elliptical Spirit CE800 2020 | |
| 800054 | CE800 ENT | Bike | FG, SPIRIT ELLIPTICAL CE800 ENT | |
| 800065 | CE800ENT | ELLIPTICAL | SPIRIT, ELLIPTICAL CE800ENT | |
| 800052 | CE800ENT | Eliptical | FG, Spirit CE800 ENT Elliptical | |
| 800055 | Spirit CE800ENT 2016 | ELLIPTICAL | Elliptical Spirit CE800ENT 2016 | 1 |
| 800050 | CE800ENT 2020 | ELLIPTICAL | FG, SPIRIT, CE800ENT 2020 ELLIPTICAL | |
| 800925 | CRW800 | Rower | Spirit CRW800 Rower | |
| 800945 | Spirit CRW800 2016 | ROWER | Rower Spirit CRW800 2016 | 1 |
| 800940 | Spirit CRW800 2020 | Rower | Rower Spirit CRW800 2020 | |
| 800998 | Spirit CRW800 H2O (NS) | ROWER | Rower Spirit CRW800 H2O (NS) | |
| 850813 | CT850 | TREADMILL | FG, SPIRIT, CT850 TREADMILL | |
| 850825 | CT850 | TREADMILL | SPIRIT, TREADMILL CT850 | |
| 850845 | Spirit CT850 2016 | TREADMILL | Treadmill Spirit CT850 2016 | |
| 850840 | Spirit CT850 2020 | Treadmill | Treadmill Spirit CT850 2020 | |
| 850850 | CT850ENT | TREADMILL | FG, TREADMILL CT850ENT | |
| 850852 | CT850ENT | Treadmill | FG, Spirit CT850 ENT Treadmill | |
| 850865 | CT850ENT | TREADMILL | SPIRIT, TREADMILL CT850ENT | |
| 850855 | Spirit CT850ENT 2016 | TREADMILL | Treadmill Spirit CT850ENT 2016 | 1 |
| 850851 | Spirit CT850ENT 2020 | Treadmill | Treadmill Spirit CT850ENT 2020 | |
| 900325 | CU900 | Bike | Spirit CU900 Bike | |
| 900346 | Spirit CU900 | BIKE | Bike Spirit CU900 | 1 |
| 900340 | CU900-LED | BIKE | FG, Bike, Spirit CU900-LED Dark Gray | |
| 900350 | CU900ENT | Upright Bike | (empty) | |
| 900356 | Spirit CU900ENT | BIKE | Bike Spirit CU900ENT | 1 |
| 800440 | Spirit CVC800 2020 | Vertical Climber | Climber Spirit CVC800 2020 | |

Every row above has `Brand` = `SPIRIT` or `Spirit` and `SOLE` = 0.

## Accessory and spare-part rows

These are parts, not machines. They are listed so a later reader does not mistake
one for a machine SKU.

| MODELNO | MODEL | FG |
|---|---|---|
| 902346 | .CU900 BRACKET | ACCESSORY |
| 851845 | .MED HANDRAIL CT850 2016 | HANDRAIL |
| 802049 | .TV CONSOLE BRACKETS - CE800 | TV CONSOLE BRACKETS |
| 802043 | .TV CONSOLE BRACKETS - CE800 2014 | TV CONSOLE BRACKETS |
| 802853 | .TV CONSOLE BRACKETS - CT850 | TV CONSOLE BRACKETS |

## Notes on what the rows do and do not say

- **CVC800 has exactly one row**, `800440`, and its `MODEL` carries the year 2020.
  The CVC800 service manual prints no model year at all. The name is the only
  evidence of a year and it is a database name, not the manual.
- **CU900ENT has two rows**, `900350` and `900356`. Neither carries a model year.
  They differ in `FG` (`Upright Bike` against `BIKE`) and in `Commercial`
  (empty against 1). Which one the CU900ENT service manual describes is not
  determined by the table.
- **CE800ENT has five rows.** Only two carry a year: `800055` (2016) and `800050`
  (2020). The CE800ENT service manual cover prints "2020 ver.", which matches
  `800050`.
- **CRW800 H2O has exactly one row**, `800998`, named `Spirit CRW800 H2O (NS)`.
  It carries no year. What `(NS)` stands for is not stated in the table.
- **CT850 has four machine rows.** `850845` is named 2016 and `850840` is named
  2020. The manual whose filename carries `850845` prints no year of its own; its
  cover prints the factory document code `ST8100-CT001` and `(110V)`. The other
  CT850 manual prints `CT850(2020)` on its cover, which matches `850840`.
- **CT850ENT and CE800 non-ENT rows exist but have no manual in this import.**
  They are recorded here so a later import does not re-query.
- The last two digits of `MODELNO` are **not** a reliable model year. `850845` is
  named 2016 and `850840` is named 2020, so the suffix is a code, not the calendar
  year. Use the year printed in `MODEL`, and where `MODEL` has no year, say the
  year is unconfirmed.
- `VERSION` is a revision counter on the row, not a machine version. Rows repeat
  across versions with identical names. Only the distinct names are listed above.
