<!-- Source: 8.5R-784145 _MR2000-SB036-01_Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

8.5R-784145
(MR2000-SB036-01)
Service Manual
-------------------------------------------------------------------Table of Contents------------------------------------------------------------------------------

1. SERIAL NUMBER LOCATION .......................................................................................................................... 4

2. COMPONENT DESCRIPTION .......................................................................................................................... 5

3. PREVENTIVE MAINTENANCE ........................................................................................................................ 6

  3.1 CHECK FOR PEDALS AND CRANK ARMS ......................................................... 6
  3.2 CHECK FOR FRONT CONSOLE MAST ............................................................. 7
  3.3 CHECK FOR EMERGENCY STOP ..................................................................... 7
  3.4 CHECK FOR ROTATING STRUCTURE ASSEMBLY .............................................. 8

4. CONSOLE SETTING ........................................................................................................................................ 9

  4.1 BASIC FUNCTIONS ...................................................................................... 9
  4.2 MAINTENANCE MODE .................................................................................. 9
  4.3 ELECTRICAL WIRING DIAGRAM .......................................................... 16
  4.4 CIRCUIT BOARD ........................................................................................ 17
  4.5 LIST OF REQUIRED MAINTENANCE TOOLS .................................................... 19

5. TROUBLESHOOTING (ELECTRONIC) ........................................................................................................... 20

  5.1 NO POWER, CONSOLE DOESN’T LIGHT ......................................................... 20
  5.2 UART COMMUNICATION ERROR................................................................. 24
  5.3 NO REVOLUTIONS ..................................................................................... 25
  5.4 INCORRECT SYMMETRY VALUE ................................................................... 27

6. PART REPLACEMENT GUIDE ....................................................................................................................... 29

  6.1 CONSOLE REPLACEMENT .......................................................................... 29
  6.2 BRAKE COVERS REPLACEMENT.................................................................. 30
  6.3 PEDALS & CRANK ARMS REPLACEMENT ...................................................... 31
  6.4 CHAIN COVERS AND ROUND DISKS REPLACEMENT ....................................... 32
  6.5 DRIVE PULLEY AND DRIVE BELT REPLACEMENT ........................................... 33
  6.6 IDLER WHEEL ASSEMBLY AND FLYWHEEL REPLACEMENT ............................... 34
  6.7 BRAKE PAD REPLACEMENT ........................................................................ 34
  6.8 LOWER CONTROL REPLACEMENT ............................................................... 35
  6.9 ADJUSTMENT FOOTS AND TRANSPORTATION WHEELS REPLACEMENT ............. 36

7. TROUBLESHOOTING .................................................................................................................................... 37

  7.1 SLIP/SHEDDING OF DRIVE BELT ................................................................. 37
  7.2 NOISE/FOOT FEELING ............................................................................... 37
  7.3 HANDGRIP/WHOLE BIKE SWAY ................................................................... 37

8. ELECTRICAL SYSTEM WIRING DIAGRAM .................................................................................................... 45
1. SERIAL NUMBER LOCATION
2. Component Description


  Item          Part Name
    1        Console Assembly
    2          Brake Lever
    3          Console Mast
    4         Chain Cover(R)
    5         Crank Arm(R)
    6              Pedal(R)
    7              Handgrip
    8         Seat Release Lever
    9    Seat Rotation Release Lever
   10           Rail Assembly
   11      Seat Track Sheet Metal
                  Assembly
   12    Seat Rotation Release Lever
   13           Adjusting Rod
   14             Seat Back
3. Preventive Maintenance


3.1 CHECK FOR PEDALS AND CRANK ARMS

As Figure 3.1.1 and 3.1.2, check regularly if Pedals are loose.
Tighten left Pedal in counterclockwise direction and tighten right Pedal in clockwise direction.
As Figure 3.1.3 and 3.1.4, check regularly if Crank Arms are loose. Tighten up the nut of Crank Arms on both sides.




                            Figure 3.1.1                   Figure 3.1.2                Figure 3.1.3               Figure 3.1.4
3.2 CHECK FOR FRONT CONSOLE MAST

As Figure 3.2.1, check Socket Head Cap Bolts (M8x3 PCS) which are secured on Console Mast if they are loose.
If so, please tighten them up. (Resolve Console Mast sway issue)




                         Figure 3.2.1

3.3 CHECK FOR EMERGENCY STOP

As Figure 3.3.1, check if M5 × 40mm_Phillips Head Screw (1 PCS) is too tight and get the brake stuck or work improperly.
If so, Please loosen the screw. If not, please adjust the cable. (Resolve emergency brake issue)
                          Figure 3.3.1


3.4 CHECK FOR ROTATING STRUCTURE ASSEMBLY

As Figure 3.4.1, 3.4.2 and 3.4.3, check if Rotating Structure Assembly works smoothly.
Loosen the 4 screws which lock on Console Mast as Figure 3.4.1.
Pull out Rotating Structure Assembly as Figure 3.4.2.
Disconnect the connector of the three wirings to remove the O-ring as Figure 3.4.3 and 3.4.4.




                          Figure 3.4.1            Figure 3.4.2             Figure 3.4.3         Figure 3.4.4
4. CONSOLE SETTING


4.1 BASIC FUNCTIONS
Refer to the User’s Manual for detailed console operations.



