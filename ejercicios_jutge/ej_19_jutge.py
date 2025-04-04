nums = input().split()
a1 = int(nums[0])
b1 = int(nums[1])
a2 = int(nums[2])
b2 = int(nums[3])
inter1 = max(a1, a2)
inter2 = min(b1, b2)
if inter1 > inter2:
    print('[]')  
else:
    print(f'[{inter1},{inter2}]')