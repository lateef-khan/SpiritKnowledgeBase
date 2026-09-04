                     1 of 34




SERVICE MANUAL
                LCB(2023)
            SU615A-SB026
         ENT UPRIGHT BIKE
                                                                                                                                                         2 of 34


                                                                     -Contents-
1.Outlines......................................................................................................................................................... 4
2.Electronic Parts ........................................................................................................................................... 5
     2.1 Console ................................................................................................................................................ 5
     2.2 Controller and Driver parts ................................................................................................................. 5
3.Electrical Configurations ......................................................................................................................... 6
4.Product Operation..................................................................................................................................... 6
5.Unit Block Diagrams................................................................................................................................ 10
6.Basic Connections and Wiring............................................................................................................. 11
     6.1 Display Board wire Connections....................................................................................................... 11
     6.2 Display Board PCB Component Locations....................................................................................... 12
       6.3 Interface Board Wire Connections ................................................................................................... 13
       6.4 Brake Controller Wire Connections .................................................................................................. 13
       6.5 Brake Controller PCB Component Locations................................................................................... 14
       6.6 Brake Controller Functions ............................................................................................................... 14
7. Product Safety Instructions................................................................................................................... 15
     7.1 Important Safety Instructions ............................................................................................................ 15
     7.2 Important Electrical Instructions ....................................................................................................... 15
     7.3 Important Grounding Instructions .................................................................................................... 15
8. Error Messages / Troubleshooting ...................................................................................................... 16
     8.1 Error Message: EEPROM ERR ........................................................................................................... 17
     8.2 Error Message: LWR not found ........................................................................................................ 17
       8.3 Error Message: LWR not match ........................................................................................................ 17
       8.4 Test Configuration ............................................................................................................................. 18
       8.5 Circuit Diagram ................................................................................................................................. 19
       8.6 Maintenance Menu ........................................................................................................................... 20
       8.7 Troubleshooting procedure Matrix .................................................................................................. 21
9. Parts Replacing Guide .......................................................................................................................... 22
     9.1 Replacing the Console ...................................................................................................................... 22
     9.2 Replacing the Handlebar and Console Mast ................................................................................... 22
     9.3 Replacing the Main Frame and Console Mast Cover ...................................................................... 23
     9.4 Replacing the Seat and Sliding Seat Mount .................................................................................... 24
       9.5 Replacing the Inner Slide tube ......................................................................................................... 25
       9.6 Replacing the Crank Arm and Pedal ................................................................................................ 25
       9.7 Replacing the Chain Cover L/R ........................................................................................................ 27
       9.8 Replacing Drive Belt and Idler Wheel Assembly ............................................................................. 28
       9.9 Replacing the Induction Brake .......................................................................................................... 29
       9.10 Replacing the Drive Pulley .............................................................................................................. 30
10. Troubleshooting .................................................................................................................................... 31
     10.1 Troubleshooting for the Console Display problem and Error Message ...................................... 31
                                                                                                                        3 of 34

10.2 Troubleshooting for the Drive Belt Slipping or Falling-off ........................................................... 32
10.3 Troubleshooting for the Noise during pedaling ............................................................................ 34
             4 of 34


1.Outlines
                                  5 of 34


2.Electronic Parts
2.1 Console




2.2 Controller and Driver parts
                                                                                             6 of 34


3.Electrical Configurations
Console              Interface that controls all functions of the Bike.
Brake Controller The circuit board consist of the DC power supply for console.
EMS Brake            It can change to increase or decrease resistance level of brake.


GENERAL INFORMATION
Console              It is including keypad to control and LCD Display.
                     Brake controller Include power supply and EMS driver control circuit.
EMS Brake            Work voltage: DC 0~21V
                     Control resistance increases and decreases.




4.Product Operation
                                                                                                                 7 of 34

Window Display Mode
IDLE Mode    -PICK ONE OF GUEST OR PERSON ACCOUNT.
             -The main screen of the Training section displays an overview of your activity and offers shortcuts to the
             most frequently used training modes: an immediate Start, a manually controlled timed workout
             (“Timer”), and up to 3 programs that you have marked as your favorites are arranged on this page for
             your quick access.
             -If in the Guest mode, you can set your age and weight here; it will help the machine calculate your
             workout summary more accurately.
             -If in the User mode, You have a personal account, including age、weight…etc. You will not need to re-
             create your profile.; it will help the machine calculate your workout summary more accurately.
