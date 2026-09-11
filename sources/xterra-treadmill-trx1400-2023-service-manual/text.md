<!-- Source: TRX1400 (T3-NT053-01)  Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

   XTERRA
  TRX1400
 T3-NT053-01
   Treadmill
Service Manual
-------------------------------------------Table of Contents----------------------------
                       1. T3 Treadmill Outlines
                       2. Electronic Parts
                           2.1 Upper Controllers
                           2.2 Lower Controller and driver
                       3. Electrical Configuration
                       4. T3 Treadmill Operation
                       5. T3 Treadmill Unit Block Diagrams
                       6. T3 Treadmill Basic Connections and Wiring
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
                       8. T3 Treadmill Error Messages / Troubleshooting for Electronic Issues
                           8.1 Error Message: E0
                           8.2 Error Message: E1
                           8.3 Error Message: E2
                           8.4 Error Message: Err/E3
                           8.5 Error Message: E4
                           8.6 Error Message: E5
                           8.7 Error Message: E6
                           8.8 Error Message: E7
                           8.9 Circuit Diagram
                           8.10    Calibration Procedure
                       9. Folding/Unfolding and Transport
                       10. General Maintenance
                           10.1    Tread Belt and Deck
                       11. Installation of the Incline Motor
                       12. Disassembling and assembling of parts
                          12.1 Lower Controller replacement
                                                              3                                 Service Manual
12.2 Console Replacement
12.3 Motor Replacement
12.4 Breaker Replacement
12.5 AC Power Switch Replacement
12.6 Front/ Rear Roller Replacement
12.7 Running Deck/ Belt & Cushion Replacement
12.8 Incline Motor Replacement




                                   4            Service Manual
Special Note on T3CEGS version:
Besides normal version, T3 treadmill is with a CE/GS version. Both versions are with exactly the same in functions and outlines except that the
power input is 110AC for normal version versus 230VAC for CEGS version and an additional Filter Choke circuit is added for CEGS version as
shown in the circuit diagram on next page.




                         T3-NT053 110V




                                                                       5                                                       Service Manual
1. T3 Treadmill Outlines




             6             Service Manual
   電子錶(含安全開關、喇叭)
Console Assembly
                              Speed/Hand
                              速度開關與手握心跳
                              Pulse Complex
                              複合組


           Incline/Hand
            揚升開關與手握心跳
            複合組 Complex
           Pulse




                          7                Service Manual
                                   Drive Motor
                   Incline Motor
                                       馬達
Motor Controller      揚升馬達
  下控板
Board

                       8                         Service Manual
2. Electronic Parts




         9            Service Manual
2.2.   Upper Controllers




                           Console




                                     10   Service Manual
2.2. Lower Controller and Driver




                 Speed Sensor




        .
                                   Lower Controller Area


                                              11           Service Manual
3. Electrical Configurations




             10                Service Manual
SAFETY KEY:
The safety key fits into the Console to activate all functions and treadmill. Without safety key, console cannot be controlled and treadmill will not be
activated.


CONSOLE:
Interface that controls all functions of the treadmill.


MAIN CONTROLLER:
The circuit board consist of the DC power supply for console, Incline driver and DC motor driver, links the console to output appropriate voltages for
motor for controlling the treadmill functions.


TREADMILL MOTOR:
This is a DC motor with variable speed. Control the 0 –90 (or 0-180) voltages from the main controller to increase or decrease speed of the running
belt.


INCLINE MOTOR:
This is an AC motor, used to control variable elevation through the console within main controller.




                                                                        11                                                              Service Manual
GENERAL INFORMATION
CONSOLE
 Contains keys、 LCD Display、Speaker、Fan、. Hand Pulse Grip、Safety key, etc.
 Main controller includes power supply, motor driver, control circuit and incline control circuit、Speed sensor, etc.
 The 220V (or CEGS) of Lower Controller Area has Filter and Chock.

TREADMILL MOTOR
DC motor with variable speed range 0-90 or (0-180) volt. Requires three wires connection: red, black and green.
The Red wire is inserted into M+.
The White wire is inserted into M-.
When voltage is higher and higher, the motor will be faster.
The green wire is grounding wire.

INCLINE MOTOR
This is a 110 or 230 volt AC motor.

All of five wire connection: red, black, white, green, and has one of 3 pins cable for position sensor.

If there is AC voltage on the Red wire (UP), the incline motor will increase the incline.

If there is AC voltage on the Black wire (DOWN), the incline motor will decrease the incline.

The White wire (COM) is neutral.
The green/yellow wire is grounding wire.




                                                                        12                                             Service Manual
4. T3 Treadmill Operation




           13               Service Manual
Display Windows




                  LCD Display




                  14            Service Manual
LCD LAYOUT




     15      Service Manual
Operation
Window Display Mode
   OFF Mode
        When user doesn’t insert the SAFETY KEY on the console, the treadmill will appear E0.
   READY Mode
        When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program profile name and cycle. Press START
   button to start treadmill on Manual Mode.
   SLEEP Mode
        In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
   RUN Mode
        In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly.
Function
   SPEED
      Display the current speed in Kilometer or mile per hour.
      DISPLAY range is 0.0 to 99.9
      WORK range is 1.0~16.0KM or 0.5~10Mile.
      Press “FAST” or” SLOW” to adjust speed, each increment and decrement is 0.1 km/h (mph).

   Incline
        Display the incline position from 0 to 10
        DISPLAY range is 0 to 99.9.
        WORK range is 0 to 10.
        INCLINE preset value is 0 to 10.
        Press “UP” or” DOWN” to adjust incline, each increment and decrement is 1.
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
     DISPLAY range is 0.0 to 9999.
     WORK range is 0.0 to 999.
 PULSE
     Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be worn.
     DISPLAY range is 0 to 999.
     WORK range is 40 to 220 BPM.
     In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds then display value will become “0”.
PROGRAM
      Display the current program item.
      Display range is 000 to 999.
      Work range is 0, P01 to P24, HRC (H-1).
      When press once Program key, then display will appear one mode, it can appeared P01 to P24, HRC (H-1) modes.




                                                                   17                                                Service Manual
Function Button Locations Function Button Locations




                                                                                          Speed quick
                       Incline quick                                                       keys 3/6/9
                      keys 3/6/9                                                             (MPH)




                                       Incline                                    Speed
                                       Up/                                        Fast/
                                       Down                                       Slow

            Speaker                                                                                Speaker




                            ENTER KEY            STOP Key   Safety   START Keys    PROGRAM KEY
                                                             Key
Function Button in the Main Mode
  READY MODE
     SAFETY KEY: Fit safety key in right position to power on the computer. When safety key is pulled away from its position, the computer will be
     automatically shut down and appear E0.
     STOP button: Press holding this key 3 seconds, the display will reset.
     START button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on window
     display, then machine starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill starts at program preset value in PROGRAM.
     ENTER button: Press “ENTER” button to change each function. In idle mode can set using time, distance and calories. Pre-set PROGRAM can
     set using time and speed, Heart Rate Control (HRC) can set time, age and the value of heart rate.
     FAST button: If user doesn’t enter a setting then this button is non-functional.
     SLOW button: If user doesn’t enter a setting then this button is non- functional.
     UP button: If user doesn’t enter a setting then this button is non- functional.
     DOWN button: If user doesn’t enter a setting then this button is non- functional.
     RAPID button: Non-function.
     PROGRAM KEY：
     Press PROGRAM keys (▲/▼) to choose whichever you want. And then confirm the every setting by pressing ENTER key, finally, press START
     key to do exercise.
     The program function has 24 programs (P1 to P24), and also has H-1 and H-2.




                                                                         19                                                         Service Manual
