   ST155
  Treadmill
Service Manual
-------------------------------------------Table of Contents----------------------------
                       1. ST125 Treadmill Outlines
                       2. Electronic Parts
                           2.1 Upper Controllers
                           2.2 Lower Controller and driver
                       3. Electrical Configuration
                       4. ST155 Treadmill Operation
                       5. ST155 Treadmill Unit Block Diagrams
                       6. ST155 Treadmill Basic Connections and Wiring
                           6.1 Display Board Wire Connections
                           6.2 Display Board PCB Component Locations
                           6.3 Amplifier Board Wire Connections
                           6.4 Driver Board Wire Connections
                           6.5 Driver Board PCB Component Locations
                           6.6 Driver Board LED Indicator Locations
                           6.7 Controller Indicator LED Debugging
                           6.8 Driver Board Function
                       7. Product Safety Instructions
                           7.1 Important Safety Instructions
                           7.2 Important Electrical Instructions
                           7.3 Important Grounding Instructions
                       8. ST155 Treadmill Error Messages / Troubleshooting for Electronic Issues
                           8.1 Error Message: E0
                           8.2 Error Message: E1
                           8.3 Error Message: E2
                           8.4 Error Message:E3
                           8.5 Error Message:E4
                           8.6 Error Message:E5
                           8.7 Error Message:E6
                           8.8 Error Message:E7
                           8.9 Circuit Diagram
                           8.10    Calibration Procedure
                           8.11    MAINTENANCE MENU
                       9. Treadmill Folding/Unfolding and Transport
                       10. General Maintenance
                           10.1 Tread Belt and Deck
                       11. Installation of the Incline Motor
                                                               2                                   Service Manual
12. Disassembling and Assembling of Parts
   12.1 Lower Controller Replacement
   12.2 Console Replacement
   12.3 Motor Replacement
   12.4 Breaker Replacement
   12.5 AC Power Switch Replacement
   12.6 Front/ Rear Roller Replacement
   12.7 Running Deck/ Belt & Cushion Replacement
   12.8 Speed Sensor Replacement
   12.9 Incline Motor Replacement




                                       3           Service Manual
Special Note on ST155 CEGS version:
Besides normal version, ST155 treadmill is with a CE/GS version. Both versions are with exactly the same in functions and outlines except that
the power input is 110AC for normal version versus 230VAC for CEGS version and an additional Filter Choke circuit is added for CEGS version
as shown in the circuit diagram on next page.




                                                                      4                                                       Service Manual
1. ST155 Treadmill Outlines




             5                Service Manual
Console

                                   Hand Pulse
                                   Sensor




                                                Speed adjustment
                                                button




          Incline adjustment
          button




                               6                                   Service Manual
                           Motor


             Driving
             Motor
Lower
Controller




                       7           Service Manual
2. Electronic Parts




         8            Service Manual
2.1 Upper Controllers




                        9   Service Manual
2.2. Lower Controller and Driver




                 Speed Sensor




                                   Lower Controller Area
                                             1             Service Manual
                                             0
3. Electrical Configurations




             10                Service Manual
SAFETY KEY:
The safety key fits into the Console to activate all functions and treadmill. Without safety key, console cannot be controlled and treadmill will not be
activated.


CONSOLE:
Interface that controls all functions of the treadmill.


MAIN CONTROLLER:
The circuit board consist of the DC power supply for console、 incline driver and DC motor driver, links the console to output appropriate voltages
for motor for controlling the treadmill functions.


TREADMILL MOTOR:
This is a DC motor with variable speed.      Control the 0 –90 (or 0-180) voltages from the main controller to increase or decrease speed of the
running belt.


INCLINE MOTOR:
This is an AC motor, used to control variable elevation through the console within main controller.




                                                                         11                                                             Service Manual
GENERAL INFORMATION
CONSOLE
 Contains keys、 LCD Display、Speaker、Fan、. Hand Pulse Grip、Safety key, etc.
 Main controller includes power supply, motor driver, control circuit and incline control circuit、Speed sensor, etc.
 The 220V (or CEGS) of Lower Controller Area has Filter and Chock.

TREADMILL MOTOR
DC motor with variable speed range 0-90 or (0-180) volt. Requires three wire connection: red, black and green.
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
4. ST155 Treadmill Operation




            13                 Service Manual
Display Windows

                       7.5” LCD Display




                  14                      Service Manual
LCD LAYOUT




     15      Service Manual
Operation
Window Display Mode
   OFF Mode
        When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the OFF Mode.
   READY Mode
        When the treadmill is ON and SAFETY KEY is inserted in console, the message window will show program profile name and cycle. Press START
   button to start treadmill on Manual Mode.
   SLEEP Mode
        In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.
   RUN Mode
        In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause the treadmill stop instantly and enter OFF Mode.
