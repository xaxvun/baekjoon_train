# import sys
# input = sys.stdin.readline

# while (True):
#     palindrome(n)



# def recursion(a, l, s):
#     if l>=s:
#         return "yes"
#     elif(l != s):
#         return "no"
#     else:
#         return recursion(a, l+1, s-1)


# def palindrome(a):
#     return recursion(a, 0, len(a)-1)

while True:
    n = input()
    if n == '0':
        break
    else:
        if n == n[::-1]:
            print("yes")
        else:
            print("no")