4.2 MAINTENANCE MODE
Maintenance Mode is intended for troubleshooting purposes.
To enter Maintenance Mode, tap the Wi-Fi icon once and the clock in the status bar six times on the Home Screen.
4.2.1 Maintenance Mode Menu Structure
 Odometer
                   Android Version
                   Firmware Version
 Software
                   LCB Version
                   Console APP Version
                                                                 Treadmill
                                                                 Upright Bike
                                                                 Recumbent Bike
                   Machine Type                                  Recumbent Stepper
                                                                 UBE
                                                                 Rehab UBE
                   Communication
                   NFC Sensor
                                                                 Resistance Increase
                                                                 Resistance Decrease
                   Keypad Test                                   Start/Stop
                                                                 Enter
 Service           Error Log
                                                                 White Color
                                                                 Blue Color
                                                                 Green Color
                   Beacon Test
                                                                 Yellow Color
                                                                 Red Color
                                                                 Crank Index Magnet Sensor
                   Crank Sensors
                                                                 Crank RPM Angle Sensor
                   Crank Calibration
 Lock Facility
 Program: ON/OFF
 Setting

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
4.2.2 Maintenance Mode – Item Descriptions

4.2.2.1 Odometer – Indicates the total belt operation time and accumulated running distance.

4.2.2.2 Software – Displays current software versions and allows updates on this page Firmware and LCB* Update Procedure
            (Note: Please keep the machine powered on during the update process.)

Step1.
Place the following three files —CS51009-01.bin, CS31003.bin, and update.json
— in the root directory of a USB drive.
Step2.
Insert the USB drive into the USB port located on the back of the console.




Step3.
On this page, press the Update button under both the Firmware and LCB* sections.
* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.

Console APP Update Options
(Note: Please keep the machine powered on during the update process.)
This system provides two methods for updating the Console APP. Either method may be used:
Method 1:

Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the Firmware and LCB*
update procedure above.

Method 2:

Step1.
In Settings, connect the machine to a Wi-Fi network.

Step2.
Return to this page. The system will automatically detect if a new version is available.

Step3.
Press the Update APK button under the Console APP section.




* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
4.2.2.3 Service

4.2.2.3.1 Machine Type –
This series of six models shares the same app. You can switch the machine type on this page.

4.2.2.3.2 Communication Test – Provides a built-in hardware loop test function.

Step1.
Prepare a 1-meter USB-A (male) to USB-B (male) cable.

Step2.
Insert the USB-A end into the USB-A port on the back of the console, and the USB-B end into the USB-B port located at the data output
interface beneath the machine.

Step3.
Prepare a 5 cm single-core wire. Strip the PVC insulation from both ends, then insert the wire into pin 2 and pin 3 of the DB9 connector at the
data output interface beneath the machine.

Step4.
On this page, press the Start button. The system will automatically check the status of the hardware loop.

(Note: The maintenance video demonstrates the actual operation process.)

4.2.2.3.3 NFC Sensor Test –
Place the NFC tag near the bottom-right corner of the console.
Each detection cycle takes three seconds. If the tag is not detected, remove it for three seconds and try again.

4.2.2.3.4 Keypad Test –
Press the physical buttons on the console to verify their functionality.

4.2.2.3.5 Error Log –
Displays the history of system errors.

4.2.2.3.6 Beacon Test –
Switch the beacon light bar colors to verify functionality.
4.2.2.3.7 Crank Sensors –
Displays the rotational speed. (Refer to Figure 1)

4.2.2.3.8 Crank Calibration –
Put the right crank at a 6 o’clock position, and then press the button below to run the test. (Refer to Figure 2)




4.2.2.4 Lock Facility Program –
When set to ON, the speed and incline profiles of the Facility program cannot be modified.
4.3 ELECTRICAL WIRING DIAGRAM
4.4 CIRCUIT BOARD

