import sys
from collections import deque
N, M, R = tuple(map(int, input().split()))
Q = deque()
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = tuple(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N+1):
    graph[i].sort()
    
def bfs(start):
    visit_cnt = 1
    visited = [0] * (N+1)
    visited[start] = visit_cnt
    Q.append(start)
    while len(Q) > 0 :
        vertex = Q.popleft()
        for j in graph[vertex]:
            if visited[j] == 0:
                visit_cnt += 1
                visited[j] = visit_cnt
                Q.append(j)

    for i in range(1, N+1):
        print(visited[i])
                
bfs(R)