<!-- Source: CU900ENT Service Manual.pdf. Text is `pdftotext -layout` per page. -->
<!-- Pages that are flattened images, OCR'd and NOT reliable: 6, 16, 20, 24, 26, 27, 28, 30, 33, 36. Page images are at `raw/page-NN.png` (300 dpi, gitignored). -->

    CU900 ENT
    Service Manual




1                    Service Manual

1. CU900 ENT Outlines
2. Electronic Parts
3. Electrical Configurations
4. CU900 ENT Product Operation
5. CU900 ENT Unit Block Diagrams
6. CU900 ENT Basic Connections and Wiring
7. CU900 ENT Error Messages /Troubleshooting
8. Disassembling and Assembling
       1. Serial Number Location
       2. Component Description
       3. Preventative Maintenance
          3-1 Check for Pedals
          3-2 Check for Console Mast
       4.   Console Setting
          4-1. Basic Functions
          4-2. Engineering Model
       5.   Troubleshooting (Electronic)
       6.   Part Replacement Guide
          6-1 Console Replacement
          6-2 Armrest Group Replacement
          6-3 Pedal/Crank Arm Replacement
          6-4 Left and Right Trim Cover Replacement
          6-5 Left and Right Chain Cover Replacement
          6-6 Front and Rear Trim Cover Replacement
          6-7 Drive System Replacement
          6-8 Chair Cushions Cover、Seat Button Replacement
          6-9 Lift Arm Group Replacement
                                2                            Service Manual

     6-10 Down Control Replacement
     6-11 Rear Horizontal Tube Replacement
     6-12 Foot Pad/Moving Wheel Replacement
7.     Troubleshooting
     7-1 Belt Slips/Falls off
     7-2 Noise and Feet Feeling
     7-3 Shaking




                         3                    Service Manual

1. CU900 ENT Outlines




          4             Service Manual

  Seat Handle Bar         Console Assembly


Handpulse W/Cable
         Assembly
                          Console Mast


              Seat        Beverage Holder




                          Console Mast Cover

             Pedal


        Side Case
                          Transportation
                          Wheel


    Rear Stabilizer




                      5                      Service Manual

<!-- PAGE 6: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-06.png` before citing anything from this page. -->

> Seat Handle Bar (R)

Seat Handle Bar (L) <

\                                               > Seat

Console Mast <«

> Pedal
Main Frame <——————
Idler Bracket <————                        ——» Rail Assembly
Induction Brake <———                      f  A
.    RS             > Crank Arm
Pedal               ()   S
G)         C)

3         -———» Rear Stabilizer

@

ts)

6                                                                                   Service Manual

2. Electronic Parts




         7            Service Manual

Upper Controllers




                        Cooling FAN




                                      DISPLAY




                    8                           Service Manual

Lower Controller and Driver




                                  HYBRID GENERATOR
             SPEED SENSOR




                                    Driver board




                              9                    Service Manual

3.Electrical Configurations




             10               Service Manual

CONSOLE:
 Interface that controls all functions of the Elliptical.

MAIN CONTROLLER:
 The circuit board consist of the DC power supply for console.

EMS FLYWHEEL :
 It can change to increase or decrease resistance level of brake.

GENERAL INFORMATION

CONSOLE
Contains Key controls and TFT Display.
Main controller include power supply 、driver control circuit.




                                                                    11   Service Manual

4. CU900 ENT Product Operation




              12                 Service Manual

Display Windows


                       10.1” TFT Display




                  13                 Service Manual

Function Locations




                     14   Service Manual

5. CU900 ENT Unit Block Diagrams




               15              Service Manual

<!-- PAGE 16: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-16.png` before citing anything from this page. -->

Elliptical Configuration

HR              KEY          WIRELESS HR
HANDLEBAR                                                RECEIVER

Y    v    ‘

COOLING                          DISPLAY CONSOLE
FAN

RPM

SENSOR

BRAKE
DRIVER BOARD             id    FLYWHEEL

Dc           ;

POWER

16                                                                                  Service Manual

6. CU900 ENT Basic Connections and Wiring




                    17                Service Manual

