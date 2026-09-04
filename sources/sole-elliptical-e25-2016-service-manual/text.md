  SE565S-SE016
      Elliptical
Service Manual
-------------------------------------------Table of Contents-------------------------------------------
      1. SE565S Elliptical Outlines
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
      8.2 Error Message: E2
      8.3 Error Message: E3
      8.4 Circuit Diagram
      8.5 Calibration Procedure
      8.6 Fuse Replacement
      8.7 Troubleshooting Procedure Matrix for Electronic Issues
      9. Troubleshooting
      9.1 Console Problem
      9.2 Side Case & Round Disk Problem
      9.3 Flywheel Problem
      9.4 Poly-V Belt Problem
                                                         2                                  Service Manual
9.5 Swing Arm Problem
9.6 Bushing Housing Problem
9.7 Controller & Incline Motor & Slide Wheel Problem
9.8 Tension Motor Problem
10. Q & A
10.1 Noise
10.2 Slip Problem
10.3 Shaking Problem
10.4 Smooth Problem
11. Disassembling and Assembling of Parts
11.1 Console Replacement
11.2 Swing Arm Replacement
11.3 Connecting Arm Replacement
11.4 Side Case Replacement
11.5 Cross Bar Replacement
11.6 Poly-V Belt Replacement
11.7 Idler Wheel Replacement
11.8 Flywheel Replacement
11.9 Bushing Housing Replacement
11.10 Slide Wheel Replacement
11.11 Incline Motor Replacement




                                                       3   Service Manual
1. SE565S-SE016 Outlines




           4               Service Manual
                                                           Console




                                                           Console Chin Cover (Rear)


                                                           Handle Bar Cover

                                                           Console Mast Cover
                                 Pedal Arm Cover (L)

                                        Round Disk

                        Side Case (L)                      Round Disk Cover


              Pedal                                           Connecting Arm Cover(R)




       Incline Cover                                          Pedal Arm Cover (R)

Inclinable Rail Cover
     Rear Bar Cover                                            Middle Stabilizer Cover


                                                               Incline Bottom Cover



                                                            Slide Wheel Cover

                                                       5                               Service Manual
                            Swing Arm (L)


                            Console Mast
                                                    Console Holder Assembly

                             Pedal Arm(L)
                                                    Swing Arm (R)


                                                    Main Frame

                           Connecting Arm (L)


                                                    Drive Pulley




                                                    Bushing Housing, Pedal Arm

                                                    Cross Bar
 Rear Rail Assembly

                                                    Wheel Assembly

                                                    Flywheel
Inclinable Rail Assembly
                                                    Connecting Arm (R)

       Incline Motor
                                                    Pedal Arm(R)



                                                6                         Service Manual
2. Electronic Parts




         7            Service Manual
2.1 Upper Controllers
                            Speaker
              Cooling FAN




                                      THUMB SWITCH

             DISPLAY




                                  8                  Service Manual
2.2 Lower Controller and Driver




                                      TENSION MOTOR
    SPEED SENSOR




     MOTOR CONTROLLER
                                      INCLINE MOTOR




                                  9           Service Manual
3. Electrical Configurations




             10                Service Manual
CONSOLE:
 Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console、incline driver and tension motor driver, link the console to output appropriate voltages
 for tension motor that control the elliptical functions.

TENSION MOTOR:
 It can change to increase or decrease resistance level of brake.

INCLINE MOTOR:
 This is an ac motor. User can to control variable elevation by console within main controller.

GENERAL INFORMATION

CONSOLE
Contains Key controls and LCD Display.
Main controller Include power supply 、 motor driver control circuit and incline control circuit.




                                                                        11                                                           Service Manual
TENSION MOTOR
   Work voltage: DC 4.5~7.5V
   Control resistance increases and decreases.

INCLINE MOTOR
This is a 115 volt AC motor.

Have four wires, red, black, white and green.

Has one 3 pins cable of position sensor.

If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.

If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.

The White wire (COM) is neutral.
The green wire is ground.




                                                                         12                    Service Manual
4. SE565S-SE016 Product Operation




                13              Service Manual
Display Windows


                       6.5” LCD Display




                  14                 Service Manual
LCD Layout



    15       Service Manual
Operation
Window Display Mode
  IDLE MODE
  1.1 Each program profile will be displayed on the MESSAGE WINDOW sequentially. And recycle display at the same time.


  DISPLAY MODE
  2.1 Pre-set: DISPLAY ON (DISABLE). You could set the DISPLAY ON/OFF by ENGINEERING MODE.
  2.2 The console will not get into SLEEP MODE when the set up is “ON”, unless turn off the power. There is no RPM input in IDEL MODE, and enter
      to SLEEP MODE after thirty minutes without pressing any key.
  2.3 In DISPLAY MODE, LCD screen will has no display, and backlit will be off. Press any key to wake up the system, and back into IDEL MODE.
  2.4 Resistance in SLEEP MODE: Incline =1, FAN system OFF.


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


  PAUSE MODE
  5.1 Press “STOP” key enter to PAUSE MODE, and exercise parameters will be recorded. Message window will display “PAUSE”, and upper window
      will display the recorded exercise parameter.
  5.2 In PAUSE MODE, DW will show” PAUSE”
  5.3 It will enter to IDLE MODE after waiting by five minutes without pressing any key in PAUSE MODE.
                                                                       16                                                       Service Manual
