SERVICE MANUAL
                  E25(2023)
             SE668S-SE038
            Elliptical Trainer




      -1-
                                                                    -Contents-
1.Outlines.....................................................................................................................................................- 3 -
    1.1 Plastic parts ......................................................................................................................................- 3 -
    1.2 Structures .........................................................................................................................................- 3 -
2.Electronic Parts .......................................................................................................................................- 4 -
     2.1 Console ............................................................................................................................................- 4 -
     2.2 Controller and Driver parts .............................................................................................................- 4 -
3.Electrical Configurations .....................................................................................................................- 5 -
4.Product Operation.................................................................................................................................- 6 -
5.Unit Block Diagrams........................................................................................................................... - 11 -
6.Basic Connections and Wiring........................................................................................................ - 12 -
     6.1 Display Board wire Connections.................................................................................................. - 12 -
       6.2 Display Board PCB Component Locations.................................................................................. - 12 -
       6.3 Interface Board Wire Connections .............................................................................................. - 13 -
       6.4 Driver Board Wire Connections ................................................................................................... - 14 -
       6.5 Driver Board function ................................................................................................................... - 15 -
       6.6 Gear Motor connector definition function .................................................................................. - 16 -
7. Product Safety Instructions.............................................................................................................. - 17 -
     7.1 Important Safety Instructions ....................................................................................................... - 17 -
     7.2 Important Electrical Instructions .................................................................................................. - 17 -
     7.3 Important Grounding Instructions ............................................................................................... - 17 -
8. Error Messages / Troubleshooting ................................................................................................. - 18 -
     8.1 Error Message: E1......................................................................................................................... - 19 -
       8.2 Error Message: E2......................................................................................................................... - 20 -
       8.3 Error Message: E3 ........................................................................................................................ - 22 -
       8.4 Circuit Diagram ............................................................................................................................ - 27 -
       8.5 Maintenance Menu ...................................................................................................................... - 28 -
       8.6 Calibration Procedure .................................................................................................................. - 28 -
       8.7 Troubleshooting procedure Matrix ............................................................................................. - 28 -
9. Parts Replacing Guide ..................................................................................................................... - 30 -
    9.1 Replacing the Console ................................................................................................................. - 30 -
    9.2 Replacing the Connecting Arm ................................................................................................... - 30 -
    9.3 Replacing the Pedal Arm ............................................................................................................. - 31 -
       9.4 Replacing the Side Case (R/L)...................................................................................................... - 31 -
       9.5 Replacing the Cross Bar ............................................................................................................... - 32 -
       9.6 Replacing the Poly-V Belt ............................................................................................................ - 32 -
       9.7 Replacing the Idler Wheel Assembly ........................................................................................... - 33 -
       9.8 Replacing the Flywheel ................................................................................................................ - 33 -
       9.9 Replacing the Bushing Housing .................................................................................................. - 34 -
       9.10 Replacing the Slide Wheel ......................................................................................................... - 34 -
       9.11 Replacing the Incline Motor....................................................................................................... - 35 -
                                                                               -2-
1.Outlines
1.1 Plastic parts




1.2 Structures




                    -3-
2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts




                                  -4-
3.Electrical Configurations
Console         Interface that controls all functions of the Elliptical.
Controller      The circuit board consist of the DC power supply for console、incline driver and tension motor driver,
                link the console to output appropriate voltages for tension motor that control the elliptical functions.
Gear Motor      It can change to increase or decrease resistance level of brake.
Incline Motor   This is an AC motor. User can control variable elevation by console within the Controller.


GENERAL INFORMATION
Console         It is including keypad to control and LCD Display.
                Main controller Include power supply and motor driver control circuit.
Gear Motor      Work voltage: DC 4.5~7.5V
                Control resistance increases and decreases.
Incline Motor   This is a 115-volt AC motor.
                Have four wires, red, black, white, and green.
                Has one 3 pins cable of position sensor.
                If there is AC voltage on the red wire (UP) the incline motor will increase the incline.
                If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
                The White wire (COM) is neutral.
                The green wire is ground.




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

                                                       -6-