SLEEP Mode   -The console will not get into SLEEP MODE when the setup is “OFF”, unless turn off the power. The sleep
             mode is to set in “ON”. There is no RPM input in IDEL MODE and enter to SLEEP MODE after 15 minutes
             without pressing any key.
             -In SLEEP MODE, TFT LCD screen will has no display, and backlit will be off. Press any key to wake up the
             system, and back into IDEL MODE.
             -Resistance in SLEEP MODE: Incline =1, Cooling Fan off.
Child Lock   -Pre-set: CHILD LOCK OFF (DISABLE). You could set the CHILD LOCK ON/OFF by Setting.
Mode         -The screen will display “CONSOLE LOCKED” when CHILD LOCK setup is ON. You could setup the CHILD
             LOCK MODE OFF by pressing “START” and ”ENTER” key for more than two seconds. After that it will enter
             to IDEL MODE.
             -All keys will be no action when CHILD LOCK MODE is active.
EXERCISE     -In IDEL MODE, press START key enter to MANUAL MODE. The age, weight is presetting value. Time
Mode         counting is count from 00:00. All countable data will count from “0”, and resistance is count up from “1”.
             -You could chose the program by pressing the program icon: MANUAL、HILL、FAT BURN、CARDIO、
             STRENGTH、HIIT、CUSTOM、HEAT RATE、FITNESS TEST. Then press “START” key to start the
             workout. All parameters will be the preset value.
PAUSE Mode   -Press “STOP” key enters to PAUSE MODE, and exercise parameters will be recorded.
             -The resistance level is “1”. The resistance should back to the preset level before it pauses when press
             “START” key or touch” Resume” icon.
             -It will enter to IDLE MODE after waiting by five minutes without pressing any key in PAUSE MODE.
END Mode     -The touch screen will display workout summary after end workout.
             END MODE workout information: Displays all finished message on the touch screen.
             -When the time counting is end, and END MODE display is finished without pressing any key in 3
             minutes. The system will enter IDLE MODE.
RESET Mode   -In idle mode (except when the child lock is on, in which case the reset function must be released first),
             press the Stop key for 3 seconds to enter the reset function and restart the system.
             -The reset mode clears all screens and enters idle mode after restarting.
                                                                                                             8 of 34

Function
SPEED      Display the current speed in mile per hour.
           DISPLAY range is 0.0 to 99.9.
           WORK range is 0.0~99.9
LEVEL      Display the level position from 1 to 40.
           DISPLAY range is 0 to 999.
           WORK range is 1 to 40.
           LEVEL preset value is 1 to 40.
           Press “UP” or ”DOWN” to adjust level, each increment and decrement is 1.
TIME       TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets the time, then timer
           is COUNT DOWN.
           DISPLAY range is 0:00 to 99:99.
           WORK range is 0:00 to 99:59.
           COUNT DOWN setup range is 10:00 to 99:00.
           When TIME is set, the count will go to zero.
           In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode” again that value will
           continue count time.
LAPS       Display the total working laps quantity.
           DISPLAY range is 0 to 99.
           WORK range is 0 to 99.
           Displays total laps quantity.
DISTANCE   Display the current distance in kilometer or Mile.
           DISPLAY range is 0.0 to 99.9.
           WORK range is 0.0 to 99.9.
CALORIES   Displays the cumulative calories burned at any given time during your workout.
           DISPLAY range is 0 to 999.
           WORK range is 0 to 999.
PULSE      Displays the heart rate beat by using hand pulse or receiver. When use receiver, a chest belt must be
           worn.
           DISPLAY range is 0 to 999.
           WORK range is 40 to 220 BPM.
           In EXERCISE Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value will become
           “0 ”.
                                                                                                              9 of 34

Function Button Locations




Button Function in each mode

Ready Mode
Stop Button     Non-function.
Start Button    Pressing “START” button to start bike, when pressing “START” button, there will be 3 second final
                count down on window display, then machine starts running. In MANUAL, bike starts at MIN LEVEL.
