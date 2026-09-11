<!-- Source: CU1000-2023 SU8880-SB028 service manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

SERVICE MANUAL
               CU1000(2023)

              SU8880-SB028

            ENT Upright Bike




      -1-
                                                                     -Contents-
1.Outlines.....................................................................................................................................................- 4 -
2.Electronic Parts .......................................................................................................................................- 5 -

       2.1 Console .........................................................................................................................................- 5 -


       2.2 Controller and Driver parts......................................................................................................- 6 -

3.Electrical Configurations .....................................................................................................................- 7 -
4.Product Operation.................................................................................................................................- 8 -

       4.1 Window Display ..........................................................................................................................- 8 -


       4.2 Function Locations .....................................................................................................................- 8 -

5.Unit Block Diagrams..............................................................................................................................- 9 -
6.Basic Connections and Wiring........................................................................................................ - 10 -

       6.1 I/O Board Bottom .................................................................................................................... - 10 -


       6.2 Driver Board PCB Component Locations .......................................................................... - 10 -

       ............................................................................................................................................................. - 10 -

       6.3 Driver Board function ............................................................................................................. - 11 -

       ............................................................................................................................................................. - 11 -
7. Error Messages / Troubleshooting ................................................................................................. - 12 -

       7.1 Error Code List.......................................................................................................................... - 12 -

       7.2 Error code items ...................................................................................................................... - 12 -


       7.3 Tools Required ......................................................................................................................... - 12 -


       7.4 Circuit Diagram ........................................................................................................................ - 13 -

8. Setting and Operation for Engineering Mode ........................................................................... - 14 -

       8.1 Operation for entering engineering mode: ..................................................................... - 14 -


       8.2 Instructions for each item of operation in engineering mode: .................................. - 14 -

       8.3 Machine Information ............................................................................................................. - 15 -

9. Software update ................................................................................................................................ - 16 -

                                                                                  -2-
       9.1 software update manager .................................................................................................... - 16 -


       9.2 Update Firmware. .................................................................................................................... - 17 -

10. GENERAL MAINTENANCE

..................................................................................................................................................................... - 17 -

       10.1 Troubleshooting procedure Matrix .................................................................................. - 18 -

11&12. Disassembling and Assembling

..................................................................................................................................................................... - 18 -




                                                                                   -3-
1.Outlines




             -4-
2.Electronic Parts
2.1 Console




      DISPLAY




   NFC log in
       &
  Shortcut key




                     -5-
2.2 Controller and Driver parts




         SPEED SENSOR




                                        Driver board




   HYBRID GENERATOR




                                  -6-
3.Electrical Configurations
Console           Interface that controls all functions of the upright bike.
Main Controller   The circuit board consists of the DC power supply for console.
EMS Flywheel      It can change to increase or decrease resistance level of brake.




GENERAL INFORMATION
Console           Contains Key controls and TFT Display. Main controller include power supply 、driver control circuit.




                                                            -7-
4.Product Operation
4.1 Window Display




                               15.6” TFT Display




4.2 Function Locations




                         -8-
5.Unit Block Diagrams




                        -9-
6.Basic Connections and Wiring

                                                                                 USB
6.1 I/O Board Bottom
                                                                                 CONNECT


                                                         GROUND




                                        Console Power
         Internet                       CONNECT
         CONNECT




                    C-safe CONNECT (4
                                                                     HDMI CONTACT
TV CONNECT          PINS)


                                                         Key Board CONNECT (20
                                    SYSTEM CABLE
                                                         PINS)
                                    CONNECT (8 PINS)




6.2 Driver Board PCB Component Locations




                                                - 10 -
6.3 Driver Board function

                       RPM             BRAKE
    CONSOLE
                     SENSOR       FLIWHEEL      DC 24V
     POWER
                      INPUT            OUTPUT   INPUT
    OUTPUT
                                                 INPUT




        SYSTEM
         WIRE




                              - 11 -
    7. Error Messages / Troubleshooting

    7.1 Error Code List


                Code       Description
                 0xB0      EEPROM Error, By Driver Board Error
                 0xB1      Resist Error, By Driver Board Error
                 0xB2      UART Error, By Driver Board Error
                 0xB3      CMD Error, By Driver Board Error




    7.2 Error code items
Error Message                             Explain
EEPROM ERR                                EEPROM failure




    7.3 Tools Required


    A multi-meter.




                                                     - 12 -
7.4 Circuit Diagram




                      - 13 -
