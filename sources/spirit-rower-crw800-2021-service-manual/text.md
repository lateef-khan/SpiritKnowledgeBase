<!-- Source: CRW800 Service Manual 800940.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

CRW800
Service Manual




             Service Manual
1.CRW800 Outlines .................................................................................................................................................................................................. 3
2. CRW800 Electronic Parts...................................................................................................................................................................................... 6
3.Electrical Configurations ....................................................................................................................................................................................... 8
4. CRW800 Product Operation ............................................................................................................................................................................... 10
    4-1 Function Description .................................................................................................................................................................................. 12
    4-2 Key button Function ................................................................................................................................................................................... 14
    4-3 Operating Instruction ................................................................................................................................................................................. 16
5. CRW800 Unit Block Diagrams ............................................................................................................................................................................ 22
6. CRW800 Basic Connections and Wiring ............................................................................................................................................................. 24
    6-1 Display Board PCB Component Locations ................................................................................................................................................... 24
       6-1-1 PCB BOARD TOP ................................................................................................................................................................................ 25
       6-1-2 PCB BOARD BOTTOM ........................................................................................................................................................................ 25
       6-1-3 TENSION MOTOR (GEAR MOTOR) CONNECTOR DEFINITION FUNCTION............................................................................................ 26
       6-1-4 GENERATOR CONTROLLER CONNECTOR DEFINITION FUNCTION ....................................................................................................... 28
7. CRW800 Error Messages / Troubleshooting ....................................................................................................................................................... 29
    7-1 Error Codes ................................................................................................................................................................................................ 30
    7-2 Prepare tools.............................................................................................................................................................................................. 31
    7-3 Error Message ............................................................................................................................................................................................ 32
    7-4 Maintenance menu in the console software .............................................................................................................................................. 35
    7-5 Troubleshooting Quick Lookup Table.......................................................................................................................................................... 36
    7-6 Console (Electronic Desk) problem ............................................................................................................................................................ 37
    7-7 Wireless heartbeat problem ...................................................................................................................................................................... 37
       7-7-1 No display of heart rate ..................................................................................................................................................................... 37
       7-7-2 Press the keypad heart rate unexpected increase / Heart rate always increasing / Wireless receiving distance is short.................... 37
       7-7-3 Light sensor problem ......................................................................................................................................................................... 38
       7-7-4 RF handheld board problem .............................................................................................................................................................. 38
9.Circuit diagram(CRW800).................................................................................................................................................................................... 39
10.Exploded View (CRW800) ................................................................................................................................................................................. 41
11.Part Replacement Guide ................................................................................................................................................................................... 43
    11-1 Chain Cover &Galvanized iron net replacement. ...................................................................................................................................... 44
                                                                                                                                                                                                                     1
    11-2 Console & Console Holder Assembly replacement. .................................................................................................................................. 46
    11-3 Handle bar & Controller Assembly replacement. ..................................................................................................................................... 48
    11-4 Flywheel Pulley、Latch &Spring Latch replacement. ............................................................................................................................... 49
    11-5 Fan & Flywheel replacement. ................................................................................................................................................................... 52
    11-6 Gear Motor & Steel Cable replacement. .................................................................................................................................................. 53
    11-7 Pedal、Pedal Plate & Wire Tie Mount replacement. ............................................................................................................................... 54
    11-8 Aluminum Track、Seat &Rear Stabilizer replacement. ............................................................................................................................ 55
    11-9 Folding End Assembly & Seat Up/Down Adjustment Knob replacement.................................................................................................. 57
    11-10 Batteries replacement............................................................................................................................................................................ 59
    11-11 Generator motor replacement. .............................................................................................................................................................. 60
    11-12 Controller board replacement. ............................................................................................................................................................... 61
12. CRW800 Troubleshooting ................................................................................................................................................................................ 62
    12-1 The Console Display troubleshooting ....................................................................................................................................................... 63
    12-2 The Resistance Level can’t adjust troubleshooting................................................................................................................................... 64
    12-3 Troubleshooting for not smooth when operating .................................................................................................................................... 65
    12-4 Troubleshooting for Other problems ....................................................................................................................................................... 66




                                                                                                                                                                                                            2
1.CRW800 Outlines




                    3
4
5
2. CRW800 Electronic Parts




                             6
7
3.Electrical Configurations




                              8
Part Name             Part Description

Console               Interface that controls all functions of the Rower.

Tension motor         It can change to increase or decrease resistance level of brake.


General Information

Part Name             Part Description

Console               Contain Keys control and LCD Display.
                      Main controller Include power supply and motor driver control circuit.

Tension motor         Work voltage: DC 4.0~6.0V
                      Control resistance increases and decreases.




                                                                                               9
4. CRW800 Product Operation




                              10
11
4-1 Function Description

stroke/min

s/m value shows the equivalent strokes per minute.

Time

1. It shows the time.
2. Range of time: 00：00~99：59(minute: second).
3. The time is accumulated for each workout mode.
4. When time is set to count down, it shows the time remaining.

Distance

1. The distance range is 0~9999 and switches to the format of 1X.XX when the value is over 9999.
2. The distance will be accumulated for each workout mode.
3. When the distance is set to count down, it shows the remaining distance.

Heart Rate

1. The heart rate range is 40~220 bpm.
2. When the heart rate signal is detected, the small dot at lower right corner of the heart rate window will be blinking together with heart rate
value showing.
3. When there is no heart rate signal detected, the heart rate window shows nothing.

Calories

1. The calorie window shows the value of calorie dissipated.
2. The calorie range is 0~999.

                                                                                                                                                    12
Watts

1. The Watt range is 0~2000.
2. When the numbers over 999 to four digits, the display would use point to show digit in thousands. E.g. 1000 shows 1.00, 1009 shows 1.01, 1240 shows 1.20,
1250 shows 1.25, 2000 shows 2.00, etc.

LEVEL

1. The level window shows the current resistance level.
2. The level range is 1~16.

500M/TIME

1. Only workout modes of Manual, Distance, Time and Calorie are with this display function.
2. For Manual workout mode as an example: When the console starts, Matrix in the middle of LCD will show the wave pattern then switch to “500M/TIME 00:00
   “ across center display after 5 seconds then switch again back to the wave pattern after another 5 seconds and continue to repeat the cycle. This is the
   function of “SCAN”.
3. The console goes directly into “SCAN” mode after start. If “MODE” button is pressed, it shows the wave pattern. Pressing the “MODE” button again, it displays
   500M/TIME and repeat again by pressing “MODE” button it goes back with “SCAN” function (recyclable).




                                                                                                                                                                   13
4-2 Key button Function

All Keys

1. Any valid key button pressed will generate a beep sound.
2. When in power off mode, pressing any key button turns on the console.

MODE Key

1. Under idle mode, pressing “MODE” key each time switches the workout mode with the following sequence:
   MANUAL →DISTANCE →TIME →CALORIES →20/10 INTERVAL →10/20 INTERVAL→CUSTOM INTERVAL→ Fat Burn → Cardio → Strength → Game
2. The default workout mode after turning on the unit is Manual mode.
3. To choose the target workout mode, when the matrix window shows the desired workout pattern and parameter window value to be set will be blinking each
   second.

Up Key

1. Under the setting mode of the target workout, the parameter is will be counted up.
2. The value increases one increment when “UP” key is pressed once.

Down Key

1. Under the setting mode of the target workout, the parameter is will be counted down.
2. The value decreases one increment when “DOWN” key is pressed once.

Start/Stop Key

1. Under idle mode, pressing Start/Stop key button enters Manual workout mode.
2. To confirm the value the window is showing when setting the parameter under each target workout mode and to start the workout mode.
3. Press to end the current workout mode and all message windows stop counting.

                                                                                                                                                            14
Reset Key

1. Pressing this key button under stopping mode, the image switches to the idle mode.
2. The reset key button is valid only in stopping mode.
3. Under any mode, pressing this key button for 3 seconds turns on the console again.




                                                                                        15
 4-3 Operating Instruction