Fan Button      It can control ON/OFF for the fan.
Display key     Non-function.


EXERCISE Mode
Stop Button     press “STOP” button to stop bike.
Start Button    Non-function.
Fan Button      It can control ON/OFF for the fan.
Display key     Press DISPLAY key to display the exercise states when you are workout. There are have data states、
                charts and track three mode.
                        10 of 34


5.Unit Block Diagrams
                                     11 of 34


6.Basic Connections and Wiring
6.1 Display Board wire Connections
                                            12 of 34

6.2 Display Board PCB Component Locations
PCB Board Top view




PCB Board Bottom view
                                        13 of 34

6.3 Interface Board Wire Connections




6.4 Brake Controller Wire Connections
                                               14 of 34

6.5 Brake Controller PCB Component Locations




6.6 Brake Controller Functions
                                                                                                                                15 of 34


7. Product Safety Instructions
7.1 Important Safety Instructions
- To reduce the risk of electric shock, disconnect your bike from the electrical outlet prior to cleaning and/or service work.
- To reduce the risk of burns, fire, electric shock, or injury to persons, install the bike on a flat level surface with access to a 120-
volt, 15-amp grounded outlet with only the bike plugged into the circuit.
- Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not attempt to disable the
grounded plug by using improper adapters or in any way modify the cord outlet.

7.2 Important Electrical Instructions
- Never use a ground fault circuit interrupt (GFCI) wall outlet with this bike. As with any appliance with a large motor, the GFCI
will trip often. Route the power cord away from any moving part of the bike including the elevation mechanism and transport
wheels.
- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can occur when a bike is
first turned on or even during use. If your bike is tripping the house circuit breaker (even though it is the proper current rating)
but the circuit breaker on the bike itself does not trip, you will need to replace the home breaker with a high inrush type. This is
not a warranty defect. This is a condition we as a manufacture have no ability to control. This part is available through most
electrical supply stores. Examples: Grainger part # 1D237, or available online at www.squared.com part # QO120HM.


7.3 Important Grounding Instructions
- This product must be grounded. If the bike should malfunction or breakdown, grounding provides a path of least
resistance for electric current, reducing the risk of electric shock. This product is equipped with a cord having an equipment-
grounding plug. The plug must be plugged into an appropriate outlet that is properly installed and grounded in accordance with
all local codes and ordinances.
- DANGER - Improper connection of the equipment-grounding conductor can result in a risk of electric shock. Check with a
qualified electrician or serviceman if you are in doubt as to whether the product is properly grounded. Do not modify the plug
provided with the product if it will not fit the outlet; have a proper outlet installed by a qualified electrician. This product is for
use on a nominal 120-volt circuit and has a grounding plug that looks like the plug illustrated below. A temporary adapter that
looks like the adapter illustrated below may be used to connect this plug to a 2-pole receptacle as shown below if a properly
grounded outlet is not available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from the adapter, must be
connected to a permanent ground such as a properly grounded outlet box cover. Whenever the adapter is used, it must
be held in place by a metal screw.
                                                                             16 of 34


8. Error Messages / Troubleshooting
Error Code List

            Code        Description
         EEPROM ERR     EEPROM failure
        LWR not found   Driver board controller is not found.
        LWR not match   Driver board controller is not match with console.


Tools Required

A multi-meter.
                                                                                                                17 of 34

8.1 Error Message: EEPROM ERR

Definition:
All screens are off, and outputs are stop when EEPROM damaged or malfunction. Display message will show “EEPROM ERR”.


Troubleshooting:
The EEPROM is abnormal, please replace the Display Board directly.


8.2 Error Message: LWR not found
Definition:
Brake controller is not found.


Troubleshooting:
1. Check connector of 6 PIN computer cable.
2. Replace Brake controller.
3. Replace Display board.


8.3 Error Message: LWR not match
Definition:
Brake controller is not match with console.


Troubleshooting:
1. Check brake controller number is CS51012.
2. Replace Display board.
                                                                                      18 of 34

8.4 Test Configuration

Test configuration: the console to brake controller connector pin defines function.




Test configuration: EMS Brake control function relate parts location.
                      19 of 34

8.5 Circuit Diagram
                                                                                                  20 of 34