Function
   SPEED
      Display the current speed in Kilometer or mile per hour.
      DISPLAY range is 0.0 to 99.9
      WORK range is 1.0~16.0KM or 0.5~12Mile.
      Press “FAST” or ”SLOW” to adjust speed, each increment and decrement is 0.1 km/h(mph).

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



                                                                       16                                                           Service Manual
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
    WORK range is 40 to 220 BPM.
    In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds then display value will become “0 ”.




                                                                      17                                          Service Manual
Function Button Locations Function Button Locations
                                                                        FAN




                                                Incline       Program
                                                Up            Up                     Enter
                     Speaker                                                                                Speaker
                                                          Incline       Program          Speed
                                                          Down          Down             Slow




               Incline quick keys                                                                   Speed         Speed quick keys
               1, 3, 5, 7, 9, 12, 15                                                                Fast          2, 3, 4, 5, 7, 9, 12



                                       Display key                                               Fan key


                                                             Start            Stop
                                                             Key              Key
                             Hand Pulse                                                              Hand Pulse

                                        Audio Hole                                   Headphone Hole
                                                                    Safety
                                                                     Key



                        Incline adjustment                                                   Speed adjustment
                        Rapid Key handrail                                                   Rapid Key handrail
Function Button in the Main Mode
  READY MODE
     SAFETY KEY: Fit safety key in right position to power on the computer. When safety key is pulled away from its position, the computer will be
     automatically shut down.
     STOP button: Non-function.
     START button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on window
     display, then machine starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill starts at program preset value in PROGRAM.
     ENTER button: Press “ENTER” button to change each function. MANUAL can set using time, Pre-set PROGRAM can set using time and speed,
     Heart Rate Control 1~2 can set time, age and the value of heart rate. User Program 1~2 can set time, speed and incline.
     Another the function is exchange and poll incline and speed profile appear.
     FAST button: If user doesn’t enter a setting then this button is non-functional.
     SLOW button: If user doesn’t enter a setting then this button is non- functional.
     UP button: If user doesn’t enter a setting then this button is non- functional.
     DOWN button: If user doesn’t enter a setting then this button is non- functional.
     SPEED RAPID button: 7 preset buttons for rapid speed: 2,3,4,5,7,9,12
     INCLINE RAPID button: 7 preset buttons for rapid incline: 1,3,5,7,9,12,15.
     FAN button: It can to control ON/OFF for the fan.
     DISPLAY KEY：
     When during exercise, press the display key will be poll MW (Message window) message.
     PROGRAM KEY：
     Press PROGRAM keys (▲/▼) to choose whichever you want. And then confirm the every setting by pressing ENTER key, finally, press START
     key to do exercise.
     The program function has 6 programs (Manual, Hill, fat burn, Cardio, Strength and Interval), and also has USER1, USER2, TH60 PCT, and
     THR80 PCT.




                                                                         19                                                         Service Manual
RUN MODE
  SAFETY KEY: When safety key is pulled away from its position, the computer will be automatically shut down.
  STOP button: press “STOP” button to stop treadmill.
  START button: non-functional.
  ENTER button: non-functional.
  FAST button: Press the button to increase your speed and each increase is 0.1KPH (0.1mph). If button is pressed continuously then
  speed increases to MAX SPEED quickly.
  SLOW button: Press the button to decrease your speed and each decrease is 0.1KPH (0.1mph). If button is pressed continuously then
  speed decreases to MIN SPEED quickly.
  UP button: Press the button to raise position and each increase is 1. The maximum incline position is 15.
  DOWN button: Press the button to lower position and each decrease is 1. The minimum incline position is 0.
  SPEED RAPID button: Speed will be set to 2, 3, 4, 5, 7, 9, 12, etc, total 7 buttons.
  INCLINE RAPID button: Incline will be set to 1, 3, 5, 7, 9, 12, 15, etc, total 7 buttons.
  Fan button: It can to control ON/OFF for the fan.
  DISPLAY KEY：
  You could select the profile of SPEED or INCLINE by pressing DISPLAY key when selecting the program.
  Press DISPLAY key to switch the exercise data shown on the message window when you are workout. After the switch, the system will scan and
  display automatically every four seconds. The information as below,
        PROGRAM NAME
        LAPS   XX
        VERT     XXX FT (THE METRIC UNITS IS SHOW “M” )
        SEG TIME XX：XX(only in HRC MODE will not show this string)
        MAX SPEED XX：XX (only in HRC and MANUAL MODE will not show this string)

  PROGRAM KEY: Non-functional.




                                                                   20                                                         Service Manual
5.ST155 Treadmill Unit Block Diagrams




                  21             Service Manual
Treadmill Configuration




                          BULETOOTH




                                      22   Service Manual
6. ST155 Treadmill Basic Connections and Wiring




                       23                 Service Manual
