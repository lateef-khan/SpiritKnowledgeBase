<!-- Source: CR1000-2023 SR8880-SB028 service manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

SERVICE MANUAL
                  CR1000(2023)

                 SR8880-SB028

            ENT Recumbent Bike




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


       6.3 Driver Board function ............................................................................................................. - 11 -

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

       9.1 software update manager .................................................................................................... - 16 -


                                                                               -2-
       9.2 Update Firmware. .................................................................................................................... - 17 -

10. GENERAL MAINTENANCE

..................................................................................................................................................................... - 17 -

       10.1 Troubleshooting procedure Matrix .................................................................................. - 18 -

11&12. Disassembling and Assembling

..................................................................................................................................................................... - 18 -

       11.1Preventative Maintenance ................................................................................................... - 19 -


       12.1Part Replacement Guide ...................................................................................................... - 20 -

13. Trouble Shooting

..................................................................................................................................................................... - 38 -

       13.1 Belt Slips While Pedaling Under High Load .................................................................. - 38 -


       13.2 Noise and/or rough feeling at the pedals ..................................................................... - 39 -


       13.3 Noise or unstable feeling ................................................................................................... - 39 -




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
Console           Interface that controls all functions of the Recumbent bike.
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




                                                          GROUND



                                         Console Power                              USB
             Internet                    CONNECT                                    CONNECT
             CONNECT




                                                                     HDMI CONTACT
                        C-safe CONNECT
TV CONNECT
                        (4 PINS)

                                                          Key Board CONNECT (20

                                     SYSTEM CABLE         PINS)

                                     CONNECT (8 PINS)




   6.2 Driver Board PCB Component Locations




                                                 - 10 -
6.3 Driver Board function



                                 BRAKE
                                FLIWHEEL
      CONSOLE           RPM                DC 24V
                                 OUTPUT
       POWER           SENSOR              INPUT
       OUTPUT           INPUT




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
                                                    - 16 -
    First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data
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
11.1Preventative Maintenance

11.11Check for Pedals
As shown in Figure11.11, 11.12, check whether the pedals are tight every week. The left pedal tightens
counter-clockwise and the right pedal tightens clockwise.




                                                   - 19 -
      Figure11.11                                           Figure11.12

11.12 Check for Console Mast
Figure 11.13, Figure 11.1214, check that all mounting screws are tight. Perform as needed when handlebars
or console seem loose. (Refer to 12.25, 12.12 for cover removal procedures to access screws)




   Figure 11.13                                      Figure 11.14

11.13Periodically Clean Iron Board
Figure 11.15, Figure 11.16, regular cleaning of aluminum seat track rails for continued smooth seat
operation and life of wheels.




   Figure 11.15                                        Figure 11.16




12.1Part Replacement Guide

12.11Console Replacement
Remove Console Chin Cover
In Figure 12.11, Figure 12.12, remove the four screws of the chin cover and remove it.




                                                   - 20 -
Figure 12.11                                      Figure 12.12

Remove console
As shown in Figure 12.13, Figure 12.14, remove the four screws from the rear of the electronic watch and
remove the wire connector to remove the electronic watch.




Figure 12.13                                      Figure 12.14

Electronic table assembly in accordance with Figure 12.11 and Figure 12.12, you can replace.

12.12Front Handlebar Replacement
Refer to Figure 12.11 for the removal of the chin cover. As shown in Figure 12.15, remove the M8 socket
screws and remove the armrest.




Figure 12.15

Refer to12.15 for the front armrest assembly.


                                                   - 21 -
12.13Rear Handlebar Replacement
Remove Rear Handle bar Cover
As shown in Figure 12.16, Figure 12.17, remove the 2 screws underneath the rear armrest cover and
remove it.




Figure 12.16                                        Figure 12.17

Remove Left and Right Cup holders
Figure 12.18, Figure 12.19, will be left and right cup under the two screws removed (about a total of 4), and
removed.




Figure 12.18                                         Figure 12.19

