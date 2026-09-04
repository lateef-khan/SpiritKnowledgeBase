                       1 of 40




SERVICE MANUAL
                 LCR(2023)
              SR625A-SB026
        ENT RECUMBENT BIKE
                                                                                                                                                         2 of 40


                                                                     -Contents-
1.Outlines......................................................................................................................................................... 4
2.Electronic Parts ........................................................................................................................................... 5
     2.1 Console ................................................................................................................................................ 5
     2.2 Controller and Driver parts ................................................................................................................. 5
3.Electrical Configurations ......................................................................................................................... 6
4.Product Operation..................................................................................................................................... 7
5.Unit Block Diagrams................................................................................................................................ 11
6.Basic Connections and Wiring............................................................................................................. 12
     6.1 Display Board wire Connections....................................................................................................... 12
     6.2 Display Board PCB Component Locations....................................................................................... 13
       6.3 Interface Board Wire Connections ................................................................................................... 14
       6.4 Brake Controller Wire Connections .................................................................................................. 14
       6.5 Brake Controller PCB Component Locations................................................................................... 15
       6.6 Brake Controller Functions ............................................................................................................... 15
7. Product Safety Instructions................................................................................................................... 16
     7.1 Important Safety Instructions............................................................................................................ 16
     7.2 Important Electrical Instructions ....................................................................................................... 16
     7.3 Important Grounding Instructions .................................................................................................... 16
8. Error Messages / Troubleshooting ...................................................................................................... 17
     8.1 Error Message: EEPROM ERR ........................................................................................................... 18
     8.2 Error Message: LWR not found ........................................................................................................ 18
       8.3 Error Message: LWR not match ........................................................................................................ 18
       8.4 Test Configuration ............................................................................................................................. 19
       8.5 Circuit Diagram ................................................................................................................................. 20
       8.6 Maintenance Menu ........................................................................................................................... 21
       8.7 Troubleshooting procedure Matrix .................................................................................................. 22
9. Parts Replacing Guide .......................................................................................................................... 23
     9.1 Replacing the Console ...................................................................................................................... 23
     9.2 Replacing the Console Mast and Cover........................................................................................... 24
     9.3 Replacing the Crank Arm and Pedal ................................................................................................ 25
     9.4 Replacing the Front Shrouds ............................................................................................................ 26
       9.5 Replacing the Belt and Idler Bracket ................................................................................................ 28
       9.6 Replacing the Crank Axle and Drive Pulley ...................................................................................... 29
       9.7 Replacing the Induction Brake .......................................................................................................... 30
       9.8 Replacing the Seat Back and Seat Back Frame................................................................................ 31
       9.9 Replacing the Seat, Seat Handlebar, and Hand pulse Sensor ........................................................ 32
       9.10 Replacing the Rear Shrouds and Harness ..................................................................................... 33
       9.11 Replacing the Sear Carriage ........................................................................................................... 34
       9.12 Replacing the Aluminum Rail and Stabilizer Cover ....................................................................... 36
                                                                                                                                                3 of 40

10. Troubleshooting .................................................................................................................................... 37
     10.1 Troubleshooting for the Console Display problem and Error Message ...................................... 37
       10.2 Troubleshooting for the Drive Belt Slipping or Falling-off ........................................................... 38
       10.3 Troubleshooting for the Noise during pedaling ............................................................................ 40
             4 of 40


1.Outlines
                                  5 of 40


2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts
                                                                                             6 of 40


3.Electrical Configurations
Console              Interface that controls all functions of the Bike.
Brake Controller The circuit board consist of the DC power supply for console.
EMS Brake            It can change to increase or decrease resistance level of brake.


GENERAL INFORMATION
Console              It is including keypad to control and LCD Display.
                     Brake controller Include power supply and EMS driver control circuit.
EMS Brake            Work voltage: DC 0~21V
                     Control resistance increases and decreases.
                                                                                                                 7 of 40


4.Product Operation




Window Display Mode
IDLE Mode    -PICK ONE OF GUEST OR PERSON ACCOUNT.
             -The main screen of the Training section displays an overview of your activity and offers shortcuts to the
             most frequently used training modes: an immediate Start, a manually controlled timed workout
             (“Timer”), and up to 3 programs that you have marked as your favorites are arranged on this page for
             your quick access.
             -If in the Guest mode, you can set your age and weight here; it will help the machine calculate your
             workout summary more accurately.
             -If in the User mode, You have a personal account, including age、weight…etc. You will not need to re-
             create your profile.; it will help the machine calculate your workout summary more accurately.
