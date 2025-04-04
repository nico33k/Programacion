words = []
words = input().split()
a = words[0]
b = words[1]
if a < b:
    print(a, '<', b)
elif a > b:
    print(a,'>',b)
else:
    print(a, '=', b)