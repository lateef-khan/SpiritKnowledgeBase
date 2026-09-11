<!-- Source: 7.0R-770145_MR490-SB018-03_Service_Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

7.0R-770145 (MR490-SB018-
03)

Service Manual
--------------------------------------------Table of Contents-------------------------------------------
            1.    Serial Number Location
            2.    Component Description
            3.    Preventative Maintenance
              3.1 Check for Pedal
              3.2 Check for Front Handle Bar
              3.3 Check for Aluminum Track
              3.4 Check for Release Lever of Mechanical Brake
            4. Setting of Electronic Console
              4.1 Basic Functions
              4.2 Maintenance Mode
            5. Troubleshooting (Electronic)
            6. Part Replacement Guide
              6.1 Console Replacement
              6.2 Pedal & Crank Arm Replacement
              6.3 Console Mast Replacement
              6.4 Console Mast Cover Replacement
              6.5 Seat back Gas Cylinder Replacement
              6.6 Seat steel cable replacement
              6.7 Seat rotation adjustment steel cable replacement
              6.8 Front Shroud Replacement
              6.9 Rear Shroud Replacement
              6.10 Induction Brake Replacement
              6.11 Controller Replacement
              6.12 Switching Power Supply Replacement
              6.13 Reed Sensor W/Cable Replacement
                  MR7000 Wiring Diagram
  1.   Serial Number Location




Figure 1.1.1
2. Component Description
1.3 Check for Aluminum Track
As shown in Figure 3.3.1 and Figure 3.3.2, regular cleaning of the surface of the aluminum track can avoid PU wheel loss.




Figure 3.3.1                           Figure 3.3.2


1.4 Check for Release Lever of Mechanical Brake
Usually, the tension of release lever becomes loose because of the abrasion of felt. You could use the steel cable to adjust the
tension. As shown in Figure 3.4.1, loosen the 2 screws on right side of the cover of mechanical brake to remove the cover. As
shown in Figure 3.4.2, adjust the distance of steel cable if you feel it’s too loose for release lever.




Figure 3.4.1                  Figure 3.4.2
 4. Setting of Electronic Console

   1.5 Basic Functions

   Refer to the user manual for the function introduction section

   1.6 Maintenance Mode

 5. Troubleshooting (Electronic)

   1.7 For detailed console operation refer to the Owner’s Manual

   1.8 Maintenance Mode : Settings and Assist for troubleshooting

  5.2.1 Maintenance Mode
     To enter the Maintenance menu (may be called Engineering mode, depending on version) press and hold down the Start, Stop and Enter
     keys.
     Keep holding the keys down for about 5 seconds and the message window will display “Engineering mode”. Press the enter button to access
     the menu below:
  a. Key Test
i. Press each key to verify it is functioning correctly. Each key press produces a beep sound and a number will show on the display. If you press a
   key and there is no beep and no number displayed then that key has malfunctioned. When all keys have been pressed the display will show
   ‘Passed’, the test program ends automatically.
     b. Display Test
ii. Lights all LED lights sequentially for visual checking
     c. Functions (Press enter to access menu)
iii.Sleep - Turns SLEEP MODE ON or OFF. When set to ‘off’ the console power is always on. When set to ‘on’ the console will go to sleep after 30
    minutes of inactivity.
iv. Pause - Turns PAUSE MODE ON or OFF. When set to ‘on’ the Pause lasts 30 minutes then the console returns to the idle mode. When set to
    ‘off’ the pause lasts indefinitely.
v. Odometer Reset - Reset odometer readings.
vi. Units - Set the measurement values to display in ENGLISH or METRIC.
vii. Beep Sound - Turns the speaker (beep sound) on or off.
   d. Security
viii.Enable or disable the child lock. When the lock was enabled, press the START and ENTER key for 3 seconds to unlock.
   e. Factory settings
ix. Brake Test
    1. Allows you to manually change resistance levels one bit at a time to test whether the brake is functioning properly. 512 is the maximum
        resistance, don't stay in high level (more than 400) for too long.
x. Sensor Test
   1. The bike has two sensors, one angle sensor for speed/velocity measurements located on the brake, and one reed switch that measures
      crank rotation which we use to determine crank position.
   2. MW will show: ANGLE 0 REED 0
       a. When sensors operate correctly: rotate the crank and the Angle reading will show pedal RPM measurement and the Reed will change
          from 0 to 1 once and beep per pedal revolution.
xi. Crank Position Cali
   1. Software calibration to set the position of the right pedal at 12 o’clock.
   2. Set right pedal to 6 o’clock position then press start.
     3. Rotate the right pedal clockwise until the console beeps.
xii. Watts Calibration (Factory use only)
xiii.Unit Type - Selects the corresponding model for the unit, MU100 for the upright bike and MR100 for the recumbent bike.

 5.2.2 Error Code
   EEPROM Error - Replace the console when the error code shows. This is the only error code for this unit.

 5.2.3 Troubleshooting and Problem Solving (See separate wiring diagram for detailed wiring information)
   No power, console doesn't light.

 5.2.4 Troubleshooting
    1. No Power
 i. Make sure the A.C. outlet has power (90~240VAC), the line cord plugged in securely and the power switch is on.
ii. Make sure all connectors in back of the console are securely seated in place. Go to next step if there is still no power on the bike.
iii. Measure the pin 1/pin 6 and pin 3/pin 6 of the 6 pin cable that connected to the console for 12V DC. Replace the console if the 12V DC was
    measured. Go to next step if there is no voltage.
