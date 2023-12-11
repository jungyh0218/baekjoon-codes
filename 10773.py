import sys
from collections import deque
N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
    val = int(sys.stdin.readline())
    if val == 0:
        stack.pop()
    else:
        stack.append(val)

print(sum(stack))
    