Remove Rear Handle bars
As shown in Figure 12.20, remove the rear armrest with 8 screws.




Figure 12.20

                                                    - 22 -
Disconnect hand pulse Wires
As shown in Figure 12.21, remove the two connectors from the connecting cable and pull out the full rear
armrest.




Figure 12.21

Please refer to 12.16 ~ 12.21 for armrest assembly.

12.14Pedal/Crank Arm Replacement
Remove Pedals
As shown in Figure 12.21, 12.22, remove the right pedal counterclockwise and remove the left pedal
clockwise.




Figure 12.21                                          Figure 12.22

Remove Crank Arm Retaining Bolt
As shown in Figure 12.23, remove the cranked screws. (About the same, please use 60 N-m when locking)




Figure 12.23
                                                      - 23 -
Remove Crank
As shown in Figure12.24, use the puller to exit the crank. (About the same)




Figure12.24

For crank and pedal assembly, please refer to 12.21 ~ 12.23.



12.15Front Shroud Replacement
Remove Mast Covers
Figure 12.25, Figure 12.26, Remove the 3 self tapping screws from the left hand side mast cover. Both
covers can now be removed. First remove the crank arms (See Procedure 12.14)




Figure 12.25                                       Figure 12.26

Remove Left Front Cover
First remove the crank arms (See Procedure 12.14). Remove the 9 screws from the left cover and take off
the cover as shown below in Figure 12.27, Figure 12.28.




                                                   - 24 -
Figure 12.27                                      Figure 12.28

Remove Right Front Cover
Remove the 4 screws as shown below in figures 12.29 & 12.30 and take off the right side cover.




Figures 12.29                                     Figures 12.30

Reverse the process to re-install the covers.



12.16Drive System Replacement
Release tension on idler
See procedure 12.14、12.15 to remove Crank ,Front Cover &Front Shroud. Refer to Figure 12.31 &12.32 to
loosen the adjustment nut on the J-bolt until the tension spring can be removed.




Figure 12.31                                     Figure 12.32

                                                   - 25 -
Remove Belt
As shown in Figure12.33, Figure 12.34, after the idler is removed you can then remove the Poly-V drive belt.
When re-installing the belt make sure the belt tension is set to 220 ~ 240 Newtons (50-55 Lbs.) and keep
the belt in the middle of pulley.




Figure12.33                                       Figure12.34



Remove Idler Assembly
As shown in Figure 12.35, Figure 12.36, loosen the 3 screws and remove the idler assembly. When
re-installing the idler assembly, make sure the bracket is rotated fully clockwise so the screws are at the end
of travel in the slots as shown.




Figure 12.35                                         Figure 12.36



Remove Brake
Refer to Figure 12.37, 12.38 , remove the 4 screws holding the brake in place and remove the brake.




                                                     - 26 -
Figure 12.37                                    Figure 12.38



Replacing the Bearing Cartridge Assembly

As shown in Figure 12.39, loosen the nut with a spanner wrench or screw driver and hammer if necessary.
When installing the new assembly be sure to align the key in the cartridge with the slot in the frame
housing. Use Loctite thread locker when installing the new cartridge.




Figure 12.39

Remove Reed Switch
As shown in Figure 12.40, loosen the reed switch screw and remove it.
When installing the reed switch ensure the space gap between the switch and the face of the magnet in the
pulley is about 2mm.




Figure 12.40

                                                  - 27 -
Drive System Installation, please refer to Figure 12.31~12.36.


12.17Rear Cover/Bottom Cover Replacement
Remove Bottom Cover
Refer to Procedure 12.15 for the removal of the front covers. As shown in Figure 12.41 and Figure 12.42,
remove the 4 screws of the left and right bottom covers.




Figure 12.41                                        Figure 12.42

Remove Rear Stabilizer Cover
Figure 12.43, Figure 12.44, remove the four screws from the left and right covers and remove covers.




Figure 12.43                                        Figure 12.44



Remove Left Rear Cover
Figure 12.45, Figure 12.46, remove the 9 screws as shown and take off cover.




                                                    - 28 -
