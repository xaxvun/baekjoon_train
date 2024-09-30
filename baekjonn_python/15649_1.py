#백트레킹 파이썬 내장함수로 구현
from itertools import permutations
n, m = map(int, input().split())
p = permutations(range(1, n+1), m)
for i in p:
   print(" ".join(map(str, i)))