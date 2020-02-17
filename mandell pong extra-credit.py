# Author : Georgia Madell
# Date : 01/27/2020
# Assignment: Lab 1
# Class: CS1 Section 1
# Purpose: To create a pong game

from cs1lib import *
import random

img = load_image("sun.png")

# paddle dimensions
PWIDTH = 20
PHEIGHT = 80

# window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# paddle speed
P_SPEED = 7

# key press values
LEFT_UP = False
LEFT_DOWN = False
RIGHT_UP = False
RIGHT_DOWN = False

# ball velocities and positions
Y_V = 0
X_V = 0
Y_B = 190
X_B = 198

# boundaries
RIGHT_WALL=400
LEFT_WALL=0
TOP_WALL=0
BOTTOM_WALL=400

# ball radius and speed
BALL_RADIUS = 9
BALL_SPEED = 4

# initial velocities of ball
INITIAL_X_V=0
INITIAL_Y_V=0

# position of paddles
X_P_LEFT = 0
Y_P_LEFT = 0
X_P_RIGHT = 380
Y_P_RIGHT = 320

# initial position of ball
INITIAL_X_B = 198
INITIAL_Y_B = 190

# initial positions of paddles
INITIAL_LEFT_X = 0
INITIAL_RIGHT_X = 380
INITIAL_LEFT_Y = 0
INITIAL_RIGHT_Y = 320

# boolean for whether game is in progress and whether the game is over
GAME_IN_PROGRESS = False

# color of ball
BLUE = False
RED = False

START_OVER = True



# takes in keyboard input from user to move paddles and start / stop the game
def kpress(k):
    global LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN, GAME_IN_PROGRESS, START_OVER, X_B, Y_B,X_P_LEFT, Y_P_LEFT, X_P_RIGHT, Y_P_RIGHT, X_V, Y_V

    # starts new game if there is current game in play
    # begins game if there is not
    if k.lower() == ' ':

        # resets paddles and ball to initial positions
        X_B = INITIAL_X_B
        Y_B = INITIAL_Y_B
        X_P_LEFT = INITIAL_LEFT_X
        Y_P_LEFT = INITIAL_LEFT_Y
        X_P_RIGHT = INITIAL_RIGHT_X
        Y_P_RIGHT = INITIAL_RIGHT_Y

        # sets ball velocities to zero
        X_V = INITIAL_X_V
        Y_V = INITIAL_Y_V

        # starting motion- giving x velocity and y velocity of ball non-zero values
        start_game()

        # setting game progress to true makes the ball move in move_ball()
        GAME_IN_PROGRESS = True

    # if a is pressed, left paddle moves up
    if k.lower() =='a':
        LEFT_UP = True
    # if z is pressed, left paddle moves down
    if k.lower() == 'z':
        LEFT_DOWN= True
    # if k is pressed, right paddle moves up
    if k.lower() == 'k':
        RIGHT_UP = True
    # if m is pressed, right paddle moves down
    if k.lower() == 'm':
        RIGHT_DOWN = True
    if k.lower() =='q':
        cs1_quit()

# starts game by putting the ball into motion by setting x and y velocities to non zero values
def start_game():
    global X_V,Y_V, BLUE
    BLUE = True
    X_V = random.uniform(2, 4)*random.choice((-1, 1))
    Y_V = random.uniform(2, 4)*random.choice((-1, 1))


# takes in keyboard input from the user to stop the movement of the paddles
def krelease(k):
    global LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN
    # if a key is released, left paddle stops moving up
    if k.lower()=='a':
        LEFT_UP = False
    # if z key is released, left paddle stops moving down
    if k.lower() == 'z':
        LEFT_DOWN= False
    # if k key is released, right paddle stops moving up
    if k.lower() == 'k':
        RIGHT_UP = False
    # if m key is released, right paddle stops moving down
    if k.lower() == 'm':
        RIGHT_DOWN = False

#moves paddles based on key press
def move_paddles():
    global LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN, Y_P_RIGHT, Y_P_LEFT
    if LEFT_UP and Y_P_LEFT>=5:
        Y_P_LEFT-=P_SPEED
    if LEFT_DOWN and Y_P_LEFT<=315:
        Y_P_LEFT+=P_SPEED
    if RIGHT_UP and Y_P_RIGHT>=5:
        Y_P_RIGHT-=P_SPEED
    if RIGHT_DOWN and Y_P_RIGHT<=315:
        Y_P_RIGHT+=P_SPEED

# checks if the ball has moved beyond the right wall
def moved_beyond_right():
    if (X_B+BALL_RADIUS)>=RIGHT_WALL:
        return True
    else:
        return False

# checks if the ball has moved beyond the left wall
def moved_beyond_left():
    if (X_B+BALL_RADIUS)<=LEFT_WALL:
        return True
    else:
        return False

