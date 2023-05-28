import tkinter as tk
import time
import math

c = tk.Canvas(width=600, height=600)
c.pack()

def ticking(X, Y):
    steps = 0
    r = 100
    rot_x = X + math.cos(steps) * r
    rot_y = Y + math.sin(steps) * r
    line = c.create_line(X, Y, rot_x,rot_y)
        
    while True:
        steps += 0.02
        rot_x = X + math.cos(steps) * r
        rot_y = Y + math.sin(steps) * r
        c.coords(line, X, Y, rot_x, rot_y)
        time.sleep(0.01)
        c.update()
                 
ticking(150,150)

