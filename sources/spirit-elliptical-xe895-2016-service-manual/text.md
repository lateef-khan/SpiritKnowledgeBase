<!-- Source: XS895 (XE895-SE022 2016) Service manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XE895-SE022
    Service Manual




1                    Service Manual
-------------------------------------Table of Contents-------------------------------------------

      1. Elliptical Outlines
      2. Electronic Parts
             2.1 Upper Controllers
      2.2 Lower Controller and Driver
      3. Electrical Configurations
      4. Product Operation
      5. Elliptical Unit Block Diagrams
      6. Elliptical Basic Connections and Wiring
      6.1 Display Board Wire Connections
      6.2 Display Board PCB Component Locations
      7. Product Safety Instructions
      7.1 Important Safety Instructions
      7.2 Important Electrical Instructions
      7.3 Important Grounding Instructions
      8. Elliptical Error Messages and Troubleshooting for electronic Issues
      8.1 Error Message: E1
      8.2 Error Message: E2
      8.3 Error Message: E3
      8.4 Circuit Diagram
      8.5 Calibration Procedure
      8.6 Fuse Replacement
      8.7 Troubleshooting Procedure Matrix
      9. Troubleshooting
      9.1 Console Problem
      9.2 Pedal Bases
      9.3 Slider adjustments
      9.5 Controller , Incline Motor,Tension Motor Problem Problem
      9.5 Flywheel & Poly-V Belt Problem
      9.6 Swing Arm Problem
      9.7 Connecting Arm Problem
      10. Q & A
      10.1 Noise
      10.2 Slip Problem
                                                         2                                 Service Manual
10.3 Play
10.4 Smooth Problem
11. Disassembling and Assembling of Parts
11.1 Swing Arm & Lower Handle Bar Replacement
11.2 Side Case Replacement
11.3 Pedal Base Replacement
11.4 Connecting Arm Replacement
11.5 Pedal Arm Replacement
11.6 Slider Adjustment
11.7 Incline Motor ,Controller & Gear Motor
11.8 Flywheel & Poly-V Belt Replacement




                                                3   Service Manual
1. XE895-SE022-01 Outlines




            4                Service Manual
          Handle Bar Cover (R)

                                     Console Assembly
                  Console Mast
                  Cover(L)
                                     Console Mast Cover(R)
                  Side Case(L)
                                     Side Case(R)




       Side Case Rear Shroud          Right Slider Cover


                                       Connecting Arm
                     Pedal (L)
                                       Cover (R)(A)




Rear Stabilizer
Cover
                                         Pedal (R)




                                         Slide Wheel Cover



                                 5                         Service Manual
     Seat Handle Bar (L)

          Console Mast          Swing Arm (R)


                                Moving Range Adjusting
     Lower Handle Bar (L)       Assembly



                Flywheel        Main Frame


       Connecting Arm (L)
                                Lower Handle Bar (R)


         Left Pedal Base

                                Connecting Arm (R)

           Pedal Arm (L)
                                Right Pedal Base

Rear Rail Assembly
                                Pedal Arm (R)




                            6                        Service Manual
                                     Adjusting Lever                                       Bushing Housing,
                                                                                           Pedal Arm

                                    Swing Assembly
                                                                                            Crank Arm
                                                                                            Assembly
                                        Incline Motor




                                Slider Adjustment (L)                                      Wheel Base

                                  Wheel Base
                 Left Driving
                 Assembly                                                                   Gear Motor

Joint Assembly


                                                                                            Connecting
                                                                                            Component




                                                                              Slider Adjustment (R)
                                                                     Right Driving
                                                                     Assembly

                                                            Joint Assembly




                                                        7                                         Service Manual
2. Electronic Parts




         8            Service Manual
2-1 Upper Controllers   Speaker
                                      THUMB SWITCH




                                              Cooling FAN
          DISPLAY




                                  9                         Service Manual
2-2 Lower Controller and Driver




                                                      SPEED SENSOR


      TENSION MOTOR




                                       MOTOR CONTROLLER


           INCLINE MOTOR



                                  10                                 Service Manual
3.Electrical Configurations




             11               Service Manual
 CONSOLE:
 Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console、stride driver and tension motor driver, link the console to output appropriate voltages
 for tension motor that control the elliptical functions.

TENSION   MOTOR:

 It can change to increase or decrease resistance level of brake.

STRIDE MOTOR:
 This is an ac motor. User can to control variable elevation by console within main controller.

GENERAL INFORMATION

CONSOLE
Contains Key controls and LCD Display.
Main controller Include power supply 、 motor driver control circuit and stride control circuit.




                                                                        12                                                          Service Manual
TENSION MOTOR
  Work voltage:DC 4.5~7.5V
  Control resistance increases and decreases.

STRIDE MOTOR
This is a 115 volt AC motor.

Have four wires, red, black, white and green.

Has one 3 pins cable of position sensor.

If there is AC voltage on the Red wire (UP) the stride motor will increase the stride.

If there is AC voltage on the Black wire (DOWN) the stride motor will decrease the stride.

The White wire (COM) is neutral.
The green wire is ground.




                                                                         13                  Service Manual
4. XE895-SE022-01 Product Operation




                 14              Service Manual
Display Windows


                       7.5” LCD Display




                  15                 Service Manual
Operation
Window Display Mode
  IDLE MODE
  1.1 Each program profile will be displayed on the MESSAGE WINDOW sequentially.And recycle display 『PRESS START FOR QUICK START OR
       PROGRAM BUTTON FOR SETUP』at the same time.
  1.2 Heart rate bar LED and Track LED will be display stand light.
      DATA window (7 segment display window) display RPM= 000，CALORIES= 12，TIME = 00:00，DISTANCE = 0.00，PULSE = - - -。
    During 5 minutes no press any key will into IDEL MODE(no contain IDEL MODE)

  DISPLAY MODE
  2.1 Pre-set: DISPLAY ON(DISABLE), You could set the DISPLAY ON/OFF by ENGINEERING MODE.
  2.2 The console will not get into SLEEP MODE when the set up is “ ON ” , unless turn off the power.There is no RPM input in IDEL MODE, and
      enter to SLEEP MODE after 20 minutes without pressing any key.
  2.3 In DISPLAY MODE, LCD screen will has no display, and backlit will be off.  Press any key to wake up the system, and back into IDEL MODE.
  2.4 Resistance in SLEEP MODE: Incline =1


  CHILD LOCK MODE
  3.1 Pre-set: CHILD LOCK OFF (DISABLE).             You could set the CHILD LOCK ON/OFF by ENGINEERING MODE.
  3.2 The message window will display “ CONSOLE LOCKED ” after twice will show ” CHILD LOCK-ON PRESS START AND ENTER TO ENABLE
      OPERATION” , when CHILD LOCK setup is ON.You could setup the CHILD LOCK MODE OFF by pressing “ START ” and ” ENTER ” key
      for more then two seconds. After that it will enter to IDEL MODE.
  3.3 All keys will be no action when CHILD LOCK MODE is active.
  EXERCISE MODE（QUICK START）
  4.1 In IDEL MODE, press START key enter to MANUAL MODE.The age, weight is presetting value.Time counting is count up from 00:00. All
      countable data will count up from “ 0 ” , and resistance is count up from “ 1 ” .
  4.2 You could chose the program by pressing the key: MANUAL、PROGRAM、USER1、USER2、HRC1、HRC2 . And then, press “START” key to start
      the workout. All parameter will be the preset value.
  PAUSE MODE
  5.1 Press “STOP” key enter to PAUSE MODE, and exercise parameters will be recorded.Message window will display “PAUSE”, and upper window
       will display the recorded exercise parameter.
                                                                     16                                                       Service Manual
5.2 In PAUSE MODE, it will display PAUSE.After 5 seconds,MW will show” PRESS START TO RESUME OR STOP TO END WORKOUT”
5.3 It will enter to IDLE MODE after waiting by five minutes without pressing any.
5.4 The STRIDE should back to “18” when the resistance level is “1”.The position of tension motor and STRIDE should back to the preset level before
    it pause when press “START” key.


END MODE
6.1 The message window will display “ WORKOUT SUMMARY ” after end workout and display workout data 3 minutes.
6.2 END MODE：
    6.2.1 Display exercise data in message window each three seconds display 『TOTAL TIME XX:XX』    『AVG SPD XX.X』
                                                                                                   、                、『AVG WATT XXX』    、『AVG
          HR XXX』、『LAPS XX』、『AVG INCLINE XX』、『TOTAL ALT XXX』
   6.2.2 LEVEL and STRIDE Display exercise data in message window and show average value.
   6.2.3 CALORIES ,TIME,DISTANCE display total data in message window .