Figure 12.45                                     Figure 12.46

Remove Right Rear Cover
Figure 12.47, Figure 12.48, remove the screw and washer from the inside frame and the bottom two screws
as shown.




Figure 12.47                                       Figure 12.48

Rear Cover & Bottom Cover assembly, please refer to 12.41~12.44.

12.18Lower Controller Replacement
Unplug the wiring connectors
Refer to Figure 12.17 for the removal of the covers. Unplug the wiring connectors in Figure 12.49.(Assemble
back in reverse of remove.)




Figure 12.49
                                                   - 29 -
Iron Plate remove.
Refer to 12.17 to remove Rear cover. As shown in Figure 12.50, loosen 4 screws to remove it.




Figure 12.50



Remove Lower Controller
Refer to Figure 12.51 to remove the four Phillips head screws that secure the lower controller.




Figure 12.51

Refer to 12.49~12.51 to assemble back lower controller.


12.19Sliding Seat Assembly Replacement
Remove Cable Ties
In Figure 12.52 cut the cable tie on the inside of the seat carriage that restrains the seat release cable. In
Figure 12.53 cut the cable tie that restrains the hand pulse wiring.




                                                      - 30 -
Figure 12.52                                      Figure 12.53

Remove the Seat Track Cover and Plastic Sweat Protector
As shown in Figure 12.54 remove the 8 screws of the seat track cover and remove the cover and sweat
protector.




Figure 12.54

Remove Release Lever and Cable
Remove the release lever assembly from the seat frame by unscrewing the two mounting bolts (Figure
12.55). Remove the cable by loosening the jam nut, as shown in Figure 12.56, then unscrew the barrel until
the inside nut is removed from the thread end of the barrel. Remove the cable end from the lever to free
up the cable for removal.




Figure 12.55                                      Figure 12.56
                                                   - 31 -
Remove Aluminum Rail End Plug
Figure 12.57, Figure 12.58, the end of the aluminum end of the two screws and the outer side of a screw
release, you can remove.




Figure 12.57                                      Figure 12.58



Remove Iron Plate
As shown in Figure 12.59, remove the four screws on the iron plate and remove them.




Figure 12.59

Remove Seat Carriage
Remove the two center, bottom screws on both sides of the carriage (Figure 12.60) and slide the carriage
off the back of the unit (Figure 12.61)




Figure 12.60                                    Figure 12.61
                                                   - 32 -
PU Wheel replacement and installation
Refer to Figure 12.62, use 6mm tool insert into PU wheel to replace it and then ensure that the PU wheel is
locked




Figure 12.62

Remove the Seat Lock Mechanism
As shown in Figure 12.63, 12.64, remove the two axles from the barrel of the locking mechanism.




Figure 12.63                                      Figure 12.64




Remove Mechanical Lift Arm
As shown in Figure 12.65, loosen the nut on the lift arm to remove the replacement. (Moving column
removal reference 12.59)
As shown in Figure 12.66, the direction of the key in the installation is in the direction of the electronic
watch. The lift arm must be in the same direction as the picture. The nut is not locked before installation
(refer to 12.66).




                                                     - 33 -
Figure 12.65                                     Figure 12.66

Remove Seat Slide
As shown in Figure 12.67, Figure 12.68, relax the 8 screws to pull out the seat rails (the screws do not need
to be removed), and do not lock them first (see 12.64).




Figure 12.67                                       Figure 12.68

Install Seat Slide Group
As shown in Figure 12.69, Figure 12.70, ensure that the PU wheel reference 12.58 is locked and will slide
into the seat rails that have not yet been locked (see 12.64).




Figure 12.69                                       Figure 12.70

Install Cable
As shown in Figure 12.71, Figure 12.72, the round end is mounted on the lift arm and the nut end is pierced
from the side notch, with the handle shown in 12.54.
                                                    - 34 -
Figure 12.71                                    Figure 12.72

