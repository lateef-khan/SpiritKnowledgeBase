<!-- Source: CT800ENT Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

  CT800 ENT
           2020 ver.


Service Manual
                                                                                                 Table of Contents

1. Outlines........................................................................................................................................................................................................................................... 4
2. Electronic Parts .............................................................................................................................................................................................................................. 6
4. Product Operation ..................................................................................................................................................................................................................... 11
5. Unit Block Diagrams .................................................................................................................................................................................................................... 15
6. Basic Connections and Wiring .................................................................................................................................................................................................. 17
7. Product Safety Instructions ........................................................................................................................................................................................................ 27
8. Error Messages / Troubleshooting ............................................................................................................................................................................................. 30
    8-1 Error code items ................................................................................................................................................................................................................... 31
    8-2 Prepare tools ........................................................................................................................................................................................................................ 32
    8-3 Error Message: E3 ................................................................................................................................................................................................................. 33
    8-4 Error Message: Incline Err .................................................................................................................................................................................................... 34
    8-5 Circuit Diagram .................................................................................................................................................................................................................... 35
    8-6 Troubleshooting procedure matrix .................................................................................................................................................................................... 36
    8-7 Troubleshooting.................................................................................................................................................................................................................... 39
    8-8 Engineering Mode Instructions ........................................................................................................................................................................................... 40
           Home .................................................................................................................................................................................................................................... 40
           Engineering Mode Settings ............................................................................................................................................................................................... 41
           Engineering Mode .............................................................................................................................................................................................................. 42
           Security................................................................................................................................................................................................................................. 43
           Diagnostics .......................................................................................................................................................................................................................... 44
           Machine Information ......................................................................................................................................................................................................... 45
           Maintenance ...................................................................................................................................................................................................................... 46
                   Maintenance - Default language Setup ................................................................................................................................................................. 47
                   Maintenance - Set default Wi-Fi................................................................................................................................................................................ 48



                                                                                                                                                                                                                                                           2
                   Maintenance - Set default Ethernet ......................................................................................................................................................................... 49
                   Maintenance - Set default Bluetooth....................................................................................................................................................................... 50
           A/V Source Setup ............................................................................................................................................................................................................... 51
           Lube Setup .......................................................................................................................................................................................................................... 52
9. Disassembling and Assembling ................................................................................................................................................................................................. 53
    9-1 Lower Controller replacement .......................................................................................................................................................................................... 54
    9-2 Console replacement ......................................................................................................................................................................................................... 54
    9-3 Drive Motor replacement ................................................................................................................................................................................................... 55
    9-4 AC Power Switch replacement ......................................................................................................................................................................................... 56
    9-5 Front / Rear Roller replacement ........................................................................................................................................................................................ 57
    9-6 Running Deck/ Belt & Cushion replacement ................................................................................................................................................................... 58
    9-7 Incline Motor replacement ................................................................................................................................................................................................ 59
10. Q&A ............................................................................................................................................................................................................................................ 60
    10-1 The Console and Error Messages..................................................................................................................................................................................... 61
    10-2 Belt Slipping and Falling-off .............................................................................................................................................................................................. 61
    10-3 Noises problem .................................................................................................................................................................................................................. 62




                                                                                                                                                                                                                                                          3
1. Outlines




              4
                        Console
        Cooling Fan



          Safety Key    Drink Bottle Holder




                        Handle Pulse Sensor
Adjustable Foot Pad


                       Running Belt

Rear Roller End Caps

                        Moving Wheel




                                              5
2. Electronic Parts




                      6
Upper Controllers




                    Display



                              Earphone
                                Port




                                         7
Lower Controller and Driver



     Drive Board
                              DC Drive Motor




      Converter

                              Incline Motor




   Power Bridge
      Board




                                               8
3. Electrical Configurations




                               9
SAFETY KEY:
To fits on the Console that activate all functions. If no safety key, console cannot be controlled.

CONSOLE:
Interface that controls all functions of the Treadmill.

MAIN CONTROLLER:
The circuit board consist of the AC power supply for console、incline driver and DC motor driver, link the console to output appropriate voltages for DC control
Board that control the Treadmill functions.

DC MOTOR:
It can change to increase or decrease speed change.

INCLINE MOTOR:
This is an AC motor. User can to control variable elevation by console within main controller.


GENERAL INFORMATION
CONSOLE:
Contains Key controls and TFT Display.

MAIN CONTROLLER:
Include power supply、DC motor、incline motor、DC control Board control circuit and incline control circuit.

INCLINE MOTOR:
This is a 110 volt AC motor.
Have four wires, red, black, white and green.
Has one 3 pins cable of position sensor.
If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
The White wire (COM) is neutral. The green wire is ground.



                                                                                                                                                                  10
4. Product Operation




                       11
Display Windows




        Tablet-friendly    Touch Screen
         Reading rack



                           Adjustable fan angle
    Cell Phone Ledge



                           USB Charging port
    Small Tray Storage



                           Convenient accessory
Stars, Stop, and Incline
                           trays
           Control Keys




                           Safety Key
        Contact Heart
           Rate Grips




                                                  12
Operation

  Starting the operation
  Plug in the power cord and switch on the main power switch located at the front, under the motor hood of the treadmill and make sure that the safety key is
  put on as the treadmill is unable to operate without the safety key.
  When the power is turned on, the screen will show the initial image and then enter the ready mode which is the beginning of the treadmill operation.

  Quick start operation
  •Press any button to wake display up if not already on.
  •Press the Start button to begin belt movement at 0.5 mph, then adjust to the desired speed using the Speed ▲ / ▼ keys.
  •To slow tread-belt press and hold the Slow key (console or hand rail) to the desired speed.
  •To stop the tread-belt press and release Stop button.

  Pause/Stop
  • Press “STOP” button once or first page button on the screen, the belt will slow down gradually till fully stop and keep values of time, distance and calorie on
  the screen. The screen will reset after 5 minutes of counting down then return to the previous status.
  • Press “START” button to continue the workout during pause.
  • Press “STOP” button twice will terminate the setting with displaying the workout summary. If “STOP”button is pressed the third time, the console will return
  to the initial status (the beginning).

  Incline
  • The incline is changeable any time during the workout.
  • Press and hold Incline ▲ / ▼ button or Incline ▲ / ▼ button on the screen to change the incline to the desired level.




                                                                                                                                                                      13
Heart rate testing feature
Pulse (heart rate) on the screen shows the current value of the heart beats per minute. You must hold both left and right stainless steel sensors to test the
pulse. The pulse value will be shown on the screen continuously. You can also use hand pulse sensors for heart rate control. The console can also detect the
pulse from heart rate stripe which is bipolar including signal transmitting.

Heart Rate Bar Graph
Display a graphical representation of your heart rate as a percentage of your estimated maximum heart rate. When you enter your age during programming,
the console will calculate your maximum heart rate then light up the graph to show the percent of estimated maximum heart rate you are currently achieving.

