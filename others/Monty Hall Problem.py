"""
Monty Hall problem
"""
from random import randint
def win(change):
    target = randint(1, 3)
    choose = randint(1, 3)
    if target != choose:
        for i in range(1, 4):
            if i != choose and i != target:
                if change:
                    return True
                return False
    elif change:
        return False
    return True

if __name__ == "__main__":
    countChange, countNotChange, total = 0, 0, 10000
    for i in range(total):
        if win(True):
            countChange += 1
        if win(False):
            countNotChange += 1
    print(countChange / total, countNotChange / total)
