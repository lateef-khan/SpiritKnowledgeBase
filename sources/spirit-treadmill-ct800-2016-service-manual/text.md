<!-- Source: CT800 800845 Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

ST8000B-YT09
Treadmill ervice
Manual (AC 120V)
-------------------------------------------Table of Contents-------------------------------------------
                       1. ST8100 Treadmill Outlines
                       2. Electronic Parts
                           2.1 Upper Controllers
                           2.2 Lower Controller and driver
                       3. Electrical Configuration
                       4. ST8100 Treadmill Operation
                       5. Unit Block Diagrams
                       6. Basic Connections and Wiring
                       6.1 Display Board PCB Component Locations
                       6.2 Inverter PCB Component Locations
                       6.3 INCLINE INTERFACE BOARD PCB Component Locations
                       6.4 Inverter LED Indicator Locations

                       6.5 INCLINE INTERFACE BOARD LED Indicator Locations
                       6.6 Controller Indicator LED debugging
                       7. Product Safety Instructions
                       7.1 Important Safety Instructions
                       7.2 Important Electrical Instructions
                       7.3 Important Grounding Instructions
                       8. Error Messages and Troubleshooting for Electronic Issues
                       8.1 Error Message: LOW SPEED
                       8.2 Error Message: INCLINE ERR
                       8.3 Calibration Procedur
                       8.4 Troubleshooting Procedure Matrix
                       9. Console Maintenanc
                       9.1 Tread Belt and Deck
                       9.2. Service Troubleshooting Checklist – Diagnosis Guide




                                                               1                         Service Manual
10. Troubleshooting Guide
     Electronic System
     Mechanical System

11. Repair Procedures
    Procedure 1 (Calibrating the unit)
    Procedure 2 (Checing wire harness for continuity)
    Procedure 3 (Speed sensor adjustment)
    Procedure 4 (Check roller for magnet)
    Procedure 5 (Adjust torque boost)
    Procedure 6 (Replacing controller)
    Procedure 7 (Replacing wire harness)
    Procedure 8 (Replacing drive motor)
    Procedure 9 (Replacing incline motor)
    Procedure 10 (Belt checking)
    Procedure 11 (Tighten drive motor)
    Procedure 12 (Grease incline motor bolt)




                                    2                   Service Manual
3   Service Manual
1. TreadmillOutlines




          4            Service Manual
             Console




Hand Pulse
Sensor




                       5
                           Service Manual
2. Electronic Parts




            6
                      Service Manual
2.1 Upper Controllers
                                Cooling FAN




                                          Safety key
                  DISPLAY




                            7                          Service Manual
.2 Lower Controller and Driver



                                                   INCLINE MOTOR



              SPEED SENSOR




               DC MOTOR




                                                                   DRIVER BOARD




                                 TRANSFORMER
                                               8                           Service Manual
3. Electrical Configurations




               9               Service Manual
SAFETY KEY
To fits on the Console that activate all functions. If no safety key, console can not be controlled.

CONSOLE
Interface that controls all functions of the Treadmill.

MAIN CONTROLLER
The circuit board consist of the AC power supply for console、incline driver and DC motor driver, link the console to output appropriate
voltages for Incline Interface Board and inverter that control the Treadmill functions.

DC MOTOR
It can change to increase or decrease speed change.

INCLINE MOTOR
This is an ac motor. User can to control variable elevation by console within main controller.

GENERAL INFORMATION
CONSOLE
Contains Key controls and LED Display.

MAIN CONTROLLER
Include power supply、DC motor、incline motor、inverter control circuit and incline control circuit.
DC MOTOR
Work voltage:DC 90V~
Control speed increases and decreases.
INCLINE MOTOR
This is a 120 volt AC motor.
Have four wires, red, black, white and green.
Has one 3 pins cable of position sensor.
If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
The White wire (COM) is neutral.
The green wire is ground.


                                                                            10                                                  Service Manual
4. Product Operation




              11

                       Service Manual
Display Windows



                       LED Display




                  12

                                     Service Manual
LED Layout




             13

                  Service Manual
Operation
Window Display Mode
OFF Mode
   When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode and all windows will appear blank.
READY Mode
   When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program profile name and cycle.
   Press START button to start treadmill on Manual Mode.
SLEEP Mode
   In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
RUN Mode
   In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly and enter OFF Mode.
 Function
SPEED
     Display the current speed in Kilometer mile per hour.
     DISPLAY range is 0.0 to 99.9
     WORK range is 0.8~20.0 kph (0.5~12 mph)
     Press “FAST” or ”SLOW” to adjust speed, each increment and decrement is 0.1 kph(mph).
Incline
     Display the incline position from 0 to 15
     DISPLAY range is 0 to 99.
     WORK range is 0 to 15.
     INCLINE preset value is 0 to 15.
     Press “UP” or ”DOWN” to adjust incline, each increment and decrement is 1.
TIME
     TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time then timer is COUNT DOWN.
     DISPLAY range is 0:00 to 99:99.
     WORK range is 0:00 to 99:59.
     COUNT DOWN setup range is 10:00 to 99:00.
     When TIME is set, the count will go to zero.
     In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will continue count up time.



                                                                      14

                                                                                                                           Service Manual
LAPS
    Display the total working laps quantity.
    DISPLAY range is 0 to 99.
    WORK range is 0 to 99.
    Displays total laps quantity.
DISTANCE
    Display the current distance in kilometer or Mile.
    DISPLAY range is 0.00 to 99.9.
    WORK range is 0.00 to 99.9.
CALORIES
    Displays the cumulative calories burned at any given time during your workout.
    DISPLAY range is 0.0 to 999.
    WORK range is 0.0 to 999.
PULSE
    Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
    DISPLAY range is 0 to 999.
    WORK range is 50 to 200 BPM.
    In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds then display value will become “0 ”.




                                                                         15

                                                                                                                  Service Manual
Function Button Locations


                                           Fan Key

                                 Cooling fan switch on or off
        DISPLAY




  Incline quick keys                           Level quick keys

        2/4/6                                     (2/4/6m)




  PROGRAM BUTTONS




    CONTROL KEYS




                            16

                                                       Service Manual
Function Button In Main Mode
READY MODE
 SAFETY KEY: Fit safety key in right position to power on the computer. When safety key is pulled away from its position, the computer
 will be automatically shut down.
 STOP button: non-functional.
 START button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on
 window display, then machine starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill starts at program preset value in
 PROGRAM.
 ENTER button: Press “ENTER” button to change each function. MANUAL can set using time, Pre-set PROGRAM can set using time
 and speed, Control set time, age and the value of heart rate. User Program 1~2 can set time, speed and incline.
FAST button: If user doesn’t enter a setting then this button is non-functional.

SLOW button: If user doesn’t enter a setting then this button is non-functional.

UP button: If user doesn’t enter a setting then this button is non- functional.

DOWN button: If user doesn’t enter a setting then this button is non- functional.

SPEED RAPID button: 5 preset buttons for rapid speed: (3,6,9km)(2,4,6m)

