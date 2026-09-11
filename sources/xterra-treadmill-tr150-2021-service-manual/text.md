<!-- Source: TR150 (GT65 - NT014) Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

 GT65 - NT014
    Treadmill
Service Manual
-------------------------------------------Table of Contents----------------------------
                       1. GT65 Treadmill Outlines
                       2. Electronic Parts
                          2.1 Upper Controllers
                          2.2 Lower Controller and driver
                       3. Electrical Configuration
                       4. GT65 Treadmill Operation
                       5. GT65 Treadmill Unit Block Diagrams
                       6. GT65 Treadmill Basic Connections and Wiring
                          6.1 Display Board Wire Connections
                          6.2 Display Board PCB Component Locations
                          6.3 Driver Board Wire Connections
                          6.4 Driver Board PCB Component Locations
                          6.5 Driver Board Function
                       7. Product Safety Instructions
                          7.1 Important Safety Instructions
                          7.2 Important Electrical Instructions
                          7.3 Important Grounding Instructions
                       8. GT65 Treadmill Error Messages / Troubleshooting for Electronic Issues
                          8.1 Error Message: E0
                          8.2 Error Message: E1
                          8.3 Error Message: E2
                          8.4 Error Message: E4
                          8.5 Error Message: E5
                          8.6 Error Message: E6
                          8.7 Error Message: E7
                          8.8 Error Message: E9
                          8.9 Circuit Diagram
                          8.10    Calibration Procedure
                          8.11    MAINTENANCE MENU




                                                            2                                     Service Manual
Special Note on GT65 CEGS version:
Besides normal version, GT65 treadmill is with a CE/GS version. Both versions are with exactly the same in functions and outlines except that
the power input is 110AC for normal version versus 230VAC for CEGS version and an additional Filter Choke circuit is added for CEGS version
as shown in the circuit diagram on next page.




                                                                      3                                                       Service Manual
1. GT65 Treadmill Outlines




             4               Service Manual
5   Service Manual
2. Electronic Parts




         6            Service Manual
2.1 Upper Controllers




                        Console




                                  7   Service Manual
2.2. Lower Controller and Driver




                         Lower Controller Area




           .



                                                 8   Service Manual
3. Electrical Configurations




             10                Service Manual
SAFETY KEY:
The safety key fits into the Console to activate all functions and treadmill. Without safety key, console will be appeared E0.


CONSOLE:
Interface that controls all functions of the treadmill.


MAIN CONTROLLER:
The circuit board consist of the DC power supply for console, and DC motor driver, links the console to output appropriate voltages for motor for
controlling the treadmill functions.


TREADMILL MOTOR:
This is a DC motor with variable speed. Control the 0 –90 (or 0-180) voltages from the main controller to increase or decrease speed of the running
belt.




                                                                        11                                                           Service Manual
GENERAL INFORMATION
CONSOLE
Contains keys、 LCD Display、Hand Pulse Grip、Safety key, etc.

MAIN CONTROLLER:
Main controller includes power supply, motor driver, control circuit, etc.
The 220V (or CEGS) of Lower Controller Area has Filter and Chock.

TREADMILL MOTOR
DC motor with variable speed range 0-90 or (0-180) volt. Requires three wires connection: red, black and green.
The Red wire is inserted into M+.
The White wire is inserted into M-.
When voltage is higher and higher, the motor will be faster.
The green wire is grounding wire.




                                                                        12                                        Service Manual
4. GT65 Treadmill Operation




            13                Service Manual
Display Windows



                  LCD Display




                    14          Service Manual
LCD LAYOUT




     15      Service Manual
Operation
Window Display Mode
   OFF Mode
      When user doesn’t insert the SAFETY KEY on the console, the treadmill will appear E0.
   READY Mode
      When the treadmill is ON and SAFETY KEY is inserted in console, then press START button to start treadmill on Manual Mode.
   SLEEP Mode
      In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
   RUN Mode
      In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly.
