import tkinter as tk
import time
import random
from string import ascii_lowercase

running = True

word_list = ["eagle", "python", "snake"]

target = random.choice(word_list)
guessed = {}.fromkeys(target, False)

def get_mask():
    global target, guessed
    return ''.join([ch if guessed[ch] else '*' for ch in target])

def on_key(event):
    global running, guessed, target, c
    if event.keysym not in guessed:
        return                  # Incorrect guess
    if guessed[event.keysym]:
        return                  # We had already guessed this letter
    guessed[event.keysym] = True
    c.itemconfigure(text1, text=get_mask())
    if False not in guessed.values():
        c.unbind_all("<Key>")
        running = False


FPS = 60
TIMESTEP = 1/FPS

c = tk.Canvas(width = 500, height = 500, background = "white")
c.pack()

x = random.randint(14, 486)
y = 14

text1 = c.create_text(x, y, text=get_mask(), font='Arial, 14',)
text2 = c.create_text(x, y, text=target, font='Arial, 14',  state='hidden')

def on_update():
    global c, x, y, running
    dy = 60 * TIMESTEP
    y += dy
    c.move(text1, 0, dy)
    c.move(text2, 0, dy)


    if y > 486:
        c.create_text(250, 225, text="NeuhÃ¡dol si!", font='Arial, 14',)
        c.itemconfigure(text2, state='normal')
        c.itemconfigure(text1, state='hidden')
        running = False

    c.update()
    if running:
        c.after(int(TIMESTEP * 1000), on_update)


c.bind_all("<Key>", on_key)
on_update()
c.mainloop()
