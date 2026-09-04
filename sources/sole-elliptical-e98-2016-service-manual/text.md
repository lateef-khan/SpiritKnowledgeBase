    SE865-YE023
    Service Manual




1                    Service Manual
----------------------------------------Table of Contents-----------------------------------------

      1. SE865 Elliptical Outlines
      2. Electronic Parts
      2.1 Upper Controllers
      2.2 Lower Controller and Driver
      3. Electrical Configurations
      4. Elliptical Operation
      5. Elliptical Unit Block Diagrams
      6. Elliptical Basic Connections and Wiring
      6.1 Display Board Wire Connections
      6.2 Display Board PCB Component Locations
      6.3 The Console Interface Board Wire Connections
      6.4 Amplifier Board Wire Connections
      6.5 Driver Board Wire Connections
      6.6 Driver Board PCB Component Locations
      6.7 Driver Board LED Indicator Locations
      6.8 Controller Indicator LED Debugging
      6.9 Driver Board Function
      6.10 Tension Motor Connector Definition Function
      7. Product Safety Instructions
      7.1 Important Safety Instructions
      7.2 Important Electrical Instructions
      7.3 Important Grounding Instructions
      8. Elliptical Error Messages and Troubleshooting for electronic Issues
      8.1 Error Message: E1
      8.2 Error Message: E3
      8.3 Circuit Diagram
      8.4 Calibration Procedure
      8.5 Fuse Replacement
      8.6 Troubleshooting Procedure Matrix
      9. Troubleshooting
      9.1 Console Problem
      9.2 Side Case & Round Disk Problem
      9.3 Flywheel Problem
                                                         2                                 Service Manual
9.4 Poly-V Belt Problem
9.5 Swing Arm Problem
9.6 Connecting Arm & Pedal Arm Problem
9.7 Controller & Incline Motor Problem
9.8 Tension Motor Problem
10. Q & A
10.1 Noise
10.2 Slip Problem
10.3 Play
10.4 Smooth Problem
11. Disassembling and Assembling of Parts
11.1 Console Replacement
11.2 Swing Arm Replacement
11.3 Connecting Arm Replacement
11.4 Pedal Arm Replacement
11.5 Console Mast Replacement
11.6 Side Case Replacement
11.7 Cross Bar Replacement
11.8 Idler Wheel Replacement
11.9 Flywheel & Poly-V Belt Replacement
11.10 Rear Frame Replacement
11.11 Rail & Incline Motor Replacement




                                            3   Service Manual
1. SE865-YE023 Outlines




           4              Service Manual
Plastic parts

                                        Handle Bar Cover (L)

                                                                      Console Assembly
                                         Console Mast Cover
                                                                      Console Bottom Cover

                                                Side Case (L)         Handle Bar Cover(R)


                                                                      Round Disk Cover

                                                                      Connecting Arm
                                                                      Cover A (L,R)
                                                 Side Case (R)

                                                                      Front Stabilizer
                                                      Pedal (L)
                                                                      Cover


                         Incline Bottom Cover
                                                                      Connecting Arm Cover
                                                                      B (L,R)
                Inclinable Rail Cover
                                                                      Pedal Arm Cover (R)

                                                                      Round Disk

                                                                      Middle Stabilizer
                                                                      Cover




                                                                  5                       Service Manual
    Handle Switch
    Bracket
                        Console Assembly




Cable Assembly




                    6                 Service Manual
Steel parts
                                            Swing Arm (L)


                                                                                       Swing Arm (R)

                                                                                       Console Mast


                                            Induction Brake
                                                                                       Drive Pulley

                                         Connecting Arm (L)
                                                                                       Cross Bar

                                         Connecting Arm (R)

                                                                                         Bushing Housing,
                                                                                         Pedal Arm
                                              Pedal Arm (R)


                                   Pedal Arm (L)


                                    Incline Motor
                                                                                         Main Frame

              Rear Rail Assembly




                                                                  Rail Base Assembly


                                                              7                                             Service Manual
Incline Motor

                    Console Display Board




                8                    Service Manual
2. Electronic Parts




         9            Service Manual
2-1 Upper Controllers                Speaker

                                               Cooling FAN
                 THUMB SWITCH




                DISPLAY




                                10                           Service Manual
2-2 Lower Controller and Driver




         EMS BRAKE
                                           SPEED SENSOR




                                       EMS CONTROLLER
        INCLINE MOTOR
                                  11               Service Manual
3.Electrical Configurations




             12               Service Manual
CONSOLE:
 Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console、incline driver and tension motor driver, link the console to output appropriate voltages
 for tension motor that control the elliptical functions.

EMS BRAKE:
 It can change to increase or decrease resistance level of brake.

INCLINE MOTOR:
 This is an ac motor. User can to control variable elevation by console within main controller.

GENERAL INFORMATION

CONSOLE
Contains Key controls and TFT Display.
Main controller Include power supply 、 EMS driver control circuit and incline control circuit.




                                                                        13                                                           Service Manual
EMS BRAKE
   Work voltage:DC 0 ~23V
   Control resistance increases and decreases.

INCLINE MOTOR
This is a 115 volt AC motor.

Have four wires, red, black, white and green.

Has one 3 pins cable of position sensor.

If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.

If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.

