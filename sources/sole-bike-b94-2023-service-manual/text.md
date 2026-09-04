SERVICE MANUAL
                B94(2023)
            SU415A-SB025
            UPRIGHT BIKE




      -1-
                                                                    -Contents-
1.Outlines.....................................................................................................................................................- 3 -
2.Electronic Parts .......................................................................................................................................- 4 -
     2.1 Console ............................................................................................................................................- 4 -
     2.2 Controller and Driver parts .............................................................................................................- 4 -
3.Electrical Configurations .....................................................................................................................- 5 -
4.Product Operation.................................................................................................................................- 6 -
5.Unit Block Diagrams........................................................................................................................... - 11 -
6.Basic Connections and Wiring........................................................................................................ - 12 -
     6.1 Display Board wire Connections.................................................................................................. - 12 -
     6.2 Display Board PCB Component Locations.................................................................................. - 13 -
     6.3 Interface Board Wire Connections .............................................................................................. - 14 -
       6.4 Gear Motor connector definition function .................................................................................. - 14 -
7. Product Safety Instructions.............................................................................................................. - 15 -
     7.1 Important Safety Instructions ....................................................................................................... - 15 -
     7.2 Important Electrical Instructions .................................................................................................. - 15 -
     7.3 Important Grounding Instructions ............................................................................................... - 15 -
8. Error Messages / Troubleshooting ................................................................................................. - 16 -
     8.1 Error Message: E1......................................................................................................................... - 17 -
     8.2 Error Message: E2......................................................................................................................... - 18 -
     8.3 Circuit Diagram ............................................................................................................................ - 20 -
     8.4 Maintenance Menu ...................................................................................................................... - 21 -
     8.5 Troubleshooting procedure Matrix ............................................................................................. - 21 -
9. Parts Replacing Guide ..................................................................................................................... - 22 -
     9.1 Replacing the Console ................................................................................................................. - 22 -
     9.2 Replacing the Handlebar and Console Mast .............................................................................. - 22 -
     9.3 Replacing the Main Frame and Console Mast Cover ................................................................. - 23 -
     9.4 Replacing the Seat and Sliding Seat Mount ............................................................................... - 24 -
     9.5 Replacing the Inner Slide tube .................................................................................................... - 25 -
     9.6 Replacing the Crank Arm and Pedal ........................................................................................... - 25 -
     9.7 Replacing the Chain Cover L/R ................................................................................................... - 27 -
     9.8 Replacing the Flywheel, Drive Belt and Bearing Housing .......................................................... - 28 -
     9.9 Replacing the Drive Belt and Drive Pulley................................................................................... - 30 -
       9.10 Replacing the Gear Motor, Steel Cable, and Reed Sensor ...................................................... - 31 -
10. Troubleshooting ............................................................................................................................... - 33 -
     10.1 Troubleshooting for the Console Display problem and Error Message ................................. - 33 -
     10.2 Troubleshooting for the Drive Belt Slipping or Falling-off ...................................................... - 34 -
     10.3 Troubleshooting for the Noise during pedaling ....................................................................... - 36 -




                                                                               -2-
1.Outlines




             -3-
2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts




                                  -4-
3.Electrical Configurations
Console       Interface that controls all functions of the Bike.
Gear Motor    It can change to increase or decrease resistance level of brake.


GENERAL INFORMATION
Console       It is including keypad to control and LCD Display.
              Main controller Include power supply and motor driver control circuit.
Gear Motor    Work voltage: DC 4.5~7.5V
              Control resistance increases and decreases.




                                                       -5-
4.Product Operation




Window Display Mode
IDLE Mode    -In DM, each program profile is displayed in the form of a page change, during which the residence time
             of the profile is 5 seconds. One program profile is displayed sequentially at a time, and the name of the
             program is displayed on the message window at the same time.
             -The heartbeat rate bar will light up from bottom to top, and the track circle will light up sequentially
             from the bottom to the middle.
             -The data window (seven-segment display window) displays RPM = 60, calories = 681, time = 30:00,
             distance = 12.0, and pulse = 125.
