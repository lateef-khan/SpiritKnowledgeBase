<!-- Source: 8.5S-785545 _MS2000-SB036-01_Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

8.5S-785545
(MS2000-SB036-01)
Service Manual
-------------------------Table of Contents-------------------------------
        1. Serial Number Location
        2. Component Description
        3. Preventative Maintenance
        3-1 Check the Pedal
        3-2 Check the Handlebar
        4.Setting of Electronic Console
        4-1 Basic Functions
        4-2 Maintenance Mode
        4-3 Electrical Wiring Diagram
        4-4 Circuit Board
        4-5 List of Required Maintenance Tools
        5.Troubleshooting (Electronic)
        5-1 No power, Console doesn’t light
        5-2 UART Communication Error
        5-3 No Revolutions
        6.Part Replacement Guide
        6-1 Console Replacement
        6-2 Handlebar Replacement
        6-3 Pedal Replacement
        6-4 Back Cover, Front Cover, Chain Cover (L, R) Replacement
        6-5 Steel Cable Replacement
        6-6 Lower Linkage Replacement
        6-7 Linear Slider Replacement
        6-8 Steel Cable Slide Wheel Replacement
        6-9 Drive Belt Replacement
        6-10Flywheel Replacement
        6-11Foot Pad, Transportation Wheel Replacement
        7.Troubleshooting
        7-1 Belt Slip
        7-2 Handlebar Wobble
7-3 O-ring Broken
7-4 Optical Sensor Board no respond
1. Serial Number Location
2. Component Description

                                                               1
                                                 5
 Item     Description
 01       Console Assembly
                                                                   7
                                                                        6        12
 02       Chain Cover (R)
 03       Chain Cover (L)
                                        4
 04       Console Mast(Upper)
 05       Rotating Structure Assembly                              10
                                        8                                             13
 06
 07
          Handle Bar (R)
          Handle Bar (L)
                                                          11
                                                                   0
                                                                   3
 08       Front Cover
                                        2                                             16
 09       Back Cover
 10       Circular Ring
 11       Pedal
 12       Seat Back
 13       Seat
                                            9                                    14
 14       Seat Rotation Release Lever
                                                15
 15       Seat Release Lever
 16       Adjusting Rod
                                                     17                               19
 17       Seat Carriage
 18       Bottom Plate                                                      18
 19       Seat Front Rear Adjusting
3. Preventative Maintenance

3-1 Check the Pedal
1. As shown in Figure 3.1.1, check whether the pedals are loose.




         Figure 3.1.1
3-2 Check the Handlebar
1. As shown in Figure 3.2.1, Check whether the left and right handlebars are loose or wobbling.




               Figure 3.2.1
4. Setting of Electronic Console

4-1 Basic Functions

1. Refer to the User’s Manual for detailed console operations.

4-2 Maintenance Mode

Maintenance Mode is intended for troubleshooting purposes.
To enter Maintenance Mode, tap the Wi-Fi icon once and the clock in the status bar six times on the Home Screen.
4.2.1 Maintenance Mode Menu Structure


                                 Odometer
                                                                           Android Version
                                                                           Firmware Version
                                 Software
                                                                           LCB Version
                                                                           Console APP Version
                                                                                                  Treadmill
                                                                                                  Upright Bike
                                                                                                  Recumbent Bike
                                                                           Machine Type           Recumbent Stepper
                                                                                                  UBE
                                                                                                  Rehab UBE
                                                                           Communication
                                                                           NFC Sensor
                                                                                                  Resistance Increase
                                                                                                  Resistance Decrease
                                                                           Keypad Test            Start/Stop
                                                                                                  Enter
                                 Service                                   Error Log
                                                                                                  White Color
                                                                                                  Blue Color
                                                                                                  Green Color
                                                                           Beacon Test
                                                                                                  Yellow Color
                                                                                                  Red Color
                                                                                                  Crank Index Magnet Sensor
                                                                           Crank Sensors
                                                                                                  Crank RPM Angle Sensor
                                                                           Crank Calibration
                                 Lock Facility Program: ON/OFF Setting


 * The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
