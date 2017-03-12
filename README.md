# TeamTimothy
##Table of Contents
Intro
Components
License Terms
Connecting to the Pi Zero

##Intro
This project started as a part of [Makers Making Change's Access Makeathon] (http://www.makersmakingchange.com/accessmakeathonsummary/)
The goal is to help Timothy, a 10 year-old boy with ataxia, play his favourite games on Wii console. This project involves modifying a standard Nintendo Wii Remote and Nunchuk by replacing the buttons and joystick with larger versions and positioning them in a more ergonomic arrangement. The factory PCBs from the controllers are retained and new inputs wired to them.

##Components
For a full list of components used, see the bill of material [here](BOM.md)

##License Terms
All hardware is licensed under [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

##Connecting to the Pi Zero
The simplest way to connect to the Raspberry Pi Zero is to create an "ethernet" connection over USB using the USB port on the Pi Zero. This allows you to connect to the Pi Zero in "headless" mode without using additional adapters or peripherals. The following guide is partly based on this [Circuit Basics tutorial](http://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/) as well as other guides.

###Setting Up Your Computer
Connecting to the Pi using ethernet over USB requires the use of a Secure Shell (SSH) client and Apple's Bonjour print service. If you are using an Apple or Linux computer, your computer comes with Terminal which you can use to connect to the Pi using SSH. If you are using a Windows computer, you will need to download an SSH client like [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) in order to use SSH (from the link, download either the MSI installer or the putty.exe binary file). 
If you are using an Apple computer, Bonjour is already installed on your computer. If you are using a Windows or Linux computer, you will need to download and install Bonjour separately. [Bonjour Print Services for Windows](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) can be found on the [Apple Downloads Website](https://support.apple.com/downloads/bonjour%2520print%2520services%2520for%2520windows) (download the latest version) while Linux users can download and install the [avahi-daemon](https://linux.die.net/man/8/avahi-daemon).
Once you have an SSH client and the Bonjour service on your computer, your computer will be ready to connect to the Raspberry Pi Zero.

###Setting Up Your Pi Zero for the First Time
If your Pi Zero comes pre-installed with the software needed to act as a Wiimote controller, you can skip this step.

###Connecting to the Pi Zero over USB
Use a regular micro-USB to USB male-to-male cable or adapter (*not* an OTG adapter) to plug in your Raspberry Pi Zero to your computer. Make sure to connect the cable or adapter to the Pi Zero port marked "USB", not the one marked "PWR" (this allows you to send data and power to the Pi over USB instead of just power). Wait approximately 90 seconds for the green light on the Pi to stop blinking and for the relevant drivers to be installed on your PC (if using Windows). Using Terminal you can connect to the Pi by typing 
"ssh pi@raspberrypi.local" and pressing Enter. Using PuTTY, you can connect by typing "raspberrypi.local" into the Host Name field in putty.exe and clicking "Open" or pressing Enter. PuTTY will prompt you to login as a user, and you can enter "pi". Both Terminal and PuTTY will prompt you for the password to pi, which in this case is "0calories". You should now be connected to the Pi! If you aren't, please read the following troubleshooting section.

###Troubleshooting 
