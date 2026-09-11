<!-- Source: XE395ENT_XE539S-SE025-01 Service Manual 2021.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XE539S-SE025-01
    Service Manual




1               Service Manual
1. XE539S-SE025-01 Outlines




             2                Service Manual
3   Service Manual
2. Electronic Parts




         4            Service Manual
Upper Controllers




         DISPLAY




                    5   Service Manual
Thumb Switch                 Cooling FAN




               Speaker




                         6                 Service Manual
Lower Controller and Driver




                                               SPEED RPM SENSOR




                              CONTROLLER




          INCLINE MOTOR                              TENSION MOTOR


                                           7                  Service Manual
3.Electrical Configurations




             8                Service Manual
CONSOLE:
 Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console、incline driver and tension motor driver, link the console to output appropriate voltages for tension
 motor that control the elliptical functions.

TENSION    MOTOR:

 It can change to increase or decrease resistance level of brake.

INCLINE MOTOR:
 This is an AC motor. User can to control variable elevation by console within main controller.
GENERAL INFORMATION

CONSOLE
   Contain keys control and TFT LCD touch panel.

TENSION MOTOR
   Work voltage:DC 4.5~7.5V
   Control resistance increases and decreases.

INCLINE MOTOR
 This is a 115 volt AC motor.

 Have four wires, red, black, white and green.

 Has one 3 pins cable of position sensor.

 If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
 If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.

 The White wire (COM) is neutral.
 The green wire is ground.
                                                                                9                                                                Service Manual
4. XE539S-SE025-01 Product Operation




                 10              Service Manual
Display Windows


                         TFT LCD TOUCH
                         PANEL & PROGRAM
                         MENU




      COOLING FAN



                         START, STOP
                         LEVEL CONTROLS



     USB
     CHARGER




                    11                     Service Manual
POWER

When the power cord is connected to the elliptical, the console will automatically power up.



QUICK START
This is the quickest way to start a workout. After the console powers up you just press the Start Workout on the screen, or press the START key to begin.
This will initiate Quick Start the Time will count up from zero and the workload may be adjusted manually by pressing the Level Up/Down keys.
There are 20 levels of resistance available for plenty of variety. The first 5 levels are very easy workloads and the changes between levels are set to a good
progression for de-conditioned users. Levels 6-10 are more challenging, but the increases in resistance from one level to the nextremain small. Levels
11-15 start getting tough as the levels jump more dramatically. Levels 16-20 are extremely hard and are good for short interval peaks and elite athletic
training.



BASIC INFORMATION
The Stop key actually has several functions. Pressing the Stop key once during a program willpause the program for 5 minutes. If you need to get a drink,
answer the phone or any of the manythings that could interrupt your workout, this is a great feature. To resume your workout during
Pause, just press the Start key. If the Stop key is pressed twice during a workout, the program will end and the console will display your Workout Summary
(Total time, Avg. Speed, Avg. Power, Avg. HR,total Laps).




PROGRAMMING THE CONSOLE
Each of the programs can be customized with your personal information and changed to suit yourneeds. Some of the information asked for is necessary to
ensure the readouts are correct. You willbe asked for your Age and Weight. Entering your Age is necessary during the Heart Rate programsto ensure the
correct settings are in the program for your Age. Otherwise the work settings couldbe too high or low for you. Entering your Weight aides in calculating a
more correct Calorie reading.Although we cannot provide an exact calorie count, we do want to be as close as possible.
                                                                              12                                                            Service Manual
CALORIE NOTE: Calorie readings on every piece of exercise equipment, whether it is in a gym or athome, are not accurate and tend to vary widely. They
are meant only as a guide to monitor yourprogress from workout to workout. The only way to measure your calorie burn accurately is in a clinical setting
connected to a host of machines. This is because every person is different and burns calories at a different rate. Some good news is that you will continue
to burn calories at an accelerated rate for at least an hour after you have finished exercising!


CHARGE PORTABLE DEVICES WITH USB PORT
You can charge your personal device during your workout using the fitness equipment’s on-consoleUSB port. To charge your mobile electronics make sure
the fitness equipment power is on.Step 1: Connect your USB charging cable (not included) to the USB Power Port and to your device.Step 2: Check to
make sure your device icon indicates it is charging.
NOTE:
• USB charging cable is not included, make sure compatible USB charging cable is being used.
• The USB port on the console is capable of powering USB devices. It provides up to 5Vdc/1.0amp of power and meets USB 2.0 regulations. You will not
be able to save your workout data toa USB via this port; it is used for charging purposes only.




                                                                               13                                                         Service Manual
5. XE539S-SE025-01 Unit Block Diagrams




                  14              Service Manual
Elliptical Configuration




                           15   Service Manual
6. Basic Connections and Wiring




               16                 Service Manual
Display Board wire Connections




                                 17   Service Manual
Display Board PCB Component Locations

 PCB Board Top




                                        18   Service Manual
PCB Board Bottom




                   19   Service Manual
The console Interface Board wire Connections




                                               20   Service Manual
Driver Board Wire Connections




                                21   Service Manual
Driver Board PCB Component Locations




                                       22   Service Manual
Driver Board function




 AC POWER
 INPUT




 AC POWER
 INPUT


                                                 INCLINE
INCLINE                                          VR
MOTOR UP



INCLINE
MOTOR COM                                    TENSION
                                             MOTOR

              INCLINE
              MOTOR DOWN
                           RPM
                                    SYSTEM
                           SENSOR
                                    WIRE




                           23                      Service Manual
Tension Motor connector definition function




        STEEL ROPE




        MAIN
        CONTROL
        1.M+                      5
        2.M-                      4
        3.+5V                     3
        4.VR                      2
        5.GND                     1




                                              24   Service Manual