4.4.1 Lower Control Board (#091) Power Supply #081 provides 24 VDC to the LCB.
The board converts it to 12 VDC for the console and supplies power to the angle and magnet sensors.
Sensor readings are used to control resistance on Brake #086.
4.4.2 Power Supply Module (#081)
AC power is converted to 24VDC to provide DC voltage for the entire system.
4.5 LIST OF REQUIRED MAINTENANCE TOOLS
                              No.        Tool Name
                              1          Multimeter
                              2          Cordless Impact Driver Set
                              3          Phillips Screwdriver
                              4          Diagonal Cutting Pliers
                              5          Needle-nose Pliers
                              6          Electric Soldering Iron
                              7          Solder Wire
                              8          Anti-static Tweezers
                              9          Heat Shrink Tubing
                              10         Utility Knife
                              11         Hex Key Set (Allen Wrench Set)
                              12         Socket Wrench Set
                              13         Cable Ties (Minimum Length: 20 cm)
                              14         Electrical Insulation Tape
                              15         Lead Wire (for guiding cable through tubing)
                              16         Insulated Gloves
                              17         Anti-static Wrist Strap
                              18         Crank Removal Tool
5. TROUBLESHOOTING (ELECTRONIC)


5.1 NO POWER, CONSOLE DOESN’T LIGHT

Step1.
Press any physical button on the console (Refer to Figure 3) to wake up the system. If the system does not respond, proceed to the next step.

Step2.
Measure the AC input voltage at the cable connected to the CN1 housing on the power supply module (Refer to Figure 4).
If no AC voltage is measured or the voltage is incorrect, check whether the power switch is turned on and the fuse is not blown (Refer to Figure
5).
Then, measure the mains voltage (Refer to Figure 6) and the voltage at the machine-side end of the power cable (Refer to Figure 7).
If correct AC voltage is present at CN1, proceed to the next step.
Step3.
Check the status of power indicator light D5 on the LCB (Refer to the Circuit Board section).
If the light is off, proceed to the next step. If the light is on, skip ahead to Step5.

Step4.
Measure pins 1 and 4 of connector CN100 on the power supply module to verify the presence of 24 VDC (Refer to Figure 8).
If 24 VDC is not measured, replace the power supply module. If 24 VDC is measured, replace the LCB.
Step5.
Measure pins 1 and 2 on the J3 cable at the rear of the console to verify 12 VDC (Refer to Figure 9).
If no 12 VDC is measured, inspect the inline connector cable (Refer to Electrical Wiring Diagram section).
If 12 VDC is measured, replace the console.
5.2 UART COMMUNICATION ERROR

Step1.
Check if cables #089 and #090 are properly connected (Refer to Electrical Wiring Diagram section).
If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.

Step2.
Check if the software version shows V255A255. If it does, update the software (Refer to Maintenance Mode section).
If not, replace both the LCB and the console.
5.3 NO REVOLUTIONS

Step1.
While pedaling the crank, check the status of indicator light D13 on the LCB (Refer to Circuit Board section).
If the light flashes, confirm that both ends of the #072 cable are properly connected (Refer to 8.Electrical Wiring Diagram section).
If the light does not flash, proceed to the next step.

Step2.
Confirm that the gap between the Hall sensor and the magnet on the drive pulley (#45-1) is 2 to 3 mm, and that the sensor is aligned with the
center point between the two arrows marks (Refer to Figure 10).
If the sensor is not installed correctly, reinstall it. If the installation is correct, proceed to the next step.

Step3.
Confirm that both ends of the #072 cable are properly connected (Refer to 8.Electrical Wiring Diagram section).
If the cable is not properly connected, reconnect both ends securely.
If the cable is already properly connected, replace both the LCB and the Hall sensor.
5.4 INCORRECT SYMMETRY VALUE

Step1.
Calibrate the crank position (Refer to Maintenance Mode section). If the issue persists, proceed to the next step.

Step2.
Position the right crank at the 6 o'clock position. Ensure that the magnet on the drive pulley (#45-1) maintains an angle of at least 90 degrees
relative to the Hall sensor (Refer to Figure 11).
Once properly aligned, install the right crank. Then, recalibrate the crank position.
6. PART REPLACEMENT GUIDE


6.1 CONSOLE REPLACEMENT

As Figure 6.1.1, remove Phillips Head Screws (M4x2PCS) from both sides of cover.
As Figure 6.1.2 and 6.1.3, remove Phillips Head Screws (M5x4PCS) that secure console bracket and remove the wirings to replace console.
Assemble Console in reverse order.




                             Figure 6.1.1                   Figure 6.1.2            Figure 6.1.3
6.2 BRAKE COVERS REPLACEMENT

As Figure 6.2.1, remove Brake Cover (R) directly, this bolt is the upper stop for Brake Lever, do not remove it.
As Figure 6.2.2, loosen the screws and flat washer to remove Brake Cover (L).




                               Figure 6.2.1                  Figure 6.2.2
6.3 PEDALS & CRANK ARMS REPLACEMENT

As Figure 6.3.1 and 6.3.2, turn pedal(R) in counterclockwise direction and pedal (L) in clockwise direction to remove pedals.
As Figure 6.3.3, remove the nut and screw inside crank. (Same on both sides, please use 60 N-m when tighten up.)
As Figure 6.3.4, remove Crank Arm with crank extractor. (Same on both sides)
Assemble Crank Arms and Pedals in reverse order.




                      Figure 6.3.1                 Figure 6.3.2               Figure 6.3.3                 Figure6.3.4
6.4 CHAIN COVERS AND ROUND DISKS REPLACEMENT


As Figure 6.4.1, refer to 6.3 to remove Crank Arms. The Round Disks at both sides would be able to remove.
As Figure 6.4.2 and 6.4.3, loosen the four screws which secure the Chain Cover at both sides.
As Figure 6.4.4, unlock hidden clips with flathead screwdrivers. (Please be gentle not apply too much power to break the clips.)
As Figure 6.4.5, remove Sheet Metal Screws (M5x2PCS) to remove Chain Covers.
As Figure 6.4.6, remove Sheet Metal Screw and Flat Washer from inner side of Chain Cover.




                           Figure 6.4.1                          Figure 6.4.2                            Figure 6.4.3




                            Figure 6.4.4                       Figure 6.4.5                            Figure 6.4.6
6.5 DRIVE PULLEY AND DRIVE BELT REPLACEMENT

As Figure 6.5.1, remove C Ring to remove Drive Pulley.
As Figure 6.5.2, slide Drive Belt out from Idler Wheel Assembly to remove Drive Belt.




                             Figure 6.5.1                        Figure 6.5.2
6.6 IDLER WHEEL ASSEMBLY AND FLYWHEEL REPLACEMENT

As Figure 6.6.1, remove screws (M5x3PCS) and nuts (M8x2PCS) as Figure 6.6.2 to remove Idler Wheel Assembly.
As Figure 6.6.3, loosen the screws (1/4"x4PCS) on both sides of flywheel to remove Flywheel.




                        Figure 6.6.1                              Figure 6.6.2                          Figure 6.6.3

6.7 BRAKE PAD REPLACEMENT

As Figure 6.7.1, loosen the screw and nut that secured the Brake Pad by open end wrench and L Allen wrench to remove Brake Pad.




                             Figure 6.7.1
6.8 LOWER CONTROL REPLACEMENT

As Figure 6.8.1, remove screws (M5x4PCS) to remove Lower Control to replace.




                                             Figure 6.8.1
6.9 ADJUSTMENT FOOTS AND TRANSPORTATION WHEELS REPLACEMENT

As Figure 6.9.1, loosen the Button Head Socket Bolt and Nylon nut by open end wrench and L Allen wrench to remove Transportation Wheels.
As Figure 6.9.2, turn counterclockwise to remove Adjustment Foots.
(Adjust the height of Adjustment Pads when the unit is not horizontal until balance.)




                                      Figure 6.9.1                                   Figure 6.9.2
7. TROUBLESHOOTING



7.1 SLIP/SHEDDING OF DRIVE BELT

7.1.1 If the belt is slipping or shedding, please refer to 6.5 and 6.6 to adjust tension by tightening nut.


7.2 NOISE/FOOT FEELING

7.2.1 It is normal phenomenon to hear the sound comes from flywheel when pedaling in reverse direction during operation.
7.2.2 If there is any feeling of foot during pedaling, please refer to 6.3 to tighten Crank Arms and Pedals.


7.3 HANDGRIP/WHOLE BIKE SWAY

7.3.1 If handgrip is shaking during operating, please refer to 3.2 to tighten screws.
7.3.2 If whole bike is wobbling during operating, please refer to Figure 6.9.2 to adjust the height of Adjust Pads.
Exploded view Drawing
Parts list
                                                           Usage
             Part#   Descriptions
                                                           Q'ty
             1       Main Frame                            1
             2       Console Mast                          1
             3       Fixing Plate                          1
             4       Brake Lever                           1
             5       Upright Brake Shaft                   1
             6       Steel Cable                           1
             7       Pedal(L.R)                            1
             8L      Crank Arm(L)                          1
             8R      Crank Arm(R)                          1
             9(A)    Idler Wheel Assembly(Lower)           1
             9(B)    Idler Wheel Assembly(Top)             1
             9(C)    Idler Wheel Assembly                  1
             10      Idler Bracket (A)                     2
             11      Idler Bracket (B)                     1
             12      6203_Bearing                          4
             13      Powder metallurgy Sleeve              2
             14      Rotating Structure Assembly(Top)      1
             15      Rotating Structure Assembly(Bottom)   1
             16      Rotate Holder Assembly                1
             17      Tension Rod Assembly                  1
             18      Brake Pad                             1
             19      Constrict Spring                      1
             20      Latch Spring                          1
             21      O-ring                                6
             22      Round Cap                             1
             24      Crank Axle                            1
             24-1    Drive Pulley                          1
             24-2    Magnet                                1
             25      6004_Bearing                          2
             26      M10 × P1.25 × 10T_Nut                 2
             27      Adjustment Foot                       3
             28      Transportation Wheel                  2
             29      Plate                                 4
             30      Drive Belt                            1
             31      Sheet Metal                           4
             32      Pad                                   9
             33      Crank Arm End Cap                     2
             35      Console Bracket                       1
             36      Console Mast Cover                    1
             37      Chain Cover(L)                        1
             38      Chain Cover(R)                        1
39    Brake Cover(L)                          1
40    Brake Cover(R)                          1
41    Round Disk                              2
42    Rear Tube Cover                         1
50    Locating Ring                           2
61    Transfer Sheet                          1
70    Console Assembly                        1
71    Interface Board                         1
72    1350mm_Connecting Wire(PHP-9)           1
73    550mm_Connecting Wire(PHP-9)            1
74    1350mm_Connecting Wire(XHP-4)           1
75    550mm_Connecting Wire(XHP-4)            1
76    AC Electronic Module                    1
77    80mm_Connecting Wire (White)            1
78    80mm_Connecting Wire (Black)            1
79    500mm_Ground Wire                       1
80    350L_Power Connecting Cable             1
81    Switching Power Supply                  1
82    300L_Ground Wire                        1
83    100mm_Power Connecting Cable            1
84    Hall Module                             1
85    450mm_Connecting Wire                   1
86    Flywheel                                1
87    300mm_Wire Brake Coil Harness(Red)      1
88    500mm_Wire Brake Coil Harness(Red)      1
89    1250mm_Connecting Wire(XHP-6)           1
90    550mm_Connecting Wire(XHP-6)            1
91    Generator/Brake Controller              1
95    Power Cord (Optional)                   1
100   Ø 17_C Ring                             2
101   Ø 10_C Ring                             2
102   Ø 17 × Ø 23.5 × 1.0T_Flat Washer        4
104   Ø 5.5 × Ø 15 × 1.5T_Flat Washer         3
105   M8 × 30mm_Flat head countersink Bolt    1
106   M8 × 20mm_Flat Head Countersink Bolt    2
107   M8 × 25mm_Flat Head Countersink Bolt    1
110   Ø 3/8" × Ø 19 × 1.5T_Flat Washer        2
111   M8 × 80mm_J Bolt                        1
112   M6 × 25mm_Socket Head Cap Bolt          1
113   M6 × 6T_Nylon Nut                       1
114   M8 × P1.25 × 65L_Socket Head Cap Bolt   1
115   1/4" × UNC20 × 3/4"_Hex Head Bolt       8
116   Ø 1/4"_Split Washer                     4
117   Ø 1/4" × 13 × 1.0T_Flat Washer          8
118   M5 × 15mm_Phillips Head Screw             8
119   5/16" × 1-3/4"_Button Head Socket Bolt    2
120   5/16" × 6T_Nylon Nut                      2
121   Ø 8.5 × Ø 18 × 1.5T_Flat Washer           6
122   M5 × 12mm_Phillips Head Screw             11
123   M8 × 6T_Nut                               2
124   M8 × P1.25 × 6T_Nylon Nut                 5
125   M5 × 40mm_Phillips Head Screw             1
127   M5 × 10mm_Slotted Set Screws              2
128   Ø 20_C Ring                               2
129   Ø 8_C Ring                                2
131   M5 × 5mm_Slotted Set Screws               17
133   Ø 5 × Ø 12 × 1.0T_Flat Washer             3
134   3.5 × 12mm_Sheet Metal Screw              5
135   3.5 × 10mm_Sheet Metal Screw              2
136   1/4" × 5.5T_Nylon Nut                     6
145   M8 × 50mm_Socket Head Cap Bolt            3
146   M5 × P0.8 × 12L_Flat Head Countersink Bolt 2
147   M5 × 10mm_Phillips Head Screw             4
148   1/4" × 1/2"_Carriage Bolt                 2
149   Nylon Washer                              2
150   6mm_Washer                                2
151   M5_Star Washer                            1
152   Phillips Head Screw Driver                1
153   Console Rear Trim                         1
154   13/15mm_Wrench                            1
155   3mm_L Allen Wrench                        1
156   6mm_ L Allen Wrench                       1
158   Wire Clamp                                2
161   M3 × 8mm_Flat Head Socket Screw           2
163   M4 × 6L_Phillips Head Screw               4
164   M4 × P0.7 × 8mm_Phillips Head Screw       4
165   M4 × 3.5T_Nut                             4
167   M3 × 6mm_Phillips Head Screw              4
501   Seat Rotation                             1
502   Seat Carriage                             1
503   Releasing Latch                           1
504   Cantilever Anchor Assembly                1
505   Seat Rotation Release Lever               1
506   Rail Assembly                             1
507   Seat Release Lever                        1
508   Seat Back Fixed Bracket                   1
509   Seat Back Bracket                         1
510   Cup Holder Sheet Metal                    1
511   Adjusting Lever                             1
512   Bottom Plate                                2
513   Seat Track Sheet Metal(L)                   1
514   Seat Track Sheet Metal(R)                   1
515   Seat Back Adjustment Sheet Metal            1
516   Adjusting Lever Rotate Axle(L)              2
517   Adjusting Lever                             1
518   Steel Cable Sliding Axis                    1
519   Handlebar                                   1
520   Adjusting Rod                               1
521   Rack                                        1
522   Back Plate                                  1
523   Sheet Metal                                 1
524   Transportation Wheel Fixing Plate           1
525   Seat Position Latch                         1
526   Sheet Metal-A                               2
527   Sheet Metal-B                               2
528   Gas Cylinder                                1
529   Rotate Disk                                 1
530   Ø 13.5 × 60L_Spring                         1
531   Constrict Spring                            2
532   Ø 15.5×26.5L_Spring                         1
533   Seat Front Read Adjusting                   2
534   Ø 31 × 9.5T_Nylon wheel                     4
535   Ø 31 × 16.2T_Nylon wheel                    27
536   Handgrip                                    1
537   Seat Back                                   1
538   Seat                                        1
539   Steel Cable-B                               1
540   Steel Cable                                 1
542   15.9 × 22mm_Podwer metallurgy Sleeve        8
543   Ø 12 × Ø 18 × 8L_Podwer metallurgy Sleeve   2
544   Spacer for Stopper Axle                     2
546   Buckle                                      10
547   Snap seat                                   10
548   Plastic flaps                               2
549   Pad                                         4
550   Beverage Holder                             1
551   Hinge Cover                                 1
552   Seat Back Cover                             1
553   Lower Plastic Cover                         1
554   Turntable cover (R)                         1
555   Turntable cover (L)                         1
559   5/16" × UNC18 × 3/4"_Hex Head Bolt          9
560   M6 × 15mm_Button Head Socket Bolt          31
561   M8 × P1.25 × 25L_Hex Head Bolt             2
562   M6 × 12mm_Socket Head Cap Bolt             2
563   M6 × 38mm_Socket Head Cap Bolt             3
564   M8 × P1.25 × 20L_Socket Head Cap Bolt      2
565   M8 × 20mm_Hex Head Bolt                    10
566   M5 × 4T_Nut                                2
567   M5 × 5T_Nylon Nut                          5
568   M6 × 6T_Nylon Nut                          9
569   5/16" × 6T_Nylon Nut                       11
570   M6 × 19L_Nut                               24
571   M8 × 1.25 × 6.5T_Square Nut                18
572   Ø 6 × Ø 16× 1.0T_Flat Washer               26
573   Ø 8.5 × Ø 18 × 1.5T_Flat Washer            21
574   Ø 16_C Ring                                6
575   M5 × 12mm_Flat Head Socket Screw           4
576   M6 × P1.0 × 50L_Button Head Socket Bolt    1
577   M10 × 20mm_Button Head Socket Bolt         1
578   3/8" × 19mm_Hex Head Bolt                  3
579   Ø 3/8" × Ø 30 × 3T_Flat Washer             2
580   M8 × P1.25(10L × 16L)_Bolt                 1
581   M6 × 25mm_Socket Head Cap Bolt             4
582   M6 × P1.0 × 40L_Socket Head Cap Bolt       3
583   Ø 5/16" × 19 × 1.5T_Curved Washer          8
584   M5 × P0.8 × 70L_Socket Head Cap Bolt       1
585   M12 × P1.75 × 120L_Socket Head Cap Bolt    1
586   5/16" × UNC18 × 5/8"_Hex Head Bolt         2
587   3/8" × 1-3/4"_Socket Head Cap Bolt         2
588   Ø 3/8" × Ø 25 × 2.0T_Flat Washer           2
589   M8 × 30mm_Flat Head Socket Screw           6
591   M12 × P1.75 × 8T_Nylon Nut                 1
592   E5_E-Clip                                  1
593   M5 × 12mm_Phillips Head Screw              14
594   3.5 × 12mm_Sheet Metal Screw               10
595   M5 × 10mm_Button Head Socket Bolt          4
596   M10 × 70mm_Socket Head Cap Bolt            1
597   M10 × 8T_Nylon Nut                         1
598   Ø 8.5 × Ø 26 × 2.0T_Flat Washer            2
599   5/16" × 1-1/4"_Hex Head Bolt               1
600   Ø 6.6 × Ø 12 × 1.5T_Flat Washer            2
601   Ø 8 × 1.5T_Split Washer                    2
602   M8 × 50mm_Hex Head Bolt                    1
603   M8 × P1.25 × 15L_Button Head Socket Bolt   2
604   M8 × 10mm_Button Head Socket Bolt          1
605   M8 × 20mm_Flat Head Countersink Bolt       4
606   M8 × 60mm_Flat Head Countersink Bolt       2
607   M8 × 7T_Nylon Nut                          2
608   Ø 8.5 × Ø 26 × 2.0T_Flat Washer            2
609   M8 × P1.25 × 20L_Button Head Socket Bolt   4
610   3/8" × 7T_Nylon Nut                        2
611   8mm L Allen Wrench                         1
612   13/14mm_Wrench                             1
613   L Allen Wrench                             1
614   M6 × P1.0(Ø 8 × 20L)_Bolt                  2
615   M6 × 12mm_Socket Head Cap Bolt             4
616   M5 × 15mm_Phillips Head Screw              4
617   Ø 6 × 25L × M5 × P0.8_Bolt                 1
618   Fixing Base                                1
8. ELECTRICAL SYSTEM WIRING DIAGRAM


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JenuePy BIIAIBS

(L0-9£0gS-000cuW)
GV LvSZ-HG's


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Table of Contents

1. SERIAL NUMBER LOCATION 2 ..cccccccneneneeeeee ee ee ne ee ee en eee eee 4
2. COMPONENT DESCRIPTION .....ccceeecenennnnnnennenenneneeeeeeeeeeeeneneee ee ee eee eee 5
3. PREVENTIVE MAINTENANCE ..,....ccccenennnnnnencenneneneeeeeeeeeeeeneneen eee 6
3.1 CHECK FOR PEDALS AND CRANK ARMG. ..........cececceceececeecececeecectececucaececaeeeseeaes 6
3.2 CHECK FOR FRONT CONSOLE MAST .......ccceceececcececeececeecececececeecesucaecusaeceseeaes 7
3.3 CHECK FOR EMERGENCY STOP........ccccececcececcececceceeeececeececucaececeececueaececaeeeseeaes 7
3.4 CHECK FOR ROTATING STRUCTURE ASSEMBLY .........ccceccececeecectececuceececseceseeaes 8
4. CONSOLE SETTING jun wcccccceceneeeneneneen ee en ee ee eee eens ee eee eee 9
4.1 BASIC FUNCTIONS ......ccccceceececccececcececeecesueaucueaecusaesucaesecueaececeecesueaeseeaeeeseeaes 9
4.2 MAINTENANCE MODE .........02cececcececeececcecececaecuececueaececuececucaececeecesueaesesaeeesueaes 9
4.3 ELECTRICAL WIRING DIAGRAM ................cccceeceecececcececeececeecesusaeceeaeeees 16
4.4 CIRCUIT BOARD... ...ccccccceceececeececuceececececucaecuceececueaececaeceeueaeseeaesesusaueeeaeeees 17
4.5 LIST OF REQUIRED MAINTENANCE TOOLS. .......2-ecccceceececeecececeececeecesucaecesaeeess 19
5. TROUBLESHOOTING (ELECTRONIC) ......cccccssccsenseeeneeneeeeeeeeeeneneenneneeeeneeneeeeeeneeeeeeeee eee eeen eens eee eeeeeeeeeeeeeeee 20
5.1 NO POWER, CONSOLE DOESN'T LIGHT .......0ccccccecceceeeseeccuceeeeeueeeeeeueeueeeeeananass 20
5.2 UART COMMUNICATION ERROR.........2cecccceceececeecececeececeececucaecececesucaeceeaeeees 24
5.3 NO REVOLUTIONS .......cccccececcececcececeececececeeaecucececueaecucecesueaeseeaeseeueaeceeaesees 25
5.4 INCORRECT SYMMETRY VALUE ........0:ccceccececeececeecececcececececucaecesaecesucaeceeaeeees 27
6. PART REPLACEMENT GUIDE ......ccccceccncnnsncncnnneneneeeeneeeeeneneneeeen en neen eee nee nee 29
6.1 CONSOLE REPLACEMENT ......cccceceecececcececceceecececuececececueaecectecesecauceeaeeeseeaes 29


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.2 BRAKE COVERS REPLACEMENT........ccccececececececececeeeeuceeueeeuueeueeeueeeueeeeeeeneeees 30
6.3 PEDALS & CRANK ARMS REPLACEMENT........0cccecccecccececeeeeueeeueseueeeueeeeeeeeeees 31
6.4 CHAIN COVERS AND ROUND DISKS REPLACEMENT.........0cccceceeeeeeeeeeeeeeeeeeees 32
6.5 DRIVE PULLEY AND DRIVE BELT REPLACEMENT .........0ccccccceeceeeceeeeeeeeeeeeeeeeees 33
6.6 IDLER WHEEL ASSEMBLY AND FLYWHEEL REPLACEMENT.........00cceeeeeeeeeeeeeeeees 34
6.7 BRAKE PAD REPLACEMENT .......cccecccecececsceceeecececeeeeeeueeeueeeuceeueeeueeeueeeeneeneees 34
6.8 LOWER CONTROL REPLACEMENT ......c.cecccecececececeeeeeceeeeueeeuueeueeeueeeueeeeeeeeeeees 35
6.9 ADJUSTMENT FOOTS AND TRANSPORTATION WHEELS REPLACEMENT..........5+ 36
7. TROUBLESHOOTING. ..wsncscssncnencecseececneeeeenneeeenneeennneeeenneee en neee en ne eee eee
7.1 SLIP/SHEDDING OF DRIVE BELT .........ccccccecceecece cece ceeeeeeueeeueeeueeeueeeueeeeeeeneeens 37
7.2 NOISE/FOOT FEELING .......ccccccecceecececececeeeceeececeeeeeeeeaeeeueeeueeeueeeueeeueeeeeeeeeens 37
7.3 HANDGRIP/WHOLE BIKE SWAY .....ccccccccecececeeececeeeeeeeeueeeeeeeueeeueseueeeueeeeeeeeeeees 37

8. ELECTRICAL SYSTEM WIRING DIAGRAM


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ZOLI-S€6 (028)
FOLPSS Z1S1. 126 0 (10) LIgHhaAs

b4aquinn jeias | |

202 1GN }2npoig ZODDDOLO9ZSP1S8z

YAEWNN TVIYdsS

Z0001092-08-86Z0Z1E1 (12) py OLPSS Z 2v0

Wi

VOLVSB8ZALSLLZVO0:28pod |q

me

I

NOILV9O1 YAGINN TVIAAS ‘4


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4. CONSOLE SETTING

4.1 BASIC FUNCTIONS

Refer to the User’s Manual for detailed console operations.

4.2 MAINTENANCE MODE

Maintenance Mode is intended for troubleshooting purposes.
To enter Maintenance Mode, tap the Wi-Fi icon once and the clock in the status bar six times on the Home Screen.

Welcome

Age Height Weight

30 165 75

Pattern

Programs w
incline chan


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2.2 Maintenance Mode — Item Descriptions
4.2.2.1 Odometer — Indicates the total belt operation time and accumulated running distance.

4.2.2.2 Software — Displays current software versions and allows updates on this page Firmware and LCB* Update Procedure
(Note: Please keep the machine powered on during the update process.)

Step].
Place the following three files —CS51009-01.bin, CS31003.bin, and update.json

— in the root directory of a USB drive.

—
—

a> tz
x. = ze

Te] CS$31003.bin FDT4 Data File
fe] C$51009-01.bin FDT4 Data File
-] DyacoV1.0.A1.22.02000A.10.apk APK =