6.3 When the time counting is end, and END MODE display is finished without pressing any key in 3 minutes.The system will enter IDLE MODE.

RESET MODE
7.1 In IDLE MODE, press STOP key for more than three seconds will enter to RESET MODE and reset the system.           If the system is in CONSOLE
    LOCK MODE you have to quit CONSOLE LOCK MODE first, and you can execute the RESET MODE.
7.2 The message window will finished the reset.After that, the system is in IDLE MODE.




                                                                      17                                                          Service Manual
Function

   SPEED
        Display the current speed in mile per hour.
        DISPLAY range is 0.0 to 99.9
        WORK range is 0.0~99.9
   Stride
        Display the stride position from 18 to 24.
        DISPLAY range is 0 to 99.
        WORK range is 18 to 24.
        STRIDE preset value is 18 to 24.
        Press “UP” or ”DOWN” to adjust stride, each increment and decrement is 0.5.
   LEVEL
        Display the stride position from 1 to 20.
        DISPLAY range is 0 to 99.
        WORK range is 1 to 20.
        LEVEL preset value is 1 to 20.
        Press “UP” or ”DOWN” to adjust stride, each increment and decrement is 1.
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




                                                                       18                                                           Service Manual
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
    In RUN Mode, if the Ellipitcal doesn’t have a signal for 8 seconds then display value will become “0 ”.




                                                                      19                                          Service Manual
Function Button Locations




     PROGRAM BUTTONS
  (Manual, Hill, Fat Burn, Strength,

        Interval, 2 User, 2HR)




                                            CONTROL KEYS

         Fan Key
  Cooling fan switch on or
             off




                                       20              Service Manual
                                               Function Button In Main Mode
READY MODE
  STOP button: Non-function.
  START button: Pressing “ START ” button to start elliptical, When pressing “START” button, there will be 3 second final count down on window
  display, then machine starts running. In MANUAL, elliptical starts at MIN LEVEL .
  LEVEL UP button: If user doesn’t enter a setting then this button is non-functional.
  LEVEL DOWN button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE UP button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE DOWN button: If user doesn’t enter a setting then this button is non- functional.
  FAN button: It can to control ON/OFF for the fan.
  ENTER KEY：
  Press ENTER key enter to parameter setting, and confirm the every setting by pressing START key no pressing ENTER key..
  Pressing ENTER key confirm the every setting or modify parameter use.




                                                                   21                                                          Service Manual
RUN MODE
  STOP button: press “STOP” button to stop elliptical.
  START button: non-functional.
  ENTER button: non-functional.
  LEVEL UP button: Press the button to increase your level and each increase is 1.
  LEVEL DOWN button: Press the button to decrease your level and each decrease is 1.
  INCLINE UP button: Press the button to raise position and each increase is 0.5, the maximum incline position is 20.
  INCLINE DOWN button: Press the button to lower position and each decrease is 0.5, the minimum incline position is 0.
  Fan button: It can to control ON/OFF for the fan.
  ENTER KEY：
        Press ENTER key to switch the exercise data when you are workout. If the display information is the latest data , press ENTER key the
        message window SCAN ICON will lightness and change to auto display every four seconds recycle. The information as below,

      CYCLE MODE WILL FIRST DISPLAY『SPEED XX.XMPH』AND TEHN DISPLAY AS BELOW：
      『WATT XXX』
      『LAPS XX』
      『ALT XXXXM』
      『TIME XX:XX』
      『MAX LV XX』(ONLY PROGRAM MODE DSPLAY)




                                                                   22                                                           Service Manual
5. XE895-SE022-01 Unit Block Diagrams




                  23              Service Manual
Elliptical Configuration




                           24   Service Manual
6. XE895-SE022-01 Basic Connections and Wiring




                      25                 Service Manual
6-1 Display Board wire Connections




                                     26   Service Manual
6-2 Display Board PCB Component Locations

  PCB Board Top




                                            27   Service Manual
PCB Board Bottom




                   28   Service Manual
The console Interface Board wire Connections




                                               29   Service Manual
Amplifier Board wire Connections




                                   30   Service Manual
Driver Board Wire Connections




                                31   Service Manual
Driver Board PCB Component Locations




                                       32   Service Manual
Driver Board LED Indicator Locations




                                                     POWER




                                       INCLINE
                                                  INCLINE
                                       MOTOR UP
                                                  MOTOR DOWN




                                       33                      Service Manual
 Controller Indicator LED debugging

 Indicator           Function                    Condition                             Reason                        Solve
   LED
LED1       Motion of stride motor   Motion of stride motor is up.          Transistor was broken.   Replace controller.
                                                                           Relay failed.
LED2       Motion of stride motor   Motion of stride motor is down.        Transistor was broken.   Replace controller.
                                                                           Relay failed




                                                                      34                                                     Service Manual
Driver Board function


    AC POWER             TRANSFORMER         TRANSFORMER
      INPUT             AC POWER INPUT     AC POWER OUTPUT




AC POWER
  INPUT




                                                                RPM
                                                               SENOR   TENSION
 INCLINE                                                                MOTOR
 MOTOR
   UP




 INCLINE
 MOTOR
   COM


 INCLINE                                 INCLINE
                                                             SYSTEM
 MOTOR                                   MOTOR
                                                              WIRE
  DOWN                                     VR      35                  Service Manual
Tension Motor connector definition function




       STEEL ROPE




        MAIN
        CONTROL
        1.M+                      5
        2.M-                      4
        3.+5V                     3
        4.VR                      2
        5.GND                     1




                                              36   Service Manual
7.   Product Safety Instructions




                37                 Service Manual
7-1 Important Safety Instructions
   - To reduce the risk of electric shock disconnect your Ellipitcal from the electrical outlet prior to cleaning and/or service work.
   - To reduce the risk of burns, fire, electric shock, or injury to persons, install the Ellipitcal on a flat level surface with access to a 115-volt, 15-amp
     grounded outlet with only the Ellipitcal plugged into the circuit.
   - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
     improper adapters or in any way modify the cord outlet.

 7/2 Important Electrical Instructions
   - Never use a ground fault circuit interrupt (GFCI) wall outlet with this Ellipitcal. As with any ap- pliance with a large motor, the GFCI will trip often. Route
     the power cord away from any moving part of the Ellipitcal including the elevation mechanism and transport wheels..
   - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a Ellipitcal is first turned on or even
     during use. If your Ellipitcal is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the Ellipitcal itself
     does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
     have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online at
     www.squared.com part # QO120HM.

 7-3 Important Grounding Instructions
   - This product must be grounded. If the Ellipitcal should malfunction or breakdown, ground- ing provides a path of least resistance for electric current,
     reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
     appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
 - DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
   serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
   outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 115-volt circuit, and has a grounding plug that looks
   like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
   as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
   can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must be connected to a permanent
   ground such as a properly grounded outlet                                                                                                      box cover.
   Whenever the adapter is used, it must be                                                                                                       held in place
   by a metal screw.




                                                                                  38                                                                 Service Manual
8. XE895-SE022-01 Error Messages /
         Troubleshooting




                39               Service Manual
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
 8-1     Error Message：E1
   Definition: All screens are off, and outputs are stop when EEPROM damaged or malfunction.Display message will show “E-1”.
   Troubleshooting: Replace upper controller.




                                                                 41                                                     Service Manual
 Error Message ： - -
   Definition：When you press the Level Up or Down key,the motor does not move.” --” appears on the display.
   Configuration：




                                                                        42                                     Service Manual
 Tension Motor Operation
                              Part           Description

                                             Key signal travels to the display.The main program IC then
                              Display
                                             sends a command signal to the drive board.

                                             Drive board receives the signal and responds by putting out
                              Drive Board
                                             power to the motor.Level UP:+5VDC;Level DOWN:-5VDC


 Tension Motor Troubleshooting

                              Part           Description
                                             If the key beeps when pressed,assume that the signal was
                              Display
                                             sent.
                              Data cable     Inspect the cable and connections.
                                             Inspect drive board power output to the motor.Press the
                                             Level Up is +5VDC;Level DOWN is -5VDC.If there is power
                              Drive Board    to the motor,but the motor does not operate,replace it.If there
                                             is no power output,inspect whether the drive board has
                                             power.


 Tension Motor Voltage Test Procedure
  1. Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in blue wire,Black probe in green
     wire) on the drive board.
  2. Turn on unit power.The display lights up.
  3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates.Resistance increases.
  4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates.Resistance decreases.
  5. If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
  6. Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.
                                                                 43                                              Service Manual
Place probes on the motor control wire(Red probe in palm wire,Black probe in black wire)


                                         44                                                Service Manual
