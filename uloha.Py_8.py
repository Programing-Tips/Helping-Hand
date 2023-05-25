import tkinter as tk
import time
import random
from string import ascii_lowercase

c = tk.Canvas(width = 500, height = 500, background = 'white')
c.pack()

running = True
def canvas_onclic(event):
    global running
    running = False

FPS = 60
TIMESTEP = 1/FPS

R = 20
x = random.randint(R, 500 - R)
y = R

egg = c.create_oval(x - R, y -R, x + R, y + R, fill = 'brown')

letter = random.choice(ascii_lowercase)
text = c.create_text(x, y, text=letter.upper(), font='Garamond1 14', state='hidden')


dy = 10

shown = False

while running:
    dx = 0
    dy += 10000 * TIMESTEP
    dy *= TIMESTEP
    y += dy
    c.move(egg, dx, dy,)
    c.move(text, dx, dy,)

    if y > 250 and not shown:
        shown = True
        c.itemconfigure(text, state="normal")
        c.bind_all(f"<KeyPress-{letter}>", canvas_onclic)

    
    if y > 500 - R:
        c.configure(background="red")
        running = False
    
    c.update()
    time.sleep(TIMESTEP)

c.mainloop()