5.4 The ramp incline level should back to “1” when the resistance level is “1”. The position of tension motor and ramp incline should back to the preset
    level before it pause when press “START” key.


END MODE
6.1 The message window will display “WORKOUT SUMMARY” after end workout.
6.2 END MODE workout information
    6.2.1 在 Display exercise data in message window each three seconds display
6.3 When the time counting is end, and END MODE display is finished without pressing any key in 3 minutes.The system will enter IDLE MODE.


RESET MODE
7.1 In IDLE MODE, press STOP key for more than three seconds will enter to RESET MODE and reset the system.( If the system is in
    CONSOLE LOCK MODE you have to quit CONSOLE LOCK MODE first, and you can execute the RESET MODE.)


7.2 The message window will finished the reset and show RESET 2 seconds. After that, the system is in IDLE MODE.




                                                                         17                                                            Service Manual
Function

   SPEED
        Display the current speed in mile per hour.
        DISPLAY range is 0.0 to 99.9
        WORK range is 0.0~99.9
   Incline
        Display the incline position from 1 to 20
        DISPLAY range is 0 to 99.
        WORK range is 0 to 20.
        INCLINE preset value is 0 to 20.
        Press “UP” or ”DOWN” to adjust incline, each increment and decrement is 1.
   LEVEL
        Display the incline position from 1 to 20
        DISPLAY range is 0 to 99.
        WORK range is 0 to 20.
        LEVEL preset value is 0 to 20.
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



                                                                        18                                                        Service Manual
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
                                                     Fan Key
                                              Cooling fan switch on or
                                                         off

               DISPLAY




          CONTROL KEYS




                                         20                              Service Manual
Function Button In Main Mode
READY MODE
  STOP button: Non-function.
  START button: Pressing “ START ” button to start Ellipitcal, When pressing “START” button, there will be 3 second final count down on window
  display, then machine starts running. In MANUAL, Ellipitcal starts at MIN LEVEL .
  LEVEL UP button: If user doesn’t enter a setting then this button is non-functional.
  LEVEL DOWN button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE UP button: If user doesn’t enter a setting then this button is non- functional.
  INCLINE DOWN button: If user doesn’t enter a setting then this button is non- functional.
  FAN button: It can to control ON/OFF for the fan.
  DISPLAY KEY：
  Select program P0~P5，U1~U2，Pressing DISPLAY key change LEVEL and INCLINE’s profile drawing.

  ENTER KEY：
  Press ENTER key enter to parameter setting, and confirm the every setting by pressing START key no pressing ENTER key..
  Pressing ENTER key confirm the every setting or modify parameter use.
  In workout mode,pressing ENTER key can modify DM display. The preset is LEVEL PROFILE, pressing ENTER key change
  display :LEVEL PROFILE →INCLINE PROFILE→SCAN(SCAN MODE every 3 seconds will change display :LEVEL PROFILE →INCLINE
  PROFILE→LEVEL PROFILE)




                                                                   21                                                          Service Manual
RUN MODE
  STOP button: press “STOP” button to stop Ellipitcal.
  START button: non-functional.
  ENTER button: non-functional.
  LEVEL UP button: Press the button to increase your level and each increase is 1.
  LEVEL DOWN button: Press the button to decrease your level and each decrease is 1.
  INCLINE UP button: Press the button to raise position and each increase is 1, the maximum incline position is 20.
  INCLINE DOWN button: Press the button to lower position and each decrease is 1, the minimum incline position is 1.
  Fan button: It can to control ON/OFF for the fan.
  DISPLAY KEY：
  Press DISPLAY key to switch the exercise data when you are workout. If the display information is the latest data , press DISPLAY key the
  message window will change to auto display every four seconds. The information as below,

      1.   『LAPS XX』
      2.   『SPEED XX.XMPH』
      3.   『RPM XXX』
      4.   『LEVEL XX』
      5.   『WATTS XXX』
      6.   『SEG TIME X：XX』




                                                                    22                                                          Service Manual
5. SE565S-SE016 Unit Block Diagrams




                 23              Service Manual
Elliptical Configuration




                           24   Service Manual
6. SE565S-SE016 Basic Connections and Wiring




                     25                Service Manual
6.1 Display Board wire Connections




                                     26   Service Manual
6.2 Display Board PCB Component Locations

 PCB Board Top




                                            27   Service Manual
PCB Board Bottom




                   28   Service Manual
6.3 The console Interface Board wire Connections




                                             29    Service Manual
6.4 Amplifier Board wire Connections




                                       30   Service Manual
6.5 Driver Board Wire Connections




                                    31   Service Manual
6.6 Driver Board PCB Component Locations




                                           32   Service Manual
6.7 Driver Board LED Indicator Locations




                                                   POWER



                                                INCLINE
                                                MOTOR DOWN



                                                INCLINE
                                                MOTOR UP




                                           33                Service Manual
 6.8 Controller Indicator LED debugging

Indicator           Function                     Condition                              Reason                         Solve
   LED
