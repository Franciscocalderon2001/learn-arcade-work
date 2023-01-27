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

# Tree Trunk
arcade.draw_rectangle_filled(100, 300, 20, 60, arcade.csscolor.ROSY_BROWN)

# Tree top
arcade.draw_circle_filled(100,330,30, arcade.csscolor.DARK_GREEN)

# Draw an ellipse and rect with
# a center of (300,300)
# width of 350
# height of 200
# arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
# arcade.draw_ellipse_outline(300,300,350,200, arcade.csscolor.RED, 3)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 100, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 150, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with trunk and arc for top
# Arc is centered at (300, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(300, 300, 20, 60, arcade.csscolor.BROWN)
arcade.draw_arc_filled(300, 320, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 100, 150, 150, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(400, 300, 305, 175, 500, 175, arcade.csscolor.BROWN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 300, 10, 60, arcade.csscolor.SANDY_BROWN)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Beautiful Sunny Day!",
                 50, 500,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.

arcade.run()