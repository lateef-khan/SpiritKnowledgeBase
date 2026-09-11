<!-- Source: TRX3500 4500 (GT90CD - NT023 NT024) Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

 GT90C-NT023
 GT90D-NT024
Treadmill Service
    Manual
-------------------------------------------Table of Contents-------------------------------------------
                       1. GT90C/D Treadmill Outlines
                       2. Electronic Parts
                            2.1 Upper Controllers
                            2.2 Lower Controller and driver
                       3. Electrical Configurations
                       4. Treadmill Product Operation
                       5. Treadmill Unit Block Diagrams
                       6. Treadmill Basic Connections and Wiring
                          6.1 Display Board PCB Component Locations
                         6.2 Display Board Wire Connections
                         6.3 Driver Board Wire Connections
                         6.4 Driver Board PCB Component Locations
                         6.5 Driver Board LED Indicator Locations
                         6.6 Controller Indicator LED Debugging
                         6.7 Driver Board Function
                       7. Product Safety Instructions
                       7.1 Important Safety Instructions
                       7.2 Important Electrical Instructions
                       7.3 Important Grounding Instructions
                       8. Treadmill Error Messages issues
                          8.1 Error Message：E0
                          8.2 Error Message：E1
                          8.3 Error Message：E2
                          8.4 Error Message：ERR
                          8.5 Error Message：E4
                          8.6 Error Message：E5
                          8.7 Error Message：E6
                          8.8 Error Message：E7
                          8.9 Circuit diagram (120/220V)
                         8.10 Calibration Procedure
                         8.11 Troubleshooting Procedure Matrix

                                                       1                                    Service Manual
 9. Folding/Unfolding and Transport
10. General Maintenance
11. Disassembling and Assembling of Parts




                                2           Service Manual
1. GT90C-NT023
  GT90D-NT024
Treadmill Outlines



        3            Service Manual
GT90C-NT023




     4        Service Manual
GT90D-NT024




     5        Service Manual
2. Electronic Parts




         6            Service Manual
2.1 Upper Controllers




                        7   Service Manual
8   Service Manual
2.2. Lower Controller and Driver




    SPEED SENSOR




                                                  Incline
                                                  Motor
                                   DC Motor
                                                            Lower Controller




                                              9                                Service Manual
3. Electrical Configurations




             10                Service Manual
   SAFETY KEY:
    To fits on the Console that activate all functions. If no safety key, console can not be controlled.


   CONSOLE:
    Interface that controls all functions of the treadmill.

   Main controller:
      The circuit board consist of the DC power supply for console、incline driver and DC motor driver, link the console to output appropriate voltages for
    motor that control the treadmill functions.


   TREADMILL MOTOR:
    This is a variable speed for DC motor. To control the 0 –180(230VAC) voltages on the main controller, it can to increase or decrease speed of
    running belt.




GENERAL INFORMATION


   CONSOLE
    Contains key control and LCD display.

   Main controller
    Include power supply 、 Motor driver control circuit and Incline control circuit.



                                                                             11                                                          Service Manual
      Treadmill motor

      DC motor with variable speed range 0-90 or (0-180) volt.

      Have three wires red, black and green.

      If there is DC voltage on the Red (white) wire (M+) the treadmill motor will turn clockwise.

      If there is DC voltage on the Black wire (M-) the treadmill motor will turn counter-clockwise.

      The higher the voltage the faster the motor turns

      The green wire is ground.


      INCLINE MOTOR
      This is a 220 volt AC motor.

      Requires four wire connection: red, black, white and green.

      Has one 3 pins cable for position sensor.

      If there is AC voltage on the Red wire (UP), the incline motor will increase the incline.

      If there is AC voltage on the Black wire (DOWN), the incline motor will decrease the incline.

      The White wire (COM) is neutral.
      The green/yellow wire is grounding wire.


NOTICE BEFORE OPERATION:
The treadmill will increase or decrease speed slowly. It means that it will take you a little time to reach the speed you adjusted. When you work on the
treadmill, you must check the emergency switch is inserted right position and the clip is on your cloth. Any of the devices above mentioned is incorrect,
and then the machine couldn‟t work.



                                                                               12                                                        Service Manual
4. Treadmill Product Operation




             13              Service Manual
Display Windows
Note: GT90C-NT023 and GT90D-NT024 LCD display screen LAYOUT are the same, just different size.
GT90C-NT023 LCD is 6.5”, GT90D-NT024 is 7.5”.

                                                         LCD Layout




                                                                  14                             Service Manual
Operation
Window Display Mode
   OFF Mode
       If treadmill is turned on, when user doesn‟t insert the SAFETY KEY on the console, the console display appears idle Mode status, but console
   doesn‟t work.
   READY Mode
        When the treadmill is turned on and SAFETY KEY is inserted in console, the message window will show 「press start for quick start or program
   button for setup」.
   RUN Mode
      In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly and enter OFF Mode.
Function
   SPEED
      Display the current speed in Kilometer or Mile per hour.
      DISPLAY range is 0.0 to 99.9 KM/H.
      WORK range is 1.0 to 16.0 KM/H (0.5~10 MPH).
       Press FAST or SLOW to adjust speed, each increment and decrement is 0.1 KM/H (MPH).
   Incline
        Display the incline position from 0 to 15.
        DISPLAY range is 0 to 99.9.
        WORK range is 0 to 15.
        INCLINE preset value is 0 to 15.
        Press UP or DOWN to adjust incline, each increment and decrement is 1.
   TIME
      Time can count up or count down. System preset is count up; if user sets the time then timer is count down.
      DISPLAY range is 0:00 to 99:99.
      WORK range is 0:00 to 99:59.
      Count up setup range is 10:00 to 99:00.
      When TIME is set, the count will go to zero.

                                                                         15                                                           Service Manual
    In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will continue count up time.
DISTANCE
    Display the current distance in kilometer or Mile.
    DISPLAY range is 0.00 to 99.99.
    WORK range is 0.00 to 99.99.
CALORIES
   Displays the cumulative calories burned at any given time during your workout.
   DISPLAY range is 0.0 to 999.
   WORK range is 0.0 to 999.
PULSE
   Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
   DISPLAY range is 0 to 999.
   WORK range is 40 to 220.
   In RUN Mode, if the treadmill doesn‟t have a signal for 8 seconds then display value will become “ P ”.
PACE
   It means: How long will takes to walk (or run) per each Km or Mile at current speed?
    The unit is min/Km or min/Mi.
    DISPLAY range is 0.00 to 99.99.
    WORK range is 0.00 to 99.99.




                                                                      16                                                        Service Manual
Function Button Locations
                                                       Note this name
                                  Incline                                         Speed
                                                     Relates to Bluetooth
                               Shortcut keys                                   Shortcut keys
           Speaker
                                                                                                             Speaker




                                                         Display




                                                           Fan vent

                         Incline                                                         Speed
                         UP (+)                                                         FAST (+)
                        DOWN (-)                                                        SOLW (-)




                                                                                               Program key
                     Fan key
                                       Start &Stop
                                                                            Enter key
                                           key            Safety key




                                                             17                                                        Service Manual
                                              Note this name
                    Incline              Relates to Bluetooth           Speed
                Shortcut keys                                       Shortcut keys

Speaker
                                                                                                  Speaker




                                                    Display




                                                     Fan vent

              Incline                                                          Speed
              UP (+)                                                          FAST (+)
             DOWN (-)                                                         SOLW (-)




                                                                                    Program key
          Fan key
                                Start &Stop
                                                                  Enter key
                                    key              Safety key




                                                      18                                                    Service Manual