iv. Open the cover and measure the pin 3 and pin 6 of the 6 pin connector at the control board for 12V DC. Replace the cable if the voltage was
   measured at the control board but not at the cable. Otherwise, go to next step.




v. Measure the input voltage at the control board at the 4 pin connector for 24V DC. Replace the control board if the voltage was measured. Go to
next step if there is no voltage.
vi. Measure the input (2 pin connector, left picture) and output (8 pin connector, right picture) voltage of the switching power supply. You should
measure the same AC voltage with step 1 at input, 24V DC at the output. Replace the cable that connects the control board and power supply if
the 24V DC was measured. Replace the power supply if the input AC voltage was measured but no output voltage. Go to next step if both voltage
was measured.




vii. Check the fuse in the Input module (located between the power switch and line cord input). Use the meter to check the fuse, the fuse should be
short. Make sure there is nothing short in the whole system and replace the fuse if the fuse was open.
2. Console Programs Do Not Start
  i. Open the cover of the console and check all cables were plugged. After checking the cables, perform the Key Test in Maintenance mode.
   Replace the keypad if the Key Test didn't pass or can't enter Maintenance mode.

3. Program Starts But No Data Registers When Bike is Pedaled
   i. Make sure all the cables in the back of console were plugged in properly.
  ii. Run the Sensor Test in Maintenance mode. Go to step iii if ANGLE didn't display correct RPM, go to step iv if REED didn't work properly.
 iii. Open the cover and measure the pin 2 and pin 9 at the cable that connect to the angle sensor for 5V DC. Check the magnet on the shaft of
    brake. The magnet should be in the center of the shaft and have 3mm gap between magnet and angle sensor. Replace the angle sensor if
    correct but there is no RPM.




iv. Open the cover and check the reed sensor. Make sure the magnet on the pulley aligns to only one of the arrow of the reed sensor and have
  about 5mm gap. Use meter to check the sensor if everything set up properly, the sensor should be short when magnet pass the sensor. Replace
  the sensor if it isn't short when magnet passes the sensor.
 v. Check the cables if there is no problem in step iii and iv. Replace the console if everything is good.
4. Symmetry Measurement is Incorrect
 i. Check the Unit Type is setting to the right model.
 ii. Check the sensors by the Sensor Test in Maintenance mode.
 iii. Run the Crank Calibration in Maintenance mode.
5. Pedal Resistance Problem
 i. Resistance too strong/weak - Check the resistance/level setting in the SETUP.




 ii. No any resistance
    1. Open the cover and make sure the cable that connect control board and coil on the brake are plugging properly at both ends. Go to next step
       if the connection was good.




  2. Run the Brake Test in Maintenance mode and set to maximum resistance (512). Replace the control board if the orange LED on the control
      board didn't light.
6. Hand Pulse Problem
   i. Check the cables in the back of console for the possible loose. Go to next step if the problem doesn't solve.
 ii. Measure the hand pulse sensor as the picture below. The two points should be short when the console was on the bike and any other two
     points shouldn't be short. Set the hand pulse sensor to the right setting if the setup was wrong. Go to next step if the setup is right.




iii. Open the cover and check the cables connection and possible broken cables. Replace the console if everything is good.
6. Part Replacement Guide

 6.1 Console Replacement

  6.1.1 Remove Electronic Console
        As shown in Figure 6.1.1, remove the 4 screws from the bottom of the electronic console and remove the cable connector
        to remove the electronic console. As shown in Figure 6.1.2, unplug the connectors of wires to remove the electronic
        console.




 Figure 6.1.1                        Figure 6.1.2

  6.1.2 Electronic console assembly: Follow step 6.1.1 in reverse order.
 Figure 6.2.3                  Figure 6.2.4                              Figure 6.2.5
6.2.2.2 Crank arm assembly: Follow step 6.2.1.1 and step 6.2.2.1 in reverse order.
6.3 Console Mast Replacement

6.3.1 Refer to step 6.1 to remove the console.
6.3.2 Remove the Steel Cover and the Bracket of Manual Brake Lever
As shown in Figure 6.3.1, take off the 2 screws of both side of steel cover to remove the steel cover of manual brake lever first.
As shown in Figure 6.3.2, take off the 2 screws to remove the plate of manual brake lever on the console mast.




Figure 6.3.1                      Figure 6.3.2
6.3.3 Remove Console Mast
As shown in Figure 6.3.3, take off the 6 bolts to remove the console mast.




Figure 6.3.3
6.3.4 Console mast assembly: Follow step 6.3.1 to step 6.3.3 in reverse order.

6.4 Console Mast Cover Replacement

6.4.1 Refer to step 6.3 to remove the console mast.

6.4.2 As shown in Figure 6.4.1, take off console mast cover to remove it.




Figure 6.4.1

6.4.3 Console mast cover assembly: Follow step 6.4.1 to step 6.4.2 in reverse order.
6.5 Seat back Gas Cylinder Replacement

6.5.1 Remove Gas Cylinder

  As shown in Figure 6.5.1, remove the four screws under the seat cushion. As shown in Figure 6.5.2, remove the safety cover by
  loosening the screws. As shown in Figure 6.5.3, cut the cable ties. As shown in Figure 6.5.4, loosen the adjustment cable and
  remove the cable head. As shown in Figure 6.5.5 and Figure 6.5.6, take off the screws and caps to remove the locking gas
  cylinder.




 Figure 6.5.1                            Figure 6.5.2                           Figure 6.5.3




 Figure 6.5.4                            Figure 6.5.5                           Figure 6.5.6

