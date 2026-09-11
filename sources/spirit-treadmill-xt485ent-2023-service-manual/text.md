<!-- Source: XT485ENT Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XT485 ENT
    Service Manual




1             Service Manual
--------------------------------------Table of Contents-------------------------------------------
                         1. Treadmill Outlines
                         2. Electronic Parts
                             2.1 Upper Controllers
                             2.2 Lower Controller and driver
                         3. Electrical Configuration
                         4. Treadmill Operation
                         5. Unit Block Diagrams
                         6. Basic Connections and Wiring
                             6.1 Display Board Wire Connections
                             6.2 Display Board PCB Component Locations
                             6.3 Driver Board Wire Connections
                             6.4 Driver Board PCB Component Locations
                             6.5 Driver Board LED Indicator Locations
                             6.6 Controller Indicator LED Debugging
                             6.7 Driver Board Function
                         7. Product Safety Instructions
                             7.1 Important Safety Instructions
                             7.2 Important Electrical Instructions
                             7.3 Important Grounding Instructions
                         8. Treadmill Error Messages / Troubleshooting
                             8.1 Error Message: E0
                             8.2 Error Message: E1
                             8.3 Error Message: E2
                             8.4 Error Message: E3
                             8.5 Error Message: E4
                             8.6 Error Message: E5
                             8.7 Error Message: E6
                             8.8 Error Message: E7
                             8.9 Error Message: E9
                             8.10 Calibration Procedure
                             8.11 Circuit Diagram
                         9. Treadmill Folding/Unfolding and Transport
                         10. General Maintenance
                                                             2                               Service Manual
    10.1 Tread Belt and Deck
    10.2. Service Troubleshooting Checklist – Diagnosis Guide
11. Installation of the Incline Motor
12. Disassembling and assembling of Parts
    12.1 Lower Controller Replacement
    12.2 Console Replacement
    12.3 Motor Replacement
    12.4 Breaker Replacement
    12.5 AC Power Switch Replacement
    12.6 Front/ Rear Roller Replacement
    12.7 Running Deck/ Belt & Cushion Replacement
    12.8 Speed Sensor Replacement
    12.9 Incline Motor Replacement




                                      3                         Service Manual
1. XT485 ENT Treadmill Outlines




               4                  Service Manual
                                       Driving Motor


                   Incline Motor

Lower Controller




                                   5                   Service Manual
2. Electronic Parts




         6            Service Manual
2.1 Upper Controllers


                                                Cooling FAN

                                  Speaker

                                                               Speed control
                                                               on handrail




                                                       Incline control
                                                       on handrail




                        DISPLAY




                                            7                             Service Manual
2.2 Lower Controller and Driver




                                                                                            INCLINE MOTOR




                        Motor Controller

                                                                                 DC MOTOR




                                           Driver system (Motor/Controller/Incline Motor)



                                                                 8                            Service Manual
2. Electrical Configurations




             9                 Service Manual
SAFETY KEY:
To fit on the console that activates all function, if no safety key, the console cannot be controlled.

CONSOLE:
Interface that controls all functions of the treadmill.

MAIN CONTROLLER:
The circuit board consists of the DC power supply for console、incline driver and DC motor driver, link the console to output appropriate voltages for
motor that control the treadmill functions.

TREADMILL MOTOR:
This is a variable speed for DC motor. To control the 0 – 180 DC volts（To control 0-90 DC voltages on 120Vac electronic power system）on the main
controller, it can to increase or decrease speed of running belt.

INCLINE MOTOR:
This is an AC motor. User can control variable elevation by console within main controller.




                                                                         10                                                       Service Manual
GENERAL INFORMATION
CONSOLE

 The console comprised of key controls and 10-inch screen display.
 Main controller Include power supply 、motor driver control circuit and incline control circuit.

TREADMILL MOTOR

It’s a variable speed on 0-90 volt DC motor. (0-180 volts DC motor on 220Vac electronic power system)
Have three wires red, black and green.
If there is DC voltage on the Red (white) wire (M+) the treadmill motor will turn clockwise.
If there is DC voltage on the Black wire (M-) the treadmill motor will turn counter-clockwise.
When the higher voltages, the speed is more faster.
The green wire is grounding.

INCLINE MOTOR

 This is a 120 volt AC motor. (220 volts AC motor on 220Vac electronic power system)
 Have four wires, red, black, white and green.
 Has one 3 pins cable of position sensor.
 If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
 If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
 The White wire (COM) is neutral. The green wire is ground.




                                                                           11                           Service Manual
4. XT485 ENT Treadmill
   Product Operation




          12             Service Manual
Display Windows
                  10” TOUCH SCREEN LAYOUT




                                            13   Service Manual
Operation
Window Display Mode
   OFF Mode
        When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode and all windows will appear blank.
   READY Mode
        When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program profile name and cycle. Press START
   button to start treadmill on Manual Mode.
   SLEEP Mode
        In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
   RUN Mode
        In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly and enter OFF Mode.

Function
   SPEED
       Display the current speed in mile per hour (kilometer per hour).
       DISPLAY range is 0.0 to 99.9
       WORK range is 0.5~12.0 mph (1.0 ~ 18.0 kmph)
       Press “FAST” or ”SLOW” to adjust speed, each increment and decrement is 0.1 km/h(mph).
   INCLINE
       Display the incline position from 0 to 15
       DISPLAY range is 0 to 999.
       WORK range is 0.0 to 15.0.
       INCLINE preset value is 0.0.
       Press “UP” or ”DOWN” to adjust incline, each increment or decrement is 0.5.
   TIME
       TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time then timer is COUNT DOWN.
       DISPLAY range is 0:00 to 999:99.
       COUNT DOWN setup range is 10:00 to 99:00.
       When TIME is set, the count will go to zero.
       In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will continue count up time.


                                                                        14                                                          Service Manual
DISTANCE
    Display the current distance in kilometer or Mile.
    DISPLAY range is 0.00 to 99.99.
    WORK range is 0.00 to 99.99.
CALORIES
    Displays the cumulative calories burned at any given time during your workout.
    DISPLAY range is 0 to 999.
    WORK range is 0 to 999.
