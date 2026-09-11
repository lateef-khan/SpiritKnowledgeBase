<!-- Source: CS800 Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

CS800( 2020)
Service Manual




             Service Manual
                                                                                          Table of Contents
1. CS800(2020) Outlines .......................................................................................................................................................................................... 3
2. CS800(2020) Electronic Parts ............................................................................................................................................................................... 6
    2-1 Upper Controllers......................................................................................................................................................................................... 7
    2-2 Lower Controller and Driver ......................................................................................................................................................................... 8
3. Electrical Configurations ...................................................................................................................................................................................... 9
4. CS800(2020) Product Operation ........................................................................................................................................................................ 11
    4-1 Display Windows ........................................................................................................................................................................................ 12
    4-2 Operation ................................................................................................................................................................................................... 13
        4-2-1 POWER .............................................................................................................................................................................................. 13
        4-2-2 QUICK START ..................................................................................................................................................................................... 13
        4-2-3 BASIC INFORMATION ......................................................................................................................................................................... 13
        4-2-4 1/4 MILE TRACK................................................................................................................................................................................. 14
        4-2-5 HEART RATE WINDOW ...................................................................................................................................................................... 14
        4-2-6 PROGRAMMABLE FEATURES ............................................................................................................................................................. 14
        4-2-7 CSAFE FEATURE ................................................................................................................................................................................. 14
5. CS800(2020) Unit Block Diagrams ...................................................................................................................................................................... 16
6. CS800(2020) Basic Connections and Wiring ....................................................................................................................................................... 18
    6-1 Display Board PCB Component Locations ................................................................................................................................................... 19
        6-1-1 DISPLAY BOARD WIRE CONNECTIONS ............................................................................................................................................... 19
        6-1-2 PCB BOARD TOP ................................................................................................................................................................................ 20
        6-1-3 PCB BOARD BOTTOM ........................................................................................................................................................................ 21
        6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS .................................................................................................................... 22
        6-1-5 GENERATOR FLYWHEEL DEFINITION FUNCTION ................................................................................................................................ 23
7. CS800(2020) Error Messages / Troubleshooting ................................................................................................................................................ 24
    7-1 Error Codes ................................................................................................................................................................................................ 25
    7-2 Prepare tools.............................................................................................................................................................................................. 25
    7-3 Error Message：EEPROM ERROR............................................................................................................................................................... 26
     Dyaco International Inc.                                                                                                                                                                                        1
    7-4 Error Message：Err ................................................................................................................................................................................... 26
        7-4-1 TENSION MOTOR OPERATION ........................................................................................................................................................... 27
        7-4-2 TENSION MOTOR TROUBLESHOOTING .............................................................................................................................................. 28
        7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE ................................................................................................................................... 29
    7-5 Test configuration and the console to driver board connector pin define function .................................................................................... 30
    7-6 MAINTENANCE MENU IN CONSOLE SOFTWARE ......................................................................................................................................... 31
    7-7 Troubleshooting procedure matrix ............................................................................................................................................................. 32
8. Circuit diagram(CS800(2020)) ............................................................................................................................................................................ 33
9. Troubleshooting(CS800(2020)) .......................................................................................................................................................................... 35
    9-1 Troubleshooting for the console ................................................................................................................................................................ 36
    9-2 Troubleshooting for the Flywheel............................................................................................................................................................... 37
    9-3 Troubleshooting for Drive Belt ................................................................................................................................................................... 38
    9-4 Troubleshooting for Swing Assembly.......................................................................................................................................................... 39
    9-5 Troubleshooting for Connecting Arm ......................................................................................................................................................... 40
10. Parts Replacement Guide ................................................................................................................................................................................ 41
    10-1 Console Replacement .............................................................................................................................................................................. 42
    10-2 Chain Cover Replacement ........................................................................................................................................................................ 43
    10-3 Swing Assembly Replacement .................................................................................................................................................................. 46
    10-4 Linked Assembly Replacement ................................................................................................................................................................. 48
    10-5 Connecting Arm Replacement.................................................................................................................................................................. 49
    10-6 Console Mast Replacement...................................................................................................................................................................... 50
    10-7 Rail Tube Replacement ............................................................................................................................................................................ 51
    10-8 Crank Arm Assembly Replacement .......................................................................................................................................................... 52
    10-9 Idle Wheel Assembly Replacement .......................................................................................................................................................... 53
    10-10 Flywheel and Drive Belt Replacement .................................................................................................................................................... 55




     Dyaco International Inc.                                                                                                                                                                                2
                     1. CS800( 2020) Outlines




Dyaco International Inc.                        3
                                               Console

  Console Mast Cover (R)

                                Console Mast Cover (R)

  Chain Cover (L)

                                      Handle Bar Cover (R)

  Pedal (L)

                                       Chain Cover (R)

  Pedal (R)

                                          Rear Side Case

  Left Slider Cover

                                         Right Slider Cover

  Handgrip CapCover (L) & (R)




Dyaco International Inc.                                      4
                                          Console Mast
 Left Handgrip
                                       Right Handgrip


                                           Drive Pulley
  Crank Arm Assembly

                                      Swing Assembly

   Rail Tube
                                            Flywheel


                                 Idler Wheel Assembly
 Connecting Arm (L)

                                          Main Frame

 Connecting Arm (R)
                                 Linked Assembly ( R)


 Rear Stabilizer           Handgrip Connecting Tube




Dyaco International Inc.                                  5
             2. CS800( 2020) Electronic Parts




Dyaco International Inc.                        6
2-1 Upper Controllers


            Console

                             Cooling Fan




  Dyaco International Inc.                 7
2-2 Lower Controller and Driver




         Tension Motor

                                  Speed Sensor




  Dyaco International Inc.                       8
                 3. Electrical Configurations




