<!-- Source: CT1000_ ST8880-ST018-01_service manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

SERVICE MANUAL
            CT1000(2023)

            ST8880-ST018

            ENT Treadmill




      -1-
                                                                     -Contents-
1.Outlines.....................................................................................................................................................- 4 -
2.Electronic Parts .......................................................................................................................................- 6 -

       2.1 Console .........................................................................................................................................- 6 -


       2.2 Controller and Driver parts ......................................................................................................- 6 -

3.Electrical Configurations .....................................................................................................................- 8 -
4.Basic Connections and Wiring...........................................................................................................- 9 -

       4.1 I/O Board Bottom.......................................................................................................................- 9 -


       4.2 DRIVER BOARD PCB Component Locations .................................................................... - 10 -

       ............................................................................................................................................................. - 10 -

       4.3 Controller debugging ............................................................................................................ - 10 -

5. Product Safety Instructions.............................................................................................................. - 11 -

       5.1 Important Safety Instructions .............................................................................................. - 11 -


       5.2 Important Electrical Instructions ......................................................................................... - 11 -


       5.3 Important Grounding Instructions ..................................................................................... - 11 -

6. Error Messages / Troubleshooting ................................................................................................. - 12 -

       6.1 Error Message: INCLINE ERR ................................................................................................ - 14 -

       6.2 Circuit Diagram(230V) ........................................................................................................... - 16 -

       ............................................................................................................................................................. - 16 -

       6.3Setting and Operation for Engineering Mode ................................................................. - 17 -


       6.4Troubleshooting procedure Matrix ..................................................................................... - 19 -

7. Software Update ................................................................................................................................ - 21 -

       7.1Software update manager ..................................................................................................... - 21 -


       7.2Update Firmware ...................................................................................................................... - 22 -

8 . Disassembling and assembling of parts .................................................................................... - 23 -

       8.1 Serial Number Location ......................................................................................................... - 23 -

                                                                                  -2-
8.2 Component Description ........................................................................................................ - 23 -


8.3 Preventative Maintenance .................................................................................................... - 25 -


8.4 Part Replacement Guide ....................................................................................................... - 25 -




                                                               -3-
1.Outlines


    Console




              Hand
              Pulse




                      -4-
                           Incline   AC Motor
          Inverter
                            Motor
           Board


Lower
Control
Board




                     -5-
2.Electronic Parts
2.1 Console




                                          DISPLAY




                                        Safety key




2.2 Controller and Driver parts




                                  -6-
 AC MOTOR             INVERTER




INCLINE MOTOR




                -7-
3.Electrical Configurations
Safety Key        To fits on the Console that activate all functions. If no safety key, console can not be controlled.
Console           Interface that controls all functions of the treadmill.
Main Controller   The circuit board consist of the AC power supply for console、incline driver and AC motor driver, link the
                  console to output appropriate voltages for Incline Interface Board and inverter that control the
                  Treadmill functions.
AC motor          It can change to increase or decrease speed change.
Incline Motor     This is an AC motor. User can to control variable elevation by console within main controller.


GENERAL INFORMATION
Console           Contains Key controls and TFT Display.
Main controller   Include power supply、AC motor、incline motor、inverter control circuit and incline control circuit.

Ac motor          Work voltage: AC 220V~
                  Control speed increases and decreases.
Incline Motor     This is a 230 volt AC motor.
                  Have four wires, red, black, white and green.
                  Has one 3 pins cable of position sensor.
                  If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
                  If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
                  The White wire (COM) is neutral.
                  The green wire is ground.




                                                             -8-
    4.Basic Connections and Wiring
    4.1 I/O Board Bottom




TV CONNECT




                                                                            HDMI CONTACT

                                                                            CONTACT
                                                                              GROUND
Internet CONNECT




                                             SYSTEM CABLE       Key Board
                             C-safe
                   Console                   CONNECT (8 PINS)   CONNECT (20 PINS)
                             CONNECT
                   Power
                   CONNECT




                                       -9-
4.2 DRIVER BOARD PCB Component Locations




