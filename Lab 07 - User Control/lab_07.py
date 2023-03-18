import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.FOREST_GREEN)


def draw_street():
    arcade.draw_line(0, 300, 800, 300, arcade.color.BLACK, 10)


def draw_pond(x, y):
    arcade.draw_ellipse_filled(180 + x, 140 + y, 400, 185, arcade.csscolor.DARK_BLUE)


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


def draw_car(x, y):
    arcade.draw_rectangle_filled(300, 370, 100, 100, arcade.color.RED)
    arcade.draw_rectangle_filled(300, 340, 200, 50, arcade.color.RED)
    arcade.draw_rectangle_filled(325, 380, 50, 30, arcade.color.BLEU_DE_FRANCE)
    arcade.draw_rectangle_filled(385, 345, 30, 15, arcade.color.YELLOW)


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BLACK_LEATHER_JACKET)

    def on_draw(self):
        """ Called whenever we need to draw the window. """

        arcade.start_render()
        draw_grass()

        draw_sun(275, 20)

        draw_pond(200, 0)

        draw_dark_mountain(-200, 0)
        draw_dark_mountain(150, 0)

        draw_mountain(-380, 0)
        draw_mountain(0, 0)
        draw_mountain(300, 0)

        draw_street()

        draw_car(0, 0)

        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(800, 600, "Drawing Example")

    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()
    arcade.run()


main()
