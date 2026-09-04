SERVICE MANUAL
               F85(2023)
            ST278-YT071
            ENT Treadmill




      -1-
                                                                    -Contents-
1.Outlines.....................................................................................................................................................- 5 -
2.Electronic Parts .......................................................................................................................................- 6 -
     2.1 Console ............................................................................................................................................- 6 -
     2.2 Controller and Driver parts .............................................................................................................- 6 -
3.Electrical Configurations .....................................................................................................................- 7 -
4.Product Operation.................................................................................................................................- 8 -
     4.1 Window Display Modes ..................................................................................................................- 8 -
     4.2 Display Function ..............................................................................................................................- 8 -
     4.3 Function Button Locations ........................................................................................................... - 10 -
     4.4 Button Function in each mode .................................................................................................... - 10 -
     4.5 Functional Overview of the SETTINGS ........................................................................................ - 12 -
5.Unit Block Diagrams........................................................................................................................... - 24 -
6.Basic Connections and Wiring........................................................................................................ - 25 -
    6.1 Display Board wire Connections.................................................................................................. - 25 -
    6.2 Display Board PCB Component Locations.................................................................................. - 25 -
    6.3 Patching Board Wire Connections .............................................................................................. - 27 -
    6.4 Driver Board Wire Connections ................................................................................................... - 28 -
    6.5 Driver Board PCB Component Locations ................................................................................... - 29 -
    6.6 Driver Board function ................................................................................................................... - 29 -
    6.7 Driver Board LED Indicator Locations ......................................................................................... - 30 -
    6.8 Controller Indicator LED debugging ........................................................................................... - 30 -
7. Product Safety Instructions.............................................................................................................. - 31 -
     7.1 Important Safety Instructions ....................................................................................................... - 31 -
     7.2 Important Electrical Instructions .................................................................................................. - 31 -
     7.3 Important Grounding Instructions ............................................................................................... - 31 -
8. Error Messages / Troubleshooting ................................................................................................. - 32 -
     8.1 Error Message: PLEASE REPLACE THE SAFETY KEY ................................................................... - 33 -
     8.2 Error Message: E1......................................................................................................................... - 35 -
     8.3 Error Message: E2/OVER CURRENT ............................................................................................ - 39 -
     8.4 Error Message: E3......................................................................................................................... - 40 -
     8.5 Error Message: E4......................................................................................................................... - 44 -
     8.6 Error Message: E5......................................................................................................................... - 45 -
       8.7 Error Message: E6 ........................................................................................................................ - 46 -
       8.8 Error Message: E7 ........................................................................................................................ - 47 -
       8.9 Circuit Diagram ............................................................................................................................ - 48 -
       8.10 Engineering Mode ...................................................................................................................... - 49 -
       8.11 Troubleshooting procedure Matrix ........................................................................................... - 54 -
9. Parts Replacing Guide ..................................................................................................................... - 57 -
     9.1 Replacing the Controller .............................................................................................................. - 57 -
       9.2 Replacing the Console ................................................................................................................. - 57 -
                                                                               -2-
9.3 Replacing the Drive Motor........................................................................................................... - 58 -
9.4 Replacing the Breaker .................................................................................................................. - 59 -
9.5 Replacing the AC Power Switch .................................................................................................. - 59 -
9.6 Replacing the Front and Rear Roller ........................................................................................... - 60 -
9.7 Replacing the Running Deck, Running belt, and Cushion ......................................................... - 61 -
9.8 Replacing the Speed Sensor ........................................................................................................ - 62 -
9.9 Replacing the Front Incline Motor ............................................................................................... - 62 -
9.10 Replacing the Rear Incline Motor .............................................................................................. - 64 -




                                                                   -3-
Special Note on ST278 CE version
Besides normal version, ST278 treadmill is with a CE version. Both versions are with exactly the same
in functions and outlines except that the power input is 110VAC for normal version versus 230VAC for
CE version and an additional Filter Choke circuit is added for CE version as shown in the below circuit
diagram.




                                                  -4-
1.Outlines




             -5-
2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts




                                  -6-
3.Electrical Configurations
Safety Key        To fit on the console that activates all function, if no safety key, the console cannot be controlled. The
                  display will show “Please Replace the Safety Key".
Console           Interface that controls all functions of the treadmill.
Main Controller   The circuit board consists of the DC power supply for console、incline driver and DC motor driver, link
                  the console to output appropriate voltages for motor that control the treadmill functions.
Drive Motor       This is a variable speed for DC motor. To control the 0 to 180 DC volts（To control 0-90 DC voltages on
                  120Vac electronic power system）on the main controller, it can to increase or decrease speed of
                  running belt.
Incline Motor     This is an AC motor. User can control variable elevation by console within main controller.


