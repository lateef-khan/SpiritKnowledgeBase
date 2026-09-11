<!-- Source: CE800 (XE890B-AE10M-02) - Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

    XE890B-AE10M
    Service Manual




1               Service Manual
--------------------------------------------Table of Contents-------------------------------------------
      1. Elliptical Outlines
      2. Electronic Parts
      2.1 Upper Controllers
      2.2 Lower Controller and Driver
      3. Electrical Configurations
      4. Elliptical Operation
      5. Basic Connections and Wiring
      6. Error Messages / Troubleshooting
      7. Troubleshooting
      7-1 Side case & Round Disk Problem
      7-2 Flywheel Problem
      7.3 Poly-V Belt Problem
      7.4 Swing Arm Problem
      7.5 Connecting Arm and Slide Wheel Problem
      8. Q & A
      8.1 Noise
      8.2 Slip Problem
      8.3 Play
      8.4 Smooth Problem
      9. Disassembling and Assembling of Parts
      9.1 Console Replacement
      9.2 Swing Arm Replacement
      9.3 Connecting Arm Replacement
      9.4 Console Mast Replacement
      95 Side Case Replacement
      9.6 Cross Bar Replacement
      9.7 Idler Wheel Replacement
      9.8 Flywheel & Poly-V Belt replacement
      9.9 Rear Frame Replacement
      9.10 Aluminum Track Replacement


                                                    2                                         Service Manual
1. XE890B-AE10M Outlines




           3               Service Manual
     Handle Bar Axle Inner         Console Assembly
     Cover

                                   Rear Handle Bar
    Front Handle Bar Cover         Cover

                                   Console Mast Cover(R)
        Console Mast Cover

                                   Round Disk Cover

       Pedal Arm Cover (R)         Front Stabilizer Cover


                                   Connecting Arm Cover A (L)
              Side case (L)

Connecting Arm Cover B (R)
                                   Connecting Arm Cover A (R)

 Connecting Arm Cover B (L)
                                   Side case (R)
                   Pedal (L)
                                   Incline Bottom Cover
    A Rear Stabilizer
                                   Rear Stabilizer Cover (B)
    Cover (A)


     Rear Stabilizer               Wheel Cover
     Cover (B)
                                   End Cap, Aluminum Step Rail




                               4                   Service Manual
         Swing Arm (L)           Console Mast


                                 Swing Arm (R)




Generator/Brake Controller

                                 Drive Belt

               Flywheel          Cross Bar


      Connecting Arm (L)


                                 Main Frame

           Pedal Arm(L)
                                 Connecting Arm (R)



       End Cap, Aluminum         Pedal Arm(R)
       Step Rail

                                 Aluminum Step Rail


                                 Aluminum Track




                             5                    Service Manual
2. Electronic Parts




         6            Service Manual
2-1 Upper Controllers


                        Cooling FAN




                                      Thumb Switch




             DISPLAY




                                           EMS BRAKE

                          7                          Service Manual
2-2 Lower Controller and Driver




        SPEED RPM SENSOR




              CONTROLLER




                                  8   Service Manual
3.Electrical Configurations




             9                Service Manual
CONSOLE:
    Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
    The circuit board consist of the generator power supply for console, link the console to output appropriate voltages for tension motor that control

    the elliptical functions.

GENERATOR FLYWHEEL :
    It can change to increase or decrease resistance level of brake.

.

GENERAL INFORMATION
CONSOLE
    Contains Key controls and LED Display.
    Main controller Include power supply(generator power )、 driver control circuit .




                                                                        10                                                             Service Manual
4. XE890B Electrical Operation




              11                 Service Manual
Display Windows
                       LED Display




                  12             Service Manual
