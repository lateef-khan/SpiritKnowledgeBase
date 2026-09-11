<!-- Source: 7.0S-770545_RS9500-SS021-02_Service_Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

7.0S-770545 (RS9500-SS021-02)

Service Manual
--------------------------------------------Table of Contents-------------------------------------------
           1.   Serial Number Location
           2.   Component Description
           3.   Preventative Maintenance
             3.1 Check for Pedal
             3.2 Check for Swing Arm
             3.3 Check for Aluminum Track
           4. Setting of Electronic Console
             4.1 Basic Functions
             4.2 Maintenance Mode
           5. Troubleshooting (Electronic)
             5.1 Product Operation
             5.2 Maintenance Mode: Settings and Assist for troubleshooting
           6. Part Replacement Guide
             6.1 Console Replacement
             6.2 Swing Arm Replacement
             6.3 Pedal Replacement
             6.4 Console Mast Cover/ Top Cover/ Shroud Replacement
             6.5 Front Connecting Cable/ Rear Connecting Cable/ Drive Cable Replacement
             6.6 Lower Linkage/ Handle Bar Linkage/ Upper Linkage Replacement
             6.7 Linear Slider Replacement
             6.8 Cable Guide Wheel Replacement
             6.9 Mounted Bearing/ Belt Replacement
             6.10 Magnet Bracket/ Gear Motor Cable / Gear Motor Replacement
             6.11 Rubber Foot and Transportation Wheel Replacement
             6.12 Seat back Gas Cylinder Replacement
             6.13 Seat steel cable replacement
             6.14 Seat rotation adjustment steel cable replacement
           7. Trouble Shooting
             7.1 Slip of Belt
             7.2 Sway of Swing Arm
             7.3 Sway of Swivel Seat
             7.4 Abnormal SPM Reading
           8. Wiring Diagram
1. Serial Number Location
2. Component Description
Lower Controller and Driver




                                                 Optical SENSOR




                                              Optical SENSOR

                              TENSION MOTOR
3. Preventative Maintenance

 3.1 Check for Pedal
  As shown in Figure 3.1.1, check whether the pedal is loose, if it is loose, you need to lock the screw.




 Figure 3.1.1

 3.2 Check for Swing Arm
  As shown in Figure 3.2.1 and Figure 3.2.2, check whether the armrests are loose or not. If it is loose, tighten the screws (Same on
  both sides).




 Figure 3.2.1                             Figure 3.2.2
3.3 Check for Aluminum Track
 As shown in Figure 3.3.1 and Figure 3.3.2, regular cleaning of the surface of the aluminum sliding rail can avoid PU wheel loss.




Figure 3.3.1                        Figure 3.3.2
4. Setting of Electronic Console

 4.1 Basic Functions

 Refer to the user manual for the function introduction section.

 4.2 Maintenance Mode

5. Troubleshooting (Electronic)

5.1 PRODUCT OPERATION
  Display Windows




                   7.5” LCD Display
For detailed console operation refer to the Owner’s Manual
5.2 Maintenance Mode: Settings and Assist for troubleshooting

 5.2.1 Maintenance menu in console software
 The console has built in maintenance/diagnostic software. The software will allow you to change the console settings from English to Metric
  and turn off the beeping of the speaker when a key is pressed for example. To enter the Maintenance menu (may be called Engineering mode,
 depending on version) press and hold down the Start, Stop and Enter keys. Keep holding the keys down for about 5 seconds and the message
 window will display “Engineering mode”. Press the enter button to access the menu below:


 • Key Test
  i. Press each key to verify it is functioning correctly. Each key press produces a beep sound and a number will show on the display. If you
     press a key and there is no beep and no number displayed then that key has malfunctioned. When all keys have been pressed the display
     will show ‘Passed’, the test program ends automatically.


 • LCD test
   i. Display all LCD for visual checking.


 • Functions
   i. Sleep - Turns SLEEP MODE ON or OFF. When set to ‘off’ the console power is always on. When set to ‘on’ the console will go to sleep after
       30 minutes of inactivity.
   ii. Pause - Turns PAUSE MODE ON or OFF. When set to ‘on’ the Pause lasts 30 minutes then the console returns to the idle mode. When set
       to ‘off’ the pause lasts indefinitely.
 iii. Odometer Reset - Reset odometer readings.
 iv. Units - Set the measurement values to display in ENGLISH or METRIC.


  • Service
   i. Motor test-
     This test runs the resistance motor from 1~20 and then 20~1.
     The resistance level shows in SPM window and the value of motor position sensor shows in STEPS window.
ii. Sensor Test-
  1. The stepper has two sensors: One Step Sensor for detecting right step or left step (located on the front left side pulley, 2 optical sensors
     and silver/black encoder wheel on pulley), and an RPM Sensor for measuring the speed of the flywheel (another optical sensor that
     senses the four bolt heads on the flywheel).
 2. There are two reflector sensors on the Step Sensor. Sensor #1 show in SPM window (1 or 0 as either black or silver is detected), Sensor
     #2 show in CALORIES window (1 or 0 as either black or silver is detected). The TIME window shows the left step position counter, the
     STEPS window show the right step position counter. The counters should go from about 0 to about 17 as you take a full step.




 3. The RPM sensor output is displayed in the PULSE window (ON/OFF as the bolt head passes the sensor) and actual RPM of the
    flywheel show in message window.
 5.2.2 Error messages
  • EEPROM Error – Solution for this is to replace the console (Note: this is the only error message)
  • Motor Error –This error means the motor that controls resistance did not respond as expected.


5.2.3 Troubleshooting and Problem Solving (See separate wiring diagram for detailed wiring information)

 No power
  i. Make sure the A.C. outlet has power (90~240VAC) and the line cord is plugged in securely to the AC adapter.




 ii. Make sure there is 12V DC at the DC plug of the adaptor and plug into the DC jack of the stepper. Replace the adaptor if there is no 12V at the
     DC plug of the adaptor. Go to next step if there is 12V but still no power to the console.
 iii. Open the left shroud and check the connector of the DC power cable. Go to next step if there is still no power to the console.




iv. Measure between pin 10 and pin 11 of the 14 pin cable that connects to the console for 12V DC. Replace the console if 12V DC is measured.
   Replace the cable if there is no 12V DC.
Console programs do not start
i. Perform the Key Test in Maintenance mode. Replace the keypad (or whole console) if the Key Test didn't pass or can't enter Maintenance
  mode.