Message Window Display
Displays messages that help guide you through the programming process. During a program the message window displays your workout data.




                                                                                                                                                                14
5. Unit Block Diagrams




                         15
Treadmill Configuration


                    HR
                                                     Cooling Fan
                 Handle Bar
                                    Console back
      HDMI Coaxial cable
           C-SAFE                   cover transfer
                    Key
                                       Board         Headphone port




                                         Power
                      Converter
                                      Bridge Board


         Power                                       DC Drive Motor
                           Filter
         Switch
                                                      RPM Sensor
                                     Drive Board
                                                      Incline Motor
         Power            AC Fan
                                                         VR Set

                                                                      16
6. Basic Connections and
          Wiring




                           17
Driver Board PCB Component Locations

PA-AE00301L-002, 3.5HP / 110V


    Connection to
    Console STD control
                                       Incline Motor
                                       UP
                                       COM
                                       DOWN
    Reed Switch Sensor




    Incline Motor VR                   AC Fan




    DC Drive Motor M+
                                       AC Input
                                       N
                                       L

    DC Drive Motor M-




                                                       18
Transfer PCB board of Console Back




                                     HDMI cable
 Safety Key (3 PINS)


                                     Coaxial cable

 STD control (4 PINS)

                                     KEYBOARD+RF
                                     (10 PINS)
 STD control (6 PINS)


                                     Audio (4 PINS)
HAND-RIGHT (3 PINS)


                                     C-Safe (5 PINS)

 HAND-LEFT (4 PINS)

                                     Fan (2 PINS)




                                                       19
The Console Keypad PCB Board

AB0054-K1 Front of the board


        Safety Key (3 PINS)    KEYBOARD+RF
                               (10 PINS)
                Safety Key     RF (3 PINS)




                                             20
The console POWER BRIDGE PCB board




                                     AC_L (Converter End)
          STD control
         (6+2+2 Pins)

                                     AC_N (Converter End)



                                     AC_N (Driver Board End)

        DC_13V/4A
     (Converter End)                 AC_N (Filter End)



                                     AC_L (Driver Board End)



           STD control               AC_L (Filter End)
    (Drive Board End)




                                                               21
The console HDMI/Coaxial cable/C-SAFE PCB board




                        Coaxial             HDMI    C-SAFE
                        Cable               Cable   (5 PINS)




                                                               22
The console Converter PCB board




              DC_13V/4A           AC_N
          (Converter End)         (Converter End)


                                  AC_L
                                  (Converter End)




                                                    23
The console mast Cable place

Putting the wire (HDMI/Coaxial cable/C-SAFE) in the groove during installation




                                                                                 24
The console back cover transfer PCB board pin define

BLE RECEVER Connector：
          P-No        P1         P2       P3       P4      P5        P6
       Description    N/C       GND      RXD      TXD     +3.3V   BLE_REST


C-Safe Connector：
           P-No         P1       P2       P3      P4       P5
        Description     RX       TX       9V      CTS     GND


USB Connector：
          P-No          P1       P2       P3       P4
       Description     +5V     USB_DM   USB_DP    GND


HAND Connector：
           P-No         P1       P2       P3       P4
        Description   HAND_R    COM      COM     HAND_L


Keypad Connector：
          P-No          P1       P2       P3       P4      P5       P6        P7
       Description    SCAN1     KEY1     KEY2     KEY3    KEY4     KEY5      KEY6


Safety Connector：
           P-No         P1       P2       P2
        Description    +12v      X       S/W




                                                                                    25
RM6T3 Main Connector(for ST8600-YT058)：
           P-No          P1          P2       P3        P4      P5     P6
        Description     DX+          DX-     GND       WK_UP   +12V   GND


ESP Connector(for ST8600-YT058)：
          P-No           P1           P2
       Description      +12V         S/W


STD Main Connector(for ST8600-YT057)：
          P-No           P1           P2      P3        P4      P5     P6
       Description      GND           RX      TX       +12V    S/W    SWD


RF Connector：
          P-No          P1           P2       P3
       Description     GND           5V    PULSE2_IN


DC FAN Connector：
          P-No          P1           P2       P3        P4
       Description     +12v         +12V     GND       GND




                                                                            26
7. Product Safety Instructions




                                 27
Important Safety Instructions

  - To reduce the risk of electric shock disconnects your treadmill from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 120-volt, 20-amp grounded
  outlet with only the treadmill plugged into the circuit.
  - Do not use an extension cord unless it is a 14 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
  improper adapters or in any way modify the cord outlet.




Important Electrical Instructions

  - NEVER use a RCD - Residual Current Device (U.S. ver.= GFCI) - wall outlet with this treadmill. As with any appliance with a large motor, the RCD/GFCI will trip
  often. Route the power mains cord away from any moving part of the treadmill including the elevation mechanism and transport wheels.
  - NEVER remove any cover without first disconnecting AC power. If voltage varies by ten percent (10%) or more, the performance of your treadmill may be
  affected. Such conditions are not covered under your warranty. If you suspect the voltage is low, contact your local power company or a licensed electrician
  for proper testing.
  -NEVER expose this treadmill to rain or moisture. This product is NOT designed for use outdoors, near a pool or spa, or in any other high humidity
  environment. The temperature specification is 40 degrees c, and humidity is 95%, non-condensing (no water drops forming on surfaces).
  - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is first turned on or even during
  use. If your treadmill is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill itself does not
  trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture have no ability
  to control. This part is available through most electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part #
  QO120HM.




                                                                                                                                                                        28
Important Grounding Instructions

  - This product must be grounded. If the exercise bike fails or malfunctions, grounding can provide a path of least resistance for current, thereby reducing the
  risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an appropriate outlet that is
  properly installed and grounded in accordance with all local codes and ordinances.

  - DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or serviceman
  if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the outlet; have a proper
  outlet installed by a qualified electrician.
  This product is for use on a nominal 230-volt circuit, and has a grounding plug that looks like the plug illustrated below. A temporary adapter that looks like the
  adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly grounded outlet is not available.
  The temporary adapter should be used only until a properly grounded outlet, (shown below) can be installed by a qualified electrician. The green-colored rigid
  earplug, or the like, extending from the adapter, must be connected to a permanent ground such as a properly grounded outlet box cover. Whenever the
  adapter is used, it must be held in place by a metal screw.




                                                                                                                                                                        29
8. Error Messages /
 Troubleshooting




                      30
8-1 Error code items

      Error Message        Cause                                                Troubleshooting
      E1                   Drive motor didn’t send output signal during         Check all the wires which from Drive motor connect well.
                           workout.
      E2                   Drive motor current is overload to trigger the       Check the situation of Running Belt and Deck; try to apply Lube
                           protection of Driver Board.                          between Running Belt and Running Deck.
      E3                   Incline motor did not work correctly.                To do the Calibration Procedure and check Incline motor wires
                                                                                connection.
      E4                   Drive motor input voltage is abnormal or the         Check all wires are connecting well and not damaged.
                           connection of Drive motor wires is not well.
      E5                   The connection between Console and Driver Board is   Check all wires are connecting well and not damaged.
                           interrupted or abnormal.
      E6                   Driver Board is defective.                           Check all wires are connecting well and not damaged.

      E7                   The AC input voltage is abnormal.                    Check whether the wall socket provides a stable voltage of about
                                                                                100~120V.
      Replace Safety Key   Safety key is not inserted.                          Insert Safety key back.

      SAFETY LOCK          Children's Safety mode is on.                        Press and hold Incline▲ key to relieve this mode.




                                                                                                                                                   31