SLEEP Mode   -The console will not get into SLEEP MODE when the setup is “OFF”, unless turn off the power. The sleep
             mode is to set in “ON”. There is no RPM input in IDEL MODE and enter to SLEEP MODE after 15 minutes
             without pressing any key.
             -In SLEEP MODE, TFT LCD screen will has no display, and backlit will be off. Press any key to wake up the
             system, and back into IDEL MODE.
                                                                                                                 8 of 40

             -Resistance in SLEEP MODE: Incline =1, Cooling Fan off.
Child Lock   -Pre-set: CHILD LOCK OFF (DISABLE). You could set the CHILD LOCK ON/OFF by Setting.
Mode         -The screen will display “CONSOLE LOCKED” when CHILD LOCK setup is ON. You could setup the CHILD
             LOCK MODE OFF by pressing “START” and ”ENTER” key for more than two seconds. After that it will enter
             to IDEL MODE.
             -All keys will be no action when CHILD LOCK MODE is active.
EXERCISE     -In IDEL MODE, press START key enter to MANUAL MODE. The age, weight is presetting value. Time
Mode         counting is count from 00:00. All countable data will count from “0”, and resistance is count up from “1”.
             -You could chose the program by pressing the program icon: MANUAL、HILL、FAT BURN、CARDIO、
             STRENGTH、HIIT、CUSTOM、HEAT RATE、FITNESS TEST. Then press “START” key to start the
             workout. All parameters will be the preset value.
PAUSE Mode   -Press “STOP” key enters to PAUSE MODE, and exercise parameters will be recorded.
             -The resistance level is “1”. The resistance should back to the preset level before it pauses when press
             “START” key or touch” Resume” icon.
             -It will enter to IDLE MODE after waiting by five minutes without pressing any key in PAUSE MODE.
END Mode     -The touch screen will display workout summary after end workout.
             END MODE workout information: Displays all finished message on the touch screen.
             -When the time counting is end, and END MODE display is finished without pressing any key in 3
             minutes. The system will enter IDLE MODE.
RESET Mode   -In idle mode (except when the child lock is on, in which case the reset function must be released first),
             press the Stop key for 3 seconds to enter the reset function and restart the system.
             -The reset mode clears all screens and enters idle mode after restarting.


Function
SPEED        Display the current speed in mile per hour.
             DISPLAY range is 0.0 to 99.9.
             WORK range is 0.0~99.9
LEVEL        Display the level position from 1 to 40.
             DISPLAY range is 0 to 999.
             WORK range is 1 to 40.
             LEVEL preset value is 1 to 40.
             Press “UP” or ”DOWN” to adjust level, each increment and decrement is 1.
TIME         TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
             is COUNT DOWN.
             DISPLAY range is 0:00 to 99:99.
             WORK range is 0:00 to 99:59.
             COUNT DOWN setup range is 10:00 to 99:00.
             When TIME is set, the count will go to zero.
             In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will
             continue count time.
LAPS         Display the total working laps quantity.
                                                                                                             9 of 40

           DISPLAY range is 0 to 99.
           WORK range is 0 to 99.
           Displays total laps quantity.
DISTANCE   Display the current distance in kilometer or Mile.
           DISPLAY range is 0.0 to 99.9.
           WORK range is 0.0 to 99.9.
CALORIES   Displays the cumulative calories burned at any given time during your workout.
           DISPLAY range is 0 to 999.
           WORK range is 0 to 999.
PULSE      Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be
           worn.
           DISPLAY range is 0 to 999.
           WORK range is 40 to 220 BPM.
           In EXERCISE Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value will become
           “0 ”.
                                                                                                             10 of 40

Function Button Locations




Button Function in each mode

Ready Mode
Stop Button     Non-function.
Start Button    Pressing “START” button to start bike, when pressing “START” button, there will be 3 second final
                count down on window display, then machine starts running. In MANUAL, bike starts at MIN LEVEL.
Fan Button      It can control ON/OFF for the fan.
Display key     Non-function.