Adjust Seat Slide Group
As shown in Figure 12.73, move the carriage to the front and lock the front two screws; move the carriage
to the last and lock the last 2 screws.
As shown in Figure12.74, lock the other screws separately.




Figure 12.73                                      Figure 12.74



Combine Slide and Lift Arm
See Figure 12.75 and refer to the 12.57 removal procedure to replace the parts and, as shown in Figure
12.76, the outer screws are locked to the bottom and fixed to the inner braces. (Both sides are the same)




Figure 12.75                                    Figure 12.76
                                                   - 35 -
Adjust Mechanical Lift Arm
As shown in Figure 12.77 move the carriage to the rear and lock the nut on the lift arm.
As shown in Figure 12.78 move the carriage to the front and use the hand to lock the front lift arm nut.
(Not too tight will not fall off)




Figure 12.77                                      Figure 12.78

Install Iron Plate and Plastic Plate
Make the heartbeat thread back and tie the strap and set the 8 screws as shown in Figure 12.79 Figure
12.80 and 12.52, 12.53.




Figure 12.79                                      Figure 12.80



12.20 Remove Seat Bottom and Seat Back.

Remove Seat Bottom
As shown in Figure 12.81, 12.82.Remove the four screws from the under-side of seat cushion.




                                                    - 36 -
Figure 12.81                                     Figure 12.82

Remove Seat Back Cover and Retaining Strap
As shown in Figure 12.83, 12.84, remove the two screws that hold on the retaining strap. Remove the cover
by grabbing the edge with your fingers and pull (Fig. 12.84) until cover un-snaps from the seat back.




Figure 12.83                                     Figure 12.84

Remove Seat Back
As shown in Figure 12.85, remove the four screws on the rear of the seat back and remove it.




Figure 12.85

Seat bottom& seat back assembly, please refer to 12.81~12.83


                                                   - 37 -
12.21 Foot Pad/Transport Wheel Replacement

Remove Transport Wheel
As shown in Figure 12.86 loosen the screw and nut and remove the wheel.




Figure 12.86

Remove Foot Pad
As shown in Figure 12.87.Loosen the locking nuts with a 15 mm wrench and turn the footpad
counterclockwise to remove.




Figure 12.87




13. Trouble Shooting
13.1 Belt Slips While Pedaling Under High Load
If you find the belt is slipping please refer to 12.15, 12.31, 12.32 to gain access to the belt adjustment.




                                                      - 38 -
13.2 Noise and/or rough feeling at the pedals
If there is a clicking sound, or feeling that something is loose, first check that the pedals are tight. Then
check that the crank arm bolts are tight. Check for play in the axle. It is also possible that the bearing
assembly nuts are loose, check those.




13.3 Noise or unstable feeling
If the front handle bars are shaking during pedaling or feel loose when grabbing them check the bolts
securing the handle bar to the mast and/or the mast bolts at the main frame.




If the seat is shaking during use check the wheels are tightened properly. It may be necessary to eliminate
                                                      - 39 -
play between the wheels and the seat track. Loosen the bottom wheels and lift up on the wrench while
retightening them. You may need to adjust the top wheels too by loosening them, lifting the seat carriage
while retightening them.




If the whole product is shaking during use check that the foot levelers are adjusted properly, please refer to
Procedure 12.21.

If there is a lot of space between PU wheels and the seat track and cause serious shaking, please refer to
12.58 to re-adjust the location of PU wheels




                                                     - 40 -


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Zz
—
>
LY
Cc DW OA

> ©
Ps LY) a
we

Ww oO

CP Oo ®


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 62 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-Contents-