Child Lock   -The default child lock is off but can be set to on or off in engineer mode.
Mode         -When the child lock is on, turn on the power. The main window will display "Console locked" twice, then
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
             Press LEVEL “UP” or ”DOWN” to adjust level, each increment and decrement is 1.
INCLINE      DISPLAY range is 0 to 99.
             WORK range is 1 to 15.
                                                       -7-
           Press Incline “UP” or ”DOWN” to adjust level, each increment and decrement is 1.
TIME       TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
           is COUNT DOWN.
           DISPLAY range is 0:00 to 99:99.
           WORK range is 0:00 to 99:59.
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
Stop Button         Non-function.
Start Button        Pressing “START” button to start Elliptical, when pressing “START” button, there will be 3 second final
                    count down on window display, then machine starts running. In MANUAL, Elliptical starts at MIN
                    LEVEL.
Level Up Button     If user doesn’t enter a setting, then this button is non-functional.
Level down          If user doesn’t enter a setting, then this button is non-functional.
Button
Incline Up Button   If user doesn’t enter a setting, then this button is non-functional.
Incline Down        If user doesn’t enter a setting, then this button is non-functional.
Button
Fan Button          It can control ON/OFF for the fan.
Enter Button        Non-function. If you have choice a program, press ENTER button to modify setting.
Program Button      To select anyone program to begin workout.
Display key         Non-function.




                                                          -9-
EXERCISE Mode
Stop Button         press “STOP” button to stop Elliptical.
Start Button        Non-function.
Level Up Button     Press the button to increase your level and each increase is 1.
Level down          Press the button to decrease your level and each decrease is 1.
Button
Incline Up Button   Press the button to increase your incline and each increase is 1.
Incline Down        Press the button to decrease your incline and each decrease is 1.
Button
Fan Button          It can control ON/OFF for the fan.
Enter Button        Non-function.
Program Button      To select anyone program to begin workout.
Display key         When in the exercise state, press the Enter key to switch the display of exercise data. If the message is
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




6.2 Display Board PCB Component Locations
PCB Board Top view




                                       - 12 -
PCB Board Bottom view




6.3 Interface Board Wire Connections




                                       - 13 -
6.4 Driver Board Wire Connections




                                    - 14 -
6.5 Driver Board function




                            - 15 -
6.6 Gear Motor connector definition function




                                          - 16 -
7. Product Safety Instructions
7.1 Important Safety Instructions
- To reduce the risk of electric shock, disconnect your Elliptical from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the Elliptical on a flat level surface with access to a
120-volt, 15-amp grounded outlet with only the Elliptical plugged into the circuit.
- Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the
grounded plug by using improper adapters or in any way modify the cord outlet.

7.2 Important Electrical Instructions
- Never use a ground fault circuit interrupt (GFCI) wall outlet with this Elliptical. As with any appliance with a large motor, the
GFCI will trip often. Route the power cord away from any moving part of the Elliptical including the elevation mechanism and
transport wheels.
- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when an
Elliptical is first turned on or even during use. If your Elliptical is tripping the house circuit breaker (even though it is the proper
current rating) but the circuit breaker on the Elliptical itself does not trip, you will need to replace the home breaker with a high
inrush type. This is not a warranty defect. This is a condition we as a manufacture have no ability to control. This part is available
through most electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part #
QO120HM.


7.3 Important Grounding Instructions
- This product must be grounded. If the Elliptical should malfunction or breakdown, grounding provides a path of least
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




                                                                   - 17 -
8. Error Messages / Troubleshooting
Error Code List

            Code      Description
                 E1   EEPROM failure
                 E2   Gear motor is failure
                 E3   The console is not detecting the incline motor VR voltage, or the voltage has exceeded
                      the range.


Tools Required

A multi-meter.




                                              - 18 -
8.1 Error Message: E1

