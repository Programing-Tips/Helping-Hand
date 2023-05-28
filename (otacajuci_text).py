import tkinter as tk
import math
import time

text = input()

running = True

c = tk.Canvas(width = 500, height = 500, background = "white")
c.pack()

def canvas_onkey(event):
    global running
    running = False

c.bind_all("<KeyPress-Super_L>", canvas_onkey)

letters = [c.create_text(i*10 + 50, 100, font="Arial, 16", text=cr) for i, cr in enumerate(text)]


for i, l in enumerate(letters):
        c.itemconfigure(l, angle=180 * math.sin(math.pi * i / (len(letters) - 1)))

blink = True 
while running:
    for l in letters:
        c.itemconfigure(l, state = "normal" if blink else "hidden")
    time.sleep(1)
    c.update()
    blink = not blink
    

c.mainloop()