_)) update.json JSON 8


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Method 1:

Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the Firmware and LCB*
update procedure above.

Method 2:
Step1.
In Settings, connect the machine to a Wi-Fi network.
Step2.
Return to this page. The system will automatically detect if a new version is available.
Step3.
Press the Update APK button under the Console APP section.

Progress Beacon Acceleration & Ni — —

Deceleration
Change Change Softwa re
Software
-~ Android
Language oe Time & Date Please make sure WiFi is working
Firmware properly and then press Update APK
to update it.
Change Change
LCB

WiFi = Standby Console App met Update

Change PauseMode @

Account 4 Units ul

| Metric | Imperial

Details

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2.2.3.7 Crank Sensors —
Displays the rotational speed. (Refer to Figure 1)

4.2.2.3.8 Crank Calibration —
Put the right crank at a 6 o’clock position, and then press the button below to run the test. (Refer to Figure 2)

Crank Sensors Crank Calibration
Put the right crank at a 6 o'clock
Position, then press the button below

Crank Index Magnet Sensor to run the tes

Off

Crank RPM Angle Sensor

0

Figure 1 Figure 2

4.2.2.4 Lock Facility Program —
When set to ON, the speed and incline profiles of the Facility program cannot be modified.


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 51 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.3 ELECTRICAL WIRING DIAGRAM