GENERAL INFORMATION
Console           The console comprised of key controls and TFT 15.6” TFT TOUCH PANNEL display.
                  Main controller Include power supply 、motor driver control circuit and incline control circuit.
Drive Motor       It’s a variable speed on 0-180 voltage DC motor on 230V. (0-90 volts DC motor on 120Vac electronic
                  power system)
                  Have three wires red, black, and green.
                  If there is DC voltage on the Red (white) wire (M+) the treadmill motor will turn clockwise.
                  If there is DC voltage on the Black wire (M-) the treadmill motor will turn counterclockwise.
                  The higher the voltage the faster the motor turns
                  The green wire is ground.
Incline Motor     This is a 230 voltage AC motor. (115 volts AC motor on 120Vac electronic power system)
                  Have four wires, red, black, white, and green.
                  Has one 3 pins cable of position sensor.
                  If there is AC voltage on the red wire (UP) the incline motor will increase the incline.
                  If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
                  The White wire (COM) is neutral.
                  The green wire is ground.




                                                           -7-
4.Product Operation




4.1 Window Display Modes
OFF Mode       When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode, and all
               windows will appear blank.
READY Mode     When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program
               profile name and cycle. Press START button or TOPCH PANNEL "START WORKOUT" to start treadmill on
               Manual Mode.
SLEEP Mode     In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
RUN Mode       In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop
               instantly and enter OFF Mode.


4.2 Display Function
SPEED          Display the current speed in Kilometer mile per hour.
               DISPLAY range is 1.0 to 22.0 km MAX or for MILE is "0.5 to12.0 MAX.
               WORK range is 1.0~22.0 km/h (0.5 ~ 12.0 mph)
               Press “FAST” or” SLOW” to adjust speed, each increment and decrement is 0.1 km/h(mph).
INCLINE        Display the incline position from 0 to 15.
               DISPLAY range is 0.
               WORK range is 0 to 15.
               INCLINE preset value is 0 to 15.
               Press “UP” or” DOWN” to adjust incline, each increment and decrement is 1.
TIME           TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
               is COUNT DOWN.
               DISPLAY range is 0:00:00 to 9:99:99.
               WORK range is 00:00 to 9:99:59.
               COUNT DOWN setup range is 10:00 to 99:00.
                                                        -8-
           When TIME is set, the count will go to zero.
           In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will
           continue count time.
DISTANCE   Display the current distance in kilometer or Mile.
           DISPLAY range is 0.00 to 99.9.
           WORK range is 0.00 to 99.9.
CALORIES   Displays the cumulative calories burned at any given time during your workout.
           DISPLAY range is 0 to 999.
           WORK range is 0 to 999.
PULSE      Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be
           worn.
           DISPLAY range is 0 to 999.
           WORK range is 50 to 200 BPM.
           In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value will become “0 ”.




                                                    -9-
4.3 Function Button Locations




4.4 Button Function in each mode

Ready Mode
Safety Key            Insert safety key in right position to power on the console.
                      When safety key is pulled away from its position, the console will be automatically shut down.
Stop Key              Non-function.
Start Key             Pressing “START” button to start treadmill, when pressing “START” button, there will be 3 second final
                      count down on window display, then machine starts running. In MANUAL, treadmill starts at MIN
                      SPEED and treadmill starts at program preset value in PROGRAM.
Touch panel
                      Press “                 ” button to change each function. MANUAL can set using time, Pre-set

                      PROGRAM and Fitness tests can set using time and speed, Heart Rate Control 1~2 can set time, age and
                      the value of heart rate. User Program 1~2 can set time, speed, and incline.
Speed quick Keys      7 preset buttons for rapid speed:    2/3/4/5/7/9/12 MI (3/6/9/12/15/18/22KM)
Incline quick Keys 7preset buttons for rapid incline: -4/-2/2/4/6/9/12
Fan key               It can control ON/OFF for the fan.
Display key           Non-function.




                                                           - 10 -
Run Mode
Safety Key             When safety key is pulled away from its position, the computer will be automatically shut down.
Stop Key               press “STOP” key to stop treadmill.
Start Key              non-functional.
Speed quick Keys       Speed will set to 2/3/4/5/7/9/12MI (3/6/9/12/15/18/22KM) speed quickly.
Incline quick Keys Incline will set to -4/-2/2/4/6/9/12 position quickly.
Fan key                It can control ON/OFF for the fan (Optional)
Display key            It can change the three-training diagrammatic, from Stats to Charts then to this Track.




                                                             - 11 -
4.5 Functional Overview of the SETTINGS

Press the gear icon    above the screen when in IDLE MODE, there are 8 sub-menu modes on the settings page, namely: 1)Unit
System, 2)Child Lock, 3)Sleep Mode, 4)Screen Brightness, 5)Date & Time, 6)Wi-Fi, 7)Language, 8)Software, 9)Media Apps, and
10)Passcode.




                                                           - 12 -