8-2 Prepare tools




                    Picture    Tool name




                              Multi-meter




                                            32
8-3 Error Message: E3

Definition
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” E3” appears on the display.


Configuration                                                                         Troubleshooting




                                                                                        Part                 Troubleshooting
                                                                                                             1. Reconnect VR wires.
                                                                                        Incline VR           2. Inspect whether the incline wires are broken or
                                                                                                             disconnected.
                                                                                                             1. Inspect the incline wire and console cable
                                                                                                             connections.
                                                                                        Display board
                                                                                                             2. Test whether the VR voltage varies at the incline wire
                                                                                                             terminal.
                                                                                                             1. Inspect the wire connections.
                                                                                        Console cable        2. Inspect whether wires are broken or crimped.
                                                                                                             3. Replace the wires and test again.
                                                                                        Incline              Inspect the display board console cable connections.




                                                                                                                                                                         33
8-4 Error Message: Incline Err

Definition
During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.


Configuration                                                                        Troubleshooting




                                                                                       Part            Troubleshooting
                                                                                                       1. Press incline UP key. The driver board UP RELAY action.
                                                                                                       2. Press incline DOWN key. The driver board DOWN RELAY
                                                                                       Display board
                                                                                                       action.
                                                                                                       3. If not as above, inspect the cable and connections.
                                                                                                       1. Inspect whether the console cable is connected well.
                                                                                       console cable
                                                                                                       2. Test by replacing the cable with a good one.
                                                                                                       Inspect whether the driver board UP/DOWN REALY is
                                                                                                       action.
                                                                                       Driver board    1. Press incline UP or DOWN key again, making the incline
                                                                                                       motor return to its position.
                                                                                                       2. If ERR still appears, re-calibrate the incline set.
                                                                                                       1. Inspect whether the incline motor is stuck.
                                                                                                       2. Inspect whether the incline gears are cracked.
                                                                                       Incline motor
                                                                                                       3. Test whether the incline motor has a broken circuit.
                                                                                                       4. Re-calibrate the incline set.




                                                                                                                                                                    34
8-5 Circuit Diagram




                      35
8-6 Troubleshooting procedure matrix

                      Condition                                                       Reason                                                                  Solve
When turn on power, ON/OFF switch isn’t lit.            1 Power cord isn’t plugged into outlet.                           1 Plug the power cord into outlet.
                                                        2 Power cord isn’t plug into unit.                                2 Plug the power cord into unit.
                                                        3 The voltage of outlet is too low.                               3 Check the voltage of outlet.
                                                        4 Plug or connector of power cord is open.                        4 Replace power cord.
                                                        5 Connector of power cord is broken.                              5 Replace power cord.
                                                        6 Connecting cable disconnected.                                  6 Check if wire is disconnected, connect it again.
                                                        7 Breaker tripped.                                                7 Press the small red button to return to original status.
                                                        8 Breaker is broken.                                              8 Replace breaker.
                                                        9 ON/OFF switch is broken.                                        9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown broken on controller.   1 Check the voltage of power is 120V. Replace controller.
When insert safe key, no display on monitor.            1 Haven’t switch ON/OFF switch.                                   1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.                          2 Insert the safe key on right position.
                                                        3 console connector not plugged in properly.                      3 Please check the wire and connect again.
                                                        4 console cable is broken.                                        4 Replace console cable.
                                                        5 Fuse on controller is blown.                                    5 Replace fuse or controller.
                                                        6 Visitor on controller is blown.                                 6 Replace visitor or controller.
                                                        7 Safety device is broken. (open)                                 7 Replace safety key device.
                                                        8 Other components are faulty.                                    8 Replace console.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)                                1 Replace the safety key device or console.
When press “START”, treadmill doesn’t start.            1 Motor wire isn’t connected into right position.                 1 Please check and plug again.
                                                        2 Motor is broken.
                                                        3 Treadmill controller shut down and TFT would be ON.             2 Replace motor or check the wire and connector if it was broken.
                                                                                                                          3 Turn off the AC switch and turn on power again.
Treadmill stops or shuts off by itself.                 1 House breaker tripped.                                          1. Reset it.
                                                        2 Treadmill breaker tripped.                                      2. Reset treadmill breaker.
                                                        3 Treadmill controller fuse is broken.                            3. Replace with new fuse
                                                        4 Treadmill controller shut down and TFT would be ON.             4. Turn off the AC switch and turn on power again.

After removing safe key, treadmill can’t stop.          1. The safety key device is broken.                               1. Replace with new safety key device.
TFT not bright, incomplete or imperfect.                1. TFT light is broken.                                           1. Replace with new TFT or console.
                                                        2. Power to console too low.                                      2. Check AC power is 120V.
                                                                                                                          3. Check power to console.
                                                                                                                          4. Replace lower controller.
TFT displays not bright, incomplete or imperfect.       1. TFT displays are broken.                                       1. Replace with new console.




                                                                                                                                                                                              36
The incline position doesn’t match console          1 Console is not calibrated.                                  1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “INCLINE ERR”. 1 Position sensor value of incline motor is wrong.            1 Turn off the AC switch and turn on power again.
                                                                                                                  2. Calibrate the monitor.
After pressing “START” button, the treadmill stops    1 Controller is broken.                                     1 Turn off the AC switch and turn on power again.
immediately.                                                                                                      2 Replace controller and calibrate it.
Erratic pulse display.                                1. Another chest belt in use around treadmill.              1. Check for other chest belt use around treadmill.
                                                      2. Other magnetic field disturbance.                        2. Change the position or direction of treadmill.
                                                      3. Receiver is broken.                                      3. Replace with new receiver.
After pressing “START” button, the treadmill stop     Controller was broken.                                      Replace with new controller and calibrate it.
Immediately.
FAST/SLOW button of SPEED ADJUSTMENT SWITCH           1 The connector of SPEED CABLE and CONSOLE not connected    1. Connect cables again.
can’t be used.                                        properly.
                                                      2 The connector of SPEED CABLE and SPEED ADJUSTMENT         2. Connect cables again.
                                                      SWITCH W/CABLE not connected properly.
                                                      3 The connector of SPEED CABLE or                           3. Connect cable again.
                                                      SPEED ADJUSTMENT SWITCH/W/CABLE is damaged.
                                                      4. Button of SPEED ADJUSTMENT SWITCH is broken.             4. Replace with new buttons.
                                                      5. The connector of SPEED CABLE or SPEED ADJUSTMENT         5. Replace with new cable.
                                                      SWITCH/W/CABLE is damaged.
                                                      6. The connector of SPEED CABLE or SPEED ADJUSTMENT         6. Replace with new cable.
                                                      SWITCH/W/CABLE is damaged.
