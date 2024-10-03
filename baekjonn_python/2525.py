a, b = map(int, input().split())
c = int(input())
hour=a + c//60
minute =b + c%60
if minute >=60:
    hour += minute//60
    minute= minute%60
if hour>=24:
    hour=hour%24
print(hour, minute)
    
