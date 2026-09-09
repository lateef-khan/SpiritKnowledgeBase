<!-- Source: CE800ENT Service Manual.pdf. Text is `pdftotext -layout` per page. -->
<!-- Pages that are flattened images, OCR'd and NOT reliable: 12, 16, 22, 26, 31, 32, 33, 34. Page images are at `raw/page-NN.png` (300 dpi, gitignored). -->

  CE800 ENT
          2020 ver.

Service Manual

                                                     Table of Contents

1. Outlines............................................................................................................................................. 4
2. Electronic Parts................................................................................................................................ 6
3. Electrical Configurations ............................................................................................................... 9
4. Product Operation ....................................................................................................................... 11
5. Unit Block Diagrams ..................................................................................................................... 15
6. Basic Connections and Wiring ................................................................................................... 17
7. Error Messages / Troubleshooting .............................................................................................. 24
   7-1 Error Message: E5 ................................................................................................................... 25
   7-2 Circuit Diagram ...................................................................................................................... 26
   7-3 Troubleshooting procedure matrix ...................................................................................... 27
   7-4 Engineering Mode Instructions............................................................................................. 28
       Home ....................................................................................................................................... 28
       Engineering Mode Settings .................................................................................................. 29
       Engineering Mode ................................................................................................................. 30
       Security .................................................................................................................................... 31
       Diagnostics.............................................................................................................................. 32
       Machine Information ............................................................................................................ 33
       Maintenance.......................................................................................................................... 34
       A/V Source Setup .................................................................................................................. 35
8. Disassembling and Assembling .................................................................................................. 36
    8-1 Console Replacement .......................................................................................................... 37
    8-2 Swing Arm Replacement ...................................................................................................... 37
    8-3 Connecting Arm Replacement ........................................................................................... 39
    8-4 Console Mast Replacement ................................................................................................ 43


                                                                                                                                                             2

8-5 Chain Cover Replacement .................................................................................................. 45
8-6 Cross Bar Replacement ........................................................................................................ 47
8-7 Idler Wheel Assembly replacement .................................................................................... 49
8-8 Flywheel & Poly-V Belt replacement................................................................................... 50
8-9 Rear Rail Assembly replacement ........................................................................................ 51
8-10 Aluminum Track replacement ........................................................................................... 53




                                                                                                                                        3

1. Outlines




              4

                       Console
   Cooling Fan



Console Mast Cover     Hand Pulse Sensor



                     Drink Bottle Holder
          Shroud



                       Pedal
   Rear Stabilizer


                     Slide Wheel Cover




                                           5

2. Electronic Parts




                      6

Upper Controllers



                        Display
                                      Cooling Fan

                                      Thumb Switch

                                      Earphone Port




                    Induction Break




                                                      7

Lower Controller and Driver




            Controller        Speed RPM Sensor




     PCB & Power Converter




                                                 8

3. Electrical Configurations




                               9

CONSOLE:
Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
The circuit board is consist of the power supply for console, link the console to output appropriate voltages for braking resistance that control Bike functions.

GENERATOR FLYWHEEL:
It can change to increase or decrease resistance level of brake.

INCLINE MOTOR:
This is an AC motor. User can to control variable elevation by console within main controller.


GENERAL INFORMATION
CONSOLE:
Contain keys control and TFT LCD touch panel. Main controller Include power supply, driver control circuit.




                                                                                                                                                                    10

4. Product Operation




                       11