6.1 Display Board wire Connections

                                                                 Connection      Connection
                                                                 with FAN        with FAN

       Bluetooth Module



                                                                        Display IC
                                                                                                   Connection with
                                                                                                   Handrail Pulse


                            Main IC


                                                    Display IC


                                                                                                                     Heart Module
                                 Connection with
                                 KEY BOARD
    Connection with
    Wireless heart                                     Connection with                 Connection with
    receiver                                           6-pin Main control wire         2-pin of AMP Line




          Connection with   Connection with        Connection with                   Connection with       Connection with
          Quick speed key   Quick speed            Safety key                        Quick incline         Quick incline key
          board             handrail buttons                                         handrail buttons      board



                                                          24                                                          Service Manual
6.2 Display Board PCB Component Locations
  PCB Board Top




                                            25   Service Manual
PCB Board Bottom




                   26   Service Manual
6.3 Amplifier Board wire Connections




                                       27   Service Manual
6.4 Driver Board Wire Connections




                                                                              M-
                                                                              connected
         AC POWER                                                             with black
            INPUT
                                                                              wire of motor
        (110V or 220v)
                                                                              M+
                                                                              connected
JK80 are Incline power                                                        with red wire
output socket,                                                                of motor
respectively:
Com: This is a
commons power, and                                                            JK60 is Incline VR
connected with white                                                          socket connected
incline power wire.                                                           with incline one
UP: This is able to                                                           of 3-pin VR wire
incline “UP”, and
connected with red
incline power wire.
DOWN: This is able to
incline “DOWN”, and                        JK90 is MAIN socket
connected with black                     connected with 6-pin of
incline power wire.                           control wire
                                                                   JK50 is Speed sensor socket
                                                                    connected with 2-pin of
                                                                      speed sensor wire



                                    28                                              Service Manual
6.5 Driver Board PCB Component Locations




                                           29   Service Manual
6.6 Driver Board LED Indicator Locations




                                                            Limit
                                                            current
                                                            LED




                                                Power LED




                                           30                         Service Manual
6.7 Controller Indicator LED debugging

  Indicator            Function                 Condition                            Reason                             Solve
    LED
POWER         Controller power     If DC voltage is normal, it would be Voltage is not correct.        Check the supply voltage is 110VAC
                                   always ON. If off, fault condition   Fuse is blown.                 or 230VAC
                                   exists.                              Transformer is no good.        Replace Fuse.
                                                                                                       Replace controller.

Limit         Over current         When lower board detect over           Protection lower board and   Replace controller.
current       Protection warning
                                   current, the LED will be light.        motor.                       Replace motor.
              light
                                                                                                       Do not block belt running.
                                                                                                       Between belt and running board
                                                                                                       need to smear Silicone oil.




                                                                     31                                                         Service Manual
6.8 Driver Board function




                         Bridge
                                                                        IGBT
      L

                      X capacitor                     Filter                                     M-
          Varistor   (Safety CAP.)                  capacitor



      N                                                                                          M+
                         FUSE

      COM
                                                                               Main IC


 UP                                                                                               INCLINE
                                                                                                  VR
                                                                RELAY
DOWN                                 TRANCEFORMER


              INCLINE
              RELAY




                                                                                     MAIN    SPEED
                                                                                   CONTORL   SENSOR




                                                           32                                Service Manual
7. Product Safety Instructions




              33                 Service Manual
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
      it will not fit the outlet; have a proper outlet installed by a qualified electrician. This product is for use on a nominal 110-volt (or 220-volt)circuit, and
      has a grounding plug that looks like the plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used to
      connect this plug to a 2-pole receptacle as shown below if a properly grounded outlet is not available. The temporary adapter should be used only
      until a properly grounded outlet, (shown below) can be installed by a qualified electrician. The green colored rigid earlug, or the like, extending from
      the adapter, must be connected to a permanent ground such as a properly grounded
      outlet box cover. Whenever the adapter is used, it
      must be held in place by a metal screw.




                                                                                 34                                                                 Service Manual
  8.ST155 Treadmill Error Messages /
Troubleshooting for Electronic Issues




                  35              Service Manual
•       Error code items：

          Error Message Explain
                E0      Safety keys dose not insert the safety module. Or safety module is broken.
                E1      Display board CPU did not receive the RPM signal.
                E2      Over current, over limit current of lower controller and motor.
                E3      The console board is not detecting the VR voltage value, or the voltage value has exceeded the range.
                E4      Power wire of motor error.
                E5      Communication signal error.
                E6      Lower controller error.
                E7      Input power error.


    •   Prepare：


                                                           Picture                           Tool name




                                                                                             Multi-meter




                                                                                36                                              Service Manual
