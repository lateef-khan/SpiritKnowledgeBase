<!-- Source: XBR55_ENT_XR329-SB013-01 Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XR329-SB013-01
    Service Manual




1               Service Manual
1. XR329-SB013-01 Outlines




            2                Service Manual
3   Service Manual
2. Electronic Parts




         4            Service Manual
Upper Controllers




         DISPLAY




                    5   Service Manual
                     Cooling FAN




       Speaker




Thumb Switch




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

GENERAL INFORMATION

CONSOLE
   Contain keys control and TFT LCD touch panel.

TENSION MOTOR
   Work voltage:DC 4.5~7.5V
   Control resistance increases and decreases.




                                                                             9                                                                   Service Manual
4. XR329-SB013-01 Product Operation




                 10              Service Manual
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
5. XR329-SB013-01 Unit Block Diagrams




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
7. XR329-SB013-01 Error Messages /
        Troubleshooting




                22               Service Manual
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
      XR329-SB013-01
ELLIPICAL CIRCUIT DIAGRAM




            27              Service Manual
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
9. Troubleshooting




      34             Service Manual
9-1   Console Disassembling and assembling
      1. Use Phillips Head Screw Driver (114) to release four pcs of M5 × 12 m/m_Phillips Head Screw (99) and unplug Computer
         Cable (44), 2100m/m_Handpulse Wire, Coiled (133) and 2100m/m_Switch Cable (Upper)_(148), and then replace the
         Console Assembly (19).




      2. Reverse above step to return Console Assembly (19).




                                                            35                                                 Service Manual
9-2   Console Mast and Cover (Take the console apart first.)
  1. Take the console apart first.
  2. Then use 12/14 m/m wrench (112) to release 2pcs of 5/16" x5/8" Hex Head Screws (68), 2pcs of 5/16"x1.5T Split Washers
     and 2pcs of 5/16”x18x1.5T Flat Washers (76) and the Handlebar Assembly (3) can be released, as shown in figure.




  3. Reverse above step to return the Handerbar (3)
  4. Separate Console Mast Cover(31) from Front Shroud(L.R)(29).(30) at left and right sides of the seam with nail or something
     flat (figures 2.3) and release the latches which lock Console Mast Cover(31) and Front Shroud(L.R)(29).(30) together to pull
     up Console Mast Cover(31) 2.
     Unscrew 6pcs of 5/16" × 5/8" Hex Head Bolt(68), 4pcs of 5/16" × 18 × 1.5T flat Washer(76) and 2pcs of 5/16" ×19 × 1.5T
     Curved Washer(83) with the 12m/m Wrench, to pull outthe Console Mast (2) as shown in figure.




                                                              36                                                  Service Manual
5. To resume Console Mast (2), guide the Computer Cable (44) and Hand Pulse Sensor Assembly W/Cable (45) through the
   Console Mast (2) and out of console securing plate (2~3) then tighten 6pcs of 5/16"×5/8"Hex Head Bolts (68), 6pcs of
   5/16"×18×1.5T Flat Washers (76) and 2pcs of 5/16"×19×1.5T Curved Washers (83) with 12m/m open wrench.




                                                        37                                               Service Manual
9-3    Crank Arm and Pedal
      1. Use 13/15mm Wrench to turn the left pedal clockwise and the right pedal counterclockwise to take off those pedals.




      2. Turn Pedals reversely respectively to return them.
      3. Take off the Crank Arm End Cap (28), and then use T-Wrench or Plug Wrench to release the Nut, as shown in figure 3 and
         4.




      4. Use proper tool to secure Crank Arms (51L&51R) and release them with Hex Wrench, as shown in figure 4.
         To resume the Crank Arms (51L&51R), use power tool or hammer to secure them and return the Nut (108) back to the
         Crank Axle (8) tighten. Return Crank Arm End Cap (28) back to Crank Arms (51L&51R).



                                                                38                                                 Service Manual
