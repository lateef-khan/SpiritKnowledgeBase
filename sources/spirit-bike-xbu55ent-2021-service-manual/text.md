<!-- Source: XBU55ENT Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XBU55 ENT
    Service Manual




1                    Service Manual
1. XBU55 ENT Outlines




          2             Service Manual
3   Service Manual
2. Electronic Parts




         4            Service Manual
Upper Controllers




         DISPLAY




                    5   Service Manual
              Cooling FAN




Speaker




          6                 Service Manual
Lower Controller and Driver




             SPEED RPM SENSOR




             TENSION MOTOR



                                7   Service Manual
3.Electrical Configurations




             8                Service Manual
CONSOLE:
 Interface that controls all functions of the Bike.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console、incline driver and tension motor driver, link the console to output appropriate voltages for tension
 motor that control the Bike functions.

TENSION    MOTOR:

 It can change to increase or decrease resistance level of brake.

INCLINE MOTOR:
 This is an AC motor. User can to control variable elevation by console within main controller.
GENERAL INFORMATION

CONSOLE
   Contain keys control and TFT LCD touch panel.

TENSION MOTOR
   Work voltage:DC 4.5~7.5V
   Control resistance increases and decreases.




                                                                              9                                                                  Service Manual
4. XBU55 ENT Product Operation




              10                 Service Manual
Display Windows


                         TFT LCD TOUCH
                         PANEL & PROGRAM
                         MENU




      COOLING FAN



                         START, STOP
                         LEVEL CONTROLS



       USB
       CHARGER




                    11                     Service Manual
POWER
When the power cord is connected to the fitness bike, the console will automatically power up.

QUICK START
This is the quickest way to start a workout. After the console powers up you just press START WORKOUT on the screen, or press the Start key to begin.
This will initiate the Quick Startmode. In Quick Start the Time will count up from zero and the workload may be adjusted manually by pressing the Level Up/
Down buttons. The dot matrix display will have only the bottom row lit at first.
There are 20 levels of resistance available for plenty of variety. The first 5 levels are very easy workloads and the changes between levels are set to a good
progression for de-conditioned users. Levels 6-10 are more challenging, but the increases in resistance from one level to the next remain small. Levels
11-15 start getting tough as the levels jump more dramatically. Levels16-20 are extremely hard and are good for short interval peaks and elite athletic
training.

BASIC INFORMATION
The Stop button actually has several functions. Pressing the Stop key once during a program will pause the program for 5 minutes. If you need to get a
drink, answer the phone or any of the many things that could interrupt your workout, this is a great feature. To resume your workout during Pause, just
press the Start key. If the Stop button is pressed twice during a workout, the program will end and the console will display your Workout Summary (Total
time, Avg. Speed, Avg. Power, Avg. HR, total Laps).


PROGRAMMING THE CONSOLE
Each of the programs can be customized with your personal information and changed to suit your needs. Some of the information asked for is necessary to
ensure the readouts are correct. You will be asked for your Age and Weight. Entering your Age ensures that the Heart Rate bar graph shows the correct
number. Your Age is also necessary during the Heart Rate control program to ensure the correct settings are in the program for your Age. Otherwise the
work settings could be too high or low for you; entering your Weight aides in calculating a more correct Calorie reading. Although we cannot provide an
exact calorie count we do want to be as close as possible.

                                                                                   12                                                       Service Manual
CALORIE NOTE: Calorie readings on every piece of exercise equipment, whether it is in a gym or at home, are not accurate and tend to vary widely. They
are meant only as a guide to monitor your progress from workout to workout. The only way to measure your calorie burn accurately is in a clinical setting
connected to a host of machines. This is because every person is different and burns calories at a different rate. Some good news is that you will continue
to burn calories at an accelerated rate for at least an hour after you have finished exercising!


CHARGE PORTABLE DEVICES WITH USB PORT
You can charge your personal device during your workout using the fitness equipment’s on-consoleUSB port. To charge your mobile electronics make sure
the fitness equipment power is on.Step 1: Connect your USB charging cable (not included) to the USB Power Port and to your device.Step 2: Check to
make sure your device icon indicates it is charging.
NOTE:
• USB charging cable is not included, make sure compatible USB charging cable is being used.
• The USB port on the console is capable of powering USB devices. It provides up to 5Vdc/1.0amp of power and meets USB 2.0 regulations. You will not
be able to save your workout data toa USB via this port; it is used for charging purposes only.




                                                                               13                                                         Service Manual
5. XBU55 ENT Unit Block Diagrams




               14              Service Manual
Bike Configuration




                     15   Service Manual
6. Basic Connections and Wiring




               16                 Service Manual