Operation
Window Display Mode
  IDLE MODE
     1.1 In the DM to scroll every 2 seconds to display each Program Profile, followed by a Program, and then show that Profile, the corresponding
         Program indicator LED ON.

      1.2 The MW will display     『SELECT A PROGRAM OR PRESS START TO BEGIN』。
       .
  Child Lock Mode   ：
      2.1 Set to ON / OFF in Engineer Mode.
      2.2 When Child Lock ON: Power On MW display "CONSOLE LOCKED" 3Sec, display "CHILD LOCK - ON, PRESS START AND ENTER TO
         ENABLE OPERATION" until you press and hold Hold & Enter Key 2 Sec and enter Idle Mode , Otherwise do not recognize any Key.


  EXERCISE MODE（QUICK START）
     3.1 In IDEL MODE, press START key enter to MANUAL MODE. The age, weight is presetting value.                      Time counting is count up from 00:00.
        All countable data will count up from “0”, and resistance is count up from “1”.


      3.2 You could chose the program by pressing the program key: MANUAL、PROGRAM、CUSTOM、FIT-TEST、HRC1、HRC2.                                     And then, press
         “START” key to start the workout. All parameter will be the preset value.


  PAUSE MODE
       4.1     Press “STOP” key enter to PAUSE MODE, and exercise parameters will be recorded. When you enter Pause Mode, Level returns to the first
             paragraph, "PAUSE PRESS START TO RESUME OR STOP TO END" is displayed on the MW, the program is paused, the DM is displayed at the
             current PROFILE and the position of the flashing motion is stopped, and the counting is stopped. No Start Key or No Speed Pulse detected, 5 minutes
             after entering Idel Mode.




                                                                               13                                                               Service Manual
END MODE
6.1 The message window will display “ END OF WORKOUT SUMMARY” when the workout is end, and display the workout information by three
    minutes.
6.2 END MODE workout information
    6.2.1 Display “AVG LEVEL XX”, “AVG SPD XX.X”, “AVG RPM XX”, AVG RAMP XX in message window each three seconds.
    6.2.2 The message window will display “PROGRAM END PRESS START TO REPEAT OR STOP TO END OR USER KEY TO SAVE”. Press
          START key to restart the same program, STOP key to stop the program, USER key to save the parameter in CUSTOM USER.
   6.2.3 DATA window will display the average value of LEVEL, PULSE.
   6.2.4 CAL window display the total calorie. TIME window display the total exercise time. DIST window display total distance. PACE window
        display PACE value.




RESET MODE
7.1 In IDLE MODE, press STOP key for more than three seconds will enter to RESET MODE and reset the system. If the system is in CONSOLE
    LOCK MODE you have to quit CONSOLE LOCK MODE first, and you can execute the RESET MODE.
7.2 The message window will display RESET two seconds, and finished the reset.   After that, the system is in IDLE MODE.




                                                                   14                                                        Service Manual
Function

   SPEED
      Display the current speed in Kilometer mile per hour.
      DISPLAY range is 0.0 to 99.9
      WORK range is 0.0~99.9
   LEVEL
      Display the incline position from 0 to 20
      DISPLAY range is 0 to 999.
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




                                                                       15                                                         Service Manual
PACE
   “Time” to finish 1KM/MILE workout
   DISPLAY range is 00:00 to 99:99.
   WORK range is 00:00 to 99:99.

DISTANCE
    Display the current distance in kilometer or Mile.
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
    In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds then display value will become “0 ”.




                                                                      16                                          Service Manual
Function Button Locations




 PROGRAM BUTTONS
 (Manual, Hill, Fat Burn,
Cardio, Strength, Interval,
 Custom, Fit-Test, 2HR)




          DISPLAY




                                          Fan Key
                                   Cooling fan switch on or
                                              off


        CONTROL KEYS




                              17                Service Manual
Function Button In Main Mode
  READY MODE
     STOP button: Non-function.
     START button: Pressing “ START ” button to start treadmill, When pressing “START” button, there will be 3 second final count down on window
     display, then machine starts running. In MANUAL, treadmill starts at MIN LEVEL .
      LEVEL UP button: If user doesn’t enter a setting then this button is non-functional.
      LEVEL DOWN button: If user doesn’t enter a setting then this button is non- functional.
      FAN button: It can to control ON/OFF for the fan.
      DISPLAY KEY：
      You could select the profile of SPEED by pressing DISPLAY key when select the program(P0~P5, CUSTOM，FIT-TEST).
      ENTER KEY：
     Press ENTER key enter to parameter setting, and confirm the every setting by pressing ENTER key.




                                                                      18                                                         Service Manual