Dyaco International Inc.                        9
Part Name             Part Description

Console               Interface that controls all functions of the Stepper.

MAIN CONTROLLER       The circuit board consist of the DC power supply for console.

ECB BRAKE             It can change to increase or decrease resistance level of brake.



GENERAL INFORMATION

CONSOLE               Contains Key controls and LED Display.
                      Main controller include power supply、ECB driver control circuit.




Dyaco International Inc.                                                                 10
         4. CS800( 2020) Product Operation




Dyaco International Inc.                     11
4-1 Display Windows


                                  LED DATA DISPLAY
                                  WINDOWS
            SCAN BUTTON FOR LED
            WINDOW
                                  Dot-Matrix
                                  MESSAGE CENTER


            SCAN BUTTON FOR
            Dot-Matrix            UP, DOWN
                                  PROGRAM CONTROL




                                  COOLONG FAN
            COOLING FAN
                                  SWITCH



                                  USB
                                  CHARGER
            START, STOP
            LEVEL CONTROLS




  Dyaco International Inc.                           12
4-2 Operation
 4-2-1 POWER

 When the AC power cord is connected to the Stepper, the console will automatically power up. When initially powered on the console will perform an internal
 self-test. During this time all the lights will turn on. When the lights go off, the Message Center will show the software version (i.e.: VER 1.0). The message
 window shows the total hours of use and total ksteps. The odometer will remain displayed for only a few seconds then the console will go to the start up display.
 The dot matrix display will be scrolling through the different profiles of the programs and the Message Center will be scrolling the start up message. You may now
 begin to use the console.

 4-2-2 QUICK START

 This is the quickest way to start a workout. After the console powers up you just press the Start key to begin. This will initiate the Quick Start mode. In Quick Start
 the Time will count up from zero, all workout data will start to accrue and the workload may be adjusted manually by pressing the Level Up and Down buttons.
 The dot matrix display will show just the bottom row lit. As you increase the workload more rows will light indicating a harder workout. The Stepper will get
 harder to pedal as the rows increase. The dot matrix has 24 columns of lights and each column represents 1 minute. At the end of the 24th column (or 24
 minutes of work) the display will wrap around and start at the first column again.
 There are 20 levels of resistance available for plenty of variety. The first 5 levels are very easy workloads and the changes between levels are set to a good
 progression for de-conditioned users. Levels 6-10 are more challenging, but the increases in resistance from one level to the next remain small. Levels 11-15 start
 getting tough as the levels jump more dramatically. Levels 16-20 are extremely difficult and are good for short interval peaks and elite athletic training.

 4-2-3 BASIC INFORMATION

 The Dot Matrix, or Profile Window, will display the workout Profile. The Message window displays pertinent exercise data. There is a Strides Per Minute window
 for pedal speed and a Level window indicating machine resistance.
 The Message Window will initially be displaying Steps ,Calories ,Pulse and Time Elapsed information. When the Scan key (△▽) is pressed the next set of
 information will appear: Vertical Distance ,Watts ,METs and Time Remaining. Pressing the Scan button, the Scan mode is activated and the Message Window will
 show each set of data for four seconds then switch to the next set of data in a continuous loop. Pressing the Scan button again will bring you back to the
 beginning.

  Dyaco International Inc.                                                                                                                                                 13
The Stop key button actually has several functions. Pressing the Stop key once during a program will pause the program for 5 minutes. If you need to get a drink,
answer the phone, or any of the many things that could interrupt your workout, this is a great feature. To resume your workout during Pause just press the Start
key. If the Stop key is pressed twice during a workout, the program will end and the console will return to the start-up screen. If the Stop key button is held down
for 3 seconds, the console will perform a complete Reset. During data entry for a program the Stop key performs a Previous Screen function. This allows you to go
back one step in the programming each time you press the Stop key button.
The Program Key is used to preview each program. When you first turn the console on, you may press program key to preview what the program profile looks
like. If you decide that you want to try a program, press the Enter key to select the program and enter into the data set-up mode.

4-2-4 1/4 MILE TRACK

The 1/4-mile track (0.4 km) will be displayed around the dot matrix window. The flashing dot indicates your progress. In the center of the track there is a lap
counter for reference.

4-2-5 HEART RATE WINDOW

The Pulse (Heart Rate) window will display your current heart rate in beats per minute during the workout. You must use both left and right stainless steel sensors
to pick up your pulse. Pulse values are displayed anytime the computer is receiving a Grip Pulse signal. You may use the Grip Pulse feature while in Heart Rate
Control. The CS800 will also pick up wireless heart rate transmitters that are Polar compatible, including coded transmissions.

4-2-6 PROGRAMMABLE FEATURES

Each of the programs can be customized with your personal information and changed to suit your needs. Some of the information asked for is necessary to
ensure the readouts are correct. You will be asked for your Age and Weight. Your Age is also necessary during the Heart Rate control program to ensure the
correct settings are in the program for your Age. Otherwise the work settings could be too high or low for you; entering your Weight aides in calculating a more
correct Calorie reading. Although we cannot provide an exact calorie count we do want to be as close as possible.

4-2-7 CSAFE FEATURE

Your console is equipped with a C-SAFE feature. The Power (POWER) port can be used for powering a remote controlled audio-visual system by connecting a
cable from the remote to the Power port at the back of the console. The Communication port (COMM) can be used to interact with fitness software applications.

 Dyaco International Inc.                                                                                                                                          14
4-2-8 TO TURN STEPPER OFF