The White wire (COM) is neutral.
The green wire is ground.




                                                                         14                    Service Manual
4. SE865-YE023 Product Operation




               15              Service Manual
Display Windows

                       10.1” TFT Display




                  16                 Service Manual
Operation
Window Display Mode
  IDLE MODE
  1.1 Display each program name.


  DISPLAY MODE
  2.1 Pre-set: DISPLAY ON (DISABLE). You could set the DISPLAY ON/OFF by ENGINEERING MODE.
  2.2 The console will not get into SLEEP MODE when the set up is “ON”, unless turn off the power. There is no RPM input in IDEL MODE, and enter
      to SLEEP MODE after thirty minutes without pressing any key.
  2.3 Use quick key to set sleep mode.In IDLE MODE press and hold ENTER+STOP+DISPLAY keys 2 seconds.use UP/DOWN key change sleep
      mode OFF or ON.Press ENTER key confirn then back to IDLE MODE.
  2.4 In DISPLAY MODE,LCD screen will has no display, and backlit will be off. Press any key to wake up the system, and back into IDEL MODE.
  2.5 Resistance in SLEEP MODE: Incline =1，Fan off.


  CHILD LOCK MODE
  3.1 Pre-set: CHILD LOCK OFF (DISABLE). You could set the CHILD LOCK ON/OFF by ENGINEERING MODE.
  3.2 The message window will display “CONSOLE LOCKED” after twice will show” CHILD LOCK-ON PRESS START AND ENTER TO ENABLE
      OPERATION”, when CHILD LOCK setup is ON.You could setup the CHILD LOCK MODE OFF by pressing “START” and ”ENTER” key for
      more then two seconds. After that it will enter to IDEL MODE.
  3.3 All keys will be no action when CHILD LOCK MODE is active.


  EXERCISE MODE（QUICK START）
  4.1 In IDEL MODE, press START key enter to MANUAL MODE.The age, weight is presetting value. Time counting is count up from 00:00. All
      countable data will count up from “0”, and resistance is count up from “1”.
  4.2 You could chose the program by pressing the key: MANUAL、PROGRAM、USER1、USER2 、HRC1、HRC2. And then, press “START” key to
      start the workout. All parameter will be the preset value.




                                                                      17                                                        Service Manual
PAUSE MODE
5.1 Press “STOP” key enter to PAUSE MODE, and exercise parameters will be recorded. Window will display “PAUSE”.
5.2 In PAUSE MODE, will show” PAUSE”


5.3 It will enter to IDLE MODE after waiting by five minutes without pressing any key in PAUSE MODE.
5.4 The ramp incline level should back to “1” when the resistance level is “1”. The position of tension motor and ramp incline should back to the preset
    level before it pause when press “START” key.




END MODE
6.1 The message window will display “WORKOUT SUMMARY” after end workout.
6.2 END MODE workout information
    6.2.1 Displays the all finished message in the WM
6.3 When the time counting is end, and END MODE display is finished without pressing any key in 3 minutes.The system will enter IDLE MODE.


RESET MODE
7.1 In IDLE MODE, press STOP key for more than three seconds will enter to RESET MODE and reset the system.( If the system is in
  CONSOLE LOCK MODE you have to quit CONSOLE LOCK MODE first, and you can execute the RESET MODE.)
7.2 The window will finished the reset. After that, the system is in IDLE MODE.




                                                                         18                                                            Service Manual
Function

   SPEED
        Display the current speed in mile per hour.
        DISPLAY range is 0.0 to 99.9
        WORK range is 0.0~99.9
   Incline
        Display the incline position from 1 to 20.
        DISPLAY range is 0 to 99.
        WORK range is 1 to 20.
        INCLINE preset value is 1 to 20.
        Press “UP” or ”DOWN” to adjust incline, each increment and decrement is 1.
   LEVEL
        Display the incline position from 1 to 20.
        DISPLAY range is 0 to 99.
        WORK range is 1 to 20.
        LEVEL preset value is 1 to 20.
        Press “UP” or ”DOWN” to adjust incline, each increment and decrement is 1.

   TIME
      TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time then timer is COUNT DOWN.
      DISPLAY range is 0:00 to 99:99.
      WORK range is 0:00 to 99:59.
      COUNT DOWN setup range is 10:00 to 99:00.
      When TIME is set, the count will go to zero.
      In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will continue count up time.
   LAPS
      Display the total working laps quantity.
      DISPLAY range is 0 to 99.
      WORK range is 0 to 99.
      Displays total laps quantity.



                                                                        19                                                        Service Manual
DISTANCE
    Display the current distance in Mile.
    DISPLAY range is 00.0 to 99.9.
    WORK range is 00.0 to 99.9.
CALORIES
    Displays the cumulative calories burned at any given time during your workout.
    DISPLAY range is 00.0 to 999.
    WORK range is 00.0 to 999.
PULSE
    Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
    DISPLAY range is 0 to 999.
    WORK range is 40 to 220 BPM.
    In RUN Mode, if the Elliptical doesn’t have a signal for 8 seconds then display value will become “0 ”.




                                                                      20                                          Service Manual