1)Unit System

Pressing this button                       toggles between Metric/Imperial units. The default setting is Imperial.
There are four sub-items below, namely: Distance, Speed, Height, and Weight.
The function of each item is described in the following table:
Distance: Units in mi/km.
Speed: Units in mph/km/h.
Height: Units in ft, in/cm.
Weight: Units in lb/kg.




                                                               - 13 -
2)Child Lock
Child Lock is OFF by default, which means it is not set. The setting range is ON/OFF. If you want to set it to ON, you need to reset
the device or press the safety key to activate the setting. The DM window in the IDLE MODE will display "Console Locked". To
unlock the console, the user needs to press and hold both the START & STOP buttons for 3 seconds and then enter the IDLE
MODE.
When it is set to ON/OFF, the corresponding explanation will be displayed.




                                                               - 14 -
3)Sleep Mode
The difference in actions between the Sleep Mode switch and SAFETY KEY display.
When Sleep Mode is OFF: removing the SAFETY KEY will not turn off the screen and there is no Sleep Mode.
When Sleep Mode is ON: removing the SAFETY KEY will turn off the screen and activate Sleep Mode. If there is no operation on
the IDLE MODE page for 15 minutes, the device will automatically enter Sleep Mode (it is not possible to enter Sleep Mode
without inserting the SAFETY KEY). When the screen is off during Sleep Mode, any key can be pressed to wake up the device.
Default: OFF
The explanation for ON/OFF will be displayed.




                                                            - 15 -
4)Screen Brightness
Adjusting to the left makes the screen darker, while adjusting to the right makes it brighter.


5)Date & Time
Press the ">" button to enter the date and time settings. The device supports switching between AM/PM and 24-hour clock
format.
Slide up and down to adjust the date and time. After completing the adjustment, press the "Save" button to save the changes.




                                                                - 16 -
6)Wi-Fi
Wireless network settings: Turn on WIFI and the system will automatically scan for nearby WIFI. Click on the WIFI name that you
want to connect to, enter the password for that WIFI, and the system will connect using the parameters inputted by the user. If
the connection is successful, pressing the Training button will return to the Settings page. If not, the device will only show
"Saved" and will not connect.


WIFI status icon: Connected          or Disconnected          .




7)Language
Press the ">" button to enter the language selection page, which includes Japanese, English, Spanish, Simplified Chinese,
German, French, Traditional Chinese, and Russian.




                                                              - 17 -
8)Software

If there is a need to update the main program, a yellow dot will be displayed on the gear icon of the IDLE MODE page.




Go to the Settings page and if a software update is detected, the Update button will light up. Click the Update button to initiate
the update process. The version will change after the update is completed. It is important not to interrupt the power supply
during the update process, as this could cause damage to the system and prevent it from functioning properly in the future.




                                                               - 18 -
If the software is already up to date, the message "Up to date" will be displayed.




                                                               - 19 -
9)Media Apps
If there are updates available for third-party media or mirroring applications, a yellow dot will be displayed on the gear icon of

the IDLE MODE page.




Go to the Settings page and navigate to the Media Apps section. If an update is detected for a third-party app, click on the '>' or

              button to enter the update list. Then click the            button for the desired app to initiate the update
process. During the update process, the power supply must not be interrupted, or the system may be damaged and unable to
function properly again. Click 'Back' to return to the Settings page.




                                                                - 20 -
- 21 -
10)Passcode
When the feature is turned ON, press the > button to enter the Enter Old Passcode page.




After entering the correct old passcode, a new passcode can be created.




                                                             - 22 -
The passcode needs to be re-entered to ensure correctness, and after completion, return to the Settings page.




If the passcode is entered incorrectly, the system will prompt "Wrong passcode. Please try again."




                                                              - 23 -
5.Unit Block Diagrams




                        - 24 -
6.Basic Connections and Wiring
6.1 Display Board wire Connections
OS version: Android 10




6.2 Display Board PCB Component Locations
PCB Board Top view




                                       - 25 -
PCB Board Bottom view




                        - 26 -
6.3 Patching Board Wire Connections
Console patching board




Console Outer Cover patching board




                                      - 27 -
6.4 Driver Board Wire Connections




                                    - 28 -
6.5 Driver Board PCB Component Locations




6.6 Driver Board function




                                       - 29 -
6.7 Driver Board LED Indicator Locations




6.8 Controller Indicator LED debugging




                                           - 30 -
7. Product Safety Instructions
7.1 Important Safety Instructions
- To reduce the risk of electric shock, disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a
220-volt, 10-amp grounded outlet with only the treadmill plugged into the circuit. 【120VAC electronic power system is 110-
volt, 15-amp】
- Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the
grounded plug by using improper adapters or in any way modify the cord outlet.