The display will automatically turn off (go to sleep) after 30 minutes of inactivity. This function is called sleep mode. In sleep mode, the stepper will power down
most everything except for a minimum of circuitry for detecting button presses and the safety button so it will start up again if these are activated. There is only a
tiny amount of current used in sleep mode (about the same as your TV when it is turned off) and it is perfectly fine to leave the main power switch on in sleep
mode. Of course you may also remove the safety
button or turn off the main power switch to power down the stepper.




 Dyaco International Inc.                                                                                                                                                15
       5. CS800( 2020) Unit Block Diagrams




Dyaco International Inc.                     16
Dyaco International Inc.   17
         6. CS800( 2020) Basic Connections and

                                       Wiring




Dyaco International Inc.                         18
6-1 Display Board PCB Component Locations

6-1-1 DISPLAY BOARD WIRE CONNECTIONS




   Dyaco International Inc.                 19
6-1-2 PCB BOARD TOP




   Dyaco International Inc.   20
6-1-3 PCB BOARD BOTTOM




   Dyaco International Inc.   21
6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS




   Dyaco International Inc.                          22
6-1-5 GENERATOR FLYWHEEL DEFINITION FUNCTION




                                                   MAIN CONTROL
        STEEL ROPE
                                                   1. M-

                                                   2. M+

                                                   3. +5
                                               1
                                               2
                                                   4. VR
                                               3
                                               4
                                                   5. GND
                                               5




   Dyaco International Inc.                                       23
                7. CS800( 2020) Error Messages /

                               Troubleshooting




Dyaco International Inc.                           24
7-1 Error Codes


                             Error Code     CAUSE
                             EEPROM ERROR   EEPROM failure
                             Err            Tension Motor failure



7-2 Prepare tools
                                            Multi-meter




  Dyaco International Inc.                                          25
7-3 Error Message：EEPROM ERROR

    Definition

    When EEPROM is defective or has memory access problems, the console will shut all display windows off and stop all the outputs. The Main
    Window will show “EEPROM ERROR”.

    Troubleshooting

    The console requires replacement.




7-4 Error Message：Err

    Definition

    When the tension motor feedback signal is abnormal or no feedback to the console, all the outputs will stop and all the display windows are
    blank but the LEVEL window will show “Err”.

    Troubleshooting

    1. Check the control cable and replug it.
    2. Check the tension motor.




  Dyaco International Inc.                                                                                                                        26
                           DISPLAY BOARD                        LEVEL +/- KEYS
                                                     +/- KEYS




              LEVEL VR                     LEVEL +/-

               SIGNAL           10 PINS     SIGNAL




                         TENSION MOTOR



Dyaco International Inc.                                                         27
7-4-1 TENSION MOTOR OPERATION

      Console

      1. Key signal travels to the display. The main program IC then sends a command signal to the drive board.
      2. Console directly controls the motor. Level UP:+4~5VDC;Level DOWN:- 4~5VDC



7-4-2 TENSION MOTOR TROUBLESHOOTING

      Console

      1. If the key beeps when pressed, assume that the signal was sent.
      2. Inspect console power output to the motor. Press the Level Up is +4~5VDC;Level DOWN is -4~5VDC.If there is power to the motor, but the
         motor does not operate, replace it. If there is no power output, inspect whether the transformer has power.

      Data cable

      Inspect the cable and connections.




   Dyaco International Inc.                                                                                                                       28
7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE

1.   Put multi-meter to the 20VDC setting. Place probes on the motor control wire(Red probe in blue wire, Black probe in green wire) on the drive board.
2.   Turn on unit power. The display lights up.
3.   Press LEVEL UP. Normal reading: +4~5VDC.Motor operates. Resistance increases.
4.   Press LEVEL DOWN. Normal reading: -4~5VDC.Motor operates. Resistance decreases.
5.   If there is no voltage, check the transformer, if there is no output, replace it.




                                                                                          Place probes on the motor control wire(Red probe
                                                                                          in palm wire, Black probe in black wire) on the
                                                                                          drive board.




     Dyaco International Inc.                                                                                                                              29
7-5 Test configuration and the console to driver board connector pin define function

                                                                     The console to driver board
                                                                     connector pin define function:
                                                                     1. MTR-
                                                                     2. MTR+
                                                                     3. 5V
                                                                     4. MTR_AD
                                                                     5. GND
                                                                     6. RPM
                                                                     7. GND
                                                                     8. N/A
                                                                     9. GND
                                                                     10. 12V
                                                                     11. N/A
                                                                     12. N/A
                                                                     13. N/A
                                                                     14. N/A

                               1 2 3 4 5 6 7 8 9 10 11 12 13 14

  Dyaco International Inc.                                                                            30
7-6 MAINTENANCE MENU IN CONSOLE SOFTWARE

To enter the Maintenance Mode, pedal the elliptical and press and hold down the Start, Stop and Enter keys. Keep holding the keys down for about 5 seconds and the
Message Center will display Maintenance Mode. Press the Enter key to access the menu below:
1. Key Test (Will allow you to test all the keys to make sure they are functioning)
2. Display Test (Tests all the display functions)
3.   Function
      -Units (Sets the display to read out in English or Metric display measurements)
           -Pause mode (have five minutes)
           -Odometer Reset (Resets the odometer)
         -Sleep mode
           -Beep sound(Control Beep)
           -CAB Protocol or CSAFE Protocol
4.   Service
            -Motor test
            -Csafe test
            -Sensor test(Test the speed sensor function)
5.   Exit




     Dyaco International Inc.                                                                                                                                        31