7. XE539S-SE025-01 Error Messages /
         Troubleshooting




                 25              Service Manual
   Error code items：


                        Error Message             Explain
                        E2                        Tension motor is failure
                                                  The console board is not detecting the VR voltage value,or the voltage
                        E3
                                                  value has exceeded the range.


   Prepare：


                                        Picture                               Tool name




                                                                               Multi-meter




                                                            26                                                             Service Manual
 Error Message ：E2
   Definition：When you press the Level Up or Down key,the motor does not move.” E2” appears on the display.
   Configuration：




                                                                             27                                Service Manual
 Tension Motor Operation
                                 Part            Description

                                                 Key signal travels to the display.The main program IC then sends a
                                 Display
                                                 command signal to the drive board.

                                                 Drive board receives the signal and responds by putting out power to
                                 Drive Board
                                                 the motor.Level UP:+5VDC;Level DOWN:-5VDC


 Tension Motor Troubleshooting

                                 Part            Description
                                 Display         If the key beeps when pressed,assume that the signal was sent.
                                 Data cable      Inspect the cable and connections.
                                                 Inspect drive board power output to the motor.Press the Level Up is
                                                 +5VDC;Level DOWN is -5VDC.If there is power to the motor,but the
                                 Drive Board
                                                 motor does not operate,replace it.If there is no power output,inspect
                                                 whether the drive board has power.


 Tension Motor Voltage Test Procedure
  1. Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the
      drive board.
  2. Turn on unit power.The display lights up.
  3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates.Resistance increases.
  4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates.Resistance decreases.
  5. If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
  6. Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.


                                                                        28                                                 Service Manual
Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the drive board.



                                                   29                                                       Service Manual
Error Message：E3
       Definition：The console board is not detecting the VR voltage value,or the voltage value has exceeded the range.” RAMP ERROR” appears on the display.
       Configuration：



         Case of RAMP ERROR
           Incline VR value exceeds the range. E3 appears on the display.
               Incline motor isn’t operation up or down,making the VR value exceed the range.
               After turning on the unit,the display board detects that the incline VR voltage exceeds the range,so E3 appears.
                  Action Flow Chart




                                                                                    30                                                             Service Manual
31   Service Manual
 Troubleshooting
            Part            Troubleshooting
                            1.Reconnect VR wires.
            Incline VR
                            2.Inspect whether the incline wires are broken or disconnected.
                            1.Inspect the incline wire and 6-pin cable connections.
            Display board
                            2.Test whether the VR voltage varies at the incline wire terminal.
                            1.Inspect the wire connections.
            6-pin cable     2.Inspect whether wires are broken or crimped.
                            3.Replace the wires and test again.
            Driver board    Inspect the display board 6-pin connections.




                                                           32                                    Service Manual
 Test configuration. The console to driver board connector pin define function




                                    The console to driver
                                    board connector pin
                                    define function:
                                    1. 12V
                                    2. GND
                                    3. TXD
                                    4. RXD
                                    5. EUP
                                    6. DMK




                                                            33                    Service Manual
   Test Configuration. Incline motor control function relate parts location

                                                                               The position sensor wires
                                                                               1.Red = Ground,
                                                                               2.White = Position signal,
                                                                               3.Black = 5vdc,
                                                                               (0~5v depending on incline position)




                                                                1. 12V
                                                                2. GND
                                           1.   RPM1            3. TXD
                                           2.   GND             4. RXD
       RED-UP                              3.   RPM2            5. EUP
                                           4.   GND             6. DMK
    White-NEUTRAL                                                                                1. MTR-
                                                                                                 2. MTR+
    BLACK-DOWN
                                                                                                 3. VREF
                                                                                                 4. MPOS
                                                                                                 5. GND




                                                       34                                             Service Manual
Test Procedure：
  1.   Run calibration again.
  2.   Does the incline motor move at all?
  3.   If no, do the Up/down lights on the incline board light?
  4.   If they light, do the relays click on?
           If the relay clicks on but the motor doesn’t move: with the incline light and relay activated check the voltage between the neutral (white) wire and the Up (red) or down
            (black) wire, depending on which direction the motor is supposed to travel according to Up/Down lights on the board. It should be about the same as the mains voltage
            ~ 115VAC. If the voltage is present but the motor doesn’t move, then the motor is bad.
           If the light is on, but the relay does not click on then the incline board needs to be replaced (Bad relay most likely).
  5.   If the motor moves, is there a sensor reading on console?
           The INCLINE window will display the computer incline setting (after speed cal. ends); 20 for max incline, 0 for lowest incline. The Incline window is a counter that is
            showing the actual position sensor output. If the motor is moving and there is no count occurring in the Incline window then there is a problem in the position sensor
            wiring or circuitry.
           If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings (should not be able to rotate).
            Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws holding it to the motor casting.
            If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the potentiometer could be bad.
           If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and there should be a voltage
            between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the lowest position (the number isn’t too critical,
            as long as it’s somewhere in this neighborhood). If there is a voltage at the white wire, and the voltage changes as the motor moves,
            but the counter still does not register then there may be a bad wire connection between the potentiometer and the console.
  6.   Check the voltage from the potentiometer at the 3-pin connector on the incline board. If there is no voltage then the wire from the motor to the connector is faulty.
  7.   If there is a voltage, check at the output connector to the console at the bottom of the incline board. If no voltage present then there is a problem on the incline board.
       There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer connector to the console connector.
       The only problems that are possible are a bad solder joint or broken circuit on the board.
           Console connector wiring, these connections are the same on the incline board and at the console.
                       Pin 3 = 5vdc
                       Pin 2 = position signal 0~5vdc
                       Pin 1 = ground
  8.   If there is voltage at the output connector to the console then check the voltage at the console. If there is no voltage there,
       but is there at the incline board then check the entire cable from incline board to console for cuts or bad connection at the inline connectors.
  9.   If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem with the console.




                                                                                        35                                                                           Service Manual
Error Message：E3
 Definition：During incline action,the display board CPU cannot read the VR value,so E3 appears.
 Configuration：




                                                                            36                    Service Manual
