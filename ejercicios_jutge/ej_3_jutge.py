num = input().split()
while len(num) < 2:
    num += input().split()
num = [int(x) for x in num]
print(sum(num))