SLEEP Mode   -Sleep mode can be set as on or off in Engineer mode.
             -When the console sleep mode is set to off, the electronic watch will not sleep unless the power is turned
             off. When set to on, if there is no RPM input in idle mode, it will enter sleep mode if there is no key press
             for 15 minutes.
             -When the console is in sleep mode, press any key to wake it up and return to idle mode immediately.
Child Lock   -The default child lock is off but can be set to on or off in engineer mode.
Mode         -When the child lock is on, turn on the power. The main window will display "Console locked" twice, then
                                                       -6-
             flash, and then display "Child lock-on. Press Start and Enter to enable operation." The user must press
             and hold both buttons at the same time to live start. After pressing the Enter key for 3 seconds, release
             the console lock and enter idle mode to continue using.
             -When the child lock is on, the keys cannot be used and cannot be used until the lock is unlocked.
EXERCISE     -In idle mode, press the Start key to directly enter manual mode. Age and weight are both preset values,
Mode         time will count from 00:00, all data will count from 0, and resistance will start from 1.
             -Press the Program key (Manual, Program, HRC) to select one of the programs. Then, press the Start key
             to start using the selected mode, and the internal parameters will be based on the preset values at that
             time.
PAUSE Mode   -Press the Stop key to enter pause mode during the exercise. The exercise parameters will be recorded,
             and the main window will display "Pause". The upper window will display the exercise data recorded at
             that time.
             -During pause mode, after "Pause" is displayed for 5 seconds, it will change to the display of mobile
             strings. The following message, "Press Start to resume or Stop to end," will be displayed once, and the
             cycle will repeat in turn.
             -If no key is pressed during pause mode for 5 minutes, it will automatically enter idle mode.
             -The resistance level returns to level 1. When you press the Start key again to resume, the position of the
             pull wire motor will return to the original number of stages before the pause.
END Mode     -When the program ends, the main window will display "End of Workout Summary" to display workout
             information in sequence.
             End mode workout information
             The MW will alternately display "AVG Level XX," "AVG SPD XX.X," and "AVG RPM XXX" every 3
             seconds. "Level" will display the average of all program data. The "Calories" window displays the total
             exercise calories, the "Time" window displays the total exercise time, and the "Distance" window
             displays the total exercise distance.
             -When the time countdown setting ends and end mode is displayed, if no key is pressed, it will
             automatically return to idle mode in 5 minutes.
RESET Mode   -In idle mode (except when the child lock is on, in which case the reset function must be released first),
             press the Stop key for 3 seconds to enter the reset function and restart the system.
             -The reset mode clears all screens and enters idle mode after restarting.


Function
RPM          Display the current speed in mile per hour.
             DISPLAY range is 0 to 888.
             WORK range is 0~120
LEVEL        DISPLAY range is 0 to 99.
             WORK range is 1 to 20.
             Press “UP” or ”DOWN” to adjust level, each increment and decrement is 1.
TIME         TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
             is COUNT DOWN.
             DISPLAY range is 0:00 to 99:99.
             WORK range is 0:00 to 99:59.
                                                       -7-
           COUNT DOWN setup range is 10:00 to 99:00.
           When TIME is set, the count will go to zero.
           In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will
           continue count time.
LAPS       Display the total working laps quantity.
           DISPLAY range is 0 to 99.
           WORK range is 0 to 99.
           Displays total laps quantity.
DISTANCE   Display the current distance in kilometer or Mile.
           DISPLAY range is 0.00 to 99.9.
           WORK range is 0.00 to 99.9.
CALORIES   Displays the cumulative calories burned at any given time during your workout.
           DISPLAY range is 0 to 999.
           WORK range is 0 to 999.