Program Starts But No Watts Value When Stepper is Pedaled
i. Make sure all the cables in the back of console were plugged in properly.
ii. Open the left shroud and make sure the cable is connected to the RPM sensor board properly.
iii. Run the Sensor Test in Maintenance mode.
iv. The PULSE window should show ON when the bolt is aligned to the sensor and RPM should show when the stepper is pedaled. Go to the
     next step if PULSE window didn't switch to ON when the bolt is aligned to the sensor.
v. Adjust the position of the sensor to align the sensor to the bolt. Make sure the surface of the sensor is parallel to the bolt and has a 1~2mm
   gap between sensor and bolt. If the problem persists, go to next step.




vi. Measure between pin 1 and pin 3 of the cable that connects to the RPM sensor board for 5V DC. If there is no 5V DC, check the connection of
    the cable or replace the cable. Replace the sensor board if there is 5V DC.
Left/Right Step Graph Incorrect
 i. Make sure all the cables in the back of console are plugged in properly.
 ii. Open the left shroud and make sure the cable is connected to the step sensor board properly.




iii. Measure between pin 1 and pin 3 of the cable that connects to the step sensor board for 5V DC. If there is no 5V DC, check the connection of
    the cable or replace the cable. Go to next step if there is 5V DC.




 iv. Run the Sensor Test in Maintenance mode.
 v. The SPM window should show ON when the reflector sensor #1 (bottom one) aligns to the silver surface. The CALORIES window should show
  ON when the reflector sensor #2 (top one) aligns to the silver surface. The step position counter of each foot (TIME and STEPS window)
  should show about 17 (15~17) when you perform a full range step. If the value is incorrect, follow next step to adjust the sensor board.
vi. Adjust the sensor to align with the center of the shaft as left picture. Make sure the surface of the sensor is parallel to the surface of the pulley
   and has a 7~9mm gap between sensor and the reflective surface of the pulley. If the problem isn’t resolved replace the sensor board.




Motor Error
 i. Make sure all the cables in the back of console are plugged in properly and there are no bent pins in the connector.
ii. Use an ohm meter to measure between pin 1 and pin 2 of the 14 pin cable that connects to the console (check at the cable connector when it is
    unplugged from the console). The reading should be about 2~3 ohm; this is the motor armature measurement and tells you the motor is most
    likely good. Use the ohm meter to measure between pin 3 and pin 5 of the 14 pin cable that connects to the console (check at the cable
    connector when it is unplugged from the console). The reading should be about 5k ohm; this is the motor position sensor. Replace the console
    if the reading is correct. Go to next step if the measurement is incorrect.




iii. Open the left shroud and check the connection of the cable that connects to the motor. Replace the motor if the connection is good. Otherwise,
     replace the cable.
Hand Pulse Problem
i. Check the cables in the back of console to ensure there is a good connection and the pins in the connector are not bent. Go to next step if the
    problem isn’t resolved.
ii. Measure the hand pulse sensor as pictured below. The two rear sensors points should be shorted when the console is on the bike and
  shouldn't be shorted to the other sensors. Set the hand pulse sensor to the right setting if the setup was wrong. Go to next step if the setup is
  right.




 iii. Open the cover and check the cables connection and possible broken cables. Replace the console if everything is good.
6. Part Replacement Guide

6.1 Console Replacement

   6.1.1 Remove Electronic Console
   As shown in Figure 6.1.1 and Figure 6.1.2, remove the four screws from the bottom of the electronic watch and remove the
   cable connector to remove the electronic console.




 Figure 6.1.1                         Figure 6.1.2

   6.1.2 Electronic console assembly: Follow step 6.1.1 in reverse order.
6.2 Swing Arm Replacement

  6.2.1 Remove the Swing Arm.
  As shown in Figure 6.2.1, remove the screws to remove the swing arm.




Figure 6.2.1

  6.2.2 Swing arm assembly: Follow step 6.2.1 in reverse order.
6.3 Pedal Replacement

  6.3.1 Remove the Pedal.
  As shown in Figure 6.3.1 and Figure 6.3.2, unscrew the screw. (The bottom of the screw is recommended to use a short
  screwdriver removed around the same.)




Figure 6.3.1                       Figure 6.3.2

  6.3.2 Pedal assembly: Follow step 6.3.1 in reverse order.
6.4 Console Mast Cover/ Top Cover/ Shroud Replacement

  6.4.1 Remove Console Mast Cover
  Remove the electronic console, please refer to Step 6.1. As shown in Figure 6.4.1, extrude the vertical console mast cover
  before and after the move. As shown in Figure 6.4.2 and Figure 6.4.3, loose the 4 screws on console mast, you can remove the
  console mast and console mast cover.




Figure 6.4.1                         Figure 6.4.2                         Figure 6.4.3

  6.4.2 Remove Top Cover
  As shown in Figure 6.4.4, release the four cover latches to remove the top cover.




Figure 6.4.4
  6.4.3 Remove Shroud
  As shown in Figure 6.4.5, loosen screws on the left and right shrouds. As shown in Figure 6.4.6, unplug the connector of DC
  power cable inside the left shroud. Then you could remove the left and right shrouds.




Figure 6.4.5                           Figure 6.4.6

  6.4.4 Console mast cover/top cover/ shroud assembly: Follow step 6.4.1 to step 6.4.3 in reverse order.
6.5 Front Connecting Cable/ Rear Connecting Cable/ Drive Cable Replacement

  6.5.1 Remove Front Connecting Cable
  As shown in Figure 6.5.1, record the length of the screw first and remove the nut. As shown in Figure 6.5.2 and Figure 6.5.3,
  remove the screw to remove the front connecting cable.




Figure 6.5.1                          Figure 6.5.2                          Figure 6.5.3

  6.5.2 Assemble Front Connecting Cable
  Adjust the tension of the front connecting cable to the length of the screw on the front side of the instrument. As shown in
  Figure 6.5.4 and Figure 6.5.5, tighten the fixing screws. As shown in Figure 6.5.6, adjust the nut so that the tension of the front
  connecting cable reaches 40 ~ 50LB.




Figure 6.5.4                          Figure 6.5.5                          Figure 6.5.6
  6.5.3 Remove Rear Connecting Cable
  As shown in Figure 6.5.7, loosen the socket head cap bolt on roller assembly to release the rear connecting cable. As shown in
  Figure 6.5.8, remove the spring-side cable head. As shown in Figure 6.5.9, remove the bolt on the other end of the steel lock to
  remove the cable.




Figure 6.5.7                         Figure 6.5.8                        Figure 6.5.9

  6.5.4 Assemble Rear Connecting Cable

   6.5.4.1 As shown in Figure 6.5.10, install the new cable on the copper sleeve plastic sliding and smoothing Division. As
   shown in Figure 6.5.11, lock onto the Pedal Plate.