EXERCISE Mode
Stop Button     press “STOP” button to stop bike.
Start Button    Non-function.
Fan Button      It can control ON/OFF for the fan.
Display key     Press DISPLAY key to display the exercise states when you are workout. There are have data states、
                charts and track three mode.
                        11 of 40


5.Unit Block Diagrams
                                     12 of 40


6.Basic Connections and Wiring
6.1 Display Board wire Connections
                                            13 of 40

6.2 Display Board PCB Component Locations
PCB Board Top view




PCB Board Bottom view
                                        14 of 40

6.3 Interface Board Wire Connections




6.4 Brake Controller Wire Connections
                                               15 of 40

6.5 Brake Controller PCB Component Locations




6.6 Brake Controller Functions
                                                                                                                                16 of 40


7. Product Safety Instructions
7.1 Important Safety Instructions
- To reduce the risk of electric shock, disconnect your bike from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the bike on a flat level surface with access to a 120-
volt, 15-amp grounded outlet with only the bike plugged into the circuit.
- Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the
grounded plug by using improper adapters or in any way modify the cord outlet.

7.2 Important Electrical Instructions
- Never use a ground fault circuit interrupt (GFCI) wall outlet with this bike. As with any appliance with a large motor, the GFCI
will trip often. Route the power cord away from any moving part of the bike including the elevation mechanism and transport
wheels.
- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a bike is
first turned on or even during use. If your bike is tripping the house circuit breaker (even though it is the proper current rating)
but the circuit breaker on the bike itself does not trip, you will need to replace the home breaker with a high inrush type. This is
not a warranty defect. This is a condition we as a manufacture have no ability to control. This part is available through most
electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part # QO120HM.


7.3 Important Grounding Instructions
- This product must be grounded. If the bike should malfunction or breakdown, grounding provides a path of least
resistance for electric current, reducing the risk of electric shock. This product is equipped with a cord having an equipment-
grounding plug. The plug must be plugged into an appropriate outlet that is properly installed and grounded in accordance with
all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a
qualified electrician or serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug
provided with the product if it will not fit the outlet; have a proper outlet installed by a qualified electrician. This product is for
use on a nominal 120-volt circuit and has a grounding plug that looks like the plug illustrated below. A temporary adapter that
looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly
grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from the adapter, must be
connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must
be held in place by a metal screw.
                                                                             17 of 40


8. Error Messages / Troubleshooting
Error Code List

            Code        Description
         EEPROM ERR     EEPROM failure
        LWR not found   Driver board controller is not found.
        LWR not match   Driver board controller is not match with console.


Tools Required

A multi-meter.
                                                                                                                18 of 40

8.1 Error Message: EEPROM ERR

Definition:
All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show “EEPROM ERR”.


Troubleshooting:
The EEPROM is abnormal, please replace the Display Board directly.


8.2 Error Message: LWR not found
Definition:
Brake controller is not found.


Troubleshooting:
1. Check connector of 6 PIN computer cable.
2. Replace Brake controller.
3. Replace Display board.


8.3 Error Message: LWR not match
Definition:
Brake controller is not match with console.


Troubleshooting:
1. Check brake controller number is CS51012.
2. Replace Display board.
                                                                                      19 of 40

8.4 Test Configuration

Test configuration: the console to brake controller connector pin defines function.




Test configuration: EMS Brake control function relate parts location.
                      20 of 40

8.5 Circuit Diagram
                                                                                                  21 of 40

8.6 Maintenance Menu
Press 10 times on “Settings” letter to enter engineering mode when you’re at the Settings page.
                                                                                                                          22 of 40

8.7 Troubleshooting procedure Matrix
Condition                       Reason                                                Solve
TFT LCDs not bright,            1. TFT LCD light is broken.                           1. Replace with new TFT LCD or console.
incomplete, or imperfect.       2. Power to console too low.                          2. Check AC power is 110-120V.
                                                                                      3. Check power to console.
                                                                                      4. Replace lower controller.
TFT LCD displays not bright,    TFT LCD displays are broken.                          Replace with new console.
incomplete, or imperfect.
Erratic pulse display.          1. Another chest belt in use around Elliptical.       1. Check for other chest belt use around
                                2. Other magnetic field disturbance.                     Elliptical.
                                3. Receiver is broken.                                2. Change the position or direction of
                                                                                         Elliptical.
                                                                                      3. Replace with new receiver.