Function Button in Main Mode
  READY MODE
     SAFETY KEY: Fit safety key in right position to power on the console. When safety key is pulled away from its position, the computer will be
     automatically shut down.
     START/ STOP button: Pressing START/STOP button to start/stop treadmill.
     On the standby first press “START” button, the console will be 3 seconds final count down on window displays, and then machine starts running in
     the Manual (normal) program. When console in the presetting programs which will be started at default speed.
     When press second time, the treadmill will be paused. If press third second time, the treadmill will be started. After that will be repeated cycle.
     ENTER button: Set presetting program item values (ex: count-down time value、count-down distance value、count-down distance calorie value).
     Or other setting confirm key.
     PROGRAM button: In the standby mode, press this key will be into presetting programs, it is can any choose one of part (P1~P30、1 HRC、2
     USER MODE) to do exercise.
     FAST button: If user doesn‟t enter a setting then this button is non-functional.
     SLOW button: If user doesn‟t enter a setting or treadmill doesn‟t working, then this button is non- functional.
     UP button: If user doesn‟t enter a setting or treadmill doesn‟t working, then this button is non- functional.
     DOWN button: If user doesn‟t enter a setting or treadmill doesn‟t working, then this button is non- functional.
     SPEED RAPID button: Non-functional.
     INCLINE RAPID button: Non-functional.
     FAN button: It can to control ON/OFF for the fan.




                                                                         19                                                            Service Manual
RUN MODE
  SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down.
  START/STOP button: Pressing START/STOP button to start/stop treadmill.
  On the standby first press “START” button, the console will be 3 seconds final count down on window displays, and then machine starts running in
  the Manual (normal) program. When console in the presetting programs which will be started at default speed.
  When press second time, the treadmill will be paused. If press third second time, the treadmill will be started. After that will be repeated cycle.
  ENTER button: non-functional.
  Program button: non-functional.
  FAST button: Press the button to increase your speed and each increase is 0.1KPH (0.1mph). If button is pressed continuously then speed
  increases to MAX SPEED quickly.
  SLOW button: Press the button to decrease your speed and each decrease is 0.1KPH (0.1mph). If button is pressed continuously then speed
  decreases to MIN SPEED quickly.
  UP button: Press the button to raise position and each increase is 1, the maximum incline position is 12.
  DOWN button: Press the button to lower position and each decrease is 1, the minimum incline position is 0.
  SPEED RAPID button: 10 preset buttons for rapid speed.
  INCLINE RAPID button: 10 preset buttons for rapid incline.
  Fan button: It can to control ON/OFF for the fan.




                                                                      20                                                            Service Manual
5. Treadmill Unit Block Diagrams




               21              Service Manual
Treadmill Configuration

               USB (Only Charge)




                                   BLUETOOTH




                                               22   Service Manual
6. Treadmill Basic Connections and Wiring




                    23                 Service Manual
6.1 Display Board PCB Component Locations
           PCB Board Top for GT90C-NT023 (TX3500)




                                                    24   Service Manual
PCB Board Top for GT90D-NT024 (TX4500)




                                         25   Service Manual
PCB Board Bottom for GT90C-NT023 (TX3500)




                                            26   Service Manual
PCB Board Bottom for GT90D-NT024 (TX4500)




                                        27   Service Manual
6.2 Display Board wire Connections
             For GT90C-NT023 (TRX3500)

  Speaker                                                                             Wireless Pulse Socket
                                                                                                                                     Fan power
                                                                                                                                     wires socket
  Speaker
                                                                                                                      AMP power
                                                                                                                      wires socket


                     MP3 Audio
                     input wires                                                                                   Bluetooth board
                     socket                                    Display IC
                                                                                                                    wires socket
                                                                                                   MAIN IC

                                                                                                                      Safety key
                                Hand Pulse Module
                                                                                                                      wires socket
                                                                            „


                                                                                                                      Main Control
                                                                                                                      wires Socket




            Hand Pulse Socket                       Incline Handrail             Key board           Speed Handrail
                                                    keys socket                  wires Socket        keys socket




                                                                            28                                                         Service Manual
              For GT90D-NT024 (TRX4500)
                                                                                               Wireless Pulse Socket
                                                                               Speaker

                                                                                                                             Fan power
                                                                                                                             wires socket
Speaker
                                                                                                              AMP power
                                                                                                              wires socket

                     MP3 Audio
                     input wires                                                                     Bluetooth board
                     socket                             Display IC                                    wires socket

                                                                                         MAIN IC
                                                                                                           Safety key
                             Hand Pulse Module                                                             wires socket




                                                                                                           Main Control
                                                                                                           wires Socket




 Hand Pulse Socket     Hand Pulse Socket         Incline Handrail         Key board       Speed Handrail
                                                 keys socket              wires Socket    keys socket




                                                                     29                                                        Service Manual
6.3 Driver Board Wire Connections




                                    30   Service Manual
6.4 Driver Board PCB Component Locations




                                           31   Service Manual
6.5 Driver Board LED Indicator Locations




                                                                       It is a signal indicate LED, the
                                                                       INFO LED does not light
                                           LED3：                       represent the lower control
                                           Power directive LED.        board was not Received upper
                                           When treadmill power, LED   console board signal.
                                           will be blazed.




                                                 32                                    Service Manual
6.6 Controller Indicator LED debugging

Indicator            Function                          Condition                             Reason                              Solve
  LED
INFO        Whether lower control board If lower control board does not Link to It is a signal indicate LED, the  Check main control wires, may be broke.
            Link to upper console control upper console control board, the      INFO LED does not light           Replace controller or upper console
            board or not.                 INFO LED does not light.              represent the lower control board board.
                                                                                was not Received upper console
                                                                                 board signal.
POWER       Controller power             If DC voltage is normal, it would be    Voltage is not correct.        Check the supply voltage is 220V.
                                         always ON. If off, fault condition      Fuse is blown.                 Replace Fuse.
                                         exists.                                 Transformer is no good.        Replace controller.




                                                                            33                                                           Service Manual
6.7 Driver Board function




                        Bridge                                                                           MOTOR
                        Rectification                                 FET                                (BLACK WIRE)
                                                                                                         M-

       230VAC IN                                                                                          MOTOR
                                        Filter capacitor
                                                                                                          (RED WIRE)
                                                                                                          M+

          INCLINE
          COM
                                                                Transformer
          WHITE
                                                                                                          SPEEDD SENSOR
       INCLINE
                     Incline        Speed
       DOWN                                                                          TORQUE
                     Relay          Relay
       BLACK


        INCLINE                                                               Main system line   INCLINE VR
        UP
        RED




                                                           34                                                 Service Manual
7. Product Safety Instructions




              35                 Service Manual
7.1 Important Safety Instructions
  - To reduce the risk of electric shock disconnect your treadmill from the electrical outlet prior to cleaning and/or service work.
  - To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat level surface with access to a 230-volt, 10-amp
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
  - This product must be grounded. If the treadmill should malfunction or breakdown, grounding provides a path of least resistance for electric current,
    reducing the risk of electric shock. This product is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
    appropriate outlet that is properly installed and grounded in accordance with all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a qualified electrician or
  serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug provided with the product if it will not fit the
  outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 230-volt circuit, and has a grounding plug that looks
  like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle
  as shown below if a properly grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
  can be installed by a qualified electrician. The green colored rigid earplug, or the like, extending from the adapter, must be connected to a permanent
  ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must be held in place by a metal screw.




                                                                                36                                                                 Service Manual
    8. Treadmill Error Messages /
Troubleshooting for Electronic Issues




                  37              Service Manual
   Error code items：


                   Error Message Explain
                   E0            The display appears E0. It means safety key is removed.
                   E1               Display board CPU did not receive the RPM signal.(only calibration)
                   E2               Treadmill motor is over load.
                                    The console board is not detecting the VR voltage value, or the voltage value has
                   ERR
                                    exceeded the range.
                   E4               Treadmill motor wires or volt possible abnormal.
                   E5               Communication single is abnormal.
                   E6               Lower Control board possible broken.
                   E7               Low volt or abnormal unstable volt.

   Prepare：

                                                  Picture                              Tool name




                                                                                       Multi-meter




                                                                      38                                                Service Manual
