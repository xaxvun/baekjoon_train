import sys
input = sys.stdin.readline
def recursion(s, l, r):
    global count
    count +=1

    if( l>=r): return 1
    elif(s[l] != s[r]): return 0
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())
for _ in range(N):
    count = 0 # 하나씩 확인 할 때마다 0으로 초기화
    print(isPalindrome(input().rstrip()), count) # .rstrip()을 사용해서 sys함수의 줄바꿈을 삭제