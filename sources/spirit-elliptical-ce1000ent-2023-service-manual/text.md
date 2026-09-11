<!-- Source: CE1000-2023 SE8880-SB028 service manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

SERVICE MANUAL
            CE1000(2023)

            SE8880-SB028

             ENT Elliptical




      -1-
                                                                   -Contents-
1.Outlines.....................................................................................................................................................- 4 -
2.Electronic Parts .......................................................................................................................................- 5 -

       2.1 Console .........................................................................................................................................- 5 -


       2.2 Controller and Driver parts ......................................................................................................- 6 -

3.Electrical Configurations .....................................................................................................................- 7 -
4.Product Operation.................................................................................................................................- 8 -

       4.1 Window Display ..........................................................................................................................- 8 -


       4.2 Function Locations .....................................................................................................................- 8 -

6.Basic Connections and Wiring........................................................................................................ - 10 -

       6.1 I/O Board Bottom .................................................................................................................... - 10 -


       6.2 Driver Board PCB Component Locations .......................................................................... - 10 -


       6.3 Driver Board function ............................................................................................................. - 11 -

7. Error Messages / Troubleshooting ................................................................................................. - 12 -

       7.1 Error Code List.......................................................................................................................... - 12 -


       7.2 Error code items ...................................................................................................................... - 12 -

       7.3 Tools Required ......................................................................................................................... - 12 -


       7.4 Circuit Diagram ........................................................................................................................ - 13 -

8. Setting and Operation for Engineering Mode ........................................................................... - 14 -

       8.1 Operation for entering engineering mode: ..................................................................... - 14 -


       8.2 Instructions for each item of operation in engineering mode: .................................. - 15 -


       8.3 Machine Information ............................................................................................................. - 16 -

9. Software update ................................................................................................................................ - 17 -

       9.1 software update manager .................................................................................................... - 17 -


       9.2 Update Firmware. .................................................................................................................... - 18 -

                                                                               -2-
10. GENERAL MAINTENANCE

..................................................................................................................................................................... - 18 -

       10.1 Troubleshooting procedure Matrix .................................................................................. - 19 -

11&12. Disassembling and Assembling

..................................................................................................................................................................... - 19 -

       11.1 Part Replacement Guide ..................................................................................................... - 20 -

13. Troubleshooting

..................................................................................................................................................................... - 32 -

       13.1 Belt Slips/Falls off .................................................................................................................. - 32 -


       13.2 Noise and Feet Feeling........................................................................................................ - 32 -




                                                                                   -3-
1.Outlines




  Item                 Description             Required Q’ty
         1.             Console                     1
         2.     Console Chin Cover (Front)          1
         3.     Console Chin Cover (Rear)           1
         4.        Drink Bottle Holder              1
         5.      Console Mast Cover (L)             1
         6.      Console Mast Cover (R)             1
         7.           Side Case (L)                 1
         8.           Side Case (R)                 1
         9.         Side Case Plate (L)             1
         10.        Side Case Plate (R)             1
         11.   Console Mast Inner Cover (L)         1
         12.   Console Mast Inner Cover (R)         1
         13.           Front Shroud                 1
         14.       Power Switch Cover               1

                                              -4-
      15.       Handle Bar Cover            2
      16.           Cover (L)               1
      17.           Cover (R)               1
      18.           Pedal (L)               1
      19.           Pedal (R)               1
      20.     Pedal Arm Cover A (L)         1
      21.     Pedal Arm Cover B (L)         1
      22.     Pedal Arm Cover A (R)         1
      23.     Pedal Arm Cover B (R)         1
      24.         Rear Shroud               2
      25.      Slide Wheel Cover A          1
      26.      Slide Wheel Cover B          2
      27.             Cap                   6
      28.          TVC Cover                1




2.Electronic Parts
2.1 Console




                                                DISPLAY



                                                  NFC log in
                                                       &
                                                  Shortcut key




                                      -5-
 2.2 Controller and Driver parts




HYBRID GENERATOR                         SPEED SENSOR




  Driver board




                                   -6-