Display Board wire Connections




                                 17   Service Manual
Display Board PCB Component Locations

 PCB Board Top




                                        18   Service Manual
PCB Board Bottom




                   19   Service Manual
The console Interface Board wire Connections




                                               20   Service Manual
Tension Motor connector definition function




        STEEL ROPE




        MAIN
        CONTROL
        1.M+                      5
        2.M-                      4
        3.+5V                     3
        4.VR                      2
        5.GND                     1




                                              21   Service Manual
7. XBU55 ENT Error Messages /
      Troubleshooting




              22                Service Manual
   Error code items：


                        Error Message             Explain
                        E2                        Tension motor is failure


   Prepare：


                                        Picture                              Tool name




                                                                             Multi-meter




                                                            23                             Service Manual
 Error Message ：E2
   Definition：When you press the Level Up or Down key,the motor does not move.” E2” appears on the display.
   Configuration：




                                                                             24                                Service Manual
 Tension Motor Operation
                                 Part            Description

                                                 Key signal travels to the display.The main program IC then sends a
                                 Display
                                                 command signal to the drive board.

                                                 Drive board receives the signal and responds by putting out power to
                                 Drive Board
                                                 the motor.Level UP:+5VDC;Level DOWN:-5VDC


 Tension Motor Troubleshooting

                                 Part            Description
                                 Display         If the key beeps when pressed,assume that the signal was sent.
                                 Data cable      Inspect the cable and connections.
                                                 Inspect drive board power output to the motor.Press the Level Up is
                                                 +5VDC;Level DOWN is -5VDC.If there is power to the motor,but the
                                 Drive Board
                                                 motor does not operate,replace it.If there is no power output,inspect
                                                 whether the drive board has power.


 Tension Motor Voltage Test Procedure
  1. Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the
      drive board.
  2. Turn on unit power. The display lights up.
  3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates.Resistance increases.
  4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates.Resistance decreases.
  5. If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
  6. Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.




                                                                        25                                                 Service Manual
Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the drive board.


                                                   26                                                       Service Manual
XBU55 ENT CIRCUIT DIAGRAM




           27               Service Manual
MAINTENANCE MENU IN CONSOLE SOFTWARE



Click the “Settings” at “Settings” page 10 times to enter “Engineer Mode”
-Settings




-Engineer Mode




                                                                            28
1. Function
  Units
   Switch between “imperial” and ”metric”

  Odo
   Click on “Reset” to clear all odometer.

  Display Mode
   Default is OFF. When set OFF, the electronic watch will go to sleep without any operation
   within 30 minutes. Press any key to wake up.

  Beep Mode
   Turn off beep mode, no beeping sound is heard.

  Software Update
   Pressing “USB” to update APK.
   Pressing “OSOTA” to update OS, then press “Check for update” down below the screen.
   Pressing “Command” to update SUB PCB.




                                                                                 29
2. Service
  Key Test
      Click “Reset” to clear key.

  Motor Test
   1. Manual : Click “Test” to Enable Test tiny move Motor function, then Click “+” or “-” to tiny
      move Motor forward or backward
      It will show AD value for current position
   2. Auto : Click “Test” to Enable Test lift test function, it will move Motor Up to High-Level then
      move motor Down to Low-Level automatically.
      It will show AD value for current position and target Level and count of cycle


  Incline Test
     1. Manual : Click “Test” to Enable Test tiny move incline Motor function, then Click “+” or “-”
         to tiny move incline Motor forward or backward
         It will show AD value for current position
     2. Auto : Click “Test” to Enable Test lift test function, it will move incline Motor Up to
         High-Level then move incline Motor Down to Low-Level automatically.
         It will show AD value for current position and target Level and count of cycle

  Sensor Test
   Click “Test” to enable test sensor, can test BT HR value, HP value, WP value and RPM.




                                                                                     30
3. Factory Setting
 Restore Factory
  Click “Clear” to restore factory.
 First Launch
  Click “ON” to set First Launch ON, then re-power ON will process First Launch UI.
 Machine Type
  See the console machine type.
 BLENAME
  Can input the new name and press SAVE then can re-name BLE device name, need re-power
  on then can use phone to scan console device for new BLE name.* just for developer test

  - Machine Type is XBU55 or XBR55




                                                                          31
4. Factory Setting
 Incline Calibration
   Click “start” to calibrate incline. The incline motor will move UP till no move any more for 3~6 sec and
   move Down till no move any more for 3~6 sec then finish to calibration , during calibration.




                                                                                             32
  Troubleshooting procedure matrix
                     Condition                                         Reason                                                Solve
