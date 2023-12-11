import sys
E, S, M = map(int, sys.stdin.readline().split())
i = 1
while True:
    e = i % 15 if i % 15 > 0 else 15
    s = i % 28 if i % 28 > 0 else 28
    m = i % 19 if i % 19 > 0 else 19
    if e == E and s == S and m == M:
        break
    i += 1
print(i)