Figure 6.5.10                        Figure 6.5.11
   6.5.4.2 As shown in Figure 6.5.12, slide the new wire around the fixed rear sliding wheel set. As shown in Figure 6.5.13,
   adjust the sliding platform welding set to the rear.




Figure 6.5.12                       Figure 6.5.13

   6.5.4.3 As shown in Figure 6.5.14, the direction of cable winding is from right to left. Make sure that the cable of the first
   groove is completely inside the cable groove. As shown in Figure 6.5.15 and Figure 6.5.16, and then wind for three turns. (To
   note that the other side of the cable installation, you need to start from the right side of the cable pulley winding)




Figure 6.5.14                       Figure 6.5.15                        Figure 6.5.16
   6.5.4.4 As shown in Figure 6.5.17, the cable head passes through the hook of the spring. As shown in Figure 6.5.18, adjust
   the tension of the wheel set. As shown in Figure 6.5.19, adjust the center of the cable head to the contour screw at a distance
   of 9cm to 10cm.




Figure 6.5.17                      Figure 6.5.18                         Figure 6.5.19
6.6 Lower Linkage/ Handle Bar Linkage/ Upper Linkage Replacement

  6.6.1 Remove Lower Linkage
  As shown in Figure 6.6.1 and Figure 6.6.2, loosen the screw to remove the lower linkage.




Figure 6.6.1                        Figure 6.6.2

  6.6.2 Remove Handle Bar Linkage
  As shown in Figure 6.6.3 and Figure 6.6.4, loosen the screw to remove the handle bar linkage.




Figure 6.6.3                        Figure 6.6.4
 6.6.3 Remove Upper Linkage
 As shown in Figure 6.6.5 and Figure 6.6.6, loosen the screw to remove the upper linkage.




Figure 6.6.5                         Figure 6.6.6

  6.6.4
       Upper linkage assembly: Follow step 6.6.1 to step 6.6.3 in reverse order.
       Handle bar linkage assembly: Follow step 6.6.1 to step 6.6.2 in reverse order.
       Lower linkage assembly: Follow step 6.6.1 in reverse order.
6.7 Linear Slider Replacement

  6.7.1 Remove Linear Slider
  Refer to Step 6.6 for removing the linkages. As shown in Figure 6.7.1, remove the screws that secure the welding pad to the
  cushion. As shown in Figure 6.7.2, loosen the four screws on the sliding platform assembly. As shown in Figure 6.7.3, loosen
  the 4 screws of the rail to remove the linear slider.




Figure 6.7.1                         Figure 6.7.2                        Figure 6.7.3

  6.7.2 Linear slider assembly: Follow step 6.7.1 in reverse order.
6.8 Cable Guide Wheel Replacement

  6.8.1 Remove Cable Guide Wheel
  Refer to Step 6.5.3 to remove the rear connecting cable. As shown in Figure 6.8.1, loosen the screws to remove the sensor
  bracket first. As shown in Figure 6.8.2 and Figure 6.8.3, the cable guide wheel can be removed after taking off the C clips.




Figure 6.8.1                         Figure 6.8.2                         Figure 6.8.3

  6.8.2 Assemble Cable Guide Wheel
  While assembling cable guide wheel, the direction of the one way bearing needs to be same as in Figure 6.8.4. As shown in
  Figure 6.8.5, after assembling the sensor bracket, the distance between sensor and cable guide wheel should be 7 ~ 9mm.




Figure 6.8.4                         Figure 6.8.5
6.9 Mounted Bearing/ Belt Replacement

  6.9.1 Loosen Idler Wheel
  Refer to Step 6.5 ~ Step 6.8 to remove connecting cables, linkages, linear slider and cable guide wheel. As shown in Figure
  6.9.1 and Figure 6.9.2, loosen socket head cap bolt and J bolt to loosen the idler wheel.




Figure 6.9.1                         Figure 6.9.2

  6.9.2 Remove Mounted Bearing
  As shown in Figure 6.9.3 and Figure 6.9.4, loosen the locking screws to remove the front and rear mounted bearing.




Figure 6.9.3                         Figure 6.9.4
  6.9.3 Remove Belt
  As shown in Figure 6.9.5, remove the belt (584L). As shown in Figure 6.9.6, remove the belt (1032L).




Figure 6.9.5                          Figure 6.9.6

  6.9.4 Belt assembly: Follow step 6.9.1 to step 6.9.3 in reverse order. As shown in Figure 6.9.1 and Figure 6.9.2, adjust the
   tightness of those two bolts to adjust the belt tension. The belt tension for belt (584L) should be 320N. The belt tension for
   belt (1032L) should be 240N.

  6.9.5 Mounted bearing assembly: Follow step 6.9.1 to step 6.9.2 in reverse order.
6.10 Magnet Bracket/ Gear Motor Cable / Gear Motor Replacement

  6.10.1Magnet Bracket Replacement

    6.10.1.1 Remove Magnet Bracket
     As shown in Figure 6.10.1, remove the four screws under the magnet bracket. As shown in Figure 6.10.2, take off the
     spring to remove the magnet bracket.




Figure 6.10.1                       Figure 6.10.2

    6.10.1.2 Magnet bracket assembly: Follow step 6.10.1.1 in reverse order.
  6.10.2Remove Gear Motor Cable and Gear Motor
  As shown in Figure 6.10.3, remove the gear motor cable by removing one end of the cable from the gear motor and using
  wrench to release the nut. As shown in Figure 6.10.4, loosen the three fixing screws of the gear motor to remove the gear
  motor.




Figure 6.10.3                        Figure 6.10.4

  6.10.3Assemble Gear Motor
  As shown in Figure 6.10.5 and Figure 6.10.6, make sure the starting position is at 11 o'clock when installing the gear motor. If
  it is not possible to use a screwdriver to loosen the middle of the screw and rotate to the correct point, and then pull the screw
  and pull the motor back to the holder.




Figure 6.10.5                        Figure 6.10.6
  6.10.4Assemble Gear Motor Cable
  As shown in Figure 6.10.7, do not tighten the nut after installing the cable pull-up motor. As shown in Figure 6.10.8, after the
  motor bracket is installed on the main frame, pay attention to the distance between the left and right sides of the aluminum
  plate and the magnet to be equidistant. If there is no equidistant to adjust the bottom two screws on one side as shown in
  Figure 6.10.9 (Do not lock to ensure that can be adjusted before and after). Connect the cable of the gear motor and install the
  spring, and adjust the resistance to Level20 on the electronic console. After pulling the cable to the position, turn the
  aluminum plate to see if the aluminum plate will touch the magnet bracket. If it touches, please adjust the magnet bracket
  back and then lock the screw.




