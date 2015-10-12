# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.show = True
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        handstr = ''
        for x in self.hand:
            handstr = handstr + str(x)
        return handstr

    def add_card(self, card):
        self.hand.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        handvalue = 0
        aces = 0
        for x in self.hand:
            if x.get_rank() == 'A':
                aces += 1
            handvalue += VALUES.get(x.get_rank())
        if aces > 0 and (handvalue + 10) <= 21:
            handvalue += 10
        return handvalue


    def busted(self):
        pass	# replace with your code
    
    def draw(self, canvas, p):
        for z in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [p[0] + CARD_CENTER[0] + 73 * self.hand.index(z), p[1] + CARD_CENTER[1]], CARD_SIZE)
       
# define deck class 
class Deck:
    def __init__(self):
        self.cards = list()
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        return "Deck contains " + " ".join([str(i) for i in self.cards])


#define event handlers for buttons
def deal():
    global outcome, in_play, score, player_hand, dealer_hand, my_deck
    if in_play:
        score -= 1
    my_deck = Deck()
    my_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        dealer_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
    in_play = True
    outcome = "Hit or Stand?"
    

def hit():
    global outcome, in_play, score
    if not in_play:
        return
    player_hand.add_card(my_deck.deal_card())
    outcome = "Hit or Stand?"
    if player_hand.get_value() > 21:
        outcome = "Busted. New deal?"
        in_play = False
        score -= 1
       
def stand():
    global outcome, score, in_play
    in_play = False
    if player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        score -= 1
        return score, outcome, in_play
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        else:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts, you win. New deal?"
                score += 1
                return score, outcome, in_play
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer wins. New deal?"
                score -= 1
                return score, outcome, in_play
            else:
                outcome = "You win. New deal?"
                score += 1
                return score, outcome, in_play
   

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, [0, 100])    
    player_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[50,75],30,"Black")
    canvas.draw_text("Score: "+str(score),[450,75],30,"Black")
    canvas.draw_text("BlackJack",[250,50],35,"Cyan")
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
