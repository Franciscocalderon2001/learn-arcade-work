"""
This is a program that I am using to draw using python programming
language and the Arcade library.

As said in the learn academy chapter 5, Multi-line comments are surrounded
by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# these are pretty cool.
# import math as an example

import math

print(math.cos(1))

# Import the "arcade" library...

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.

arcade.run()