nums = input().split()
a1 = int(nums[0])
b1 = int(nums[1])
a2 = int(nums[2])
b2 = int(nums[3])
if a1 == a2 and b1 == b2:
    print('=')
elif a1 >= a2 and b1 <= b2:
    print('1')
elif a2 >= a1 and b2 <= b1:
    print('2')
else:
    print('?')