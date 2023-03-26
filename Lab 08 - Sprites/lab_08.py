""" Sprite Sample Program """

import random
import arcade

laser_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
arcade.play_sound(laser_sound)

capture_sound = arcade.load_sound(":resources:sounds/coin2.wav")
arcade.play_sound(capture_sound)

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
COIN_COUNT = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lab 8"


# Red laser class
class Laser(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y -= 1

        # See if we went off-screen
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprites lists.
        self.player_list = None
        self.coin_list = None
        self.laser_list = None

        # Player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # Create coins
        for i in range(COIN_COUNT):
            laser = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_COIN + .25)

            laser = Laser(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_COIN + .25)

            coin = arcade.Sprite(":resources:images/alien/alienBlue_jump.png", SPRITE_SCALING_COIN)

            coin = Coin(":resources:images/alien/alienBlue_jump.png", SPRITE_SCALING_COIN)

            # position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            laser.center_x = random.randrange(SCREEN_WIDTH)
            laser.center_y = random.randrange(SCREEN_HEIGHT)
            laser.change_x = random.randrange(-3, 4)
            laser.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

            self.laser_list.append(laser)

    def on_draw(self):

        arcade.start_render()
        self.laser_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        if len(self.coin_list) == 0:
            arcade.draw_text("Game Over",
                             300, 400,
                             arcade.color.WHITE, 30)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.coin_list) == 0:
            return
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.laser_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        laser_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.laser_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(capture_sound)

        for laser in laser_hit_list:
            laser.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(laser_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
