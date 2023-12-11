import sys
from collections import deque
N = int(sys.stdin.readline())
stack = deque()
for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == 'top':
        print(stack[-1] if len(stack) > 0 else -1)