Figure 6.10.7                        Figure 6.10.8                        Figure 6.10.9
6.11 Rubber Foot and Transportation Wheel Replacement

  6.11.1Rubber Foot Replacement
  There are six rubber feet under the machine. As shown in Figure 6.11.1, unscrew the uppermost iron nut to replace the
  rubber foot.




Figure 6.11.1

  6.11.2Transportation Wheel Replacement
  As shown in Figure 6.11.2, remove the screw cap to replace the transportation wheel.




Figure 6.11.2
6.12 Seat back Gas Cylinder Replacement

  6.12.1 Remove Locking Gas Cylinder
  As shown in Figure 6.12.1, remove the four screws under the seat cushion. As shown in Figure 6.12.2, remove the safety cover
  by loosening the screws. As shown in Figure 6.12.3, cut the cable ties. As shown in Figure 6.12.4, loosen the adjustment cable
  and remove the cable head. As shown in Figure 6.12.5 and Figure 6.12.6, take off the screws and caps to remove the locking
  gas cylinder.




Figure 6.12.1                       Figure 6.12.2                        Figure 6.12.3




Figure 6.12.4                      Figure 6.12.5                         Figure 6.12.6

  6.12.2 Locking gas cylinder assembly: Follow step 6.12.1 in reverse order.
6.13 Seat Steel Cable Replacement

  6.13.1 Replacement of Steel Cable for the Seat Back Angle Adjustment

    As shown in Figure 6.13.1, loosen the adjustment cable screw and remove the cable end.
    As shown in Figure 6.13.2, Adjust the adjustment screw beneath the release handle to the position that allows the cable to
    be removed, then remove and replace the cable.




Figure 6.13.1                      Figure 6.13.2


    6.13.2 Assembly for steel cable for the seat back angle adjustment: Follow step 6.13.1 in reverse order.
6.14     Seat rotation adjustment steel cable replacement

  6.14.1 Replacement of Steel Cable for the Seat rotation adjustment

       As shown in Figure 6.14.1, cut the cable tie.
       As shown in Figures 6.14.2 and 6.14.3, rotate the seat to an angle to make it easier to remove the cable end and the spring. As
       shown in Figure 6.14.4, adjust the adjustment screw beneath the release handle to the position that allows the cable to be
       removed, then remove and replace the cable.




             Figure 6.14.1                         Figure 6.14.2




            Figure 6.14.3                         Figure 6.14.4
       6.14.2 Assembly for steel cable for the Seat rotation adjustment: Follow step 6.14.1 in reverse order.
7. Trouble Shooting

 7.1 Slip of Belt

    7.1.1 If it is found that the belt slipping phenomenon, as shown in Figure 7.1.1, Figure 7.1.2 or reference on step 6.9.4, adjust
           the tension by tightening the screw and nut.




 Figure 7.1.1                           Figure 7.1.2

    7.1.2 If you adjust the belt tension, there is still slippery phenomenon. The reason may be that the one-way bearing in the
           cable guide wheel is broken, you need to replace the cable guide wheel (refer to steps 6.8).
7.2 Sway of Swing Arm

  7.2.1 If you find the swing arm is shaking during the step-on, lock the screw as shown in Figure 7.2.1.




Figure 7.2.1

  7.2.2 If the phenomenon of shaking still exists, check whether the quick release telescopic tube adjustment to the locking
         position as shown in Figure 7.2.2.




Figure 7.2.2
7.3 Sway of Swivel Seat

  7.3.1 Sway of swivel seat is caused by the gap between seat wheel adjustment plate and aluminum track assembly. The
         solution is as follows:
         Use a cross screwdriver to remove the fixing screw (as shown in Figure 7.3.1). Then use the 11mm wrench and the right
         hand as the 13mm wrench. Tighten the 11mm wrench first and lock it in the front direction (as shown in Figure 7.3.2)
         and behind (as shown in Figure 7.3.3).




Figure 7.3.1                        Figure 7.3.2                        Figure 7.3.3
7.4 Abnormal SPM Reading

  7.4.1 Check for Optical Sensor Board of Encoder
  As shown in Figure 7.4.1 and Figure 7.4.2, check whether the connecting cable of the optical sensor board of encoder is loose
  or not. The distance between bar code sticker and the optical sensor board of encoder should be between 7 ~ 9mm.




Figure 7.4.1                        Figure 7.4.2

  7.4.2 Check for Optical Sensor Board of RPM
  As shown in Figure 7.4.3 and Figure 7.4.4, check whether the connecting cable of the optical sensor board of RPM is loose or
  not. The distance between the optical sensor board of RPM and the screw head should be between 1 ~ 2mm.




Figure 7.4.3                        Figure 7.4.4
Exploded view drawing
7.0 S parts list


             Item    Description                      Qty

               1     Main Frame                       1
               2     Console Mast                     1
               3     Swing Arm (R)                    1
               4     Swing Arm (L)                    1
               5     Pedal Plate (R)                  1
               6     Pedal Plate (L)                  1
               7     Seat Slider (R)                  1
               8     Seat Slider (L)                  1
               9     Drive Pulley                     1
              10     Idler Bracket                    1
               11    Brake Motor Bracket              1
              12     Lower Linkage A                  2
              13     Lower Linkage B                  2
              14     Rubber Cushion Bracket           2
              15     Seat Carriage                    1
              16     Seat Back Bracket                1
              17     Handle Bar                       1
              18L    Seat Wheel Adjustment Plate(L)   2
              18R    Seat Wheel Adjustment Plate(R)   2
              19     Seat Stop Assembly               2
              20     Rotate Seat Assembly             1
              21     Seat Back Bracket                1
              22     Seat Rotation Release Lever      1
              23     Cantilever Anchor Assembly       1
              24     Adjusting Lever                  1
              25     Front Connecting Cable           1
              26     Rear Connecting Cable            1
              27     Drive Cable                      2
              28     Pedal                            2
              29     Console Assembly                 1
             29-01   Console Top Cover                1
             29-02   Console Bottom Cover             1
             29-03   Battery Cover                    1
             29-04   Console Display Board            1
             29-05   Deflector Fan Grill              1
