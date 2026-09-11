<!-- Source: CT900ENT Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

     CT900 ENT
    Service Manual




1                    Service Manual
--------------------------------------------Table of Contents-------------------------------------------

                                 1. CT900 ENT Outlines
                                 2. Electronic Parts
                                 3. Electrical Configurations
                                 4. CT900 ENT Basic Connections and Wiring
                                 5. Product Safety Instructions
                                 6. ST8100 Error Messages / Troubleshooting
                                 7. General Maintenance
                                 8. Treadmill Folding/Unfolding and Transport
                                 9. General Maintenance
                                 10. Installation of the Incline Motor




                                                    2                                         Service Manual
1. CT900 ENT Outlines




          3             Service Manual
Console




          Hand
          Pulse




          4       Service Manual
                                   AC Motor
          Inverter       Incline
           Board          Motor

Lower
Control
Board




                     5                        Service Manual
2. Electronic Parts




         6            Service Manual
Upper Controllers
                        Cooling FAN




         DISPLAY



                                      Safety key




                    7                              Service Manual
Lower Controller and Driver




                                  INCLINE MOTOR
               AC MOTOR




                                      INVERTER




                              8                   Service Manual
3.Electrical Configurations




             9                Service Manual
SAFETY KEY:
 To fits on the Console that activate all functions. If no safety key, console can not be controlled.

CONSOLE:
 Interface that controls all functions of the Treadmill.

MAIN CONTROLLER:
 The circuit board consist of the AC power supply for console、incline driver and AC motor driver, link the console to output appropriate voltages for
 Incline Interface Board and inverter that control the Treadmill functions.

AC MOTOR:
 It can change to increase or decrease speed change.

INCLINE MOTOR:
 This is an ac motor. User can to control variable elevation by console within main controller.

GENERAL INFORMATION

CONSOLE
 Contains Key controls and TFT Display.

MAIN CONTROLLER
  Include power supply、AC motor、incline motor、inverter control circuit and incline control circuit.




                                                                          10                                                        Service Manual
AC MOTOR
   Work voltage:AC 120V~
   Control speed increases and decreases.

INCLINE MOTOR
 This is a 120 volt AC motor.
 Have four wires, red, black, white and green.
 Has one 3 pins cable of position sensor.
 If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
 If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
 The White wire (COM) is neutral.
 The green wire is ground.




                                                                          11                    Service Manual
4. CT900 ENT Basic Connections and Wiring




                    12                 Service Manual
I/O Board Bottom




                                                         Key Board
                   HDMI CONTACT                          CONNECT (24
                                                         PINS)
                                    N.A.




                                                                       SYSTEM CABLE
                         GROUND
                                                                       CONNECT (8
                                                                       PINS)




                       Internet   Console        TV CONNECT       C-safe CONNECT
                       CONNECT    Power
                                  CONNECT




                                            13                                        Service Manual
DRIVER BOARD PCB Component Locations




              VFD015TM12A


                  14                   Service Manual
Controller debugging
 Indicator           Function                     Condition                              Reason                                Solve
   LED
POWER      Controller power          If AC voltage is normal, it would be    Voltage is not correct.          Check the supply voltage is 110~120V.
                                     always ON. If off, fault condition      Fuse is blown.                   Replace Fuse.
                                     exists.                                 Transformer is no good.          Replace controller.
UP         Motion of incline motor   Motion of incline motor is up.          Transistor was broken.           Replace controller.
                                                                             Relay failed.
DOWN       Motion of incline motor   Motion of incline motor is down.        Transistor was broken.           Replace controller.
                                                                             Relay failed
START      START                     No execution start                      Check control cable plugged in   Replace controller.
FAST+      FAST                      No execution fast                       Check control cable plugged in   Replace controller.
SLOW+      SLOW                      No execution slow                       Check control cable plugged in   Replace controller.




                                                                        15                                                             Service Manual
5. Product Safety Instructions




              16                 Service Manual
Important Safety Instructions
  - To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 120-volt, 20-amp
    grounded outlet with only the treadmill plugged into the circuit.
  - Do not use an extension cord unless it is a 14 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
    improper adapters or in any way modify the cord outlet.

Important Electrical Instructions
  - Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any ap- pliance with a large motor, the GFCI will trip often. Route
    the power cord away from any moving part of the treadmill including the elevation mechanism and transport wheels..
  - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is first turned on or even
    during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill itself
    does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
    have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online at
    www.squared.com part # QO120HM.

Important Grounding Instructions
  - This product must be grounded. If the treadmill should malfunction or breakdown, ground- ing provides a path of least resistance for electric current,
    reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
    appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
  serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
  outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 120-volt circuit, and has a grounding plug that looks
  like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
  as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
  can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must be connected to a permanent
  ground such as a properly grounded outlet box cover.
  Whenever the adapter is used, it must be held in place by
  a metal screw.




                                                                               17                                                                 Service Manual
6. CT900 ENT Error Messages /
       Troubleshooting




              18                Service Manual
Error Code Messages：
 Error   Description                     Remarks Error
 Code
 01H     Low voltage trip                By Inverter Error
 02H     Abnormal temperature sensor     By Inverter Error
 04H     Output overcurrent              By Inverter Error
 06H     Inverter overvoltage            By Inverter Error
 08H     Abnormal ground                 By Inverter Error
 09H     Inverter overheat               By Inverter Error
 0AH     Motor overload                  By Inverter Error
 0BH     Inverter overload               By Inverter Error
 0CH     System overload                 By Inverter Error
 0DH     Motor disconnection detection   By Inverter Error
 0EH     Brake fault                     By Inverter Error
 21H     Flash drive program failure     By Inverter Error
 22H     EEPROM failure                  By Inverter Error
 23H     Low voltage display             By Inverter Error
 25H     Emergency Stop (ESP)            By Inverter Error
 29H     Motor overheat                  By Inverter Error
 40H     Un-know mode                    By MCU Board Error
 41H     Inverter no-response            By MCU Board Error
 42H     Bike board no-response          By MCU Board Error
 44H     Console I2CNo-response          By MCU Board Error
 50H     Abnormal Update MCU FW          By MCU Board Error
 EAH     UCB Is Not Math LCB Device      GUI Error
 ECH     UCB To LCB Is No Response       GUI Error
 EDH     LCB Unknown Device              GUI Error




                                                              19   Service Manual
   Prepare：


               Picture        Tool name




                              Multi-meter




                         20                 Service Manual
 Error Message：INCLINE ERR
 Definition：During incline action, the display board CPU cannot read the VR value.
 Configuration：




                                                                      21             Service Manual
Cause of INCLINE ERR
      Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
           Explanation
                Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which
                   changes the VR value.
                The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it
                   should be. INCLINE ERR appears on the display.
           Action Flow Chart




                                                                          22                                                          Service Manual
Troubleshooting
            Part            Troubleshooting
                            1.Inspect whether the 8-PIN cable is connected well.
            8-pin cable
                            2.Test by replacing the cable with a good one.
                            1.Press incline UP or DOWN key again, making the incline motor return to its
            INVERTER        position.
                            2.If ERR still appears, re-calibrate the incline set.
                            1.Inspect whether the incline motor is stuck.
                            2.Inspect whether the incline gears are cracked.
            Incline motor
                            3.Test whether the incline motor has a broken circuit.
                            4.Re-calibrate the incline set.




                                                      23                                                   Service Manual
Circuit diagram(120V)




                        24   Service Manual
                                     Setting and Operation for Engineering Mode

