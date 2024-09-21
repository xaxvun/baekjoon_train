# import sys
# N = int(sys.stdin.readline())
# k = 1
# if N>0:
#     for i in range(1,N+1):
#         k *= i
# print(k)

#함수로 만들어 보기
def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))