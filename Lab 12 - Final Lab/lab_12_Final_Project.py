"""
[Tito's Maze Game]

The maze using a depth-first search maze generation algorithm from Arcade library.
https://www.algosome.com/articles/maze-generation-depth-first.html

Maze Artwork comes from https://kenney.nl
Background image comes from: https://www.freepik.com/free-vector/earth-texture_997013.htm#query=dirt%20background%20game&
position=9&from_view=search&track=robertav1_2_sidr. website is freepick.com
Background artist: Omelapics


If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.maze_depth_first
"""
import random
import arcade
# Code import timeit comes from https://docs.python.org/3/library/timeit.html, from Docs Python.
import timeit
# Code import os comes from https://www.geeksforgeeks.org/os-module-python-examples/, website name is GeeksforGeeks.
import os
# Code import tkinter as tk comes from https://docs.python.org/3/library/tkinter.html, form Docs Python.
import tkinter as tk

# These sounds were collected from Python Arcade Academy,
# URL: https://api.arcade.academy/en/latest/resources.html?highlight=backgrounds
capture_sound = arcade.load_sound(":resources:sounds/coin2.wav")
arcade.play_sound(capture_sound)
rock_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

# Organized all the values of my SPRITES
NATIVE_SPRITE_SIZE = 128
SPRITE_SCALING = 0.25
SPRITE_SIZE = int(NATIVE_SPRITE_SIZE * SPRITE_SCALING)
SPRITE_SCALING_COIN = 0.4
SPRITE_SCALING_ROCK = 0.4

# Dimensions of the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Title of the screen
SCREEN_TITLE = "Final Project"

# Movement speed of player
MOVEMENT_SPEED = 3

# Organized the number of rocks and coins
NUMBER_OF_ROCKS = 20
NUMBER_OF_COINS = 30

# Code for the maze to run properly
TILE_EMPTY = 0
TILE_CRATE = 1

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 31
MAZE_WIDTH = 31

MERGE_SPRITES = True

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 200


class StartMenu:
    def __init__(self, window):
        self.window = window

        # Created a button to start the game
        # Code came from geeksforgeeks, URL: https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/
        self.start_button = tk.Button(window, text="Welcome to Tito's Maze Game. Instructions:  "
                                                   "Move options up, down, left, right. \n"
                                                   "You have 3 lives, avoid bombs. "
                                                   "Collect all the diamonds (30 diamonds) "
                                                   "as fast as you can. \n"
                                                   "Try to beat your fastest time! You can also quit by pressing 'Q'"
                                                   " \nor restart the game by pressing 'R' "
                                                   "throughout the game.\n"
                                                   " Good luck!", command=self.start_game)
        self.start_button.pack()

        # Create a button to Start, used it as the quit button so the start button can explain the rules.
        self.quit_button = tk.Button(window, text="Start Game", command=self.quit_game)
        self.quit_button.pack()

    def start_game(self):
        # Close the start menu and start the game
        self.window.destroy()
        game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        game.setup()
        arcade.run()

    def quit_game(self):
        # Close the start menu and quit the game
        self.window.destroy()


# Create the start menu window
# Code comes from the geeksforgeeks website
root = tk.Tk()
start_menu = StartMenu(root)

# Run the start menu window
root.mainloop()