#070, Console

Cah Ge
oo

#090 LCS3100B-1

#089 #73 #75

v 7

#084 Magnet Sensor a A

— { #086, Brake and Angle Sensor

O aa ae

#091] Lower Control Board = [= a 2
#045-2 Magnet Bl = & 5 i

[>] #072 Fe

eou
int
=
to 7

g
§Ce joe] #72, | #74

_ |#077, Neutral vy

ite aS) Line
#076, , AC Power Entry Module
with Switch and Fuse

#071, Data Transfer Board


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 83 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Wake the
To wake the system, | System Result:

Issue: -
Console doesn't light >} press the membrane >} The system is in
key on the console. sleep mode.
No te Result:
vance measured | Check mains voltage,
Measure the AC power cord, fuse,
>| input voltage onthe [>] power switch and
power supply module, internal power
wiring . (#076, 077,
078, 080)
24 VDC
is not
Pa Light off Measure pins 1and4 | measured Result:
Check power > of CN100 on the >| Replace Power
indicator light DS. power supply module Supply Module (#081)
to confirm 24 VDC.
24 VOC
measured
>} Result:
Replace LCB (#091)
12 VDC
not
tae Check for 12 VDC on measured
Inspect the inline
h —<—
‘ easritosintd st cable.
2 (#089, 090)
12 VDC
measured
Result:
>| Replace Console
(#070)

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting description.


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.2 UART COMMUNICATION ERROR

Step].
Check if cables #089 and #090 are properly connected (Refer to Electrical Wiring Diagram section).
If not connected, reconnect it or replace the cable if faulty. If properly connected, proceed to the next step.

Step2.

Check if the software version shows V255A255. If it does, update the software (Refer to Maintenance Mode section).
If not, replace both the LCB and the console.

Check Procedure

Improper
connection
Issue: Result:
UART Check the cables : Ensure proper cable
Communication (#089, 090) connection or
Error replace if faulty.
Proper
connection Incorrect
Check the software Result:
version Update Software
cas Result:
>| Replace LCB and
Console (#091, 070)

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description.


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 61 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Fash | Result
"ee Check indicator light Ensure that the cable
No : bations Di3 asthe pedal = ris properly
rotates. connected at both
ends, (#072)
Improper
connection
ses AS bap Check the cable i Result:
8 mt OfOperly connected ——j ao
between Hall sensor
at both ends, (#072) properly,
and magnet,
—— Proper
connection
A essed or
sensor (#091, 084)
Incorrect R It:
Reinstall the Hall
sensor. (#084)

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description.


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.4 INCORRECT SYMMETRY VALUE

Step1.
Calibrate the crank position (Refer to Maintenance Mode section). If the issue persists, proceed to the next step.

Step2.

Position the right crank at the 6 o'clock position. Ensure that the magnet on the drive pulley (#45-1) maintains an angle of at least 90 degrees
relative to the Hall sensor (Refer to Figure 11).

Once properly aligned, install the right crank. Then, recalibrate the crank position.

_—
=

f- #084, Hall Sensor :
Wa at least 90 degrees |

at

wh ,
t! ~

at least 90 degrees ( © 2

-
vf

.

b , Position the right crank at
\ he 6 o'clock position.

Figure 11


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 39 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Resolved
sans Calibrate the crank Result
Incorrect Symmetry osttion Problem corrected
Value cai via calibration.

Problem
remains Result:
x Reinstall the crank in
the correct
Orientation,

Note: The Check Procedure provides an overview of possible causes, For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description.


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
961 ccI vSI esl

90

Buimeig MOdIA papo|dxy


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
39 Brake Cover(L)

40 Brake Cover(R)

41 Round Disk

42 Rear Tube Cover

50 Locating Ring

61 Transfer Sheet

70 Console Assembly

71 Interface Board

72 1350mm_Connecting Wire(PHP-9)

73 550mm_Connecting Wire(PHP-9)

74 1350mm_Connecting Wire(XHP-4)

75 550mm_Connecting Wire(XHP-4)

76 AC Electronic Module

77 80mm_Connecting Wire (White)

78 80mm_Connecting Wire (Black)

79 500mm_Ground Wire

80 350L_Power Connecting Cable

81 Switching Power Supply

82 300L_Ground Wire

83 100mm_Power Connecting Cable

84 Hall Module

85 450mm_Connecting Wire

86 Flywheel

87 300mm_Wire Brake Coil Harness(Red)
88 500mm_Wire Brake Coil Harness(Red)
89 1250mm_Connecting Wire(XHP-6)

90 550mm_Connecting Wire(XHP-6)

91 Generator/Brake Controller

95 Power Cord (Optional)

100 @17_C Ring

101 @10_C Ring

102 QO17 x @23.5 x 1.0T_Flat Washer

104 05.5 x O15 x 1.5T_Flat Washer

105 MS8 x 30mm_Flat head countersink Bolt
106 M8 x 20mm_Flat Head Countersink Bolt
107 M8 x 25mm_Flat Head Countersink Bolt
110 03/8" x O19 x 1.5T_Flat Washer

111 M8 x 80mm_J Bolt

112 M6 x 25mm_Socket Head Cap Bolt
113 M6 x 6T_Nylon Nut

114 M8 x P1.25 x 65L_Socket Head Cap Bolt
115 1/4" x UNC20 x 3/4''"_Hex Head Bolt
116 @1/4"'_Split Washer

117 Q1/4" x 13 x 1.0T_Flat Washer


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
560 M6 x 15mm_Button Head Socket Bolt 31
561 M8 x P1.25 x 25L_Hex Head Bolt 2
562 M6 x 12mm_Socket Head Cap Bolt 2
563 M6 x 38mm_Socket Head Cap Bolt 3
564 M8 x P1.25 x 20L_Socket Head Cap Bolt 2
565 M8 x 20mm_Hex Head Bolt 10
566 M5 x 4T Nut 2
567 M5 x 5T_Nylon Nut 5
568 M6 x 6T_Nylon Nut 9
569 5/16" x 6T_Nylon Nut 11
570 M6 x 19L_Nut 24
571 M8 x 1.25 x 6.5T_Square Nut 18
572 6 x O16x 1.0T_Flat Washer 26
573 Q8.5 x O18 x 1.5T_Flat Washer 21
574 @16_C Ring 6
575 M5 x 12mm_Flat Head Socket Screw 4
576 M6 x P1.0 x 50L_Button Head Socket Bolt 1
577 M10 x 20mm_Button Head Socket Bolt 1
578 3/8"" x 19mm_Hex Head Bolt 3
579 3/8" x @30 x 3T_Flat Washer 2
580 M8 x P1.25(10L x 16L)_Bolt 1
581 M6 x 25mm_Socket Head Cap Bolt 4
582 M6 x P1.0 x 40L_Socket Head Cap Bolt 3
583 @5/16" x 19 x 1.5T_Curved Washer 8
584 MS x P0.8 x 70L_Socket Head Cap Bolt 1
585 M12 x P1.75 x 120L_Socket Head Cap Bolt {1
586 5/16" x UNC18 x 5/8''"_Hex Head Bolt 2
587 3/8" x 1-3/4''_Socket Head Cap Bolt 2
588 Q3/8"' x O25 x 2.0T_Flat Washer 2
589 M8 x 30mm_Flat Head Socket Screw 6
591 M12 x P1.75 x 8T_Nylon Nut 1
592 E5_E-Clip 1
593 M5 x 12mm_Phillips Head Screw 14
594 3.5 x 12mm_ Sheet Metal Screw 10
595 MS5 x 10mm_Button Head Socket Bolt 4
596 M10 x 70mm_Socket Head Cap Bolt 1
597 M10 x 8T_Nylon Nut 1
598 Q8.5 x O26 x 2.0T_Flat Washer 2
599 5/16" x 1-1/4""_Hex Head Bolt 1
600 (6.6 x O12 x 1.5T_Flat Washer 2
601 08 x 1.5T_Split Washer 2
602 MS8 x 50mm_Hex Head Bolt 1
603 M8 x P1.25 x 15L_Button Head Socket Bolt 2
604 M8 x 10mm_Button Head Socket Bolt 1


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 44 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8. ELECTRICAL SYSTEM WIRING DIAGRAM

#070, Console

Lc]
(os) Gs

zd ||
t #090 Lcs3100B-4

#089 #73 #75

¥ ¥

#084 Magnet Sensor , f
— \ L

OL = #091 ere Control Board wane

#045-2 Magnet a oo S 5s
#072 z >

B to
an or Y) 7d lwza

#083

#078, Line
#076, , AC sower ‘Entry Module
with Switch and Fuse

#071, Data Transfer Board