8. Setting and Operation for Engineering Mode
8.1 Operation for entering engineering mode:
Press “Welcome” button 10 consecutive repetitions to enter engineering mode.




8.2 Instructions for each item of operation in engineering mode:
After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the
machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection
must match the actual machine otherwise it will be unable to operate the machine properly.




                                                   - 14 -
8.3 Machine Information




                          - 15 -
9. Software update
9.1 software update manager




Image for Treadmill/ Elliptical / Bike Software Update
    First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data
                                                   - 16 -
you want to update to the USB.
Then insert the USB Transcend, click the engineering mode and update the software.


Treadmill




Elliptical/Bike




9.2 Update Firmware.
Image for Treadmill/ Elliptical / Bike Firmware Update




10. GENERAL MAINTENANCE
1. Wipe down all areas in the sweat path with a damp cloth after each workout.
2. If a squeak, thump, clicking or rough feeling develops the main cause is most likely one of two reasons:
1) The hardware was not sufficiently tightened during assembly. All bolts that were installed during
assembly need to be tightened as much as possible. It may be necessary to use a larger wrench than the
one provided if you cannot tighten the bolts sufficiently. I cannot stress this point enough; 90% of calls to
the service department for noise issues can be traced to loose hardware.
2) The crank arm nut and/or the pedals need to be retightened.
3. If squeaks or other noises persist, check that the unit is properly leveled. There are 2 leveling pads on the
bottom of the rear stabilizer, use a 14mm wrench (or adjustable wrench) to adjust the levelers.

                                                     - 17 -
WARNING
The effect that the safety level of the equipment can be maintained only if it is examined regularly for
damage and wear.
1)Replace defective components immediately and/or keep the equipment out of use until repair.
2)The components which are most susceptible to wear: Belt、PU wheel、Bearing、Idler.


10.1 Troubleshooting procedure Matrix


Condition                         Reason                                         Solve
TFT not bright, incomplete or     1. TFT light is broken.                        1. Replace with new TFT or console.
imperfect.                        2. Power to console too low.                   2. Check power to console.
                                                                                 3. Replace lower controller.
TFT displays not bright,          1. TFT displays are broken.                    1. Replace with new console.
incomplete or imperfect.

Erratic pulse display.            1. Another chest belt in use around product.   1. Check for other chest belt use around
                                  2. Other magnetic field disturbance.           product.
                                  3. Receiver is broken.                         2. Change the position or direction of
                                                                                 product.
                                                                                 3. Replace with new receiver.
Hand pulse lost its function.     1. Hands not on the hand pulse sensors or      1. Two hands hold the hand pulse.
(No pulse displayed on monitor)   only one hand on sensor.
                                  2. The connector of HANDPULSE W/WIRE           2. Connect the cable again.
                                  and Console not connected properly.
                                  3. The wires got damaged when connecting       3. Replace with new cable.
                                  the HANDPULSE W/WIRE and Console.
                                  4. Hand pulse board is broken.                 4. Replace console or Hand pulse board.
Wireless lost its function.       1. Chest belt not worn properly.               1. Check chest belt has proper contact
(No pulse displayed on monitor)                                                    with skin and is oriented correctly.
                                  2. Distance is too far and exceeds range of    2. User chest belt in front of console
                                  receiver.                                        within 3 feet.
                                                                                 3. Replace with new lithium battery type is
                                  3. Chest belt battery is weak or dead.         CR2032.
Chest belt too close to the       Weak battery.                                  Replace with new lithium battery with
product.                                                                         type CR2032.




11&12. Disassembling and Assembling
Serial Number & code Location

                                                             - 18 -
11.1 Preventative Maintenance

11.11 Check for Pedals

As shown in Figure 11.11, 11.12 , check regularly whether the pedal is loose, lock the left pedal
counterclockwise, and press the right pedal clockwise.




                                                    - 19 -
Figure 11.11                                   Figure 11.12

11.12 Check for Console Mast
As shown in Figure 11.13, check that the six screws on the riser are loose and lock if loose.
(Vertical tube shaking problem excluded)




Figure 11.13


12.1 Part Replacement Guide


12.11 Console Replacement
As shown in Figure 12.11, remove the 4 screws of the chin cover and remove it.




Figure 12.11

                                                     - 20 -
Remove the wire connector to remove the console.




Figure 12.12

Console assembly in accordance with Figure 12.11 and 12.12, you can replace.

12.12 Keyboard replacement
Remove four screws from the back of keyboard.




Figure 12.13

Refer to figure 12.14 , remove 20pin and Handpulse Wire on the keyboard to remove keyboard




