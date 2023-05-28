from tkinter import *
from tkinter.ttk import *

import random



class Platno():

    def __init__(self, width, height, even = [], odd = []) -> None:
        self.width=width
        self.height=height
        self.even=even
        self.odd=odd
        self.canvas=Tk()
        self.canvas=Canvas(self.canvas,width = self.width, height = self.height)
        self.canvas.pack()

    def generate_100_numbers(self):

        x = 25

        y = 25

        for i in range(100):

            if y <= self.height - 30:

                n=random.randint(0, 1000)

                self.canvas.create_text(x, y, text=n, font="Garamond 20")

                y += 25

                if n % 2 == 0:

                    self.even.append(n)

                if n % 2 !=0:

                    self.odd.append(n)

            else:

                x += 100

                y = 25 

        return (self.even, self.odd)


    def draw_even_odd_numbers(self, zoznam):

        x = 25

        y = 25

        for i in range(len(zoznam)):

            if y <= self.height - 30:

                self.canvas.create_text(x,y,text = zoznam[i],font="Garamond 20")

                y += 25

            else:

                x += 100

                y = 25


canvas = Platno(500, 500)
canvas.generate_100_numbers()


parne_cisla = Platno(500, 500)
parne_cisla.draw_even_odd_numbers(canvas.even)


neparne_cisla = Platno(500, 500)
neparne_cisla.draw_even_odd_numbers(canvas.odd)


mainloop()
