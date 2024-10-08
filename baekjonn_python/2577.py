a=int(input())
b=int(input())
c=int(input())
result = list(str(a*b*c))

for i in range(0,10):
    count = 0
    for num in result:
        if i == int(num):
            count +=1
    print(count)