RUN MODE
  SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down and appear E0.
  STOP button: press “STOP” button to stop treadmill.
  START button: non-functional.
  ENTER button: The function can took turn showing calories and distance.
  FAST button: Press the button to increase your speed and each increase is 0.1KPH (0.1mph). If button is pressed continuously then
  speed increases to MAX SPEED quickly.
  SLOW button: Press the button to decrease your speed and each decrease is 0.1KPH (0.1mph). If button is pressed continuously then
  speed decreases to MIN SPEED quickly.
  UP button: Press the button to raise position and each increase is 1. The maximum incline position is 10.
  DOWN button: Press the button to lower position and each decrease is 1. The minimum incline position is 0.
  RAPID button: Total 6 preset buttons for rapid speed and incline next to the display right side and left side.
  Rapid speed buttons: 3, 6, 9. Rapid speed buttons: 3, 6, 9.
  PROGRAM KEY: Non-functional.




                                                                         20                                                   Service Manual
5. T3 Treadmill Unit Block Diagrams




                  21              Service Manual
Treadmill Configuration




                          BULETOOTH




                                      22   Service Manual
6. T3 Treadmill Basic Connections and Wiring




                       23                 Service Manual
6.1 Display Board wire Connections




                                                                                    Heart Module




                           Connection for
                           5-pin Main control
                           wires

                           Connection for Safety key
                                                                                        Connection for
                                                                                        Handrail Pulse




          Connection for
          Bluetooth

                           Connection for
                           KEYBOARD             Connection    Connection for 2-   Connection for
                                                for FAN       pin of AMP power    Wireless heart
                                                              wires               receiver




                                                         24                                              Service Manual
6.2 Display Board PCB Component Locations
  PCB Board Top




                                            25   Service Manual
PCB Board Bottom




                   26   Service Manual
6.3 Driver Board Wire Connections




       AC POWER
          INPUT                                                                          M–
      (110V or 220v)                                                                     black wire of
                                                                                         motor

                                                                                         M+
                                                                                         red wire of
This area are Incline                                                                    motor
power output socket
Com: white incline
power wires.
UP: red incline power
wires.
DOWN: black incline
power wires.
                                                                                          Speed sensor
                                                                                          socket connected
                                                                                          (2-pins)




                                                                     Incline VR socket
                                         MAIN control wires socket
                                                                     connected
                                         connected



                                    27                                                         Service Manual
6.4 Driver Board PCB Component Locations




                                           28   Service Manual
6.5 Driver Board LED Indicator Locations




                                                            INFO
                                                            LED
                                                Power LED




                                           29                      Service Manual
6.6 Controller Indicator LED debugging

     Indicator        FUNCTI                      Condition                          Reason                             Solve
       LED              ON
     POWER       Controller power        If DC voltage is normal, it        Voltage is not correct.        Check the supply voltage is
                                         would be always ON. If off,        Fuse is blown.                 110V(or 220V). Replace Fuse.
                                         fault condition exists.            Transformer is no              Replace controller.
                                                                            good.

     INFO        Whether lower control   If lower control board does        It is a signal indicate LED,   Check main control wires, may be
                 board Link to upper     not Link to upper console          the INFO LED does not          broke.
                 console control board   control board, the INFO LED        light represent the lower      Replace controller or upper console
                 or not.                 does not light.                    control board was not          board.
                                                                            Received upper console
                                                                            board signal.




                                                                       30                                                              Service Manual
6.7 Driver Board function



                               Bridge                                  IGBT

                      L

                                                     Filter                                 M-
                          FUSE                     capacitor

                      N
                                                                                            M+
          Varistor                       X capacitor
                                        (Safety CAP.)

                COM

                                        RELAY
                 UP
                          INCLINE
                          RELAY                         TRANCEFORMER
                                                                                             SPEED
                                                                                             SENSOR
               DOWN

                                                                                  INCLINE
                                                                          MAIN    VR
                                                                        CONTORL
                                                                          LINE




                                                            31                                   Service Manual
7. Product Safety Instructions




              32                 Service Manual
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
     grounded outlet, (shown below) can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from the adapter, must
     be connected to a permanent ground such as a properly grounded
     outlet box cover. Whenever the adapter is used, it
     must be held in place by a metal screw.




                                                                                33                                                                 Service Manual
   8. T3 Treadmill Error Messages /
Troubleshooting for Electronic Issues




                  34              Service Manual
•       Error code items：

                   Error Message Explain
                            E0    Safety keys dose not insert the safety module. Or safety module is broken.
                            E1    Display board CPU did not receive the RPM signal.
                            E2    Over current, over limit current of lower controller and motor.
                            Err   The console board is not detecting the VR voltage value, or the incline’s motor no power.
                            E4    Power wires of motor error.
                            E5    Communication signal error.
                            E6    Lower controller error.
                            E7    Input power error.


    •   Prepare：


                                                            Picture                            Tool name




                                                                                                Multi-meter




                                                                               35                                             Service Manual
8.1 Error message: E0
   Definition: Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken.
   Configuration:

                                     Console

                                                                                                   Lower controller
                                 SAFETY MODULE                       (+12V) signal via S/W
                                                                     of Main control line
                                                                     form a safety switch
                                                                     loop.

                                        SAFET
                                        Y KEY


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




                                                                          36                                                             Service Manual
8.2 Error Message：E1
    Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed
    RPM sensor, but when the Calibration which it is a necessary.)
•   Configuration：




                                    Send and receive
                                     speed signal via
                                     TX/RX of 5-pin Main
                                     line.




                                                                      37                                                      Service Manual
Cause of E1
The motor doesn’t turn：E1 appears.
        ■   Explanation:
            ◆ The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor
                signal.
            ◆ Configuration




                                              Send and receive
                                              speed signal via
                                              TX/RX of 5-pin Main
                                              line.




                                                                         38                                                           Service Manual
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
  message     Possible cause            Things to check      Solution




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
    •      8.3 Error Message：E2/OVER CURRENT
    •      Definition: When lower board detect over current, then LED light up and display appear “E2”.
            The means is lower board need to protect itself and motor. Prevent lower board and motor is burned.
    •      Solve over current:
           First, check whether smear Silicone oil or not. And then when during the using treadmill, do not
           block belt running. If aforementioned did not process problem, suggest Replacing lower control
           board or Replacing motor.

•       8.4 Error Message: Err or E3
•       Definition: The console board is not detecting the VR voltage value, or the voltage value hasexceeded
        the range.” Err or E3” appears on the display.
•       Configuration：




                                          The incline VR
                                          single via TX/RX of
                                          Main control lines
                                          sent and receive.




                                                          44                                  Service Manual