4.3 Controller debugging

Indicator     Function             Condition                           Reason                            Solve

     LED
POWER       Controller      If AC voltage is normal, it Voltage is not correct.         Check the supply voltage is 220~230V.
            power           would be always ON. If off, Fuse is blown.                  Replace Fuse.
                            fault condition exists.     Transformer is no good.         Replace controller.
UP          Motion of       Motion of incline motor is Transistor was broken.           Replace controller.
            incline motor   up.                         Relay failed.
DOWN        Motion of       Motion of incline motor is Transistor was broken.           Replace controller.
            incline motor   down.                       Relay failed
START       START           No execution start         Check control cable plugged in   Replace controller.
FAST+       FAST            No execution fast          Check control cable plugged in   Replace controller.
SLOW+       SLOW            No execution slow          Check control cable plugged in   Replace controller.




                                                              - 10 -
5. Product Safety Instructions
5.1 Important Safety Instructions
- To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a
230-volt, 15-amp grounded outlet with only the treadmill plugged into the circuit.
- Do not use an extension cord unless it is a 14 AWG or better with only one outlet on the end. Do not attempt to disable the
grounded plug by using improper adapters or in any way modify the cord outlet.



5.2 Important Electrical Instructions
- Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any ap- pliance with a large motor, the
GFCI will trip often. Route the power cord away from any moving part of the treadmill including the elevation mechanism and
transport wheels..
- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is
first turned on or even during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current
rating) but the circuit breaker on the treadmill itself does not trip, you will need to replace the home breaker with a high inrush
type. This is not a warranty defect. This is a condition we as a manufacture have no ability to control. This part is available
through most electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part #
QO120HM.



5.3 Important Grounding Instructions
- This product must be grounded. If the treadmill should malfunction or breakdown, ground- ing provides a path of least
resistance for electric current, reducing the risk of electric shock. This product is equipped with a cord having an
equipment-grounding plug. The plug must be plugged into an appropriate outlet that is properly installed and grounded in
accordance with all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a
qualified electrician or serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug
provided with the product if it will not fit the outlet; have a proper outlet installed by a qualified electrician. This product is for
use on a nominal 230-volt circuit, and has a grounding plug that looks like the plug illustrated below. A temporary adapter that
looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly
grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplug, or the like, extending from the adapter, must be
connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held
in place by a metal screw.




                                                                   - 11 -
6. Error Messages / Troubleshooting

Error Code List

  Error   Description              Remarks Error
  Code
  0x01    EEPROM Error             By Inverter Error
  0x02    ntcF                     By Inverter Error
  0x03    LE1                      By Inverter Error
  0x04    OE                       By Inverter Error
  0x05    PFCt                     By Inverter Error
  0x06    GF                       By Inverter Error
  0x07    OH                       By Inverter Error
  0x08    OL                       By Motor Error
  0x09    OL1                      By Inverter Error
  0x0A    OLO                      By Inverter Error
  0x0B    PrEr                     By Inverter Error
  0x0C    0C:EEr                   By Inverter Error
  0x0D    LE                       By Inverter Error
  0x0E    ESP                      By Inverter Error
  0x0F    drvF                     By Inverter Error
  0x10    LP                       By Inverter Error
  0x11    HP                       By MCU Board Error
  0x12    Ht                       By MCU Board Error
  0x20    Incline error            By incline motor Error
  0x31    Uart error               By MCU Board Error
  0x40    Speed error              By MCU Board Error
  0x41    Short circuit error      By Inverter Error
  0x42    Motor volt error         By motor line Error
  0x43    Controller error         By Inverter Error
  0x44    External volt error      By Inverter Error




                                - 12 -
Tools Required

A multi-meter.




                 - 13 -
6.1 Error Message: INCLINE ERR
Definition:
During incline action, the display board CPU cannot read the VR value.
Configuration:




Cause:
Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
Explanation
Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which
changes the VR value.
The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it
should be. INCLINE ERR appears on the display.
Action Flow Chart




                                                               - 14 -
   Troubleshooting:

Part                  Troubleshooting
                      1.Inspect whether the 8-PIN cable is connected well.
8-pin cable
                      2.Test by replacing the cable with a good one.
                      1.Press incline UP or DOWN key again, making the incline motor return to its
INVERTER              position.
                      2.If ERR still appears, re-calibrate the incline set.
                      1.Inspect whether the incline motor is stuck.
                      2.Inspect whether the incline gears are cracked.
Incline motor
                      3.Test whether the incline motor has a broken circuit.
                      4.Re-calibrate the incline set.




                                               - 15 -
6.2 Circuit Diagram(230V)




                            - 16 -
6.3Setting and Operation for Engineering Mode
1. Operation for entering engineering mode:
      Press “Welcome” button 10 consecutive repetitions to enter engineering mode.




2. Instructions for each item of operation in engineering mode:
      After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the machine.
      There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection must match the actual
      machine otherwise it will be unable to operate the machine properly.




                                                           - 17 -
About This Machine   Introduction
Type                 There are three modes for the Machine Type Treadmill/ Elliptical/ Upright Bike/Recumbent
                     Bike.
                     Please select for the machine. The selection must match the actual machine otherwise it will
                     be unable to operate the machine properly.
Preferences          Introduction
Beep                 ON/ OFF for beep sound mode.


GS Mode              GS MODE is a setting function for treadmill mode only:
                     GS MODE ON is a function mode that the incline won’t resume. GS MODE OFF is a function
                     mode that the incline will resume. (Under Elliptical / Bike mode, please set it OFF)
Pause Mode           ON/OFF Pause Time Mode. (Minutes：Seconds)

Sleep Mode           ON/OFF for sleep mode The display always lights when turns off. When there is no action for
                     15 minutes after turning on the power, it enters sleep mode.

Workout Time Limit   ON/OFF set limit machine usage time.


Machine Setup        Introduction
Language             To set default language for the first page window. There are 12 languages in the menu.


Date & Time          Set console time system.


Units                English/Metric mode switching.

Video                STB / TV / None mode switching

Protocol             Select “C-SAFE or CAB” button for TV switching box (Choose one is allowed only).

WiFi                 Please hit WiFi button to proceed WiFi setting.

Software             1.   Please keep wired network or connect to wifi network to update software automatically
                     2.   USB update as follows
Firmware             1.   Please keep wired network or connect to wifi network to update software automatically
                     2.   USB update as follows
App Manager          Please keep a wired network or connect to a wifi network to automatically update the app
                     software.

Service              Introduction
Key Test             Press the "button" to start calibration.
                     The corresponding screen display of the physical button flashes.
NFC Test             Please correspond to the location of the NFC sensor, and when the sensor is detected, the
                     information will be displayed on the screen
Drive Motor Test     The used to test the corresponding information of motor kilometers per hour and rotational
                     speed.


                                                - 18 -
 Incline Motor                      Press “Calibration” button to start calibrating.
                                    It calibrates incline motor only. There is no calibration for the tread belt.
                                    (When calibration is completed, calibration window disappears)
 Error Code Log                     Diagnose and save malfunction error messages for technician to inspect the machine and
                                    troubleshooting Press “Error Code Log” button 10 consecutive repetitions to clear the error
                                    message




6.4Troubleshooting procedure Matrix
Condition                            Reason                                            Solve
After turning on power, treadmill    Incorrect input power, varistor is blown          Check the voltage of power is 220V.
has a popping sound.                 broken on controller.                             Replace controller. (On 120Vac electronic
                                                                                       power system need 110V)
When insert safe key, no display     1. Haven’t switch ON/OFF switch.                  1. Switch the AC switch.
on monitor.                          2. Insert the Safe key on wrong position.         2. Insert the safe key on right position.
                                     3. 12 PIN Computer connector not plugged          3. Please check the wire and connect
                                     in properly.                                      again.
                                     4. 12 PIN computer cable is broken.               4. Replace 12 PIN computer cable.
                                     5. Fuse on controller is blown.                   5. Replace fuse or controller.
                                     6. Varistor on controller is blown.               6. Replace varistor or controller.
                                     7. Safety device is broken. (open)                7. Replace safety key device.
                                     8. Other components are faulty.                   8. Replace console.
