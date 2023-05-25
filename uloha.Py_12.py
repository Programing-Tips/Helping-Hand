import tkinter as tk
import random as rnd
import math
import time

WIDTH = 600
HEIGHT = 400
R = 20
SPEED = 5

c = tk.Canvas(width=WIDTH, height=HEIGHT, background="white")
c.pack()

lines = []
with open("subor.txt", 'r') as f:
    lines = f.readlines()

coords = [[int(n) for n in line.split(' ')] for line in lines]

circles = [c.create_oval(x - R, y - R, x + R, y + R, fill="black") for x, y in coords]

vels = []
for _ in circles:
    angle = 2 * math.pi * rnd.random()
    vels.append([SPEED * math.cos(angle), SPEED * math.sin(angle)])

running = True
while running:
    for i in range(len(circles)):
        dx, dy = vels[i]
        coords[i][0] += dx
        coords[i][1] += dy
        c.move(circles[i], dx, dy)
        if R > coords[i][0] or coords[i][0] > WIDTH - R:
            vels[i][0] *= -1
        if R > coords[i][1] or coords[i][1] > HEIGHT - R:
            vels[i][1] *= -1

    time.sleep(.1)
    c.update()