3.Electrical Configurations
Console           Interface that controls all functions of the elliptical.
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

  6.1 I/O Board Bottom


                                                                         USB
                                                           GROUND        CONNECT



                                        Console Power
             Internet
                                        CONNECT
             CONNECT




                                                                         HDMI CONNECT

                    C-safe CONNECT (4
TV CONNECT
                    PINS)



                                        SYSTEM CABLE
                                                             Key Board CONNECT
                                        CONNECT (8 PINS)
                                                             (20 PINS)




  6.2 Driver Board PCB Component Locations




                                                  - 10 -
6.3 Driver Board function

                                    BRAKE
           CONSOLE          RPM
                                  FLIWHEEL   DC 24V
           POWER       SENSOR
                                   OUTPUT    INPUT
           OUTPUT       INPUT




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




                                                 - 14 -
8.2 Instructions for each item of operation in engineering mode:
After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the
machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection
must match the actual machine otherwise it will be unable to operate the machine properly.




                                                   - 15 -
8.3 Machine Information




                          - 16 -
9. Software update
9.1 software update manager




Image for Treadmill/ Elliptical / Bike Software Update
    First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data
you want to update to the USB.
                                                   - 17 -
Then insert the USB Transcend, click the engineering mode and update the software.


Treadmill




Elliptical/Bike




9.2 Update Firmware.
Image for Treadmill/ Elliptical / Bike Firmware Update




10. GENERAL MAINTENANCE
1. Wipe down all areas in the sweat path with a damp cloth after each workout.
2. If a squeak, thump, clicking or rough feeling develops the main cause is most likely one of two reasons:
1)The hardware was not sufficiently tightened during assembly. All bolts that were installed during
assembly need to be tightened as much as possible. It may be necessary to use a larger wrench than the
one provided if you cannot tighten the bolts sufficiently. I cannot stress this point enough; 90% of calls to
the service department for noise issues can be traced to loose hardware.
2)The crank arm nut and/or the pedals need to be retightened.
3.If squeaks or other noises persist, check that the unit is properly leveled. There are 2 leveling pads on the
bottom of the rear stabilizer, use a 14mm wrench (or adjustable wrench) to adjust the levelers.

WARNING
The effect that the safety level of the equipment can be maintained only if it is examined regularly for
                                                     - 18 -
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
Serial Number Location



                                                             - 19 -
11.1 Part Replacement Guide

11.11 Console Replacement
Show on Figure 11.11、Figure 11.12 Unbolt the Console-mast tube cover by removing those 2 screws.




    Figure 11.11                                          Figure 11.12



Unbolt the console by removing the 4 screws and disconnecting connectors to PCB.




                                                 - 20 -
       Figure 11.13                                            Figure 11.14

Unbolt the Keyboard by removing the 4 screws and disconnecting connectors to Keyboard.




            Figure 11.15                                           Figure 11.16

You can reinstall the console back by reverse the processes of 11.11 until 11.16

11.21 Handlebar Left/Right Replacement
As shown in Figure 11.21 and Figure 11.22, remove the swing cover, and then M10x60L (2pcs) and
M10x55L (1pc) screws removed, you can remove the armrest.




          Figure11.21                                Figure11.22

Reassembly handlebar by reversing the process 11.21.

11.31 Console Mast Cover Left/Right Replacement
As shown in Figure 11.31 and Figure11.32, remove the M5 screws (2pcs) on both sides after removing the
rear tapping screws (2pcs) from the riser cover.

                                                    - 21 -
    Figure11.31                               Figure11.32

Assembly Console Mast Cover by reversing the process 11.31

11.41 Front Cover Replacement
As shown in Figure 11.41, remove the front chain cover by removing the M5 screw (2pcs).




    Figure11.41

11.51 Power Cover Replacement
As shown in Figure 11.51, remove the M5 screw (2pcs) and remove the power cover.




Figure11.51

11.61 Left/Right Main Cover Replacement
As shown in Figure 11.61, Figure 11.62 and Figure 11.63, remove the M5 screw (8pcs) and remove the left
                                                  - 22 -
and right chain cover.




       Figure 11.61                      Figure 11.62                                   Figure 11.63

11.71 Crank Arm Replacement
As shown in Figure 11.71, remove M10x60L screws (1pc) and M10x15L screws (1pc), and then you can
remove and replace the crank.




Figure 11.71

As shown in Figure 11.72, remove the crank screw. (Please use 100 N-m when locking. Right side and left
side are the same.)




Figure 11.72