Figure 12.14

Follow Figure 12.13& 12.14 to assemble it in the order of removal.


12.13 Armrest Group Replacement

Refer to Figure 12.13 and 12.14 to remove Handpulse Wire and follow Figure 12.15&12.16 to remove
front& rear chin cover screws.



                                                   - 21 -
      Figure 12.15                        Figure 12.16


Refer to Figure 12.17 to remove Socket Head Cap Bolt, Split Washer and Flat Washer to remove Armrest
Group.




Figure 12.17

Refer to Figure 12.17 to assembly back.

12.14 Pedal/Crank Arm Replacement

As shown in Figure12.18, 12.19, remove the right pedal counterclockwise and remove the left pedal
clockwise.




       Figure 12.18                Figure 12.19                    Figure 12.20




                                                   - 22 -
  Figure 12.21

Remove the crank screw as shown in Figure 12.20. (About the same, please use 60 N-m when locking)

As shown in Figure 12.21, use the puller to exit the crank. (Left and right sides are the same.)

Please refer to 12.18 ~ 12.21 for crank and pedal assembly.




12.15 Left and Right Trim Cover Replacement

As shown in Figure 12.22, Figure 12.23, remove the four self-tapping screws from the left-hand cover to
remove the left and right standings.




                    Figure 12.22                              Figure 12.23



12.16 Left and Right Chain Cover Replacement

Loose seat riser cover 3 screws as shown in Figure 12.24, Figure 12.25.


                                                     - 23 -
Figure 12.24   Figure 12.25




                              - 24 -
Figure 12.26, Figure 12.27, Figure 12.28, the left chain cover 7 self-tapping screws, 3 screws removed, you
can remove the left chain cover; the right chain cover 3 screws removed, you can remove Right chain cover.
(Please refer to step 12.14 for removing crank.)




            Figure 12.26                Figure 12.27




                    Figure 12.28


Please refer to 12.24, 12.25 for the left and right chain cover assembly.




12.17    Front and Rear Trim Cover Replacement

As shown in Figure 12.29, Figure 12.30, remove the two screws from the front and rear trims and remove
them.




                                                     - 25 -
                    Figure 12.29                               Figure 12.30

Before and after the decoration cover please refer to 12.29.




12.18    Drive System Replacement

Remove the crank, left and right riser chain cover and left and right chain cover Please refer to 12.14, 12.15,
12.16, as shown in Figure 12.31, Figure 12.32, remove the nut and hook screw, you can remove the spring.




                    Figure 12.31                               Figure 12.32

Draw the belt as shown in Figure 12.33, Figure 12.34. (The belt is maintained in the middle of the belt
during installation, the belt tension is maintained at 180 to 210 N)




                    Figure 12.33                               Figure 12.34


As shown in Figure 12.35, loosen the three screws and remove the idler. (The need to install the idler
counterclockwise to the end of the lock)




                                                     - 26 -
                   Figure 12.35

As shown in Figure 12.36, 12.37, the flywheel 4 screws can be removed to remove the flywheel.




                   Figure 12.36                              Figure 12.37



As shown in Figure 12.38, loosen the five-way nut and remove the five-way turntable. (Need to align the
keyway in the installation, the five-nut on the lock.)




                   Figure 12.38

As shown in Figure 12.39, loosen the reed switch screw and remove it. (Installation with the belt on the
magnet with a distance of 1mm)




                                                    - 27 -
                    Figure 12.39


Please refer to 12.31 ~ 12.36 for the installation of transmission system parts.


12.19    Chair Cushions Cover、Seat Button Replacement

As shown in Figure 12.40, Figure 12.41, remove the 2 screws from the front and rear seats.




          Figure 12.40




            Figure 12.41


As shown in Figure 12.42, Figure 12.43, remove the four screws and remove the cushion.

                                                     - 28 -
     Figure 12.42




  Figure 12.43


Please refer to 12.41 for the cushion assembly.

Please refer to 12.40 for the front and rear seat cover assembly.


12.20   Lift Arm Group Replacement

Set the seat adjustment group to the highest as shown in Figure 12.44.




                                                    - 29 -
Figure 12.44

Remove the carriage cable as shown in Figure 12.45, 12.46, 12.47.




  Figure 12.45                          Figure 12.46




  Figure 12.47

As shown in Figure 12.48 ~ 12.52 will be on the handle of the two screws, you can remove the cable,
handle.




  Figure 12.48                           Figure 12.49




                                                   - 30 -