INCLINE RAPID button: 5preset buttons for rapid incline: 2,4,6

 FAN button: It can to control ON/OFF for the fan.
 DISPLAY KEY：You could select the profile of SPEED or INCLINE by pressing DISPLAY key when select the program.
 ENTER KEY：Press ENTER key enter to parameter setting, and confirm the every setting by pressing ENTER key.Press START key to
 finish the setting.You could change the display of DISPLAY MODE by pressing ENTER key.




                                                                    17

                                                                                                                           Service Manual
RUN MODE
SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down.
STOP button: press “STOP” button to stop treadmill.
START button: non-functional.
ENTER button: non-functional.
FAST button: Press the button to increase your speed and each increase is 0.1kph(0.1mph). If button is pressed continuously then speed
increases to MAX SPEED quickly.
SLOW button: Press the button to decrease your speed and each decrease is 0.1kph(0.1mph). If button is pressed continuously then speed
decreases to MIN SPEED quickly.
UP button: Press the button to raise position and each increase is 1, the maximum incline position is 12.

DOWN button: Press the button to lower position and each decrease is 1, the minimum incline position is 0.

SPEED RAPID button: Speed will set to 2,4,6m quickly.

INCLINE RAPID button: Incline will set to 2,4,6 position quickly.

FAN button: It can to control ON/OFF for the fan.
DISPLAY KEY：
Press DISPLAY key to switch the exercise data shown on the message window when you are workout. After the switch, the system will scan
and display automatically every four seconds. The information as below,
       PROGRAM NAME
       LAPS   XX
       VERT         XXX FT (THE METRIC UNITS IS SHOW “KM” )
       SEG TIME XX：XX(only in HRC MODE will not show this string)
       MAX SPEED         XX：XX (only in HRC and MANUAL MODE will not show this string)




                                                                    18

                                                                                                                         Service Manual
5. Unit Block Diagrams




             19

                         Service Manual
Treadmill Configuration




                          20   Service Manual
6. Basic Connections and Wiring




               21                 Service Manual
6.1 Display Board PCB Component Locations


   PCB Board Top




                                            22   Service Manual
6.2 PCB Board Bottom
                                                                    COOLING FAN


                                                     JK9




          WRITER

                          JK16




    SYSTEM CABLE (12             JK13
                                              JK14
    PINS)

                                                           SAFETY




                                                                                  JK11   CONTACT HR
                   KEY BOARD                                                             HANDLEBAR /
                                                                                         WIRELESS HR
                                        JK3


                                                                    23                                 Service Manual
6.3 DRIVER BOARD PCB Component Locations




                                                             DC MOTOR M+


      AC IN                                                   DC MOTOR M-




 INCLINE DOWN

 INCLINE COM

 INCLINE UP




    TO AC FAN

                TRAN
                TRANSFORMER   INCLINE VR
                                                        REED SWITCH
                                           CONNECTION     SENSOR
                                           TO CONSOLE
                                      24                          Service Manual
6.4 DRIVER BOARD LED Indicator Locations




                                                               MOT_DRV


                                                                SHUT_DOWN




                                                              LIMI



                                                              RPM SENSOR




                                                        PWM
                                                POWER
                      INC_UP     INC_DW



                                           25                   Service Manual
6.5Controller Indicator LED debugging

 Indicator           Function                     Condition                             Reason                              Solve
   LED
POWER      Controller power          If AC voltage is normal, it would be    Voltage is not correct.       Check the supply voltage is90~110V.
                                     always ON. If off, fault condition      Fuse is blown.                Replace Fuse.
                                     exists.                                 Transformer is no good.       Replace controller.
UP         Motion of incline motor   Motion of incline motor is up.          Transistor was broken.        Replace controller.
                                                                             Relay failed.

DOWN       Motion of incline motor   Motion of incline motor is down.        Transistor was broken.        Replace controller.
                                                                             Relay failed
SPEED      RPM sensor indicator      The speed sensor didn't detect          Check the gap between speed   To keep the gap-distance less than 3
                                     Signal completely.                      sensor and magnet.            mm.




                                                                        26                                                       Service Manual
7. Product Safety Instructions




               27            Service Manual
7.1 Important Safety Instructions
   - To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
   - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 120-volt, 15-amp
     grounded outlet with only the treadmill plugged into the circuit.
   - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
     improper adapters or in any way modify the cord outlet.
 7.2 Important Electrical Instructions
   - Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any appliance with a large motor, the GFCI will trip often. Route
     the power cord away from any moving part of the treadmill including the elevation mechanism and transport wheels..
   - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a treadmill is first turned on or even
     during use. If your treadmill is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill itself
     does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
     have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online at
     www.squared.com part # QO120HM.
 7.3 Important Grounding Instructions
   - This product must be grounded. If the treadmill should malfunction or breakdown, ground- ing provides a path of least resistance for electric current,
     reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
     appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
 - DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
   serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
   outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 120-volt circuit, and has a grounding plug that looks
   like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
   as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
   can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must be connected to a permanent
   ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held in place by a metal screw.




                                                                                 28

                                                                                                                                                Service Manual
8. Error Messages and
    Troubleshooting



          29

                        Service Manual
﹒ Error code items：

             Error Message             Explain
             LOW SPEED                 Display board CPU did not receive the RPM signal.
                                       The console board is not detecting the VR voltage value, or the
             INCLINE ERR
                                       voltage value has exceeded the range.




﹒ Prepare：

                             Picture                           Tool name




                                                                Multi-meter




                                                 30

                                                                                                         Service Manual
8.1 Error Message：LOW SPEED
   Definition：Display board CPU did not receive the RPM signal.
   Configuration：





                                                                   31

                                                                        Service Manual
Cause of LOW SPEED
The motor doesn’t turn：LS1/LOW SPEED appears.

Explanation

The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receiver the RPM sensor signal.

Configuration




                                                                                       -32-                                                    Service Manual
The console show LOW SPEED




                             -33-   Service Manual
LOW SPEED solution follow chart




                                  34
                                       Service Manual
LOW SPEED solution follow chart – check RPM sensor device procedure：




                                    35
                                                             Service Manual
                                                                                                        Is sensor cable
                                                                                                        connected properly?




Checking the speed sensor
1) Remove the motor cover hood.
2) The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will
    have a belt around it that also goes to the motor). The speed sensor is small and black with a wire
    connected to it.
3) Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on
   the face of the pulley; make sure the sensor is aligned with the magnet. There is a screw that holds the
   sensor in place that needs to be loosened to adjust the sensor. Re-tighten the screw when finished.




                        Reed switch RPM Speed
                        sensor device




                                                                           36                                                 Service Manual
LOW SPEED issue troubleshooting form


                LS1/LOW
                              Possible cause                  Things to check       Solution
                SPEED message


                                 The monitor hasn't receive   check the speed
                                                                                    Make sure the good connection for
                                 any speed signal for 8       sensor cable is in
                                                                                    cables
                                 seconds                      good connection



                                                              Check the gap
                                 The speed sensor didn't                           To keep the gap-distance less
                                                              between speed sensor
                                 detect signal completely.                         than 3 mm.
                                                              and magnet.




                 The motor can
                   not move                                   Check if the sensor
                                 Defective sensor or bad
                                                              and cables are circuit Change the sensor or cables.
                                 cable connection.
                                                              short damaged.




                                                              Check if the motor
                                                                                    Re-plug the cables
                                                              wire is plug well and
                                 The motor can not work.                            again or change
                                                              the controller is
                                                                                    another controller.
                                                              normal power supply.




                                                                 37                                                     Service Manual