7.2 Important Electrical Instructions
- Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any appliance with a large motor, the
GFCI will trip often. Route the power cord away from any moving part of the treadmill including the elevation mechanism and
transport wheels.
- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill
is first turned on or even during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current
rating) but the circuit breaker on the treadmill itself does not trip, you will need to replace the home breaker with a high inrush
type. This is not a warranty defect. This is a condition we as a manufacture have no ability to control. This part is available
through most electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part #
QO120HM.


7.3 Important Grounding Instructions
- This product must be grounded. If the treadmill should malfunction or breakdown, grounding provides a path of least
resistance for electric current, reducing the risk of electric shock. This product is equipped with a cord having an equipment-
grounding plug. The plug must be plugged into an appropriate outlet that is properly installed and grounded in accordance with
all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric
shock. Check with a qualified electrician or serviceman if you are in doubt as to whether the product is
properly grounded. Do not modify the plug provided with the product if it will not fit the outlet; have a
proper outlet installed by a qualified electrician. This product is for use on a nominal 220-volt (on 120VAC electronic
power system need 110VAC) circuit and has a grounding plug that looks like the plug illustrated below. A temporary adapter that
looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly
grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from the adapter, must be
connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held
in place by a metal screw.




                                                                   - 31 -
8. Error Messages / Troubleshooting
Error Code List

            Code          Description
     PLEASE REPLACE THE   The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed.
         SAFETY KEY
                 E1       Display board CPU did not receive the RPM signal.
                 E2       Over current, over limit current of lower controller and motor.
                 E3       The console board is not detecting the VR voltage value, or the voltage value has
                          exceeded the range.
                 E4       Power wire of motor error.
                 E5       Communication signal error.
                 E6       Lower controller error.
                 E7       Input power error.


Tools Required

A multi-meter.




                                                    - 32 -
8.1 Error Message: PLEASE REPLACE THE SAFETY KEY




Definition:
Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is
broken.
Configuration:




Cause:
The console is not inserted the safety key, cause to console is not form a +12V’s loop (safety switch loop). So, display will be
appeared “PLEASE REPLACE THE SAFETY KEY”.
But possibly main control wires or component of lower controller is broken. (Because lower controller sent (+12V) signal via S/W
of main control wire to upper control board to form a safety switch loop.)
The socket on the Android 10 console board where the Safety Key module connector is inserted:




                                                             - 33 -
Troubleshooting:
Part                 Troubleshooting
                     Insert the safety key, and then use multi-meter transform into short circuit gear position to check safety
Safety module        module wires whether short or not.
                     Reinsert Main control wire.
Main control wires   Replace main control wire.
Display board        Replace upper control board.



Note: Before check hardware, first check software setting.
Remove safety key, press STOP & START & ENTER keys, and at the same time insert the safety key. The
display into “ENGINEERING MODE”, Press FAST/SLOW or UP/DOWN keys, to find “functions”, and press
Enter key into “DISPLAY MODE”, and then press Enter key into choosing on or off. When choose “off”,
this is mean display off after removed safety key. When choose “on” which is display on and appear
“PLEASE REPLACE THE SAFETY KEY” after removed safety key.




                                                         - 34 -
8.2 Error Message: E1




Definition:
Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM
sensor, but when the Calibration which it is a necessary.)
Configuration:




Cause:
The motor doesn’t turn then E1 appears.
The drive board did not sent voltage to the motor, so the motor did not operate. And the display board did not receive the RPM
sensor signal.




                                                             - 35 -
E1 solution follow chart:




                            - 36 -
E1 solution follow chart – check RPM sensor device procedure:




                                                - 37 -
Checking the speed sensor:
1. Remove the motor cover hood.
2. The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will have a belt around
it that also goes to the motor). The speed sensor is small and black with a wire connected to it.
3. Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley;
make sure the sensor is aligned with the magnet. There is a screw that holds the sensor in place that needs to be loosened to
adjust the sensor. Re-tighten the screw when finished.


Troubleshooting:
        E1                      Possible cause                             Things to check                           Solution
                    The upper console board hasn’t          check the speed sensor cable is in good        Make sure the good
                    received any speed signal for 8 seconds connection                                     connection for cables
The motor           The speed sensor didn't detect signal      Check the gap between speed sensor and To keep the gap-distance less
cannot move         completely.                                magnet.                                than 3 mm.
                    Defective sensor or bad cable              Check if the sensor and cables are circuit Change the sensor or cables.
                    connection.                                short damaged.




                                                                 - 38 -
8.3 Error Message: E2/OVER CURRENT