PULSE
    Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
    DISPLAY range is 0 to 999.
    WORK range is 50 to 200 BPM.
    In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds then display value will become “0 ”.
PACE
    It means: How long will takes to walk (or run) per each Km or Mile at current speed?
    The unit is min/Km or min/Mi.
    DISPLAY range is 00：00 to 99：99.
    WORK range is 00：00 to 99：99.




                                                                        15                                        Service Manual
Function Button Locations




        Quick SPEED & INCLINE
               BUTTONS
                                                                 Function Buttons
                                                                 Operation control




                                                                      Disable Button
                                                                      On Handrail
                                                                      SPEED/INCLINE Switch
                                                                      ON or OFF
                Fan Button
        Cooling fan switch on or off           Safety Key
                                            Emergency function



                                       16                                            Service Manual
Function Button In Main Mode
   READY MODE
      SAFETY KEY: Set safety key in right position to power on the computer. When safety key is pulled away from its position, the computer will be
      automatically shut down.
      STOP Button: Non-function.
      START Button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on window
      display, then machine starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill starts at program preset value in PROGRAM.
      FAST Button：If user doesn’t enter a setting then this button is non-functional.
      SLOW Button：If user doesn’t enter a setting then this button is non- functional.
      Quick SPEED & INCLINE Button：Non-function.
      FAN BUTTON：It can to control ON/OFF for the fan.
      HANDRAIL SWITCH CONTROL Button：It can turn the handrail switch off.




                                                                        17                                                           Service Manual
RUN MODE
  SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down.
  STOP Button: press “STOP” button to stop treadmill.
  START Button: non-functional.
  FAST Button: Press the button to increase your speed and each increase is 0.1kph(0.1mph). If button is pressed continuously then speed increases
  to MAX SPEED quickly.
  SLOW Button: Press the button to decrease your speed and each decrease is 0.1kph(0.1mph). If button is pressed continuously then speed
  decreases to MIN SPEED quickly.
  UP Button: Press the button to raise position and each increase is 0.5, the maximum incline position is 15.
  DOWN Button: Press the button to lower position and each decrease is 0.5, the minimum incline position is 0.
  Quick SPEED & INCLINE Button：You are able to set your speed and incline settings quickly by using the quick keys on the console. Just press
  either Speed or Incline, then select either 2 or 3 digits and the treadmill will automatically adjust to that value. This saves time because you don’t
  have to press and hold or hold a button down until reaching the desired value.
  FAN Button: It can to control ON/OFF for the fan.
  HANDRAIL SWITCH CONTROL Button：It can turn the handrail switch off.




                                                                       18                                                             Service Manual
5. XT485 ENT Treadmill
 Unit Block Diagrams




          19             Service Manual
Treadmill Configuration




                          20   Service Manual
6. XT485 ENT Treadmill Basic Connections
              and Wiring




                   21                      Service Manual
6.1 Display Board wire Connections




                                     22   Service Manual
6.2 Display Board PCB Component Locations

   PCB Board Top




                                            23   Service Manual
PCB Board Bottom




                   24   Service Manual
6.3 Driver Board Wire Connections




                                    25   Service Manual
6.4 Driver Board PCB Component Locations




                                           26   Service Manual
6.5 Driver Board LED Indicator Locations




                                                POWER LED
                                                IT'S MUST BE CONNECT
                                                CONSLOE AND SET SAFETY
                                                KEY TO CHECK




                                           27                            Service Manual
6.6 Controller Indicator LED debugging

 Indicator          Function                    Condition                                 Reason                        Solve
    LED
POWER      Controller power    If DC voltage is normal, it would be always   Voltage is not correct.   Check the supply voltage is 120Vac.
                               ON. If off, fault condition exists.           Fuse is blown.            (on 220Vac electronic power system
                                                                             Transformer is no good.    need 220Vac)
                                                                                                       Replace Fuse.
                                                                                                       Replace controller.




                                                                  28                                                 Service Manual
6.7 Driver Board function




                            29   Service Manual
7. Product Safety Instructions




              30                 Service Manual
7.1 Important Safety Instructions
  - To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 120-volt, 15-amp
    grounded outlet with only the treadmill plugged into the circuit.【220Vac electronic power system is 220-volt, 10-amp】
  - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
    improper adapters or in any way modify the cord outlet.
7.2 Important Electrical Instructions
  - Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any ap- pliance with a large motor, the GFCI will trip often.
    Route the power cord away from any moving part of the treadmill including the elevation mechanism and transport wheels..
  - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is first turned on or even
    during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill
    itself does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a
    manufacture have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online
    at www.squared.com part # QO120HM.
7.3 Important Grounding Instructions
 - This product must be grounded. If the treadmill should malfunction or breakdown, ground- ing provides a path of least resistance for electric current,
   reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
   appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
 - DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or serviceman
    if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the outlet; have a
    proper outlet installed by a qualified electrician. This product is for use on a nominal 120-volt (on 220Vac electronic power system need 220Vac ) circuit,
    and has a grounding plug that looks like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to
    connect this plug to a 2-pole receptacle as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until
    a properly grounded outlet, (shown below) can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the
    adapter, must be connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held in
    place by a metal screw.




                                                                             31                                                             Service Manual
      8. XT485 ENT Treadmill
Error Messages / Troubleshooting




               32              Service Manual
Error code items：
      Error Message   Explain
             E0       The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed.
             E1       Display board CPU did not receive the RPM signal.(only calibration)
             E2       Treadmill motor is over load.
             E3       The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.
             E4       Treadmill motor wires or volt possible abnormal.
             E5       Communication single is abnormal.
             E6       Lower Control board possible broken.
             E7       Incline calibration error
             E9       Speed calibration error
   Prepare：

                                                      Picture                               Tool name




                                                                                            Multi-meter




                                                                          33                                                  Service Manual