8-2 Error Message：E2
   Definition：The console board is not detecting the VR voltage value,or the voltage value has exceeded the range.”E3” appears on the display.
   Configuration：




                                                                          45                                                          Service Manual
   Case of RAMP ERROR
     Stride VR value exceeds the range. E3 appears on the display.
        Stride motor isn’t operation up or down,making the VR value exceed the range.
        After turning on the unit,the display board detects that the stride VR voltage exceeds the range,so E3 appears.
        Action Flow Chart




                                                                       46                                                  Service Manual
 Troubleshooting
            Part            Troubleshooting
                            1.Reconnect VR wires.
            Stride VR
                            2.Inspect whether the stride wires are broken or disconnected.
                            1.Inspect the stride wire and 14-pin cable connections.
            Display board
                            2.Test whether the VR voltage varies at the stride wire terminal.
                            1.Inspect the wire connections.
            14-pin cable    2.Inspect whether wires are broken or crimped.
                            3.Replace the wires and test again.
            Driver board    Inspect the display board 14-pin connections.




                                                       47                                       Service Manual
 Test configuration. The console to driver board connector pin define function




            14                 The console to driver board
            13
            12                 connector pin define
            11                 function:
            10
            9                  The console to driver board
            8                  connector pin define
            7
            6                  function:
            5                  1. MTR-
            4
            3                  2. MTR+
            2
            1
                               3. +5V
                               4. MPOS
                               5. GND
                               6. RPM1
                               7. GND
                               8. RPM2
                               9. GND
                               10. +12V
                               11.GND
                               12. INC+
                               13. INC-
                               14. IPOS



                                                             48                   Service Manual
                Configuration.Stride motor control function relate parts location



                                                           INCLINE MOTOR                        INCLINE MOTOR
                                                                  UP LED                           DOWN LED




                   The position sensor wires
                                                                                                  1.     MTR-
                   1.Red = Ground,
                                                                                                  2.     MTR+
                   2.White = Position signal,
                                                                                                  3.     +5V
                   3.Black = 5vdc,
                                                                           1. RPM1                4.     MPOS      1. MTR-
                   (0~5v depending on incline position)
   RED-UP                                                                  2. GND                 5.     GND       2. MTR+
                                                                           3. RPM2                                 3. +5V
                                                                           4. GND                                  4. MPOS
                                                                                                                   5. GND
White-NEUTRAL
                                                                                                                   6. RPM1
                                                                                                                   7. GND
                                                                                                                   8. RPM2
BLACK-DOWN                                                                           4,3,2,1           5,4,3,2,1
                                                                                                                   9. GND
                                                                                                                   10. +12V
                                                                                                                   11.GND
                                                                              14,13,12,11,10,9,8,7,6,5,4,3,2       12. INC+
                                                          3,2,1
                                                                                                                   13. INC-
                                                                                                                   14. IPOS


                                                            49                                                          Service Manual