7-7 Troubleshooting procedure matrix

 Condition                                           Reason                                      Solve
 LEDs not bright, incomplete or imperfect.           1. LED light is broken.                     1. Replace with new LED or console.
                                                     2. Power to console too low.                2. Check AC power is 220-240V or 110-120V.
                                                                                                 3. Check power to console.
                                                                                                 4. Replace lower controller.
 LED displays not bright, incomplete or imperfect.   1. LED displays are broken.                 1. Replace with new console.
 Erratic pulse display.                              1. Another chest belt in use around         1. Check for other chest belt use around Stepper.
                                                        Stepper.                                 2. Change the position or direction of Stepper.
                                                     2. Other magnetic field disturbance.        3. Replace with new receiver.
                                                     3. Receiver is broken.
 Hand pulse lost its function.                       1. Hands not on the hand pulse sensors or 1. Two hands hold the hand pulse.
 (No pulse displayed on monitor)                        only one hand on sensor.
                                                     2. The connector of HANDPULSE W/WIRE 2. Connect the cable again.
                                                        and Console not connected properly.
                                                     3. The wires got damaged when connecting 3. Replace with new cable.
                                                        the HANDPULSE W/WIRE and Console.
                                                     4. Hand pulse board is broken.              4. Replace console or Hand pulse board.
 Wireless lost its function.                         1. Chest belt not worn properly.            1. Check chest belt has proper contact with skin and is oriented
 (No pulse displayed on monitor)                     2. Distance is too far and exceeds range of    correctly.
                                                     receiver.                                   2. User chest belt in front of console within 3 feet.
                                                     3. Chest belt battery is weak or dead.      3. Replace with new lithium battery type is CR2032.
 Chest belt too close to the Stepper.                Weak battery.                               Replace with new lithium battery with type CR2032.




  Dyaco International Inc.                                                                                                                                      32
           8. Circuit diagram( CS800( 2020) )




Dyaco International Inc.                        33
Dyaco International Inc.   34
          9. Troubleshooting( CS800( 2020) )




Dyaco International Inc.                       35
9-1 Troubleshooting for the console
Situation:
No display on monitor.
Solve:
1. Check the power supply or test with a new one.
2. Check all computer cables are plug well.




3.   Check all wires inside the console and the chain cover are plug well. And check there are no pinched wires.




     Dyaco International Inc.                                                                                      36
9-2 Troubleshooting for the Flywheel
Situation:
The console can adjust the resistance level and gear motor operates normally, but the resistance doesn’t change.
Solve:
Check the steel cable is mounted on the flywheel.




Situation:
There is a noise when the flywheel is spinning.
Solve:
Check the noise is from the flywheel friction drive pulley or idle wheel. If so follow the replacement steps to reinstall those parts.
If the noise comes from flywheel, please do the replacement.




    Dyaco International Inc.                                                                                                             37
9-3 Troubleshooting for Drive Belt
Situation:
Drive Belt drops from drive pulley.
Solve:
Follow the Chain cover replacement to take off right Chain cover and loose the idle wheel assembly then mount Drive Belt back.
Spin the drive pulley slowly to see if the drive pulley swings too much or the drive pulley, idle wheel, and flywheel are not aligned to cause Drive Belt to fall off.
Then spin the drive pulley in high speed (100~120RPM) to test again.
If the drive pulley, flywheel pulley, and idle wheel assembly are not aligned, to adjust the flywheel to appropriate locate can fix it.




Situation:
Drive Belt is Skidding.
Solve:
To use a 13mm open-end wrench to adjust the nut of J-Bolt can fix it.




If Drive Belt is worn please do the replacement.

    Dyaco International Inc.                                                                                                                                             38
9-4 Troubleshooting for Swing Assembly
Situation:
There is a clearance between bushing and axle.
Solve:
The bushing may be worn after a long time of usage requires replacement.




    Dyaco International Inc.                                               39
9-5 Troubleshooting for Connecting Arm
Situation:
The broken pedal.
Solve:
To do the pedal replacement.




Situation:
There is a vibration feeling from feet when pedaling.
Solve:
It’s maybe the bearing of Slide wheel is defective require replacement.




    Dyaco International Inc.                                              40
                 10. Parts Replacement Guide




Dyaco International Inc.                       41
10-1 Console Replacement
Step 1: Use a screwdriver to remove 4 screws (5*10mm) which locking console on console mast.




Step 2: Unplug wires then take off the console.




Step 3: Plug wires back before install the console then tighten 4 screws back.
Note: Do not pitch the wires.




    Dyaco International Inc.                                                                   42
10-2 Chain Cover Replacement
Step 1 : Use a screwdriver to remove both side handle bar cover.




Step 2: Use a screwdriver to remove 3 screws(ψ4*15mm) then take off console mast covers.




Step 3: Use a screwdriver to remove 7 screws(ψ4*15mm).




    Dyaco International Inc.                                                               43
Step 4: Remove a screw which locking both left and right chain covers.




Step 5: Remove 5 screws(ψ5*19mm) of right side chain cover then take off it.




Step 6: Remove 5 screws(ψ5*19mm) of left side chain cover then take off it.




    Dyaco International Inc.                                                   44
Step 7: Use a Needle nose plier to remove DC socket nut, then unmount DC power wire from chain cover.




Step 8: To do the reverse of above steps to install both side chain cover back.




    Dyaco International Inc.                                                                            45
10-3 Swing Assembly Replacement
Step 1: Follow the steps of Chain Cover Replacement to take off both chain covers.
Step 2: Use a 12mm open-end wrench to remove inside bolt and washer of swing assembly axle.




Step 3: Unmount axle and separate the swing assembly and connecting arm.




    Dyaco International Inc.                                                                  46
Step 4: Use a 12mm open-end wrench to remove bolt and washer which locking swing assembly with mainframe, then take off swing assembly.




Step 5: To do the reverse of above steps to install swing assembly back.
Note: Make sure axle and U-plate alignment before tighten the bolt.




    Dyaco International Inc.                                                                                                              47
10-4 Linked Assembly Replacement
Step 1: Follow Chain Cover Replacement to take off both left and right Chain Cover.
Step 2: Remove outside hex head bolt and washer which locking the axle then removes the axle.