Figure 12.50




Figure 12.51   Figure 12.52




                       - 31 -
As shown in Figure 12.53, 12.54, 12.55, 12.56. Remove the screw and nut from the lifting arm to remove
the seat riser.




Figure 12.53                           Figure 12.54




Figure 12.55




Figure 12.56




                                                  - 32 -
As shown in Figure 12.57, 12.58 remove the cap on the lift arm, you can remove the lift arm.




                    Figure 12.57                               Figure 12.58

Install the seat riser group Refer to 12.44 ~ 12.48



12.21 Down Control Replacement

As shown in Figure 12.59, remove the four screws from the control panel and release the power to remove
the replacement.




  Figure 12.59




                                                      - 33 -
12.22   Rear Horizontal Tube Replacement

As shown in Figure 12.60, 12.61 loosen the bottom 3 screws and remove it.




                   Figure 12.60                            Figure 12.61




12.23   Foot Pad/Moving Wheel Replacement

As shown in Figure 12.62, loosen the screw and cap and remove the wheel.




                   Figure 12.62




                                                  - 34 -
As shown in Figure 12.63, move the wheel counterclockwise. (Adjust the height of the four feet when not
flat until the balance)




  Figure 12.63




                                                  - 35 -


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 71 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-Contents-

TL OUTINGS... cece ccceeeccsseescsseeseesecseesecsessecnsssecsaeesesaecseaecaessecsassecsaeeaesaecseaecaessecaaseeceasesesaecseeaecaesaesaaseneaaees -4-
QZ.EIO@CHOMIC PITS ...........ceeceseesceseescesecseesecseesecseeseceseescsaecsessecsessecaesseceaeeseesecsessecseseeseaseceaeesessecaesaesaeseeaeees -5-
2.1 CONSOLE wo.cecccccccccccscsesesesssscscscscsessssvsssesesesssesasscsesessvassssssssesesassesesssasasassesesesesasscsesasasacsesesesesecaeseneees -5-
2.2 Controller ANd Driver Parts.........cccccceecesecsesesesceeseeesesesescseeeseeceeeeceesesesesesaeaeseeeeteeseeeneneneneass -6-
3. Electrical COMPIQUIATIONS ...0..... ee c ee cceteesceseeseesecseesecseesecaseseceseceesaecaessecsecsecseseseaeeesaecaesaesaeseessaseeeees -7-
vd oXe [ULo4 ©) ol) co] | (0) s ee eee -8-
4.1 WINdOW DISPLAY... eee sesssesseseesesesesneseeeesesesueneesescaesusneeeseassnsucseseeesansneaeeteesaesnsneeteecateneaeeteeeatey -8-
4.2 FUNCTION LOCATIONS.........cccecccscscscsssesssssscsesesesecesecscsesessssssssesesesesassesesesasasacsesecesesacacsesssacacseseeeeesees -8-
5. Unit BlOCK DiC Gras. .......... ee ccccccccssssecsseseceeeecesecseesecsessecsesseceeeeceaeeseaecaessecaeseessaseseaeceesaecaeeaesaeseeneees -9-
6.Basic CONNECTIONS AN, WITING. 0.00.00... ccceccsseecceseesceseeseesecsessecsessecesececeaecsessecseseecaeseesaeeseeaeeaeeaeeas -10-
6.1 1/O Board BottOM.....cccccccccccssscsesesssecscscscscsesssscscsesesesesesacscsesssavassesesesesescacscsesessacssseseeesesacas -10-
6.2 Driver Board PCB Component LOCATIONS. ...........ecceeeesesecseseseseeeeseseseseseeseaceeeeeteeseeaeatsnseeees -10-
Leen cece cece nea eeeeeEEEEGEAEAAA AA EEEEEEGEAEAAAAAAEEEEESEAEEAAAAEEEEEESEAEAAAAAAAEEEEEEESEEEAAIASSEELEEESEA;AAA ASSES EEESEA;EAE GASSES EE ESCA EEEE AES EEEEEES -10-
6.3 Driver Board FUNCON cc ccccccccceseeesesesesesesesesescscsesesesescscsesesescscsescscscscscscscscsesesescstscsescseans -11-
Leen cece cece nea eeeeeEEEEGEAEAAA AA EEEEEEGEAEAAAAAAEEEEESEAEEAAAAEEEEEESEAEAAAAAAAEEEEEEESEEEAAIASSEELEEESEA;AAA ASSES EEESEA;EAE GASSES EE ESCA EEEE AES EEEEEES -11-
7. Error Messages / TroUDICSHOOTING...............cccecceccesesseesecseesecseeecseececaecaeesecseseecaeseeceaeeeseaesaeeaeeaeeats -12-
7.1 Error Code LiSt......cccccccccccscscscscsssscsesesssescscscscsessssvassescsesesesasscsesssavasasassesesesascscsesessvacasseseeesesacas -12-
7.2 Error COG itOMS .....ccecccccccscscscsesssscsesesesesesccscscsessssvsssesesesesesesscsesssavasassesesesesacscsesesavacasaeseeesesaeas -12-
7.3 TOONS REQUIPOC 00.0... eceeeecesesesseseseseseeeesesesesesseseseseeseseuescaeaessusseacaceeeteueecaeaesesueneaceeeeetesecasanenseeeees -12-
TA Circuit Dia Qraim i eesessesessessesscseesesssssnescesesssssneneeseeesesnsneeeeecsesusseeesecaesusaeeeeecassusaeeteeasaneneeees - 13 -
8. Setting and Operation for Engineering Mode ...........ccccccccsseeccsseesceseesseecseeeeceseeceseeeeeseeaeeaeens -14-
8.1 Operation for entering ENGINEELFING MOE? ........eecsesesecseeseeseeeeseeseeeeseeseeeeneeneeeeaeeneetentens -14-
8.2 Instructions for each item of operation in engineering MOdE?%......... cece -14-
8.3 Machine INFOrmation .......cccccccccscssssssssessseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseeeseeeseeeees -15-
9. SOFTWALE UPCAFE 00... ec ccccecsceeesessesseesecseesecssesecsaecseesecsessecsessecseseeseaecsseaecaeseecaeseeseaseeseaesaeeaesaeeats -16-


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9.1 Software UPCate MANAGED ........ceseseesesseseeseeeesesseeeesesseeeesesneeeesesueeesessusseeecseeneeessesneeeeataneeteatens -16-
9.2 Update Firmware. .........cccccccecesessesesesesseesscsesesesececscseseeeeseseseaesnsususacaeseeeeeeusacaeansessneaeeeeeeeeeeeeatans -17-
10. GENERAL MAINTENANCE
EEE EEE EE ESET ESSE SOOO EE ESETSSESS ESS S OOO ETESOSES SSS SOOO OT ESSSOSESS SOOO OOOTESOSESE SSS SOSOSESCSOSESSS SOOO OSOSSTSSSSSSSS SSS SSTSSSTESTSSSSS -17-
10.1 Troubleshooting procedure Matrix... eccseesseeeseessseseeseeasseseeseeasseneetesiseneeeeeeens -18-
11&12. Disassembling and Assembling
EEE EEE EE ESET ESSE SOOO EE ESETSSESS ESS S OOO ETESOSES SSS SOOO OT ESSSOSESS SOOO OOOTESOSESE SSS SOSOSESCSOSESSS SOOO OSOSSTSSSSSSSS SSS SSTSSSTESTSSSSS -18-


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 45 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-v-