6.5.2 Gas cylinder assembly: Follow step 6.5.1 in reverse order.
6.6 Seat Steel Cable Replacement

6.6.1 Replacement of Steel Cable for the Seat Back Angle Adjustment

  As shown in Figure 6.6.1, loosen the adjustment cable screw and remove the cable end.
  As shown in Figure 6.6.2, Adjust the adjustment screw beneath the release handle to the position that allows the cable to
  be removed, then remove and replace the cable..




 Figure 6.6.1                       Figure 6.6.2


6.6.2 Assembly for steel cable for the seat back angle adjustment: Follow step 6.6.1 in reverse order.
6.7 Seat rotation adjustment steel cable replacement

 6.7.1 Replacement of Steel Cable for the Seat rotation adjustment

  As shown in Figure 6.7.1, cut the cable tie.
  As shown in Figures 6.7.2 and 6.7.3, rotate the seat to an angle to make it easier to remove the cable end and the spring. As
  shown in Figure 6.7.4, adjust the adjustment screw beneath the release handle to the position that allows the cable to be
  removed, then remove and replace the cable.




              Figure 6.7.1                          Figure 6.7.2




              Figure 6.7.3                            Figure 6.7.4
   6.7.2 Assembly for steel cable for the Seat rotation adjustment: Follow step 6.7.1 in reverse order.
  6.9.1.2 Rear shroud (L) assembly: Follow step 6.9.1.1 in reverse order.

 6.9.2 Rear Shroud (R) Replacement

  6.9.2.1 Refer to step 6.9.1.1 to remove the rear shroud (L).

  6.9.2.2 As shown in Figure 6.9.2, take off the screw on the main frame first. As shown in Figure 6.9.3, take off the 2 screws
   on the rear shroud (R) to remove the rear shroud (R).




Figure 6.9.2                                  Figure 6.9.3

  6.9.2.3 Rear shroud (R) assembly: Follow step 6.9.2.1 to step 6.9.2.2 in reverse order.
6.10   Induction Brake Replacement

 6.10.1Replacement for Tension Spring of Idler Assembly and Eye Bolt

  6.10.1.1Refer to step 6.8 to remove the front shroud.

  6.10.1.2Remove the Eye Bolt and Tension Spring
  As shown in Figure 6.10.1 and Figure 6.10.2, loosen the nuts on eye bolt to remove the eye bolt and the tension spring at the
  same time.




Figure 6.10.1                          Figure 6.10.2

  6.10.1.3Eye bolt and tension spring assembly: Refer to Figure 6.10.3 and Figure 6.10.4 and follow step 6.10.1.2 in reverse
   order. Then, use the nuts of the eye bolts to adjust the belt tension. The belt tension should be in 220N to 240N. Then, refer
   to step 6.10.1.1 in reverse order.
Figure 6.10.3   Figure 6.10.4
 6.10.2Drive Belt Replacement

  6.10.2.1Refer to step 6.8 to remove the front shroud.

  6.10.2.2Refer to step 6.10.1 to remove the eye bolt and tension spring. Then, the drive belt could be removed.

  6.10.2.3Drive belt assembly: Follow step 6.10.2.2 in reverse order. As shown in Figure 6.10.5 and Figure 6.10.6, the drive belt
   should be kept in the middle of groove of the drive pulley and the pulley of the induction brake. Then, refer to step 6.10.2.1
   in reverse order.




Figure 6.10.5                         Figure 6.10.6
 6.10.3Idler Wheel Assembly Replacement

  6.10.3.1Refer to step 6.8 to remove the front shroud.

  6.10.3.2Refer to step 6.10.1 to remove the eye bolt and tension spring.

  6.10.3.3Refer to step 6.10.2 to remove the drive belt.

  6.10.3.4As shown in Figure 6.10.7, loosen the 3 screws to remove the idler wheel assembly.




Figure 6.10.7
   6.10.3.5Assemble the idler wheel assembly: As shown in Figure 6.10.8, luck the idler wheel assembly counterclockwise and
    follow step 6.10.3.1 to step 6.10.3.4 in reverse order.




Figure 6.10.8
 6.10.4Induction Brake Replacement

  6.10.4.1Refer to step 6.8 to remove the front shroud.

  6.10.4.2Refer to step 6.10.1 to remove the eye bolt and tension spring.

  6.10.4.3Refer to step 6.10.2 to remove the drive belt.

  6.10.4.4Refer to step 6.10.3 to remove the idler wheel assembly.

  6.10.4.5As shown in Figure 6.10.9, loosen the 2 screws on both side of induction brake to remove the induction brake.




Figure 6.10.9
  6.10.4.6Induction brake assembly: As shown in Figure 6.10.10, push the induction brake forward to the end and follow step
   6.10.4.1 to step 6.10.4.5 in reverse order.




Figure 6.10.10

6.11   Controller Replacement

 6.11.1Refer to step 6.9 remove the rear shroud (L).

 6.11.2As shown in Figure 6.11.1, take off all the connectors and loosen the 2 screws to remove the controller.




Figure 6.11.1
 6.11.3Controller assembly: Follow step 6.11.1 to step 6.11.2 in reverse order.
6.12   Switching Power Supply Replacement

 6.12.1Refer to step 6.9 remove the rear shroud (L).

 6.12.2As shown in Figure 6.12.1 and Figure 6.12.2, take off all the connectors and loosen the 4 plastic standoffs to remove the
       switching power supplier.