LCDs not bright, incomplete or imperfect.           1. LCD light is broken.                      1. Replace with new LCD or console.
                                                    2. Power to console too low.                 2. Check AC power is 110-120V.
                                                                                                 3. Check power to console.
                                                                                                 4.Replace lower controller.
LCD displays not bright, incomplete or imperfect.   1. LCD displays are broken.                  1. Replace with new console.
The incline position doesn’t match console          1 Console is not calibrated.                 1 Calibrate the console.
Erratic pulse display.                              1. Another chest belt in use around Bike.    1. Check for other chest belt use around Bike.
                                                    2. Other magnetic field disturbance.         2. Change the position or direction of Bike.
                                                    3. Receiver is broken.                       3. Replace with new receiver.
Hand pulse lost its function.                       1. Hands not on the hand pulse sensors or    1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                        only one hand on sensor.
                                                    2. The connector of HANDPULSE W/WIRE 2. Connect the cable again.
                                                       and Console not connected properly.
                                                    3. The wires got damaged when connecting 3. Replace with new cable.
                                                       the HANDPULSE W/WIRE and Console.
                                                    4. Hand pulse board is broken.              4. Replace console or Hand pulse board.
Wireless lost its function.                         1. Chest belt not worn properly.            1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                    oriented correctly.
                                                    2. Distance is too far and exceeds range of 2. User chest belt in front of console within 3 feet.
                                                    receiver.                                   3. Replace with new lithium battery type is CR2032.

                                                    3. Chest belt battery is weak or dead.
Chest belt too close to the Bike.                   Weak battery.                                Replace with new lithium battery with type CR2032.




                                                                                   33                                                              Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS I

jenuepy 8dIAlas
INA SSnaXx


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SOUTINOG LNA SSNaXx *}


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS ¢

AV'IdSIG

LlealelS

& Lo 6 v + °

i4San5 "0113H

$19]]01]U04 addy


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS L

YOLOW NOISNAL

YOSNAS Wda Gddd$

JOALIQ Puke 413]|01]U0D JMO}


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

suoneinbipuoy [e914]99/F7¢


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

uoleiadC JONPOJd LNA SSNgX “Fp


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS Il

dHOUAVHO
qsn

STOYLNOD THAYT
dO.LS “LUVLS

LiAMdS

LNOWMOM Levis

iLS3ND °O113H

ONAN
WVddDOdd % THAHNVd
HONOL GOT LAL

smopul(\ Aeldsig


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

sweibeig yIo/g Iu) LNA SSngXx 's


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUBP AIWAIS '

YOLOW HOLIMS SAAC
; MOd
NOISNAL

YONAS
Ida

WI
YDiVadsS

NV4 duvoOd AV'IdSIG

NIANIM

YHAISOa UVa IGNVH

Ady

YH SSH TAMIA MH

uoleinbiyuod ex1g


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Gui, pue SuoljaauU0y aISeg “9g


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS tI

(SNId 9) qDaAVHO

HOLIMS HINOAL) orgy watsas

Vas TAONVH
YH LOVLINOO

davod Ady

YH SSATAUIM,
€0-TOOOTVLV

NI SANIT

UY MAN VAds ‘| YANVAdS NVd DNTTOO)D

SUOI]D9UUOYD 211M pseog Ae\dsig


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS a

doy, prvog God

SUOI]}E907] JUBUOdWIOD g4dd pieog Aejdsig


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS
61

[O-ZOOLES:
OIA 10-700105)

wonog prog qd


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS 0z

YONHS
HS'1Nd
dIYDANVH

YONHS
HS'1Nd

dIYDANVH

HaIM

TT-c-cOOTESI-M

SUOI]OOUUOYD OJIM P1LOG BORj19}U] BJOSUOD aU]


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS Iz

CNO'S
UAL
ASt'€

WT

+I
“IOULNOOD
NIV

UOI]}OUNJ UOILIUIJAp 410]}099UUO0D JO}OWY UOISUa]


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

burnlooysaqnol]
/ sabessayy 40417 LNA SSNEX ‘Z


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDP a1Ala¢ €Z

7 0

S@WeU [OO] aINIDId

: aedaig @

QIN]Te] ST JOJOU! UOTSUIT, cH

ureydxq ISeSSIJ JOM

: SUID]T 9pod JONI ®


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Error Message : E2

@ Definition : When you press the Level Up or Down key,the motor does not move.” E2” appears on the display.

@ Configuration :

LEVEL
DISPLAY BOARD UP/DOWN KEYS UP/DOWN
KEYS
A
LEVEL LEVEL
VR UP/DOWN
SIGNAL SIGNAL
v
TENSION MOTOR

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Tension Motor Operation