8.1 Error message: E0
     Definition: Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken.
     Configuration:

                                       Console

                                                                                                      Lower controller
                                   SAFETY MODULE                        (+12V) signal via S/W
                                                                        of Main control line
                                                                        form a safety switch
                                                                        loop.

                                        SAFETY
                                         KEY


     Cause of E0
            The console is not inserted the safety key, cause to console is not form a +12V’s loop (safety switch loop). So display will be appeared E0.
     But possibly main control wires or component of lower controller is broken. (Because lower controller sent (+12V) signal via S/W of main control wire
     to upper control board to form a safety switch loop.)

     Troubleshooting
       Part                     Troubleshooting
       Safety module            Insert the safety key, and then use Multi-meter transform into short circuit
                                gear position to check safety module wires whether short or not.
       Main control wires       Reinsert Main control wire.
                                Replace main control wire.
       Display board            Replace upper control board.


Note: Before check hardware, first check software setting.
Remove safety key, press STOP & START & ENTER keys, and at the same time insert the safety key. The display into “ENGINEERING MODE”,
Press FAST/SLOW or UP/DOWN keys, to find “functions”, and press Enter key into “DISPLAY MODE”, and then press Enter key into choosing on or off.
When choose “off”, this is mean display off after removed safety key. When choose “on” which is display on and appear E0 after removed safety key.

                                                                             37                                                           Service Manual
8.2 Error Message：E1
    Definition: Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed
    RPM sensor, but when the Calibration which it is a necessary.)
•   Configuration：




                                    Send and receive
                                     speed signal via
                                     TX/RX of 6-pin Main
                                     line.




                                                                      38                                                      Service Manual
Cause of E1
The motor doesn’t turn：E1 appears.
        ■   Explanation:
             The drive board did not sent voltage to the motor, so the motor didn’t operate. And the display board didn’t receive the RPM sensor
                signal.
             Configuration




                                             Send and receive
                                              speed signal via
                                              TX/RX of 6-pin Main
                                              line.




                                                                         39                                                           Service Manual
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




           Reed switch RPM
           Speed sensor
           device




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
    •      8.2 Error Message：E2/OVER CURRENT
    •      Definition: When lower board detect over current, then LED light up and display appear “E2”.
            The means is lower board need to protect itself and motor. Prevent lower board and motor is burned.
    •      Solve over current:
           First, check whether smear Silicone oil or not. And then when during the using treadmill, do not
           block belt running. If aforementioned did not process problem, suggest Replacing lower control
           board or Replacing motor.

•       8.3 Error Message：E3
•       Definition: The console board is not detecting the VR voltage value, or the voltage value hasexceeded
        the range.” E3 appears on the display.
•       Configuration：




                                         The incline VR
                                         single via TX/RX of
                                         Main control lines
                                         sent and receive.




                                                         44                                   Service Manual
Case of E3
Incline VR value exceeds the range. E3 appear on the display.
        Incline motor isn’t operation up or down, making the VR value exceed the range.
        After turning on the unit, the display board detects that the incline VR voltage exceeds the
           range, so E3 appears.
        Action Flow Chart




                                                45                                    Service Manual
 •      Troubleshooting
Part                       Troubleshooting
       Display board       1. Check Incline keys whether key stuck or not.
     Incline power cable   1. Inspect the wire connections.
               &
                           2. Inspect whether wires are broken or crimped.
       incline VR cable
                           3. Replace the wires and test again.
        Driver board       1. Replace the driver board.




                                                     46                      Service Manual
•   Test configuration. The console to driver board connector pin define function




                                Pin 1        GND
                                Pin 2        TXD
                                Pin 3        RXT
                                Pin 4        VCC
                                Pin 5        SW




                                1, 2, 3, 4, 5, 6


                                                    47                              Service Manual
•   Test Configuration.
•   Incline motor control function relate parts location




                                                                         Incline
                                                                   One of 3-pin VR
                                                                          wire
                                                                (It is a position wire)

        Com-white
                                                           GND
        UP-Red                                             SENSOR PIN (AD)
        DOWN-black                                         +5V VCC


      Incline
       Relay
      Incline
       Relay




                                    49                              Service Manual