Figure 6.12.1                            Figure 6.12.2(

 6.12.3Switching power supply assembly: Follow step 6.12.1 to step 6.12.2 in reverse order.
6.13   Reed Sensor W/Cable Replacement

 6.13.1Refer to step 6.8 to remove the front shroud.

 6.13.2Refer to step 6.9 remove the rear shroud.

 6.13.3As shown in Figure 6.13.1, take off the 4 screws to remove the step cover.




Figure 6.13.1

 6.13.4As shown in Figure 6.13.2, loosen the screw. As shown in Figure 6.13.3, cut all the cable ties along with the reed sensor
       w/cable. As shown in Figure 6.13.4, unplug the connector of reed sensor w/cable on the controller to remove it.
Figure 6.13.2                      Figure 6.13.3




Figure 6.13.4

 6.13.5Reed sensor w/cable assembly: Follow step 6.13.1 to step 6.13.4 in reverse order. The distance between reed sensor and
       magnet should be 2mm.
  7.3 Sway of Swivel Seat

   7.3.1 Sway of swivel seat is caused by the gap between seat wheel adjustment plate and aluminum track assembly. The
          solution is as follows:
          Use a cross screwdriver to remove the fixing screw (as shown in Figure 7.3.1). Then use the 11mm wrench and the right
          hand as the 13mm wrench. Tighten the 11mm wrench first and lock it in the front direction (as shown in Figure 7.3.2)
          and behind (as shown in Figure 7.3.3).




Figure 7.3.1                           Figure 7.3.2                           Figure 7.3.3
Exploded view drawing
7.0 R parts list

          Item     Description                         Qty

            1      Main Frame                          1
            2      Console Mast                        1
            3      Mast Handle bar Assembly            1
            4      Seat Carriage                       1
            5      Seat Back Bracket                   1
            6      Handle Bar                          1
            7      Rear Stabilizer                     1
           9L      Seat Wheel Adjustment Plate(L)      2
           9R      Seat Wheel Adjustment Plate(R)      2
           10      Idler Bracke                        1
           11      Holder Assembly                     2
           12      Seat Position Latch                 2
           13      Backing Plate                       3
           14      Aluminum Track                      1
           15      Rack                                1
           16      Seat Stop Assembly                  2
           17      Rubber Foot                         2
           18      Transportation Wheel                2
           19      Console Assembly                    1
          19-01    Console Top Cover                   1
          19-02    Console Bottom Cover                1
          19-03    Console Display Board               1
          19-04    Key Board                           1
          19-05    Interface Board                     1
          19-06    W/Receiver, HR                      1
          19-07    UART Adapter Board                  1
           20      Drive Pulley                        1
           21      650m/m_Handpulse W/Cable Assembly   1
           22      Ø 25 × 15T_Rubber Foot Pad          2
Item   Description                           Qty
30     Front Shroud (R)                      1
31     Console Mast Cover                    1
32     Front Stabilizer Cover                1
33     Bottom Cover                          1
34     Round Disk                            2
35     Rear Shroud( L )                      1
36     Rear Shroud( R )                      1
37     Rear Stabilizer Cover                 1
38     Rotate Seat Assembly                  1
39     Seat Back Bracket                     1
40     Rotate Seat Adjusting Lever           1
41     Adjusting Lever                       1
43     Power Cord (Optional)                 1
52     6004_Bearing                          2
53     6203_Bearing                          4
54     Drive Belt                            1
55     Induction Brake                       1
56     Magnet                                1
57     Tension Rod Assembly                  1
58     Cantilever Anchor Assembly            1
59     Idler Wheel Assembly (Upper)          1
60     Idler Wheel Assembly (Lower)          1
61     Seat                                  1
62     Seat Back                             1
64     Handgrip Foam                         2
65     3/8" × 2- 1/4"_Hex Head Bolt          4
4
68     5/16" × 5/8"_Hex Head Bolt            8
71     3/8" × 2"_Hex Head Bolt               4
72     1/4" × 13 × 1T_Flat Washer            9
73     1/4" × 19 × 1.5T_Flat Washer          4
76     5/16" × 18 × 1.5T_Flat Washer         6
77     3/8" × 19 × 1.5T_Flat Washer          10
78     3/16" × 15 × 1.5T_Flat Washer         3
79     Ø 8 × Ø 18 × 3T_Knurled Lock Washer   4
80     Ø 1/4"_Split Washer                   4
Item   Description                                   Qty
82     5/16" × 1.5T_Split Washer                      8
83     5/16" × 19 × 1.5T_Curved Washer                6
84     3/8" × 25 × 2.0T_Flat Washer                   4
85     Ø 17_C Ring                                    2
86     Ø 20_C Ring                                    2
88     M8 × 7T_Nyloc Nut                              4
89     3/8" × 7T_Nyloc Nut                            6
91     5/16" × 6T_Nyloc Nut                           5
93     M6 × 38m/m_Socket Head Cap Bolt                2
94     5/16" × 3/4"_Hex Head Bolt                     6
95     M5 × 12m/m_Flat Head Socket Screw             10
97     Ø 3 × 20m/m_Tapping Screw                      4
98     M6 × 15m/m_Phillips Head Screw                 2
99     M5 × 12m/m_Phillips Head Screw                21
100    Ø 5.5 × Ø 15 × 1T_Flat Washer                  4
101    M5 × 15m/m__Socket Head Cap Bolt               3
102    5 × 19m/m_Tapping Screw                        6
103    Ø 3.5 × 12m/m_Sheet Metal Screw               18
104    Ø 12.9 × 30L_Spring                            1
106    5/16" × 1-3/4"_Button Head Socket Bolt         4
107    Ø 3.5 × 20m/m_Sheet Metal Screw                3
109    3/8" × 7T_Nut                                  4
110    3/8" × 2"_Flat Head Socket Bolt                2
111    M5 × P0.8 × 10L_Flat Phillips Head Screw       8
112    12/14m/m_Wrench                                1
114    Phillips Head Screw Driver                     1
116    Pedal(L)                                       1
117    Pedal(R)                                       1
126    HGP Wire Grommet                               1
127    5/16" × 16 × 1T_Flat Washer                    3
128    Seat Back Cover                                1
129    M6 × P1.0 × 6T(mm)_Nyloc Nut                   3
131    Ø 20 × 88m/m_Adjusting Lever Rotate Axle(L)    1
132    14/15m/m_Wrench                                1
141    Handle Bar Cover                               1
143    Seat Track Fixing Plate                        1
Item   Description                             Qty
148    Block                                   1
160    5/16" × 16mm × 1.5T_Flat Washer         6
161    M6 × 10L_Flat Phillips Head Screw       4
162    1/4" × 16 × 1.0T_Flat Washer            4
163    Ø 5/8" × 13.2 × 8m/m_Sleeve             4
164    M6 × 19L_Nut                            4
165    M6 × 10L_Button Head Socket Bolt        4
166    PU Wheel                                7
167    Steel Cable(1100L)                      1
173    M5 × 5.0T_Nyloc Nut                     2
175    3/8" × 2-3/4"_Hex Head Bolt             2
177    Rubber Foot Pad                         1
178    75 × 25 × 2.0T_Square End Cap           1
179    Ø 13.5 × 60L_Spring                     1
180    M5 × 30m/m_Phillips Head Screw          4
181    M5 × 6L_Phillips Head Screw             2
185    3/8" × 4T_Nut                           1
187    M4 × 5L_Phillips Head Screw             4
188    M10 × 1.25_Nut                          2
190    M6 × 10L_Phillips Head Screw            4
191    M6 × P1.0 × 30m/m_Phillips Head Screw   1
192    M5 × 20m/m_Phillips Head Screw          1
193    Ø 10_C Ring                             2
194    Ø 17 × 23.5mm × 1T_Flat Washer          4
195    Ø 5 × Ø 12 × 1.0T_Flat Washer           1
196    Ø 6.5 × Ø 25 × 1.5T_Flat Washer         2
197    M6 × P1.0 × 5.0T_Nut                    3
198    Ø 10 × Ø 24 × 3T_Nylon Washer           2
200    M5_L Allen Wrench                       1
201    Short Phillips Head Screw Driver        1
202    Ø 5 × Ø 10 × 1T_Flat Washer             1
203    Ø 8.5 × Ø 18 × 1.5T_Flat Washer         10
205    Ø 8.5 × Ø 26 × 2.0T_Flat Washer         2
206    Ø 10 × Ø 25 × 1.5T_Flat Washer          2
207    5/16" × UNC18 × 3/4"_Hex Head Bolt      8
208    5/16" × UNC18 × 1-1/4_Hex Head Bolt     1
Item   Description                                    Qty
209    5/16" × UNC18 × 5/8"_Hex Head Bolt              2
213    5/16" × UNC18 × 6T_Nyloc Nut                    9
215    3/8" × UNC16 × 7T_Nyloc Nut                     2
216    M6 × P1.0 × 6T_Nyloc Nut                        2
217    M12_Nyloc Nut                                   1
220    3/8" × UNC16 × 1-3/4"_Socket Head Cap Bolt      2
221    M6 × P1.0 × 40L_Socket Head Cap Bolt            2
222    M6 × P1.0 × 25L_Socket Head Cap Bolt            5
223    M12 × P1.75 × 120L_Socket Head Cap Bolt         1
225    M5 × P0.8 × 70L_Phillips Head Screw             1
227    M8 × P1.25 × 20L_Button Head Socket Bolt        4
228    M8 × P1.25 × 25L_Button Head Socket Bolt        3
229    5/16" × UNC18 × 3/4"_Button Head Socket Bolt    1
230    M5 × P0.8 × 4T_Luck Nut                         1
231    Ø 16_C Ring                                     3
232    Ø 14 × 10 × 25m/m_Podwer metallurgy Sleeve      2
234    Ø 16 × 66L × 13_Torsion-Spring                  2
236    Power Adaptor                                   1
237    Generator/Brake Controller                      1
238    AC Electronic Module                            1
239    15.9 × 22m/m_Podwer metallurgy Sleeve           4
241    Scale Arrowhead                                 2
242    Cover                                           1
244    Cylinder                                        1
245    Rotate Disk                                     1
246    Lever Fixing Plate                              1
247    Release Lever(147mm×44mm×52mm)                  1
248    ChenChin Torsion-Spring                         2
249    Release Lever(TKL24AF(Left))                    2
250    Brake Pad - Wool Felt                           1
251    Steel Cable(358mm)                              1
258    Steel Cable(84.5×76cm)                          1
262    800m/m_Wire Brake Coil Harness(Red)             1
263    950m/m_Wire Brake Coil Harness(Red)             1
264    1300m/m_Sensor W/Cable                          1
266    1950m/m_Computer Cable(Ferrite Core)            1
Item   Description                                  Qty
267    350m/m_Connecting Wire,Adaptor Power Cord     1
268    1200m/m_Connecting Wire(Ferrite Core)         1
269    2100m/m_Hand Pulse Sensor Assembly W/Cable    1
270    80m/m_Connecting Wire (White)                 1
271    200m/m_Ground Wire                            1
272    1500m/m_Computer Cable                        1
273    800m/m_Hand Pulse Extension Cable             1
274    Hand Pulse Wire, SMP-2V+800mm                 1
275    Iron Cover                                    2
276    M6 × P1.0 × 57L_Eye Bolt                      1
277    Ø 1/2" × Ø 26 × 2.0T(mm)_Flat Washer          1
280    10m/m_Wrench                                  1
281    80m/m_Connecting Wire (Black)                 1
282    Ø 12 × Ø 18 × 8L_Podwer metallurgy Sleeve     2
283    M8_L Allen Wrench                             1
284    13.14m/m_Wrench                               1
285    M4 × P0.7 × 12L_Phillips Head Screw           6
286    M4 × P0.7 × 5T_Nyloc Nut                      2
287    Isolation Column                              4
288    Ø 10 × Ø 25 × 0.8T_Nylon Washer               4
289    M4 × 3.5T_Nut                                 4
290    M5_Star Washer                                2
291    M8 × P1.5 × 120L_J Bolt                       1
292    Ø 8.5 × Ø 26 × 2.0T_Flat Washer               2
293    M8 × P1.25 × 6.0T_Luck Nut                    2
295    Ø 5 × Ø 12 × 1.0T_Flat Washer                 4
296    Ø 8 × 1.5T_Spring Washer                      1
297    25mm × 50m/m_Square End Cap                   2
298    Ø 8 × Ø 20 × 1T_Nylon Washer                  2
299    HGP Wire Grommet                              2
300    Ø 5 × 1.5T_Spring Washer                      2
301    450m/m_Ground Wire                            1
302    Crank Arm (L)                                 1
303    Crank Arm (R)                                 1
304    Ø 5.5 × Ø 15 × 1.5T_Flat Washer               6
305    Buckle                                        4
306    Snap Seat                                     4


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
irre
tare
repens
ere aero ot

(u)pnosys au0csy | ZO

(1)pnosys 34043 | 90

PY BjoOsuC> ‘ 49A0D

ayesg fe21UueYyr2y 42A27 aseajoy

U0d4 ‘4eg BjpueH ‘|
Ajquiassy ajosuo> }to |
Pa | oa


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. Preventative Maintenance.