PULSE      Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be
           worn.
           DISPLAY range is 0 to 999.
           WORK range is 40 to 220 BPM.
           In EXERCISE Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value will become
           “0 ”.




                                                      -8-
Function Button Locations




Button Function in each mode

IDLE Mode
Stop Button       Non-function.
Start Button      Pressing “START” button to start bike, when pressing “START” button, there will be 3 second final
                  count down on window display, then machine starts running. In MANUAL, bike starts at MIN LEVEL.
Level Up Button   If user doesn’t enter a setting, then this button is non-functional.
Level down        If user doesn’t enter a setting, then this button is non-functional.
Button
Fan Button        It can control ON/OFF for the fan.
Enter Button      Non-function. If you have choice a program, press ENTER button to modify setting.
Program Button    To select anyone program to begin workout.
Display key       Non-function.




                                                        -9-
EXERCISE Mode
Stop Button       press “STOP” button to stop bike.
Start Button      Non-function.
Level Up Button   Press the button to increase your level and each increase is 1.
Level down        Press the button to decrease your level and each decrease is 1.
Button
Fan Button        It can control ON/OFF for the fan.
Enter Button      Non-function.
Program Button    To select anyone program to begin workout.
Display key       When in the exercise state, press the Enter key to switch the display of exercise data. If the message is
                  to display the last data, press the Enter key again to display the data scan, which becomes an
                  automatic cycle mode every 4 seconds.
                  In the cycle mode, it will first display "LAPS XX" and then display the following:
                  "SPEED XX.X MPH"
                  "SPEED XX.X RPM"
                  "L XX MAX LV XX" (only program mode will display max level)
                  "WATT XXX"
                  "SEG TIME XX:XX"




                                                        - 10 -
5.Unit Block Diagrams




                        - 11 -
6.Basic Connections and Wiring
6.1 Display Board wire Connections




                                     - 12 -
6.2 Display Board PCB Component Locations
PCB Board Top view




PCB Board Bottom view




                                       - 13 -
6.3 Interface Board Wire Connections




6.4 Gear Motor connector definition function




                                          - 14 -
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




                                                                  - 15 -
8. Error Messages / Troubleshooting
Error Code List

            Code      Description
                 E1   EEPROM failure
                 E2   Gear motor is failure


Tools Required

A multi-meter.




                                              - 16 -
8.1 Error Message: E1

Definition:
When the EEPROM is damaged or there is a problem with access, all windows will be turned off, all outputs will stop, and MW
will display "E1".


Troubleshooting:
The EEPROM is abnormal, please replace the Display Board directly。




                                                            - 17 -
8.2 Error Message: E2

Definition:
When you press the Level Up or Down key, the motor does not move.” E2” appears on the display.


Gear Motor Operation:
Part                      Description
                          Key signal travels to the display. The main program IC then sends a command
Display
                          signal to the drive board.
                          Drive board receives the signal and responds by putting out power to the
Drive Board
                          motor. Level UP: +5VDC; Level DOWN: -5VDC


Gear Motor Troubleshooting:
Part                      Description
Display                   If the key beeps when pressed, assume that the signal was sent.
Data cable                Inspect the cable and connections.
                          Inspect drive board power output to the motor. Press the Level Up is +5VDC;
                          Level DOWN is -5VDC.If there is power to the motor, but the motor does not
Drive Board
                          operate, replace it. If there is no power output, inspect whether the drive board
                          has power.


Gear Motor Voltage Test Procedure:
1. Put the multi-meter on the 20VDC setting and place the probes on the motor control wire (red probe in brown wire, black
probe in black wire) on the drive board.
2. Turn on the unit power. The display will light up.
3. Press LEVEL UP. The normal reading should be +5~6.0 VDC, and the motor should operate with resistance increasing.
4. Press LEVEL DOWN. The normal reading should be -5~6.0 VDC, and the motor should operate with resistance decreasing.
5. If there is no voltage, inspect the power socket and the holder FUSE. If it is broken, replace it.
6. Inspect the drive board POWER LED to see if it is lit. If it is not lit, the drive board is bad and needs to be replaced.




                                                             Place probes on the motor control wire

                                                             (Red probe in brown wire, Black probe in

                                                             black wire) on the drive board.




                                                                  - 18 -