8.1 Error Message：Display appears「PLEASE REPLACE THE SAFETY KEY」on the screen. (E0)
 Definition: Display board CPU did not receive the Safety device signal.

 Configuration：                                                                  Screen display：




 Troubleshooting


 Part                       Troubleshooting
 Safety key /               1. Safety key necessary be set.
 Safety Switch Module       2. Check Safety Switch Module’s Pin place on the console board.




                                                                            34                     Service Manual
8.2 Error Message：E1
Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM sensor, but
when the Calibration which it is a necessary.)

 Configuration：
Cause of E1




                                   Send and receive speed
                                   signal via TX/RX of
                                   5-pin Main wire.




                                                                            35                                                           Service Manual
The motor doesn’t working：E1 appears.

  ■   Explanation:
      ◆ The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor
          signal.
      ◆ Configuration：




                                          Send and receive
                                           speed signal via
                                           TX/RX of 5-pin
                                           Main wire.




                                                                         36                                                         Service Manual
E1 solution follow chart




                           37   Service Manual
E1 solution follow chart – check RPM sensor device procedure：




                                                                38   Service Manual
•   Assembling the speed sensor
    1. Remove the motor cover hood.
    2.   The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will have a belt around it that also goes
         to the motor). The speed sensor is small and black with a wire connected to it.
    3.   Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley; make sure the
         sensor is aligned with the magnet. There is a screw that holds the sensor in place that needs to be loosened to adjust the sensor. Re-tighten the
         screw when finished.




                                                                              39                                                              Service Manual
E1 issue troubleshooting form

    E1
                              Possible cause                             Things to check                                       Solution
    message

                 The upper console board       hasn't    check the speed sensor cable is in good            Make sure the good connection for cables
 The motor       receive any speed signal for 8          connection
 cannot move     seconds



                 The speed sensor didn't detect signal Check the gap between speed sensor and               To keep the gap-distance less than 3 mm.
                 completely.                             magnet.



                 Defective sensor or bad cable           Check if the sensor and cables are circuit short   Change the sensor or cables.
                 connection.                             damaged.




8.3 Error Message：E2/OVER CURRENT
   Definition: When lower board detect over current, then display appear “E2”.
               The means is lower board need to protect itself and motor. Prevent lower board and motor is burned.
   Solve over current: First, check whether smear Silicone oil or not. And then when during the using treadmill, do not block belt running.
                           If aforementioned did not process problem, suggest Replacing lower control board or Replacing motor.




                                                                            40                                                             Service Manual
8.4 Error Message：E3
   Definition: The console board is not detecting the VR voltage value, or the voltage value hasexceeded the range. ” E3 ” appears on the display.
   Configuration：




Case of E3
Incline VR value exceeds the range. E3 appear on the display.
       ◆     Incline motor isn’t operation up or down, making the VR value exceed the range.
       ◆     After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so E3 appears.
       ◆     Action Flow Chart

                                                                             41                                                          Service Manual
42   Service Manual
Troubleshooting


 Part             Troubleshooting
 Incline VR       1. Reconnect VR wire.
                  3. Inspect whether the incline wires are broken or disconnected.
 Display board
                  1. Inspect the wire connections.

                  2. Test whether the VR voltage varies at the incline wire terminal.

 5-pin cable      1. Inspect the wire connections.
                  2. Inspect whether wire are broken or crimped.
                  3. Replace the wires and test again.
 Driver board     Replace the driver board.




                                                                         43             Service Manual
Test configuration. The console to driver board connector pin define function




                                              1,
                                              2,
                                              3,
                                              4,
                                              5,




                                                                44              Service Manual
Test Configuration. Incline motor control function relate parts location




                                                                           The position sensor wires
                                                                           Black = Ground,
                                                                           White = Position signal,
                                                                           Red = 5vdc,
                                                                           (0~5v depending on incline position)




         WHITE-NEUTRAL

              RED-UP

          BLACK-DOWN




                                                                  45                                              Service Manual
Test Procedure：

   1.   Run calibration again.
   2.   Does the incline motor move at all?
   3.   If no, do the Up/down lights on the incline board light?
   4.   If they light, do the relays click on?
        ◆     If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red)
              or down (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the
              mains voltage ~ 110VAC (230VAC). If the voltage is present but the motor doesn’t move, then the motor is bad.
        ◆     If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).
   5.   If the motor moves, is there a sensor reading on console?
        ◆ The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0 for lowest incline. The Incline window is a counter that is
               showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the position
               sensor wiring or circuitry.
        ◆ If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
               Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
               If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
        ◆ If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black
               and red wire and there should be a voltage
              between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical, as long as it’s
              somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register then
              there may be a bad wire connection between the potentiometer and the console.

   6.   Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
   7.   If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board.
        There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.
        The only problems that are possible are a bad solder joint or broken circuit on the board.
        ◆     Console connector wiring, these connections are the same on the incline board and at the console.
                     ■     Pin 1 = ground
                     ■     Pin 2 = position signal 0~5vdc
                      ■     Pin 3= 5vdc
   8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the incline board then check
        the entire cable from incline board to console for cuts or bad connection at the inwire connectors.
   9.   If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.


                                                                                           46                                                                         Service Manual
Error Message：E3 / INCLINE ERR
Definition: During incline action, the display board CPU cannot read the VR value, so E3 appears.
Configuration：




                                                                             47                     Service Manual
 Cause of INCLINE E3

     Press the incline UP/DOWN key. The incline doesn’t operate. E3 appears on the display.
Explanation
         When press incline key, the display board CPU reads the incline VR value. If there is no VR value change to the CPU, the incline is not operating, and
then appear E3 appears on the display.
 Action flow chart：




                                                                              48                                                             Service Manual
Troubleshooting
Part            Troubleshooting
Display board   1. Press Incline UP key, or Press Incline DOWN key. If not as above, inspect the cable and connections.

5-pin cable     1. Inspect whether the 5-PIN cable is connected well.
                2. Test by replacing the cable with a good one.
Incline cable   1. Inspect whether the incline power wire and incline VR cable is connected well.

Driver board    1. Press Incline UP or DOWN key again, making the incline motor return to its position.
                2. If ERR still appears, re-calibrate the incline set.
                3. If it still have problems, replace the driver board to check.

                 1. Inspect whether the incline motor is stuck.
                 2. Inspect whether the incline gears are cracked.
