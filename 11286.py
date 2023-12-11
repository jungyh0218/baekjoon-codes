import sys
import heapq

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(n), n))
        