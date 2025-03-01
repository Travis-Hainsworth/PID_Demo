# switch
#
# A helper library to get the position of a switch.
#
# Function:
#   is_switch_on() - returns True if switch on, or false if not
#
# Notes:
#   Following this tutorial BUT with a few modifications to the code:
#   https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#
#   If you want more info on: 
#       pull up vs pull down
#       faster ways to read a button press
#       debouncing
#   then read https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
#
# Components:
#   Switch
#   1k Resistor
#
# Author:
#   YOUR NAMES HERE, and Travis Hainsworth
#   CU Boulder
#   Spring 2025
import RPi.GPIO as GPIO

# You'll notice that the pin numbers do not exactly match the GPIO numbers
# for example, pin 18 corresponds to GPIO 24. The following command sets
# the system to ready the GPIO number (i.e. 24 in this example).
GPIO.setmode(GPIO.BCM)

# ----------------------------------------------------------------------- #
# ---------------             Initialize Pins             --------------- #
# ----------------------------------------------------------------------- #
"""
YOU FILL IN THE PIN NUMBERS
"""
pin_number = 

# Now we'll initialize the pin. We'll initialize it to be using a pull down
# resistor:
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# ----------------------------------------------------------------------- #
# ---------------            Check Switch State           --------------- #
# ----------------------------------------------------------------------- #
def is_switch_on():
    """
    YOUR CODE HERE.

    return True is the switch is on, or False if it isn't
    """
    return False


# ----------------------------------------------------------------------- #
# ---------------             Test Functions              --------------- #
# ----------------------------------------------------------------------- #
# Here we will validate our code. Once we have validated it, comment out 
# this section, then our other scripts will call the above functions
import sys
import time
# We'll start with a try and except block. This will allow our code to exit
# nicely if any keyboard functions are pressed:

try:
    print("Press Ctrl+C to exit")
    while True:
        """
        YOU CODE HERE
        """
        # Call your functions:
        switch_on = 

        # Print whether the switch is on or not:
        
        """
        STOP CODING
        """

        # Sleep for half a second so that the screen doesn't just fill up
        # super quick:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)