8.2 Error Message：INCLINE ERR
   Definition：The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” ERR” appears on the display.
   Configuration：




                                                                               38                                                         Service Manual
The console show Err
Definition：INCLINE problem, DM show “ERR”, engineering mode error.




                                                               39    Service Manual
Case of INCLINE show Err
Incline VR value exceeds the range. INCLINE Err appears on the display.
Incline motor isn’t operation up or down, making the VR value exceed the range.
After turning on the unit, the display board detects that the incline VR voltage exceeds the range,so INCLINE Err
appears. Action Flow Chart




                                                                          40                                        Service Manual
Troubleshooting


            Part            Troubleshooting

                            1.Reconnect VR wires.
            Incline VR
                            2.Inspect whether the incline wires are broken or disconnected.

                            1.Inspect the incline wire and 12-pin cable connections.
            Display board
                            2.Test whether the VR voltage varies at the incline wire terminal.

                            1.Inspect the wire connections.
            12-pin cable    2.Inspect whether wires are broken or crimped.
                            3.Replace the wires and test again.

            Incline board   Inspect the display board 12-pin connections.




                                                        41                                       Service Manual
Test configuration. The console to driver board connector pin define function
PCB Board Bottom
                                                        P4‐P1
                                                                         COOLING FAN

                                                        JK9

              WRITER            JK16




        SYSTEM CABLE (12      JK13
        PINS)                                   JK14

                                                                SAFETY
                              P1‐P12
                                                P1‐P2



                                        JK3                                                    CONTACT HR
                                                                                       JK11    HANDLEBAR /
                  KEY BOARD
                                                                                               WIRELESS HR
                                       P1‐P12
                                                                                       P1‐P4

                                                                    42                                       Service Manual
Pin definition
  JK13
   P1    Controller S／W P5           Speed up output      P9    Speed sensor input
   P2    UP                   P6     Speed down output P10 +VCC
   P3    DOWN                 P7     GND                  P11 VR IN
   P4    Vin                  P8     GND                  P12 GND


  JK14
         Safety switch signal input         VDD
   P1                                 P2


  JK9

   P1    FAN OUT     P3       GND

   P2    FAN OUT     P4       GND



  JK11

   P1    GND       P2     VCC

   P3    HEART     P4



  JK3：

   P1     KEY_D0        P2         KEY_D1    P3        KEY_D2     P4    KEY_D3

   P5     KEY_D4        P6         KEY_D5    P7        KEY_D6     P8    KEY_D7

   P9     SCAN_0        P10        SCAN_1    P11       SCAN_2     P12 SCAN_3



                                                                               43    Service Manual
Test Configuration. Driver board control function relate parts location




                                                                                     DC MOTOR
                                                          MOTOR
                                                          POWER




     INCLINE                                                      JK4
     POWER           JK2
                                                                  P3‐P1




                                                                     P12‐P1

                                                                        JK1
                                               INCLINE VR


                                                                        CONNECTION
                                                                        TO CONSOLE
                                                     44

                                                                                       Service Manual
Pin definition
JK1 (CONNECTION TO CONSOLE)

                                                   Speed   sensor
P1   Controller S／W P5   Speed up output P9
                                                   input
                         Speed         down
P2   UP            P6                         P10 +VCC
                         output
P3   DOWN          P7    GND                  P11 VR IN
P4   Vin           P8    GND                  P12 GND


JK4 (INCLINE VR)

P1   +VCC          P2    VR IN                P3   GND


JK2 (INCLINE POWER)

BLACK WIRE     DOWN      WHITE WIRE       COM       RED WIRE   UP


DC MOTOR(MOTOR POWER)

WHITE WIRE     M- RED WIRE        M+




                                                               45

                                                                    Service Manual
Test Procedure：
 1.    Run calibration again.
 2.    Does the incline motor move at all?
 3.    If no, do the Up/down lights on the incline board light?
 4.    If they light, do the relays click on?
      If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red)
       or down (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as
       the mains voltage ~110VAC. If the voltage is present but the motor doesn’t move, then the motor is bad.
      If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).
 5.    If the motor moves, is there a sensor reading on console?
      The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0 for lowest incline. The Incline window is a counter
       that is showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the
       position sensor wiring or circuitry.
      If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
      Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
      If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
      If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and there should be a voltage
      between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical,
      as long as it’s somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves,
      but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
 6.    Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is
        faulty.
 7.    If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the
       incline board.
      There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.
      The only problems that are possible are a bad solder joint or broken circuit on the board.
      Console connector wiring, these connections are the same on the incline board and at the console.
                   Pin 10 = 5vdc
                   Pin 11 = position signal 0~5vdc
                   Pin 12 = ground
 8.    If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there,
      but is there at the incline board then check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
 9.    If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.



                                                                                   46

                                                                                                                                                    Service Manual
 Error Message：INCLINE ERR
  Definition：During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

  Configuration：




                                                                        47

                                                                                                              Service Manual
Cause of INCLINE show Err

         Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
          Explanation

           Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which changes the VR value.
           The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it should be. INCLINE E2
            appears on the display.
          Action Flow Chart




                                                                               48
                                                                                                                                             Service Manual
Troubleshooting
            Part            Troubleshooting
                            1.Press incline UP key. The driver board UP LED lights.
            Display board   2.Press incline DOWN key. The driver board DOWN LED lights.
                            3.If not as above, inspect the cable and connections.
                            1.Inspect whether the 12-PIN cable is connected well.
            12-pin cable
                            2.Test by replacing the cable with a good one.
                            Inspect whether the driver board UP/DOWN LED is lit.
                            1.Press incline UP or DOWN key again, making the incline motor return to its
            Driver board
                            position.
                            2.If ERR still appears, re-calibrate the incline set.
                            1.Inspect whether the incline motor is stuck.
                            2.Inspect whether the incline gears are cracked.
            Incline motor
                            3.Test whether the incline motor has a broken circuit.
                            4.Re-calibrate the incline set.




                                                       49
                                                                                                           Service Manual
     8.3 CALIBRATION PROCEDURE
 CALIBRATION PROCEDURE
1)    Remove the safety key
2)    Press and hold down the Start and Fast (speed up) buttons with one hand and replace the safety key with the other. Continue to hold the Start and Fast key
      until the window displays “Factory settings”, then press the enter key.
