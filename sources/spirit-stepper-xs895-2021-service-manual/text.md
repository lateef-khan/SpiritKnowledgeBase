<!-- Source: XS895 Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

XS300B- YS006
Service Manual




             Service Manual
                                                                                            Table of Contents
1. Outlines ............................................................................................................................................................................................................... 3
2. Electronic Parts .................................................................................................................................................................................................... 4
    2-1 Upper Controllers......................................................................................................................................................................................... 5
    2-2 Lower Controller and Driver ......................................................................................................................................................................... 6
3. Electrical Configurations ...................................................................................................................................................................................... 7
4. Product Operation ............................................................................................................................................................................................... 9
    4-1 Display Windows ........................................................................................................................................................................................ 10
    4-2 Operation ................................................................................................................................................................................................... 11
        4-2-1 POWER .............................................................................................................................................................................................. 11
        4-2-2 Dot Matrix Center Display ................................................................................................................................................................. 11
        4-2-3 1/4 Mile Track ................................................................................................................................................................................... 11
        4-2-4 Pulse Grip Feature ............................................................................................................................................................................. 11
        4-2-5 Calorie Display ................................................................................................................................................................................... 11
        4-2-6 Speakers ............................................................................................................................................................................................ 12
    4-3 Function Button Locations ......................................................................................................................................................................... 14
5. Unit Block Diagrams........................................................................................................................................................................................... 15
6. Basic Connections and Wiring ............................................................................................................................................................................ 17
    6-1 Display Board PCB Component Locations ................................................................................................................................................... 18
        6-1-1 DISPLAY BOARD WIRE CONNECTIONS ............................................................................................................................................... 18
        6-1-2 PCB BOARD TOP ................................................................................................................................................................................ 19
        6-1-3 PCB BOARD BOTTOM ........................................................................................................................................................................ 20
        6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS .................................................................................................................... 21
        6-1-5 AMPLIFIER BOARD WIRE CONNECTIONS ........................................................................................................................................... 22
        6-1-6 TENSION MOTOR CONNECTOR DEFINITION FUNCTION..................................................................................................................... 23
7. Error Messages /Troubleshooting ...................................................................................................................................................................... 24
    7-1 Error Codes ................................................................................................................................................................................................ 25
    7-2 Prepare tools.............................................................................................................................................................................................. 25
     Dyaco International Inc.                                                                                                                                                                                             1
    7-3 Error Message：E1 .................................................................................................................................................................................... 26
    7-4 Error Message：E2 .................................................................................................................................................................................... 26
        7-4-1 TENSION MOTOR OPERATION ........................................................................................................................................................... 28
        7-4-2 TENSION MOTOR TROUBLESHOOTING .............................................................................................................................................. 28
        7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE ................................................................................................................................... 29
    7-5 Error Message：E3 .................................................................................................................................................................................... 30
    7-6 Test configuration. The console to driver board connector pin define function.......................................................................................... 33
    7-7 Engineering Mode Menu ........................................................................................................................................................................... 34
    7-8 Troubleshooting procedure matrix ............................................................................................................................................................. 35
8. Circuit Diagram .................................................................................................................................................................................................. 37
9. Common Problems ............................................................................................................................................................................................ 39
    9-1 Troubleshooting For Console...................................................................................................................................................................... 40
    9-2 Troubleshooting For Pedal arm .................................................................................................................................................................. 41
    9-3 Troubleshooting For Connect arm .............................................................................................................................................................. 42
    9-4 Troubleshooting For Incline motor and Controller board and Gear motor ................................................................................................. 43
    9-5 Troubleshooting For Flywheel and Drive belt ............................................................................................................................................. 44
    9-6 Troubleshooting For Noise ......................................................................................................................................................................... 45
    9-7 Troubleshooting For Drive Belt Slipping ..................................................................................................................................................... 46
10. Parts Replacement Guide ................................................................................................................................................................................ 47
    10-1 Console Replacement .............................................................................................................................................................................. 48
    10-2 Side Case Replacement ............................................................................................................................................................................ 48
    10-3 Pedal Assembly replacement ................................................................................................................................................................... 50
    10-4 Pedal Arm replacement ........................................................................................................................................................................... 51
    10-5 Swing Arm replacement ........................................................................................................................................................................... 53
    10-6 Up Right replacement .............................................................................................................................................................................. 53
    10-7 Rear Rail Assembly replacement .............................................................................................................................................................. 54
    10-8 Incline motor, Gear motor, and Controller board replacement ................................................................................................................ 55
    10-9 Idler Wheel Assembly, Flywheel, and Drive belt replacement .................................................................................................................. 57
    10-9 Crank and Drive pulley replacement ........................................................................................................................................................ 58
     Dyaco International Inc.                                                                                                                                                                                        2
                           1. Outlines




Dyaco International Inc.                 3
                           2. Electronic Parts




Dyaco International Inc.                         4
2-1 Upper Controllers


                  Display




  Dyaco International Inc.   5
2-2 Lower Controller and Driver

         Tension Motor




                                  Incline motor




         Speed Sensor




  Dyaco International Inc.                        6
                 3. Electrical Configurations




Dyaco International Inc.                        7
Part Name             Part Description

CONSOLE               Interface that controls all functions of the Stepper.

MAIN CONTROLLER       The circuit board consist of the DC power supply for console、incline driver and tension motor driver, link the console to
                      output appropriate voltages for tension motor that control the Stepper functions.

TENSION MOTOR         It can change to increase or decrease resistance level of brake.

INCLINE MOTOR         This is an ac motor. User can to control variable elevation by console within main controller.



GENERAL INFORMATION

CONSOLE               Contains Key controls and LCD Display.
                      Main controller Include power supply 、 motor driver control circuit and incline control circuit.

TENSION MOTOR         Work voltage: DC 4.5~7.5V
                      Control resistance increases and decreases.

INCLINE MOTOR         This is a AC motor.
                      Have four wires, red, black, white and green.
                      Has one 3 pins cable of position sensor.
                      If there is AC voltage on the Red wire (UP) the incline motor will increase the incline.
                      If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the incline.
                      The White wire (COM) is neutral.
                      The green wire is ground.




Dyaco International Inc.                                                                                                                          8
                           4. Product Operation




Dyaco International Inc.                          9
4-1 Display Windows



                             7.5” LCD Display




  Dyaco International Inc.                      10