1. The screen is with full display and the buzzer beeps for two seconds after turning on. Pressing “Start” button goes directly to “Manual” workout mode or pressing
   “MODE” button to switch and select a workout mode with the workout sequence shown as below:
   MANUAL →DISTANCE →TIME →CALORIES →20/10 INTERVAL →10/20 INTERVAL→CUSTOM INTERVAL→ Fat Burn → Cardio → Strength → Game
   The program name will scroll from left to right to tell the user what it is.




2. To choose MANUAL mode (Fig. 2-1)
   1. Pressing Start/Stop button and begins the workout mode or pulling the paddle under the idle mode and enters directly to Manual workout mode.
   2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 2-2) and 500M/TIME (Fig. 2-3) or pressing “MODE”
   button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
   3. Pressing “UP” or “DOWN” button and adjusts the resistance level which is shown at bottom right corner of “LEVEL” window.




                                                                                                                                                                       16
3. To choose target distance count-down Distance workout mode (Fig. 3-1)
   1. Use UP/DOWN buttons to adjust and set the workout distance. The default distance is 100M with increment of 50M up or down. Press Start/Stop button to
   confirm the setting and start the workout mode.
   2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 3-2) and 500M/TIME (Fig. 3-3) or pressing “MODE”
   button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
   3. Distance window counts down from target distance setting value and shows the remaining distance of the workout.
   4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   5. When the distance is counted down to 0, the workout completes and the buzzer sounds with a long beep. If paddling continues, the distance count-down repeats.




4. To choose target time count-down Time workout mode (Fig. 4-1)
   1. Use UP/DOWN buttons to adjust and set the workout time. The default distance is 1:00 with 1-minute increment of up or down (99:00 maximum). Press
   Start/Stop button to confirm the setting and start the workout mode.
   2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 4-2) and 500M/TIME (Fig. 4-3) or pressing “MODE”
   button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
   3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   4. Time window counts down from the setting time value and shows the remaining time of the workout.
   5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




                                                                                                                                                                   17
5. To choose target calorie count-down Calories workout mode (Fig. 5-1)
   1. Use UP/DOWN buttons to adjust and set the target calorie. The default value is 100 with increment of 10 up or down. Press Start/Stop button to confirm the
   setting and start the workout mode.
   2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 5-2) and 500M/TIME (Fig. 5-3) or pressing “MODE”
   button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
   3. Calorie window counts down from the setting target calorie value and shows the remaining calorie of the workout.
   4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   5. When calorie is counted down to 0, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




6. To choose 20/10 INTERVAL workout mode (Fig. 6-1)
   1. The image at the center of LCD: 20 seconds (Exercise)/10 seconds (Rest)
   2.Pressing Start/Stop button starts the workout mode.
   3. The image at the center of LCD shows time count-down of current workout and wave (Fig. 6-2) or rest time count-down and mark (Fig. 6-3).
   4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   5. There are 10 Exercise/Rest cycles for each workout time.
   6. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




                                                                                                                                                                   18
7. To choose 10/20 INTERVAL workout mode (Fig. 7-1)
   1. The image at the center of LCD: 10 seconds (Exercise)/20 seconds (Rest)
   2. Pressing Start/Stop button starts the workout mode.
   3. The image at the center of LCD shows time count-down of current workout and wave (Fig. 7-2) or rest time count-down and mark (Fig. 7-3).
   4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   5. There are 10 Exercise/Rest cycles for each workout time.
   6. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




8. To choose CUSTOM NTERVAL workout mode (Fig. 8-1)
   1. User-define time (Exercise)/time (Rest): the default is 10 seconds (Exercise)/10 seconds (Rest)
   2. The value at left side of the matrix window flashes for setting the exercise time. Use UP/DOWN buttons to adjust and set the workout time. The default time is
   10 seconds with 1-second increment of up or down. Press Start/Stop button to confirm the setting and start the workout mode.
   3. The value at right side of the matrix window flashes for setting the rest time. Use UP/DOWN buttons to adjust and set the workout time. The default time is 10
   seconds with 1-second increment of up or down. Press Start/Stop button to confirm the setting and start the workout mode.
   4. The image at the center of LCD: 10 seconds (Exercise)/10 seconds (Rest)
   5. Pressing Start/Stop button starts the workout mode.
   6. The image at the center of LCD shows time count-down of current workout and wave (Fig. 8-2) or rest time count-down and mark (Fig. 8-3).
   7. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   8. There are 10 Exercise/Rest cycles for each workout time.
   9. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




                                                                                                                                                                       19
9. To choose Fat Burn workout mode (Fig. 9-1)
   1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
   5-minute (99:00maximum). Press Start/Stop button to start the workout mode.
   2. The image at the center of LCD shows the fat burn profile (Fig. 9-2)
   3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
   4. Time window starts count-down from the setting time and shows the remaining workout time.
   5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




10. To choose cardio workout mode (Fig. 10-1)
    1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
     5-minute (99:00maximum). Press Start/Stop button to start the workout mode.
     2. The image at the center of LCD shows the cardio profile (Fig. 10-2)
     3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
     4. Time window starts count-down from the setting time and shows the remaining workout time.
     5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




                                                                                                                                                               20
11. To choose Strength workout mode (Fig. 11-1)
    1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
     5-minute (99:00maximum). Press Start/Stop button to start the workout mode.
     2. The image at the center of LCD shows the strength profile (Fig. 11-2)
     3. Time window starts count-down from the setting time and shows the remaining workout time.
     4. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.




12. To choose GAME workout mode (Fig. 11-1)
    1. Pressing Start/Stop button and begins the GAME workout mode (11-2).
     2. Three dots at left side represents the user position and the image shift one profile left per second and continue to scroll.
     3. The position of the user will not shift. However, the faster the user stroke, the higher the user’s position. When there is no stroke, the position of the user goes
     down to the lowest. The height of the user’s position is equivalent to the speed the user strokes.
     4. The time for the game workout starts counting down from 5 minutes and ends when time is up.




                                                                                                                                                                           21
5. CRW800 Unit Block Diagrams




                                22
23
6-1 Display Board PCB Component Locations




6. CRW800 Basic Connections and Wiring




                                            24
6-1-1 PCB BOARD TOP




6-1-2 PCB BOARD       BOTTOM




                               25
6-1-3 TENSION MOTOR (GEAR MOTOR) CONNECTOR DEFINITION FUNCTION




                                                                 26
27
6-1-4 GENERATOR CONTROLLER CONNECTOR DEFINITION FUNCTION




                                                           GENERATOR INPUT
                                                           1 : AC
                                                           2 : N/A
                                                           3 : AC
                    OUTPUT DC

                    123
                    1: POSITIVE
                    2: N/A
                    3: NEGATIVE




                                                                             28
7. CRW800 Error Messages /
     Troubleshooting




                             29
7-1 Error Codes

                  Error Message Code   Problem Description

                            E1         Console (Electronic Desk) EEPROM failure



                            E2         Cable tension communication error




                                                                                  30
7-2 Prepare tools




                    Multi-meter




                                  31
7-3 Error Message

    Error code: E1
    Description of the Situation

    When the screen displays "E1" "RAM ERROR" message, it means that the system console EEPROM failure, all functions are disabled.


    Troubleshooting

    Replace the console (Electronic Desk)




                                                                                                                                      32
Error code: E2
Description of the Situation

When the "E2" "MOTOR ERROR" message is displayed, the communication with the cable tensioner is abnormal and all functions are stopped.


Cable tensioner operation


     Device              Description
     Console             When you press the UP or DOWN key while in program mode, the LEVEL value displayed on the console
                         display increases or decreases. At the same time send a command signal to the cable tensioner action.
     Cable tensioner     Receives the command signal from the console and actuation



