import random
import math
import tkinter

def primefactors(x):

    if x==1:

        primeNumbers.append("1 nie je prvocislo")

    for i in range(2, x + 1):

        while x % i==0:

            primeNumbers.append(i)

            x/= i

    return primeNumbers



x = random.randint(0,100)

print("x:", x)

primeNumbers = []

print(primefactors(x))


c = tkinter.Canvas(width=800, height=800)

c.pack()

x = 10

y = 50

for i in range(len(primeNumbers)):

    c.create_oval(x, y, x + 50, y + 50,fill="yellow")

    c.create_text(x + 5, y + 25, text = primeNumbers[i], font="Arial 20")

    x +=60

c.mainloop()
