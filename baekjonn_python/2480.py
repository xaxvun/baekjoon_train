# list=[]
# list= map(int, input().split())
# if(list[0]!=list[1]&list[1]!=list[2]&list[0]!=list[2]):
#     m = max(list)
#     print(m*100)
# elif():
#     print()
# else

a,b,c = map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)