Speed button just can press FAST, can’t press SLOW.

Speed button just can press SLOW, can’t press FAST.
UP/DOWN button of                                     1 The connector of INCLINE CABLE and CONSOLE not connected 1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used.              properly.
                                                      2. The connector of INCLINE CABLE and INCLINE ADJUSTMENT 2. Connect the wires again.
                                                      SWITCH W/CABLE not connected properly.
Incline button just can press UP, can’t press DOWN.   3. The connector of INCLINE CABLE or INCLINE ADJUSTMENT    3. Replace the cable.
Incline button just can press DOWN, can’t press UP.   SWITCH CABLE got damage.
                                                      4. Button of INCLINE ADJUSTMENT SWITCH is broken.          4. Replace buttons.
                                                      5. The connector of INCLINE CABLE or INCLINE ADJUSTMENT    5. Replace the cable.
                                                      SWITCH CABLE got damage.
                                                      6. The connector of INCLINE CABLE or INCLINE ADJUSTMENT    6. Replace the cable.
                                                      SWITCH CABLE damaged.
Hand pulse lost its function.                         1. Hands not on the hand pulse sensors or only one hand on 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                       sensor.
                                                      2. The connector of HANDPULSE W/WIRE and Console not       2. Connect the cable again.
                                                      connected properly.



                                                                                                                                                                        37
                                               3. The wires got damaged when connecting the HANDPULSE   3. Replace with new cable.
                                               W/WIRE and Console.
                                               4. Hand pulse board is broken.                           4. Replace console or Hand pulse board.
Wireless lost its function.                    1. Chest belt not worn properly.                         1. Check chest belt has proper contact with skin and is oriented correctly.
(No pulse displayed on monitor)                 2. Distance is too far and exceeds range of receiver.   2. User chest belt in front of console within 3 feet.
                                                3. Chest belt battery is weak or dead.                  3. Replace with new lithium battery type is CR2032.
Chest belt too close to the treadmill.         Weak battery.                                            Replace with new lithium battery with type CR2032.
Tread belt does not run in center.             Tread belt tension not even across tread belt.           See treadmill belt adjustment
Tread belt hesitates while being stepped on.   Insufficient lubricant on tread belt.                    See treadmill belt lubrication
                                               Tread belt tension insufficient
Black particles collecting under treadmill.    Drive belt is breaking in.                               Vacuum under treadmill periodically.
Noise under motor cover.                       1. Worn brushes or bearings on motor.                    1. Replace with new motor.
                                               2. Front roller bearings are defective.                  2. Replace with new front roller.
                                               3. Drive belt is misadjusted (too tight or too loose).   3. Adjust motor position.
Noise in the rear of the treadmill.            1. Rear roller bearings are defective.                   1. Replace with new rear roller.
                                               2. Rear roller misaligned.                               2. Adjust rear roller position.




                                                                                                                                                                                      38
8-7 Troubleshooting
  Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common problems
  that may not be covered under the treadmill’s warranty.
                       PROBLEM                                                                    SOLUTION/CAUSE
  Display does not light                                          1) Tether cord not in position.
                                                                  2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                                                  3) Plug is disconnected. Make sure plug is firmly pushed into 120 VAC wall outlet.
                                                                  4) Breaker panel circuit breaker may be tripped.
                                                                  5) Treadmill defect. Contact your dealer.
  Running belt does not stay centered                             The user may be walking while favoring or putting more weight on either the left or right foot. If this walking pattern
                                                                  is natural, track the belt slightly off-center to the side opposite from the belt movement.

  Treadmill belt hesitates when walked/run on                     See General Maintenance section on running belt Tension. Adjust as necessary.
  Motor is not responsive after pressing start                    Reset power. If still no good contact service.
  Treadmill will only achieve approximately 7mph                  This indicates motor should be receiving power to operate. Do not use an extension cord. If an extension cord is
  /10 kph but shows higher speed on display                       required it should be as short as possible and heavy duty 16-gauge minimum, low voltage. Contact an electrician or
                                                                  your dealer. A minimum of 100 volt AC current is required.
  Treadmill trips on board 20 amp circuit                         High belt/ deck friction. See General Maintenance section on cleaning the deck. If cleaning doesn't prevent this from
                                                                  reoccurring, check to see if there is significant wear of the deck. If so, the deck may need to be flipped if it is on its
                                                                  original side.
  Computer shuts off when console is                              Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to Grounding Instructions
  touched (on a cold day) while walking/running
  Circuit breaker trips, but not the treadmill circuit breaker.   Need to replace the house breaker with a “High inrush current” type breaker.




                                                                                                                                                                                               39
8-8 Engineering Mode Instructions

Home
Click on the Home icon at the top of the main page center 10 times to enter a total of 7 sub-menu modes on the setting page.




                                                                                                                               40
Engineering Mode Settings

                Items                 Description
                Engineering Mode      Set the Speed and Incline
                Security              Set Lock Accumulate mileage.
                Diagnostics           The Error Diagnostics
                Machine Information   Set Machine Type, GS Mode, Touch sound, Sleep Mode ,Safety Mode, Zero mileage.
                Maintenance           Set default language ,WiFi , Etherent, Bluetooth, USB update, update OS.
                A / V Source Setup    Set audio/visual source.
                Lube Setup            Set Lube Suggest.




                                                                                                                       41
Engineering Mode
  Set the Speed and Incline：
  1. The default Speed is Minimum 0.5(mi/hr) - Maximum 12.0 (mi/hr).
  2. The default Incline is 15 level ,Wheel size is 2.98.
  3. Click on the calibration to start setting.




                                                                       42
Security
   Set Lock Accumulate mileage：
   1. Set a four-digit number password and the number of kilometers you want to lock.
   2. Can use the set password to unlock or use the password 2222 to unlock.




                                                                                        43
Diagnostics




              44
Machine Information
  Set Machine type ,GS Mode, Beep Mode, Sleep Mode ,Safety Mode, Zero mileage：
  1. GS Mode：The default is OFF.
  2. Beep Mode：Touch sound, the default is ON
  3. Sleep Mode：The default is OFF. When set ON, the electronic watch will go to sleep without any operation within 30 minutes. Press any key to wake up during
  sleep.
  4. Safety Mode：The default is OFF.
  5. Zeroing：Click on this key to clear all mileage.




                                                                                                                                                                  45
Maintenance
Set default language, Wi-Fi, Ethernet, Bluetooth, USB update, update OS




                                                                          46
Maintenance - Default language Setup
Choose a language as the starting language.




                                              47
Maintenance - Set default Wi-Fi
When Wi-Fi is set to on, select a connectable network link.




                                                              48
Maintenance - Set default Ethernet
Choose a wired Ethernet connection.




                                      49