D5        Controller power          If DC voltage is normal, it would be    Voltage is not correct.   Check the supply voltage is 110~120V.
POWER                               always ON. If off, fault condition      Fuse is blown.            Replace Fuse.
                                    exists.                                 Transformer is no good.   Replace controller.
D2        Motion of incline motor   Motion of incline motor is up.          Transistor was broken.    Replace controller.
                                                                            Relay failed.
D4        Motion of incline motor   Motion of incline motor is down.        Transistor was broken.    Replace controller.
                                                                            Relay failed




                                                                       34                                                      Service Manual
6.9 Driver Board function
                          TRANSFORMER      TRANSFORMER
                          AC POWER INPUT   AC POWER OUTPUT
 AC POWER
 INPUT




 AC POWER
 INPUT


                                                             RPM
                                                             SENSOR

INCLINE
MOTOR UP
                                                                      TENSION
                                                                      MOTOR
INCLINE
MOTOR COM


                                                                      SYSTEM
                                                                      WIRE
             INCLINE                            INCLINE
             MOTOR DOWN                         VR




                                                 35                   Service Manual
6.10 Tension Motor connector definition function




       STEEL ROPE




      MAIN
      CONTROL
      1.M+                        5
      2.M-                        4
      3.+5V                       3
      4.VR                        2
      5.GND                       1




                                              36   Service Manual
7.   Product Safety Instructions




                37                 Service Manual
7.1 Important Safety Instructions
  - To reduce the risk of electric shock disconnect your Ellipitcal from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the Ellipitcal on a flat level surface with access to a 115-volt, 15-amp
    grounded outlet with only the Ellipitcal plugged into the circuit.
  - Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the grounded plug by using
    improper adapters or in any way modify the cord outlet.

7.2 Important Electrical Instructions
  - Never use a ground fault circuit interrupt (GFCI) wall outlet with this Ellipitcal. As with any ap- pliance with a large motor, the GFCI will trip often. Route
    the power cord away from any moving part of the Ellipitcal including the elevation mechanism and transport wheels..
  - Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a Ellipitcal is first turned on or even
    during use. If your Ellipitcal is tripping the house circuit breaker (even though it is the proper current rating) but the circuit breaker on the Ellipitcal itself
    does not trip, you will need to replace the home breaker with a high inrush type. This is not a warranty defect. This is a condition we as a manufacture
    have no ability to control. This part is available through most electrical supply stores. Examples:Grainger part # 1D237, or available online at
    www.squared.com part # QO120HM.

7.3 Important Grounding Instructions
  - This product must be grounded. If the Ellipitcal should malfunction or breakdown, ground- ing provides a path of least resistance for electric current,
    reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
    appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
  serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
  outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 230-volt circuit, and has a grounding plug that looks
  like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
  as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
  can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must be connected to a permanent ground
  such as a properly grounded outlet box cover.                                                                                                    Whenever the
  adapter is used, it must be held in place by a                                                                                                   metal screw.




                                                                                 38                                                                 Service Manual
8. SE565S-SE016 Error Messages /
        Troubleshooting




               39              Service Manual
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
8.1 Error Message：E1
 Definition: All screens are off, and outputs are stop when EEPROM damaged or malfunction.   Display message will show “E-1”
 Troubleshooting: Replace upper controller.




                                                             41                                                 Service Manual
8.2 Error Message ：E2
   Definition：When you press the Level Up or Down key, the motor does not move.” E2” appears on the display.
   Configuration：




                                                                        42                                      Service Manual
 Tension Motor Operation
                              Part            Description

                                              Key signal travels to the display. The main program IC then
                              Display
                                              sends a command signal to the drive board.

                                              Drive board receives the signal and responds by putting out
                              Drive Board
                                              power to the motor. Level UP:+5VDC;Level DOWN:-5VDC


 Tension Motor Troubleshooting

                              Part            Description
                                              If the key beeps when pressed, assume that the signal was
                              Display
                                              sent.
                              Data cable      Inspect the cable and connections.
                                              Inspect drive board power output to the motor. Press the
                                              Level Up is +5VDC;Level DOWN is -5VDC.If there is power
                              Drive Board     to the motor, but the motor does not operate, replace it. If
                                              there is no power output ,inspect whether the drive board has
                                              power.


 Tension Motor Voltage Test Procedure
  1. Put multi-meter to the 20VDC setting. Place probes on the motor control wire(Red probe in brown wire, Black probe in black
     wire) on the drive board.
  2. Turn on unit power. The display lights up.
  3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates. Resistance increases.
  4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates. Resistance decreases.
  5. If there is no voltage, inspect power socket the holder FUSE. If broke replace it.
  6. Inspect the drive board POWER LED whether lit. If no lit the drive board is bad. Replace it.
                                                                  43                                             Service Manual
Place probes on the motor control wire(Red probe in brown wire, Black probe in black wire) on the drive board.

                                                    44                                                  Service Manual