Function Button Locations




       PROGRAM BUTTONS
    (Manual, Hill, Fat Burn, Strength,

          Interval, 2 User, 2HR)
                                                     Fan Key
                                              Cooling fan switch on or
                                                         off

               DISPLAY




          CONTROL KEYS




                                         21                              Service Manual
                                               Function Button In Main Mode
READY MODE
  STOP button: Non-function.
  START button: Pressing “ START ” button to start Elliptical, When pressing “START” button, there will be 3 second final count down on window
  display, then machine starts running. In MANUAL, Elliptical starts at MIN LEVEL .
  LEVEL UP button: If user doesn’t enter a setting then this button is non-functional.
  LEVEL DOWN button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE UP button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE DOWN button: If user doesn’t enter a setting then this button is non- functional.
  FAN button: It can to control ON/OFF for the fan.
  DISPLAY KEY：If user doesn’t enter a setting then this button is non- functional.
  ENTER KEY：
  Press ENTER key enter to parameter setting, and confirm the every setting by pressing START key no pressing ENTER key..
  Pressing ENTER key confirm the every setting or modify parameter use.
  In workout mode,pressing ENTER key can modify DM display. The preset is LEVEL PROFILE, pressing ENTER key change
  display :LEVEL PROFILE →INCLINE PROFILE→SCAN(SCAN MODE every 3 seconds will change display :LEVEL PROFILE →INCLINE
  PROFILE→LEVEL PROFILE)




                                                                   22                                                          Service Manual
RUN MODE
  STOP button: press “STOP” button to stop Elliptical.
  START button: LEVEL & INCLINE PROFILE
  ENTER button: non-functional.
  LEVEL UP button: Press the button to increase your level and each increase is 1.
  LEVEL DOWN button: Press the button to decrease your level and each decrease is 1.
  INCLINE UP button: Press the button to raise position and each increase is 1, the maximum incline position is 20.
  INCLINE DOWN button: Press the button to lower position and each decrease is 1, the minimum incline position is 1.
  Fan button: It can to control ON/OFF for the fan.
  DISPLAY KEY： Press DISPLAY key to display the exercise data 5 seconds when you are workout.




                                                                  23                                                   Service Manual
5. SE865-YE023 Unit Block Diagrams




                24              Service Manual
Elliptical Configuration




                           25   Service Manual
6. SE865-YE023 Basic Connections and Wiring




                     26                Service Manual
6-1 Display Board wire Connections




                                     27   Service Manual
6-2   Display Board PCB Component Locations

  PCB Board Top




                                              28   Service Manual
PCB Board Bottom




                   29   Service Manual
6-3 The console Interface Board wire Connections




                                             30    Service Manual
6-4 Amplifier Board wire Connections




                                       31   Service Manual
6-5   Driver Board Wire Connections




                                      32   Service Manual
6-6 Driver Board PCB Component Locations




                                           33   Service Manual
6-7 Driver Board LED Indicator Locations




                                                INCLINE
                                                MOTOR UP




                                                 INCLINE
                                                 MOTOR DOWN



                                           34                 Service Manual
6-8 Controller Indicator LED debugging

 Indicator           Function                     Condition                              Reason                        Solve
   LED
LED1       Motion of incline motor   Motion of incline motor is down.        Transistor was broken.   Replace controller.
                                                                             Relay failed.
LED2       Motion of incline motor   Motion of incline motor is up.          Transistor was broken.   Replace controller.
                                                                             Relay failed




                                                                        35                                                     Service Manual
6-9 Driver Board function




AC POWER
INPUT



AC POWER
INPUT



INCLINE
MOTOR COM



INCLINE
MOTOR UP


                                                    SPEED
                                                    SENSOR
INCLINE                     INCLINE
MOTOR DOWN                  VR

                                           SYSTEM
                                           WIRE


                                      36            Service Manual
7.   Product Safety Instructions




                37                 Service Manual
7-1 Important Safety Instructions
  - To reduce the risk of electric shock disconnect your Elliptical from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the Elliptical on a flat level surface with access to a 115-volt, 15-amp
    grounded outlet with only the Elliptical plugged into the circuit.
  - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
    improper adapters or in any way modify the cord outlet.

7-2 Important Electrical Instructions
  - Never use a ground fault circuit interrupt (GFCI) wall outlet with this Elliptical. As with any appliance with a large motor, the GFCI will trip often. Route
    the power cord away from any moving part of the Elliptical including the elevation mechanism and transport wheels..
  - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a Elliptical is first turned on or even
    during use. If your Elliptical is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the Elliptical itself
    does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
    have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online at
    www.squared.com part # QO120HM.

7-3 Important Grounding Instructions
  - This product must be grounded. If the Elliptical should malfunction or breakdown, grounding provides a path of least resistance for electric current,
    reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
    appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
  serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
  outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 115-volt circuit, and has a grounding plug that looks
  like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
  as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
  can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must be connected to a permanent
  ground such as a properly grounded outlet box cover.
  Whenever the adapter is used, it must be held in place
  by a metal screw.




                                                                                 38                                                                 Service Manual