Definition:
When the controller detects that the operating current for the drive motor is above standard, the display will light up and show
the message "E2." This indicates that the controller needs to protect itself and the drive motor in order to prevent damage.
Typically, this is due to the running belt needing lubricate or its bottom fiber being worn seriously and requiring replacement. A
dried or worn running belt generates more friction between itself and the running deck. The resulting high friction causes the
controller requires to provide more current for the drive motor to maintain speed.
Troubleshooting:
First, we recommend that users lubricate the bottom of the running belt according to the instructions provided in the owner's
manual. If this does not resolve the issue, it may be due to excessive wear and tear on the running belt, in which case
replacement is necessary. By replacing the running belt, the operating current for the drive motor will return to normal levels.
If the E2 error still occurs after replacing the running belt, then either the controller or the drive motor may be defective. Since
the drive motor is a passive component, it is less likely to be the cause of the issue. Therefore, replacing the controller should be
the first option to consider.




                                                                - 39 -
8.4 Error Message: E3




Definition:
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” E3” appears on the
display.
Configuration:




                                                             - 40 -
Cause:
Incline VR resistor value exceeds the range. E3 appear on the display.
-The incline motor isn't operating up or down, causing the VR value to exceed the range.
-After turning on the unit, the display board detects that the incline VR voltage exceeds the range, and E3 appears.
-Action Flow Chart:




Troubleshooting:
Part                        Troubleshooting
                            Press incline keys, see the display weather appear value or not.
Display board               If no values, please check keys weather keys stuck or not, or replace display board.

                            -Inspect the wire connections.
Incline power cable
                            -Inspect whether wires are broken or crimped.
& incline VR cable          -Replace the wires and test again.
Controller                  Replace the controller.

                            -Inspect whether the incline motor is stuck.
                            -Inspect whether the incline gears are cracked.
Incline Motor               -Test whether the incline motor has a broke circuit.
                            -Recalibrate the incline set.




                                                              - 41 -
Test configuration:
The console to driver board connector pin define function.




Incline motor control function relate parts location.




                                                    - 42 -
Test procedure:
1.Run calibration again.
2.Does the incline motor move at all?
3.If not, do the Up/down lights on the controller light?
4.If they light, do the relays click on?
◆If the relay clicks on but the motor does not move: with the incline light and relay activated check the voltage between the
neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel
according to Up/Down lights on the board. It should be about the same as the mains voltage ~ 110VAC (230VAC). If the voltage is
present but the motor doesn’t move, then the motor is bad.
◆If the light is on, but the relay does not click on then the controller needs to be replaced (Bad relay most likely).
5.If the motor moves, is there a sensor reading on console?
◆The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0 for lowest incline.
The Incline window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count
occurring in the Incline window, then there is a problem in the position sensor wiring or circuitry.
◆If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings
(should not be able to rotate).
Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws
holding it to the motor casting.
If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the
potentiometer could be bad.
◆If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and
there should be a voltage between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the
lowest position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage at the white
wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire
connection between the potentiometer and the console.
6.Check the voltage from the potentiometer at the 3-pin connector on the controller. If there is no voltage, then the wire from
the motor to the connector is faulty.
7.If there is a voltage, check at the output connector to the console at the bottom of the controller. If no voltage present, then
there is a problem on the controller.
There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer
connector to the console connector.
The only problems that are possible are a bad solder joint or broken circuit on the board.
◆Console connector wiring, these connections are the same on the controller and at the console.
■Pin 1 = ground
■Pin 2 = position signal 0~5vdc
■Pin 3= 5vdc
8.If there is a voltage at the output connector to the console, then check the voltage at the console. If there is no voltage at
the console but there is a voltage at the controller, then check the entire cable from the controller to the console for cuts or
bad connections at the input wire connectors.
9.If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem
with the console.


                                                                 - 43 -
8.5 Error Message: E4




Definition:
Motor power wire error.
Configuration:




Cause:
Power wire of Motor does not insert lower controller.

Troubleshooting:
Part                      Troubleshooting
Controller                Insert power wire of motor.
Drive Motor               Replace Motor.
Display board             Replace upper control board.




                                                         - 44 -
8.6 Error Message: E5




Definition:
The communication between the console and the controller is poor. It may be due to a faulty main control wire, but it's also
possible that either the display board or the controller is malfunctioning.
Configuration:




Cause:
The main control wire is possibly broken. But E5 maybe has another problem, like a component of the controller or console.
Troubleshooting:
Part                           Troubleshooting
Lower controller board         Replace main control wire.
Main control wires             Reinsert or replace Main control wire.
Display board                  Replace display board.




                                                              - 45 -
8.7 Error Message: E6




Definition:
The lower controller component is fault.
Configuration:




Cause:
The controller component is fault, Like Transistor、IGBT、control module…etc.
Troubleshooting:
Part                             Troubleshooting
Controller                       Insert power wire of motor.
Display board                    Only Replace upper control board.




                                                               - 46 -
