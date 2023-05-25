import tkinter as tk
import time
import random
from string import ascii_lowercase

running = True


word_list = ["pes",]

target = random.choice(word_list)
guess = "*" * len(target)
correct = 0


def canvas_onkey(event):
    global running, guess, correct, target, c

    if event.keysym == target[correct]:
        g = list(guess)
        g[correct] = target[correct]
        guess = ''.join(g)
        c.itemconfigure(text1, text=guess)
        correct += 1

    if correct == len(target):
        running = False


FPS = 60
TIMESTEP = 1/FPS

c = tk.Canvas(width = 500, height = 500, background = "white")
c.pack()

x = random.randint(14, 486)
y = 14

text1 = c.create_text(x, y, text=guess, font='Arial, 14',)
text2 = c.create_text(x, y, text=target, font='Arial, 14',  state='hidden')

shown = False

dy = 0

while running:
    dx = 0
    dy += 5000 * TIMESTEP
    dy *= TIMESTEP
    y += dy
    c.move(text1, dx, dy)
    c.move(text2, dx, dy)
    c.bind_all(f"<Key>", canvas_onkey)


    if y > 486 and not shown:
        shown = True
        c.create_text(250, 225, text="Neuhádol si!", font='Arial, 14',)
        c.itemconfigure(text2, state='normal')
        c.itemconfigure(text1, state='hidden')
        running = False

    c.update()
    time.sleep(TIMESTEP)


c.mainloop()