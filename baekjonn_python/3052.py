numbers=list()
for i in range(10):
    numbers.append(int(input())%42)
numbers=set(numbers)
print(len(numbers))