4-2 Operation
 4-2-1 POWER

 When power is connected to the Incline stepper the console will automatically power up. These models are connected directly to 120-volt,15-amp or
 220-volt,10-amp and there is a power switch located where the line cord plugs into the unit on the left side near the middle.
 When it is first powered on, the console will perform an internal self-test. During this time all the lights will turn on, the Message Window display will show a
 software version (i.e.: VER 1.0), and the VERTICAL Window will display an altimeter reading. The Time Window shows how many total hours the Incline stepper
 has been used.
 The altimeter and time will remain displayed for only a few seconds then the console will go to the startup display. The dot matrix display will be scrolling through
 the different profiles of the programs and the Message Center will be scrolling the startup message. You may now begin to use the console.

 4-2-2 Dot Matrix Center Display

 Twenty columns of boxes (10 high) indicate each segment of a workout. The boxes only show an approximate level (resistance) of effort. They do not necessarily
 indicate a specific value - only an approximate percent to compare levels of intensity. In Manual Operation the resistance dot matrix window will build a profile
 “picture” as values are changed during a workout. The Lap track will move in a counterclockwise direction.

 4-2-3 1/4 Mile Track

 The 1/4-mile track (one lap) will be displayed around the dot matrix window. The flashing segment indicates your progress. Once the 1/4-mile (Metric - 0.4k) is
 complete this feature will begin again. There is a lap counter in the message window for monitoring your distance.

 4-2-4 Pulse Grip Feature

 The Pulse (Heart Rate) window will display your current heart rate in beats per minute during the workout. You must use both stainless steel sensors on the
 stationary grips or the heart rate transmitter chest strap to display your pulse. Pulse value displays anytime the upper display is receiving a Pulse signal. You may
 not use the Pulse Grip feature while in Heart Rate Programs.

 4-2-5 Calorie Display


  Dyaco International Inc.                                                                                                                                               11
Displays the cumulative calories burned at any given time during your workout. Note: This is only a rough guide used for comparison of different exercise
sessions, and is not to be used for medical purposes.

4-2-6 Speakers

The console has built-in Speakers and an audio input jack. There is no volume control on the console. The volume must be controlled on the Audio Source.

4-2-7 Quick Start

This is the quickest way to start a workout. After the console powers up you just press the Start key to begin, this will initiate the Quick Start mode. In Quick Start
the Time will count up from zero and the workload may be adjusted manually by pressing the Level +/- buttons. The dot matrix display will have only the bottom
row lit at first. As you increase the work load more rows will light indicating a harder workout. The Incline Stepper will get harder to pedal as the rows increase.
There are 20 levels of resistance available for plenty of variety. The first 5 levels are very easy workloads and the changes between levels are set to a good
progression for de-conditioned users. Levels 6-10 are more challenging, but the increases in resistance from one level to the next remain small. Levels 11-15 start
getting tough as the levels jump more dramatically. Levels 16-20 are extremely hard and are good for short interval peaks and elite athletic training.

4-2-8 Basic Information

The Message Center will initially be displaying the Program name. When in scan mode during a program, FPM(floors per minute) will be displayed for four
seconds, then move on and display FLOORS. The data changes to Laps completed, Segment time, SCAN. Pressing the Enter key again will bring you back to the
beginning.
The Stop key actually has several functions. Pressing the Stop key once during a program will pause the program for 5 minutes. If you need to get a drink, answer
the phone or any of the many things that could interrupt your workout, this is a great feature. To resume your workout during Pause, just press the Start key. If
the Stop key is pressed twice during a workout, the program will end and the console will display your Workout Summary (Total time, Avg. fpm, total floors, Avg.
HR, total Laps). If the Stop key is held down for 3 seconds or a third time during the program, the console will perform a complete Reset. During data entry for a
program the Stop key performs previous screen or segment function. This allows you to go back to change programming data.

4-2-9 Program Keys

The program keys are used to preview each program. When you first turn the console on you may press each program key to preview what the program profile

 Dyaco International Inc.                                                                                                                                                 12
looks like. If you decide that you want to try a program, press the corresponding program key and then press the Enter key to select the program and enter into
the data-setting mode.
The Incline Stepper has a built in heart rate monitoring system. Simply grasping the hand pulse sensors on the stationary handle bars or wearing the heart rate
transmitter (see Using Heart Rate Transmitter section) will start the Heart Icon blinking (this may take a few seconds). The Pulse Display Window will display your
heart rate, or Pulse in beats per minute.
The console includes a built-in fan to help keep you cool. To turn the fan on, press the key on the left side of the console.

4-2-10 Muscle Activation Figure

There is an anatomical figure located at the top of the console. This figure will light all areas that are activated when using the Stepper trainer. These will light up
during any of the programs. You can control which muscles are activated by customizing the resistance profile during the set up phase of console programming. If
you accept the default program profile, the selected program will determine which muscles will be activated by automatically adjusting the resistance. Generally
the following guidelines hold true: The upper body LED’s will activate when you are either holding onto the swing arms or at anytime your hands aren’t onto the
pulse grip sensors.
• The lower body lights will activate in three degrees of engagement: Green represents minimal muscle involvement, Amber represents medium involvement,
and red represents full or heavy activation.
• Levels 0-7.5 Incline: Amber - Gluteals and Quadriceps light up; Green - Hamstrings and Calves light up.
• Levels 8-20 Incline: Red – Gluteals light up, Amber – Quadriceps light up, Green – Hamstrings and Calves Light up.

4-2-11 Heart Rate % Profile

The console LCD screen will display your current heart rate anytime a pulse is detected. The Bar Graph, located to the right of the LCD screen, will show your
current heart rate % in relation to your projected maximum heart rate, which is determined by your age that you entered during the programming phase of any
of the 10 programs. The significance of the bar graph colors are as follows:
     50-60% of maximum is Amber
     65-80% of maximum is Amber and Green
     85-90% or more is Amber, Green, and Red



 Dyaco International Inc.                                                                                                                                                  13
4-3 Function Button Locations




     PROGRAM BUTTONS

    (Manual, Hill, Fat Burn,
       Cardio, Strength,
                                 Control Keys
       HIIT, 2User, 2HR)




           FAN KEY

  Cooling fan switch on or off




  Dyaco International Inc.                      14
                      5. Unit Block Diagrams




Dyaco International Inc.                       15
Dyaco International Inc.   16
             6. Basic Connections and Wiring




Dyaco International Inc.                       17
6-1 Display Board PCB Component Locations

6-1-1 DISPLAY BOARD WIRE CONNECTIONS




   Dyaco International Inc.                 18
6-1-2 PCB BOARD TOP




   Dyaco International Inc.   19
6-1-3 PCB BOARD BOTTOM




   Dyaco International Inc.   20
6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS




   Dyaco International Inc.                          21
6-1-5 AMPLIFIER BOARD WIRE CONNECTIONS




   Dyaco International Inc.              22
6-1-6 TENSION MOTOR CONNECTOR DEFINITION FUNCTION




                                                    1
            STEEL ROPE
                                                    2
                                                    3
                                                    4
                                                    5
                                                    6
                                                    7
                                                    8



                                                    1
                                                    2
                                                        SPEED
                                                        SENSOR
                                                        1 GND
                                                        2 SPEED




   Dyaco International Inc.                                       23
       7. Error Messages / Troubleshooting




Dyaco International Inc.                     24
7-1 Error Codes


                             Error Code   CAUSE
                             E1           EEPROM is defective or operate abnormal.
                             E2           Tension motor is failure
                             E3           Incline motor error



7-2 Prepare tools
                                          Multi-meter




  Dyaco International Inc.                                                           25
7-3 Error Message：E1

    Definition

    The memory IC of EEPROM is defective.

    Troubleshooting

    The display board requires replacement.