1.Operation for entering engineering mode:
Press “Home” button 10 consecutive repetitions to enter engineering mode.




2. Instructions for each item of operation in engineering mode:
 After entering engineering mode, first priority is to enter “Machine Information” mode to set the type of the
 machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection must
 match the actual machine otherwise it will be unable to operate the machine properly.




                                                                          25                                      Service Manual
There are three modes for the Machine Type Treadmill/ Elliptical/ Bike. Please select for the machine.The selection must match the actual
machine otherwise it will be unable to operate the machine properly.


  GS MODE is a setting function for treadmill mode only:
  GS MODE ON is a function mode that the incline won’t resume. GS MODE OFF is a function          mode that the incline will resume.
  (Under Elliptical / Bike mode, please set it OFF)

 To set child lock function. When it is set ON, the display and buttons lock and are unable to use.
 To unlock, press and hold “UP” button for 3 seconds till OFF and children are able to use. This is an unlock function once only.


SPEAKER volume control, ON for display / OFF for hide (Speaker is optional)



DISTANCE/ HOUR Instruction for resetting DISTANCE/ HOUR:
Under Machine Information, press and hold “UP” button for 3 seconds to clear DISTANCE/
HOUR.

SW VERSION.

JNI VERSION.

FW VERSION.

OS VERSION.

Update Manager.




                                                             26                                                             Service Manual
                                                     Image for Treadmill Mode




                                                   Image for Elliptical / Bike Mode



ON/ OFF for beep sound mode

ON/OFF for sleep mode The display always lights when turns off. When there is no action for 30
minutes after turning on the power, it enters sleep mode.

To set max. incline level at 15.

English/Metric mode switching

Max. speed setting is 12 for English mode, 20 for Metric.

                                                             27                                  Service Manual
Min, speed control: 0.5 for English mode, 0.8 for Metric.

              Press “Calibration” button to start calibrating.
              It calibrates incline motor only. There is no calibration for the tread belt.
              (When calibration is completed, calibration window disappears)




To set distance locking function, when the distance reaches the setting value, the display and
buttons lock and are unable to use.
To unlock, press and hold “UP” button for 3 seconds. This is an unlock function once only.
(If password forgets, use default password 2222 to unlock the DISTANCE)

To set the value of DISTANCE (100 ~ 9999 Miles)



To set the password to unlock DISTANCE.




                                                               28                                Service Manual
Diagnose and save malfunction error messages for technician to inspect the machine and
troubleshooting.


Press “Error Code Log” button 10 consecutive repetitions to clear the error message.




                                                           29                            Service Manual
To set default language for the first page window. There are 12 languages in the
menu.




                                               30                                  Service Manual
            Image for Treadmill Software Update                      Image for Elliptical / Bike Software Update

                   First, add a new folder to the USB Transcend with file name “Dyaco” and transit each software
                  item to be updated or video files from new webs to the folder. Then insert the USB Transcend to
                  USB slot on back of the console and turn on the power of the treadmill.
Treadmill




Elliptical/Bike




                                                                                31                                  Service Manual
Treadmill updating procedure 1.   Elliptical/Bike updating procedure 1.




                                                        32                Service Manual
When update is completed please turn off the       When update is completed please turn off the
treadmill power to wait inverter to discharge      Elliptical / Bike power to wait adapter to discharge
for 10 seconds then resume the power and enter     for 3 seconds then resume the power and enter
the first page for operation.                      the first page for operation.




Press “Home” button 10 continuous repetitions to     Press “Home” button 10 continuous repetitions to
enter engineering mode then go to treadmill          enter engineering mode then go to Elliptical / Bike
updating page to proceed program updating,           updating page to proceed program updating,




                                                                        33                                 Service Manual
Updating procedure 2.                              Updating procedure 2.
To update App manager.                             Repeat previous step, turning off-on-first page-updating
page


                                                 Updating procedure 3.
                                                 To update App manager.




               Please press Install APK button to proceed APK software updating.




                                                                      34                                      Service Manual
                    Please press Install APK button to proceed APK software updating.




                    When updating is completed, press “Open” button to open APP software. When entering the
                    first page after completing updating, this product is able to operate.

Remark: If the image is shown after updating, then there is intermittence for the console during transmitting so that the error message is shown.




To eliminate this, press               button 10 consecutive repetitions to enter the first page. Whatever error message is shown, this will eliminate it and
 enter the first page for operation.




                                                                              35                                                            Service Manual
There are 6 preset web pages such as Face Book / You Tube etc.




          Press You Tube button for 2 seconds and the web page is deleted.




         Instruction for adding new webs


                                                                        36   Service Manual
 First, add a new folder to the USB Transcend with file name “Dyaco” and transit each software
item to be updated or video files from new webs to the folder. Then insert the USB Transcend to USB
slot on back of the console and turn on the power of the treadmill.




         Enter the new website (like flipboard.com)

         Enter the new filename (like flipboard)




The icon of new filename “flipboard” for the new website.


      Press Internet Manager button 10 consecutive repetitions to enter the preset adding website
      mode then hit “OK” button to complete adding the website.




                                                              37                                      Service Manual
Please hit WiFi button to proceed WiFi setting.




                                                  38   Service Manual
There is instructions for network setting, please hit “Ethernet” button to enter setting
window.




Please hit “Ethernet” to enter network setting mode.




Under “Connection Type”, select “DHCP” button the network will automatically search
for the connection. Select “Static IP” for manual setting.




                                                           39                              Service Manual
Press “Etherner Configuration” button 10 consecutive repetitions to enter Android setting
mode and hit “Date&Time” to select the area and time setting is completed.




 Please select the area.

                  Check for Automatic Date & Time to apply the time provided by the web.
                  Please resume the treadmill power when complete.




Select “C-SAFE or CAB” button for TV switching box (Choose one is allowed only)


                                                         40                                 Service Manual
    Brightness adjustment button




FTP IP ADDRESS is set at 61.218.169.200。

FTP PORT is set at 21。

ACCOUNT is set to be dyaco_service(lower case only)

PASSEORD is set at 23751545。

               SERIAL NUMBER is treadmill serial number to feedback for Error Log, for
               example CR800-ENT(5638880810000001).


               PATH is Error Log for feedback customer name, for example
               dyaco_service/SPIRIT FITNESS




                                                          41                             Service Manual
   To turn on or off Error Log feedback function and to set the feedback time.



Press “FTP Upload Test” button to upload information when finish. The green circle represents
upload completed while red circle is for error message or upload failed, please verify for correct
setting or network is not turned on. (When using Error Log feedback function, be aware of if WiFi is
connected.)




    Please select the player source such as TV / HDMI mode.

    Hit “OSD Menu” button as main menu, and select AUTO/DTV/ATV Tuner then hit “OSD
    Enter” button to proceed to next step.

    Hit “OSD Enter” button to select the country and use the arrow keys to choose. When finish,
    hit “OSD Enter” button again to proceed with channel searching. Wait until search ends.


                                                              42                                       Service Manual
     Channel searching                  Arrow keys




This button updates the channel list.

For HDMI function, please directly hit “HDMI” and connect the signal source to enjoy.

This button is for software R&D engineer only.




                                                         43                             Service Manual
Version for blue tooth module.

Hit “Clear” button, it clears all messages on the window.

Hit “Pair Mode” button, window displays “Enter pairing mode” and wait for blue tooth
connection.

Hit “Deleted Pair” button, window displays “OK” and disconnect blue tooth connection.