RUN MODE
  STOP button: press “STOP” button to stop treadmill.
  START button: non-functional.
  ENTER button: non-functional.
  LEVEL UP button: Press the button to increase your level and each increase is 1.
  LEVEL DOWN button: Press the button to decrease your level and each decrease is 1.
  Fan button: It can to control ON/OFF for the fan.
  DISPLAY KEY：
       Press DISPLAY key to switch the exercise data when you are workout. If the display information is the latest data , press DISPLAY key the
       message window will display “DATA SCAN” by two seconds, and then change to auto display every four seconds. The information as
       below,
      『SPEED XX.XMPH』
      『SPEED ** RPM』
      『LEVEL XX MAX XX』(只有 PROGRAM MODE 會顯示) ( only in PROGRAM MODE will show this string)
      『WATT XXX』
      『SEG TIME X：XX』(只有 HRC MODE 不顯示) (only in HRC MODE will not show this string)
      『DATA SCAN』




                                                                   19                                                          Service Manual
5. XE890B Basic Connections and Wiring




                  20                 Service Manual
Display Board PCB Component Locations

 PCB Board Top




                                        21   Service Manual
PCB Board Bottom




                   22   Service Manual
Display Board wire Connections
                                                  COOLING FAN




                                 KEY BOARD




                                             23                 Service Manual
Driver Board PCB Component Locations




                                       24   Service Manual
Driver Board Wire Connections
                                      GENERATOR BRAKE
                                      RESISTANCE VOLTAGE




                                       CN2




 SYSTEM
              CN3
 CABLE




                                         CN1




                                     GENERATOR POWER




                                25                     Service Manual
Driver Board function
                                      GENERATOR
                                      RESISTANCE
                                       VOLTAGE




SYSTEM
CONTROL
                             GENERATOR POWER 2




                             GENERATOR POWER 1




                        26            Service Manual
GENERATOR Flywheet definition function




                                              GENERATOR




                                                          GENERATOR
                                                          RESISTANCE
                                                           VOLTAGE




                                         27                       Service Manual
6. XE890B Error Messages /
     Troubleshooting




            28               Service Manual
    Error code items：


                     Error Message                 Explain
                     EEPROM ERROR                  EEPROM failure




     Error Message：EEPROM ERROR
 Definition: displayed in the MW window "EEPROM ERROR"
 When the EEPROM is damaged or accesses a problem, all the windows are OFF, all outputs are STOP, MW
  displays "EEPROM ERROR"
 Troubleshooting: Replace upper controller.




                                                             29                                         Service Manual
30   Service Manual
MAINTENANCE MENU IN CONSOLE SOFTWARE

   The console has built in maintenance/diagnostic software. The software will allow you to change the
   console settings from English to Metric and turn off the beeping of the speaker when a key is pressed for
   example. To enter the Maintenance Menu (may be called Engineering Mode, depending on version)
   press and hold down the Start, Stop and Enter keys keep holding the keys down for about 5 seconds
   and the Message Window will display “Engineering Mode”. Press the Enter button to access the menu
   below. Press the Level ▲/▼ keys to navigate the menu.
   A. Key Test - Will allow you to test all the keys to make sure they are functioning
   B. Display Test - Automatically tests all LED’s
                                                              ▲▼
   C. Functions - Press Enter to access settings, use Level / keys to scroll
       I.    Sleep Mode - Turn off to have the console power down automatically after 30 minutes of inactivity
       II. Pause Mode - Turn on to allow 5 minutes of pause, turn off to have console pause indefinitely
       III. ODO Reset - Resets the odometer
       IV. Units - Choose from English or Metric display readings
       V. BEEP MODE - ON/OFF
       VI. DA TEST- For testing the DA function
       VII. ELLIPTICAL / BIKE
   D. Security - Allows you to lock the keypad so no unauthorized use of the machine is allowed. When the
      child lock is enabled, the console will not allow the keypad to operate unless you press and hold the Start
      and Enter buttons for 3 seconds to unlock the console.




                                                      31                                       Service Manual