Part Description

Disol Key signal travels to the display. The main program IC then sends a
ispla ;
pray command signal to the drive board.

Drive board receives the signal and responds by putting out power to

Drive Board
me Boat the motor.Level UP:+5VDC;Level DOWN:-5VDC

@ Tension Motor Troubleshooting

Part Description
Display If the key beeps when pressed,assume that the signal was sent.
Data cable Inspect the cable and connections.

Inspect drive board power output to the motor.Press the Level Up is
+5VDC;Level DOWN is -SVDC.If there is power to the motor,but the
motor does not operate,replace it.If there is no power output,inspect

Drive Board

whether the drive board has power.

@ Tension Motor Voltage Test Procedure
1. Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the
drive board.
2. Turn on unit power. The display lights up.
3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates.Resistance increases.
4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates.Resistance decreases.
5. If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
6. Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.

25 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
XBU355 ENT CIRCUIT DIAGRAM

CONSOLE

L

NZ J
Ze

Ch :

Te ia

| SPEED SENSE

D4A05

27 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
MAINTENANCE MENU IN CONSOLE SOFTWARE

Click the “Settings” at “Settings” page 10 times to enter “Engineer Mode
-Settings

a6 & & B a
SETTINGS
Display Brightness WiFi Bluetooth Software®
Date Time Child Lock Units
Display Mode

* $ & @ nx ©

€ ENGINEER MODE

FUNCTION

Unit renin) METRIC
Odo 9999 HOUR 9999 KM
Display OFF
Beep OFF

-Engineer Mode

28


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
1. Function

@ Units
Switch between “imperial” and ”metric”

®@ Odo
Click on “Reset” to clear all odometer.

@ Display Mode
Default is OFF. When set OFF, the electronic watch will go to sleep without any operation
within 30 minutes. Press any key to wake up.

@ Beep Mode
Turn off beep mode, no beeping sound is heard.

® Software Update
Pressing “USB” to update APK.
Pressing “OSOTA’ to update OS, then press “Check for update” down below the screen.
Pressing “Command” to update SUB PCB.

- ENGINEER MODE

FUNCTION

Unit METRIC
Odo 9999 HOUR 9999 KM
Display Fon] OFF
Beep Foon] OFF

29


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. Service

@ Key Test
Click “Reset” to clear key.

@ Motor Test
1. Manual : Click “Test” to Enable Test tiny move Motor function, then Click “+” or
move Motor forward or backward
It will show AD value for current position
2. Auto : Click “Test” to Enable Test lift test function, it will move Motor Up to High-Level then
move motor Down to Low-Level automatically.
It will show AD value for current position and target Level and count of cycle

to tiny

@ Incline Test
1. Manual : Click “Test” to Enable Test tiny move incline Motor function, then Click “+” or
to tiny move incline Motor forward or backward
It will show AD value for current position
2. Auto : Click “Test” to Enable Test lift test function, it will move incline Motor Up to
High-Level then move incline Motor Down to Low-Level automatically.
It will show AD value for current position and target Level and count of cycle

@ Sensor Test
Click “Test” to enable test sensor, can test BT HR value, HP value, WP value and RPM.

€ ENGINEER MODE

SERVICE

Key Test 20 RESET
Maunal AD: XXXX + — TEST

Motor Test
Auto AD: XXXX L.e2o CNT:XXXXX TEST
Maunal AD: XXXX + —
Incline Test
Auto AD: XXXX Leo CNT:XXXXX
Sensor Test HRS: HP: WP: 60 RPM

30


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. Factory Setting

@ Restore Factory
Click “Clear” to restore factory.
@ First Launch
Click “ON” to set First Launch ON, then re-power ON will process First Launch UI.
@ Machine Type
See the console machine type.
@ BLENAME
Can input the new name and press SAVE then can re-name BLE device name, need re-power
on then can use phone to scan console device for new BLE name.” just for developer test

- Machine Type is XBU55 or XBR55

S ENGINEER MODE

FACTORY SETTING

Restore Factory CLEAR
First Launch ON

Machine Type @ XBU55-UpRight Bike XBR55-Recumbent Bike

BLENAME Phone's Name SAVE

31


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4. Factory Setting

@ Incline Calibration
Click “start” to calibrate incline. The incline motor will move UP till no move any more for 3~6 sec and
move Down till no move any more for 3~6 sec then finish to calibration , during calibration.

¢ ENGINEER MODE
CALIBRATION
MAX. AD: XXXX DIRECTION:
Incline Calibration
MIN. AD: XXXX CURRENT AD: XXXXX

32