<!-- PAGE 12: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-12.png` before citing anything from this page. -->

Display Windows

Bluetooth
Heart rate Icon

Stars, Stop, and LEVEL
Control Keys

Home

=e            Exercise              ge           Internet
7             Programs

ff                Screen                  (Aa)
a)     Mirroring       Me      maid

To begin workout press START on the keypad below.

SPIRIT

TFT LCD Touch Panel &
Program Menu

Adjustable fan angle

USB Charging port

12

Operation

  FUNCTIONS OF THIS UPRIGHT BIKE
  The Touchscreen is used for operating all functions. You can directly touch any button on the screen or through quick button on the bottom to control
  functions. On the lower portion of the console there is the Start button to begin the workout, Stop button to pause/stop programs, Level button to change
  workload.

  QUICK START
  This is the quickest way to start a workout. After the console powers up you just press the Start button to begin. This will initiate the Quick Start mode. In
  Quick Start the Time will count up from zero, all workout data will start to accrue and the workload may be adjusted manually by pressing on the screen or the
  Up and Down buttons on lower control panel.

  HEART RATE FEATURE
  The Pulse (Heart Rate) on the screen shows the current value of the heart beats per minute. You must use both left and right stainless steel sensors to pick up
  your pulse. Pulse values are displayed anytime the computer is receiving a signal from the hand pulse sensors. You may use the hand pulse sensors while in
  Heart Rate Control. The CU800ENT will also pick up wireless heart rate transmitters that are Polar and Bluetooth compatible.

  INTERNET
  The Internet section offers various streaming, news, and social media options. The machine must be connected to the internet in order for the apps to work.
  Simply click on the app of your choice to connect. Follow any on-screen prompts to continue login or other authorizations as needed.

  EARPHONE
  The console has built-in an earphone sound output jack. The Jack is not an audio input jack. The volume must be controlled on the speaker icon.




                                                                                                                                                                    13

CHARGING FUNCTION
Charge your personal device during your workout using the fitness equipment’s on-console USB port. To charge your mobile electronics make sure the fitness
equipment power is on.
NOTE：
* USB charging cable is not included; make sure compatible USB charging cable is being used.
** Your device “charging” icon may or may not indicate it is charging. Depending on the amount of current your particular device requires for charging the icon
may not be on but your device is still charging, but possibly at a lower charge rate.
***The USB port on the console is capable of powering USB devices. It provides up to 5Vdc/1.0 amp of power and meets USB 2.0 regulations. You will not be
able to save your workout data to a USB via this port; it is used for charging purposes only.



PROGRAMMABLE FEATURES
Each of the programs can be customized with your personal information and changed to suit your needs. Some of the information asked for is necessary to
ensure the readouts are correct. You will be asked for your Age and Weight. Your Age is necessary during the Heart Rate control program to ensure the correct
settings are in the program for your Age. Otherwise the work settings could be too high or low for you; entering your Weight aides in calculating a more
correct Calorie reading. Although we cannot provide an exact calorie count we do want to be as close as possible.




                                                                                                                                                                  14

5. Unit Block Diagrams




                         15

<!-- PAGE 16: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-16.png` before citing anything from this page. -->

Bike Configuration

COOLING

HEART RATE               C-SAFE
(WIRELESS)                FUNCTION

         :

FAN

HR

DISPLAY BOARD

(HANDLEBAR)

USB           le

CHARGER

POWER

On/Off SWITCH
MODULE

<               KEYBOARD

~

INDUCTION
BRAKE

AN

A

POWER BOARD

RPM
SENSOR

V

CONTROLLER

(FOR TFT LCD             <

>| TOUCH PANEL)

>| (RESISTANCE
CONTROL)

i)

16

6. Basic Connections and
          Wiring




                           17

The back of console transfer PCB board




             HDMI Cable


                                         Ethernet Cable


              Hand Pulse
                 (4 Pins)



                                         C-SAFE Cable (5 Pins)
              Hand Pulse
                 (3 Pins)




                                         System Cable (6 Pins)


    System Cable (4 Pins)




                                                                 18

Driver Board PCB Component Locations and Wire Connections




                                                            Controller Cable
          RPM Sensor


        Brake Coil Wire                                     AC L (input)



                                                            AC N (input)




                                                                               19

The console POWER BRIDGE PCB board and POWER CONVERTER




                                                         AC_L (Output)
   Computer Cable
       (6+2+2 Pins)

                                                         AC_N (Output)




        DC_13V/4A
     (Converter End)                                     AC_N (Input)



                                                         AC_L (Input)




    Controller Cable




                                                                         20

The Console HDMI/Coaxial cable/C-SAFE PCB board




                        Coaxial             HDMI    C-SAFE
                        Cable               Cable   (5 PINS)




                                                               21

<!-- PAGE 22: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-22.png` before citing anything from this page. -->

Power Converter PCB board

POWER CONVERTER
V+ (RED)

POWER CONVERTER
V- (BLACK)

wie te de we de de os
2©0eceeee
™eOorcrcr@eeso

ec el &€° @@

e@er °C ee

—

% @©@00CSC06

a

AC_N
(AC Output)

AC_L
(AC Output)

22

Flywheel definition function




                               Induction Brake




                               Resistance Voltage




                                                    23

7. Error Messages /
 Troubleshooting




                      24

7-1 Error Message: E5

Definition
It is a Poor communication, between the console and lower controller is poor communication, almost it is bad on a main control wire, but also possible bad at console
board or lower controller.


Configuration                                                                        Troubleshooting




                                                                                        Part                       Troubleshooting
                                                                                                                   Replace main control wire.
                                                                                        Lower controller board
                                                                                                                   Replace new lower controller.
                                                                                                                   Reinsert Main control wire.
                                                                                        Main control wires
                                                                                                                   Replace main control wire.
                                                                                                                   1. Inspect the wire connections.
                                                                                        Console cable              2. Inspect whether wires are broken or crimped.
                                                                                                                   3. Replace the wires and test again.
                                                                                        Console                    Replace new console.




                                                                                                                                                                     25

<!-- PAGE 26: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-26.png` before citing anything from this page. -->