I/O Board Bottom
                                     Internet
                                     CONNECT



                                                 GROUND




                     Console Power
                     CONNECT
                                                 HDMI CONTACT




                                                 SYSTEM CABLE
                      Right Hand                 CONNECT (8 PINS)
                      Pulse Wire


                      Left Hand
                      Pulse Wire


                                                 C-safe CONNECT




                   TV CONNECT



                                            18                      Service Manual

Driver Board PCB Component Locations




                                       19   Service Manual

<!-- PAGE 20: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-20.png` before citing anything from this page. -->

Driver Board function

RPM        CONSOLE             BRAKE
SENSOR             POWER                       FLIWHEEL
OUTPUT
INPUT        OUTPUT

i%   0 3a  :                    -                :             >       -   -    ~  .
*       ——          eS Hs                        2                       -                      =
       A he             er) 4    —_—  — ae                 ein
TEV 22 oy inix6-R10-LL0 BOARD REN bas     nore

WIRE

0                                                                                  Service Manual

7. CU900 ENT Error Messages /
       Troubleshooting




              21                Service Manual

Error Code Messages：

 Error   Description                  Remarks Error
 Code
  40H    Un-know mode                 By MCU Board Error
  41H    Inverter no-response         By MCU Board Error
  42H    Bike board no-response       By MCU Board Error
  44H    Console I2CNo-response       By MCU Board Error
  50H    Abnormal Update MCU FW       By MCU Board Error
 EAH     UCB Is Not Math LCB Device   GUI Error
 ECH     UCB To LCB Is No Response    GUI Error
 EDH     LCB Unknown Device           GUI Error




                                                           22   Service Manual

   Error code items：


                    Error Message             Explain
                    EEPROM ERR                EEPROM failure




   Prepare：


                                    Picture                    Tool name




                                                               Multi-meter




                                                        23                   Service Manual

<!-- PAGE 24: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-24.png` before citing anything from this page. -->

(CU900-ENT)
UPRIGHT CIRCUIT DIAGRAM

—
—
a)
Oo
a)
CSAFE HDMI         A——       =
BNC RJ45        KC     HW
Combo Board      LN LL QL)     :
$ |)
x || 2
FLYWHEET                 HW  O
a || oi
=|\=
O  O
O  oO
Z||<
o]}o
0  oD

BRAKE ECT &

8 PIN COMPUTER CABLE

SPEED SENSOR
AC ACAPTER                                                               0      O                           oO   o—
FSP100-RTAAN2                                                                    CN4 CNB                            CN3
DYA-W10A-IMX6-R10-LCD
INPUT : AG 100-240V                                                                                 BOARD
OUTPUT : DC 24V//4.17A                                                         cna                                   on?

[_] BRAKE                               oO

2 PIN RED WIRE BRAKE

:      i
LT} @

DC JACK

24                                                      Service Manual

               Setting and Operation for Engineering Mode
1. Operation for entering engineering mode:
   Press “Home” button 10 consecutive repetitions to enter engineering mode.




2. Instructions for each item of operation in engineering mode:
   After entering engineering mode, first priority is to enter “Machine Information” mode to set the type of
   the machine. There are three modes: Treadmill/ Elliptical/ Bike. Please select for the machine. The
   selection must match the actual machine otherwise it will be unable to operate the machine properly.




             There are three modes for the Machine Type Treadmill/ Elliptical/ Bike. Please select for the
             machine. The selection must match the actual machine otherwise it will be unable to operate
             the machine properly.

             GS MODE is a setting function for treadmill mode only:
             GS MODE ON is a function mode that the incline won’t resume. GS MODE OFF is a function
             mode that the incline will resume. (Under Elliptical / Bike mode, please set it OFF)

             To set child lock function. When it is set ON, the display and buttons lock and are unable to
             use.
             To unlock, press and hold “UP” button for 3 seconds till OFF and children are able to use.
             This is an unlock function once only.

                                                   25                                      Service Manual

