from collections import Counter
import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards_count = Counter(cards)
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    print(cards_count[nums[i]], end=' ' if i < M - 1 else '\n')
        
    