Troubleshooting procedure matrix

                    Condition                                      Reason                                           Solve
LEDs not bright, incomplete or imperfect.        1. LED light is broken.                   1. Replace with new LED or console.
                                                 2. Generator Power to console too low.    2. Check generator power connection.
                                                                                           3. Replace controller.
LED displays not bright, incomplete or imperfect. 1. LED displays are broken.              1. Replace with new console.
Erratic pulse display.                            1. Another chest belt in use around      1. Check for other chest belt use around bike.
                                                     treadmill.                            2. Change the position or direction of bike.
                                                  2. Other magnetic field disturbance.     3. Replace with new receiver.
                                                  3. Receiver is broken.
Hand pulse lost its function.                     1. Hands not on the hand pulse sensors 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                      or only one hand on sensor.
                                                  2. The connector of HANDPULSE            2. Connect the cable again.
                                                     W/WIRE and Console not connected
                                                     properly.                             3. Replace with new cable.
                                                  3. The wires got damaged when
                                                     connecting the HANDPULSE W/WIRE 4. Replace console or Hand pulse board.
                                                     and Console.
                                                  4. Hand pulse board is broken.
Wireless lost its function.                       1. Chest belt not worn properly.         1. Check chest belt has proper contact with skin and is
(No pulse displayed on monitor)                   2. Distance is too far and exceeds range    oriented correctly.
                                                     of receiver.                          2. User chest belt in front of console within 3 feet.
                                                  3. Chest belt battery is weak or dead.   3. Replace with new lithium battery type is CR2032.
No resistance                                     1. Control board are broken.             1. Replace with new Control board.
                                                  2. Generator brake resistance voltage    2. Please re-install wire.
                                                     wire shedding.




                                                                           32                                                           Service Manual
7. Troubleshooting




        33           Service Manual
7-1 Side case & Round Disk Problem
   1. Major problem is noises cause by rubbing between two parts. Identify if the noise is caused by shifting or swing of the Round
      Disk,.




   2. If it is the shifting of the Round Disk, Crank which is causing the noise, release both left and right Chain Covers and
       re-assemble them again.




                                                                 34                                                    Service Manual
   3. If it the swing of the Round Disk, Crank which is causing the noise, then release both Chain Covers and Round Disk, Crank
       then use Phillips head screwdriver to release 16pcs of 5x16m/m tapping screws with 1/4"x19m/m flat washers on Round
       Disk, Crank. Put Cross Bar with Round Disk, Crank on a level surface and check for any sign of warp. Correct the warp with
       force to within 3 mm tolerance.



7-2 Flywheel Problem
   1. 如磁控飛輪有異音,先檢查是否有異物掉落或磨擦,逕行調整,如無法調整則需更換新品。If there is abnormal sound coming from
      the magnetic flywheel, first check if are any foreign objects or friction, make adjustments. If adjustments are not able to be
      made, replace with new part.




                                                                35                                                   Service Manual
7-3 Poly-V Belt Problem
   1. If the Belt falls off, release right Chain Cover and loosen Idler Wheel Assembly and return the Belt on its place. Then turn the
       Belt slowly and watch for the shifting between the Belt and Drive Pulley and the alignment of the Belt, Drive Pulley and
       Inductive Flywheel. Check again at speed as high as 100 to 120 RPM. Resume the unit when everything is fine.

   2. If there is a problem with the alignment, Adjust the Flywheel to a proper position.




   3. If the Belt slips, adjust the nut on J-bolt with 13 mm wrench, as shown in figure 2.

   4. If the Poly-V Belt worn or damaged, replace with new part.




                                                                 36                                                    Service Manual
7-4 Swing Arm Problem
   1. Handlebars are not absolutely tight for easy to assemble to the end user. It is normal for handlebars to shift a little bit.
      However, noises may be caused as time lasts because parts wear. The solution for the noise is to apply some grease on
      mast shaft. If the noises are from button bracket, it needs to change 6005_Bearing