Case of Err
Incline VR value exceeds the range. Err appear on the display.
       ◆ Incline motor isn’t operation up or down, making the VR value exceed the range.
       ◆ After turning on the unit, the display board detects that the incline VR voltage exceeds the
           range, so Err appears.
       ◆ Action Flow Chart




                                                45                                    Service Manual
 •      Troubleshooting
Part                       Troubleshooting
       Display board       1.Check Incline keys whether key stuck or not.
     Incline power cable   1. Inspect the wires connections.
               &
                           2. Inspect whether wires are broken or crimped.
       incline VR cable
                           3. Replace the wires and test again.
        Driver board       1. Replace the driver board.




                                                     46                      Service Manual
•   Test configuration. The console to driver board connector pin define function




                               Pin 1   SW
                               Pin 2   VDD
                               Pin 3   TXD
                               Pin 4   RXD
                               Pin 5   GND




                                                    47                              Service Manual
•   Test Configuration. Incline motor control function relate parts location




                      Com-white
                                                                Incline
                                                      One of 3-pin VR wires
                      UP-Red                           (It is a position line)

                                         GND
                                         SENSOR PIN (AD)
                      DOWN-black         +5V VCC




                                    49                                      Service Manual
Test Procedure：
  1.   Run calibration again.
  2.   Does the incline motor move at all?
  3.   If no, do the Up/down lights on the incline board light?
  4.   If they light, do the relays click on?
       ◆    If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the
            voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which
            direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the
            same as the mains voltage ~ 110VAC (230VAC). If the voltage is present but the motor doesn’t move, then
            the motor is bad.
       ◆    If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay
            most likely).
  5.   If the motor moves, is there a sensor reading on console?
       ◆    The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0
            for lowest incline. The Incline window is a counter that is showing the actual position sensor output. If the
            motor is moving and there is no count occurring in the Incline window then there is a problem in the
            position sensor wiring or circuitry.
       ◆    If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose,
            creating false readings (should not be able to rotate).
            Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the
            two Phillips screws holding it to the motor casting.
            If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If
            everything is tight then the potentiometer could be bad.
       ◆    If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black
            and red wire and there should be a voltage
            between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest
            position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage
            at the white wire, and the voltage changes as the motor moves, but the counter still does not register then
            there may be a bad wire connection between the potentiometer and the console.
  6.   Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then
       the wires from the motor to the connector is faulty.
  7.   If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage
       present then there is a problem on the incline board.
       There are no electronic components on the board for this signal; there are just circuit connections from the
       potentiometer connector to the console connector.
       The only problems that are possible are a bad solder joint or broken circuit on the board.
       ◆    Console connector wiring, these connections are the same on the incline board and at the console.
                  ■     Pin 1 = 5vdc
                  ■     Pin 2 = position signal 0~5vdc
                    ■    Pin 3= ground
  8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no
       voltage there, but is there at the incline board then check the entire cable from incline board to console for cuts
       or bad connection at the inline connectors.
  9.   If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a
       problem with the console.




                                                              59                                            Service Manual
Error Message： Err
Definition: During incline action, the display board CPU cannot read the VR value, so Err appears.
Configuration：




                       INCLINE Signal
                       via TX/RX of
                       Main control
                       line sent and
                       receive.




                                              Incline drive power   Incline drive power




                                                50                                        Service Manual
 Cause of INCLINE Err
     Press the incline UP/DOWN key. The incline doesn’t operate. Err appears on the display.
Explanation
     When press incline key, the display board CPU reads the incline VR value. If there is no VR value
     change to the CPU, the incline is not operating, and then appear Err appears on the display.
Action Flow Chart:




                                                  51                                    Service Manual
Troubleshooting
Part            Troubleshooting
                1. Press incline keys, see the display weather appear value or not.
Display board       If no values, please check keys weather keys stuck or not, or replace
                    upper control board.
                1. Inspect whether the incline power wires and incline VR cable are
Incline cable
                   connected well.
Driver board    1. View the lower control board whether had Components of incline part
                  obvious and serious damage.

                  1. Inspect whether the incline motor is stuck.
                  2. Inspect whether the incline gears are cracked.
Incline motor
                  3. Test whether the incline motor has a broke circuit.
                  4. Recalibrate the incline set.




                                          52                                   Service Manual
8.5 Error Message：E4
Definition: Motor power wires error.
Configuration:




                           Signal via
                 RPM or    TX/ RX of        Send
                  Motor    main control     command of
                  signal   wires.           start or speed
                 return.                    signal.




                                                Power of Motor
                                                (90DCV or
                                                180DCV)




Cause of E4:
     Power wires of Motor does not insert lower controller.


 Troubleshooting
 Part                      Troubleshooting
 Lower controller          Insert power wires of motor.
 Motor                     Replace Motor.
 Display board             Replace upper control board.




                                                    53           Service Manual
8.6 Error Message：E5
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




                                                     54                                     Service Manual
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
 Part                      Troubleshooting
 Lower controller          Insert power wire of motor.
 Display board             Only Replace upper control board.




                                                       55                          Service Manual
8.8 Error Message：E7
Definition: Input power anomaly, possibly too low or too high or unstable.
Configuration:



                                                    Console
    Wall outlet
    AC 110V
    Or
    AC 220V


                                                                   Signal via main
    Overload                                                       control line.
    protection


     Power Switch                             Lower controller


     CE PART or 220V to match
     Filter and Chock.


Cause of E7:
     The wall outlet possibly unstable, cause to treadmill working power does not stable.
     Another problem possibly power part of lower controller board is broken.


 Troubleshooting
 Part         Troubleshooting
 Wall outlet Use Multi-meter transform into AC 1000V to check wall outlet volt whether 110AC or
             220AC or not. And the voltage whether stable or not.
 Lower       Replace Lower controller board.
 controller
 board




                                                   56                                   Service Manual
8.9 Circuit diagram:



                       T3-NT053




                              57   Service Manual
T3-NT053




           58   Service Manual
        8.10 CALIBRATION PROCEDURE
1. Remove the Safety Key.
2. Press and hold down the PROGRAM and at the same time replace the Safety Key.
3. First, setting wheel size diameter is 42 then press Enter.
4. Second, setting minimum speed to 10 and then press Enter.
5. Third, setting maximum speed (if needed) to 160 and then press Enter.
6. Fourth, setting maximum elevation to 10 and then press Enter.
7. Press Start button to begin calibration. The process is automatic; the speed will start up without warning, so do not stand on the belt.




                                                                             54                                                           Service Manual
Troubleshooting procedure matrix
                    Condition                                              Reason                                                Solve
When turn on power, ON/OFF switch isn’t lit.            1 Power cord isn’t plugged into outlet.      1 Plug the power cord into outlet.
                                                        2 Power cord isn’t plug into unit.           2 Plug the power cord into unit.
                                                        3 The voltage of outlet is too low.          3 Check the voltage of outlet.
                                                        4 Plug or connector of power cord is open.   4 Replace power cord.
                                                        5 Connector of power cord is broken.         5 Replace power cord.
                                                        6 Connecting cable disconnected.             6 Check if wires are disconnected, connect it again.
                                                        7 Breaker tripped.                           7 Press the small red button to return to original status.
                                                        8 Breaker is broken.                         8 Replace breakers.
                                                        9 ON/OFF switch is broken.                   9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown    1 Check the voltage of power is 110V or 230V. Replace
                                                       broken on controller.                         controller.
