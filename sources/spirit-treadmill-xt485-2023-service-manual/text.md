<!-- Source: XT485 (485823) Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

                  1 of 48




SERVICE MANUAL
           XT485(2023)
          XT626-NT075
             Treadmill
                                                                                                                                                          2 of 48


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
       6.3 Interface Board Wires Connections .................................................................................................. 14
       6.4 Amplify Board Wires Connections.................................................................................................... 15
       6.5 Driver Board Wire Connections ........................................................................................................ 16
       6.6 Driver Board PCB Component Locations ........................................................................................ 17
       6.7 Driver Board function ........................................................................................................................ 17
       6.8 Driver Board LED Indicator Locations .............................................................................................. 18
       6.9 Controller Indicator LED debugging ................................................................................................ 18
7. Product Safety Instructions................................................................................................................... 19
     7.1 Important Safety Instructions............................................................................................................ 19
     7.2 Important Electrical Instructions ....................................................................................................... 19
     7.3 Important Grounding Instructions .................................................................................................... 19
8. Error Messages / Troubleshooting ...................................................................................................... 20
     8.1 Error Message: E0.............................................................................................................................. 21
     8.2 Error Message: E1.............................................................................................................................. 22
     8.3 Error Message: E2/OVER CURRENT ................................................................................................. 25
     8.4 Error Message: E3.............................................................................................................................. 26
     8.5 Error Message: E4.............................................................................................................................. 30
     8.6 Error Message: E5 ............................................................................................................................. 31
     8.7 Error Message: E6 ............................................................................................................................. 32
     8.8 Error Message: E7 ............................................................................................................................. 33
     8.9 Circuit Diagram ................................................................................................................................. 34
       8.10 Calibration Procedure ..................................................................................................................... 35
       8.11 Maintenance Menu ......................................................................................................................... 35
       8.12 Troubleshooting procedure Matrix ................................................................................................ 36
9. Parts Replacing Guide .......................................................................................................................... 39
     9.1 Replacing the Controller ................................................................................................................... 39
     9.2 Replacing the Console Assembly ..................................................................................................... 40
     9.3 Replacing the Drive Motor................................................................................................................ 41
     9.4 Replacing the Breaker ....................................................................................................................... 42
                                                                                                                                      3 of 48

9.5 Replacing the AC Power Switch ....................................................................................................... 43
9.6 Replacing the Front and Rear Roller ................................................................................................ 43
9.7 Replacing the Running Deck, Running belt, and Cushions ............................................................. 45
9.8 Replacing the Speed Sensor ............................................................................................................. 46
9.9 Replacing the Incline Motor .............................................................................................................. 47
             4 of 48


1.Outlines
                                  5 of 48


2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts
                                                                                                                      6 of 48


3.Electrical Configurations
Safety Key        The safety key fits into the Console to activate all functions and treadmill. Without safety key, console
                  cannot be controlled, and treadmill will not be activated.
Console           Interface that controls all functions of the treadmill.
Main Controller   The circuit board consists of the DC power supply for console、incline driver and DC motor driver, link
                  the console to output appropriate voltages for motor that control the treadmill functions.
Drive Motor       This is a DC motor with variable speed.     Control the 0 –90 (or 0-180) voltages from the main controller
                  to increase or decrease speed of the running belt.
Incline Motor     This is an AC motor. User can control variable elevation by console within main controller.


GENERAL INFORMATION
Console           Contains keys、 LCD Display、Speaker、Fan、. Hand Pulse Grip、Safety key, etc.
                  Main controller includes power supply, motor driver, control circuit and incline control circuit、Speed
                  sensor, etc. The 220V (or CEGS) of Lower Controller Area has Filter and Chock.
Drive Motor       DC motor with variable speed range 0-90 or (0-180) volt.     Requires three wire connection: red, black,
                  and green.
                  The Red wire is inserted into M+.
                  The White wire is inserted into M-.
                  When voltage is higher and higher, the motor will be faster.
                  The green wire is grounding wire.
Incline Motor     This is a 110 or 230 volt AC motor.
                  All of five wire connection: red, black, white, green, and has one of 3 pins cable for position sensor.
                  If there is AC voltage on the Red wire (UP), the incline motor will increase the incline.
                  If there is AC voltage on the Black wire (DOWN), the incline motor will decrease the incline. The White
                  wire (COM) is neutral.
                  The green/yellow wire is grounding wire.
                                                                                                           7 of 48


4.Product Operation




Window Display Mode
OFF Mode     When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode.
READY Mode   When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program
             profile name and cycle. Press START button to start treadmill on Manual Mode.
SLEEP Mode   In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
RUN Mode     In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop
             instantly and enter OFF Mode.


Function
SPEED        Display the current speed in Kilometer or mile per hour. DISPLAY range is 0.0 to 99.9.
             WORK range is 1.0~20.0KM or 0.5~12.0Mile.
             Press “FAST” or ”SLOW” to adjust speed, each increment and decrement is 0.1 km/h(mph).
INCLINE      Display the incline position from 0 to 15.
             DISPLAY range is 0 to 99.
             WORK range is 0 to 15. INCLINE preset value is 0 to 15.
             Press “UP” or ”DOWN” to adjust incline, each increment and decrement is 0.5.
TIME         TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
             is COUNT DOWN.
             DISPLAY range is 00:00 to 99:99.
             WORK range is 00:00 to 99:59.
             COUNT DOWN setup range is 10:00 to 99:00.
             When TIME is set, the count will go to zero.
             In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will
             continue count time.
                                                                                                              8 of 48

LAPS       Display the total working laps quantity.
           DISPLAY range is 0 to 999.
           WORK range is 0 to 999.
           Displays total laps quantity.
DISTANCE   Display the current distance in kilometer or Mile.
           DISPLAY range is 0.00 to 99.9.
           WORK range is 0.00 to 99.99.
CALORIES   Displays the cumulative calories burned at any given time during your workout.
           DISPLAY range is 0 to 9999.
           WORK range is 0 to 999.
PULSE      Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be
           worn.
           DISPLAY range is 0 to 999.
           WORK range is 50 to 200 BPM.
           In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value will become “0 ”.
                                                                                                                 9 of 48

Function Button Location




