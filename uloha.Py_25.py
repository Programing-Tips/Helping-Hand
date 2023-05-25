import random



lst = []
for i in range(10):
  lst.append(random.randint(0, 100))


newl=[]
for i in lst:
    newl.append(bin(int(i))[2:])


f = open("uloha-25.txt", "w")
f.writelines([str(i)+'\n' for i in newl])
f.close()