Please refer to process 11.71 for crank and pedal assembly.

                                                   - 23 -
11.81 Swing Arm Replacement
As shown in Figure 11.81 and Figure 11.82, remove the screw (1pc) that locks on the swing tube.




              Figure 11.81                           Figure 11.82


As shown in Figure 11.83 to Figure 11.85, remove the foot rod group of fish-eye bearings, you can
successfully remove the swing tube replacement.




         Figure 11.83                      Figure 11.84                      Figure 11.85

11.91 Pedal Arm and Right & Left Outer Replacement

As shown in Figure 11.91 to Figure 11.93, remove the screw (1pc) attached to the connecting rod and the
bearing bushings and refer to Figure 11.83-11.85 to remove the foot link.




         Figure 11.91                      Figure 11.92                      Figure 11.93

As shown in Figure 11.94, remove the M5 screws (6pcs) and replace plastic cover of the foot pedal.




                                                   - 24 -
  Figure 11.94

As shown in Figure 11.95 to Figure11.97, replace the screws (8pcs) with the cover A, B and the rear foot
pedal attached to the foot pedal.




            Figure 11.95                   Figure 11.96                   Figure 11.97

12.11 Pedal Arm and Right & Left Inner Replacement

As shown in Figure 12.11, replace the M5 screw (2pcs) attached to the connecting rod cover and replace it.




Figure 12.11

As shown in Figure 12.12 to Figure 12.16, use the tool to open the sun's wrench's tension and then remove
the Sun and the nuts and see Figure 11.91 to Figure 11.93 to replace the shaft connecting rod.




                                                   - 25 -
            Figure 12.12                Figure 12.13                Figure 12.14




          Figure 12.15                         Figure 12.16


12.21 Poly-V Drive Belt, EM Flywheel and Idler Wheel Bracket Replacement

Refer to Procedure 11.61, Procedure 11.71 and Procedure 12.11 to remove the crank and the left and right
chain cover and the shaft connecting rod. As shown in Figure 12.21 and 12.22, remove the nut and hook
type screws.




            Figure 12.21                                 Figure 12.22

Remove the belt as shown in Figure 12.23 (When the belt is installed in the middle of the belt, belt tension
maintained at 280 ~ 310N)




                                                    - 26 -
Figure 12.23

As shown in Figure 12.24, press the roller (3pcs) when the roller is locked to the flywheel. (Refer to Figure
12.21 to Figure 12.23 to disassembly belt.)




Figure 12.24

As shown in Figure 12.25, the flywheel 4 screws can be removed to remove the flywheel.




Figure 12.25

Please refer to Procedure 12.21 to Procedure 12.24 for the installation of drive system parts.

As shown in Figure 12.26 to Figure 12.27, loosen the reed switch screw and remove it. (Installation with the
belt on the magnet with a distance of 2mm)




           Figure 12.26                        Figure 12.27


Please refer to Procedure 12.21 for the installation of transmission system parts.


                                                     - 27 -
12.31 Lower Control Board Replacement

As shown in Figure 12.31 and Figure 12.32, remove the plastic column, and then you can remove the
control board.




  Figure 12.31                          Figure 12.32


12.41 Main Roller Replacement

As shown in Figure 12.41, loosen the M5 screw (3pcs) to remove the left and right side of the carriage base
cover B.




Figure 12.41

As shown in Figure 12.42, loosen the M5 screw (3pcs) to remove the carriage base cover A.




                                                   - 28 -
Figure 12.42

As shown in Figure 12.43, remove the M8 screw (4pcs) by using the tool to remove the slide guard.




Figure 12.43

As shown in Figure 12.44 and Figure 12.45, the screws M10 (6pcs) on both sides are released and the slide
wheel group can be removed and replaced.




               Figure 12.44                       Figure 12.45


12.51 Roller Track Plate Replacement

As shown in Figure 12.51, replace the aluminum rail with the M6 screw (6pcs) attached to the aluminum
rail.




Figure 12.51

                                                   - 29 -
12.61 Console Mast Replacement

As shown in Figure 12.61 and Figure 12.62, remove the M10 screws (4pcs) on both sides, then remove the
standpipe and remove the electronic watch before removing the riser.




   Figure 12.61                                      Figure 12.62

12.71 Handle Bar Mounting Bracket Replacement

