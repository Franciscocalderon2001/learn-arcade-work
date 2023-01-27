"""
This is a program that I am using to draw using python programming
language and the Arcade library. Will be using to draw an illustration

As said in the learn academy chapter 5, Multi-line comments are surrounded
by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""
# Created by: Francisco Calderon

# These are pretty cool.
# Import math as an example

import math

print(math.cos(1))

# Import the "arcade" library...

import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)


# Draw an ellipse and rect with
# a center of (300,300)
# width of 350
# height of 200
# arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
# arcade.draw_ellipse_outline(300,300,350,200, arcade.csscolor.RED, 3)

# Drew a elliptic pond
arcade.draw_ellipse_filled(180, 140, 150, 200, arcade.csscolor.DARK_BLUE)

# House with a triangular roof and arc door, also a two windows
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 100, 150, 150, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(400, 300, 305, 175, 500, 175, arcade.csscolor.BROWN)
arcade.draw_arc_filled(400, 25, 80, 120, arcade.csscolor.BLANCHED_ALMOND, 0, 180)
arcade.draw_circle_filled(440,120,25, arcade.csscolor.BLACK)
arcade.draw_circle_filled(360,120,25, arcade.csscolor.BLACK)
arcade.draw_circle_filled(440,120,23, arcade.csscolor.WHITE)
arcade.draw_circle_filled(360,120,23, arcade.csscolor.WHITE)
arcade.draw_circle_filled(410,45,5, arcade.csscolor.BLACK)
arcade.draw_circle_filled(390,45,5, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(400, 55, 5, 60, arcade.csscolor.BLACK)

# Draw a mountain using a polygon
arcade.draw_polygon_filled(((500, 450),
                            (400, 390),
                            (360, 300),
                            (630, 300),
                            (590, 390)
                            ),
                           arcade.csscolor.SADDLE_BROWN)

# Tree with circle top all around fence of the house
arcade.draw_rectangle_filled(50, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(50,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(150, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(150,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(250, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(250,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(350, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(350,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(450, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(450,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 300, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(550,330,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 200, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(550,230,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 100, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(550,130,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 0, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(550,30,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(50, 200, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(50,230,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(50, 100, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(50,130,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(50, 0, 20, 60, arcade.csscolor.ROSY_BROWN)
arcade.draw_circle_filled(50,30,30, arcade.csscolor.DARK_GREEN)


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