Button Function in each mode
Ready Mode
Safety Key           Fit safety key in right position to power on the computer. When safety key is pulled away from its
                     position, the computer will be automatically shut down.
Stop Key             Non-functional.
Start Key            Pressing “START” button to start treadmill, when pressing “START” button, there will be 3 second
                     final count down on window display, then machine starts running. In MANUAL, treadmill starts at
                     MIN SPEED and treadmill starts at program preset value in PROGRAM.
Enter Key            Press “ENTER” button to change each function. MANUAL can set using time, Pre-set PROGRAM can
                     set using time and speed, Heart Rate Control 1~2 can set time, age, and the value of heart rate.
                     User Program 1~2 can set time, speed, and incline.
                     Another the function is exchange and poll incline and speed profile appear.
Speed Fast Key       If user doesn’t enter a setting, then this button is non-functional.
Speed Slow Key       If user doesn’t enter a setting, then this button is non-functional.
Incline Up Key       If user doesn’t enter a setting, then this button is non-functional.
Incline Down Key     If user doesn’t enter a setting, then this button is non-functional.
Speed quick Keys     Non-functional.
Incline quick Keys   Non-functional.
Fan Switch           It can control ON/OFF for the fan.
Child Lock Key       When this in ENGINEERING MODE setting lock key ON that all keyboard button no working, then
                     MW will show the “HOLD CHILD LOCK BUTTON 3 SECONDS TO UNLOCK”. (On the IDLE MODE does
                     not work after 5 minutes of detection, the locked will ON.) if lock key off at ENGINEERING MODE
                                                                                                                10 of 48

                     setting, that unit keyboard can working.
Disable Key          To control ON/OFF for the handrail speed/incline switch.


Run Mode
Safety Key           When safety key is pulled away from its position, the computer will be automatically shut down.
Stop Key             press “STOP” key to stop treadmill.
Start Key            non-functional.
Enter Key            non-functional.
Speed Fast Key       Press the button to increase your speed and each increase is 0.1KPH (0.1mph). If button is pressed
                     continuously then speed increases to MAX SPEED quickly.
Speed Slow Key       Press the button to decrease your speed and each decrease is 0.1KPH (0.1mph). If button is
                     pressed continuously then speed decreases to MIN SPEED quickly.
Incline Up Key       Press the button to raise position and each increase is 0.5. The maximum incline position is 15.
Incline Down Key     Press the button to lower position and each decrease is 0.5. The minimum incline position is 0.
Speed quick Keys     10 preset buttons for rapid speed:    1，2，3，4，5，6，7，8，10，12 MI
                     (2/4/6/8/10/12/14/16/18/20KM)
Incline quick Keys   10 preset buttons for rapid incline: 0，1，2，4，5，6，8，10，12，15
Fan key              It can control ON/OFF for the fan.
Child Lock Key       Non-functional.
Disable Key          To control ON/OFF for the handrail speed/incline switch.
                        11 of 48


5.Unit Block Diagrams
                                     12 of 48


6.Basic Connections and Wiring
6.1 Display Board wire Connections
                                            13 of 48

6.2 Display Board PCB Component Locations
PCB Board Top view




PCB Board Bottom view
                                        14 of 48

6.3 Interface Board Wires Connections
                                      15 of 48

6.4 Amplify Board Wires Connections
                                    16 of 48

6.5 Driver Board Wire Connections
                                           17 of 48

6.6 Driver Board PCB Component Locations




6.7 Driver Board function
                                                                                                                                             18 of 48

6.8 Driver Board LED Indicator Locations




6.9 Controller Indicator LED debugging

Indicator
LED       Function                  Condition                              Reason                            Solve
POWER     Controller power          If DC voltage is normal, it would be   Voltage is not correct. Fuse is   Check the supply voltage is 110VAC or 230VAC

                                    always ON. If off, fault condition     blown.                            Replace Fuse.

                                    exists.                                Transformer is no good.           Replace controller.


Limit     Over current Protection   When lower board detect over           Protection lower board and        Replace controller.

current   warning light             current, the LED will be light.        motor.                            Replace motor.

                                                                                                             Do not block belt running.

                                                                                                             Between belt and running board need to smear

                                                                                                             Silicone oil.

                                                                           Transistor was broken.
UP        Motion of incline motor   Motion of incline motor is up.                                           Replace controller.
                                                                           Relay failed.
                                                                           Transistor was broken.
DOWN      Motion of incline motor   Motion of incline motor is down.                                         Replace controller.
                                                                           Relay failed

SPEED     RPM sensor indicator      The speed sensor didn't detect signal Check the gap between speed        To keep the gap-distance less than 3 mm.

                                    completely.                            sensor and magnet.
                                                                                                                                 19 of 48


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
                                                                                                          20 of 48


8. Error Messages / Troubleshooting
Error Code List

            Code      Description
                 E0   Safety keys dose not insert the safety module. Or safety module is broken.
                 E1   Display board CPU did not receive the RPM signal.
                 E2   Over current, over limit current of lower controller and motor.
                 E3   The console board is not detecting the VR voltage value, or the voltage value has
                      exceeded the range.
                 E4   Power wire of motor error.
                 E5   Communication signal error.
                 E6   Lower controller error.
                 E7   Input power error.


Tools Required

A multi-meter.
                                                                                                                          21 of 48

8.1 Error Message: E0
Definition:
Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is
broken.
Configuration:




Cause:
The console is not inserted the safety key, cause to console is not form a +12V’s loop (safety switch loop). So, display will be
appeared “E0”.
But possibly main control wires or component of lower controller is broken. (Because lower controller sent (+12V) signal via S/W
of main control wire to upper control board to form a safety switch loop.)


Troubleshooting:
Part                      Troubleshooting
                          Insert the safety key, and then use multi-meter transform into short circuit gear position to check safety
Safety module             module wires whether short or not.
                          Reinsert Main control wire.
Main control wires        Replace main control wire.
Display board             Replace upper control board.


