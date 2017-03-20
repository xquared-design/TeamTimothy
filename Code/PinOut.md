# RPi Zero GPIO Pinout Mapping

## Inputs

### Red buttons
Button | Physical Pin # | (BCM) Pin Name.
--- | --- | ---
1 | 11 | GPIO17
2 | 13 | GPIO27
3 | 15 | GPIO22 
4 | 29 | GPIO5 
5 | 31 | GPIO6

### Joystick button
Button | Physical Pin # | (BCM) Pin Name.
--- | --- | ---
6 | 37 | GPIO26

## Outputs (WiiMote buttons)

Button | Physical Pin # | (BCM) Pin Name.
--- | --- | ---
A | 12 | GPIO18
B | 16 | GPIO23
C | 18 | GPIO24 
Z | 22 | GPIO25
 
## VCC and GND Connections

Purpose | Physical Pin #s | (BCM) Pin Name.
--- | --- | ---
Power WiiMote | 1, 17| 3.3V
Ground WiiMote| 9, 25, 39 | GND 

Check out [pinout.xyz](https://pinout.xyz/#) for an interactive pinout diagram and [this sparkfun tutorial](https://learn.sparkfun.com/tutorials/raspberry-gpio) for a detailed explanation of GPIO on the Raspberry Pi.

## Nominal button functions from left to right

C button can be in joystick (button 6)

A, B, Combo 1, Combo 2, Z (buttons 1-5)

