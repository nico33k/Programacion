first = ''
second = ''
nums = input().split()
a1 = int(nums[0])
b1 = int(nums[1])
a2 = int(nums[2])
b2 = int(nums[3])
if a1 == a2 and b1 == b2:
    first = '='
elif a1 >= a2 and b1 <= b2:
    first = '1'
elif a2 >= a1 and b2 <= b1:
    first = '2'
else:
    first = '?'
inter1 = max(a1, a2)
inter2 = min(b1, b2)
if inter1 > inter2:
    second = '[]'  
else:
    second = (f'[{inter1},{inter2}]')
print(f'{first} , {second}')