Maintenance - Set default Bluetooth
When Bluetooth is set to On, select a connectable network link.




                                                                  50
A/V Source Setup
The CAB mode is an external TV box (HDMI) channel selection / the C-SAFE mode is an infrared interface.




                                                                                                          51
Lube Setup
Set Lube Suggest, the default is 4000Hrs




                                           52
9. Disassembling and
     Assembling



                       53
9-1 Lower Controller replacement                                                  9-2 Console replacement

Step 1: Use a screwdriver to remove the Motor Base Cap (L) and (R), then remove   Step 1: Use M8 L Allen wrench to remove 8 bolts of Locking Plate(R) and (L).
the Motor Top Cover.                                                              Step 2: Disconnect console wirings and replace with new console.




Step 2: Disconnect all lower controller wirings
Step 3: Use Phillips head Screwdriver to remove and replace with new lower
controller and reconnect all wirings.




                                                                                                                                                                 54
9-3 Drive Motor replacement
Step 1: Use a screwdriver to remove the Motor Base Cap (L) and (R) then remove   Step 3: Use M8 L Allen Wrench to remove 4 motor locking bolts under the
the Motor Top Cover.                                                             treadmill.




Step 2: Remove motor grounding wire (green yellow) and computer cables (U, V,    Step 4: Replace the motor with new one after removing the motor belt, then
W) and use 14mm open end wrench tension screw and M8 L-shape Allen wrench        resume parts in reverse order, including the motor belt. (Make sure that the belt
to release motor adjusting bolts.                                                is parallel to the frame), not to tighten 4 bolts temporarily.




                                                                                                                                                                55
                                                                                 9-4 AC Power Switch replacement
Step 5: Use 14mm open end wrench to adjust the belt tension with tension gauge   Step 1: Use Phillips head screwdriver to remove the front cover (7 tapping screws)
until the Tension reads with white range between 70~75 Lbs. Then use M8          and also remove AC input module cables. Use again the Phillips head screwdriver
L-shape Allen wrench to tighten 4 motor adjusting bolts to secure.               to remove overload protective device. Resume cable connections all parts in
                                                                                 reverse order after replacement.




Step 6: Connect the grounding wire and computer cable back.




                                                                                                                                                                56
9-5 Front / Rear Roller replacement

Step 1: Use a screwdriver to release 2 screws of rear roller end Caps and remove   Step 3: Use a screwdriver to remove the Motor Base Cap (L) and (R) then remove
end caps.                                                                          the Motor Top Cover. Then use 14mm open end wrench tension screw and M8
                                                                                   L-shape Allen wrench to release motor adjusting bolts and 4 motor locking bolts
                                                                                   under the treadmill. Then loose the drive belt.
                                                                                   Step 4: Use M8 L-shape Allen wrench to release the front roller screw and remove
                                                                                   the front roller. Replace with new front and rear rollers and resume all parts with
                                                                                   reverse order.
                                                                                   Step 5: Adjust the belt tension and run the belt in the center. Refer to step 11.3 (5)
                                                                                   for adjusting the belt tension.



Step 2: Use M8 L-shape Allen wrench to two screws for rear rollers and remove
the roller.




                                                                                                                                                                     57
9-6 Running Deck/ Belt & Cushion replacement

Step 1: Follow the step of front and rear roller replacement to remove both of the   Step 3: Use M6 L-shape Allen wrench to release 6pcs of Socket Head Cap Bolts for
rollers.                                                                             cushions and remove them together with Deck Cross Brace, as shown in figure
                                                                                     below.




Step 2: Use M6 L-shape Allen wrench to release 8pcs of Socket Head Cap Bolts
and remove step rails as shown in the figure below. Release 8pcs of Flat Head
Countersink Bolts and remove both deck and the belt as shown in the figure
below.




                                                                                     Step 4: Replace with new deck, belt and cushions and return all parts with reverse
                                                                                     order.




                                                                                                                                                                    58
9-7 Incline Motor replacement

※Zeroing the incline motor before take it apart from the machine or assemble it
onto the frame. The zeroing distance is 235mm.
Step 1: Use Phillips head screwdriver to release screws and remove left and right
motor base caps and motor top cover. Turn the treadmill to stand on one side and
remove cables connected on the lower controller connecting to the incline motor
then remove the incline motor with 17mm open end wrench.




Step 2: Use 17mm open end wrench to install new incline motor and resume all
cable connections.




                                                                                    59
10. Q&A




          60
10-1 The Console and Error Messages                                          10-2 Belt Slipping and Falling-off

Screen did not show anything. Please follow below steps to check:            Belt slipping:
Step 1: Check the connection of computer cables.                             Follow the steps of 9-5. Left and Right Shrouds replacement to remove both
                                                                             shrouds.
                                                                             Check the tension of drive belt with a sonic belt tension meter, the value must be
                                                                             250±50HZ.
                                                                             If the value is not right in the range then the spring or belt may loose needs
                                                                             replacement.



Step 2: Check Power adapter connector is fully insert DC socket of Bike.
Step 3: Check Power adapter output voltage is the same as its label shows.
No heart rate showing when using hand pulse. Please follow below steps to
check:
Step 1: Check hand pulse wires connection from it to console.
                                                                             Because Drive belt is consumable, it is normal for long-term use to loosen.

                                                                             Belt Falling-off:
                                                                             When encountering Drive belt falling-off, follow the steps of 9. Disassembling and
                                                                             Assembling to mount drive belt back then rotate the drive pulley forward and
                                                                             backward to ensure Drive belt won’t fall off.
                                                                             If the drive belt keeps falling off, it is possible that the bike dropped during
                                                                             transportation and caused some parts to be misaligned. The drive pulley, idle
                                                                             wheel assembly, flywheel, and mainframe need to be checked to see which part
                                                                             is defective and require replacement.




                                                                                                                                                              61
10-3 Noises problem

Unsecured assembly bolts are the main reason. For other reasons, some parts are     3. Noise inside the bike. To remove both side of Shroud, then check the noise is
deformed or position shifted.                                                       from which part. The most reason is drive pulley friction the front of right shroud.
We list some possibilities:                                                         To replace drive pulley or add some form tape on the shroud to make a gap
1. The noise from pedal. The pedal is a consumable item, and it will wear out and   between pulley and shroud can repair it.
cause noise after long-term use. To replace pedals when they are making noises.




2. The noise from crank. Sometimes Crank may loose and start to make noise
after long-term use. To tighten crank locking nut can fix the noise.




                                                                                                                                                                     62


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
IONUDW SdIAIOS

‘JOA OZOZ

LNA 008L9


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 79 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Table of Contents

OUTINGS... ee eeceeesecssecsseeesseceseceeessaeceseceseecsaecsseceseessaeceaeceseessaeceaeeeseessceceaeceseesscecsaeceseesscecesecestesceceaeceseeeseeceaeceseeesceceaeceaeessceceaeceaeeesceceseceaeeeeeceaeceseceeeceaeceaeeeeeseaeesas 4
 EI@CTFONIC POTS... eeeceesneceseeescecsseceseessneceaecescecsceceseceseeccecsseceseecaecsaeceseecsaecsaeceeeceseceseceseecssecsseesceceneceseescecaecessessaeceaecestesececsaeceaeesedeceaeceseeseseceseceeeseaeceaeceeesaeeeas 6