Definition:
When the EEPROM is damaged or there is a problem with access, all windows will be turned off, all outputs will stop, and MW
will display "E1".


Troubleshooting:
The EEPROM is abnormal, please replace the Display Board directly.




                                                            - 19 -
8.2 Error Message: E2
Definition:
When you press the Level Up or Down key, the motor does not move.” E2” appears on the display.


Configuration:




Gear Motor Operation:
Part                   Description
                       Key signal travels to the display. The main program IC then sends a command
Display
                       signal to the drive board.
                       Drive board receives the signal and responds by putting out power to the
Drive Board
                       motor. Level UP: +5VDC; Level DOWN: -5VDC


Gear Motor Troubleshooting:
Part                   Description
Display                If the key beeps when pressed, assume that the signal was sent.
Data cable             Inspect the cable and connections.
Drive Board            Inspect drive board power output to the motor. Press the Level Up is +5VDC;

                                                            - 20 -
                          Level DOWN is -5VDC.If there is power to the motor, but the motor does not
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




                                                            Place probes on the motor control wire (Red

                                                            probe in brown wire, Black probe in black

                                                            wire) on the drive board.




                                                                  - 21 -
8.3 Error Message: E3
Definition:
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” RAMP ERROR” appears on
the display.


Configuration:




                                                            - 22 -
Case of RAMP ERROR:
Incline VR value exceeds the range. E3 appears on the display.
Incline motor isn’t operation up or down, making the VR value exceed the range.
After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so E3
appears. Action Flow Chart:




                                                    - 23 -
Troubleshooting:
Part               Troubleshooting
                   -Reconnect VR wires.
Incline VR
                   -Inspect whether the incline wires are broken or disconnected.
                   -Inspect the incline wire and 14-pin cable connections.
Display board
                   -Test whether the VR voltage varies at the incline wire terminal.
                   -Inspect the wire connections.
14-pin cable       -Inspect whether wires are broken or crimped.
                   -Replace the wires and test again.
Driver board       Inspect the display board 14-pin connections.




                                                         - 24 -
Test configuration: the console to driver board connector pin defines function.




                                                  - 25 -
Test configuration: Incline motor control function relate parts location.




                                                   - 26 -
8.4 Circuit Diagram




                      - 27 -
8.5 Maintenance Menu
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

8.6 Calibration Procedure
Incline Calibration
If there is a problem with the incline, try running the calibration. Press the Incline ▲ key and the Start key at the same time.
Hold them down for 5 seconds and the Incline calibration will start and run automatically. If the problem persists, contact service
department.


8.7 Troubleshooting procedure Matrix
Condition                       Reason                                               Solve
LCDs not bright, incomplete,    1. LCD light is broken.                              1. Replace with new LCD or console.
or imperfect.                   2. Power to console too low.                         2. Check AC power is 110-120V.
                                                                                     3. Check power to console.
                                                                                     4. Replace lower controller.
LCD displays not bright,        LCD displays are broken.                             Replace with new console.
incomplete, or imperfect.
INCLINE ERR, INCLINE            Position sensor value of incline motor is wrong.
                                                                              1 Turn off the AC switch and turn on power
window shows “E3” error                                                          again.
code.                                                                         2. Follow 8.6 Calibration procedure to
                                                                                 calibrate the incline motor.
Erratic pulse display.        1. Another chest belt in use around Elliptical. 1. Check for other chest belt use around
                              2. Other magnetic field disturbance.               Elliptical.
                              3. Receiver is broken.                          2. Change the position or direction of
                                                                                 Elliptical.
                                                                              3. Replace with new receiver.
Both the incline adjustment -The connector of INCLINE CABLE and CONSOLE not Connect the wires again.
switches, up and down, do     connected properly.
not function                  -The connector of INCLINE CABLE and INCLINE
                              ADJUSTMENT SWITCH W/CABLE not connected
                              properly.
