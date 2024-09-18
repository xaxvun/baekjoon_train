import sys
stack=[]
sum_v=0
k=int(sys.stdin.readline())

for _ in range(k):
    num = int(sys.stdin.readline())

    if stack and num == 0: #스텍에 값이 존재하고 입력받은 값이 0이면
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))