Troubleshooting


     Device              Troubleshooting
     Console             1. Check the connection of motherboard’s 8-pin cable.
                         2. When UP or DOWN is pressed, a beep sound is generated, if yes that it is determined that the signal has
                            been sent.
     8-pin Cable         1. Check the cable connections.
                         2. Check if the cable is broken or curled.
                         3. Replace the cable and retest.
     Cable tensioner     Check the 8-pin cable connection.




                                                                                                                                          33
Cable tensioner fault / Voltage measurement procedure

1. Place the multifunction meter at 12VDC. Place the probe in the motor control line on the drive board (the red probe is blue wire and the
black probe is green wire).
3. Turn on the power of device to tension motor. The console display lights.
4. Press the LEVEL UP measurement to the normal reading: +4.0 ~ 6.0VDC, motor action, resistance increases.
5. Press LEVEL DOWN. Normal reading: -4.0 ~ -6.0VDC. Motor work. Resistance decreases.
6. If there is no voltage, please check the generator controller socket terminals whether the voltage, if not please change another one
controller.
7. If the generator controller can work fine, replace the cable tensioner.




                                                                              Place the probe on the motor control cable on the drive board
                                                                              (the red probe is blue wire and the black probe is green wire).




                                                                                                                                                34
7-4 Maintenance menu in the console software

 1.   In the IDLE MODE, press UP and DOWN key for 3 seconds into the engineering mode one.
 2.   Pressing the RESET key at any time returns to IDLE MODE.
 3.   Enter the engineering mode one, do the LCD byte display test, each byte lit sequentially, after testing, directly into the main menu screen.
 4.   Console window displayed "FUN", press MODE to enter option :
                                        Menu             Item
                                        FUNCTION >       KEY TEST
                                                         ODOMETER RESET
                                                         UNITS >               ENGLISH / METRIC
                                                         MOTOR TEST >          Correction related
                                                         MANUAL


 5.   If you select "KEY TEST", press the MODE key to confirm the entry, and the console window will display "PRESS ALL KEYS" in a flowing way. "KEY NUMBER" will
      be displayed in the DISTANCE window when the KEY is pressed. After all the keys have been pressed, the console window will display "OK". After 2 seconds, it
      will automatically return to the "KEY TEST"
 6.   If "ODOMETER RESET" is selected, press the MODE key to confirm the entry and display "ODO RESET" on the console window. Press UP → DOWN → MODE to
      clear the total mileage and total time. When clear, the display will show "RET". After 2 second the program will return to "ODOMETER RESET" submenu.
 7.   If you select "UNITS" as the unit switch, "UNITS" will be displayed in the console window. Press the MODE key to enter the unit switching screen. In the
      console window, the default unit is "MI". Press UP / DOWN key to switch, when switching metric, the console window displays "KM". Press the MODE key to
      select OK, automatically return to the "UNITS" sub-menu screen.
 8.   If you select "MOTOR TEST" as the motor auto test, "MOTOR TEST" will be displayed in the console window. When you press MODE, "TEST" will be displayed
      in the console window, "L 01" (L01 ~ L16) will be displayed in the DISTANCE window. Press UP / DOWN / MODE to do TEST, do increment to the highest, and
      then descending to the minimum, every 2 seconds change once, back to do MOTOR drag cable test, press the RESET button to do the end, return to the
      "MOTOR TEST Sub-menu screen.
 9.   If "MANUAL" is selected as the motor manual test, "TEST" will be displayed in the console window. When TEST is entered by pressing MODE, the DISTANCE
      window will display "XX" (XX is the motor COUNTER value), and DW will show "L1 ~ L16 Press the UP key to increase the number of segments up to 16, press
      the DOWN key to decrease the number of segments to 1, press the RESET key to complete the input, and then return to the MANUAL submenu screen.
                                                                                                                                                                 35
 7-5 Troubleshooting Quick Lookup Table
Happening                                      Caused                                                      Processing Step
LCD display does not shine, incomplete or      1. LCD backlight damage.                                     1. Check the battery.
imperfect                                      2. Console power is too low.                                 2. Replace the new LCD module or the control electronics.
                                                                                                            3. Check the power of the console.
                                                                                                            4. Check the generator.
The heartbeat display value is incorrect       1. May be received another heart rate strap signal.          1. Check that there is no other heart rate strap around the machine being
                                               2. There may be other electric field noise interference.     used.
                                               3. The wireless heartbeat receiver is damaged.               2. Try changing the machine direction or position.
                                                                                                            3. Replace the new wireless heartbeat receiver.
Wireless heartbeat has no effect               1. The Heart rate strap is not properly worn.                1. Check that the Heart rate strap is in proper contact with the skin and in
(The heartbeat value is not displayed on the   2. The distance is too far above the receiver.               the right direction.
monitor)                                       3. The battery of heart rate strap is low or has no voltage. 2. Keep the chest strap within 3 feet of the console.
                                                                                                            3. Please replace the new lithium battery type CR2032.
Wireless heartbeat reception is too short      The battery is low.                                          Please replace the new lithium battery type CR2032.
(must be very close to the console)
RF handheld board problem                      1. Level UP/DOWN canned not changed.                        1. Check the battery.
                                                                                                           2. Check that the receiving board is in the correct position
                                                                                                           3. Near the source of interference (such as fluorescent lamp rectifier,
                                                                                                           cable interference power, etc.)
                                                                                                           4. Check the cable，or replace the RF radio reception module
Light sensor problem                           1. No count.                                                1. Check that the receiving board is in the correct position
                                                                                                           2. Check the light point and the receiving point for dust obstruction
                                                                                                           3. Check the cable
                                                                                                           4. Replace the light sensor




                                                                                                                                                                                           36
 7-6 Console (Electronic Desk) problem
The normal operation of the console screen will be normal display, if not light up check the generator power is the normal power supply or change another one to
check is work or check the generator controller is correctly, the controller have output voltage, and then check all the wire is indeed Plug in the console, the console
cover removed to check whether all the wires inserted in the correct location, and check whether the wire fracture.




 7-7 Wireless heartbeat problem

        7-7-1 No display of heart rate

        A、Make sure that the heart rate strap is worn in place.
        B、Make sure that the battery power of the heart rate strap is sufficient.
        C、Whether the range of the wireless heartbeat has been exceeded.
        D、Check whether the wireless heartbeat module is in the correct position.
        E、Replace the wireless heartbeat receiver module.

        7-7-2 Press the keypad heart rate unexpected increase / Heart rate always increasing / Wireless receiving distance is
        short
        A、Check that the receiving board is in the correct position.
        B、To confirm whether the keypad sound is too loud caused.
        C、Disturbed wireless heartbeat near the source of interference. (Such as fluorescent lamp rectifier, cable interference power, etc…)
        D、Replace the wireless heartbeat receiver module.




                                                                                                                                                                           37
7-7-3 Light sensor problem

A、 Check that the receiving board is in the correct position.
B、 Check whether the light-emitting point and the receiving point are obstructed by dust.
C、Check the cable connection.
D、Replace the light sensor module.

7-7-4 RF handheld board problem

A、 Check the battery power.
B、 Check that the receiving board is in the correct position
C、Whether disturbed by the source of near interference. (such as fluorescent lamp rectifier, cable interference power, etc.)
D、Check the cable connection.
E、Replace the RF receiver module




                                                                                                                               38
9.Circuit diagram(CRW800)




                            39
40
10.Exploded View (CRW800)




                            41
42
11.Part Replacement Guide




                            43
11-1 Chain Cover &Galvanized iron net replacement.
Step 1: Remove the Ø 5 × 16L_Tapping Screw(111) x2pcs from the Chain Cover (L) (71) by using Phillips Head Screw Driver, take apart the 3.5 × 12L_Sheet Metal Screw(112)x9pcs from the Chain Cover (R)
(72), and then it works to take apart the Chain Cover (L) (71) completely.




Step 2: Loose the 3/8" × UNC16 × 3-3/4"_Socket Head Cap Bolt (83) by using the L Allen Wrench(8m/m) and pushing the 3/8" × 11T_Nyloc Nut.
Noted: Please do not take out the Screw.