7-4 Error Message：E2

    Definition

    Gear motor operate abnormal or display board can’t receive signal from gear motor.

    Troubleshooting

    1. Check the control cable and replug it.
    2. Check the tension motor.




  Dyaco International Inc.                                                               26
Dyaco International Inc.   27
7-4-1 TENSION MOTOR OPERATION

      Display

      Key signal travels to the display. The main program IC then sends a command signal to the drive board.

      Drive Board

      Drive board receives the signal and responds by putting out power to the motor. Level UP:+5VDC;Level DOWN:-5VDC



7-4-2 TENSION MOTOR TROUBLESHOOTING

      Display

      If the key beeps when pressed, assume that the signal was sent.

      Data cable

      Inspect the cable and connections.

      Drive Board

      Inspect drive board power output to the motor. Press the Level Up is +5VDC;Level DOWN is -5VDC.If there is power to the motor, but the
      motor does not operate, replace it. If there is no power output, inspect whether the drive board has power.




   Dyaco International Inc.                                                                                                                    28
7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE

1.   Put multi-meter to the 20VDC setting.Place probes on the motor control wire(Red probe in blue wire, Black probe in green wire) on the drive board.
2.   Turn on unit power.The display lights up.
3.   Press LEVEL UP. Normal reading : +5.5~6.0VDC.Motor operates.Resistance increases.
4.   Press LEVEL DOWN. Normal reading : -5.5~6.0VDC.Motor operates.Resistance decreases.
5.   If there is no voltage,inspect power socket the holder FUSE.If broke replace it.
6.   Inspect the drive board POWER LED whether lit.If no lit the drive board is bad.Replace it.




                                                                                  Place probes on the motor control wire(Red probe
                                                                                  in blue wire, Black probe in green wire) on the
                                                                                  drive board.




     Dyaco International Inc.                                                                                                                             29
7-5 Error Message：E3
    Definition

    The console board is not detecting the VR voltage value or the voltage value has exceeded the range.” STEP ERROR” appears on the display.

    Configuration




  Dyaco International Inc.                                                                                                                      30
  Case of INCLINE E3

  Incline VR value exceeds the range. STEP ERROR appears on the display.
  Incline motor isn’t operation up or down, making the VR value exceed the range.
  After turning on the unit, the display board detects that the incline VR voltage exceeds the range, so INCLINE E3 appears.

  Action Flow Chart




Dyaco International Inc.                                                                                                       31
  Troubleshooting

  Part              Troubleshooting

  Incline VR        1. Reconnect VR wires.
                    2. Inspect whether the incline wires are broken or disconnected.

  Display board     1. Inspect the incline wire and 11-pin cable connections.
                    2. Test whether the VR voltage varies at the incline wire Stepper.

  11-pin cable      1. Inspect the wire connections.
                    2. Inspect whether wires are broken or crimped.
                    3. Replace the wires and test again.

  Driver board      Inspect the display board 11-pin connections.




Dyaco International Inc.                                                                 32
7-6 Test configuration. The console to driver board connector pin define function



         AMP                                             HR HAND
        POWER
                                      FAN

                                                                                1.SPEED
                                                                                2.GND
                                                                                3.VCC+5V
                                                                                4.ZERO
                                                                                5.COUNT
                                                                                6.MOTOR-
                                                                                7.MOTOR+
                                                                                8.VIN
                                HR                                              9.INC UP
                                                                                10.INC DOWN
                             RECEIVE                                            11.INC VR

                                 R
                KEYS


                                                                 11,10,9,8,7,6,5,4,3,2,1



  Dyaco International Inc.                                                                    33
7-7 Engineering Mode Menu

The console has built in maintenance/diagnostic software. The software will allow you to change the console settings from English to Metric and turn off the
beeping of the speaker when a key is pressed for example. To enter the Engineering Mode Menu, press and hold down the Start, Stop and Enter keys. Keep
holding the keys down for about 5 seconds and the message center will display Engineering Mode Menu. Press the Enter button to access the menu below:
1. Key Test (Will allow you to test all the keys to make sure they are functioning)
2. LCD Test (Tests all the display functions)
3. Functions (Press Enter to access settings and Up arrow to scroll)
    i. Display Mode (Turn off to have the console power down automatically after 20 minutes of inactivity)
    ii. Pause Mode (Turn on allow 5 minutes of pause, turn off to have the console pause indefinitely)
    iii. ODO Reset (Resets the odometer)
    iv. Units (Sets the display to readout in English or Metric display measurements)
    v. Beep (Turns off the speaker so no beeping sound is heard)
    vi. Motor Test
    vii. Safety
4. Security (Allows the keypad to be locked to prevent unauthorized use)




    Dyaco International Inc.                                                                                                                                   34
7-8 Troubleshooting procedure matrix

 Condition                                        Reason                                                        Solve
 LCDs not bright, incomplete or imperfect.        1. LCD light is broken.                                       1. Replace with new LCD or console.
                                                  2. Power to console too low.                                  2. Check AC power is 110-120V or 220-240V.
                                                                                                                3. Check power to console.
                                                                                                                4. Replace lower controller.
 LCD displays not bright, incomplete or imperfect. 1. LCD displays are broken.                                  1. Replace with new console.
 The incline position doesn’t match console        1 Console is not calibrated.                                 1 Calibrate the console.
 INCLINE ERR ,INCLINE window displays “STEP        1 Position sensor value of incline motor is wrong.           1 Turn off the AC switch and turn on power again.
                                                                                                                2. Calibrate the monitor.
 ERROR”.
 Erratic pulse display.                            1. Another chest belt in use around Stepper.                 1. Check for other chest belt use around Stepper.
                                                   2. Other magnetic field disturbance.                         2. Change the position or direction of Stepper.
                                                   3. Receiver is broken.                                       3. Replace with new receiver.
 UP/DOWN button of                                 1 The connector of INCLINE CABLE                             1 Connect the wires again.
 INCLINE ADJUSTMENT SWITCH can’t be used.             and CONSOLE not connected properly.
                                                   2. The connector of INCLINE CABLE                            2. Connect the wires again.
                                                   and INCLINE ADJUSTMENT SWITCH W/CABLE not connected
 Incline button just can press UP, can’t press     properly.
 DOWN.                                                                                                          3. Replace the cable.
 Incline button just can press DOWN, can’t press 3 The connector of INCLINE CABLE or
 UP.
                                                   INCLINE ADJUSTMENT SWITCH CABLE
                                                   got damage.                                                  4. Replace buttons.
                                                   4. Button of INCLINE ADJUSTMENT SWITCH is broken.
                                                   5. The connector of INCLINE CABLE or                         5. Replace the cable.
                                                   INCLINE ADJUSTMENT SWITCH CABLE
                                                   got damage.                                                  6. Replace the cable.
                                                   6. The connector of INCLINE CABLE or
                                                   INCLINE ADJUSTMENT SWITCH CABLE
                                                   damaged.
 Hand pulse lost its function.                     1. Hands not on the hand pulse sensors or only one hand on   1. Two hands hold the hand pulse.
 (No pulse displayed on monitor)                      sensor.
                                                   2. The connector of HANDPULSE W/WIRE and Console not         2. Connect the cable again.
                                                      connected properly.

  Dyaco International Inc.                                                                                                                                          35
                                       3. The wires got damaged when connecting the HANDPULSE   3. Replace with new cable.
                                          W/WIRE and Console.
                                       4. Hand pulse board is broken.                           4. Replace console or Hand pulse board.
