# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
"""it'll appear  at the center of table initially"""
ball_pos = [WIDTH / 2, HEIGHT / 2] 
ball_vel = [0, 0]
paddle1_pos = [0, (HEIGHT/2)-40]
paddle2_pos = [0, (HEIGHT/2)-40]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    x_vel = random.randrange(120, 240)/60.0
    y_vel = random.randrange(60, 180)/60.0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [ x_vel, -y_vel] 
    if direction == LEFT:
        ball_vel = [ -x_vel, -y_vel]
    

# define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2
    ball_pos = [WIDTH / 2, HEIGHT / 2] 
    ball_vel = [0, 0]
    paddle1_pos = [0, (HEIGHT/2)-40]
    paddle2_pos = [0, (HEIGHT/2)-40]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[0] >= WIDTH - PAD_WIDTH-BALL_RADIUS:
        # hitting paddle 2 (right paddle)
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= (paddle2_pos[1] + PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] + ball_vel[0]/10
            ball_vel[1] = ball_vel[1] + ball_vel[1]/10
            ball_vel[0] = - ball_vel[0] - 1
            
        else:
            ball_vel = [0, 0]
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            score1 += 1
            spawn_ball(LEFT)
    
    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        # hitting paddle 1 (left paddle)
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= (paddle1_pos[1] + PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] + ball_vel[0]/10
            ball_vel[1] = ball_vel[1] + ball_vel[1]/10
            ball_vel[0] = - ball_vel[0]    + 1
           
        else:
            ball_vel = [0, 0]
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            score2 += 1
            spawn_ball(RIGHT)
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0] += paddle1_vel[0]
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[0] += paddle2_vel[0]
    paddle2_pos[1] += paddle2_vel[1]
   
    if paddle1_pos[1] <= 0:
        paddle1_vel[1] = 0
    if paddle1_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle1_vel[1] = 0
     
    if paddle2_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle2_vel[1] = 0
    if paddle2_pos[1] <= 0:
        paddle2_vel[1] = 0
    
    # draw paddles
    c.draw_polygon([[0, paddle1_pos[1]], [0, paddle1_pos[1] + PAD_HEIGHT],[PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1]]], 2, 'white', 'white') #left paddle
    c.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos[1] ], [WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT],[WIDTH, paddle2_pos[1] + PAD_HEIGHT], [WIDTH, paddle2_pos[1]]], 2, 'white', 'white') #Right paddle
    
    # draw scores
    c.draw_text(str(score1), [WIDTH/2-45, 30], 30, 'white')
    c.draw_text(str(score2), [WIDTH/2+30, 30], 30, 'white')
    

def keydown(key):
    global paddle1_vel, paddle2_vel
    current_key = chr(key)
   
    if key == simplegui.KEY_MAP['down'] and paddle2_pos[1] < HEIGHT - PAD_HEIGHT: # right paddle up
        paddle2_vel[1] = 0
        paddle2_vel[1] = paddle2_vel[1] + 5
    elif key == simplegui.KEY_MAP['up'] and paddle2_pos[1] > 0: # right paddle down
        paddle2_vel[1] = 0
        paddle2_vel[1] = paddle2_vel[1] - 5
   
    elif key == simplegui.KEY_MAP['W'] and paddle1_pos[1] > 0: #left paddle up
        paddle1_vel[1] = 0
        paddle1_vel[1] = paddle1_vel[1] - 5
    elif key == simplegui.KEY_MAP['S'] and paddle1_pos[1] < HEIGHT - PAD_HEIGHT: # left paddle down
        paddle1_vel[1] = 0
        paddle1_vel[1] = paddle1_vel[1] + 5
    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    current_key = chr(key)
    if key == simplegui.KEY_MAP['down']: # right paddle up
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP['up']: # right paddle down
        paddle2_vel[1] = 0
   
    elif key == simplegui.KEY_MAP['W']: #left paddle up
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP['S']: # left paddle down
        paddle1_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label("Left players use 'W' for up and 'S' for down")
frame.add_label("Right players use up-arrow for up and down-arrow for down")
frame.add_button('RESTART', new_game, 100)



# start frame
new_game()
frame.start()