Cause of E3
        Press the incline UP/DOWN key.The incline doesn’t operate. E3 appears on the display.
           Explanation
               Press the incline UP and DOWN key.The driver board UP or DOWN indicator lights.The incline operates,moving the VR,which changes the VR
                    value.
               The display board CPU reads the incline VR value.If there is no VR value change,to the CPU,the incline is not operating when it should be. E3
                    appears on the display.
           Action Flow Chart




                                                                              37                                                              Service Manual
Troubleshooting
            Part            Troubleshooting

            Display board   If not as above,inspect the cable and connections.

                            1.Inspect whether the 6-PIN cable is connected well.
            6-pin cable
                            2.Test by replacing the cable with a good one.

                            1.Press incline UP or DOWN key again,making the incline motor return to its position.
            Driver board
                            2.If E3 still appears,re-calibrate the incline set.

                            1.Inspect whether the incline motor is stuck.
                            2.Inspect whether the incline gears are cracked.
            Incline motor
                            3.Test whether the incline motor has a broken circuit.
                            4.Re-calibrate the incline set.




                                                           38                                                       Service Manual
      XE539S-SE025-01
ELLIPICAL CIRCUIT DIAGRAM




                            39
MAINTENANCE MENU IN CONSOLE SOFTWARE



Click the “Settings” at “Settings” page 10 times to enter “Engineer Mode”
-Settings




-Engineer Mode




                                                                            40
1. Function
  Units
   Switch between “imperial” and ”metric”

  Odo
   Click on “Reset” to clear all odometer.

  Display Mode
   Default is OFF. When set OFF, the electronic watch will go to sleep without any operation
   within 30 minutes. Press any key to wake up.

  Beep Mode
   Turn off beep mode, no beeping sound is heard.

  Software Update
   Pressing “USB” to update APK.
   Pressing “OSOTA” to update OS, then press “Check for update” down below the screen.
   Pressing “Command” to update SUB PCB.




                                                                                 41
2. Service
  Key Test
      Click “Reset” to clear key.

  Motor Test
   1. Manual : Click “Test” to Enable Test tiny move Motor function, then Click “+” or “-” to tiny
      move Motor forward or backward
      It will show AD value for current position
   2. Auto : Click “Test” to Enable Test lift test function, it will move Motor Up to High-Level then
      move motor Down to Low-Level automatically.
      It will show AD value for current position and target Level and count of cycle


  Incline Test
     1. Manual : Click “Test” to Enable Test tiny move incline Motor function, then Click “+” or “-”
         to tiny move incline Motor forward or backward
         It will show AD value for current position
     2. Auto : Click “Test” to Enable Test lift test function, it will move incline Motor Up to
         High-Level then move incline Motor Down to Low-Level automatically.
         It will show AD value for current position and target Level and count of cycle

  Sensor Test
   Click “Test” to enable test sensor, can test BT HR value, HP value, WP value and RPM.




                                                                                     42
3. Factory Setting
 Restore Factory
  Click “Clear” to restore factory.
 First Launch
  Click “ON” to set First Launch ON, then re-power ON will process First     Launch UI.
 Machine Type
  See the console machine type.
 BLENAME
  Can input the new name and press SAVE then can re-name BLE device name, need re-power
  on then can use phone to scan console device for new BLE name.* just for developer test

   -Machine Type is XE395




                                                                          43
4. Factory Setting
 Incline Calibration
   Click “start” to calibrate incline. The incline motor will move UP till no move any more for 3~6 sec and
   move Down till no move any more for 3~6 sec then finish to calibration , during calibration.




                                                                                             44
  Fuse replacement




           FUSE 5A




If your elliptical loses power or will not start, check the fuse located on the motor controller.
DANGER: Turn the power switch off and unplug the elliptical to reduce the risk of an electric shock
Remove FUSE holder.
Remove and replace the fuse on the holder
                                                                                  45                  Service Manual
  Troubleshooting procedure matrix

                     Condition                                           Reason                                                   Solve
LCDs not bright, incomplete or imperfect.             1. LCD light is broken.                         1. Replace with new LCD or console.
                                                      2. Power to console too low.                    2. Check AC power is 110-120V.
                                                                                                      3. Check power to console.
                                                                                                      4.Replace lower controller.
LCD displays not bright, incomplete or imperfect.     1. LCD displays are broken.                     1. Replace with new console.
The incline position doesn’t match console            1 Console is not calibrated.                    1 Calibrate the console.
INCLINE ERR ,INCLINE window displays “E3”.            1 Position sensor value of incline motor is     1 Turn off the AC switch and turn on power again.
                                                                                                      2. Calibrate the monitor.
                                                      wrong.
Erratic pulse display.                                1. Another chest belt in use around Ellipitcal. 1. Check for other chest belt use around elliptical.
                                                      2. Other magnetic field disturbance.            2. Change the position or direction of elliptical.
                                                      3. Receiver is broken.                          3. Replace with new receiver.
UP/DOWN button of                                     1 The connector of INCLINE CABLE                1 Connect the wires again.
INCLINE ADJUSTMENT SWITCH can’t be used.                and CONSOLE not connected properly.
                                                      2. The connector of INCLINE CABLE               2. Connect the wires again.
                                                      and INCLINE ADJUSTMENT SWITCH
Incline button just can press UP, can’t press DOWN.   W/CABLE not connected properly.
Incline button just can press DOWN, can’t press UP.
                                                                                                      3. Replace the cable.
                                                      3 The connector of INCLINE CABLE or
                                                      INCLINE ADJUSTMENT SWITCH CABLE
                                                      got damage.                                     4. Replace buttons.
                                                      4. Button of INCLINE ADJUSTMENT
                                                      SWITCH is broken.                               5. Replace the cable.
                                                      5. The connector of INCLINE CABLE or
                                                      INCLINE ADJUSTMENT SWITCH CABLE 6. Replace the cable.
                                                      got damage.
                                                      6. The connector of INCLINE CABLE or
                                                      INCLINE ADJUSTMENT SWITCH CABLE
                                                      damaged.