Test configuration:
The console to driver board connector pin define function.




                                                   - 19 -
8.3 Circuit Diagram




                      - 20 -
8.4 Maintenance Menu
The console has built in maintenance/diagnostic software. The software will allow you to change the console settings from
English to Metric and turn off the beeping of the speaker when a key is pressed for example. To enter the Maintenance Menu
(may be called Engineering Mode, depending on version) press and hold down the Start, Stop and Enter keys keep holding the
keys down for about 5 seconds and the Message Window will display “Engineering Mode”.

Press the Enter button to access the menu below. Press the Level ▲/▼ keys to navigate the menu.
A. Key Test - Will allow you to test all the keys to make sure they are functioning.
B. Display Test - Automatically tests all LCD’s.
C. Functions - Press Enter to access settings, use Level ▲/▼ keys to scroll.
       I. ODO Reset - Resets the odometer.
       II. Units - Choose from English (Imperial) or Metric display readings.
       III. Sleep Mode - Turn off to have the console power down automatically after 30 minutes of inactivity.
       IV. Motor Test - Continually runs the tensioning gear motor.
       V. Manual - Allows stepping of the gear motor.
       VI. Pause Mode-Turn on to allow 5 minutes of pause, turn off to have console pause indefinitely.
       VII. Key Tone - Turn on or off the beep sound when a key is pressed.
D. Security - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the
child lock is enabled, the console will not allow the keypad to operate unless you press and hold the Start and Enter buttons for 3
seconds to unlock the console.
E. Factory Set
F. Exit - Select to exit Maintenance Menu


8.5 Troubleshooting procedure Matrix
Condition                       Reason                                            Solve
LCDs not bright, incomplete,    1. LCD light is broken.                           1. Replace with new LCD or console.
or imperfect.                   2. Power to console too low.                      2. Check AC power is 110-120V.
                                                                                  3. Check power to console.
                                                                                  4. Replace lower controller.
LCD displays not bright,        LCD displays are broken.                          Replace with new console.
incomplete, or imperfect.
Erratic pulse display.          1. Another chest belt in use around bike.      1. Check for other chest belt use around bike.
                                2. Other magnetic field disturbance.           2. Change the position or direction of bike.
                                3. Receiver is broken.                         3. Replace with new receiver.
Hand pulse lost its function.   1. Hands not on the hand pulse sensors or only 1. Two hands hold the hand pulse.
(No pulse displayed on             one hand on sensor.
monitor)                        2. The connector of HANDPULSE W/WIRE and 2. Connect the cable again.
                                   Console not connected properly.
                                3. The wires got damaged when connecting the 3. Replace with new cable.
                                   HANDPULSE W/WIRE and Console.
                                4. Hand pulse board is broken.                 4. Replace console or Hand pulse board.
Wireless lost its function.     1. Chest belt not worn properly.               1. Check chest belt has proper contact with skin
(No pulse displayed on                                                            and is oriented correctly.
monitor)                        2. Distance is too far and exceeds range of    2. User chest belt in front of console within 3
                                receiver.                                         feet.
                                                                               3. Replace with new lithium battery type is
                                3. Chest belt battery is weak or dead.            CR2032.
Chest belt too close to the     Weak battery.                                  Replace with new lithium battery with type
bike.                                                                             CR2032.




                                                               - 21 -
9. Parts Replacing Guide
9.1 Replacing the Console
Step 1: Use Phillips head screwdriver to release four M5×12mm Phillips Head Screws and Console and both hand pulse sensor
       cables to take console apart.




Step 2: Reverse above step to resume console.