8.1 Error Message：Display appears「E0」on the Message Window
   Definition：Display board CPU did not receive the Safety device signal.
   Configuration：




                              The safety key signal by TX、RX of
                              5-Pin Main control wires to transport.




                                                                             39   Service Manual
 Safety Pin place on the console board.




                                           40   Service Manual
Safety key device test
         Test configuration




                      Turn to buzzer setting of Ω gear.                                        Turn to buzzer setting of Ω gear.




                               Safety key device is normal                                                  Safety key device is bad


   Test procedure
    1. Put safety key in position.
    2. Use to the multi-meter, and turn to the buzzer setting of Ω gear. Place the red probe on the safety key device pin. Place the black probe on the
        safety key another pin.
    3. If the meter shows 0.00 or more. The safety key device is normal.
    4. If the meter shows OL. The safety key device is bad. Please replace the safety key device. Then check again.




                                                                           41                                                            Service Manual
 Safety key connect to the board




            Safety key 2-Pin is
            inserted on keyboard
            socket


                                    The 2 pins safety socket converted into
                                    5 pins socket, and then it is connected
                                    bifurcation of keyboard wires.
                                    Finally, safety pins will be inserted safety
                                    socket of the upper control board.


                                                                42                 Service Manual
 PLEASE INSTALL SAFETY KEY TO START issue troubleshooting form
PLEASE INSTALL
SAFETY KEY TO         Possible cause                     Things to check                               Solution
START message

Display board CPU did Safety key is loose or unplugged   Check the position of the safety key device   Reset the safety key correctly
not receive the Safety
    device signal.                                                                                     Reconnect all cables to ensure them in
                       Bad cables connection             Check all cables connection
                                                                                                       good connection




                                                                 43                                                            Service Manual
8.2 Error Message：E1
   Definition：Only happen calibration, Display board CPU did not receive the RPM signal.
   Configuration：




                                                                          5Pin




                                                                              44            Service Manual
 Cause of E1
The motor doesn’t turn：E1 appears.
            Explanation
              The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receiver the RPM sensor signal.
              Configuration




                                                                                     5Pin




                                                                                45                                                                 Service Manual
E1 solution follow chart

                           E1




                                46   Service Manual
E1 solution follow chart – check RPM sensor device procedure：




                             47                             Service Manual
      Checking the speed sensor
1) Remove the motor cover hood.
2) The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will
have a belt around it that also goes to the motor). The speed sensor is small and black with a wire
connected to it.
3) Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on
the face of the pulley; make sure the sensor is aligned with the magnet. There is a screw that holds the
sensor in place that needs to be loosened to adjust the sensor. Re-tighten the screw when finished.




              Reed switch RPM Speed
              sensor device




                                                             48                                           Service Manual
E1 issue troubleshooting form
E1 message        Possible cause               Things to check          Solution


                  Possible cause               Things to check          Solution




                  The monitor hasn't receive   check the speed sensor
                                                                      Make sure the good connection for
                  any speed signal for 8       cable is in good
                                                                      cables
                  seconds                      connection


E1 message
The motor can not                              Check the gap
                  The speed sensor didn't                           To keep the gap-distance less than
move                                           between speed sensor
                  detect signal completely.                         3 mm.
                                               and magnet.




                                               Check if the sensor
                  Defective sensor or bad                               Change the sensor or
                                               and cables are circuit
                  cable connection.                                     cables.
                                               short damaged.




                                                      49                                       Service Manual
8.3 Error Message：E2/OVER CURRENT
    •       Definition: When lower board detect over current, then LED light up and display appear “E2”.
            The means is lower board need to protect itself and motor. Prevent lower board and motor is
           burned.
    •      Solve over current:
           First, check whether smear Silicone oil or not. And then when during the using treadmill, do not
           block belt running. If aforementioned did not process problem, suggest Replacing lower control
           board or Replacing motor.



8.4 Error Message： ERR
       Definition：The console board is not detecting the VR voltage value, or the voltage value has exceeded the
        range.”ERR” appears on the display.
       Configuration：




                                      5Pin




                                                            50                                       Service Manual
Case of ERR
    Incline VR value exceeds the range. ERR appears on the display.
      Incline motor isn’t operation up or down, making the VR value exceed the range.
      After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so
         ERR appears.
        Action Flow Chart




                                                  51                                        Service Manual
  Troubleshooting
Part            Troubleshooting
                1. Reconnect VR wires.
Incline VR
                2. Inspect whether the incline wires are broken or disconnected.
                1. Inspect the incline wire and 5-pin cable connections.
Display board
                2. Test whether the VR voltage varies at the incline wire terminal.
                1. Inspect the wire connections.
5-pin cable     2. Inspect whether wires are broken or crimped.
                3. Replace the wires and test again.
Driver board    Inspect the display board 5-pin connections.




                                              52                                      Service Manual
Test Configuration. Incline motor control functions relate parts location




                                                                      The position sensor wires
                                                                      Red = Ground,
                                                                      White = Position signal,
      INCLINE POWER COM
                                                                      Black = 5vdc,
                 (WHITE)                                              (0~5v depending on incline position)


    INCLINE POWER DOWN
                (BLACK)


       INCLINE POWER UP
                  (RED)


                                                      1. SW 2.+12V 3.TXD    4.RXD     5.GND




                                                 53                                                          Service Manual
Error Message： INCLINE ERR
Definition：During incline action, the display board CPU cannot read the VR value, so   INCLINE ERR appears.
Configuration：




                            E1




                                                   54                                      Service Manual
   LCD show Err on the incline window：




                                 55       Service Manual
Cause of INCLINE ERR
    Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
  Explanation：
    Press the incline UP and DOWN key. The driver board up or down indicator lights. The incline operates,
  moving the VR, which changes the VR value.
    The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is
  not operating when it should be. INCLINE ERR appears on the display.
  Action Flow Chart




                                                    56                                        Service Manual
Troubleshooting
Part            Troubleshooting
                1. Press incline UP key. The driver board UP LED lights.
Display board   2. Press incline DOWN key. The driver board DOWN LED lights.
                3. If not as above, inspect the cable and connections.
                1. Inspect whether the 5-PIN cable is connected well.
5-pin cable
                2. Test by replacing the cable with a good one.
                Inspect whether the driver board UP/DOWN LED is lit.
                1. Press incline UP or DOWN key again, making the incline motor return to its
Driver board
                position .
                2. If ERR still appears, re-calibrate the incline set.
                1. Inspect whether the incline motor is stuck.
                2. Inspect whether the incline gears are cracked.
Incline motor
                3. Test whether the incline motor has a broken circuit.
                4. Re-calibrate the incline set.




                                          57                                       Service Manual
8.5 Error Message：E4
Definition: Motor power wires error.




                            Signal via
                 RPM                           Send command
                            TX/ RX of
                   or                          of start or
                            main control
                 Motor                         speed signal.
                            wires.
                 signal
                 return.




Configuration:




Cause of E4:
    Power wires of Motor does not insert lower controller.



 Troubleshooting
 Part                        Troubleshooting
 Lower controller            Insert power wires of motor.
 Motor                       Replace Motor.
 Display board               Replace upper control board.
                                                         58    Service Manual
8.6 Error Message：E5
Definition: it is a Poor communication, between the console and lower controller is poor communication, almost it is
bad on a main control wires, but also possible bad at console board or lower controller.
Configuration:




                                           Console


                         Signal via main
                         control wire to
                         communication.



                                     Lower controller