<!-- PAGE 26: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-26.png` before citing anything from this page. -->

SPEAKER

<4 ON OP

SPEAKER volume control, ON for display / OFF for hide (Speaker is optional)

DISTANCE/HOUR      DISTANCE/ HOUR Instruction for resetting DISTANCE/ HOUR:
(     a         Under Machine Information, press and hold “UP” button for 3 seconds to clear
DISTANCE/ HOUR.

SW VERSION

are: ree  SW VERSION.

‘ore UNI VERSION.

FW VERSION

nT  FW VERSION.

OS VERSION

(   801-105271750      OS VERSION.

Update Manager.

Engineering Mode

Settings
Engineering Mode

Engineering Mode

security
Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

BEEP MODE

ON/ OFF for beep sound mode

< ON
nals       ON/OFF for sleep mode. The display always lights when turns off. When there is no action
4 OFF OP

for 30 minutes after turning on the power, it enters sleep mode.

UNITS

own   English/Metric mode switching

26                                                      Service Manual

<!-- PAGE 27: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-27.png` before citing anything from this page. -->

Settings
Engineering Mode

Security

Security
Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

Enter

OC MODE        To set distance locking function, when the distance reaches the setting value, the display and
er ©   buttons lock and are unable to use.
To unlock, press and hold “UP” button for 3 seconds. This is an unlock function once only.
(If password forgets, use default password 2222 to unlock the DISTANCE)

SET LOCK ACCUMULATE MILEAGE

<         ‘mm lo set the value of DISTANCE (100 ~ 9999 Miles)

SET LOCK P,

om           To set the password to unlock DISTANCE.

Diagnostics

Settings                                                                       Error Code Log

Engineering Mode

Security
Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

Diagnose and save malfunction error messages for technician to inspect the machine and
troubleshooting.
Press “Error Code Log” button 10 consecutive repetitions to clear the error message.

Error Code Log
Error Code Log

Error Code Log

27                                                      Service Manual

<!-- PAGE 28: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-28.png` before citing anything from this page. -->

Maintenance

Settings
Engineering Mode

Maintenance

Default Language Setup

Security
Software Update Manager

Internet Manager
WiFi/Ethernet Setup
Machine Setup
FTP Settings

Diagnostics
Machine Information
Maintenance
TV Setup
BT Setup

To set default language for the first page window. There are 12 languages in the

Default Language Setup jiments

Default Language Setup

Deutsch

Francais

Portugués
ety 0}

Software Update Manager

Software Update Manager

Update OS
Update App
Update Firmware
Update App Manager
Update Bike Firmware

First, add a new folder to the USB Transcend with file name “Dyaco” and transit each software
item to be updated or video files from new webs to the folder. Then insert the USB Transcend
to USB slot on back of the console and turn on the power of the treadmill.

28                                                      Service Manual

Elliptical/Bike




  Elliptical/Bike updating procedure 1.




  When update is completed please turn off the
  Elliptical / Bike power to wait adapter to discharge
  for 3 seconds then resume the power and enter
  the first page for operation.




                                                         29   Service Manual

<!-- PAGE 30: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-30.png` before citing anything from this page. -->

Home

ro ow

=     Exercise
4        Programs

To begin workout press the START key on the keypad below. To view an
Exercise Program or change the Language, select either key above

Press “Home” button 10 continuous repetitions to
enter engineering mode then go to Elliptical / Bike
updating page to proceed program updating,

Updating procedure 2.   Update Firmware

Repeat previous step, turning off-on-first page-updating

Updating procedure 3.  Update App Manager

To update App manager.

App Update Manager
V1.2

Install APK

Uninstall APK

install APK        Please press Install APK button to proceed APK software updating.
install APK        Please press Install APK button to proceed APK software updating.

30                                                      Service Manual

                   When updating is completed, press “Open” button to open APP software. When entering
                   the first page after completing updating, this product is able to operate.


Remark: If the image is shown after updating, then there is intermittence for the console during transmitting
so that the error message is shown.




To eliminate this, press              button 10 consecutive repetitions to enter the first page. Whatever error
 message is shown, this will eliminate it and enter the first page for operation.




There are 6 preset web pages such as Face Book / You Tube etc.




           Press You Tube button for 2 seconds and the web page is deleted.




                                                       31                                     Service Manual

Instruction for adding new webs



   First, add a new folder to the USB Transcend with file name “Dyaco” and transit each software
   item to be updated or video files from new webs to the folder. Then insert the USB Transcend
   to USB slot on back of the console and turn on the power of the treadmill.




            Enter the new website (like flipboard.com)


            Enter the new filename (like flipboard)


  The icon of new filename “flipboard” for the new website.



        Press Internet Manager button 10 consecutive repetitions to enter the preset adding
        website mode then hit “OK” button to complete adding the website.




                                           32                                  Service Manual

