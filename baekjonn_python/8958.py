num = int(input())

for i in range(num):
    test = list(input())
    numbers = 0
    results=0
    for j in test:
        if j == 'O':
            numbers += 1
            results += numbers
        else:
            numbers = 0
    print(results)