7-2 Circuit Diagram

=                               oO
f    f
ho
0                                    3
a                                                  BLACK WARE
VETTE VARE
RACK WARE
VMITE WARE                                                                  tt
x<
i           STs                           Jt 1-                                                               m
i                                                                                   8                        on
Hi                   3 PIN CABLE   Le                             oO
Q               B4| ov| 88                                      O              na
9                    mn          one)         De                                     ht         oO                  ~<
z                       ae      zs           5                 4 PIN CABLE   ry         =                  a
5                m=| Oa                                                 Yn              oO
fe)                o =     zs                                                    oO              OD
———     m                D        a                                                    m
s                 -                iS)                                                                              ©
=          j                                                                                                      an
m 0                                                                                                                                   -
:                d              Bs  age    F:                                                 [] (]            >
n                                2             *                                                5                 a
5 PINS CONTROLLER                                                                       é
CARE
23                                                           6+4(6+2+2) PINS COMPUTER CABLE                    é
_                        HDMI CABLE
aq | 2                          ETHERNET CABLE
—
:  i                       5 PINS C-SAFE CABLE

26

7-3 Troubleshooting procedure matrix

                 Condition                                          Reason                                                          Solve
TFT touch panel not bright, incomplete or     1. Power cord isn’t plugged into outlet               1. Check power cord to line equipment.
imperfect.                                    2. TFT touch panel is broken.                         2. Check the power has 120VAC.
                                                                                                    3. Replace new console.
Erratic pulse display.                        1. Another chest belt in use around treadmill.        1. Check for other chest belt use around bike.
                                              2. Other magnetic field disturbance.                  2. Change the position or direction of bike.
                                              3. Receiver is broken.                                3. Replace with new receiver.
Hand pulse lost its function.                 1. Hands not on the hand pulse sensors or only one 1. Two hands hold the hand pulse.
(No pulse displayed on monitor)                  hand on sensor.
                                              2. The connector of HANDPULSE W/WIRE and 2. Connect the cable again.
                                                 Console not connected properly.
                                              3. The wires got damaged when connecting the 3. Replace with new cable.
                                                 HANDPULSE W/WIRE and Console.
                                              4. Hand pulse board is broken.                        4. Replace console or Hand pulse board.
Wireless lost its function.                   1. Chest belt not worn properly.                      1. Check chest belt has proper contact with skin and is oriented
(No pulse displayed on monitor)               2. Distance is too far and exceeds range of receiver.    correctly.
                                              3. Chest belt battery is weak or dead.                2. User chest belt in front of console within 3 feet.
                                                                                                    3. Replace with new lithium battery type is CR2032.
Bluetooth chest strap heart rate monitor no   1. No heart rate display on console.                  1. Check the Bluetooth chest strap of power is enough.
function                                                                                            2. Turn on Bluetooth on the console of system, tap the name of
(No pulse displayed on monitor)                                                                        the Bluetooth device you want to pair with your Bluetooth
                                                                                                       chest strap.
No resistance                                 1. Control board are broken.                          1. Replace with new Control board.
                                              2. Generator brake resistance voltage wire shedding. 2. Please re-install wire.
                                              3. Driver IC broken.                                  3. Replace the new console.
No internet                                   1.Can not to use internet                             1. Check Wi-Fi must be turned on, and WIFI must be connected.
                                                                                                    3. Ethernet must be connected and set.




                                                                                                                                                                  27

7-4 Engineering Mode Instructions

Home
Click on the Home icon at the top of the main page center 10 times to enter a total of 6 sub-menu modes on the setting page.




                                                                                                                               28

Engineering Mode Settings

                Items                 Description
                Engineering Mode      Set the unit, Sleep mode
                Security              Set Lock Accumulate mileage.
                Diagnostics           The Error Diagnostics
                Machine Information   Set Machine Type, GS Mode, Touch sound, Sleep Mode, Safety Mode, Zero mileage.
                Maintenance           Set default language, Wi-Fi, Ethernet, Bluetooth, USB update, update OS.
                A / V Source Setup    Set audio/visual source.




                                                                                                                       29