<!-- PAGE 33: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-33.png` before citing anything from this page. -->

WiFi/Ethernet Setup

WiFi/Ethernet Setup
WiFi
Ethernet

WIFI          Please hit WiFi button to proceed WiFi setting.

Wi-Fi Setting

On                        Scan                    Add Network
Disgusting                  Disable
DrayTek                   Disable

Macrokiosk-1                  Disable

Fth         There is instructions for network setting, please hit “Ethernet” button to enter setting
ernet     window.

Ethernet Configuration

Ethernet Configuration

Configure Ethernet devices

IP Address

192.168.192.28

MAC Address

00:18:70:91:48:7F

Ethernet Configuration           Please hit “Ethernet” to enter network setting mode.

Configure Ethernet devices

Ethernet Configuration

Network Setting

Ethernet Devices:                        IP address

Connection Type                      NetMask
* DHCP

Static IP                                    Gateway address

33                                                      Service Manual

DNS address

Under “Connection Type”, select “DHCP” button the network will automatically search for
the connection. Select “Static IP” for manual setting.


Press “Etherner Configuration” button 10 consecutive repetitions to enter Android setting
mode and hit “Date&Time” to select the area and time setting is completed.




   Please select the area.


                  Check for Automatic Date & Time to apply the time provided by the
                  web.
                  Please resume the treadmill power when complete.




Select “C-SAFE or CAB” button for TV switching box (Choose one is allowed only)


Brightness adjustment button




                                  34                                    Service Manual

FTP IP ADDRESS is set at 61.218.169.200.


FTP PORT is set at 21.


ACCOUNT is set to be dyaco_service(lower case only)


PASSEORD is set at 23751545.


                SERIAL NUMBER is treadmill serial number to feedback for Error Log, for
                example CR800-ENT(5638880810000001).


                PATH is Error Log for feedback customer name, for example
                dyaco_service/SPIRIT FITNESS




   To turn on or off Error Log feedback function and to set the feedback time.




Press “FTP Upload Test” button to upload information when finish. The green circle
represents upload completed while red circle is for error message or upload failed, please
verify for correct setting or network is not turned on. (When using Error Log feedback function,
be aware of if WiFi is connected.)




                                       35                                     Service Manual

<!-- PAGE 36: FLATTENED IMAGE. The text below is OCR and is incomplete, especially for labels printed over line art. Read `raw/page-36.png` before citing anything from this page. -->

TV Setup

TV Setup

OSD Menu.                Update Channel List

ae Saas       Please select the player source such as TV / HDMI mode.

(<4   Ty eS

OSD Menu

Hit “OSD Menu” button as main menu, and select AUTO/DTV/ATV Tuner then hit “OSD
Enter” button to proceed to next step.

OSD Enter      Hit “OSD Enter” button to select the country and use the arrow keys to choose. When
es finish, hit “OSD Enter’ button again to proceed with channel searching. Wait until search
ends.

Channel searching                    Arrow keys

3 °%...VHF CH     16
=
%\ MENU

TV Setup                                                                                                                TV Setup

OSD Menu                    Update Channel List

OSD Enter
mer

MER © Oo WAR
A

HUGRE DMS

sink ae 48
DIW/ATY      Hit i
(sai                       )

HAS (USB)

mean :  0 Fan
eM  > 0 WAR            <P>

x. VER CH

MENU

v

Scan channel is progressing.

Update channel list button .Please scan
OSD menu buttons                            p

channels first .

This button updates the channel list.

| Update Channel List

Mealelbietoialie       For HDMI function, please directly hit “HDMI” and connect the signal source to enjoy.

(<4   Ty eS

SSemeeaaeeem § | his button is for software R&D engineer only.

36                                                      Service Manual

                  Version for blue tooth module.


                  Hit “Clear” button, it clears all messages on the window.


                  Hit “Pair Mode” button, window displays “Enter pairing mode” and wait for blue tooth
                  connection.
                  Hit “Deleted Pair” button, window displays “OK” and disconnect blue tooth connection.


                  Hit “Reset” button, window displays “Bluetooth device is power on” and blue tooth to turn
                  on again.
                  Hit this button to modify the name of blue tooth connection. Press “Rename BT Device”
                  button to enter when complete.
                  This button enters the modified name for blue tooth


                  Button for headphone volume control


Instruction for blue tooth operation procedure:
1. Press “Pair Mode” button, the window shows “Enter pairing mode” and proceed to the next step.
2. Turn on the cell phone or ipad and searching device, the display shows “ENT console”. Hit for coding
   operation and both cell phone window and console display will start coding requisition. When both are hit
   to confirm, the coding completes and function of blue tooth operation is available.




                                                     37                                    Service Manual

GENERAL MAINTENANCE
1. Wipe down all areas in the sweat path with a damp cloth after each workout.
2. If a squeak, thump, clicking or rough feeling develops the main cause is most likely one of two reasons:
         1) The hardware was not sufficiently tightened during assembly. All bolts that were installed during
            assembly need to be tightened as much as possible. It may be necessary to use a larger
            wrench than the one provided if you cannot tighten the bolts sufficiently. I cannot stress this
            point enough; 90% of calls to the service department for noise issues can be traced to loose
            hardware.
         2) The crank arm nut and/or the pedals need to be retightened.
3. If squeaks or other noises persist, check that the unit is properly leveled. There are 2 leveling pads on the
   bottom of the rear stabilizer, use a 14mm wrench (or adjustable wrench) to adjust the levelers.



WARNING
The effect that the safety level of the equipment can be maintained only if it is examined regularly for
damage and wear.
         1) Replace defective components immediately and/or keep the equipment out of use until repair.
         2) The components which are most susceptible to wear: Belt、PU wheel、Bearing、Idler.




                                                       38                                     Service Manual

Troubleshooting procedure matrix

                    Condition                                      Reason                                           Solve
TFT not bright, incomplete or imperfect.         1. TFT light is broken.                   1. Replace with new TFT or console.
                                                 2. Power to console too low.              2. Check power to console.
                                                                                           3. Replace lower controller.
TFT displays not bright, incomplete or imperfect. 1. TFT displays are broken.              1. Replace with new console.
Erratic pulse display.                            1. Another chest belt in use around      1. Check for other chest belt use around product.
                                                     product.                              2. Change the position or direction of product.
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
(No pulse displayed on monitor)                                                               oriented correctly.
                                                  2. Distance is too far and exceeds range 2. User chest belt in front of console within 3 feet.
                                                  of receiver.                             3. Replace with new lithium battery type is CR2032.

                                                 3. Chest belt battery is weak or dead.
Chest belt too close to the product.             Weak battery.                             Replace with new lithium battery with type CR2032.




                                                                          39                                                          Service Manual

8. Disassembling and Assembling




               40            Service Manual

1. Serial Number Location




                            41   Service Manual

 2. Component Description

Part Number     Part Description
      1        Console Assembly
    2          Console Assembly
    3          reading race holder
    4              cooling fan
    5               End Cap
    6             Side Case (L)
    7            Sider Case (R)
    8         Front Stabilizer Cover
    9         Rear Stabilizer Cover
    10             Rear Cover
    11               Cap
    12          Console Mast
                   Cover-L
    13          Console Mast
                   Cover-R
    14        Console Mast Cover
    15         Electronic Module
    16         Beverage Holder
    17         Front Seat Cover
    18          Rear Seat Cover
    19               Pedal
    20           Release Lever




                                       42   Service Manual

3. Preventative Maintenance
   3.1 Check for Pedals
   As shown in Figure 3.1.1, 3.1.2, check regularly whether the pedal is loose, lock the left pedal
   counterclockwise, and press the right pedal clockwise.




Figure 3.1.1                  Figure 3.1.2




                                              43                                               Service Manual

   3.2 Check for Console Mast
   As shown in Figure 3.2.1, check that the six screws on the riser are loose and lock if loose.
    (Vertical tube shaking problem excluded)




Figure 3.2.1

4. Console Setting

   4.1 Basic Functions

   4.2 Engineering Model

5. Troubleshooting (Electronic)




                                             44                                               Service Manual

6. Part Replacement Guide
   6.1 Console Replacement
       6.1.1 As shown in Figure 6.1.1, remove the 2 screws of the chin cover and remove it.




Figure 6.1.1




                                            45                                                Service Manual

       6.1.2 As shown in Figure 6.1.2 and Figure 6.1.3, remove the four screws from the rear of the
             electronic watch and remove the wire connector to remove the electronic watch.




Figure 6.1.2               Figure 6.1.3

       6.1.3 Electronic table assembly in accordance with 6.1.1 and 6.1.2, you can replace.




                                             46                                               Service Manual

   6.2 Armrest Group Replacement

       6.2.1 Refer to Figure 6.1.1 for the removal of the chin cover. As shown in Figure 6.2.1, remove the
             M8 cap and remove the armrest to remove the armrest group (need to hold the armrest to
             avoid danger).




Figure 6.2.1                        Figure 6.2.1

       6.2.2 Please refer to 6.2.1 for armrest assembly.




                                              47                                              Service Manual

   6.3 Pedal/Crank Arm Replacement

       6.3.1 As shown in Figure 6.3.1, 6.3.2, remove the right pedal counterclockwise and remove the left
             pedal clockwise.




Figure 6.3.1            Figure 6.3.2               Figure 6.3.3             Figure 6.3.4

       6.3.2 Remove the crank screw as shown in Figure 6.3.3. (About the same, please use 60 N-m when
             locking)

       6.3.3 As shown in Figure 6.3.4, use the puller to exit the crank. (Left and right sides are the same.)

       6.3.4 Please refer to 6.3.1 ~ 6.3.3 for crank and pedal assembly.




                                              48                                                Service Manual

   6.4 Left and Right Trim Cover Replacement

       6.4.1 As shown in Figure 6.4.1, Figure 6.4.2, remove the four self-tapping screws from the left-hand
             cover to remove the left and right standings.




Figure 6.4.1                        Figure 6.4.2




                                             49                                              Service Manual

   6.5 Left and Right Chain Cover Replacement

       6.5.1 Loose seat riser cover 3 screws as shown in Figure 6.5.1, Figure 6.5.2.




Figure 6.5.1               Figure 6.5.2




                                             50                                        Service Manual

       6.5.2 Figure 6.5.3, Figure 6.5.4, Figure 6.5.5, the left chain cover 7 self-tapping screws, 3 screws
             removed, you can remove the left chain cover; the right chain cover 3 screws removed, you
             can remove Right chain cover. (Please refer to 6.3 for removing crank.)




Figure 6.5.3                         Figure 6.5.4                           Figure 6.5.5

       6.5.3 Please refer to 6.5.1, 6.5.2 for the left and right chain cover assembly.




                                               51                                              Service Manual

   6.6 Front and Rear Trim Cover Replacement

       6.6.1 As shown in Figure 6.6.1, Figure 6.6.2, remove the two screws from the front and rear trims
             and remove them.




Figure 6.6.1                        Figure 6.6.2

       6.6.2 Before and after the decoration cover please refer to 6.6.1 can.




                                             52                                              Service Manual

   6.7 Drive System Replacement

       6.7.1 Remove the crank, left and right riser chain cover and left and right chain cover Please refer
             to 6.3, 6.4, 6.5, as shown in Figure 6.7.1, Figure 6.7.2, remove the nut and hook screw, you can
             remove the spring.




Figure 6.7.1                        Figure 6.7.2

       6.7.2 Draw the belt as shown in Figure 6.7.3, Figure 6.7.4. (The belt is maintained in the middle of
             the belt during installation, the belt tension is maintained at 180 to 210 N)




Figure 6.7.3                        Figure 6.7.4

                                              53                                               Service Manual

       6.7.3 As shown in Figure 6.7.5, loosen the three screws and remove the idler. (The need to install
             the idler counterclockwise to the end of the lock)




Figure 6.7.5

       6.7.4 As shown in Figure 6.7.6, 6.7.7, the flywheel 4 screws can be removed to remove the flywheel.




Figure 6.7.6                        Figure 6.7.7




                                             54                                              Service Manual

       6.7.5 As shown in Figure 6.7.8, loosen the five-way nut and remove the five-way turntable. (Need to
             align the keyway in the installation, the five-nut on the lock.)




Figure 6.7.8

       6.7.6 As shown in Figure 6.7.9, loosen the reed switch screw and remove it. (Installation with the
             belt on the magnet with a distance of 1mm)




Figure 6.7.9

       6.7.7 Please refer to 6.7.1 ~ 6.7.6 for the installation of transmission system parts.


                                              55                                                Service Manual

   6.8 Chair Cushions Cover、Seat Button Replacement

       6.8.1 As shown in Figure 6.8.1, Figure 6.8.2, remove the 2 screws from the front and rear seats.




Figure 6.8.1                        Figure 6.8.2

       6.8.2 As shown in Figure 6.8.3, Figure 6.8.4, remove the four screws and remove the cushion.




Figure 6.8.3                        Figure 6.8.4

       6.8.3 Please refer to 6.8.2 for the cushion assembly.

       6.8.4 Please refer to 6.8.1 for the front and rear seat cover assembly.
                                              56                                             Service Manual

   6.9 Lift Arm Group Replacement

       6.9.1 Set the seat adjustment group to the highest as shown in Figure 6.9.1.




Figure 6.9.1

       6.9.2 Remove the carriage cable as shown in Figure 6.9.2, 6.9.3, 6.9.4.




Figure 6.9.2                        Figure 6.9.3                         Figure 6.9.4
                                             57                                         Service Manual

       6.9.3 As shown in Figure 6.9.5 ~ 6.9.9 will be on the handle of the two screws, you can remove the
             cable, handle.




Figure 6.9.5                       Figure 6.9.6                        Figure 6.9.7




Figure 6.9.8                       Figure 6.9.9




                                            58                                              Service Manual

       6.9.4 As shown in Figure 6.9.10, 6.9.11, 6.9.12, 6.9.13 Remove the screw and nut from the lifting arm
             to remove the seat riser.




Figure 6.9.10                       Figure 6.9.11                         Figure 6.9.12




Figure 6.9.13




                                             59                                               Service Manual

       6.9.5 As shown in Figure 6.9.14, 6.1.15 remove the cap on the lift arm, you can remove the lift arm.




Figure 6.9.14                         Figure 6.9.15

       6.9.6 Install the seat riser group Refer to 6.9.1 ~ 6.9.5.




                                                60                                            Service Manual

   6.10   Down Control Replacement

       6.10.1 As shown in Figure 6.10.1, remove the four screws from the control panel and release the
             power to remove the replacement.




Figure 6.10.1




                                            61                                             Service Manual

   6.11    Rear Horizontal Tube Replacement

       6.11.1 As shown in Figure 6.11.1, 6.11.2, loosen the bottom 3 screws and remove it.




Figure 6.11.1                      Figure 6.11.2




                                            62                                               Service Manual

   6.12   Foot Pad/Moving Wheel Replacement

       6.12.1 As shown in Figure 6.12.1, loosen the screw and cap and remove the wheel.




Figure 6.12.1




                                           63                                             Service Manual

       6.12.2 As shown in Figure 6.12.2, move the wheel counterclockwise. (Adjust the height of the four
             feet when not flat until the balance)




Figure 6.12.2




                                            64                                             Service Manual

7. Troubleshooting

   7.1 Belt Slips/Falls off

       7.1.1 If you find the belt slip and off the phenomenon, please refer to 6.5, 6.7.1, 6.7.2, 6.7.3, the nut
             can be adjusted to adjust the tension.




                                               65                                                 Service Manual

7.2 Noise and Feet Feeling

   7.2.1 In the course of the use of reversing trample to hear the sound generated by the flywheel, this
         is a normal phenomenon.

   7.2.2 If you find a foot feeling in the process, please refer to 3.1 to lock the pedal, if the foot
         phenomenon still exists, please refer to 6.3 check whether the crank is loose.




                                            66                                                  Service Manual

7.3 Shaking

   7.3.1 If you find the front armrest during use, please refer to 6.2 to lock the screw.




   7.3.2 If you find serious seat back and forth during treading, refer to 6.8 to lock the seat connection
         screw.




                                          67                                                Service Manual

7.3.3 If the whole product is shaking during use, please refer to 6.12.2 to adjust the height of the
      mat.




                                       68                                                Service Manual