Hand pulse lost its function.   1. Hands not on the hand pulse sensors or only one 1. Two hands hold the hand pulse.
(No pulse displayed on             hand on sensor.
monitor)                        2. The connector of HANDPULSE W/WIRE and              2. Connect the cable again.
                                   Console not connected properly.
                                3. The wires got damaged when connecting the          3. Replace with new cable.
                                   HANDPULSE W/WIRE and Console.
                                4. Hand pulse board is broken.                        4. Replace console or Hand pulse board.
Wireless lost its function.     1. Chest belt not worn properly.                      1. Check chest belt has proper contact with
(No pulse displayed on                                                                   skin and is oriented correctly.
monitor)                        2. Distance is too far and exceeds range of receiver. 2. User chest belt in front of console within 3
                                                                                         feet.
                                3. Chest belt battery is weak or dead.                3. Replace with new lithium battery type is
                                                                                         CR2032.
Chest belt too close to the     Weak battery.                                         Replace with new lithium battery with type
Bike.                                                                                    CR2032.
                                                                                                                    23 of 40


9. Parts Replacing Guide
9.1 Replacing the Console
Step 1: Unscrew 4pcs of M5x12m/m Phillips Head Screws (99) with Phillips Head Screwdriver (114) and the Console (19) can be
       released. (Figure 1)
Step 2: Unplug all connected cables behind the console. (Figure 2)
Step 3: Reverse above steps to install the new console.
Step 4: Use Phillips head screwdriver to release four M5 3.5×12mm Phillips Head Screws then remove the PAD holder. (Figure 3)




                        Figure 1                                                     Figure 2




                      Figure 3
                                                                                                                        24 of 40

9.2 Replacing the Console Mast and Cover
Step 1: Take the console apart first.
Step 2: Then use 12/14 m/m wrench (112) to release 2pcs of 5/16" x5/8" Hex Head Screws (68), 2pcs of 5/16"x1.5T Split
       Washers and 2pcs of 5/16”x18x1.5T Flat Washers (76) and the Handlebar Assembly (3) can be released, as shown in
       figure 1.
Step 3: Reverse the above step to resume the Handlebar Assembly (3).
Step 4: Separate Console Mast Cover (31) from Front Shroud (L/R) (29) (30) at left and right sides of the seam with properly tool
       (figures 2.3) and release the latches which lock Console Mast Cover (31) and Front Shroud (L/R) (29) (30) together to pull
       up Console Mast Cover (31).
Step 5: Unscrew 6pcs of 5/16" × 5/8" Hex Head Bolt (68), 4pcs of 5/16" × 18 × 1.5T flat Washer (76) and 2pcs of 5/16" × 19 × 1.5T
       Curved Washer (83) with the 12m/m Wrench, to pull out the Console Mast (2) as shown in figure 4.
Step 6: To resume Console Mast (2), guide the Computer Cable (44) and Hand Pulse Sensor Assembly W/Cable (45) through the
       Console Mast (2) and out of console securing plate (2~3) then tighten 6pcs of 5/16"×5/8"Hex Head Bolts (68), 6pcs of
       5/16"×18×1.5T Flat Washers (76) and 2pcs of 5/16"×19×1.5T Curved Washers (83) with 12m/m open wrench.




                        Figure 1                                                          Figure 2




                        Figure 3                                                          Figure 4
                                                                                                                       25 of 40

9.3 Replacing the Crank Arm and Pedal
Step 1: Use 13/15m/m wrench to turn the Left Pedal (116) clockwise and Right Pedal (117) counterclockwise to disassemble
       these two pedals. (Figure 1, 2)
Step 2: Turn pedals reversely against the above step to resume both pedals.
Step 3: Take off the Crank Arm End Cap (28) and release the M10x1.25 Nut (108) by using the wrench as shown in figure 3.
Step 4: Use the plug matching with the Cranks (51L, 51R) and turn with hex wrench to release the Cranks (51L, 51R) as shown in
       figure 4.
Step 5: To resume the Cranks (51L, 51R), use the hammer to hit the Cranks tightly match with the Drive Pulley Axle (8) and turn
       the nut tightly onto the Axle. Plug in the Crank Arm End Cap.




                       Figure 1                                                         Figure 2




                       Figure 3                                                         Figure 4
                                                                                                                       26 of 40