Wireless lost its function.            1. Chest belt not worn properly.                         1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                                                                    oriented correctly.
                                       2. Distance is too far and exceeds range of receiver.    2. User chest belt in front of console within 3 feet.
                                                                                                3. Replace with new lithium battery type is CR2032.
                                       3. Chest belt battery is weak or dead.
Chest belt too close to the Stepper.   Weak battery.                                            Replace with new lithium battery with type CR2032.




 Dyaco International Inc.                                                                                                                                 36
                           8. Circuit Diagram




Dyaco International Inc.                        37
Dyaco International Inc.   38
                           9. Common Problems




Dyaco International Inc.                        39
9-1 Troubleshooting For Console
The Screen doesn’t lit.
                           Check AC Switch is on.




                           Check all the wires that connect to
                           Console are plug well.




                           Unmount Fuse from AC Switch and
                           check it. If it is defective to do the
                           replacement.




    Dyaco International Inc.                                        40
9-2 Troubleshooting For Pedal arm
Noise from Pedal arm. (It usually cause by the bearing is defective.)
                                          Replace Pedal arm’s bearing.




                                         Replace the Slide wheels’ bearing.




    Dyaco International Inc.                                                  41
9-3 Troubleshooting For Connect arm
Noise from Connect arm.
                           Check Rod end bearing.
                           If this bearing has clearance and cause
                           noise please does the replacement.




                           If the noise comes from Pedal
                           assembly, check Pedal locking screws
                           are secured, and the top of the
                           assembly is taped foam tapes.




    Dyaco International Inc.                                         42
9-4 Troubleshooting For Incline motor and Controller board and Gear motor
Incline motor is no function.
                                Check all the incline motor wires are       If there is no resistance when pedaling,
                                plug well and all the electronic parts      please check console is ok, first.
                                are good.                                   Then check Gear motor is functional.
                                                                            If Gear motor is defective then unmount
                                                                            steel cable and replace Gear motor.




                                Incline motor needs to be adjusted to
                                the right length when doing the
                                replacement.
                                Setting the motor to zero then rotate
                                the outer tube to let the distance
                                between two bolt holes is 245mm.




    Dyaco International Inc.                                                                                     43
9-5 Troubleshooting For Flywheel and Drive belt
Adjust the resistance level but it is not functional or some noise comes from Flywheel.
                                             If Gear motor is operating normally,         b. With low speed operating. If drive
                                             check Steel cable is mounted on              belt, drive pulley and flywheel are not
                                             Flywheel in the right way.                   aligned, please adjust flywheel to make
                                                                                          the alignment.




                                          If there is noise coming when Flywheel          Drive belt slipping problem, please adjust
                                          is spinning.                                    nut on J bolt with 13mm wrench.
                                          Check Flywheel, Drive pulley, and Idle
                                          wheel assembly friction each other
                                          causes the noise. Or Flywheel makes
                                          the noise itself.



                                          Drive belt dropping problem, please
                                          take off chain cover (R) and loosen idler
                                          wheel assembly, and then reassemble
                                          the drive belt.
                                          please check the followings:
                                          a With low speed operating. If drive
                                          pulley swing too much, please make
                                          the replacement.


    Dyaco International Inc.                                                                                                    44
9-6 Troubleshooting For Noise

When the unit has noise problem,
please check the followings and refer
to replaced steps accordingly.
1. Bearings on joint areas.
2. Flywheel.
3. Slide wheels.
4. Pedals.




    Dyaco International Inc.            45
9-7 Troubleshooting For Drive Belt Slipping
When the unit has drive belt slipping problem
                                          Tighten bolt and nut on crank arm.




                                         Adjust drive belt tension with 13mm
                                         wrench.




    Dyaco International Inc.                                                   46
               10. Parts Replacement Guide




Dyaco International Inc.                     47
10-1 Console Replacement                                               10-2 Side Case Replacement
                         Step 1: Remove 4 Console locking                                     Step 1: Use a screwdriver to remove 2
                         screws then unplug all wires and take                                screws then take off both left and right
                         off Console.                                                         side Handle Bar Cover.




                         Step 2: To plug all wires first and install                          Step 2: Use a screwdriver to remove 3
                         Console then secure 4 locking screws.                                screws then take off Console mast cover.
                         Note: All wires should not be pinched.




                                                                                              Step 3: Use a 12mm and 13mm box
                                                                                              wrench to remove Upper Handle Bar
                                                                                              locking bolts and washers then take off
                                                                                              both sides of Upper Handle Bar.




  Dyaco International Inc.                                                                                                          48
                       Step 4: Use a screwdriver to remove       Step 7: Remove Rear Side Case.
                       Chain cover locking screws then take
                       off right Chain Cover.




                       Step 5: Use a screwdriver to remove       Step 8: To do the reverse of above steps
                       left Chain cover locking screws.          to install back.
                                                                 Note: Do not pinched wires.




                       Step 6: To record AC switch wires color
                       and location then unplug wires’. Take
                       off left Chain cover.




Dyaco International Inc.                                                                              49
10-3 Pedal Assembly replacement
                         Step 1: Follow the steps of “Chain cover   Step 4: Take off Pedal Assembly.
                         replacement” to remove both Chain
                         covers.




                         Step 2: Use a 17mm box wrench and an       Step 5: Use a 19mm box wrench to loose
                         M6 Allen-wrench to remove the rod          rod end bearing nut then remove it.
                         end bolt which link Pedal Assembly and
                         Pedal Bar Assembly.




                         Step 3: Use a 12mm box wrench to           Step 6: Use a screwdriver to remove 4
                         remove Pedal Assembly axle locking         Pedal locking screws then take off it.
                         bolt.




  Dyaco International Inc.                                                                               50
                                                            10-4 Pedal Arm replacement
                       Step 7: Use a 12mm box wrench to                           Step 1: Follow the steps of “ Pedal
                       remove Pedal Bar Assembly locking                          Assembly replacement” to take off Pedal
                       bolt and washer then take off it.                          Assembly.




                       Step 8: To do the reverse of above                         Step 2: Remove Slide Wheel Covers with
                       steps to install back.                                     a screwdriver.
                       Note: The Pedal assembly axle must
                       align with Pedal Bracket.




                                                                                  Step 3: Use a 14mm box wrench and a
                                                                                  M8 Allen wrench to remove Pedal Arm
                                                                                  locking bolt then take off it.




Dyaco International Inc.                                                                                             51
                       Step 4: Use a 12mm box wrench to       Step 6: Use a 12mm box wrench to
                       unmount Slide wheel.                   remove Bushing Housing locking bolt
                       Note: The axle must be aligned when    then take off it.
                       installing Slide wheel back.




                                                              Step 7: To do the reverse of above steps
                                                              to install all parts.
                                                              Note: The axle needs be aligned when
                                                              installing.




                       Step 5: Use a 12mm box wrench to
                       remove the bolts which locking Swing
                       Arm A on Pedal Arm Bushing Housing
                       then take off axle.




