This car controller was developed using Adafruits CircuitPython Libary found here:
https://github.com/adafruit/circuitpython
This repository includes installation instructions and a variety of other documentation.
A key advantage of this library is the baility to control  independent DC motors.

Control was achieved using a simple while loop and selection statements to capture continuous user input.

Wireless control was achieved using an SSH connection over WiFi from a remote machine to the Pi, provided both devices were on the 
same network and the IP address of the Pi is known. Once SSH connection is established, the program is simply run from the
command line on the Pi.

See README-USER for user operator instructions.