Function
   SPEED
      Display the current speed in Kilometer or mile per hour.
      DISPLAY range is 0.0 to 99.9
      WORK range is 1.0~16.0KM or 0.5~12Mile.
      Press “FAST” or” SLOW” to adjust speed, each increment and decrement is 0.1 km/h (mph).

   TIME
      TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time then timer is COUNT DOWN.
      DISPLAY range is 0:00 to 99:99.
      WORK range is 0:00 to 99:59.
      COUNT DOWN setup range is 10:00 to 99:00.
      When TIME is set, the count will go to zero.
      In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will continue count up time.




                                                                      16                                                           Service Manual
 DISTANCE
     Display the current distance in kilometer or Mile. DISPLAY range is 0.00 to 99.9.
     WORK range is 0.00 to 99.9.
 CALORIES
     Displays the cumulative calories burned at any given time during your workout.
     DISPLAY range is 0.0 to 999.
     WORK range is 0.0 to 999.
 PULSE
     Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
     DISPLAY range is 0 to 999.
     WORK range is 40 to 220 BPM.
PROGRAM
      Display the current program item.
      Display range is 000 to 999.
      Work range is 0, P1 to P12.
      When press once Program key, then display will appear one mode, it can appear P1 to P12 modes.




                                                                       17                                          Service Manual
Function Button Locations
Function Button in the Main Mode
  READY MODE
     SAFETY KEY: Fit safety key in right position to power on the computer. When safety key is pulled away from its position, the computer will be
     automatically shut down and appear E0.
     STOP button: Press holding this key 3 seconds, the display will reset.
     START button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on window
     display, then machine starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill starts at program preset value in PROGRAM.
     The other function is that in the calibration which is thought of confirmation key to confirm parameter.
     FAST button: If user doesn’t enter a setting then this button is non-functional.
     SLOW button: If user doesn’t enter a setting then this button is non- functional.
     RAPID button: Non-functional.
     PROGRAM KEY: Non-functional.
     Press PROGRAM keys (▲/▼) to choose whichever you want. And then confirm the every setting by pressing ENTER key, finally, press START
     key to do exercise.
     The program function has 12 programs (P1 to P12).
     When into calibration, press

     the program key to enter to calibration mode.




                                                                       19                                                           Service Manual
RUN MODE
  SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down and appear E0.
  STOP button: press “STOP” button to stop treadmill.
  START button: non-functional.
  ENTER button: The function can took turn showing calories and distance.
  ▲ (FAST) button: Press the button to increase your speed and each increase is 0.1KPH (0.1mph). If button is pressed continuously then
  speed increases to MAX SPEED quickly.
  ▼ (SLOW) button: Press the button to decrease your speed and each decrease is 0.1KPH (0.1mph). If button is pressed continuously then
  speed decreases to MIN SPEED quickly.
  RAPID button: 9 preset buttons for rapid speed: 0 to 9. Because it is can adjusted rapid speed, first pressed speed key, and then select 1
  or 2 digits, else the treadmill will automatically adjust to that value.
  PROGRAM KEY: Non-functional.




                                                                             20                                                   Service Manual
5. GT65 Treadmill Unit Block Diagrams




                  21              Service Manual
Treadmill Configuration
                     KEY
                    BOARD




                          BULETOOTH




                                      22   Service Manual
6. GT65 Treadmill Basic Connections and Wiring




                      23                  Service Manual
6.1 Display Board wire Connections


                       CONNECTION            Connection with
                       WIRELESS              KEY BOARD
                                                                              Connection with
                                                                              Handrail Pulse


Connection
with
Safety key                                                                                      Heart Module



    GND
    RXD
                                                                    MAIN IC
    TXD
    VDD                             Display IC
    SW




          Connection with
          MP3 POWER
          WIRES




                                                               24                                   Service Manual
6.2 Display Board PCB Component Locations
  PCB Board Top




                                            25   Service Manual
PCB Board Bottom




                   26   Service Manual
6.3 Driver Board Wire Connections




                                                                M-
                                                                connected
                                                                with black
                   AC POWER                                     wire of motor
                     INPUT
                    AC 110V                                     M+
                    AC 220V                                     connected
                                                                with red wire
                                                                of motor




                                                                 Speed sensor
                                                                 socket connected
                                                                 with 2-pin of
                                                                 speed sensor
                                                                 wires.

                                    MAIN control wires socket
                                    connected with 5-pin of
                                    control wires.




                                         27                                         Service Manual
6.4 Driver Board PCB Component Locations




                                           28   Service Manual
6.5 Driver Board function




                                Bridge                              IGBT



                                          X capacitor
               AC220V INPUT N            (Safety CAP.)                               M-
                                                                Filter
                                                              Capacitor
                            Varistor                                                 M+
                                            RELAY
               AC220V INPUT L




                                          TRANCEFORMER

                                                                                     SPEED
                                                                                     SENSOR
                                                                             MAIN
                                                                           CONTORL
                                                                            WIRES



                                                         29                                   Service Manual