Incline motor    3. Test whether the incline motor has a broke circuit.
                 4. Recalibrate the incline motor.




                                                                         49                                               Service Manual
 8.5 Error Message：E4
 Definition: Motor power wire error.
 Configuration：




Cause of E4:
    Power wire of Motor does not insert lower controller.

 Troubleshooting
 Part                        Troubleshooting
 Lower controller            Insert power wire of motor.
 Motor                       Replace Motor.
 Display board               Replace upper control board.

                                                            50   Service Manual
 8.6 Error Message：E5
        Definition: it is a Poor communication, between the console and lower controller is poor communication, almost it is bad on a main control wire, but
        also possible bad at console board or lower controller.
        Configuration：




Cause of E5:
 The main control wire is possibly broken. But E5 maybe has another problem, like component of lower controller or console board.

 Troubleshooting
 Part                        Troubleshooting
 Lower controller board      Replace main control wire.
 Main control wires          Reinsert main control wire.
                             Replace main control wire.
 Display board               Replace upper control board.

                                                                             51                                                           Service Manual
8.7 Error Message：E6
 Definition: The lower controller component is fault.
 Configuration：




Cause of E6:
        The lower controller component is fault, Like Transistor、IGBT、control module…etc.



 Troubleshooting
 Part                        Troubleshooting
 Lower controller            Insert power wire of motor.
 Display board               Only Replace upper control board.


                                                                           52               Service Manual
8.8 Error Message：E7
Definition: Incline Calibration Error.
 Cause of E7:
        When machine works fail by incline motor at Calibration time, the consoledisplay board will jump to E7 error.

Troubleshooting
 Part                   Troubleshooting
 Wall outlet            Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or 220AC or not. And the voltage
                        whether stable or not.
 Incline motor           Step 1: Checking wiring to eliminate poor wire connecting between incline motorand controller as illustrated below.
                         Step 2: If wiring is good, then:
                         a) Replace controller first.
                         b) if a) doesn’t fix the issue then replace Incline Motor finally.




                                                                                 53                                                      Service Manual
8.9 Error Message：E9
Definition: Speed Calibration Error.
 Cause of E7:
        When machine works fail by motor at Calibration time, the console display board will jump to E9 error.

Troubleshooting
 Part                   Troubleshooting
Controller               Step 1: Checking wiring to eliminate poor wire connecting between Driving motorand controller as illustrated below.
                         Step 2: If wiring is good, then:
                         a) Install Speed Sensor to Calibrate Speed as ERROR E1 mentioned.
                         b) If a) doesn’t work, replace controller then do calibration again.
                         c) If b) doesn’t fix the issue then replace driving Motor then does calibration againfinally.




                                                                               54                                                        Service Manual
8.10 CALIBRATION PROCEDURE
1. Choose settings function on screen bottom right corner then click on “Software” button.




2. On the screen will be show software version and click on “software version C006_XT485…” to continue five times for this step.




                                                                            55                                                     Service Manual
3. You need to enter password 20160620 to confirm before enter the calibration screen.

4. Choose CONTROLLER function, set the units for imperial or metric.




5. If you want to calibrate speed, click on “Start calibrating speed” to mark on screen bottom left corner. No choice this item, only incline level calibration.
  Click on CHECK SPEED to begin calibration.
6. The process is automatic; the speed will start up without warning, so do not stand on the belt. When calibration be finished on calibration successfully
   screen, click on reboot to exit.




                                                                                56                                                             Service Manual
8.11 Circuit Diagram




                       57   Service Manual
9. Treadmill Folding/Unfolding and
             Transport




                58               Service Manual
FOLDING INSTRUCTIONS
 Do not attempt to move the unit unless it is in the folded and locked position. Be sure the power cord is secured to avoid possible damage. Use
 both handrails to maneuver the unit to the desired position.

  TO FOLD THE TREADMILL
   Make certain the treadmill is at minimum incline. Lift the treadmill running deck
   until it is secured by the locking telescoping tube assembly in center back of base.


  TO UNFOLD THE TREADMILL
   Apply slight forward pressure* on the treadmill running deck with one hand. Pull down on the
   unlocking lever and slowly lower the running deck to the floor. The deck will lower
   unassisted when it reaches about waist high.
        *At the rear roller area to relieve pressure on the locking system.




                                                                               59                                                     Service Manual
10. General Maintenance




           60             Service Manual
 10.1 Tread belt and Deck
 Your treadmill uses a very high-efficient low-friction bed. Performance is maximized when the bed is kept as clean as possible. Use a soft, damp cloth or
 paper towel to wipe the edge of the belt and the area between the belt edge and frame. Also reach as far as practical directly under the belt edge. This
 should be done once a month to extend belt and bed life. Use water only - no cleaners or abrasives. A mild soap and water solution along with a nylon
 scrub brush will clean the top of the textured belt. Allow the belt to dry before using.


 Belt Dust - This occurs during normal break-in or until the belt stabilizes. Wiping excess off with a damp cloth will minimize buildup.


 General Cleaning - Dirt, dust, and pet hair can block air inlets and accumulate on the running belt. On a monthly basis: vacuum underneath your
 treadmill to prevent buildup. Once a year, you should remove the black motor hood and vacuum out dirt that may accumulate. UNPLUG POWER CORD
 BEFORE THIS TASK.


 BELT ADJUSTMENTS:
 Tread-belt Tension Adjustment - Adjustment must be made from the rear roller. The adjustment bolts are located at the end of the step rails in the end
 caps, as noted in diagram below.




Tracking / Tension                                                                       Tracking / Tension
Adjustment                                                                              Adjustment
                      Note: Adjustment is through small hole in the end cap.


                                                                                61                                                          Service Manual
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
A 10 mm Allen wrench is provided to adjust the rear roller. Make tracking adjustments from the left side only. Set belt speed at approximately 3 to 5
kph.
Remember, a small adjustment can make a dramatic difference!