Hand pulse lost its function.                         1. Hands not on the hand pulse sensors or       1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                          only one hand on sensor.
                                                      2. The connector of HANDPULSE W/WIRE 2. Connect the cable again.
                                                         and Console not connected properly.
                                                                                     46                                                                      Service Manual
                                          3. The wires got damaged when connecting 3. Replace with new cable.
                                             the HANDPULSE W/WIRE and Console.
                                          4. Hand pulse board is broken.              4. Replace console or Hand pulse board.
Wireless lost its function.               1. Chest belt not worn properly.            1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                          oriented correctly.
                                          2. Distance is too far and exceeds range of 2. User chest belt in front of console within 3 feet.
                                          receiver.                                   3. Replace with new lithium battery type is CR2032.

                                          3. Chest belt battery is weak or dead.
Chest belt too close to the Ellipitcal.   Weak battery.                                Replace with new lithium battery with type CR2032.




                                                                       47                                                                Service Manual
9. TROUBLESHOOTING




        48           Service Manual
9-1. Console Problem
    1. Under normal use console screen will display, if there is no display, first check AC adapter to make sure it is in the correct position.




    2. Next, check if all the wires are inserted in the firmly and securely on to the console




                                                                          49                                                              Service Manual
    3. Then remove the AC adapter fuse to check for damage, replace if damaged.




    4. Remove console cover, left and right chain covers, check if all the wires are inserted in the correct positions and check if whether the wires
       broken.

9-2. Side case & Round Disk Problem
    1. The potential reason why there could be a problem here is due to the friction created causing abnormal sounds. However, to determine this,
       you will need to check to see if the large disk is not centered or offset.




    2. If the disc is not centered causing friction, remove the left and right chain cover and reassemble. Refer to the assembly and disassembly
       procedures.
    3. If the disc is offset causing friction, remove the left and right chain cover, use Phillips screwdriver and remove the 5x16mm Tapping Screw as
       well as the 1/4 "x19mm flat washer. Placed the round disk and the Cross Bar on a flat surface to check if either is deformed. If deformed, check
       to see if the deformity can be fixed manually. The deformity occurs mostly caused by external force and thus is why the product goes through
       a quite room test on the production line to ensure that the standards of +/-3mm are met before shipment.
                                                                        50                                                            Service Manual
9-3. Flywheel Problem
    1. This problem is very rare, most of the time the problem is caused by incorrect cable adjustments or improper assembly causing offset creating
       abnormal sounds. Please follow the magnetic flywheel and cable disassembly procedures to commence adjustments.




    2. If there is abnormal sound coming from the magnetic flywheel, first check if are any foreign objects or friction, make
       adjustments. If adjustments are not able to be made, replace with new part.




                                                                      51                                                           Service Manual
9-4. Poly-V Belt Problem
  1.   If the Poly-V Belt falls off, first remove the right chain cover and Idler Wheel Plate, and then reinstall the Poly-V Belt. Once reinstalled, rotate at low
       speed to observe if the Drive Pulley or Poly-V Belt is offset or deformed. Check if the belt pulley is offset or if the belt, Drive Pulley, Magnetic
       flywheel are not aligned in a straight line. Lastly, rotate at high speed (100-200RPM) and test with abrupt stops to check for abnormalities. If
       everything is ok, restore to fully assemble.




  2.   If the three parts are not aligned in a straight line, adjust the magnetic flywheel to the proper place.   Adjustments are always made to product
       ensuring alignment before shipment from factory.




                                                                              52                                                                Service Manual
3.   If the Poly-V Belt is slipping, simply adjust the cap the on hook-type screw with the #13 wrench to adjust. Refer to the
     disassembly procedures for adjustment.




4.   If the Poly-V Belt worn or damaged, replace with new part.




                                                                  53                                                     Service Manual
9-5. Swing Arm Problem
  1.   To make assembly easier for consumers, there will be minor difference in size (0.05mm~0.07mm). Therefore, it is normal for a little
       shake/wobble to exist, but after prolonged use, small parts due to friction wear will generate noise. The solution is to add thick lubricant into the
       top of Ø 25x296L Swing Arm Axle.      If the noise is emitting from the bottom bracket, then the 6005 bearings needs to be replaced.
  2.   When the keys on the handrails are not functioning, first remove the stickers, use a Phillips head screw driver and remove
       the M5x20mm screws securing the keys to the Swing Arm.
       Check to see if the wires for the keys and swing arm are connected properly.




  3.   Next check the wire connection between the swing arm and the lower arm are connected properly.                          At the same time, also
       check to see if the wire is broken




                                                                            54                                                             Service Manual
9-6. Connecting Arm Problem
  1.   The elliptical uses linked structure design, thus if there is a problem in the link it will affect other parts of the structure. Therefore, every part of
       the elliptical structure is important, more importantly, asides from resolving and replacing problem parts, it is also important to lubricate frequently.
       So it is advised during, maintenance or repairs to lubricate preventing potential problems in the future.




  2.   There are many things that may affect or create problems with the footing. The main issue is if the sliding wheel of the linked structure slides
       smoothly and parallel on top of the Inclinable Rail Assembly. In short, the main cause would be side Inclinable Rail Assembly and the Inclinable
       Rail Assembly are not parallel, side Inclinable Rail Assembly and the main frame bottom bracket rotating sleeve do not come together as 90
       degrees.




                                                                             55                                                               Service Manual
3.   Check to see if left/Right connecting arm and left/right step is connected properly, if sliding wheel has the correct rotation degrees, slipping
     occurrences or bearing damages, unsecured connections causing noises.          Use #19 Open-End Wrench to remove the fish eye bearing and
     replace with a new part.




4.   Generally maintenance should start from the sliding wheels, replacing the sliding wheels or adding lubrication to the top of the sliding wheel arcs.
     Check the main structure for abnormalities, abnormalities in parallel parts, make sure that the problem is with the parts and not assembly before
     replacing the parts.




                                                                          56                                                              Service Manual