Cause of E5:
        The main control wires is possibly broken. But E5 maybe has another problem, like component of lower
controller or console board.




 Troubleshooting
 Part                          Troubleshooting
 Lower controller board        Replace main control wire.
 Main control wires            Reinsert Main control wire.
                               Replace main control wire.
 Display board                 Replace upper control board.




                                                           59                                      Service Manual
8.7 Error Message：E6
Definition: The lower controller component is fault.
Configuration:




                                           Console




                         Signal via main
                         control wire.



                                    Lower controller


Cause of E6:
        The lower controller component is fault, Like Transistor、IGBT、control module…etc.



 Troubleshooting
 Part                         Troubleshooting
 Lower controller             Insert power wire of motor.
 Display board                Only Replace upper control board.




                                                       60                                   Service Manual
8.8 Error Message：E7
Definition: Input power anomaly, possibly too low or too high or unstable.
Configuration:




Cause of E7:
        The wall outlet possibly unstable, cause to treadmill working power does not stable.
        Another problem possibly power part of lower controller board is broken.



 Troubleshooting
 Part          Troubleshooting
 Wall outlet Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or
               220AC or not. And the voltage whether stable or not.

 Lower         Replace Lower controller board.
 controller
 board




                                                          61                                   Service Manual
8.9 Circuit diagram




                      62   Service Manual
63   Service Manual
64   Service Manual
65   Service Manual
  8.10 CALIBRATION PROCEDURE
Calibration
After remove the Safety key, and then hold down the “ENTER KEY and FAST KEY” at the same time replace the safety key.
The treadmill‟s console will be into Calibration mode. The MW display window of console will appear and roll “A0464 VER (soft version) FACTORY
SETTING PRESS ENTER”.
1. After the ENTER key, The MW display window of console will appear “GRADE RETURN ON THEN PRESS ENTER”.
   (1) If choose “ON”, it‟s means after the used treadmill and does not returned at last time, incline had been keeping stretching, when open the power
   again, the incline will be auto returned lower point (0).
   (2) If choose “OFF” which have been keeping stretching until after press start key.
2. Set kilometers or miles. Press the Enter key to confirm and move to the next item.
3. Set wheel diameter to 60. Press the Enter key to confirm and move to the next item.
3. Set the minimum speed of 1KM (0.5Mi). Press the Enter key to confirm and move to the next item.
4. Set the maximum speed of 18KM (12Mi). Press the Enter key to confirm and move to the next item.
5. Set the maximum incline value of 12, and then press the Enter key to confirm. It will automatically enter into the calibration display.
6. Press the START/STOP key to start the calibration. It will return to the standby screen automatically after the calibration is complete.




                                                                              66                                                              Service Manual
8.11 Troubleshooting procedure matrix
                    Condition                                             Reason                                                Solve
When turn on power, ON/OFF switch isn‟t lit.           1 Power cord isn‟t plugged into outlet.      1 Plug the power cord into outlet.
                                                       2 Power cord isn‟t plug into unit.           2 Plug the power cord into unit.
                                                       3 The voltage of outlet is too low.          3 Check the voltage of outlet.
                                                       4 Plug or connector of power cord is open.   4 Replace power cord.
                                                       5 Connector of power cord is broken.         5 Replace power cord.
                                                       6 Connecting cable disconnected.             6 Check if wire is disconnected, connect it again.
                                                       7 Breaker tripped.                           7 Press the small red button to return to original status.
                                                       8 Breaker is broken.                         8 Replace breaker.
                                                       9 ON/OFF switch is broken.                   9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown   1 Check the voltage of power is 220V. Replace controller.
                                                        broken on controller.
When insert safe key, no display on monitor.            1. Haven‟t switch ON/OFF switch.            1 Switch the AC switch.
                                                        2. Insert the Safe key on wrong position.   2 Insert the safe key on right position.
                                                        3.12 PIN Computer connector not plugged     3 Please check the wire and connect again.
                                                          in properly.                              4 Replace 5-PIN computer cable.
                                                        4 .12 PIN computer cable is broken.         5 Replace fuse or controller.
                                                        5. Fuse on controller is blown.             6 Replace varistor or controller.
                                                        6. Varistor on controller is blown.         7 Replace safety key device.
                                                        7. Safety equipment is broken. (open)       8 Replace console.
                                                        8.Other components are faulty.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)          1 Replace the safety key device or console.

When press “START”, treadmill doesn‟t start.           1 Motor M+ or M- wire isn‟t connected into   1 Please check and plug again.
                                                         right position.
                                                       2 Motor is broken.                           2 Replace motor or check the wire and connector if it was
                                                       3 Treadmill controller shut down and LED       broken.
                                                       would be ON.                                 3 Turn off the AC switch and turn on power again.
Treadmill stops or shuts off by itself.                1 House breaker tripped.                     1. Reset it.
                                                       2 Treadmill chopper tripped.                 2. Reset treadmill breaker.
                                                       3 Treadmill controller fuse is broken.       3. Replace with new fuse
                                                       4 Treadmill controller shut down and LED     4. Turn off the AC switch and turn on power again.
                                                       would be ON.

After removing safe key, treadmill can‟t stop.         1. The safety key device is broken.          1. Replace with new safety key device.
LCDs not bright, incomplete or imperfect.              1. LCD light is broken.                      1. Replace with new LCD or console.
                                                       2. Power to console too low.                 2. Check AC power is 220V.
                                                                                                    3. Check power to console.
                                                                                                    4.Replace lower controller.
                                                                                   67                                                                 Service Manual
LCD displays not bright, incomplete or imperfect.     1. LCD displays are broken.                     1. Replace with new console.
When press “START” button to start treadmill, running 1. Controller experienced unusual shut          1. Turn off power and reset the treadmill.
belt isn‟t running and window displays “E1” error        down; the Shut_D light will be always
message after 10 seconds.                                bright.                                      2. Plug wires again.
                                                      2. Motor wires (red, black) aren‟t plugged into
                                                         controller.                                  3. Plug the wire again on controller, connector and console.
                                                      3. Computer cables not connected properly. 4. Replace with new wires.
                                                      4. Computer cables are broken or damaged. 5. Replace with new motor belt.
                                                      5. Motor belt is broken.                        6. Replace with new controller.
                                                      6. Controller is broken.                        7. Replace with new motor.
                                                      7. Motor is broken.                             8. Replace with new console.
                                                      8. Console is broken.
The speed of the belt doesn‟t match console display. 1. Console is not calibrated.                    1.Calibrate the console
The incline position doesn‟t match console            1 Console is not calibrated.                    1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “ERR”.           1 Position sensor value of incline motor is     1 Turn off the AC switch and turn on power again.
                                                      wrong.                                          2. Calibrate the monitor.
After pressing “START” button, the treadmill stops    1 Controller is broken.                         1 Turn off the AC switch and turn on power again.
immediately.                                                                                          2 Replace controller and calibrate it.
Erratic pulse display.                                1. Another chest belt in use around treadmill. 1. Check for other chest belt use around treadmill.
                                                                                                      2. Change the position or direction of treadmill.
                                                      2. Other magnetic field disturbance.            3. Replace with new receiver.

                                                       3. Receiver is broken.
After pressing “START” button, the treadmill stop      Controller was broken.                        Replace with new controller and calibrate it.
immediately.




                                                                                    68                                                                  Service Manual