Dyaco International Inc.                                                                            52
10-5 Swing Arm replacement                                        10-6 Up Right replacement
                         Step 1: Follow the steps of “Side Case                          Step 1: Follow the User manual to take
                         replacement” to take off Side cases.                            off Up Right.
                         Step 2: Use a 12mm box wrench to
                         remove Swing Arm Axle outside locking
                         bolt then unmount axle. Use a 17mm
                         box wrench and a M6 Allen wrench to
                         remove rod end bearing locking bolt
                         then take off Swing Arm C.

                         Step 3: Use a 12mm box wrench to                                Step 2: Remove Round Caps of Handle
                         remove the bolt which locking Bushing                           bar then pull off hand pulse and rapid
                         Housing with mainframe. Then take off                           key wires from handle bar.
                         Swing Arm A and Swing Arm B.




                         Step 4: To do the reverse of above                              Step 3: Use a screwdriver to remove
                         steps to install all parts.                                     Hand pulse screws then take off hand
                         Note: The axle needs be aligned when                            pulse set.
                         installing.




  Dyaco International Inc.                                                                                                    53
                                                               10-7 Rear Rail Assembly replacement
                       Step 4: Pull out Handle bar Rapid key                          Step 1: Follow the steps of “Pedal Arm
                       cap.                                                           replacement” to take off both Pedal
                       Note: Rapid key cap needs be aligned                           Arms.
                       when installing.                                               Step 2: Use a screwdriver to remove
                       Step 5: To do the reverse of above                             Incline Cover locking screw then take off
                       steps to install all parts.                                    Incline Cover.




                                                                                      Step 3: Use 2 14mm box wrenches to
                                                                                      remove Rear Rail assembly locking bolts
                                                                                      then take off Rear Rail assembly.




Dyaco International Inc.                                                                                                    54
                                                             10-8 Incline motor, Gear motor, and Controller board replacement
                       Step 4: Use 2 14mm box wrenches to                                     Step 1: Follow the steps of “Side Case
                       remove Incline Bracket locking bolt                                    replacement” to take off Side case.
                       then take off Incline Bracket.                                         Step 2: Use a screwdriver to remove
                       Step 5: To do the reverse of above                                     Controller board cover locking screw
                       steps to install all parts.                                            then take off the cover.




                                                                                              Step 3: Remember all wires location
                                                                                              before unplug them. Use a screwdriver
                                                                                              to remove Controller board.




                                                                                              Step 4: Before replace gear motor, use
                                                                                              Console to adjust resistance level to
                                                                                              MAX then cut off power. Unmount steel
                                                                                              cable from Gear motor.




Dyaco International Inc.                                                                                                               55
                       Step 5: Use a screwdriver to remove
                       Gear motor and unplug wire. Then take
                       off Gear motor.




                       Step 6: Use 2 17mm box wrenches to
                       remove Incline motor locking bolts. Cut
                       off wire ties and remove Incline motor
                       ground wire with a screwdriver.
                       Disconnect Incline motor wires from
                       Controller board then take off Incline
                       motor.


                       Step 7: To do the reverse of above
                       steps to install all parts.




Dyaco International Inc.                                         56
10-9 Idler Wheel Assembly, Flywheel, and Drive belt replacement
                                 Step 1: Follow the steps of “Gear motor
                                 replacement” to unmount steel cable
                                 from Flywheel. Then use a 13mm box
                                 wrench to remove adjust nut from
                                 J-bolt.




                                 Step 2: Use a 13mm box wrench to          Step 4: Take off Drive belt from Drive
                                 remove Idle wheel Carriage Bolt then      pulley.
                                 take off Idle wheel assembly.




                                 Step 3: Use a 15mm box wrench to          Step 5: To do the reverse of above steps
                                 remove Flywheel locking nuts then take    to install Flywheel and Drive belt. Use
                                 off Flywheel from mainframe.              17mm box wrenches to adjust Flywheel
                                                                           location to let Drive belt center on Drive
                                                                           pulley then secure Flywheel locking nuts.




   Dyaco International Inc.                                                                                         57
                                                                 10-9 Crank and Drive pulley replacement
                                                                                         Step 1: Follow the 10-8 steps to
                                                                                         unmount Drive belt.
                                                                                         Step 2: Use a 12mm box wrench to
                                                                                         remove Crank locking bolt.




                       Step 6: Adjust Idle wheel assembly to                             Step 3: Use a 13mm box wrench and M6
                       let Drive belt at right tension. (Use a                           Allen wrench to loose nuts which locking
                       sonic belt tension meter to measure,                              Crank on Drive pulley Axle. Then take off
                       the right value is 190Hz+/-10Hz.)                                 Crank.
                       Rotate Crank to check Flywheel, Drive
                       belt, and Drive pulley is operating
                       smoothly. Then install all other parts.


                                                                                         Step 4: Use an M2 Allen wrench to loose
                                                                                         2 bolts which locking axle on Bearing.
                                                                                         Then take off Drive pulley assembly.




Dyaco International Inc.                                                                                                      58
                       Step 5: To do the reverse of above
                       steps to install all parts.
                       Note: The direction of the woodruff
                       key, the round head direct to the axle.




Dyaco International Inc.                                         59
Dyaco International Inc.   60


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 118 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Table of Contents

L. OUTINGS oo... cccccccccceseeeeeeeeceeeceeaeseseeeeeeeeeeeeseaeeesseeeeeeeeeeeeaeeaeeseeeeeeeeeeeesaaeeessEEEEESESEGGGAGAAAAAEEEESSSSSSSGIAAAOAAEEEEEESSSSSS;SSAAOSSSEESEESCES;;;;AA ASA AAssEEEEEEEEG;EE OSE E OSES EES 3
Peas =i (1018 0) 0) (08 ok-) ee eee cerns 4
2-1 Upper Controllers...........cccccccccccccccccesesessseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaeeeeseeeeeeeeeeessaaeeeeeeeeeeeeeeessaeeeseeeeeeeeeeeeGGGeeeeseeeeececse;;;;;GGs EEE ECEESEEE;;;O EASA EEEESEEEEEES 5
2-2 Lower Controller ANd Driver ........cccccsssesssscccccccccsseeessseeeeeceeeeeeeeeeeeeeeeeeeeeeeeesaeeeeeeeeeeeeeeeeessaeeeeeeeeeeeeeeeesseaeeeeseeeeeeeeeeesseeeeeeeeseeeeeeeessaaaeaaaseeeeeeeeeeas 6

