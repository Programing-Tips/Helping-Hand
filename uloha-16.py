import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
SIZE = 20

c = tk.Canvas(width = WIDTH, height = HEIGHT, background = "white")
c.pack()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
    

for y in range (0, HEIGHT, 2*SIZE):
    for x in range(0, WIDTH, SIZE):
        c.create_rectangle(x, y, x+SIZE, y + SIZE, fill= random_color())
        c.create_oval(x, y + SIZE, x+ SIZE, y + 2*SIZE, fill = random_color())


c.mainloop()