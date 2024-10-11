#메모리 용량 초과
# import sys

# n = int(sys.stdin.readline())
# lst = []

# for i in range(n):
#     lst.append(sys.stdin.readline().strip())
# lst.sort()
# for i in lst:
#     print(i)

import sys

N  = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 

for i in range(10001): 
    if arr[i] != 0:
        for j in range(arr[i]): 
            print(i)