8.3 Error Message：E3
   Definition：The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.” RAMP ERROR” appears on the
    display.
   Configuration：




                                                                       45                                                         Service Manual
   Case of RAMP ERROR
     Incline VR value exceeds the range. E3 appears on the display.
        Incline motor isn’t operation up or down, making the VR value exceed the range.
        After turning on the unit, the display board detects that the incline VR voltage exceeds the range,so E3 appears.
        Action Flow Chart




                                                                       46                                                    Service Manual
 Troubleshooting
            Part            Troubleshooting
                            1.Reconnect VR wires.
            Incline VR
                            2.Inspect whether the incline wires are broken or disconnected.
                            1.Inspect the incline wire and 14-pin cable connections.
            Display board
                            2.Test whether the VR voltage varies at the incline wire terminal.
                            1.Inspect the wire connections.
            14-pin cable    2.Inspect whether wires are broken or crimped.
                            3.Replace the wires and test again.
            Driver board    Inspect the display board 14-pin connections.




                                                       47                                        Service Manual
 Test configuration. The console to driver board connector pin define function




                                The console to driver board
                                connector pin define
                                function:
                                1.SPEED
                                2.GND
                                3.VCC+5V
                                4.VR
                                5.GND
                                6.M-
                                7.M+
  11
                                8.VIN
  10
                                9.INC+
  9
                                10.INC -
  8
  7
  6
  5
  4
  3
  2
  1


                                                         48                       Service Manual
   Test Configuration. Incline motor control function relate parts location

                                                                  INCLINE MOTOR                 INCLINE MOTOR
                                                                      UP LED                      DOWN LED



                                                                                                                1. M-
                        The position sensor wires
                                                                                                                2. M+
                        1.Red = Ground,
                                                                                                                3. +5V
                        2.White = Position signal,
                                                                                                                4. VR
                        3.Black = 5vdc,
                                                                                                                5. GND
                        (0~5v depending on incline position)
                                                                       1. SPEED
                                                                       2. GND
    RED-UP
                                                                                                                1.M-
                                                                                        1,2      5,4,3,2,1
                                                                                                                2.M+
                                                                                                                3.+5Vcc
                                                                                                                4.VR
White-NEUTRAL
                                                                                                                5.GND
                                                                                                                6.SPEED
                                                                                                                7.GND
    BLACK-DOWN
                                                               3,2,1          14,13,12,11,10,9,8,7,6,5,4,3,2    8.NA
                                                                                                                9. NA
                                                                                                                10.VIN
                                                                                                                11.GND
                                                                                                                12.INC+
                                                                                                                13.INC-
                                                                                                                14.INC VR

                                                                         49                                                 Service Manual
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




                                                                                     50                                                                         Service Manual
Error Message：E3
 Definition：During incline action, the display board CPU cannot read the VR value, so E3 appears.
 Configuration：




                                                                      51                            Service Manual
Cause of E3
      Press the incline UP/DOWN key. The incline doesn’t operate. E3 appears on the display.
           Explanation
             Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline operates, moving the VR, which
                 changes the VR value.
             The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is not operating when it
                 should be. E3 appears on the display.
           Action Flow Chart




                                                                         52                                                         Service Manual
Troubleshooting
            Part            Troubleshooting
                            1.Press incline UP key. The driver board UP LED lights.
            Display board   2.Press incline DOWN key. The driver board DOWN LED lights.
                            3.If not as above, inspect the cable and connections.
                            1.Inspect whether the 14-PIN cable is connected well.
            14-pin cable
                            2.Test by replacing the cable with a good one.
                            Inspect whether the driver board UP/DOWN LED is lit.
                            1.Press incline UP or DOWN key again, making the incline motor return to its
            Driver board
                            position.
                            2.If E3 still appears, re-calibrate the incline set.
                            1.Inspect whether the incline motor is stuck.
                            2.Inspect whether the incline gears are cracked.
            Incline motor
                            3.Test whether the incline motor has a broken circuit.
                            4.Re-calibrate the incline set.




                                                      53                                                   Service Manual
8.4 Circuit Diagram

                      SE565S-SE016
               ELLIPICAL CIRCUIT DIAGRAM




                           54              Service Manual
8.5 CALIBRATION PROCEDURE

   Incline Calibration:
   If there is a problem with the incline, try running the calibration. Press the Incline ▲ key and the Start
   key at the same time. Hold them down for 5 seconds and the Incline calibration will start and run
   automatically. If the problem persists contact service department.



MAINTENANCE MENU IN CONSOLE SOFTWARE

   The console has built in maintenance/diagnostic software. The software will allow you to change the
   console settings from English to Metric and turn off the beeping of the speaker when a key is pressed for
   example. To enter the Maintenance Menu (may be called Engineering Mode, depending on version)
   press and hold down the Start, Stop and Enter keys keep holding the keys down for about 5 seconds
   and the Message Window will display “Engineering Mode”. Press the Enter button to access the menu
   below. Press the Level ▲/▼ keys to navigate the menu.
     A. Key Test - Will allow you to test all the keys to make sure they are functioning
     B. Display Test - Automatically tests all LCD’s
     C. Functions - Press Enter to access settings, use Level ▲/▼ keys to scroll
          I.      ODO Reset - Resets the odometer
          II.     Units - Choose from English (Imperial) or Metric display readings
          III.    Display Mode - Turn off to have the console power down automatically after 30 minutes of inactivity
          IV.     Motor Test - Continually runs the tensioning gear motor
          V.      Manual - Allows stepping of the gear motor
          VI.     Pause Mode-Turn on to allow 5 minutes of pause, turn off to have console pause indefinitely
          VII.    Key Tone - Turn on or off the beep sound when a key is pressed
     D. Security - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the
     child lock is enabled, the console will not allow the keypad to operate unless you press and hold the Start and
         Enter buttons for 3 seconds to unlock the console.
     E. Factory Set
     F. Exit - Select to exit Maintenance Menu




                                                       55                                         Service Manual
  8.6 Fuse replacement




          FUSE 5A




