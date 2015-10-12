# implementation of card game - Memory

import simplegui
import random

"""initializing all the variables used"""
list_1 = range(8) # list 1 of range [0, 8)
list_2 = range(8) # list 2 of range [0, 8)
# concatenation of two lists as explained in the development process
list = list_1 + list_2 
turns = 0
state = 0
exposed = [False for i in range(16)]
choice1 = 0
choice2 = 0

# helper function to initialize globals
def new_game():
    global exposed, list, turns, choice1, choice2, state
    random.shuffle(list)
    turns = 0
    state = 0
    exposed = [False for i in range(16)]
    choice1 = 0
    choice2 = 0
    
     
# define event handlers
def mouseclick(pos):
    global state, choice1, choice2, turns, exposed, list
    pick = int(pos[0] / 50)
    # when first card of a turn is picked
    if state == 0:
        choice1 = pick
        exposed[choice1] = True
        state = 1
        turns += 1
    #when second card of a turn is picked
    elif state == 1:
        if not exposed[pick]:
            choice2 = int(pos[0] / 50)
            exposed[choice2] = True
            state = 2
    
    #when third card is picked, previously picked cards are compared
    #if they turn out to be same, nothing is done, and the new card 
    #is exposed, else, both the previously picked cards are flipped 
    #over and third card is exposed which then becomes first card for
    #the new turn   
    else:
        if not exposed[pick]:
            if list[choice1] == list[choice2]:
                pass
            else:
                exposed[choice1] = False
                exposed[choice2] = False
            choice1 = pick
            exposed[choice1] = True
            state = 1
            turns += 1
    label.set_text("Turns = " + str(turns))
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, list
    offset = 50
    hor_pos = -25
    exposed_pos = -50
    for i in range(16):
        hor_pos += offset
        exposed_pos += offset
        if (exposed[i] == True):
            canvas.draw_text(str(list[i]), [hor_pos, 50], 30, "White")
        else:
            canvas.draw_polygon([(exposed_pos, 0), (exposed_pos + 50, 0), (exposed_pos + 50, 100), (exposed_pos + 0, 100)], 2, "Red", "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