FAST/SLOW button of SPEED ADJUSTMENT                  1 The connector of SPEED CABLE (UPPER) 1. Connect cables again.
SWITCH can‟t be used.                                    and CONSOLE not connected properly.
                                                      2 The connector of SPEED CABLE (UPPER) 2. Connect cables again.
                                                        and SPEED ADJUSTMENT SWITCH
                                                        W/CABLE not connected properly.
                                                      3 The connector of SPEED CABLE (UPPER) 3. Connect cable again.
                                                        or SPEED ADJUSTMENT
                                                        SWITCH/W/CABLE is damaged.
                                                      4. Button of SPEED ADJUSTMENT SWITCH
                                                         is broken.                          4. Replace with new buttons.

                                                    5. The connector of SPEED CABLE           5. Replace with new cable.
Speed button just can press FAST, can‟t press SLOW.    (UPPER) or SPEED ADJUSTMENT
                                                       SWITCH/W/CABLE is damaged.
Speed button just can press SLOW, can‟t press FAST. 6. The connector of SPEED CABLE           6. Replace with new cable.
                                                       (UPPER) or SPEED ADJUSTMENT
                                                       SWITCH/W/CABLE is damaged.
UP/DOWN button of                                   1 The connector of INCLINE CABLE (UPPER) 1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can‟t be used.              and CONSOLE not connected properly.
                                                    2. The connector of INCLINE CABLE         2. Connect the wires again.
                                                    (UPPER) and INCLINE ADJUSTMENT
Incline button just can press UP, can‟t press DOWN. SWITCH W/CABLE not connected properly.
Incline button just can press DOWN, can‟t press UP. 3 The connector of INCLINE CABLE          3. Replace the cable.
                                                    (UPPER) or INCLINE ADJUSTMENT
                                                    SWITCH CABLE got damage.
                                                    4. Button of INCLINE ADJUSTMENT           4. Replace buttons.
                                                    SWITCH is broken.
                                                    5. The connector of INCLINE CABLE         5. Replace the cable.
                                                    (UPPER) or
                                                    INCLINE ADJUSTMENT SWITCH CABLE
                                                    got damage.
                                                    6. The connector of INCLINE CABLE         6. Replace the cable.
                                                    (UPPER) or
                                                    INCLINE ADJUSTMENT SWITCH CABLE
                                                    damaged.
Hand pulse lost its function.                       1. Hands not on the hand pulse sensors or 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                        only one hand on sensor.
                                                    2. The connector of HANDPULSE W/WIRE 2. Connect the cable again.
                                                       and Console not connected properly.
                                                    3. The wires got damaged when connecting 3. Replace with new cable.
                                                       the HANDPULSE W/WIRE and Console.
                                                    4. Hand pulse board is broken.            4. Replace console or Hand pulse board.

                                                                               69                                                       Service Manual
Wireless lost its function.                    1. Chest belt not worn properly.                 1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                    oriented correctly.
                                               2. Distance is too far and exceeds range of      2. User chest belt in front of console within 3 feet.
                                                receiver.                                       3. Replace with new lithium battery type is CR2032.

                                               3. Chest belt battery is weak or dead.
Chest belt too close to the treadmill.         Weak battery.                                    Replace with new lithium battery with type CR2032.
Tread belt does not run in center.             Tread belt tension not even across tread belt.
                                                                                                See treadmill belt adjustment


Tread belt hesitates while being stepped on.   Insufficient lubricant on tread belt.            See treadmill belt lubrication
                                               Tread belt tension insufficient
Black particles collecting under treadmill.    Drive belt is breaking in.                       Vacuum under treadmill periodically.
Noise under motor cover.                       1. Worn brushes or bearings on motor.            1. Replace with new motor.
                                               2. Front roller bearings are defective.          2. Replace with new front roller.
                                               3. Drive belt is misadjusted (too tight or too   3. Adjust motor position.
                                               loose).
Noise in the rear of the treadmill.            1. Rear roller bearings are defective.           1. Replace with new rear roller.
                                               2. Rear roller misaligned.                       2. Adjust rear roller position.




                                                                             70                                                                   Service Manual
9.Folding/Unfolding and Transport




                71             Service Manual
72   Service Manual
10. General Maintenance




           73             Service Manual
74   Service Manual
75   Service Manual
76   Service Manual
11. Disassembling and
 Assembling of Parts




          77            Service Manual
78   Service Manual
79   Service Manual
80   Service Manual
81   Service Manual
82   Service Manual
83   Service Manual
84   Service Manual
85   Service Manual
86   Service Manual
87   Service Manual
88   Service Manual
89   Service Manual
90   Service Manual
91   Service Manual
92   Service Manual
93   Service Manual


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SOUIJINO |[JWIPeALL
PZ0.LN-G06LD
EZOLN-OQ0G6LD ‘1


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
alg lolalo
WwW ;

————S—————
wl st) om) a ~


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS
8

SAI ADINO

OOSEXaL SNITONI

HII xy


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

JOALIG PUe 19]|01]U0D J9MO7

6G


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

uonesado JOnNpOdd |[lwWpeatL "FP


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 52 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Display Windows

Note: GT90C-NT023 and GT90D-NT024 LCD display screen LAYOUT are the same, just different size.
GT90C-NT023 LCD is 6.5”, GT90D-NT024 is 7.5”.

LCD Layout

f PACE {CALORIES TIME DISTANCE PULSE

CCC) | CCC) | CC Ci | cic HE | CHCi Cy

LL | Ce

OOOO | OOO | Oooo

TTT TT TTT Tit Tiere iit iii
TTITTITittT 90% == BEES

_. . SEES EEE 50% == —SEEEEEEEE lL

OO 0 SEER eee ee

Ce ee —

INCLINE BESS eo c CCC BS SPEED
TTITTITittl 50% m—_ HERES

NW AA) NWA MA IN) A MY MZ) MI"
scan UN UN AN AN AN AN A AY AVAL

14 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Function Button Locations

Note this name
Relates to Bluetooth

~NWETTA

Incline

Shortcut keys wee Shortcut keys

INCLINE
le
10

4

QUICK KEYS

Incline Speed
UP (4) FAST (4)
DOWN (-) P SOLW (-)

Program key

Start &Stop
key

17 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Note this name

Relates to Bluetooth
Shortcut keys Shortcut keys

Incline Speed

speep V
le

5

QUICK KEYS

Fan vent

Incline . \ ‘ Speed
UP (+) aN FAST (+)
DOWN (-) } fi SOLW (-)

Program key

Start &Stop

Enter key
key

18 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

swelsbeig YIO/g WU) [[lupeaLL 'S


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 33 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
Treadmill Configuration

| —= reed
RECEIVER
COMING DISPLAY BOARD
SAFETY KEY

HR
HANDLEBAR

AMPLIFIER
LINE IN
BLUETOOTH |

==>

INCLINE

CURRENT : DRIVER BOARD MOTOR
BRAKER

K VR SET

SPEAKER
uk

Sa | POWER - :
wes =a SWITCH

RPM
SENSOR

22 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Bul, pue suoljaauu0) Jiseg |/Ilwipeall “9


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.1 Display Board PCB Component Locations
PCB Board Top for GT90C-NT023 (TX3500)

rn mee 4S 4-4-S-4 -S OSES
¢2# t+ & = cae = & fe 46.7 of

iE

a

oon
!
|

|

PYM hhh th hh dd dd 0 A nd a a =
Oe) oom Tosss0990098 Gee a es ‘eum

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS oz

(00S7XL) PZOLN-GO6LD 10) doy pueog god


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 40 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
PCB Board Bottom for GT90C-NT023 (TX3500)