Test Procedure：
    1.   Run calibration again.
    2.   Does the stride motor move at all?
    3.   If no, do the Up/down lights on the stride board light?
    4.   If they light, do the relays click on?
          If the relay clicks on but the motor doesn’t move: with the stride light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down
                (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the mains voltage
                ~ 115VAC. If the voltage is present but the motor doesn’t move, then the motor is bad.
          If the light is on, but the relay does not click on then the stride board needs to be replaced (Bad relay most likely).
    5.   If the motor moves, is there a sensor reading on console?
          The STRIDE window will display the computer stride setting (after speed cal. ends); 20 for max stride, 0 for lowest stride. The Stride window is a counter that is
                showing the actual position sensor output. If the motor is moving and there is no count occurring in the Stride window then there is a problem in the position sensor
                wiring or circuitry.
          If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
                Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
                If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
          If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and there should be a voltage
                between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical,
                as long as it’s somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves,
                but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
    6.   Check the voltage from the potentiometer at the 3-pin connector on the stride board. If there is no voltage then the wire from the motor to the connector is faulty.
    7.   If there is a voltage, check at the output connector to the console at the bottom of the stride board. If no voltage present then there is a problem on the stride board.
         There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.
         The only problems that are possible are a bad solder joint or broken circuit on the board.
          Console connector wiring, these connections are the same on the stride board and at the console.
                              Pin 3 = 5vdc
                              Pin 2 = position signal 0~5vdc
                              Pin 1 = ground
    8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there,
         but is there at the stride board then check the entire cable from stride board to console for cuts or bad connection at the inline connectors.
    9.   If there is voltage at the console connector, but no count in Stride window when motor is moving then there is a problem with the console.




                                                                                       50                                                                        Service Manual
8-3 Error Message：E3
 Definition：During stride action,the display board CPU cannot read the VR value,so E3 appears.
 Configuration：




                                                                     51                          Service Manual
Cause of E3
      Press the stride UP/DOWN key.The stride doesn’t operate. E3 appears on the display.
          Explanation
             Press the stride UP and DOWN key.The driver board UP or DOWN indicator lights.The stride operates,moving the VR,which changes
                the VR value.
             The display board CPU reads the stride VR value.If there is no VR value change,to the CPU,the stride is not operating when it should
                be. E3 appears on the display.
          Action Flow Chart




                                                                        52                                                        Service Manual
Troubleshooting
            Part            Troubleshooting
                            1.Press stride UP key.The driver board UP LED lights.
            Display board   2.Press stride DOWN key.The driver board DOWN LED lights.
                            3.If not as above,inspect the cable and connections.
                            1.Inspect whether the 14-PIN cable is connected well.
            14-pin cable
                            2.Test by replacing the cable with a good one.
                            Inspect whether the driver board UP/DOWN LED is lit.
                            1.Press stride UP or DOWN key again,making the stride motor return to its
            Driver board
                            position.
                            2.If E3 still appears,re-calibrate the stride set.
                            1.Inspect whether the stride motor is stuck.
                            2.Inspect whether the stride gears are cracked.
            Stride motor
                            3.Test whether the stride motor has a broken circuit.
                            4.Re-calibrate the stride set.




                                                      53                                                Service Manual
     XE895-SE022-01
ELLIPICAL CIRCUIT DIAGRAM




           54               Service Manual
CALIBRATION PROCEDURE

   Stride Calibration:
   If there is a problem with the stride, try running the calibration. Press the Stride ▲ key and the Start key
   at the same time. Hold them down for 5 seconds and the Stride calibration will start and run
   automatically. If the problem persists contact service department.




MAINTENANCE MENU IN CONSOLE SOFTWARE

   The console has built in maintenance/diagnostic software. The software will allow you to change the
   console settings from English to Metric and turn off the beeping of the speaker when a key is pressed for
   example. To enter the Maintenance Menu (may be called Engineering Mode, depending on version)
   press and hold down the Start, Stop and Enter keys keep holding the keys down for about 5 seconds
   and the Message Window will display “Engineering Mode”. Press the Enter button to access the menu
   below. Press the Level ▲/▼ keys to navigate the menu.
   a. Key Test (Will allow you to test all the keys to make sure they are functioning).
   b. LCD Test (Tests all the display functions).
   c. Functions (Press Enter to access settings and Up arrow to scroll).
       i.   Display Mode (Turn off to have the console power down automatically after 20 minutes of inactivity).
       ii. Pause Mode (Turn on allow 5 minutes of pause, turn off to have the console pause indefinitely).
       iii. ODO Reset (Resets the odometer).
       iv. Unit (Press enter to select ENGLISH or METRIC).
       v. Beep (Turns off the speaker so no beeping sound is heard).
       vi. Motor Test (Press Enter to run the resistance motor up and down in a continuous loop. Display shows
            level setting and position sensor reading. Press Stop to end test).
       vii. Safety.
   d. Security (Allows the keypad to be locked to prevent unauthorized use)




                                                     55                                       Service Manual
  8-6 Fuse replacement




          FUSE 5A




If your elliptical loses power or will not start, check the fuse located on the motor controller.
DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric shock
Remove FUSE holder.
Remove and replace the fuse on the holder

                                                                           56                         Service Manual
  8-7 Troubleshooting procedure matrix

                    Condition                                        Reason                                             Solve
LCDs not bright, incomplete or imperfect.          1. LCD light is broken.                    1. Replace with new LCD or console.
                                                   2. Power to console too low.               2. Check AC power is 110-120V.
                                                                                              3. Check power to console.
                                                                                              4.Replace lower controller.
LCD displays not bright, incomplete or imperfect. 1. LCD displays are broken.                 1. Replace with new console.
The stride position doesn’t match console         1 Console is not calibrated.                1 Calibrate the console.
STRIDE ERR ,STRIDE window displays “E3”.          1 Position sensor value of stride motor is 1 Turn off the AC switch and turn on power again.
                                                                                              2. Calibrate the monitor.
                                                  wrong.
Erratic pulse display.                            1. Another chest belt in use around         1. Check for other chest belt use around elliptical.
                                                     Ellipitcal.                              2. Change the position or direction of elliptical.
                                                  2. Other magnetic field disturbance.        3. Replace with new receiver.
                                                  3. Receiver is broken.
UP/DOWN button of                                 1 The connector of STRIDE CABLE             1 Connect the wires again.
STRIDE ADJUSTMENT SWITCH can’t be used.             and   CONSOLE    not connected  properly.
                                                  2. The connector of STRIDE CABLE            2. Connect the wires again.
                                                  and STRIDE ADJUSTMENT SWITCH
Stride button just can press UP, can’t press      W/CABLE not connected properly.
DOWN.
Stride button just can press DOWN, can’t press                                                3. Replace the cable.
UP.                                               3 The   connector of STRIDE  CABLE   or
                                                  STRIDE ADJUSTMENT SWITCH CABLE
                                                  got damage.                                 4. Replace buttons.
                                                  4. Button of STRIDE ADJUSTMENT
                                                  SWITCH is broken.                           5. Replace the cable.
                                                  5. The connector of STRIDE CABLE or
                                                  STRIDE ADJUSTMENT SWITCH CABLE 6. Replace the cable.
                                                  got damage.
                                                  6. The connector of STRIDE CABLE or
                                                  STRIDE ADJUSTMENT SWITCH CABLE
                                                  damaged.
Hand pulse lost its function.                     1. Hands not on the hand pulse sensors 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                      or only one hand on sensor.
                                                  2. The connector of HANDPULSE               2. Connect the cable again.
                                                     W/WIRE and Console not connected
                                                                            57                                                            Service Manual
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
Chest belt too close to the Ellipitcal.   Weak battery.                            Replace with new lithium battery with type CR2032.




                                                                  58                                                          Service Manual
9. Troubleshooting




        59           Service Manual
9-1 Console Problem
   1. Under normal use console screen will display, if there is no display, first check AC adapter to make sure it is in the correct position.




   2. Next, check if all the wires are inserted in the firmly and securely on to the console.




                                                                   60                                                         Service Manual
3.   Then remove the AC adapter fuse to check for damage, replace if damaged.




4. Remove console cover, left and right chain covers, check if all the wires are inserted in the correct positions and check
   if whether the wires broken.




                                                         61                                                  Service Manual
9-2    Pedal Bases
      1. Left and Right Pedal Bases and Pedal Arms (L)& (R) are the most important part of this model. Pay attention to the
         maintenance.
      2. If there are some noises happened, please check if it is rubbed or something dropped, and then check Aluminum Track.
         If it got damage, please replace it as soon as possible.
      3. If the Ø38_Slide Wheel, Urethane gets damage, if yes, replace it directly.
      4. Clean the Aluminum Track and Ø38_Slide Wheel , Urethane and add some lubricants.




      5. If it looses, just use 11m/m_wrench to adjust the Ø38_Slide Wheel, Urethane which on the adjustment wheel fixing
         plate in tight appropriately.




                                                            62                                                Service Manual
9-3    Slider adjustments
      1. Slider adjustment is the most important part of stride adjustments. Check if the Ø40 Adjustment Transportation Wheel
          is damaged or not. If yes, please replace it according to the disassembly steps.
      2. Check if Swing Assembly (#16) is defaced on the surface. Get some lubricants after wiping.




      3. Adjust Wheel Base according to the disassembly steps if it has space between two parts, also adjust to the standard
         scales.




                                                             63                                                Service Manual
9-4    Controller , Incline Motor,Tension Motor Problem Problem
      1. Incline motor, controller and gear motor are all electronic components. Please do not disassemble it if you are
         unfamiliar with these parts.
      2. When incline motor is not functioning, check all the wire for secure connection, check incline controller and power
         adaptor is damaged or broken. Replace damaged or broken parts.
      3. To return the incline motor, make sure it has been reset then turn the tubing clockwise to the end as shown. Turn the tubing again but
          counterclockwise two and half circles or let the center between two holes be 245 ±1 mm.




      4. If there is no resistance, first check to see if console is functioning normally. Next check the Gear Motor cable, if worn or damaged remove
          the Steel Cable. Use Phillips screw driver to remove the Tapping Screw w 5x19 securing the Gear Motor cable and replace cable with new.




                                                                        64                                                          Service Manual
9-5 Flywheel & Poly-V Belt Problem
   1. There are two kinds of problems caused of flywheel as general. One is adjusted resistance doesn’t work, another is
      noise problem. When the user uses the console to adjust the resistance, but it doesn’t work and the gear motor is
      working. Check the steel cable if it works with the flywheel or it is loose.




   2. Check the flywheel, Ø330_Drive Pulley and Idler Wheel Assembly if they are rubbed while the flywheel is spinning and
      causing the noise problem, and then disassemble the steps of flywheel and reset. If it is caused the noise problem of
      flywheel by itself, we suggest have a new replacement directly.
   3. If the Poly-V Belt is slipping, simply adjust the cap the on hook-type screw with the #13 wrench to adjust. Refer to the
      disassembly procedures for adjustment.




   4. If the Poly-V Belt worn or damaged, replace with new part.




                                                           65                                                  Service Manual
10. Q & A




  66        Service Manual
10-1    Noise
       1. There are potentially many locations where noise can originate from, but it is not easy to isolate the location
          specifically. In the front, the chain cover and the round disk, EPE, round disk, sleeve, Cross Bar ‚ Belt and belt pulley,
          Idler Wheel Plate ‚ Swing Arm, Swing Arm Axle, Flywheel, Steel Cable, Slide Wheel and Crank Arm during
          assembly along with side Inclinable Rail Assemblys as well as pedals. The main reasons are usually not enough
          lubrication, unsmooth rotations, and loose screws. Because the product is designed based on linked designs,
          resolving noise issue will vary from machine to machine depending on actual situation.




                                                              67                                                    Service Manual
10-2    Slip Problem
       1. The CAP Socket Head Cap Bolt 3/8 "x2-1/4 on top and nyloc nut 3/8" x11T must be tightened securely.




       2. Belt: This issue appears quite often, because after a period of time, most belts will become loose from use
          depending on usage time. Solution will depend on weight and adjustment methods, refer to belt disassembly
          procedures for references.




                                                           68                                                Service Manual
10-3    Play
       1. Shaking is mainly due to loose screws, so check and tighten loose screws first. Check connection points to see if gaps have been
           created after prolong use causing wear and tear or improper assembly. For example, shaking of the foot pedal is caused by loose
           Carriage Bolts, from improper assembly.




10-4 Smooth Problem
     1. Check for loose screws if machine motion feels unsmooth. Check if there are foreign object on or around the sliding
           rail, use an alcohol wipe to remove and re-lubricate with lubricant.




                                                                   69                                                         Service Manual
11.Disassembling and assembling
              of Parts




               70            Service Manual
11-1. Swing Arm & Lower Handle Bar Replacement
     1. Use a Phillips screwdriver to remove Sheet Metal Screws 3.5x12mm securing the swing arm covers (Front and Back)




     2. Remove the 3/8" × 2-1/4"_Socket Head Cap Bolt (#137), Ø3/8" × Ø19 × 1.5T_Flat Washer (#176) and 3/8" × 7T_Nyloc
        Nut (#165) and fix the upper handle bar and lower handle bar by using two of 14m/m wrenches.




                                                                71                                                    Service Manual
3.    Disconnect the wiring connecting the upper and lower swing arms.




4. When the keys on the handrails are not functioning, first remove the stickers, use a Phillips head screw driver and remove the M5x20mm
     Flat Head Socket Screws securing the keys to the Swing Arm.




                                                               72                                                        Service Manual
5.   Separate the cables of resistance button and 450m/m_handle wire (upper), and get the handle switch.




6. Use 14mm wrench to release 3/8"x3/4" Hex Head Bolt together with 3/8"x30x1.5T Flat Washer which secure Swing
   Arms.




                                                      73                                                   Service Manual
7.    Release the M5 × 15L_Phillips Head Screw of Connecting Arm Cover A and Connecting Arm Cover(B) by using
     Phillips head Screw Driver. Remove the Connecting Arm Cover(A)&(B).




8. Use #12 and #13 open end wrench affix swing arm assembly and remove Hex Head Bolt 5/16”x1-1/4”, flat washer
   5/16”x20x1.5T and nyloc nut 5/16”x7T. Remove swing arm assembly.




9. Reassemble in the reverse order as disassembly.




                                                     74                                             Service Manual
11-2. Side Case Replacement
     1. Remove Seat Handle Bar and Lower Handle Mast Assembly. (Refer to step 11-1)
     2. Remove two of the Ø4 × 15L_Sheet Metal Screw of Console Mast Cover by using the Phillips Head Screw Driver.




     3. Use Phillips head screwdriver to remover eight Sheet Metal Screws Ø 4x15L and remove left chain cover.




     4. Screw on Side Case(R) of Main Frame by using Phillips head Screw Driver.




                                                                   75                                            Service Manual
5. Remove the 5 × 19L_Tapping Screw on the Side Case (L) of Main Frame by using Phillips head Screw Drive.




6. Remember the position of AC Input Module and the color of cables. Remove two of the Connecting Wire and Ground
   Wire, and then it can remove the Side Case (L) and then it can remove the Side Case (L).




                                                    76                                              Service Manual
7. Remove the 5 × 19L_Tapping Screw on Side Case Rear Shroud of main frame by using the Phillips Head Screw
   Driver.




8. According to above instructed steps and reassemble again. Do not clip the cables, Side Caser(R)&(L), the connection
   of Side Case Rear Shroud and lock the screws.




                                                      77                                                Service Manual
11-3. Pedal Base Replacement
    1.   First remove the Pedal Bar Assembly, then use Phillips head screwdriver to remove the Phillips Head Screws M5x10mm securing the
         cover to pedal arm joint and remove pedal arm joint cover.




    2.   Pull out the end of Slider Cover by hands.




    3.   Remove the 5/16" × 1/2"_Hex Head Bolt, Ø5/16" × 23 × 1.5T_Curved Washer of connecting Component by using
         12m/m_Wrench. Separate the Connecting Component and Swing Assembly.




                                                                   78                                                       Service Manual
4.   Pull out the Pedal Base (L)&(R) in back and separate with the Connecting Arm (L)&(R).




5.   Release the 5/16" × 1/2"_Hex Head Bolt and Ø8.5 × Ø26 × 2.0T_Flat Washer of connecting Component by using
     12m/m_Wrench.




                                                        79                                           Service Manual
6.    Use 12mm open end wrench to remove hex socket screw 5/16”x1/2”mm and flat washer Ø 8.5x26x1.5T. Pull out the
     pedal carriage bolts to remove the Pedal Bar Assembly




7.   Release the 5/16" × 15L_Hex Head Bolt of Pedal Arms by using 12m/m_Wrench. Ø38_Slide Wheel, Urethane.




8.   Remove Adjustment Wheel Fixing Plate(L)& (R) by using the 12m/m_Wrench and release 5/16" × 15L_Hex Head Bolt,
     Ø5/16" × Ø23 × 1.5T_Flat Washer from Left and Right Pedal Base.




                                                     80                                              Service Manual
9. Regarding to above steps to assemble again.
10. Lock Ø8 × Ø16 × 2T_Flat Washers in the middle of Slide Wheel, Urethane and Adjustment Wheel Fixing Plate (L) & (R)
    when assemble the Ø38_Slide Wheel , Urethane.




11. Adjust Ø38_Slide Wheel , Urethane and Aluminum Track by using 11m/m_Wrench and 1/4" × 1/2"_Hex Head Bolt
    while lock the Left and Right Pedal Base back on Pedal Arm (L)& (R).




                                                      81                                               Service Manual
11-4. Connecting Arm Replacement
    1. Remove the Left and Right Pedal Bases according to the disassembly steps. Separate the screws of M12 ×
        P1.75_Rod End Bearing from Lower Handle Bar (L) & (R) and Pedal Arm (L) & (R).




    2. Remove the 5/16" × 1/2"_Hex Head Bolt and Ø5/16" × Ø23 × 1.5T_Flat Washer from the Pedal Arm (L) & (R) and Rear
        Rail Assembly by using 12m/m_Wrench.




                                                         82                                              Service Manual
3.   Pull out the Pedal Axle(Ø 17x95L) from the inside of Pedal Arm (L) & (R).




4. Remove six pieces of M5 × 6L_Phillips Head Screws from Frame Cover and brush by using Phillips Head Screw
    Driver.




5. Remove the M5 × 6L_Phillips Head Screws from Pedal Arm (L) & (R) of Aluminum Axle End Cap by using Phillips
    Head Screw Driver.




                                                        83                                          Service Manual
6.   Remove the three pieces of 5/16" × 1/2"_Hex Head Bolt from the Pedal Arm (L) & (R) of Aluminum Track by using
     M5_L Allen Wrench.




7. Release the Nut from the M12 × P1.75_Rod End Bearing by using 19m/m_Wrench.




8. According to above steps to assemble again.
9. Line up the Pedal Axle with surface of breach of Fixing Plate and lock with the screw.




                                                        84                                             Service Manual
11-5. Pedal Arm Replacement
    1. Remove the Side Case (L) & (R) and Pedal Arm (L) & (R) according to the disassemble steps.
    2. Pull out the Ø17 × 34L_Rotate Axle A from the inside. Remove the 5/16" × 1/2"_Hex Head Bolt and Ø5/16" × Ø23 ×
       1.5T_Flat Washer from the outside of Ø17 × 34L_Rotate Axle A for Slider Adjustment (L) & (R) of Joint Assembly by
       using 12m/m_Wrench.




    3. Remove the 5/16" × 1/2"_Hex Head Bolt and Ø5/16" × Ø23 × 1.5T_Flat Washer from the Crank Arm Assembly for
       Bushing Housing, Pedal Arm by using 12m/m_Wrench.




                                                          85                                                Service Manual
4.    Remove the 5/16" × 1/2"_Hex Head Bolt and Ø8.5 × Ø26 × 2.0T_Flat Washer from the Rear Rail Assembly for Joint
     Assembly by using 12m/m_Wrench.




5. If you want to remove the J4FM-1719-09_Bushing from the Joint Assembly, please use the pole which is smaller than
   Ø 17 and hit the bushing.




6. Use #8 hex wrench and #14wrench to remove Gap socket screw 3/8”x2-1/4”, flat washer 3/8”x19x1.5T and nyloc nut 3/8”x11T connecting
     the Inclinable Rail Assembly and rotating block, to remove Inclinable Rail Assembly.




                                                                  86                                                 Service Manual
7. If you want to remove the WFM-2528-21_Bushing from the Bushing Housing, Pedal Arm, please use the pole which is
   smaller than Ø 25 and hit the bushing.




8. If you want to remove the WFM-1719-12_Bushing from the Rear Rail Assembly, please use the pole which is smaller Ø
   17 and hit the bushing.




                                                     87                                               Service Manual
9.    Remove two piece of the M5 × 15L_Phillips Head Screw from the Slide Wheel Cover by using the Phillips Head
     Screw Driver when take apart the Ø78_Slide Wheel, Urethane.




10. Remove the Ø17_C Ring and Ø17 × 0.5T_Wave Washer from the Pedal Arm (L) & (R) of Ø78_Slide Wheel, Urethane
    by using the C Ring.




11. Reverse above procedures to resume Pedal Arm.




                                                      88                                               Service Manual
12. Following the steps gradually as beginning of Ø17 × 0.5T_Wave Washer, Ø78_Slide Wheel, Urethane, Ø17 ×
    0.5T_Wave Washer, and Ø17_C Ring when assemble the Ø78_Slide Wheel, Urethane.




13. Line up the Wheel Base with surface of Ø17 × 34L_Rotate Axle A when assemble the Joint Assembly and Adjusting
    Lever and lock with the screw.




14. Lock the Bushing Housing, Pedal Arm on the Pedal Arm (L) & (R) by using the torque wrench to up to 550lb.




                                                      89                                                Service Manual
11-6. Slider Adjustment
     1. According to the slider adjustment disassembly steps to remove joint Assembly.
     2. Use no.12 wrench to remove 5/16”x1/2”hex head bolt and 5/16”x23x1.5T flat washer from B Ø 178x41LRotate Axle
        which fixed on swing Assembly on the main frame.




     3. Pull out the B Ø 178x41LRotate Axle




                                                         90                                              Service Manual
4. And use 12 m/m wrench to release the 5/16" × 1/2"_Hex Head Bolt & Ø8.5 × Ø26 × 2.0T_Flat Washer and also remove
   Swing Assembly & Slider Adjustment which is fixed at Adjusting Lever on Moving Range Adjusting Assembly.




5. Use no. 12 m/m to release the 5/16" × 1/2"_Hex Head Bolt & Ø8.5 × Ø26 × 2.0T_Flat Washer which is fixed at
   Adjusting Lever on Slider Adjustment and then could remove Adjusting Lever.




                                                     91                                               Service Manual
6. Use less then Ø 17 round bar to knock down the J4FM-1719-09_ bushing from Adjusting Lever.




7. Use 13 m/m wrench to release M8 × 6.3T_Nut which is fixed on Wheel Base, and release the M8 × 20L_Socket Head
   Cap Bolt. And then can pull out swing Assembly.




8. Use less then Ø 17 round bar to knock down the J4FM-1719-09_ bushing from swing Assembly.




                                                    92                                             Service Manual
9. Use M5_Allen Wrench & No 13 m/m_Wrench to remove the 5/16" × 1-3/4"_Button Head Socket Bolt, 5/16" × 7T_Nyloc
   Nut which fixed on Ø40_Adjustment Transportation Wheel on Slider Adjustment. And then can remove
   Ø40_Adjustment Transportation Wheel & Wheel Base.




10. Reverse the procedures to return parts.
11. When reverse the Swing Assembly combines with main frame, Bψ178x41L_Rotate Axle needs to be align the flat
    portion of the notch on the U-seat and locked screw.




                                                     93                                              Service Manual
12. When lock back for Ø40_Adjustment Transportation Wheel need to pay attention for 5/16" × 7T_Nyloc Nut have to
    same position as crank which locked in the Slider Adjustment Axle.




13. When every part were assembly, use torque wrench to lock M8 × 20L_Socket Head Cap Bolt to 150lbs which is fixed
    for wheel base, and lock tight for M8 × 6.3T_Nut and cover back the slider cover on slider adjustment




                                                      94                                               Service Manual
11-7. Incline Motor ,Controller & Gear Motor
     1. According to instructions of slider adjustment to remove slider adjustment, and use Allen wrench M6 to release Socket
        head cap bolt (M8 × 40L) which secure fixing piece on the main frame




     2. Plug in the power supply before remove Incline Motor, use console to adjust program to 21”(as shown in Figure 2), if
        need to remove Gear Motor then adjust resistance control to max.(level 20) and cut off the power.




                                                            95                                                 Service Manual
3. And then use 2 pieces of 17 wrenches to release incline set screws(Ø 10x62L), flat washer (3/8”x19x1.5T),nylon
   nut(M10x8T), nylon washer (Ø 24x Ø 10x3T)*2pcs from moving range adjusting assembly.




4. Release the incline set screws (Ø 10x40L), flat washer (3/8” x19x1.5T), nylon nut (M10x8T) which fixed incline motor.




5. And then use Phillips head screw driver to release Tapping screw(Ø 5x19L)*4pcs, circuit cover from fixed circuit cover
   on main frame.




                                                       96                                                  Service Manual
6. Use the diagonal pliers to cut the cable ties of the fixed wires, and use Phillips Head Screw Driver to release tapping
   screw(Ø 5x19L) from incline motor also unplug the wire from incline motor connected to the controller (and remember
   the wire position). And then the incline motor wire can be pulled out and remove incline motor.




7. Before remove the gear motor needs to take out Steel Cable first.




8. Use Phillips Head Screw Driver to release tapping screw(Ø 5x19L)*2pcs from fixed gear motor. Pull out connected wire
   then remove gear motor.




                                                        97                                                 Service Manual
9. Remember all the wire position before release controller, and then pull out all of wires, and use Philips Head Screw to
   remove tapping screw(Ø 5x19L)*2pcs from fixed control plate on main frame.




10. When remove spring, use 2 pieces of 14 wrenches to release hex head bolt (3/8x19L), washer (3/8” x19x1.5T), nylon
    nut(3/8”x7T) which foxed moving range adjusting assembly then can remove spring.




                                                        98                                                  Service Manual
11. Use 12mm wrench to release hex head bolt (5/16’’x1/2’) and washer (5/16’’x23x1.5T) which fixed on inclines rotate
    axle A Ø 17x108L.




12. Pull out the inclines rotate axle Ø 17x108L from the other side then remove moving range adjusting assembly.




                                                       99                                                 Service Manual
13. Use a smaller than Ø 17 round bar to knock down the bushing J4FM




14. Reassemble in the reverse order as disassembly
15. When reassemble Incline rotate axle must align the notch plane and then fasten a screw.




16. Reassemble the incline motor with nylon washer (Ø 24x Ø 10x3T)*2pcs.




                                                      100                                     Service Manual
     17. Completed fasten incline motor and all the wires, Plug in the power supply and use console to adjust program to 18”,
         and then fasten socket head cap bolt (M8x40L) which fixed on spring. And fasten all the parts.




11-8. Flywheel & Poly-V Belt Replacement
      1. According to the gear motor disassembly steps to remove the steel cable from magnetron flywheel




                                                            101                                                 Service Manual
2. Use 13mm wrench to release nylon nut(M8x7T) fixed at idler wheel assembly on main frame.




3. Use 13mm wrench to release adjust screw, nylon nut(M8x9T), rod end sleeve, flat washer (5/16”x23x1.5T) fixed on
     idler wheel assembly




4. Pull out the drive belt from drive pulley.




                                                     102                                               Service Manual
5. Release nylon nut(M8x7T),flat washer (5/16”x23x1.5T), carriage bolt (M8x20L)which fixed on idler wheel assembly.
     Then remove the idler wheel assembly.
6. When remove the idler wheel bearing 6203 use C clip to release the C Ring Ø 17 which fixed on idler wheel
     assembly.




7. Use 15mm wrench to release flange nut 3/8" -UNF26 x 11T which fixed on magnetic flywheel.




                                                     103                                                Service Manual
8. And then remove the magnetic flywheel together with the belt from main frame oblique side.




9. Reassemble in the reverse order as disassembly.
10. When reloading the magnetic flywheel and belt, reversing drive pulley, belt and drive pulley must maintain in the
     middle position.




                                                      104                                                 Service Manual
11.   If belt biased to one side, release flange nut 3/8" -UNF26 x 11T and use 17mm wrench adjust nut fixed on magnetic
      flywheel inner. Belt and drive pulley must maintain in the middle position, and then fasten flange nut 3/8" -UNF26 x
      11T.




12.   Use nylon nut(M8x9T) on screw shackle to tight up and flick belt with a crisp sound or use sonic device measured
      at190HZ(±10)( As shown in Figure 10) and then turn crank arm assembly to make belt and flywheel rotation
      smoothly, then reassembly other parts.




                                                       105                                                 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS 1

"OU JeUOIeUJa}U] ODBAG

OIVAC

jenuep) 9dIAIaS
cc04S-S684X


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

S9UI/INO TO-2204S-S68AX 'T


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDY 2d1A1aS c

JOAOD |28UM PIS

(uy) leped
JOAOD
Jaziiqeys 1e8y

(Yu) sen0g

wu Bundeuu09 (7) leped

J@AOD JOPIIS WUBIY pnoiys Jeay ese9 apis

(y)esed apis

(Y)J9A0D }Sey BJoSuOD

(q)ese9 apis

(4)49A0D
JSP BJOSUOD
A\quiessy ajoSsuoD

(Y) JOAOD Jeg sjpueH


=== OCR SUPPLEMENT, PDF PAGE 6 ===
<!-- render-vs-extraction: 60 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS 9

(uy) Wy leped
Ajquiassy |ley se3y

—.

(P LZA
SS
eseg jeped jybIy SS Ses hr,

WIV |eps
—- (q) way leped

ee ee fig
Py | ay) 4
| y ii Za aseg |2Pad Yo

) elim

g J oS
tee 2) i

