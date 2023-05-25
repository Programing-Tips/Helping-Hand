import random

with open ("uloha-15.txt", 'r') as f:
    names = [name.strip() for name in f.readlines()]
    table = []
    for name in names:
            jumps = [random.randint(350, 850) for _ in range(6)]
            pb = max(jumps)
            table.append((name, pb))
            
    best = ("", 0)
    for name, pb in table:
        best_name, best_jump = best
        if pb > best_jump:
            best= (name, pb)
            
    print(table)
    print("Winner:", best)