tw rie viewer TUL, O4! at WA we ole ( ee * be ee
. ,

ALAR I

AO4E4_VIG 20170609

o8 (aman)

TA CEEeeeadeceeenierett
DAPAAREDLIAEDDH

LLovedgogo/ tivo
UU a
WHZL | peads
wow E7900"
COLS P9POY EZOLNVequnnGuRuW eboig

OVPSPOV: INI § Uoldyaseq
T2POLOLOOY | 4equinny Wed

Seb heeeeehoeseseeee te eeeeaeaeeaaeeeneennen

26 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 49 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
PCB Board Bottom for GT90D-NT024 (TX4500)

TF oe Wes
SOELFICCIC HES OO CAk eRe eee ne nent? yee
Vile, ‘ ‘

®

mee receererety ~~ -
Part Number A001010422
Description » INC ~A0465A0

ProgrammingNu mber. NTO24 AO4ES $107
70622.mot

Speed: 12K™M

TTT
041706234025

‘ee ere h ee eaeeeaee ae
Pigt
kh hi ee ob

Service Manual
27

=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 37 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.2 Display Board wire Connections
For GT90C-NT023 (TRX3500)

Speaker / Wireless Pulse Socket ,
; : | , iy Fan power
_— oe eae a = wires socket
Speaker = ’ VACLP hr ater Lesa Alene (0 4 aw | PM ee Wa Me
P sills Bae | OR he AMP power

wires socket

MP3 Audio

input wires | hey ot Bluetooth board

socket wires socket

f  aneereveneeeeieeeeet
TULA RMASRBP LS

Main Control
wires Socket

LLOVEESOLI+VO
UO TT a
WHET | paads
your ezg0e”

COTS PSPOY ECOLNVequUNNGuKuWebaig
OVPSPOY ONI : Goldssaq

Incline Handrail Key board Speed Handrail
keys socket wires Socket | keys socket

28 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7
7 eS

For GT90D-NT024 (TRX4500)

9

MP3 Audio
input wires

socket

Hand Pulse Module

Part Number - A001010422
Description : INC ~A0465A0

70622.mot
Speed: 12KM

Progra mmingNu mberNT024 AoaEs $102

Fate

i

priaeeerroeeererety
BEDAARRELUADEDE

D0 ep
04 |

keys socket

Incline Handrail

29

Speaker
PCOEERTTED Che

veeeeeeee

Wireless Pulse Socket

s, +
AMP power

wires socket

Bluetooth board

wires socket

Safety key

wires socket

Aeaeieine

{eee eeeas

Key board
wires Socket

Speed

keys s

ew 7 (yyw

Main Control
wires Socket

Handrail

ocket

Fan power

wires socket

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUD 11a 0€

SUO]I]OOUUND DIA PALO JSALG €°9


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP aI1AIaG I€

Ssuoi}eo0'7 juauOdwO04y 0d pieog J9ALG 79


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.7 Driver Board function

MOTOR
(BLACK WIRE)
M-

Bridge
Rectification

230VAC IN MOTOR

(RED WIRE)
M+

INCLINE Otrrs: |

COM oS =F) —
—_—— ee | ransformer . i"
WHITE ; a)
SO en : ms Warsesa9 oi

od

- —_ SPEEDD SENSOR

INCLINE ne , =
OWN Maem \ncline Speed ; ro Teed

qe Relay we Relay ~ he - <
BLACK Y Oise

Be

INCLINE = Main system line = INCLINE VR
UP
RED

34 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SUONONASU] AJajesS JONPOld *Z


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Sanss| 91U01]9a/F7 404 Hullooysajqnos]
/ sabessayy 407 pfiupeas] “9


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.1 Error Message : Display appears ' EO ; on the Message Window

@ Definition : Display board CPU did not receive the Safety device signal.
@ Configuration :

ae ese pete alge ie ica cee a

|

|

SAFETY KEY
ieee “GR AL |
|
CONSOLE |
2 PIN SAFETY KEY

DISPLAY BOARD |

|

pene ee oe ee ee eed |
The safety key signal by TX + RX of
5-Pin Main control wires to transport.

MOTOR
VOLTAGE

AC POWER » DRIVER BOARD ce »> MOTOR

39 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS OP

*pieOg dJOSUOD ay} UO adeRI|d Uld AJaBJeES  @


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
8.2 Error Message : E1

@ Definition : Only happen calibration, Display board CPU did not receive the RPM signal.

@ Configuration :

CONSOLE
DISPLAY BOARD

MOTOR SPEED

RPM SENSOR .
SIGNAL 5Pin

SIGNAL

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER » DRIVER BOARD

=< SIGNAL

= RPM
; SENSOR

44 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of E1

The motor doesn’t turn : El appears.
m@ Explanation
@ = The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receiver the RPM sensor signal.
@ Configuration

CONSOLE
DISPLAY BOARD

RPM SENSO) . KOTOR SPEED
sicNAL | SP SIGNAL

MOTOR
VOLTAGE

2 PIN > MOTOR

~~

AC POWER » DRIVER BOARD

= SIGNAL

2 PIN RPM
SENSOR

45 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 47 ===
<!-- render-vs-extraction: 44 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart

El
showing up

DI ves Check RPM sensor

NO

Open the inotorhood
and tum the power
beck on

Press “start” to
count down and
watch the PWM

LED on the
controller

Connect properly ——————

7 YES

Tum the power back
on und press “start” NO
to count down

Are only POWER and PWM LEDs on YES

YES

Motor cable connected to M+ M-
terminals properly
Yes Replace Console

¥ YES

Problem fixed is

Problem fixed

” Replace controlier Problem fixed

Replace controller

46 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 48 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart — check RPM sensor device procedure :‘

Check RIM sensor

Sensor cable connected

i? NO—#| Conpect Properly

YES
t

Move the roller so
thit magent closest
to the sensor

Make sure the gap
between magnet/sensor less
than 3 mim

Achust sensor
position

YES

Replace sensor wath
cable

um power hack or>

press “start” and
comnidown

Is function OK?

VYES—e| Problem fixed

NO
Y

Replace computer
cuble

‘um power back ony
press “start” and
comnidown fs function
OK?

—VES—e| = Problem fixed

NO

Replace Console

47 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
{aT art2i

eet ts ¥
As eS

@ Checking the speed sensor
1) Remove the motor cover hood.
2) The speed sensor is located on the left side of the frame, right next to the front roller pulley (the pulley will
have a belt around it that also goes to the motor). The speed sensor is small and black with a wire
connected to it.
3) Make sure the sensor is as close as possible to the pulley without touching it. You will see a magnet on
the face of the pulley; make sure the sensor is aligned with the magnet. There is a screw that holds the

sensor in place that needs to be loosened to adjust the sensor. Re-tighten the screw when finished.

Reed switch RPM Speed

sensor device

48 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 50 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 issue troubleshooting form

E1 message Possible cause Things to check Solution

Possible cause Things to check Solution

The monitor hasn't receive |check the speed sensor ;
Make sure the good connection for

any speed signal for 8 cable is in good
; cables
seconds connection
E1 message
Th t t Check the ga
© moron cane The speed sensor didn't cap To keep the gap-distance less than
move . between speed sensor
detect signal completely. 3 mm.
and magnet.
. Check if the sensor
Defective sensor or bad _ _, |Change the sensor or
; and cables are circuit
cable connection. cables.
short damaged.

49 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.3 Error Message: E2/OVER CURRENT

° Definition: When lower board detect over current, then LED light up and display appear “E2”.
The means is lower board need to protect itself and motor. Prevent lower board and motor is
burned.

e Solve over current:

First, check whether smear Silicone oil or not. And then when during the using treadmill, do not
block belt running. If aforementioned did not process problem, suggest Replacing lower control

board or Replacing motor.

8.4 Error Message : ERR

@ Definition : The console board is not detecting the VR voltage value, or the voltage value has exceeded the
range.” ERR” appears on the display.
@ Configuration :

DISPLAY BOARD

INCLINE
VR
VOLTAGE
INCLINE
MOTOR
DRIVER BOARD oa VR VOLTAGE INCLINE VR SET

C) INCLINE DOWN LED
C) INCLINE UP LED