Step 3: Remove the bolt which locking the linked assembly with the crank, then take off the linked assembly.




Step 4: To do the reverse of above steps to install back.
Note : Make sure axle and U bracket alignment before tightening the bolts.




    Dyaco International Inc.                                                                                   48
10-5 Connecting Arm Replacement
Step 1: Follow the steps of Swing Assembly Replacement and Linked Assembly Replacement to remove the axles of Connecting Arm.
Step 2: Use a screwdriver to remove 2 screws which locking the Slide Wheel Cover then take off the cover and Connecting Arm.




Step 3: Use a circlip plier to remove the circlip Ø 17 then remove the slide wheel.




Step 4: Use a screwdriver to remove 4 screws(M5*10mm) then take off pedal.




Step 5: To do the reverse of above steps to install back.




    Dyaco International Inc.                                                                                                    49
10-6 Console Mast Replacement
Step 1: Follow the User Manual to take off the console mast.
Step 2: Remove the end caps of handle pulses.




Step 3: Put out the Handle pulse wires from under the tube.




Step 4: Use a screwdriver to remove 2 screws(ψ3x20mm) then remove the handle pulse with wire.




Step 5: To do the reverse of above steps to install back.
Note : Do not pinch the wires.



    Dyaco International Inc.                                                                    50
10-7 Rail Tube Replacement
Step 1: Follow the Connecting Arm Replacement to take off the connecting arm.
Step 2: Use a screwdriver to remove a screw(M5*10mm) of Slider Cover then take off it.




Step 3: Use 2 14mm open-end wrenches to remove the bolts and nuts which locking the Rail tube then take off it.




Step 4: To do the reverse of above steps to install back.




    Dyaco International Inc.                                                                                      51
10-8 Crank Arm Assembly Replacement
Step 1: Follow the Linked Assembly Replacement to take off Linked Assembly.
Step 2: Use a 12mm wrench to remove a hex head bolt and a flat washer which locking the crank.




Step 3: Use a M6 L-Allen wrench and a 13mm wrench to loose the bolt(M8*35L) then take off the Crank Arm Assembly.




Step 4: To do the reverse of above steps to install back.
Note: The direction of the woodruff key, the round head direct to the axle.




    Dyaco International Inc.                                                                                        52
10-9 Idle Wheel Assembly Replacement
Step 1: Follow the Linked Assembly Replacement to take off left Linked Assembly.
Step 2: Use a 13mm open-end wrench to loose the nut(M8*7T) which locking Idle Wheel Assembly on the Main Frame.




Step 3: Use a 13mm open-end wrench to remove the nut which locking on the J-bolt then unmount the drive belt from drive pulley.




Step 4: To do the reverse of above steps to install back. Use the nut of J-bolt to adjust drive belt tension then use Sonic belt tension meter to measuring belt tension.




    Dyaco International Inc.                                                                                                                                                53
Step 5: Operate the crank to make sure the belt is aligned with drive pulley, flywheel pulley, and idle wheel, and then install back all other parts.




    Dyaco International Inc.                                                                                                                            54
10-10 Flywheel and Drive Belt Replacement
Step 1: First, use the console to set the resistance level to MAX, and then turn off power. Follow the Idle Wheel Assembly Replacement to take off the idle wheel assembly.
Step 2: Unmount the steel cable from flywheel, then unmount drive belt from drive pulley.




Step 3: Use 15mm open-end wrench to loose 2 nuts which locking on flywheel, then take off flywheel and drive belt.




Step 4: To do the reverse of above steps to install back. Then use crank assembly to operating the drive pulley to make sure drive belt is aligned with flywheel pulley, idle wheel, and
drive pulley. If not, use a 17mm open-end wrench to adjust the nuts of flywheel to center the belt on the drive pulley.




Step 5: Adjust the drive belt tension with the idle wheel assembly, and then install back all other parts.



    Dyaco International Inc.                                                                                                                                                          55


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
enue des

oophp

ENUBW BDIAJAS ,
(ozoz)ooss) 9 &7_

/


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 100 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Table of Contents

1. CS800(2020) OUtlINeS ....cecccsesesesesssssesesscscscscscscscscscscacscacscscavacacavacavavavavacacavacavavavavacavavacavacavacavacavavacacavacacacacacavacavavavavavavavavavavavavavavavavavacavavacacacacens 3
2. CSBOO(2020) Electronic Parts ......cccccccccccccccccccceeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeseeeeeeseeeeeeeeeeeeeeeeSeeSSESEEES;;E;EEESEEEEEEEEEEEEEEEEE ES 6
2-1 Upper Controllers...........cccccccccccccccccesesessseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaeeeeseeeeeeeeeeessaaeeeeeeeeeeeeeeessaeeeseeeeeeeeeeeeGGGeeeeseeeeececse;;;;;GGs EEE ECEESEEE;;;O EASA EEEESEEEEEES 7
2-2 Lower Controller ANd Driver ........cccccsssesssscccccccccsseeessseeeeeceeeeeeeeeeeeeeeeeeeeeeeeesaeeeeeeeeeeeeeeeeessaeeeeeeeeeeeeeeeesseaeeeeseeeeeeeeeeesseeeeeeeeseeeeeeeessaaaeaaaseeeeeeeeeeas 8