One of the incline adjustment -The connector of INCLINE CABLE or INCLINE      -Replace buttons
switches, either up or down, ADJUSTMENT SWITCH CABLE got damage.              -Replace the cable.
does not function.            -Button of INCLINE ADJUSTMENT SWITCH is broken.
                              -The connector of INCLINE CABLE or INCLINE
                              ADJUSTMENT SWITCH CABLE got damage.
                              -The connector of INCLINE CABLE or INCLINE
                              ADJUSTMENT SWITCH CABLE damaged.

                                                               - 28 -
Condition                       Reason                                                Solve
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
Elliptical.                                                                              CR2032.




                                                               - 29 -
9. Parts Replacing Guide
9.1 Replacing the Console
STEP 1: Use Phillips head screwdriver to remove Phillips Head Screws M5x10mm (4pcs) securing the console. Unfasten all
connected wires and remove console. (As shown in Figure 1 and 2)
STEP 2: Reassemble in the reverse order as disassembly (Be sure to not crush or damage wiring during process)
STEP 3: To remove both upper and lower console cover, remove the Sheet Metal Screws 3.5x12 that is securing the console.
(Should only be done by a professional)
STEP 4: Use Phillips head screwdriver to remove Phillips Head Screws M5x10mm (2pcs) then move out the Drink Bottle Holder.
(As shown in Figure 3)




9.2 Replacing the Connecting Arm
STEP 1: Use the Phillips Head Screwdriver to remove swing arm joint cover B (left and right) (As shown in Figure 1)
STEP 2: Use 12 and #13 open end wrenches to release Hex Head Bolt 5/16" x1-1/4", flat washer 5/16" x 20 x 1.5T and nut 5/16" x
7T which secure the Rod End Bearing. (As shown in Figure 2)
STEP 3: Use a 12mm open-end wrench to remove the hex socket screw 5/16”x15mm and flat washer 5/16”x20. Pull out the
pedal axle fix plates to remove the Pedal Bar Assembly. (As shown in Figure 3)
STEP 4: Use Phillips screwdriver to remove Phillips Head Screw M5x10mm securing the pedal and remove pedal. (As shown in
Figure 4)




                                                              - 30 -
9.3 Replacing the Pedal Arm
STEP 1: First remove the Pedal Bar Assembly, then use Phillips head screwdriver to unscrew Pedal Arm Cover. (Figure 1)
STEP 2: Use M8 hex wrench and #14 wrench to remove Gap socket screw 3/8”x2-1/4”, two flat washer 3/8”x19x1.5T and nylon
nut 3/8”x11T connecting the Inclinable Rail Assembly and rotating block, to remove Inclinable Rail Assembly. (Figure2 and 3)
STEP 3: Use #12 hex wrench to remove hex head bolt 5/16”x15mm and flat washer 5/16”x35x1.5T, to remove Bushing Housing,
Pedal Arm. (As shown in Figure 4)
STEP 4: Reassemble in the reverse order as disassembly.




9.4 Replacing the Side Case (R/L)
STEP 1: Remove the Connecting Arm and Pedal Arm (Refer to step 9.2 and 9.3)
STEP 2: Follow the assembly instructions by owner’s manual of reverse steps, Use the Phillips Head Screwdriver to remove the
console mast cover. (As shown in Figure 1)
STEP 3: Use Phillips head screwdriver to release 9pcs of 3.5x16 self-tapping screws and 3pcs of 5x16 x 3 tapping screws to take
Right Side Case apart. (As shown in Figure 2 and 3)
STEP 4: To take the Left Side Case apart, release 3.5x16 self-tapping screws with 1/4"x19 flat washers on the main frame and
3pcs of 5x16 Tapping Screws. Then disconnect two red jumpers and white grounding (remember to mark for red jumpers) to
release left Side Case. (As shown in Figure 4 and 5 and 6)
STEP 5: Install back this part, connect the red jumpers and the grounding back on the AC Electronic Module.
STEP 6: Return Left Side Case (with one 5/16" x 23 x 1.5T flat washer on it) onto the main frame and use3.5x16self tapping screw
with 1/4"x19 flat washer to hold it (not too tight temporarily) then tighten with 3pcs of 5x16 tapping screws (make sure Side
Case matches with Round Disk). Tighten 4x15 self-tapping screws. (As shown in Figure 7)
STEP 7: Match both Side Cases with each other and use 9pcs of 3.5x16 self-tapping screws and 3pcs of 5x16 tapping screws to
secure them.
STEP 8: Reverse above procedures to resume Pedal Arm and Connecting Arm.




                                                              - 31 -