50 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Case of ERR
M@ Incline VR value exceeds the range. ERR appears on the display.
@ Incline motor isn’t operation up or down, making the VR value exceed the range.
@ After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so
ERR appears.
@ Action Flow Chart

( INCLINE VR +)
<n > + —

DRIVER BOARD

VR VOLTAGE? N at
y
|
CABLE
VR VOLTAGE? N >

DISPLAY BOARD

<—Kiarie_—>—_1»—+
Y

y
DISPLAY OPERATES ERR APPEARS ON
NORMALLY THE DISPLAY

51 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 55 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Error Message : INCLINE ERR

Definition : During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | panywarecys
INCLINE

El
INCLINE INCLINE
VR UP/DOWN
VOLTAGE SIGNAL
MOTOR

DRIVER BOARD — VR VOLTAGE INCLINE VR SET

Ni

C) INCLINE DOWN LED
C INCLINE UP LED

54 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 37 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of INCLINE ERR

Press the incline UP/DOWN key. The incline doesn’t operate. INCLINE ERR appears on the display.
Explanation :

Press the incline UP and DOWN key. The driver board up or down indicator lights. The incline operates,
moving the VR, which changes the VR value.

The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the incline is
not operating when it should be. INCLINE ERR appears on the display.

Action Flow Chart
_
( DISPLAY BOARD »)
388 INCLI
y

|
DRIVER BOARD

a TIRING tPF AC HON,
UP LED crs INCLING > N

ce PAGK INCREASKS er 7
ere

al
Y

—e
eee IM PWN Ae rier, ~
DOWN LED L4G19S.INC LINE —_ _N- _ "
WEN TAC DEORE AES

eo

Y
i

INCLINE Mtr

de

a ale
1
ll Pose

Y
L : ¥
SHOW EQINGCLINE ERR
C NO LRR MESSAGE ) (! MESSAGE )
—— a

56 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 59 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.5 Error Message: E4

Definition: Motor power wires error.

DISPLAY BOARD

As

Signal via
RPM TX/ RX of Send command
or . of start or
main control
Motor speed signal.

Vv

INCLINE
MOTOR

DRIVER BOARD om VR VOLTAGE INCLINE VR SET

C) INCLINE DOWN LED
C) INCLINE UP LED

Configuration:

Cause of E4:

Power wires of Motor does not insert lower controller.

Troubleshooting

Part Troubleshooting

Lower controller Insert power wires of motor.
Motor Replace Motor.

Display board Replace upper control board.

58 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 62 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.8 Error Message: E7

Definition: Input power anomaly, possibly too low or too high or unstable.

Configuration:

Console

Vall outlet
AC 110V
Or

AC 220V

7 Signal via main
Overload control line.
protection

4 ’
Power Switch _—> Lower controller

14

CE PART or 220V to match
Filter and Chock.

Cause of E7:
The wall outlet possibly unstable, cause to treadmill working power does not stable.

Another problem possibly power part of lower controller board is broken.

Troubleshooting

Part Troubleshooting
Wall outlet |Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110ACV or
220AC or not. And the voltage whether stable or not.

Lower Replace Lower controller board.
controller
board

61 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 63 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
8.9 Circuit diagram

GT90C-NT023 120V
TREADMILL CIRCUIT DIAGRAM

62 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 64 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
TREADMILL CIRCUIT DIAGRAM
AC POWER INPUT | § ——_-:
Power cable ; 5-PIN
? MAIN CONTROL WIRES

GT90C-NT023 CEGS 220V

CONTROLLER|=ig J
ee JK
MOTOR a | | 5-PIN LOWER MAIN CONTROL WIRES
| ia 2PIN
GROUND WIRE ———— “= SENSOR WIRE

63

Service Manual


=== OCR SUPPLEMENT, PDF PAGE 65 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
GT90D-NT024 120V

TREADMILL CIRCUIT DIAGRAM
ie ——_,
3
5-PIN :
MAIN CONTROL WIRES =
keys = DEFINITION 5,
i-- sw
BREAKER 2+ vod
3—- TD
it Se ~

4 Z
iy!
z
| [Ug
ACI aco § GROUND WIRE Ay
CONTROLLER|=2o™ au
COM.
M+ M- JK JK
i 0 0
MOTOR BLACK WARE 5-PIN LOWER MAIN CONTROL WIRES
| aroun wire = gENSOR wrRE

64 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 66 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AIIAIAS 69

WVYSVIC LINDO THWAVAYL
A0@?Z SOAD VZOLN-G06LS


=== OCR SUPPLEMENT, PDF PAGE 70 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
FAST/SLOW button of SPEED ADJUSTMENT 1 The connector of SPEED CABLE (UPPER) |1. Connect cables again.
SWITCH can’t be used. and CONSOLE not connected properly.
2 The connector of SPEED CABLE (UPPER) |o ¢ t cabl in.
and SPEED ADJUSTMENT SWITCH Onset eanies again
W/CABLE not connected properly.

3 The connector of SPEED CABLE (UPPER
or SPEED ADJUSTMENT E ( ) 13. Connect cable again.
SWITCH/W/CABLE is damaged.

4. Button of SPEED ADJUSTMENT SWITCH
is broken. 4. Replace with new buttons.

5. Replace with new cable.
Speed button just can press FAST, can’t press SLOW. : (UPPER) oF SPEED ADJUST ENT P

; ; SWITCH/W/CABLE is damaged.
Speed button just can press SLOW, can’t press FAST. 6. The connector of SPEED CABLE 6. Replace with new cable.

(UPPER) or SPEED ADJUSTMENT
SWITCH/W/CABLE is damaged.

UP/DOWN button of 1 The connector of INCLINE CABLE (UPPER)|1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used. and CONSOLE not connected properly.
2. The connector of INCLINE CABLE 2. Connect the wires again.

(UPPER) and INCLINE ADJUSTMENT

Incline button just can press UP, can’t press DOWN. = |SWITCH W/CABLE not connected properly.

Incline button just can press DOWN, can’t press UP. {3 The connector of INCLINE CABLE 3. Replace the cable.
(UPPER) or INCLINE ADJUSTMENT
SWITCH CABLE got damage.
4. Button of INCLINE ADJUSTMENT 4. Replace buttons.
SWITCH is broken.
5. The connector of INCLINE CABLE 5. Replace the cable.
(UPPER) or
INCLINE ADJUSTMENT SWITCH CABLE
got damage.
6. The connector of INCLINE CABLE 6. Replace the cable.
(UPPER) or
INCLINE ADJUSTMENT SWITCH CABLE
damaged.

Hand pulse lost its function. 1. Hands not on the hand pulse sensors or /|1. Two hands hold the hand pulse.
(No pulse displayed on monitor) only one hand on sensor.
2. The connector of HANDPULSE W/WIRE_ |2. Connect the cable again.
and Console not connected properly.
3. The wires got damaged when connecting |38. Replace with new cable.
the HANDPULSE W/WIRE and Console.
4. Hand pulse board is broken. 4. Replace console or Hand pulse board.

69 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 72 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

piodsues pue bulpjojup/bulpjo4'6


=== OCR SUPPLEMENT, PDF PAGE 73 ===
<!-- render-vs-extraction: 84 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
» UNFOLDING
Pull locking Knob and hold running deck and lower down to the

floor.
(As shown Figure 1_2.)

» FOLDING
Pull the locking knob with right hand, left hand lift the running deck
up to 30cm then two hands lift it until it is locked by the locking
knob. (As shown in Figure 3_4)

>» TRANSPORT
Before moving the treadmill, convert the treadmill to the storage as
described above. Make sure that the Locking Knob is closer fully
over the frame guide.

1). Hold the upper ends of the handrails. Place one foot on the
base .

2). Tilt the treadmill back until it rolls freely on the rear wheels.
Carefully move the treadmill to the desired location. To
reduce the risk of injury, use extreme caution while moving
the treading. Do not attempt to move the treadmill over an
uneven surface.

3). Place one foot on the base, and carefully lower the treadmill
until it is resting in the storage position.