When insert safe key, no display on monitor.            1 Haven’t switch ON/OFF switch.              1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.     2 Insert the safe key on right position.
                                                        3 5-PIN Main control wires not plugged in    3 Please check the wire and connect again.
                                                          properly.                                  4 Replace 5-PIN Main control wires.
                                                        4 5- PIN Main control wires are broken.      5 Replace fuse or controller.
                                                        5 Fuse on controller is blown.               6 Replace varistor or controller.
                                                        6 Varistor on controller is blown.           7 Replace safety key device.
                                                        7. Safety equipment is broken. (open         8 Replace console.
                                                        circuit)
                                                        8 Other components are faulty.
With no safe key but treadmill could display or operate 1 Safety device is broken. (short)           1 Replace the safety key device or console.

 When press “START”, treadmill doesn’t start.           1 Motor M+ or M- wire isn’t connected into   1 Please check and plug again.
                                                          right position.
                                                        2 Motor is broken.                           2 Replace motor or check the wire and connector if it was
                                                        3 Treadmill controller shut down.              broken.
                                                                                                     3 Turn off the AC switch and turn on power again.
Treadmill stops or shuts off by itself.                 1 House breaker tripped.                     1. Reset it.
                                                        2 Treadmill breaker tripped.                 2. Reset treadmill breaker.
                                                        3 Treadmill controller fuse is broken.       3. Replace with new fuse
                                                        4 Treadmill controller shut down.            4. Turn off the AC switch and turn on power again.

After removing safe key, treadmill can’t stop.          1. The safety key device is broken.          1. Replace with new safety key device.




                                                                                    55                                                                Service Manual
LCDs not bright, incomplete or imperfect.              1. LCD light is broken.                       1. Replace with new LCD or console.
                                                       2. Power to console too low.                  2. Check AC power is 110V or 230V.
                                                                                                     3. Check power to console.
                                                                                                     4. Replace lower controller.
LCD displays not bright, incomplete or imperfect.      1. LCD displays are broken.                   1. Replace with new console.
The speed of the belt doesn’t match console display.   1. Console is not calibrated.                 1.Calibrate the console
The incline position doesn’t match console             1 Console is not calibrated.                  1 Calibrate the console.
INCLINE ERR, INCLINE window displays “Err”.            1 Position sensor value of incline motor is   1 Turn off the AC switch and turn on power again.
                                                       wrong.                                        2. Calibrate the monitor.
After pressing “START” button, the treadmill stops     1 Controller is broken.                        1 Turn off the AC switch and turn on power again.
immediately.                                                                                          2 Replace controller and calibrate it.
Erratic pulse display.                                 1. Another chest belt in use around treadmill. 1. Check for other chest belt use around treadmill.
                                                       2. Other magnetic field disturbance.           2. Change the position or direction of treadmill.
                                                       3. Receiver is broken.                         3. Replace with new receiver.
After pressing “START” button, the treadmill stops     Controller was broken.                        Replace with new controller and calibrate it.
immediately.
FAST/SLOW button of SPEED ADJUSTMENT                   1. Maybe keys stuck.                          1. Replace key board.
SWITCH can’t be used.                                  2. Maybe upper control is broken.             2. Replace upper Controller.
Speed button just can press FAST, can’t press SLOW.    3. Maybe lower control is broken.             3. Replace lower Controller.
Speed button just can press SLOW, can’t press FAST.
UP/DOWN button of                                   1. The incline VR or incline power               1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used.               wires not connected properly.                 2. Replace the cable.
Incline button just can press UP, can’t press DOWN. 2. The incline VR or incline power               3. Replace buttons.
Incline button just can press DOWN, can’t press UP.    wires are damaged.                            4. Replace the Incline.
                                                    3. Maybe keys stuck.
                                                    4. Inspect whether the incline                   6. Replace the Incline.
                                                          motor is stuck.
                                                       5. Inspect whether the incline
                                                          gears are cracked.




                                                                                  56                                                                 Service Manual
Hand pulse lost its function.                  1. Hands not on the hand pulse sensors or        1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                   only one hand on sensor.
                                               2. The connector of HANDPULSE W/WIRE             2. Connect the cable again.
                                                  and Console not connected properly.
                                               3. The wires got damaged when connecting         3. Replace with new cable.
                                                  the HANDPULSE W/WIRE and Console.
                                               4. Hand pulse board is broken.                   4. Replace console or Hand pulse board.
Wireless lost its function.                    1. Chest belt not worn properly.                 1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                    oriented correctly.
                                               2. Distance is too far and exceeds range of      2. User chest belt in front of console within 3 feet.
                                                receiver.                                       Replace with new lithium battery type is CR2032.

                                               3. Chest belt battery is weak or dead.
Chest belt too close to the treadmill.         Weak battery.                                    Replace with new lithium battery with type CR2032 .
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




                                                                           57                                                                  Service Manual
9. Folding/Unfolding and Transport




                58              Service Manual
➢ UNFOLDING
  Pull locking knob and hold running deck and lower down to the
  floor.
  (As shown Figure 1.)

➢ FOLDING
  Pull the locking knob with right hand, left hand lift the running
  deck up to 30cm then two hands lift it until it is locked by the
  locking knob. (As shown in Figure 2-3)

➢ TRANSPORT
  Before moving the treadmill, convert the treadmill to the storage
  as described above. Make sure that the Locking Knob is closer
  fully over the frame guide.

     1). Hold the upper ends of the handrails. Place one foot on
         the base .
     2). Tilt the treadmill back until it rolls freely on the rear wheels.
         Carefully move the treadmill to the desired location. To
         reduce the risk of injury, use extreme caution while moving
         the treading. Do not attempt to move the treadmill over an
         uneven surface.
     3). Place one foot on the base, and carefully lower the
          treadmill until it is resting in the storage position. (As
          shown in Figure. 4 )




59                                                                      Service Manual
10. General Maintenance




           60             Service Manual
10.1 Tread belt and Deck
Your treadmill uses a very high-efficient low-friction bed. Performance is maximized when the bed is kept as clean as possible. Use a soft, damp cloth or paper
towel to wipe the edge of the belt and the area between the belt edge and frame. Also reach as far as practical directly under the belt edge. This should be done
once a month to extend belt and bed life. Use water only - no cleaners or abrasives. A mild soap and water solution along with a nylon scrub brush will clean the top
of the textured belt. Allow the belt to dry before using.

Belt Dust - This occurs during normal break-in or until the belt stabilizes. Wiping excess off with a damp cloth will minimize buildup.

General Cleaning - Dirt, dust, and pet hair can block air inlets and accumulate on the running belt. On a monthly basis: vacuum underneath your treadmill to
prevent buildup. Once a year, you should remove the black motor hood and vacuum out dirt that may accumulate. UNPLUG POWER CORD BEFORE THIS TASK.