TL OUTINGS... cece ccceeeccsseescsseeseesecseesecsessecnsssecsaeesesaecseaecaessecsassecsaeeaesaecseaecaessecaaseeceasesesaecseeaecaesaesaaseneaaees -4-
QZ.EIO@CHOMIC PITS ...........ceeceseesceseescesecseesecseesecseeseceseescsaecsessecsessecaesseceaeeseesecsessecseseeseaseceaeesessecaesaesaeseeaeees -5-
2.1 CONMSOME .o.ceccccccccscscseseseseescscscscsessssvsssesesesesesasscsessssvassesesssesesassesesssssasassesesesesasscsessvasacseseeesesecaeseseees -5-
2.2 Controller ANd Driver Parts.........cccccceecesecsesesesceeseeesesesescseeeseeceeeeceesesesesesaeaeseeeeteeseeeneneneneass -6-
3. Electrical COMPIQUIATIONS ...0..... ee c ee cceteesceseeseesecseesecseesecaseseceseceesaecaessecsecsecseseseaeeesaecaesaesaeseessaseeeees -7-
vd oXe [ULo4 ©) ol) co] | (0) s ee eee -8-
4.1 WINdOW DISPLAY... eee sesssesseseesesesesneseeeesesesueneesescaesusneeeseassnsucseseeesansneaeeteesaesnsneeteecateneaeeteeeatey -8-
4.2 FUNCTION LOCATIONS.......ccccccccccccscscsessssescsesesesecesecscsessssssssesesesssesascsesesesasassssesecesesacsesesssacasseseeeeesess -8-
5. Unit BlOCK DiC Gras. .......... ee ccccccccssssecsseseceeeecesecseesecsessecsesseceeeeceaeeseaecaessecaeseessaseseaeceesaecaeeaesaeseeneees -9-
6.Basic CONNECTIONS CAN WITIING. 0.00.00... ccecccsseeccsseesceseeseesecsecsecaeseeceaeeeceaecsesaecseseecaeseeceaeeseeaecaeeaeeas -10-
6.1 1/O Board BottOM.....cccccccccccssscsesesssecscscscscsesssscscsesesesesesacscsesssavassesesesesescacscsesessacssseseeesesacas -10-
6.2 Driver Board PCB Component LOCATIONS. ...........ecceeeesesecseseseseeeeseseseseseeseaceeeeeteeseeaeatsnseeees -10-
6.3 Driver Board FUNCON cc ccccccccceseeesesesesesesesesescscsesesesescscsesesescscsescscscscscscscscsesesescstscsescseans -11-
7. Error Messages / TroUDICSHOOTING...............cccecceccesesseesecseesecseeecseececaecaeesecseseecaeseeceaeeeseaesaeeaeeaeeats -12-
7.1 Error Code LiSt......cccccccccccscscscscsssscsesesssescscscscsessssvassescsesesesasscsesssavasasassesesesascscsesessvacasseseeesesacas -12-
7.2 Error COE itOMS w....cccccccccccscscsssssscsesesesesecccscscsessssvavsesesesesesesscsesssavasassesesesesasscsesesavacasseseeesesacas -12-
7.3 TOOIS REQUIFEC 00.0... eseeeecesesessesesesesessesesesesesueseseseesesesescaesesususscacaeeeeesescaeaesesueneaceceeeteeeesatansesenees -12-
TA Circuit Dia Qraim i eesessesessessesscseesesssssnescesesssssneneeseeesesnsneeeeecsesusseeesecaesusaeeeeecassusaeeteeasaneneeees - 13 -
8. Setting and Operation for Engineering MOde ........... cc ccceccsceeceeesceseeseeecseseeceeeeceseeeeeseeaeeaeens -14-
8.1 Operation for entering ENGINEELFING MOE? ........eecsesesecseeseeseeeeseeseeeeseeseeeeneeneeeeaeeneetentens -14-
8.2 Instructions for each item of operation in engineering MOAE?....... eset -14-
8.3 Machine INFOrmation .......cccccccccscssssssssessseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseseeeseeeseeeees -15-
9. SOFTWALE UPCAFE 00... ec ccccecsceeesessesseesecseesecssesecsaecseesecsessecsessecseseeseaecsseaecaeseecaeseeseaseeseaesaeeaesaeeats -16-
9.1 Software UPCate MANAGED ........ceseseesesseseeseeeesesseeeesesseeeesesneeeesesueeesessusseeecseeneeessesneeeeataneeteatens -16-


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 27 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9.2 Update Firmware. .........cccccccecesessesesesesseesscsesesesececscseseeeeseseseaesnsususacaeseeeeeeusacaeansessneaeeeeeeeeeeeeatans -17-

