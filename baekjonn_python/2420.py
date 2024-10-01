#파이썬 절대값 내장 함수 사용
n,m = map(int, input().split())
absolute_value= abs(n-m)
print(absolute_value)

#내장함수 없이 풀기
n,m = map(int, input().split())
if n>=m:
    print(n-m)
else:
    print(m-n)