4 ‘
LA ,
(y) seg a]pueH JaMo07 A\ I 4
SV 22

(y) Wuy Buyosuu09

(q) way Budeuu0D

. 1 KP
“a 4Y/
ewes uley| eK \\ jaQUMA|4
SZ
CAS
ound
im
A\quessy (4) seg a]puey Jamo7

Bunsnipy ebuey Bulaop\

(y) Wy BuIms \Se\| BjOSuOD

1) seg ejpueyH yeas


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Va) | \ A

\ \\ \ jae * : a
\ ye \\" 4 <5

ma

\\@e
7

i ©
4
Oo D

3 |
cg ri
<<
>
a €¢
o)
om
>
2
c
fw
3
Oo) O00 @ = > O ee
= oO {@) a> on 3 an
no
~ 35 re) ® oS o >
Fa] =) = = 3% ~— 5
_ o8 = a o> = a
DS (e) iat) => 5
50 g @ 3 )
a D


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

S

SHUCd IIUOA]IVI]/4 “2


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS 6

aatrtrmaasvias

\ a
Nv3 Buljoo5 \ \

AW1dS10

jayeads S19]]01]U0D Jadd¢f T-z


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDJ 9d1A1aS OL

YOLOW ANITONI

YATIOULNOOS YOLOW