Note: Before check hardware, first check software setting.
Remove safety key, press STOP & START & ENTER keys, and at the same time insert the safety key. The display into
“ENGINEERING MODE”, Press FAST/SLOW or UP/DOWN keys, to find “functions”, and press Enter key into “SLEEP MODE”, and
then press Enter key into choosing on or off. When choose “ON”, this is mean display off after removed safety key. When
choose “OFF” which is display on and appear E0 after removed safety key.
                                                                                                                      22 of 48

8.2 Error Message: E1
Definition:
Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM
sensor, but when the Calibration which it is a necessary.)
Configuration:




Cause:
The motor doesn’t turn then E1 appears.
The drive board did not sent voltage to the motor, so the motor did not operate. And the display board did not receive the RPM
sensor signal.
                            23 of 48

E1 solution follow chart:
                                                                24 of 48

E1 solution follow chart – check RPM sensor device procedure:
                                                                                                                             25 of 48




Checking the speed sensor:
1. Remove the motor cover hood.
2. The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will have a belt around
it that also goes to the motor). The speed sensor is small and black with a wire connected to it.
3. Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley;
make sure the sensor is aligned with the magnet. There is a screw that holds the sensor in place that needs to be loosened to
adjust the sensor. Re-tighten the screw when finished.


Troubleshooting:
        E1                      Possible cause                             Things to check                          Solution
                    The upper console board hasn’t          check the speed sensor cable is in good        Make sure the good
                    received any speed signal for 8 seconds connection                                     connection for cables
The motor           The speed sensor didn't detect signal     Check the gap between speed sensor and To keep the gap-distance less
cannot move         completely.                               magnet.                                than 3 mm.
                    Defective sensor or bad cable             Check if the sensor and cables are circuit Change the sensor or cables.
                    connection.                               short damaged.




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
                                                                                                                       26 of 48

8.4 Error Message: E3
Definition:
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” E3” appears on the
display.
Configuration:




Cause:
Incline VR resistor value exceeds the range. E3 appear on the display.
-The incline motor isn't operating up or down, causing the VR value to exceed the range.
-After turning on the unit, the display board detects that the incline VR voltage exceeds the range, and E3 appears.
-Action Flow Chart:
                                                                                                             27 of 48

Troubleshooting:
Part                  Troubleshooting
                      Press incline keys, see the display weather appear value or not.
Display board         If no values, please check keys weather keys stuck or not, or replace display board.
                      -Inspect the wire connections.
Incline power cable
                      -Inspect whether wires are broken or crimped.
& incline VR cable    -Replace the wires and test again.
Controller            Replace the controller.

                      -Inspect whether the incline motor is stuck.
                      -Inspect whether the incline gears are cracked.
Incline Motor         -Test whether the incline motor has a broke circuit.
                      -Recalibrate the incline set.



Test configuration:
The console to driver board connector pin define function.
                                                                                                                             28 of 48

Incline motor control function relate parts location.




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
                                                                                                                         29 of 48

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
                                                         30 of 48

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
                                                                                                                        31 of 48

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
                                                                              32 of 48

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
                                                                                                                     33 of 48

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
                              34 of 48

8.9 Circuit Diagram




                XT626-YT075
                                                                                                                          35 of 48

8.10 Calibration Procedure
1. Remove the safety key
2. Press and hold down the Start and Fast + buttons and replace the safety key. Continue to hold the Start and Fast key until the
   window displays “Factory settings”, then press the Enter key.
3. You will now be able to set the display to show Metric or English settings (Miles vs. Kilometers). To do this, press the up or
   down key to show which you want, then press Enter. (The maximum speed is displayed in the speed window, and the
   maximum elevation is displayed in the incline window.)
4. Adjust the maximum speed (if needed) to 20.0 kmph and then press Enter. (IMPERIAL set 12.0MPH)
5. Adjust the minimum speed (if needed) to 1.0 kmph and then press Enter. (IMPERIAL set 0.5MPH)
6. Make sure the wheel size diameter is 2.43 then press Enter.
7. Grade return – On (This allows the incline to return to zero when Stop is pressed.)
8. Press Start to begin calibration. The process is automatic; the speed will start up without warning, so do not stand on the belt.

8.11 Maintenance Menu
1. Press and hold the Start, Stop and Enter key at the same time, until the display shows “ENGINEERING MODE MENU PRESS
ENTER” (it may say maintenance menu, depending on version). Press the Enter key.
2. You can now scroll through the menu using the Speed ▲/▼ keys. Use the Stop key to return to previous menu selection. The
menu selections are:
A. Key Test - Will allow you to test all the keys to make sure they are functioning.
B. Display Test - Tests all the display functions
C. Functions - Press Enter to access settings, use Speed ▲/▼ keys to scroll.
I. SLEEP Mode - Turn ON to have the console power down automatically after 30 minutes of inactivity.
II. Pause Mode - Turned on to allow 5 minutes of pause, turn off to have console pause in definitely.
III. Maintenance - Reset lube message and odometer readings.
IV. Units - Choose from English or Metric display readings.
V. Key Tone - Will turn on/off beeping noise that is made when keys are pressed.
D. Security - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the child lock is enabled, the
console will not allow the keypad to operate unless you press and hold the Start and Enter buttons for 3 seconds to unlock the
console.
E. Exit
                                                                                                                       36 of 48

8.12 Troubleshooting procedure Matrix
Condition                           Reason                                        Solve
When turn on power, ON/OFF          1.Power cord isn’t plugged into outlet.       1.Plug the power cord into outlet.
switch isn’t lit.                   2.Power cord isn’t plug into unit.            2.Plug the power cord into unit.
                                    3.The voltage of outlet is too low.           3.Check the voltage of outlet.
                                    4.Plug or connector of power cord is open.    4.Replace power cord.
                                    5.Connector of power cord is broken.          5.Replace power cord.
                                    6.Connecting cable disconnected.              6.Check if wires are disconnected, connect
                                    7.Breaker tripped.                            it again.
                                    8.Breaker is broken.                          7.Press the small red button to return to
                                    9.ON/OFF switch is broken.                    original status.
                                                                                  8.Replace breakers.
                                                                                  9.Replace AC switch.
After turning on power, treadmill   Incorrect input power, varistor is blown      Check the voltage of power is 220V.
has a popping sound.                broken on controller.                         Replace controller. (On 120Vac electronic
                                                                                  power system need 110V)
