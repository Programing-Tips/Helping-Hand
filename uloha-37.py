import tkinter as tk

c = tk.Canvas(width = 500, height = 500, background = "white")
c.pack()

f = open("oznam-37.txt", "r")
text = f.read()
z = [ord(c) for c in text]


c.create_text(250,250, text=z)

c.mainloop()