72 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 74 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

QIUCUDJUIE/ [EAODUDE) ‘OL


=== OCR SUPPLEMENT, PDF PAGE 75 ===
<!-- render-vs-extraction: 139 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
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

—|© \\
Adjustment Adjustment

Tracking / Tension Tracking / Tension

Note: Adjustment is through small hole in the end cap.

74 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 76 ===
<!-- render-vs-extraction: 171 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Tighten the rear roller bolts only enough to prevent slippage at the front roller. Turn both tread-belt tension adjustment bolts in increments of 1/4 turn
each and inspect for proper tension by walking on the belt at a low speed, making sure the belt does not slip. Keep tensioning the bolts until the belt
stops slipping.

e If you feel the belt is tight enough, but it still slips, the problem may be a loose Motor drive belt under the front cover.

DO NOT OVERTIGHTEN - Over tightening will cause belt damage and premature bearing failure.

TREADBELT TRACKING ADJUSTMENT:
The performance of your treadmill is dependent on the frame running on a reasonably level surface. If the frame is not level, the front and back roller
cannot run parallel, and constant belt adjustment may be necessary.

The treadmill is designed to keep the tread-belt reasonably centered while in use. It is normal for some belts to drift near one side while the belt is
running with no one on it. After a few minutes of use, the tread-belt should have a tendency to center itself. If, during use, the belt continues to move
toward one side, adjustments are necessary.

TO SET TREADBELT TRACKING:

A6 mm Allen wrench (97) is provided for this adjustment. Make tracking adjustments on the left side bolt. Set belt speed at 3 mph. Be aware that a small
adjustment can make a dramatic difference which may not be apparent right away.

lf the belt is too close to the left side, then turn the bolt only a 1/4 turn to the right (clockwise) and wait a few minutes for the belt to adjust itself.
Continue to make 1/4 turns until the belt is stabilized and the edge is within the range marked on the motor hood. If the belt is too close to the right side, turn
the bolt counter-clockwise. The belt may require periodic tracking adjustment depending on use and walking/running characteristics. Some users may

affect tracking differently. Expect to make adjustments as required to center the tread-belt. Adjustments will become less of a maintenance concern as the
belt is used. Proper belt tracking is an owner responsibility common with all treadmills.

75 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 77 ===
<!-- render-vs-extraction: 100 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ATTENTION:
DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING /
TENSION ADJUSTMENTS IS NOT COVERED UNDER THE WARRANTY.

BELT/DECK LUBRICATION
Your treadmill should require little maintenance other then periodically applying lubricant. Lubricating under the treadbelt will ensure superior performance

and extend its life expectancy.

HOW TO CHECK TREADBELT FOR PROPER LUBRICATION?

Lift one side of the treadbelt and feel the top surface of the treadboard.
If the surface is slick to the touch, then no further lubrication is required.

If the surface is dry to the touch, apply one packet of lubricant or half of the bottle of lubricant.

HOW TO APPLY LUBRICANT?

1. Lift one side of treadbelt.
2. Pour one half of the lubricant bottle under the center of the treadbelt on the top surface of the treadboard.
3. Walk on the treadmill at a slow speed for 3 to 5 minutes to evenly distribute lubricant.

NOTE: DO NOT over lubricate treadboard. Any excess lubricant that comes out should be wiped off.

IMPORTANT: ONLY USE HALF THE BOTTLE OF LUBRICANT PER APPLICATION
LUBRICATION SCHEDULE.

1. After the first 25 hours of use (2-3 months) apply one half bottle of lubricant.

2. Every 50 hours of use (5-8 months) apply one half bottle of lubricant.

76 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 78 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Sieg Jo buljquiassy
pue buljquiassesig ‘[|


=== OCR SUPPLEMENT, PDF PAGE 79 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
11-1 Lower Controller Replacement

Remove motor cover
Disconnect all lower controller wirings
Use Phillips head Screwdriver to remove, replace with new lower controller and reconnect all wirings.

ies |
S1

78 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 80 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11-2 Console Replacement

1. Use M5 LAllen wrench to remove 4 Button Head Socket Bolts from the console support

79 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 81 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11-3 Motor Replacement

1. Use Phillips head screwdriver to remove 3 Tapping screw securing the motor cover.

Mer veur sree


=== OCR SUPPLEMENT, PDF PAGE 82 ===
<!-- render-vs-extraction: 45 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. Remove motor grounding wire (greenish yellow), motor wire (+) red and motor wire (-) black.

2 2

4. Use 14mm T-shaped socket wrench to loosen 4 screws, use 14mm open end wrench to loosen 1 belt tension screw,
remove motor and replace with new. Reassemble in reverse order of disassembly, re-hook belt (readjust belt to be
parallel with main frame after re-hooking). Do not tighten 4 securing screws yet.

81 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 83 ===
<!-- render-vs-extraction: 40 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5. Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area
between 70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws. Connect
grounding wires and motor wires (red M+, black M-)

11-4 Breaker Replacement

Remove Breaker connection wiring, replace part and reconnect wiring.

82 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 84 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11-5 AC Power Switch Replacement

Disconnect wiring to AC power switch, replace AC power switch and reconnect wiring.

11-6 Front/ Rear Roller Replacement

1 Use Phillips head screwdriver to loosen 2 screws on the rear adjustment base.

83 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 85 ===
<!-- render-vs-extraction: 44 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2 Use M6 L Allen wrench to loosen 2 screws on the rear roller.

3 Remove motor cover, use 14mm T-shaped socket wrench to loosen 4 screws. Use 14mm open end wrench to loosen
1 belt tension screw and loosen drive belt.

4 Use 13mm wrench to loosen front roller screws, remove front and back rollers, and replace with new. Reassemble in
reverse order of disassembly.

5 When reassembled, running belt tension needs to be adjusted and centered.

84 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 86 ===
<!-- render-vs-extraction: 20 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
6 Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area

85 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 87 ===
<!-- render-vs-extraction: 39 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
11-7 Running Deck/ Belt & Cushion Replacement(Please take the cylinder before replacement)
1. After running board has been folded, use M5 Allen wrench and 12m/m wrench to remove securing screws on cylinder
and remove the cylinder.

86 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 88 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. Use the cross screwdriver to remove the 2 umbrella head cross screws, and use the cross screwdriver to remove the
4 Chinese face tapping screws of the left and right decorative strips, and then remove the decorative strip according
to the direction of the arrow.

87 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 89 ===
<!-- render-vs-extraction: 51 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. User Phillips head screwdriver to remove the 8 screws securing the running board. Remove the running board and
replace running board or running belt. If cushions need to be replaced, remove 6 cushions and replace. Reassemble
in the reverse order as disassembly. When reassembled, running belt tension needs to be adjusted and centered.

4. Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area
between 70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.

88 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 90 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11-8 Speed Sensor Replacement(including the wire)

First remove motor top cover.
Remove speed sensor wiring and proceed with parts replacement.
After replacement, a test to check if the sensor registers the magnet is required.

89 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 91 ===
<!-- render-vs-extraction: 27 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
11-9 Incline Motor Replacement

1. First adjust treadmill to folded position, then proceed with old incline motor replacement.

aes |

SL / /
—

——= oy

. SE ~

90 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 92 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. Incline Range must be adjusted to 195 mm minimum prior to installation.
ime |

KG

—

i}
d

= ()

91 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 93 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
3. Use14 wrench to assemble new incline motor.

92 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 94 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS 66

J9]/O1]UOD YUM BULIM JOJOW SUIJOUI}O8UUOD “PF
