import random

number = random.randint(1, 100)

while (guess := int(input("Hadaj: "))) != number:
    if guess > number:
        print("menej")
    else:
        print("viac")
