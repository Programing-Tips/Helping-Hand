from tkinter import *
import tkinter as tk
import random
import time
doboku = int(input())
horedole = int(input())
root = tk.Tk()
w = 500
h = 500
my_canvas = Canvas(root, width = w, height = h, bg = 'white')
my_canvas.pack()
x = random.randint(0,400)
y = random.randint(0,400)
my_circle = my_canvas.create_oval(x,y,x+10,y+10)

while x > 0 and x < w-10 and y > 0 and y < h-10:
    my_canvas.move(my_circle,doboku,horedole)
    x+=doboku
    y+=horedole
    my_canvas.update()
    time.sleep(0.5)


root.mainloop()
