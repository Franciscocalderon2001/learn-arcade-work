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


class Car:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        # Draw the car body
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)
        # Draw the wheels
        arcade.draw_circle_filled(self.position_x - 35, self.position_y - 30, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 35, self.position_y - 30, 20, arcade.color.BLACK)
        # Draw the windshield
        arcade.draw_triangle_filled(self.position_x - 40, self.position_y + 20, self.position_x + 40,
                                    self.position_y + 20, self.position_x, self.position_y + 80, arcade.color.AERO_BLUE)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the car hit the edge of the screen. If so, change direction

        if self.position_x > SCREEN_WIDTH:
            self.position_x = SCREEN_WIDTH

        if self.position_y > SCREEN_HEIGHT:
            self.position_y = SCREEN_HEIGHT


class Emoji:
    def __init__(self, position_x, position_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        # emoji face
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        # emoji eyes
        arcade.draw_circle_filled(self.position_x - 8,
                                  self.position_y + 3,
                                  4,
                                  arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 8,
                                  self.position_y + 3,
                                  4,
                                  arcade.color.BLACK)
        # emoji lips
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 10, 20, 4, arcade.color.BLACK)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.emoji = Emoji(50, 500, 20, arcade.color.YELLOW)

        self.car = Car(200, 350, 0, 0, 150, 50, arcade.color.RED)

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

        self.emoji.draw()

        self.car.draw()

    def update(self, delta_time):
        self.car.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.emoji.position_x = x
        self.emoji.position_y = y

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.car.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.car.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.change_x = 0


def main():
    window = MyGame(800, 600, "Drawing Example")

    arcade.set_background_color(arcade.color.SKY_BLUE)

    arcade.start_render()
    arcade.run()


main()