# Created class for the bombs.
class Rock(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Adjusted how fast the bombs fall down
        self.center_y -= 2

        # See if we went off-screen
        if self.top < 0:
            self.bottom = 1100


# The maze construction came from Python Arcade, for more information see this URL:
# https://www.algosome.com/articles/maze-generation-depth-first.html
# The above function _create_grid_with_cells creates a 2D grid of cells
# that can either be a crate or an empty cell.
# Odd rows and columns have empty cells, while even rows and columns have crates,
# and the border cells are crates as well.
def _create_grid_with_cells(width, height):
    """ Create a grid with empty cells on odd row/column combinations. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            if column % 2 == 1 and row % 2 == 1:
                grid[row].append(TILE_EMPTY)  # add an empty cell for odd rows and columns
            elif column == 0 or row == 0 or column == width - 1 or row == height - 1:
                grid[row].append(TILE_CRATE)  # add a crate cell for border rows and columns
            else:
                grid[row].append(TILE_CRATE)  # add a crate cell for even rows and columns
    return grid


# The make_maze_depth_first function generates a maze using a depth-first algorithm.
# The maze is based on the grid created by the _create_grid_with_cells function.
# The vis array keeps track of visited cells, and
# the walk function uses recursion to visit neighboring cells, and remove crates between cells that are connected.
# The random.shuffle(d) randomizes the order in which the neighboring cells are visited,
# leading to a unique maze each time the function is called.
# The returned maze is a 2D array where crates represent walls, and empty cells represent paths in the maze.
def make_maze_depth_first(maze_width, maze_height):
    maze = _create_grid_with_cells(maze_width, maze_height)

    w = (len(maze[0]) - 1) // 2
    h = (len(maze) - 1) // 2
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    def walk(x: int, y: int):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        random.shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                maze[max(y, yy) * 2][x * 2 + 1] = TILE_EMPTY
            if yy == y:
                maze[y * 2 + 1][max(x, xx) * 2] = TILE_EMPTY

            walk(xx, yy)

    walk(random.randrange(w), random.randrange(h))

    return maze


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Set start time for the timer
        self.start_time = 0

        # Organize all my sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.rock_list = None

        # Player info
        self.health = 3
        self.score = 0
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Used to scroll in the game
        self.view_bottom = 0
        self.view_left = 0

        # Time to process
        self.processing_time = 0
        self.draw_time = 0

        self.background = arcade.load_texture("/Users/mirkocalderon/Downloads/earth-texture/696 Large.png")

        self.restart_game = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        self.start_time = timeit.default_timer()

        # Info for player
        self.score = 0
        self.health = 3

        # Create the maze
        maze = make_maze_depth_first(MAZE_WIDTH, MAZE_HEIGHT)

        # Create sprites based on 2D grid
        if not MERGE_SPRITES:
            # This is the simple-to-understand method. Each grid location
            # is a sprite.
            for row in range(MAZE_HEIGHT):
                for column in range(MAZE_WIDTH):
                    if maze[row][column] == 1:
                        wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
                        wall.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                        wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                        self.wall_list.append(wall)
        else:
            # This uses new Arcade 1.3.1 features, that allow me to create a
            # larger sprite with a repeating texture. So if there are multiple
            # cells in a row with a wall, we merge them into one sprite, with a
            # repeating texture for each cell. This reduces our sprite count.
            for row in range(MAZE_HEIGHT):
                column = 0
                while column < len(maze):
                    while column < len(maze) and maze[row][column] == 0:
                        column += 1
                    start_column = column
                    while column < len(maze) and maze[row][column] == 1:
                        column += 1
                    end_column = column - 1

                    column_count = end_column - start_column + 1
                    column_mid = (start_column + end_column) / 2

                    wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING,
                                         repeat_count_x=column_count)
                    wall.center_x = column_mid * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.width = SPRITE_SIZE * column_count
                    self.wall_list.append(wall)

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer"
                                           "/maleAdventurer_walk5.png",
                                           SPRITE_SCALING + .02)
        self.player_list.append(self.player_sprite)

        # Randomly place the player. If we are in a wall, repeat until we aren't.
        placed = False
        while not placed:

            # Randomly position
            self.player_sprite.center_x = random.randrange(MAZE_WIDTH * SPRITE_SIZE)
            self.player_sprite.center_y = random.randrange(MAZE_HEIGHT * SPRITE_SIZE)

            # Are we in a wall?
            walls_hit = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
            if len(walls_hit) == 0:
                # Not in a wall! Success!
                placed = True

        for i in range(NUMBER_OF_ROCKS):
            # Create Rock instance
            rock = arcade.Sprite(":resources:images/tiles/bomb.png", SPRITE_SCALING_ROCK - .02)

            rock = Rock(":resources:images/tiles/bomb.png", SPRITE_SCALING_ROCK - .02)

            rock.center_x = random.randrange(SCREEN_WIDTH + 300)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = random.randrange(-3, 4)
            rock.change_y = random.randrange(-3, 4)

            self.rock_list.append(rock)

        for i in range(NUMBER_OF_COINS):
            # Create the coin instance
            coin = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING_COIN)

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                row = random.randrange(MAZE_HEIGHT)
                column = random.randrange(MAZE_WIDTH)
                if maze[row][column] == TILE_EMPTY:
                    coin_placed_successfully = True
                    coin.center_x = (column * SPRITE_SIZE) + (SPRITE_SIZE / 2)
                    coin.center_y = (row * SPRITE_SIZE) + (SPRITE_SIZE / 2)
                    self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        print(f"Total wall blocks: {len(self.wall_list)}")

    def draw_timer(self):
        elapsed_time = int(timeit.default_timer() - self.start_time)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background image
        arcade.draw_lrwh_rectangle_textured(-400, - 400, 1800, 1800, self.background)

        self.draw_timer()

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.rock_list.draw()

        if self.health == 0:
            arcade.draw_text("Game Over",
                             self.view_left + 350,
                             SCREEN_HEIGHT - 375 + self.view_bottom,
                             arcade.color.WHITE, 40)
            arcade.draw_text("Press 'Q' to quit",
                             self.view_left + 320,
                             SCREEN_HEIGHT - 425 + self.view_bottom,
                             arcade.color.WHITE, 40)
            return

        if len(self.coin_list) == 0:
            arcade.draw_text("You Win!",
                             self.view_left + 350,
                             SCREEN_HEIGHT - 400 + self.view_bottom,
                             arcade.color.WHITE, 40)
            arcade.draw_text("Try to get a faster time!",
                             self.view_left + 250,
                             SCREEN_HEIGHT - 450 + self.view_bottom,
                             arcade.color.WHITE, 30)

        # Draw info on the screen
        sprite_count = len(self.wall_list)

        elapsed_time = int(timeit.default_timer() - self.start_time)

        output = f"Health Count: {self.health}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 640 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Time: {elapsed_time:02d}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 660 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Score Count: {self.score}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 680 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Sprite Count: {sprite_count}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 20 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 40 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 60 + self.view_bottom,
                         arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

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
        elif key == arcade.key.Q:
            arcade.close_window()
        elif key == arcade.key.R:
            self.restart_game = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.health == 0:
            return

        if len(self.coin_list) == 0:
            return

        start_time = timeit.default_timer()

        if self.restart_game:
            self.setup()
            self.restart_game = False

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.coin_list.update()
        self.rock_list.update()

        rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.rock_list)

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        for rock in rock_hit_list:
            rock.remove_from_sprite_lists()
            self.health -= 1
            arcade.play_sound(rock_sound)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(capture_sound)

        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Save the time it took to do this.
        self.processing_time = timeit.default_timer() - start_time


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    root = tk.Tk()
    start_menu = StartMenu(root)
    main()
