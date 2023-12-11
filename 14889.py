from collections import deque
N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

def get_sum(team):
    sum_val = 0
    for i in range(len(team)):
        for j in range(len(team)):
            sum_val += S[team[i]][team[j]]
    return sum_val

min_val = 9999999

visited = [0] * N
def dfs(start_node, count):
    global min_val
    visited[start_node] = 1
    
    if count == N // 2: # return condition
        start = [x for x in range(N) if visited[x] == 1]
        link = [x for x in range(N) if visited[x] == 0]
        start_sum = get_sum(start)
        link_sum = get_sum(link)
        diff = abs(start_sum - link_sum)
        min_val = min((diff, min_val))
        #print(start, link, min_val) 
        visited[start_node] = 0   
        return
    
    for i in range(start_node+1, N):
        if visited[i] == 0:
            dfs(i, count+1)
    visited[start_node] = 0
            
    
            
dfs(0, 1)
print(min_val)