3)    You will now be able to set the display to show Metric or English settings. To do this, press the up or down key to show which you want, then press enter.
4)    Make sure the wheel size diameter is 2.98 then press enter
5)    Adjust the minimum speed (if needed) to 0.8kph and then press enter
6)    Adjust the maximum speed (if needed) to 20.0kph and then press enter
7)    Adjust the maximum elevation (if needed) to 15 and then press enter
8)    Press start to begin calibration. The process is automatic; the speed will start up without warning, so do not stand on the belt.
9)    During calibration the speed calibration will happen first then incline calibration. When incline starts the INCLINE LED window will show the actual reading from
      the potentiometer (VR). If the incline is at the bottom position the reading in the Incline window will be about 235. The Distance window will show the computer
      setting of % grade for incline. The first setting will be 15, so the incline motor will start to move the treadmill base up towards the 15% grade setting. The Incline
      window should show a readout that is changing as the base inclines, from a reading of about 235 until the base reaches the top where the readout should be
      around 22.
       If this number does not change at all when the incline motor moves, then the console is not receiving a reading from the potentiometer.

      Adjusting the speed sensor:
      If the calibration does not pass you may need to check the speed sensor alignment.
      1) Remove the motor cover hood.
      2) The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will have a belt around it that also goes to the motor).
           The speed sensor is small and black with a wire connected to it.
           Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on the face of the pulley; make sure the sensor is aligned
           with the magnet. There is a screw that holds the sensor in place that needs to be loosened to adjust the sensor. Re-tighten the screw when finished.




                                                                                                                                                          Service Manual
                                                                                      50
Maintenance menu:
1) Press and hold the Start, Stop and Enter key at the same time, until the display shows “Engineering mode” (it may say maintenance menu, depending on version).
   Press the Enter key.
2) You can now scroll through the menu using the up and down keys. Use the Stop key to return to previous menu selection. The menu selections are:


    1) Key Test – Press each key to verify it is functioning correctly
    2) Display test - Lights all LED lights
    3) Functions
        i.     Sleep - Turns sleep mode on or off. When off, display is always lit.
       ii.     Pause - Turns pause mode on or off. When on, Pause lasts 5 minutes.
      iii.     Maintenance - Reset odometer readings
      iv.      Units - Set display to English or Metric readings
       v.     Grade Return (GS Mode) - Returns the elevation to lowest setting when pause is pressed
      vi.      Beep – Turns the speaker (beep sound) on or off.
    4) Security – Sets the Child Lock function. This function locks out the keypad until a pre-determined key sequence is pressed. Key sequence = Start & Enter
         held down together until unlocked.




                                                                                                                                                Service Manual
                                                                                 51
If calibration fails:
   a. Remove motor cover and check all the wiring connections from the incline motor to the incline board are good. Push in all connectors to make sure they are fully seated.
      The connectors to be concerned with are:
   i. The 3 power wires for the motor: Red = Up, Black = Down, White = Neutral.
  ii. The position sensor wires, 3-pin connector with board ref. Designation of ‘VR’. Red =5vdc, Black = Ground, White = Position signal
      (0~5v depending on incline position).

iii. Main wire harness at bottom of board.




                  3 power wires for the motor




                                      UP
                                                 DOWN


                                                                                                    Main wire



                                3-pin connector with board


    b.   Run calibration again.
    c.   Does the incline motor move at all?
    d.   If no, do the Up/down lights on the incline board light?
    e.   If they light, do the relays click on?
                                                                                                                                                             Service Manual
                                                                                     52
            i. If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red) or
                 down (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the
                 mains voltage ~ 120VAC. If the voltage is present but the motor doesn’t move, then the motor is bad.
           ii. If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).
f.   If the motor moves, is there a sensor reading on console?
            i. The Distance window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0 for lowest incline. The Incline window is a counter that is
                 showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the position
                 sensor wiring or circuitry.
           ii. If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
              Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
              If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
          iii. If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and there should be a voltage
              between the red and white wire. This voltage will be about 4.5~4.7 vdc when the motor is at the lowest position (the number isn’t too critical, as long as
              it’s somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves, but the counter still does not register
              then there may be a bad wire connection between the potentiometer and the console.




                                                                                                                                                               Service Manual
                                                                                    53
iv. Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
 v. If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the
    incline board. There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the
    console connector. The only problems that are possible are a bad solder joint or broken circuit on the board.
           1. Console connector wiring, these connections are the same on the incline board and at the console.
                   a. Pin 10 = white wire, 5vdc
                   b. Pin 11 = light blue wire, position signal 0~5vdc
                   c. Pin 12 = pink wire, ground
vi. If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there, but is there at the incline board then
    check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
vii. If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.




                                                                                                                                                    Service Manual
                                                                          54
8.4 Troubleshooting procedure matrix
                    Condition                                            Reason                                                    Solve
When turn on power, ON/OFF switch isn’t lit.          1 Power cord isn’t plugged into outlet.         1 Plug the power cord into outlet.
                                                      2 Power cord isn’t plug into unit.              2 Plug the power cord into unit.
                                                      3 The voltage of outlet is too low.             3 Check the voltage of outlet.
                                                      4 Plug or connector of power cord is open.      4 Replace power cord.
                                                      5 Connector of power cord is broken.            5 Replace power cord.
                                                      6 Connecting cable disconnected.                6 Check if wire is disconnected, connect it again.
                                                      7 Breaker tripped.                              7 Press the small red button to return to original status.
                                                      8 Breaker is broken.                            8 Replace breaker.
                                                      9 ON/OFF switch is broken.                      9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown     1 Check the voltage of power is110-120V. Replace
                                                        broken on controller.                         controller.
 When insert safe key, no display on monitor.           1 Haven’t switch ON/OFF switch.               1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.      2 Insert the safe key on right position.
                                                        3 12 PIN Computer connector not plugged       3 Please check the wire and connect again.
                                                          in properly.                                4 Replace 12 PIN computer cable.
                                                        4 12 PIN computer cable is broken.            5 Replace fuse or controller.
                                                        5 Fuse on controller is blown.                6 Replace varistor or controller.
                                                        6 Varistor on controller is blown.            7 Replace safety key device.
                                                        7 Safety device is broken. (open)             8 Replace console.
                                                        8 Other components are faulty.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)            1 Replace the safety key device or console.
 When press “START”, treadmill doesn’t start.           1 AC Motor U or V or W wire isn’t connected   1 Please check and plug again.
                                                          into right position.                        2 Replace motor or check the wire and connector if it was
                                                        2 Motor is broken.                              broken.
                                                        3 Treadmill controller shut down and LED      3 Turn off the AC switch and turn on power again.
                                                          would be ON.
Treadmill stops or shuts off by itself.                 1 House breaker tripped.                      1. Reset it.
                                                        2 Treadmill breaker tripped.                  2. Reset treadmill breaker.
                                                        3 Treadmill controller fuse is broken.        3. Replace with new fuse
                                                        4 Treadmill controller shut down and LED      4. Turn off the AC switch and turn on power again.
                                                          would be ON.
After removing safe key, treadmill can’t stop.          1. The safety key device is broken.           1. Replace with new safety key device.
LCDs not bright, incomplete or imperfect.               1. LCD light is broken.                       1. Replace with new LCD or console.
                                                        2. Power to console too low.                  2. Check AC power is 110-120V.
                                                                                                      3. Check power to console.
                                                                                                      4.Replace lower controller.

                                                                                                                                                Service Manual
                                                                               55
