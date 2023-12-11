from collections import Counter
import sys

trees = []
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    else:
        trees.append(tree)
total = len(trees)
trees_count = Counter(trees)

kinds = sorted(trees_count.keys())

for k in kinds:
    print(f'{k} {round(100 * trees_count[k]/total, 4):.4f}')
        