9.4 Replacing the Front Shrouds
Step 1: Take apart the crank arm and console mast cover.
Step 2: To release Left Front Shroud (29), use Phillips Head Screwdriver to release 7pcs of ø3.5x16 Sheet Metal Screw (103) and
       2pcs of 5x16 Tapping Screws (101) as shown in figure 1.
Step 3: To release Right Front Shroud (30), on the mainframe, unscrew 2pcs of Ø3.5 × 16mm sheet Metal Screws (103) with 2pcs
       of 3/16" × 15mm × 1.5T_Flat Washers (78) then, on the Right Front Should, unscrew 2pcs of 5x16 Tapping Screws At last,
       take DC adaptor (48) cable away from the AC power switch connector (159) to remove front Shroud (R) (30), as shown in
       figures 2, 3 and 4.




                         Figure 1                                                       Figure 2




                         Figure 3                                                       Figure 4
                                                                                                                          27 of 40

Step 4: To resume the Right Front Shroud, put it on the mainframe and plug in Locate 2pcs of Ø3.5 × 16mm Sheet Metal Screws
       (103) with 2pcs of 3/16"x15mmx1.5T Flat Washers (78) on the mainframe loosely then tighten 2pcs of 5x16 Tapping
       Screws (101) on the mainframe and tighten up all loose screws.
Step 5: Match Left Front Chain Cover (29) with Right Front Chain Cover (30) and secure both covers with 7pcs of Ø3.5 × 16mm
       Sheet Metal Screws (103) and then 2pcs of 5x16 Tapping Screws (101).
Step 6: Pay special attention to install Front Shroud (30) as On/Off Switch (159) must be secured with left and right Front Shrouds
       (29)(30). Top and bottom of the On/Off Switch (159) will be secured inside of left and right Front Shroud (29)(30) while
       left and right of On/Off Switch (159) will be secured outside of left and right Front Shroud (29)(30) as shown in figure 5.




                         Figure 5
                                                                                                                          28 of 40

9.5 Replacing the Belt and Idler Bracket
Step 1: Take both left and right front shrouds apart.
Step 2: Use 13 m/m wrench to release M8x7T Nut and take off the J-Bolt. (Figure 1.)
Step 3: Use Phillips Head Screwdriver to unscrew 3pcs of M6x7T Phillips Head Screws on Idle Arm and the Belt can be taken off.
       as shown in figure 2.
Step 4: To release the Idle Arm, Unscrew 3pcs of M6x15 Phillips Head Screws with 3pcs ofø1/4" Split Washers and 3pcs of
       1/4”x13x1T.
Step 5: To resume the Belt and Idle Arm, use Phillips Head Screwdriver to secure the Generator Flywheel with 3pcs of M6x15
       Phillips Head Screws together with 3pcs ofø1/4" Split Washers and 3pcs of 1/4”x13x1T Flat Washers. Turn the Drive Pulley
       to let the Belt on the Pulley, hook the J-Bolt on the mainframe and use 13 m/m wrench to tighten M8x7T Nut on the J-
       Bolt until the Belt is with acceptable tension. Use audio tension gauge to make sure the frequency within the range
       of180±10HZ. At last, turn the Drive Pulley and make sure the Drive Belt is set in the center without falling out of pulley, as
       shown in figure 3.




                         Figure 1                                                          Figure 2




                 Figure 3
                                                                                                                        29 of 40

9.6 Replacing the Crank Axle and Drive Pulley
Step 1: Take apart both left and right shrouds and the drive belt.
Step 2: Use C-ring pliers to take off ø20 C-ring axle and the Drive Pulley Axle can be released as shown in figure 1.
Step 3: To release the Drive Pulley, use 2pcs of wrench to unscrew 4pcs of 1/4”x3/4” Hex Head Screws (66) with 8pcs of
       1/4”x13x1T Flat Washers (72) and 4pcs of 1/4" × 5.5T Nut (90) as shown in figure 2.
Step 4: Reverse the above steps to install new Crank Axle.




                         Figure 1                                                          Figure 2
                                                                                                                 30 of 40

