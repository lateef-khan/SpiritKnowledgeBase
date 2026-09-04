 SRVO SR260
Service Manual
                                                                                               Table of Contents

 1. Outlines .......................................................................................................................................................................................................................... 3
2. Safety instructions ........................................................................................................................................................................................................... 6
3. Explosive view .................................................................................................................................................................................................................. 9
4. Disassembly instructions ............................................................................................................................................................................................... 11
5. Circuit Diagrams ............................................................................................................................................................................................................. 23
6. Block diagram ................................................................................................................................................................................................................ 25
7. Key component list ........................................................................................................................................................................................................ 27
8. Detailed description of components ............................................................................................................................................................................. 29
     8-1 Display main board ............................................................................................................................................................................................... 30
       8-1-1 CN5：RS485&12V Power connector ............................................................................................................................................................ 31
       8-1-2 CN1：Debug port ......................................................................................................................................................................................... 32
        8-1-3 CN6&CN7: Left & Right speaker port ............................................................................................................................................................ 33
      8-2 Controller module ................................................................................................................................................................................................ 34
        8-2-1 CN3：AC port ............................................................................................................................................................................................... 35
        8-2-2 CN2：Motor power port .............................................................................................................................................................................. 36
        8-2-3 CN6: RS485 Communication interface .......................................................................................................................................................... 37
        8-2-4 CN7: Encoder port......................................................................................................................................................................................... 38
      8-3 Controller module ................................................................................................................................................................................................ 39
        8-3-1 CN3: AC input port ........................................................................................................................................................................................ 40
        8-3-2 CN1 & CN2 Direct-current output port ......................................................................................................................................................... 41
     8-4 Wireless control module ...................................................................................................................................................................................... 42
9. Error Messages & Troubleshooting ............................................................................................................................................................................... 43




                                                                                                                                                                                                                                            2
1. Outlines




              3
                         Top View
No.   Parts Name

1     Display Panel

2     Rope Hatch

3     Left End Cover

4     Right End Cover

5     Frame

6     Foot Board Panel

7     Shock Pad          Bottom View

8     Wheels

9     Back Cover




                                       4
No.   Parts Name
                                Left Side View
10    AC Switch and Socket

11    Lifting Handle Cover

12    Display Module

13    Servo Motor Module

14    Cooling Fan

15    Controller
                                Bottom View without Back Cover
16    Full Range Power Supply




                                                                 5
2. Safety instructions




                         6
Safety warning

     The current of the power supply and communication cable is
     dangerous. To avoid the danger of electric shock:
     ˙Do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm
     ˙Connect power cords to a properly wired and grounded electrical outlet
     ˙Whenever possible, use one hand only to connect or disconnect signal cables
     ˙Never turn on any equipment when there is evidence of fire, water, or structural damage.
     ˙Disconnect the attached power cords, before you open the device covers, unless instructed otherwise in the installation and configuration procedures.
     ˙Connect and disconnect cables as described in the following procedures when installing, moving, or opening covers on this product or attached devices.


                         To connect:                                             To disconnect:
                         1. Turn everything OFF.                                 1. Turn everything OFF.
                         2. First, attach all cables to devices.                 2. First, remove power cords from outlets.
                         3. Attach signal cables to connectors.                  3. Remove signal cables from connectors.
                         4. Attach power cords to outlets.                       4. Remove all cables from devices.
                         5. Turn devices ON.




                                                                                                                                                               7
Matters need attention

     1.   Please use the same battery when replacing battery.
     2.   Battery abuse or mishandling can cause overheat, liquid leakage, or an explosion. To avoid possible injury, do the following:
          ˙Do not short-circuit the battery, or expose it to water or other liquids.
          ˙Heating the battery to more than 100°C (212°F)
          ˙Do not open, dissemble, or service any battery.
     3.   The power control button on the device may not completely cut off the current supplied to the device; at the same time, the device may have
          multiple power cords. To completely power off the device, make sure all power cords are disconnected.
     4.   Do not remove any component housing that has a hazard label.




                                                                                                                                                        8
3. Explosive view




                    9