10. GENERAL MAINTENANCE

EEE EEE EE ESET ESSE SOOO EE ESETSSESS ESS S OOO ETESOSES SSS SOOO OT ESSSOSESS SOOO OOOTESOSESE SSS SOSOSESCSOSESSS SOOO OSOSSTSSSSSSSS SSS SSTSSSTESTSSSSS -17-
10.1 Troubleshooting procedure Matrix... eccseesseeeseessseseeseeasseseeseeasseneetesiseneeeeeeens -18-

11&12. Disassembling and Assembling

EEE EEE EE ESET ESSE SOOO EE ESETSSESS ESS S OOO ETESOSES SSS SOOO OT ESSSOSESS SOOO OOOTESOSESE SSS SOSOSESCSOSESSS SOOO OSOSSTSSSSSSSS SSS SSTSSSTESTSSSSS -18-
11.1 Preventative Maintenance ........ccsecessesssseseesesseseseesesesssneseeeeesaesusseeteesassneseetsesateeneeteeeens -19-
12.1 Part Replacement Guide .........c.cccesecscsesesesseesesesesesecscseseeeeeeseecseaesesneneaeaeseetesecatansesesesaeeseeeees - 20-

13. Trouble Shooting

EEE EEE EE ESET ESSE SOOO EE ESETSSESS ESS S OOO ETESOSES SSS SOOO OT ESSSOSESS SOOO OOOTESOSESE SSS SOSOSESCSOSESSS SOOO OSOSSTSSSSSSSS SSS SSTSSSTESTSSSSS - 38 -
13.1 Belt Slips While Pedaling Under High Load oo... ccseeeeseenseeereeeesseeeeseeessneneeeeeees - 38 -
13.2 Noise and/or rough feeling at the Pedals 0.0... eeeseseeseeeeeeeeneeeeeseeteeseeteeseeneeees - 39-
13.3 Noise or unstable feeling ........ ces eecessesseeseceeesneeeeseseesesesesseeeeseeseeseneeneeeeatsneeteatseeteessetaetees - 39-


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 86 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
J8A02 UDIMS OV
JBAI] BSeAIaY

[epad

u-Aiquassy

3IGeO/M ae

TAiquessy

(oz) (9) (zt<9t) (vt) (92) (et<zt) (tt) (4z@<ot+6) (st) — (st) algeo/M asindpueyy

(1) 4@p|OH aiog yuLIG
(4) J@PIOH ajog YUL
Jang ypeg Jas

deo pul a|xXy winuiwnyy
deo

(4) JeA0D JEZIIIGeIS 1e8Y
(7) 8009 JeziIIqeis 1e84y

JON JBZIIIGEIS JULY

ypolg
(4) pnouys se8y

(7) pnoys e984

Jan0D weag
(44) pnosys yuol4
(1) pnouug quoi

YAEBAOD JS B|OSUOD
“THBA0D JSE/\ B|OSUOD,

ded apis duBpuey
(ueay)J8A0D

ulud ajosuog
(yuoJ4)

JO@AOD UlYD ajosuoD

J8A02 pseogkay
(2-12) )»=s (pzsez)—s«éot)—Cts«éS)—“(<éi)SCS;*‘C?‘'D (woHog)8A09 8849S
(do] )ianog uaai0g

uondusseq

SOUILINO'L


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SuO!}ed07 UOI}DUNY Z'y

JSEODIM

SEICIIN

Ae\dsiq 141 .9°St
Aejdsiq MOpUuIM L'?

UOIDI9dO JONPOld'p


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.Unit Block Diagrams