9.2 Replacing the Handlebar and Console Mast
Step 1: Follow the section 9.1 to remove the console.
Step 2: Using a 5mm L-Allen wrench to remove 4 pcs of 5/16” x 5/8” Hex head bolts, 4 pcs of 5/16” x 18mm x 1.5T flat washers
       and 4 pcs of 5/16” x 1.5T Split washers which secured the handlebar assembly (L/R).




Step 3: Remove four Ø3 × 10m/m Tapping Screws to remove Handgrip Side Caps (Top)and (Bottom).




                                                            - 22 -
Step 4: Use Phillips head screwdriver to release four 20m/m Tapping Screws securing Hand pulse W/Cable Assembly and
       separate Hand pulse W/Cable Assembly from each other and remove,




Step 5: Reverse above step to resume.


9.3 Replacing the Main Frame and Console Mast Cover
Step 1: Follow section 9.2 to remove the console and both sides of the handlebar.
Step 2: Slightly press the Console Mast Cover to separate it from left and right Chain covers.




Step 3: Using 12 wrench to release 7pcs of 5/16" × 5/8"_Hex Head Bolt, 6pcs of 5/16" × 18mm ×1.5T_Flat Washer and 1pcs of
       5/16" × 19 ×1.5T_Curved Washer and the Handlebar can be released.




Step 4: To resume installing the Console Mast, guide the Computer Cable through the Console Mast and out of the console
       mounting plate. Then, insert the Console Mast onto the Mainframe. Use a 12 mm wrench to tighten 7 pieces of 5/16" ×
       5/8" Hex Head Bolts, 6 pieces of 5/16" × 18mm × 1.5T Flat Washers, and 1 piece of 5/16" × 19 × 1.5T Curved Washer.
                                                               - 23 -
       Finally, reattach the Console Mast and Chain Covers respectively.


9.4 Replacing the Seat and Sliding Seat Mount
Step 1: Use 14 mm wrench to loosen both hex head bolts to remove Seat.




Step 2: Use 14 mm wrench to remove the Cap Nut.




Step 3: Turn to take Brake Tension Knob apart from Fix Plate and remove Sliding Seat Mount.




Step 4: To resume, install Sliding Seat Mount on Seat Slider then put Fix Plate on it. Install Brake Tension Knob from bottom
       upward to Fix Plate and tighten with 3/8"x7T Nut. At last, insert Seat into the sliding tube and tighten both hex head bolts
       with 14 mm wrench.




                                                               - 24 -
9.5 Replacing the Inner Slide tube
Step 1: Remove the Locking Knob.




Step 2: pull seat slider and seat post cover up. Take Center spatial wrap apart from Main Frame with a rubber hammer (refer to
       photo 2), and then use Phillips Head Screwdriver to release 2 pcs of 4 × 12m/m Sheet Metal Screws, then remove Slide
       Spacer with rubber hammer to take Seat Slider and Center spatial wrap apart.




Step 3: To resume, return Center spatial wrap back to Seat Slider then return Slide Spacer in Seat Slider and tighten with two pcs
       of 4×12m/m Sheet Metal Screws and insert into the Main frame. Use rubber hammer to return Center spatial wrap and
       resume Locking Knob.


9.6 Replacing the Crank Arm and Pedal
Step 1: Use 13/15mm open end wrench to take apart pedals by turning left pedal clockwise and right pedal counterclockwise.




                                                              - 25 -
Step 2: To resume pedals, turn pedals with reversed directions respectively.
Step 3: Take Crank Arm End Cap apart and use plug wrench to release the nut.




Step 4: Apply crank tool on the crank to fix and use Allen wrench to release the crank.




Step 5: To resume the crank (16L,16R), use air crank tool or rubber hammer to fix the crank (16L,16R) on the axle and tighten the
       nut on the crank axle and plug in the Crank Arm End Cap.




                                                               - 26 -