Test Procedure：
  1.   Run calibration again.
  2.   Does the incline motor move at all?
  3.   If no, do the Up/down lights on the incline board light?
  4.   If they light, do the relays click on?
           If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the
            voltage between the neutral (white) wire and the Up (red) or down (black) wire, depending on which
            direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the
            same as the mains voltage ~ 110VAC (230VAC). If the voltage is present but the motor doesn’t move, then
            the motor is bad.
           If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay
            most likely).
  5.   If the motor moves, is there a sensor reading on console?
           The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0
            for lowest incline. The Incline window is a counter that is showing the actual position sensor output. If the
            motor is moving and there is no count occurring in the Incline window then there is a problem in the
            position sensor wiring or circuitry.
           If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose,
            creating false readings (should not be able to rotate).
            Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the
            two Phillips screws holding it to the motor casting.
            If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If
            everything is tight then the potentiometer could be bad.
           If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black
            and red wire and there should be a voltage
            between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest
            position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage
            at the white wire, and the voltage changes as the motor moves, but the counter still does not register then
            there may be a bad wire connection between the potentiometer and the console.
  6.   Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then
       the wire from the motor to the connector is faulty.
  7.   If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage
       present then there is a problem on the incline board.
       There are no electronic components on the board for this signal; there are just circuit connections from the
       potentiometer connector to the console connector.
       The only problems that are possible are a bad solder joint or broken circuit on the board.
           Console connector wiring, these connections are the same on the incline board and at the console.
                  ■     Pin 1 = 5vdc
                  ■     Pin 2 = position signal 0~5vdc
                    ■    Pin 3= ground
  8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no
       voltage there, but is there at the incline board then check the entire cable from incline board to console for cuts
       or bad connection at the inline connectors.
  9.   If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a
       problem with the console.




                                                             59                                             Service Manual
Error Message：E3 / INCLINE ERR
 Definition: During incline action, the display board CPU cannot read the VR value, so E3 appears.
 Configuration：




                                               Incline drive power   Incline drive power




                                                50                                         Service Manual
 Cause of INCLINE E3
      Press the incline UP/DOWN key. The incline doesn’t operate. E3 appears on the display.
Explanation
      When press incline key, the display board CPU reads the incline VR value. If there is no VR value
      change to the CPU, the incline is not operating, and then appear E2 appears on the display.
Action Flow Chart:




                                                   51                                    Service Manual
Troubleshooting
Part            Troubleshooting
                1. Press incline keys, see the display weather appear value or not.
Display board       If no values, please check keys weather keys stuck or not, or replace
                    upper control board.
                1. Inspect whether the incline power wire and incline VR cable is connected
Incline cable
                   well.
Driver board    1. View the lower control board whether had Components of incline part
                  obvious and serious damage.

                  1. Inspect whether the incline motor is stuck.
                  2. Inspect whether the incline gears are cracked.
Incline motor
                  3. Test whether the incline motor has a broke circuit.
                  4. Recalibrate the incline set.




                                          52                                   Service Manual
8.4 Error Message：E4
Definition: Motor power wire error.
Configuration:




                                      To Motor power




                                         53            Service Manual
Cause of E4:
     Power wire of Motor does not insert lower controller.


 Troubleshooting
 Part                     Troubleshooting
 Lower controller         Insert power wire of motor.
 Motor                    Replace Motor.
 Display board            Replace upper control board.



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
      The main control wire is possibly broken. But E5 maybe has another problem, like component of
lower controller or console board.




 Troubleshooting
 Part                     Troubleshooting
 Lower controller board   Replace main control wire.
 Main control wires       Reinsert Main control wire.
                          Replace main control wire.
 Display board            Replace upper control board.



                                                   54                                   Service Manual
8.6 Error Message：E6
Definition: The lower controller component is fault.
Configuration:



                                      Console



                       Signal via main
                       control line.




                                 Lower controller




Cause of E6:
        The lower controller component is fault, Like Transistor、IGBT、control module…etc.


 Troubleshooting
 Part                       Troubleshooting
 Lower controller           Insert power wire of motor.
 Display board              Only Replace upper control board.




                                                       55                              Service Manual
8.7 Error Message：E7
Definition: Input power anomaly, possibly too low or too high or unstable.
Configuration:



                                                     Console
    Wall outlet
    AC 110V
    Or
    AC 220V

                                                                    Signal via main
    Overload                                                        control line.
    protection


     Power Switch                              Lower controller


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




                                                     56                                    Service Manual
8.8 Circuit diagram:




                       57   Service Manual
58   Service Manual
 8.9 CALIBRATION PROCEDURE
1. Remove the Safety Key.
2. Press and hold down the Start and Speed ▲ buttons and at the same time replace the Safety Key.
   Continue to hold the Start and Speed ▲ keys until the window displays “Factory settings,” then press the Enter key.
3. You will now be able to set the display to show Metric or English settings (Miles vs. Kilometers). To do this, press the incline▲/▼ key to show which
   you want, then press Enter. (The maximum speed value is displayed in the speed window, and the maximum elevation value is displayed in the incline
   window.)
4. Grade return – On (This allows the incline to return to zero when Stop button is pressed. For sale in Europe, EU standards require this to be off )
5. Press Start button to begin calibration. The process is automatic; the speed will start up without warning, so do not stand on the belt.