3. Electrical CONFIQUrATIONS ............ccccccccccccssseeeseeeeeeeceeeeeeeeeeeeeeeeeeeeeeessaaeeeseeeeeeeeeeeGsGGGeesEEEEEESESAGSSAAAAAASEEEESSSSS;S;;GAAEAAEEEESESESS;;;;;AOASSAEEEECEEESEE;;E AAA AA EEEEEEEEEEES 7
va I goo [6 [ 1mm @) 0-1 a- 1410) 0 ese 9
7. BY Sy 6) F- VAN 01010 (0) See eee 10
A-2 OPE ration ........cseccccssscccssccccseeeeeaeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeaaeeeeeeeeeeeeeeeeeGeeeeeeGeeGGAAEEASAAAEESAOES;EAAEEEGIOEES;AAEESS;AAESS;IOESS;;OSS;;OOESE;HOSSE;O AE SEEH OA SEEEEEEEEEES 11
4-2-1 POWER 2.......:cccccccccccccccccueeeeseeeeeeeeeeeeeeeeeeseeeeeeeeeeeeseaeeeeeeeeeeeeeeessaeeeeseeeeeeeeeeeGaGeesesGEEsECEESGGS;AAAAAASESESESS;S;;;;G;ASOSAEESESECEEGE;;;E AAA AAA ES EEEEEEEEEEE BEBE 11

4-2-2 Dot Matrix Center Display ...........cccccccsssssseeecccceeeeseeseeesseeeeeeeeeeseeeeeeeeeeeeeeeeeesaeeeeeeeeeeeeeeeessaeeeeeeeeeeeeeeeeesseeeeeeeseeeeeeeeessaaeaaaseeeeeeeeeeessaaaages 11

4-2-3 1/4 Mille Track wo.cccccccccccccccccccccccccscceceeseeccecccccsseseeueueusceeeescsseseuuuuuusseeecescssseuuuuuusseeesecssseeuuuueussceecessssseuuuuueussceeeessssseuuuuueesceeeeseseseauuaaenes 11

4-2-4 PUISE Grip FEATULe ....... cc cceecececccccccecceeeeeeseeeeeeeeeeeesaeeeeeeeeeeeeeeeeeessseeeeseeeeeeeeeGGGGGGAAAEEEESSSSSS;SSIAAAAAEEESSSSSS;;;;;;ASOSEEEEEEEESGE;;;E AA AAAASESEEEEEEEEE EEE ES 11

7 od @r- 1 (0) 0-08 BY [:) ©) -\ eee ce 11

4-2-6 SPCAKESS .......cccccccccccccccccceaesseeeeeeeeeeeeeeeeseeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeaaeeeeseeeeeeeeeessGGeesesSEEEEEEEGSGSGAAAAAAEEEEESSS;S;S;;GAASSSEEEEESSESEE;;;E AOA AAsSSEEEEEEEEEEE EB EES 12

A-3 FUNCTION BUTTON LOCATIONS .........eeeeceeeccceeeececeeeeecneeeeeneeeeeeaeeeeeeeeeeeeeeeeeeaeeeeeeeeeeeeGeeeeGAAEEE;ASEES;AAAEEESIAEES;;AEEE;;IAEEE;IOEESS;OESS;;AOEEE;AOESE;O AE SESAAASEEHE EE EEEES 14

oan OJ) heal =) (010), as D) F< 24 9-09 | eee 15
6. Basic CONNECTIONS ANC WILING.........cccccceessesseeeeccccceeseaaeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeesssaeeeeeeeeeeeeeeGGGGGGsGsAEEEEES;ESE;;;GAAAAASEESESS;SS;;;;;;AOSASAEEEECESEsE;;E AAA AEEEEEEEEEEEES 17
6-1 Display Board PCB COMPONENt LOCATIONS...........cccssesesssseccccceeceesaeeeseeeeeeeeeeeesaaeeeeeeeeeeeeeeeeesseaeesseeeeeeeeeeeesaaaeeeeseeeeeeeeeesssaueessssseeeeeeeessaauaagaseesees 18
6-1-1 DISPLAY BOARD WIRE CONNECTIONS ............cccccccccccccceeeeeseeeeceeeeeesaeeeeeeeeeeeeeeeesseeeeeeeeeeeeeeeeessseeeeeeeeeeeeeeeeessaeeeeseseeeeeeeeessaaaaeaseeseeeeeeeeas 18

6-1-2 PCB BOARD TOP 1... ..cccccccccccsssessseeeeeeeeeeeeeeaseeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeeesaaeeeeseeeeeeeeeeessaGGeeseeeeecEEGA;;;;GAGAASEEEESSSESSS;;;;AOSSAAEESEEEEEEs;;;A AAA AEEEEEEEEEEES 19

6-1-3 PCB BOARD BOTTOM. ...........:ssssssseeecccceeceseaeseeeeeeeeeeeeesaeeeeeeeeeeeeeeeeeeasaeeesseeeeeeeeeesssaeeeeeeeeeeeeeeeessGeeeesseeeeeeeeeeessaeaeeseeesseeeeeeessauaaesseeseeeeeeeeas 20

6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS. .........ccccccccssssssssseeeeccceeeeeeeeeseeeeeceeeeessseeeesseeeeeeeeeeesseeaeesssseeeeeeeessuaaaesseeseeeeeeeeas 21

6-1-5 AMPLIFIER BOARD WIRE CONNECTIONS ..........ccccccccccscessssseeeeeceeeeeeeaseesseeeeeeeeeeeeseeeeeeeeeeeeeeeeessseeeesseeeeeeeeeeessaeaeesesseeeeeeessssaaaasseeseeeeeeeeas 22

6-1-6 TENSION MOTOR CONNECTOR DEFINITION FUNCTION ...........ccccccccssssssssseecccceeecseeeessseeeeeeeeeesseaeessseeseeeeeeeesseeeeessesseeeeeeesssaaaesseeseeeeeeeeas 23

7. Error Messages /Troubleshooting..........csssssscccccccccccesssssssseeeeecccececesesessseeeeeceeeeeeeeeesseeeeeeeeceeseeeeeesaaseeeeeeeceeeeeeeesassseeeeeeeeeeeeeeesaaaaeeeeeeceeeeeeeesaasaeenss 24
y fas aol 0 0) ol © 00 | 5 eee 25
7-2 Prepare tOOls......... seennnmeeeenennnnnnnsnnennenennnnnnnnsnnnnnnnenennnnnnnnnnennnnnnnennnnnnnnnnnnenennnnnnnnnnnnnntennnnnnnennnnnnnnnnnennntnnnnnnnnnnnnnnnnnnnnnennnnnnnnnnnnnnssstsss 25


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 107 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7-3 Error Message : E1
7-4 Error Message : E2
7-4-1 TENSION MOTOR OPERATION

7-4-2 TENSION MOTOR TROUBLESHOOTING ...........eeeeeeeeeceeeeeeeeeeeeeeeeeeeeeeeeaaaaeeeeeeeeeeeeeeeaaaaaeeeeeeeeeeeeeeeaaaaeeeeeeeeeeeeeeeaaaaasseeeeeeeeeeeeaaaaaseeeeeeeeeeees
7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE ........... ccc seeseeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeenaaaaaeeeeeeeeeeeeeeaaaaeseeeeeeeeeeeeeaaaaasseeeeeeeeeeeeeaaaaaseeeeeeeeeeess