9-7. Controller & Incline Motor Problem
  1.   When incline motor is not functioning, check all the wire for secure connection, check incline controller and power adaptor is damaged or broken.
       Replace damaged or broken parts.




  2.   Make sure the incline motor is reset to zero when you install a new one. Rotate the incline barrel clockwise to the end and
       then rotate the same barrel counterclockwise in one and a half circle. Make sure the distance of two hole sites is 204±1mm




                                                                          57                                                           Service Manual
9-8. Gear Motor Problem
  If there is no resistance, first check to see if console is functioning normally. Next check the Gear Motor cable, if worn or damaged remove the Steel
  Cable. Use Phillips screw driver to remove the Tapping Screw w 5x19 securing the Gear Motor cable and replace cable with new.




                                                                          58                                                             Service Manual
10. Q & A




   59       Service Manual
10-1. Noise
  There are potentially many locations where noise can originate from, but it is not easy to isolate the location specifically. In
  the front, the chain cover and the round disk, EPE, round disk, sleeve, Cross Bar ‚ Belt and belt pulley, Idler Wheel Plate ‚
  Swing Arm, Swing Arm Axle, Flywheel, Steel Cable, Slide Wheel and Crank Arm during assembly along with side Inclinable
  Rail Assemblys as well as pedals. The main reasons are usually not enough lubrication, unsmooth rotations, and loose
  screws. Because the product is designed based on linked designs, resolving noise issue will vary from machine to machine
  depending on actual situation.




                                                             60                                                     Service Manual
10-2. Slip Problem
  Slipping problems can be verified by the following steps.
  1. M12 x P1.75 Rod End Bearing : M12 Nut on top must be securely tightened with Pedal Bar Assembly, and Rod End Bearing
      needs to be vertical.




  2.   Bushing Housing, Pedal Arm: the CAP Socket Head Cap Bolt 3/8 "x2-1/4 on top and nyloc nut 3/8" x11T must be
       tightened securely, recommended weight is between 500~600Lbs.




                                                         61                                                Service Manual
3.   Cross Bar : CAP Socket Head Cap Bolt M8x40m/m on top of the Cross Bar on the must be tightened to recommend
     550~600Lbs.




4.   Belt: This issue appears quite often, because after a period of time, most belts will become loose from use depending on
     usage time. Solution will depend on weight and adjustment methods, refer to belt disassembly procedures for references.




                                                          62                                                  Service Manual
10-3. Resistance & Incline Problem
Shaking is mainly due to loose screws, so check and tighten loose screws first. Check connection points to see if gaps have been created after prolong
use causing wear and tear or improper assembly. For example, shaking of the foot pedal is caused by loose Carriage Bolts, from improper assembly.




                                                                       63                                                            Service Manual
10-4. Smooth Problem
  1.   Check for loose screws if machine motion feels unsmooth.
  2. Check if there are foreign object on or around the sliding rail, use an alcohol wipe to remove and re-lubricate with lubricant.




                                                                      64                                                               Service Manual
11. Disassembling and assembling of
                 Parts




                 65                   Service Manual
11-1 Console Replacement
    1.   Use Phillips head screwdriver to remove Phillips Head Screws M5x10mm (4pcs) securing the console. Unfasten all connected wires and
         remove console.




    2.   Reassemble in the reverse order as disassembly (Be sure to not crush or damage wiring during process)




                                                                66                                                         Service Manual
11-2 Swing Arm Replacement
    1.   Use a Phillips screwdriver to remove Sheet Metal Screws 3.5x12mm securing the swing arm covers (Front and Back)




    2.   Disconnect the wiring connecting the upper and lower swing arms.




                                                                67                                                         Service Manual
3.   Use 12m/m_Wrench to release 5/16" × 15m/m_Hex Head Bolt and 5/16"x23x1.5T washer which secure the Handle
     Bar, as shown in figure 3.




4.   Release Fish-eye bearing by using 12 mm and 13 mm wrenches to unscrew it 5/16”x 1-1/4”hex head screw x 1, 5/16”x20x1.5T flat
     washer x 1 and 5/16”x7T nut x 1, as shown in figure 4.




                                                            68                                                        Service Manual
5.   To take apart the swing arm assembly, use#12 and #13 open end wrenches to release three Hex Head Bolts 5/16" x
     1-3/4" together with three nyloc nut 5/16" x 7T, and two curve washers 5/16"x 23 x 1.5T and separate upper Swing
     Arm and lower Swing Arm from each other.




6.   To take apart the Handle Switch Bracket, tear off Handle Switch sticke first then use Phillips head screw driver to
     release two Flat Head Socket Screws M5×20mm and the Handle Switch Bracket, handlebar resistance cable or
     incline cable can be taken apart.




Reassemble in the reverse order as disassembly

                                                       69                                                    Service Manual
11-3        Connecting Arm Replacement
       1.    Remove swing arm assembly and swing arm (If removal of pedal tube, simply remove swing arm with Rod End Bearing attached)
       2.    Use 12mm open end wrench to remove hex head bolts 5/16" x1-1/4" and flat washer 5/16”x20.




       3.    Use 12mm open end wrench to remove hex socket screw 5/16”x15mm and flat washer 5/16”x20. Pull out the pedal carriage bolts to
             remove the Pedal Bar Assembly.




                                                                    70                                                        Service Manual
4.   If removal of adjustable pedal set, Use Phillips screwdriver to remove Phillips Head Screw M5x10mm and Bushing 19×14×10×(5+4)T.
     Pull out Axle of locking pin and use circlip pliers to remove circlip Ø 10.   Remove Locking Pin Assembly.




                                                                  71                                                  Service Manual
    5.   Use Phillips screwdriver to remove Phillips Head Screw M5x10mm securing the pedal and remove pedal.




    6.   Reassemble in the reverse order as disassembly