8. SE865-YE023 Error Messages /
        Troubleshooting




               39                 Service Manual
   Error code items：


                    Error Message             Explain
                    E1                        EEPROM failure
                    E2                        Tension motor is failure
                                              The console board is not detecting the VR voltage value,or the
                    E3
                                              voltage value has exceeded the range.

   Prepare：


                                    Picture                              Tool name




                                                                         Multi-meter




                                                        40                                                     Service Manual
   8-1 Error Message：E1
 Definition: All screens are off, and outputs are stop when EEPROM damaged or malfunction.Display message will
  show “E1”.
 Troubleshooting: Replace upper controller.




                                                       41                                             Service Manual
 Test configuration. The console to driver board connector pin define function




                                 1
The console to driver board      2
connector pin define             3
function:                        4
1.+12V                           5
2.GND                            6
3.VCC+5V                         7
4.PWM                            8
5.AD                             9
6.SPD                            10
7.P/C                            11
8. INC+
9. INC -
10. INC VR
11. NA




                                                  42                              Service Manual
                Test Configuration. Incline motor control function relate parts location




                                                                                                      1.+12V
                                                                                                      2.GND
White-NEUTRAL                                          The position sensor wires                      3.VCC+5V
                                                       1.Red = Ground,                                4.PWM
   RED-UP                                              2.White = Position signal,                     5.AD
                                                       3.Black = 5vdc,                                6.SPD
                                  INCLINE
BLACK-DOWN                        MOTOR                (0~5v depending on incline position)           7.P/C
                                                                                                      8. INC+
                                   UP LED
                                                                                                      9. INC -
                                                                                                      10. INC VR
                                  INCLINE                                                             11. NA
                                  MOTOR                     1,2,3           11,10,9,8,7,6,5,4,3,2,1
                                 DOWN LED


                                                  43                                                        Service Manual
Test Procedure：
    1.   Run calibration again.
    2.   Does the incline motor move at all?
    3.   If no, do the Up/down lights on the incline board light?
    4.   If they light, do the relays click on?
          If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down
                (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the mains voltage
                ~ 115VAC. If the voltage is present but the motor doesn’t move, then the motor is bad.
          If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).
    5.   If the motor moves, is there a sensor reading on console?
          The INCLINE window will display the computer incline setting (after speed cal. ends); 20 for max incline, 0 for lowest incline. The Incline window is a counter that is
                showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the position sensor
                wiring or circuitry.
          If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
                Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
                If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
          If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and there should be a voltage
                between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical,
                as long as it’s somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves,
                but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
    6.   Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
    7.   If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board.
         There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.
         The only problems that are possible are a bad solder joint or broken circuit on the board.
          Console connector wiring, these connections are the same on the incline board and at the console.
                              Pin 3 = 5vdc
                              Pin 2 = position signal 0~5vdc
                              Pin 1 = ground
    8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there,
         but is there at the incline board then check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
    9.   If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.




                                                                                       44                                                                         Service Manual
Error Message：E3
 Definition：During incline action,the display board CPU cannot read the VR value,so E3 appears.
 Configuration：




                                                                      45                          Service Manual
Cause of E3
      Press the incline UP/DOWN key.The incline doesn’t operate. E3 appears on the display.
          Explanation
             Press the incline UP and DOWN key.The driver board UP or DOWN indicator lights.The incline operates,moving the VR,which
                changes the VR value.
             The display board CPU reads the incline VR value.If there is no VR value change,to the CPU,the incline is not operating when it
                should be. E3 appears on the display.
          Action Flow Chart




                                                                        46                                                        Service Manual
Troubleshooting
            Part            Troubleshooting
                            1.Press incline UP key.The driver board UP LED lights.
            Display board   2.Press incline DOWN key.The driver board DOWN LED lights.
                            3.If not as above,inspect the cable and connections.
                            1.Inspect whether the 11-PIN cable is connected well.
            11-pin cable
                            2.Test by replacing the cable with a good one.
                            Inspect whether the driver board UP/DOWN LED is lit.
                            1.Press incline UP or DOWN key again,making the incline motor return to its
            Driver board
                            position.
                            2.If E3 still appears,re-calibrate the incline set.
                            1.Inspect whether the incline motor is stuck.
                            2.Inspect whether the incline gears are cracked.
            Incline motor
                            3.Test whether the incline motor has a broken circuit.
                            4.Re-calibrate the incline set.




                                                      47                                                  Service Manual
8-3 ELLIPICAL CIRCUIT DIAGRAM




             48                 Service Manual
8-4 CALIBRATION PROCEDURE

   Incline Calibration:
   If there is a problem with the incline, try running the calibration. Press the Incline ▲ key and the Start
   key at the same time. Hold them down for 5 seconds and the Incline calibration will start and run
   automatically. If the problem persists contact service department.


MAINTENANCE MENU IN CONSOLE SOFTWARE

   The console has built in maintenance/diagnostic software. The software will allow you to change the
   console settings from English to Metric and turn off the beeping of the speaker when a key is pressed for
   example. To enter the Maintenance Menu (may be called Engineering Mode,depending on version) press
   and hold down the Start, Stop and Enter keys keep holding the keys down for about 5 seconds and until
   the display shows display “Engineering Mode”. Press the Enter button to access the menu below. Press
   the Level▲/▼keys to navigate the menu.

     A. KEY TEST - Will allow you to test all the keys to make sure they are functioning.
     B. UNIT MODE - Choose from English or Metric display readings.
     C. BRAKE TEST – Testing of the EMS brake.
     D. DISPLAY MODE - Turn off to have the console power down automatically after 30 minutes of inactivity.
     E. PAUSE MODE - Turned on to allow 5 minutes of pause, turn off to have console.
     F. KEY TONE - Turn on or off the beep sound when a key is pressed.
     G. CHILD LOCK - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the
     child lock is enabled, the console will not allow the keypad to operate unless you press and hold the Start and
     Enter buttons for 3 seconds to unlock the console.




                                                          49                                      Service Manual
  8-5 Fuse replacement




          FUSE 5A