8.8 Error Message: E7




Definition:
Input power anomaly, possibly too low or too high or unstable.
Configuration:




Cause:
The wall outlet possibly unstable, cause to treadmill working power does not stable. Another problem possibly power part of
lower controller board is broken.
Troubleshooting:
Part                           Troubleshooting
Wall outlet                    Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or 220AC
                               or not. And the voltage whether stable or not.

Controller                     Replace Lower controller board.




                                                             - 47 -
8.9 Circuit Diagram




                      - 48 -
8.10 Engineering Mode
Press 10 times on “Settings” letter to enter engineering mode when you’re at the Settings page.
There are 6 main functions list: Engineering Mode, Diagnostics, Machine Information, Maintenance, Lube Setup, and Key Test.




                                                            - 49 -
1.Calibration procedure
Step 1: Press Engineering Mode to enter Calibration. Hit the block to enter the value by digital keyboard, and press ENTER to
save and close the keyboard. The display will appear the max./min. value if the entered value exceeds the range. The English
range: Max. (12.0)/Min. (0.5); the Metric range: Max. (20.0); Min. (1.0)




Step 2: Press Calibration button to start the procedure.




                                                              - 50 -
2.Machine Information
GR Mode (Grade Return) Default: ON Setting: ON/OFF
When GR MODE-OFF is switched to ON if the incline doesn’t back to zero, switch it to ON then go back to Setting, the incline
should back to zero.
When the GR Mode is ON:
-When the treadmill is power on, the incline should be at zero.
-When the user pauses the machine during workout, the incline should be at zero.
-When end of workout and the display at SUMMARY page, the incline should be at zero.
-When the display at HOME page, the incline should be at zero.
-When unplugging the SAFETY KEY, the incline shouldn’t return zero. When plugging the SAFETY KEY, the incline should be at
zero.
When the GR Mode is OFF:
-When the treadmill is power on, the incline shouldn’t be at zero.
-When the users pause the machine during workout, the incline should be at current level and shouldn’t be at zero.
-When end of workout and the display at SUMMARY page, the incline shouldn’t be at zero.
-Press START to begin; the incline should be at zero or at the current set level.
-When unplugging the SAFETY KEY, the incline shouldn’t be at basic level. When plugging back the SAFETY KEY, the incline
shouldn’t be at basic level.


Beep Mode (Buzzer Switch) Default: ON Setting: ON/OFF
This especially indicate the finger hitting sound of the touch panel, not indicate the actual keys on console keyboard. When it
switched to ON, it will appear the buzzer sound if the users hit the touch panel. When it switched to OFF, the buzzer sound will
be closed.


Display Mode Default: ON Setting: ON/OFF
About the sleeping mode function and display of SAFETY KEY function. When the setting is ON, the console won’t power down if
the users remove the SAFETY KEY. When the setting is OFF, the console will power down if the users remove the SAFETY KEY, the
display will turn off to have the console power down automatically after 30 minutes of inactivity. The user can press any key to
wake up the console.


Child Lock Default: OFF Setting: ON/OFF
If the user set the Child Lock ON, please repower the machine or re-plug the safety key to execute. The display will go to IDLE
MODE DM and will show “CONSOLE LOCKED”. The display will also show “Press Start and Display to enable operation” at the
bottom. The user can press START & STOP key within 3 seconds to unlock the Console to enter IDLE MODE.




                                                                 - 51 -
3.Lube Setup
-It’s the function to remind the user to lube deck, default time is 90 hours. The upper right on the display will show the total
using hour. Setting range: 90~200 hours.
-Power on the machine and if the total using hour reach the setting hours, the display will show the message ”LUBE DECK PRESS
STOP TO RESET LUBE MESSAGE” within 3 seconds, then the message will close and go to IDLE MODE.




-When the display goes to IDLE MODE, the Lube message won’t appear again until next setting hours (default 90 hours or user
defined hours). And the total using hour and distance won’t be clear, they will be kept accumulating.
-When the display shows the Lube message, the user can press STOP key to clear the message. And the Lube message won’t
appear again until next setting hours (default 90 hours or user defined hours). And the total using hour and distance won’t be
clear, they will be kept accumulating.
-Press STOP key to clear the Lube message. Or enter Lube Setup to hit “Zeroing”, then the display will show “Are you sure the
lube parameter needs to be reset?”. Select Yes to reset the total Using hour or not.
-If the total using hour doesn’t reach setting hour and the user decides to reset the Using hour, the accumulated using hour will
reset as zero.




                                                                - 52 -
4.Key Test
-Hit Key Test and the display will show you the name of the key, please press the according key to do key test.
-The display will show a message “All Done!” within 5 seconds when all the keys have been pressed to finish the test.




                                                               - 53 -