9-4   Front Shroud & Round Disk
      1. Dismantle and take apart Crank Arm (51L. 51R)
      2. Remove the round disk (34) with fingers.
      3. When assemble the round disk pay attention to the direction, because latch has different size, FRONT facing forward and
         then assemble.( figures 4.)




      4. Dismantle and take apart Console Mast Cover (31)
      5. To release Left Front Chain Cover (29), use Phillips Head Screw Driver to release 5pcs of ø3.5x12 Self Tapping Screws
         (103) and 3pcs of 5x16 Tapping Screws (101).
      6. To release Right Front Chain Cover (30), on the mainframe, unscrew 2pcs of Ø 3.5x20 Self Tapping Screws (107) with 2pcs
         of Ø 5 x16x1.5Tflat Washers (78) then, on the Right Front Chain Cover, unscrew 2pcs of 5x16 Tapping Screws and unplug.
      7. When reserve the right front shroud (30) to main frame use Ø3.5 × 16m/m_Sheet Metal Screw(103), 3/16"x15mmx1.5T
         Flat Washer(78) to slightly fixed and combined with left shroud(29) and right shroud(30) and use Ø3.5 ×16m/m_Sheet
         Metal Screw(103)*7pcs to lock and then adjust crank axle(8) & bottom cover to relative position and use 5 × 16m/m(101)
         tapping screw to fixed .




                                                              39                                                  Service Manual
9-5    Gear Motor, Steel Cable and Reed Switch Sensor
      1. Take both left and right front shrouds apart. (29)。
      2. Remove the Steel Cable (62) on the Flywheel (55). Be careful to treat the aluminum plate gently as it deforms easily to
         cause scratching noises as shown in figure.




      3. Use Phillips head screw driver to remove two M5 × 12m/m_Phillips Head Screws (99) on the Gear Motor (43) and take it
         apart as shown in figure.




                                                               40                                                 Service Manual
4. Use Phillips head screw driver to remove M5 × 12m/m_Phillips Head Screw (99) and take the Reed Switch Sensor (46)
   apart, as shown in figure.




5. To adjust the cable range with the Console (19) when reassembling the Steel Cable (62), increase the resistance to max.
   level with the console and tighten the Steel Cable with screw. The aluminum plate is at lowest position when the resistance
   is the maximum. Use two 8 mm open end wrench to secure, as shown in figure.




                                                           41                                                  Service Manual
9-6    Drive Pulley Axle and Drive Pulley
      1. Disassemble Front Shrouds (29.30) and the Drive Belt (54).
      2. Use C-ring pliers to release Ø 20_C-ring (86) to take apart Crank Axle (8), as shown in figure 1.




      3. Use 11mm_wrench to to unscrew Crank Axle (8) and Drive Pulley (20), 4 pcs of 1/4" × 3/4"_Hex Head Bolts (66) together
         with 8 pcs of 1/4" × 13 × 1T_Flat Washers (72) and 4 pcs of 1/4" × 8T_Nuts (90), and take apart Drive Pulley (20), as
         shown in figure 2.




      4. Reverse procedures to return parts.




                                                                 42                                             Service Manual
9-7   Flywheel and Drive Pulley
 1. Take both left and right front shrouds(29)(30).
 2. Use 13 mm open end wrench to loosen the Nyloc Nut (88) on the J Bolt (87) and remove the J Bolt (87), as shown in figure.




 3. Use 6 mm Allen wrench and 14 mm open end wrench to release 3/8" × 3/4"_Button Head Socket Bolt (81), 3/8" × 7T_Nyloc
    Nut (89) and 3/8" × 19 × 1.5T_Flat Washer (77) then take the Idler Wheel Assembly (10) apart.




                                                              43                                                 Service Manual
4. Remove the Drive Belt (54), as shown in figure.




5. Remove the steel cable on the Flywheel (55) and use 15 mm open end wrench to release 3/8"-UNF26_Nut (121) on the
   Flywheel (55) to remove the Flywheel (55), as shown in figure.




                                                       44                                             Service Manual
6. To resume, hang the Drive Belt (54) on the Flywheel (55) then install the Flywheel on the Mainframe (1). Try to align the
   Flywheel with the Pulley (20) in line and turn the Nut (120) outward till it touches the Mainframe (1) then use 15 mm and 17 mm
   open end wrenches to tighten the Nut (120) and 3/8"-UNF26_Nut (121). Tighten the Nut (119) and 3/8"-UNF26_Nut (121) at
   the other side, as shown in figure.




7. Use 6 mm Allen wrench and 14 mm open end wrench to tighten 3/8" × 3/4"_Button Head Socket Bolt (81), 3/8" × 7T_Nyloc Nut
   (89) and 3/8" × 19 × 1.5T_Flat Washer to secure Idler Wheel Assembly on the Mainframe (1) then turn reversely 1/4 turn to
   release a little then install J-Bolt (87) with M8 × 7T_Nyloc Nut (88) onto the Idler Wheel Assembly (10) and the Mainframe (1),
   as shown in figure.




                                                               45                                                  Service Manual