# checks if the ball has moved beyond the top wall
def moved_beyond_top():
    if (Y_B-BALL_RADIUS) <= TOP_WALL:
        return True
    else:
        return False


# checks if the ball has moved beyond the bottom wall
def moved_beyond_bottom():
    if (Y_B+BALL_RADIUS) >= BOTTOM_WALL:
        return True
    else:
        return False

# checks for collision between ball and left paddle
def hit_left_paddle():
    global X_B, Y_B
    if (Y_P_LEFT) <= (Y_B+BALL_RADIUS) and (Y_B-BALL_RADIUS) <= (Y_P_LEFT+PHEIGHT) and (X_B - BALL_RADIUS) <= (X_P_LEFT+PWIDTH):
        X_B = PWIDTH + BALL_RADIUS + 1
        return True
    else:
        return False

# checks for collision between ball and right paddle
def hit_right_paddle():
    global X_B, Y_B
    if (Y_P_RIGHT) <= (Y_B+BALL_RADIUS) and (Y_B-BALL_RADIUS) <= (Y_P_RIGHT+PHEIGHT) and (X_B+BALL_RADIUS) >= (X_P_RIGHT):
        X_B = RIGHT_WALL - PWIDTH - BALL_RADIUS - 1
        return True

    else:
        return False

# moves the ball
def move_ball():
    global X_B, Y_B, GAME_IN_PROGRESS,X_V,Y_V, GAME_OVER, BLUE, RED

    # if the ball hits one of the paddles, changes its direction using x velocity
    if hit_left_paddle():
        X_V = (-1)*X_V

        # When the ball bounces off a moving paddle, accelerate the ball slightly in the direction of the paddle’s motion
        if LEFT_UP:
            Y_V = Y_V-1
        if LEFT_DOWN:
            Y_V = Y_V + 1

        # changing color of ball when it bounces
        if BLUE:
            BLUE = False
            RED = True

        elif RED:
            RED = False
            BLUE = True

    if hit_right_paddle():
        X_V = (-1) * X_V

        # When the ball bounces off a moving paddle, accelerate the ball slightly in the direction of the paddle’s motion
        if RIGHT_UP:
            Y_V = Y_V - 1

        if RIGHT_DOWN:
            Y_V = Y_V + 1

        # changing color of ball when it bounces
        if BLUE:
            BLUE = False
            RED = True

        elif RED:
            RED = False
            BLUE = True

    # if the ball reaches the left or right wall, ends the game
    elif moved_beyond_right():
        GAME_IN_PROGRESS = False


    elif moved_beyond_left():
        GAME_IN_PROGRESS = False

    # if the ball reaches the top or bottom wall, changes its direction using y velocity
    elif moved_beyond_top():
        Y_V = Y_V*(-1)
    elif moved_beyond_bottom():
        Y_V = Y_V*(-1)

    # moves the paddle if the game is in progress
    if GAME_IN_PROGRESS:
        X_B = X_B + X_V
        Y_B = Y_B + Y_V

    # if the game is not in progress (i.e. ball has reached left or right wall), it stops the motion of the ball by setting velocities equal to zero
    else:
        X_V = INITIAL_X_V
        Y_V = INITIAL_Y_V

# resets paddles and ball to initial positions
def draw_start_game_instructions():
    global X_B, Y_B, X_P_LEFT,X_P_RIGHT, Y_P_LEFT,Y_P_RIGHT, RED, BLUE
    if not(GAME_IN_PROGRESS):
        X_B = INITIAL_X_B
        Y_B = INITIAL_Y_B
        X_P_LEFT = INITIAL_LEFT_X
        Y_P_LEFT = INITIAL_LEFT_Y
        X_P_RIGHT = INITIAL_RIGHT_X
        Y_P_RIGHT = INITIAL_RIGHT_Y
        RED = False
        BLUE = True


# draw paddles
def draw_paddles():
    disable_stroke()
    move_paddles()
    set_fill_color(0, .3, .9)
    draw_rectangle(X_P_LEFT, Y_P_LEFT, PWIDTH, PHEIGHT)
    draw_rectangle(X_P_RIGHT, Y_P_RIGHT, PWIDTH, PHEIGHT)

# draws ball
def draw_ball():
    disable_stroke()
    if BLUE:
        set_fill_color(0, .3, .9)
    if RED:
        set_fill_color(1,0,0)
    draw_circle(X_B, Y_B, BALL_RADIUS)

# main drawing function
def draw_frame():

    set_clear_color(1,1,1)
    clear()
    draw_image(img, 125, 125)
    draw_paddles()
    move_ball()
    draw_ball()
    draw_start_game_instructions()

start_graphics(draw_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, key_press=kpress, key_release=krelease)