8.11 Troubleshooting procedure Matrix
Condition                           Reason                                        Solve
After turning on power, treadmill   Incorrect input power, varistor is blown      Check the voltage of power is 220V.
has a popping sound.                broken on controller.                         Replace controller. (On 120Vac electronic
                                                                                  power system need 110V)
When insert safe key, no display    1. Haven’t switch ON/OFF switch.              1. Switch the AC switch.
on monitor.                         2. Insert the Safe key on wrong position.     2. Insert the safe key on right position.
                                    3. 12 PIN Computer connector not plugged      3. Please check the wire and connect
                                    in properly.                                  again.
                                    4. 12 PIN computer cable is broken.           4. Replace 12 PIN computer cable.
                                    5. Fuse on controller is blown.               5. Replace fuse or controller.
                                    6. Varistor on controller is blown.           6. Replace varistor or controller.
                                    7. Safety device is broken. (open)            7. Replace safety key device.
                                    8. Other components are faulty.               8. Replace console.
With no safe key but treadmill      Safety device is broken. (short)              Replace the safety key device or console.
could display or operate
When press “START”, treadmill       1. Motor M+ or M- wire isn’t connected into   1. Please check and plug again.
doesn’t start.                      right position.                               2. Replace motor or check the wire and
                                    2. Motor is broken.                           connector if it was broken.
                                    3. Treadmill controller shut down and LED     3. Turn off the ON/OFF switch and turn on
                                    would be ON.                                  power again.
Treadmill stops or shuts off by     1. House breaker tripped.                     1. Reset it.
itself.                             2. Treadmill breaker tripped.                 2. Reset treadmill breaker.
                                    3. Treadmill controller shut down and LED     3. Belt / deck lubrication.
                                    would be ON.                                  4. Turn off the ON/OFF switch and turn on
                                                                                  power again.
After removing safety key,          1. The safety key device is broken.           1. Replace with new safety key device.
treadmill can’t stop.                                                             2. Replace controller.
                                                                                  3. Replace console.
TFT LCD not bright, incomplete,     1. Connector fall off.                        1. Check connector again.
or imperfect.                       2. TFT LCD light is broken.                   2. Replace with new LCD or console.
                                    3. Power to console too low.                  3. Check power to console.
                                                                                  4. Replace lower controller.
TFT LCD displays not bright,        TFT LCD displays are broken.                  Replace with new console.
incomplete, or imperfect.
The speed of the belt doesn’t       Controller is not calibrated, or the          1.Execute the calibration procedure.
match console display.              parameters of the controller are incorrect.   2.Replace controller.
The incline position doesn’t        Controller is not calibrated.                 Calibrate the console.
match console




                                                             - 54 -
Condition                          Reason                                         Solve
INCLINE ERR, INCLINE window        1. connector fall off.                         1. Check connector of cable.
displays “E3”.                     2. Position sensor value of incline motor is   2. Calibrate the console.
                                   wrong.




After pressing “START” button,     Controller is broken.                          1. Turn off the AC switch and turn on
the treadmill stops immediately.                                                  power again.
                                                                                  2. Replace controller and calibrate it.
Erratic pulse display.             1. Another chest belt in use around            1. Check for other chest belt use around
                                   treadmill.                                     treadmill.
                                   2. Other magnetic field disturbance.           2. Change the position or direction of
                                   3. Receiver is broken.                         treadmill.
                                                                                  3. Replace with new receiver.
After pressing “START” button,     Controller was broken.                         Replace with new controller and calibrate
the treadmill stops immediately.                                                  it.
FAST/SLOW button of SPEED          1. The connector of SPEED CABLE and            1. Connect cables again.
ADJUSTMENT SWITCH can’t be         CONSOLE not connected properly.                2. Check the wire of SPEED ADJUSTMENT
used.                              2. The connector of SPEED CABLE and SPEED      SWITCH.
UP/DOWN button of                  ADJUSTMENT SWITCH W/CABLE not                  2. Replace with new cable.
INCLINE ADJUSTMENT SWITCH          connected properly.                            3. Replace new SPEED ADJUSTMENT
can’t be used.                     3. Button of SPEED ADJUSTMENT SWITCH is        SWITCH.
                                   broken.
                                   4. The connector of SPEED CABLE or SPEED
                                   ADJUSTMENT SWITCH/W/CABLE is
                                   damaged.
Hand pulse lost its function.      1. Hands not on the hand pulse sensors or      1. Two hands hold the hand pulse.
(No pulse displayed on monitor)    only one hand on sensor.                       2. Connect the cable again.
                                   2. The connector of HANDPULSE W/WIRE           3. Replace with new cable.
                                   and Console not connected properly.            4. Replace console or Hand pulse board.
                                   3. The wires got damaged when connecting
                                   the HANDPULSE W/WIRE and Console.
                                   4. Hand pulse board is broken.