Turn the bolt clockwise to move the belt to the right. Turn the bolt only a 1/4 turn and wait a
few minutes for the belt to adjust itself. Continue to make 1/4 rotation turns until the belt
stabilizes in the center of the running deck.

The belt may require periodic tracking adjustment depending on use and walking/running
characteristics. Some users will affect tracking differently. Expect to make adjustments as required to center the tread-belt. Adjustments will become
less of a maintenance concern as the belt is used. Proper belt tracking is an owner responsibility common with all treadmills.
                                                                              62                                                             Service Manual
ATTENTION:
DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING /
TENSION ADJUSTMENTS IS NOT COVERED UNDER THE WARRANTY.


BELT/DECK LUBRICATION
   First, you want to clean between the belt and deck to remove any debris that may be trapped. Use a clean, non-fraying rag, t-shirt, or light towel.
   Halfway between the end of the treadmill and motor cover, shove the garment under the belt until you can grasp it on both sides of the belt. Drag
   the garment the length of the entire belt 1-2 times. Remove the garment.

   Do not lubricate with anything other than approved lubricant. Your treadmill comes with one tube of “Lube” and extra tubes can be ordered directly
   from or your authorized dealer. You may also use a Lube-n-Walk kit that can be purchased through both aforementioned sellers.

   Keeping the deck lubricated at the recommended intervals ensures the longest life possible for your treadmill. If the lubricant dries out, the friction
   between the belt and deck rises and places undue stress on the drive motor, drive belt and electronic motor control board, which could result in
   catastrophic failure of these expensive components. Failure to lubricate the deck at regular intervals may void the warranty.

   The belt & deck come pre-lubricated and subsequent lubrication should be performed every 90 hours of use or if you notice that the deck is dry. It is
   recommended that you reach between the belt and deck to verify there is lubrication present, every other month.




                                                                             63                                                            Service Manual
10.2. Service Troubleshooting Checklist – Diagnosis Guide

Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common
problems that may not be covered under the treadmill’s warranty.


PROBLEM                                                     SOLUTION/CAUSE
Display does not light                            1) Tether cord not in position.
                                                      2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                                      3) Plug is disconnected. Make sure plug is firmly pushed into
                                                      220 Vac wall outlet. (On 120Vac electronic power system need 110Vac power)
                                                      4) Breaker panel circuit breaker may be tripped.
                                                      5) Treadmill defect. Contact your dealer.
Tread-belt does not stay centered                The user may be walking while favoring or putting more weight
                                                      on either the left or right foot. If this walking pattern is natural,
                                                      track the belt slightly off-center to the side opposite from the belt
                                                      movement.


Treadmill belt hesitates when walked/run on     See General Maintenance section on Tread-belt Adjustment.
                                                      Motor drive belt may be loose.


Motor is not responsive after pressing start   1) If the belt moves, but stops after a short time and the
                                                       display shows “E1”, run calibration (See section 8.1 on Error Message: E1).
                                                      2) If you press start and the belt never moves, then the
                                                         display shows E1, contact service.




                                                                                             64                                            Service Manual
Treadmill will only achieve approximately        This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord.
10 kph but shows higher speed on display        If an extension cord is required it should be as short as possible and heavy duty 16 AWG minimum. Low household voltage.
                                                        Contact an electrician or your dealer. A minimum of 220 volt AC current, 50 hz is required. (on 120Vac electronic power
                                                           system need have 110Vac)


Treadmill trips on board 10 amp circuit                High belt/deck friction. See General Maintenance section on Belt/Deck Lubrication..
Computer shuts off when console is               Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to section 7.3 for Grounding Instructions.
touched (on a cold day) while walking/running
House circuit breaker trips, but not the         Need to replace the house breaker with a “High inrush current” type breaker (see section 7.2 for Important Electrical
treadmill circuit breaker.                             Instructions.)
Treadmill with noises                               1. If the noise is coming from the rollers, .
                                                       2. If the noise is coming when the user is running on the treadmill with lowest level of incline , it could be due to too much
                                                           pressure with the incline cylinder. (only in case of the lowest incline level).
                                                       3. If there is knocking noise during the workout, check and make sure all bolts are tightened.
                                                       4. When there is thumping noise while the belt is running. This happens with a brand new treadmill or when the treadmill has
                                                          not been used for a long time. This is due to the belt has been shaped with rollers and harden because of low temperature.
                                                          Running the belt for tens of minutes the thumping noise will gradually go away.


Noise under motor cover.                           1. Worn brushes or bearings on motor. Replace with new motor brushes.
                                                       2. Front roller bearings are defective. Replace with new front roller.
                                                       3. Drive belt is misadjusted (too tight or too loose).    Adjust motor position.
Noise in the rear of the treadmill.              1. Rear roller bearings are defective.      Replace with new rear roller
                                                      2. Rear roller misaligned.          Adjust rear roller position.
Tread belt hesitates while being                  1. Insufficient lubricant on tread belt.
 stepped on.                                          2. Tread belt tension insufficient

Black particles collecting under                  Drive belt is breaking in. Vacuum under treadmill periodically.
treadmill.

                                                                                             65                                                                      Service Manual
11. Installation of the Incline Motor




                  66                Service Manual
            225


  Incline Range must be adjusted to
225mm minimum prior to installation.




                  67                   Service Manual
12. Disassembling and assembling
            of Parts




               68              Service Manual
 12.1 Lower Controller Replacement
    Disassemble the motor cover and Disconnect all lower controller wirings, replace with new lower controller and reconnect all wirings.




12.2 Console Replacement
 When replacing console, use Phillips head screwdriver to remove left and right handlebar covers.




 Use M6 L Allen wrench to remove 4 button head socket bolts from the console support.

                                                                            69                                                              Service Manual
Disconnect console wirings and replace with new console.




                                                           70   Service Manual
12.3 Motor Replacement
     Use Phillips head Screwdriver to remove 5 tapping screws and, and then disassemble the motor cover.




Remove motor grounding wire (greenish yellow), motor wire (+) red and motor wire (-) black.




                                                                          71                               Service Manual