If your elliptical loses power or will not start, check the fuse located on the motor controller.
DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric shock
Remove FUSE holder.
Remove and replace the fuse on the holder

                                                                           50                         Service Manual
  8-6 Troubleshooting procedure matrix

                    Condition                                        Reason                                            Solve
LCDs not bright, incomplete or imperfect.          1. LCD light is broken.                   1. Replace with new LCD or console.
                                                   2. Power to console too low.              2. Check AC power is 110-120V.
                                                                                             3. Check power to console.
                                                                                             4.Replace lower controller.
LCD displays not bright, incomplete or imperfect. 1. LCD displays are broken.                1. Replace with new console.
The incline position doesn’t match console        1 Console is not calibrated.               1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “E3”. 1 Position sensor value of incline motor is 1 Turn off the AC switch and turn on power again.
                                                                                             2. Calibrate the monitor.
                                                  wrong.
Erratic pulse display.                            1. Another chest belt in use around        1. Check for other chest belt use around elliptical.
                                                     Elliptical.                             2. Change the position or direction of elliptical.
                                                  2. Other magnetic field disturbance.       3. Replace with new receiver.
                                                  3. Receiver is broken.
UP/DOWN button of                                 1 The connector of INCLINE CABLE           1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used.            and   CONSOLE    not connected properly.
                                                  2. The connector of INCLINE CABLE          2. Connect the wires again.
                                                  and INCLINE ADJUSTMENT SWITCH
Incline button just can press UP, can’t press     W/CABLE not connected properly.
DOWN.
Incline button just can press DOWN, can’t press                                              3. Replace the cable.
UP.                                               3 The   connector of INCLINE  CABLE  or
                                                  INCLINE ADJUSTMENT SWITCH
                                                  CABLE
                                                                                             4. Replace buttons.
                                                  got damage.
                                                  4. Button of INCLINE ADJUSTMENT
                                                                                             5. Replace the cable.
                                                  SWITCH is broken.
                                                  5. The connector of INCLINE CABLE or
                                                  INCLINE ADJUSTMENT SWITCH                  6. Replace the cable.
                                                  CABLE
                                                  got damage.
                                                  6. The connector of INCLINE CABLE or
                                                  INCLINE ADJUSTMENT SWITCH
                                                  CABLE
                                                  damaged.
Hand pulse lost its function.                     1. Hands not on the hand pulse sensors 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                      or only one hand on sensor.
                                                                            51                                                           Service Manual
                                          2. The connector of HANDPULSE            2. Connect the cable again.
                                             W/WIRE and Console not connected
                                             properly.                             3. Replace with new cable.
                                          3. The wires got damaged when
                                             connecting the HANDPULSE W/WIRE 4. Replace console or Hand pulse board.
                                             and Console.
                                          4. Hand pulse board is broken.
Wireless lost its function.               1. Chest belt not worn properly.         1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                       oriented correctly.
                                          2. Distance is too far and exceeds range 2. User chest belt in front of console within 3 feet.
                                          of receiver.                             3. Replace with new lithium battery type is CR2032.

                                          3. Chest belt battery is weak or dead.
Chest belt too close to the Elliptical.   Weak battery.                            Replace with new lithium battery with type CR2032.




                                                                  52                                                          Service Manual
9. Troubleshooting




        53           Service Manual
9-1    Console Problem
      1. Display: If there is no display, follow the following procedures for diagnosis.




      2. If the display does not come on, make sure that AC power switch is turned on.




      3. If necessary, replace the fuse of the AC    power switch module.




                                                                54                         Service Manual
4. Remove console cover, left and right chain covers, check if all the wires are inserted in the correct positions and
   check if whether the wires broken.




                                                        55                                                  Service Manual
9-2    Side case & Round Disk Problem
      1. Rubbing noises are the most case which occurs at this portion. It is caused either by the round disk off center or the
         swing of the round disk.




      2. If the round disk is off center, take it apart and resume according to the procedures for replacing chain covers.
      3. If the round disk swings with too much displacement, take apart chain covers and the round disk, and use Phillips head
         screw driver to release 5x16mm tapping screws and 1/4"x19mm flat washers. Put the round disk with cross bar on the
         platform and check any deforms. Deform can be corrected with force. The displacement due to the swing of the round
         disk is within 3 mm prior to shipping.




                                                              56                                                   Service Manual
9-3    Flywheel Problem
      1. The problem with Inductive Flywheel is rare. If there is no resistance, take off both Chain Covers and check for
         disconnection or breakage for electric cables.




      2. If there is noise with the flywheel, check if there is foreign material or abnormal rubbing. Replace with new flywheel if
         the noise can not be fixed.




                                                               57                                                    Service Manual
