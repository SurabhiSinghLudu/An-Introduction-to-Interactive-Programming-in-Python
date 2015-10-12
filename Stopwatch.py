# implementation of "Stopwatch: The Game"

import simplegui

# define global variables
""" integer t keeps track of time in tenths of seconds"""
t = 0
"""counter x and y keep a track of the reflexes"""
""" x is the number of successful stops"""
""" y is the number of stops """
x = 0
y = 0
""" stop is a boolean used to detect if the timer is already stopped"""
stop = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    a = int(t / 10) / 60
    b = int((t - a * 600) / 100)
    c = int(((t - a * 600) % 100) / 10)
    d = t % 10
    return str(a)+':'+str(b)+str(c)+'.'+str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global t
    global stop
    stop = False
    timer.start()
    
def stop():
    global t
    global x
    global y
    global stop
    if(stop == False):
        stop = True
        if(t % 10 == 0):
            x = x + 1
        y = y + 1
    timer.stop()
    
def reset():
    global t
    global x
    global y
    global stop
    timer.stop()
    stop = False
    t = 0
    x = 0
    y = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t=t + 1

# define draw handler
def draw(canvas):
    global x
    global y
    canvas.draw_text(format(t),[100,110], 50, "white")
    canvas.draw_text(str(x)+'/'+str(y),[260, 25], 25, "green")

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)


# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start, 100)
frame.add_button("stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