LCD displays not bright, incomplete or imperfect.    1. LCD displays are broken.                   1. Replace with new console.
When press “START” button to start treadmill, running 1. Controller experienced unusual shut     1. Turn off power and reset the treadmill.
belt isn’t running and window displays “LS1/LOW          down; the Shut_ DOWN light will be
SPEED” error message after 10 seconds.                   always bright.                          2. Plug wires again.
                                                      2. AC Motor wires (U or V or W) aren’t
                                                         plugged into controller.                3. Plug the wire again on controller, connector and console.
                                                      3. Computer cables not connected properly. 4. Replace with new wires.
                                                      4. Computer cables are broken or damaged. 5. Replace with new motor belt.
                                                      5. Motor belt is broken.                   6. Replace with new controller.
                                                      6. Controller is broken.                   7. Replace with new AC motor.
                                                      7. AC Motor is broken.                     8. Replace with new console.
                                                      8. Console is broken.
The speed of the belt doesn’t match console display. 1. Console is not calibrated.               1.Calibrate the console
The incline position doesn’t match console           1 Console is not calibrated.                  1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “INCLINE        1 Position sensor value of incline motor is   1 Turn off the AC switch and turn on power again.
ERR”.                                                wrong.                                        2. Calibrate the monitor.
After pressing “START” button, the treadmill stops   1 Controller is broken.                        1 Turn off the AC switch and turn on power again.
immediately.                                                                                        2 Replace controller and calibrate it.
Erratic pulse display.                               1. Another chest belt in use around treadmill. 1. Check for other chest belt use around treadmill.
                                                     2. Other magnetic field disturbance.           2. Change the position or direction of treadmill.
                                                     3. Receiver is broken.                         3. Replace with new receiver.
After pressing “START” button, the treadmill stop    Controller was broken.                         Replace with new controller and calibrate it.
immediately.
 FAST/SLOW button of SPEED ADJUSTMENT               1 The connector of SPEED CABLE and   1. Connect cables again.
 SWITCH can’t be used.                                 CONSOLE not connected properly.
                                                    2 The connector of SPEED CABLE and   2. Connect cables again.
                                                      SPEED ADJUSTMENT SWITCH
                                                      W/CABLE not connected properly.    3. Connect cable again.
                                                    3 The connector of SPEED CABLE or
                                                      SPEED ADJUSTMENT SWITCH/W/CABLE
                                                      Is damaged.                        4. Replace with new buttons.
                                                    4. Button of SPEED ADJUSTMENT SWITCH
                                                       is broken.                        5. Replace with new cable.
                                                    5. The connector of SPEED CABLE or
Speed button just can press FAST, can’t press SLOW.    SPEED ADJUSTMENT                  6. Replace with new cable.
                                                       SWITCH/W/CABLE is damaged.
Speed button just can press SLOW, can’t press FAST. is damaged.



                                                                                                                                              Service Manual
                                                                             56
                                                      6. The connector of SPEED
                                                       CABLE or SPEED ADJUSTMENT
                                                       SWITCH/W/CABLE is damaged.
                                                                                                    1 Connect the wires again.
UP/DOWN button of                                     1 The connector of INCLINE CABLE
INCLINE ADJUSTMENT SWITCH can’t be used.                 and CONSOLE not connected properly.        2. Connect the wires again.
                                                      2. The connector of INCLINE CABLE
                                                         and INCLINE ADJUSTMENT
Incline button just can press UP, can’t press DOWN.      SWITCH W/CABLE not connected               3. Replace the cable.
Incline button just can press DOWN, can’t press UP.      properly.
                                                      3 The connector of INCLINE CABLE or
                                                         INCLINE ADJUSTMENT SWITCH                  4. Replace buttons.
                                                         CABLE got damage.
                                                      4. Button of INCLINE ADJUSTMENT               5. Replace the cable.
                                                         SWITCH is broken.
                                                      5. The connector of INCLINE CABLE or          6. Replace the cable.
                                                         INCLINE ADJUSTMENT SWITCH
                                                         CABLE got damage.
                                                      6. The connector of INCLINE CABLE or
                                                         INCLINE ADJUSTMENT SWITCH
                                                         CABLE damaged.
Hand pulse lost its function.                         1. Hands not on the hand pulse sensors or     1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                          only one hand on sensor.
                                                      2. The connector of HANDPULSE W/WIRE          2. Connect the cable again.
                                                         and Console not connected properly.
                                                      3. The wires got damaged when connecting      3. Replace with new cable.
                                                         the HANDPULSE W/WIRE and Console.
                                                      4. Hand pulse board is broken.                4. Replace console or Hand pulse board.
Wireless lost its function.                           1. Chest belt not worn properly.              1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                       2. Distance is too far and exceeds range of      oriented correctly.
                                                         receiver.                                  2. User chest belt in front of console within 3 feet.
                                                      3. Chest belt battery is weak or dead.        3. Replace with new lithium battery type is CR2032.
Chest belt too close to the treadmill.                Weak battery.                                   Replace with new lithium battery with type CR2032 .
Tread belt does not run in center.                    Tread belt tension not even across tread belt.
                                                                                                      See treadmill belt adjustment
Tread belt hesitates while being stepped on.          Insufficient lubricant on tread belt.Tread belt See treadmill belt lubrication
                                                      tension insufficient
Black particles collecting under treadmill.           Drive belt is breaking in.                    Vacuum under treadmill periodically.


                                                                                                                                                 Service Manual
                                                                                   57
Noise under motor cover.              1. Worn brushes or bearings on motor.            1. Replace with new motor.
                                      2. Front roller bearings are defective.
                                      3. Drive belt is misadjusted (too tight or too   2. Replace with new front roller.
                                       loose).
                                                                                       3. Adjust motor position.
Noise in the rear of the treadmill.   1. Rear roller bearings are defective.           1. Replace with new rear roller.

                                      2. Rear roller misaligned.                       2. Adjust rear roller position.




                                                                                                                           Service Manual
                                                                   58
9.General Maintenance




                        Service Manual
          59
9.1. Service Troubleshooting Checklist – Diagnosis Guide

Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common problems
that may not be covered under the treadmill’s warranty.

PROBLEM                                         SOLUTION/CAUSE

Display does not light                          1) Tether cord not in position.
                                                2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                                 3) Plug is disconnected. Make sure plug is firmly pushed into
                                                   120 VAC wall outlet.
                                                4) Breaker panel circuit breaker may be tripped.
                                                5) Treadmill defect. Contact your dealer.

Tread-belt does not stay centered               The user may be walking while favoring or putting more weight
                                                on either the left or right foot. If this walking pattern is natural,
                                                track the belt slightly off-center to the side opposite from the belt
                                                movement.

Treadmill belt hesitates when walked/run on     See General Maintenance section on Tread-belt Adjustment.
                                                Motor drive belt may be loose.

Motor is not responsive after pressing start    1) If the belt moves, but stops after a short time and the
                                                    display shows “LS”, run calibration (See procedure on next page).
                                                2) If you press start and the belt never moves, then the
                                                   display shows LS, contact service.

Treadmill will only achieve approximately       This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord.
7 mph but shows higher speed on display        If an extension cord is required it should be as short as possible and heavy duty 16 gauge minimum.
                                                 Low household voltage. Contact an electrician or your dealer.
                                                 A minimum of 120 volt AC current, 60 hz is required.




                                                                                       60                                                             Service Manual
Tread-belt stops quickly/suddenly when          High belt/deck friction.
tether cord is pulled

Treadmill trips on board 15 amp circuit         High belt/deck friction.

 Computer shuts off when console is             Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to Grounding Instructions .