Hit “Reset” button, window displays “Bluetooth device is power on” and blue tooth to
turn on again.



                                                            44                          Service Manual
                     Hit this button to modify the name of blue tooth connection. Press “Rename BT Device”
                     button to enter when complete.

                     This button enters the modified name for blue tooth

                     Button for headphone volume control

Instruction for blue tooth operation procedure:
1.Press “Pair Mode” button, the window shows “Enter pairing mode” and proceed to the next step.
2.Turn on the cell phone or ipad and searching device, the display shows “ENT console”. Hit for coding operation
  and both cell phone window and console display will start coding requisition. When both are hit to confirm, the
  coding completes and function of blue tooth operation is available.


Troubleshooting procedure matrix
                    Condition                                             Reason                                                 Solve
When turn on power, ON/OFF switch isn’t lit.           1 Power cord isn’t plugged into outlet.      1 Plug the power cord into outlet.
                                                       2 Power cord isn’t plug into unit.           2 Plug the power cord into unit.
                                                       3 The voltage of outlet is too low.          3 Check the voltage of outlet.
                                                       4 Plug or connector of power cord is open.   4 Replace power cord.
                                                       5 Connector of power cord is broken.         5 Replace power cord.
                                                       6 Connecting cable disconnected.             6 Check if wire is disconnected, connect it again.
                                                       7 Breaker tripped.                           7 Press the small red button to return to original status.
                                                       8 Breaker is broken.                         8 Replace breaker.
                                                       9 ON/OFF switch is broken.                   9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown   1 Check the voltage of power is 100-120V. Replace
                                                        broken on controller.                       controller.
 When insert safe key, no display on monitor.           1 Haven’t switch ON/OFF switch.             1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.    2 Insert the safe key on right position.
                                                        3 8 PIN Computer connector not plugged      3 Please check the wire and connect again.
                                                          in properly.                              4 Replace 8 PIN computer cable.
                                                        4 8 PIN computer cable is broken.           5 Replace fuse or controller.
                                                        5 Fuse on controller is blown.              6 Replace varistor or controller.
                                                        6 Varistor on controller is blown.          7 Replace safety key device.
                                                        7 Safety device is broken. (open)           8 Replace console.
                                                        8 Other components are faulty.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)          1 Replace the safety key device or console.

 When press “START”, treadmill doesn’t start.          1 AC Motor U or V or W wire isn’t connected 1 Please check and plug again.
                                                         into right position.
                                                                                    45                                                                  Service Manual
                                                       2 Motor is broken.                            2 Replace motor or check the wire and connector if it was
                                                                                                       broken.
                                                       3 Treadmill controller shut down and TFT      3 Turn off the AC switch and turn on power again.
                                                       would be ON.
Treadmill stops or shuts off by itself.                1 House breaker tripped.                      1. Reset it.
                                                       2 Treadmill breaker tripped.                  2. Reset treadmill breaker.
                                                       3 Treadmill controller fuse is broken.        3. Replace with new fuse
                                                       4 Treadmill controller shut down and TFT      4. Turn off the AC switch and turn on power again.
                                                       would be ON.

After removing safe key, treadmill can’t stop.         1. The safety key device is broken.           1. Replace with new safety key device.
TFT not bright, incomplete or imperfect.               1. TFT light is broken.                       1. Replace with new TFT or console.
                                                       2. Power to console too low.                  2. Check AC power is 110-120V.
                                                                                                     3. Check power to console.
                                                                                                     4.Replace lower controller.
TFT displays not bright, incomplete or imperfect.     1. TFT displays are broken.                    1. Replace with new console.
When press “START” button to start treadmill, running 1. Controller experienced unusual shut         1. Turn off power and reset the treadmill.
belt isn’t running and window displays “LS1/LOW          down; the Shut_ DOWN light will be
SPEED” error message after 10 seconds.                   always bright.                              2. Plug wires again.
                                                      2. AC Motor wires (U or V or W) aren’t
                                                         plugged into controller.                    3. Plug the wire again on controller, connector and console.
                                                      3. Computer cables not connected properly. 4. Replace with new wires.
                                                      4. Computer cables are broken or damaged. 5. Replace with new motor belt.
                                                      5. Motor belt is broken.                       6. Replace with new controller.
                                                      6. Controller is broken.                       7. Replace with new AC motor.
                                                      7. AC Motor is broken.                         8. Replace with new console.
                                                      8. Console is broken.
The speed of the belt doesn’t match console display. 1. Console is not calibrated.                   1.Calibrate the console
The incline position doesn’t match console            1 Console is not calibrated.                   1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “INCLINE 1 Position sensor value of incline motor is            1 Turn off the AC switch and turn on power again.
ERR”.                                                 wrong.                                         2. Calibrate the monitor.
After pressing “START” button, the treadmill stops    1 Controller is broken.                        1 Turn off the AC switch and turn on power again.
immediately.                                                                                         2 Replace controller and calibrate it.
Erratic pulse display.                                1. Another chest belt in use around treadmill. 1. Check for other chest belt use around treadmill.
                                                                                                     2. Change the position or direction of treadmill.
                                                      2. Other magnetic field disturbance.           3. Replace with new receiver.

                                                       3. Receiver is broken.
After pressing “START” button, the treadmill stop      Controller was broken.                        Replace with new controller and calibrate it.
immediately.


FAST/SLOW button of SPEED ADJUSTMENT                   1 The connector of SPEED CABLE and            1. Connect cables again.
                                                                                   46                                                                  Service Manual
SWITCH can’t be used.                               CONSOLE not connected properly.
                                                    2 The connector of SPEED CABLE and          2. Connect cables again.
                                                      SPEED ADJUSTMENT SWITCH
                                                      W/CABLE not connected properly.
                                                    3 The connector of SPEED CABLE or           3. Connect cable again.
                                                      SPEED ADJUSTMENT SWITCH/W/CABLE
                                                      is
                                                      damaged.
                                                    4. Button of SPEED ADJUSTMENT SWITCH 4. Replace with new buttons.
                                                       is broken.
                                                    5. The connector of SPEED CABLE or          5. Replace with new cable.
Speed button just can press FAST, can’t press SLOW.
                                                       SPEED ADJUSTMENT
                                                       SWITCH/W/CABLE is damaged.
Speed button just can press SLOW, can’t press FAST.                                             6. Replace with new cable.
                                                    6. The connector of SPEED CABLE or
                                                       SPEED ADJUSTMENT
                                                       SWITCH/W/CABLE is damaged.
UP/DOWN button of                                   1 The connector of INCLINE CABLE            1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used.              and CONSOLE not connected properly.
                                                    2. The connector of INCLINE CABLE           2. Connect the wires again.
                                                    and INCLINE ADJUSTMENT SWITCH
Incline button just can press UP, can’t press DOWN. W/CABLE not connected properly.
Incline button just can press DOWN, can’t press UP.                                             3. Replace the cable.
                                                    3 The connector of INCLINE CABLE or
                                                    INCLINE ADJUSTMENT SWITCH CABLE
                                                    got damage.                                 4. Replace buttons.
                                                    4. Button of INCLINE ADJUSTMENT
                                                    SWITCH is broken.                           5. Replace the cable.
                                                    5. The connector of INCLINE CABLE or
                                                    INCLINE ADJUSTMENT SWITCH CABLE             6. Replace the cable.
                                                    got damage.
                                                    6. The connector of INCLINE CABLE or
                                                    INCLINE ADJUSTMENT SWITCH CABLE
                                                    damaged.