MAINTENANCE MENU
 1. Press and hold the Start, Stop and Enter key at the same time, until the display shows “ENGINEERING MODE MENU PRESS ENTER” (it may say
 maintenance menu, depending on version).Press the Enter key.
 2. You can now scroll through the menu using the Speed ▲/▼ keys. Use the Stop key to return to previous menu selection. The menu selections are:
 A. Key Test - Will allow you to test all the keys to make sure they are functioning
 B. Display Test - Tests all the display functions
 C. Functions - Press Enter to access settings, use Speed ▲/▼ keys to scroll
 I. Display Mode - Turn off to have the console power down automatically after 30 minutes of inactivity
 II. Pause Mode - Turned on to allow 5 minutes of pause, turn off to have console pause in definitely
 III. Maintenance - Reset lube message and odometer readings
 IV. Units - Choose from English or Metric display readings
 V. Key Tone - Will turn on/off beeping noise that is made when keys are pressed.
 D. Security - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the child lock is enabled, the console will not allow
 the keypad to operate unless you press and hold the Start and Enter buttons for 3 seconds to unlock the console.
 E. Exit




                                                                            54                                                          Service Manual
8.10 Troubleshooting procedure matrix
                       Condition                                           Reason                                                Solve
When turn on power, ON/OFF switch isn’t lit.            1 Power cord isn’t plugged into outlet.      1 Plug the power cord into outlet.
                                                        2 Power cord isn’t plug into unit.           2 Plug the power cord into unit.
                                                        3 The voltage of outlet is too low.          3 Check the voltage of outlet.
                                                        4 Plug or connector of power cord is open.   4 Replace power cord.
                                                        5 Connector of power cord is broken.         5 Replace power cord.
                                                        6 Connecting cable disconnected.             6 Check if wire is disconnected, connect it again.
                                                        7 Breaker tripped.                           7 Press the small red button to return to original status.
                                                        8 Breaker is broken.                         8 Replace breakers.
                                                        9 ON/OFF switch is broken.                   9 Replace AC switch.
After turning on power, treadmill has a popping sound. 1 Incorrect input power, varistor is blown    1 Check the voltage of power is 110V or 230V. Replace
                                                       broken on controller.                         controller.
When insert safe key, no display on monitor.            1 Haven’t switch ON/OFF switch.              1 Switch the AC switch.
                                                        2 Insert the Safe key on wrong position.     2 Insert the safe key on right position.
                                                        3 6-PIN Main control wire not plugged in     3 Please check the wire and connect again.
                                                          properly.                                  4 Replace 6-PIN Main control wire.
                                                        4 6- PIN Main control wire is broken.        5 Replace fuse or controller.
                                                        5 Fuse on controller is blown.               6 Replace varistor or controller.
                                                        6 Varistor on controller is blown.           7 Replace safety key device.
                                                        7 Safety device is broken. (open circuit)    8 Replace console.
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
LCDs not bright, incomplete or imperfect.               1. LCD light is broken.                      1. Replace with new LCD or console.
                                                        2. Power to console too low.                 2. Check AC power is 110V or 230V.
                                                                                                     3. Check power to console.
                                                                                                     4. Replace lower controller.

                                                                                    55                                                                Service Manual
LCD displays not bright, incomplete or imperfect.      1. LCD displays are broken.                   1. Replace with new console.
The speed of the belt doesn’t match console display.   1. Console is not calibrated.                 1.Calibrate the console
The incline position doesn’t match console             1 Console is not calibrated.                  1 Calibrate the console.
INCLINE ERR, INCLINE window displays “E3”.             1 Position sensor value of incline motor is   1 Turn off the AC switch and turn on power again.
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
Incline button just can press DOWN, can’t press UP.    wire is damaged.                              4. Replace the Incline.
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
9. Treadmill Folding/Unfolding and
             Transport\




                58              Service Manual
     FOLDING INSTRUCTIONS
        Do not attempt to move the unit unless it is in the folded and locked
        position. Be sure the power cord is secured to avoid possible
        damage. Use both handrails to maneuver the unit to the desired
        position.
      TO FOLD THE TREADMILL
     Make certain the treadmill is at minimum incline. Lift the treadmill running
     deck until it is secured by the locking telescoping tube assembly in
     center back of base.

      TO UNFOLD THE TREADMILL
     Apply slight forward pressure* on the treadmill running deck with one
     hand. Pull down on the unlocking lever and slowly lower the running
     deck to the floor. The deck will lower unassisted when it reaches about
     waist high.
     *At the rear roller area to relieve pressure on the  locking system.



     TRANSPORTATION
     INSTRUCTIONS
     The treadmill is equipped with four transport wheels that are engaged
     when the treadmill is folded. After folding simply roll the treadmill away.




59                                                                   Service Manual
10. General Maintenance




           60             Service Manual
10-1 Tread belt and Deck
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




    Tracking /                                                                           Tracking / Tension
     Tension                                                                             Adjustment
