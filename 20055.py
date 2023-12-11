from collections import deque
N, K = [int(x) for x in input().split()]

durability = deque([int(x) for x in input().split()])
robot_pos = deque([])
step = 1

while True:
    # step 1
    durability.appendleft(durability.pop())
    if len(robot_pos) > 0 and robot_pos[len(robot_pos)-1] == N-1:
        robot_pos.pop()
    for i, v in enumerate(robot_pos):
        if robot_pos[i] < N-1:
            robot_pos[i] += 1

            
            
    # step 2
    if len(robot_pos) > 0 and robot_pos[len(robot_pos)-1] >= N-1 :
            robot_pos.pop()
    for i in range(len(robot_pos)-1, -1, -1):
        if durability[robot_pos[i] + 1] == 0 or (i < len(robot_pos)-1 and robot_pos[i+1] == robot_pos[i] + 1):
            continue
        else:
            robot_pos[i] += 1
            durability[robot_pos[i]] -= 1
    
    #step 3
    if durability[0] >= 1:
        robot_pos.appendleft(0)
        durability[0] -= 1
    
    #step 4
    if durability.count(0) >= K:
        break
    else:
        step += 1 
        continue
    
    
print(step) 