Hand pulse lost its function.                       1. Hands not on the hand pulse sensors or 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                        only one hand on sensor.
                                                    2. The connector of HANDPULSE W/WIRE 2. Connect the cable again.
                                                       and Console not connected properly.
                                                    3. The wires got damaged when connecting 3. Replace with new cable.
                                                       the HANDPULSE W/WIRE and Console.
                                                    4. Hand pulse board is broken.              4. Replace console or Hand pulse board.
Wireless lost its function.                         1. Chest belt not worn properly.            1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                    oriented correctly.
                                                    2. Distance is too far and exceeds range of 2. User chest belt in front of console within 3 feet.
                                                                                47                                                                Service Manual
                                               receiver.                                        3. Replace with new lithium battery type is CR2032.

                                               3. Chest belt battery is weak or dead.
Chest belt too close to the treadmill.         Weak battery.                                  Replace with new lithium battery with type CR2032.
Tread belt does not run in center.             Tread belt tension not even across tread belt. See treadmill belt adjustment

Tread belt hesitates while being stepped on.   Insufficient lubricant on tread belt.            See treadmill belt lubrication
                                               Tread belt tension insufficient
Black particles collecting under treadmill.    Drive belt is breaking in.                       Vacuum under treadmill periodically.
Noise under motor cover.                       1. Worn brushes or bearings on motor.            1. Replace with new motor.
                                               2. Front roller bearings are defective.          2. Replace with new front roller.
                                               3. Drive belt is misadjusted (too tight or too   3. Adjust motor position.
                                               loose).
Noise in the rear of the treadmill.            1. Rear roller bearings are defective.           1. Replace with new rear roller.
                                               2. Rear roller misaligned.                       2. Adjust rear roller position.




                                                                             48                                                                 Service Manual
7. General Maintenance




          49             Service Manual
Service Troubleshooting Checklist – Diagnosis Guide
Before contacting your dealer for aid, please review the following information. It may save you both time and expense.
This list includes common problems that may not be covered under the treadmill’s warranty.


PROBLEM                                                SOLUTION/CAUSE
Display does not light                         1) Tether cord not in position.
                                               2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                               3) Plug is disconnected. Make sure plug is firmly pushed into
                                                 120 VAC wall outlet.
                                               4) Breaker panel circuit breaker may be tripped.
                                               5) Treadmill defect. Contact your dealer.

Tread-belt does not stay centered              The user may be walking while favoring or putting more weight
                                               on either the left or right foot. If this walking pattern is natural,
                                               track the belt slightly off-center to the side opposite from the belt
                                               movement.

Treadmill belt hesitates when walked/run on    See General Maintenance section on Tread-belt Tension.
                                               Motor drive belt may be loose.

Motor is not responsive after pressing start   1) If the belt moves, but stops after a short time and the
                                                display shows “LS”, run calibration (See procedure on
                                                next page).
                                               2) If you press start and the belt never moves, then the
                                                  display shows LS, contact service.




                                                                                          50                                        Service Manual
Treadmill will only achieve approximately        This indicates motor should be receiving power to operate. Low AC voltage
7 Mph but shows higher speed on display         to treadmill. Do not use an extension cord. If an extension cord is required
                                                 it should be as short as possible and heavy duty 14 gauge minimum.
                                                Low household voltage. Contact an electrician or your dealer.
                                                A minimum of 110 volt AC current, 50/60 hz is required.

Tread-belt stops quickly/suddenly when           High belt/deck friction.
tether cord is pulled

Treadmill trips on board 20 amp circuit          High belt/deck friction.

Computer shuts off when console is              Treadmill may not be grounded. Static electricity is “crashing” the computer.
touched (on a cold day) while walking/running   Refer to Grounding Instructions .

House circuit breaker trips, but not the        Need to replace the house breaker with a “High
treadmill circuit breaker.                      inrush current” type breaker




                                                                                       51                                       Service Manual
8. Treadmill Folding/Unfolding and
             Transport




                52              Service Manual
     TRANSPORTATION
     INSTRUCTIONS
       Carefully lift the treadmill at the rear roller
       area, grasping the two side end caps, and
       roll the treadmill away.




53                                                  Service Manual
9. General Maintenance




          54             Service Manual
 9.1 Tread belt and Deck
 Your treadmill uses a very high-efficient low-friction bed. Performance is maximized when the bed is kept as clean as possible. Use a soft, damp cloth or
 paper towel to wipe the edge of the belt and the area between the belt edge and frame. Also reach as far as practical directly under the belt edge. This
 should be done once a month to extend belt and bed life. Uses water only - no cleaners or abrasives. A mild soap and water solution along with a nylon
 scrub brush will clean the top of the textured belt. Allow the belt to dry before using.

 The low maintenance (routine monthly cleaning), dual-sided hard wax deck is designed to withstand up to 32,000 kilometers on each side. If the original
 side of the deck shows significant wear, it needs to be flipped.

 Contact your service technician for assistance. Do not apply any type of lubricant or wax to the surface.

 Belt Dust - This occurs during normal break-in or until the belt stabilizes. Wiping excess off with a damp cloth will minimize buildup.

 General Cleaning - Dirt, dust, and pet hair can block air inlets and accumulate on the running belt. On a monthly basis: vacuum underneath your
 treadmill to prevent buildup. Once a year, you should remove the motor hood and vacuum out dirt that may accumulate. UNPLUG POWER CORD
 BEFORE THIS PERFORMING THIS TASK. Do not attempt any servicing or adjustments other than those described in this manual. Opening the motor
 cover must be left to trained service personnel familiar with electro-mechanical equipment and authorized under the laws of the country in question to
 carry out maintenance and repair work.

 BELT ADJUSTMENTS:
 Tread-belt Tension Adjustment - Adjustment must be made from the rear roller. The adjustment bolts are located at the end of the step rails in the end
 caps, as noted in diagram below.




Tracking / Tension                                                                  Tracking / Tension
Adjustment                                                                          Adjustment



                     Note: Adjustment is through small hole in the end cap.


                                                                               55                                                           Service Manual
Tighten the rear roller bolts only enough to prevent slippage at the front roller. Turn both tread-belt tension adjustment bolts in increments of 1/4 turn
each and inspect for proper tension by walking on the belt at a low speed, making sure the belt does not slip. Keep tensioning the bolts until the belt
stops slipping.

      If you feel the belt is tight enough, but it still slips, the problem may be a loose Motor drive belt under the front cover.

DO NOT OVERTIGHTEN – Over tightening will cause belt damage and premature bearing failure.


TREADBELT TRACKING ADJUSTMENT:
The performance of your treadmill is dependent on the frame running on a reasonably level surface. If the frame is not level, the front and back roller
cannot run parallel, and constant belt adjustment may be necessary.

The treadmill is designed to keep the tread-belt reasonably centered while in use. It is normal for some belts to drift near one side while the belt is
running with no one on it. After a few minutes of use, the tread-belt should have a tendency to center itself. If, during use, the belt continues to move
toward one side, adjustments are necessary.

TO SET TREADBELT TRACKING:
A 10 mm Allen wrench is provided to adjust the rear roller. Make tracking adjustments from the left side only. Set belt speed at approximately 3 to 5 kph.
Remember, a small adjustment can make a dramatic difference!

Turn the bolt clockwise to move the belt to the right. Turn the bolt only a 1/4 turn and wait a few
minutes for the belt to adjust itself. Continue to make 1/4 rotation turns until the belt stabilizes in the
center of the running deck.