8.6 Maintenance Menu
Press 10 times on “Settings” letter to enter engineering mode when you’re at the Settings page.
                                                                                                                          21 of 34

8.7 Troubleshooting procedure Matrix
Condition                       Reason                                                Solve
TFT LCDs not bright,            1. TFT LCD light is broken.                           1. Replace with new TFT LCD or console.
incomplete, or imperfect.       2. Power to console too low.                          2. Check AC power is 110-120V.
                                                                                      3. Check power to console.
                                                                                      4. Replace lower controller.
TFT LCD displays not bright,    TFT LCD displays are broken.                          Replace with new console.
incomplete, or imperfect.
Erratic pulse display.          1. Another chest belt in use around Elliptical.       1. Check for other chest belt use around
                                2. Other magnetic field disturbance.                     Elliptical.
                                3. Receiver is broken.                                2. Change the position or direction of
                                                                                         Elliptical.
                                                                                      3. Replace with new receiver.
Hand pulse lost its function.   1. Hands not on the hand pulse sensors or only one 1. Two hands hold the hand pulse.
(No pulse displayed on             hand on sensor.
monitor)                        2. The connector of HANDPULSE W/WIRE and              2. Connect the cable again.
                                   Console not connected properly.
                                3. The wires got damaged when connecting the          3. Replace with new cable.
                                   HANDPULSE W/WIRE and Console.
                                4. Hand pulse board is broken.                        4. Replace console or Hand pulse board.
Wireless lost its function.     1. Chest belt not worn properly.                      1. Check chest belt has proper contact with
(No pulse displayed on                                                                   skin and is oriented correctly.
monitor)                        2. Distance is too far and exceeds range of receiver. 2. User chest belt in front of console within 3
                                                                                         feet.
                                3. Chest belt battery is weak or dead.                3. Replace with new lithium battery type is
                                                                                         CR2032.
Chest belt too close to the     Weak battery.                                         Replace with new lithium battery with type
Bike.                                                                                    CR2032.
                                                                                                                    22 of 34


9. Parts Replacing Guide
9.1 Replacing the Console
Step 1: Use Phillips head screwdriver to release four M5×12mm Phillips Head Screws and Console and both hand pulse sensor
       cables to take console apart.




Step 2: Reverse above step to resume console.


9.2 Replacing the Handlebar and Console Mast
Step 1: Follow the section 9.1 to remove the console.
Step 2: Using a 5mm L-Allen wrench to remove 4 pcs of 5/16” x 5/8” Hex head bolts, 4 pcs of 5/16” x 18mm x 1.5T flat washers
       and 4 pcs of 5/16” x 1.5T Split washers which secured the handlebar assembly (L/R).




Step 3: Remove four Ø3 × 10m/m Tapping Screws to remove Handgrip Side Caps (Top)and (Bottom).
                                                                                                                    23 of 34

Step 4: Use Phillips head screwdriver to release four 20m/m Tapping Screws securing Hand pulse W/Cable Assembly and
       separate Hand pulse W/Cable Assembly from each other and remove,




Step 5: Reverse above step to resume.


9.3 Replacing the Main Frame and Console Mast Cover
Step 1: Follow section 9.2 to remove the console and both sides of the handlebar.
Step 2: Slightly press the Console Mast Cover to separate it from left and right Chain covers.




Step 3: Using 12 wrench to release 7pcs of 5/16" × 5/8"_Hex Head Bolt, 6pcs of 5/16" × 18mm ×1.5T_Flat Washer and 1pcs of
       5/16" × 19 ×1.5T_Curved Washer and the Handlebar can be released.




Step 4: To resume installing the Console Mast, guide the Computer Cable through the Console Mast and out of the console
       mounting plate. Then, insert the Console Mast onto the Mainframe. Use a 12 mm wrench to tighten 7 pieces of 5/16" ×
       5/8" Hex Head Bolts, 6 pieces of 5/16" × 18mm × 1.5T Flat Washers, and 1 piece of 5/16" × 19 × 1.5T Curved Washer.
                                                                                                                         24 of 34

       Finally, reattach the Console Mast and Chain Covers respectively.


9.4 Replacing the Seat and Sliding Seat Mount
Step 1: Use 14 mm wrench to loosen both hex head bolts to remove Seat.