With no safe key but treadmill       Safety device is broken. (short)                  Replace the safety key device or console.
could display or operate
When press “START”, treadmill        1. Motor M+ or M- wire isn’t connected into       1. Please check and plug again.
doesn’t start.                       right position.                                   2. Replace motor or check the wire and
                                     2. Motor is broken.                               connector if it was broken.
                                     3. Treadmill controller shut down and LED         3. Turn off the ON/OFF switch and turn on
                                     would be ON.                                      power again.
Treadmill stops or shuts off by      1. House breaker tripped.                         1. Reset it.
itself.                              2. Treadmill breaker tripped.                     2. Reset treadmill breaker.
                                     3. Treadmill controller shut down and LED         3. Belt / deck lubrication.
                                     would be ON.                                      4. Turn off the ON/OFF switch and turn on
                                                                                       power again.
After removing safety key,           1. The safety key device is broken.               1. Replace with new safety key device.
treadmill can’t stop.                                                                  2. Replace controller.
                                                                                       3. Replace console.
TFT LCD not bright, incomplete,      1. Connector fall off.                            1. Check connector again.
or imperfect.                        2. TFT LCD light is broken.                       2. Replace with new LCD or console.
                                     3. Power to console too low.                      3. Check power to console.
                                                                                       4. Replace lower controller.

                                                                - 19 -
Condition                          Reason                                         Solve
TFT LCD displays not bright,       TFT LCD displays are broken.                   Replace with new console.
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
Hand pulse lost its function.      1. Hands not on the hand pulse sensors or      1. Two hands hold the hand pulse.
(No pulse displayed on monitor)    only one hand on sensor.                       2. Connect the cable again.
                                   2. The connector of HANDPULSE W/WIRE           3. Replace with new cable.
                                   and Console not connected properly.            4. Replace console or Hand pulse board.
                                   3. The wires got damaged when connecting
                                   the HANDPULSE W/WIRE and Console.
                                   4. Hand pulse board is broken.
Wireless lost its function.        1. Chest belt not worn properly.               1. Check chest belt has proper contact


                                                              - 20 -
Condition                            Reason                                           Solve
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




7. Software Update
7.1Software update manager




                                                                  - 21 -
Image for Treadmill/ Elliptical / Bike Software Update
First, enter the root directory (topmost layer) in the USB Transcend, and then transfer the project data you want to update to the
USB.
Then insert the USB Transcend, click the engineering mode and update the software.




7.2Update Firmware
I




                                                              - 22 -
8 . Disassembling and assembling of parts
8.1 Serial Number Location




8.2 Component Description




                             - 23 -
- 24 -
8.3 Preventative Maintenance
Check if running belt is in the middle.
As shown in Figure 8.31、8.32，check periodically if running belt is in the middle. If not, remove the left and right side
adjustment screw and take out Adjustment Base and then adjust screws to keep running belt stays in middle.




                 Figure 8.31                      Figure 8.32




Check if drive belt has loosened.
As shown in Figure 8.33、8.34 When drive belt slips, please check if belt is too loose. If yes, please remove
M10 caps by using the 17th T-Shirt and then adjust the required belt tension.




               Figure 8.33                       Figure 8.34




8.4 Part Replacement Guide
Console Replacement
As shown in Figure 8.41, use the screwdriver to remove the console chin cover 4 umbrella head screws.



                                                                - 25 -
      Figure 8.41


As shown in Figure 8.42, use the cross screwdriver to remove the 4 umbrella head screws of console, loosen
electronic control cable connector, and then you can remove the console.




           Figure 8.42


Follow Figure 8.41 & 8.42 in reverse to assembly back.


Lower Control Board Replacement
As shown in Figure 8.43, use the screwdriver to loosen the eight umbrella head screws that secure the motor cover
to remove the motor cover.




                                                             - 26 -
      Figure 8.43