Step 3: Take out the Ø 5 × 16L_Tapping Screw (111) x2pcs by using the Philips screwdriver, then Chain Cover (R) could be removed.




                                                                                                                                                                                                  44
Step 4: Take out the Galvanized iron net (L) and Galvanized iron net (R) from the Chain Cover (L) and Chain Cover (R) and make it straight from the hole.
Noted: It can be taken out the single chain cover and Galvanized iron.




Step 5: To do the reverse of above steps to install Chain Cover (L) (71) and Chain Cover (R) (72). Be careful about the Chain Cover Foam must aim at the hole.




                                                                                                                                                                 45
11-2 Console & Console Holder Assembly replacement.
Step 1: Take out the 3.5 × 12L_Sheet Metal Screw (112)x4pcs from the Console(43) by using the driver to the Top cover of Console(43), and then remove the 500m/m Computer Cable (Upper) (44) and
wireless cables or receivers.




Step 2: Remove the 3/8" × UNC16 × 3-3/4"_Socket Head Cap Bolt (83) by using the L Allen Wrench (8m/m) if the user wants to take out the Console Assembly (43). Separate the 500m/m Computer
Cable (Upper)(44) and controller.




Step 3: Take out the Chain Cover (L) and Chain Cover (R) first. Then separate the 500m/m Computer Cable (Upper)(44) and 500m/m Computer Cable (Lower) (45) if the user wants to remove the
Console Holder Assembly. Apart from the Board(34), and then take out the 3/8" × UNC16 × 3-3/4"_Socket Head Cap Bolt (83), then the user can get the Console Holder Assembly(7) and Console
Assembly(43) at meanwhile.




                                                                                                                                                                                               46
Step 4: To do the reverse of above steps to resume the console assemble (43). Be noticed the processing of pass through the 3/8" × UNC16 × 3-3/4"_Socket Head Cap Bolt (83) and 500m/m Computer
Cable (Upper), which may interfere with each other, need techniques.




                                                                                                                                                                                                  47
11-3 Handle bar & Controller Assembly replacement.
Step 1: Take out the 3.5 × 12L_Sheet Metal Screw (112) x2pcs and Sheet Metal Screw (132) x2pcs from the Controller Assembly (36) by using the driver (see figure 1), and pass the Handle through the
Ribbon Roll (30). Be careful it needs to pass Handle (10) through the Ribbon Roll (30) and fix it on the Hook (9). It is to avoid the Ribbon Roll (30) goes back to the chain cover.




Step 2: If the user wants to change the PVC Sleeve (50), it needs to remove the Controller Assembly (36) directly.
Step 3: Remove the 3.5 × 12L_Sheet Metal Screw (112) x1PC from the Battery Cover (36~3) if the user only wants to remove the battery.




                                                                                                                                                                                                       48
11-4 Flywheel Pulley、Latch &Spring Latch replacement.
Step 1: Adjust the resistance to the highest on the Console and remove the Power Cord. Take out the Chain Cover (L)(71). Chain Cover (R)(72) 、Handle(10)、Controller Assembly (36) and Console Holder
Assembly (7) with Console Assembly (43).
Step 2: Loose the M6 × 6T_Nyloc Nut (103) and3/8" × UNF26 × 11T_Nut (82) by using 10/15m/m Wrench.




Step 3: Take out the M8 × P1.25 × 20L_Socket Head Cap Bolt (84)x4pcs by 6m/m L Allen Wrench. Move forward the Flywheel Pulley (25)、Latch (26)、Spring          Latch (27)、Attaching Plate (8L) and
Attaching Plate (8R).




Step 4: Fix the Flywheel Pulley (25) by hands and take out the M6 × P1.0 × 18L_Button Head Socket Bolt (89) by using 4m/m L Allen Wrench. Take out M5 × 10L_Phillips Head Screw (86)x3pcs by using
driver and remove the Attaching Plate (8R) with Bearing(6201 UOU).




                                                                                                                                                                                                     49
Step 5: Take out the M5 × 10L_Phillips Head Screw (86) x 2pcs by using driver. Separate the Attaching Plate (8R) with Bearing (6201 UOU).
Step 6: Remove the Ø 20 x1.2t _C Ring(108) by clip and also Ø 20 × 29 × 0.3T_Wave Washer(96), Spring     Latch(27) and Latch(26).




Step 7: Be careful of the steps when reassemble the parts back.
a)   The position of Spring   Latch(27) and Attaching Plate (8R).




b) Fix the Attaching Plate (8L) and Attaching Plate (8R) after put the Drive Belt (6PJ-787L)(24) on the Flywheel Pulley(25).




c)   Tie up the 3/8" × UNF26 × 11T Nut (82) and adjust the M6 × 6T_Nyloc Nut(103). Adjust the Drive Belt to the Tension value of 70~80BLS and Flywheel(23). Tie up 3/8" × UNF26 × 11T Nut(82).




                                                                                                                                                                                                 50
Step 8: To mount generator belt to generator pulley.




Step 9: To insert the Idle Wheel Screw to the generator Fixing Plate then locking the generator with a bolt (M6 *1.0*18L) and a flat washer.




Step 10: To adjust the nut of idle wheel screw to the right tension which the generator belt won’t skidding.




Step 11: Test with pull the handle bar to make sure there won’t be any noise.




                                                                                                                                               51
11-5 Fan & Flywheel replacement.
Step 1: Adjust the assistance of console to the highest and remove the power cord. Take out the Chain Cover (L)(71)& Chain Cover (R)(72).
Step 2: Pull out the Steel Cable (66) from the Flywheel(23).




Step 3: Use 10/15m/m Wrench to loose M6 × 6T_Nyloc Nut(103) &3/8" × UNF26 × 11T_Nut(82).




Step 4: Use 6m/m L Allen Wrench to take out the M8 × P1.25 × 20L_Socket Head Cap Bolt(84)x4pcs. Move forward the Flywheel Pulley(25), Latch(26), Spring   Latch(27) and Attaching Plate (8L) (8R)
which the Drive Belt(24) can be removed.




Step 5: Release the Flywheel(23) & Fan(22).
Step 6: Use driver to remove M5 × P0.8 × 15L_Phillips Head Screw(78)x6pcs and Flywheel(23) & Fan(22) can be separated.
Step 7: To do the reverse of above steps to resume the Flywheel Pulley、Latch &Spring Latch.

                                                                                                                                                                                                    52
11-6 Gear Motor & Steel Cable replacement.
Step 1: Adjust the assistance of console to the highest and remove the power cord. Take out the Chain Cover (L)(71)& Chain Cover (R)(72).
Step 2: Pull out the Steel Cable (66) from the Flywheel (23).
Step 3: Use driver to take out Ø 5 × 16L_Tapping Screw (111) x 2pcs. Take out the Front Gear Motor Cover(74)& Rear Gear Motor Cover(75).




Step 4: Use 8m/m Wrench to remove M5 × 5T_Nyloc Nut of Steel Cable(66).




Step 5: Remove the cables from Gear Motor(35). Use driver to take out M5 × P0.8 × 15L_Phillips Head Screw(78)x2pcs




Step 6: To do the reverse of above steps to resume parts.




                                                                                                                                            53
11-7 Pedal、Pedal Plate & Wire Tie Mount replacement.
Step 1: Use 5m/m Wrench to take out the M8 × P1.25 × 12L_Button Head Socket Bolt(123)x6pcs, Ø 5/16" × Ø 18 × 1.5T_Flat Washer(122)x6pcs. Release the Pedal (L) & (R), Pedal(68), Pedal Plate(69) and
Wire Tie Mount(67).




Step 2: Use the driver to take out the M4 × 5L_ Phillips Head Screw (113)x4pcs, Pedal(68), Pedal Plate(69) and Wire Tie Mount(67)