No   Name                  QTY   No   Name              QTY   No   Name                     QTY
1    Main frame weldment   1     10   Controller        2     19   Full range power board   1
2    Left end cover        1     11   Shock pad         4     20   Handle                   2
3    Right end cover       1     12   Cooling fan       2     21   Ankle strap              2
4    Frame                 2     13   Speaker           2     22   Belt                     1
5    Back cover            1     14   Speaker bracket   1     23   Connecting buckle        2
6    Footboard panel       1     15   wheels            2     24   Mat                      1
7    Rope hatch            1     16   AC switch         1
8    Rope Outlet Cover     2     17   Display module    1
9    Reels module          2     18   Power cord        1




                                                                                                  10
4. Disassembly instructions



                              11
Step 1: Disassembly of the back cover

As shown in the figure below, first unscrew the four shock pads in the four-corner frame counterclockwise, and then use a Phillips screwdriver to remove the 14
screws in the circle in the figure below to uncover the back cover.




                                                                                                         Shock pad



                                                                                                          Screws




                                                                                                                                                                  12
Step 2: Disassembly of motor

*This step requires the completion of step 1 to operate.
Use a 6mm Allen wrench to remove the four screws (8 in total for two motors) shown in the figure and remove the ground wire locked on the rack and the Remove
the wire on the control assembly to complete the disassembly of the motor assembly.




                                                                                                           Screws




                                                                                                                                                                13
Step 3: Disassembly of lifting handle cover

Use a 4mm Allen wrench to remove the two screws in the frame, and then the handle cover can remove to complete the removal of the handle cover.




                                                                                                                               Screws




                                                                                                                                                  14
Step 4: Disassembly of right end cover

*This step requires the completion of steps 1,2.
First, remove the connection terminals corresponding to the fan and the speaker, and then use a Phillips screwdriver to remove the four screws in the following
circle, and then the right end cover can remove outwards.




                                                                                                                                        Screws




                                                                                                                                                                  15
Step 5: Disassembly of left end cover

*This step requires the completion of steps 1,2,3.
Remove the corresponding connector of the fan and AC switch socket, and then use a Phillips screwdriver to remove the four screws in the following circle, and
then the left end cover can remove outwards.




                                                                                                                                    Screws




                                                                                                                                                                 16
Step 6: Disassembly of full range PFC power board

Use a Phillips screwdriver to remove the three screws in the following circles and use a screwdriver to loosen all the wiring connector in the fame to completely
remove the PFC power board.




                                                                                                             Screws


                                                                                                             Wiring Connector




                                                                                                                                                                    17
Step 7: Disassembly of controller

Use a 4mm Allen wrench to remove the four bolts in the upper circle of the two electronic control components respectively and pull out all the wires on the
electronic control components.




                                                          z           z
                                                          z           z
                                                                                                              Screws
                                                          z           z
                       z           z
                                                          z           z
                       z           z

                       z           z
                       z           z




                                                                                                                                                              18
Step 8: Disassembly of display module

Use a Phillips screwdriver to remove all four screws of the display and control assembly and pull out all the wire connectors.




             z           z
             zz          zz
             z           z

                                                                                                                    Screws




                                                                                                                                 19
Step 9: Disassembly of frame

*This step needs to complete steps 1~5 to operate, it is recommended to complete step 6 before operating.
Use a 10mm open-end wrench to remove the three nuts on the two side bars respectively, with a total of six nuts, and then the frame can be removed outwards.



                z                  z                           z
                z                  z                           z
                                                                                                   Nut




                                                                                                                                                               20
Step 10: Disassembly of speaker

Use a Phillips screwdriver to remove the two screws in the circle to completely disassemble the speaker.




                                                     z                                                     Screws
                                                     z


                                                    z
                                                    z




                                                                                                                    21
Step 11: Disassembly of cooling fan

This step is recommended to complete steps 4,5 to operate.
Use a Phillips screwdriver to remove the four screws in the circle. (Four on the left end cap and two on the right end cap.)




                                                                                                                               Screws




                                                                                                                                        22
5. Circuit Diagrams




                      23
24
6. Block diagram




                   25
