# Magnetic Stirring Module
# Overview
Magnetic stirring is a commonly used method in chemistry experiments. Through a magnetic field in the stirrer, a stir bar spins quickly to mix components in a flask/vial, creating a uniform mixture and increasing the rate of reactions. This repository contains instructions / materials / code for creating a low-cost stirring module which is programmable and compatible with the Opentrons liquid handler deck slots, so it can be incorporated in automated workflows in self-driving labs (SDLs).


### Authors
Monique Ngan, Lab Technician \
Owen Alfred Melville, Staff Scientist\
*The 3D design was inspired by SDL 5 \
[Acceleration Consortium](https://acceleration.utoronto.ca/)

## Summary of Steps
1. Order the required parts 
2. 3D Print the case
3. Assemble the electronic components
4. Run code to operate the stirring module


## Tools Required For this Project
- [Soldering Iron](https://www.amazon.ca/Weller-Soldering-Station-WLACCBSH-02-Silicone/dp/B08MC4HVTR?th=1)
- [Heat Gun](https://www.amazon.ca/Mini-Heat-Shrink-Gun-Dual-Temp-dp-B09TYM45BH/dp/B09TYM45BH/ref=dp_ob_title_hi)
- [Wire cutters](https://www.amazon.ca/BOOSDEN-Crafting-Spring-Loaded-Plastics-Clippers/dp/B08ZCHYGN7/?th=1)
- [3D printer](https://ca.store.bambulab.com/products/p1s?srsltid=AfmBOorLX7Ki2ZaYaFx6AWRBcr8wJq_0mTlmHkm-IWXz0sfFRXeNtMNX)

## Required skills
- Soldering
- Basic Python Coding

# Step 1: Order Required Parts
These are the materials required for the current design of the stirring module which holds 6 vials. Please note prices may vary over time.

| Item | Supplier | Part Number | Number | Cost (CAD) | Total Cost (CAD) |
| ---- | ----| ----| ----| ----| ----|
| [Raspberry Pi Pico](https://www.pishop.ca/product/raspberry-pi-pico-wh-pre-soldered-headers/) | PiShop | 402-1 | 1 | 9.80 | 9.80 |
| [Raspberry Pi Grove Shield](https://www.digikey.ca/en/products/detail/seeed-technology-co-ltd/103100142/13688265?s=N4IgTCBcDaIIwFYCcB2AtHADAZi5uALGGgHIAiIAugL5A) | DigiKey | 1597-103100142-ND | 1 | 6.32 | 6.32 |
| [25mm x 25mm Square Fan](https://www.digikey.ca/en/products/detail/sunon-fans/MF25100V1-1000U-A99/7805269) | DigiKey | 259-1830-ND | 6 | 14.71 | 88.26 |
| [Barrel Power Connector](https://www.digikey.ca/en/products/detail/same-sky-formerly-cui-devices/PJ-102AH/408448) | DigiKey | CP-102AH-ND | 1 | 1.14 | 1.14 |
| [5V Barrel Power Supply](https://www.digikey.ca/en/products/detail/tri-mag-llc/L6R06H-050/7682614) | DigiKey | 364-1251-ND | 1 | 10.15 | 10.15 |
| [NPN Transistor](https://www.digikey.ca/en/products/detail/nexperia-usa-inc/PZT2222A-115/1158011?s=N4IgTCBcDaIIwHYwILQBYwFYwrigBAHIAiIAugL5A) | DigiKey | 1727-4252-1-ND | 1 | 0.80 | 0.80 |
| [USB A to Micro B Cable](https://www.digikey.com/en/products/detail/cvilux-usa/DH-20M50056/13177301) | DigiKey | DH-20M50056 | 1 | 3.33 | 3.33 |
| [**5V Diode INSERT LINK**]() | DigiKey | DH-20M50056 | 1 | 2.08 | 2.08 |

### Materials Required - Kits
These materials come in kits, so you may not need them if you already have similar materials. They can be used for other projects as well.
| Item | Supplier | Cost (CAD) | Total Cost (CAD) |
| ---- | ----| ----| ----|
| [PCB Boards](https://www.amazon.ca/BOJACK-6-Prototype-Soldering-Compatible-Arduino/dp/B091PZQ4W7/) | Amazon Canada | 21.99 | 21.99 |
| [Metal Magnets](https://www.amazon.ca/Magnets-Refrigertor-Whiteboard-Durable-Multi-Use/dp/B07BJFD6FL/?th=1) | Amazon Canada | 9.99 | 9.99 |
| [Resistors](https://www.amazon.ca/Resistor-Assorted-Resistors-Assortment-Experiments/dp/B07L851T3V/?th=1) | Amazon Canada | 16.99 | 16.99 |
| [Solder Seal Connectors](https://www.amazon.ca/Kuject-Connectors-Waterproof-Electrical-Automotive/dp/B073RMRCC3/?th=1) | Amazon Canada | 17.99 | 17.99 |


### Generic Materials Required
- Solder
- Wires (at least Red & Black)
- Filament for 3D Printing ([PLA](https://ca.store.bambulab.com/products/pla-basic-filament?gad_source=1&gclid=Cj0KCQjwpP63BhDYARIsAOQkATYc5jM-nciSOOw8pbxHA_WIkh3n5OJYfMMvQm4q8-BjsxyQY5-RIlQaAhdqEALw_wcB), [PETG](https://ca.store.bambulab.com/collections/petg/products/petg-hf))

## Photo of Materials
<img src="https://github.com/user-attachments/assets/f905ab22-6efc-444d-a480-7640467af008" width = "468" height = "600">

# Step 2: 3D Print the stirring module casing and electronics casing.
In this repo, you can find `.stl` which are 3D printing files for the casing of the stirring module (designed for electrochemical cell vials with a 28mm diameter) and the _optional_ electronics case which holds and organizes the Raspberry Pi (RPi) & PCB.

`Stirring_Module.f3d` is an editable 3D Printing File containing both the lid and base, so it can be redesigned to fit your needs.

| File Name | Purpose | Filament | Printing Considerations |
| ---- | ----| ----| ----|
| Stirring Module Base.stl | Holds the fans used for stirring | PLA | Print with normal supports.|
| Stirring Module Lid.stl | Holds the vials on top of fans | PLA | Print with the cylinders for the vials facing downwards, with normal supports.|
|Electronics Casing/Pico Holder_MainBody v2.stl| Holds RPi Grove Shield & RPi | PETG | N/A |
|Electronics Casing/Pico Holder_Main_Lid v4.stl| Lid for the Main Component | PETG | N/A |
|Electronics Casing/Pico Holder_Port_Door_Back.stl| Slides into the back of the PCB holding component | PETG| N/A |
|Electronics Casing/Pico Holder_Port_Door_Stirring_Module v2.stl| Slides into the front of the PCB holding component | PETG| Orient with side saying "PORT" facing up |
|Electronics Casing/Pico Holder_Port_Modular v11.stl| Hold the PCB | PETG| N/A|
|Electronics Casing/Pico_Aux_Lid_Snap.stl| Snaps onto the top of PCB holding component | PETG| N/A|

# Step 3: Assemble Components
## 3a: Assemble the PCB Board
### Parts Required
- PCB board from Kit (60x40 mm)
- Wires 
- 1x 1000 Ohm resistor
- 1x 5.6 Ohm resistor
- 1x 390 Ohm resistor
- 1x NPN Transistor
- 1x 5V diode
- 1x Power Barrel Connector
- 2x Heat Shrink Connector

### Circuit Diagram
![stirring_module_circuit](https://github.com/user-attachments/assets/ab85338e-2480-4929-9b23-1145f1889081)
(an image of the soldered PCB is attached below)

### Soldering Steps
The following written instructions will give a description of the circuit diagram. If you are familiar with electronics, feel free to just solder the circuit diagram. 

1. Mount the power connector in the top left corner of the PCB and solder in a 1000 Ohm resistor between the power and ground sides. This creates a power port, where the pin that is at the back of the barrel connector is your +5V pin, and the pin closer to the opening is the ground.
   
2. The GPIO ground pin wire can be a bare wire or a wire with an open pin. Solder in one end of the wire into the PCB in series between the ground of the barrel connector and the resistor (See diagram). This wire will be connected to the RPi Grove Shield in a later step.

3. For the NPN transistor, the drawing below shows the schematic (with the trapezoidal part that sticks out facing forward). Pin 1 (base) goes to the 390 Ohm resistor that eventually goes to the RPi GPIO pin.  Pin 2 (collector) goes to the fans and power supply. Pin 3 (emitter) goes to ground. 

4. Similar to the GPIO ground pin, one end of the short wire (bare or with open pin) is soldered in series with the 330 Ohm resistor and the emitter pin from the transistor.
   
5. For the diode, orient it so the silver bar (which indiciates the cathode) points towards the +5V side of the current going into the fan. The diode is used to protect the circuit from the reverse flow of voltage after the fan is turned off, as rotational motors create a magnetic and energetic field which can flow in the opposite direction of the current, damaging the circuit. This way, it will flow back into the fan, using up the energy.

6. For the wires that connect to the fan, solder in black and red wire, for the ground and + terminals respectively. We connect these to the fan wires in the next step.

## 3b: Connecting PCB to Fans
1. Place the fans into the slots in the base piece of the casing. Thread the wires through the hole at the bottom of the slot and collect the wires of the fans in the row at one end of the case.
2. Combine all the black wires (ground) together by twisting the exposed wires together securely. You should have the same number of black wires and the number of fans. Repeat this step for all the red wires.
3. Use a heat shrink connector to solder together the combined black wires with the "Black Fans" wire from the PCB. Repeat for the red wire and the "Red Fans" wire.

## 3c: Assemble PCB & Raspberry Pi
The last step to setting up is connecting the GPIO wires to the Raspberry Pi. The electronic casing (optional) can be printed and used to organize the wires in the project. Slide the side module in with the central square unit.
1. Place the Raspberry Pi on the Rasperry Pi Grove Shield. Optionally, place the grove shield and PCB into the square unit and side unit of the electronic casing.
2. Connect the RPi GPIO Pin 0 to the "GP0" slot on the RPi Grove shield. If using the electronic casing, thread the wire through one of the honeycombs in the side panel.
3. Connect the RPi Ground Pin to any slot that says "GND" on the RPi Grove shield.

#### Image of Soldered Circuit + RPi
<img src="https://github.com/user-attachments/assets/ffd1aeaa-bdd7-4fed-9f0c-01aae3cf2324" width = "500" height = "286">

## 3d: Assemble Electronics Casing (Optional)
Finally, insert the side panels into the side module and put on the lids to complete the assembly of the electronics.

# Step 4:  Operating the Stirring Module
1. Download Visual Studio Code (VS Code) and Python.
2. Download the MicroPico Extension in VS Code, which will be used to communicate with the RPi.
3. Plug in the micro USB-B end of the cable into the RPi and the USB-A end into your computer, while pressing the BOOTSEL button on the RPi. This should open a file directory for the RPi on your computer.
4. **Flash the RPi** by downloading the [UF2 file for the RPi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) and transferring the file into the RPi's directory. The file directory should disappear from your files explorer. Unplug and replug the RPi to your computer.
5. Download `stirring_module.py` and open it in VS Code. Feel free to edit this script to accomodate for different uses, for example for changing the stir speed and duration. 

This program contains methods for operating the fan, which are described below and also documented in comments within the script. These methods are called in a try-escape block (to be uncommented out in the code) where the program can be stopped by pressing `ctrl+c` on the keyboard. 
- `initialize_fans()`: This function is for initializing pulse width modulation (PWM) at the given GPIO pin where the fans are connected to. Be sure to save the returned object as it will be required for calling the subsequent functions.
- `stir()`: commands the fans to stir at a given power (1-100) which is controlled through pwm signals, for a designated amount of time in _minutes_.
- `stop()`: stops the fans
- `fans.deinit()`: deinitializes the signal for the pin. It is to be used at the very end of the program.
- `initialize_and_stir()`: contains all of the above functions in order, for easier operation

6. To run the file, right click in the editor and select **"Upload file to Pico"** and **"Run File on Pico"** afterwards. Be sure to **uncomment** the try-escape block to run the methods described.

7. Optionally, the module can be run without using the MicroPico REPL terminal, using the Python subpackage module. Download and run `stirring_module_controller.py`, where `run_stirring_module()` will call `initialize_and_stir()` with the given parameters.
      -  Note that `stirring_module.py` needs to be uploaded to the RPi and the Pico needs to be disconnected. As well, the **COM number** needs to be edited.

*🎉🎉Congratulations you are all set for using the stirring module!*

## Tested Power Values for Solutions of Various Viscosities
- Minimum power: **45** for all fans to turn on. Lower than this, only some fans will operate.
- Maximum power: **92**. Higher than this, the fans turn too quickly and the whole module starts to shake.

| Solution (listed in increasing viscosity) | Micro Stir Bar | Larger Stir Bar (514) |
| ---- | ----| ----|
| Acetone | 45-75 | 60-75 (80 starts to bounce) |
| Water  | 45-70 | 60-90 |
| 0.1% PEG in water  | 45-80 | 50-80 |
| 10% PEG in water  | 45-85 | 60-85 |
| 25% PEG in water  | 70-92 (for all speeds - mainly vibrates and doesn't stir well) | 70-80 |
| 50% PEG in water | Not possible | Not possible (70 moves very slowly, still only vibrating at 92) |

## Trouble Shooting Common Errors
**Error 1**: Trouble Connecting to RPi (when using the MicroPico Extension in VSCode)
![Screenshot of Micropico Connection Error](https://github.com/user-attachments/assets/304d4ee8-6075-4c89-b44c-f000ccae95ec)
or a `error running on raw repl` \
=> Restart VSCode. If this does not help, restart your computer.\
Other potential solutions: uninstall / reinstall MicroPico extension & check if the RPi is connected (Windows > Device Manager > Ports, To see if RPi is connected via USB) 

**Error 2**: COM in use (when using subprocess to operate RPi) \
Ensure the RPi is disconnected in the MicroPico REPL terminal, as both can not be connected at the same time.

## Current Limitations & Future Work
- Currently, the inidividual fans are spinning at slightly different speeds which is important to note for lower stir speeds as some fans may stop stirring as it does not have enough power. Future prototypes should work on improving electrical connections to the fans, as this is the suspected reason for this issue.