When insert safe key, no display    1. Haven’t switch ON/OFF switch.              1. Switch the AC switch.
on monitor.                         2. Insert the Safe key on wrong position.     2. Insert the safe key on right position.
                                    3. 6 PIN Computer connector not plugged in    3. Please check the wire and connect
                                    properly.                                     again.
                                    4. 6 PIN computer cable is broken.            4. Replace 6 PIN computer cable.
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
                                                                                                                      37 of 48

Condition                          Reason                                         Solve
LCD not bright, incomplete, or     1. Connector fall off.                         1. Check connector again.
imperfect.                         1. LCD light is broken.                        1. Replace with new LCD or console.
                                   2. Power to console too low.                   2. Check power to console.
                                                                                  3. Replace lower controller.
LCD displays not bright,           LCD displays are broken.                       Replace with new console.
incomplete, or imperfect.
The speed of the belt doesn’t      Controller is not calibrated, or the           1.Execute the calibration procedure.
match console display.             parameters of the controller are incorrect.    2.Replace controller.
The incline position doesn’t       Controller is not calibrated.                  Calibrate the console.
match console
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
                                                                                                                          38 of 48

Condition                            Reason                                           Solve
Hand pulse lost its function.        1. Hands not on the hand pulse sensors or        1. Two hands hold the hand pulse.
(No pulse displayed on monitor)      only one hand on sensor.                         2. Connect the cable again.
                                     2. The connector of HANDPULSE W/WIRE             3. Replace with new cable.
                                     and Console not connected properly.              4. Replace console or Hand pulse board.
                                     3. The wires got damaged when connecting
                                     the HANDPULSE W/WIRE and Console.
                                     4. Hand pulse board is broken.
Wireless lost its function.          1. Chest belt not worn properly.                 1. Check chest belt has proper contact
(No pulse displayed on monitor)      2. Distance is too far and exceeds range of      with skin and is oriented correctly.
                                     receiver.                                        2. User chest belt in front of console
                                     3. Chest belt battery is weak or dead.           within 3 feet.
                                                                                      3. Replace with new lithium battery type is
                                                                                      CR2032.
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
                                                                                                           39 of 48


9. Parts Replacing Guide
9.1 Replacing the Controller
Remove Motor cover and unplug all the controller wires. Then replace Controller and plug all wires back.
                                                                                                         40 of 48

9.2 Replacing the Console Assembly
STEP 1: Use Phillips head screwdriver to loosen the 8 Sheet Metal Screw then remove the Upright cover.




STEP 2: Using an M6 L-Allen wrench to remove 4 bolts which securing the console on the uprights.




STEP 3: Disconnect all the control wires then replace the console assembly.
                                                                                                     41 of 48

9.3 Replacing the Drive Motor
STEP 1: Loose 5 Motor cover locking screws with a screwdriver.




STEP 2: Unmount Drive motor ground wire and 2 input wires (black and red wire.).




STEP 3: Remove 4 Drive motor Locking bolts with a 14mm T-type socket spanner and loose Drive belt.
Then do the reverse move to mount Drive motor back and 4 locking bolts but do not secure.
                                                                                                                  42 of 48

STEP 4: Adjust Drive belt tension with a 14mm open-end wrench. Measure belt tension with a tension meter. The tension needs
to be about 70~75LBS.




STEP 5: Plug Drive motor 2 input wires to Controller (Red to M+ / Black to M-) and mount ground wire.


9.4 Replacing the Breaker
Unplug Breaker wires to replace and plug wires back.
                                                                                                 43 of 48

9.5 Replacing the AC Power Switch
Unplug AC Power switch wires to replace and plug wires back.




9.6 Replacing the Front and Rear Roller
STEP 1: Remove both Adjustment base cover screws with a screwdriver then take off them.




STEP 2: Remove 2 Rear Roller locking bolts with a M6 L-Allen wrench then take off Rear Roller.




STEP 3: Remove Drive motor cover then unmount Drive belt from Front Roller.
STEP 4: Remove Front Roller locking bolt with a 13mm wrench then take off Front Roller.
                                                                                                   44 of 48

STEP 5: Adjust Running belt to the center is necessary when installing Front / Rear Roller back.
                                                                                                                         45 of 48

9.7 Replacing the Running Deck, Running belt, and Cushions
※Note: To perform these replacements, the Cylinder needs to be dismounted first.
STEP 1: Folding treadmill. Unmount Cylinder with an M5 Hex wrench and a 12mm open-end wrench.




STEP 2: Follow the 9.6 section to remove the front and rear rollers. Using a screwdriver to remove the foot rail fixing screws on
both sides. Then follow the direction to side both foot rails out.
                                                                                                                 46 of 48

STEP 3: Remove 8 Running Deck locking screws then take off Running Deck. Now you can replace Running Deck, Running Belt,
and Cushions. To do the reverse steps to install them back.
STEP 4: Adjust Running belt tension and center it.




9.8 Replacing the Speed Sensor
Remove Motor cover then unplug Speed Sensor wire from Controller and replace it.
                                                                               47 of 48

9.9 Replacing the Incline Motor
STEP 1: Take off Motor cover then folding treadmill.




STEP 2: Unplug Incline motor wires and unmount Incline motor from treadmill.
STEP 3: To adjust spare Incline motor to lower (225mm).




STEP 4: Install Incline motor back with 14mm open-end wrench.
                                                  48 of 48

STEP 5: Plug Incline motor wires to Controller.


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 81 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2 of 48