7. Product Safety Instructions




              30             Service Manual
7.1 Important Safety Instructions
   - To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
   - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 230-volt, 10-amp
     (110-volt, 15A) grounded outlet with only the treadmill plugged into the circuit.
   - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
     improper adapters or in any way modify the cord outlet.
 7.2 Important Electrical Instructions
   - Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any appliance with a large motor, the GFCI will trip often. Route
     the power cord away from any moving part of the treadmill including the elevation mechanism and transport wheels..
   - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is first turned on or even
     during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill itself
     does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
     have no ability to control. This part is available through most electrical supply stores. Examples: Grainger part # 1D237, or available online at
     www.squared.com part # QO120HM.
 7.3 Important Grounding Instructions
  - This product must be grounded. If the treadmill should malfunction or breakdown, grounding provides a path of least resistance for electric current,
    reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
    appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
    - DANGER – Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified
      electrician or serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if
      it will not fit the outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 110-volt circuit, and has a
      grounding plug that looks like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this
      plug to a 2-pole receptacle as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly
      grounded outlet, (shown below) can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from the adapter,
      must be connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held in place by a metal
    screw.




                                                                                 31                                                                 Service Manual
  8. GT65 Treadmill Error Messages /
Troubleshooting for Electronic Issues




                  32              Service Manual
•       Error code items：
                            Error Message                                      Explain
                                 E0         Safety keys dose not insert the safety module. Or safety module is broken.
                                 E1         Display board CPU did not receive the RPM signal.
                                 E2         Over current, over limit current of lower controller and motor.
                                 E4         Power wires of motor error.

                                 E5         Communication signal error.

                                 E6         Lower controller error.

                                 E7         Input power error.

                                 E9         Calibration error.


    •   Prepare：

                                                   Picture                                  Tool name




                                                                                             Multi-meter




                                                                          33                                             Service Manual
8.1 Error message: E0
   Definition: Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken.
   Configuration:

                                     Console

                                                                                                   Lower controller
                                 SAFETY MODULE                       (+12V) signal via S/W
                                                                     of Main control wires
                                                                     form a safety switch
                                                                     loop.

                                        SAFETY
                                         KEY


   Cause of E0
           The console is not inserted the safety key, cause to console is not form a +12V’s loop (safety switch loop). So display will be appeared E0.
   But possibly main control wires or components of lower controller are broken. (Because lower controller sent (+12V) signal via S/W of main control
   wires to upper control board to form a safety switch loop.)

   Troubleshooting
                        Part                      Troubleshooting
                        Safety module            Insert the safety key, and then use Multi-meter transform into short circuit
                                                 gear position to check safety module wires whether short or not.
                        Main control wire        Reinsert Main control wires.
                                                 Replace main control wire.
                        Display board             Replace upper control board.




                                                                          34                                                             Service Manual
8.2 Error Message：E1
    Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed
    RPM sensor, but when the Calibration which it is a necessary.)
•   Configuration：




                                    Send and receive
                                     speed signal via
                                     TX/RX of 5-pin Main
                                     wires.




                                                                      35                                                      Service Manual
Cause of E1
The motor doesn’t turn：E1 appears.
        ■   Explanation:
            ◆ The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor
                signal.
            ◆ Configuration




                                              Send and receive
                                              speed signal via
                                              TX/RX of 5-pin Main
                                              wires.




                                                                         36                                                           Service Manual
E1 solution follow chart




                           40   Service Manual
E1 solution follow chart – check RPM sensor device procedure：




                                     41                         Service Manual
•   Checking the speed sensor
     1. Remove the motor cover hood.
     2. The speed sensor is located on the left side of the frame, right next to the front roller pulley (the
        pulley will have a belt around it that also goes to the motor). The speed sensor is small and
        black with a wire connected to it.
     3.   Make sure the sensor is as close as possible to the pulley without touching it. You will see a
          magnet on the face of the pulley; make sure the sensor is aligned with the magnet. There is a
          screw that holds the sensor in place that needs to be loosened to adjust the sensor. Re-tighten
          the screw when finished.




              Read switch RPM
              speed sensor device.




                                                   42                                      Service Manual
 E1 issue troubleshooting form
     E1
     message   Possible cause            Things to check      Solution




               Possible cause            Things to check      Solution




               The upper console         check the speed
                                                              Make sure the good connection
               board hasn't receive      sensor cable is in
                                                              for cables
               any speed signal for 8    good connection
               seconds