9.7 Replacing the Chain Cover L/R
Step 1: Take apart pedals and crank arm. Separate the Console Mast Cover, and use Phillips head screwdriver to release nine
       Ø3.5 × 16m/m Sheet Metal Screw and three 5 ×16m/m Tapping Screw, which secure left shroud.




Step 2: Use 15mm open end wrench to take apart DC Power Cord and to take left shroud apart.




Step 3: Use Phillips head screwdriver to release 3 pcs of 5 ×16m/m Tapping Screw to remove Chain Cover R.
Step 4: To resume, install Right Side Case on the Main Frame by using Align the center of the Wheel with the center of the Axle
       and secure with 3pcs of 5x16mm Tapping Screws by using Phillips Head Screwdriver then install back DC Power Cord, to
       secure further. Match Left Side Case with Right Side Case and secure with 9pcs of 3.5x12mm Self Tapping Screws, 3pcs of
       5x16mm Tapping Screws. Follow step 2.1 to resume Cranks and Pedals.




                                                              - 27 -
9.8 Replacing the Flywheel, Drive Belt and Bearing Housing
Step 1: Follow section 9.7 to remove Chain Cover L/R.
Step 2: Use 11 mm open end wrench to release 1/4" × 8T_Nyloc Nut to the end and use 6 mm Allen wrench to remove to
       remove M10 x P1.25 × 15L_Button Head Socket Bolt and take Bearing Housing apart.




Step 3: Take down steel cable on Flywheel and take notice of handling with care on Aluminum sheet of steel cable (as remarked)
       when disassembling because it’s an Aluminum sheet with spring. If it doesn’t handle with care, it will become distorted
       and cause noise when rubbing. This is a very important point.




Step 4: Then, take down the belt from Drive Pulley, use 15 mm Wrench to loosen 2pcs x 3/8"-UNF26_Nut of Flywheel (refer to
       photo) Take apart the flywheel and the belt.




Step 5: To resume, secure the Bearing Housing on the Main frame with M10XP1.25X15L_Button Head Socket Bolt.
                                                             - 28 -
Make sure that Nut Stopper is securely on the Main Frame.




Step 6: To resume, return the Drive Belt onto Flywheel and back to Main Frame. Align the Flywheel and the Drive Pulley in line.
       Turn 3/8"-UNF26 × 4T_Nut by the Drive Pulley outward till it touches Main Frame and turn the other 3/8"-UNF26_Nut
       inward. At last, use 15 mm and 17 mm open end wrenches to tighten both 3/8"-UNF26 × 4T_Nut and 3/8"-UNF26_Nut.
       The same way for 3/8"-UNF26 × 3T_Nut and 3/8"-UNF26_Nut at the other side.




Step 7: Return Drive Belt back to the Drive Pulley and Flywheel. Turn Drive Pulley to locate the Drive Belt in center. If not, loosen
       3/8" UNF26_Nut of the Flywheel and adjust Nuts to secure. Use 11 mm open end wrench to tighten 1/4" × 8T_Nyloc Nut
       until Drive Belt is tight with Bearing Housing. Use sound wave tension gauge to make sure the reading is 450 N (Remark).
       At last, turn Drive Pulley to make sure Drive Belt is in center without falling apart. Return Steel Cable back to Flywheel.




                                                                - 29 -
9.9 Replacing the Drive Belt and Drive Pulley
Step 1: Follow section 9.7/9.8 to remove the Chain Cover L/R and Drive Belt.
Step 2: Use C Ring tweezers to remove Ø20 C Ring on Crank Arbor.




Step 3: Use two 11 mm open end wrenches to remove four 1/4" × 3/4"_Hex Head Bolts together with four 1/4" × 8T_Nyloc Nuts
       on Crank Arbor and Drive Pulley to take Drive Pulley apart.




Step 4: Reverse above step to resume.




                                                              - 30 -