3. Electrical CONFIQUrATIONS .............cccccccccccssseseseeeeeceeeeeeseeeeeeeeeeeeeeeeeeeseaeeeseeeeeeeeeeeGGGGGeesSEEEEEESESASSSGAAAAASEEEESSSSS;SS;GAASAASEEESSSSSSS;;;GASGASAESECEEEEE;;;;A A AAAS EEEEEEEEEEES 9
val Gist :1010] 00910) gel (im @)0]-1¢-] 4 (0) 4 ee 11
7. BY Sy 6) F- VAN 01010 (0) See eee 12
A-2 OPE ration ........cseccccssscccssccccseeeeeaeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeaaeeeeeeeeeeeeeeeeeGeeeeeeGeeGGAAEEASAAAEESAOES;EAAEEEGIOEES;AAEESS;AAESS;IOESS;;OSS;;OOESE;HOSSE;O AE SEEH OA SEEEEEEEEEES 13
4-2-1 POWER 2... cc ceccceccccesccneecceececeeeeseeeeeeeeseeeeeeeeeaeeeeeeeeeeeeeeeeeeeeeeaeeeseeeeGeeeeGeeeGaeeeGeeeeGaeGGGESGGAEESGE:GHES;GAESGEESGGIESS;ES;IESS;OESS;OESEEASE;EESEEAEESEESEEESEEE ESS 13

4-2-2 QUICK START .........cccccecccsscccsscceeecceseeceeeeseeeeseeeeeeeeeeeeeeeeeeeeeeaeeeseeeeeeeeeeeeeeeeeeGeeeeeeeeseeeeseeeeGeeseeeeGaeeseeeeeeeeeeeeeeae esses eeseeeseueesacesaeeeaeesaeeeaages 13

4-2-3 BASIC INFORMATION. ............cccccccsscccssccesecceeceseceeeeeeeeeeeeeeeeeeeseeeeseeeeeeeeeeeeeseeeeeeeseeeeGeeeeGeesaeeeseeeeeeeeeeeeeeeeseeeesaeeeseeeseueesaucesaeeeasesaeeeaaees 13
eo) 14

4-2-5 HEART RATE WINDOW, ..........c.cccccsecccssccssecceeeccecceeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeGeeeseeeeseeeeeeeeeeeeeeeeeeseeeeeeeeseeeeeeeesaucesaeesaeesaneeaagss 14

4-2-6 PROGRAMMABLE FEATURES .............ccccsecccsscccsecceeecceeeeseeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeseeeeseeeeGeeeeeeeeseeeeeeeeseeeeseeeseeeeseueeseeceeueesaucesaeesasesaneeagees 14

A-2-7 CSAFE FEATURE ...........cccceccseccsecceecneeeneceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeGeeseeeseeeGeeeaeeGeeeGeeseeeseeeGeeeaeeGeeeeeeeeeeeeeeeeesaeeeeeseeesaeeeeeeeeeseeeneeseeeeeesneeseeees 14

5. CS800(2020) Unit Block Diagrarns.......ccccccccccccccccceceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeGGGSEEEEEEEEEEEEEEEEEEEEEESEEEEEEEEEEEEEEEEEEEEEEEEEES 16
6. CSBO0(2020) Basic CONNECTIONS ANC WIFI .......eccccccccccccccccececeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesGGGGEEEEEEEESEEEEEEESEEEEEEEEEEAEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES 18
6-1 Display Board PCB COMPONENt LOCATIONS...........cccssesesssseccccceeceesaeeeseeeeeeeeeeeesaaeeeeeeeeeeeeeeeeesseaeesseeeeeeeeeeeesaaaeeeeseeeeeeeeeesssaueessssseeeeeeeessaauaagaseesees 19
6-1-1 DISPLAY BOARD WIRE CONNECTIONS ...........cccceccccssccesecceeeeceeceseeeeeeeseeeeseeeeeeeeeeeeseeeeeeeeeeeeeseeeeeeeeeeeeeseeeeeeeeseeeeeeeeseeeseueesaesesaeesaueesaeeees 19

6-1-2 PCB BOARD TOP ...........ccccsecccssccceeceeeeceeeeceeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeGeeeeeeeeGeeeeGeeeGeeeeGeeeeGeeeGGeeeGeeeeGeeeGGsGGAES;GESGEESEGOESS;OEEGEHSEGE SEE E ESSE EEEEE EEE: 20

6-1-3 PCB BOARD BOTTOM ............cccccssccssccceeeececeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeseeeeGeeeeeeeGeeeeeeeeeeeeeGeeeeseeeeeeeeseeeeaeeesee esses eesaeeseueesausesaeesaueesaeees 21

6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS .............ccccccccsscccsscceeseceeecceecceeeeceeeeseeeseeeeeeeeseeceseeeseeeseeeeseeessueesaeseseeesaeesaeeees 22

6-1-5 GENERATOR FLYWHEEL DEFINITION FUNCTION ............c.cccccsscccsecceseceseecnecceeeeeeeeeseeeeeeeeeeeeseeeeseeeeeeeesaeeeeeeeseeeeseeeeseeeseueesacesaeesaseseneees 23

7. CS800(2020) Error Messages / TrOUDICSHOOTING..........cccscccccccccceessssssssseeeeeccecceceeeesnssseeeeeeeeeecesesesasseeeeeeceseceeseeaaseeeeeeeeeeeeeeeeaasaeeeeeeeeeeeeeeeseasaeeess 24
y fas aol 0 0) ol © 00 | 5 eee 25
7-2 PrePare tOOIS.......cccecccccssssssseeeececeeeeeeseessseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeessaaeeesseeeeeeeeeeeGsGGGessGEEEEEESSGSSS;GAAASAEEEEESSESSS;SAAAAGAAEEEESESSESS;;;SO OS AsAsEEEEEEEESsEEA OEE OSEEEES 25
7-3 Error Message FE PRO ERROR ais ce eueenenemennenmnnnnnanenetennntnanennnnnnnntnnennnnmnannnnnnns sess: 26


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 72 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7-4 Error Me@SSage = Er wo... eeeeecceecccseccenecceeeeeeeeeeeeeaeeeeeeeeeeeeeeeeeeaeeeeaeeeaeeeeeeeeeaeeeaeeeeaeeeeaeeeaeeeaeeGGa EASA EAGHEA;GAES;IEESGEES;GEES;HESSGHES;GHESSHSEGHESSEEEESH EES EEE EA
7-4-1 TENSION MOTOR OPERATION
7-4-2 TENSION MOTOR TROUBLESHOOTING