11-4 Pedal Arm Replacement
    1. ollow procedures 11-3 to take apart Connecting Arm.
    2. Disassemble Connecting Arm first and use Phillips head screw driver to release M5x10mm Phillips Head Screw to
       take apart Pedal Arm Cover, as shown in figure 1.




                                                               72                                              Service Manual
3. Use #8 hex wrench and #14 open end wrench to remove Gap socket screw 3/8”x2-1/4”, flat washer 3/8”x19x1.5T and
   nyloc nut 3/8”x11T connecting the Inclinable Rail Assembly and rotating block, to remove Inclinable Rail Assembly.




4. Use #12 open end wrench to remove hex head bolt 5/16”x15mm and flat washer 5/16”x35x1.5T, to remove Bushing
   Housing, Pedal Arm.




                                                    73                                                 Service Manual
5. To take the slide wheel apart, use Phillips head screw driver to release two Phillips head screws M5x15mm and take
   the slide wheel cover first.




6.   Use circlip pliers to remove circlip Ø 17 and remove sliding wheels




7. Reassemble in the reverse order as disassembly Following the steps gradually as beginning of Ø 17 × 0.5T_Wave
   Washer, Ø 78_Slide Wheel, Urethane, Ø 17 × 0.5T_Wave Washer, and Ø 17_C Ring when assemble the Ø 78_Slide
   Wheel, Urethane.




                                                       74                                              Service Manual
11-5 Console Mast Replacement
    1.   Follow procedure 2 to take apart the handle bar. Use Phillips head screwdriver to rele ase 3pcs of 3.5x16mm Sheet Metal Screws
         to take apart left and right console mast covers, as shown in figure 1.




    2.   Use # 14 open end wrench to remove hex head bolts 3/8”x3/4”, Curved Washers 3/8 "x23 x2T, external hex head bolts 3/8" x2-1/4 "and
         Spring Washer 3/8" x2T that secures the Console Mast.




                                                                75                                                         Service Manual
3.   Remove Console Mast and Console Mast cover together, pull out control wires and incline wires and separate covers
     from Console Mast.




4.   If Handpulse Assembly needs to be disassembled, use Phillips Head Screwdriver to remove Tapping Screws Ø 3x20 2 on the
     Handpulse Bar. Gently pull out the wiring connecting the from the Handpulse Bottom Cover and disconnect from connector on the
     Handpulse Top Cover.




5.   Reassemble in the reverse order as disassembly




                                                            76                                                          Service Manual
11-6 Side Case Replacement
     1.   Remove Swing Arm and Inclinable Rail Assembly.




     2.   Use Phillips head screwdriver to remover nine Sheet Metal Screws 3.5x16 mm and remove right chain cover.




                                                           77                                              Service Manual
3.   Unscrew right Chain Cover on the mainframe by releasing three Tapping Screws 5x19mm.




4.   Further release Sheet Metal Screw 3.5x16mm together with flat washer 1/4"x19 which is inside the right Chain Cover.




                                                      78                                                  Service Manual
5.   Remove 3pcs 5 × 19m/m_Tapping Screw from left chain cover which fixed on main frame. And pull out power
     cable(RED 2pcs) and ground wire(green 1pc) then you can remove left chain cover ( as 5.6 diagram)




6.   Use screw driver to release M4 × 12m/m_Phillips Head Screw *2pcs, M4 X 5T_Nyloc Nut and then remove AC power
     ( as 7 diagram)




7.   Reassemble in the reverse order as disassembly




                                                      79                                             Service Manual
11-7    Cross Bar Replacement
       1.   Remove left and right chain cover. (refer to 11.6 above)
       2.   Remove elliptical side cover Round Disk Cover, use 12mm Open End Combination Spanner Wrench to remove hex head bolt
            5/16”x15mm, flat washer 5/16”x35x1.5T securing the cross bar.




       3.   Use #13 wrench and loosen the outer Nut M8x6.3T (steel lvl 10). Use #13 wrench and hex wrench (M6) to loosen the inner Nut and
            remove the cross bar.




       4.   Use Phillips head screw driver to release Tapping Screws which secure the Round Disk and separate Cross Bar and Round Disk from
            each other.




                                                                   80                                                         Service Manual
     5.   When reassembling, place the cross bar into the center of the rotating mandrel. Next place the Woodruff Key with the rounded part facing
          inwards. Reassemble remaining parts in the reverse order as disassembly




11-8 Idler Wheel Replacement
     1.   Remove the cross bar. (refer to 11.7 above)
     2.   Use #13 Double Open-End Wrench to loosen nyloc nut M8x9T on the hook screws to remove belt. Use #13 wrench Double Open-End
          Wrench to remove screws M8x20, nyloc nut M8x7T and flat washer 5/16”x20x1.5T to remove the Idler wheel.




                                                                    81                                                           Service Manual
     3.   Reassemble parts in the reverse order as disassembly, tighten the nyloc nuts M8x9T on top of the hook screws, flick the belt for crisp
          sound to check tightness or use a sound measuring device to measure at 190HZ(±10), reassemble the remaining parts.




11-9 Flywheel & Poly-V Belt replacement
     1.   Plug in the power. The resistance should read maximum value.
     2.   Follow procedure 11-8 to take apart the Idler Wheel the Console and take apart the Steel Cable.




                                                                    82                                                            Service Manual
3.   Use #15 Double Open-End Wrench to loosen nyloc nut 3/8”-UNF26x9T on flywheel and main-frame. Remove flywheel and belt.




4.   Reassemble parts in the reverse order as disassembly and adjust belt and center the belt wheel. Reassemble the remaining parts.




                                                             83                                                          Service Manual
11-10 Rear Frame Replacement
    1.   Use Phillips head screw driver to remove the Phillips Head Screws M5x15mm below Incline Bottom Cover. Disconnect the power and VR
         wirings for the incline motor.




    2.   Use two 14mm Double Open-End Wrench and 12mm Double Open-End Wrench to remove hex head bolt 3/8"x1-1/2", flat washer
         3/8"x19x1.5T, nyloc nut 3/8x7T, outer hex head bolt 5/16”x2-1/4”, spring washer 5/16"x1.5T, flat washer 5/16" x20x1.5T and star washer
         ψ5/16. Remove rear frame.




    3.   Reassemble parts in the reverse order as disassembly and make sure wirings are connected correctly (same color wire to same color
         socket)


                                                                  84                                                           Service Manual