Step 2: Use 14 mm wrench to remove the Cap Nut.




Step 3: Turn to take Brake Tension Knob apart from Fix Plate and remove Sliding Seat Mount.




Step 4: To resume, install Sliding Seat Mount on Seat Slider then put Fix Plate on it. Install Brake Tension Knob from bottom
       upward to Fix Plate and tighten with 3/8"x7T Nut. At last, insert Seat into the sliding tube and tighten both hex head bolts
       with 14 mm wrench.
                                                                                                                        25 of 34

9.5 Replacing the Inner Slide tube
Step 1: Remove the Locking Knob.




Step 2: pull seat slider and seat post cover up. Take Center spatial wrap apart from Main Frame with a rubber hammer (refer to
       photo 2), and then use Phillips Head Screwdriver to release 2 pcs of 4 × 12m/m Sheet Metal Screws, then remove Slide
       Spacer with rubber hammer to take Seat Slider and Center spatial wrap apart.




Step 3: To resume, return Center spatial wrap back to Seat Slider then return Slide Spacer in Seat Slider and tighten with two pcs
       of 4×12m/m Sheet Metal Screws and insert into the Main frame. Use rubber hammer to return Center spatial wrap and
       resume Locking Knob.


9.6 Replacing the Crank Arm and Pedal
Step 1: Use 13/15mm open end wrench to take apart pedals by turning left pedal clockwise and right pedal counterclockwise.
                                                                                                                       26 of 34




Step 2: To resume pedals, turn pedals with reversed directions respectively.
Step 3: Take Crank Arm End Cap apart and use plug wrench to release the nut.




Step 4: Apply crank tool on the crank to fix and use Allen wrench to release the crank.




Step 5: To resume the crank (16L,16R), use air crank tool or rubber hammer to fix the crank (16L,16R) on the axle and tighten the
       nut on the crank axle and plug in the Crank Arm End Cap.
                                                                                                                       27 of 34

9.7 Replacing the Chain Cover L/R
Step 1: Take apart pedals and crank arm. Separate the Console Mast Cover, and use Phillips head screwdriver to release nine
       Ø3.5 × 16m/m Sheet Metal Screw and three 5 ×16m/m Tapping Screw, which secure left shroud.




Step 2: Use 15mm open end wrench to take apart DC Power Cord and to take left shroud apart.




Step 3: Use Phillips head screwdriver to release 3 pcs of 5 ×16m/m Tapping Screw to remove Chain Cover R.
Step 4: To resume, install Right Side Case on the Main Frame by using Align the center of the Wheel with the center of the Axle
       and secure with 3pcs of 5x16mm Tapping Screws by using Phillips Head Screwdriver then install back DC Power Cord, to
       secure further. Match Left Side Case with Right Side Case and secure with 9pcs of 3.5x12mm Self Tapping Screws, 3pcs of
       5x16mm Tapping Screws. Follow step 2.1 to resume Cranks and Pedals.
                                                                                                                        28 of 34

9.8 Replacing Drive Belt and Idler Wheel Assembly
Step 1: Follow section 9.7 to remove Chain Cover L/R.
Step 2: Use 13 m/m wrench to release M8x7T Nut (77) and take off the J-Bolt (85). Use Phillips Head Screwdriver to unscrew
       3pcs of M6x7T Phillips Head Screws on Idle Arm (9) and the Belt (14) can be taken off.




Step 3: To release the Idle Arm (9), Unscrew 3pcs of M6x15 Phillips Head Screws (56) with 3pcs ofø1/4" Split Washers (73) and
       3pcs of 1/4”x13x1T.
Step 4: To resume the Belt (14) and Idle Arm (9), use Phillips Head Screwdriver to secure the Generator Flywheel (20) with 3pcs
       of M6x15 Phillips Head Screws together with 3pcs ofø1/4" Split Washers (73) and 3pcs of 1/4”x13x1T Flat Washers (69).
       Turn the Drive Pulley (15) to let the Belt on the Pulley, hook the J-Bolt on the mainframe and use 13 m/m wrench to
       tighten M8x7T Nut (77) on the J-Bolt until the Belt (14) is with acceptable tension. Use audio tension gauge to make sure
       the frequency within the range of180~205HZ. At last, turn the Drive Pulley (15) and make sure the Drive Belt (14) is set in
       the center without falling out of pulley.
                                                                                                                   29 of 34