As shown in Figure 12.71, remove the M10 screws (4pcs) on both sides to remove the heartbeat bracket.
Refer to Procedure 11.11 to remove the electronic watch before dismantling.




Figure 12.71

12.81 Handle Bar, Center Replacement

As shown in Figure 12.81, the self-tapping screw (2pcs) will be locked on the cup holder and the cup holder
can be replaced after loosening.




Figure 12.81
                                                   - 30 -
As shown in Figure 12.82, Figure 12.83, use the tool to release the heartbeat handle, as shown in Figure
12.83. Refer to Figure 12.81 and Figure 12.71.




   Figure 12.82                                             Figure 12.83

12.91 Leveling Foot and Transport Wheel Replacement

As shown in Figure 12.91, remove the screw and cap and remove the wheel.




Figure 12.91

As shown in Figure 12.92, move the wheel counterclockwise. (Adjust the height of the four feet when not
flat until the balance.)




Figure 12.92
                                                   - 31 -
13. Troubleshooting
13.1 Belt Slips/Falls off

If the belt is found to slip and fall off, please refer to Procedure 12.21, the tension of the pressure roller can
be adjusted to adjust the tension, belt tension maintained at 280 ~ 310N.




             Figure 13.1




13.2 Noise and Feet Feeling

If there is a sense of graininess, such as re-treading, such as the use of the bearing is the roller is not the
general ball, so give the operation will feel the same, this is normal.

Where there is a lot of abnormal sound, it is not easy to detect, from the fish eye axis and the fish eye
bearing (Figure 13.21 ) in the operation touch, the most important reason is the lack of lubrication or
rotation is not smooth or Loose screws, because the machine itself is linked to the structure of the way, it
must be in accordance with the actual situation to deal with the machine.




     Figure 13.21

The surface of the sliding wheel group is kept clean and can be dusted for a long period of time, need
regular maintenance and cleaning, and can maintain wheel life. (Refer to Procedure 12.41 for the removal
                                                       - 32 -
of the sliding wheel base cover A, B and the slide guard)




      Figure 13.22

As shown in Figure 13.23, regularly clean the aluminum rails to extend the service life. (It is recommended
to use alcohol to remove the dust attached to the aluminum rail.)




     Figure 13.23




                                                    - 33 -
Shaking

As shown in Figure 13.3, check whether the handle is loose and shake. Please loosen the screw if it is loose.
(See Procedure 11.21 for disassembly wobbles cover.)




      Figure 13.3




                                                    - 34 -


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jeondijj4 INI
8Z09S-08884S

(€Z0Z)O000L4D

TWANVIAW SAQDIAMdSAS


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 60 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-Contents-