AIALIG PUue J9]JOIJUOD JIMO’'] 2-2


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

S

suoneinbiUoZd /eI14199/F7'¢


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

uoneiad¢C JONpPOld T0-ZZ04S-S684X “pb


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS Gq

= a = —— ee =
Y3a.LN3 dOLls wAN LYVLS NV4
/ @® = a + -— < “3

Z- 4H 4H Z-43aSN oF W3SN IWANSLNIHLONSYIS O1GYYD = NUNd IVs = TH TWANVW

2& TT MA BY F %

SJ sHoueapsnn
one
ae

oo-o00 G88
31140ud 3 Cuuw 9eae

11Vu LYV3H [a

Ae\dsig G01 .G°2

smopulM Ae|dsig


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 50 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[/DNUD 201A1a 0z

Ho
JO UO YOIUMS Ue} Hul|jooD
Asy ue

7- 4H 4H Z-43aSN oF W3SN IWANSLNIHLONSYIS O1GYYD = NUNd IVs = TH TWANVW

a & Tr mM aA BY FF %

(MHZ JESN Z ‘JeAJeyUy
‘yBuens ‘wing ye ‘IIH ‘Jenuey|)
SNOLLNG WWeSOud

LINAS

3JUNJOUd JDSNW

08

; OO-00
71 aa CT al
jive LUV3H

suolje907] uoyINg UONOUNS


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDY 2d1A1aS