E1
message
The motor
cannot move
                                         Check the gap
               The speed sensor didn't                      To keep the gap-distance less
                                         between speed
               detect signal completely.                    than 3 mm.
                                         sensor and magnet.




                                         Check if the sensor
               Defective sensor or bad   and cables are      Change the sensor
               cable connection.         circuit short       or cables.
                                         damaged.




                                               43                                  Service Manual
•   8.3 Error Message：E2/OVER CURRENT
•   Definition: When lower board detect over current, then display appear “E2”.
     The means is lower board need to protect itself and motor. Prevent lower board and motor is burned.
•   Solve over current:
    First, check whether smear Silicone oil or not. And then when during the using treadmill, do not block belt running. If aforementioned did not
    process problem, suggest Replacing lower control board or Replacing motor.




                                                                        47                                                            Service Manual
8.4 Error Message：E4
Definition: Motor power wires error.
Configuration:




                           Signal via
                 RPM or    TX/ RX of         Send
                  Motor    main control      command of
                  signal   wires.            start or speed
                 return.                     signal.




                                                  Power of Motor
                                                  (90DCV or
                                                  180DCV)




Cause of E4:
     Power wires of Motor does not insert lower controller.


 Troubleshooting
 Part                       Troubleshooting
 Lower controller           Insert power wires of motor.
 Motor                      Replace Motor.
 Display board              Replace upper control board.




                                                      48           Service Manual
8.5 Error Message：E5
Definition: it is a Poor communication, between the console and lower controller is poor communication,
almost it is bad on a main control wires, but also possible bad at console board or lower controller.
Configuration:



                                       Console



                      Signal via main
                      control wire to
                      communication.



                                 Lower controller




Cause of E5:
      The main control wires is possibly broken. But E5 maybe has another problem, like component of
lower controller or console board.




 Troubleshooting
 Part                      Troubleshooting
 Lower controller board    Replace main control wire.
 Main control wires        Reinsert Main control wire.
                           Replace main control wire.
 Display board             Replace upper control board.




                                                     49                                     Service Manual
8.6 Error Message：E6
Definition: The lower controller component is fault.
Configuration:



                                      Console



                       Signal via main
                       control wire.




                                 Lower controller




Cause of E6:
        The lower controller component is fault, Like Transistor、IGBT、control module…etc.


 Troubleshooting
 Part                       Troubleshooting
 Lower controller           Insert power wire of motor.
 Display board              Only Replace upper control board.




                                                       50                              Service Manual
8.7 Error Message：E7
Definition: Input power anomaly, possibly too low or too high or unstable.
Configuration:



                                                    Console
    Wall outlet
    AC 110V
    Or
    AC 220V


                                                                   Signal via main
    Overload                                                       control wires.
    protection


     Power Switch                             Lower controller


     CE PART or 220V to match
     Filter and Chock.


Cause of E7:
     The wall outlet possibly unstable, cause to treadmill working power does not stable.
     Another problem possibly power part of lower controller board is broken.


 Troubleshooting
 Part         Troubleshooting
 Wall outlet Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or
             220AC or not. And the voltage whether stable or not.
 Lower       Replace Lower controller board.
 controller
 board




                                                   51                                   Service Manual
8.8 Error Message：E9
Definition: Calibration error.
Configuration:




                                 Send and receive
                                  speed signal via
                                  TX/RX of 5-pin
                                  Main wires.




Cause of E9:
     Maybe cause to Calibration error:
1. In the Calibration, the speed sensor may come off or over more than 3mm of gap-distance.
2. In the Calibration, main wires may come off or defective contact.
3. In the Calibration, power off and then power on immediately.
4. In the Calibration, power is Unstable or lower power.
5. In the Calibration, the parameter may not correct or the parameter does not deposit entirely.


 Troubleshooting
 Part                Troubleshooting
 Wall outlet         Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV
                     or 220AC or not. And the voltage whether stable or not.
 speed sensor        Check speed sensor gap-distance whether less then 3mm or not.
 Main wires          Check main wires whether it may be broken.
 Calibration again Before the calibration, should check parameter whether setting correct or not. In the
                   calibration, person and things cannot stand or put on the belt.
 Lower Driver        Replace Lower Driver board.
 board
 Upper control       Replace Upper control board.
 board

                                                      52                                      Service Manual