-Contents-
TOUTS. eee cece cneeeeecneeseeceneesesecseesecacsaesecaesaesecaesaesecsessesecseesesaesaesecaesaesecaeaesecaecaeeecsessecessassecaeeateeeateas 4
Q.EIECHOMIC PUES... eccceceeecseeseeecseeseeecseesecececeeecassaesecaesaesecneaesacsesseceesaesecassaeeesaeeaeeecaesaeeecearseseeeateeeateas 5
2.1 COMNMSOIC ...eeeceeesscecssccecsseeecsseeecsseeeesaeeeeaeeesaaecesaaeeseaaeceeaaecseaaesseaaeceeaeesesaeesesaeecsaaeeceaeeceeeesnaeeessaeeeeneeeeaees 5
2.2 Controller AN Driver Parts vcs cesescssecssecseecseeeseeseceeecsaecseeeeeeeeeeecssecsaecseeeseeeeeseessaessaecseeeseseeaeeessaeeaeeaee 5
3.Electrical COMPIQUIATIONS 00.0.0... eee cccccscssesecsceseecsessesecssssesecsecseecsessesecsessesaeseesesassaesessesseeessesaesessesaeeass 6
vd oXe [UL o4 ©) ol) co] | (0) 4 ee eee 7
5. Unit BlOCK DiC Gra. .......... ccc cccecccssesecsceeecseeeeceseescesecsessecaessecaasseceaeeaesaecsessecaessecaasseseaeeeeeaesaeseesaeseesaeeeres 11
6.Basic CONNECTIONS ANA WITING.............. cc cccecccscesecssesecseeecseeecssecscesecsessecsessecseseeceaecesaecsessecaesaecaeeersneees 12
6.1 Display Board Wire CONNECTIONS... cecesscssecsesseeeseesecesecsaeceeeaeeeeeeeecsaeceaecaaeeaeeeeeesessaessaesaeeeaeeeeesaeesaeed 12
6.2 Display Board PCB Component LOCAtIONS...... eee eeecesecetecseeeeeeeeeeecssecaecaeeeaeeseeseesaecaeeaaeeaeeeeeeaeesaeed 13
6.3 Interface Board Wires CONNECHIONS...... se ceseeseeseeeeeeeceeceseceeeseeeeeeseceaecsaecaaeeaeseeeeeesaesaeeaeeeaeeeeeeaeeeaeed 14
6.4 Amplify Board Wires CONNECTIONS... ceceseesesseeseeseceeceaeceeeseeseeesecaecsaecaaeeaeeeeeeseeaecsaesaeeeaeeeeeeaeesaeed 15
6.5 Driver Board Wire CONNECtIONS.... cs eecesscesecsesseeeeeseecesecsaeceesseeeeeeeessaecaecaaeeaeeeeeseesaecaesaeeeaeeeeeeaeeeaeed 16
6.6 Driver Board PCB Component LOCATIONS «eee eeeeeecetecetecseeeeeeeeeeeceaecaecaeeeaeseeesessaecaeeaeeeaeeeeeeaeesaeed 17
6.7 Driver Board FUNCTION... eeseeeeseeseeeseeesecsaeceeeaeeeeeseeceaecsaecaeeeaeeeeessessaecsaecaaeeaeeeeeeseesaecaesaeeeaeeeeesaeeeaeed 17
6.8 Driver Board LED Indicator LOCAtIONS .....eeeeeeeeseseecesecesecneeeseeeeeeeeceaecsaecaaeeaeseeeseeaecsaecaeeeaeeeeeseeenaeed 18
6.9 Controller Indicator LED CEDUGQING ....seeseeesseesesseceseceecseeeseeeeeseecsaecaecaaeeaeeeeeeessaecsaesaaeeaeeeeeseeesaeed 18
7. Product Safety INStrUctions............ ccc cccccssesesscssessescseesecscseesessessesecsessesecsecsececsessecessaseessesaseessesaeeesseeaees 19
7.1 Important Safety INStrUCTIONS..... ce eeseeeeseeeeeseeeeseceaecseeeaeeeeeeeeceaecsaecsaeeaeeeeesseesaesaecaaeeaeeseeseeassessaeenaeeaee 19
7.2 Important Electrical INStrUCTIONS oo. eeesseeseseeeesecesecneeeaeeseeeeeeesecsaecseecaeeeeesseeeaesaecaaesaeeeeeeeaeaeseaeenaeeaee 19
7.3 IMportant GroUNCiNG INStFUCtIONS .... ee eeeeeeeseeeseceecseeeseeseeeeeeesecaecaaeeaeeeeeeeesaesaecaaecaeeeeeseeseaessaeeaaeeaee 19
8. Error Messages / TrOUDIESHOOTING.............c cc cceccccsssscsssescsseeeceseescesecsessecseseecseseeceaececsaeeaeeaecaessesaeserenaees 20
B.1 Error M@SSAGE: EQ... eeeeesceesseeseesssecsseceeeeeeeeceecsseceseeseseecsuecsaeseseeseseecsuecsaeseeeeeeasecsueceseseeeeseasessaseeaeaeeges 21
8.2 Error M@SSAGE:! El... eeeeesceesseeseesseecsseceseeeseeeesuecsaeeeseeseaeecsuecsseseeeeecseecsuecsaeeceeeseaeecsueceaeseeeeseaaessaeseeaeaaes 22
8.3 Error Message: E2/OVER CURRENT ....eseesessesseesseseeceseceaeceesseeseeseesaeceaecaaeeaeeeeessesaecaaesaaeeaeeeeeseeeeaeed 25
8.4 Error M@SSAGE: ES... eeeeesceeesssseesseecsseceseeeseecsecsseceseeseseecsuecsaeseseeseaeecsuecssesceeeecaeecueceseseeeeseaaessaaseeaeenes 26
8.5 Error M@SSAGE: EA... eeeeescescseeseesseecseeceseeseseeceecsseeeseeseseecsuecsaeseseeseseecsueceaesceeeecaeecsueceseseeeeseaaessaeeeaeaeenes 30
8.6 Error M@SSAGE: ED ..eeeeeesceessseseeessecsseceeeeeseeecuecsaeeeseeseseecsuecsaeseseescseecsuecsaeseeeeseaeecsueceaeseeeeseaeecsaeseaeaeenes 31
8.7 Error MESSAGE: EG ...eeeeesceesseeseeeseecseceseeseeeecsaecsaeeeseeseseecsuecsaeseseeseseecsuecsaeseeeeseaeecsueceaeseeeeseaeecsaaseaeaseges 32
8.8 Error MESSAGE: E7 ..eeeecesceseseeseeesecseceseeseseecuecsaeceseeseseecsuecsaeseeeeseseecauecsaeseeeeeeseecsaeceaeeeeeeseagessaaeeeaeeges 33
B.9 CirCUit DIAGrAM ...eeeeeseeessecssecsseseeseeeeecssecaecaeeeaeeeeessecaecsaecaeeeseeeeassecaecsaecaaeeaeeeeeeaesaecaaesaaeeaeeeeeseessaeed 34
8.10 Calibration PrOCCCUIEC «uss ceseeessessessecesecssecseesseeseeseecsaecaecaaeeaeeeeesecaecsaecaaeeaeseeessessaecaaesaaeeaeeeeeeaeseaeed 35
B.11 Maintenance MENU ....esceeseeescesseceeeceeeeeeseecseecaeeeeeeeaeecaaecsaeeeseeesaeecaaecsaeseaeeeaeessaesaeeeeeeseaeesaeeeeeseaes 35
8.12 Troubleshooting Procedure Matrix ...eeceseeesseseeeseceseceecseeseeseeeeecsaeceaeceeeaeseeeseesaecaesaeeeaeeeeeeaeesaeed 36
9. Parts REplacing Guide ......... eee ccccccssssscseeeeceseescesecsessecsessecsessecesseacsaecsessecseseeceasesaseaeeaecaesaesaesereaaees 39
9.1 Replacing the CONtrOller ce eeessesessecssecssecseesseeseeesecsecsaeceeeeeseeseecssecsaecaaeeaeeeeesessaecsaesaaeeaeeeeeseessaeed 39
9.2 Replacing the Console ASSEMDIy oo... ceseesesesseeeeeseecssecsaecseeeeeeeeseessaecaecaaeeaeseeeseesaecaeeaaeeaeeeeeeaeseaeed 40
9.3 Replacing the Drive MOtol.... ce eeeesssscssecssecseeseesessecsecsaecseeeseeseeseecssecaecaaesaeseeeeessaeceaesaeeeaeeeeeseeseaeed 41
9.4 Replacing the Breaker oo... ceceessescsscssecssecseesseessesseceecsaeceesseeseeseessaecaecaaeeaeeseeseseaecaesaaeeaeeeeeseeesaeed 42


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9.7 Replacing the Running Deck, Running belt, ANd CUSNIONS veces eee ceeseeeeeseeseeesseeseeeteeeeeseeeeeee
9.8 Replacing the SOCCA SENSOM.. ea eeeescesecssecseeeseeseeesecesecsaeceesaeeeeeseesesecaecaaeeaeeeeeesesaecaesaaeeaeeeeeeaeeeaeed