HBAS] aseajay
elBPped
HBAOD yeas Jeay
HBAOD EIS JUoI4
HapjoyH ebeiaacag
ca|Npo- I!40999/5
HBAOD ISB BJOSUDD
eYABAOD SEW BJOSuOD
oe TIBA0D ISB BJOSuOD
edeg
HMBAOD JEZIIGEIS Jeay
HMBAOD JEZIIGEIS UCI
o(y) SBD Japis
o(7) aseQ apis
rIBSYISAOD UIYD ajosuoD
(JUOJ4) JAAOD UIUD ajosuoD
opaeoghay
edeg pug
(WOYOGNSAOD Usa!DS

(do | J8A0D UaaIDS

euogdipsap = WA}

SOUILINO'L


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SuO!}ed07 UOI}DUNY Z'y

JSBODIIM

Aeidsiq 141 .9°Sk

ISOC

Ke\dsiq MOpUIM Ly
UOHDISdO JONPOld'y


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.Unit Block Diagrams

DISPLAY CONSOLE«
A A * A A A A
SYSTEM Console Power
HDMI C-safe TV Internet
ae cre PP CONNECT CONNECT* |} CONNECT~ }]} CONNECT |] CONNECT:
CONNECTING BOARD:
KEY«
DRIVER BOARD<« CONNECTING:
BOARD#
t ft fF 7
DC Brake: RPM Handlebar:

POWER4 | Flywheel] | SENSOR


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 33 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-IT-

EQ Pe
ree we

