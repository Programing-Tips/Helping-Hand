import math
import random
import tkinter as tk

c = tk.Canvas(width='600', height='600', background="white")
c.pack()

with open("uloha-17.txt") as f:
    rows = [row.strip() for row in f.readlines()]
    heights = [[int(n) for n in row] for row in rows]

west = [max(row) for row in heights]

south = heights[0]
for row in heights:
    for i in range(len(row)):
        col = row[i]
        if col > south[i]:
            south[i] = col
            
SIZE = 40

for i, value in enumerate(west):
    c.create_rectangle(i*SIZE, 200, (i + 1) * SIZE, 200- value * SIZE//2, fill="black")
    
for i, value in enumerate(south):
    c.create_rectangle(i*SIZE, 400, (i + 1) * SIZE, 400- value * SIZE//2, fill="black")

c.mainloop()