9.5 Replacing the AC Power Switch
9.6 Replacing the Front and Rear Roller

9.9 Replacing the Incline Motor


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 36 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4 of 48

1.Outlines

1 Console 11. =Motor Cover

2 Foot Pad 12 = Running Belt

3. ~=Heart rate sensor 13 Base Frame Cover (L)

4 Fan 14 Rear Adjustment Cover (L)
5 Speaker 15 Rear Adjustment Cover (R)
6 Drink Bottle Holder (L) 16 MainFrame

7 Drink Bottle Holder (R) 17 Incline Handlebar Key

8 Base Frame 18 Speed Handlebar Key

9 Upright (L) 19 Foot Rail

Upright (R) 20 = Pad Holder


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5 of 48

2.Electronic Parts

2.1 Console

Serr

ddl

= Cooling Fan (<)) Speaker

2.2 Controller and Driver parts

Speed Sensor !

Drive Motor
Incline Motor <= F
: aot

Controller


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7 of 48

4.Product Operation

SPIRIT

= -——-e 9" LCD Display

: A idhesdealbeal

A2TR2 ORD ORs tar RATES

Incline

Speed
Handlebar key

Handlebar key

Window Display Mode

OFF Mode When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode.

READY Mode When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program

profile name and cycle. Press START button to start treadmill on Manual Mode.

SLEEP Mode In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.

RUN Mode In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop

instantly and enter OFF Mode.

Function

SPEED Display the current speed in Kilometer or mile per hour. DISPLAY range is 0.0 to 99.9.
WORK range is 1.0%20.0KM or 0.5%12.0Mile.
Press “FAST” or ”SLOW” to adjust speed, each increment and decrement is 0.1 km/h(mph).

INCLINE Display the incline position from 0 to 15.
DISPLAY range is 0 to 99.
WORK range is 0 to 15. INCLINE preset value is 0 to 15.
Press “UP” or ”?DOWN?” to adjust incline, each increment and decrement is 0.5.

TIME TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer

is COUNT DOWN.

DISPLAY range is 00:00 to 99:99.

WORK range is 00:00 to 99:59.

COUNT DOWN setup range is 10:00 to 99:00.

When TIME is set, the count will go to zero.

In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will

continue count time.


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9 of 48

Function Button Location

SPIRIT

Fan Key e_

_# Enter Key

SPIRIT

a ; ia ei . e Program Ke
Child Lock Key * Sl = “os

_e® Speed Quick Keys

— 4/2/3/4/5/6/7/8/10/12 MI
2/4/6/8/10/12/
14/16/18/20 KM

___-® Speed Fast Key

Incline Quick Keys
0/1/2/4/5/6/8/10/12/15

Incline Up Key *—__

Incline Down Key *-, ———# Speed Slow key

~~ ~~ STOP Key
START key ® _~* Safety Key
Button Function in each mode
Ready Mode
Safety Key Fit safety key in right position to power on the computer. When safety key is pulled away from its
position, the computer will be automatically shut down.
Stop Key Non-functional.
Start Key Pressing “START” button to start treadmill, when pressing “START” button, there will be 3 second
final count down on window display, then machine starts running. In MANUAL, treadmill starts at
MIN SPEED and treadmill starts at program preset value in PROGRAM.
Enter Key Press “ENTER” button to change each function. MANUAL can set using time, Pre-set PROGRAM can
set using time and speed, Heart Rate Control 1~2 can set time, age, and the value of heart rate.
User Program 1~2 can set time, speed, and incline.
Another the function is exchange and poll incline and speed profile appear.
Speed Fast Key If user doesn’t enter a setting, then this button is non-functional.
Speed Slow Key If user doesn’t enter a setting, then this button is non-functional.
Incline Up Key If user doesn’t enter a setting, then this button is non-functional.
Incline Down Key If user doesn’t enter a setting, then this button is non-functional.
Speed quick Keys Non-functional.
Incline quick Keys Non-functional.
Fan Switch It can control ON/OFF for the fan.
Child Lock Key When this in ENGINEERING MODE setting lock key ON that all keyboard button no working, then