~ PFOCUCT OPESAHON ooo... eecccccccccssscccessscecesesseeceesssaeecesesaeeeeeesseeeeeeesaeeeeeesaeeeeeeaaeeeeesaeeeeeesaeeeeeesaaeeeeesaeeeeeesaeeeeeesaaeeeeeaaeeeeeesaeeeeeesaeeeeeessaeeceeesaeecesesaeeceeesseeceseaaeeeeenaes 11
EUMIT BIOCK DIGGIN .......eeeecccccssscccesessceceseseeceesssseeeeeesseeeeeeaeeeeeeesaeeeeeesaeeeeeesaaeeeeeaaeeeeeesaeeeeeesaaeeeeeaaeeeeeesaeeeeeesaaeeeeeaseeeeeesaeeeeeesaeeeceessaeeceeesaeeceeessaeeceeesseeceseaaeseeenaas 15
~ BASIC CONNECTIONS CAIN WING ......cccccccccssscccesssseccesesseeccsesseeceeesseeecesesaeeeeeesaaeeeeesseeeeeesaeeeeeesaeeeeeesaeeeeeesaeeeeeesaeeeeeeesaeeeeeesaeeeeeesaeeeceesaeecesesaeecesesaaeseceesaeecesesaaeeeeenaas 17
. PrOCUCT SAFETY INSTTUCTIONS oo... ccccccsscccssssscceesssseeceseseeceseseeseeeeseeeceeesaeeeeeesaaeeeeesaeeeeeesaeeeeeesaeeeeeessaeeeeeesaeeeeeesaeeeeeesaeeeeeesaeeceeesseeeceesaeeceeesaeecesessseecceesseecesesaaeeeeenaas 27
Error MESSAGES / TTOUDICSNOOTING .o.....cececccccesssscccesssseecesesseeceeesseeecesesaeeeeeeseeeeeeesaeeeeeesaeeeeeeaseeeeeesaeeeeeesaeeeeeesaeeeeeesseeeeeesaeeeeeesaeeeceessaeeceeesaeeceseaaeecesesseecesesaaeeeeenaas 30
8-1 Error COE ITEMS ues eeeeeeseceseeessecesecseecsnecesecescecsaecsaeesseecsnecsseesaecaeceseessceceaeceaeessceceseceaeesceceaeceseessceceaecessesceceseceaeecaeceseeeseeceaeceaeeeeeceaeceaeeeseeseaeceaeeeteeeeaeeeaeees 31
[ad >) O10 | fos (010) cess 32
8-3 ErrOr MESSAGE: ES ....ceccccccccccccessssssseeeeeecesseeesseeeeeeeeeeeseesseeeeeeeeeeseeesaeeeeeeeeeeeesaaGeeeeeeeeeseeaaGGeeeeeeeeseesaGGGGeeeeeeeeesAGGGGGSGC;SESEEAGGEEGESSSSEASEA;;;EEESEEeseeesG;;;EEEESeEEEeEAEGOEES 33
8-4 Error MESSAGE? INCIING Et oo. eeecesecccssssscceesssseecesesseecesesseeseeesseeeeeeesseeeeeesaeeeeeeaeeeeeeeseeeeeeesaeeeeeesaeeeeeeaaeeeeesaeeeeeesaeeeeeesaeeeeeeaeeeeeessaeeeceesaeecesessaeeceeesaeecesesaeeeeses 34
8-5 CirCUIT DIA QLOIM ....ceccccssscccesssscccesesseecesesseeeeeseseeecesesseeeeeesaeeeeeeseeeeeeesaeeeeeesaeeeeeesaaeeeeeaGeeeeeesaeeeeeesaeeeeeesaGeeeeesaeeeeeesaeeeeeesaeeeeeeaaeeeesesaeeeceesaeecesesaaeeceeesaeecesesaeeeeses 35
8-6 TTOUBIESNOOTING PFOCE CULE MAM IX .....c.ccceccesscccesesseccesesscecceesseeeeessseeceeeaeeeeeeeseeeeeeeseeeeeeesaeeeeeesaeeeeeeaaeeeeeesaeeeeeesaeeeeeesaeeeeeesaeeeceeesaeeseeesaeeceeessaeecesesaeecesesaaeeeses 36
8-7 TTOUBDIGSNOOTING........ccccsscccesssscccesesseecesessseeeeseseeecesesseeeeeeaeeeeeeseeeeeeesseeeeeesaeeeeeesaGeeeeeaGeeeeeesaeeeeeesaeeeeeesaGeeeeeaaeeeeeesaeeeeeesaaeeeeesaaeecesesaeeeeeesaeeecsesseeeceeesaeecesesaeeseses 39
8-8 ENGINEETING MOCE INSTTUCTIONS ........ccccssscccesssscccesesseecesesseeceesssseeeesssaeeeeeeaeeeeeesaeeeeeeseeeeeeesaeeeeeesaeeeeeesaaeeeeesaaeeeeeesaeeeeeesaaeeeeeaaeeeeeesaeeceeesaeecesesaaeeceeesaeecesesaeeseses 40
HOME... .scccesscccesscecsseeceseecesacecsseecesacecssacecsaeeescecesaeecsaeessscecssaeecsaeessseecesaeecsaeecsseecesacecsaeecsseecesaeecsaeecssaecesacecsaeecssaecesaeeceeaeecssaecesaeeceeacesssaeessaeesenatecsaeeeeaeecsuas 40
ENGINEETING MOCE SETTINGS ......ccccccccsssscccesesseeceeessceeeesssaeeceeesaeeeceesseeeeeeesaeeeeeesaeeeeeeaaeeeeeesaeeeeeesaeeeeeesaeeeeeeaaeeeeeesaeeeeeesaaeeeeessaeeeeeesaeecesesaaeceeesaseeceeaaeeeeeesaeeeeses Al
ENGINE ESTING MOE 1... .cccccccscssscccesssscecesssseeceeesaeeceessseeeceseaeeeeeesaeeeeeesseeeeeeesaeeeeeesaeeeeeesaaeeeeeaaeeeeeesaeeeeeesaeeeeeesaeeeeeesaeeeeeesaaeeeeesaaeeeeeesaeeccessaeceeesaseeceeeaaeeceeesaaeeeses 42

