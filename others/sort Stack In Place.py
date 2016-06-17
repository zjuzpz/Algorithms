def sortStackInPlace(stack):
    if stack:
        temp = stack.pop()
        sortStackInPlace(stack)
        sortedInsert(stack, temp)

def sortedInsert(stack, num):
    if not stack or num > stack[-1]:
        stack.append(num)
    else:
        temp = stack.pop()
        sortedInsert(stack, num)
        stack.append(temp)

if __name__ == "__main__":
    stack = [-3, -6, 0, 7, 2, 1, 5]
    sortStackInPlace(stack)
    print(stack)