Step 3: Use the driver to take out the M5 × 12L_Flat Head Socket Screw (107)x4pcs and Wire Tie Mount(67).




Step 4: To do the reverse of above steps to resume parts




                                                                                                                                                                                                  54
11-8 Aluminum Track、Seat &Rear Stabilizer replacement.
Step 1: Use the driver to take out M5 × 10L_Phillips Head Screw(85)x3pcs and Connecting Cover(63).




Step 2: Use 5m/m Wrench to take out the M8 × P1.25 × 12L_Button Head Socket Bolt(123)x6pcs, Ø 5/16" × Ø 18 × 1.5T_Flat Washer(122)x6pcs. Release the Aluminum Track(51), Seat sets(49)(16)(53)(54)
and Rear Stabilizer(3).




Step 3: Take out the Seat sets(49)(16)(53)(54) in the front.
Step 4: Use 4m/m Wrench to release M6 × P1.0 × 18L_Button Head Socket Bolt(89)x2pcs, M6 × P1.0 × 10L_Button Head Socket Bolt(129)x4pcs. Remove the Seat Stop Cover(65) & Rear Stabilizer(3).




                                                                                                                                                                                               55
Step 5: Use 6m/m Wrench &14m/m Wrench to take 3/8" × UNC16 × 1-1/4"_Button Head Socket Bolt(105), 3/8" × 11T_Nyloc Nut(106) and Pulley(54) apart.




Step 6: Use the driver to take M6 × 15L_Phillips Head Screw(124), Seat(49) and Seat Attaching Board(16) apart.




Step 7: To do the reverse of above steps to resume parts.




                                                                                                                                                    56
11-9 Folding End Assembly & Seat Up/Down Adjustment Knob replacement.
Step 1: Remove Aluminum Track(51)& Pedal (L)(R).
Step 2: Use 6m/m Wrench to take M8 × P1.25 × 15L_Socket Head Cap Bolt(98)x2pcs and Folding End Assembly(6) apart.




※ Please note it is not allowed to take out 2pcs of M8 × P1.25 × 15L_Socket Head Cap Bolt(98), please get a new piece of M8 × P1.25 × 15L_Socket Head Cap Bolt(98) to lock the original position.
Follow the same steps to get another one.
Step 3: Use 10m/m Wrench to take M6 × 6T_Nyloc Nut(103) apart.




Step 4: Use 22m/m Wrench to take 22L × M16 × M22 × 37L_Knob Nut(46)& Seat Up/Down Adjustment Knob(47).




※Please note 22L × M16 × M22 × 37L_Knob Nut(46) is fixed by thread-locker, remember add 1~2cc thread-locker when reverse above steps to resume part.



                                                                                                                                                                                               57
Step 5: Use 13m/m Wrench to remove the M8 × P1.25 × 13T_Cap Nut(100)x2pcs, M8 × P1.25 × 20L_Hex Head Bolt(99)x2pcs and take Tension Spring(48) and Main Frame(1) apart.




Step 6: Use 8m/m Wrench to remove the 3/8" × UNC16 × 1"_Socket Head Cap Bolt) (101)x2pcs, Ø 3/8" × 20 × 3.0T_Flat Washer(102)x2pcs and take Seat Stop Axle(15) and Tension Spring(48) apart.




Step 7: To do the reverse of above steps to resume parts




                                                                                                                                                                                               58
11-10 Batteries replacement.
Step 1: Use a screwdriver to remove a screw of battery cover on the back of console then replace batteries.




                                                                                                              59
11-11 Generator motor replacement.
Step 1: Please follow the steps of Chain cover replacement to take off Chain cover.
Step 2: To loose the nut (M8*7T) which locking with the idle wheel bolt, then remove the button socket cap screw and take off the generator.




Step 3: To do the reverse of above steps to install the generator back.




                                                                                                                                               60
11-12 Controller board replacement.
Step 1: Lie down the machine.




Step 2: Use a screwdriver to remove 4 screws(M5*10L).




Step 3: Unplug the control wire then replace the controller board.




Step 4: To do the reverse of above steps to install back.



                                                                     61
12. CRW800 Troubleshooting




                             62
12-1 The Console Display troubleshooting
Q: Count Times doesn’t show in display.
A: Please check the connections with optical coupler Board (34) or the connection of all wires.




Q: The console doesn’t display.
A: Please check the connection with 750m/m DC Power Cord(39), Gear Motor(35), and 500m/m Computer Cable (Upper)(44).




                                                                                                                       63
12-2 The Resistance Level can’t adjust troubleshooting
Please check Controller Assembly(36) and Console Assembly(43) if there’s no adjustable resistance separately. If it is the problem of Controller Assembly(36), please refer to step 1. If it is the problem of
Console Assembly(43), please refer to step 3.
1.Please follow the steps of instruction manual or the message on the sticker to proceed the calibration of RF module. If there’s still no resistance, please use driver to remove the 3.5 × 12L_Sheet Metal
Screw(112)x1pc from the Battery Cover(36~3) and check if has power of Controller Assembly(36). If not, please replace directly. If yes, please remove the 3.5 × 12L_Sheet Metal Screw(112)x2pcs from
the Controller Assembly(36) and check the connection of Resistance Button W/Cable+Faceplate (36~4) and RF Module(35). Or take out the 3.5 × 12L_Sheet Metal Screw(112)x4pcs from the console.
Open the cover of console and check the connections of cables on the Console Bottom Cover(43~2). It is get easier to find the problem if you have RF Module(35).




2. Release the 3.5 × 12L_Sheet Metal Screw(112)x4pcs from the Console(43). (See figure 2) Check the PCB board(43~4) and 500m/m_Computer Cable (Upper). Release the Chain Cover (R)(72) and check
the Gear Motor(35) and 500m/m_Computer Cable (Lower)(45).
3. Release the the Chain Cover (R)(72) and check the Drive Belt(24), Flywheel(23) if it is without problem. Check the connections with Gear Motor(35), Steel Cable(66), and Flywheel(23) and check if is
without problem of adjustable resistance.
The problems could be:
a) Gear Motor(35)- Please check there’s any the noise while working. If yes, please get the Steel Cable(66) to the maximum. If not, please replace Gear Motor(35) directly.
b) Flywheel(23)- Please check if the Steel Cable is broken or Flywheel gets stuck. Check the trouble shooting step by step.




                                                                                                                                                                                                           64
12-3 Troubleshooting for not smooth when operating
Q: Ribbon Roll can’t Spring Back.
A: Release the Chain Cover (R)(72) and check the Latch(26). If the ribbon roll can spring back, the problem could be broken on the other side. Please pull it out and check.




If the Latch(26) cannot spring back, please release the Attaching Plate (8R) to check the connections of Spring   Latch(27~2) and Latch(26). (See figure 2 as in red circle) If the Spring Latch(27~2) is
broken, please replace it directly.




Q: Ribbon Roll works not smoothly or gets stuck.
A: The Ribbon Roll may get in reverse position. Please pull it out and check, please also check Chain Cover (R) (72)




                                                                                                                                                                                                            65
12-4 Troubleshooting for Other problems
Q: Slide works not smoothly.
A: Please follow below steps until the slide works.
1. Please clean Aluminum Board(52)& Aluminum Track Pulley(53).
2. Please loose 3pcs of 3/8" × 11T_Nyloc Nut(106).
3. Check and replace Aluminum Track Pulley(53) or Pulley(54).




Q: Noise.
A: Please refer to the cause of noise to find out the problems. The main reasons and parts are below.
1. Screw Kits not fixed. Please check.
2. Please check four of Adjustment Foot Pad(59) are fixed to the ground and also adjust the each of Nuts.
3. Tie the Seat Up/Down Adjustment Knob(47). If it has the noise, please get some lubrication on the position of screw.