8. Return the Drive Belt (54) back to Drive Pulley (20) and the Flywheel (55), then turn the Drive Pulley to make sure the belt
   turns smoothly in the center. Loosen the 3/8"-UNF26_Nut (121) on the Flywheel (55) and adjust both Nuts (119) and (120) if
   the Belt is not in the center. Secure when alignment is done. Use 13 mm wrench to tighten M8 × 7T_Nyloc Nut (88) on the
   J-Bolt until Idler Wheel (10) pressing the belt tightly. Use belt tension gauge to make sure the tension reads 450N. (Note 1).
   Turn the Drive Pulley (20) to make sure that the Drive Belt (54) is in the center without falling apart, as shown in figures 1 &2).




9. Assemble the Steel Cable (62) to the Flywheel (55) at the end.
Note: If the Drive Belt (54) were new, it has to adjust the tension of value to be 540N, because the belt has ductility and the tension
of value will be decreased while using a period of time.




                                                                 46                                                     Service Manual
9-8    Disassembling/Assembling of Seat Carriage Cover and Seat Back Bracket
      1. Use Phillips Head Screw Driver to release 4 pcs of Ø 4 × 16m/m_Sheet Metal Scre (105).




      2. Use two 14mm_Wrenchs to release 2 pcs of 3/8" × 4"_Hex Screw (67) and 2 pcs of 3/8" × 7T _Nyloc Nut(89).




                                                             47                                              Service Manual
3. Use a 12 mm and 13 mm Wrench to release a 5/16" × 1- 1/4"_Hex Screw (70) and a 5/16" × 18mm × 1.5T_Flat Washer
   (76), and then you could take Seat Back Assembly (5) and Mesh Seat Back (63) off.




4. Loose the cable from the Mesh Seat Back (63).
5. Reverse above step to resume




                                                    48                                              Service Manual
9-9   Release Lever and Steel Cable
      Steel Cable (58):
      Use the 8m/m_Wrench to fix the Nut of Gas Cylinder (See figure 1). Use the Wrench to release the Head Bolt of Release
      Lever (40) (See figure 2) and also remove the Steel Cable (280L) (58). Reverse above steps to resume.




      Release Lever (40):
      Remove the Steel Cable (280L) (58) first and use 12/13m/m_Wrench to release the 5/16" × UNC18 × 1-1/2"_Hex Head Bolt
      (188) x1pc, Ø 5/16" × Ø 18 × 1.5T_Flat Washer (76) x1pc, 5/16" × 6T_Nyloc Nut (91) x1pc. (See figure 3) and the Release
      Lever (40) & Chen Chin Torsion-Spring (186) can be released from the Seat Carriage (4). Put the Chen Chin Torsion-Spring
      (186) on the Release Lever (40) while assembling. Reverse above steps to resume. Check for the Release Lever (40) if
      machine motion feels unsmooth. If it feels unsmooth, please adjust the Screws. (See figure 3)




                                                             49                                                 Service Manual
9-10 Gas Cylinder (Remark 8)
     1. Use Phillips Head Screw Driver to loosen 2 pcs of M5 × 12_Phillips Head Screw (99), and then take off the Seat Carriage
        Cover (125), as shown in figure 1.




     2. Use 2 pcs of 13mm_wrenchs to release a 5/16" × 2- 1/2"_Hex Head Screw (69), a 5/16" × 18mm × 1.5T_Flat
        Washer (76), and a 5/16"_Nyloc Nut (91), as shown in figure 2.




                                                             50                                                 Service Manual
3. Use a 12 mm and a 13mm wrench to release a 5/16" × 1- 1/4"_Hex Head Screw (70), a 5/16" × 18mmx1.5T_Flat
   Washer (76), and a 5/16"_Nyloc Nut (91), as shown in figure 3.




4. Use 8 mm Wrench to release the screws Secured on the steel cable, and then take Steel Cable (58) and Gas Cylinder
   (57) apart, and take Gas Cylinder (57) off, as shown in figure 4.




5. Reverse the above steps to return parts.




                                                     51                                               Service Manual