sueibeig YIO/g UN T0-2Z04S-S684X "G


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 40 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS bz

WOSNAS
Waal

HOLIMS
Jb Pe Ke
LAS YA —<—= >
YOLOW —— qaduYuvod wAAnd
ANIIONI

YO.LOW

NOISNAL

ino
ANIT
NIANTI
WALI NV

wd
WANVHAdS

UVAaTIOGNVH
4H

SINOHL NWA
Guvod AV 1WdSid => ONFIOO3
waAITY ——»
YH SSA TAL = as

uoleinbiyuog jeondiy|y


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDY 2d1A1aS

Huu pue SuolIaUUO’D IISeg TO-2Z0AS-S684xX 9


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1 Display Board wire Connections

BLUETOOTH
+<—_

SYSTEM CABLE | nC

32 | -
perpen | CS11016-24
_——
KEY BOARD a L112 |_n0 |< WIRELESS HR
LEVEL STRIDE | CONTACTHR

THUMB SWITCH || THUMB SWITCH| HANDLEBAR |) COOLING FAN

26 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JDNUDY 2d1A1aS lz

90309 Oo OS

ath “ a

a

tliat th as. ml

do] pueog god

SUOI}EIO7] JUBUOdWIOD Add pieog Aeldsig Z-9


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 34 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E5)a37
ft) aes Exar.
) Sjeas G

530 alt)

Sor

sah =9Ggiedis

Cs: iT) aig aye 2p?
Spo en Tw,

a t 88 *

CBE m ai

a Hl dnc.

cacaaae bia

im

a
Ea
ie sageeeyy ag B j

(T= Tea

- owe a oO


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUDJ] aI1A1aS 6z

HOLIMS
qINNHL
HCriLLs

YONAS AS Td
dIYDANVH

HOLIMS
qINNHL
THAT

YONAS AST1Nd
dIYDAUNVH

I-COOLTSO-M

TaIM
WALSAS

SUOI]DDUUOZD JJIM PLO JI9¥j.19]U] BJOSUOD OUL


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUDJ] aI1A1aS og

(SNIdZ)
Yanvads

S00¢9S0

NI oJanv pieog Jayijduiy

(SNIdZ)
Ywayvads

SUOI]JDBUUOND JJIM Pieog JaIIdwy


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Driver Board Wire Connections

AC POWER
TRANSFORMER
| A
POWER
SWITCH
¥
>[no] [s |] C13]
FUSE .
CS62004-00L ; TENSION
+— RED — 7 MOTOR
INCLINE MOTOR| «— WHITE —
«— BLACK +—{ Down]
18 | [su |
5 A .
INCLINE MOTOR RPM
— SYSTEM CABLE a

31 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Driver Board PCB Component Locations

| DANGER ~ : £UU
| HIGH | REVI: 2a
/VOLTAGE om

CoreStar Co

‘ee

a VavuU 94V-0 ‘ = Re Tyee |

32 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 34 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUD|T ad1AIaS -

c+ = OAAPE OAPD PD

wrt cu

LOH OV

NMOd YOLOW

Seg ie dN YOLOW | oe | a -

ANMION! YE \caoe 7 E
Noes ANITONI . = — a. Yowrt0a |
', —— is |
JONVE |

th . = : q - = . ~ =
ae —F B ee] 4 IC ; ~~ ‘e

pomeramey .

SUOI}E907J JOJEDIPU] G31 pueog JAG


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Driver Board function

AC POWER TRANSFORMER TRANSFORMER
INPUT AC POWER INPUT AC POWER OUTPUT

#

: : : WRI ip Compliant :
| : — el as a * y
AC POWER marsh. a Sin < (eae "
Og am —— timoc "heel fens | & Ll o> =
INPUT “ # : —~ ares |e . | « -
E : | REV1:2 ee ww ° EA oa | @ Pea |
_ HIGH na — ine -2(m | i
| VOLTAG : , = J : CoreStar Co-, tta— fo 3 UN | > 12]
ma | Fi -_ " -- @ face " o3 | a = tb
2 ' =) " | a |

> TENSION
MOTOR

INCLINE
MOTOR
UP

INCLINE .
MOTOR |i F %
COM |

an et 0

a U4VU 94V-0 Pes YRS Tie |

INCLINE INCLINE
SYSTEM
MOTOR MOTOR
WIRE

DOWN VR Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
[/DNUD 201A1a 9¢

GN9'S
YA'v
AS+°€
We

+L
TOYLNOO
NIV

UONDUN] UONIUAP 10}99UU0D JOO UOISUADL


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

SsuOHonijsu] Ajafes JONPOld “2


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
/DNUD|T GdIAda

bHunooysajqnoll
/ sabessajj JO1F T0-2Z054S-S685X ‘8


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Error Message : --

@ Definition : When you press the Level Up or Down key,the motor does not move.” --” appears on the display.
@ Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | upnown KEYS

LEVEL Zz LEVEL.
COUNT Lins UP/DOWN
SIGNAL = SIGNAL

MOTOR VOLTAGE
(CWICCW) TENSION
MOTOR
DRIVER BOARD < WR

42 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-2 Error Message : E2

@ Definition : The console board is not detecting the VR voltage value,or the voltage value has exceeded the range.”E3” appears on the display.
@ Configuration :

DISPLAY BOARD

VAN

INCLINE
VR
VOLTAGE
INCLINE
MOTOR
DRIVER BOARD Koa VR VOLTAGE INCLINE VR SET

C) INCLINE DOWN LED
OC) INCLINE UP LED

45 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Case of RAMP ERROR
m Stride VR value exceeds the range. E3 appears on the display.
@ Stride motor isn’t operation up or down,making the VR value exceed the range.
@ After turning on the unit,the display board detects that the stride VR voltage exceeds the range,so E3 appears.

@ Action Flow Chart
C INCLINE VR +)

Ee

y
|
DRIVER BOARD

a

a

+
|

DISPLAY BOARD

Kan

¥

| ¥
DISPLAY OPERATES ERR APPEARS ON
NORMALLY THE DISPLAY

46 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test configuration. The console to driver board connector pin define function

fy ROS ee etic Se xr onaettenettrel Aaa iy a se hata

st )(1)]
ca7)r63
On . sm
Sie E isle

bal "mea The console to driver board

Be connector pin define : oot oe

@5 Ris oF AIS a eat Fajcis
ene function: cae Org; Tae a
cy = wa) oe a Bae ns = ae

as.
wis

2 The console to driver board
connector pin define
function:

1. MTR-

2. MTR+
3. +5V

. MPOS
. GND
. RPM1
. GND
. RPM2
. GND
10. +12V
11.GND
12. INC+
13. INC-
14. IPOS

48 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
i

_ HIGH

Configuration.Stride motor control function relate parts location

Ji0

“eo oer

<

e

> -¢

OLTAG

~ eS
Ue
poe eee

rae | :
r 8 =
t

J4

J

INCLINE MOTOR
UP LED

INCLINE MOTOR
DOWN LED

» 21

Compliant

| > ww, ort fs foe VSS | BRE

The position sensor wires

1. MTR-

1.Red = Ground,
; ee 2. MTR+