7-5 Connecting Arm and Slide Wheel Problem
   1. Since ellipticals a lot of levers to connect and move parts, Parts interact and affect others a lot. It is very important to lubricate
      each moving parts and joints


   2. There are many factors, which affect the feeling of smoothness. The most important key point is to make sure that sliding
      wheels move parallel and smoothly on the rails. In brief, Pedal Arm should keep parallel with Connecting Arm and both Pedal
      Arm and mainframe keep perpendicular to the bushings.




                                                                    37                                                      Service Manual
3. Check to see if left/Right connecting arm and left/right step is connected properly, if sliding wheel has the correct rotation degrees, slipping
   occurrences or bearing damages, unsecured connections causing noises.          Use #22 open end wrench to remove the fish eye bearing and replace
   with a new part.




4. During maintenance, start from sliding wheels by applying lubricant on wheels or replace if necessary




                                                                         38                                                              Service Manual
8. Q & A




   39      Service Manual
8-1.   Noise
       1. The part making noises is hard to identify. From Chain Cover rubbing Crank Round Disk Cover, Bushing Housing and
          Cross Bar, Belt and Drive Pulley, Idler Wheel Assembly, Handlebar and Mast shaft, Flywheel and Cable to Sliding Wheels
          and Rail Assembly, even Pedals, etc. Insufficient lubrication, smoothness or loose screws are major causes



8-2.   Slip Problem
       1. Slipping problems can be verified by the following steps.
          1-1.M14 x P1.75 Fish-eye bearing: M14 nut must be firmly tightened with Connecting Arm and fish-eye bearing
               perpendicular to the bolt

          1-2.Cross Bar : CAP Socket Head Cap Bolt M8x40m/m on top of the Cross Bar on the must be tightened to recommend
               550~600Lbs.

          1-3.The bolt cap M8x15 on short bushing has to tighten.


       2. The Belt: Belt slipping is quite usual because the belt gets less tensioned as time lasts. Time duration and user weight are
          major factors. Follow procedure to adjust the belt tension




                                                                 40                                                    Service Manual
8-3.   Shaking Problem
       1. Wobble is usually caused by loose screw. When there is wobble, try to tighten all screws and check for installation faults
          or worn out of parts when time lasts. Like a wobble pedal is usually caused by carriage bolt not installed properly. If the
          unit wobbles, adjust the screws for footpad beneath Front Stabilizer

8-4.   Smooth Problem
       1. Check tightness of screws and bolts if the unit clicks.
       2. Otherwise, there might be foreign materials on either the rail or Slide Wheel. Use rubbing alcohol to wipe and apply some
          lubricant both parts




                                                                 41                                                   Service Manual
9.Disassembling and assembling
           of Parts




              42             Service Manual
9-1.   Console Replacement
       1. Use Phillips head screwdriver to remove Phillips Head Screws M5x10mm (4pcs) securing the console. Unfasten all
          connected wires and remove console.
       2. Reassemble in the reverse order as disassembly (Be sure to not crush or damage wiring during process)




                                                             43                                                Service Manual
9-2.   Swing Arm Replacement
       1. Use a Phillips screwdriver to remove Sheet Metal Screws 3.5x12mm securing the swing arm covers (Front and Back)




                                                            44                                                Service Manual
2. Use 14mm open end wrench to remove the hex head bolt 3/8"x15mm and flat washer 3/8"x30x2.0T securing the swing
   arm assembly.




                                                    45                                               Service Manual
3. Use Phillips head screwdriver to the Phillips Head Screw M5x15mm and Sheet Metal Screw 3.5x12 to remove swing arm
   joint cover A (left and right)




                                                     46                                               Service Manual
4.    Use 17m/m_ Combination Wrench and 12mm hex-key wrench to remove M10 × P1.5 × 8T_Nut and M10 ×
     1.5(38L)_Bolt of fixed Swing Arm and Rod End Bearing to take down Swing Arm.




                                                   47                                            Service Manual