9-11 Seat, Seat Handle Bar and Handpulse W/Cable Assembly
     1. Take Left and Right Bottle Holder (38, 39) and Release Lever (40) off.
     2. Use Phillips Head Screw Driver to release four M6 × 15m/m_Phillips Head Screws (98) and take the Seat (61) apart, as
        shown in figure 1.




     3. Use two 14mm Open End Wrenches to release two 3/8" × 2 3/4"_Hex Head Bolts (175) four 3/8" × 2"_Hex Head Bolts,
        six 3/8" × 7T_Nyloc Nuts (89) and six 3/8" × 19 × 1.5T_Flat Washers, which secure Seat Carriage (4), to take apart Seat
        Handle Bar (6), as shown in figures 2.




                                                             52                                                 Service Manual
4. Take apart HGP Wire Grommet (126) which secure Handpulse Assemblies (27). Use Phillips Head Screw Driver to
   release four Ø 3 × 20m/m_Tapping Screws and take Handpulse Assemblies (27) apart, as shown in figure 3 and 4.




5. Reverse above steps to return parts.




                                                   53                                              Service Manual
9-12   Buttons on The Handle Bar (Remark 9)
       1. Use your hand or the tool with flat bead to take the Handgrip End Cap (144) off and get Resistance Button W/Cable (145)
          out, as shown in figure 1.




       2. Take apart Resistance Button W/Cable (145) and Switch Cable (lower) (151), as shown in figure2.




       3. Tear Up/Down Handgrip Resistance Lable (146 and 147), and then take off Handgrip Button W/Cable (145).




                                                               54                                                 Service Manual
     4. Pay attention to reverse the Headgrip End Cap’s direction. Must match the rasied part on Handlegrip End Cap (144) with
        the concave part on Handbar (6).




9-13 Rear Shrouds and Harness
     1. Use Phillips Head Screw Driver to release 7 pcs of Ø 3.5 × 16m/m_Sheet Metal Screws (103) and 2 pcs of 5 ×
        16m/m_Tapping Screws (101) which are on left Rear Shroud (35). Unplug 300m/m_Handpulse Wire, Coiled (26),
        2100m/m_Handpulse Wire, Coiled (133), and 2100m/m_Switch Cable (Upper)_(148), and then left Rear Shroud (35) can
        be taken apart.




                                                            55                                                  Service Manual
2. On the Right Rear Chain Cover (36), unscrew Ø 3.5x16 Self Tapping Screws (103) with 3/16" × 15mm × 1.5T_Flat
   Washers (78) and 2pcs of 5x16 Tapping Screws (101) and the Right Rear Chain Cover (36) can be released as shown in
   figure)。




3. Use special tools to remove nut from hand pulse cable sensor assembly(26) and handle switch bracket and then could
   separate right/left rear shroud.
   When reserve the rear shroud use flat washer 5/16"×16×1T(127) place on rear shroud (R) plastic column and then
   through a hole of plastic column to main frame (1) and use Ø 3.5 × 16m/m_Sheet Metal Screw x 1pc, 3/16" × 15mm ×
   1.5T_Flat Washer (78) slightly fixed and then combines left & right rear shroud(35)(36), and locked with Ø 3.5 ×
   16m/m_Sheet Metal Screw*6pcs,and adjust bottom cover position and use 5 × 16m/m_Tapping Screw(01110) x4pcs to
   fixed on the main frame.




                                                     56                                                Service Manual
9-14 Seat Carriage
     1. Disassemble Rear Shrouds (35, 36).
     2. Use Phillips Head Screw Driver to 2 pcs of M6 × 15_screws (98) and Seat Stop Axles (11) can be taken apart, as shown
        in figure 1. Pull up Release Lever (40) to take Seat Carriage (4) apart.




     3. Use Phillips Head Screw Driver to release four M6 × 10L_Flat Phillips Head Screws (161), 4 pcs of 1/4" × 16 × 1.0T_Flat
        Washer and four Sleeve (162). Then use 13 mm Open End Wrench to release four M8 ×7T _Nyloc Nuts (88) and four Ø 8
        × Ø 18 ×3T_Knurled Lock Washers (79) and take apart Seat Wheel Adjustment Plate (9L, 9R), as shown in figures 2 and
        3.




     4. Disassemble Rear Shrouds (35, 36).

                                                             57                                                  Service Manual