9.7 Replacing the Induction Brake
Step 1: Take both left, right front shrouds and Drive belt apart.
Step 2: Unplug electric wires connected to the Generator Flywheel then use 11 m/m wrench to unscrew 4pcs of 1/4”x3/4” Hex
       Head Screws with 4pcs of 1/4"x13x1T Flat Washers and 4pcs of ø1/4"Split Washers and you can release Generator
       Flywheel.
Step 3: Follow steps in order to resume the flywheel.
                                                                                                                    31 of 40

9.8 Replacing the Seat Back and Seat Back Frame
Step 1: Use open wrench to unscrew 6pcs of 3/8"×3/4"Hex Head Bolts (176) and 6pcs of 3/8"×19×1.5T Flat Washers (77) to take
       apart Seat Back Frame (5) as shown in figure 1.
Step 2: Use Phillips Head Screwdriver to unscrew Seat Back Cover, 4pcs of M5×15m/m Phillips Head Screws as shown in figure 2.
Step 3: Use Combination M5 Allen Wrench to release M8×15m/m Button Head Socket Bolt to take Seatback Cushion apart as
       shown in figure 3.
Step 4: Reverse above step to resume.




                        Figure 1                                                      Figure 2




                      Figure 3
                                                                                                                      32 of 40

9.9 Replacing the Seat, Seat Handlebar, and Hand pulse Sensor
Step 1: Use Phillips Head Screwdriver to release 4pcs of M6× 15mm Phillips Head Screws (98) to take the Seat (61) apart as
       shown in figure 1.
Step 2: Use two 14m/m Wrenches to unscrew Seat Carriage (4), 2pcs of 3/8"×2-3/4" Hex Head Bolts (175), 4pcs of 3/8" × 1-
       3/4"_Hex Head Bolt (71), 6pcs of 3/8"×7T Nyloc Nuts (89) and 6pcs of Ø3/8"×19m/m×1.5T Flat Washers (77), to take
       apart Seat Handlebar (6). as shown in figures 2 & 3.
Step 3: Unplug HGP Wire Grommet (126) which secures Hand pulse W/Cable Assembly (21.27) and use Phillips Head Screwdriver
       to release 4pcs of Ø3×20mm Tapping Screws (97) to take apart Hand pulse W/Cable Assembly (21,27) as shown in figures
       4 & 5.




                       Figure 1                                                   Figure 2




                       Figure 3                                                   Figure 4




                    Figure 5
                                                                                                                     33 of 40

9.10 Replacing the Rear Shrouds and Harness
Step 1: Use Phillips Head Screwdriver to unscrew 7pcs of Ø3.5x16 Self Tapping Screws (103) and 2pcs of 5x16 Tapping Screws
       (101), which are on Left Rear Chain Cover (35). Unplugging Hand pulse wire (26) and Left Rear Chain Cover can be
       released as shown in figures 1 & 2).
Step 2: On the Right Rear Chain Cover (36), unscrew Ø 3.5x16 Self Tapping Screws (103) with 3/16" × 15mm × 1.5T_Flat
       Washers (78) and 2pcs of 5x16 Tapping Screws (101) and the Right Rear Chain Cover (36) can be released as shown in
       figure 3)。
Step 3: To resume Rear Shroud (R)(36), return Rear Shroud (R)(36) onto the Main Frame (1) and slightly tighten with Ø3.5×16mm
       Sheet Metal Screw (103) and 3/16"×15mm×1.5T Flat Washer (78), then use 2pcs of 5×16m/m Tapping Screws (101) to
       secure on the Main Frame (1) and lock with Ø3.5×16m/m Sheet Metal Screw (103).
Step 4: Combine Rear Shroud (L) (35) and Rear Shroud (R) (36) together and secure with 7pcs of Ø3.5×16m/m Sheet Metal
       Screws (103) and 2pcs of 5×16m/m Tapping Screws (101).




                       Figure 1                                                        Figure 2




                       Figure 3
                                                                                                                          34 of 40

9.11 Replacing the Sear Carriage
Step 1: Take apart Aluminum Axle End Cap (135) as shown in figure 1.
Step 2: Use 2pcs of Phillips Head Screw Drivers to release two M6×15m/m Phillips Head Screws (98) as shown in figure 2 to take
       apart Seat Stop Axle (11) and pull Seat Front/Aft Adjustment Lever (167) upward to take apart Seat Carriage (4).