NY> 1010] 11h Ae ese 43
DICIQNOSTICS .oo..eeeccsscccesssseccesessceceessseeeeesssseeeeeesseeeeeesseeeesesseeeeeesaeeeeeesaeeeeeesaeeeeeesaeeeeeesaaeeeeesaGeeeeeesaeeeeeesaeeeeeeaGeeeeeaaeeeeeesaeeeeeessaeeceeesaeeceeesaaeseeesaseecesesaeeceeesaeesenes 44
MACHINE INFOMATION 0... eescceseesteceseeesceesseceseeescecsceceaeceseessaeceaeceseecsaeceaeceseecsceceaecetecsceceaeceseesaeceseceseessaeceseceaeessceceseceateseeeceseceseeseeceseceaeeeaeceaeceaeeeeeeseaeseaeees A5
MAINTENANCE oe eeesccsseeessecsceescecssecesecescecsaecssecescecscecsaeceseesaeceaeceseecceceseceseecsaeceseceseeesceceseceseeceaecaecescesseeceaeceaeessceceseceseeseaeceseceseeseeceseceaeeceeceaeceaeeeeeeseaeseaeees 46
MAINTENANCEY - DEFAUITIANQUAGE SETUP uc ccccccccccsssscccesesseeceesssseecesesseeceeesseeeeesesaeecesesaeeeeeeesseeeeeesseeeesesaeeseeeaseeceeesaeecesesaeeeccesaaeecesesaeecesesaaeeeeeesaeees 47
Maintenance - Set GEFAUIT Wi-Fi... ee eeeceeseceseceseeesseceseesscecsneceseceseecsaecsseeeseeceaecsaeesscecsaeceseessceceaeceaeesscecsaeeeseesceceseceaeesececeseseaeesceceaeceeeseaeceaeeeeeseaeesas 48


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Maintenance - Set de
Maintenance - Set de

A/V Source SeTUP ...... eee

LUDE SETUP oo. cccceeeeeees

9. Disassembling and Assembling
9-1 Lower Controller replacem
9-2 Console replacemer........
9-3 Drive Motor replacement..

9-4 AC Power Switch replacement
9-5 Front / Rear Roller replacement

9-6 Running Deck/ Belt & Cush
9-7 Incline Motor replacement

10-1 The Console and Error Me
10-2 Belt Slipping and Falling-o
10-3 Noises problem ..............06.

fault Ethernet

ION FEPIACEIMEN .....ceccccesscccesssscccesesseecceesseeecesssseecesesaeeeeeessaeeeeeesaeeeeeeesaeeeeeesaeeeeeesaeeeeeessaeeceeesaeeeeeesaeeeceesaeecceesaeeeeeeeseeeeeeesaeeeeees
SSOQES .oeecescccsscessccsssceseceseeessecsseeeseeceseceseesseeessecsseeseeesseceseeeseecesecsseesseeceseceseesseeceseceseesseeceseceseessaesseceseesseesessceseceseeseseceseeeeeenseengs
PE ee eececesecssscssccesseceseceseeeseecsssceseeeeeceseceseesseecesecsseessssceseceseecseeceseesseeessecesecsseeesseceseesseecsssceseeeseeeseceseeeseeeeseceseeeseeceseceseeseeeeseeeseees

fault Bluetooth

ent


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
oO >

fe) or

omy | a

= 5

fo} O

oO o

0)

5 BY Q oO

fo 6 oO 5
—

O = < ©

Q U ~ mm

9 a eo
< Ss

c
=
5 = a) =! s
< S 2 R 3D
5 oO QO ~ w
© = O @ o.
= @ a = °
> a s oF
o) oO °
o) iy —-
as © io}
ol
2 O


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
= faa ”
Q O Ye Ke)
e) = InN ae —_
© £ OZ re) o&
S 3 ao a) fe)
a Oo fy CO D I
r O Va < O

(Za) (Za) NY (Za) (Za)
Zz Zz Zz Zz Zz
a a ja a a
o =x <2 o =x
~ > > Ee b—
® £ g x th
> 5 ; w A
[a4
i) O O a O
ie a) a) Z <
” a D < =


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
The Console Keypad PCB Board

AB0054-K1 Front of the board

Safety Key (3 PINS)

Safety Key

=

Ro) AB0054— K1-V1L0

—20200313

ea \e “”

SAFETY @@ @@SAFETY- 5x1 KEYBOARD @

=)
|
JK: j

=

|

@)

a {__

2

ned

KEYBOARD+RF
(10 PINS)

RF (3 PINS)

20


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
—~ => c Cc

xe) xe) LU Lo

Cc c Oo

LW Lu fu ze)

oa (e) — oO

2 = Q re) O o
O © ~ Wu = Lu
> = oO ro ©

c = > O S D
O O = = = 4
O O a iz fa) it
, Z 4 4 a a"
O O O O

< x < < < <

5 2 $3 ©

Ca > OG €
O ZS O
Oo Q = 9 O

ae ay (a)
+ O oO

Do Aa > D


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
The console HDMI/Coaxial cable/C-SAFE PCB board

AC0044—K1—V1.0—200116

Coaxial HDMI
Cable Cable

Ciek

C-SAFE
(5 PINS)

fs
YA

22


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
suoi}onij}suy Ajajes JONPOId "2


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
43

Ja aW-l NA

SQUIDU [OO]

SIND

SJOOL SIDASIlg 7-8


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-3 Error Message: E3

Definition
The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” E3” appears on the display.

Configuration Troubleshooting

Part Troubleshooting
1. Reconnect VR wires.

DISPLAY BOARD

Incline VR 2. Inspect whether the incline wires are broken or
disconnected.

1. Inspect the incline wire and console cable

connections.

INCLINI Display board
VR 2. Test whether the VR voltage varies at the incline wire
ee terminal.
1. Inspect the wire connections.
Console cable 2. Inspect whether wires are broken or crimped.
3. Replace the wires and test again.
INCLINE Incline Inspect the display board console cable connections.
MOTOR
DRIVER BOARD xx VR VOLTAGE INCLINE VR SET

© INCLINE DOWN RELAY

@) INCLINE UP RELAY

33


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-4 Error Message: Incline Err

Definition
During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Configuration Troubleshooting

Part

Troubleshooting

DISPLAY BOARD ° UPDOWNKEYS | uenown evs

Display board

console cable
INCLINE INCLINE

VR UP/DOWN
VOLTAGE SIGNAL
\
al Driver board
INCLINE
MOTOR
DRIVER BOARD < r LINE VR VOLTAGE INCLINE VR SET Incline motor
~

© INCLINE DOWN RELAY

1. Press incline UP key. The driver board UP RELAY action.
2. Press incline DOWN key. The driver board DOWN RELAY
action.

3. If not as above, inspect the cable and connections.

1. Inspect whether the console cable is connected well.

2. Test by replacing the cable with a good one.

Inspect whether the driver board UP/DOWN REALY is
action.

1. Press incline UP or DOWN key again, making the incline
motor return to its position.

2. If ERR still appears, re-calibrate the incline set.

1. Inspect whether the incline motor is stuck.

2. Inspect whether the incline gears are cracked.

3. Test whether the incline motor has a broken circuit.

4. Re-calibrate the incline set.

(©) INCLINE UP RELAY

34


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 72 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-5 Circuit Diagram

ui »