5. Use Phillips Head Screw Driver to 2 pcs of M6 × 15_screws (98) and Seat Stop Axles (11) can be taken apart, as shown
   in figure 1. Pull up Release Lever (40) to take Seat Carriage (4) apart.
6. Use Phillips Head Screw Driver to release four M6 × 10L_Flat Phillips Head Screws (161), 4 pcs of 1/4" × 16 × 1.0T_Flat
   Washer and four Sleeve (162). Then use 13 mm Open End Wrench to release four M8 ×7T _Nyloc Nuts (88) and four Ø 8
   × Ø 18 ×3T_Knurled Lock Washers (79) and take apart Seat Wheel Adjustment Plate (9L, 9R), as shown in figures 2 and
   3.




7. Use M4 Allen wrench and 10m/m Wrench open end wrench to release M5×45m/m Socket Head Cap Bolt (171) and
   M5×5T Nyloc Nut (173) as shown in figure.




                                                        58                                                 Service Manual
8. Use Phillips Head Screw Driver to release two M5×25m/m Flat Head Socket Screws (169) then pull out Lever Anchor
   (168) to take apart Seat Front/Aft Adjustment Lever (167) as shown in figure.




9. Use M5 Allen wrench and 11mm Open End Wrench to take apart M6 × 38m/m_Socket Head Cap Bolt (93), 1/4" × 13 ×
   1T_Flat Washer (72) and M6_Nyloc Nut (129), and then take off Seat Position Latch (12), as shown in figure 5.




                                                    59                                              Service Manual
10. To install Seat Front/Aft Adjustment Lever (167), consolidate Seat Front/Aft Adjustment Lever (167) and Lever Anchor
    (168) and secure with two M5×25m/m Flat Head Socket Screws (169) then place Spring (104) in Seat Position Latch (12)
    and secure with a M5×45m/m Socket Head Cap Bolt (171) by going through Seat Position Latch (12), Spring (104), ø 15×
    6×4T Nylon Washer(170), Seat Front/Aft Adjustment Lever(167) and ø 3/16"×10×1T Flat Washer (172), from top to
    bottom and tighten with M5× 5T Nyloc Nut (173).




11. Use 13mm Open End Wrench to slightly tighten 4 pcs of M8 × 7T_Nyloc Nut, 4 pcs of Ø 8 × Ø 18 × 3T_Knurled Lock
    Washer (79) , and 4 pcs of Seat Wheel Adjustment Plate (9L&9R) on Seat Carriage (4).
12. Install the completed Seat Carriage (4) onto the Aluminum Track (14) and adjust the position of Seat Wheel Adjustment
    Plate (9L.9R) with 11 and 13m/m Wrenches by using 11m/m Wrench at front of left side and turn counterclockwise first,
    then using 13m/m Wrench to tighten M8 × 7T Nyloc Nut (88) (Figure 1). At the front of right side, use 11m/m Wrench by
    turning clockwise and use 13m/m Wrench to tighten M8×7TNyloc Nut (88). (Figure 2). Turning hex bolt at the rear of right
    side counterclockwise and clockwise at the rear of left side to secure.




                                                         60                                                  Service Manual
13. To test the smoothness, if seat carriage is too tight, reversely adjust four screws until the smoothness is acceptable.
    Tighten four Sleeves (163) with four 1/4" × 16 ×1.0T_Flat Washers, M6 × 10L_Flat Phillips Head Screws (161) to secure.
    Seat Stop Axle (11) and Rear Shrouds (35, 36) can be installed.




                                                        61                                                  Service Manual
9-15   Aluminum Trail and Stabilizer Cover
       Induction Brake Controller
       After taking Rear Chain Cover (L/R)_(35, 36), unplug the cables on the Induction Brake controller (43), and then use Phillips
       Head Screw Driver to release 2 pcs of 5 ×19_Tapping Screws and take apart Induction Brake Controller (43), as shown in
       figure 1.




       Aluminum
       Take apart Rear Shrouds (35,36) and Seat Carriage (4), and then use 12mm Open End Wrench to release 6 pcs of 5/16"
       ×3/4"_Hex Screws (94), 5/16" × 3/4"_Flat Washers (160), and 5/16" × 1.5T_Spilt Washers (82), and then take apart
       Aluminum (14), as shown in figure 2.




                                                                62                                                   Service Manual
