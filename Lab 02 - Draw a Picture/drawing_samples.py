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

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

#Tree Trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#Tree top
arcade.draw_circle_filled(100,350,30, arcade.csscolor.DARK_GREEN)



# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.

arcade.run()