Wireless lost its function.        1. Chest belt not worn properly.               1. Check chest belt has proper contact
(No pulse displayed on monitor)    2. Distance is too far and exceeds range of    with skin and is oriented correctly.
                                   receiver.                                      2. User chest belt in front of console
                                   3. Chest belt battery is weak or dead.         within 3 feet.
                                                                                  3. Replace with new lithium battery type is
                                                                                  CR2032.




                                                            - 55 -
Condition                            Reason                                           Solve
Chest belt too close to the          Weak battery.                                    Replace with new lithium battery with
treadmill.                                                                            type CR2032.
Tread belt does not run in center.   Tread belt tension not even across tread         See treadmill belt adjustment
                                     belt.
Tread belt hesitates while being     Insufficient lubricant on tread belt.            See treadmill belt lubrication
stepped on.                          Tread belt tension insufficient
Black particles collecting under     Drive belt is breaking in.                       Vacuum under treadmill periodically.
treadmill.
Noise under motor cover.             1. Worn brushes or bearings on motor.            1. Replace with new motor.
                                     2. Front roller bearings are defective.          2. Replace with new front roller.
                                     3. Drive belt is misadjusted (too tight or too   3. Adjust motor position.
                                     loose).
Noise in the rear of the             1. Rear roller bearings are defective.           1. Replace with new rear roller.
treadmill.                           2. Rear roller misaligned.                       2. Adjust rear roller position.




                                                              - 56 -
9. Parts Replacing Guide
9.1 Replacing the Controller
Remove Motor cover and unplug all the controller wires. Then replace Controller and plug all wires back.




9.2 Replacing the Console
STEP 1: Use a screwdriver to remove the 4 Phillips head screws which secured the console on the console support.




STEP 2: Unplug all the wires, then replace the console.




                                                             - 57 -
9.3 Replacing the Drive Motor
STEP 1: Loose 5 Motor cover front locking screws with a screwdriver.




STEP 2: Unmount Drive motor ground wire and 2 input wires (black and red wire.).




STEP 3: Remove 4 Drive motor Locking bolts with a 14mm wrench and loose Drive belt.
Then do the reverse move to mount Drive motor back and 4 locking bolts but do not secure.




STEP 4: Adjust Drive belt tension with a 14mm open-end wrench. Measure belt tension with a tension meter. The tension needs
to be about 70~75LBS.




STEP 5: Plug Drive motor 2 input wires to Controller (Red to M+ / Black to M-) and mount ground wire.


                                                             - 58 -
9.4 Replacing the Breaker
Unplug Breaker wires to replace and plug wires back.




9.5 Replacing the AC Power Switch
Unplug AC Power switch wires to replace and plug wires back.




                                                               - 59 -
9.6 Replacing the Front and Rear Roller
STEP 1: Remove both Adjustment base cover screws with a screwdriver then take off them.




STEP 2: Remove 2 Rear Roller locking bolts with a M6 L-Allen wrench then take off Rear Roller.




STEP 3: Remove Drive motor cover then unmount Drive belt from Front Roller.
STEP 4: Remove Front Roller locking bolt with a 13mm wrench then take off Front Roller.
STEP 5: Adjust Running belt to the center is necessary when installing Front / Rear Roller back.




                                                               - 60 -
9.7 Replacing the Running Deck, Running belt, and Cushion
Note: To do these replacements need to unmount Cylinder first.
STEP 1: Folding treadmill. Unmount Cylinder with a L-Allen wrench and 12mm open-end wrench.




STEP 2: Remove Foot Rails with a screwdriver.




STEP 3: Remove 8 Running Deck locking screws then take off Running Deck. Now you can replace Running Deck, Running Belt,
and Cushions. To do the reverse steps to install them back.
STEP 4: Adjust Running belt tension and center it.




                                                              - 61 -
9.8 Replacing the Speed Sensor
Remove Motor cover then unplug Speed Sensor wire from Controller and replace it.




9.9 Replacing the Front Incline Motor
STEP 1: Take off Motor cover then folding treadmill.




STEP 2: Unplug Incline motor wires and unmount Incline motor from treadmill.
STEP 3: To adjust spare Incline motor to lower (225mm).




                                                           - 62 -
STEP 4: Install Incline motor back with 14mm open-end wrench.




STEP 5: Plug Incline motor wires to Controller.




                                                           - 63 -
9.10 Replacing the Rear Incline Motor
STEP 1: Unplug all the rear incline motor wires from the rear incline control board.
STEP 2: Use 2 14mm open-end wrenches to unmount the rear incline motor.




STEP 3: To adjust spare Incline motor to lower (205mm).




STEP 4: Install rear Incline motor back with 14mm open-end wrench.
STEP 5: Plug rear Incline motor wires to its control board.




                                                               - 64 -
