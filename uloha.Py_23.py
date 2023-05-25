from tkinter import *
import tkinter as tk
root = tk.Tk()
w = 600
h = 600
x = w //2
y = h //2
my_canvas = Canvas(root, width = w, heigh = h, bg = 'white')
my_canvas.pack()
my_circle = my_canvas.create_oval(x,y,x+10,y + 10)

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)
def right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)
def up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)
def down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)
root.bind("<Left>",left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()