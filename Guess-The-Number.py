import random
import simplegui

# initializing global variables used
secret_number = 0
guess_allowed = 7
game = 1
# helper function to start and restart the game
def new_game(): 
    global secret_number
    global guess_allowed
    global game
    print " "
    if game:
        print "New game Started. Range 0 to 100"
        secret_number = random.randrange(0, 100)
        guess_allowed = 7
    else:
        print "New game Started. Range 0 to 1000"
        secret_number = random.randrange(0, 1000)
        guess_allowed = 10
    print "Guesses Remaining: ", guess_allowed
    pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0, 100) and restarts
    print " "
    print "Range changed. New Range is 0 to 100"
    global game
    game = 1
    new_game()
    pass

def range1000():
    # button that changes range to range [0, 1000) and restarts
    print " "
    print "Range changed. New Range is 0 to 1000"
    global game
    game = 0
    new_game()
    pass
    
def input_guess(guess):
    """ Reads input from input field and compares it with 
        Secret Number and then prints appropriate response
        and starts new game when number of guesses exhausted""" 
    global secret_number
    global guess_allowed
    global game
    guess = int(guess)
    guess_allowed -= 1
    print " "
    print "Your Guess was ", guess
    print "Guesses Remaining: ", guess_allowed
    if secret_number > guess:
        print "Higher!"
    elif secret_number < guess:
        print "Lower!"
    else:
        print "Correct! You Won!"
        new_game()
    if guess_allowed <= 0:
        print "You have lost."
        new_game()
    pass

    
# creating frame
f = simplegui.create_frame("Guess the number", 300, 200)


# register event handlers for control elements
f.add_button("Range : [0, 100)", range100)
f.add_button("Range : [0, 1000)", range1000)
f.add_input("Guess a number and enter", input_guess, 200)


# call new_game and start frame
new_game()
f.start()