7-4-3 TENSION MOTOR VOLTAGE TEST PROCEDURE.............ccssssssseeccccceccceeeesseeeeeeeeeeessseeeeeeeeeeeeeeeessseeeeseeeeeeeeeeeessseeeesssseeeeeeeessuaaaesseeseeeeeeeeas

7-5 Test configuration and the console to driver board connector pin define function
7-6 MAINTENANCE MENU IN CONSOLE SOFTWARE.,...........cccccccccccccsesssseeeecccceeessaeeeseseeeeeeeeeeesseeeseeeeeeeeeeeeeesseeeeesseeeeeeeeeesssaseeesssseeeeeeeessaauaagseeeess
7-7 Troubleshooting ProCceCure MaAtrix.........ccccccccccccccsseesseeeeececeeeeesseesesseeeeeeeeeeesseeeeeeeeeeeeeeeeeesesseseseeeeeeeeeeeesaeeeeeseseeeeeeeesessauaeesssseeeceeeeesaauaagaeeeess
Sam Of goL8 | emo f-¥ 240-100] ( Oy 1 010] 010720) ) eee csr
9. Troubleshooting(CS800(2020)) .......cccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeseeeseeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees
9-1 Troubleshooting for the CONSOLE ..........cccccccccccssseeesseeeeeeeeeeeeeeeeeeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeesGeeeeseeeeeeeeeeeessaaeeeseeeeeeeeeeeesseaeeeesseeeeeeeeessaaaaaaseeeeeeeeeeas
9-2 Troubleshooting for the FlyWheel............cccccccssssssssseeeeeccceeeeeeeseeeeeeeeeeeeeeesseeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeessaeeeeeseeeeeeeeeeeseeeeesessseeeeeseessauaaaaseeeeeeeeeeeas
9-3 Troubleshooting for Drive Belt .............cccccccccccsssssesseeeeececeeeeeaeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeseeeeeseeeeeeeeeeeessaeeeeseeeeeeeeeeeessaueeeessseeeeeeeessaaaaasseeeeeeeeeeeas
9-4 Troubleshooting for SWiNg ASSEMDIY..........ccccccssssesssseccccceeeeeeeseeseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeesaeeeeseeeeeeeeeeeessaeeeeseeeeeeeeeeeeseaeeessessseeeeeeessauaaasseeeeeeeeeeeas
9-5 Troubleshooting for CONNECTING ALM .......cccccccsssssssseseecccceeeeeaeeeeseeeeeeeeeeeesaaeeeeeeeeeeeeeeeesseeeeesSeeeeeeeeeesssaaeeesseeeeeeeeeeesaaaaeaessseeeeeseessaaaaasseeeeeeeeeeeas
10. Parts Replace Ment Guide ...........ccccccccccccccccccceeesseeeeeeeeeeeeeseeeeeseeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeesssGGeesSeEsEECEE;;;;;;AAAASOEESEESEEEESE;;GA SAA AAASEEEEEEEEEEEE EBB ES
10-1 Console REPlaceMeNt ...........ccccccccccccccccccaessseeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeseeeeeeeeeeeesseeseeeGeseeesGEG;;;;GAAAAEEEEEEESES;;;;AAAASSSEESEESESESS;;;A AAA SAO SE EEEEEEEEEEE BEBE
10-2 Chain Cover Replace Ment ............ccccccccccsesssseseeeecceeeeessaaeseseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaeeeeeeeeeeeeeeeeessaeeeeseeeeeeeeGsGs;sAAGASAEEESESEESES;;;EA AAA AAAAEEEEEEEEEEEE EEE ES
10-3 Swing Assembly ReplaceMent...........cccccccssssssssseecccceeceeaeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeessGeeeeseeeeeeeeeeeessseeeeeeeeeeeeeeeeesaaaeeesssseeeeeeeeseaaaaees
10-4 Linked Assembly Replacement ...........ccccccssssssseeeccccceeceaeeeesseeeeeeeeeeeseeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeesssseeeeesseeeeeeeeeesauaeaesssseeeeeeeeseaaagees
10-5 Connecting Arm ReplaceMe nt.........cccccccssssssssseeecceceeeseaeesseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeeessaeeeeseeeeeeeeeeeeseseeeeesseeeeeeeeessaaaeeesssseeeeeeeeeeauagees
10-6 Console Mast ReplaceMe nt...........cccccccccsssssssseeeecceeeeeeaaeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeessseeeeeeeeeeeeeeeeeesaaaeaessseeeeeeeeeseaaagees
10-7 Rail TUbe ReEplaceMe nt ............cccccccccccccccesessseeeeeccceeeeeaeeeesseeeeeeeeeeeeeeeeeeseeeeeeeeeeeessaeeeeeeeeeeeeeeeeGssGGGsssEEEEEEEESS;;;;AAOAAASEESEESEEEE;;;;A OSA SAASSEEEEEEEEEEE BEBE
10-8 Crank Arm Assembly ReplaceMent ...........::cccccccccccccccsaessssseeseeeeeeeeeeeeseeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeessseeeeeseeeeeeeeeeesseseeeeeeeeeeeeeeeeesauaeeesssseeeeeeeeeeaaagees
10-9 Idle Wheel Assembly Replacement ............:.ccccccccccccccceesssseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeesseeeeeseeeeeeeeeeeeseaeeeeeseeeeeeeeeesseaaaeassssseeeeeeeseauagees
10-10 Flywheel and Drive Belt ReplaceMent.............ccccccccssssssssseeeeceeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeeeseeeeeeeeseeeeeeeeessauaaeeseseeeeeeeeeeeaaagees


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
€ "DU JOUOILOUIdJU] OODA

