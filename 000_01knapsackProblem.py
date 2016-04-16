"""
0/1 knapsack problem
"""
class Item():
    def __init__(self, weight, val):
        self.weight = weight
        self.val = val
        
def knapsack(items, capacity):
    items.sort(key = lambda x: x.weight)
    lookup = [[0 for j in range(capacity + 1)] for i in range(len(items))]
    for j in range(items[0].weight, capacity + 1):
        lookup[0][j] = items[0].val
    for i in range(1, len(items)):
        for j in range(1, capacity + 1):
            if j < items[i].weight:
                lookup[i][j] = lookup[i - 1][j]
            else:
                lookup[i][j] = max(lookup[i - 1][j], items[i].val + lookup[i - 1][j - items[i].weight])
    res, weight, value = [], capacity, lookup[-1][-1]
    for i in reversed(range(len(items))):
        if not i:
            res.append(items[0].weight)
            continue
        w, v = weight - items[i].weight, value - items[i].val
        if w >= 0 and lookup[i - 1][w] == v:
            res.append(items[i].weight)
            weight, value = w, v
        if not weight:
            break
    return (lookup[-1][-1], res)

if __name__ == "__main__":
    items = [Item(1, 1), Item(3, 4), Item(4, 5), Item(5, 7)]
    print(knapsack(items, 7))
    items = [Item(2, 6), Item(2, 3), Item(6, 5), Item(5, 4), Item(4, 6)]
    print(knapsack(items, 10))
