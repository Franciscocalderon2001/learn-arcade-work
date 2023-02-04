# Created by: Francisco Calderon

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.FOREST_GREEN)


def draw_pond(x, y):
    arcade.draw_ellipse_filled(180 + x, 140 + y, 150, 200, arcade.csscolor.DARK_BLUE)


def draw_house(x, y):
    arcade.draw_rectangle_filled(400 + x, 100 + y, 125, 125, arcade.csscolor.WHITE)
    arcade.draw_triangle_filled(400 + x, 250 + y, 320 + x, 140 + y, 485 + x, 140 + y, arcade.csscolor.BROWN)
    arcade.draw_arc_filled(400 + x, 38 + y, 70, 100, arcade.csscolor.BLANCHED_ALMOND, 0, 180)
    arcade.draw_circle_filled(435 + x, 110 + y, 20, arcade.csscolor.BLACK)  # big circles
    arcade.draw_circle_filled(365 + x, 110 + y, 20, arcade.csscolor.BLACK)  # big circles
    arcade.draw_circle_filled(435 + x, 110 + y, 18, arcade.csscolor.LIGHT_GRAY)  # thin circles
    arcade.draw_circle_filled(365 + x, 110 + y, 18, arcade.csscolor.LIGHT_GRAY)  # thin circles
    arcade.draw_circle_filled(410 + x, 50 + y, 4, arcade.csscolor.BLACK)  # small circles
    arcade.draw_circle_filled(390 + x, 50 + y, 4, arcade.csscolor.BLACK)  # small circles
    arcade.draw_rectangle_filled(400 + x, 63 + y, 4, 50, arcade.csscolor.BLACK)


def draw_mountain(x, y):
    arcade.draw_polygon_filled(((500 + x, 450 + y),
                                (400 + x, 390 + y),
                                (360 + x, 300 + y),
                                (630 + x, 300 + y),
                                (590 + x, 390 + y)
                                ),
                               arcade.csscolor.SADDLE_BROWN)


def draw_dark_mountain(x, y):
    arcade.draw_polygon_filled(((500 + x, 450 + y),
                                (400 + x, 390 + y),
                                (360 + x, 300 + y),
                                (630 + x, 300 + y),
                                (590 + x, 390 + y)
                                ),
                               arcade.csscolor.ROSY_BROWN)


def draw_tree(x, y):
    arcade.draw_rectangle_filled(50 + x, 300 + y, 20, 60, arcade.csscolor.ROSY_BROWN)
    arcade.draw_circle_filled(50 + x, 330 + y, 30, arcade.csscolor.DARK_GREEN)


def draw_sun(x, y):
    arcade.draw_circle_filled(500 + x, 550 + y, 40, arcade.color.YELLOW)
    arcade.draw_line(500 + x, 550 + y, 400 + x, 550 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 600 + x, 550 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 500 + x, 450 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 500 + x, 650 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 550 + x, 600 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 550 + x, 500 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 450 + x, 600 + y, arcade.color.YELLOW, 3)
    arcade.draw_line(500 + x, 550 + y, 450 + x, 500 + y, arcade.color.YELLOW, 3)


def draw_text(x, y):
    arcade.draw_text("Wonderful Day To Be Outside!",
                     10 + x, 560 + y,
                     arcade.color.BLACK, 24)


def main():
    arcade.open_window(SCREEN_HEIGHT, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_grass()
    draw_text(0, 0)
    draw_sun(70, 20)


    draw_dark_mountain(-210, 0)

    draw_mountain(-380, 0)
    draw_mountain(0, 0)

    draw_house(-220, 250)
    draw_house(100, 250)

    draw_pond(0, 0)
    draw_pond(320, 0)

    draw_tree(0, 0)
    draw_tree(0, -65)
    draw_tree(0, -130)
    draw_tree(0, -195)
    draw_tree(0, -260)
    draw_tree(0, -325)
    draw_tree(270,0)
    draw_tree(270, -65)
    draw_tree(270, -130)
    draw_tree(270, -195)
    draw_tree(270, -260)
    draw_tree(270, -325)



    arcade.finish_render()
    arcade.run()


main()