11-11 Rail & Incline Motor replacement
     1.   Remove rear frame. (refer to 11.10 above)
     2.   Use Phillips head screwdriver to remove screws M5x15mm from Rear Bar Cover, Inclinable Rail Cover and Incline Cover, then remove
          parts.




     3.   Use two 14mm wrenches to remove hex head bolt 3/8”x2-1/2” together with flat washer 3/8"x19x1.5T, nyloc nut
          3/8"x7T and two Nylon Washers Ø 3/8'' x Ø 35 x5T which secure Incline tube and Rear Rail Assembly..




                                                                 85                                                        Service Manual
4.   Use 14mm wrench to release 2pcs *M10x130mm Hex Head Bolt, Ø 3/8" × Ø 19 × 1.5T_Flat Washer and 3/8" ×
     7T_Nyloc Nut which fixed on incline motor ( as 5 diagram)




5.   Use Phillips head screwdriver to remove tapping screw 5x19 from incline motor grounding wire. Cut the Wire Tie Mount and remove
     incline motor.




                                                            86                                                          Service Manual
6.   Use 12mm wrench to remove head hex bolt 5/16"x1 and flat washer 5/16"x 35x2T from rail assembly, remove the rail assembly.




7.   If removal of aluminum rail is needed, remove Phillips head screws M5x15mm from aluminum rail to proceed.




8.   Reassemble in the reverse order as disassembly (Be sure that the grounding wire of the incline motor is firmly secured on
     the frame tube of the Rear Frame.)




                                                            87                                                         Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS I

jenuepy 8dIAlas
LO-Sc04S-S6ESAX


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

S3UI/INO L0-SZOIS-S6ESIX ‘|


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS ¢

AV TdSIG

$19]]01]U04 addy


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS L

YOLOW NOISNAL YOLOW ANITONI

JOALIQ Puke 413]|01]U0D JMO}


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

suoneinbipuoy [e914]99/F7¢


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

uolNeladC JONPOJd L0-SZOAS-SG6ESAX “Pp


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS Il

dHOUAVHO
qsn

STOWLNOD THAT
dOLS “LUV.LS
LIAMAaSs
a v
iLS3N5D °O113H
ONAN
WVaDOUd ¥ TANVd
HONOL GOT LAL

smopul(\ Aeldsig


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

sweibeig YOO/g uN LO-SZOAS-S6ESAX ‘S


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS cI]

WOSNAS
Wal

HOLIMS
os asn4
XOLOW auvod waAria
ANTTIONI

YOLOW
NOISNSL

YANWHdS YH
HOLIMS
duvod AV TdSId SNIIO09

UWIAA
UH SSATIUIM = AIM

uolneinbiuoy jeondiy|y


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

Gui, pue SuoljaauU0y aISeg “9g


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS LI

(SNId 9) qDOuUVHO

HOLIMS dINNHL FIA) WAISAS

Vast TONVH
YH LOVINOO
duvod AdN

YH SSATAMIM,
LO-LOOOLVLV

NI ANTT

u adNVads “| MANVddS NVd DNITIOOD

SUOI]D9UUOYD 211M pseog Ae\dsig


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS a

doy, prvog God

SUOI]}E907] JUBUOdWIOD g4dd pieog Aejdsig


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS
61

[O-ZOOLES:
OIA 10-700105)

wonog prog qd


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS 02

YONHS

ia qsind

dIdDAUNVH

YONHS

[ i | asind

dIYDAUNVH

aie
WALSAS 7

00-1-COOTESO-M

HOLIMS HOLIMS
qINOHL qINOHL
THAT HNITIONI

SUOI]OOUUOYD OJIM PLO BORj19}U] BJOSUOD aU


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS iz

YOLOW
NOISNHL

YOSNHS Wd

LHS YA
YOLOW

ANITONI cay
ALIHA\ —» YO.LOIWN

ANIIONI
NMOd MOV TE —

HTdVO WHLSAS SOOTSSO

HO.LIMS
YAHMOd

YAMOd OV

SUOI]OBUUOZD JJI/\\ pseOg JOALIG


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS zz

LW 892 r 20sue? ac r a | ASM SOOLSSO

SUO!}e907] }JUBUOdWIOD gdd pieog JeALIG


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Driver Board function

AC POWER
INPUT

AC POWER
INPUT

INCLINE
MOTOR UP

INCLINE aS a) || ie =2 ae

MOTOR COM aE e,

ERED ES v = : a ~ TENSION

€ss51005 fev 1. 2 #

INCLINE
MOTOR DOWN

RPM
SENSOR

23 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS yz

CNO'S
UAL
ASt'€

WT

+I
“IOULNOOD
NIV

UOI]}OUNJ UOILIUIJAp 410]}099UUO0D JO}OWY UOISUa]


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

burnlooysaqnol]
/ sabessajyj 40117 10-SZ0AS-S6ESGAX *Z


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Error Message : E2

@ Definition : When you press the Level Up or Down key,the motor does not move.” E2” appears on the display.

@ Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | vpacwnkeys

Eigen

LEVEL LEVEL
COUNT UP/DOWN
SIGNAL SIGNAL

bd

MOTOR VOLTAGE

TENSION
MOTOR

A
DRIVER BOARD VR -
N

27 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
@ Tension Motor Operation

Part Description

Disol Key signal travels to the display.The main program IC then sends a
ispla ;
pray command signal to the drive board.

Drive board receives the signal and responds by putting out power to

Drive Board
me Boat the motor.Level UP:+5VDC;Level DOWN:-5VDC

@ Tension Motor Troubleshooting

Part Description
Display If the key beeps when pressed,assume that the signal was sent.
Data cable Inspect the cable and connections.