9.5 Replacing the Cross Bar
STEP 1: Follow procedures 9.2, 9.3 and 9.4 to take apart Connecting Arm, Pedal Arm and both Side Cases.
STEP 2: Take off the Round Disk Cover by using a tapering stick. (As shown in Figure 1)
STEP 3: Remove elliptical side cover Round Disk Cover, use 12mm wrench to remove hex head bolt 5/16”x15mm, flat washer
5/16”x35x1.5T securing the cross bar. Use 13 wrench and loosen the outer bolt M8x6.3T (steel level 10). Use #13 wrench and hex
wrench (M6) to loosen the inner bolt and remove the cross bar. (As shown in Figure 2 and 3)
STEP 4: Use Phillips head screwdriver to release 8pcs of 5x16 tapping screws with 1/4"x19flat washers to separate the Cross Bar
from Round Disk Cover. (As shown in Figure 4)
STEP 5: To resume, secure the Round Disk on the Cross Bar and return it on the Crank Axle, align the Cross Bar with square hole
and put 7x7x25L Woodruff Key in the hole and tighten M8x40 socket head cap screw together with two M8x6.3T nuts until it
reaches 500 Kg-cm. Return and tighten 5/16" x 15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer. (As shown in Figure 5
and 6)
STEP 6: Follow above procedures to resume Connecting Arm, Pedal Arm, and both left and right-Side Cases with Round Disk
Cover.




9.6 Replacing the Poly-V Belt
STEP 1: Follow procedures 9.2,9.3, 9.4 and 9.5 to take apart Connecting Arm, Pedal Arm, both Chain Covers and the Cross Bar.
STEP 2: Use 13 mm wrench to loosen M8 x 9T nut on M8x170mm J-bolt and on Idler Wheel, and another M8 x 7T nut and the
Belt can thus be released. (As shown in Figure 1,2 and3)
STEP 3: To resume, return the Belt on the Drive Pulley and Flywheel then tighten M8 x 9T nut until the acoustic gauge reads 190
Hz (+/- 10 Hz) when it is played with finger, then tighten M8 x 7T nut. (As shown in Figure 4)
STEP 4: Reassemble in the reverse order as disassembly.




                                                               - 32 -
9.7 Replacing the Idler Wheel Assembly
STEP 1: Follow procedures 9.2, 9.3, 9.4, 9.5 and 9.6 to take apart Connecting Arm, Pedal Arm, both left and right-Side Cases,
Cross Bar, and the Belt.
STEP 2: Use 13 mm wrench to loosen M8 x 9T nut on M8x170mm J-bolt together with 5/16" x 23 x 1.5T flat washer until J-bolt is
released. Use the same wrench to release M8 x 20 carriage bolt, which secures Idler Wheel Assembly, together with 5/16" x 20 x
1.5T flat washer and M8 x 7T nut to take Idler Wheel Assembly apart. (As shown in Figure 1 and 2)
STEP 3: To resume, tighten M8x20 carriage bolt, 5/16" x 20 x 1.5T flat washer and M8 x7T nut to secure Idler Wheel Assembly (to
be tighten after the belt has been adjusted) and return the J-bolt and other parts.