Step 3: Use Phillips Head Screwdriver to release 4pcs of M6×10L Flat Phillips Head Screws (161), 4pcs of Ø7×Ø15×1.5T Flat
       Washers (162) and 4pcs of Sleeve (163). Then use 13m/m Wrench to release 4pcs of M8×7T Nyloc Nuts (88) and 4pcs of
       Ø8×Ø18×3T Knurled Lock Washers (79) and take Seat Wheel Adjustment Plate (9L.9R) apart as shown in figures 3, 4.




                       Figure 1                                                        Figure 2




                       Figure 3                                                        Figure 4


Step 4: Use M4 Allen wrench and 10m/m Wrench open end wrench to release M5×45m/m Socket Head Cap Bolt (171) and
       M5×5T Nyloc Nut (173) as shown in figure 5.
Step 5: Use Phillips Head Screwdriver to release two M5×25m/m Flat Head Socket Screws (169) then pull-out Lever Anchor (168)
       to take apart Seat Front/Aft Adjustment Lever (167) as shown in figure 6.
Step 6: Use M5 Allen wrench and 11m/m Wrench to release M6×38m/m Socket Head Cap Bolt (93), 1/4"×13×1T Flat Washer (72)
       and M6 Nyloc Nut (129) nut and take Seat Position Latch (12) apart as shown in figure 7.
Step 7: To install Seat Front/Aft Adjustment Lever (167), consolidate Seat Front/Aft Adjustment Lever (167) and Lever Anchor
       (168) and secure with two M5×25m/m Flat Head Socket Screws (169) then place Spring (104) in Seat Position Latch (12)
                                                                                                                          35 of 40

       and secure with a M5×45m/m Socket Head Cap Bolt (171) by going through Seat Position Latch (12), Spring (104), ø15×
       6×4T Nylon Washer(170), Seat Front/Aft Adjustment Lever(167) and ø3/16"×10×1T Flat Washer (172), from top to
       bottom and tighten with M5× 5T Nyloc Nut (173).
Step 8: Install the completed Seat Carriage (4) onto the Aluminum Track (14) and adjust the position of Seat Wheel Adjustment
       Plate (9L.9R) with 11 and 13m/m Wrenches by using 11m/m Wrench at front of left side and turn counterclockwise first,
       then using 13m/m Wrench to tighten M8 × 7T Nyloc Nut (88) (Figure 8). At the front of right side, use 11m/m Wrench by
       turning clockwise and use 13m/m Wrench to tighten M8×7TNyloc Nut (88). (Figure 9). Turning hex bolt at the rear of right
       side counterclockwise and clockwise at the rear of left side to secure.
Step 9: Testing if the smoothness is acceptable, turn four hex bolts reversely then tighten until smoothness is acceptable. Install
       four Sleeves (163) on hex bolts respectively and secure with four Ø7×Ø15×1.5T Flat Washers (162) and four M6×10L Flat
       Phillips Head Screws (161). (Figure 5) Install Seat Stop Axle (11) and Aluminum Axle End Cap (135) to complete.




                      Figure 5                                                      Figure 6




                      Figure 7                                                      Figure 8
                                                                                                                       36 of 40




                      Figure 9



9.12 Replacing the Aluminum Rail and Stabilizer Cover
Step 1: Remove both left and right Rear Shrouds (35, 36) and Seat Carriage (4) then use 12 mm open end wrench to remove six
       5/16" × 3/4"_Hex Head Bolts (94), six 5/16" × 16 × 1.5T_Flat Washers and six 5/16" × 1.5T_Split Washers (82) to take
       apart the Aluminum Track (14), as shown in figure 1.
Step 2: Remove both left and right Rear Shrouds (35, 36) and both left and right Front Shrouds (29, 30). Use Phillips head screw
       to remove four M5 × 12mm Phillips Head Screws (99) to take apart the Step Cover, as shown in figure 2.




                        Figure 1                                                        Figure 2
                                                                                                                         37 of 40


10. Troubleshooting
10.1 Troubleshooting for the Console Display problem and Error Message
Problem: The Screen doesn't light or has no power.
Solution:
1. Make sure the console (19) and computer cables (44) are connected properly.
2. If the connection of all cables is good, then check the power adaptor is providing the correct voltage to the Bike.