4. Slide has noise. Please clean Aluminum Track Pulley(53), Pulley(54) and Aluminum Board(52). If it is not workable, please replace Aluminum Track Pulley(53) and Pulley(54) directly.
5. Fan(22) or Flywheel(23) has noise. Please release the Chain Cover (L)(71)&Chain Cover (R)(72) and check.

                                                                                                                                                                                          66


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 145 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
L.CRW800 OUTLINGS...........ccccccccccccccsseseeeeeeeeceeeeeeeeeeeeeeeeeeeeeeeeaaeeeeseeeeeeeeeeeesaeeeeeseeeeeeeeeeGGGGGeessEEEEEESESG;SSAAAOAASEEEESESS;S;;S;AAOSSAEESECECES;;;;;A AAA AASEEEEEESEEGEEE OSA EOEE SESS 3
2. CRW800 Electronic Parts..........ccccccccccccccsssessseeeeeceeeeeseeeseeseeeeeeeeeeeeseeeeeseeeeeeeeeeeesaeeeeeseeeeeeeeeeGGsGGGeesSEEESEEES;;;;;GAAOASEEESSSSES;;;;;GAO GASSES ECEEEEEE;;E AAAS AEE EEEEEEEEES 6
3.Electrical CONFIQUATIONS ............cccccccccccccsssseseeeeeeeeeeeeseeeseeeeeeeeeeeeessaeeeeseeeeeeeeeeeesGGGsesEEEEEEEESASSSAAAAAASEEEESSSS;;S;;AAAAAEEEESSSESSG;;;;AO GASSES ECEEEEEs;;E AEA AAOEEEEEEEEEEES 8
TA G1 AYAVE:101 0m oa cole [6(e1 ml ©) 0\~1 ¢-) 0 (0) 9 cee 10
A-1 FUNCTION DESCIIPTION ...........ceccccsescccnseeeeneeeeeeaeeeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeeeGeeeeeeGeeGGAAEEASAAEEEGIOEE;;IAEEESIOEES;;IEEE;;AAES;;IOEEE;;OESS;;AOE;E;HOAESE;OOESEEAAOEEEE EEE EEEE 12
4-2 Key DUttOn FUNCTION ........ccccceccccssessseeeeccceceeeeaeeeeeeeeeeeeeeeeeaaeeeeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeeeGGGGeesEEEEEEEESSESGAAAAAAEEEEESSES;;;;AAAOASAESESECESSEG;;;EA AAAS EEEEEEEEEEEE EBB EE 14
A-3 Operating INSTFUCTION ..........ccccccseeccceseeceneeeeeeaeeeeeneeeeeeeeeeeaeeeeeeeeeeeeeeeeeeaeeeeeeGeeeGGGAEEASAAEEEGIOEESESAEESSIAEES;AIESES;AAESS;IOEES;;OEES;;OOESE;HOESE;O OE SEEAAA SESH OEE EEEES 16

5. CRW800 Unit BIOCK Diagrams ..........cccccccessssseeeeccceeeeseeaeesseeeeeeeeeeeseeseeeseeeeeeeeeeesseeeeeeeeeeeeeeeeeGeGaeeeseeeeeeeeeeessGseeesseeeeeeeeeeeesaaeeeesseeeeeeeeeessaueaaseeeeeeeeeeas 22
6. CRW800 Basic CONNECTIONS ANC WILING ..........cccccccccssseseseseececeeeeeeaeeeseseeeeeeeeeeeseseeeeeeeeeeeeeeeesssaeeeseeeeeeeeeeesssseeeseeeeeeeeeeeessaaeeeesssseeeeeeessuaueasseseeeeeeeeeas 24
6-1 Display Board PCB COMPONENt LOCATIONS...........ccccsssessseeeccccceceeaaeeeeeeeeeeeeeeeseeeeeseeeeeeeeeeeeesseeeseseeeeeeeeeeeessaeeeeeeeeeeeeeeeeessauaesssssseeeeeeessuauaaaaseeeees 24

coo keel 13 8 310) -\ 4 Dt | O) 25

co ova 4 O13 8310) -V. 1D 10) tO) \\/ ne 25

6-1-3 TENSION MOTOR (GEAR MOTOR) CONNECTOR DEFINITION FUNCTION .............:::ssssssssssssssssssssssssssssseeeessseeesceeseeseseeeeeeeesseeseeeaseeeaees 26

6-1-4 GENERATOR CONTROLLER CONNECTOR DEFINITION FUNCTION .............cccccccccccceeesssseecccceceesseeeeesseeseeceeeeessseeessseeeeeeeeeessuaaaesseeseeeeeeees 28

7. CRW800 Error Messages / TrOUDICSHOOtING.............cceeeessscceeccceeecesesssnseeeeeccceceeeseessasseeeeeeeeeseeeeesaaseeeeeeeceeeeeeeesassseeeeeeeeeeeeeeesaaaeaeeeeeeeeeceeeeseaasaeeess 29
y fas aol 0 0) al OX 00 | 5 ee eee 30
7-2 PrePare tOOIS.......cccecccccssssssseeeececeeeeeeseessseeeeeeeeeeeeseeeeeeeeeeeeeeeeeeessaaeeesseeeeeeeeeeeGsGGGessGEEEEEESSGSSS;GAAASAEEEEESSESSS;SAAAAGAAEEEESESSESS;;;SO OS AsAsEEEEEEEESsEEA OEE OSEEEES 31
7-3 ErrOr M@SSAC 2.0... ceeccceecccescceeeecneeeeaeeeeeeeeeeeeueeeaeeeeaeeeeeeeeaeeeeaeeeGaeeeaeeeeaeeeGaeeGGeAGHEEGGEEE;HEA;GHEA;GEES;IEE;GHES;GEES;IES;GEESS;EES;HES;GEESSGH ESSE SESH SSHE ESSE REE HESS EA 32
7-4 Maintenance Menu in the CONSOLE SOFTWALE ...........ceeeeececcccececceeeeeesseeeeeeeeeeeseeeeeeeseeeeeeeeeeesseaeeeseeeeeeeeeeeesaeaeeesseeeeeeeeeesssaeeeessssseeeeeeessaaaaaaasseees 35
7-5 Troubleshooting QUICK LOOKUP Table..........ccccccccccssssssssseecccceeeeeseaeeeeseeeeeeeeeeeseaeeeseeeeeeeeeeeeeseeseeeseeeeeeeeeeeesaaeeeesseeeeeeeeeesssaeeeessssseeeeeeessaaaaagseeeess 36
7-6 Console (Electronic Desk) Problem ........cccccccccccccccceceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees 37
7-7 Wireless heartbeat Problem ...........ccccsssssssecccccceeeeeeeeeseeeeeeeeeeeesseeeesseeeeeeeeeeessaeeeeeeeeeeeeeeeeesseaeeeseeeeeeeeeeeeseeeeeeeseeeeeeeeeesssaeaeessusseeeeeeessaauaasaeeeees 37
7-7-1 NO display Of Heart rate .........ccececccccccccccccsssseseseeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeGsGeeeeeeeeeeeeeeeGsGGGsssEEEEESE;EE;S;;GAOGAAAAEECECEEEE;;;A AAAS EEEEEEEEEES 37

7-7-2 Press the keypad heart rate unexpected increase / Heart rate always increasing / Wireless receiving distance is Short...........::::006 37

Vay fares 24 01 X10 S10) a ©) 0) ©) (=) 00 eee eee 38

7-7-4 RF handheld board problem..........ccccccccccsssssssseeeeccceeeeeeeeeesseeeeeeeeeeeeeeeeeeeseeeeeeeeeeesseeeeeeeeeeeeeeeeessseeeeeeeeeeeeeeeeessaeaeeeeeeseeeeeeessaaaaesseeseeeeeeeeas 38
Q.Circuit diagram (CRW800)...........cccccccccccecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees 39
sO =>'¢e)(olel-YomVal-\ iV (61,0)\\4:10]0) ee 41
11.Part Replacement Guide ............cccseescseeccccccccceeeeseseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaaeeeeeeeeeeeeeeeesaaeeeesSSEeeESEGA;;A;AAAAASEEEESSESE;;;;;AAAASEESEESSESESE;;;O OS AAAAEEEEEEEEEEEE EEE ES 43
11-1 Chain Cover &Galvanized iron Net replace MENt............ccccccccccccccccceeessseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesseeeseseeeeeeeeeeesseaeeeessseeeeeeeesesauaeeesssseeeeeeeeeeaaaaees 44


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 43 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
12.