touched (on a cold day) while walking/running

House circuit breaker trips, but not the         Need to replace the house breaker with a “High
treadmill circuit breaker.                      inrush current” type breaker




                                                                                   61                                                                   Service Manual
                                        Treadmill Troubleshooting

ELECTRONIC SYSTEM
No power                                   1.     Unit must be plugged into an outlet with power.

There is no power to the console.          2.     Power switch must be illuminated.
                                           3.     Tether cord must be in place.
                                           4.     Check treadmill circuit breaker.
                                           5.     Check “POWER” LED on controller.
                                           6.     Make sure wires on board are plugged in securely.
                                           7.     Check wire harness for continuity.
                                           8.     If LED’s on controller are not lit, test fuse on controller. If fuse is good, replace
                                                  controller.
                                           9.     If LED’ are on, replace console.
LS error                                   1. Run the calibration procedure.
Belt movement for a few seconds            2. Adjust speed sensor.
then LS error                              3. Check roller for magnet.
                                           4. Check wire harness for continuity.
                                           5. If roller has a magnet and sensor adjustment does not fix, replace speed
                                                  sensor.
LS error                                   1. Run the calibration procedure.

No belt movement at all then LS error      2. Check wire harness for continuity.

                                           3. Look at LED labeled “PWM”.

                                                --If it lights up when the START button is pressed, replace the controller.

                                                --If it does not light when the START button is pressed, replace the console.

Incline does not work                      1. Run the calibration procedure.

                                           2. Check wire harness for continuity.

                                           3. If there is an ERR message in the incline window, make sure that all the wires
                                                  from the incline motor are connected to the controller correctly. If they are
                                                  connected correctly, and the calibration does not fix, replace the incline motor.

                                           4. When the UP and DOWN buttons are pressed, there should be a “beep” and a
                                                  number change in the incline window. If there isn’t ,replace the console.

                                           5. Observe the UP and DOWN diagnostic lights on the controller. When the UP or
                                                  DOWN buttons are pressed, you should (1) see one of the lights come on and
                                                  (2) hear a relay click.

                                                 --If there is no relay click and no diagnostic lights, replace console, lower and
                                                  middle wire harness, and controller.

                                                   --If there is a relay click and a diagnostic light and motor wires are connected
                                                  correctly, replace incline motor.

Belt surging                               1. Adjust torque boost.

Belt speeds up and slows down frequently   2. Adjust speed sensor.

                                           3. Replace controller.



                                                                      62                                          Service Manual
                                      Treadmill Troubleshooting
MECHANICAL SYSTEM
Belt noise                                  1. Check belt to see if it needs to be tracked.

                                            2. Take off motor hood to make sure noise is from belt.

                                            3. Check belt and deck for damage.

                                            4. Check deck and re-lube.

Drive motor noise                           1. Check wires around motor for rubbing.

                                            2. Remove, clean and re-insert the motor brushes.

                                            3. Replace motor.

Deck noise                                  1. Tighten deck bolts.

Squeaking or creaking while walking         2. Clean and re-lube deck.




                                                                63                                    Service Manual
                                 Treadmill Troubleshooting
PROCEDURE 1： Calibrating the unit
1.1 Remove tether cord.
1.2 Press and hold the START and FAST buttons. Replace the tether cord while maintaining the buttons.
    Message window will be displayed “FACTORY SETTING”, press ENTER to go into test mode.
1.3 Use UP/DOWN button to change from Km (metric) to M (English).
1.4 Wheel size will be displayed in the Distance window. Use the UP/DOWN buttons to change. It should be set
    to 2.92~2.98.
1.5 Minimum speed will be displayed in the Distance window. Use the UP/DOWN buttons to change. It should
    be set to 0.5.
1.6 Max speed will be displayed in the Distance window. Use the UP/DOWN buttons to change. It should be set
    to 12.0.
1.7 Max elevation will be displayed in the Distance window. Use UP/DOWN buttons to change. It should be set
    to 15.
1.8 Press START. Unit will now auto-calibrate the speed and incline. Do not stand on belt during calibration.
    Unit will reset when it completes the calibration.

PROCEDURE 2： Checking wire harness for continuity
2.1 Set your multimeter to read ohms.
2.2 Place the test leads at opposite ends of the wire, make sure both leads are on the same wire and are in
    contact with metal.
2.3 If the reading is close to 0 ohms, the wire has continuity (unbroken).
2.4 If the reading is very high or there is no reading at all, there is no continuity.
2.5 If there is no continuity, the harness needs to be replaced.

PROCEDURE 3： Speed sensor adjustment
3.1 Take off the motor hood..
3.2 The speed sensor is located on the frame, near where the drive belt goes around the front roller.

PROCEDURE 4： Check roller for magnet
4.1 The front roller should have a round magnet and a round counter weight.
4.2 Take a screw or something metallic and test each one.
4.3 Only one should be magnetic.

PROCEDURE 5： Adjust torque boost
5.1 Using a small screw driver, turn the dial counter clockwise until it stops.
5.2 Press the START button on the console.
5.3 With someone standing on the walking belt, turn clockwise until the belt begins to move.
5.4 Increase the speed and check for smooth belt movement.


PROCEDURE 6： Replacing controller
6.1 Disconnect power cord from unit.
6.2 Remove motor hood.
6.3 Remove two Phillips screws holding in the controller.
6.4 Disconnect all wires connected to the controller.
6.5 Insert new controller, secure with Phillips screws.
6.6 Reconnect wires to controller.



                                                            64                                 Service Manual
                                  Treadmill Troubleshooting

PROCEDURE 7： Replacing wire harness
7.1    Turn power switch off.
7.2 Unplug harness from console and controller.
7.3 Tie the end of the new harness to the old harness (with a zip-tie or spare wire).
7.4 As you pull the old harness out of the upright, you will pull the new harness in.
7.5 Connect to board and console, & turn power back on.

PROCEDURE 8： Replacing drive motor
8.1    Turn power switch off.
8.2 Disconnect red and black motor wires from controller.
8.3 Take off drive belt.
8.4 Insert new motor into place.
8.5 Put drive belt on.
8.6 Put in four motor bolts. Do not tighten them all the way down.
8.7 Tighten down the four motor bolts.
8.8 Plug the motor wires into the controller.



PROCEDURE 9： Replacing incline motor
10.1 Turn power switch off.
10.2 Turn treadmill onto its side.
10.3 Disconnect motor wires from controller.
10.4 Remove bolt from incline tube.
10.5 Remove bolt from top of incline motor and take out motor.
10.6 Insert new motor and put in bolt on the top.
10.7 Reconnect motor wires to controller.
10.8 Turn on unit. The new motor should turn until it is at “zero”.
10.9 Insert bolt into incline tube.




                                                            65                          Service Manual
                                  Treadmill Troubleshooting

PROCEDURE 10： Belt Checking

1. Check belt to see if it touches belt guide.




2. If belt touches belt guide, turn on unit power and then press the START button on the console. Let it run at
   the lowest speed 0.5mph.
3. To make belt in the center, use an Allen Wrench to turn left rear roller adjustment clockwise. No more than
   1/4” of a turn.