BELT ADJUSTMENTS:
Tread-belt Tension Adjustment - Adjustment must be made from the rear roller. The adjustment bolts are located at the end of the step rails in the end caps, as
noted in diagram below.




     Tracking /
      Tension                                                                            Tracking / Tension
 Adjustment                                                                              Adjustment


                     Note: Adjustment is through small hole in the end cap.




                                                                                    61                                                              Service Manual
Tighten the rear roller bolts only enough to prevent slippage at the front roller. Turn both tread-belt tension adjustment bolts in increments of 1/4 turn each and
inspect for proper tension by walking on the belt at a low speed, making sure the belt does not slip. Keep tensioning the bolts until the belt stops slipping.

   •   If you feel the belt is tight enough, but it still slips, the problem may be a loose Motor drive belt under the front cover.

DO NOT OVERTIGHTEN – Over tightening will cause belt damage and premature bearing failure.



TREADBELT TRACKING ADJUSTMENT:
The performance of your treadmill is dependent on the frame running on a reasonably level surface. If the frame is not level, the front and back roller cannot run
parallel, and constant belt adjustment may be necessary.

The treadmill is designed to keep the tread-belt reasonably centered while in use. It is normal for some belts to drift near one side while the belt is running with no
one on it. After a few minutes of use, the tread-belt should have a tendency to center itself. If, during use, the belt continues to move toward one side, adjustments
are necessary.

TO SET TREADBELT TRACKING:
A 10 mm Allen wrench is provided to adjust the rear roller. Make tracking adjustments from the left side only. Set belt speed at approximately 3 to 5 kph.
Remember, a small adjustment can make a dramatic difference!

Turn the bolt clockwise to move the belt to the right. Turn the bolt only a 1/4 turn and wait a few minutes for
the belt to adjust itself. Continue to make 1/4 rotation turns until the belt stabilizes in the center of the
running deck.

The belt may require periodic tracking adjustment depending on use and walking/running characteristics.
Some users will affect tracking differently. Expect to make adjustments as required to center the tread-belt.
Adjustments will become less of a maintenance concern as the belt is used. Proper belt tracking is an
owner responsibility common with all treadmills.




                                                                                     62                                                                 Service Manual
ATTENTION:
DAMAGE TO THE RUNNING BELT RESULTING FROM IMPROPER TRACKING /
TENSION ADJUSTMENTS IS NOT COVERED UNDER THE WARRANTY.


BELT/DECK LUBRICATION
   First, you want to clean between the belt and deck to remove any debris that may be trapped. Use a clean, non-fraying rag, t-shirt, or light towel. Halfway
   between the end of the treadmill and motor cover, shove the garment under the belt until you can grasp it on both sides of the belt. Drag the garment the length
   of the entire belt 1-2 times. Remove the garment.

   Do not lubricate with anything other than approved lubricant. Your treadmill comes with one tube of “Lube” and extra tubes can be ordered directly from or your
   authorized dealer. You may also use a Lube-n-Walk kit that can be purchased through both aforementioned sellers.

   Keeping the deck lubricated at the recommended intervals ensures the longest life possible for your treadmill. If the lubricant dries out, the friction between the
   belt and deck rises and places undue stress on the drive motor, drive belt and electronic motor control board, which could result in catastrophic failure of these
   expensive components. Failure to lubricate the deck at regular intervals may void the warranty.

   The belt & deck come pre-lubricated and subsequent lubrication should be performed every 90 hours of use or if you notice that the deck is dry. It is
   recommended that you reach between the belt and deck to verify there is lubrication present, every other month.




                                                                                  63                                                                  Service Manual
10.2. Service Troubleshooting Checklist – Diagnosis Guide

Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common problems that may
not be covered under the treadmill’s warranty.

PROBLEM                          SOLUTION/CAUSE

Display does not light                        1) Tether cord not in position.
                                              2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                              3) Plug is disconnected. Make sure plug is firmly pushed into 220 VAC wall outlet.
                                              4) Breaker panel circuit breaker may be tripped.
                                              5) Treadmill defect. Contact your dealer.

Tread-belt does not stay centered             The user may be walking while favoring or putting more weight
                                              on either the left or right foot. If this walking pattern is natural,
                                              track the belt slightly off-center to the side opposite from the belt
                                              movement.

Treadmill belt hesitates when walked/run on   See General Maintenance section on Tread-belt Adjustment.
                                              Motor drive belt may be loose.




                                                                                       64                                                         Service Manual
Treadmill will only achieve approximately       This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord.
10 kph but shows higher speed on display        If an extension cord is required it should be as short as possible and heavy duty 16 AWG minimum. Low household voltage.
                                                Contact an electrician or your dealer. A minimum of 220 volt AC current, 50 hz is required.


Treadmill trips on board 15 amp circuit           High belt/deck friction. See General Maintenance section on Belt/Deck Lubrication..

Computer shuts off when console is                Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to section 7.3 for Grounding Instructions.

touched (on a cold day) while walking/running

House circuit breaker trips, but not the          Need to replace the house breaker with a “High inrush current” type breaker (see section 7.2 for Important Electrical
treadmill circuit breaker.                        Instructions.)

Treadmill with noises                           1. If the noise is coming from the rollers, .
                                                2. If the noise is coming when the user is running on the treadmill with lowest level of incline , it could be due to too much
                                                pressure with the incline cylinder. (only in case of the lowest incline level).
                                                3. If there is knocking noise during the workout, check and make sure all bolts are tightened.
                                                4. When there is thumping noise while the belt is running. This happens with a brand new treadmill or when the treadmill has
                                                not been used for a long time. This is due to the belt has been shaped with rollers and harden because of low temperature.
                                                Running the belt for tens of minutes the thumping noise will gradually go away.

Noise under motor cover.                        1. Worn brushes or bearings on motor. Replace with new motor brushes.
                                                2. Front roller bearings are defective. Replace with new front roller.
                                                3. Drive belt is misadjusted (too tight or too loose). Adjust motor position.

Noise in the rear of the treadmill.             1. Rear roller bearings are defective. Replace with new rear roller
                                                2. Rear roller misaligned.    Adjust rear roller position.

Tread belt hesitates while being                1. Insufficient lubricant on tread belt.
stepped on.                                      2. Tread belt tension insufficient

Black particles collecting under                Drive belt is breaking in. Vacuum under treadmill periodically.
treadmill.




                                                                                           65                                                                    Service Manual
11. Installation of the Incline Motor




                  66               Service Manual
Incline Range must be adjusted to 165mm minimum prior to installation.




                                  67                                     Service Manual
12. Disassembling and
 Assembling of Parts




          68            Service Manual
12-1   Lower Controller Replacement
       1.   Use Phillips head screwdriver to remove 4 Button Head Socket Bolts from the Motor Top Cover.




       2.   Disconnect all lower controller wirings, Replace with new lower controller and reconnect all wirings.




                                                                       69                                           Service Manual
12-2   Console Replacement
       1.   Use M5 L Allen wrench to remove 4 Button Head Socket Bolts from the console support




                                                                  70                              Service Manual