9-4    Poly-V Belt Problem
      1. If the Poly-V Belt falls off, first remove the right chain cover and Idler Wheel Plate, and then reinstall the Poly-V Belt.
         Once reinstalled, rotate at low speed to observe if the Drive Pulley or Poly-V Belt is offset or deformed. Check if the
         belt pulley is offset or if the belt, Drive Pulley, Magnetic flywheel are not aligned in a straight line. Lastly, rotate at high
         speed (100-120RPM) and test with abrupt stops to check for abnormalities. If everything is ok.




      2. If the three parts are not aligned in a straight line, adjust the magnetic flywheel to the proper place.      Adjustments are
         always made to product ensuring alignment before shipment from factory.




      3. If the Poly-V Belt is slipping, simply adjust the cap the on hook-type screw with the #13 wrench to adjust. Refer to the
         disassembly procedures for adjustment.


                                                                  58                                                      Service Manual
59   Service Manual
9-5    Swing Arm Problem
  1. There are 0.05mm~0.07 mm tolerances with the parts for the concern of easy assembly by the user and it is normal with
     slight play. Noises might be caused due to these tolerances after certain time of usage. It is recommended to add crease
     or thick lubricant on Ø25x296L console mast shaft for the handle bar. If noises come from 6005 bearing, replace the
     bearing.
  2. If handlebar button does not function, then tear off the sticker and use Phillips head screw driver to release M5x20mm
     Flat Head Socket Screw which secures the handlebar button, as shown in figure 1 and 2. Check and make sure that
     handlebar button is connected with lower cable properly, as shown in figure 3




  3. Check and make sure that upper and lower handle     wires are connected properly and free from damage.




                                                            60                                                 Service Manual
9-6   Connecting Arm & Pedal Arm Problem
      1. Since elliptical machine are full of moving parts with joints, parts are related to each other and proper lubrication is
         important. Lubricating with crease as shown in figures 1 & 2 while maintaining or replacing parts can eliminate
         potential problems.




      2. There are many causes for un-smoothness. Slide wheels moving parallel and freely on the rail is the key factor which
         is affected by the pedal arm parallel to the rail and perpendicular to the bearing housing.
      3. Swing Arms must connect freely to connecting arms, the true circle of slide wheels without slippage and rod end
         (fish-eye) bearing is without damage and tight enough to eliminate noises. If necessary, use 19mm wrench to replace
         rod end bearing.




                                                               61                                                   Service Manual
4. If the incline motor does not function, first check the proper connection of the cables then the damage of the incline
   controller, the transformer and the console. Replace the part which is damaged, as shown in figures 1, 2, 3 & 4.




                                                         62                                                  Service Manual
9-7   Controller & Incline Motor Problem
      1. If the incline motor does not function, first check the proper connection of the cables then the damage of the incline
         controller, the transformer and the console. Replace the part which is damaged.




                                                               63                                                  Service Manual
2. Make sure the incline motor is reset to zero when you install a new one. Rotate the incline barrel clockwise to the end
   and then rotate the same barrel counterclockwise in one and a half circle. Make sure the distance of two hole sites is
   207±1mm (see picture 5 & 6).




                                                        64                                                 Service Manual
10. Q & A




   65       Service Manual
10-1 Noise
     1. Noises are general problem for elliptical and difficult to troubleshoot, from rubbing between chain covers and round
        disk, bushing housing and the cross bar, the belt and the drive pulley, idler wheel, handle bar and console mast shaft,
        flywheel and the steel cable concerning the front portion of the elliptical to the rear portion such as slide wheels and
        clank axle with wave washers, pedal arms and pedals, as shown in figures 1 and 2. Major causes for noises are
        insufficient lubricant, un-smoothness and loose screws. Since those are moving parts and interactively, problem
        solving must be treated case by case.




                                                             66                                                  Service Manual
10-2    Slip Problem
       1. There are four situations which cause slippage.
       2. M12 x P1.75 rod end (fish-eye) bearing: M12 nut on top must be tighten enough to the connecting arm and
          perpendicular to M12 x P1.75 rod end bearing.




       3. Bushing housing: 3/8" x2-1/4" Socket Head Cap Screw and 3/8" x11T nut on top must be tight enough, as shown in
          figure 2, with 500~600 lbs of force suggested.




                                                            67                                                Service Manual
4. Cross Bar: M8x40m/m Socket Head Cap Screw on the cross bar must be tight enough, as shown in figure 3, with
   550~600 lbs of force suggested.




5. Belt: This issue appears quite often, because after a period of time, most belts will become loose from use depending
   on usage time. Solution will depend on weight and adjustment methods, refer to belt disassembly procedures for
   references.




                                                       68                                                 Service Manual
10-3 Play
     1.   Shaking is mainly due to loose screws, so check and tighten loose screws first. Check connection points to see if gaps
          have been created after prolong use causing wear and tear or improper assembly. For example, shaking of the foot
          pedal is caused by loose Carriage Bolts, from improper assembly.




10-4 Smooth Problem
     1. Check for loose screws if machine motion feels unsmooth. Check if there are foreign object on or around the sliding
        rail, use an alcohol wipe to remove and re-lubricate with lubricant.




                                                              69                                                 Service Manual
11.Disassembling and assembling
              of Parts




               70            Service Manual