4. When belt is in the center, there will be no more belt noise.




                                                            66                               Service Manual
                                   Treadmill Troubleshooting

PROCEDURE 11： Tighten Drive Motor

1. Remove motor top cover and check if motor screws are loose.
2. Tighten




PROCEDURE 12： Grease Incline Motor Bolt

1. Adjust incline level to the highest.
2. Remove motor cover. Check bushing and bolt of incline motor.
3. If bushing or bolt of incline motor is dirty or dry, clean it and then grease it.




                                                               67                      Service Manual
                                  Treadmill Troubleshooting

Engineering Mode


1.   Remove the tether cord.
2.   Press and hold the START, ENTER, and STOP buttons and replace the tether cord.
3.   The display will show “ENGINEERING MODE MENU”. Press ENTER.
4.   Press the UP or DOWN buttons to scroll through the following sub menus:
     －KEY TEST
     －DISPLAY TEST
     －FUNCTIONS
     －SECURITY

       -CALIBRATION:
        Speed Calibration: In this mode, you can test the speed.
        Incline Calibration: In this mode, you can test the incline.

     －KEY TEST
      Press all buttons on console.

     －DISPLAY TEST
      Press ENTER. Console will test each segment or LED. Look to see if there are any burned
        out or not working.

     －FUNCTIONS
      Sleep Mode On/Off -------------------------- Press ENTER to turn on or off.
      Beep Sound On/Off -------------------------- Press ENTER to turn on or off.
      GS Mode On/Off------------------------------ Press ENTER to turn on or off.
      Units English/Metric-------------------------- Press ENTER to change.
      Maintenance ---------------------------------- Press ON/OFF to change.
      Lube Message Reset------------------------ Press ENTER to reset.
      Odometer Message Reset----------------- Preset ENTER to reset.

     －SECURITY
      The display will show “CONSOLE LOCKED” before idle mode----------------------------
      Press ENTER to turn on or off. To unlock display, press START and ENTER.




                                                             68                             Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Du] Jeuol}eUusa}U] OoeAG

OOVAC

(AozT Ov) JONUCI/
DIIAJO |JIWUPeCoI]

60LA-d0008sLS


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 120 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2 >> S
o C8 UOHISUUOD APPIN WW OOD NIdzZL BCC # =] bold
& E
®o

a oi In 3
oO = oD <
E 2 Ee — fo)
xs) [or N
& 8 <2) im —78 SB i
~ 7 ao ~ oe a
no £ oF :
£ _ el o| £
Lf Amo}|akjuses6)aiqed punold S =
a De Ky So
or o| = z=} ©
SISlel 4 a -
g|"|5| = S| o
Bia < =
aq" ° oO
ia ie)
ge 3 Zz
£35 7 Yn
z S =
ira]
ob BG
23,8 Sanaa aa
210829 oO o& 4 Ins eso eb
HDADFSULHNONN SSS wwe MME OS
®O z 3 a
=) &y2
oO To) c es 5
= Osc i) 2 © 58 2
x = io) LN 4 en
Coo op>He Ft Bp
SS55LZ9A FEE <~F fi rs Ui 25
pos pas 5S dD) ae Zz .
novor~oneaosnea a) AS s 3]
2. KC] 0 0 | a}
Lt} tt ty tt ty aS
T T T T tu LU
TKTNMFOORDDOTKN Z
rea
0 ol
Zor
tf
ag
ke
2
=| £
= ao =
O aul RIG WWOSh = 3 alll
ke 4 oOo (0) =
= ce —________] S| a (e)
= SIM eum WwOSP 3
iS) c
~¢ faq (0)
Oo g
= — 58 Oo
Q i Os5 g
SN o Bred ee 5
55 o 'S) as}
a6 YOLODANNOD a =
= | fe)
35 2 = II g
£U (Mo}}BA/UB9ID oul PUNO)

3 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDY 2d1AlaS

SOUIINO| [MW pedlL “T


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[DNUD|T AIIALIS

SUeCd IJIUOI}II|4 Z


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AlaS L

AV1dSIG

NvV4 3uljooD

$19]]01]U09 add TZ


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[DNUD|T AIIALIS

uoieiadoO JONPOld "vy


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[DNUD[T AIIAJIS

cL

Aeidsiq ait

smopul\\ Aeldsiq


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 28 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AlaS

oT

SNOLLNG NWVeSOdd

A\SoOlv
46 @3)—Z
1/9) 6/s)\m'y
a€jezie/i

9/v/7

(w9/r/Z)

shay YOINb auljou|

sha) OINb jaAaT

conan)

JJO 40 UO YOIMS Ue} BUI|OOD

Aa ue4

suolje907] UOWWNg UONJUN{


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[DNUD|T AIIALIS

sueibeig yOoOIg UN “Ss


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUD|T 2d1AlaS oz

HOLIMS
WAMOd
Jas YA

fn | CY eo
a — Guvod wAAra ideo totiae
ANTIONI

ino
aNrl
NIANTT
MAID Id NV

wd
UAAVAdS

UVAATIONVH
4H

Aan suas ==> =
auvod AV 1dSId ONF1009
UsAMoaU
WH SSA THIN =

uoieINH WUD |jlwpeasL


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUD| Jd1A1aS

Bull pue SuoldaUUOZD JISeg ‘9


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUD|Y AD1A1aS zz

do} pieog god

SUOI}ENO7] JUBUOdWIOD Add pieog Avjdsiq [9


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.2 PCB Board Bottom

1512-155] 1400
et)
8122882450145
¥J-66240

—SSSaes
Sees

Saad

=t*r?r FPtrrr

SYSTEM CABLE (12 | paca | : i = @ |

PINS)

PSH do. o zill =: pe SS ‘s
Ose : =H

eteztatet tiescetee  €tzeerreree

fe @rrerrtee ererrstece #eerrrere

evensess SRSEE SEPP REESE Seeteecer ci eerssee SSStttess SPS ereEe Sferrerer

CONTACT HR
HANDLEBAR /

WIRELESS HR

23 Service Manual

KEY BOARD


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.3 DRIVER BOARD PCB Component Locations

_|_S pc Motor M+ |

‘env x wes = | range | : _

Pare |. ; 72-090908001 Me

[_ INCLINE DOWN ems 8 3 emi ii MN II

ee co 02873500037
¥- 3-2350L

[ INCLINE COM

g INCLINE UP

TO AC FAN

TRANSFORMER INCLINE VR

REED SWITCH

CONNECTION SENSOR
TO CONSOLE

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.4 DRIVER BOARD LED Indicator Locations

gf ew Y | __f mot_prv )

% St:
oe SHUT_DOWN

*. 1 wo 4

*
-

re 1.3 12-090908001 AO
100) AAT )
ae’ £02873500037 al
- —£2o LIMI
~S = 3 |

i = ‘ f 4
ne tl) o/ ' RPM SENSOR |

