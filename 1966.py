from collections import deque
T = int(input())
for _ in range(T):
    N, M = tuple(map(int, input().split()))
    inputs = [int(x) for x in input().split()]
    queue = deque([(i, v) for i, v in enumerate(inputs)])
    order = 0
    while True:
        max_val = max([x[1] for x in queue])
        if queue[0][1] == max_val:
            order += 1
            doc = queue.popleft()
            if doc[0] == M:
                print(order)
                break
        else:
            queue.append(queue.popleft())
            