7-5 Error Me@SSage + ES oo... eecceeccescccseccenseceeeeeeeeecaeeeaeeeeeeeeeaeeeeeeeeaeeeeaeeeaeeeeaeeeeaeeeaeeeeaeeeeaeeeaeeeeaeeeGaeeeaeeGaEeGGAESGHEA;GEES;GEES;HES;;EES;;H ESSE SEGHESSEE ESSE EEEE SEES
7-6 Test configuration. The console to driver board connector pin define function
7-7 Engineering MOde MENU .......ccccccccccsssssssseeeeccceeeeeeaaeeeseeeeeeeeeeeeeseaeeeseeeeeeeeeeeesseeeeeeeeeeeeeeeeesGGGeeesSeeeeeeESSGG;;GAAGSAAEESESECSSES;;;AG SS AOAsEEEEEEESESGEA OE AEOEEEEES
7-8 Troubleshooting ProceCure MaAtrix..........ccccccccccccccseessseeeeececeeeeeeseesesseeeeeeeeeeessaeeeeeeeeeeeeeeeesseseeeseeeeeeeeeeeessaeeeeseeeeeeeeeessssaeaeessssseeeeeesssaauaagaseeeess
8. CIrCUit Diagram ........ccceeccccsesccceseeeeneseeeeaeeeeneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeGeeeeeaseeeeeaeeeeGGeeeeGGGeeeGAAEESAAASEEGIAEEE;AOEESSIISES;IAEEE;AOEES;;OSSS;IOSES;EOESS;OOESSGHAEEEEOEEEEO EEE ES
oan @o) 0010010) 00N 22 0) 0) (=) 0 0 eens
9-1 Troubleshooting FOr CONSOLE............ccccccccccccccceseeeesseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseseeeeeeeeeeeeeeeessGeeeesseeeeeeeeeeessGeeeeseeeeeeeeeeeessaeeeeeesseeeeeeeessaaaaaesseseeeeeeees
9-2 Troubleshooting For Pedal Arm ...........ccccccccccccsssessssseeeeeeceeeeeeeeeeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeesGeeeeseeeeeeeeeeeessaeeeeseeeeeeeeeeeeseeeeeeesseeeeeeeessauaaaaseseeeeeeeeas
9-3 Troubleshooting FOr CONNECE ALM... ccccccccccsssseeseeeeeeeceeeeeaeeeeeeeeeeeeeeeeeeseaeeeeeeeeeeeeeeeeesGeeeeseeeeeeeeeeeeGsGaeeeseeeeeeeeesesGsssGsssssSEEEEEEGsEs;GE AA AAEEEEEEEEEEES
9-4 Troubleshooting For Incline motor and Controller board and Gear MOTOS ........ccccccccsssssssseeeececeeeecaeesesseeeeceeeeesseueesseeeeeeeeeeesssauaaasseeseeeeeeees
9-5 Troubleshooting For Flywheel and Drive Delt .............cccccccccsssssssseeeeecceeeeeeeeeeeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeseeeeeeseeeeeeeeeeeeseaueeesssseeeeeeeessaaaaaaseeeeeeeeeees
9-6 Troubleshooting FOr NOISE ...........ccsessesseccccccccceeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeessGeeeesSeeeeeGESS;;;;AAAAAEEESSSSESS;;;;GAOSSSAEEEEEESESE;;GE AA AOAEEEEEEEEEEES
9-7 Troubleshooting For Drive Belt SliPPing .............ccccccccccccccccceeesssseeeceeeeeeeseeeeeeeeeeeeeeeeeeeseseeeseeeeeeeeeeeesseeeeesseeeeeeeeeeeseaeeeeeesseeeeeeeessaaaeaaseeeeeeeeeeas
10. Parts Replace Ment Guide ...........ccccccccccccccccccceeesseeeeeeeeeeeeeseeeeeseeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeesssGGeesSeEsEECEE;;;;;;AAAASOEESEESEEEESE;;GA SAA AAASEEEEEEEEEEEE EBB ES
10-1 Console REPlaceMeNt ...........ccccccccccccccccccaessseeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeseeeeeeeeeeeesseeseeeGeseeesGEG;;;;GAAAAEEEEEEESES;;;;AAAASSSEESEESESESS;;;A AAA SAO SE EEEEEEEEEEE BEBE
10-2 Side Case REPlaceME Nt ............ccccccccccccccceeesssseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeseeeeeeeeeeeeseGeeeeeeeeeeeeeeeGGGGGGAAsEEEEEEESSS;;;;;AOASASEESESSCESE;;EGA OA ASASEEEEEEEEEEEE BEBE
10-3 Pedal Assembly replace Mme nt ...........cccccccssssssseeeecceceeeeeaeeeeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeesseeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeeessseeeeeeeeeeeeeeeeesaaaaeesssseeeeeeeeeeaaaaees
10-4 Pedal Arm replace Me nt ............cccccccccccccsssessseeeecceeeeeesaeeesseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeesseeeeeeeeeeeeeeeeessGeeeeseeeeeeeeEs;;;;;AAASSSSESEESCEES;;;;A AAA AOSAEEEEEEEEEEEE BEBE
10-5 SWING ArM rePlACEMENK ............ccccccccccccccesesseseeeeeceeeeeeeeeeeseeeeeeeeeeeeesseeeeseeeeeeeeeeeeGGGGseesSEEEEESESSSSSAGAAAAAEEEESESSSS;;;;AAAASEEESESSECES;;;;E OSA SASEEEEEEEEEEEEE BEBE
10-6 Up Right replaceMent ............ccccccccccccccccceeeseeeeeeeeeeeeesseeeseeeeeeeeeeeeeeseeeeeseeeeeeeeeeeesseeeeeeeeeeeeeeeeGssGGeeesGEEEEE;ES;;;;;;AOASAEESESECEES;;;;A OAS AASESEEEEEEEEEEE BEBE
10-7 Rear Rail Assembly replace Ment ............:ccsssssseeecccccecceeeeeeseeeeeeeeeeeeeeeeseeeeeeeeeeeeeesaeeeeeeeeeeeeeeeeeesseeeeeeeeeeeeeeeeeseeeeeeseeeeeeeeeeeeseaaeeesssseeeeeeeeeeaaagees
10-8 Incline motor, Gear motor, and Controller board replace Ment ...........cccccccsssesccecceeseecceccueseccecsauseecceecuuseecceesauseccesseueeeecessuuneeceseseugeceeeeauggess
10-9 Idler Wheel Assembly, Flywheel, and Drive belt replaceMent ..............ccccccccccccccseessseeeeccceeeeeseesseseeeeeeeeeeeesseeeesseeeeeeeeeesseaaasesseeeeeeeeeeseaaagees
10-9. Crank. and. Drive pulley replace Ment. .csnssss«««nn..sssssnnnssssssessesesesssnn ss eeeeean see eeann nse easn nsw lleenleen NNN « «==


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
€ "DU JOUOILOUIdJU] OODA

SOUI]INO ‘L


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
v "DU JOUOILOUIdJU] OODA

SJL DIUON}D9]Z 'Z


=== OCR SUPPLEMENT, PDF PAGE 6 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
G “OU JOUOILOUE}U] OODAG

Ae\dsiq

S19|]O1JUOD JaddA T-Z


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
L "DU JOUOILOUIdJU] OODA

