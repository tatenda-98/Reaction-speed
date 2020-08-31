from tkinter import *
import time
from random import *
#from random import choice


root = Tk()

c = Canvas(root, width=600, height=600, bg="black")
c.pack(side=TOP)

global milliseconds1    #set global variables that can be used in all the functions
global milliseconds2
global list
counter = 0



def start():
    global milliseconds1
    global list

    list = [onClick_square, onClick_oval, onClick_star]
    x = randint(1, 500)                                 #creates random x, y values to use for the coordinates for the square
    y = randint(1, 500)

    s = c.create_rectangle(x, y, x+20, y+20, fill='white')    #creates square

    milliseconds1 = int(round(time.time() * 1000))      #puts the current time into the millisecond variable
    c.tag_bind(s, '<ButtonPress-1>', choice(list))           #when the square is clicked then the onclick function is called


def onClick_square(event):
    global milliseconds1
    global milliseconds2
    global counter
    global list

    list = [onClick_square, onClick_oval, onClick_star]
    milliseconds2 = int(round(time.time() * 1000))      #gets a second current time
    if (milliseconds2 - milliseconds1) < 4000:          #compares the first current time to the one set above and if there is less than a 2 second difference than increment the counter
        counter += 1

    counter_button.config(text="score: %d" % counter)   #button for the score
    c.delete('all')                                     #deletes all the objects on the canvas

    x = randint(1, 500)
    y = randint(1, 500)

    milliseconds1 = int(round(time.time() * 1000))
    s = c.create_rectangle(x, y, x+20, y+20, fill='white')      #creates a new square
    c.tag_bind(s, '<ButtonPress-1>', choice(list))           #recalls an onClick function when the square/oval is pressed


def onClick_oval(event):
    global milliseconds1
    global milliseconds2
    global counter
    global list

    list = [onClick_square, onClick_oval, onClick_star]

    milliseconds2 = int(round(time.time() * 1000))  # gets a second current time
    if (milliseconds2 - milliseconds1) < 2000:  # compares the first current time to the one set above and if there is less than a 2 second difference than increment the counter
        counter += 3

    x = randint(60, 120)
    y = randint(60, 120)

    c.delete('all')

    milliseconds1 = int(round(time.time()*1000))
    circle = c.create_oval(x, x, y, y, fill="yellow")    #creates a circle
    c.tag_bind(circle, "<ButtonPress-1>", choice(list))

def onClick_star(event):
    global milliseconds1
    global milliseconds2
    global counter
    global list

    list = [onClick_square, onClick_oval, onClick_star]

    milliseconds2 = int(round(time.time() * 1000))  # gets a second current time
    if (milliseconds2 - milliseconds1) < 1000:  # compares the first current time to the one set above and if there is less than a 2 second difference than increment the counter
        counter += 5

    a = randint(95,105)
    b = randint(120,140)
    h = randint(100,115)
    d = randint(70,95)
    e = randint(40,65)

    c.delete('all')

    milliseconds1 = int(round(time.time()*1000))
    star = c.create_polygon(a, b, h, h, b, a, h, d, a, e, d, d, e, a, d, h, outline="Green", fill= "blue")
    c.tag_bind(star, "<ButtonPress-1>", choice(list))




start_button = Button(root, text="Start", command=start)        #button to start draw the first square
counter_button = Label(text="score: %d" % counter)             #button that keeps track of the score
start_button.pack()
counter_button.pack()
root.mainloop()