Step Cover
Take apart Rear Shroud (35, 36) and Front Shroud (29, 30), and then use Phillips Head Screw Driver to release 4 pcs of M5
×12_Head Screws (99), and then take apart Step Cover (33), as shown in figure 3.




                                                       63                                                  Service Manual
9-16    Console
       Q Display won’t come on:
       A:
          1. Follow procedures below for checking when your display couldn’t show anything.
          2. Make sure that Console (19) and computer cable (44) are connected properly, as shown in figure 1.
          3. Use multi-meter to check output voltage at each connect contact.

       Q No speed readout:
       A:
          1. If the display is on but without speed readout, disassemble Front Shroud (29) and make sure 9P computer cable (44)
             and Hall Sensor (46) are properly connected, as shown in figure 2.
          2. If there is no problem with the connection, there is problem with either Hall Sensor (46) or the magnet. (56). Use
             another magnet to test Hall Sensor (46), replace it when necessary.

       Q No pulse displayed
       A:
          1. When the console displays but is without heart beat. Check if Hand Pulse Sensor Assembly W/Cable (45) is properly
             connected to Console assembly (19) (Figure 1), or if Handpulse W/Cable Assemblies (21.27) are properly connected
             with Hand Pulse Sensor Assembly W/Cables (26), as shown in figure.
          2. If there is no problem with installation, dismantle Rear Shroud (L) (35) and check if Handpulse W/Cable Assemblies (26)
             are properly installed with Hand Pulse Sensor Assembly W/Cable (45), as shown in figure.
             If all are connected properly, use multi meter to check cable continuity.
       Remark:
       Console and related parts were factory tested and it is rare that the unit fails at this part.




                                                                64                                                   Service Manual
9-17    Belt Slipping and Falling-off
       Q:Slippage
       A:
            1. Disassemble Front Shrouds
            2. Use 13m/m Wrench to turn M8×7T Nyloc Nut (88) clockwise until sound wave frequency falls between 450N. However,
               since the machine is with drive belt, slippage is possible depending on the weight of the user or the way the user uses.
               Generally, slippage is rare, as shown in figure.
            3. Since Drive Belt (54) stretches and wears, it is normal that Drive Belt (54) gets loose as time lasts.

       Q: Drive Belt falling off
       A:
         Follow Procedure #5 in section I to install, Drive Belt (54) requires to turn back and forth to see if it falls off. Adjust Drive Belt
         (54) on notch beyond against the side it falls off. If it still keeps falling off, try to replace Drive Pulley (20), Idler Wheel
         Assembly (10) or Induction Brake (55). If it still keeps falling off, the unit might have been seriously dropped and the frame
         were deformed and the whole unit requires to be replaced. It is rare that the unit fails at this part because it would be tested
         in the factory before shipping. This problem will occur when the unit drops from a high and incorrect way to put on the
         ground.




                                                                      65                                                       Service Manual
9-18
       Q: Noises
       A: Noises are mostly caused by loose screws/bolts, sometimes rubbing or poor smoothness due to mechanical
       deformity/shifting may also causes noises:
           1. Noises at Seat Carriage (4) are mostly caused by loose Seat Wheel Adjustment Plate due to long time usage and
              usually accompanied with serious play. Procedures 10 in section I could re a remedy, as shown in figure 1.




          2. Noises at left/right Pedals (116) (117): Pedals wear out could cause poor smoothness and noises. Replacing Pedals
             (116) (117) as shown in figure 2.




                                                             66                                                 Service Manual
3. Crank Arm (51L.R) loose can also cause poor smoothness and noises, although the chance is low. Tighten, as shown
   in figure 3, to remedy noises




4. If noises still persists after disassembling Front Shrouds (29, 30), find the spot where noises initiate and replace parts
   when necessary.




                                                        67                                                    Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS I

jenuepy 8dIAlas
LO-€LOgS-6cbEuUxXx


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SOUI/INO LO-ELOES-6cEUX *}


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS ¢

AV'IdSIG

Liles

v

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
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

uoHesad¢— JONPOJd LO-ELOGS-6ZEYX “fp


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
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

sweibeig YIO/g LUN LO-€LOGS-6ZEYX 'S


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS C]

HOLIMS :
WAMOd aMOd

YONAS YOLOW
Idd NOISNAL

YaIWAdS

NV davod AV'TdSId

NIANI
HOLIMS
aWNHL

YHAISOda Ves IGNVH

AWN

YH SSH TSMIN 4H

