from collections import deque
N, M = tuple(map(int,input().split()))
queue = deque(range(1, N+1))
nums = list(map(int, input().split()))
ops = 0
for n in nums:
    if queue.index(n) <= len(queue) // 2:
        while queue[0] != n:
            ops += 1
            queue.append(queue.popleft())
        queue.popleft()
    else:
        while queue[0] != n:
            ops += 1
            queue.appendleft(queue.pop())
        queue.popleft()
        
print(ops)