Item    Description                       Qty
29-06   Wind Duct (L)                      1
29-07   Wind Duct (R)                      1
29-08   Water-resist Rubber                1
29-09   Fan Fixing Plate                   2
29-10   LCD Transparent Piece              1
29-11   Console Speaker Cover (L)          1
29-12   Console Speaker Cover (R)          1
29-13   400m/m_Fan Assembly                1
29-14   W/Receiver, HR                     1
29-15   Console Key Board                  1
29-16   Interface Board                    1
29-17   Fan Grill Anchor                   2
29-18   USB Adapter Board                  1
29-19   UART Adapter Board                 1
 30     Rubber Foot                        6
 31     End Cap, Oval Stabilizer Tube      4
 32     Linear Slider                      2
 33     M6 × Ø 20 × 35L_Rubber Cushion     2
 34     Ø 100 × 134L_Passive Wheel         1
 35     Ø 80 × 22L_Drive Wheel             1
 36     Ø 84 × 32L_Cable Drive Pulley      2
 37     Belt (8PJ), 584mm                  1
 38     Belt (8PJ), 1032mm                 1
 39     Adjustable Idler Wheel Axle        1
 40     Drive Pulley                       1
 41     Lower Linkage                      2
 42     Slider Sleeve                      2
 43     Flywheel Mass                      1
 44     Gear Motor                         1
 45     Braking Magnet                     4
 46     Roller                             6
 47     Cable Spring(Ø 15.5×26.5L)         2
 48     Gear Motor Spring(Ø 13×20.3L)      1
 49     Steel Cable Roller(Ø 6×Ø 24×7L)    2
 50     WFM-2528-16_Plastic Bushing        4
 51     Rubber Pad                         4
