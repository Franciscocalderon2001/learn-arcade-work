import arcade
import random
import os
from pyglet.math import Vec2

laser_sound = arcade.load_sound(":resources:sounds/hurt3.wav")

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.4

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

VIEWPORT_MARGIN = 300

CAMERA_SPEED = 0.3
MOVEMENT_SPEED = 4

NUMBER_OF_COINS = 50

capture_sound = arcade.load_sound(":resources:sounds/coin2.wav")
arcade.play_sound(capture_sound)


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


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None
        self.laser_list = None
        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/alien/alienBlue_front.png",
                                           SPRITE_SCALING - .2)

        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512

        # -- Set up the walls
        # Create a series of vertical walls
        for y in range(0, 1600, 64):
            for x in range(200, 1650, 210):
                if random.randrange(5) > 0:
                    wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

            # Create four bordering walls
        for x in [0, 1600]:
            for y in range(0, 1600, 64):
                wall = arcade.Sprite(":resources:images/tiles/planetMid.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in [0, 1600]:
            for x in range(0, 1600, 64):
                wall = arcade.Sprite(":resources:images/tiles/planetMid.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        # -- Randomly place coins where there are no walls
        # Create the coins
        for i in range(NUMBER_OF_COINS):

            # Create the coin instance
            coin = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING_COIN)
            laser = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_COIN + .25)
            laser = Laser(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_COIN + .25)

            laser.center_x = random.randrange(SCREEN_WIDTH)
            laser.center_y = random.randrange(SCREEN_HEIGHT)
            laser.change_x = random.randrange(-3, 4)
            laser.change_y = random.randrange(-3, 4)

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(1600)
                coin.center_y = random.randrange(1600)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

            self.laser_list.append(laser)

            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.OUTER_SPACE)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # Camera that we will use to draw all sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.laser_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()

        if len(self.coin_list) == 0:
            arcade.draw_text("Game Over",
                             300, 400,
                             arcade.color.WHITE, 30)

        # Select the camera for our GUI

        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
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

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