0-Av6 OATO<GD>

9 (ama) teay (OS

y Stelios) &

- S O° 404
ies 6CLO9SSD

LNdLno LNdLno

7SS5HMI14 YOSNSAS YSMOd

SyVYHa Wdd AIOSNOD

UO!}IUN} PALO JOA €°9

oO +e

a 6<cLOoSsSsso

iNWUG-BUW SESE > Md HL ‘$2 .


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 49 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7.4 Circuit Diagram

SU8880-SB028 230V
Upright Bike CIRCUIT DIAGRAM

RJ45 INTERNET ©

TVRFCABLE
C-SAVE ©

HDMI @&————_

6-PIN MAIN CONTROL WIRES
Oo
AC POWER INPUT — —
\_fL i
PLUG
TFT POWER
Ns) a (] INPUT
[we] FIEIBGe
Power cable
4-PIN XHP 3-PIN XHP
Connector
100W Power Adapter Holding heartbeat
OUTPUT
DC 24V/5A
DC JACK
a — ©
INPUT POWER OUT TO
pe2avisa L__] U TFT POWER
CONTROLLER _ 6-PIN MAIN CONTROL WIRES

M+ JK
0 Communication transfer board

HDMI
RJ45 TV RF
INTERNET CABLE C-SAFE

|

2-PIN

SENSOR WIRE

-13-


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8. Setting and Operation for Engineering Mode

8.1 Operation for entering engineering mode:

Press “Welcome” button 10 consecutive repetitions to enter engineering mode.

Maintenance Mode

Abed Thee Machine Pepterens ee

8.2 Instructions for each item of operation in engineering mode:

After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the
machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection
must match the actual machine otherwise it will be unable to operate the machine properly.

Maintenance Mode

About This Machine Preferences Machine Setup Service

Upright Bike +

Reset Odometer 5 I

Display Brightness

 @

-14-


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 119 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.3 Machine Information

About This Machine Introduction e

Typee There are three modes for the Machine Type Treadmill/ Elliptical/ Upright |,
Bike/Recumbent Bike. «
Please select for the machine. The selection must match the actual machine
otherwise it will be unable to operate the machine properly.e

Preferences Introduction fe

Beepe ON/ OFF for beep sound modee ‘

Pause Modee ON/OFF Pause Time Mode. (Minutes : Seconds) ‘

Sleep Modee ON/OFF for sleep mode The display always lights when tums off. When |,
there is no action for 15 minutes after turning on the power, it enters sleep
mode.

Workout Time Limite ON/OFF set limit machine usage timee ,

Machine Setup Introduction ,

Club Informatione Information or promotional display provided by the clube ‘

Languages To set default language for the first page window. There are 12 languages in |,
the menu.e¢

Date & Times Set console time system.¢ ,

Unitse English/Metric mode switching.¢ ,

Videos STB / TV / None mode switching ,

Protocole Select “C-SAFE or CAB" button for TV switching box + ‘
(Choose one is allowed only).¢

WiFie Please hit WiFi button to proceed WiFi setting.-

Softwaree 1. Please keep wired network or connect to wifi network to update software |.

automatically~
2. USB update as followse
Firmwaree 1. Please keep wired network or connect to wifi network to update software |.
automatically~
2. USB update as followse
App Manager- Please keep a wired network or connect to a wifi network to automatically |.
update the app software.e

-15-


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 71 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Service Introduction ‘

Key Teste Press the "button" to start calibration « ‘
The corresponding screen display of the physical button flashes.
NFC Teste Please correspond to the location of the NFC sensor, and when the sensor |:
is detected, the information will be displayed on the screene
Communication Teste Perform hardware tests such as RS232 or USB+ ‘

(If testing, please contact the relevant personnel or maintenance personnel)q

Brake Teste Resistance output test ;
(If testing, please contact the relevant personnel or maintenance personnel)«

Sensor Tests- Test that the sensor is working+ ,
(If testing, please contact the relevant personnel or maintenance personnel)«

Error Code Loge Diagnose and save malfunction error messages for technician to inspect the |,
machine and troubleshooting Press “Error Code Log” button 10
consecutive repetitions to clear the error messagee

9. Software update

9.1 software update manager

Software Done v

Automatic Update  ]
TFT OS

LWR

Software Update

Image for Treadmill/ Elliptical / Bike Software Update

First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data
-16-


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-VC-

S@'7T eunsi4 v2‘7T eun3i4


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-TE-

7ST aunsl4 TST aunsl4

0S°ZT aunsi4
