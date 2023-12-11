teams = input().split(' ')
pts = {}
for team in teams:
    if team not in pts.keys():
        pts[team] = 0.0
        
for i in range(6):
    input_val = input().split(' ')
    team_a = input_val[0]
    team_b = input_val[1]
    pts[team_a] += float(input_val[2]) + float(input_val[3])*0.5
    pts[team_b] += float(input_val[3])*0.5 + float(input_val[4])
    
print(pts)
for team in teams:
    print(pts[team]/3)
    