The belt may require periodic tracking adjustment depending on use and walking/running
characteristics. Some users will affect tracking differently. Expect to make adjustments as required
to center the tread-belt. Adjustments will become less of a maintenance concern as the belt is used.
Proper belt tracking is an owner responsibility common with all treadmills.




                                                                                  56                                                           Service Manual
ATTENTION:
DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING /
TENSION ADJUSTMENTS IS NOT COVERED UNDER THE WARRANTY.
Unplug treadmill before performing any maintenance.




RECOMMENDED MAINTENANCE OF RUNNING BELT/DECK



Note: ● Please clean wax on roller during flipping deck or replacing belt/belt.
      ● The low maintenance (routine monthly cleaning), dual-sided hard wax deck is designed to withstand up to 20,000 Kilometer/12,500 Miles on
        each side. If the original side of the deck shows significant wear, it needs to be flipped. Contact your service technician for assistance. Do not
        apply any type of lubricant or wax to the surface.




                                                                             57                                                             Service Manual
9.2. Service Troubleshooting Checklist – Diagnosis Guide
Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common
problems that may not be covered under the treadmill’s warranty.

PROBLEM                                                 SOLUTION/CAUSE
Display does not light                          1) Tether cord not in position.
                                                2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                                3) Plug is disconnected. Make sure plug is firmly pushed into
                                                110 VAC wall outlet.
                                                4) Breaker panel circuit breaker may be tripped.
                                                5) Treadmill defect. Contact your dealer.

Tread-belt does not stay centered               The user may be walking while favoring or putting more weight
                                                on either the left or right foot. If this walking pattern is natural,
                                                track the belt slightly off-center to the side opposite from the belt
                                                movement.

Treadmill belt hesitates when walked/run on     See General Maintenance section on Tread-belt Adjustment.
                                                Motor drive belt may be loose.

Motor is not responsive after pressing start    1) If the belt moves, but stops after a short time and the
                                                  display shows “LS/LOW SPEED”, run calibration (See section 8.1 on Error Message: LS/LOW SPEED).
                                                 2) If you press start and the belt never moves, then the
                                                    display shows LS/LOW SPEED, contact service.


Treadmill will only achieve approximately         This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord.
10 kph but shows higher speed on display          If an extension cord is required it should be as short as possible and heavy duty 16 AWG minimum. Low household voltage.
                                                   Contact an electrician or your dealer. A minimum of 110 volt AC current, 60 hz is required.

Treadmill trips on board 15 amp circuit           High belt/deck friction. See General Maintenance section on Belt/Deck Lubrication..

 Computer shuts off when console is               Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to section 7.3 for Grounding Instructions.
touched (on a cold day) while walking/running

House circuit breaker trips, but not the          Need to replace the house breaker with a “High inrush current” type breaker (see section 7.2 for Important Electrical
treadmill circuit breaker.                        Instructions.)




                                                                                           58                                                                      Service Manual
Treadmill with noises                 1. If the noise is coming from the rollers, .
                                      2. If the noise is coming when the user is running on the treadmill with lowest level of incline , it could be due to too much pressure
                                          with the incline cylinder. (only in case of the lowest incline level).
                                      3. If there is knocking noise during the workout, check and make sure all bolts are tightened.
                                      4. When there is thumping noise while the belt is running. This happens with a brand new treadmill or when the treadmill has not
                                         been used for a long time. This is due to the belt has been shaped with rollers and harden because of low temperature. Running
                                         the belt for tens of minutes the thumping noise will gradually go away.

Noise under motor cover.                1. Worn brushes or bearings on motor. Replace with new motor brushes.
                                        2. Front roller bearings are defective. Replace with new front roller.
                                        3. Drive belt is misadjusted (too tight or too loose). Adjust motor position.

Noise in the rear of the treadmill.   1. Rear roller bearings are defective.   Replace with new rear roller
                                      2. Rear roller misaligned.      Adjust rear roller position.

Tread belt hesitates while being        1. Insufficient lubricant on tread belt.
 stepped on.                           2. Tread belt tension insufficient

Black particles collecting under        Drive belt is breaking in. Vacuum under treadmill periodically.
treadmill.




                                                                               59                                                                       Service Manual
10. Installation of the Incline Motor




                  60               Service Manual
Incline Range must be adjusted to 315 mm minimum prior to installation.



                                  61                                      Service Manual
1. Serial Number Location




                            62   Service Manual
2. Component Description




                                                 AC Motor

                           Inverter    Incline
                            Board       Motor

            Lower
            Control
            Board



                                      63                    Service Manual
Console




           Hand
           Pulse




          64       Service Manual
3. Preventative Maintenance

TO SET TREADBELT TRACKING:
A 10 mm Allen wrench is provided to adjust the rear roller. Make tracking adjustments from the left side only. Set belt speed at
approximately 3 to 5 kph.

Remember, a small adjustment can make a dramatic difference!

Turn the bolt clockwise to move the belt to the right. Turn the bolt only a 1/4 turn and
wait a few minutes for the belt to adjust itself. Continue to make 1/4 rotation turns
until the belt stabilizes in the center of the running deck.

The belt may require periodic tracking adjustment depending on use and
walking/running characteristics. Some users will affect tracking differently. Expect to
make adjustments as required to center the tread-belt. Adjustments will become less
of a maintenance concern as the belt is used. Proper belt tracking is an owner responsibility common with all treadmills.




                                                            65                                                          Service Manual
4. Part Replacement Guide

   4.1 Console Replacement

      4.1.1 As shown in Figure 4.1.1, use the screwdriver to remove the LED chin cover 4 umbrella head
            screws.




      Figure 4.1.1

      4.1.2 As shown in Figure 4.1.2, remove the electronic control cable connector, use the cross
            screwdriver to remove the electronic watch 4 umbrella head screws, you can remove the
            electronic form.




      Figure 4.1.2

      4.1.3 Electronic watch assembly can be replaced according to 4.1.1 and 4.1.2.




                                            66                                              Service Manual
4.2 Lower Control Board Replacement

   4.2.1 As shown in Figure 4.2.1, use the male screwdriver to loosen the eight umbrella head screws
         that secure the motor cover to remove the motor cover.




   Figure 4.2.1

   4.2.2 Remove the lower controller by removing the controller-related line and using the cross
         screwdriver to remove the controller as shown in Figure 4.2.2.




   Figure 4.2.2

   4.2.3 Replace the components and insert the wires back in accordance with 4.2.1 and 4.2.2.

                                         67                                               Service Manual
4.3 Motor Replacement

   4.3.1 Refer to Step 4.2.1 to remove the motor cover.

   4.3.2 As shown in Figure 4.3.1, use the screwdriver to remove the motor ground wire (green yellow)
         and the motor connected to all wires on the control panel.




   Figure 4.3.1

   4.3.3 As shown in Figure 4.3.2, remove the motor under the cover button.




   Figure 4.3.2

   4.3.4 As shown in Figure 4.3.3, use the tool to secure the red arrow and release the belt with the 13th
         T-sleeve to remove the belt and remove the belt from the motor.

                                          68                                                Service Manual
Figure 4.3.3

4.3.5 Remove the four M10 caps using the 17th T-Shirt to remove the motor from the motor.




Figure 4.3.4

4.3.6 Refer to Step 4.3.5 to replace the motor. The motor needs to push forward, the belt hook back.