DISPLAY CONSOLE«
A A * A A A A
SYSTEM Console Power
HDMI C-safe TV Internet
OO NECT: CONNECT CONNECT= |} CONNECT: CONNECT |} CONNECT:
CONNECTING BOARD:
KEY:
DRIVER BOARD<« CONNECTING:
BOARD#
{ ft f L
DC Brake: RPM Handlebar:

POWER4 | Flywheel] | SENSOR


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.Basic Connections and Wiring

6.1 1/0 Board Bottom

GROUND

Console Power
Internet CONNECT
CONNECT
SS
: ry,

ao ue
a as

HDMI CONTACT

C-safe CONNECT
(4 PINS)

TV CONNECT

Key Board CONNECT (20

SYSTEM CABLE PINS)
CONNECT (8 PINS)

6.2 Driver Board PCB Component Locations

-10-


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-IT-

EU ees
Meee

0-Av6 OATO<GD>

‘gLoesso

LAdLNO
d3dMOd
ATIOSNOO

YOSNAS
Wdd

LAdLNO
TSASHMI 1A
dyVdd

UO!}IUN} PALO JOA €°9

ov“ 4eu
ereesee


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 33 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7.4 Circuit Diagram

SR8880-SB028 230V
Recumbent Bike CIRCUIT DIAGRAM

RMGINTERMET &
Tw i CABLE

i a
yo ————————_—

6-FIN MAIN CONTROL MRES
fv POWER INPUT — —
_L -_
[eae]
Power cable ~
aH
, a «CS
q|
(e) inasieniadiemaal *) |
f Hk aie Fail 4
100W Power Adapter
oureyt
Oc aaa
—-
a [] treme
PIN MAIN GONTPOOL WARES.

CONTROLLER =>

-13-


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
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

Recumbent Bike

Reset Odometer S I

Display Brightness

oa)

-14-


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 114 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.3 Machine Information

About This Machine Introduction

Typee There are three modes for the Machine Type Treadmill/ Elliptical/ Upright |,
Bike/Recumbent Bike. +
Please select for the machine. The selection must match the actual machine
otherwise it will be unable to operate the machine properly.¢

4

Preferences Introduction ‘

Beepe ON/ OFF for beep sound modee F

Pause Modee ON/OFF Pause Time Mode (Minutes : Seconds) ;

Sleep Modee ON/OFF for sleep mode The display always lights when tums off. When |,
there is no action for 15 minutes after turning on the power, it enters sleep
mode.

Workout Time Limite ON/OFF set limit machine usage time.¢ ,

Machine Setup Introduction ,

Languagee To set default language for the first page window. There are 12 languages in |,
the menue

Date & Timee Set console time system. ;

Units English/Metric mode switching. ,

Videos STB / TV / None mode switchinge ,

Protocole Select “C-SAFE or CAB” button for TV switching box (Choose one is allowed |,
only).

WIFie Please hit WiFi button to proceed WiFi setting.

Softwares 1. Please keep wired network or connect to wifi network to update software |.

automatically~
2. USBupdate as followse
Firmwaree 1. Please keep wired network or connect to wifi network to update software |.
automatically
2. USB update as followse
App Managere Please keep a wired network or connect to a wifi network to automatically |.
update the app software +

e

-15-


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 74 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Service Introduction ,

Key Teste Press the "button" to start calibration « ‘
The corresponding screen display of the physical button flashes.
NFC Teste Please correspond to the location of the NFC sensor, and when the sensor |:

is detected, the information will be displayed on the screene

Communication Test- Perform hardware tests such as RS232 or USBe ,
(If testing, please contact the relevant personnel or maintenance personnel)+

Brake Teste Resistance output test- ;
(If testing, please contact the relevant personnel or maintenance personnel)+

Sensor Tests- Test that the sensor is workinge ,
(If testing, please contact the relevant personnel or maintenance personnel)

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
-16-


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
(</})

m ir
Be
Ee He ii
7 = M ne

11.1Preventative Maintenance

11.11Check for Pedals
As shown in Figure11.11, 11.12, check whether the pedals are tight every week. The left pedal tightens
counter-clockwise and the right pedal tightens clockwise.

“eg