SOUIIINO (0ZOZ )008S)D ‘L


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
i200} 04044) 09040
"DU JOUO|LOUJEJU] OODAG

(Y) 8 (q) JaaoQdeD dubpuey

JOAND APIS HO]

(Y) [epad

JOAOD JEPI|S 1Y6IY
8SEY Apis JeOY

(Y) JeAOD UleUD

(7) leped

(7) 4aA09 UleYyD

(Y) JOA0D ISeY BJOSUOD

(Y) JOA0D Jeg s]pueH

(Y) J9A0D JSeW BJOSUOD

9|OSUOD


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9 "DU JOUOILOUIdJU] OODA

SAL g 31U01}99]9 (OZOZ )008S) Z


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
L “OU JOUOILOUE}U] OODAG

ue 4 SuI|OO) z£& — feD EB Sd, 889 De
| aes

S19|]O1JUOD JaddA T-Z


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6 "DU JOUOILOUIdJU] OODA

suoizeanbhijuo) jediaz3a/9 “€


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
UL "DU JOUO|LOUJEJU] OODAG

uo!ze19dO JINpOld (0ZOZ)008S) ‘VP


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4-1 Display Windows

DISTANCE

CALORIES PULSE TIME ELAPSED

688 65 ==

SPEED

TRACK
e e

@ PROFILE 4

J U.

WATTS METs TIME REMAINING

a
e ie,

e
ec eee 0
eee $ ENTER

a a ||

SPIRIT —_\>..

Level LEVEL
M START STOP =
[jy 3)

12


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
OT "DU JOUOILOUIdJU] OODA

sweibeig 4201g 31UN (OZOZ)O08S) ‘Ss


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LT "DU JOUOILOUIdJU] OODA

d
YOLOW “ ee eo eo . sano
NOISNH.L

HLOOLAN Ta
HOUVHO
qasn
davod AV IdSId
NVA
YONHS
ONFIOOOD
an AWM dvd IGNVH
SSH THaIM MH


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SUR

o UO

= =

WN

5 Oo

<

oz

wo

ne)

oo .6|Uwy)

= a

in ©)

(on @)

Sf ®F

> QQ

m oO

4 3

2 8

" 3S

ro)

5

or

T—

Oo

re)

Q)

a >,

S S
rc

Zz Tp)
ss
Z
&
w
Q
py
>
¥2]
(op)


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Oc

—

: ———

t1-2002S) Ione

VAN, WANT, TANT WANT WANT FANT AST WANT TANT VAST ANT VAST AMT VANE TANT TANT TAN Tet

dOl GYVOd ddd ¢-T-9


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 28 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
TC "DU JOUOILOUIdJU] OODA

wee ew —
ovvewe Pmcooncc Y t a
Looossc0eotD
Oat s-soorts> { q

a) ©

mee rs ae Wesecvees ussevveee. deve so 00 UBUVUY Ges MeVUYYIVE uesovg—e Mesdeeede Soveueved

WOLLOd GYVOd ddd E-T-9


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1-4 THE CONSOLE INTERFACE BOARD WIRE CONNECTIONS

J21
W-CS24005-1-10

SYSTEM
‘|

HANDGRIP
PULSE WIRE

J20 |

Dyaco International Inc. 22


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
cc

GND 'S

YA 1
G+ 'E
TI ¢

“INT

ddOuY 1441S
TOYULNOO NIV

NOILONNA NOILINISAG TASHMA14 YOLVYEANAD S-T-9


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ao)
—N
S
So
>
i]
So
a 3
a 0UC«*SS
©
2 5
> =
> Y
Oo y
= ©
— ee


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
NO e
U m
D =
Oo Oo
oO my
=x (@)
o) O
ct ok
Oo a)
eo) n
n

5 =
a
<13
m
an oO
e)
oO


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
LC

"DU JOUO|LOUJEJU] OODAG

YOLOW NOISNSAL

TWNOIS TWNOIS

-/+ TANF YA TSA

SAAM -/+ TAAST GuvV0Od AV IdSId


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7-5 Test configuration and the console to driver board connector pin define function

The console to driver board
TM ee) ee ee ep connector pin define function:
bh Whe. PE eo ary es ry Sa 1. MTR-
2. MTR+
3. 5V

; a a ; . 5. GND
2 | oe ae . a 6. RPM

== 7. GND

(@)

8. N/A

9. GND
10. 12V
11. N/A

aanaaa

[oN Cf \ 12. N/A

a ttl ‘ Fy Ly \ } fut
| ai jou mh : | 13. N/A
TS —TS oes wee O14. N/A

PAAAAR

12345678910111213 14
Dyaco International Inc. 30


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
cE "DU JOUOILOUIdJU] OODA

((0ZOZ )O08SD )WiesBelp yNdAID “gs


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Oyaco

Appliance inlet

© | [asns || ° —S

CONNECTOR
CONSOLE
Black White
_
HP- HP-
~
< RIGHT LEFT
OO —
~
Ld 4s) A
5 a a
a Oo oO
a Zz) &Z
oO o a
Zz fap) +r
r4 —— es
o Black White
Oo
—
AC Adapter
SPin 2Pin 3Pin

3Pin
DC power cord

SPin i] cl DC output wire

Motor wire ePin
RPM Sensor wire

SPEED SENSOR

Gear Motor

Dyaco International Inc. 34


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
GE "DU JOUOILOUIdJU] OODA

((0ZOZ )008SD )/Hulzooysa|qnoAL 6


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Tv "DU JOUOILOUIdJU] OODA

SpIND JUBWAIL|/day S}Ved OL