4.3.7 Refer to Step 4.3.4, use 13 T-type sleeve, adjust the required belt tension, the value can be
      adjusted to 120 ~ 130HZ.

4.3.8 Connect the motor ground wire and the motor to all the wires on the control panel.




                                        69                                                 Service Manual
4.4 A.C. Input Module Replacement

   4.4.1 Refer to Step 4.2.1 to remove the motor cover.

   4.4.2 Remove the AC power switch ground wire using a screwdriver as shown in Figure 6.4.1.




   Figure 4.4.1

   4.4.3 Remove the AC power switch module with the cross screwdriver and switchboard 8 as shown in
         Figure 6.4.2.




   Figure 4.4.2

   4.4.4 After replacing the new product, replace it in the order of removal.



                                           70                                          Service Manual
4.5 Front and Rear Roller Replacement

   4.5.1 As shown in Figure 4.5.1, use the screwdriver to remove the left and right side adjustment
         screw.




   Figure 4.5.1

   4.5.2 As shown in Figure 4.5.2, use the No. 8 L-type hex wrench to remove the two rear wheel screws.




   Figure 4.5.2

   4.5.3 Refer to Step 4.2.1 to remove the motor cover.

   4.5.4 Refer to Step 4.3.3 and Step 4.3.4 to release the belt. Please refer to 4.5.1 and 4.5.2 for the
         assembly of the left and right chain cover.

   4.5.5 As shown in Figure 4.5.3, remove the front roller with the No. 8 L-shaped hex wrench and
                                            71                                                  Service Manual
        remove the front roller.




   Figure 4.5.3

   4.5.6 Replacement of the new front and rear rollers, and then assembled in the order of removal.

   4.5.7 When assembled, adjust the running belt tension, so that running in the set. Refer to step 4.3.4,
         use 13 T-type sleeve, adjust the belt tension 120 ~ 130HZ can.




4.6 Running Deck, Running Belt and Cushion Replacement

   4.6.1 Refer to Step 4.5.1 to Step 4.5.5 to remove the front and rear rollers.
   4.6.2 As shown in Figure 4.6.1, use a screwdriver to remove the screws on the rear cover.




   Figure 4.6.1

   4.6.3 As shown in Figure 4.6.2, use the No. 6 L-shaped hex wrench to loosen the 8 screws of the
                                          72                                              Service Manual
     retaining strip.




Figure 4.6.2




                        73   Service Manual
4.6.4 As shown in Figure 4.6.3, remove the left and right trims in the direction of the arrow.




Figure 4.6.3

4.6.5 As shown in Figure 4.6.4, use the No. 4 L-type hexagonal wrench to remove the running plate
      fixing screw. Set off the running board; choose to replace the running board or running belt. To
      change the cushion, as shown in Figure 6.6.5, and then remove the 8 buffer to replace the new,
      assembled and then removed in order to replace.




Figure 4.6.4                      Figure 4.6.5

4.6.6 When assembled, adjust the running belt tension, so that running in the set.


                                        74                                                 Service Manual
4.7 Incline Motor Replacement

   4.7.1 Refer to Step 4.2.1 to remove the motor cover.

   4.7.2 As shown in Figure 4.7.1, Figure 4.7.2, Figure 4.7.3, move the machine up on the paper tube, use
         the No. 17 opening wrench 2 to remove the lifting motor The screws that are fixed to the lifting
         frame , Use the No. 17 opening wrench 2 to remove the lifting motor fixed to the main frame of
         the screw and detachable motor, remove the need to be associated with the line removed.




   Figure 4.7.1                 Figure 4.7.2                   Figure 4.7.3

   4.7.3 As shown in Figure 4.7.4, the lifting motor should be adjusted to a minimum stroke of 315 mm to
         be set up (about five turns in the end).




   Figure 4.7.4
                                           75                                              Service Manual
4.7.4 As shown in Figure 4.7.5, the assembly of the lifting motor should be replaced in the order of
      removal and connected to the control and grounding lines.




Figure 4.7.5




                                       76                                                Service Manual
4.8 Idler Replacement

   4.8.1 Refer to Step 4.3.1 to Step 4.3.5 and remove the motor.

   4.8.2 As shown in Figure 4.8.1, remove the press pulley by removing the C with the tool.




   Figure 4.8.1

   4.8.3 Replace the new product, and then replace the assembly in the order of removal.




                                          77                                               Service Manual
4.9 Hand Pulse Control Board and Hand Pulse Set Replacement

   4.9.1 Refer to Step 4.1.1 and Step 4.1.2 to remove the electronic watch group.

   4.9.2 As shown in Figure 4.9.1, remove the 18 screws from the upper bracket of the fixed bracket with
         a screwdriver to remove the bracket cover.




   Figure 4.9.1

   4.9.3 As shown in Figure 4.9.2, remove the 12P control cable connector and remove the core module
         wire to remove the new product.




   Figure 4.9.2

                                          78                                              Service Manual
4.9.4 As shown in Figure 4.9.3, use the hexagonal wrench to remove the four hexagonal screws, you
      can replace the hand-held group, assembled and then removed in order to replace.




Figure 4.9.3




                                     79                                             Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS I

“Ou] JeEUOIZEUIa}U| OOBAG

OIVAd

jenuepy BdIAlas
INA 006L9


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SOUIJINO LNA OO6LO *}


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

JO}OW OV

JOJOY\
SUI|OU|

NS ee

pieog
JOUSAU|


=== OCR SUPPLEMENT, PDF PAGE 6 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SHEd IIUOIIA/FZ ‘Z


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS L

an Oe AVTdSIC

NVd surjoop

$19]]01]U04 addy


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS 9

qdSlysAnNni

YOLOW OV
YOLOW SNITONI

eam 14 Bner
a)

oo

JOALIQ Puke 413]|01]U0D JMO}


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

suoneinbijuoy Jeo1j9e/F7'¢


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Bui pue suoljsaUUOD IIseg INF 006LO ‘“b


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS c]

LOANNOO
JOMOd

g|osuoD

LOANNOO
}OUI9]U|

LOANNOD 8eS-O

8) LOANNOO
qJ1EgVO WALSAS

72) LOANNOO
pueog Aoy

Wwo}og pseog O/|


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SUONONA]SU] AJajeg JONPOId °C


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

burnlooysaqnol]
/ sabessay] 40449 INF 006L9 9


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Error Code Messages :

Error |Description Remarks Error
Code