4.2.2 Maintenance Mode – Item Descriptions
4.2.2.1 Odometer – Indicates the total belt operation time and accumulated running distance.
4.2.2.2 Software – Displays current software versions and allows updates on this page
       Firmware and LCB* Update Procedure
       (Note: Please keep the machine powered on during the update process.)
       Step 1. Place the following three files —CS51009-01.bin, CS31003.bin, and update.json — in the root directory of a USB drive.




       Step 2. Insert the USB drive into the USB port located on the back of the console.




       Step 3. On this page, press the Update button under both the Firmware and LCB* sections.
       The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
Console APP Update Options
(Note: Please keep the machine powered on during the update process.)
This system provides two methods for updating the Console APP. Either method may be used:
Method 1: Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the Firmware and LCB* update
procedure above.
Method 2:
Step 1. In Settings, connect the machine to a Wi-Fi network.
Step 2. Return to this page. The system will automatically detect if a new version is available.
Step 3. Press the Update APK button under the Console APP section.




* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
4.2.2.3 Service
        4.2.2.3.1 Machine Type – This series of six models shares the same app. You can switch the machine type on this page.
       4.2.2.3.2 Communication Test – Provides a built-in hardware loop test function.
                Step 1. Prepare a 1-meter USB-A (male) to USB-B (male) cable.
                Step 2. Insert the USB-A end into the USB-A port on the back of the console, and the USB-B end into the USB-B port located at the data output
       interface beneath the machine.
                Step 3. Prepare a 5 cm single-core wire. Strip the PVC insulation from both ends, then insert the wire into pin 2 and pin 3 of the DB9 connector at the
       data output interface beneath the machine.
                Step 4. On this page, press the Start button. The system will automatically check the status of the hardware loop.
       Note: The maintenance video demonstrates the actual operation process.
       4.2.2.3.3 NFC Sensor Test – Place the NFC tag near the bottom-right corner of the console. Each detection cycle takes three seconds. If the tag is not detected,
       remove it for three seconds and try again.
       4.2.2.3.4 Keypad Test – Press the physical buttons on the console to verify their functionality.
       4.2.2.3.6 Error Log – Displays the history of system errors.
       4.2.2.3.6 Beacon Test – Switch the beacon light bar colors to verify functionality.
       4.2.2.3.7 Crank Sensors – Displays the rotational speed.
       4.2.2.3.8 Crank Calibration – Put the right crank at a 6 o’clock position, then press the button below to run the test.
4.2.2.4 Lock Facility Program – When set to ON, the speed and incline profiles of the Facility program cannot be modified.
4-3 Electrical Wiring Diagram
       4-4 Circuit Board

