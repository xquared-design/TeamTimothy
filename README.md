# TeamTimothy
##Table of Contents
1. Intro
2. Components
3. License Terms
4. Connecting to the Pi Zero

##Intro
This project started as a part of [Makers Making Change Access Makeathon](http://www.makersmakingchange.com/accessmakeathonsummary/), an initiative of the [Neil Squire Society](http://www.neilsquire.ca).
The goal is to help Timothy, a 10 year-old boy with ataxia, play his favourite games on Wii console. This project involves modifying a standard Nintendo Wii Remote and Nunchuk by replacing the buttons and joystick with larger versions and positioning them in a more ergonomic arrangement. The factory PCBs from the controllers are retained and new inputs wired to them. The code is executed using a Raspberry Pi Zero with Raspbian. 

##Components
For a full list of components used, see the bill of material [here](BOM.md).

##License Terms
All hardware is licensed under [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

##Connecting to the Pi Zero
The following sections are partly based on this [Circuit Basics tutorial](http://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/) and on other guides.

The simplest way to connect to the Raspberry Pi Zero is to create an "ethernet" connection over USB using the USB port on the Pi Zero. This allows you to connect to the Pi Zero in "headless" mode without using additional adapters or peripherals.

###Setting Up Your Computer
Connecting to the Pi using ethernet over USB requires the use of a Secure Shell (SSH) client and Apple's Bonjour print service. If you are using an Apple or Linux computer, your computer comes with Terminal which you can use to connect to the Pi using SSH. If you are using a Windows computer, you will need to download an SSH client like [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) in order to use SSH (from the link, download either the MSI installer or the putty.exe binary file). 

If you are using an Apple computer, Bonjour is already installed on your computer. If you are using a Windows or Linux computer, you will need to download and install Bonjour separately. [Bonjour Print Services for Windows](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) can be found on the [Apple Downloads Website](https://support.apple.com/downloads/bonjour%2520print%2520services%2520for%2520windows) (download the latest version) while Linux users can download and install the [avahi-daemon](https://linux.die.net/man/8/avahi-daemon).

Once you have an SSH client and the Bonjour service on your computer, your computer will be ready to connect to the Raspberry Pi Zero.

###Setting Up Your Pi Zero for the First Time
If your Pi Zero comes pre-installed with the software needed to act as a Wiimote controller, you can skip this step.

###Connecting to the Pi Zero over USB
Use a regular micro-USB to USB male-to-male cable or adapter (*not* an OTG adapter) to plug in your Raspberry Pi Zero to your computer. Make sure to connect the cable or adapter to the Pi Zero port marked "USB", not the one marked "PWR" (this allows you to send data and power to the Pi over USB instead of just power). Wait approximately 90 seconds for the green light on the Pi to stop blinking and for the relevant drivers to be installed on your PC (if using Windows). 

Using Terminal you can connect to the Pi by typing `ssh pi@raspberrypi.local` and pressing Enter. Using PuTTY, you can connect by typing `raspberrypi.local` into the Host Name field in putty.exe and clicking "Open" or pressing Enter. PuTTY will prompt you to login as a user and you should enter `pi`. Both Terminal and PuTTY will prompt you for the password to pi, which in this case is `0calories`. You should now be connected to the Pi! If you aren't, please read the following section, otherwise please skip to the "Setting Up a Shared Internet Connection on Windows" section.

####Installing RNDIS Drivers on Windows
You may get the following error message when connecting to the Pi: 
>Unable to open connection to raspberrypi.local
>Host does not exist

If you have made sure that you are using a non-OTG USB cable connected to the USB port of the Pi Zero, you have installed the necessary software on your Windows computer and Pi and you *still* get this error, then you may need to install the RNDIS drivers. With the Pi still connected to the computer, open "Windows Device Manager" and locate the Pi under "Other Devices" as "RNDIS/Ethernet Gadget". Right-click on it and click "Update Driver Software...". Click "Browse my computer for driver software" in the window that opens up and click "Let me pick from a list of device drivers on my computer" in the following window. Scroll down the list that appears, select "Network Adapters", and click "Next". Scroll down the Manufacturer list on the left side and click "Microsoft", then scroll down the list on the right side and click "Remote NDIS Compatible Device" and click "Next". Click "Yes" in the warning that appears and wait for the driver to finish installing. Once installation is complete, you should see a window that confirms that Windows has sucessfully updated your driver software. You should now be able to log in to your Pi with PuTTY using raspberrypi.local.

###Setting Up a Shared Internet Connection on Windows
If you type `sudo ping www.google.com` when connected to the Pi, you will get an error similar to the following:
>ping: unknown host www.google.com

This is because your Pi Zero is not connected to the internet. The following steps show how to share your existing internet connection with your Pi.

With the Pi Zero still plugged in, open the "Network Connections" window. The Raspberry Pi will show up as a separate Ethernet connection with the name "Ethernet #" and labelled something similar to "USB Ethernet/RNDIS Gadget". Choose the internet connection on your computer which you want to share (for example the Wi-Fi connection), right-click it, and click "Properties". In the window that shows up, open the "Sharing" tab and check the box that says "Allow other network users to connect through this computer’s Internet connection”. Click the drop-down menu below that and find the network connection that corresponds to the Pi. Select it and then click "OK". 

The "Network Connections" window will now show your computer's internet connection as being "Shared". Reboot your Pi with `sudo reboot` and close PuTTY. Reopen PuTTY and connect to the Pi again, and after logging in enter `ifconfig`. You should see a "usb0" connection showing TX and RX packets being sent and received, showing that your Pi now has shared internet access from your computer! If you wish to test the connection further, enter `sudo ping www.google.com` to see packets being received. Press `Ctrl + C` to stop the ping output (alternatively, enter `sudo ping -c 10 www.google.com` to only ping 10 times).