9-3.   Connecting Arm Replacement
       1. First, follow the procedure 2 to remove the handle bar (if you need the connecting bar only, just take apart the connection
          between handle bar and fish-eye bearing)
       2. Use Phillips head screwdriver to release Pedal Arm Cover, then release of M6x15m/m screws to and take Front Covers.




                                                                48                                                    Service Manual
3. Use hex-key wrench to remove 5/16"× 3/4"_Hex Head Bolt and 5/16" × 35 × 1.5T_Flat Washer of Pedal Arm to take down
   Pedal Arm and Connecting Arm.




                                                     49                                                Service Manual
4. Use 12 mm wrench to release5/16" x 15m/m hex head bolt and 5/16" x 23 x 1.5T flat washer, which secure the
   Connecting Arm. Then release the carriage bolt and take apart the Connecting Arm.




5. If removal of adjustable pedal set, use Phillips Head Screw Driver and remove four Phillips Head Screws M5x10mm.




                                                      50                                                 Service Manual
6. To take the slide wheel apart, use Phillips head screw driver to release two Phillips head screws M5x15mm and take the
   slide wheel cover first.




7. Use circlip pliers to remove circlip Ø17 and remove sliding wheels




                                                        51                                                 Service Manual
8. Following the steps gradually as beginning of Ø17 × 0.5T_Wave Washer, Ø78_Slide Wheel, Urethane, Ø17 ×
   0.5T_Wave Washer, and Ø17_C Ring when assemble the Ø78_Slide Wheel, Urethane.




                                                    52                                               Service Manual
9-4.   Console Mast Replacement
       1、 Remove the Swing Arms. (Refer to step 11.2)
       2、 Take down Ø25_Wave Washer of Console axle both sides and use Phillips head screwdriver to take down 4pcs Ø3.5 ×
          12L_Sheet Metal Screw, and then take apart and remove the Console Mast Cover.




                                                            53                                               Service Manual
3、 Loosen 3pcs M8 × 1.25 × 25L_Hex Socket Cap Screw about 15mm, remove the last one pc Hex Socket Cap Screw and
  5/16" × 23 × 1.5T_Flat Washer, and then push console mast to take apart console mast and main frame and take out
  computer cable.




                                                    54                                              Service Manual
4、 To dismantle Handpulse Assembly, take the Round Cap apart first and use Phillips head screw driver to release two
   Tapping Screwsψ3x20mm. Pull out Handpulse W/Cable from the bottom and pull Handpulse Top Cover upward.




5、 Reassemble in the reverse order as disassembly




                                                       55                                                  Service Manual
9-5.    Side Case Replacement
       1. Remove Pedal Arm and Console Mast Assembly.
       2. Phillips head screwdriver to remover 7 Sheet Metal Screws 4x19mm from left and right chain cover and Tapping Screws
          5x16mm that secures right chain cover to mainframe, remove right chain cover.




                                                             56                                                Service Manual
3.   And remove 4x16mm x1pcs Tapping Screw and Ø1/4" × 19m/m_flat washer which fixed on main frame from left chain
     cover. And remove 5x16x3pcs tapping screw and then can take out left chain cover.




                                                     57                                               Service Manual