26
7. Key component list




                        27
No   Part number       Description
1    004.049.0052850   Power Cord, Three Plug-Suffix,VCTF/3×2.0mm2/OD8.5mm,2000mm,Black,New Certificate A12-0127-AC2+A12-0120-AC2,without PE bag, BS
2    004.036.0054297   External AC Power Socket, 3Pin, Black, Single Phase 3 C ores, DIP, With One Set of Rocker Switches, YQ
3    004.049.0052821   Ground wire, 4.8 in-line terminal TO fork terminal, 1015#16, 400mm, yellow-green, without PE bag, GXD
4    004.049.0052849   AC Power Cord, 4.8 In-line TO Fork Terminal Thickness 0.8, 1015#14, 550mm, Black, Sleeve Amorphous Magnetic Ring, Without PE Bag, GXD
5    004.049.0052894   Low voltage PFC output power cable,6.3 flag TO fork terminal, UL1015#16,1300mm, black, with 742214 and 740262 rings, without PE bag,
                       GXD
6    004.057.0054583   Single power module, rbt.pfc.01,90 to 130V,0 v-330 v, without firmware
7    004.049.0052894   PC260 Power &485 communication cable & Fan, PHS-5Y T O 2*PHSD-6Y(2*3P),2725,1200&800mm, with magnetic ring, wide buckle, tail
                       sleeve 740262 magnetic ring, SH
8    004.057.0055008   Display control, YD. ESP32,6 ~ 18V, DC5V, power station, MC U:ESP32, digital tube, KG and LBS soft cutting, onboard antenna, SK
9    004.028.0052625   Speaker,36×36×18mm,430 ~ 12000Hz,4ohm,3W,90dB, full frequency, 115mm, XH2.5, wire length 105,1 single horn,1, TDA
10   004.039.0050054   fan, CC8025H12D,80×80×25mm,12V,0.27A, PWM,37.48CFM/ min,3.17mmH2O,32.5dBA, QL
11   004.057.0054999   Speaker,36×36×18mm,430 ~ 12000Hz,4ohm,3W,90dB, full f requency,115mm, XH2.5, wire length 105,1 single horn,1, TDA
12   004.039.0052708   Motor, 98×98×167mm, DC motor, servo motor,220V,3.4A,4 000rpm,24N×m,6:1,5,80%, overseas motor, optical brining, motor body with
                       shielding cover, motor with ground wire, magnetic ring, LCJD
13   004.050.0057226   PC260 horn cable, PHS-2Y TO TJC3-2P, UL1007,350mm, without magnetic ring, set with 740141 ring, GXD
14   004.049.0052894   PC260 Power &485 communication cable & Fan, PHS-5Y T O 2*PHSD-6Y(2*3P),2725,1200&800mm, with magnetic ring, wide buckle, tail
                       sleeve 740262 magnetic ring, SH
15   004.050.0057002   AC neutral wire,4.8 terminal TO4.8 terminal, UL1015#14,60 mm, without magnetic ring,2 square wire, GXD
16   004.050.0057003   AC live wire,4.8 terminal TO4.8 terminal,1015#14,60mm, without magnetic ring, GXD




                                                                                                                                                               28
8. Detailed description of
       components




                             29
8-1 Display main board




                                 No   Port Name   Description

                                 1    CN5         RS485&12V Power connector

                                 2    CN1         Debug port
                                 3    CN6         Left Speaker port

                                 4    CN7         Right Speaker port



                             3
        1
                         2
                             4




                                                                              30
8-1-1 CN5：RS485&12V Power connector




                                      Pin   Name      Description

                                       1    12V       +12V DC Power Supply

                                       2    GND       Ground
                                       3    RS485_A   RS485_A

                                       4    RS485_B   RS485_B

                                       5    GND       Ground




                                                                             31
8-1-2 CN1：Debug port




                       Pin   Name       Description        Default

                        1    5V         DC5V               /
                        2    UART0_TX   TX                 /

                        3    UART0_RX   RX                 /

                        4    RES        MCU reset          /

                        5    GPIO0      Enter 0BOOT mode

                        6    GND        Ground




                                                                     32
