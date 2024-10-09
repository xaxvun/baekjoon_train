# words=list(map(str, input()))
# alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# results=[-1 for i in range(len(alphabet))]
# for i in range(len(words)):
#     for j in range(len(alphabet)):
#         if alphabet[j]==words[i]:
#             results[j]=i
# for i in range(len(results)):
#     print(results[i], end=' ')
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')