If your elliptical loses power or will not start, check the fuse located on the motor controller.
DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric shock
Remove FUSE holder.
Remove and replace the fuse on the holder




                                                                           56                         Service Manual
  8.7 Troubleshooting procedure matrix
                    Condition                                      Reason                                        Solve
LCDs not bright, incomplete or imperfect.        1. LCD light is broken.               1. Replace with new LCD or console.
                                                 2. Power to console too low.          2. Check AC power is 110-120V.
                                                                                       3. Check power to console.
                                                                                       4.Replace lower controller.
LCD displays not bright, incomplete or imperfect. 1. LCD displays are broken.          1. Replace with new console.
The incline position doesn’t match console        1 Console is not calibrated.         1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “E3”. 1 Position sensor value of incline motor is 1 Turn off the AC switch and turn on power again.
                                                  wrong.                               2. Calibrate the monitor.
Erratic pulse display.                            1. Another chest belt in use around  1. Check for other chest belt use around elliptical.
                                                     Elliptical.                       2. Change the position or direction of elliptical.
                                                  2. Other magnetic field disturbance. 3. Replace with new receiver.
                                                  3. Receiver is broken.
UP/DOWN button of                                 1 The connector of INCLINE CABLE     1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used. and CONSOLE not connected properly.
                                                  2. The connector of INCLINE CABLE    2. Connect the wires again.
                                                  and INCLINE ADJUSTMENT SWITCH
Incline button just can press UP, can’t press     W/CABLE not connected properly.
DOWN.                                             3 The connector of INCLINE CABLE or 3. Replace the cable.
Incline button just can press DOWN, can’t press INCLINE ADJUSTMENT SWITCH
UP.                                               CABLE got damage.
                                                  4. Button of INCLINE ADJUSTMENT      4. Replace buttons.
                                                  SWITCH is broken.
                                                  5. The connector of INCLINE CABLE or 5. Replace the cable.
                                                  INCLINE ADJUSTMENT SWITCH
                                                                                       6. Replace the cable.
                                                  CABLE got damage.
                                                  6. The connector of INCLINE CABLE or
                                                  INCLINE ADJUSTMENT SWITCH
                                                  CABLE damaged.




Hand pulse lost its function.                    1. Hands not on the hand pulse sensors 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                     or only one hand on sensor.
                                                                         57                                                         Service Manual
                                          2. The connector of HANDPULSE            2. Connect the cable again.
                                             W/WIRE and Console not connected
                                             properly.                             3. Replace with new cable.
                                          3. The wires got damaged when
                                             connecting the HANDPULSE W/WIRE 4. Replace console or Hand pulse board.
                                             and Console.
                                          4. Hand pulse board is broken.
Wireless lost its function.               1. Chest belt not worn properly.         1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)           2. Distance is too far and exceeds range    oriented correctly.
                                          of receiver.                             2. User chest belt in front of console within 3 feet.
                                          3. Chest belt battery is weak or dead.   3. Replace with new lithium battery type is CR2032.
Chest belt too close to the Ellipitcal.   Weak battery.                            Replace with new lithium battery with type CR2032.




                                                                  58                                                          Service Manual
9. Troubleshooting




          59         Service Manual
9.1 Console Problem
1. Display: If there is no display, follow the following procedures for diagnosis.
2. Make sure Power is plug in properly and AC breaker is not activated




3. Make sure that all connectors, including cables for the console, and AC power, are connected properly. Disassemble the
   console to check cables inside it if necessary.
4. If all connections are fine then check to determine if cable breaks or console or lower controller fails.




                                                                  60                                       Service Manual
9.2 Side case & Round Disk Problem
5. The potential reason why there could be a problem here is due to the friction created causing abnormal sounds. However, to
   determine this, you will need to check to see if the large disk is not centered or offset.




6. If the disc is not centered causing friction, remove the left and right chain cover and reassemble. Refer to the assembly and
   disassembly procedures.
7. If the disc is offset causing friction, remove the left and right chain cover, use Phillips screwdriver and remove the 5x16mm
   Tapping Screw as well as the 1/4 "x19mm flat washer. Placed the round disk and the Cross Bar on a flat surface to check if
   either is deformed. If deformed, check to see if the deformity can be fixed manually. The deformity occurs mostly caused by
   external force and thus is why the product goes through a quite room test on the production line to ensure that the standards of
   +/-3mm are met before shipment.




                                                                61                                                  Service Manual
9.3 Flywheel Problem
1. This problem is very rare, most of the time the problem is caused by incorrect cable adjustments or improper assembly
   causing offset creating abnormal sounds. Please follow the magnetic flywheel and cable disassembly procedures to
   commence adjustments.