MW will show the “HOLD CHILD LOCK BUTTON 3 SECONDS TO UNLOCK”. (On the IDLE MODE does
not work after 5 minutes of detection, the locked will ON.) if lock key off at ENGINEERING MODE


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11 of 48

5.Unit Block Diagrams

=a WIRELESS HR
“ ‘—T  RECEIVER
COOLING FAN }—¢ ¢—# SAFETY KEY
HR
HANDLEBAR id @—>| AMPLIFIER @—>] SPEAKERL/R
A |
BLUETOOTH }#——

ad MOTOR

CURRENT |__ 4) DRIVER || INCLINE
a R O ARD MOTOR

t—? = =VR SET

POWER

——|
POWER SWITCH t

RPM SENSOR


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 55 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
é , = a
| suoqing 8 a | a

fEsPUeY GuvOeASy

SUI|DU! YIINO
Kay ayes Gy

suoling
a|qep joUOD |reupuey
ule) uld-9 peeds yoIN?

JOAIQOOI
Oye WY SSO[OJIM
JaMOdq
Josey

gsn feubis disnyy sf
41d )

BS JaMOd 2InP OW

a oIsnW 31d a
asing pueH

cup
OG yes US

oe

id Ald

: 1

SUOIDBUUOD JIM Pleog Aeldsig [9

BulIM PUD SUOIDaUUOZD JISDg'9

8v 49 eL


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
14 of 48

6.3 Interface Board Wires Connections

DISPLAY BOARD DISPLAY BOARD. Ori AY BOARD icp ay BOARD
i SAFETY KEY

RF _JK5 JK 8

INTERFACE BOARD
(Inside of the console)

16PIN CABLE 8 PIN CABLE

DISPLAY BOARD
HAND PULSE

GROUNDING 19s —

KEYPAD
AA02260-00T-01-K1

INTERFACE BOARD

(INSIDE OF CONSOLE BRACKET) USB CHARGING

AA02260-00T-01-K2

HAND PULSE

INCLINE
(GRIP) SPEED HR

UP/DOWN FAST/SLOW precEIveR SAFETY KEY
(HANDRAIL) (HANDRAIL)


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Q fn
Zz Qh
> = a
- Cc ms
5 aD Cc
ra a)
ra


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
17 of 48

6.6 Driver Board PCB Component Locations

Tr) ¥

" Ss

a

ww

6.7 Driver Board function

AC in L Drive motor M-

AC in N Drive motor M+

AC FAN

AC FAN Incline motor VR
Incline motor DOWN

Display board Speed
Sensor

Incline motor COM

Incline motor UP


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
19 of 48

7.Product Safety Instructions

7.1 Important Safety Instructions

- To reduce the risk of electric shock, disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a
220-volt, 10-amp grounded outlet with only the treadmill plugged into the circuit. [[120VAC electronic power system is 110-
volt, 15-amp ]

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

PY lai Improper connection of the equipment-grounding conductor can result in a risk of electric
shock. Check with a qualified electrician or serviceman if you are in doubt as to whether the product is
properly grounded. Do not modify the plug provided with the product if it will not fit the outlet; have a

proper outlet installed by a qualified electrician. This product is for use on a nominal 220-volt (on 120VAC electronic
power system need 110VAC) circuit and has a grounding plug that looks like the plug illustrated below. A temporary adapter that
looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly
grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from the adapter, must be
connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held
in place by a metal screw.

Adapter
Grounded Outlet

NN tab of

(10) “T\ metal Screw Grounding
Bh Screw

Grounding Pin \ rounded Outlet Box


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
22 of 48

8.2 Error Message: E1

Definition:
Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM
sensor, but when the Calibration which it is a necessary.)

Configuration:

CONSOLE
DISPLAY BOARD

Send and receive 4

i i RPM SENSOR MOTOR SPEED
speed signal via TX/RX samane Aaceectcy
of 6-pin Main wire. =

v

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER >» DRIVER BOARD

= SIGNAL

PIN RPM
— SENSOR

Cause:

The motor doesn’t turn then E1 appears.

The drive board did not sent voltage to the motor, so the motor did not operate. And the display board did not receive the RPM
sensor signal.


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 68 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart:

El showing up — Reset power L—»

Press start again

Replace upper console board or
update the program of upper
console board

‘ >| Replace lower control driver board

Use multi-meter to
Check Wain control line
socket pin2 & pind is
DC12V)

Then, press start and
use multi-meter to
Check driver board

notor socket weather

voltage or not?

NO

Check display whether Countdown
or not after pressing start?

Did belt moves after
start?

Check lower control
driver board weather
enough Power?
(AC: 2207)

Check power source from wall weather
stable AC220V or not?

Vv

Check main control line
whether split or not?

Check RPM sensor
whether well or not?

23 of 48

Adjust sensor gap distance to 2nm.

Did belt moves after
start?

YES

Replace Motor

>

Solve the problem

Replace main
control line
Replace RPM
sensor
Vv v


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 48 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
24 of 48

E1 solution follow chart — check RPM sensor device procedure:

Check RPM sensor
procedure

Sensor cable connected

iy? NO—e] Conpect Properly

YES

¥

Move the rolier so
that meegent closest
to the scnsur

Make surc the gap
between magnct'senser less
than 3 mo

NO Adhust sensor
position

YES

Replace sensor with
cable

um power back o
press “start” and
comnidown
Is function OK?

YE Propiem fixed

NO

Replace computer
cuble

um power back a
press “start” and
commidown ts function
OK?

YES—e} Probtern fixed

NO

Replace Comsile


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
26 of 48
8.4 Error Message: E3

Definition:
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” E3” appears on the
display.

Configuration:

DISPLAY BOARD

. : The incline VR
aie le single via TX/RX of
VOLTAGE Main control wire
send and receive.

INCLINE
MOTOR
DRIVER BOARD a= VR VOLTAGE INCLINE VR SET

Cause:

Incline VR resistor value exceeds the range. E3 appear on the display.

