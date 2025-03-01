# PID Demo
#
# An interactive demo of PID control. The needle will aim for a set
# location and users can manually tune the PID gains to visualize the
# effects on performance
#
# Notes:
#   * This demo is inspired by two videos:
#           https://www.youtube.com/watch?v=fusr9eTceEo&t=102s
#              https://www.youtube.com/watch?v=qKy98Cbcltw
#   * We will utilize three helper scripts that have been written by 
#     different teams
#
#   * Potentiometer readings are the raw values, they have not been scaled.
#     We will scale them to the desired gains here.
#
#   * Encoder readings are in ***ENCODER TEAM FILL THIS IN*** units
#
#
# Author:
#   YOUR NAMES HERE, and Travis Hainsworth
#   CU Boulder
#   Spring 2025

# ----------------------------------------------------------------------- #
# ---------------            Import Libraries             --------------- #
# ----------------------------------------------------------------------- #
# Used for exiting with Ctrl+C
import sys

"""
YOUR CODE HERE
"""
# Motor library:

# Other libraries: (explain what they are and why they're needed)

"""
STOP CODING
"""

# ----------------------------------------------------------------------- #
# ---------------        Import Helper Functions          --------------- #
# ----------------------------------------------------------------------- #
# Script to read potentiometers:
from knobs.py import read_p_pot, read_i_pot, read_d_pot, get_pot_limits
# Script to read switch state:
from switch.py import is_switch_on
# Script to read encoder value:
from read_encoder.py import get_encoder_position, get_encoder_limits


# ----------------------------------------------------------------------- #
# ---------------         Initialize Reference            --------------- #
# ----------------------------------------------------------------------- #
# Set the reference (a.k.a. goal) position
"""
YOU CODE HERE
"""

goal = 

"""
STOP CODING
"""

# ----------------------------------------------------------------------- #
# ---------------         Initialize the Motor            --------------- #
# ----------------------------------------------------------------------- #
# Using the i2c_simple_example.py from the pololu motoron python library's
# example:
"""
YOU CODE HERE
"""
# Initialization:

# Setting acceleration limits:

"""
STOP CODING
"""


# ----------------------------------------------------------------------- #
# ---------------    Take Note of our Hardware Limits     --------------- #
# ----------------------------------------------------------------------- #
# Potentiometer limits:
min_pot, max_pot = get_pot_limits()

# Encoder limits:
min_encoder, max_encoder = get_encoder_limits()



# ----------------------------------------------------------------------- #
# ---------------            Map Pots to Gains            --------------- #
# ----------------------------------------------------------------------- #
# Here we map the raw potentiometer readings to our desired gains. This will
# be a function that can be called and will return all three PID gains
def get_gains():
    p_min = 0
    i_min = 0
    d_min = 0

    """
    YOU CODE HERE
    """
    p_max = 
    i_max = 
    d_max = 

    """
    STOP CODING
    """

    # Read the current pot position (this script was written in "knobs.py"):
    p_pot = read_p_pot()
    i_pot = read_i_pot()
    d_pot = read_d_pot()

    # Set the gains using a linear mapping bounded by the min_pot, max_pot, 
    # p_min, p_max, p_pot
    """
    YOU CODE HERE
    """
    p_gain = 
    i_gain = 
    d_gain = 

    """
    STOP CODING
    """

    return p_gain, i_gain, d_gain 



# ----------------------------------------------------------------------- #
# ---------------              Do the Thing!              --------------- #
# ----------------------------------------------------------------------- #
# We'll put this in a try loop in case we need to exit for some reason

try:
    print("Press Ctrl+C to exit")

    # Only run the code when the switch is turned on (this script was 
    # written in "switch.py"):
    while is_switch_on():

        # Get current position (this script was written in "read_encoder.py")
        position = get_encoder_position()

        # Calculate error
        error = goal - position

        # Get current gains (this function was written a few sections above)
        p, i, d = get_gains()

        # Do something with it:
        """
        YOU CODE HERE
        """
        # in addition the the five variable just above, you might want 
        # to use:
        #   mc.set_speed(1, speed_value)
        #   min_encoder and/or max_encoder

        """
        STOP CODING
        """





except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)