8.9 Circuit diagram:




                       54
55
 8.10 CALIBRATION PROCEDURE

1. Remove the Safety Key.
2. Press and hold down the PROGRAM and at the same time replace the Safety Key, at the speed
   window appears “Eng”.
3. First, press START key, to adjust wheel size diameter is 42 then press START key.
4. Second, setting minimum speed to 1km (0.5Mi for imperial units) and then press START key.
5. Third, setting maximum speed to 16km (10Mi for imperial units).
6. Press Start button to begin calibration. The process is automatic; the treadmill’s belt will start up
   and it is not preparatory warning, so do not stand on the belt.




                                                                            56
8.11 Troubleshooting procedure matrix
                       Condition                                          Reason                                                    Solve
When turn on power, ON/OFF switch isn’t lit.           1 Power cord isn’t plugged into outlet.          1 Plug the power cord into outlet.
                                                       2 Power cord isn’t plug into unit.               2 Plug the power cord into unit.
                                                       3 The voltage of outlet is too low.              3 Check the voltage of outlet.
                                                       4 Plug or connector of power cord is open.       4 Replace power cord.
                                                       5 Connector of power cord is broken.             5 Replace power cord.
                                                       6 Connecting cable disconnected.                 6 Check if wires are disconnected, connect it again.
                                                       7 Breaker tripped.                               7 Press the small red button to return to original status.
                                                       8 Breaker is broken.                             8 Replace breakers.
                                                       9 ON/OFF switch is broken.                       9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown       1 Check the voltage of power is 110V or 230V. Replace
                                                       broken on controller.                            controller.
When insert safe key, no display on monitor.            1 Haven’t switch ON/OFF switch.                 1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.        2 Insert the safe key on right position.
                                                        3 5-PIN Main control wires not plugged in       3 Please check the wire and connect again.
                                                          properly.                                     4 Replace 5-PIN Main control wires.
                                                        4 5- PIN Main control wires are broken.         5 Replace fuse or controller.
                                                        5 Fuse on controller is blown.                  6 Replace varistor or controller.
                                                        6 Varistor on controller is blown.              7 Replace safety key device.
                                                        7. Safety equipment is broken. (open circuit)   8 Replace console.
                                                        8 Other components are faulty.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)              1 Replace the safety key device or console.
 When press “START”, treadmill doesn’t start.          1 Motor M+ or M- wire isn’t connected into       1 Please check and plug again.
                                                         right position.
                                                       2 Motor is broken.                               2 Replace motor or check the wire and connector if it was
                                                       3 Treadmill controller shut down.                  broken.
                                                                                                        3 Turn off the AC switch and turn on power again.
Treadmill stops or shuts off by itself.                1 House breaker tripped.                         1. Reset it.
                                                       2 Treadmill breaker tripped.                     2. Reset treadmill breaker.
                                                       3 Treadmill controller fuse is broken.           3. Replace with new fuse
                                                       4 Treadmill controller shut down.                4. Turn off the AC switch and turn on power again.

After removing safety key, treadmill can’t stop.       1. The safety key device is broken.              1. Replace with new safety key device.

LCDs not bright, incomplete or imperfect.              1. LCD light is broken.                          1. Replace with new LCD or console.
                                                       2. Power to console too low.                     2. Check AC power is 110V or 230V.
                                                                                                        3. Check power to console.
                                                                                                        4. Replace lower controller.
LCD displays not bright, incomplete or imperfect.      1. LCD displays are broken.                      1. Replace with new console.
                                                                                   57                                                                   Service Manual
The speed of the belt doesn’t match console display.   1. Console is not calibrated.                  1.Calibrate the console
After pressing “START” button, the treadmill stops     1 Controller is broken.                        1 Turn off the AC switch and turn on power again.
immediately.                                                                                          2 Replace controller and calibrate it.
Erratic pulse display.                                 1. Another chest belt in use around treadmill. 1. Check for other chest belt use around treadmill.
                                                       2. Other magnetic field disturbance.           2. Change the position or direction of treadmill.
                                                       3. Receiver is broken.                         3. Replace with new receiver.