1.1 Check for Pedal
As shown in Figure 3.1.1 and Figure 3.1.2, check whether the pedalis loosened. If the right pedal is loosened, lock it clockwise.
If the left pedal is loosened, lock it counterclockwise...

Figure 3.1.1 Figure 3.1.2-

1.2 Check for Front Handle Bar
As shown in Figure 3.2.1, check if the handle is properly adjusted or loosened, and if it is loose, tighten the screw.

Figure 3.2.1-


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.2 Pedal & Crank Arm Replacement.

6.2.1 Pedal Replacement-

6.2.1.1 Remove Pedal-
As shown in Figure 6.2.1 and Figure 6.2.2, the left pedalis disassembled counterclockwise and the right pedalis
disassembled clockwise.-

Figure 6.2.1 Figure 6.2.2.
6.2.1.2 Pedalassembly: Follow step 6.2.1 in reverse order.
6.2.2 Crank Arm Replacement-
6.2.2.1 Remove Crank Arm

As shown in Figure 6.2.3 and Figure 6.2.4, remove the crank arm end cap and loosen the nut anticlockwise. As shown in
Figure 6.2.5, use the extractor to withdraw the crank arm. (Both sides are the same.)-


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.8.1 Front Shroud (L) Replacement-

6.8.1.1 As shown in Figure 6.8.1, take off the round disk.-