Adjustment


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
   recommended that you reach between the belt and deck to verify there is lubrication present, every other month. If you check and there isn’t any lubrication
   present, follow the procedure below even though the “Lube” indicator isn’t lit on the console. Otherwise, lubricate when the console’s lubrication reminder lights
   after 90 hours of use. Use the following procedure to apply the silicone lubricant:
     1. Turn the power switch off and unplug the power cord from the wall outlet.
     2. Measure 18” from the edge of the motor cover; kneel down and reach under the belt approximately 4- 6” from one edge. Squirt a line of lubricant about 1/8”
        wide x 15” long in an “S” pattern perpendicular to the motor cover.
     3. Repeat the process on the opposite side.
     4. Plug the electrical cord back into the outlet and turn the power switch on.
     5. Walk on the belt at a moderate speed for five minutes to evenly distribute the silicone lube.
     6. If the “Lube” message appears on the console, perform the following procedure to reset the message:
         1. To enter the Engineering Mode Menu press and hold down the Start, Stop and Enter keys, then at the same time insert the Safety Key. Keep holding
            the keys down until the Message Window displays Engineering Mode Menu. Press the Enter button to access
         2. Press the Speed ▲ button (or Speed ▼button to go backwards) until “Functions”
            appears; press Enter.
         3. Press the Speed ▲ button until “Maintenance” message appears; press Enter to reset lube message.
         4. Press Stop to exit Engineering mode and resume use of your treadmill.
                                                                                  63                                                                  Service Manual
10-2. Service Troubleshooting Checklist – Diagnosis Guide

Before contacting your dealer for aid, please review the following information. It may save you both time and expense. This list includes common problems that may
not be covered under the treadmill’s warranty.

  PROBLEM                                      SOLUTION/CAUSE

 Display does not light                        1) Tether cord not in position.
                                               2) Circuit breaker on front grill tripped. Push circuit breaker in until it locks.
                                               3) Plug is disconnected. Make sure plug is firmly pushed into
                                                  110 VAC wall outlet. (for 220V model is 220 VAC)
                                               4) Breaker panel circuit breaker may be tripped.
                                               5) Treadmill defect. Contact your dealer.

Tread-belt does not stay centered              The user may be walking while favoring or putting more weight
                                               on either the left or right foot. If this walking pattern is natural,
                                               track the belt slightly off-center to the side opposite from the belt
                                               movement.

Treadmill belt hesitates when walked/run on     See General Maintenance section on Tread-belt Adjustment.
                                                Motor drive belt may be loose.


Motor is not responsive after pressing start   1) If the belt moves, but stops after a short time and the
                                                  display shows “LS1/LOW SPEED”, run calibration (See section 8.2 on Error Message: LS1/LOW SPEED).
                                               2) If you press start and the belt never moves, then the
                                                  display shows LS1/LOW SPEED, contact service.

Treadmill will only achieve approximately      This indicates motor should be receiving power to operate. Low AC voltage to treadmill. Do not use an extension cord.
10 kph but shows higher speed on display        If an extension cord is required it should be as short as possible and heavy duty 16 AWG minimum. Low household voltage.
                                               Contact an electrician or your dealer. A minimum of 220 volt AC current, 50 hz is required (of 110 volt AC current, 60 hz is required).

Treadmill trips on board 15 amp circuit           High belt/deck friction. See General Maintenance section on Belt/Deck Lubrication..


Computer shuts off when console is             Treadmill may not be grounded. Static electricity is “crashing” the computer. Refer to section 7.3 for Grounding Instructions.
touched (on a cold day) while walking
/running




                                                                                             64                                                                    Service Manual
House circuit breaker trips, but not the    Need to replace the house breaker with a “High inrush current” type breaker (see section 7.2 for Important Electrical
treadmill circuit breaker.                  Instructions.)

Treadmill with noises                       1. If the noise is coming from the rollers, .
                                            2. If the noise is coming when the user is running on the treadmill with lowest level of incline, it could be due to too much pressure
                                               with the incline cylinder. (only in case of the lowest incline level).
                                             3. If there is knocking noise during the workout, check and make sure all bolts are tightened.
                                            4. When there is thumping noise while the belt is running. This happens with a brand new treadmill or when the treadmill has not
                                               been used for a long time. This is due to the belt has been shaped with rollers and harden because of low temperature. Running
                                               the belt for tens of minutes the thumping noise will gradually go away.

Noise under motor cover.                   1. Worn brushes or bearings on motor. Replace with new motor brushes.
                                           2. Front roller bearings are defective. Replace with new front roller.
                                           3. Drive belt is misadjusted (too tight or too loose). Adjust motor position.

Noise in the rear of the treadmill.        1. Rear roller bearings are defective. Replace with new rear roller
                                           2. Rear roller misaligned.    Adjust rear roller position.

