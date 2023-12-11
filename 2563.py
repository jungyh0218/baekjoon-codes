N = int(input())
commands = []
for _ in range(N):
    commands.append(tuple(map(int, input().split())))
    
papers = []
for _ in range(100):
    papers.append([0]*100)

for c in commands:
    horizontal, vertical = c
    for i in range(vertical, vertical + 10):
        for j in range(horizontal, horizontal + 10):
            papers[i][j] = 1
            
print(sum([sum(x) for x in papers]))