2.   Disconnect console wirings and replace with new console.




                                                            71   Service Manual
12-3   Motor Replacement
       1.   Use Phillips head screwdriver to remove 4 Sheet Metal Screw the motor cover.




       2.   Remove motor grounding wire (greenish yellow), motor wire (+) red and motor wire (-) black.




                                                                    72                                    Service Manual
3.   Use 14mm T-shaped socket wrench to loosen 4 screws, use 14mm open end wrench to loosen 1 belt tension screw, remove motor
     and replace with new. Reassemble in reverse order of disassembly, re-hook belt (readjust belt to be parallel with main frame after re-
     hooking). Do not tighten 4 securing screws yet.




4.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between 70-75LBS. Use
     14mm T-shaped socket wrench to secure and tighten 4 securing screws. Connect grounding wires and motor wires (red M+, black M-)




                                                               73                                                          Service Manual
12-4   Breaker Replacement
       1.   Remove Breaker connection wiring, replace part and reconnect wiring.




12-5   AC Power Switch Replacement
       1.   Disconnect wiring to AC power switch, replace AC power switch and reconnect wiring.




                                                                   74                             Service Manual
12-6   Front/ Rear Roller Replacement
       1.   Use Phillips head screwdriver to loosen 2 screws on the rear adjustment base.




       2.   Use M5 L Allen wrench to loosen 2 screws on the rear roller.




                                                            75                              Service Manual
3.   Remove motor cover, use 14mm T-shaped socket wrench to loosen 4 screws. Use 14mm open end wrench to loosen 1 belt tension
     screw and loosen drive belt. Use 11mm wrench to loosen front roller screws, remove front and back rollers, and replace with new.
     Reassemble in reverse order of disassembly. When reassembled, running belt tension needs to be adjusted and centered.




                                                            76                                                         Service Manual
4.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between 70-75LBS. Use
     14mm T-shaped socket wrench to secure and tighten 4 securing screws.




                                                           77                                                      Service Manual
12-7   Running Deck/ Belt & Cushion Replacement (Please take the cylinder before replacement)
       1.   After running board has been folded, use M5 L Allen wrench and 12m/m wrench to remove securing screws on cylinder and remove
            the cylinder
       2.   Perform step #12.6 and remove front and rear rollers.




       3.   Take down foot rail tablet and according to the arrow direction to remove foot rail. Cleaning the foam tape from foot rail and running
            deck.




                                                                      78                                                           Service Manual
4.   User Phillips head screwdriver to remove the 8 screws securing the running board. Remove the running board and replace running
     board or running belt. If cushions need to be replaced, remove 6 cushions and replace. Reassemble in the reverse order as
     disassembly.




5.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between 70-75LBS. Use
     14mm T-shaped socket wrench to secure and tighten 4 securing screws.




                                                            79                                                       Service Manual
6.   Prepare a double-sided foam tape (1Tx10mmx1170L)*4pcs, each of foot rails need to be affixed with two foam tape as the arrow
     shows.




7.   And then paste foot rail on the running deck.




                                                            80                                                        Service Manual
12-8   Incline Motor Replacement
       1.   First remove the motor cover and adjust treadmill to folded position, then proceed with old incline motor replacement.




                                                                     81                                                              Service Manual
2.   Incline Range must be adjusted to 165mm minimum prior to installation.




                165


3.   Use 14mm wrench to assemble new incline motor.




                                                            82                Service Manual
4.   Connect incline motor wiring with controller




                                               Red
                                               紅色連接 wire Connect
                                                         UP端 to
                                               “UP”
                                               White wire Connect to
                                               白色連接COM端
                                               “COM”
                                               Black wire Connect to
                                                黑色連接DOWN端
                                               “DOWN”




                                                             83        Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jenuepy 8dIAlEas
/upead |

LO-ESOLN-EL
OOVLXYL
Vodsalx


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 33 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
12.2 Console Replacement

12.3 Motor Replacement

12.4 Breaker Replacement

12.5 AC Power Switch Replacement

12.6 Front/ Rear Roller Replacement

12.7 Running Deck/ Belt & Cushion Replacement
12.8 Incline Motor Replacement

4 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Special Note on T3CEGS version:

Besides normal version, T3 treadmill is with a CE/GS version. Both versions are with exactly the same in functions and outlines except that the
power input is 110AC for normal version versus 230VAC for CEGS version and an additional Filter Choke circuit is added for CEGS version as
shown in the circuit diagram on next page.

(31G0GIW) 318V9 YALNdWOO +,

Nids CC m
i
=
= Z|
Ww
pm
YIM GNNOYS cc
5 = R o a =. SHIM SLIHM ws
o A>reoO Jum Gad ) w
O < JEIM NOW TE - 2 S
uy O | | | | | F1GVO HA ANMONI Nid-€] Sia ° 5
Or IT TT | YAONI | O[5 Z| <2
= -nNOMTW a)
as
oc =
S - Ww <| Oo —
~— @& * c
~~ A 5 57k
5S ! a
e 3YIM MOV1E = Q| |S
<< | —samsore—! 1
am
' =
oD Q
ee C] a wl | | 3
- ey} 3
=| 5s oc )
El & O +X
3} 5 =
—— fe)
E =

1

5 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
Console Assembly ~ Speed/Hand

Pulse Complex

Sa

Incline/Hand
Pulse Complex

7 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
vm)

Drive Motor

Motor Controller
Board

Incline Motor

8 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jOnUuDPY AI1ALIG

MT

g|OSUOD

HIISLXRy

$19]|01]U04 1addp

‘oS


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
2.2. Lower Controller and Driver

Ne Lower Controller Area _/

I Service Manual

=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
i EE
y eae “d a

&&2
72

des
Ni
fi =A 26

. F: 7


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jonuvyy 291A4a¢ SI

INOAV1 G91


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jonUuDYY 9I1A1dS

sweibeig YIO/g Hup [flwpeatL EL "Ss


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 34 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
Treadmill Configuration

KEY =» WIRELESS HR
RECEIVER
COOLING DISPLAY BOARD
SAFETY KEY

HR | SPEAKER
HANDLEBAR LR

AMPLIFIER
LINE IN
BULETOOTH

=) MOTOR
INCLINE
CURRENT DRIVER BOARD MOTOR
BRAKER
K VR SET

POWER Fi 7
BOWER ==> SWITCH

RPM
SENSOR

22 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.1 Display Board wire Connections

Heart Module

i . “a ‘i a ea mitt
Connection for aris | IgoseaA0W0
5-pin Main control rat
wires

Connection for
Handrail Pulse

Connection for
Bluetooth

Connection for ;
KEYBOARD Connection | Connection for 2- Connection for
for FAN pin of AMP power Wireless heart

receiver

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
6.2 Display Board PCB Component Locations
PCB Board Top

25 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
PCB Board Bottom

cS

D8 MOAne
- MIRE RK -ADHS EeART ANS
by Wh ‘isang
103 GLA
: — a! te

: Service Manual


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 46 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.3 Driver Board Wire Connections

AC POWER 0666 066