After pressing “START” button, the treadmill stops     Controller was broken.                         Replace with new controller and calibrate it.
immediately.
FAST/SLOW button of SPEED ADJUSTMENT                   1. Maybe keys stuck.                             1. Replace key board.
SWITCH can’t be used.                                  2. Maybe upper control is broken.                2. Replace upper Controller.
Speed button just can press FAST, can’t press SLOW.    3. Maybe lower control is broken.                3. Replace lower Controller.
Speed button just can press SLOW, can’t press FAST.
Hand pulse lost its function.                       1. Hands not on the hand pulse sensors or           1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                        only one hand on sensor.
                                                    2. The connector of HANDPULSE W/WIRE                2. Connect the cable again.
                                                       and Console not connected properly.
                                                    3. The wires got damaged when connecting            3. Replace with new cable.
                                                       the HANDPULSE W/WIRE and Console.
                                                    4. Hand pulse board is broken.                      4. Replace console or Hand pulse board.
Wireless lost its function.                         1. Chest belt not worn properly.                    1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                            oriented correctly.
                                                    2. Distance is too far and exceeds range of         2. User chest belt in front of console within 3 feet.
                                                     receiver.                                          Replace with new lithium battery type is CR2032.

                                                       3. Chest belt battery is weak or dead.
Chest belt too close to the treadmill.                 Weak battery.                                    Replace with new lithium battery with type CR2032 .
Tread belt does not run in center.                     Tread belt tension not even across tread belt.
                                                                                                        See treadmill belt adjustment
Tread belt hesitates while being stepped on.           Insufficient lubricant on tread belt.            See treadmill belt lubrication
                                                       Tread belt tension insufficient
Black particles collecting under treadmill.            Drive belt is breaking in.                       Vacuum under treadmill periodically.
Noise under motor cover.                               1. Worn brushes or bearings on motor.            1. Replace with new motor.
                                                       2. Front roller bearings are defective.          2. Replace with new front roller.
                                                       3. Drive belt is misadjusted (too tight or too   3. Adjust motor position.
                                                       loose).
Noise in the rear of the treadmill.                    1. Rear roller bearings are defective.           1. Replace with new rear roller.
                                                       2. Rear roller misaligned.                       2. Adjust rear roller position.

                                                                                   58                                                                  Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
*OU] JEUOIJEUA}U] OweAG

OIVACd

jenueypy adIAlasg
[ILUpead |

VIOLN - S9LD


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jonupyy aoiasasy

SOUI/INO [[fUIpeetl GILS bt


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG L

g|OSUOD

$19]|01]U04 Jaddf L'z


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG

uole1ado¢C jjiupeas, SOLD ‘vp


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG rl

Ke\dsiq ao7

smopul(\ Aeldsig


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
suo!}e007] UO}INg UO!}OUN-


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG

swelbeig YIO/g WU |[IWIpeatL GILD ‘S


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Treadmill Configuration

KEY
BOARD

DISPLAY BOARD
SAFETY KEY

HR
HANDLEBAR

ss, MOTOR

aiaune DRIVER BOARD
BRAKER

a | POWER
BOWER ==> SWITCH

22 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG SZ

do] pieog god
SuOI}e907] JUBUOdWIOD g4dd pieog Aejdsig z'9


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
one a

~ Ave “ Md
Pha bb
pha rst nu LJ}


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG 8Z

suoi}eo0'7 juauOdwO04y 0d pieog J9SALG 79


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jonubpy dondog 62

1 @

aoNtgy E4

UOd]HOUN} pueog JSALG S°9


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jONUDPY 2I1Asay’

SUOI]ONASU] AjJajesS JONPOldq *Z


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDPW 4I1AsaG

sanss| 91/U01]9a/F7 404 Buljooysajqnos]
/ sabessayy JO11F [Jlwpeatl GIL ‘9


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.2 Error Message: E1

Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed
RPM sensor, but when the Calibration which it is a necessary.)

¢ Configuration:

CONSOLE
DISPLAY BOARD

Send and receive |
speed signal via

. . RPM SENSOR MOTOR SPEED
TX/RX of S-pin Main SIGNAL SIGNAL
wires. | |

MOTOR
VOLTAGE

2 PIN » MOTOR

AC POWER » DRIVER BOARD

_— RPM
SENSOR

35 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of E1

The motor doesn’t turn: E1 appears.

m Explanation:

@ The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor
signal.

@ Configuration

CONSOLE
DISPLAY BOARD

Send and receive

speed signal via RPM SENSOR MOTOR SPEED
TX/RX of 5-pin Main | SIGNAL | ees
wires. |

MOTOR
VOLTAGE

2 PIN MOTOR