Inspect drive board power output to the motor.Press the Level Up is
+5VDC;Level DOWN is -SVDC.If there is power to the motor,but the
motor does not operate,replace it.If there is no power output,inspect

Drive Board

whether the drive board has power.

@ Tension Motor Voltage Test Procedure
1. Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in brown wire,Black probe in black wire) on the
drive board.
2. Turn on unit power.The display lights up.
3. Press LEVEL UP. Normal reading : +5~6.0VDC.Motor operates.Resistance increases.
4. Press LEVEL DOWN. Normal reading : -5~6.0VDC.Motor operates.Resistance decreases.
5. If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
6. Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.

28 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
C INCLINE VR +)
S ‘

Y
|

DRIVER BOARD

ae TR

E

|

CABLE

Rana

x

l

DISPLAY BOARD

ena

7.
| Y
DISPLAY OPERATES ERR APPEARS ON
NORMALLY THE DISPLAY

31 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Test Configuration. Incline motor control function relate parts location

(The position sensor wires _

1.Red = Ground,
2.White = Position signal,
3.Black = 5vdc,

(0~5v depending on incline position)

RED-UP

White-NEUTRAL 2

A

2. MTR+
3. VREF

BLACK-DOWN 4h

sen a3 30) io o ” SH i

4. MPOS

CSS1005 Revi.2 — Console r ECE MIB

34 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Error Message : K3

Definition : During incline action,the display board CPU cannot read the VR value,so E3 appears.

Configuration :

DISPLAY BOARD ‘ UPDOWNKEYS | ip avwarceys

A

INCLINE INCLINE
VR UP/DOWN
VOLTAGE SIGNAL

\Z

INCLINE
MOTOR
DRIVER BOARD ex: VR VOLTAGE INCLINE VR SET

OC) INCLINE DOWN LED
OC) INCLINE UP LED

36 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Cause of E3
@ Press the incline UP/DOWN key.The incline doesn’t operate. E3 appears on the display.
@ Explanation
@ Press the incline UP and DOWN key.The driver board UP or DOWN indicator lights. The incline operates,moving the VR,which changes the VR
value.
@ The display board CPU reads the incline VR value.If there is no VR value change,to the CPU,the incline is not operating when it should be. E3
appears on the display.
@ Action Flow Chart

C DISPLAY BOARD +)

|
DRIVER BOARD

DURING UP ACTION,
UP LED LIGHTS INCLINE
VOLEAGE INCREASES

IN DOWN ACTION,
DOWN LED LIGHTS.INCLINE
VOLTAGE DECREASES

Y

|

INCLINE MOTOR

Sr

DOWN LED LIGHTS,
INCLINE LOWERS?

¥

¥

|
=e > SHOW INCLINE E35

37 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
XES39S-SE025-01
ELLIPICAL CIRCUIT DIAGRAM

|
=F S54 TENSION

MOTOR INCLINE
MOTOR

U

39


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
MAINTENANCE MENU IN CONSOLE SOFTWARE

Click the “Settings” at “Settings” page 10 times to enter “Engineer Mode
-Settings

a6 & & B a
SETTINGS
Display Brightness WiFi Bluetooth Software®
Date Time Child Lock Units
Display Mode

* $ & @ nx ©

€ ENGINEER MODE

FUNCTION

Unit renin) METRIC
Odo 9999 HOUR 9999 KM
Display OFF
Beep OFF

-Engineer Mode

40


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
1. Function

@ Units
Switch between “imperial” and ”metric”

®@ Odo
Click on “Reset” to clear all odometer.

@ Display Mode
Default is OFF. When set OFF, the electronic watch will go to sleep without any operation
within 30 minutes. Press any key to wake up.

@ Beep Mode
Turn off beep mode, no beeping sound is heard.

® Software Update
Pressing “USB” to update APK.
Pressing “OSOTA’ to update OS, then press “Check for update” down below the screen.
Pressing “Command” to update SUB PCB.

- ENGINEER MODE

FUNCTION

Unit METRIC
Odo 9999 HOUR 9999 KM
Display Fon] OFF
Beep Foon] OFF

41


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2. Service

@ Key Test
Click “Reset” to clear key.

@ Motor Test
1. Manual : Click “Test” to Enable Test tiny move Motor function, then Click “+” or
move Motor forward or backward
It will show AD value for current position
2. Auto : Click “Test” to Enable Test lift test function, it will move Motor Up to High-Level then
move motor Down to Low-Level automatically.
It will show AD value for current position and target Level and count of cycle

to tiny

@ Incline Test
1. Manual : Click “Test” to Enable Test tiny move incline Motor function, then Click “+” or
to tiny move incline Motor forward or backward
It will show AD value for current position
2. Auto : Click “Test” to Enable Test lift test function, it will move incline Motor Up to
High-Level then move incline Motor Down to Low-Level automatically.
It will show AD value for current position and target Level and count of cycle

@ Sensor Test
Click “Test” to enable test sensor, can test BT HR value, HP value, WP value and RPM.

€ ENGINEER MODE

SERVICE

Key Test 20 RESET
Maunal AD: XXXX + — TEST

Motor Test
Auto AD: XXXX L.e2o CNT:XXXXX TEST
Maunal AD: XXXX + —
Incline Test
Auto AD: XXXX Leo CNT:XXXXX
Sensor Test HRS: HP: WP: 60 RPM

42


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4. Factory Setting

@ Incline Calibration
Click “start” to calibrate incline. The incline motor will move UP till no move any more for 3~6 sec and
move Down till no move any more for 3~6 sec then finish to calibration , during calibration.

¢ ENGINEER MODE
CALIBRATION
MAX. AD: XXXX DIRECTION:
Incline Calibration
MIN. AD: XXXX CURRENT AD: XXXXX

44


=== OCR SUPPLEMENT, PDF PAGE 65 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aS

SJID
{0 SUI]GQUIASSD puD sUul|quassvSsiIg *T]