11-2 Console & Console Holder Assembly replace Ment. ............cccccccccccscsessssseeeeeceeeeeseeseesseeeeeeeeeeeeseeeeeeeeeeeeeeeeesseeeeesesseeeeeeeeeesaaaeeesseeseeeeeeeeeaaagees 46
11-3 Handle bar & Controller Assembly replace Ment. ..........:cccccccccccccccceseessseeeeeeeeeeeeeeeeeeseeeeeeeeeeeeseeseeseeeeeeeeeeesseeeeeeeeseeeeeeeeeesauaeeessseeeeeeeeeseauagees 48
11-4 Flywheel Pulley + Latch &Spring Latch replace Ment. ............cccccccccsssssssseeeeeceeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeessseeeeeeeeeeeeeeeeesauaasesseeseeeeeeeseaaagees 49
11-5 Fan & Flywheel replace Ment..........cccccccccsssssssseeeccceeeesseeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeeessGeeeeseeeeeeeeeeeeseeeeeeeseeeeeeeeeeeseaaeaesssseeeeeeeeeeaaaaees 52
11-6 Gear Motor & Steel Cable replacement. ..........cccccccccccssssssseeeeeeeeeeeeeeeseeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeeeesaeeeeseeeeeeeeeeeesseeeeeeseeeeeeeeeeeseuaeeesssseeeeeeeeeeaaagees 53
11-7 Pedal + Pedal Plate & Wire Tie MOUNt replaCceMEeNt. ...........cccccccccsssssseeeeeeeeceeeeeeaeseeeeeeeeeeeeeeeseeeeeseeeeeeeeeeesseseeeessseeeeeeeeesseaaesessseeeeeeeeeseaaaaees 54
11-8 Aluminum Track + Seat &Rear Stabilizer replaceMent. ..........cccccccccsssssssseecccceeeeeeeseeeseeeeeeeeeeesseeeeeeeeeeeeeeeeesseaeeeeeeeeeeeeeeeesseaaaeesseeeeeeeeeeseaaagges 55
11-9 Folding End Assembly & Seat Up/Down Adjustment Knob replace Ment............ccccccccsccsssssssceeeecccceeeeesssssseeeeeeceeeeceessesaseeeeeceeeeeeeessstaaaeees 57
11-10 Batteries replacEMent............cccccccccccccccesessseseeeeeeeeeesaaeeeeseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaaaeeeeeeeeeeeeeeeeGGGsGesSEEEEEEEES;;;;AAA ASSESS ESECEEES;;; EASA AAAS EEEEEEEEEEE BEBE 59
11-11 Generator MOtOr FEPIACEMENE.........ccccccssssseeeeecccceceseaeeeeeeeeeeeeeeeeeseeeeeeeeeeeeeeeeeGGaGesesEEEEESESES;;;AGAAAAAEEEEESESES;;;;SAGAOAEEEEESCEES;;;EAE AA SASSEEEEEEEEEEEEE BEES 60
11-12 Controller board replaceMent..........ccccccssssssseecccccceeeeeseseseeeeeeeeeeeeseeeeeeeeeeeeeeeeeesaeeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeesssseeeseeseeeeeeeeessaaaeeasssseeeeeeeeeeaaagees 61
CRW 800 Troubleshooting ..........ccccccssssssseseecccceceeeseeessseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaeeeeeseeeeeeeeeeeessGaeeeseeeeeeeeeeeessGeeeeseeeeeeessGG;GGAG GSAS EEEEEECEG;;;E AAAS OEE EEEEEEEEES 62
12-1 The Console Display troubleshooting .............ccccccccccccssssssseeeeecceeeeseeesseeeeeeeeeeeeeseeeeeeeeeeeeeeeeeessaeeeeseeeeeeeeeeeeseaeeeseeseeeeeeeeeeseuaeeeseseeeeeeeeeeeaaaaees 63
12-2 The Resistance Level can’t AdjUSt trOUDIESHOOTING..............cccccccccceseesseeseeeeeeeeeeeeeaseeeeeeeeeeeeeeesseeeeeseeeeeeeeeeesseseeeeeeseeeeeeeeessaaaeeesssseeeeeeeeeeaaagges 64
12-3 Troubleshooting for Not SMOOTH WhEN OPE ating ............ccccccccccccccceesssseeeeeeceeeeeeeeseeseeeeeeeeeeeesseeeeeeeeeeeeeeeeesseaeeeeeseeeeeeeeeeesaaaeeessseseeeeeeeseaaagees 65
12-4 Troubleshooting for Other Problems ............cccccccccccccsseesssseeeececeeeeeeaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesseeeeeseeeeeeeeeeeessseeeeeeeeeeeeeeeesaaaeeessseeeeeeeeeseauagees 66


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 30 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
oped
}004 jusuysnipy

19ZI! iee
4@A0D pug a

Jel, WnuIluniy

"1EPed
ye9S
dOZIIGe}S JUOI4
‘naueey 4J3A02D Bunseuu0D
Ja/j01}U0D
* Jou os
uoll paziuRBAjes
eYyszey
o(y) 42005 UleYD
J) 42A0D UleUD
-Alquiessy
ajosuoD


=== OCR SUPPLEMENT, PDF PAGE 6 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
“Teped

pieog Bulyoeyy jees
“yYOOH

eyoje Buds 9
yoje7 ‘Adijndg jeeymAjy
cued 9 [PeyMAlS

-Ajquiessy
JapjOH ajosuog


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
large ICD - _
Matrix Window Se 930 s6¢ see es Ten innovative programs
Shistssitssessissttssesee offer a variety of workouts
Builtin Heart
6 B

Rate Receiver

Easy Touch
Control Butons


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
IT

SUOING JO1UO>

yonoy-Aspj a
. JOAIBDSY @|DY
A Goh ho SE: Ss YDS} UlINg
SOOM io AN@\iDA od JOYO ° eesecce 333335"
swoiBoid aAyOAouU! Ud} eo *ss sss sss sss ese. MOPUIAA XLIDV/

Qt 2610)

Li€l CBh GE

Lids


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. To choose target distance count-down Distance workout mode (Fig. 3-1)
1. Use UP/DOWN buttons to adjust and set the workout distance. The default distance is 100M with increment of 50M up or down. Press Start/Stop button to
confirm the setting and start the workout mode.
2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 3-2) and 5OOM/TIME (Fig. 3-3) or pressing “MODE”
button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
3. Distance window counts down from target distance setting value and shows the remaining distance of the workout.
4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
5. When the distance is counted down to 0, the workout completes and the buzzer sounds with a long beep. If paddling continues, the distance count-down repeats.
0&8 Pe

. soe
* +8

- ««
sreere

=

ore seer Ld

'
u '

Fig. 3-1 Fig. 3-2 Fig. 3-3
4. To choose target time count-down Time workout mode (Fig. 4-1)
1. Use UP/DOWN buttons to adjust and set the workout time. The default distance is 1:00 with 1-minute increment of up or down (99:00 maximum). Press
Start/Stop button to confirm the setting and start the workout mode.
2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 4-2) and 500M/TIME (Fig. 4-3) or pressing “MODE”
button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
4. Time window counts down from the setting time value and shows the remaining time of the workout.
5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

8 +00