Engineering Mode
  1.   Units (Choice KM or Mile).
  2.   Beep Mode (Turn off beep of button, no beeping sound is heard).
  3.   Sleep Mode (The default OFF. When set ON, the electronic watch will go to sleep without any operation within 30 minutes. Press any key to wake up).
  4.   Pause Mode (Turn on allow 5 minutes of pause, turn off to have the console pause indefinitely).




                                                                                                                                                             30

<!-- PAGE 31: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-31.png` before citing anything from this page. -->

Security
Set Lock Accumulate mileage :
1. Seta four-digit number password and the number of kilometers you want to lock.
2. | Canuse the set password to unlock or use the password 2222 to unlock.

Security                                                             Se

Lock Mode                                      Set Lock Password to Activate
©            ON            oO

Set Lock Accumulate Mileage                      Confirm Set Lock Password to Activate

©           100           Db)

<!-- PAGE 32: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-32.png` before citing anything from this page. -->

Diagnostics
Recorder the error code on machine during running.

Error Code Log

0x0021           Treadmill-> Motor Error

0x0021           Treadmill-> Motor Error

0x0021           Treadmill-> Motor Error

<!-- PAGE 33: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-33.png` before citing anything from this page. -->

Machine Information
1. Machine Type (Choice exercise equipment, this machine is CE800).
2. RPM Detection (Turns off the speaker so no beeping sound is heard).
3. Safety Lock : The default is OFF. (For EMS system)
4. Zeroing : Click on this key to clear all odometer.

Machine Information

Machine Type                                 Distance :         11.61 km

CE800          Db)

Hour :              1.16 hr
RPM Detection

ON                bs)                                                     Zeroing

Safety Lock
OFF

°                               SW Version :       T29_ 20200312

FW Version:      V1.0

OS Version :      V1.0

<!-- PAGE 34: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-34.png` before citing anything from this page. -->

Maintenance
Set default Language, Wi-Fi or Ethernet, enable Bluetooth function, Update APP (USB of manual update), Update OS (reserved), Update APPS (internet
function of APPs)

Maintenance

Default Language Setup

WiFi Setup
Etherent Setup

BT Setup

Update App(USB)

Update OS

System & Apps

A/V Source Setup
  1. C-Safe protocol. (HDMI transfer to screen on TV of Entertainment function).
  2. CAB protocol (connect a set-box transfer to screen on TV of Entertainment function).




                                                                                            35

8. Disassembling and
     Assembling



                       36

8-1 Console Replacement
Step 1: Use a screwdriver to remove 4 bolts (M5*10mm), then unplug the control wire and Handpulse wires then take off the console.




Step 2: To reassemble the console do the reverse of step 1.


8-2 Swing Arm Replacement
Step 1:   Use a screwdriver to remove 3 screws (3.5*12mm) of handle bar cover then remove the covers.




                                                                                                                                     37

Step 2: Use a 14mm open-end wrench to remove the hex head bolt(3/8”*15mm) and flat washer (3/8”*30*2.0T).




Step 3: Use a screwdriver to remove the connecting arm cover (A) and (B).




Step 4: Use a 17mm open-end wrench and 12mm L- Allen wrench to remove the bolt of rod end bearing.




                                                                                                            38

8-3 Connecting Arm Replacement
 Step 1: Follow the step of 10-2 to unmount the connecting arm from the swing arm.
 Step 2: Use the screwdriver to remove the screw(M6*15mm) of the pedal arm cover then remove it.




 Step 3: Use an L-Allen wrench to remove the bolt(5/16”*3/4” hex head) and flat washer(5/16”*35*1.5T), then unmount the pedal arm and the connecting arm.




                                                                                                                                                            39

Step 4: Use a 12mm open-end wrench to remove the hex head bolt(5/16”*15mm) and flat washer(5/16”*23*15T). Remove the carriage bolt then disassembly the
connecting arm from the pedal arm.




Step 5: Use a screwdriver to remove 4 screws(M5*10mm) from the pedal then remove it.




                                                                                                                                                     40

Step 6: Before unmount the slide wheels, use a screwdriver to remove 2 screws (M5*15mm) of the slide wheel cover.




Step 7: Use a circlip plier to remove the circlip Ø 17 then remove the slide wheel.




                                                                                                                    41

Step 8: To do the reverse of the above steps, and add 3 wave washers (Ø 17) to the slide wheel axle showing below fig.




                                                                                                                         42

