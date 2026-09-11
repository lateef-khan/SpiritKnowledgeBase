<!-- Source: E50H CT800 2020.pdf. Six photographed pages (Skia/PDF export, no text layer). tesseract read 8-19 words per page, so every page below is a TRANSCRIPT typed from the 100 dpi render by the orchestrating agent on 2026-09-11, not OCR. Photographed cards are slightly cut off at their edges; a cut-off word is marked [cut]. Text set by the author of the document (headings, notes) is separated from the photographed cards. -->

=== TRANSCRIPT, PDF PAGE 1 ===
[document text]
Spirit TM CT800 #800840 E-50H

Error Message for DC Motor Controller

[photographed card, header partly cut]
ERROR MESSAGE of New CT800&CT850(2020)
For D/C Motor Controlling System:
E1: No out put from motor.
E2: Overloading protection.
E3: Incline Error.
E4: Abnormal voltage input to motor or wrong wiring between motor/control board.
E5: Communication error between console/control board.
E6: Control board malfunction.
E7: Abnormal voltage input to control board from house power.

[document text]
Error message for AC Transformer

=== TRANSCRIPT, PDF PAGE 2 ===
[photographed card, header partly cut: "...RROR MESSAGE :"]
For A/C Transforming System:

E-01H: Low voltage break (Please make sure if input power from house power is too low).
E-02H: Abnormal Temperature is detected.
E-04H: (OC) Transformer over output current.
E-06H: (OE) Transformer over output voltage.
E-07H: (PFC) Transformer abnormal.
E-08H: (GF) Ground failed.
E-09H: (OH) Transformer over heat.
E-0AH: (OL) Motor Overloading.
E-0BH: (OL1) Transformer Overloading.
E-0CH: (OLO) System Overloading.
E-21H: (PrEr Flash) Program failed.
E-22H: EEPROM.
E-23H: Low Voltage.
E-25H: Emergency Stop.
E-26H: (drvF Driver) Setting error.
E-27H: (LP) Low voltage input.
E-28H: (HP) High voltage input.
E-29H: (HT) High Temperature Notice.
E-41H: (OLO) System overloading.
E-42H: (HT) High Temperature warning.

Solution: all above are related with transformer error, so please check the wiring first before replace a new transformer.

[document text]
The console displays error code at intiaial startup?

=== TRANSCRIPT, PDF PAGE 3 ===
[photograph of the console, dot-matrix window reading "E-50H"; display labels visible: DISTANCE, PACE, WATTS, METs, TIME REMAINING, TRACK, SPEED, INCLINE; keys ENTER, up/down arrows, PROGRAM]
[red overlay text on the photograph]
CT800 #800840
E-50H Service Doc.

[document text]
UPPER DISPLAY

=== TRANSCRIPT, PDF PAGE 4 ===
[photograph of the lower controller board, red connector strip, labels drawn on the photo in red: JK15, JK10, JK11, JK30; in yellow: JK6]

[document text]
Note: The upper computer cable, SP# must be plugged into the JK6/ STD red 6-pin port.

Procedure on Repair

=== TRANSCRIPT, PDF PAGE 5 ===
[photographed card, header partly cut: "...of New C..."]
E-50H: Communication error between console and transformer.
Solution:
a). Checking wiring.
b). Replacing a new transformer.
c). Replacing a new console.

E-51H: Internal Signal error of console.
a). Checking wiring.
b). Replacing console.
(For TFT only)

E-52H: Incline error during calibration.
a). Checking Incline VR wiring.
b). Checking Incline motor wiring.
c). Checking if the spiral stuck.
d. Replacing a new transformer.

E3: Incline error.
a). Checking Incline VR wiring.
b). Checking Incline motor wiring.
c). Checking if the spiral stuck.
d). Replacing a new transformer.

[document text]
Middle computer cable w/ heavier insulated jacket, plus zip tie anchor at R console support bracket.

=== TRANSCRIPT, PDF PAGE 6 ===
[photograph: a replacement console cable - a black corrugated-sleeved harness beside a plain black cable - hanging in front of SPIRIT FITNESS spare-parts cartons on a warehouse shelf; carton labels read "SPIRIT FITNESS", "MADE IN TAIWAN", "SPARE PARTS", a part label "CT800(800840)..." with a barcode, a handwritten "RM040004B A-20" and "44981-3..." [cut]; no further legible text]