2. If there is abnormal sound coming from the magnetic flywheel, first check if are any foreign objects or friction, make
   adjustments. If adjustments are not able to be made, replace with new part.




                                                           62                                              Service Manual
9.4 Poly-V Belt Problem
1. If the Poly-V Belt falls off, first remove the right chain cover and Idler Wheel Plate, and then reinstall the Poly-V Belt. Once
   reinstalled, rotate at low speed to observe if the Drive Pulley or Poly-V Belt is offset or deformed. Check if the belt pulley is
   offset or if the belt, Drive Pulley, Magnetic flywheel are not aligned in a straight line. Lastly, rotate at high speed (100-200RPM)
   and test with abrupt stops to check for abnormalities. If everything is ok, restore to fully assemble.




2. If the three parts are not aligned in a straight line, adjust the magnetic flywheel to the proper place.   Adjustments are always
   made to product ensuring alignment before shipment from factory.




                                                                  63                                                    Service Manual
3. If the Poly-V Belt is slipping, simply adjust the cap the on hook-type screw with the #13 wrench to adjust. Refer to the
   disassembly procedures for adjustment.




4. If the Poly-V Belt worn or damaged, replace with new part.




                                                                64                                           Service Manual
9.5 Swing Arm Problem
1. To make assembly easier for consumers, there will be minor difference in size (0.05mm~0.07mm). Therefore, it is normal for
   a little shake/wobble to exist, but after prolonged use, small parts due to friction wear will generate noise. The solution is to
   add thick lubricant into the top of Swing Arm Axle.




2. If the noise is emitting from the bottom bracket, then the 6203 bearings needs to be replaced.




                                                                 65                                                  Service Manual
9.6 Bushing Housing Problem
1. The problem with Bushing Housing is rare. However, a few units might have noise problem as time lasts. Applying some
   grease on ψ25 x 111.5 L shaft on Cross Bar Assembly, may be helpful for solving this problem.




2. If the plastic Bushing has been worn out, replace it with a new one.




                                                                66                                       Service Manual
9.7 Controller & Incline Motor & Slide Wheel Problem
1. The elliptical uses linked structure design, thus if there is a problem in the link it will affect other parts of the structure. Therefore, every part of the
     elliptical structure is important, more importantly, asides from resolving and replacing problem parts, it is also important to lubricate frequently.   So
     it is advised during, maintenance or repairs to lubricate preventing potential problems in the future.




2. There are many things that may affect or create problems with the footing. The main issue is if the sliding wheel of the linked structure slides
     smoothly and parallel on top of the Inclinable Rail Assembly. In short, the main cause would be side Inclinable Rail Assembly and the Inclinable Rail
     Assembly are not parallel, side Inclinable Rail Assembly and the main frame bottom bracket rotating sleeve do not come together as 90 degrees.
3.   Check to see if left/Right connecting arm and left/right step is connected properly, if sliding wheel has the correct rotation degrees, slipping
     occurrences or bearing damages, unsecured connections causing noises.
4.   Generally maintenance should start from the sliding wheels, replacing the sliding wheels or adding lubrication to the top of the sliding wheel arcs.
     Check the main structure for abnormalities, abnormalities in parallel parts, make sure that the problem is with the parts and not assembly before
     replacing the parts.




                                                                              67                                                              Service Manual
9.8 Controller & Incline Motor Problem
1. When incline motor is not functioning, check all the wire for secure connection, check incline controller and power adaptor is damaged or broken.
    Replace damaged or broken parts.




                                                                         68                                                        Service Manual
10. Q & A




    69      Service Manual
10.1 Noise
(1) There are potentially many locations where noise can originate from, but it is not
easy to isolate the location specifically. In the front, the chain cover and the round disk,
EPE, round disk, sleeve, Cross Bar ‚ Belt and belt pulley, Idler Wheel Plate ‚ Swing Arm,
Swing Arm Axle, Flywheel, Steel Cable, Slide Wheel and Crank Arm during assembly
along with side Inclinable Rail Assemblys as well as pedals. The main reasons are
usually not enough lubrication, unsmooth rotations, and loose screws. Because the
product is designed based on linked designs, resolving noise issue will vary from
machine to machine depending on actual situation.




                                             70                              Service Manual
10.2 Slip Problem
(1) Slipping problems can be verified by the following steps.
     1-1 M12 x P1.75 Rod End Bearing : M12 Nut on top must be securely tightened with
     Pedal Bar Assembly, and Rod End Bearing needs to be vertical.




    1-2 Bushing Housing, Pedal Arm: the CAP Socket Head Cap Bolt 3/8 "x2-1/4 on top
    and nyloc nut 3/8" x11T must be tightened securely.

    1-3 Cross Bar : CAP Socket Head Cap Bolt M8x40m/m on top of the Cross Bar

(2) Belt: This issue appears quite often, because after a period of time, most belts will
    become loose from use depending on usage time. Solution will depend on weight
    and adjustment methods, refer to belt disassembly procedures for references.




                                            71                              Service Manual
10.3 Shaking Problem
(1) Shaking is mainly due to loose screws, so check and tighten loose screws first.
    Check connection points to see if gaps have been created after prolong use causing
    wear and tear or improper assembly. For example, shaking of the foot pedal is
    caused by loose Carriage Bolts, from improper assembly.