Figure 6.8.1-

6.8.1.2 As shown in Figure 6.8.2, take off the screw on the front of front shroud (L). As shown in Figure 6.8.3, take off the 7~
screws on the front shroud (L) to remove the front shroud (L).-


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.8.1.3 Frontshroud (L) assembly: Follow step 6.8.1.1 to step 6.8.1.2 in reverse order.-
6.8.2 Front Shroud (R) Replacement-
6.8.2.1 Refer to step 6.8.1 to remove the front shroud (L).-

6.8.2.2 Asshown in Figure 6.8.4, take off the round disk..

Figure 6.8.4~

6.8.2.3 As shown in Figure 6.8.5, take off the 2 screws on the main frame first. As shown in Figure 6.8.6, take off the 2
screws on the front shroud (R). As shown in Figure 6.8.7, unplug 3 wires in the front and inside the front shroud (R) to
remove the front shroud (R).-

Figure 6.8.5.


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
a 2
* =)
-
an:
a
Pc) ~D
a UF
r—)
ar
S =
a &
(ae
—
—-_
a Of
o>
3 &
eB
g .= 2 a) a
a) =
5 Le
7 2 6
= reese
ob
i}
| ny
|
an
_
>
SS
oO
ge
ad
-_
—
°o
Zz
—
a
la = |
a
ge
N
w
=
a
¥
=
Fi
a)
~
o t
=
o
—
o
»
_
wn
7
_
°
i—}
i=


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 48 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7. Trouble Shooting.

7.1 Slip/ Shedding of Drive Belt-
If you find the belt slipping or falling off, please refer to Figure 7.1.1 and Figure 7.1.2, and follow step 6.10.1.3 to tighten the nut
to adjust the tension.-

Figure 7.1.1 Figure 7.1.2«