uoneinbiyuo0y oyIg


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Gui, pue SuoljaauU0y aISeg “9g


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS LI

(SNId 9) qHDUVHO

HOLIMS €INNHL q1gVD WALSAS

avast TONVH
YH LOVINOO
qauvod AdN

YH SSHTAMIM,
cO-LOOOLVLV

NI ANTT

u YANVadS "T MaNVadS NVd DNITIOOD

SUOI]D9UUOY 211M pseog Ae\dsig


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
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[OUD SOTAIOS :

YONHS

481d

dIdDANVH

WHILSAS Of

09-T-COOTTSD-M

HOLIMS
qINDHL
THAYT

SUOI]OOUUOYD OJIM PLO BORj19}U] BJOSUOD aU


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
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

burnlooysaqnol]
/ sabessay 401 L0-€LOGS-6ZEYX *Z


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

Disol Key signal travels to the display.The main program IC then sends a
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
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
aa —
L.
_ > —. ~ a en| 4 [-
<a c L SARRARARADAan ool

q cy cen

ae | [Ol me


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


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9-14 Seat Carriage
1. Disassemble Rear Shrouds (35, 36).
2. Use Phillips Head Screw Driver to 2 pcs of M6 x 15 screws (98) and Seat Stop Axles (11) can be taken apart, as shown

in figure 1. Pull up Release Lever _ to take Seat Carriage (4) apart.

3. Use Phillips Head Screw Driver to release four M6 x 10L_Flat Phillips Head Screws (161), 4 pcs of 1/4" x 16 x 1.0T_Flat
Washer and four Sleeve (162). Then use 13 mm Open End Wrench to release four M8 x7T _Nyloc Nuts (88) and four 08
x O18 x3T_Knurled Lock Washers (79) and take apart Seat Wheel Adjustment Plate (9L, 9R), as shown in figures 2 and
3.

4. Disassemble Rear Shrouds (85, 36).

57 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 58 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5. Use Phillips Head Screw Driver to 2 pcs of M6 x 15 screws (98) and Seat Stop Axles (11) can be taken apart, as shown
in figure 1. Pull up Release Lever (40) to take Seat Carriage (4) apart.

6. Use Phillips Head Screw Driver to release four M6 x 10L_Flat Phillips Head Screws (161), 4 pcs of 1/4" x 16 x 1.0T_Flat
Washer and four Sleeve (162). Then use 13 mm Open End Wrench to release four M8 x7T _Nyloc Nuts (88) and four @8
x O18 x3T_Knurled Lock Washers (79) and take apart Seat Wheel Adjustment Plate (9L, 9R), as shown in figures 2 and
3.

7. Use M4 Allen wrench and 10m/m Wrench open end wrench to release M5x45m/m Socket Head Cap Bolt (171) and
M5x5T Nyloc Nut (173) as shown in figure.

58 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 60 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
10. To install Seat Front/Aft Adjustment Lever (167), consolidate Seat Front/Aft Adjustment Lever (167) and Lever Anchor
(168) and secure with two M5x25m/m Flat Head Socket Screws (169) then place Spring (104) in Seat Position Latch (12)
and secure with a M5x45m/m Socket Head Cap Bolt (171) by going through Seat Position Latch (12), Spring (104), @15~x
6x4T Nylon Washer(170), Seat Front/Aft Adjustment Lever(167) and @3/16"x10x1T Flat Washer (172), from top to

bottom and tighten with M5x 5T Nyloc Nut (173).

11. Use 18mm Open End Wrench to slightly tighten 4 pcs of M8 x 7T_Nyloc Nut, 4 pcs of O@8 x @18 x 3T_Knurled Lock
Washer (79) , and 4 pcs of Seat Wheel Adjustment Plate (9L&9R) on Seat Carriage (4).

12. Install the completed Seat Carriage (4) onto the Aluminum Track (14) and adjust the position of Seat Wheel Adjustment
Plate (9L.9R) with 11 and 13m/m Wrenches by using 11m/m Wrench at front of left side and turn counterclockwise first,
then using 18m/m Wrench to tighten M8 x 7T Nyloc Nut (88) (Figure 1). At the front of right side, use 11m/m Wrench by
turning clockwise and use 13m/m Wrench to tighten M8x7TNyloc Nut (88). (Figure 2). Turning hex bolt at the rear of right
side counterclockwise and clockwise at the rear of left side to secure.

60 Service Manual