10.4 Smooth Problem
(1) Check for loose screws if machine motion feels unsmooth.
(2) Check if there are foreign object on or around the sliding rail, use an alcohol wipe to
     remove and re-lubricate with lubricant.




                                            72                              Service Manual
11. Disassembling and assembling of
               Parts




                 73             Service Manual
11.1 Console Replacement
1. Use Phillips head screw driver to remove the Phillips Head Screws M5x15mm (3pcs) securing the bottom cover (front and
   back) of the console as well as the Sheet Metal Screws 3.5x12mm (2pcs). Remove bottom console cover.




2. Use Phillips head screwdriver to remove Phillips Head Screws M5x10mm (4pcs) securing the console. Unfasten all connected
   wires and remove console.




3. Reassemble in the reverse order as disassembly (Be sure to not crush or damage wiring during process)
4. To remove both upper and lower console cover, remove the Sheet Metal Screws 3.5x12 that is securing the console. (Should
   only be done by a professional)


                                                             74                                               Service Manual
11.2 Connecting Arm Replacement
1. Use Phillips head screwdriver to the Phillips Head Screw Driver to remove swing arm joint cover B (left and right)




2. Use 12 and #13 open end wrenches to release Hex Head Bolt 5/16" x1-1/4", flat washer 5/16" x 20 x 1.5T and nut 5/16" x 9T
   which secure the Rod End Bearing.




                                                                75                                                 Service Manual
3. Use 12mm open end wrench to remove hex socket screw 5/16”x15mm and flat washer 5/16”x20. Pull out the pedal carriage
   bolts to remove the Pedal Bar Assembly




4. Use Phillips screwdriver to remove Phillips Head Screw M5x10mm securing the pedal and remove pedal.




                                                           76                                              Service Manual
11.3 Pedal Arm Replacement
1. First remove the Pedal Bar Assembly, then use Phillips head screwdriver to unscrew Pedal Arm Cover.




2. Use M8 hex wrench and #14wrench to remove Gap socket screw 3/8”x2-1/4”, two flat washer 3/8”x19x1.5T and nyloc nut
   3/8”x11T connecting the Inclinable Rail Assembly and rotating block, to remove Inclinable Rail Assembly.




                                                             77                                            Service Manual
3. Use #12 hex wrench to remove hex head bolt 5/16”x15mm and flat washer 5/16”x35x1.5T, to remove Bushing Housing, Pedal
   Arm.




4. Reassemble in the reverse order as disassembly




                                                           78                                             Service Manual
11.4 Side Case Replacement
1. Remove Swing Arm and Inclinable Rail Assembly.
2. Slightly press the Console Mast Cover to take it apart from Side Cases.




3. Use Phillips head screwdriver to release 7pcs of 4x19 self tapping screws and 3pcs of 5x16 x 3 tapping screws to take Right
   Side Case apart.




                                                              79                                                 Service Manual
4. To take the Left Side Case apart, release 4x15 self tapping screws with 1/4"x19 flat washers on the main frame and 3pcs of
   5x16 Tapping Screws. Then disconnect two red jumpers and white grounding (remember to mark for red jumpers) to release
   left Side Case.




5. To resume, connect the red jumpers and the grounding back on the AC Electronic Module.
6. Return Left Side Case (with one 5/16" x 23 x 1.5T flat washer on it) onto the main frame and use 4x15self tapping screw with
   1/4"x19 flat washer to hold it (not too tight temporarily) then tighten with 3pcs of 5x16 tapping screws (make sure Side Case
   matches with Round Disk). Tighten 4x15 self tapping screws.




7. Match both Side Cases with each other and use 7pcs of 4x19 self tapping screws and 3pcs of 5x16 tapping screws to secure
   them.
8. Reverse above procedures to resume Pedal Arm and Connecting Arm.

                                                               80                                                 Service Manual
11.5 Cross Bar Replacement
1. Follow procedures 11-2, 11-3 and 11-4 to take apart Connecting Arm, Pedal Arm and both Side Cases.
2. Take off the Round Disk Cover by using a tapering stick.




3. Remove elliptical side cover Round Disk Cover, use 12mm wrench to remove hex head bolt 5/16”x15mm, flat washer
   5/16”x35x1.5T securing the cross bar.Use #13 wrench and loosen the outer bolt M8x6.3T (steel lvl 10). Use #13 wrench and
   hex wrench (M6) to loosen the inner bolt and remove the cross bar.




                                                             81                                               Service Manual
4. Use Phillips head screwdriver to release 8pcs of 5x16 tapping screws with 1/4"x19flat washers to separate the Cross Bar from
   Round Disk Cover.




5. To resume, secure the Round Disk on the Cross Bar and return it on the Crank Axle, align the Cross Bar with square hole and
   put 7x7x25L Woodruff Key in the hole and tighten M8x40 socket head cap screw together with two M8x6.3T nuts until it
   reaches 500 Kg-cm. Return and tighten 5/16" x 15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer.




6. Follow above procedures to resume Connecting Arm, Pedal Arm, and both left and right Side Cases with Round Disk Cover.




                                                              82                                                 Service Manual
