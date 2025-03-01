# read_encoder
#
# A helper library to get the position of the encoder.
#
# Function:
#   get_encoder_position() - returns the position of the encoder
#   get_encoder_limits()   - returns the min and max of the encoder
#
# Notes:
#   There are many ways to accomplish this. For a not great implementation
#   see the canvas announcement "Motor Position Control"
#
#   The output is in ***ENCODER TEAM FILL THIS IN*** units
#
# Author:
#   YOUR NAMES HERE, and Travis Hainsworth
#   CU Boulder
#   Spring 2025


# ----------------------------------------------------------------------- #
# ---------------            Import Libraries             --------------- #
# ----------------------------------------------------------------------- #
"""
YOU CODE HERE
"""



# ----------------------------------------------------------------------- #
# ---------------             Initialize Pins             --------------- #
# ----------------------------------------------------------------------- #
"""
YOU CODE HERE
"""



# ----------------------------------------------------------------------- #
# ---------------            Helper Functions             --------------- #
# ----------------------------------------------------------------------- #
# The primary read function will be defined in the next section, but
# include in this section any helper functions that you need 
"""
YOU CODE HERE
"""



# ----------------------------------------------------------------------- #
# ---------------            Primary Functions            --------------- #
# ----------------------------------------------------------------------- #
def get_encoder_limits():
    """
    YOU CODE HERE
    """
    encoder_min = 
    encoder_max = 

    return encoder_min, encoder_max


def get_encoder_position():
    """
    YOU CODE HERE
    """
    return 0


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
        encoder_position = 
        
        """
        STOP CODING
        """
        # now we will print the values using f strings.
        # f strings are neat. You should look them up
        # The ":03" will print 3 digits and will fill in any excess with
        # zeros
        print(f"Encoder position: = {encoder_position:03}")


        # Sleep for half a second so that the screen doesn't just fill up
        # super quick:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)