4.4.1 Lower Control Board (#105)
     Power Supply #081 provides 24 VDC to the LCB. The board converts it to 12 VDC for the console and supplies power to the angle and magnet sensors.
     Sensor readings are used to control resistance on Brake #086.
4.4.2 Power Supply Module (097)
     AC power is converted to 24VDC to provide DC voltage for the entire system.
4-5 List of Required Maintenance Tools
  No.    Tool Name
  1      Multimeter
  2      Cordless Impact Driver Set
  3      Phillips Screwdriver
  4      Diagonal Cutting Pliers
  5      Needle-nose Pliers
  6      Electric Soldering Iron
  7      Solder Wire
  8      Anti-static Tweezers
  9      Heat Shrink Tubing
  10     Utility Knife
  11     Hex Key Set (Allen Wrench Set)
  12     Socket Wrench Set
  13     Cable Ties (Minimum Length: 20 cm)
  14     Electrical Insulation Tape
  15     Lead Wire (for guiding cable through tubing)
  16     Insulated Gloves
  17     Anti-static Wrist Strap
  18     Crank Removal Tool
5. Troubleshooting (Electronic)

   5-1 No power, console doesn’t light
      Step 1. Press any physical button on the console (see Figure 3) to wake up the system. If the system does not respond, proceed to the next step.
      Step 2. Measure the AC input voltage at the cable connected to the CN1 housing on the power supply module (see Figure 4).
      If no AC voltage is measured or the voltage is incorrect, check whether the power switch is turned on and the fuse is not blown (see Figure 5).
      Then, measure the mains voltage (see Figure 6) and the voltage at the machine-side end of the power cable (see Figure 7).
      If correct AC voltage is present at CN1, proceed to the next step.




      Figure 3                         Figure 4                                  Figure 5                                        Figure 6




    Figure 7
Step 3. Check the status of power indicator light D5 on the LCB (refer to the Circuit Board section). If the light is off, proceed to the next step. If the light is on,
skip ahead to Step 5.
Step 4. Measure pins 1 and 4 of connector CN100 on the power supply module to verify the presence of 24 VDC (see Figure 8). If 24 VDC is not measured,
replace the power supply module. If 24 VDC is measured, replace the LCB.
Step 5. Measure pins 1 and 2 on the J3 cable at the rear of the console to verify 12 VDC (see Figure 9). If no 12 VDC is measured, inspect the inline connector
cable (see Electrical Wiring Diagram section). If 12 VDC is measured, replace the console.




                                 Figure 8                                                           Figure 9
Check Procedure




                                                                                                                                                            (#097)




                                                                                                                                                        (#105)




                                                                                                                                               (#86)



Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description
5-2 UART Communication Error
Step 1. Check if cables #103 and #104 are properly connected (see Electrical Wiring Diagram section). If not connected, reconnect it or replace the cable if
faulty. If properly connected, proceed to the next step.
Step 2. Check if the software version shows V255A255. If it does, update the software (see Maintenance Mode section). If not, replace both the LCB and the
console.

Check Procedure




Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description.
5-3 No revolutions

Left/Right Step Graph Incorrect

1. Make sure all the cables in the back of console are plugged in properly.
2. Open the left shroud and make sure the cable is connected to the step sensor board properly.




3. Measure between pin 1 and pin 3 of the cable that connects to the step sensor board for 5V DC. If there is no 5V DC, check the connection of the cable or
   replace the cable. Go to next step if there is 5V DC.




4. Run the Sensor Test in Maintenance mode.
5. The SPM window should show ON when the reflector sensor #1 (bottom one) aligns to the silver surface. The CALORIES window should show ON when
   the reflector sensor #2 (top one) aligns to the silver surface. The step position counter of each foot (TIME and STEPS window) should show about 17
   (15~17) when you perform a full range step. If the value is incorrect, follow next step to adjust the sensor board.
6. Adjust the sensor to align with the center of the shaft as left picture. Make sure the surface of the sensor is parallel to the surface of the pulley and has a
   7~9mm gap between sensor and the reflective surface of the pulley. If the problem isn’t resolved replace the sensor board
7. Program Starts But No Data Registers When Stepper is Pedaled
8. Make sure all the cables in the back of console are plugged in properly.
9. Run the Sensor Test in Maintenance mode. Go to step iii if ANGLE didn't display correct RPM, go to step iv if REED didn't work properly.
10. Open the cover and measure the pin 2 and pin 9 at the cable that connect to the angle sensor for 5V DC. Check the magnet on the shaft of brake. The magnet
    should be in the center of the shaft and have 3mm gap between magnet and angle sensor. Replace the angle sensor if correct but there is no RPM.
6. Part Replacement Guide

6-1 Console Replacement
6-1-1 As shown in Figure 6.1.1, and 6.1.2, remove the 2 screws at the bottom of the rear tube cover, then take off the rear tube cover Figure 6.1.3.




      Figure 6.1.1                   Figure 6.1.2                    Figure 6.1.3

6-1-2 As shown in Figure 6.1.4,and 6.1.5, remove the 4screws underneath the console, then disconnect the wire connectors to remove the console.。




             Figure 6.1.4                                Figure 6.1.5

Install console in reverse order following Figures 6.1.1, 6.1.2, 6.1.3, 6.1.4, and 6.1.5.
6-2    Handlebar Replacement

1. As shown in Figure 6.2.1, remove the screws to replace the part.




                  Figure 6.2.1

2. Install Handlebar in reverse order following Figures 6.2.2, 6.2.3, 6.2.4, 6.2.5, 6.2.6, 6.2.7, and 6.2.8.




          Figure 6.2.2                          Figure 6.2.3                                       Figure 6.2.4
         Figure 6.2.5   Figure 6.2.6   Figure 6.2.7




Figure 6.2.8
6-3 Pedal Replacement

1. As shown in Figure 6.3.1,and 6.3.2，loosen the screw by turning it counterclockwise.




                  Figure 6.3.1                                Figure 6.3.2

2. Install pedal in reverse order following Figures 6.3.1, and 6.3.2.
6-4 Back Cover, Front Cover, Chain Cover (L, R) Replacement

1. Use a flat wrench and insert it into the latch shown in Fig. 6.4.1.
   Pry it upward from bottom to top to push the rear upper cover upward.
   Then follow Figs. 6.4.2 and 6.4.3 to remove the back cover.




                Figure 6.4.1                                     Figure 6.4.2   Figure 6.4.3
2. As shown in Figure 6.4.4，pull the front cover outward to remove it.




             Figure 6.4.4

2. As shown in Figure 6.4.5, loosen the screws on the Chain Covers (L and R).
   As shown in Figure 6.4.6 and Figure 6.4.7, first loosen the front and rear screws securing the left Chain Cover (L).
   Then pull the outer housing outward (Figure 6.4.8) to remove the left Chain Cover (L).




Figure 6.4.5                             Figure 6.4.6        Figure 6.4.7           Figure 6.4.8
4. Install Chain Cover (L, R) in reverse order following Figures 6.4.1, 6.4.2, 6.4.3, 6.4.4, 6.4.5, 6.4.6, 6.4.7, and 6.4.8.
6-5 Steel Cable Replacement

1. As shown in Figure 6.5.1，note the screw length, then remove the nut and bolt to detach the steel cable.




Figure 6.5.1

3. Adjust the tension of the front steel cable to match the screw length measured before disassembly. As shown in Figure, tighten the idle wheel screw.。
   As shown in Figure 6.5.5, adjust the nut to set the steel cable tension to 40–50 lb.




               Figure 6.5.4                        Figure 6.5.5
3. Figure 6.5.7,and 6.5.8,loosen the screw on the Slide Wheel (Urethane) to release the steel cable tension, then remove the steel cable end on the spring side.As
shown in Figure 6.5.9, and Figure 6.5.10, remove the bolt at the other end of the steel cable to detach the steel cable.




                 Figure 6.5.7                                     Figure 6.5.8                                Figure 6.5.9




               Figure 6.5.10
4. Install the lower steel cable.

STEP1
As shown in Figure 6.5.9, assemble the bolt, spring, and washer according to the order shown in the figure.。As shown in Figure 6.5.11, tighten the Pedal Plate
(R).




              Figure 6.5.11
As shown in Figure 6.5.12，assemble the bolt, spring, and washer according to the order shown in the figure.。As shown in Figure 6.5.12, tighten the Pedal
Plate (L).




            Figure 6.5.12
STEP2
As shown in Figure 6.5.13,route the steel cable around the installed Slide Wheel (Urethane) assembly.。As shown in Figure 6.5.1, move the right and left Pedal
Plates to the rearmost position.
                 Figure 6.5.13                                 Figure 6.5.14

STEP3
As shown in Figure 6.5.15, the steel cable should be routed from right to left.
Ensure that the cable is properly seated in the first groove of the cable pulley at the beginning.
As shown in Figure 6.5.16,and Figure 6.5.17 ,wrap it three times.。(Note that when installing the steel cable on the other side, it must also be routed starting
from the right side of the cable pulley.)




                 Figure 6.5.15                             Figure 6.5.16                                              Figure 6.5.17
STEP4
As shown in Figure 6.5.18, insert the steel cable end into the hook of the spring.
As shown in Figure 6.5.19, adjust the tension of the Slide Wheel (Urethane).
As shown in Figure 6.5.20, adjust the steel cable head so that the center-to-bolt distance is between 9 cm and 10 cm.




               Figure 6.5.18                                 Figure 6.5.19                                      Figure 6.5.20

6-6 Lower Linkage Replacement

1. As shown in Figure 6.6.1, and 6.6.2, loosen the screw to replace the lower linkage.




                 Figure 6.6.1                                 Figure 6.6.2
2. As shown in Figure 6.6.3, and 6.6.4, loosen the screw to replace Lower Linkage A.




                    Figure 6.6.3                               Figure 6.6.4

3. As shown in Figure 6.6.5、6.6.6,loosen the screw to replace Lower Linkage B.




                 Figure 6.6.5                                  Figure 6.6.6

4. Install Lower linkage ,lower linkage A, lower linkage B in reverse order following Figures 6.6.1,6.6.2,6.6.3,6.6.4,6.6.5,and 6.6.6.。
6-7 Linear Slider Replacement

1. Refer to 6-6 (Lower Linkage Replacement) to remove the linkage and refer to section 6-5 (Steel cable replacement) to remove the steel cable.
   As shown in Figure 6.7.1, remove the screws from the Rubber Cushion Bracket.
   As shown in Figure 6.7.2, loosen the two screws at the rear of the Seat Front/Rear Adjusting.
   As shown in Figure 6.7.3, loosen the four screws on the Pedal Plate.
   As shown in Figure 6.7.4, loosen the two screws located beneath the left and right Pedal Plates to replace the Seat Front/Rear Adjusting unit.




                  Figure 6.7.1                                       Figure 6.7.2                           Figure 6.7.3




                Figure 6.7.4
2. Install Linear slider in reverse order following Figures 6.7.1,6.7.2,6.7.3, and 6.7.4.
6-8 Steel Cable Slide Wheel Replacement

1.   As shown in Figure 6.8.1, remove the L sheet metal.
     As shown in Figure 6.8.2, adjust the rear Slide Wheel (Urethane) to fully release the steel cable tension, then remove the steel cable end from the spring (as
     shown in Figure 6.8.3). Use a tool to remove the C-clip (as shown in Figure 6.8.5), then the Steel Cable Slide Wheel (Urethane) can be replaced.
     When installing, pay attention to the direction of the one-way bearing, as shown in Figure 6.8.4.
     After completion, reinstall the L sheet metal. As shown in Figure 7.4.1, the distance between the Optical Sensor Board and the Steel Cable Slide Wheel
     should be 7–9 mm.




                   Figure 6.8.1                                 Figure 6.8.2                                           Figure 6.8.3




                   Figure 6.8.4                                   Figure 6.8.5                                          Figure 6.8.6
 6-9 Drive Belt Replacement

1. As shown in Figure 6.9.1, use an 8 mm hex wrench to turn the screw counterclockwise to loosen the idler pulley.




Figure 6.9.1
2. As shown in Figure 6.9.2 before replacing the belt, and as shown in Figure 6.9.3 after replacing the belt.




                  Figure 6.9.2                                         Figure 6.9.3
3. Install Drive Belt in reverse order following Figures 6.9.1,6.9.2,6.9.3. As shown in Figure 6.9.1, adjust the tightness of the bot to set the drive belt tension. The
drive belt tension should be 80 N.
6-10 FLYWHEEL REPLACEMENT

1.   Before replacing the flywheel, first loosen the idler pulley (Figure 6.9.1), then remove the drive belt.
     Use a tool to loosen the four screws securing the flywheel (Figures 6.10.1 and 6.10.2).
     Once these steps are completed, the flywheel can be replaced.




          Figure 6.10.1                       Figure 6.10.2

6-11 Foot Pad, Transportation Wheel Replacement
1. As shown in Figure 6.11.1, turn the footpad counterclockwise to remove and replace it.
(There are four foot pads located underneath the machine.)




                  Figure 6.11.1
2. As shown in Figure 6.11.2, remove the nylon nut and the bolt to replace the transportation wheel.




            Figure 6.11.2
7. Troubleshooting

7-1 Belt slip

1. If the drive belt is slipping, as shown in Figure 7.1.1, tighten the screw clockwise to adjust the drive belt tension.




               Figure 7.1.1
2. If the drive belt tension has been adjusted and slipping still occurs, the cause may be faulty unidirectional bearing inside the Steel Cable Slide Wheel.
   In this case, the Steel Cable Slide Wheel needs to be replaced. (Please refer to Steps 6–8 Steel Cable Slide Wheel Replacement for replacement instructions)
7-2 Handlebar Wobble

1. If you the handlebar wobbling during pedaling, please tighten the bolts, as shown in Figure 7.2.1.




               Figure 7.2.1

2. If the wobbling persists, check whether the quick release lever on the handle slider is tightened and in the locked position, as shown in Figure 7.2.2.




               Figure 7.2.2
7-3 O-ring Broken
Loosen the four screws securing the Console Mast, as shown in Figure 7.3.1., then pull out the Rotating Structure Assembly, as shown in Figure 7.3.2. After
disconnecting the three wire connectors, the O-ring can be removed (Figures 7.3.3 and 7.3.4).




             Figure 7.3.1                           Figure 7.3.2                            Figure 7.3.3




           Figure 7.3.4
7-4 Optical Sensor Board No Respond

1. As shown in Figure 7.4.1,7.4.2, check whether the wiring of the Optical Sensor Board is loose.
   The distance between the Optical Sensor Board and the barcode sticker on the Steel Cable Slide Wheel should be 7–9 mm, as shown in Figure 7.4.2.
   Loosen the screws to adjust it (left and right).




         Figure 7.4.1                        Figure 7.4.2


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jenuepy VIIAIBS
(L0O-9€09S-000ZSW)
GPSS8Z-SS'8


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
puodset ou preog tosusg [eoT1dQ p-)
usyolg SUII-Q ¢-)


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 15 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
1. Serial Number Location

SERIAL NUMBER

‘SERIAL NUMBER

wade ww: nena

7855452601000003

) {ih

(870) a 1107
MADE IN TAIWAN

U.S. Pat. See
w eniritfitness com

legal


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4, Setting of Electronic Console

4-1 Basic Functions

1. Refer to the User’s Manual for detailed console operations.
4-2 Maintenance Mode

Maintenance Mode is intended for troubleshooting purposes.
To enter Maintenance Mode, tap the Wi-Fi icon once and the clock in the status bar six times on the Home Screen.

iM}

Welcome

Age Height Weight
years cm kg

30 165 de)

Programs w|
incline chan


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2.2 Maintenance Mode — Item Descriptions

4.2.2.1 Odometer — Indicates the total belt operation time and accumulated running distance.

4.2.2.2 Software — Displays current software versions and allows updates on this page
Firmware and LCB’ Update Procedure

(Note: Please keep the machine powered on during the update process.)
Step 1. Place the following three files —CS51009-01.bin, CS31003.bin, and update.json — in the root directory of a USB drive.

a Ebi]
[i=] CS31003.bin FDT4 Data File
[m=] C$51009-01.bin FDT4 Data File
||] DyacoV1.0.A1.22.0..000A.10.apk APK =

©) update.json JSON 82

Step 2. Insert the USB drive into the USB port located on the back of the console.

Step 3. On this page, press the Update button under both the Firmware and LCB* sections.
The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Console APP Update Options

(Note: Please keep the machine powered on during the update process.)

This system provides two methods for updating the Console APP. Either method may be used:

Method 1: Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the Firmware and LCB* update
procedure above.

Method 2:

Step 1. In Settings, connect the machine to a Wi-Fi network.

Step 2. Return to this page. The system will automatically detect if a new version is available.

Step 3. Press the Update APK button under the Console APP section.

¢ Back < Back

Progress Beacon Acceleration &

Deceleration

pena ‘tise Software
Android

Language Time & Date Please make sure WiFi is working
Firnware properly and then press Update APK

to update it

Change Change
LCB

WiFi Standby Console App ss Update

Change PauseMode @&

Account = Units

Metric Imperial
Details J

Update APK

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 64 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4-3 Electrical Wiring Diagram

#086, Console

J6
Cost) Gs
Gai
ae #104 aad
#103 #89 #91
¥ ¥v
”» a
[ ] #085, Brake and Angle Sensor
#106 IR Reflective Sensor Board = =
Step Position & Direction #105] Lower Control Board = /— | #102

oa >
ba fw]
- —

We —— 4, = é fT w102

=o

CNS g os J
Reflective Encoder 8 Cs 04 #88 #90

Disc

#099

#097,
Power

Supply
Module

Cor}

De 1098 ‘fi ae Neutral t Se —
N=) S)4094, ine

#092, , AC Power Entry Module
with Switch and Fuse an Data Transfer we


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4-4 Circuit Board

4.4.1 Lower Control Board (#105)
Power Supply #081 provides 24 VDC to the LCB. The board converts it to 12 VDC for the console and supplies power to the angle and magnet sensors.

Sensor readings are used to control resistance on Brake #086.

wai

Aa &

®
~~
hy

tc =

fo |
|


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5. Troubleshooting (Electronic)

5-1 No power, console doesn’t light
Step 1. Press any physical button on the console (see Figure 3) to wake up the system. If the system does not respond, proceed to the next step.
Step 2. Measure the AC input voltage at the cable connected to the CN1 housing on the power supply module (see Figure 4).
If no AC voltage is measured or the voltage is incorrect, check whether the power switch is turned on and the fuse is not blown (see Figure 5).
Then, measure the mains voltage (see Figure 6) and the voltage at the machine-side end of the power cable (see Figure 7).
If correct AC voltage is present at CN1, proceed to the next step.

#097, Power Supply Module

Measured 110 VAC
or 220 VAC
depending on the

easured 110 VAC (am
or 220 VAC
depending on the
mains voltage.

Figure 4 Figure 5 Figure 6

Measured 110 VAC
or 220 VAC

Bddepending onthe —

Figure 7


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 61 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Wake the
seus: To wake the system, system Result:
Console doesn’t light press the membrane The system is in
key on the console. sleep mode.
No ic Result:
reaponee measured | Check mains voltage,
Measure the AC power cord, fuse,
input voltage on the power switch and
power supply module. internal power
wiring .
AC 24 VDC
oltage 9
¥ Light off i
saamtweed ight o Measure pins 1 and 4 measured Result:
Check power of CN100 on the >| Replace Power
indicator light DS. power supply module
to confirm 24 VDC. sere MS (i027)
24 VDC
measured
Result:
“| Replace LCB (#105)
12 VDC
not
d :
till Check for 12 VDC on perenne — the inline
>| the J3 cable at the pe
rear of the console compertor cable.
z (#089, 090)
12 VDC
measured
Result:
>| Replace Console
(#86)

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 9 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5-2 UART Communication Error

Step 1. Check if cables #103 and #104 are properly connected (see Electrical Wiring Diagram section). If not connected, reconnect it or replace the cable if
faulty. If properly connected, proceed to the next step.

Step 2. Check if the software version shows V255A255. If it does, update the software (see Maintenance Mode section). If not, replace both the LCB and the
console.

Check Procedure
improper
connection
Issue: Result:
UART Check the cables Ensure proper cable
_——_——> —— >
Communication (#103, 104) connection or
Error replace if faulty.
Proper
connection Incorrect
Check the software EEE Result:
version Update Software
Correct Result:
>| Replace LCB and
Console

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to the troubleshooting
description.


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8°79 ansIy

L79 omnsty 9°79 oINSI J $79 omsty