17


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5. To choose target calorie count-down Calories workout mode (Fig. 5-1)
1. Use UP/DOWN buttons to adjust and set the target calorie. The default value is 100 with increment of 10 up or down. Press Start/Stop button to confirm the
setting and start the workout mode.
2. The image at the center of LCD will scan every 5 seconds to show the stroke speed with wave pattern (Fig. 5-2) and SOOM/TIME (Fig. 5-3) or pressing “MODE”
button to cancel scanning with wave pattern only. Pressing “MODE” again switches the image to show 500M/TIME.
3. Calorie window counts down from the setting target calorie value and shows the remaining calorie of the workout.
4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
5. When calorie is counted down to 0, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.
Bobi 28 Of

uu?

99
Fig. 5-1 Fig. 5-2
6. To choose 20/10 INTERVAL workout mode (Fig. 6-1)
1. The image at the center of LCD: 20 seconds (Exercise)/10 seconds (Rest)
2.Pressing Start/Stop button starts the workout mode.
3. The image at the center of LCD shows time count-down of current workout and wave (Fig. 6-2) or rest time count-down and mark (Fig. 6-3).
4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
5. There are 10 Exercise/Rest cycles for each workout time.

6. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

im nen aon
iG uid iG 0G

i
serre

18


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7. To choose 10/20 INTERVAL workout mode (Fig. 7-1)
1. The image at the center of LCD: 10 seconds (Exercise)/20 seconds (Rest)
2. Pressing Start/Stop button starts the workout mode.
3. The image at the center of LCD shows time count-down of current workout and wave (Fig. 7-2) or rest time count-down and mark (Fig. 7-3).
4. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
5. There are 10 Exercise/Rest cycles for each workout time.
6. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

iG CGaY ig chIy 66

j
Fig. 7-1 Fig. 7-2 Fig. 7-3

8. To choose CUSTOM NTERVAL workout mode (Fig. 8-1)
1. User-define time (Exercise)/time (Rest): the default is 10 seconds (Exercise)/10 seconds (Rest)
2. The value at left side of the matrix window flashes for setting the exercise time. Use UP/DOWN buttons to adjust and set the workout time. The default time is
10 seconds with 1-second increment of up or down. Press Start/Stop button to confirm the setting and start the workout mode.
3. The value at right side of the matrix window flashes for setting the rest time. Use UP/DOWN buttons to adjust and set the workout time. The default time is 10
seconds with 1-second increment of up or down. Press Start/Stop button to confirm the setting and start the workout mode.
4. The image at the center of LCD: 10 seconds (Exercise)/10 seconds (Rest)
5. Pressing Start/Stop button starts the workout mode.
6. The image at the center of LCD shows time count-down of current workout and wave (Fig. 8-2) or rest time count-down and mark (Fig. 8-3).
7. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
8. There are 10 Exercise/Rest cycles for each workout time.
9. When workout completes, the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.
{G OG84 (9 0Ri4 66

ore

19


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 11 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9. To choose Fat Burn workout mode (Fig. 9-1)

1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
5-minute (99:00maximum). Press Start/Stop button to start the workout mode.

2. The image at the center of LCD shows the fat burn profile (Fig. 9-2)

3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.

4. Time window starts count-down from the setting time and shows the remaining workout time.

5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

1G G68 ic

Fig. 9-1 Fig. 9-2

10. To choose cardio workout mode (Fig. 10-1)
1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
5-minute (99:00maximum). Press Start/Stop button to start the workout mode.
2. The image at the center of LCD shows the cardio profile (Fig. 10-2)
3. Under the workout mode, pressing UP or DOWN key button adjusts the resistance level.
4. Time window starts count-down from the setting time and shows the remaining workout time.
5. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

ao 4
os a pad ++ oa+s > se re rs ae a

Fig. 10-1 Fig. 10-2

20


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
11. To choose Strength workout mode (Fig. 11-1)

1. Pressing Start/Stop button and begins the workout mode or setting the workout time. Use UP/DOWN buttons to adjust the time. The increment of adjustment is
5-minute (99:00maximum). Press Start/Stop button to start the workout mode.

2. The image at the center of LCD shows the strength profile (Fig. 11-2)

3. Time window starts count-down from the setting time and shows the remaining workout time.

4. When time is counted down to 0:00, the workout completes and the buzzer sounds with a long beep. If paddling continues, the time count-down repeats.

-- —
beeen been ‘eos ‘ome

Fig. 11-1 Fig 11-2

12. To choose GAME workout mode (Fig. 11-1)
1. Pressing Start/Stop button and begins the GAME workout mode (11-2).
2. Three dots at left side represents the user position and the image shift one profile left per second and continue to scroll.
3. The position of the user will not shift. However, the faster the user stroke, the higher the user’s position. When there is no stroke, the position of the user goes
down to the lowest. The height of the user’s position is equivalent to the speed the user strokes.
4. The time for the game workout starts counting down from 5 minutes and ends when time is up.
iG O4S5 ic

- *e
—-— fF F 7

21


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
eC

YSTIOULNOD
YOsNas YOLOW yOIWHANAD YOIWYHANAD
Wd NOISNAL

OHV08 AV Ids! (4vSS10NVH)
TOYHLNOd TSAS7
da

YSAla0S5q YH
SS 15d


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SUO!}2907 JUBUOdWO gdd pueog Aejdsiq T-9


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 21 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
SC

WO1LLOd GuYWOd ddd C-T-9

as ee) ed te!

ibe
sé ates ef
hit afl | BBE j

‘e ‘ nh babes i
t ;

7

/ = 2 feo
© e c Ge = ©

dOl GUYVOd Add T-T-9


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9¢

NOILONN4 NOILINISAG YOLIINNOD (YOLOW YVvd9) YOLOW NOISNAL €-T-9


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6-1-4 GENERATOR CONTROLLER CONNECTOR DEFINITION FUNCTION

GENERATOR INPUT
1:AC

2:N/A

= 3:AC

i

er Ris _

3: NEGATIVE "s0076-Vi.0-20z00218 3)

28


=== OCR SUPPLEMENT, PDF PAGE 31 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Oe

JOJIJ9 UOIJEOIUNWILUOD UOISUd} BIGeD 7d
ain|le} WOUdaa (4S9q 91U04}998/4) ajosuoD La
uoldiissag wa|qoid apOD agessajp] 410119

Sapo) JO [-Z


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Te

JayaW-lN|A

S]O0} Jedald 7-2


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 26 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
#CW800B-YRO03 ROWER SCHEMATIC

YROO3 o
CONSOLE

w
a
oO
a
Wi
=
z
=
(o}
oO
=
a
HANDLEBAR |
GEAR ——
MOTOR

uw y

z 3

Fa w

= w

o
x
2
=| _fipi] ae
GENERTOR |_|
GENERATOR) 3 PIN CABLE _| RY IK.

JK 1
T TOR)
ouTeuT SPEED SENSOR

40


=== OCR SUPPLEMENT, PDF PAGE 43 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ov GOLLWNVVLVO6OL

8zI Zeb 99h

pa

og

M\/ fp
of YK
mala
VHS

J ¢-| g
ze Za Be og
4 SS
Se v be 68
i I<cr 16 98
v=tV
A wae

008M


=== OCR SUPPLEMENT, PDF PAGE 44 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
apind JuUaWIaIe/d|ay Lied’ LI


=== OCR SUPPLEMENT, PDF PAGE 66 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
dyaco

12-3 Troubleshooting for not smooth when operating

Q: Ribbon Roll can’t Spring Back.

A: Release the Chain Cover (R)(72) and check the Latch(26). If the ribbon roll can spring back, the problem could be broken on the other side. Please pull it out and check.

L

~

«
z= ao
4
’ a ta Se ty
“ aS
’ a
b |
e.

If the Latch(26) cannot spring back, please release the Attaching Plate (8R) to check the connections of Spring Latch(27~2) and Latch(26). (See figure 2 as in red circle) If the Spring Latch(27~2) is

broken, please replace it directly.

Q: Ribbon Roll works not smoothly or gets stuck.

A: The Ribbon Roll may get in reverse position. Please pull it out and check, please also check Chain Cover (R) (72)

65