As shown in Figure 8.44, remove the lower controller by removing the controller-related line and using the cross
screwdriver to remove the controller.




     Figure 8.44


Replace the components and insert the wires back in accordance with 8.43 and 8.44.


Motor Replacement
Refer to Step 8.43 to remove the motor cover.
As shown in Figure 8.45, use the screwdriver to remove the motor ground wire (green yellow) and the motor
connected to all wires on the control panel.




                                                              - 27 -
    Figure 8.45


As shown in Figure 8.46, use 17th wrench to secure the red arrow and release screws.




       Figure 8.46


As shown in Figure 8.47, use 17th T-shirt to loose four M10 caps and then remove belt and motor to replace motor.




Figure 8.47


                                                            - 28 -
Refer to step 8.47 to assembly motor back. Not secure caps at first. The motor needs to push forward and then hook
back the belt.
Use 17th wrench to adjust the required belt tension, and the value can be adjusted to 80-90BLS. After that secure
the cap.
Connect the motor ground wire and the motor to all the wires on the control panel.




A.C. Input Module Replacement
Refer to step 8.43 to remove the motor cover.
Remove the AC power switch ground wire by using screwdriver as shown in Figure 8.48




Figure 8.48


Remove the AC power switch module with cross screwdriver and switchboard 8 as shown in Figure 8.49.




Figure 8.49


After replacing the new product, assemble it in the order of removal.


Front and Rear Roller Replacement


                                                              - 29 -
As shown in Figure 8.50, use the screwdriver to remove the left and right side adjustment screw.




Figure 8.50


As shown in Figure 8.51, use the No. 8 L-type hex wrench to remove the two rear wheel screws.




Figure 8.51


Refer to Step 8.43 to remove the motor cover.
Refer to Step 8.47 to release the belt. Please refer to 8.50 and 8.51 for the assembly of the left and right chain cover.
As shown in Figure 8.52, remove the front roller with the No. 8 L-shaped hex wrench and remove the front roller.




      Figure 8.52
                                                                - 30 -
Replacement of the new front and rear rollers, and then assembled in the order of removal.
When assembled, adjust the running belt tension, so that running in the set.




Running Deck, Running Belt and Cushion Replacement
Refer to Step 8.50 to Step 8.52 to remove the front and rear rollers.
As shown in Figure 8.53, use a screwdriver to remove the screws on the rear cover.




  Figure 8.53




As shown in Figure 8.54, use the No. 6 L-shaped hex wrench to loosen the 8 screws of the
retaining strip.




  Figure 8.54




                                                               - 31 -
As shown in Figure 8.55, remove the left and right trims in the direction of the arrow.




 Figure 8.55


As shown in Figure 8.56, use the No. 6 L-type hexagonal wrench to remove eight the running plate fixing screws. Set
off the running board and choose to replace the running board or running belt. To change the cushion, as shown in
Figure 8.57, and then remove the 8 buffer and replace with the new ones. Assembled it in the order of removal.




      Figure 8.56                                    Figure 8.57


When assembled, adjust the running belt tension, so that running belt in the set.




Incline Motor Replacement


Refer to Step 8.43 to remove the motor cover.


As shown in Figure 8.58, Figure 8.59, Figure 8.60, move the machine up on the paper tube, use No. 17 opening
wrench 2 pcs to remove the lifting motor screws that are fixed to the lifting frame. Use No. 17 opening wrench 2 pcs
to remove the lifting motor fixed to the main frame of the screw and detachable motor, remove the need to be
associated with the line removed.




                                                               - 32 -
      Figure 8.58                                         Figure 8.59                    Figure 8.60


As shown in Figure 8.61, the lifting motor should be adjusted to a minimum stroke of 315 mm to be set up (Circle to
end and then circle 5 turns in reverse.)




   Figure 8.61


Assembly of the lifting motor should in the order of removal and connected to the control and grounding lines.


Hand Pulse Control Board and Hand Pulse Set Replacement


Refer to Step 8.41 and Step 8.42 to remove the console.
As shown in Figure 8.62, remove the 18 screws from the upper bracket of the fixed bracket with a screwdriver to
remove the bracket cover.




 Figure 8.62


                                                             - 33 -
