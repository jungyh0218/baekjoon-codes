from collections import deque
N = int(input())
for _ in range(N):
    stack = deque([])
    parenthesis = input()
    flag = True
    for c in parenthesis:
        if c == '(':
            stack.append(c)
        else: # case ')'
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()
    if flag:
        if len(stack) == 0:
            print('YES')
        else: 
            print('NO')
    else:
        print('NO')
    