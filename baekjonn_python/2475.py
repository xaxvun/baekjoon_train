#2475
a = list(map(int, input().split()))
b = 0
for i in range(5):
    b += a[i]**2
print(b%10)

#10951

while True:
    try:
        a,b=map(int, input().split())
        print(a+b)
    except:
        break