11.6 Poly-V Belt Replacement
1. Follow procedures 11-2, 11-3, 11-4 and 11-5 to take apart Connecting Arm, Pedal Arm, both Chain Covers and the Cross Bar.
2. Use 13 mm wrench to loosen M8 x 9T nut on M8x170mm J-bolt and on Idler Wheel, and another M8 x 7T nut and the Belt can
   thus be released.




3. To resume, return the Belt on the Drive Pulley and Flywheel then tighten M8 x 9T nut until the acoustic gauge reads 190 Hz
   (+/- 10 Hz) when it is played with finger, then tighten M8 x 7T nut.




4. Reassemble in the reverse order as disassembly



                                                              83                                                 Service Manual
11.7 Idler Wheel Replacement
1. Follow procedures 11-2, 11-3, 11-4, 11-5 and 6 to take apart Connecting Arm, Pedal Arm, both left and right Side Cases, Cross
   Bar and the Belt.
2. Use 13 mm wrench to loosen M8 x 9T nut on M8x170mm J-bolt together with 5/16" x 23 x 1.5T flat washer until J-bolt is
   released. Use the same wrench to release M8 x 20 carriage bolt, which secures Idler Wheel Assembly, together with 5/16" x
   20 x 1.5T flat washer and M8 x 7T nut to take Idler Wheel Assembly apart.




3. To resume, tighten M8x20 carriage bolt, 5/16" x 20 x 1.5T flat washer and M8 x7T nut to secure Idler Wheel Assembly (to be
   tighten after the belt has been adjusted) and return the J-bolt and other parts.




                                                               84                                                Service Manual
11.8 Flywheel Replacement
1. Follow procedures 11-2, 11-3, 11-4, 11-5, 11-6 and 11-7 to take apart Connecting Arm, Pedal Arm, both Side Covers, Cross Bar,
   the Belt and Idler Wheel Assembly.
2. Plug in the power and adjust the resistance to level 20 and release the steel cable.




3. Use #15 wrench to loosen nyloc nut 3/8”-UNF26x9T on flywheel and main-frame. Remove flywheel and belt.




4. To resume the Flywheel, return the Belt onto grooves on the Flywheel and return the Flywheel onto the mainframe.




                                                              85                                                 Service Manual
5. Tighten both 3/8" -UNF26 x 9T nutsReturn the steel cable onto the Flywheel (with 45 degree) and then return the Idler Wheel
   Assembly.




6. Turn the Drive Pulley and check if the belt is secured. Adjust both 3/8"-UNF26 x 4T nuts to position the belt in the middle on
   the Drive Pulley and then tighten all other screws. Adjust the Belt to a proper tension.




7. Follow procedures 11-7,11-6,11-5,11-4,11-3 and 11-2 to return other parts.




                                                                86                                                 Service Manual
11.9 Drive Pulley Replacement
1. Follow procedures 11-2 and11-3 to take apart Connecting Arm, Pedal Arm, left and right Side Cases, Cross Bar and the Belt.
2. Use 12 mm wrench to release 5/16" x 15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer and the Bushing Housing can be
   release.




3. To resume, be sure thatψ25 wave washer is returned onto the shaft then return the Bushing Housing onto the shaft and tighten
   with 5/16" x15m/m hex head bolt with 5/16" x 35 x 1.5T flat washer.




4. Follow procedures 11-3 ~ 11-4 and 11-2 ~ 11-5 to return Pedal Arm and Connecting Arm.




                                                              87                                                 Service Manual
11.10 Slide Wheel Replacement
1. To take the slide wheel apart, use Phillips head screw driver to release two Phillips head screws M5x15mm and take the slide
   wheel cover first.




2. Use circlip pliers to remove circlip Ø17 and remove sliding wheels




3. Reverse above steps to resume the pedal arm and return wavy washes Ø 17 back to left and right slide wheels.




                                                               88                                                Service Manual
11.11 Incline Motor Replacement
1. Remove chain covers.
2. Use Phillips head screwdriver to remove 3 Phillips Head Screws M5x15mm from Incline Cover, then remove parts.




3. Use two 14mm wrenches to remove hex head bolt 3/8”x2-1/2” together with flat washer 3/8"x19x1.5T, nyloc nut 3/8"x7T and
   two Nylon Washers Ø3/8'' x Ø35 x5T which secure Incline tube and Incline Motor.




4. Use two #14 Open End Combination Spanner Wrench to remove hex head bolt 3/8”x2-1/2”, flat washer 3/8"x19x1.5T and
   nyloc nut M10 x 8T from outer Rail Tube and Incline adjustable assembly. Remove inclined adjustable assembly.

                                                             89                                               Service Manual
5. Use Phillips head screwdriver to remove tapping screw 5x16 from incline motor grounding wire. Cut the wire and remove
   incline motor.




6. Use 12mm wrench to remove from Rail Assembly hex head bolt 5/16"x1, flat washer 5/16"x 35x2T and pull out locking tube
   assembly and remove rail assembly.




                                                             90                                                Service Manual
7. If removal of aluminum rail is needed, remove Phillips head screws M5x15mm from aluminum rail to proceed.




8. Reassemble in the reverse order as disassembly.




                                                             91                                                Service Manual