-The incline motor isn't operating up or down, causing the VR value to exceed the range.

-After turning on the unit, the display board detects that the incline VR voltage exceeds the range, and E3 appears.
-Action Flow Chart:

Zz Zz Z Z er

= > = = -
> > < ~ = 3
~ _ =x = ad
3 f &-) = = z=
= oe - = - = i > - ar |
= = + <= -xz
Zz 3 mA a = <9
_ = ZF. x 4
S - SK


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
27 of 48

Troubleshooting:

Part Troubleshooting

Press incline keys, see the display weather appear value or not.
If no values, please check keys weather keys stuck or not, or replace display board.

Display board

-Inspect the wire connections.
-Inspect whether wires are broken or crimped.
-Replace the wires and test again.

Incline power cable
& incline VR cable

Controller Replace the controller.

-Inspect whether the incline motor is stuck.
-Inspect whether the incline gears are cracked.
-Test whether the incline motor has a broke circuit.
-Recalibrate the incline set.

Incline Motor

Test configuration:
The console to driver board connector pin define function.

Syne COG

RSH

ee P1 GND
P2 TXD
P3 RXT
P4 VCC
P5 SW
P6 FAN E/D


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
28 of 48

Incline motor control function relate parts location.

The position sensor wire
P1 GND(Red)
DOWN-Black P2 Position signal (White)
COM-White P3 +5Vcc (Black)
UP-Red

Incline Relay

Test procedure:

1.Run calibration again.

2.Does the incline motor move at all?

3.If not, do the Up/down lights on the controller light?

4.If they light, do the relays click on?

@ If the relay clicks on but the motor does not move: with the incline light and relay activated check the voltage between the
neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel
according to Up/Down lights on the board. It should be about the same as the mains voltage ~ 110VAC (230VAC). If the voltage is
present but the motor doesn’t move, then the motor is bad.

lf the light is on, but the relay does not click on then the controller needs to be replaced (Bad relay most likely).

5.If the motor moves, is there a sensor reading on console?

@The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, O for lowest incline.
The Incline window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count
occurring in the Incline window, then there is a problem in the position sensor wiring or circuitry.

@\f there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings
(should not be able to rotate).

Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws
holding it to the motor casting.

If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the
potentiometer could be bad.

@ If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and
there should be a voltage between the red and white wire. This voltage will be about 4.5~%4.7 Vdc when the motor is at the
lowest position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage at the white
wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire

connection between the potentiometer and the console.


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
29 of 48

6.Check the voltage from the potentiometer at the 3-pin connector on the controller. If there is no voltage, then the wire from
the motor to the connector is faulty.

7.1f there is a voltage, check at the output connector to the console at the bottom of the controller. If no voltage present, then
there is a problem on the controller.

There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer
connector to the console connector.

The only problems that are possible are a bad solder joint or broken circuit on the board.

@Console connector wiring, these connections are the same on the controller and at the console.

WiPin 1 = ground

BiPin 2 = position signal O~Svdc

BBPin 3= 5vdc

8.If there is a voltage at the output connector to the console, then check the voltage at the console. If there is no voltage at
the console but there is a voltage at the controller, then check the entire cable from the controller to the console for cuts or
bad connections at the input wire connectors.

9.If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem

with the console.


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
30 of 48
8.5 Error Message: E4

Definition:
Motor power wire error.

Configuration:

DISPLAY BOARD

4

The signal
RPM or via TX/ RX Send
Motor of Main command of
signal control wire+ start or speed
return.- signal «

MOTOR

Power of Motor-+-

DRIVER BOARD

1

Cause:

Power wire of Motor does not insert lower controller.

Troubleshooting:

Part Troubleshooting
Controller Insert power wire of motor.
Drive Motor Replace Motor.

Display board Replace upper control board.


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
32 of 48
8.7 Error Message: E6

Definition:
The lower controller component is fault.

Configuration:

Console

Signal via main
control wire to
communication.

Lower controller

Cause:
The controller component is fault, Like Transistor » IGBT + control module::-etc.

Troubleshooting:

Part Troubleshooting

Controller Insert power wire of motor.

Display board Only Replace upper control board.


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
33 of 48

8.8 Error Message: E7

Definition:
Input power anomaly, possibly too low or too high or unstable.

Configuration:

Console

Wall outlet
AC 110V
Or

AC 220V

| Signal via main
Overload control wire.
protection

¥
Power Switch ;———.—>_ Lower controller

>
ts I

CE PART or 220V to match
Filter and Chock.

Cause:

The wall outlet possibly unstable, cause to treadmill working power does not stable. Another problem possibly power part of
lower controller board is broken.

Troubleshooting:

Wall outlet Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or 220AC

lor not. And the voltage whether stable or not.

Controller Replace Lower controller board.


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 40 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
34 of 48

8.9 Circuit Diagram

XT626-YT075 TREADMILL SCHEMATIC

6 PIN COMPUTER CABLE
Cc} yy
“\/
a
a
INPUT POWER 3
ae
ive)
y ®
PLUG 4
1?)
£
©
“
{y comecror av
On /O#
SWITCH
BREAKER
INLET oO
a ?
BLACK Wine
WHITE WIRE w
2
w | Oo
wx =
t I¢
FILTER a
—.| oS
3 3 INCLINE
=| = MOTOR
“NS
“\/
w
a
qQ
3
Lt
E
M+ M JK 51 | yk 90 ¥ &
oO
1®)
wi z
o¢ a
ive]
MOTOR WHITE WIRE

SPEED SENSOR ENSOR
GROUNDING


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
41 of 48

9.3 Replacing the Drive Motor

STEP 1: Loose 5 Motor cover locking screws with a screwdriver.

TE | 1 by
Plilg@- ttt i TG al | |

STEP 2: Unmount Drive motor ground wire and 2 input wires (black and red wire.).

Tite ||

= —E

AAC AA

STEP 3: Remove 4 Drive motor Locking bolts with a 14mm T-type socket spanner and loose Drive belt.

Then do the reverse move to mount Drive motor back and 4 locking bolts but do not secure.


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
48 of 48

STEP 5: Plug Incline motor wires to Controller.

—
(y
SR)
SS
|
i]

ip

Black wire connects to DOWN port:
