<!-- Source: 8.5UE-785045 _MZ2000-SB036-01_Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

 8.5UE-785045
(MZ2000-SB036-01)
Service Manual
--------------------------------------------Table of Contents-------------------------------------------
            1. Serial Number Location
            2. Component Description
            3. Preventative Maintenance
               3.1 Check for Pedal
               3.2 Check for Circular Ring
               3.3 Check for Rail Assembly
               3.4 Check and Troubleshooting for a console O-ring
               3.5 Check for Seat Carriage
            4. Setting of Electronic Console
               4.1 Basic Functions
               4.2 Maintenance Mode
               4.3 Electrical Wiring Diagram
               4.4 Circuit Board
               4.5 List of Required Maintenance Tools
            5. Troubleshooting (Electronic)
               5.1 No power, console doesn’t light
               5.2 UART Communication Error
               5.3 No revolutions
               5.4 Incorrect Symmetry Valu
            6. Part Replacement Guide
               6.1 Console Replacement
               6.2 Transportation Wheel Replacement
               6.3 Seat Pad Replacement
               6.4 Seat Back Pad Replacement
               6.5 Seat Back Steel Cable Replacement
               6.6 Seat Steel Cable (for adjusting forward and backward) Replacement
               6.7 Seat Gas Cylinder Replacement
               6.8 Plastic cover Replacement
               6.9 Cantilever Steel Cable Replacement
               6.10 Crank Arm Replacement
               6.11 Circular Ring Handle Assembly Replacement
               6.12 Crank Arm Assemble Steps
   6.13 Cantilever steel cable (Leg position) Replacement
   6.14 Chain Replacement
   6.15 Drive Belt & Chain Wheel Replacement
   6.16 Flywheel & Idler Bracket Replacement
   6.17 Generator/Brake Controller Replacement
   6.18 Gas Cylinder & Lift Adjustment Replacement
7. Troubleshooting
   7.1 Machine wobbling
   7.2 Noise issue
8. 8.5UE Exploded view drawing
9. 8.5UE Part List
10.8.5UE Wiring Diagram
1.Serial Number Location
2. Component Description



      Item Description
      01   Cantilever
      02   Circular Ring
      03   Console Assembly
      04   Rotating Structure Assembly
      05   Front Upper Cover
      06   Rear Shroud
      07   Front Lower Cover
      08   Pedal
      09   Pedal Cover
      10   Seat Release Lever
      11   Rail Assembly
      12   Seat Rotation Release Lever
      13   Seat Back Cover
      14   Handgrip
      15   Bottom Plate
      16   Seat Back
      17   Seat
      18   Crank Arm
      19   Seat Carriage
3. Preventative Maintenance

3.1 Check for Pedal

As shown in Figure 3.1.1, please check the screws regularly for any loosening, and if any are loose, please tighten them.




                                                            Figure 3.1.1
3.2 Check for Circular Ring

As shown in Figure 3.2.1, check the screws regularly for any loosening, and if any are loose, please tighten them.
As shown in Figure 3.2.2, check the smoothness of the Circular Ring when it rotates. If it is too loose or too tight (Figure 3.2.2), simply
tighten or loosen the screws accordingly (Left and Right are the same method).




                                           Figure 3.2.1                                             Figure 3.2.2
3.3 Check for Rail Assembly

As shown in Figure 3.3.1, check the screws regularly for any loosening, and if any are loose, please tighten them.




                                               Figure 3.3.1
3.4 Check and Troubleshooting for a console O-ring

As shown in Figure 3.4.1,3.4.2, and 3.4.3, check whether the Rotating Structure Assembly moves smoothly. Loosen the four screws
attached to the Console Mast as shown in (Figure 3.4.1), then pull out the Rotating Structure Assembly as shown in (Figure 3.4.2). After
disconnecting the three connections, you can remove the O-ring, as shown in (Figure 3.4.3,3.4.4).




                         Figure 3.4.1          Figure 3.4.2             Figure 3.4.3            Figure 3.4.4
3.5 Check for Seat Carriage

As shown in Figure 3.5.1, check the screws regularly for any loosening, and if any are loose, please tighten them.




                                                              Figure 3.5.1
4. Setting of Electronic Console

4.1 Basic Functions

Refer to the User’s Manual for detailed console operations.

4.2 Maintenance Mode

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

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
 Console APP Update Options
 (Note: Please keep the machine powered on during the update process.)
 This system provides two methods for updating the Console APP. Either method may be used:
 Method 1:
 Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the
 Firmware and LCB* update procedure above.
 Method 2:
 Step 1. In Settings, connect the machine to a Wi-Fi network.
 Step 2. Return to this page. The system will automatically detect if a new version is available.
 Step 3. Press the Update APK button under the Console APP section.




 * The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
4.2.2.3   Service

          4.2.2.3.1   Machine Type – This series of six models shares the same app. You can switch the machine type on this page.
          4.2.2.3.2   Communication Test – Provides a built-in hardware loop test function.
                      Communication Test – Provides a built-in hardware loop test function.
                      Step 1. Prepare a 1-meter USB-A (male) to USB-B (male) cable.
                      Step 2. Insert the USB-A end into the USB-A port on the back of the console, and the USB-B end into the
                      USB-B port located at the data output interface beneath the machine.
                      Step 3. Prepare a 5 cm single-core wire. Strip the PVC insulation from both ends, then insert the wire into
                      pin 2 and pin 3 of the DB9 connector at the data output interface beneath the machine.
                      Step 4. On this page, press the Start button. The system will automatically check the status of the hardware
                      loop.
                      Note: The maintenance video demonstrates the actual operation process.
          4.2.2.3.3   NFC Sensor Test – Place the NFC tag near the bottom-right corner of the console.
                      Each detection cycle takes three seconds.
                      If the tag is not detected, remove it for three seconds and try again.
          4.2.2.3.4   Keypad Test – Press the physical buttons on the console to verify their functionality.
          4.2.2.3.5   Error Log – Displays the history of system errors.
          4.2.2.3.6   Beacon Test – Switch the beacon light bar colors to verify functionality.
          4.2.2.3.7   Crank Sensors – Displays the rotational speed. (see Figure 1)
          4.2.2.3.8   Crank Calibration – Put the right crank at a 6 o’clock position, then press the button below to run the test.
                      (See Figure 2)




                         Figure 1          Figure 2
      4.2.2.4   Lock Facility Program – When set to ON, the speed and incline profiles of the Facility program cannot be modified.

4.3 Electrical Wiring Diagram
4.4 Circuit Board
  4.4.1 Lower Control Board (#084)
       Power Supply #075 provides 24 VDC to the LCB. The board converts it to 12 VDC for the console and supplies power to the angle
       and magnet sensors. Sensor readings are used to control resistance on Brake #079
4.4.2 Power Supply Module (#075)
      AC power is converted to 24VDC to provide DC voltage for the entire system.
4.5 List of Required Maintenance Tools

                                         No.                   Tool Name
                                         1                     Multimeter
                                         2             Cordless Impact Driver Set
                                         3                 Phillips Screwdriver
                                         4               Diagonal Cutting Pliers
                                         5                 Needle-nose Pliers
                                         6                Electric Soldering Iron
                                         7                     Solder Wire
                                         8                Anti-static Tweezers
                                         9                 Heat Shrink Tubing
                                         10                    Utility Knife
                                         11          Hex Key Set (Allen Wrench Set)
                                         12                Socket Wrench Set
                                         13       Cable Ties (Minimum Length: 20 cm)
                                         14             Electrical Insulation Tape
                                         15    Lead Wire (for guiding cable through tubing)
                                         16                 Insulated Gloves
                                         17               Anti-static Wrist Strap
                                         18                Crank Removal Tool
5.    Troubleshooting (Electronic)

5.1 No power, console doesn’t light

     Step 1. Press any physical button on the console (see Figure 3) to wake up the system. If the system does not respond, proceed to the
     next step
     Step 2. Measure the AC input voltage at the cable connected to the CN1 housing on the power supply module (see Figure 4). If no AC
     voltage is measured or the voltage is incorrect, check whether the power switch is turned on and the fuse is not blown (see Figure 5).
     Then, measure the mains voltage (see Figure 6) and the voltage at the machine-side end of the power cable (see Figure 7). If correct
     AC voltage is present at CN1, proceed to the next step.




               Figure 3                             Figure 4                                          Figure 5
Figure 6   Figure 7
Step 3. Check the status of power indicator light D5 on the LCB (refer to the Circuit Board section). If the light is off, proceed to the
next step. If the light is on, skip ahead to Step 5.
Step 4. Measure pins 1 and 4 of connector CN100 on the power supply module to verify the presence of 24 VDC (see Figure 8). If 24
VDC is not measured, replace the power supply module. If 24 VDC is measured, replace the LCB.
Step 5. Measure pins 1 and 2 on the J3 cable at the rear of the console to verify 12 VDC (see Figure 9). If no 12 VDC is measured,
inspect the inline connector cable (see Electrical Wiring Diagram section). If 12 VDC is measured, replace the console.




                              Figure 8                                              Figure 9
                                                           Check Procedure




Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.
5.2 UART Communication Error

   Step 1. Check if cables are properly connected (see Electrical Wiring Diagram section). If not connected, reconnect it or replace the
   cable if faulty. If properly connected, proceed to the next step.
   Step 2. Check if the software version shows V255A255. If it does, update the software (see Maintenance Mode section). If not, replace
   both the LCB and the console.

                                                           Check Procedure




Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.
5.3 No revolutions

   Step 1. While pedaling the crank, check the status of indicator light D13 on the LCB (see Circuit Board section). If the light flashes,
   confirm that both ends of the cable are properly connected (see Electrical Wiring Diagram section). If the light does not flash,
   proceed to the next step.
   Step 2. Confirm that the gap between the Hall sensor (078) and the magnet on the Chain Wheel (208) is 2 to 3 mm, and that the
   sensor is aligned with the center point between the two arrow marks (see Figure 10). If the sensor is not installed correctly, reinstall it.
   If the installation is correct, proceed to the next step.
   Step 3. Confirm that both ends of the cable are properly connected (see Electrical Wiring Diagram section). If the cable is not
   properly connected, reconnect both ends securely. If the cable is already properly connected, replace both the LCB and the Hall
   sensor.




                                                                 Figure 10
                                                           Check Procedure




Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.
5.4 Incorrect Symmetry Value

   Step 1. Calibrate the crank position (see Maintenance Mode section). If the issue persists, proceed to the next step.
   Step 2. Position the right crank at the 6 o'clock position. Ensure that the magnet on the Chain Wheel (208) maintains an angle of at
   least 90 degrees relative to the Hall sensor (see Figure 11). Once properly aligned, install the right crank. Then, recalibrate the crank
   position.




                                                                 Figure 11
                                                           Check Procedure




Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.
6. Part Replacement Guide
6.1 Console Replacement

6.1.1 Remove Electronic Console
      As shown in Figure 6.1.1, remove 2 pcs bolts from the Rear Tube Cover
      As shown in Figure 6.1.2, 6.1.3, remove 4 pcs from the back of the console, and then disconnect the cable to remove the console.




                      Figure 6.1.1                        Figure 6.1.2                 Figure 6.1.3
      Install console in reverse order following Figures 6.1.1, 6.1.2, and 6.1.3.
6.2 Transportation Wheel Replacement

6.2.1 Remove Transportation Wheel
      As shown in Figure 6.2.1, remove the bolt by turning it counterclockwise. (Right and Left side are the same method)




                                                        Figure 6.2.1

     As shown in Figure 6.2.2, Secure one side, and loosen the other side by turning it counterclockwise.




                                                        Figure 6.2.2

     Install transportation wheel in reverse order following Figures 6.2.1, 6.2.2.
6.3 Seat Pad Replacement

6.3.1 Remove seat pad
      As shown in Figure 6.3.1, 6.3.2, 6.3.3, remove the screws counterclockwise in order.




                         Figure 6.3.1                                Figure 6.3.2            Figure 6.3.3
      Install seat pad in reverse order following Figures 6.3.1, 6.3.2, and 6.3.3
6.4 Seat Back Pad Replacement

6.4.1 Remove seat back
      As shown in Figure 6.4.1, insert a flat-head screwdriver between the plastic cover and the seat back, then pry it open.
      As shown in Figure 6.4.2, remove the bolts by turning them counterclockwise.



                 6.5 椅背拆除




                      Figure 6.4.1                                     Figure 6.4.2
      Install seat back in reverse order following Figures 6.4.1 and 6.4.2.
6.5 Seat Back Steel Cable Replacement

6.5.1 Remove seat back steel cable.
      As shown in Figure 6.5.1, use a tool to loosen the area marked by the red circle, then remove the cable head and the screw.
      As shown in Figure 6.5.1, cut the cable tie, then use both hands to apply force in the direction of the arrows shown in the figure
      6.5.2 to remove and replace it.




                    Figure 6.5.1                                                      Figure 6.5.2
      Install seat back steel cable in reverse order following Figures 6.5.1 and 6.5.2.
6.6 Seat Steel Cable (for adjusting forward and backward) Replacement

6.6.1 Remove seat steel cable.
      As shown in Figure 6.6.1, use the C-clip to remove the E buckle, then use a tool to loosen the screw and remove it.
      As shown in Figure 6.6.2, and 6.6.3, use a tool to loosen the screw and remove it.
      As shown in Figure 6.6.4, remove the steel cable head in the direction of the arrow to take out and replace the cable.




                     Figure 6.6.1                                         Figure 6.6.2
                     Figure 6.6.3                                                         Figure 6.6.4
Install seat steel cable in reverse order following Figures 6.6.1, 6.6.2, 6.6.3, and 6.6.4.
6.7 Seat Gas Cylinder Replacement

6.7.1 Remove seat Gas Cylinder
      As shown in Figure 6.7.1, use a tool to loosen the screw and remove it.
      As shown in Figure 6.7.2, use a tool to loosen the screw and remove it, and then remove the seat gas cylinder.




                       Figure 6.7.1                                       Figure 6.7.2
      Install seat Gas Cylinder in reverse order following Figures 6.7.1 and 6.7.2.
6.8 Plastic cover Replacement

6.8.1 Remove Plastic cover.
      As shown in Figure 6.8.1, remove the seat.
      As shown in Figure 6.8.2, have someone assist you in tilting the machine to the side, then use a tool to loosen and remove the screws
      (4 pcs in total) to take off the pedal cover.
      As shown in Figure 6.8.3 and 6.8.4, insert a flat-head screwdriver into the gap where the covers join and pry them open. Apply
      some force to release the clips and the locking grooves.
      As shown in Figure 6.8.5, use a tool to loosen and remove the screws (10 pcs in total) to take off the pedal rear shroud.
      As shown in Figure 6.8.6, twist the top cover with both hands to remove it.




                 Figure 6.8.1                                                Figure 6.8.2
      Figure 6.8.3                            Figure 6.8.4                      Figure 6.8.5             Figure 6.8.6
Install plastic cover in reverse order following Figures 6.8.1, 6.8.2, 6.8.3, 6.8.4, 6.8.5, and 6.8.6.
6.9 Cantilever Steel Cable Replacement

6.9.1 Remove Cantilever Steel Cable.
      As shown in Figure 6.9.1, use the tool to remove the cable tie.
      As shown in Figure 6.9.2, remove the steel cable end.
      As shown in Figure 6.9.3, use the tool to remove screws, and then remove the steel cable end.
      As shown in Figure 6.9.4, and 6.9.5, use the tool to remove the screws.
      As shown in Figure 6.9.6, remove the plastic cover at the red-circled area, then use a tool to remove the screws. After that, you can
      open the Ring Grip cover.
      As shown in Figure 6.9.7, use the tool to remove the screws at the red-circled area, and then pull out the steel cable.




                        Figure 6.9.1                          Figure 6.9.2                                Figure 6.9.3
           Figure 6.9.4                                  Figure 6.9.5                                         Figure 6.9.6




         Figure 6.9.7
Install cantilever steel cable in reverse order following Figures 6.9.1, 6.9.2, 6.9.3, 6.9.4, 6.9.5, 6.9.6 and 6.9.7.
6.10 Crank Arm Replacement

6.10.1 Remove Crank Arm.
      As shown in Figure 6.10.1, use a No. 5 hex wrench to loosen the flat head socket screw counterclockwise.
      As shown in Figure 6.10.2, 6.10.3, and 6.10.4, use a 13 mm open-end wrench to loosen the crank retaining sleeve counterclockwise,
      then remove the crank retaining sleeve.
      As shown in Figure 6.10.5, use a nut remover to loosen the M10 flange nut counterclockwise.




         Figure 6.10.1                  Figure 6.10.2             Figure 6.10.3                Figure 6.10.4         Figure 6.10.5

      Install crank arm in reverse order following Figures 6.10.1, 6.10.2, 6.10.3, 6.10.4, and 6.10.5.
6.11 Circular Ring Handle Assembly Replacement

6.11.1 Remove Circular Ring Handle Assembly.
      As shown in Figure 6.11.1, and 6.11.2, use No. 6 hex wrench to loosen the M10 button head socket bolt counterclockwise.




                  Figure 6.11.1                        Figure 6.11.2
     Install Circular Ring Handle Assembly in reverse order following Figures 6.11.1, 6.11.2.
6.12 Crank Arm Assemble Steps

6.12.1 Assemble Circular Ring Handle Assembly.
      As shown in Figure 6.12.1, 6.12.2, 6.12.3, 6.12.4, 6.12.5, 6.12.6, 6.12.7, and 6.12.8, install in the order shown in Figure.




         Figure 6.12.1          Figure 6.12.2             Figure 6.12.3          Figure 6.12.4




         Figure 6.12.5             Figure 6.12.6            Figure 6.12.7         Figure 6.12.8

      Before reassembling the circular ring, make sure to place the #197 wave washer in first. Then follow the sequence (Figure 6.12.1 to
      Figure 6.12.8). Following the Figures, you can install the crank arm onto the cantilever.
6.13 Cantilever steel cable (Leg position) Replacement

6.13.1 Cantilever steel cable (Leg position) remove.
      As shown in Figure 6.13.1, use the tool to remove the cable tie.
      As shown in Figure 6.13.2, use the tool to remove the screws and remove the steel cable end.
      As shown in Figure 6.13.3, use the tool to remove the screws and remove the steel cable end, then remove the steel cable.




                Figure 6.13.1                           Figure 6.13.2                         Figure 6.13.3
      Install Cantilever steel cable (Leg position) in reverse order following Figures 6.13.1, 6.13.2, and 6.13.3.
6.14 Chain Replacement

6.14.1 Chain remove.
      As shown in Figure 6.14.1, use the tool to loosen the Chain Wheel.
      As shown in Figure 6.14.2, use the needle-nose pliers to remove the Chain Fasten.
      As shown in Figure 6.14.3, Remove the metal plate and disengage the connecting clip to take off the chain.




               Figure 6.14.1                        Figure 6.14.2                        Figure 6.14.3
      Install Chain in reverse order following Figures 6.14.1, 6.14.2, and 6.14.3.
6.15 Drive Belt & Chain Wheel Replacement

6.15.1 Drive Belt and Chain Wheel remove.
      As shown in Figure 6.15.1, use the tool to loosen the Chain Wheel.
      As shown in Figure 6.15.2, use the tool to remove the screws and remove the sensor sheet metal.
      As shown in Figure 6.15.3, remove the drive belt.
      As shown in Figure 6.15.4, and 6.15.5, use the tool to remove the screws and nuts, then remove chain wheel assembly.




              Figure 6.15.1                         Figure 6.15.2                         Figure 6.15.3
               Figure 6.15.4                                                Figure 6.15.5

Install drive belt & chain wheel in reverse order following Figures 6.15.1, 6.15.2, 6.15.3, 6.15.4, and 6.15.5.
6.16 Flywheel & Idler Bracket Replacement

6.16.1 Flywheel and Idler Bracket remove.
      As shown in Figure 6.16.1, remove the drive belt.
      As shown in Figure 6.16.2, use needle-nose pliers to remove the spring.
      As shown in Figure 6.16.3, use the tool to remove the screws at the red-circled area, then remove the Idler Bracket.




                Figure 6.16.1                       Figure 6.16.2                                Figure 6.16.3

      Install flywheel & idler bracket l in reverse order following Figures 6.16.1, 6.16.2, and 6.16.3.
6.17 Generator/Brake Controller Replacement

6.17.1 Generator/Brake Controller remove.
      As shown in Figure 6.17.1, disconnect all the wires.
      As shown in Figure 6.17.2, use the tool to remove the screws at the red-circled area, then remove the Generator/Brake Controller.




                  Figure 6.17.1                                 Figure 6.17.2

      Install Generator/Brake Controller l in reverse order following Figures 6.17.1, and 6.17.2.
6.18 Gas Cylinder & Lift Adjustment Replacement

6.18.1 Cylinder & Lift Adjustment remove.
      As shown in Figure 6.18.1, use the tool to remove the cable tie.
      As shown in Figure 6.18.2, remove the steel cable end.
      As shown in Figure 6.18.3, use a tool to remove one of the screws and loosen the other so that the bracket can be moved aside.
      As shown in Figure 6.18.4, use a tool to remove the axle and the screw.
      As shown in Figure 6.18.5, use a tool to remove the axle and the screw, then remove the Idler Bracket gas cylinder and lift
      Adjustment.




                  Figure 6.18.1                               Figure 6.18.2                            Figure 6.18.3
                  Figure 6.18.4                                               Figure 6.18.5

Install Cylinder & Lift Adjustment in reverse order following Figures 6.18.1, 6.18.2, 6.18.3, 6.18.4, and 6.18.5.
7. Troubleshooting
7.1 Machine wobbling.

7.1.1 Machine Adjustment.
      As shown in Figure 7.1.1, adjust the height of the 4pcs adjustment foot until the unit is balanced.
      As shown in Figure 7.1.2, and 7.1.3, check these screws are tightened.




                   Figure 7.1.1                          Figure 7.1.2                               Figure 7.1.3

7.2 Noise issue.

7.2.1 During use, the sounds generated by the chain and flywheel during forward and backward rotation are normal.
8. 8.5UE Exploded view drawing
9. 8.5UE Part List
10. 8.5UE Wiring Diagram


=== OCR SUPPLEMENT, PDF PAGE 1 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
jenuepy ddIAIas
(L0O-9€09S-0002ZIN)
GP0S8Z-JNS's


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 29 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4. Setting of Electronic Console

4.1 Basic Functions

Refer to the User’s Manual for detailed console operations.
4.2 Maintenance Mode

Maintenance Mode is intended for troubleshooting purposes.
To enter Maintenance Mode, tap the Wi-Fi icon once and the clock in the status bar six times on the Home Screen.

£93 Nn > => 12:15

tt 4}

Welcome .
Age Height Weight
years cm kg

22 l¢ 3

30 165 75

Pattern

2t more accurate results, please Programs w
provide your physical data incline chan


=== OCR SUPPLEMENT, PDF PAGE 13 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2.2 Maintenance Mode — Item Descriptions
4.2.2.1 Odometer — Indicates the total belt operation time and accumulated running distance.
4.2.2.2 Software — Displays current software versions and allows updates on this page

Firmware and LCB* Update Procedure
(Note: Please keep the machine powered on during the update process.)
Step 1. Place the following three files —CS51009-01.bin, CS31003.bin, and update.json — in the root directory of a USB drive.

lal Ea]
[=] CS31003.bin FDT4 Data File|
fe) C$51009-01.bin FDT4 Data File|
|] DyacoV1.0.A1.22.0.000A.10.apk APK =

| update.json JSON 82

Step 2. Insert the USB drive into the USB port located on the back of the console.

——— ote

Wi eiteesan,

Insert the USB flash drive


=== OCR SUPPLEMENT, PDF PAGE 14 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Step 3. On this page, press the Update button under both the Firmware and LCB* sections.

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.
Console APP Update Options
(Note: Please keep the machine powered on during the update process.)
This system provides two methods for updating the Console APP. Either method may be used:
Method 1:
Place the file DyacoV1.0.A1.22.0.xxxxA.10.apk in the root directory of the USB drive, and follow the same steps as the
Firmware and LCB* update procedure above.
Method 2:
Step 1. In Settings, connect the machine to a Wi-Fi network.
Step 2. Return to this page. The system will automatically detect if a new version is available.
Step 3. Press the Update APK button under the Console APP section.

; < Back <¢ Beck
Progress Beacon Acceleration &

Deceleration

Change Change Softwa re
ear Software
Language : Time & Date Please make sure Wifi is working
Firmware properly and then press Update APK
to update it
Change Change
LCB
WiFi Standby Console Ap => Update
A
cS
Change PauseMode @

Account hf Units

Metric | mperia
Details }

Update APK

* The full name of LCB is Lower Control Board. Please refer to the Circuit Board section for further information.


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 36 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4.2.2.4 Lock Facility Program — When set to ON, the speed and incline profiles of the Facility program cannot be modified.

4.3 Electrical Wiring Diagram

a
2061 Console
=
51) Gs
iTS |
Ps 1

2078 Magnet Sensor ‘ 4
<1 —
—

1 = Ome
| | #084 Lower Control Board ; Es
~ 4
al é

#211 Magnet

ebay .

215

073 f 1 2071 Neutral y

ors \ aes =!) i aaa

=

=070 AC Power Entry Module
with Switch and Fuse #065 Data Transfer Board


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Measured 110 VAC
or 220 VAC
depending on the

mains voltage.

Figure 6 Figure 7


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 56 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Wake the
‘seuss To wake the system, system Result:
“ r he membrane >>
C led 't light p——-1_ press the membrane The system is in
key on the console. sleep mode.
No A
No shines Result:
response measured Check mains voltage,
Measure the AC power cord, fuse,
> input voltage onthe [——————>} power switch and
power supply module. internal power
wiring .
24 VDOC
tes not
voltage Light off Measure pins 1 and 4 measured
measured Result:
> Check power 3 of CN100 on the >! Replace P
indicator light DS. power supply module Sieh Mice
to confirm 24 VDC.
24 VDC
measured
Result:
“| Replace LCB
12 VDC
not
Light on measured Result:

Check for 12 VDC on

Inspect the
the J3 cable at the ania
rear of the console. —

12 VDC

measured

Result:
Replace Console

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.


=== OCR SUPPLEMENT, PDF PAGE 24 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5.2 UART Communication Error

Step 1. Check if cables are properly connected (see Electrical Wiring Diagram section). If not connected, reconnect it or replace the
cable if faulty. If properly connected, proceed to the next step.

Step 2. Check if the software version shows V255A255. If it does, update the software (see Maintenance Mode section). If not, replace
both the LCB and the console.

Check Procedure
improper
connection
Issue: Result:
UART Check the cables 2 Ensure proper cable
Communication connection or
Error replace if faulty.
Proper
connection incorrect
> Check the software Result:
version Update Software
Correct Result:
>| Replace LCB and
Console

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 39 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Flash Result:
pecs Check indicator light Ensure that the cable
ns vevoladions p13 as the pedal p> is properly
rotates. connected at both
ends.
improper
Correct connection
siaae lane gap Check the cable is Result:
————} properly connected >| Connect the cable
between Hall sensor aa hos anda: 0 3
and magnet.
Proper
connection
Result:
>| Replace LCB and Hall
sensor

Incorrect
Result:

> Reinstall the Hall
sensor.

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 17 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Check Procedure

Resolved

Result:
Problem corrected
via calibration.

Issue:
incorrect Symmetry
Value

Calibrate the crank

position.
7

Problem .
Reinstall the crank in
the correct
orientation.

Note: The Check Procedure provides an overview of possible causes. For detailed troubleshooting steps and inspection points, refer to
the troubleshooting description.


=== OCR SUPPLEMENT, PDF PAGE 53 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8. 8.5UE Exploded view drawing

074
077 \ 103
8-201

080 _ 124
068

08!
169

063 071

083,

N72

nm. 06g, 073
11g

we

40

MZ2000
2025/08/18


=== OCR SUPPLEMENT, PDF PAGE 54 ===
<!-- render-vs-extraction: 8 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
‘50

MR2000/MS2000/MZ2000 % Fi #5
2025/06/11


=== OCR SUPPLEMENT, PDF PAGE 55 ===
<!-- render-vs-extraction: 153 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9. 8.5UE Part List

Item Description Qty Item Description
1 Main Frame 1 47 Isolation Column
2 Pedal 2 49 Round Cap
3 Back Plate(A) 7 4 54 6203_Bearing
4 Back Plate(B) 1 57 = Bearing(UCP-20)
5 _ Rotating Structure Assembly(Top) | 58 Bearing(UCP-25)
6 Rotating Structure Assembly(Bottom) a S89 __690522_Bearing
7 Console Transfer Bracket 1 60__Cantilever
8 Pulley Axle-A 1 61 Console Assembly
62 Resistance Button W/Cable
Tl Pulley-E 1 -
- 63 1300mm_Connecting Wire
v4 Sheet Metal Axis-A 1 : ; .
64 5S5Omm_Connecting Wire{(PHP-6)
B — : 65 Interface Board
4 Axle-B _ 66 _ 1700mm_Connecting Wire(PHP-9)
& Adjustment Axis-B 67 550mm_Connecting Wire(PHP-9)
19 Sheet Metal od 68 1700mm_Connecting Wire(XHP-4)
20 ‘Fixing Bracket 1 69 SSOmm_Connecting Wire(XHP-4)}
2 Sheet Metal 1 70 AC Electronic Module
22 = Connecting Plate 1 71 80mm_Connecting Wire (White)
23 _~—SOCTTrransfer Sheet 1 72 80mm_Connecting Wire (Black)
27 Console Bracket , 1 73  SOOmm_Ground Wire
293 Gas Cylinder 1 74 350L_Power Connecting Cable
30 Lift Adjustment 1 7S Switching Power Supply
32 Steel Cable 1 76 300L_Ground Wire
35 Tole Belt , 1 77 250m m_Power Connecting Cable
37 Spring 2 78 ~~ Hall Module
38 Rubber Foot 3 79 = Flywheel
: 80 250mm_Wire Brake Coil Harness(Red)
39 Transportation Wheel z 81 200mm_Wire Brake Coil Harness(Red)
a td a 82 950mm_Connecting Wire(XHP-6)
4| Buckle 10 83 SSOmm_Connecting Wire(XHP-6)
42 Snap seat uy 84 Generator/Brake Controller
me) O-ring . 6 85 = Reflective Panel
44 Pedal Mat 1 86  250mm_Connecting Wire(XHP-4)
45 Nylon Washer ; 2 87 Ring Grip (R)

46 Pad 2 ess Ring Grip (L)


=== OCR SUPPLEMENT, PDF PAGE 56 ===
<!-- render-vs-extraction: 208 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
JOYysIUYy MII [PISW ISEYS WW x +
jousuy dubpuey OL MaIDS [P1aW WeYSTWWZ| « SS
soysuy duBbpuey JBYSEM JEIS OLD

aje|d aseq Japi|s paxi4 , MaIDS PRS} SdijjtuG™WWZI x SW

ansa|s Buruieqas YURID Og de> PesH 1ey3I0S™ WS] = SW

BABAIS BPX HULID , 10g de> peay 1eyD0S"WIOF « OW

Buuesg™zoz9o 4Og 184905 PPSH YONG 10Z « ST ld « SW

Bury sejnauiD , Bure TUS

ay INN UOJAN™L9 * .9YS

wy 4UBID , YOU 14305 PPSH UOTING ,+7/F-L * .9YS

JBYSEM UOJANTILE « SLD « BD INN UOIAN™19 = SZIld « BW

a1e\|d JeaM\ you ded Peasy 1syxI0S~ WILY = SZ « SW

diID-3-73 JBYSEM WIIS™F/1D

A3y MUPOOM™IOL « S JOYSEM IE|4~ LOL * SL * w/OD

JBYSEM 1/4 LOE « SZ = WB/ED YOY PESH XBH™7/E * OZINN * w/L

MBIDS 194DOS PRSH Ie|-4"WIWI « £/Od « YW {|EuUondgO) PuoD JaMmog
MIDS IBAIOS PEFH I|4 TLE * SIN-LE * LID JBYSEM IE|4-LOL * CLO * SD
Og 1yD0S PSH UONNG SL « Sid « OLW 7 YOR ded pesH 1820S 101 = LOd « 7W
MIS PRSH SAI” WWOL x SW INN UOIAN™L8 * OL

JBYSEM, 5 JBYSEM IE|S~1SL « STD « OLD

INN UOIANTIS'S » o7/L yOu ded PesH 1842057 WWOs « OLW

you aGewer ,Z/l * «/L . mains Buiddey~79| « SO

SMBIIS 18S PSNO[S“WIWOL « SW Bury D°S7O

SM2IIS JeS PeTO|S™WWS « SW ¥SIg PUNOY

duue|> sui JBAOD Jeg 8|PUBH

INN7LSE « vW , Buiun Buiuonisog Bury Jeu

MBS PREAH SAijIYq™ Wg = SW J@AOD @QNL JeBY
MaJ2S PRaH Sdiyjiuq™Wug x 7 JBAOD dol

MII 184905 PSH 1e|4 Wig = CW JBaNOD Pred
Aay HNIPOOM IBAOD IBMO7 WOJ4

M@JIS PESH SAII|IUd™ WW] x SW 4JBAOD Jaddp ywol4
INN UO|ANT19 = SW pnouys 1e384

INN LOL * STId * OLW JaAS7] aseajey

JOUSEM IES71SL « BLD * SBD Bnid duo bury
MBIIS |BIBW sys” WWwg| x 7 JBAOD UOTIN,G duy Bury
uopdusseq uondioseq


=== OCR SUPPLEMENT, PDF PAGE 57 ===
<!-- render-vs-extraction: 194 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
J213W 1s8UuS Feld FINE
aleid 42eg , BASIS

yoey WI] Jee ajosuoD

poy Bunsn (py z , JBUSE/ SARA" x SIO

segs|pueH INN LOS * Old * SW

SIX BUIPIS 3IQeD [937S M@J2S |P2UM PIPIMTZS * SW

sane7 Bunsnipy JBYSENM IEl4 LOL * SETH * LID

O)epey 272204 4an87 Bunsnipy Buy DOLD
IPI@W IS38yYs IUsWIsNipy 42eg IeaS JBYSEM WIGSTISL « SD
(Y)IEIEW IWeEYsS 4221 1235 de> punoy

O)IEIPW I@28YS 42241 1eAaS Buyeag |EUONe/IPIUN

aeld wonog Buueag soso

Janzq Bunsnipy Buuds uolsuey

IPI@W I@9YS JAPIOH dnd FIQED [2821S

7JO}IBlg YIP Wess §-1s4921g Je|P]

124921g Paxi4 49eg 188s ¥-784921g J2/P]

JONAS] BSEIISY ILIS qey2e7g Buixig

Aiquuassy ley JEPIS

J3aA37 SSea|3ay UONeI0YH 1288S M2125 184305 PSH 1e|4{7~Wiwigz « SW
Ajquuassy sousuy yangiueD ; SAsa|5 ABunelew JaMpPOd™ GZ = OL « +1

yoie7 Burseajay JBYSeM JEIS SW

abewies eas a Buiysng

UONeIOY 1238S Bury Bunes07

weo4 : J@AUGQ M2I2S PAH sdiyiud

qeuBbey YIUussM UsI|¥ 7
(yy-SeD0g)UIEYD 5 MIS PESH Sdijiyd™ WW] x SW

(65-Sza9g)MIe4> MIDS PRSH SAiI|IYq™WWOL x SW

(WWE's « STD « OFD)IF2UM UIEYD : SMA1DS 18S Pao|s"wws « SW

(Wig « OBD+ WWE x LED x 77B)ISOUM UEUD MaIdS [EIS 199US WIWIOL » SE
(WWE = LED « vyD)IB2UM YIEYD —_ yur ajpuery

(WIWSL « OFD « LED)IPPUM UEYD Bunds

(wwz'sZ « S7D * OFB)IB2UM UIEUD ’

Asy JNUPOOMWWOZ * £ « L

yog ded pea 19420S~ WOOL * OLW

MIDS [EIB ISYS“ WILY = ¢

uopdoseq

g-arxy Buixig
D-aKy Buixig
3|pueH
soyouy
uopdyoseq


=== OCR SUPPLEMENT, PDF PAGE 58 ===
<!-- render-vs-extraction: 209 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
YOY PESH XBHWF/EL * WDU/S Og ded pesH 1eyx30S~ WILE =x OW

JUSEM I°|4- LOZ « 97D x SBD . og de> peay 19490S"WWZI « IW

INN UO|AN™L8 = OLIN Og PREAH XPH™1SZ « SZ Id « BW

Yog Ged pesyH Wey2.0S™WIWWIDY, = OW , Og 184305 pesH vOoTING™WuS| « OW
Og 14205 peasy UOTING™ WWE « SW OG PRESH XPH~.7/F * BLINN * wDU/S
MaJI2S [P1leW SYS WW « SS (7) 48A03 BIGeIUIN,

MIDS PRSH SAI!Ud™WWZ| « SW (4) 48N02 aIQeqNL
dij>-37S3 JBAOD DNISE}d JBMO7

INN UOIAN™ZL J@AOD YEG eas

MBI2IS J@4D0S PSH Je|4"WWOF « BW JBAOD SBulH
JOYSeM IE|A” LOT « STD * .B/SD ; JBP|OH sHeisnag

Og de> peasy 18xD0S WHE « .H/E-L « B/E peg
YOY PSH XSH™8/S * BLINN * wDL/S ; sdeyj 21se|q
0g de> peaH 18490SOZI « SL'Id * ZI. 1eas deus
Og ded peasy 19420S7 104 « 80d « SW 3)2Ng
JBUSE/MM\ PSAIND ISL « GL * VSO , 3|xv seddojs Jo} yaneds

Og de> PeSH 184305104 « Old « SW ansa|s ABunj|eIaW JBMPOd 18 « BLD « Z1D
yog de> peasy ieyD20S™WwSZ « OW , aAasa|S ABuny|elew JaMpod™WWwZzZ « 6SL
ywoR 91 « OUST id « BW SIDED 1993S

JBUSEM IEL4~LE * OLD * .B/ID G-319eD [91S

YOY PESH XSHWILUE| « B/E 1835

YORg 1420S PP38H UOTING™WWOZ « OLIN yoeg 1238S
YOg 194305 PES UOWNG™ 105 « Old « 9W duBpuey
M@J2S 124205 PSH 12] 47~ WwW] = SW a jes4yM uo|AN“G¥809
Bury DID Is84M WOd

JBYSEM IE|4~ISL « SLD « SBD Bunsnipy pesy 1uo14 1838S

JOYSEM IE|S~LOL «LD « 9D Buuds

INN BeNbs7|S9 x SZL* BW : Buds Jou suoD

IAN“T6L * SV Guuds

INN UOIAN™L9 = .9YS . SIG 212104

INN UO|AN719 = OW sapuljAD seo

INN UO|AN™ 1S x SW g-lIaW~W 188US

INN" L? = SIN V-IEISW 1884S

Og PRsH XeH™WWOT « BW Yyd1e7 UOIISO 1835
yOg de> peay 1420S 0z « STid « SIN a1e|q Burxig aay YONeuodsues |
uopdyusseg uopdyoseq


=== OCR SUPPLEMENT, PDF PAGE 59 ===
<!-- render-vs-extraction: 72 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Item Description

600 66 O12 « 15T_Flat Washer

601 8 ~« 1ST_Split Washer

602 M8 « 35mm_Hex Head Bolt

603 M8s~ P1.25~ 15L_ Button Head Socket Bolt
604 M8 10mm_Button Head Socket Bolt
605 M8s~« 20mm_Flat Head Countersink Bolt
606 MB « 60mm_Flat Head Countersink Bolt
607 M8~*«7T_Nylon Nut

608 285 « 026 « 20T_Flat Washer

609 Mé&8~« P1.25 « 20L_ Button Head Socket Bolt
610 3/8" « 7T_Nylon Nut

6n 8mm_LAllen Wrench

612 13/l4mm_Wrench

613) 5 « 26 120L_L Allen Wrench

614 M6~ P1.O0(@8 « 20L)_Bolt

61S MG « 12mm_Socket Head Cap Bolt

616 9 MS~« 15mm_Phillips Head Screw

617 6 « 25L * MS « PO.8_Bolt

618 = Fixing Base


=== OCR SUPPLEMENT, PDF PAGE 60 ===
<!-- render-vs-extraction: 39 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
10. 8.5UE Wiring Diagram

{uss}
16
4
3
r icssn0gp-3
2078 Magnet Sensor +4 4
= #079 Brake and Angle Sensor
|__tr}.. 2084 Lower Control Board B eh
#211 Magnet : St
=k c i
Ll
oo
073 A i ne < 2071 Neutral ; +’ +
o—— ‘SS +72 Line

#070 AC Power Entry Module a wore)
with Switch and Fuse 2065 Data Transfer Board
