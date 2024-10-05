n = int(input())
k = str(input())
n_list= list(map(int, str(k)))
result = 0
for i in range(0, n):
    result += n_list[i]
print(result)