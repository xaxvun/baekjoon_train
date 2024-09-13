s = input()
I = set()
for i in range(1, len(s)+1):
    for j in range(len(s)):
        I.add(s[j:j+i])
print(len(I))
