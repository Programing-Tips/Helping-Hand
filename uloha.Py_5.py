import random

Numbers=[]
for i in range(1, 36):
    Numbers.append(i)

for i in range(1):
    x=random.sample(Numbers, k=5,)

print(Numbers, x)