Item   Description                         Qty
52     Flywheel Axle Set Collar (R)        2
53     Cable Guide Wheel Axle              2
54     One Way Bearing                     2
55     6203_Ball Bearing                   4
56     6003_Ball Bearing                   2
57     6902_Ball Bearing                   10
58     Mounted Bearing                     4
60     Aluminum Disc Drive Pulley          1
61     Aluminum Brake Disc                 1
62     Magnet Bracket                      1
63     Rubber Isolation Mount              4
64     Gear Motor Cable                    1
66     Quick Release lever                 2
67     Ø 9 × Ø 49 × 1.5T_Cup Washers       2
68     Rear Shroud ( R )                   1
69     Rear Shroud ( L )                   1
70     End Cap                             2
71     Shroud ( R )                        1
72     Shroud ( L )                        1
73     Top Cover                           1
74     Console Mast Cover                  1
75     Bottom Step Cover                   1
76     Slide End Cap Spacer                2
77     Ø 65_Transportation Wheel           2
79     Shroud Bracket                      4
80     Sensor Bracket                      2
81     Shroud Fixing Plate                 1
82     Pedal Isolation Rubber              2
83     Seat Stop Axle                      2
84     Seat Position Latch                 2
85     Backing Plate                       3
86     Aluminum Track                      1
87     Rack, Seat Position                 1
88     650m/m_Handpulse W/Cable Assembly   1
89     Ø 32(1.8T)_Button Head Plug         2
90     Ø 38_Seat Track Wheel               8
Item   Description                               Qty
92     850m/m_Hand Pulse W/Cable Assembly( R)    1
93     Seat Cushion                              1
94     Seat Back                                 1
95     Ø 12.9× 30L_Spring                        1
96     Ø 7_HGP Wire Grommet                      1
97     Seat Back Cover                           1
98     Adjusting Lever Rotate Axle(L)            1
99     Seat Track Fixing Plate                   1
100    5/8" × 13.2 × 8L_Sleeve                   4
101    PU Wheel                                  7
102    Steel Cable                               1
104    Square End Cap                            1
105    Ø 13.5 × 60L_Spring                       1
106    Podwer Metal Sleeve(15.9×22mm)            8
107    Scale Arrowhead                           2
108    Safety Cover                              1
109    Locking Gas Cylinder                      1
110    Rotate Disk                               1
111    Release Lever(Left)                       2
112    Steel Cable(84.5×76cm)                    1
116    Podwer Metal Sleeve(Ø 12×Ø 18×8L)         2
117    25.4 × 50.5 × 14.3m/m_Square End Cap      2
118    Pedal Foam Cushion                        2
119    M5 × P0.8 × 25L_Socket Head Cap Bolt      24
120    M6 × P1.0 × 15L_Socket Head Cap Bolt      14
121    M6 × P1.0 × 20L_Socket Head Cap Bolt      8
122    M6 × P1.0 × 25L_Socket Head Cap Bolt      4
123    M6 × P1.0 × 55L_Socket Head Cap Bolt      1
124    M8 × P1.25 × 12L_Socket Head Cap Bolt     8
125    M8 × P1.25 × 20L_Socket Head Cap Bolt     4
126    M6 × P1.0 × 12L_Socket Head Cap Bolt      4
127    M12 × P1.75 × 120L_Socket Head Cap Bolt   1
129    M6 × P1.0 × 40L_Socket Head Cap Bolt      2
130    M10 × P1.5 × 75L_Socket Head Cap Bolt     3
131    M6 × P1.0 × 38L_Socket Head Cap Bolt      2
132    3/8" × UNC16 × 2"_Hex Head Bolt           4
Item   Description                                      Qty
133    M6 × P1.0 × 40L_Hex Head Bolt                     3
134    5/16" × UNC18 × 3/4"_Hex Head Bolt               14
135    5/16" × UNC18 × 1-1/4_Hex Head Bolt               1
136    5/16" × 5/8"_Hex Head Bolt                        2
137    M8 × P1.25 × 25L_Hex Head Bolt                    4
138    M10 × P1.5 × 40L_Hex Head Bolt                    4
139    M5 × P0.8 × 12L_Socket Head Cap Bolt              4
140    3/8" × UCN16 × 3-1/4"_Hex Head Bolt,20L           2
141    Ø 3.5 × 12L_Phillips Head Self-Tapping Screw     12
142    Ø 5.5 × Ø 15 × 1T_Flat Washer                     4
143    M5 × P0.8 × 12L_Phillips Head Screw              21
144    M5 × P0.8 × 20L_Phillips Head Screw               2
145    M5 × P0.8 × 6L_Phillips Head Screw                2
146    M6 × P1.0 × 10L_Phillips Head Screw               4
147    M4 × P0.7 × 10L_Phillips Head Screw               4
148    5/16" × UNC18 × 3/4"_Hex Head Bolt                1
149    M8 × P1.25 × 20L_Button Head Socket Bolt          4
150    M8 × P1.25 × 25L_Button Head Socket Bolt          3
151    M6 × P1.0 × 10L_ Button Head Socket Bolt          4
152    5/16" × UNC18 × 1-3/4"_Button Head Socket Bolt    2
153    M8 × P1.25 × 16L_Hex Head Bolt                    2
154    3/8" × UNC16 × 2-1/2"_Hex Head Bolt               2
155    M5 × P0.8 × 12L_Phillips Head Screw               8
156    M5 × 6L_Phillips Head Screw                       4
157    M5 × P0.8 × 70L_Phillips Head Screw               1
158    M5 × P0.8 × 12L_Flat Head Phillips Screw         10
160    M5 × P0.8 × 10L_Flat Phillips Head Screw          8
161    M6 × 10L_Flat Head Phillips Screw                 4
162    M6 × P1.0 × 57L_Eye Bolt                          1
163    M8 × P1.25 × 80L_J Bolt                           1
164    Ø 5 × 1.5T_Split Washer                           8
165    Ø 6 × 1T_Split Washer                            12
166    Ø 8 × 1.5T_Split Washer                          20
167    Ø 10 × Ø 25 × 2T_Flat Washer                      6
168    Ø 5 × Ø 12 × 1.0T_Flat Washer                    21
169    Ø 6.5 × Ø 13 × 1T_Flat Washer                     5
Item   Description                                  Qty
170    Ø 3/8" × Ø 30 × 3T_Flat Washer               10
172    Ø 8.5 × Ø 18 × 1.5T_Flat Washer              12
173    Ø 8.5 × Ø 26 × 2.0T_Flat Washer              2
174    Ø 12.7 × Ø 26 × 2.0T_Flat Washer             1
175    M6 × P1.0 × 10L_Socket Head Cap Bolt         2
176    Ø 6 × Ø 19 × 3.0T_Flat Washer                21
177    Ø 6.5 × Ø 16 × 1.0T_Flat Washer              4
178    Ø 8 × Ø 16 × 1.5T_Flat Washer                6
179    Ø 6.6 × Ø 12 × 1.5T_Flat Washer              8
181    M5 × P0.8 × 15L_Phillips Head Screw          12
183    Ø 3 × 20L_Self Tapping Screw                 4
184    Ø 8 × 23 × 1.5T_Curved Washer                2
185    Ø 8 × 19 × 1.5T_Curved Washer                4
186    Ø 8 × Ø 18 × 3T_Knurled Lock Washer          4
187    M6 × P1.0 × 6T_Nyloc Nut                     8
188    M5 × P0.8 × 5.0T_Nyloc Nut                   1
189    M8 × P1.25 × 7T_Nyloc Nut                    5
190    3/8" × UNC16 × 7T_Nyloc Nut                  10
191    M8 × P1.25 × 6T_Nyloc Nut                    5
192    M10 × P1.5 × 8T_Nyloc Nut                    4
193    5/16" × UNC18 × 6T_Nyloc Nut                 13
194    Ø 10 × 2T_Split Washer                       2
195    Ø 45 × Ø 21.8 × 2.5T_Flat Washer             2
197    3/8" × UNC16 × 1-3/4"_Socket Head Cap Bolt   2
198    M12_Nyloc Nut                                1
199    M6 × P1.0 × 5T_Nut                           4
200    M5 × P0.8 × 4T_Nut                           1
201    E5_E-Clip                                    2
202    Ø 10_C-Clip                                  2
203    Ø 16_C-Clip                                  5
204    Ø 17_C-Clip                                  4
205    Ø 28_Inner Snap Ring                         10
207    M6 × 19L_Nut                                 4
209    12/14m/m_Wrench                              1
210    13/14m/m_Wrench                              1
211    Wrench, 10mm                                 1
Item   Description                         Qty
212    M5_L Allen Wrench                   1
213    M8_L Allen Wrench                   1
214    Phillips Head Screw Driver          1
215    Swing Arm Drive Weldment            2
216    3/8" × 3/4"_Hex Head Bolt           12
217    Ø 10 × Ø 19 × 1.5T_Flat Washer      4
218    Ø 10 × 21.3 × 7.8T_Curved Washer    8
219    HGP Wire Grommet                    2
220    Dummy Plug                          1
221    Optical Sensor Board (CS63008-00)   1
222    Optical Sensor Board (CS63008-10)   1
223    1550m/m_Computer Console Cable      1
224    250m/m_Encoder Cable                1
225    100m/m_DC Power Cord                1
226    650m/m_Hall Sensor Cable            1
227    1550m/m_Hand Pulse Cable, Upper     1
228    1550m/m_Hand Pulse Cable, Lower     1
229    Power Adapter                       1
230    Power Cord (Optional)               1
231    Foot Strap, Narrow                  2
232    Foot Strap, Wide                    2
233    Seat Belt                           1
234    32 × 2.5T_Round End Cap             2
235    Swivel Handle                       2
236    Swivel Handle Range Limiter         2
237    Ø 5 × 16L_Tapping Screw             2
239    800m/m_Handpulse Wire               1
240    800m/m_Handpulse Wire (White)       1
241    100m/m_Connecting Wire              1
242    Short Phillips Head Screw Driver    1
243    Ø 10 × 2T_Spring Washer             12
244    Axle Positioning Ring               2
245    Ø 18 × Ø 32 × 1.5T_Nylon Washer     4
246    M5 × 10m/m_Slotted Set Screw        4
247    Axle                                4
249    Ø 17_Wave Washer                    2
Item   Description                       Qty
250    5/16" × Ø 20 × 3.0T_Flat Washer    4
251    M8 × 10 × 30L_Bolt                 4
252    Ø 10 × Ø 24 × 3.0T_Nylon Washer   14
258    Ø 10 × Ø 14 × 25.5L_Sleeve         1
259    Podwer metallurgy Sleeve           2
261    Ø 3/8" × Ø 20 × 3T_Flat Washer     2
262    Buckle                             4
263    Snap Seat                          4
8. Wiring Diagram


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jenuepy ddIAles

(ZO-LZOSS-00S6SuY) S7SOZZ-S0'Z


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. Component Description

item Description

01 Console

02 Pedal

03 Console Mast Cover
O4 Top Cover

05 End Cap

06 Shroud iL)

07 Bottom Step Cover
8 Shroud (R)

OSs Seat Back Cover
10 Rear Shroud (R}

11 Rear Shroud {L)

12 End Cap, Oval

Stabilizer Tube


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
‘AW1dSi0

ue4 8ul]ooD

*SdaqOAJUO.D daddy
“Sueg 21U0NIa/z


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
‘¢ a SEE 000