Tread belt hesitates while being           1. Insufficient lubricant on tread belt.
stepped on.                                2. Tread belt tension insufficient

Black particles collecting under             Drive belt is breaking in. Vacuum under treadmill periodically.




                                                                                      65                                                                     Service Manual
11. Installation of the Incline Motor




                  66               Service Manual
            225




Incline Range must be adjusted to
225mm minimum prior to installation.




                  67                   Service Manual
12. Disassembling and assembling of
               Parts




                 68             Service Manual
12-1 Lower Controller Replacement
     1.   Use phillips head screw driver to remove 5 button tapping screws from the motor top Cover, Remove
          motor cover




     2.   Disconnect all lower controller wirings, Use Phillips head Screwdriver to remove, replace with new lower controller
          and reconnect all wirings.




                                                          69                                                  Service Manual
12-2 Console Replacement
     1.   Use a M5 L Allen Wrench to loosen the six Sheet Metal Screw then remove the console mast cover




     2.   Use L Allen wrench to remove 4 button head socket bolts from the console support




     3.   Disconnect console wirings and replace with new console.




                                                        70                                                 Service Manual
12-3 更換馬達 Motor Replacement
    1.   Use a Phillips Head Screw Driver to loosen the 5 tapping screws on motor cover, then remove the motor cover




    2.   Remove motor grounding wire (greenish yellow), motor wire (+) red and motor wire (-) black.




    3.   Use 14mm T-shaped socket wrench to loosen 4 screws, use 14mm open end wrench to loosen 1 belt tension
         screw, remove motor and replace with new. Reassemble in reverse order of disassembly, re-hook belt (readjust
         belt to be parallel with main frame after re-hooking). Do not tighten 4 securing screws yet.




                                                        71                                               Service Manual
4.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area
     between 70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws. Connect
     grounding wires and motor wires (red M+, black M-)




                                                   72                                               Service Manual
12-4 Breaker Replacement
     1.   Remove Breaker connection wiring, replace part and reconnect wiring.




12-5 AC Power Switch Replacement
     1.   Disconnect wiring to AC power switch, replace AC power switch and reconnect wiring.




                                                        73                                      Service Manual
12-6 Front/ Rear Roller Replacement
     1.   Use Phillips head screwdriver to loosen 2 screws on the rear adjustment base.




     2.   Use M6 L Allen wrench to loosen 2 screws on the rear roller.




     3.   Remove motor cover, use 14mm T-shaped socket wrench to loosen 4 screws. Use 14mm open end wrench to
          loosen 1 belt tension screw and loosen drive belt. Use 13mm wrench to loosen front roller screws, remove front
          and back rollers, and replace with new. Reassemble in reverse order of disassembly. When reassembled, running
          belt tension needs to be adjusted and centered. Belt tension also needs to be adjusted




                                                          74                                              Service Manual
4.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area
     between 70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.




                                                   75                                               Service Manual
12-7 Running Deck/ Belt & Cushion Replacement(Please take the cylinder before
  replacement)
     1.   After running board has been folded, use M5 Allen wrench and 12m/m wrench to remove securing screws on
          cylinder and remove the cylinder.




     2.   Follow procedures 12-6 to Front/ Rear Roller Replacement
     3.   Use a Phillips head screwdriver to loosen 6 screws, remove the top step cover in the direction of the indicating
          arrows and remove 8 screws on the front and back of the foot rail then remove the front and back of foot rail in the
          direction of the indicating arrows.




                                                           76                                                   Service Manual
4.   User Combination M5 Allen Wrench to remove the 8 screws securing the running board. Remove the running
     board and replace running board or running belt. If cushions need to be replaced, remove 6 cushions and replace.
     Reassemble in the reverse order as disassembly.




5.   Use 14mm open end wrench to adjust belt tension using tension measuring device. Adjust to white LBS area
     between 70-75LBS. Use 14mm T-shaped socket wrench to secure and tighten 4 securing screws.




                                                     77                                                Service Manual
12-8 Speed Sensor Replacement(including the wire)
     1. First remove motor top cover. Remove speed sensor wiring and proceed with parts replacement. After replacement,
        a test to check if the sensor registers the magnet is required.




                                                       78                                              Service Manual
12-9 Incline Motor Replacement
     1. First adjust treadmill to folded position, then proceed with old incline motor replacement.




     2. Incline Range must be adjusted to 225mm minimum prior to installation.




                     225




     3. User Combination M8 Allen Wrench and 14mm wrench to assemble new incline motor.




                                                           79                                         Service Manual
80   Service Manual
4. Connect incline motor wiring with controller




                 Red wire Connect to
                 “UP”
                 White wire Connect to
                 “COM”
                 Black wire Connect to
                 “DOWN”




                                                  81   Service Manual