11-1. Console Replacement
     1. Use Phillips head screw driver to release three M5x15mm Phillips head screws and two 3.5x12 m/m Sheet Metal
        Screws to take apart front and rear Mast Covers.




     2. Use Phillips head screw driver to release four M5x10mm Phillips head screws and disconnect Computer cable, Handle
        Resistance Wire, Handle Incline wire and Handpulse Cable to take Console apart.




     3. Reassemble in the reverse order as disassembly (Be sure to not crush or damage wiring during process)
     4. Release 3.5x12 Sheet Metal Screws if opening top and bottom console covers is necessary. (To be opened by
        professionals only)




                                                          71                                               Service Manual
11-2. Swing Arm Replacement
     1. Use a Phillips screwdriver to remove Sheet Metal Screws 3.5x12mm securing the swing arm covers (Front and Back)




     2. Disconnect the wiring connecting the upper and lower swing arms.




     3. Use Phillipshead screw driver to release M5x15mm Phillips Head Screws and 3.5x12 Sheet Metal Screws which
        secure left and right Connecting Arm Covers A.




                                                          72                                              Service Manual
4. Release M5x15mm Phillips Head Screws and 3.5x12 Sheet Metal Screws which secure left and right Connecting Arm
   Covers B.




                                                   73                                             Service Manual
5. Use 14mm wrench to release 3/8"x3/4" Hex Head Bolt together with 3/8"x30x1.5T Flat Washer which secure Swing
   Arms.




6. Use #12 and #13 open end wrench affix swing arm assembly and remove Hex Head Bolt 5/16”x1-1/4”, flat washer
   5/16”x20x1.5T and nyloc nut 5/16”x7T. Remove swing arm assembly.




7. Reassemble in the reverse order as disassembly




                                                    74                                              Service Manual
11-3. Connecting Arm Replacement
     1. Remove swing arm assembly and swing arm (Refer to step 11.2) (If removal of pedal tube, simply remove swing arm
        with Rod End Bearing attached)
     2. Use 12mm open end wrench to remove hex socket screw 5/16”x15mm and flat washer 5/16”x20. Pull out the pedal
        carriage bolts to remove the Pedal Bar Assembly.




     3. Use Phillips screwdriver to remove Phillips Head Screw M5x10mm securing the pedal and remove pedal.




                                                          75                                              Service Manual
4. To resume, tighten the Pedal back on the Connecting Arm, return it onto the Pedal Arm and secure with carriage bolt in
   the square hole, as shown in figure 6. Tighten carriage bolt with 5/16" x 15m/m hex head bolt and 5/16" x 23 x 1.5T flat
   washer.




5. Reassemble in the reverse order as disassembly.




                                                        76                                                  Service Manual
11-4. Pedal Arm Replacement
     1. First remove the Pedal Bar Assembly (Refer to step 11.3), then use Phillips head screwdriver to remove the Phillips
        Head Screws M5x10mm securing the cover to pedal arm joint and remove pedal arm joint cover.




     2. Use M8 hex wrench and #14wrench to remove Gap socket screw 3/8”x2-1/4”, two flat washer 3/8”x19x1.5T and nyloc
        nut 3/8”x11T connecting the Inclinable Rail Assembly and rotating block, to remove Inclinable Rail Assembly.




     3. Use #12 hex wrench to remove hex head bolt 5/16”x15mm and flat washer 5/16”x35x1.5T, to remove Bushing Housing,
        Pedal Arm.




                                                            77                                                 Service Manual
4. Use circlip pliers to remove circlip Ø17 and remove sliding wheels.




5. Reverse above procedures to resume Pedal Arm.




                                                       78                Service Manual
11-5. Console Mast Replacement
     1. Follow the procedure to disassemble Swing Arm.
     2. Separate Console Mast cover by gently pulling back with your hands, separate left and right cover.
     3. Use 14mm wrench to remove hex head bolts 3/8”x3/4”, Curved Washers 3/8 "x23 x2T, external hex head bolts 3/8"
        x2-1/4 "and Spring Washer 3/8" x2T that secures the Console Mast.




     4. Use Phillips head screw driver to release two Ø3x20 Tapping Screws which secure Hand Pulse Assembly and pull out,
        disconnect cables.




                                                          79                                               Service Manual
5. Unplug the Round Cap under handpulse tube and pull out handpulse cables to take Handpulse Sensor Assembly
   apart.




6. Remove Console Mast and Console Mast cover together, pull out control wires and incline wires and separate covers
   from Console Mast.




7. Reassemble in the reverse order as disassembly.




                                                     80                                               Service Manual
11-6. Side Case Replacement
     1. Follow procedures to Swing Arms and Pedal Arms.
     2. Use Phillips head screw driver to release M5x15mm Phillips Head Screws to take apart Front Stabilizer Cover.




     3. Use Phillips head screw driver to release 4x19 Sheet Metal Screws, and 5x 16 Tapping Screws which secure left Side
        Case and take it apart.




                                                           81                                                Service Manual
4. Again, use Phillips head screw driver to release 4x15 Sheet Metal Screws, 1/4"x19 Flat Washers and 5x16 Tapping
   Screws, as shown in figure, which secure right Side Case on the Mainframe.




