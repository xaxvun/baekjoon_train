#팩토리얼을 반복문 돌면서 구하는 풀이
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())

# result = 1
# for i in range(K):
#     result *= N
#     N -=1

# divisor = 1
# for i in range(2, K+1):
#     divisor *= i
# print(result // divisor)

#팩토리얼 재귀 함수를 정의해서 푸는 문제
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

# nCk = n!/(n-k)!k!
print(factorial(N) // (factorial(N-K) * factorial(K)))