Problem: The console doesn’t show the Speed value.
Solution:
1. When the console displays without speed, dismantle Front Shroud (L)(29) to check Computer Cable (44) and Sensor W/Cable
  (46) to make sure of proper installation, as shown in figure.
2. If installation is OK, normally there is problem with Sensor W/Cable (46) or Magnet (56). Use another magnet to determine if
  there is a problem with Sensor W/Cable (46). Either Sensor W/Cable (46) or Magnet (56) requires replacement.
                                                                                                                         38 of 40

Problem: The Console doesn’t show the heart rate when using the handgrip pulse.
Solution:
1. When the console displays but is without heart rate. Check if Hand Pulse Sensor Assembly W/Cable (45) is properly connected
  to Console assembly (19) (Figure 1), or if Hand pulse W/Cable Assemblies (21.27) are properly connected with Hand Pulse
  Sensor Assembly W/Cables (26), as shown in figure 1.
2. If there is no problem with installation, dismantle Rear Shroud (L) (35) and check if Hand pulse W/Cable Assemblies (26) are
  properly installed with Hand Pulse Sensor Assembly W/Cable (45), as shown in figure 2.
3. If there is no problem with the installation, check all connection with instrument with probe and replace if necessary.




                           Figure 1                                                             Figure 2



10.2 Troubleshooting for the Drive Belt Slipping or Falling-off
Problem: The drive belt is slipping when pedaling.
Solution:
1. Take apart both left and right front shrouds. (29.30)
2. Use 13m/m Wrench to turn M8×7T Nyloc Nut (88) clockwise until sound wave frequency falls between 450N. However, since
  the machine is with drive belt, slippage is possible depending on the weight of the user or the way the user uses. Generally,
  slippage is rare, as shown in figure.
3. Since the driving belt itself is with malleability and is expendable, it is normal to get loose as time lasts.
                                                                                                                            39 of 40

Problem: The drive belt is falling off when pedaling.
Solution: Please follow the instructions outlined in Section 9.7 of the Parts Replacement Guide to properly install the Drive Belt.
After installation and adjustment, it is essential to conduct a functional test on the Drive Belt (54) by rotating the drive pulley
both forward and backward. In case the belt dislodges, perform adjustments on the Drive Belt (54) in the opposite direction of
the displacement, adjusting one notch at a time. Repeat the testing procedure.
Should the issue persist even after adjustments, it is recommended to inspect and potentially replace the Drive Pulley (20), Idler
Wheel Assembly (10), or Generator/Brake (55). If the problem remains unresolved, it could indicate deformation of the Main
Frame, suggesting a need for complete machine replacement. However, such instances are rare, given that each machine
undergoes thorough testing prior to shipment.
                                                                                                                              40 of 40

10.3 Troubleshooting for the Noise during pedaling
Problem: The Bike is making noise when pedaling.
Solution:
The causes of the noises are mostly loose screws. Sometimes it is because of parts being deformed or shifting causing rubbing or
unsmooth moving. Most causes are as follows:
1. The noise from Seat Carriage (4) is generally caused by loose Seat Wheel Adjustment Plate (9L.9R). It is a normal phenomenon
  for a long-term used machine which with a wobble. Follow the instructions outlined in Section 9.10 of the Parts Replacement
  Guide 10 to resolve, as shown in Figure 1.
2. Noise with Pedal (116). (117) is generally caused by the wear of Pedal (116). (117) and must be replaced, as shown in Figure 2.
3. Left and right crank (51L.R). Sometimes crank (51L.R) gets loose causing noises and not moving smoothly. Tightening the crank
  fixes the problem, as shown in figure 3.
4. Noises inside Front Shrouds Both left and right Front Shrouds needs to be removed to determine the location where making
  noises. In many cases, there is Drive Pulley (20) which rubbing right shroud that causes noise. The solution will be replacing
  the Drive Belt Pulley (20) or putting an extra 5/16"×16×1T Flat Washer at right Front Shroud (30), as shown in figure 4.
5. If there are still noises without left and right front shrouds (29.30), identify the location of the noise and replace parts if
  necessary.




                         Figure 1                                                             Figure 2




                         Figure 3                                                             Figure 4
