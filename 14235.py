import sys
import heapq

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    n = list(map(int, sys.stdin.readline().strip().split()))
    if n[0] == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap) * -1)
        else:
            print(-1)
    else:
        for x in n[1:]:
            heapq.heappush(heap, x * -1)
        