Use 14mm T-shaped socket wrench to loosen 4 screws, use 14mm T-shaped socket wrench to loosen a side tension screw as well as a
  rear drive belt tension screw , remove motor and replace with new.
Reassemble in reverse order of disassembly, re-hook belt (readjust belt to be parallel with main frame after re-hooking). Do not
  tighten 4 securing screws yet.




Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between
70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.
Connect grounding wires and motor wires (red M+, black M-)




                                                               72                                                 Service Manual
12.4 Breaker Replacement
Remove Breaker connection wiring, replace part and reconnect wiring.




12.5 AC Power Switch Replacement
Disconnect wiring to AC power switch, replace AC power switch and reconnect wiring.




                                                                          73          Service Manual
12.6 Front/ Rear Roller Replacement
Use Phillips head screwdriver to loosen 2 screws on the rear adjustment base.




Use M6 L Allen wrench to loosen 2 screws on the rear roller.




                                                                            74   Service Manual
Use Phillips head Screwdriver to remove screws. Disassemble left and right upright bracket cover. Remove the motor cover.
Use 14mm T-shaped socket wrench to loosen 4 securing screws. Use 14mm wrench to loosen a side tension screw as well as a rear
drive belt tension screw in order to loosening the drive belt.
When reassembled, running belt tension needs to be adjusted and centered.




Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between
70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.
Connect grounding wires and motor wires (red M+, black M-)




                                                               75                                                Service Manual
12.7 Running Deck/ Belt & Cushion Replacement (※Be sure to disassemble the cylinder prior to this replacement procedure)
After folding the treadmill, use M5L Allen wrench and 12mm wrench to release the screw which secure the cylinder and take it apart.
Perform item (F), procedures to replace front and rear rollers.




Remove the left and right foot rail cap. Use a Phillips head screwdriver to remove 6 screws and bracket from back of foot rail. Remove the foot rail in the
direction of the indicating arrows.




                                                                                  76                                                         Service Manual
User Phillips head screwdriver to remove the 8 screws securing the running board. Remove the running board and replace running
board or running belt. If cushions need to be replaced, remove 6 cushions and replace. Reassemble in the reverse order as
disassembly.




Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between
70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.
Connect grounding wires and motor wires (red M+, black M-)




                                                                77                                                Service Manual
12.8 Speed Sensor Replacement(including the wire)
First remove motor top cover.
Remove speed sensor wiring and proceed with parts replacement.
After replacement, a test to check if the sensor registers the magnet is required.




12.9 Incline Motor Replacement
Remove the motor hood and fold the treadmill, then remove the incline motor.




                                                                               78    Service Manual
Incline Range must be adjusted to 225mm minimum prior to installation.




             225



Use M6,M8 L wrench and # 14 wrench to assemble new incline motor.




                                                             79          Service Manual
Connect incline motor wiring with controller




                                          Red wire Connect to “UP”
                                          White wire Connect to “COM”
                                          Black wire Connect to “DOWN”




                                                                    80   Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIIGS I

"oul JEUOIZEUIAJU] OOBAG

OIVAd

jenuepy BdIAlas
INA S8VLX


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jpnUuvYT 9I1ALAS

Saul/INO |[iwWpoas, INI S8VLX ‘T


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2.1 Upper Controllers

Cooling FAN

Speaker

Speed control
on handrail

Incline control
on handrail

fee Olt1 2131415161718) 9 1es)k

Ne DISPLAY

7 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIIGS 9

(JOJO/ SUIJOUJ/J9|]O4JUOD/JOJO/\) WA}SAS JOALG

a y

; = | J9||O1JUOD JOJO/\
——— . 4

YOLOW ANITONI

JIANG PUE 43]]012U0D JAMO] ZZ


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jpnUuvYT 9I1ALAS 6

SUOIJDINBIJUO) JO0I14}D9]FJ °Z


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIIGS

uolj}D1adC JINpOld
[J{UPRDAAL INF S8VLX ‘VY


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 34 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDY AD1A1aG CI

it ea a ny £

poAes WOJ} 9sO0yU) Wei301d eb 39sooy)

s]|NsaJ ayeuNI9e e1OUU aIejND|e>
jay |jIM Yysiam pue ase 4INOA SuIp|Acid

iLSSND ‘O113H

= isan) =

LNOAV'T NHAaOS HONOL..01

smopul  Ae|dsiq


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Function Button Locations

dad 8 «& (& &

HELLO, GUESTI

results

START WORKOUT
at

Choose a Program

Quick SPEED & INCLINE
BUTTONS

Function Buttons
Operation control

y 4 INCLIN =
Cm |SELEC

Disable Button
On Handrail
SPEED/INCLINE Switch
ON or OFF

Fan Button
Cooling fan switch on or off

Safety Key
Emergency function

16 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIIGS

swiDJBbdIG YI0/g UN
[ffUpdball INA G8VLX °S


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Treadmill Configuration

KEYBOARD => —a WIRELESS HR
RECEIVER
os tveras 7 — DISPLAY BOARD
5 > = SAFETY KEY

HR SPEAKER
HANDLEBAR LR
AMPLIFIER
LINE IN

— > MOTOR

INCLINE

CURRENT DRIVER BOARD MOTOR
BRAKER

K VR SET

‘ POWER
POWER » SWITCH

20 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 48 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDY aI1AIaG (aa

LAxMDOS SHIM
TVYONVH ANITONI

LAMOOS SYIM
TVYONVH G3adS

13ax900S
SYIM GYVOSAAy

LaxD0S GYVOg
LAdNI OIGNY Edi

Quvog Olanv
/ HLOOLANTE

LaxX90S
waAAVaAdS

Laxyo0S
AIGVD YALNdNOD

Lax90S
SYIM Ady ALASAVS

Guvog
YSSSNVUL PACE
13xOOS NVA 0d

LAXDOS SAYIM

4sind GNVH ="

SSA1SuIM YH

1axMO0S GYVOE gsn

SUOIJPDIUUOZ JIM pseog Aejdsiq T'9

ONIGNNOYD


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDY aI1AIaG €T

s

=

dol pueog gd

SUO!}E90] JUBUOUdWIOD gd pseog Aejdsiq 7°9


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 28 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
g-TMILL-V20
feo-cneme
“a Hy fo

Customer Mod
Part Number
Description 3

Programming r xT495 110018
$014 210127 ENM 2021.01.29-12.5

inn a

210201A001

je if
a001010652

IPL release


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDY aI1AIaS cz

SUOIJIOUUO) DIIM\ PAlOg JOALIG €°9


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.7 Driver Board function