4.   Reassemble in the reverse order as disassembly (Flat Washer 5/16 "x23x1.5T is to be placed on the left cover)




                                                        58                                                  Service Manual
9-6.    Cross Bar Replacement
       1. Remove left and right chain cover. (Refer to step 11.6)
       2. Remove round disk cover and use 6mm L allen wrench to release M8X40mm socket head cap bolt which fixed on cross
          Ba




       3. Use 12mm wrench to remove 5/16"x10mm button head socket bolt and 5/16”x35x1.0T _flat washer and then can take
          down cross cranks.




                                                            59                                              Service Manual
4. Use Phillips head screw driver to release Tapping Screws which secure the Round Disk and separate Cross Bar and
   Round Disk from each other.
5. When reassembling, place the cross bar into the center of the rotating mandrel. Next place the Woodruff Key with the
   rounded part facing inwards. Reassemble remaining parts in the reverse order as disassembly.




                                                        60                                                  Service Manual
9-7.    Idler Wheel Replacement
       1.   Remove the cross bar. (Refer to step 11.7)
       2.   Use #13 wrench to loosen nyloc nut M8x9T on the hook screws to remove belt. Use #13 wrench to remove screws
            M8x20, nyloc nut M8x7T and flat washer 5/16”x20x1.5T to remove the Idler wheel.




       3.   Reassemble parts in the reverse order as disassembly, tighten the nyloc nuts M8x9T on top of the hook screws, flick the
            belt for crisp sound to check tightness or use a sound measuring device to measure at 190HZ(±10), reassemble the
            remaining parts.




                                                                 61                                                  Service Manual
9-8.    Flywheel & Poly-V Belt replacement
       1.   Follow the idler wheel disassembly steps to take down idler wheel and use 11mm wrench to remove 1/4" × 3/4"_hex head
            bolt, Ø1/4" × 19 m/m flat washers, Ø1/4"_Spring Washer and remove power controller wire then can take down Induction
            Brake.




       2.   Reverse above steps to return all parts and adjust the position of the drive belt at the center on the drive pulley (according
            to idler wheel assembling procedures) and resume all parts.




                                                                    62                                                     Service Manual
9-9.   Rear Frame Replacement
       1.   Use hex-key wrench to remove 3/8" × UNC16 × 2-1/4"_Button Head Socket Bolt x2, 3/8" × UNC16 × 3-3/4"_Button Head
            Socket Bolt x2, 3/8" × 19 × 1.5T_Flat Washer x2, 3/8" × UNC16 × 2"_Flat Head Socket Bolt x2 of Rail Support Tube, and
            then remove Rail Support Assembly.




       2.   Use Phillips head screwdriver to remove M5 × P0.8 ×12L_Phillips Head Screw of Rear Stabilizer Cover A/B, take down
            Rear Stabilizer Cover.




                                                                63                                                 Service Manual
3.   Use 6MM hex-key wrench to remove 3/8" × UNC16 × 2-1/4"_Button Head Socket Bolt, 3/8" × UNC16 × 3-3/4"_Button
     Head Socket Bolt, 3/8" × UNC16 × 2"_Flat Head Socket Bolt, 3/8" × 19 × 1.5T_Flat Washer and then take down Rail
     Assembly.




4.   Reassemble in the reverse order as disassembly




                                                       64                                                Service Manual
9-10.    Aluminum Track Replacement
        1.   Remove Rear Stabilizer Cover (Please refer to the method of removing Rail Assembly to take down Rear Stabilizer
             Cover)
        2.   Use 12mm wrench to remove 5/16” × 3/4"_hex head bolt x 3pcs and retaining bracket, aluminum track and take down
             aluminum track to change.




        3.   Reassemble in the reverse order as disassembly




                                                               65                                                Service Manual


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG I

"OU JeUOIeUJa}U] ODBAG

OIVAC

jenuepy BdIAlas
WOLdAV-g0684x


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

SOUIIINO WOLIV-G06EIX "1


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 33 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

yoes| WNUIWN|y

wey days wnuiwnyy

rey dais
uunuiunyy ‘dey pug

(y) Uy [eped

(Y) way Buyoeuu0D
(q)uuy [eped

ewe uley\
(q) way Buloeuu09
weg Ssolp

JaoumA|4

eg SAG

19||ONJUOD eyesg/oyessuesy

(Y) way Buims

Se BJOSUOD ) way ume


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG 8

YSATIOULNOO

YOSNAS Wd Gasdd$S

ADALIG PUB J9][O1]UOD JOMO'T] 2-2


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

suojeinbijuoy [eo14j9e/F7'¢


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

uoleladoC [BI14199/F G0683X “p


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG ZI

( V1
a“ NG ww ) ‘S)

BAT DNL

“IMS
— ap
.. = @E

©
LINAS 0

= /

Ae\dsiq Gat

smopulM\ Aejdsig


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Function Button Locations

PROGRAM BUTTONS
(Manual, Hill, Fat Burn,
Cardio, Strength, Interval,
Custom, Fit-Test, 2HR)

[ DISPLAY

RESISTANCE LEVEI _f
Fan Key

' (~ ENTER w ) “sS
© rs — —1___" © , Cooling fan switch on or
mT) =) off

a

L CONTROL KEYS x Aa

17 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

bulij, pue suolaauu0) dIS@g GO68AX 'G


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Display Board PCB Component Locations