noon enooooooosoo i

aia weasels melee |
ty, BODO oOoooonooooooee WATTS |
_..., COEEOOOGEOOR0onoogae) |

‘He 889 98:88 8988 e

aT | DEBE 2)

LCD Layout


=== OCR SUPPLEMENT, PDF PAGE 47 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
a es" T)- [COSS- 00S 6SA

duyy ett

Bulmejp MaIA pepo|dxy


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
29-6 [Wind Duct (L)

29-7 ___|Wind Duct (R)

29-8 Water-resist Rubber

29-9 Fan Fixing Plate

29-10  |LCD Transparent Piece

29-11 = nsole Speaker Cover (L)
29-12 [Console Speaker Cover (R)

29-13 [400mm Fan Assembly

29-14 [W/Receiver, HR

29-15 _ _|Key Board

29-16 __[Interface Board

29-17 — [Fan Grill Anchor

29-18 [Interface Board

29-19 _|UART Board

30 Foot Pad

31 End Cap

32 Linear Slider

33 M6 x @20 x 35L_ Rubber Foot
34 1100 x 134L Passive Wheel
35 I@80 x 22L_Drive Wheel

36 I@B4 x 32L Steel Cable Slide Wheel
37 Drive Belt(S84L)

38 Drive Belt(1032L)

39 [Adjustable Idler Wheel Axle
40 Drive Pulley

41 Lower Linkage

Ev, Hollow Plug

A3 e urved weight Block
44 Gear Motor

45 Braking Magnet

46 Slide Wheel

A? 15.5 * 26.5L Sprin

As @13 x 20.3L Spring

49 I@6 x 24 = 7L Steel Cable Slide Wheel


=== OCR SUPPLEMENT, PDF PAGE 50 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
50 25 x 428 x 16L_ Bushing 4
51 Rubber Pad 4
52 Flywheel Axle Retaining Collar (R) 2
53 Cable Guide Wheel Axle 2
54 Unidirectional Bearing 2
55 6203 Bearing 4
56 6003 Bearing 2
57 6902 Bearing 10.
58 Bound Bearing Axle Assembly 4
60 Aluminum Disc Drive Pulley 1
61 Aluminum Brake Disc 1
62 Magnet Bracket 1
63 Bushing 4
64 Steel Cable,Resistance 1
66 Quick Release lever 2
67 Bushing washer 2
68 Rear Shroud ( R ) 1
69 Rear Shroud (L) 1
70 Bearing Shaft Plug 2
71 Chain Cover (R) 1
72 Chain Cover (L) 1
73 Top Cover 1
74 Console Mast Cover 1
75 Bottom Cover 1
76 Handgrip End Cap 2
ii @65 Transportation Wheel 2
79 Chain Cover Bracket 4
80 PCB Bracket 2
81 Chain Cover Fixing Plate 7
83 Holder Assembly ?
64 Seat Position Latch 2
85 Backing Plate 3

86 Aluminum Track

87 Rack


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
88 '750mm_Handpulse W/Cable Assembly

89 1@32(1.8T) Button Head Plug \2
90 @38 Seat Track Wheel 8
92 900mm_Hand Pulse W/Cable Assembly 1
93 Seat 1
94 Seat Back 1
96 i@7_ HGP Wire Grommet 1
97 Seat Back Cover 1
199 Seat Track Fixing Plate 1
100 5/8" x 13.2 x 8L Sleeve 4
101 PU Wheel 4
104 Square End Cap 1
105 @13.5 x 54L Spring 1
106 15.9 x 22mm_ Powder Metallurgy Sleeve 4
107 Scale Arrowhead 2
108 Safety Cover 1
109 Gas Cylinder 1
110 Rotate Disk 1
112 Steel Cable 1
116 i@12 x O18 x 8L_ Powder Metallurgy Sleeve 2
17 125.4 x 50.5 x 14.3mm_Square End Cap b
118 Pedal Foam 2
119 M5 x PO.8 x 25L_Socket Head Cap Bolt \24
120 M6 x P1.0 x 15L_ Socket Head Cap Bolt 14
121 M6 x P1.0 x 20L_ Socket Head Cap Bolt 8
122 M6 x 25L_ Socket Head Cap Bolt 4
123 M6 x 55L_Socket Head Cap Bolt 1
124 M8 x P1.25 x 12L_ Socket Head Cap Bolt 8
125 M8 x P1.25 x 20L Socket Head Cap Bolt 4
126 |M6 x P1.0 x 12L_ Socket Head Cap Bolt 16
127 M12 x P1.75 x 120L_ Socket Head Cap Bolt 1
130 M10 x P1.5 x 75L_Socket Head Cap Bolt 3
131 M6 x 38L_ Socket Head Cap Bolt 2
132 3/8" x 2" Hex Head Bolt 4


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
133 M6 = P1.0 x 40L_Hex Head Bolt 3

134 5/16" x UNC18 x 3/4" Hex Head Bolt 14
135 5/16" x UNC18 « 1-1/4 Hex Head Bolt 1
136 5/16" x 5/8" Hex Head Bolt 2
137 Mé8 = P1.25 x 25L_Hex Head Bolt 4
138 M10 x 40L_Hex Head Bolt 4
139 M5 x 12L Socket Head Cap Bolt 4
140 3/8" x UCN16 x 3-1/4" Hex Head Bolt 2
141 3.5 x 12mm_Sheet Metal Screw 12
142 45.5 x 415 x 1T_Flat Washer 4
143 M5 x 12mm _Phillips Head Screw 21
144 M5 x 20mm_Phillips Head Screw 2
145 M5 x 6mm_Phillips Head Screw p
146 M6 x 10L_ Phillips Head Screw 4
147 M4 PO? x 10L Phillips Head Screw 4
148 5/16" x UNC18 x 3/4" Hex Head Bolt 1
149 Mé x 20mm _ Button Head Socket Bolt 4
150 M8 =x P1125 x 25L Button Head Socket Bolt 3
15] M6 x 10L_ Button Head Socket Bolt 4

152 5/16" x UNC18 x 1-3/4" Button Head Socket Bolt__|2

N53 __|M8x P1.2516L_Hex Head Bolt p

154 3/8" x» UNC16 x 2-1/2" Hex Head Bolt 2
155 M5 x 12L_Phillips Head Screw 8
156 M5 x 6L Phillips Head Screw 4
158 M5 x 12L_ Flat Head Phillips Screw 10
160 M5 = P0.8 x 10L Flat Phillips Head Screw 8
161 M6 x 10L Flat Phillips Head Screw 4
162 M6 = 57L_Idle Wheel Screw 1
163 Mé& x 80mm _| Bolt 1
164 5 x 1,57 Split Washer fs|
65 M6 x 1T_Soplit Washer 12
166 8 x 1.5T Split Washer 19

167 3/8" x G25 x 2.0T Flat Washer 6


=== OCR SUPPLEMENT, PDF PAGE 53 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
168 @5 x @12 x 1.0T_Flat Washer 20
169 @1/4" x 13 x 1.0T_Flat Washer 5
170 @3/8" x @30 x 3T Flat Washer 14
172 @8.5 x O18 x 1.5T Flat Washer 12
173 @8.5 x @26 x 2.0T_ Flat Washer {2
174 @12.7 x @26 x 2.0T Flat Washer 1
175 M6 x P1.0 x 10L_ Socket Head Cap Bolt {2
176 @6 x O19 x 3.0T Flat Washer 21
177 @1/4" x @16 x 1.0T_ Flat Washer 4
178 @5/16" x 16 x 1.5T Flat Washer 6
179 @6.6 x @12 x 1.5T Flat Washer 16
181 M5 x PO.8 x 12L_Phillips Head Screw 12
183 3 x 20mm_Tapping Screw 4
184 @8 x 23 x 1.5T Curved Washer \2
186 @8 x @18 x 3T Knurled Lock Washer 4
187 M6 x 6T_Nylon Nut 6
188 M5 x 5T_ Nylon Nut 1
189 M8 x 7T_ Nylon Nut 5
190 8" x UNC16 x 7T Nylon Nut 10
191 Ms x P1.25 x 6T_Nylon Nut 5
192 M10 x 8T_Nylon Nut 4
1193 5/16" x 6T_ Nylon Nut 13
194 10 x 2T_ Split Washer 2
195 @45 x 21.8 x 2.5T Flat Washer \2
197 3/8" x UNC16 x 1-3/4" Socket Head Cap Bolt 2
M12_ Nylon Nut 1
M6 x P1.0 x 5T Nut 4
E5 E-Clip \2
@10 C Ring 2
O16 C Ring 2
@17_C Ring 3
@28 Inner Snap Ring 10
M6 x 719L_ Nut 4


=== OCR SUPPLEMENT, PDF PAGE 54 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
12/14mm_Wrench 1
13/14mm_Wrench 1
10mm_Wrench 1
5mm_L Allen Wrench 1
8mm_L Allen Wrench 1
Phillips Head Screw Driver 1
Swing Arm Drive Weldment 2
216 3/8" x 3/4" Hex Head Bolt 12
217 @3/8" x @19 x 1.5T Flat Washer 4
218 @10 x 21.3 x 7.8T Curved Washer 8
Wire Cap 2
Block 1
Optical Sensor Board (CS63008-00) 1
Optical Sensor Board (CS63008-10) 1
1550mm_ Computer Cable 1
250mm_Encoder Cable 1
100mm_DC Power Cord 1
650mm _Hall Sensor Cable 1
1550mm_ Handpulse Wire (Upper) 1
1550mm_Handpulse Wire (Lower) 1
Power Adapter 1
Power Cord (Optional) 1
Sticky Banding Stripe 2
Sticky Banding Stripe A
Seat Belt 1
32 x 2.5T Round End Cap 2
Swivel Handle 2
Swivel Handle Range Limiter b
@5 x 16L_ Tapping Screw 2
800mm _Handpulse Wire 1
800mm_Handpulse Wire (White) 1
100mm _ Connecting Wire 1
Short Phillips Head Screw Driver 1
10 x 2T_ Split Washer 12


=== OCR SUPPLEMENT, PDF PAGE 55 ===
<!-- render-vs-extraction: 74 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[244 Axle Positioning Ring 2
245 @18 x @32 x 1.5T Nylon Washer 4
46 M5 x 10mm _Slotted Set Screw 4
ar JAxle 4
249 @17 x 0.3T_ Wave Washer 2
250 5/16" x @20 x 3.0T_ Flat Washer 4
51 M8 x 10 x 30L Bolt 4
52 @10 x @24 x 3.0T_ Nylon Washer 14
11.9 x O8.5 x 15mm _Rod End Sleeve 1
59 Powder Metallurgy Sleeve 2
61 @3/8" x @20 x 3T_ Flat Washer A
62 Buckle 4
263 Snap Seat 4
64 Transportation Wheel Fixing Plate 1
99 @5/16" x 16 x 1T_ Flat Washer 1
300 Nylon wheel 3
309 M8 x 30mm_Flat Head Socket Screw 6
310 M5 x P0.8 x 25L_Flat Head Socket Screw \2
311 M5 x P0.8 x 45L_ Socket Head Cap Bolt 1
312 @5 x @10 x 1.0T Flat Washer 1
313 M8 x 1.25 x 6.5T_ Square Nut 6
[330 Release Lever \2
331 Nylon Handgrip 2
332 Lever Anchor 1
333 Seat Front/Aft Adjustment Lever 1
[334 @13.5 x 30mm_Spring 1
335 Handgrip 1
336 Rubber Foot Cover 2

337 Stee! Cable


=== OCR SUPPLEMENT, PDF PAGE 56 ===
<!-- render-vs-extraction: 117 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8. Wiring Diagram
MS7000 Wiring Diagram

Console
Hand pulse
eaw—
ocv~-— > a
Pe Mo Cole
=e _——— -
= rat Me a
Cranes. =5Y +5¥
bd Vee MIO YE) >
ie owes Cmte °
———Se SS a
EE ee ae eee ee ee
fats wy
Lad Rad aS hy
|_210 _) ___aadt See _j _ iat Ry
red OMe u
ria. lualt G oY ay
tis | Seren a be] : vy

r =.
See ey See

ETT] tk] Pes M ¥
Ant_™
Fi} Licht Give | vim | tae apis = aE 2 : — —_
~ mea | oD TO te) wae Tay 1 sv Pe | vemse | uroneveo| =]
3s nee oro 0

aad Ts | aaa =

ba aD ee
jie Se. | Cote coon Lars Lis. Bee, |
ed. vin] izy rm ~ Sv Sv “Sa smi) vv
= Bt 222 2 Pet eT we : ——" OR) 2)
a a ae se 4 BRM,

2 «sv e3v

0

Switching Power Supply
90 ~ 260 VAC input
12 VDC output, 1.6A

IR Sensor Board (One IR Reflective Sensor Board

sensor version)
Brake RPM

Brake Motor

we
aS

Reflective
Encoder Disc