TL OUTINGS... cece ccceeeccsseescsseeseesecseesecsessecnsssecsaeesesaecseaecaessecsassecsaeeaesaecseaecaessecaaseeceasesesaecseeaecaesaesaaseneaaees -4-
QZ.EIO@CHOMIC PITS ...........ceeceseesceseescesecseesecseesecseeseceseescsaecsessecsessecaesseceaeeseesecsessecseseeseaseceaeesessecaesaesaeseeaeees -5-
2.1 CONSOLE wo.cecccccccccccscsesesesssscscscscsessssvsssesesesssesasscsesessvassssssssesesassesesssasasassesesesesasscsesasasacsesesesesecaeseneees -5-
2.2 Controller ANd Driver Parts ..........ccccccceesesesseseseseeeseeeseseseseeseeeeeececeeeesesesesesaeaeseeeeeseseeeensneneneass -6-
3. Electrical COMPIQUIATIONS ...0..... ee c ee cceteesceseeseesecseesecseesecaseseceseceesaecaessecsecsecseseseaeeesaecaesaesaeseessaseeeees -7-
vd oXe [ULo4 ©) ol) co] | (0) s ee eee -8-
4.1 WINdOW DISPLAY... eee sesssesseseesesesesneseeeesesesueneesescaesusneeeseassnsucseseeesansneaeeteesaesnsneeteecateneaeeteeeatey -8-
4.2 FUNCTION LOCATIONS.........cccecccscscscsssesssssscsesesesecesecscsesessssssssesesesesassesesesasasacsesecesesacacsesssacacseseeeeesees -8-
6.Basic CONNECTIONS AN WITIING. 0.0.0.0... ccceccsseeccsseescesesseesecsecsecsesseceaececaecsessesseseecaeseseaeeeesaesaeeaeeas -10-
6.1 1/O Board BottOM.....cccccccccccssscsesesssecscscscscsesssscscsesesesesesacscsesssavassesesesesescacscsesessacssseseeesesacas -10-
6.2 Driver Board PCB Component LOCATIONS. ...........ecceeeesesecseseseseeeeseseseseseeseaceeeeeteeseeaeatsnseeees -10-
6.3 Driver Board FUNCON cc ccccccccceseeesesesesesesesesescscsesesesescscsesesescscsescscscscscscscscsesesescstscsescseans -11-
7. Error Messages / TroUDICSHOOTING...............cccecceccesesseesecseesecseeecseececaecaeesecseseecaeseeceaeeeseaesaeeaeeaeeats -12-
7.1 Error Code LiSt......cccccccccccscscscscsssscsesesssescscscscsessssvassescsesesesasscsesssavasasassesesesascscsesessvacasseseeesesacas -12-
7.2 Error COE itOMS w....cccccccccccscscsssssscsesesesesecccscscsessssvavsesesesesesesscsesssavasassesesesesasscsesesavacasseseeesesacas -12-
7.3 TOOIS REQUIFEC 00.0... eseeeecesesessesesesesessesesesesesueseseseesesesescaesesususscacaeeeeesescaeaesesueneaceceeeteeeesatansesenees -12-
TA Circuit Dia Grain ........eeececcesesecscseseseeeeesseseseseseescseseeeseseseseaesesusneacseeeeceueecaeaesesuseeaceeeeeteeeesaeanseseeeees -13-
8. Setting and Operation for Engineering Mode ...........ccccccccsseeccsseesceseesseecseeeeceseeceseeeeeseeaeeaeens -14-
8.1 Operation for entering ENGINEELFING MOE? ........eecsesesecseeseeseeeeseeseeeeseeseeeeneeneeeeaeeneetentens -14-
8.2 Instructions for each item of operation in engineering MOAE?....... eset -15-
8.3 Machine INFOrmation .......cccccccccscssssssssessseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseeeseeeseeeees - 16 -
9. SOFTWALE UPCAFE 00... ec ccccecsceeesessesseesecseesecssesecsaecseesecsessecsessecseseeseaecsseaecaeseecaeseeseaseeseaesaeeaesaeeats -17-
9.1 Software UPCate MANAGED 0... seeeseesesseseeseeeeseeseeeesessceeesesneeeesesueeesessusaeeecsesneeecaeeneeeeataneetentens -17-
9.2 Update Firmware. .........cccccccecesessesesesesseesscsesesesececscseseeeeseseseaesnsususacaeseeeeeeusacaeansessneaeeeeeeeeeeeeatans - 18 -

-2-


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
1.Outlines

2
3
9. (6)
15
13
14
28
7
9. (10)
imal If 12 26
Item Description Required Q’ty
1. Console 1
2. Console Chin Cover (Front) 1
3. Console Chin Cover (Rear) 1
4. Drink Bottle Holder 1
5. Console Mast Cover (L) 1
6. Console Mast Cover (R) 1
7. Side Case (L) 1
8. Side Case (R) 1
9. Side Case Plate (L) 1
10. Side Case Plate (R) 1
11. Console Mast Inner Cover (L) 1
12. Console Mast Inner Cover (R) 1
13. Front Shroud 1
14. Power Switch Cover 1

a

-


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SUuOI}EIO] UO!PUNY Z'7

ele

Aeidsiq 141 .9°Sk

Ae|dsiq MopulM L'7
UOHNDISdO JONPOld'p


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.Unit Block Diagrams

DISPLAY CONSOLE»

SYSTEM Console Power. 1 nial C-safe TV Internet
connect, || CONNECT. CONNECT. || connecTe || connect. || connect.
CONNECTING BOARD+
KEY.
DRIVER BOARDe CONNECTING.
BOARD.
t t t HRs
DCs Brakew RPM + Handlebar+

POWER | Flywheel SENSOR+


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Sit 1)
a(t 1)

= (7-7) aor