01H Low voltage trip By Inverter Error
02H _  |Abnormal temperature sensor |By Inverter Error
04H ~=|Output overcurrent By Inverter Error
06H ___|Inverter overvoltage By Inverter Error
08H [Abnormal ground By Inverter Error
09H _ |Inverter overheat By Inverter Error
OAH  |Motor overload By Inverter Error
OBH __ |Inverter overload By Inverter Error
OCH _ |System overload By Inverter Error
ODH _ |Motor disconnection detection |By Inverter Error
OEH _ [Brake fault By Inverter Error
21H Flash drive program failure By Inverter Error
22H  |EEPROM failure By Inverter Error
23H Low voltage display By Inverter Error
25H Emergency Stop (ESP) By Inverter Error
29H __|Motor overheat By Inverter Error
40H Un-know mode By MCU Board Error
41H _ {Inverter no-response By MCU Board Error
42H _ |Bike board no-response By MCU Board Error
44H __|Console I2CNo-response By MCU Board Error

50H {Abnormal Update MCU FW By MCU Board Error

EAH UCB Is Not Math LCB Device /GUI Error

ECH |UCBToLCB Is No Response  |GUI Error

EDH LCB Unknown Device GUI Error

19 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS 0z

JOJOW-NIN

SwWeU [OO] BIND

: qeddlq @


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Error Message : INCLINE ERR

Definition : During incline action, the display board CPU cannot read the VR value.
Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | pawwarcys

INCLINE z INCLINE
VR Be UP/DOWN
VOLTAGE = SIGNAL

INCLINE
MOTOR
DRIVER BOARD ex VR VOLTAGE INCLINE VR SET

C) INCLINE DOWN LED
OC) INCLINE UP LED

21 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 34 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of INCLINE ERR
m Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
Explanation
@ Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which
changes the VR value.
@ The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it
should be. INCLINE ERR appears on the display.

Action Flow Chart
C DISPLAY BOARD _

J

DRIVER BOARD

PMI UF Ac TICO™N.,
Ci 82? 8 .1csde TSI tee
Wood bf Ate INCREASES

IN Pots weN Aco ric i,
Ow ™ LET 1 eGHIS.iNMCLIMNE
WOM TAGs DECREASES

INCLINE MOTOR

UP LED LitagHt=.

INCLINE RISES? = a
~
DOWN LED LIGHTS.
INCLINE LOWERS? _ -
=
| ¥

- ae = SHOW INCLINE E2
C NO ERR MESSAGE ) C MESSAGE >

22 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 56 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Circuit diagram(120V)

3 18800-WT002
TREADMILL CIRCUIT DIAGRAM

AC POWER INPUT (ew _ay
Ss

PLUG
=
2
oO
c AC SWITCH
se SAFE HDMI
oD BNC RJ45
g i
e WHITE WIRE Combo Board ra
= WHITE WIRE =
5 =
oO
o WHITE WIRE =
+ e FILTER 3 <
BLACK WIRE BLACK WIR rT
kK
»
oO
INCLINE 2
MOTOR oO
ee z
5 fe)
o B
Ss CO] wl lw
S| Slee
anaes
E| O KE
= Teel]
ag
o oO 2|° ° LU
a |
Aba abe g GROUND WIRE
re
DOWN
AC INVERTER=gp——
os
—~ COM
UV W
0
a ERP BOARD
TO INVERTER
SIGNAL WIRE
a i | RPM SENSOR SIGNAL
GROUND WIRE

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Setting and Operation for Engineering Mode

1.Operation for entering engineering mode:
Press “Home” button 10 consecutive repetitions to enter engineering mode.

Settings
Engineering Mode

Home
Oo TV % ~) Language

Security
Diagnostics
Machine Information

—7@ Exercise a2
=4 progiante Internet

Maintenance
TV Setup
BT Setup

To begin workout press the START key on the keypad below. To view an
Exercise Program or change the Language, select either key above

2. Instructions for each item of operation in engineering mode:
After entering engineering mode, first priority is to enter “Machine Information” mode to set the type of the
machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection must
match the actual machine otherwise it will be unable to operate the machine properly.

Machine Information

Settings Machine Information
Engineering Mode MACHINE TYPE W VERSION

Security

GS MODE

Diagnostics

Maintenance
TV Setup
BT Setup

25 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
MACHINE TYPE

There are three modes for the Machine Type Treadmill/ Elliptical/ Bike. Please select for the machine.The selection must match the actual
j UCN} ~machine otherwise it will be unable to operate the machine properly.

als GS MODE is a setting function for treadmill mode only:
<4 OFF GS MODE ON is a function mode that the incline won’t resume. GS MODE OFF is a function mode that the incline will resume.
(Under Elliptical / Bike mode, please set it OFF)
"west —sTo set child lock function. When it is set ON, the display and buttons lock and are unable to use.
To unlock, press and hold “UP” button for 3 seconds till OFF and children are able to use. This is an unlock function once only.

SPEAKER

4 ON DP

SPEAKER volume control, ON for display / OFF for hide (Speaker is optional)
a=

DISTANCE/HOUR

= DISTANCE/ HOUR Instruction for resetting DISTANCE/ HOUR:
Under Machine Information, press and hold “UP” button for 3 seconds to clear DISTANCE/
HOUR.

SW VERSION

JNI VERSION

omnis JNI VERSION.

FW VERSION

ono FW VERSION.

OS VERSION

( 801-1505271750 OS VERSION.

Update Manager

V1.2

Update Manager.

26 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Engineering Mode

Settinas Engineering Mode

Engineering Mode

WHEEL SIZE MAX. SPEED
Security o> nT

BEEP MODE MIN. SPEED

Machine Information a
Calibration

Maintenance

>
Ty Seup cre EC
>

BT Setup

Engineering Mode

BEEP MODE

or ON/ OFF for beep sound mode

@ > ON/OFF for sleep mode_ The display always lights when turns off. When there is no action for 30
minutes after turning on the power, it enters sleep mode.

>
Cm) To set max. incline level at 15.

>
English/Metric mode switching

MAX. SPEED

en Max. speed setting is 12 for English mode, 20 for Metric.

27 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
MIN. SPEED

_ ee Min, speed control: 0.5 for English mode, 0.8 for Metric.
[calration gs oe
hs Press “Calibration” button to start calibrating.
It calibrates incline motor only. There is no calibration for the tread belt.
(When calibration is completed, calibration window disappears)
Calibration Calibration

Settings

Security

Ciyuicciry wivuc

Security o OF C
Diagnostics => — _ > " ea — —,
Machine Information
Maintenance
TV Setup
BT Setup

LOCK MODE

<4 OFF (OP

To set distance locking function, when the distance reaches the setting value, the display and
buttons lock and are unable to use.

To unlock, press and hold “UP” button for 3 seconds. This is an unlock function once only.

(If password forgets, use default password 2222 to unlock the DISTANCE)

SET LOCK ACCUMULATE MILEAGE

SEED Jo set the value of DISTANCE (100 ~ 9999 Miles)

To set the password to unlock DISTANCE.

28 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Settings Error Code Log
Engineering Mode

Security
Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

Error Code Log

Diagnose and save malfunction error messages for technician to inspect the machine and
troubleshooting.

Error Code Log

Press “Error Code Log” button 10 consecutive repetitions to clear the error message.

Error Code Log

29 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Maintenance

Settings
Engineering Mode

Maintenance

Default Language Setup

Security
Software Update Manager

Internet Manager
WiFi/Ethernet Setup
Machine Setup
FTP Settings

Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

Default Language Setup

To set default language for the first page window. There are 12 languages in the
menu.

Default Language Setup

Portugués Nederlands

Norsk

30 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
— oan

o ay) «)
a Bagae
duasping png dv.png ups tpboard png tan pag kngou pag

Treadmill updating procedure 1. Update Firmware Elliptical/Bike updating procedure my Update Ble Firmware

32 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
When update is completed please turn off the When update Is completed please turn off the

treadmill power to wait inverter to discharge Elliptical / Bike power to wait adapter to discharge
for 10 seconds then resume the power and enter for 3 seconds then resume the power and enter
the first page for operation. the first page for operation.

Programs —¢7? ~~ Programs

To begin workout press the START key on the keypad below. To view an
Exercise Program or change the Language, select either key above.

To begin workout press the START key on the keypad below. To view an
Exercise Program or change the Language, select either key above

Press “Home” button 10 continuous repetitions to Press “Home” button 10 continuous repetitions to
enter engineering mode then go to treadmill enter engineering mode then go to Elliptical / Bike
updating page to proceed program updating, updating page to proceed program updating,

