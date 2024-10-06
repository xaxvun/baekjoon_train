T = int(input())
for i in range(T):
    a,b = input().split()
    a = int(a)
    b = str(b)
    list(b)
    for i in range(len(b)):
        print(b[i]*a,end="")
    print("")

#수정한 코드
#굳이 받고 나서 int, str 정할 필요 없이 출력시 수정하면 됨
T = int(input())

for i in range(T):
    a, b = input().split()
    for j in range(len(b)):
        print(b[j] * int(a), end = '')
    print('')