5. Disconnect Ground Wire and Controller Connecting Wire from AC power Switch and take right Side Case apart.




                                                     82                                               Service Manual
6. Reassemble in the reverse order as disassembly (Flat Washer 5/16 "x23x1.5T is to be placed on the left chain cover)




                                                      83                                                Service Manual
11-7. Cross Bar Replacement
     1. Follow procedures 11-2, 11-3 and 11-4 to take apart Connecting Arm, Pedal Arm and both Side Cases. ake off the
        Round Disk Cover by using a tapering stick.




     2. Remove elliptical side cover Round Disk Cover, use 12mm wrench to remove hex head bolt 5/16”x15mm, flat washer
        5/16”x35x1.5T securing the cross bar. Use #13 wrench and loosen the outer bolt M8x6.3T (steel lvl 10). Use #13
        wrench and hex wrench (M6) to loosen the inner bolt and remove the cross bar.




                                                          84                                               Service Manual
3. Use Phillips head screwdriver to release 8pcs of 5x16 tapping screws with 1/4"x19flat washers to separate the Cross
   Bar from Round Disk Cover, Crank.




4. To resume, secure the Round Disk on the Cross Bar and return it on the Crank Axle, align the Cross Bar with square
   hole and put 7x7x25L Woodruff Key in the hole and tighten M8x40 socket head cap screw together with two M8x6.3T
   nuts until it reaches 500 Kg-cm. Return and tighten 5/16" x 15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer.




5. Follow above procedures to resume Connecting Arm, Pedal Arm, and both left and right Side Cases with Round Disk
   Cover.




                                                      85                                                 Service Manual
11-8. Flywheel & Poly-V Belt Replacement
     1. Follow procedures to take apart Cross Bar.
     2. Use 13 mm wrench to loosen M8 x 9T nut on M8x170mm J-bolt together with 5/16" x 23 x 1.5T flat washer until J-bolt
        is released. Use the same wrench to release M8 x 20 carriage bolt, which secures Idler Wheel Assembly, together
        with 5/16" x 20 x 1.5T flat washer and M8 x 7T nut to take Idler Wheel Assembly apart, as shown in figures 1 and 2.




     3. Follow above procedures to resume and tighten the M8 Nyloc Nut on the J Bolt until the Belt generate sound wave
        170HZ(±10).




                                                           86                                                Service Manual
11-9. Flywheel Replacement
     1. Follow the procedures to take Idler Wheel Assembly apart.
     2. Disconnect all electric cables for Inductive Flywheel and cut the tie for the Cables.




     3. Use 11 mm wrench to release 4pcs of 1/4" x 3/4"hex head bolt with 1/4" spring washers and 1/4"x13x1T flat washers
        and take the Inductive Flywheel apart.




     4. To resume, Return the Inductive Flywheel back on the Main Frame and secure with 4pcs of 1/4" x 3/4" hex head
        screws with 3pcs of 1/4" spring washer and 3pcs of flat washers then connect all electric cables back on.
     5. To resume parts, reverse above procedures and adjust the Belt in the center of the Drive Pulley, as shown in figure 4.




                                                              87                                                Service Manual
88   Service Manual
11-10.   Rear Frame Replacement
     1. Use Phillips head screw driver to release M5x15mm Phillips Head Screws and disconnect incline motor power
        connecting wire and incline motor connecting wire.




     2. Use two 14mm and a 12mm wrenches to release 3/8"x1-1/2" Hex Head Bolts, 3/8"x19x1.5T Flat Washers, 3/8x7T
        Nyloc Nuts, 5/16x2-1/4 Hex Head Bolts, 5/16"x1.5T Split Washers, 5/16" x20x1.5T Flat Washers and Ø5/16 Star
        Washer, which secure Rail Base Assembly and pull it apart.




     3. Follow above procedures to resume parts and make sure wires are properly connected with color codes match.




                                                          89                                              Service Manual
11-11.   Rail & Incline Motor Replacement
     1. Follow the procedures to take Rail Base Assembly apart.
     2. Use Phillips head screw driver to release M5x15mm Phillips head screws which secure Rear Bar Case, Inclinable Rail
        Cover and Incline Cover.




     3. Use two 14mm wrenches to release 3/8"x2-1/2" Hex Head Bolts, 3/8"x19x1.5T Flat Washers and 3/8"x7T Nyloc Nuts
        which secure Rear Rail Assembly and Incline Motor Holder.




                                                          90                                                Service Manual
4. Use two 17mm wrenches to release M10x130m/m" Hex Head Bolts, 3/8"x19x1.5T Flat Washers and M10 x 8T Nyloc
   Nuts which secure Incline Motor and Incline Device.




5. Use Phillips head screw driver to release 5x16 Tapping Screw and the Ground wire and pull it out after cutting the wire
   tie to take apart the Incline Motor, as shown in figures 6 and 7.




                                                        91                                                 Service Manual
6. Use 12mm wrench to release 5/16"x1 Hex Head Bolt and 5/16"x 35x2T flat washer which secure Rail Assembly. Pull
   out Locking Tube Assembly and take apart Rail Assembly.




7. Release M5x15mm Phillips Head Screw which secure aluminum rail to take the rail apart, if necessary.




8. Reverse above steps to resume parts.




                                                      92                                                  Service Manual