33 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Updating procedure 2. Update AND Manager Updating procedure 2. Update Firmware

To update App manager. Repeat previous step, turning off-on-first page-updating
page

App Update Manager

v1.2
nese Updating procedure 3. Update App Manager

Uninstall APK To update App manager.

App Update Manager
V1.2

Install APK

Uninstall APK

install APK Please press Install APK button to proceed APK software updating.

34 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
First, add a new folder to the USB Transcend with file name “Dyaco” and transit each software
item to be updated or video files from new webs to the folder. Then insert the USB Transcend to USB
slot on back of the console and turn on the power of the treadmill.

— Enter the new website (like flipboard.com)

ize: 150 KB)

Enter the new filename (like flipboard)

Tipboss! Pas The icon of new filename “flipboard” for the new website.

internet Manager Press Internet Manager button 10 consecutive repetitions to enter the preset adding website
mode then hit “OK” button to complete adding the website.

37 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS ge

aiqesia L-ysonooey

aiqesia yayAeiq

aiqesig bunsnbsig

JOMION Ppy ueog uo

Bumas 14-IM

‘Bula 141M P9e00Jd 0} VOTING 141M WY BSeaId iN

yauayyy
'IM

dag 9W94)3/!4IM

nag 2413/14.

Jobeuey jausayuy


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Ethernet There is instructions for network setting, please hit “Ethernet” button to enter setting

window.

Ethernet Configuration

IP Address

192.168.192.28

MAC Address

00:18:70:91:48:7F

Ethernet Configuration
devices

Please hit “Ethernet” to enter network setting mode.

Ethernet Configuration

Network Setting

Ethernet Devices. IP address

Connection Type NetMask
DHCP

elo? Gateway address

DNS address

Connection Type
DHCP

Static IP

Under “Connection Type”, select “DHCP” button the network will automatically search
for the connection. Select “Static IP” for manual setting.

39 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Hee Configuration Press “Etherner Configuration” button 10 consecutive repetitions to enter Android setting

mode and hit “Date&Time” to select the area and time setting is completed.

Select time zone
MT+08:00. pe t

Please select the area.

Automatic date & time
Jse network-provided tim:

Machine Setup

Machine Setup

Check for Automatic Date & Time to apply the time provided by the web.
Please resume the treadmill power when complete.

(4° CABO

e

CSAFE Port Setup

~« CAB >

Select “C-SAFE or CAB” button for TV switching box (Choose one is allowed only)

40 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Brightness Control

102

Brightness adjustment button

FTP Settings

FTP Settings
i “ae — —

FTP. | FTP Upload Test _| Test

FTP IP ADDRESS is set at 61.218.169.200 :
FTP PORT

ACCOUNT
ACCOUNT is set to be dyaco_service(lower case only)
PASSEORD is set at 23751545 »

es SERIAL NUMBER is treadmill serial number to feedback for Error Log, for

example CR800-ENT(5638880810000001).

_—kx
a PATH is Error Log for feedback customer name, for example

dyaco_service/SPIRIT FITNESS

41 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
AUTO UPLOAD ON/OFF

< ON >

Hour Min
+ +
12 00

FTP Upload Test

To turn on or off Error Log feedback function and to set the feedback time.

Press “FTP Upload Test” button to upload information when finish. The green circle represents
upload completed while red circle is for error message or upload failed, please verify for correct
setting or network is not turned on. (When using Error Log feedback function, be aware of if WiFi is
connected.)

TV Setup

TV Setup

Please select the player source such as TV / HDMI mode.

OSD Menu Hit “OSD Menu” button as main menu, and select AUTO/DTV/ATV Tuner then hit “OSD
Enter” button to proceed to next step.

OSD Enter
es §~=Hit “OSD Enter” button to select the country and use the arrow keys to choose. When finish,

hit “OSD Enter” button again to proceed with channel searching. Wait until search ends.

42 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3 %...VHF CH 16

MENU Channel searching

Arrow keys

TV Setup
j 080 Menu |
1 BA ti
mer

mika :  o Pam a

eM : 0 WAR <P>

TV Setup

MRE: Oo WAR

x. VER CH

‘MENU

Scan channel is progressing.

i n. Ss
GSD menuibuttons Update channel list button .Please scan

channels first .

Update Channel List

Tuner £

This button updates the channel list.

This button is for software R&D engineer only.

43 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
BT Setup

BT Setu p Show BT firmware version.

levice.

BT Setup

BT device name/rename button to
change your define BT name.

Version for blue tooth module.

Hit “Clear” button, it clears all messages on the window.

Hit “Pair Mode” button, window displays “Enter pairing mode” and wait for blue tooth
connection.

Deleted Pair

Hit “Deleted Pair” button, window displays “OK” and disconnect blue tooth connection.

Reset

Hit “Reset” button, window displays “Bluetooth device is power on” and blue tooth to
turn on again.

44 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

wodsuelL
pue Huipjojur/bulpjog |j!wpesil “g


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 32 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ATTENTION:
DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING /
TENSION ADJUSTMENTS IS NOT COVERED UNDER THE WARRANTY.

Unplug treadmill before performing any maintenance.

Semi-

Task How To Daily Weekly Monthly Annually Annually
Wipe Down Unit a ees @
water
Clean Under Belt Towel or vacuum ¢
Check Belt Tension/Tracking Feel/Visual 6
Clean Under Motor Cover | Vacuum carefully ®
Check Hardware Wrench @
Inspect for Deck Wear Visual ®
Inspect Drive Belt Visual ®
RECOMMENDED MAINTENANCE OF RUNNING BELT/DECK
Total Using Distance 20,000 Km/ 12,500 Mile 40,000 Km/ 25,000 Mile
Tasks Flipping Deck Replacing Belt and Deck

Note: e Please clean wax on roller during flipping deck or replacing belt/belt.
e The low maintenance (routine monthly cleaning), dual-sided hard wax deck is designed to withstand up to 20,000 Kilometer/12,500 Miles on
each side. If the original side of the deck shows significant wear, it needs to be flipped. Contact your service technician for assistance. Do not
apply any type of lubricant or wax to the surface.

57 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 60 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

AOJO/] QUIJIU] BY] JO UOlJE//E}SU] Ol


=== OCR SUPPLEMENT, PDF PAGE 62 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jpnUudvJA 291ALay’ z9

NVMIVL NISQVW $000602}-}1-0}-Z0P0001}

YSSWNN WWId3s

UO1}B907] JOQUINN [Blas "1


=== OCR SUPPLEMENT, PDF PAGE 63 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS €9

1O1O/\ pieog
SuIoU| JOUSAU|

JO}OW OV

Or
=

G

uoldiudsag jUsUOdWIOY *Z


=== OCR SUPPLEMENT, PDF PAGE 67 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2 Lower Control Board Replacement

4.2.1 As shown in Figure 4.2.1, use the male screwdriver to loosen the eight umbrella head screws
that secure the motor cover to remove the motor cover.

Figure 4.2.1

4.2.2 Remove the lower controller by removing the controller-related line and using the cross
screwdriver to remove the controller as shown in Figure 4.2.2.

BAG
ae

af Vas
re az .
NZ Ke De

Figure 4.2.2

4.2.3 Replace the components and insert the wires back in accordance with 4.2.1 and 4.2.2.

67 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 73 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS cL

7'9'r ounbig

‘dis bulureyss