7.2 Noise/ Feet Feeling~
As shown in Figure 7.2.1 and Figure 7.2.2, if there is any feeling of foot during pedaling, please refer to step 3.1 to lock the
pedal. If the phenomenon of foot still exists, please refer to step 6.2 to check whether the crank loose.-

Figure 7.2.1 Figure 7.2.2«


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
toe

BLL
Sy ore a

Tx Ray,
fo bee Zp,

€

Bulmesp MalA papo|dxy


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7.0 R parts list

Item Description lOty_|

u Main Frame 1
iConsole Mast 1

3 Mast Handlebar 1
Seat Carriage 1

5 Seat Back Bracket 1
6 Handle Bar 1
Rear Stabilizer 1

L Seat Wheel Adjustment Plate(L) 2
OR Seat Wheel Adjustment Plate(R) A
10. Idler Bracket 1
11 Holder Assembly j2
12 Seat Position Latch 2
13 Backing Plate 13
14 {Aluminum Track 1
15 Rack 1
16 Seat Stop Assembly 2
7 Rubber Foot b
18 Transportation Wheel 2
19 Console Assembly 1
19-1 Console Top Cover 1
19-2 Console Bottom Cover 1
19-3 Console Display Board 1
19-4 Key Board 1
19-5 Interface Board 1
19-6 W/Receiver, HR 1
19-7 UART Adapter Board 1
0 Drive Pulley 1
750mm_Handpulse W/Cable Assembly 1

25 x 15T Rubber Foot Pad 2

32(1.8T) Button Head Plu |2

4 25.4 x 2.0T_ Button Head Plug 2

5 138 Seat Track Wheel 8
7 900mm_Handpulse W/Cable Assembly(White) 1
8 {Crank Arm End Cap 2


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
= Front Shroud (L)

Front Shroud (R) 1
~ {Console Mast Cover 1
32 Front Stabilizer Cover 1
33 Bottom Cover 1
34 Round Disk j2
35 Rear Shroud (L) 1
36 Rear Shroud (R) 1
37 Rear Stabilizer Cover 1
—~B8 Rotate Seat Assembly 1
39 Seat Back Bracket 1
143 Power Cord (Optional) 1
52 16004 Bearing 2
53 6203 Bearing 4
54 Drive Belt 1
55 Flywheel 1
56 {Magnet 1
57 Tension Rod Assembly 1
58 |Cantilever Anchor Assembly 1
59 Idler Wheel Assembly (Upper) 1
60 Idler Wheel Assembly (Lower) 1
61 Seat 1
62 Seat Back 1
| (64 Handgrip Foam 2
65 3/8" x 2- 1/4"_Hex Head Bolt 4
66 1/4" x 3/4" Hex Head Bolt 4
68 5/16" x 5/8" Hex Head Bolt 10
71 3/8" x 2" Hex Head Bolt 4
72 1/4" x 13 x 1T_Flat Washer 9
73 1/4" x19 x 1.5T Flat Washer 4
176 15/16" x 18 x 1.5T Flat Washer 6
77 3/8" x 19 x 1.5T Flat Washer 12
78 3/16" x 15 x 1.5T Flat Washer 3
79 ge x O18 x 3T_ Knurled Lock Washer 4
80 @1/4" Split Washer 4
-(g2 paces Split Washer 8
83 5/16" x 19 x 1.5T Curved Washer 2


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
84 3/8" x 25 x 2.0T Flat Washer 4
85 ee C Ring 2
86 1020 C Ring 2
88 M8 x 7T_ Nylon Nut 4
3/8" x 7T Nylon Nut 8
1 15/16" x 6T_ Nylon Nut 14
3 M6 x 38mm _Socket Head Cap Bolt 2
4 5/16" x 3/4" Hex Head Bolt l6
5 M5 x 12mm_Flat Head Socket Screw 10
7 lo3 x 20mm_ Tapping Screw 4
8 M6 x 15mm _Phillips Head Screw 2
99 M5 x 12mm_Phillips Head Screw {21
100 125.5 x @15 x 1T_ Flat Washer 4
101 M5 x15mm_ Socket Head Cap Bolt 3
102 5 x 19mm_Tapping Screw le
103 @3.5 x 12mm_Sheet Metal Screw 18
106 5/16" x 1-3/4" Button Head Socket Bolt 4
107 3.5 x 20mm_Sheet Metal Screw 3
11 M5 = P0.8 x 10L Flat Phillips Head Screw 8
112 12/14mm_ Wrench 1
114 Phillips Head Screw Driver 1
116 Pedal(L.R) 1
126 HGP Wire Grommet 1
127 5/16" x 16 x 1T_Flat Washer 4
128 Seat Back Cover 1
129 M6 x 6T_ Nylon Nut 3
132 14/15mm_Wrench 1
141 Handle Bar Cover 1
143 Seat Track Fixing Plate 1
148 Block 1
160 |5/16" x 16 x 1.5T Flat Washer \6
161 M6 x 10L_Flat Phillips Head Screw 4
162 1/4" x 16 x 1.0T Flat Washer 4
163 1@5/8" x 13.2 x 8mm _ Sleeve 4
164 M6 x 19L_Nut 4
165 M6 x 10L_Button Head Socket Bolt 4
166 PU Wheel 4


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
173 MS x 5T_Nylon Nut 2
175 3/8" x 2-3/4" Hex Head Bolt 2
V7 Rubber Foot Pad 1
178 75% 252.07 Square End Ca 7
179 @13.5 x 54. Spring 1
180 M5 = 30mm_Phillips Head Screw 4
181 M5 x 6L_Phillips Head Screw 2
185 3/8" x 4T Nut 1
187 M4 5L Phillips Head Screw 4
188 M10 = P1.25 x 10T Nut 2
190 M6 *10L_ Phillips Head Screw 4
191 M6 x 30mm_Phillips Head Screw 1
192 M5 x 20mm_Phillips Head Screw 1
193 @10_C Ring 2
HEE! @1? x 623.5 x 1T_Flat Washer 4
195 5 = @12 « 1.07T_Flat Washer 5
196 6.5 =x 225 x 1.57 Flat Washer 2
197 M6 = P1.0 x 5.0T Nut 3
198 @10 x @i24 x 3T_ Nylon Washer 2
200 S5mm_L Allen Wrench 1
[201 Short Phillips Head Screw Driver 1
203 8.5 = 218 = 1.57 Flat Washer 10
205 x 26 = 2.0T Flat Washer 2
206 @10 x @25 x 1.5T_Flat Washer 2
207 5/16" x UNC18 x 3/4" Hex Head Bolt 6
208 5/16" x UNC18 x 1-1/4 Hex Head Balt 1
217 M12 Nylon Nut 1
220 3/8" x UNC16 x 1-3/4" Socket Head Cap Bolt 2
222 M6 x 25mm_Socket Head Cap Bolt 5
— M12 x P1.75 x 120L Socket Head Cap Bolt 1
Mé8 x 20L Button Head Socket Bolt 4
os Mé « P1.25 x 25L_Button Head Socket Balt 3
229 5/16" x UNC18 x 3/4" Hex Head Bolt 1
1232 @14 = 10 x 25mm _ Powder Metallurgy Sleeve 2
234 @16 x 66L x 13. Tension Spring 2

236 Switching Power Supply
[237 Brake Controller


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 69 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
238 AC Input Module

241 Scale Arrowhead

242 Cover

244 __|Gas Cylinder

245 Rotate Disk

246 Lever Fixing Plate

247 Release Lever(147mmx44mmx52mm)

248 Torsion-Spring

50 Brake Pad

251 Steel Cable(358mm)

258 Steel Cable

262 800mm_ Wire Brake Coil Harness(Red)

263 950mm_Wire Brake Coil Harness(Red)

264 1300mm_Speed Sensor VW/Cable

266 1950mm_Computer Cable

267 350mm_Connecting Wire Adaptor Power Cord

268 1200mm_ Connecting Wire

269 2100mm_Handpulse Wire

270 80mm Connecting Wire (White)

27 (200mm _ Ground Wire

272 1500mm_Computer Cable

273 800mm_Handpulse Wire

74 800mm_ Handpulse Wire( White)

275 lron Cover

276 M6 = 57L_Idle Wheel Screw

277 12.7 x @26 = 2.0T Flat Washer

280 10mm_ Wrench

281 8Omm_ Connecting Wire (Black)

262 G12 x @18 « BL Powder Metallurgy Sleeve

1283 8mm_L Allen Wrench

284 1314mm_ Wrench

285 M4 12L Phillips Head Screw

286 M4 x 5T Nylon Nut

287 Isolation Column

288 (23/8" « @19 x 1.57 Flat Washer


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 52 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
289 M4 x 3.5T Nut 4
290 M5 Star Washer 2
291 MS x P15 x 120L | Bolt 1
292 8.5 x @26 = 2.0T Flat Washer 2
293 M8 x 6T Luck Nut 2
297 (25.4 x 50.5 x 14.3L_ Square End Cap [2
299 Wire Cap 2
300 @5*15T Split Washer 2
(301 450mm _Ground Wire 1
302 Crank Arm (L) 1
303 [Crank Arm(R) 1
304 _-|@5.5x @15«1.5T Flat Washer 6
305 Buckle 4
306 Snap Seat 4
308 Transportation Wheel Fixing Plate 1
314 M5 PO.8 x 25L Flat Head Socket Screw 2
315 M5 = PO.8 « 45L_ Socket Head Cap Bolt 1
316 5 = 410 x 1.0T Flat Washer 1
317 M6 x P10 x 12L Socket Head Cap Bolt 12
318 6x 212 «1.57 Flat Washer 8
371 M8 x 30mm_Flat Head Socket Screw 6
322 M8 x 1.25% 6.57 Square Nut 6
330 Nylon wheel [3
331 Release Lever 2
[332 Nylon Handgrip [2
[333 Lever Anchor 1
334 Seat Front/Aft Adjustment Lever 1
335 @13.5 x 30mm_Spring 1
336 Handeri 1
337 Steel Cable(S40L) 1
338 Seat Belt 1


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 74 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
a4iM punoli9

dns s2mMOd Zur aA

Ai HUDRAS wwg0z
(¥) a1qe2/™ (1) sqea/m

s0SuUe5 asind puey J0SUe5 25/Nd puey

2jnpow

34M Burnssuu0> 3ndul Dy =
i t
wwoozt
ps0? Jamog
aq
3yqe2/m “Assy Jemod 90 AGE WWOSE ¥
s0SUa5 asjnd
puey WwoOTZ
SajOsQUO? ayeZE
: ssouseH
= [HOD Syesg SIM WWINSE
- wows 2ye2g VOR NpU
eS - 2/G2> Joyndwo? wWwOSET wees i " P
iS
Ajqwiesse ajosucD ye ::
os S3SUJEH a ; Sih)
a POD Syesg s41M WwOOSs ' : WE "*

ij 2922
: JOSUSS YURI WWIOSST

3/ Qed sOSUSS SjBUE WWIOOST

weiseig SULIM\ OOOZYW