9.9 Replacing the Induction Brake
Step 1: Follow section 9.7/9.8 to remove the Chain Cover L/R and Drive Belt.
Step 2: Unplug electric wires connected to the Induction Brake (20) then use 11 m/m wrench to unscrew 4pcs of 1/4”x3/4” Hex
       Head Screws (54) with 4pcs of 1/4"x13x1T Flat Washers (69) and 4pcs of ø1/4"Split Washers (76) and you can release
       Induction Brake (20).




Step 3: Follow steps in order to resume the Induction Brake.
                                                                                                                30 of 34

9.10 Replacing the Drive Pulley
Step 1: Follow section 9.7 to remove Chain Cover L.
Step 2: Use C Ring tweezers to remove Ø20 C Ring on Crank Arbor, as shown in figure.




Step 3: Use two 11 mm open end wrenches to remove four 1/4" × 3/4"_Hex Head Bolts together with four 1/4" × 8T_Nyloc Nuts
       on Crank Arbor and Drive Pulley to take Drive Pulley apart as shown in figure.




Step 4: Reverse above step to resume.
                                                                                                                         31 of 34


10. Troubleshooting
10.1 Troubleshooting for the Console Display problem and Error Message
Problem: The Screen doesn't light or has no power.
Solution:
1. Make sure the console and computer Cables are connected properly.
2. If the connection of all cables is good, then check the power adaptor is providing the correct voltage to the Bike.




Problem: The console doesn’t show the Speed value.
Solution:
1. When the console displays without speed, dismantle Chain covers to check Computer Cable and Sensor W/Cable to make sure
  of proper installation, as shown in figure.
2. If installation is OK, normally there is problem with Sensor W/Cable or Magnet. Use another magnet to determine if there is a
  problem with Sensor W/Cable (46). Either Sensor W/Cable or Magnet requires replacement.
                                                                                                                        32 of 34

Problem: The Console doesn’t show the heart rate when using the handgrip pulse.
Solution:
1. The console is displaying but there is no HR shown. Check if hand pulse sensor cable is properly connected to the console, as
  shown in figure 1 and if hand pulse assemblies’ cables are properly connected with sensor wires.
2. If they are all connected well, check Hand pulse Assembly. Replace the wire cable if necessary. Remark: The console and
  related parts were all inspected prior to shipping and the probably of defective is low.




10.2 Troubleshooting for the Drive Belt Slipping or Falling-off
Problem: The drive belt is slipping when pedaling.
Solution:
1. Take apart both left and right Chain Covers and Crank Arms.
2. Use 13 mm open end wrench to tighten M8 Nylon Nut until sound wave tension gauge reads 180~205Hz. Since this model is
  driven by Drive Belt, the user weight or the way of use may cause the belt to slip. Generally, the belt won’t slip under normal
  usage.
3. Since the driving belt itself is with malleability and is expendable, it is normal to get loose as time lasts.
                                                                                                                                 33 of 34

Problem: The drive belt is falling off when pedaling.
Solution: Follow the section 9.8 of Parts replacing Guide to install the driving belt and test by revolving forward and backward
after adjustment. If the belt falls off, adjust it one groove toward the direction the belt falling off and test again. If the belt still
falls off, the machine might be so heavily dropped that part dimension deviates. Try to replace the drive pulley, Bearing Housing
or flywheel. If the problem persists, the mainframe could be deformed and the whole unit should be replaced. The possibility of
such a circumstance is low as all units were tested prior to shipping.
                                                                                                                      34 of 34

10.3 Troubleshooting for the Noise during pedaling
Problem: The drive belt is slipping when pedaling.
Solution:
The causes of noises are mostly loose screws. Sometimes it is because of parts being deformed or shifting causing rubbing or
unsmooth moving. Most causes are as follows:
1. Noises coming from left and right pedals. This is mostly pedal wear causing noises and not moving smoothly. The worn-out
pedal must be replaced, as shown in figure.




2. Left and right crank. Sometimes crank gets loose causing noises and not moving smoothly. Tightening the crank can fix the
problem, as shown in figure.