INPUT ae M—
(110V or 220v) (* oe 1 = black wire of
rY A oO motor
— | a: -
8 a sa” = red wire of
This area are Incline e i eco | - —»| motor
power output socket 6 eee H
Com: white incline € ” ee CO -" =
power wires. se ae . = <= 2 oe of\e0
veges incline power a == nnn mm mm HOCUCURROOCORRRROOON Coneons
At Loon | an r a5
DOWN: back incline eas sree Goodie “GET Tt
. | a
P = ° 7 O 66 aa enee en 0 aL o
@ sn" g == m Speed sensor
e@ @ 5 1. socket connected
ke | | CONS ee 8 © “eo _») (2-pins)
8 7 BH ses i a sees se —
ny tate”? fs - =" mecce: sae

@
o g | na\8
Incline VR socket
connected

MAIN control wires socket
connected

27 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi; re-OCR at 0 degrees after the first pass scored a wrong rotation -->
6.4 Driver Board PCB Component Locations

ber =
=

a
fb TEST t
ie

28 Service Manual

=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6.5 Driver Board LED Indicator Locations

4° Ome be o_o SEED
> >,

~/ 1 mit

Vv, = - a pk:
3 |
: ae ay ee LED | be a ry

ats sey Ve

& Sey

ay

29 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jonUuDYY 9I1A1dS

SUOI]ONASU] AJajesS JONPOlq *Z


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jOnUuDPY AI1ALIG

sanss| 91/U01]9a/F7 404 Buljooysajqnos]
/ sabessayy 4047 jjlupeas, EL "9


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.2 Error Message: E1

Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed
RPM sensor, but when the Calibration which it is a necessary.)

¢ Configuration:

CONSOLE
DISPLAY BOARD

Send and receive |
speed signal via edsg
MOTOR SPEED

. . RPM SENSOR
TX/RX of 5-pin Main SIGNAL SIGNAL

line. | |

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER » DRIVER BOARD

_ RPM
SENSOR

37 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 40 ===
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
TX/RX of 5-pin Main SIGNAL |: BIGNAL

line. | |

MOTOR
VOLTAGE

2 PIN > MOTOR

AC POWER >» DRIVER BOARD

_ RPM
SENSOR

38 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 76 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart

El shoving up >} feset porer -— Press start again

Replace upper console board or
update the progran of upper
console board

Check display whether Countdom
or not after pressing start?

Check main control line
whether split or not?

Replace sain
control Line

Did belt noves after
start?

co Replace lover control driver board

Check RPM sensor
iether well or not?

Replace RPi
sensor

Check lover control
driver board weather
enough Power?
(AC: 2201)

[se multi-neter to
Check Vain control line
socket pin? & pind 1s
N12")

Adjust sensor gap distance to 2am

Did belt moves after
start?

Check poser source from wall weather
stable AC220V or not?

Then, press start and
use multi-neter to
Check driver board

notor socket weather

voltage or not?

\)

IN

IBS

Y
Replace Notor Hp} Solie the problen

40 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 45 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 solution follow chart - check RPM sensor device procedure:

Check RPM sensor
Procedure

Sensor cable connected

property? NO—t| Connect Properly

YES
Y

Move the roller so
thut meagent closest
to the sensor

Make sure the gap
between maynet'sensor less
than 3 mm

NO Adhust sensor
position

YES

y

Replace sensor with
cable

YES—| = Problem fixed
Is function OK?

NO

Replace computer
cuble

‘umm power back ott>
press “start” and

comnidown ts function
OK?

YES—e] Problem fixed

NO

ul

Replace Console

4] Service Manual


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 issue troubleshooting form

E1
message Possible cause Things tocheck Solution
Possible cause Things to check Solution
The upper console check the speed ;
. , Make sure the good connection
board hasn't receive sensor cable is in for cables
any speed signal for 8 good connection
seconds
E1
message
The motor
cannot move Check th
eck the ga
The speed sensor didn't g@P To keep the gap-distance less
. between speed
detect signal completely. than 3 mm.
sensor and magnet.
Check if the sensor
Defective sensor orbad_ jand cables are Change the sensor
cable connection. circuit short or cables.

damaged.

43 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Case of Err
Incline VR value exceeds the range. Err appear on the display.

@ Incline motor isn’t operation up or down, making the VR value exceed the range.

@ After turning on the unit, the display board detects that the incline VR voltage exceeds the
range, so Err appears.

@ Action Flow Chart

( INCLINE VR )
<<

|
y

a
DRIVER BOARD

VR VOLTAGE? N

\

if

CABLE

DISPLAY BOARD

Y

| !

DISPLAY OPERATES ERR APPEARS ON
NORMALLY THE DISPLAY

45 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 48 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test configuration. The console to driver board connector pin define function

a

ol

ne 401 3 GAM TRAMIZT SD8 HAUL

Gerson 4
arr mi aM niall

04210361A0
—_—

7 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 50 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test Procedure:

1. Run calibration again.

2. Does the incline motor move at all?

3. — Ifno, do the Up/down lights on the incline board light?
4. If they light, do the relays click on?

@ = Ifthe relay clicks on but the motor doesn’t move: with the incline light and relay activated check the
voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which
direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the
same as the mains voltage ~ 110VAC (230VAC). If the voltage is present but the motor doesn’t move, then
the motor is bad.

@ = Ifthe light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay
most likely).

5. — If the motor moves, is there a sensor reading onconsole?

@ The INCLINE window will display the computer incline setting (after soeed cal. ends); 15 for max incline, 0
for lowest incline. The Incline window is a counter that is showing the actual position sensor output. If the
motor is moving and there is no count occurring in the Incline window then there is a problem in the
position sensor wiring or circuitry.

@ = Ifthere is acount, but the calibration fails then the position sensor (Potentiometer) could be loose,
creating false readings (should not be able to rotate).

Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the
two Phillips screws holding it to the motor casting.
If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If
everything is tight then the potentiometer could be bad.
@ = If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black
and red wire and there should be a voltage
between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest
position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage
at the white wire, and the voltage changes as the motor moves, but the counter still does not register then
there may be a bad wire connection between the potentiometer and the console.
6. | Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then
the wires from the motor to the connector is faulty.
7. — If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage
present then there is a problem on the incline board.
There are no electronic components on the board for this signal; there are just circuit connections from the
potentiometer connector to the console connector.
The only problems that are possible are a bad solder joint or broken circuit on the board.
@ Console connector wiring, these connections are the same on the incline board and at the console.
mg Pin 1=5vdec
m = Pin 2= position signal 0~5vdc
m ~=©Pin 3= ground
8. If there is voltage at the output connector to the console then check the voltage at the console. If there is no
voltage there, but is there at the incline board then check the entire cable from incline board to console for cuts
or bad connection at the inline connectors.
9. If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a
problem with the console.

59 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Error Message: Err

Definition: During incline action, the display board CPU cannot read the VR value, so Err appears.

Configuration:
—— INCLINE
DISPLAY BOARD é UP'DOWN KEYS UP/DOWN KEYS

INCLINE Signal

INCLINE via TX/RX of INCLINE

VR Main control UP/DOWN

VOLTAGE line sent and SIGNAL

receive.

YZ

+ Incline drive power

Inalina Aria —

