# knobs
#
# A helper library to get the position of rotary potentiometers.
# 
# Functions:
#   read_p_pot()     - returns the position of the potentiometer assigned to p
#   read_i_pot()     - same, but for i
#   read_d_pot()     - same, but for d
#   get_pot_limits() - returns the minimum and maximum possible pot values
#
# Notes:
#   This can be done with an ADC hat (which we have), or by using resistors
#   and capacitors (which we will do here). We will be doing the second
#   method so that we get exposure to another style of circuitry. We will
#   be following this tutorial:
#   https://www.circuitbasics.com/using-potentiometers-with-raspberry-pi/ 
#   but will be slightly modifying the code to suit our needs.
#
# Components (per knob):
#   Rotary pot
#   2x 1k resistors
#   220 nf capacitor#   
#
# Author:
#   YOUR NAMES HERE, and Travis Hainsworth
#   CU Boulder
#   Spring 2025
import RPi.GPIO as GPIO
import time
import sys # This is used to exit the program with Ctrl+C

# You'll notice that the pin numbers do not exactly match the GPIO numbers
# for example, pin 18 corresponds to GPIO 24. The following command sets
# the system to ready the GPIO number (i.e. 24 in this example).
GPIO.setmode(GPIO.BCM)

# ----------------------------------------------------------------------- #
# ---------------             Initialize Pins             --------------- #
# ----------------------------------------------------------------------- #
# Each pot will need two pins
"""
YOU FILL IN THE PIN NUMBERS
"""
# Proportional pin:
p_pin_a = 
p_pin_b =

# Integral:
i_pin_a =
i_pin_b =

# Derivative:
d_pin_a = 
d_pin_b = 


# ----------------------------------------------------------------------- #
# ---------------       Note Potentiometer Limits         --------------- #
# ----------------------------------------------------------------------- #
def get_pot_limits():
    """
    YOU CODE HERE
    """
    minimum_reading =
    maximum_reading =

    return minimum_reading, maximum_reading


# ----------------------------------------------------------------------- #
# ---------------           Read Potentiometer            --------------- #
# ----------------------------------------------------------------------- #
# We will create a function that reads the potentiometer. At this point we
# are just returning the raw value of the reading.
def read_p_pot():
    value = 0
    """
    YOU CODE HERE
    """
    return value

def read_i_pot():
    value = 0
    """
    YOU CODE HERE
    """
    return value

def read_d_pot():
    value = 0
    """
    YOU CODE HERE
    """
    return value


# ----------------------------------------------------------------------- #
# ---------------             Test Functions              --------------- #
# ----------------------------------------------------------------------- #
# Here we will validate our code. Once we have validated it, comment out 
# this section, then our other scripts will call the above functions

# We'll start with a try and except block. This will allow our code to exit
# nicely if any keyboard functions are pressed:

try:
    print("Press Ctrl+C to exit")
    while True:
        """
        YOU CODE HERE
        """
        # Call your functions:
        p_val = 
        i_val = 
        d_val = 
        """
        STOP CODING
        """
        # now we will print the values using f strings.
        # f strings are neat. You should look them up
        # The ":03" will print 3 digits and will fill in any excess with
        # zeros
        print(f"P pot = {p_val:03}   I pot = {i_val:03}   D pot = {d_val:03}")

        # Sleep for half a second so that the screen doesn't just fill up
        # super quick:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)