As shown in Figure 8.63, use the hexagonal wrench to remove the four hexagonal screws, you can replace the
hand-held group, assembled it in the order of removal.




Figure 8.63




                                                            - 34 -


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 66 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
-Contents-

TL OUTINGS... cece ccceeeccsseescsseeseesecseesecsessecnsssecsaeesesaecseaecaessecsassecsaeeaesaecseaecaessecaaseeceasesesaecseeaecaesaesaaseneaaees -4-
QZ.EIO@CHOMIC PITS ...........ceeceseesceseescesecseesecseesecseeseceseescsaecsessecsessecaesseceaeeseesecsessecseseeseaseceaeesessecaesaesaeseeaeees -6-
2.1 CONSOME .o.ceccccccccssscsesesesescscscscsessssvsssesesesesesasscsesessvassesssesesesassesesesasasassesesesesassesesssasasseseeeeesecaeaeneees -6-
2.2 Controller ANd Driver Parts ..........ccccccceesesesseseseseeeseeeseseseseeseeeeeececeeeesesesesesaeaeseeeeeseseeeensneneneass -6-
3. Electrical COMPIQUIATIONS ...0..... ee c ee cceteesceseeseesecseesecseesecaseseceseceesaecaessecsecsecseseseaeeesaecaesaesaeseessaseeeees -8-
A.Basic CONNECTIONS ANd WiTING.............ccccccccesecsesecseesecseeseceeeeeceseceessecseesecseseecaasseseaeeeessecsesaesaesreaeees -9-
4.1 1/0 Board BOttOM......ccccccccccscscscscsesssssscsesesssesecscscsessssvsssssesesesesassesesesasasssassecesesacscsesasaacseseeeeesess -9-
4.2 DRIVER BOARD PCB Component LOCatIONS ..........eecececceeeeteteseseseeeeeeeeeteeeeieatsnsneteaeeeeteees -10-
Leen cece cece nea eeeeeEEEEGEAEAAA AA EEEEEEGEAEAAAAAAEEEEESEAEEAAAAEEEEEESEAEAAAAAAAEEEEEEESEEEAAIASSEELEEESEA;AAA ASSES EEESEA;EAE GASSES EE ESCA EEEE AES EEEEEES -10-
4.3 Controller AEDUGGING «00... eseecessesssesseseesesssesseseesenssesneneeeenesesneaeeeeeeaesueaeeeeesaesnsneeeesansnsneeteeeens - 10-
5. Product Safety IMstructions. ............ cc ccccccseescseescesesseesecseesecsececeaseeceaecseesecseseesaeseeceaseeeeseseesaeeaeeaeeas -11-
5.1 Important Safety INStrUCTIONS ........cecseeseeseseseeseseseesesessesseseeneeesaeeneeesaesneeteesseaeeessneneeeentenees -11-
5.2 Important Electrical INStrUCtIONS ......... ce eeceeceetesesesesseseseeeeeesesesesesseeaeaeeeeteneeeaeatenseseneeeeeeees -11-
5.3 Important Grounding INStrUCTIONS 0.0... seteseeseeeesesesesneeeeeeseaesneneeteecatssneeteeeaseneneeees -11-
6. Error Messages / TrOUDIESNOOTING............ cece ccceseesceseessesecseesecseeseceseeeceaecsessecseseecaasecaeeseeaecaeeaeeas -12-
6.1 Error Message: INCLINE ERR... ccs esessecsesseseeesessesesesscseeceeeseeessasansnsnsneaeeceeeeeeesatanenseeneas -14-
6.2 Circuit Diagrarn(230V) .......eeseceecececseseseseseeseseseseecesescsesesesesscaeaceeecesescseaesnssaeacseeeeteesesaeaneeeenees -16-
Leen cece cece nea eeeeeEEEEGEAEAAA AA EEEEEEGEAEAAAAAAEEEEESEAEEAAAAEEEEEESEAEAAAAAAAEEEEEEESEEEAAIASSEELEEESEA;AAA ASSES EEESEA;EAE GASSES EE ESCA EEEE AES EEEEEES -16-
6.3Setting and Operation for Engineering MOde .........ceessesssecseeseseeeeseeseeeeseeseseeseeneeeeneenees -17-
6.4Troubleshooting Procedure Matrix oo... seesseeecseeeeseeseeeeeessseeseeeseeassesseeseesassnsneeteeeaseneneeees -19-
7. SOFTWALE UP dte ooo. cc cccccccsceessessecseesecseesecseeecaecsecsecsessecsesseseaseesaeceeesecaeseecaaseeseaseeseaeeaseaesaeeats -21-
7.1Software Update MANAGE .........ecesecceseeseeseeeeseeseeeesesseeecsesneeeesesneeeeaesneeeeaesueateessnsaeeecaneneeeeneenees -21-
7. QU pdate Firmware .........cecccesesssseseseeseeescseseseseeseseseeeecesescaesessesseacaceeeceseecseaesesusaeaceeeeeeeneesaeansnseeees -22-
8 . Disassembling and assembling Of Palts «0.0.0... ec cccseeeecsseescsseescesecseesecseseecseeeecseeeeesaeeaeeaeeas -23-
8.1 Serial NUMber LOCATION... cece esesssseseseeseseseseseseseseseseseseseseseseseseseseseseseeeeseeeeeeeeeeeeeeeseees - 23 -


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
seeeaeeeeeeeneecaaecsaeeeseeeeneesaaecsaeceseeseneesaaeceaeeeseeseaeesaaeseaeeeeeseaeesaaeseaeees adUeUAaIUIe| BAeJUaAAald €°8