2.White = Position signal,

3. +5V
3.Black = 5vdc,
(0-5v depend acl tion) 4. MPOS

~5v depending on incline position
5. GND

|

14,13,12,11,1 7 4,3,2
J 3, J J 0,9,8, ,6,9, 9,

49

. MTR- \
2. MTR+

3. +5V
4. MPOS
5. GND
6. RPM1
7. GND
8. RPM2
9. GND

10. +12V
11.GND
12. INC+

13. INC-
14. IPOS )

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-3 Error Message : E3

Definition : During stride action,the display board CPU cannot read the VR value,so E3 appears.
Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | upmowNn keys

As

INCLINE INCLINE
VR UP/DOWN
VOLTAGE SIGNAL

\Z

INCLINE
MOTOR
DRIVER BOARD ex VR VOLTAGE INCLINE VR SET

OC) INCLINE DOWN LED
OC) INCLINE UP LED

51 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of E3

m Press the stride UP/DOWN key.The stride doesn’t operate. E3 appears on the display.
@ Explanation
@ Press the stride UP and DOWN key.The driver board UP or DOWN indicator lights. The stride operates, moving the VR,which changes
the VR value.
@ The display board CPU reads the stride VR value.lf there is no VR value change,to the CPU,the stride is not operating when it should
be. E3 appears on the display.
@ Action Flow Chart

C DISPLAY BOARD +)

DRIVER BOARD

DURING UP ACTION,

IN DOWN ACTTICNN
DOWN LED LIGHTS.INCLINE
VOL TAGE DECREASES

_N——_————

INCLINE MOTOR

Nt

DOWN LED LIGHTS,
INCLINE LOWERS?

¥

¥

|
seas 2 SHOW INCLINE E35
C NO ERR MESSAGE > C MESSAGE »

52 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 54 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Of 8 s

oI
“aT Sl
mn it
ni ="
= o) =


=== OCR SUPPLEMENT, PDF PAGE 56 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-6 Fuse replacement

FUSE 5A

SS

- SN os
~ ~ ‘ SRB .
ak ans.
‘ek: = FN
a a =
RARE A E

If your elliptical loses power or will not start, check the fuse located on the motor controller.
DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric shock
Remove FUSE holder.

Remove and replace the fuse on the holder

56 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8-7 Troubleshooting procedure matrix

Condition Reason Solve
LCDs not bright, incomplete or imperfect. 1. LCD light is broken. 1. Replace with new LCD or console.
2. Power to console too low. 2. Check AC power is 110-120V.

3. Check power to console.
4.Replace lower controller.

LCD displays not bright, incomplete or imperfect. |1. LCD displays are broken. 1. Replace with new console.
The stride position doesn’t match console 1 Console is not calibrated. 1 Calibrate the console.
i i “EQ” iti i ig |1 Turn off the AC switch and turn on power again.
STRIDE ERR ,STRIDE window displays “E3”. were. sensor value of stride motor is > Calibrate the monitor. p g
Erratic pulse display. 1. Another chest belt in use around 1. Check for other chest belt use around elliptical.
Ellipitcal. 2. Change the position or direction of elliptical.

2. Other magnetic field disturbance. 3. Replace with new receiver.

3. Receiver is broken.
UP/DOWN button of 1 The connector of STRIDE CABLE 71 Connect the wires again.

STRIDE ADJUSTMENT SWITCH can’t be used. and CONSOLE not connected properly.
2. The connector of STRIDE CABLE 2. Connect the wires again.

and STRIDE ADJUSTMENT SWITCH

Stride button just can press UP, can’t press WI/CABLE not connected properly.
DOWN.
f : , 3. Replace the cable.
age button just can press DOWN, can't press {4 Th, connector of STRIDE CABLE or
STRIDE ADJUSTMENT SWITCH CABLE
got damage. 4. Replace buttons.
4. Button of STRIDE ADJUSTMENT
SWITCH is broken. 5. Replace the cable.

5. The connector of STRIDE CABLE or

STRIDE ADJUSTMENT SWITCH CABLE 6. Replace the cable.
got damage.

6. The connector of STRIDE CABLE or

STRIDE ADJUSTMENT SWITCH CABLE

damaged.
Hand pulse lost its function. 1. Hands not on the hand pulse sensors /|1. Two hands hold the hand pulse.
(No pulse displayed on monitor) or only one hand on sensor.

2. The connector of HANDPULSE 2. Connect the cable again.

W/WIRE and Console not connected

37 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 65 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9-5 Flywheel & Poly-V Belt Problem

1. There are two kinds of problems caused of flywheel as general. One is adjusted resistance doesn’t work, another is
noise problem. When the user uses the console to adjust the resistance, but it doesn’t work and the gear motor is
working. Check the steel cable if it works with the flywheel or it is loose.

a

2. Check the flywheel, @330 Drive Pulley and Idler Wheel Assembly if they are rubbed while the flywheel is spinning and
causing the noise problem, and then disassemble the steps of flywheel and reset. If it is caused the noise problem of
flywheel by itself, we suggest have a new replacement directly.

3. Ifthe Poly-V Belt is slipping, simply adjust the cap the on hook-type screw with the #13 wrench to adjust. Refer to the
disassembly rm ut oo

4. lf the Poly-V Belt worn or damaged, replace with new part.

65 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 68 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
10-2 Slip Problem
1. The ja Socket Head Cap, Bolt 3/8 "x2-1/4 on top and nyloc nut 3/8" x11T must be tightened securely.

\
» Agee

Ny GC ed el
: \* "il il ‘ |
be — |

2. Belt: This issue appears quite often, because after a period of time, most belts will become loose from use
depending on usage time. Solution will depend on weight and adjustment methods, refer to belt disassembly
procedures for rae

WOO |

68 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 69 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
10-3 Play

1. Shaking is mainly due to loose screws, so check and tighten loose screws first. Check connection points to see if gaps have been
created after prolong use causing wear and tear or improper assembly. For example, shaking of the foot pedal is caused by loose
Carriage Bolts, from improper assembly.

i Ae 2 oj8 7 ae i ez i p~
& ii? _ oe . ——— a a j ———_
rs 4 att —— _ é — i ————
“ { } oF _ . @ }- Cone ' = -
Se ee [ ai ~ =

10-4 Smooth Problem

1. Check for loose screws if machine motion feels unsmooth. Check if there are foreign object on or around the sliding
rail, use an alcohol wipe to remove and re-lubricate with lubricant.

\> << ES Sy
jJ tE- iC

69 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 77 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7. Remove the 5 x 19L_ Tapping Screw on Side Case Rear Shroud of main frame by using the Phillips Head Screw

Driver.
4 [SS Tee |
if = 4 : | A ED 2 nn
Pp . 0 SA | i\e Nal} Ih { oR
4 ee” “wr 7 — _— ies =
i" ~~ a! fle =

Sig |, Se (*
——~ 5, — pe. ‘

8. According to above instructed steps and reassemble again. Do not clip the cables, Side Caser(R)&(L), the connection
of Side Case Rear Shroud and lock the screws.

77 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 84 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6. Remove the three pieces of 5/16" x 1/2" Hex Head Bolt from the Pedal Arm (L) & (R) of Aluminum Track by using
M5_LAllen Wrench.

eS
S —

& Es ee SSS

8. According to above steps to assemble again.
9. Line up the Pedal Axle with surface of breach of Fixing Plate and lock with the screw.

ae
———
a ge —
: SS — 2
— —— ¢
— > “=i
= — A Si
ee > Te
a ee C
ee lj) =
—— et —
—

84 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 95 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11-7. Incline Motor ,Controller & Gear Motor
1. According to instructions of slider adjustment to remove slider adjustment, and use Allen wrench M6 to release Socket
head cap bolt (M8 x 40L) which secure fixing piece on the main frame

St A eal
‘ | AS ) > ¥ ty \
| pa

| ; = }

| | ee 8) pHY

2s

|

|

|
2. Plug in the power supply before remove Incline Motor, use console to adjust program to 21”(as shown in Figure 2), if
need to remove Gear Motor then adjust resistance control to max.(level 20) and cut off the power.

y Soi \
iP : a eager ) f at |
Pe J J |
~. 2 j . |
: ei, vee
1 Wen \

95 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 102 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. ae 13mm wrench to release nylon nut(M8x7T) fixed at idler wheel assembly on main frame.

/ Kir %
1 AX
?

“1. es
nch to release adjust screw, nylon nut(M8x9T), rod end sleeve, flat washer (5/16”x23x1.5T) fixed on

idler wheel assembly -

| * ,
4. Pull out the drive belt from drive pulley.

102 Service Manual