25 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[DNUD|T AIIALIS

suononijsu Ajajes JONPOld "2


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.1 Error Message : LOW SPEED

@ Definition : Display board CPU did not receive the RPM signal.
@ Configuration :
e

CONSOLE
DISPLAY BOARD

MOTOR SPEED
SIGNAL

RPM SENSOR |=
SIGNAL

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER » DRIVER BOARD

=< SIGNAL

2 PIN RPM
SENSOR

31

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of LOW SPEED
The motor doesn’t turn : LS1/LOW SPEED appears.

Explanation
The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receiver the RPM sensor signal.

Configuration

CONSOLE
DISPLAY BOARD

RPM SENSOR é MOTOR SPEED
SIGNAL |e SIGNAL

| ;

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER » DRIVER BOARD

= SIGNAL

- RPM
: SENSOR

-32- Service Manual


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUDJ] aI1A1aS -¢-

INTDNI

SaHOTVD JINVISIG

DNVLSIG INIDNI

iSNINHYM

" LIANAS

o

GSddS MO] MOYS IjOSUuOD JUL


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 53 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LOW SPEED solution follow chart

LS1I/LOW
SPEED
showing up

D ES Check RPM sensor
ia procedure

NO

u

Open the motorhood
and turn the power
back on

hd
Press "start" to
count down and
watch the PWM
LED on the
controller

Connect properly |<

NO YES——+}_s Replace cable

7 YES

Tum the power back
on and press "start™ NO
to count down

um the power
back on. Is
function OK?

Are only POWER and PWM LEDs on

YES
YES
Replace controller

NO

:

Motor cable connected to M+ M-

Hl terminals properly
Py YES Replace Console
Problem fixed
Problem fixed YES
Y
ar Replace controller Problem fixed

YES

Turn the power back on and press NO
art" to count down. Is function OK2 {
Replace controller

NO

ul

Replace motor

34
Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 67 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LOW SPEED solution follow chart - check RPM sensor device procedure :

Check RPM semsor
procedure

Sensor cable commected

fa Noe) Conmece Properky
property?

YRS.
¥

Miowe the roller sao
that nmeagent closest
bo thee semsaor

Miakoe sume th re -
pata ana “wdjust sensor

hetwecm mene semis bees hii] eee
Than 3 mm P a
TES.
Replace semsor with
cable
um power back o
age fF al
posse Uatert™ and ES — te Problem fixedt

comm hha
Ts fuoection (+R?

iL
¥

Replace computer
cable

Tm power back o
press "start" emicl
cormintdiown Ts Tumection

CakY

ES Proipler Fixect

hc

¥

Replace (Sonscbe

35
Service Manual


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.2 Error Message : INCLINE ERR

@ Definition : The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” ERR” appears on the display.
@ Configuration :

DISPLAY BOARD

INCLINE
VR
VOLTAGE
INCLINE
MOTOR
DRIVER BOARD ex: VR VOLTAGE INCLINE VR SET

©) INCLINE DOWN LED
QC INCLINE UP LED

38 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUD/[ AI1A1aS 6E

6066006000 seegecogoes
: ® e686 6 ® 600
4 e ; bt 4 lL ae | :

S0CG000CC000000 000008

‘JO1J9 BPOW Suaaulsua “,YYI,, MOYS WIC “Wa|qosd INITONI : UOIUIEq
JJ=] MOUS 3JOSUOD BY L


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Case of INCLINE show Err

Incline VR value exceeds the range. INCLINE Err appears on the display.
Incline motor isn’t operation up or down, making the VR value exceed the range.
After turning on the unit, the display board detects that the incline VR voltage exceeds the range,so INCLINE Err

appears. Action Flow Chart C +)
INCLINE VR

ee

~
i
DRIVER BOARD

ive a

E
|

DISPLAY BOARD

a

¥

| ¥

DISPLAY OPERATES ERR APPEARS ON
NORMALLY THE DISPLAY
40

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test configuration. The console to driver board connector pin define function

PCB Board Bottom

m! JK16
hues

—SSnnee
seuss

eee

eoseer v +++tPr reerrr
SYSTEM CABLE (12 a SSS S_.-—CSOCiC
| = :
PINS) es = JK14 F
aU

i ali 5
P1-P12
Le = P1- P2 rerre

seenenece SRSEE SEP SFP eee ce eeeeser SPSPPSESE Seeteesen

CONTACT HR
e | ner
== ore> .| sen EE WIRELESS HR
P1-P12
P1-P4

42 Service Manual

Brerrzsice feererere

SSPPESEES Sfrrrerrr


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Pin definition

JK13

P1 |ControllerS“W |P5 _— |Speed up output PQ |Speed sensor input
P2 |UP P6 |/Speed down output P10 |+VCC

P3  |DOWN P7 |GND P11 |VRIN

P4 |Vin P8 |GND P12 |GND

JK14

P1 Safety switch signal input p2 |VDD

JK9

P1 |FAN OUT |P3  |GND

P2 |FANOUT |P4  |GND

JK11

Pi |GND P2 |VCC

P3  |HEART /|P4

JK3 :

P1 |KEY_DO |P2 |KEY_D1 |P3 |KEY_D2 |P4 |KEY_D3

P5 |KEY_D4 |P6 |KEY_D5 |P7 |KEY_D6 |P8 | KEY_D7

P9 |SCAN_0 |P10 |SCAN.1 |P11 |SCAN 2 | P12] SCAN 3

43 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test Configuration. Driver board control function relate parts location
|

atoll
eee ee eee
oN i —- .
2

7]
40 ,s oa!

< . a
eS ee ee Mad i ee | of DC MOTOR ]
oT

POWER ed : tae
_) ares :

A r
a

- eo“,
a: ie: | =

oa TE 5 12-090908004

pone 0a AA

4 £02973500037
mere’ \ <> 350L

o*.

CONNECTION
TO CONSOLE

44

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Pin definition
JKL (CONNECTION TO CONSOLE)

P1 |ControllerS/W|P5 [Speed up output [pg [Peet — sensor

input
P2 |upP pe [speed downl5i9 |+vcc
output
P3 [DOWN P7 |GND P11 |vRIN
Pa Vin Pg |GND P12 |GND
JK4 (INCLINE VR)
P1 |+VCC P2 |VRIN P3 |GND

JK2 (INCLINE POWER)

BLACK WIRE |DOWN WHITE WIRE |COM RED WIRE |UP

DC MOTOR(MOTOR POWER)

WHITE WIRE |M- |RED WIRE |M+

45

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Error Message : INCLINE ERR

Definition : During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Configuration :

DISPLAY BOARD (S08 BE uemoanccvs

INCLINE 7 INCLINE
VR & UP/DOWN
VOLTAGE = SIGNAL

INCLINE
MOTOR

DRIVER BOARD ex VR VOLTAGE INCLINE VR SET

C) INCLINE DOWN LED
OC) INCLINE UP LED

47

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 41 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of INCLINE show Err

m Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
Explanation

@ Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which changes the VR value.

@ The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it should be. INCLINE E2
appears on the display.

Action Flow Chart

C DISPLAY Ch RI )

we
]

GROVER Beso

nM

IM ewe ayo ea,
oa LE Ln be LM
SOT A ECR EAS ES

Talo E Mico Tore

LIP LEE LesHTS,
INCLINE RISES?

DOWN LED LiGHrTs.,
TALIM Ee Low ERS

oa
| ¥

= ape = SHA LDSeCCLIM Ee eo
Cc Moo ERP MESS “cre -) C MESS AacE +)

48
Service Manual