apind JUuaWade|day Wed 7g

Uuol}dludsag JUaUOdWOD 2°g


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOMOd

LOANNOO
ayes-—

(SNId 02) LOANNOO (SNId 8) LOANNOO gjOsu0D

pieog Aey A1gVvVO WALSAS

LOANNOO JeUJ9}U|

Wha

wo}10g pseog O/I L'v
BulllM PUD SUO}DaUUOD SISDg'p


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6. Error Messages / Troubleshooting

Error Code List

Error |Description Remarks Error
Code

0x01. |EEPROM Error By Inverter Error
0x02 _—s[ntcF By Inverter Error
0x03 |LE1 By Inverter Error
0x04 |OE By Inverter Error
0x05 = |PFCt By Inverter Error
0x06 = |GF By Inverter Error
0x07 |OH By Inverter Error
0x08 = |OL By Motor Error

0x09 |OL1 By Inverter Error
Ox0A jOLO By Inverter Error
OxOB_ _|PrEr By Inverter Error
Ox0C |0C:EEr By Inverter Error
OxOD  |LE By Inverter Error
OxOE |ESP By Inverter Error
OxOF = |drvF By Inverter Error
0x10 =|LP By Inverter Error
0x11 = |HP By MCU Board Error
0x12 s/Ht By MCU Board Error
0x20 {Incline error By incline motor Error
0x31 = |Uart error By MCU Board Error
0x40 |Speed error By MCU Board Error
0x41 =‘ [Short circuit error By Inverter Error
0x42 = [Motor volt error By motor line Error
0x43 [Controller error By Inverter Error

0x44 _—— [External volt error By Inverter Error

-12-


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.1 Error Message: INCLINE ERR

Definition:
During incline action, the display board CPU cannot read the VR value.

Configuration:

DISPLAY BOARD ‘ UPDOWNKEYS |, payww cys

4 4

INCLINE 7 INCLINE
VR a UP/DOWN
VOLTAGE = SIGNAL

INCLINE
MOTOR
DRIVER BOARD — VR VOLTAGE INCLINE VR SET

NY

C) INCLINE DOWN LED
OC) INCLINE UP LED

Cause:

Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.

Explanation

Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which
changes the VR value.

The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it
should be. INCLINE ERR appears on the display.

Action Flow Chart

-14-


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cc DISPLAY BOARD 5

i

DRIVER BOARD

DURING UF ACTION.
Ci £8? 81s TSI ee
oS FACE Ina REASES

IN FStOeWwN Ac ric

DOWN LED 1 eGHTS INCLINE — MN =
VM TrA<c&s Ee DWSECReEASES
a
i
INCLINE MoToOoR
— ™N a on a
2
DOWN LED LicHtrs. ™~ o>

INCLINE LOWERS?

w
! ¥

wae a SHOW INCLINE E2
C NO ERR MESSAGE ») C Saree >

Troubleshooting:
Part Troubleshooting

1.Inspect whether the 8-PIN cable is connected well.
8-pin cable

2.Test by replacing the cable with a good one.

1.Press incline UP or DOWN key again, making the incline motor return to its
INVERTER position.
2.If ERR still appears, re-calibrate the incline set.

1.Inspect whether the incline motor is stuck.
2.Inspect whether the incline gears are cracked.
3.Test whether the incline motor has a broken circuit.
4.Re-calibrate the incline set.

Incline motor

-15-


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 71 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.2 Circuit Diagram(230V)

ST8880-ST018 230V
TREADMILL CIRCUIT DIAGRAM

TFT
DC Power, (+

C-SAFE —-—_——___

| 6-PIN Upper Main Control Wire
co
ae |
WS S ACK
Kile WN
+. iy

HDMI —=—————-

AC POWER INPUT

| All} = Rv45
PLUG TV
Cable RF
Connector
Power cable W t
~ uo
Connector Front Transfer Board
BREAKER AC SWITCH
Teer
SOCKET
P| 1] arty can
Grounding TeDELTA Inverter bridge board 1
Control Wire
TFT DC DELTA
= IN Control Wire
Grounding i INCLINE MOTOR
Nin Lin Lout H F :
FILTER = i ti
Nout § E 5
6 & a
< <=
Nin Nout 9 alee |
Choke z GROUND WIRE
L_] 3
fforweter DC To Inverter bridge | i
pidge boss QUT Control Wire
cable DOWN
Grounding _-—ol..,, Inverter UP
——Hl COM
AC MOTOR
UVW G
| Optically Coupled Sensing
if GROUND WIRE

-16-


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.3Setting and Operation for Engineering Mode
1. Operation for entering engineering mode:

Press “Welcome” button 10 consecutive repetitions to enter engineering mode.

Maintenance Mode

Bhd Thee he te fopte ee

2. Instructions for each item of operation in engineering mode:
After entering engineering mode, first priority is to enter “About This Machine” mode to set the type of the machine.
There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The selection must match the actual

machine otherwise it will be unable to operate the machine properly.

Maintenance Mode 4 To Android

About This Machine Preferences Machine Setup Service

Treadmill v

Reset Odometer S

Display Brightness

@

-17-


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Condition Reason Solve

(No pulse displayed on monitor) 2. Distance is too far and exceeds range of with skin and is oriented correctly.
receiver. 2. User chest belt in front of console
3. Chest belt battery is weak or dead. within 3 feet.

3. Replace with new lithium battery type is

CR2032.

Chest belt too close to the Weak battery. Replace with new lithium battery with
treadmill. type cR2032),
Tread belt does not runincenter. Tread belt tension not even across tread See treadmill belt adjustment

belt.
Tread belt hesitates while being Insufficient lubricant on tread belt. See treadmill belt lubrication
stepped on. Tread belt tension insufficient
Black particles collecting under Drive belt is breaking in. Vacuum under treadmill periodically.
treadmill.
Noise under motor cover. 1. Worn brushes or bearings on motor. 1. Replace with new motor.

2. Front roller bearings are defective. 2. Replace with new front roller.

3. Drive belt is misadjusted (too tight or too 3. Adjust motor position.

loose).
Noise in the rear of the 1. Rear roller bearings are defective. 1. Replace with new rear roller.
treadmill. 2. Rear roller misaligned. 2. Adjust rear roller position.

7. Software Update

7.1Software update manager

Software

Automatic Update

TFT OS

LWR

-21-