ooLJe~ 31 (et R26 4 arm sali Carmors 1
at | rahe 3 2 7 4 nds i 127 is
ez ‘ f =2
J ee : : 2 .- (tsi, ee
C30 my y — «

| MW
Ci6 Ri4” RIZCIS fas
tyme) (ieee fa fn)

waa


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 54 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7.4 Circuit Diagram

SE8880-SB028 230V
Elliptical CIRCUIT DIAGRAM

RJ45 INTERNET ©

TVRFCABLE GQ———————___,
CSAVE ©

ALM)

6-PIN MAIN CONTROL WIRES
fo
AC POWER INPUT ——h a
os 7
PLUG
is} TFT POWER
ae. {] INPUT
[vee] F=I=]Aa
Power cable
4-PIN XHP 3-PIN XHP
Connector
100W Power Adapter Holding heartbeat
OUTPUT
DC 24V /5A
Dc JACK
——— ©
INPUT POWER OUT TO
pe2avisa [___]| UJ TFT POWER
6PIN MAIN CONTROL WIRES
CONTROLLER |=

M+ JK
i Communication transfer board

HDMI
RJ45. TV RF
INTERNET CABLE  C-SAFE

Ld

2-PIN

SENSOR WIRE

-13-


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.2 Instructions for each item of operation in engineering mode:

After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the
machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection
must match the actual machine otherwise it will be unable to operate the machine properly.

Maintenance Mode

About This Machine Preferences Machine Setup Service

Display Brightness

-15-


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 115 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.3 Machine Information

| About This Machine Introduction»
Typee There are three modes for the Machine Type Treadmill/ Elliptical/ Upright |,
Bike/Recumbent Bike. +
Please select for the machine. The selection must match the actual machine
otherwise it will be unable to operate the machine properly.¢
|Preferencess Introductions

Beepe ON/ OFF for beep sound modee ‘

Pause Modee ON/OFF Pause Time Mode (Minutes : Seconds) ;

Sleep Modee ON/OFF for sleep mode The display always lights when turns off. When |,
there is no action for 15 minutes after turning on the power, it enters sleep
mode.¢

Workout Time Limite ON/OFF set limit machine usage timee ,

4

Machine Setup Introduction

Languagee To set default language for the first page window. There are 12 languages in |,
the menu.¢
Date & Timee Set console time system. |
Unitse English/Metric mode switching.+ ,
Videoe STB / TV/ None mode switchinge ,
Protocole Select “C-SAFE or CAB" button for TV switching box (Choose one is allowed |,
only).¢
WiFie Please hit WiFi button to proceed WiFi setting.
Softwaree 1. Please keep wired network or connect to wifi network to update software |,
automatically
2. USB update as followse
Firmwaree 1. Please keep wired network or connect to wifi network to update software |.
automatically~
2. USB update as followse
App Managere Please keep a wired network or connect to a wifi network to automatically |,

update the app software.

e

-16-


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 64 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Service Introduction ,

Key Teste Press the "button" to start calibration.
The corresponding screen display of the physical button flashes.¢
NFC Teste Please correspond to the location of the NFC sensor, and when the sensor |:
is detected, the information will be displayed on the screene
Brake Teste Resistance output test

(If testing, please contact the relevant personnel or maintenance personnel)+

Sensor Testse Test that the sensor is working+ .
(If testing, please contact the relevant personnel or maintenance personnel)

Brake Teste Resistance output test .
(If testing. please contact the relevant personnel or maintenance personnel)+

Error Code Loge Diagnose and save malfunction error messages for technician to inspect the |,
machine and troubleshooting press “Error Code Log” button 10 consecutive
repetitions to clear the error message.¢

9. Software update

9.1 software update manager

Software Done v

Automatic Update  ]
TFT OS

LWR

Software Update

Image for Treadmill/ Elliptical / Bike Software Update
First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data
you want to update to the USB.
-17-


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
12.31 Lower Control Board Replacement

As shown in Figure 12.31 and Figure 12.32, remove the plastic column, and then you can remove the
control board.

Figure 12.31 Figure 12.32

12.41 Main Roller Replacement

As shown in Figure 12.41, loosen the M5 screw (3pcs) to remove the left and right side of the carriage base
cover B.

Figure 12.41

As shown in Figure 12.42, loosen the M5 screw (3pcs) to remove the carriage base cover A.

Lye eae
cae x Fi
ao td
Ss om
ume <<

-28 -