8-4 Console Mast Replacement
 Step 1: Follow the steps of 10-2 to remove the swing arm.
 Step 2: Remove the wave washer(ψ25) from both left and right side axle then use a screwdriver to remove 4 screws(3.5*12mm) of the console mast covers(L) & (R)
 and remove them.




 Step 3: Use an L-Allen wrench to loose 3 bolts(M8*25mm) of the console mast then remove the last bolt(M8*25mm) which a flat washer(5/16”*23*1.5T) with.
 Push the console mast to the front of the machine and unmount it from the mainframe then remove the control cable.




                                                                                                                                                           43

Step 4: Remove the roundcap first then use a screwdriver to remove 2 tapping Screws (ψ3x20mm) of the handpulse then pull out the handpulse wire from the
tube then remove the handpulse assembly.




Step 5: To do the reverse of the above steps to reassembly console mast.




                                                                                                                                                           44

8-5 Chain Cover Replacement
 Step 1: Follow the steps of “swing arm replacement” and “connecting arm replacement” to remove swing arm and connecting arm.
 Step 2: Use a screwdriver to remove 7 screws(4*19mm sheet metal screw) and 3 screws(5*16mm Tapping Screw) , then remove the right chain cover.




 Step 3: Remove the screw(4*16mm sheet metal screw) and flat washer(ψ5/16"*ψ23*1.5T) which lock the left chain cover on the mainframe and remove 3
 screws(5*16mm Tapping Screw), then remove the left chain cover.




                                                                                                                                                     45

Step 4: To do the reverse of the above steps to reassemble the chain cover. (Remember to add the flat washer inside the left chain cover)




                                                                                                                                            46

8-6 Cross Bar Replacement
Step 1: Follow the steps of “Chain Cover replacement” to remove both of the chain cover.
Step 2: Remove the Round Disk Cover, then use a 6mm L-Allen wrench to remove the bolt(M8*40mm Socket Head Cap Bolt) which lock the cross bar on the axle.




Step 3: Use a 12mm open-end wrench to remove a bolt(5/16”*15mm hex head bolt) and a flat washer(5/16”*35*1.5T) then unmount the cross bar and the round disk.




                                                                                                                                                            47

Step 4: Use a screwdriver to remove 8 screws(5*16mm tapping screw) and 8 flat washers(1/4”*19mm) then disassemble the round disk from the cross bar.
Step 5: To do the reverse of the above steps to reassemble the round cover and cross bar.(note the direction of the woodruff key, the round head direct to the axle)




                                                                                                                                                                       48

8-7 Idler Wheel Assembly replacement
Step 1: Follow the steps of “Cross Bar replacement” to remove cross bar.
Step 2: Use a screwdriver to remove 3 screws(M6*15mm) then use 13mm open-end wrench to loose the nut(M8*9T) from “J bolt”. Unmount the belt from drive pulley
then remove 3 screws(M6*15mm) to remove idler wheel assembly.




Step 3: To do the reverse of the above steps to reassemble the idler wheel assembly. Adjust the nut which on the J bolt to adjust the tension of the belt to the right
value (About 185Khz~210Khz by using sonic belt tension meter)




                                                                                                                                                                   49

8-8 Flywheel & Poly-V Belt replacement
Step 1: Follow the steps of “Idler Wheel Assembly replacement” to remove idler wheel assembly.
Step 2: Use an 11mm open-end wrench to remove flywheel 4 locking bolts(1/4”*3/4” hex head bolt), 4 flat washers(1/4”*19), and 4 spring washers(1/4”). Unplug the
power cable then remove the flywheel.




Step 3: To do the reverse of above steps to reassemble the flywheel and other parts.




                                                                                                                                                             50

8-9 Rear Rail Assembly replacement
Step 1: Use an L-Allen wrench to remove the bolts, flat washers, and spring washers which locking the rail support assembly.




Step 2: Use a screwdriver to remove the rear stabilizer cover (A) & (B).




                                                                                                                               51

Step 3: Use a 6mm L-Allen wrench to remove all the bolts, flat washers, curve washers which locking the rear rail assembly.




Step 4: To do the reverse of the above steps to reassemble the rear rail assembly.




                                                                                                                              52

8-10 Aluminum Track replacement
Step 1: Remove the rear stabilizer cover (A) & (B).
Step 2: Use a 12mm open-end wrench to remove 3 bolts (5/16”*3/4” hex head bolt) then remove the aluminum track.




Step 3: To do the reverse of the above steps to reassemble.




                                                                                                                  53