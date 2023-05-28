import random
list = []
for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    list.append((x,y)) 
body = 0
while body < 10:
    x,y = list.pop()
    odpoved = x*y
    if odpoved == int(input(f'{x}*{y}')):
        body+= 1
    else:
        list = [(x,y)] + list
