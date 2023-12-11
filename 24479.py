import sys
from collections import deque

N, M, R = tuple(map(int, input().split()))
stack = deque()
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = tuple(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N+1):
    graph[i].sort(reverse=True)
    
def dfs(start):
    visit_cnt = 1
    visited = [0] * (N+1)
    stack.append(start)
    while len(stack) > 0 :
        vertex = stack.pop()
        if visited[vertex] >= 1:
            continue
        visited[vertex] = visit_cnt
        visit_cnt += 1
        for j in graph[vertex]:
            if visited[j] == 0:
                stack.append(j)

    for i in range(1, N+1):
        print(visited[i])
                
dfs(R)