9.10 Replacing the Gear Motor, Steel Cable, and Reed Sensor
Step 1: Follow section 9.7 to remove Chain Cover L.
Step 2: Remove Steel Cable from Flywheel. When releasing the steel cable, be sure to release the aluminum plate gently as it
       deforms easily to cause noise.




Step 3: Use Phillips head screwdriver to remove two M5 × 12m/m Phillips Head Screws on the Gear Motor to take apart the Gear
       Motor.




Step 4: Release the Steel Cable from the Gear Motor to take it apart.




                                                              - 31 -
Step 5: Use Phillips head screwdriver to remove M5 × 12m/m Phillips Head Screw and take Reed Switch apart.




Step 6: Use Console to adjust the moving range when installing Steel Cable. The way is after finishing installing Steel Cable,
       control with console to turn the tension to maximum then adjust the Steel Cable to that the exposed cable is tight. The
       aluminum plate is at lowest position for the maximum tension. Use two 8 mm open end wrench to tighten the adjusting
       screw when complete.




                                                               - 32 -
10. Troubleshooting
10.1 Troubleshooting for the Console Display problem and Error Message
Problem: The Screen doesn't light or has no power.
Solution:
1. Make sure the console and computer Cables are connected properly.
2. If the connection of all cables is good, then check the power adaptor is providing the correct voltage to the Bike.




Problem: The console doesn’t show the Speed value.
Solution:
1. When the console displays without speed, dismantle Chain covers to check Computer Cable and Sensor W/Cable to make sure
  of proper installation, as shown in figure.
2. If installation is OK, normally there is problem with Sensor W/Cable or Magnet. Use another magnet to determine if there is a
  problem with Sensor W/Cable (46). Either Sensor W/Cable or Magnet requires replacement.




                                                                - 33 -
Problem: The Console doesn’t show the heart rate when using the handgrip pulse.
Solution:
1. The console is displaying but there is no HR shown. Check if hand pulse sensor cable is properly connected to the console, as
  shown in figure 1 and if hand pulse assemblies’ cables are properly connected with sensor wires.
2. If they are all connected well, check Hand pulse Assembly. Replace the wire cable if necessary. Remark: The console and
  related parts were all inspected prior to shipping and the probably of defective is low.




10.2 Troubleshooting for the Drive Belt Slipping or Falling-off
Problem: The drive belt is slipping when pedaling.
Solution:
1. Take apart both left and right Chain Covers and Crank Arms.
2. Use 11 mm open end wrench to tighten 1/4"x8T Nyloc Nut until sound wave tension gauge reads 450N. Since this model is
  driven by Drive Belt, the user weight or the way of use may cause the belt to slip. Generally, the belt won’t slip under normal
  usage.
3. Since the driving belt itself is with malleability and is expendable, it is normal to get loose as time lasts.




                                                                  - 34 -
Problem: The drive belt is falling off when pedaling.
Solution: Follow the section 9.8 of Parts replacing Guide to install the driving belt and test by revolving forward and backward
after adjustment. If the belt falls off, adjust it one groove toward the direction the belt falling off and test again. If the belt still
falls off, the machine might be so heavily dropped that part dimension deviates. Try to replace the drive pulley, Bearing Housing
or flywheel. If the problem persists, the mainframe could be deformed and the whole unit should be replaced. The possibility of
such a circumstance is low as all units were tested prior to shipping.




                                                                   - 35 -
10.3 Troubleshooting for the Noise during pedaling
Problem: The drive belt is slipping when pedaling.
Solution:
The causes of noises are mostly loose screws. Sometimes it is because of parts being deformed or shifting causing rubbing or
unsmooth moving. Most causes are as follows:
1. Noises coming from left and right pedals. This is mostly pedal wear causing noises and not moving smoothly. The worn-out
pedal must be replaced, as shown in figure.




2. Left and right crank. Sometimes crank gets loose causing noises and not moving smoothly. Tightening the crank can fix the
problem, as shown in figure.




                                                             - 36 -