3 i i i
3 e 3 5
v4 Q fal v tL. 5
z Gnou6 yeoqueey BUPIOH Nid ¢ w -—2 8 a] E 9
S zZ v4 ra s E
S 2°55 5 ° % 0
3)
<{ 35! z SUM LH § z
& fh s au G3 . bi $

x a S Qa 3° Zz
a ° “I o JYIM MOV1E 5 & ing
= O z 2° Ww FIGVO UEINANOO SNMONI Nid= S 2 8 Z
oO <x - - aN yOVTE . 159 : g 0
l — ad 14 z
o) A = | zumaien A 3 E gla

Zz

LL. MIM aLIHM lan 3] 1 8 3 a

O55 u 00 wu =z) $| °° re
£0 |||_: ° | |g z <<] ar

0 t

14 ES 00 = 3 : © S

5

© Yo c i, ©
6° ,* |B $F JFhRe—
— 4 gE 8 rT
US Q ra = z| |-
Q Pra re) ws
< Les §$ Eliz :
LW dnou6 yeoqueey Sup} Nid ¢ 3 —— wy _ 8 < Nae 2
ow - ul & = z Oo O fe
- E ¥ ye | é 5 5
4
=> ap ° ° oO
so 6f (B a al

oO
2° F & ot a
< 8 8 Guy (MOA UM useiD}euN UeeID

és)


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-8 Engineering Mode Instructions

Home
Click on the Home icon at the top of the main page center 10 times to enter a total of 7 sub-menu modes on the setting page.

Home

Exercise
Programs

Entertainment Language

P QUICK START

AO


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Engineering Mode
Set the Speed and Incline :
1. The default Speed is Minimum 0.5(mi/hr) - Maximum 12.0 (mi/hr).
2. The default Incline is 15 level ,Wheel size is 2.98.
3. Click on the calibration to start setting.

Engineering Mode

Max. Incline

Wheel Size

Max. Speed

Min.Speed

Incline AD Value

Max. AD

Current AD

Min. AD

42


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Security
Set Lock Accumulate mileage :
1. Seta four-digit number password and the number of kilometers you want to lock.
2. | Canuse the set password to unlock or use the password 2222 to unlock.

Security

Lock Mode Set Lock Password to Activate

Set Lock Accumulate Mileage Confirm Set Lock Password to Activate

Mileage
100 - 990

43


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
‘}eEWOUge UOyedUNWWOZ

‘"adeUOA |eUsayxa |eEWIOUqY

‘“aBe1JOA JOJOW |eWJOUqY

"a3e}OA JeUa}xa |eEWUOUGY

‘}eEUOUge UOQedIUNWLWO?

‘}JeUSIS INdjNO JOJOW ON

30] eposy 41049

soysoubpig


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Machine Information
Set Machine type ,GS Mode, Beep Mode, Sleep Mode ,Safety Mode, Zero mileage :‘
1. GS Mode : The default is OFF.
2. Beep Mode : Touch sound, the default is ON
3. Sleep Mode : The default is OFF. When set ON, the electronic watch will go to sleep without any operation within 30 minutes. Press any key to wake up during
sleep.
4. Safety Mode : The default is OFF.
5. Zeroing : Click on this key to clear all mileage.

Machine Information

Machine Type Distance : 11.61 km

Hour: 1.16 hr

Beep Mode

Oo ow Oo SW Version : T29_ 20200312

Sleep Mode FW Version : V1.0

Safety Lock

OS Version: V1.0

A5


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 27 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
suysel did
SO aiepdn
ddy eiepdn

dnjes 1d

dnjyes }uas98u}3

dnyes 141M

dnjes esensue] ynejoq

SOUCUDIUIEI/

SO ajepdn ‘ayepdn gs ‘ujoojanyg ‘“yausayry ‘14-IAA ‘ABSensue] yNejJap jas
Ss ouDUSIUIDWw


=== OCR SUPPLEMENT, PDF PAGE 47 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
KUI90d

1S4ON lo=ig

spuejiapan sensnyod

ey) hs

ouelje}| sieSuel4

By yosinaq

joueds3 ysi|su

asensuey

‘asengue| 8uljejys ay} se adensu_e| e asooyuy
dnjes e6on6up| jInoJeq - SDUDUSJUIDW


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Maintenance - Set default Wi-Fi
When Wi-Fi is set to on, select a connectable network link.

. A sil-huawei

Va silviewtest24g

~.  RICOM

%.  STARMAX_107A

vs CMCC

LA ChinaNet-Skx2

LA haoyunlai

48


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 36 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6V

oophp

o’ssz'ssz'ssz
ssauppy 4SeIN

cSNG

L'L'B9L°Z6L
LSNQ

L'L’S9L°Z6L
Aenayed

6ZL LB9LZ6L
SSaJPPV dl

€4-40-00-VV- L-Zs
ssauppy DVI

Oju] PauUOD

SPOW d/ 2381S

ePOW ddHG

uo

yausay}y

‘UOIJIBUUOD JBUIIYIW Pam e asooyD
fJOUISULA {INDJOP {eS - SDUDUSIJUIDWZ


=== OCR SUPPLEMENT, PDF PAGE 50 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Maintenance - Set default Bluetooth
When Bluetooth is set to On, select a connectable network link.

Bluetooth

On

Paired Device

\  KIW-TLOO

Available Device

No Bluetooth device found nearby

After turning on the Bluetooth device on t3-p1, nearby devices will be able to detect the device.

50


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Lube Setup
Set Lube Suggest, the default is 4000Hrs

Lube Setup

Cumulative Distance : 11.61 km

Cumulative Time: 1.16 hr

Zeroing


=== OCR SUPPLEMENT, PDF PAGE 55 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9-3 Drive Motor replacement

Step 1: Use a screwdriver to remove the Motor Base Cap (L) and (R) then remove
the Motor Top Cover.

PELE OL

A

wcooogtlemd) F220
gS —J
li]
Step 2: Remove motor grounding wire (green yellow) and computer cables (U, V,

W) and use 14mm open end wrench tension screw and M8 L-shape Allen wrench
to release motor adjusting bolts.

Step 3: Use M8 L Allen Wrench to remove 4 motor locking bolts under the
treadmill.

=H

©
©

Step 4: Replace the motor with new one after removing the motor belt, then
resume parts in reverse order, including the motor belt. (Make sure that the belt
is parallel to the frame), not to tighten 4 bolts temporarily.

fet flesh

Vt imi

95


=== OCR SUPPLEMENT, PDF PAGE 59 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9-7 Incline Motor replacement

+ Zeroing the incline motor before take it apart from the machine or assemble it
onto the frame. The zeroing distance is 235mm.

Step 1: Use Phillips head screwdriver to release screws and remove left and right
motor base caps and motor top cover. Turn the treadmill to stand on one side and
remove cables connected on the lower controller connecting to the incline motor
then remove the incline motor with 17mm open end wrench.

48 -— - (to)

hol
ws Se SY
& ©

Step 2: Use 17mm open end wrench to install new incline motor and resume all
cable connections.

59