AC POWER >» DRIVER BOARD

_ RPM
SENSOR

36 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 90 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart

E] shoving wp + Teset power —py Press start again

Replace upper console beard or
update the progran of upper

console board

Check display shether (cuntdoun
or not after pressing start?

Did belt aoves after Check nein control line Replace main
Wether split or mot? control Line
co Replace lover control driver toard
Check FPA sensce Ieplace FAX
whether vell or not? Sense

Check lover control
driver board seather

eough Poser?
(K: Bi)

lse multi-seter to
Check Kein control line
socket pin? £ pind is
Ki)

Adjust sensor gap distance to 2m,

Did belt moves after
start?

(heck porer source frow sal! weather
stable A230) or not?

Thea, press start and

") e,
use Bui Ti-weter to
Qheck driver board iB
motor socket weather vy
voltage or not?
Y

Replace (tor Hp} {iit tle prota

40 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 48 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart — check RPM sensor device procedure:

Check RPM sensor
prowedure

Sensor cable connected

property”? NO—] Connect Properly

YES
Y

Move the roller so
that meagent closest
to the sensor

Make sure the gap
between maynet'sensor less
than 3 mim

NO Adjust sensor
position

YES

Y

Replace sensor with
cable

‘um power back ott>
press “start” and
comnidewn
Is function OK?

YES—| = Problem fixed

NO
Y

Replace computer
cuble

ur power back ott
press “start" and
comnidown fs function
OK?

YES—e] Problem fixed

NO

ul

Replace Console

4] Service Manual


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 issue troubleshooting form

E1
message Possible cause Things to check Solution
Possible cause Things to check Solution
The upper console check the speed ;
. , Make sure the good connection
board hasn't receive sensor cable is in
; ; for cables
any speed signal for 8 good connection
seconds
E1
message
The motor
cannot move Check th
eck the ga
The speed sensor didn't gp To keep the gap-distance less
. between speed
detect signal completely. than 3 mm.
sensor and magnet.
Check if the sensor
Defective sensor orbad_ jand cables are Change the sensor
cable connection. circuit short or cables.

damaged.

43 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.8 Error Message: E9

Definition: Calibration error.
Configuration:

CONSOLE
DISPLAY BOARD

Send and receive } Lr
speed signal Via |rsysinsoe | | serron SPEED
TX/RX of 5-pin SONAL as
Main wires. |

i iN MOTOR

AC POWER [ z DRIVER BOARD

RPM
SENSOR

; rtm

Cause of E9:
Maybe cause to Calibration error:
1. Inthe Calibration, the soeed sensor may come off or over more than 3mm of gap-distance.
2. Inthe Calibration, main wires may come off or defective contact.
3. Inthe Calibration, power off and then power on immediately.
4. Inthe Calibration, power is Unstable or lower power.
5. Inthe Calibration, the parameter may not correct or the parameter does not deposit entirely.

Troubleshooting
Part Troubleshooting
Wall outlet Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV

or 220AC or not. And the voltage whether stable or not.
speed sensor _|Check speed sensor gap-distance whether less then 3mm or not.
Main wires Check main wires whether it may be broken.

Calibration again |Before the calibration, should check parameter whether setting correct or not. In the
calibration, person and things cannot stand or put on the belt.

Lower Driver Replace Lower Driver board.
board
Upper control |Replace Upper control board.
board

52 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.9 Circuit diagram:

GT65-NT014 110V
TREADMILL CIRCUIT DIAGRAM

OOOOOOOOOO >
i :
Gown Main System Pin Define
AC SWITCH 0 LYS
ry 1—- sw om
g 2-- vpp
| oe, 3-+- TXD
BA 4—- RXD
7 WIRE 5—-— GND
|
I
lI
CONTROLLER

M+ M- JK JK

ore 1s | | mone

Tri | Bi


=== OCR SUPPLEMENT, PDF PAGE 47 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
GT65-NT014 220V CEGS
TREADMILL CIRCUIT DIAGRAM

0600606006065 >

O60

AC POWER INPUT 2 ro) ro) ro)

ACSWITCH 9) 0 Main System Pin Define

Q san BREAKER
AC oO
[J] g

:
f bcc

=)

Ac AC

CONTROLLER

M+ M- JK JK

2—- VDD
3—- TXD

| 4—1- RXD
5— GND
FILTE

5 PIN COMPUTER CABLE (LOWER)
2pin

nn re