8-1-3 CN6&CN7: Left & Right speaker port




                                           Pin     Name   Description                        Default

                                           CN6-1   L+     Left channel positive pole
                                           CN6-2   L-     Left channel negative electrode
                                           CN7-1   R+     Right channel positive pole

                                           CN7-2   R-     Right channel negative electrode




                                                                                                       33
8-2 Controller module




          2

                        1


                            No   Port Name   Description

                            1    CN3         AC port

                            2    CN2         Motor power port
                            3    CN6         RS485 Communication interface

                            4    CN7         Encoder port
     3


     4




                                                                             34
8-2-1 CN3：AC port




                    Pin   Name   Description   Default

                     1    L      AC_L          /
                     2    N      AC_N          /




                                                         35
8-2-2 CN2：Motor power port




                             Pin   Name   Description   Default

                              1    U      U             /

                             3     V      V             /

                             5     W      W             /




                                                                  36
8-2-3 CN6: RS485 Communication interface




                                           Pin   Name      Description            Default

                                            1    12V       +12V DC Power Supply
                                            2    GND       Ground
                                            3    RS485_B   RS485_A

                                            4    RS485_A   RS485_B
                                            5    GND       Ground




                                                                                            37
8-2-4 CN7: Encoder port




                          Pin   Name      Description   Default

                           1    ENC_Z-    ENC_Z-

                           2    ENC_Z+    ENC_Z+

                           3    ENC_B-    ENC_B-

                           4    ENC_B+    ENC_B+

                           5    ENC_A-    ENC_A-

                           6    ENC_A+    ENC_A+

                           7    ENC_5V    ENC_5V

                           8    ENC_GND   ENC_GND




                                                                  38
8-3 Controller module




                        1


                                No   Port Name   Description

                                1    CN3         AC input port

                                2    CN1         DC output port

                                3    CN2         DC output port


                            2



                            3




                                                                  39
8-3-1 CN3: AC input port




                           Pin   Name   Description                   Default

                            1    L      AC firewire input terminal       /

                            2    N      AC null line input terminal      /

                            3    PE     AC Grounding Terminal            /




                                                                                40
8-3-2 CN1 & CN2 Direct-current output port




                                             Pin     Name   Description                    Default

                                             CN1-1   L1     DC output positive terminal       /

                                             CN1-2   N1     DC output negative terminal       /

                                             CN1-3   PE1    PE ground electrode terminal      /

                                             CN2-1   L2     DC output positive terminal       /

                                             CN2-2   N2     DC output negative terminal       /

                                             CN2-3   PE2    PE ground electrode terminal      /




                                                                                                     41
8-4 Wireless control module




                              42
9. Error Messages &
  Troubleshooting




                      43
Error Code   Error message              Probable cause                           Suggested action
0x40         Power module low voltage   Defective power module/ Utility power    Restart machine. Replace module if issue not resolved.
                                        low voltage

0x80         FO control error           Power module defective/low voltage/ or   Turn off machine
                                        short circuit

0x100        Power module high          Power module overload                    Turn off machine to cool down
             temperature

0x400        High voltage               Voltage too high for control module      Turn off machine, check bleeder resistor.

0x800        Low voltage                Voltage too low for control module       Turn off machine. Check utility power voltage.

0x40000      Encoder off set error      Defective encoder or loose contact       Turn off machine and check encoder

0x80000      Encoder value error        Defective encoder or loose contact       Turn off machine and check encoder

0x400000     Encoder not connected      Defective encoder or loose contact       Turn off machine and check encoder

0x800000     Voltage unstable           Current sampling unstable voltage        Restart machine. Replace motor control board if issue is
                                                                                 not resolved.

0x4000000    UVW cord error             Cord loose contact                       Turn off machine, plug in all cords securely.

0x10000000   Braking control error      Bleeder resistor overload                Turn off machine. Turn machine back on when motor is
                                                                                 cooled.

0x40000000   Electrical load            Electrical load overload                 Turn off machine. Turn machine back on when motor is
                                                                                 cooled.




                                                                                                                                            44
