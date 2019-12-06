# Imports
# Adafruit CircuitPython MotorKit Library - https://github.com/adafruit/circuitpython
from adafruit_motorkit import MotorKit
import sys, tty, termios, time

# Initialize MotorKit object
kit = MotorKit()

# Constant storing initial gear 
gear = 1.0

# Function to capture keyboard character input using python stdin
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	# Returns character pressed
    return ch

# Loop to continuously scan for character input using getch()
# Some throttles are arbitrarily pos/neg based on wiring of the motors
while True:
	kit = MotorKit()
	char = getch()

	# Break out of loop to stop car/inputs
	if(char == 'p'):
		break

	# 1st gear selected using Alpha1
	if(char == '1'):
		gear = .3

	# 2nd gear selected using Alpha2
	if(char == '2'):
		gear = .6
	
	# 3rd gear selected using Alpha3 (max throttle)
	if(char == '3'):
		gear = 1.0

	# Stop all motors
	if(char == 'q'):
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
		kit.motor3.throttle = 0
		kit.motor4.throttle = 0

	# Move forwards
	if(char == 'w'):
		kit.motor1.throttle = -(gear)
		kit.motor2.throttle = gear
		kit.motor3.throttle = gear
		kit.motor4.throttle = gear

	# Skid steer left
	if(char == 'a'):
		kit.motor1.throttle = -(gear)
		kit.motor2.throttle = -(gear)
		kit.motor3.throttle = -(gear)
		kit.motor4.throttle = gear
	
	# Skid steer right
	if(char == 'd'):
		kit.motor1.throttle = gear
		kit.motor2.throttle = gear
		kit.motor3.throttle = gear
		kit.motor4.throttle = -(gear)

	# Move backwards
	if(char == 's'):
		kit.motor1.throttle = 1.0
		kit.motor2.throttle = -1.0
		kit.motor3.throttle = -1.0
		kit.motor4.throttle = -1.0

	# Front wheel drive forwards
	if(char == 'i'):
		kit.motor3.throttle = 1.0
		kit.motor4.throttle = 1.0
	
	# Read wheel drive forwards
	if(char == 'o'):
		kit.motor1.throttle = -(gear)
		kit.motor2.throttle = gear