\
M— (To DC Motor)
WHITE or BLACK WIRE
POWER INPUT y,
~
M+ (To DC Motor)
~ 2 RED WIRE
= F ?
‘Ai ¥ t = “+ ™~
WHITE WIRE (COM) OF ery —— THE VR SENSOR OF
INCLINE MOTOR POWER q
' : | | INCLINE
RED WIRE (UP) OF as Li y r ‘
INCLINE MOTOR POWER wu Oe SPEED SENSOR
\ f pa — (RESERVE)
r ~ J

BLACK WIRE (DOWN) OF

INCLINE MOTOR POWER
\

CONNECT TO CONSOLE

29 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jpnUuvYT 9I1ALAS

suoonijsu] Ajofos JINpOld °Z


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIIGS

buljooysajqnol / sabossaij 40417
[J{UPbAAL INA S8VLX ‘8


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.1 Error Message > Display appears ' PLEASE REPLACE THE SAFETY KEY , onthe screen. (EO)
Definition: Display board CPU did not receive the Safety device signal.

Configuration: Screen display :

SAFETY KEY |
| SIGNAL

AN | |
CONSOLE i ec
DISPLAY BOARD MI Porkexes |
|
a eee a eee a |
aa PLEASE REPLACE THE SAFETY KEY

’

MOTOR
VOLTAGE

AC POWER DRIVER BOARD mm ) MOTOR
C POWER [| R BO ==

Troubleshooting

Part Troubleshooting

Safety key / 1. Safety key necessary be set.
Safety Switch Module

2. Check Safety Switch Module’s Pin place on the console board.

34 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.2 Error Message : E1

Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM sensor, but
when the Calibration which it is a necessary.)

Configuration:

Cause of E1

CONSOLE
DISPLAY BOARD

Send and receive speed }

. . RPM SENSOR MOTOR SPEED
signal via TX/RX of SIGNAL SIGNAL
5-pin Main wire. | {

MOTOR
VOLTAGE

2 PIN » MOTOR

AC POWER | )» DRIVER BOARD

ead SIGNAL

2 PIN RPM
SENSOR

35 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
The motor doesn’t working: E1 appears.

m~ Explanation:
@ The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor

signal.

@ Configuration :

CONSOLE
DISPLAY BOARD

Send and receive

. . RPM SENSOR MOTOR SPEED
speed signal via SIGNAL SIGNAL
TX/RX of 5-pin | '

MOTOR
VOL TAGE

2 PIN MOTOR

AC POWER > DRIVER BOARD

= SIGNAL

2 PIN RPM
SENSOR

36 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 73 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart

El showing up Pm Reset power > Press start again

Replace upper console board or
update the program of upper
console board

Check display whether Countdown
or not after pressing start?

Check main control line
whether split or not?

Did belt noves after
start?

Replace main
control line

k p| Replace lover control driver board

Check RP\ sensor Replace RPM
whether well or not? sensor
Use multi-meter to Check lower control
Check Main control line driver board weather
socket pin? & pind is enough Power?
Dc12V) (AC: 2201) Adjust sensor gap distance to 2nm.
Did belt moves after x Vv Vv

5
Check power source from wall weather start:

stable AC220V or not?
Then, press start and

use multi-neter to
Check driver board
notor socket weather
voltage or not?

NO

YES
YES

Replace Motor » Solve the problem

37 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 44 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
YES

Move the roller so
that regent closest
to the scnsear

Make sure the gap
between magnct'senser jess
than 3 mim

YES

Is function OK?

NO

Replace computer
cuble

‘um power back a
press “start” and
comrmdown fs fiumction
OK?

NO

Replace Comsole

YE

YE

Conpect Properly

Adjust sensor
position

Propicm fixed

Problern fixed


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Reed switch RPM
speed sensor device

Assembling the speed sensor

1. Remove the motor cover hood.

2. Thespeed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will have a belt around it that also goes
to the motor). The speed sensor is small and black with a wire connected to it.

3. Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley; make sure the

sensor is aligned with the magnet. There is a screw that holds the sensor in place that needs to be loosened to adjust the sensor. Re-tighten the
screw when finished.

39 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.4 Error Message: E3

Definition: The console board is not detecting the VR voltage value, or the voltage value hasexceeded the range. ” E3” appears on the display.
Configuration:

DISPLAY BOARD

: The incline VR
DANE single via TX/RX of
VOLTAGE Main control wire
send and receive.

INCLINE
MOTOR

DRIVER BOARD <= VR VOLTAGE | INCLINE VR SET

L

Case of E3
Incline VR value exceeds the range. E3 appear on the display.
@ = Incline motor isn’t operation up or down, making the VR value exceed the range.
@ After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so E3 appears.

@ = Action Flow Chart

41 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ERR APPEARS ON
THE DISPLAY


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test Procedure:

1. Runcalibration again.
2. Does the incline motor move at all?
3. If no, do the Up/down lights on the incline board light?
4. If they light, do the relays click on?
@ = ‘If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red)
or down (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the
mains voltage ~ 110VAC (230VAC). If the voltage is present but the motor doesn’t move, then the motor is bad.

@ = If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).

5. If the motor moves, is there a sensor reading onconsole?

@ = The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, O for lowest incline. The Incline window is a counter that is
showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the position
sensor wiring orcircuitry.

@ = ‘If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able torotate).

Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.

@ = ‘If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black
and red wire and there should be a voltage
between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical, as long as it’s
somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register then
there may be a bad wire connection between the potentiometer and the console.

6. Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
7. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board.
There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.

The only problems that are possible are a bad solder joint or broken circuit on the board.