INCLINE
MOTOR
DRIVER BOARD eax VR VOLTAGE INCLINE VR SET

50 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 44 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of INCLINE Err

Press the incline UP/DOWN key. The incline doesn’t operate. Err appears on the display.
Explanation

When press incline key, the display board CPU reads the incline VR value. If there is no VR value

change to the CPU, the incline is not operating, and then appear Err appears on the display.
Action Flow Chart:

DISPLAY BOARD

=

or ——— N actign?§———

—
!

DRIVER BOARD

nm

a RANG AP AC HON,
— UIP LED RCTS INCLINI N a

_
VOL. TAG INCREASES —

ae a

y
a.

a “~~
IN PMOWN AC EIN,
DOWN LED LIGLTS.INCLINE = -N- a
~ VCH TAGE DEORE AREA

Sees:
“
!

INCLINE: Morror

Ba

~
> =

ae
— UP LED LIGHTS, om. N a

Oc ee LINE RISES?
pete

a Se
¥

jp oe a

bitin <4
—~ DOWN LED LIGHTS, N -
ING (LINE LOWERS?
cE.

a =F

i?
| y

' SHOW E2/INCLINE ERR
C NO ERR MESSAGE ) ‘« MESSAGE )

—— —_—

51 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 54 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.5 Error Message: E4

Definition: Motor power wires error.

Configuration:
DISPLAY BOARD 4
A 4, EN |
Signal via
RPM or TX/ RX of Send
Motor main control 4 command of
signal wires. start or speed
return. signal.
MOTOR
ss Power of Motor
DRIVER BOARD (90DCV or
14R2NNCV) JA
Cause of E4:

Power wires of Motor does not insert lower controller.

Troubleshooting

Part Troubleshooting

Lower controller Insert power wires of motor.
Motor Replace Motor.

Display board Replace upper control board.

53 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 58 ===
<!-- render-vs-extraction: 55 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8.9 Circuit diagram:

T3-NT053 =. 110V
TREADMILL CIRCUIT DIAGRAM

AC i INPUT | Ce |
|. Qweommannw | a
PLUG =e OY a
=
LW
a
HAND PULSE HAND nase Q

re)
Quick handrail Quick handrail a
button button =
. . . oO
we Main System Pin Define z/2
AC SOCKET TJBREAKER is | @
AC SWITCH 0 SN/
T | Ww i—- SW mF
= 2—- VDD
Ground WHITE vce 8 a—- TAD
a 4—1- RXD
g a IBLACK WIRE 5 _ | GN D
EB INCLINE
: MOTOR
=
5
AC AC
DOWN
CONTROLLER} =op——
nn
M+ M- JK JK
| |
MOTOR RED WIRE
BLACK WIRE 5 PIN COMPUTER CABLE (LOWER)
7 2pin
| esis WIRE —<—<$$—=3 SENSOR WIRE

57 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 59 ===
<!-- render-vs-extraction: 56 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
T3-NT053 220V CEGS
TREADMILL CIRCUIT DIAGRAM

er
AC POWER INPUT
A A a
PLUG Vv Vv a
ll ll 7
Ww
HAND PULSE HAND PULSE zZ
& & <x
Quick handrail Quick handrail
button button Ww
=]
. : a
ein pe Main System Pin Define z|2
(FEMALE) Z15
AC SOCKET [1] BREAKER “i?
AC SWITCH 0 lxU)
ry 7 1—- S/W *\/
2—- VDD
Ground ||| WHITE mei 6 3—- TXD
3 4—- RXD
z- BLACK WIRE 5—- GND
@
: INCLINE
5 MOTOR
2
g
5 FILTER CHOKE
AC AC
DOWN
CONTROLLER| 239
owe
M+ M- JK JK
0
MOTOR RED WIRE
BLACK WIRE 5 PIN COMPUTER CABLE (LOWER)
2pin
| GROUND WIRE 3 SENSOR WIRE
58 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 62 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LCDs not bright, incomplete or imperfect. 1. LCD light is broken. 1. Replace with new LCD or console.
2. Power to console too low. 2. Check AC power is 110V or 230V.
3. Check power to console.
4. Replace lower controller.

LCD displays not bright, incomplete or imperfect. 1. LCD displays are broken. 1. Replace with new console.

The speed of the beltdoesn’t match console display. |1. Console is not calibrated. 1.Calibrate the console

The incline position doesn’t match console 1 Console is not calibrated. 1 Calibrate the console.

INCLINE ERR, INCLINE window displays “Err”. 1 Position sensor value of incline motor is [1 [urn off the AC switch and turn on power again.
wrong. 2. Calibrate the monitor.

After pressing “START” button, the treadmill stops 1 Controller is broken. 1 Turn off the AC switch and turn on power again.

immediately. 2 Replace controller and calibrate it.

Erratic pulse display. 1. Another chest belt in use around treadmill. |1. Check for other chest belt use around treadmill.
2. Other magnetic field disturbance. 2. Change the position or direction of treadmill.
3. Receiver is broken. 3. Replace with new receiver.

After pressing “START” button, the treadmill stops Controller was broken. Replace with new controller and calibrate it.

immediately.

FAST/SLOW button of SPEED ADJUSTMENT 1. Maybe keys stuck. 1. Replace key board.

SWITCH can’t be used. 2. Maybe upper control is broken. 2. Replace upper Controller.

Speed button just can press FAST, can’t press SLOW. |3. Maybe lower control is broken. 3. Replace lower Controller.

Speed button just can press SLOW, can’t press FAST.

UP/DOWN button of 1. The incline VR or incline power 1 Connect the wires again.

INCLINE ADJUSTMENT SWITCH can’t be used. wires not connected properly. 2. Replace the cable.

Incline button just can press UP, can’t press DOWN. /2. The incline VR or incline power 3. Replace buttons.

Incline button just can press DOWN, can’t press UP. wires are damaged. 4. Replace the Incline

; ; 3. Maybe keys stuck, 6. Replace the Incline.

4. Inspect whether the incline » Nepiace tne incine.

motor is stuck.
5. Inspect whether the incline
gears are cracked.

56 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 66 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jPnNUDPY 9I1ALAS

QUUBUDZ]UIP| [P1DUDE) ‘OL


=== OCR SUPPLEMENT, PDF PAGE 78 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
12-3 Motor Replacement
1. Use Phillips head screwdriver to remove 4 Sheet Metal Screw the motor cover.

GoD . Q

|] |
We |

|

2. Remove motor grounding wire (greenish yellow), motor wire (+) red and motor wire (-) black.
LB

| (ll

A # ALS |

oO 9 -

72 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 79 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. Use 14mm T-shaped socket wrench to loosen 4 screws, use 14mm open end wrench to loosen 1 belt tension screw, remove motor
and replace with new. Reassemble in reverse order of disassembly, re-hook belt (readjust belt to be parallel with main frame after re-
hooking). Do not tighten 4 seca ews yet.

aly
TSI)

MT

eo.

4. Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area between 70-75LBS. Use
14mm T-shaped socket wrench to secure and tighten 4 securing screws. Connect grounding wires and motor wires (red M+, black M-)

73 Service Manual
