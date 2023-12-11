hour, minute = map(int, input().split(' '))
time = int(input())

hour += time // 60
minute += time % 60

if minute >= 60:
    minute = minute % 60
    hour += 1
    
if hour >= 24:
    hour = hour % 24
    
print(hour, minute)