suoizeanbhijuo) jediaz3a/9 “€


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6 "DU JOUOILOUIdJU] OODA

uoize139dQ9 JINPOAd ‘Vv


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 42 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
dyaco

4-1 Display Windows

ne
E
calories TIME VEArcAL ” -
9000 RYeTeTae 7.5” LCD Display
Sieieie | j fj i j Sieieioie =
ajeia. Sie iaiaie.
ainie a @ ! I aimiaieie
TTT
Zig sees
ain =

Tm Mmm Mme =
ey Cs EE OT ee Ee OT Ee Ee on
Dil ld bid al id Gd la bia JA

YY AN AA AY A TA A TAS

SPIRIT

10


=== OCR SUPPLEMENT, PDF PAGE 15 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4-3 Function Button Locations

cCALoMES TIME VERTICAL
Si aiaie, Siaiaie,

Wa ls 17) Wal ’ vr Wa ve a aa fs CCl
ee Ee OT MA IMA Ia IMA et a
Ord al hd Gd al Gnd hd lad neal fA
YAY AA AN it A TA A TAS

SPIRIT

14


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
GT
"DU JOUO|LOUJEJU] OODAG

sweibeig 430]g UN ‘S


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
KEY | — WIRELESS HR
RECEIVER
verity DISPLAY BOARD
THUMB
SWITCH
HANDLEBAR LR

AMPLIFIER

LINE IN |

TENSION
MOTOR

FUSE =

tL Ke

RPM
SENSOR

Dyaco International Inc. 16


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1 Display Board PCB Component Locations

6-1-1 DISPLAY BOARD WIRE CONNECTIONS

AMP. ° HR
POWER. FAN HANDLEBAR.
JK7. JK13. IK4.
AAOI75.
WIRELESS:
HR aa % *
KEY» SYSTEM.

BOARD- CABLE.

Dyaco International Inc. 18


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
dyaco

6-1-3 PCB BOARD BOTTOM

A512-210121006/200
1) 001} ARE a
BO0BAA017530141
PA-AAO175¢
AAO1755-200428 V1.1

P
Soe RR FOE a Fy |
© abelian iad bniaiaNdibiiaiai
MOARAELEARaba ees esraiateg at
=

beaauugd
genee2z2 3

fititiag

20


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS

IK7+ THUMB
SWITCHe

J INCLINE

SYSTEM WIRE» K JR6« THUMB
20 SWITCHe

HANDGRIP
JK11 JK10+ PLUSE
SENSOR#

HANDGRIP
PLUSE
SENSOR#

Dyaco International Inc. 71


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1-5 AMPLIFIER BOARD WIRE CONNECTIONS

SPEAKER
= (2 PINS)
1K7
AUDIO IN Tisuaanink BOARD
YJ-8509
SPEAKER
= (2 PINS)

POWER ———+| JK2

Dyaco International Inc. 22


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
cc

dddds ¢
CND I
YOSNAS
dddds

-—_——%

NOILONNA NOILINISAG YOLOANNOD YOLOW NOISNAL 9-T-9


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
VC "DU JOUOILOUIdJU] OODA

Hul}ooUsajqnoll / sabessayy 40419 “2


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
DISPLAY BOARD ‘ UPDOWNKEYS | panctwn Keys

LEVEL z LEVEL
COUNT is UP/DOWN
SIGNAL = SIGNAL

wy"

MOTOR VOLTAGE

sled] TENSION
MOTOR

Vi
DRIVER BOARD COUNT
NI

Dyaco International Inc. 7


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7-5 Error Message : E3

Definition

The console board is not detecting the VR voltage value or the voltage value has exceeded the range.” STEP ERROR” appears on the display.

Configuration

DISPLAY BOARD

INCLINE
VR
VOLTAGE

INCLINE
MOTOR

DRIVER BOARD ee VR VOLTAGE INCLINE VR SET

€) INCLINE DOWN LED

O INCLINE UP LED

Dyaco International Inc. 30


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ve

7-6 Test configuration. The console to driver board connector pin define function

ee be be We

elotindedet-d-de

eek ee : =

A512-210121006/200
QE N01 OEY

BO08AA01 7530141
3 a i paaaoi7s: | CSPEED

ssoitesgnoge vin! 2.GND
3.VCC+5V
ee 4.ZERO -
age. Ge 5.COUNT
" ee 6.MOTOR- ' \ |
ree 7.MOTOR+ a)
9.INC UP 8
10.INC DOWN a
11.INC VR

weeds

11,10,9,8,7,6,5,4,3,2,1

33


=== OCR SUPPLEMENT, PDF PAGE 38 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LE "DU JOUOILOUIdJU] OODA

wejibeig NIAID “8


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SE "DU JOUOILOUIdJU] OODA

7 [> YOLOW
8 g. a uva9
2 = Wdd
5 S

fe}
“7
YOLOW <
ANIIONI sab)
Ss
(0)

SIGED YAU ED ONIL

Nes YsaTIONLNOO

‘S1IM YOR|G

SIM SOUUM Woo
OM Poy an
NOW NOV
i
OHO =
OVO a =
zm =
Q 2
Oo YOSNAS g
= 3S1NdGNvH : &
U
Cc
a a
m
ys) ———
oO
& LFINI SONVIIddV
oD

"

yY Y

—_ @uYOo YAMOd

AIOSNOO

oopDhp


=== OCR SUPPLEMENT, PDF PAGE 40 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6€ "DU JOUOILOUIdJU] OODA

SW9/qG0ig UOWIWIOD 6


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9-5 Troubleshooting For Flywheel and Drive belt

Adjust the resistance level but it is not functional or some noise comes from Flywheel.

Naw, If Gear motor is operating normally,
wee check Steel cable is mounted on

Flywheel in the right way.

b. With low speed operating. If drive
belt, drive pulley and flywheel are not
aligned, please adjust flywheel to make
the alignment.

Z

If there is noise coming when Flywheel Drive belt slipping problem, please adjust

is spinning. nut on J bolt with 13mm wrench.
Check Flywheel, Drive pulley, and Idle
wheel assembly friction each other
causes the noise. Or Flywheel makes

the noise itself.

take off chain cover (R) and loosen idler

a ane Tl | Drive belt dropping problem, please

| —| wheel assembly, and then reassemble
the drive belt.

please check the followings:

a With low speed operating. If drive
pulley swing too much, please make

the replacement.

Dyaco International Inc. AA


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Step 4: Take off Pedal Assembly.

10-3 Pedal Assembly replacement
Step 1: Follow the steps of “Chain cover { (
replacement” to remove both Chain ql | (/

“s
“sae
eo
covers. “eg | /
> r~
——

SS“

I Step 2: Use a 17mm box wrench and an Step 5: Use a 19mm box wrench to loose

M6 Allen-wrench to remove the rod rod end bearing nut then remove it.
end bolt which link Pedal Assembly and

Pedal Bar Assembly.

Step 3: Use a 12mm box wrench to Step 6: Use a screwdriver to remove 4
remove Pedal Assembly axle locking

bolt.

Pedal locking screws then take off it.

Dyaco International Inc. 50
