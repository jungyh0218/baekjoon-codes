import sys
import heapq
heap = []
scores = [0] * 1001 # 가능한 최대 일수 = 1001일
N = int(sys.stdin.readline())

for _ in range(N):
    n = list(map(int, sys.stdin.readline().strip().split()))
    # 기준: 높은 점수를 먼저 선정. 같은 점수라면 촉박한 것부터 수행하도록 함.
    # 가능한 한 과제를 수행 가능한 마지막 날부터 채움.
    # 과제를 할 수 있는 날이 없을 경우 pass  
    heapq.heappush(heap, (n[1] * -1, n[0]))

while len(heap) > 0:
    peek = heapq.heappop(heap)
    idx = peek[1]
    while scores[idx] > 0 and idx > 0:
        idx -= 1
    scores[idx] += peek[0] * -1
    
    
print(sum(scores[1:]))