PCB Board Top

000 o300

ees TI TITrrrrryyyryriyry |
©0000000 0000000000000 808
© CC COCOEOOECOCOEORGOOOCOOHS
©CCCCOOOOOCOOOOOOOOEOCEEE
©0000000 00000000 00000888
©000000000000000 00000008
©00000000O0CCOOCCOCOOOCO
800 00000 00000000 00000CC8
eee r ter TIrTisisyiriyy
da bharrrIIIIIIIVirrrryry
a =e

393
a

.

? >

3 a °
a a

965 PPPOE See eee eases

Ph) tststetsy

3999999099909009 39900000 ce aee¢

1 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 16 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
ene
a |

oeeeeene ereveet

> phieener
™
@

So)
i) eeennaee

e
eerrerer eeareer
ee
Sgguiigd sags Fv ee sie s

] :

PYYTTTT TT LE


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 19 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
oeeeeene erereet

beieaeer

ererere

S ) LL

e
eerrerer eeareer
eee ees eee eee
tug nt vais =e eeie «sie s

ss 2 As

FTTTTITT TP MLL


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Driver Board PCB Component Locations

Ot,

‘¢ as. f 9993

3 au —er ee
& .s 94-0

R26 OV

_—

24 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG cz

Y3AMOd YOLVYANAD

O-Ar6
“ae wie BE

. wo » -
cov
|
’

i)

cw y

os
4

= [oe
me |°

Site eee

ADVLIOA AONVLSISSAY
dyVvued YOLVYANAD

SUOI]O9UUOZD dJI/\\ pseOg J9ALIG


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG 97

| YWAMOd HOLVHSANAD |

O-Ar6
“ae wie BE

. wo » -
cov
|
’

ADVLIOA
AONVLSISSAY
YOLVYANAD

uoloun) pueog J8AUG


=== OCR SUPPLEMENT, PDF PAGE 27 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnUDY a1A1aS LZ

ADVLIOA
AONVLSISSAY
YOLVYANAD

YOLVYANAD

uOHoUNY UOIHUEp JBOYMA|4 HOLVHANAD


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG

burllooysaqnol]
/ sabessayy 40117 g0683X “9


=== OCR SUPPLEMENT, PDF PAGE 30 ===
<!-- render-vs-extraction: 37 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOnNUDP AI1A1AS o¢

ao []

EVO SELLA Nid 9
€ND
vo |
aTOT Tene

WETIOWINOO BOLVYENED
MOSNSS Nid ¢

\oO

5

Q (TaLM SOV T/A) NI € A
—a CLEET TOPE aN py
=| et Tt \e

czk JL bb

: WaMAOd YOLVYENED a

CQ

Bs ISHHMA‘H WOLVEENED

OLLVINHHDS “TVOLLd I TTH WOTHV-d068H x


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
3. If it the swing of the Round Disk, Crank which is causing the noise, then release both Chain Covers and Round Disk, Crank
then use Phillips head screwdriver to release 16pcs of 5x16m/m tapping screws with 1/4"x19m/m flat washers on Round
Disk, Crank. Put Cross Bar with Round Disk, Crank on a level surface and check for any sign of warp. Correct the warp with
force to within 3 mm tolerance.

7-2Flywheel Problem
1. MEET A SR TORRE BA Ra BES ET eS, MR led 9 Fg Ean © If there is abnormal sound coming from
the magnetic flywheel, first check if are any foreign objects or friction, make adjustments. If adjustments are not able to be
made, replace with new part.

35 Service Manual


=== OCR SUPPLEMENT, PDF PAGE 58 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JONUDP AI1A1aG gc

(QAO YO] BY} UO P9dE|d 9q 0} SI 1SG°LXE?X,, 9L/G eyUSeN JeI4) A\quiessesip se Japlo asianal 9U} Ul BjquiesseeYy