@ Console connector wiring, these connections are the same on the incline board and at the console.
| Pin 1 = ground
| Pin 2 = position signal O~S5vdc
| Pin 3= 5vdc

8. If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the incline board then check
the entire cable from incline board to console for cuts or bad connection at the inwire connectors.
9. If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.

46 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 47 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Error Message: E3 / INCLINE ERR
Definition: During incline action, the display board CPU cannot read the VR value, so E3 appears.
Configuration :

DISPLAY BOARD . UPDOWNKEYS | , pamwwarneys

4m

INCLINE Signal

INCLINE - INCLINE
receive.
Incline drive => Incline drive power
INCLINE
MOTOR
DRIVER BOARD = VR VOLTAGE INCLINE VR SET

47 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of INCLINE E3

Press the incline UP/DOWN key. The incline doesn’t operate. E3 appears on the display.
Explanation

When press incline key, the display board CPU reads the incline VR value. If there is no VR value change to the CPU, the incline is not operating, and
then appear E3 appears on the display.
Action flow chart :

i™
(, )
Z 23
cz
é i 3 + i bat
nS
+24
c
ic
. x
. Zz z Zz Z \ }
N ‘ reo
{ \ \ / \ / \ / \ /\ / o™
i) \ \ \ \
/ / / /
\ f \ i>) / \ / \
c } 3 os f z2\ / =x\ ~ f. \ JE a
= pA ~: /z=3 fui > {sz {/&Z \ =
2 f = = / ] / 252 \ ~ Cd \ f 2 \ <
ae - =x ‘ f 3-2 = -= =:
§ IS2\ S {sts \ f x \ = / =2 \ { 32 \ Z
: Io | 2 if Zs \ f/ #2: \. J} 2] f/f =¥* \ f/f ee \ -
> £2 oo { 255 aan’ . aa “: \ — prem =p > 2
< ox) a. \ =< / \ <-+ / 7 \ cZ / \ “4 / oe
- \4e| > \ 2-3 / \ ate / - \ ee / \ 7% f zy
7 vs | \ «5° \ =- 7 > \ Sa a
£ Fy a \ =f \ 222 / 7 \&Z / \Z3 / -
bel —_ “fs \ 2 - \~ ~/ \ >
| \ f \ 3 / \ / x / Z
\; \ / . \ / \ /
\ / | \ / \/ \/ \/ \ /
aed \ y V L___| Vv Vv NY

48 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 50 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.5 Error Message: E4

Definition: Motor power wire error.

Configuration :

DISPLAY BOARD

Fan

The signal
RPM or via TX/ RX Send
Motor of Main command of
signal control wirew start or speed
return_~ signal.+

MOTOR

Power of Motore
DRIVER BOARD

VA

Cause of E4:

Power wire of Motor does not insert lower controller.

Troubleshooting

Part Troubleshooting

Lower controller Insert power wire of motor.
Motor Replace Motor.

Display board Replace upper control board.

50 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 55 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.10 CALIBRATION PROCEDURE

1. Choose settings function on screen bottom right corner then click on “Software” button.

tv)
€] @ KN 5S) £ ==) ANNA 7 12:05
SETTINGS
Display WiFi Bluetooth Software
Date Time Child Lock Units

* $ & a an 2)

2. On the screen will be show software version and click on “software version CO06_XT485...” to continue five times for this step.

< @ ch x a Guest = 9:17 PMA
SOFTWARE
C006_XT485_T1001B_S002_201130_EN (J
VOUs
Your software version is the latest
BACK
* & & a wm ©

55 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 56 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. You need to enter password 20160620 to confirm before enter the calibration screen.

4. Choose CONTROLLER function, set the units for imperial or metric.

€ @ qh x ee Guest = 09:19 PM
DEVICE INFO CONTROLLER FREQUENCY
vine we
WHEEL DIAMETER TORQUE VALUE PWM START PWM SEGMENTATION
60 65 0 0
MIN SPEED MAX SPEED MAX INCLINE
0.5 mph 12.0 mph 15%

besuiri guna? CHECK SPEED

5. If you want to calibrate speed, click on “Start calibrating speed” to mark on screen bottom left corner. No choice this item, only incline level calibration.
Click on CHECK SPEED to begin calibration.

6. The process is automatic; the speed will start up without warning, so do not stand on the belt. When calibration be finished on calibration successfully

screen, click on reboot to exit.

56 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 47 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.11 Circuit Diagram

S SD
(Madd N)3IVD HALNAWOD SNids SS (F700) 319 V9 HALNdINOD SNid S eq

rt]
=
© ul
ke
<= u “| ~2o009
= _ tit
T BLL
oO f & ITT I
Ww 5 eNO?
Sw E
fe) th SHU SLIM re}
ra Z te
i) 8 ; = SHU YOW'E d FA a
Fe wl w oie
CN =|= ty
oS HIS Z
EK — =| a =
Z oo
Ww ho o—_“ S o
a - — ul BL
KE 56 = nH S| 2
al HH} 8
* = tl z| 8,
5
a2

57 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 60 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jpnUuvYT 9I1ALAS 09

IIUDUIUIDIAJ [DADUID ‘OT


=== OCR SUPPLEMENT, PDF PAGE 73 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cc
=
S
© ~
= oO
= :
= 5
8 o

(oD)
c ze}
Cc
S (a0)

(e)
e $s
: iad
=

_e)
; a
ie oO
8 :
a lok
@ O
S x
o ;
ro! 8
Qa
‘ eo
xn S o
2 ~
= Ov
= 5 2
= 83
Cc a -
2 E z
is {e)
a =c& Aa

1S)

= 2#q
5 =
O F4 2
, - ag
£ @\ \ S > =
© gi-\ 2 5
v 4 \ = fe
rt a uy 2
> Cc
8 { a in 8


=== OCR SUPPLEMENT, PDF PAGE 79 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
PPRUD A PIHIIS ;

i
a
I uf
=
{ c—
__ — :
-
— | sh
j= a
| A a
: by
a

"u01}e]/e}SU! OF JOLId LUINWIUIW WUWWGZZz 0} paysnfpe aq ysnw aguey auljduy|
