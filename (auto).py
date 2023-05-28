import tkinter as tk
import time
from tkinter import ttk
from tkinter import *

root = tk.Tk()
c = tk.Canvas(width = 500, height = 500, background = 'white')
c.pack()


running = True
def canvas_onclic(event):
    global running
    running = False

FPS = 60
TIMESTEP = 1/FPS

R = 20
x = 510
y = 430

car_image = tk.PhotoImage(file=r'Adresa obrazku')
car = c.create_image(x - R, y -R, image = car_image, anchor=tk.NW)

dx =  10


while running:
    dx =-200*TIMESTEP
    dy = 0
    x += dx
    c.move(car, dx, dy,)

    if x <= 20:
        x = 500 
        c.moveto(car, 500, 410,)  
    
    c.update()
    time.sleep(TIMESTEP)

c.mainloop()