9.8 Replacing the Flywheel
STEP 1: Follow procedures 9.2, 9.3, 9.4, 9.5, 9.6 and 9.7 to take apart Connecting Arm, Pedal Arm, both Side Covers, Cross Bar,
the Belt, and Idler Wheel Assembly.
STEP 2: Plug in the power and adjust the resistance to level 20 and release the steel cable. (As shown in Figure1)
STEP 3: Use 15 wrench to loosen nylon nut 3/8”-UNF26x9T on flywheel and main-frame. Remove flywheel and belt. (As shown in
Figure 2)
STEP 4: To resume the Flywheel, return the Belt onto grooves on the Flywheel and return the Flywheel onto the mainframe.
STEP 5: Tighten both 3/8" -UNF26 x 11T nuts Return the steel cable onto the Flywheel (with 45 degree) and then return the Idler
Wheel Assembly. (As shown in Figure 4)
STEP 6: Turn the Drive Pulley and check if the belt is secured. Adjust both 3/8"-UNF26 x 4T nuts to position the belt in the middle
on the Drive Pulley and then tighten all other screws. Adjust the Belt to a proper tension. (As shown in Figure 5)
STEP 7: Follow procedures 9.7,9.6,9.5,9.4,9.3 and 9.2 to return other parts.




                                                               - 33 -
9.9 Replacing the Bushing Housing
STEP 1: Follow procedures 9.2 and 9.3 to take apart Connecting Arm, Pedal Arm, left and right-Side Cases, Cross Bar and the Belt.
STEP 2: Use 12 mm wrench to release 5/16" x 15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer and the Bushing Housing
can be release. (As shown in Figure1)
STEP 3: To resume, be sure that Ø 25 wave washer is returned onto the shaft then return the Bushing Housing onto the shaft and
tighten with 5/16" x15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer. (As shown in Figure 2)
STEP 4: Follow procedures 11-2, 11-5 and 11-3, 11-4 to return Pedal Arm and Connecting Arm.




9.10 Replacing the Slide Wheel
STEP 1: To take the slide wheel apart, use Phillips head screwdriver to release two Phillips head screws M5x15mm and take the
slide wheel cover first. (As shown in Figure1)
STEP 2: Use 12mm open wrench to remove Hex head bolts and remove sliding wheels. (As shown in Figure2 and 3)
STEP 3: Reverse above steps to resume the pedal arm and return wavy washes Ø 17 back to left and right slide wheels.




                                                              - 34 -
9.11 Replacing the Incline Motor
STEP 1: Follow procedures 9.2 and 9.3 to take apart Connecting Arm, Pedal Arm.
STEP 2: Use Phillips head screwdriver to remove Phillips Head Screws M5x15mm from Incline Cover, then remove parts. (As
shown in Figure 1, 2 and 3)
STEP 3: Use two 14mm wrenches to remove hex head bolt 3/8”x2-1/2” together with flat washer 3/8"x19x1.5T, nylon nut
3/8"x7T and two Nylon Washers Ø3/8'' x Ø35 x5T which secure Incline tube and Incline Motor. (As shown in Figure 4)
STEP 4: Use two 17mm Open End Wrench to remove hex head bolt 3/8 x2-1/2, flat washer 3/8 x 19 x1.5T and nylon nut M10 x
8T from outer Rail Tube and Incline adjustable assembly. Remove inclined adjustable assembly. (As shown in Figure 5)
STEP 5: Use Phillips head screwdriver to remove tapping screw 5x16 from incline motor grounding wire. Cut the wire tie then
take off the incline motor. (As shown in Figure 6)
STEP 6: Use 12mm wrench to remove from Rail Assembly hex head bolt 5/16"x1, flat washer 5/16"x 35x2T and pull-out locking
tube assembly and remove rail assembly. (As shown in Figure 7)
STEP 7: If removal of aluminum rail is needed, remove Phillips head screws M5x15mm from aluminum rail to proceed. (As shown
in Figure 8)
STEP 8: Zeroing the incline motor before taking it apart from the machine or assemble it onto the frame. The zeroing distance is
207mm. (+/- 1mm) (As shown in Figure 9 and 10)
STEP 9: Reassemble in the reverse order as disassembly.




                                                              - 35 -
