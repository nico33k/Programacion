nums = input().split()
euro = int(nums[0])
cent = int(nums[1])
total = euro * 100 + cent

b500 = total // 50000
total = total % 50000

b200 = total // 20000
total = total % 20000

b100 = total // 10000
total = total % 10000

b50 = total // 5000
total = total % 5000

b20 = total // 2000
total = total % 2000

b10 = total // 1000
total = total % 1000

b5 = total // 500
total = total % 500

c2 = total // 200
total = total % 200

c1 = total // 100
total = total % 100

c50 = total // 50
total = total % 50

c20 = total // 20
total = total % 20

c10 = total // 10
total = total % 10

c5 = total // 5
total = total % 5

c2c = total // 2
total = total % 2

c1c = total

print("Banknotes of 500 euros:", b500)
print("Banknotes of 200 euros:", b200)
print("Banknotes of 100 euros:", b100)
print("Banknotes of 50 euros:", b50)
print("Banknotes of 20 euros:", b20)
print("Banknotes of 10 euros:", b10)
print("Banknotes of 5 euros:", b5)
print("Coins of 2 euros:", c2)
print("Coins of 1 euro:", c1)
print("Coins of 50 cents:", c50)
print("Coins of 20 cents:", c20)
print("Coins of 10 cents:", c10)
print("Coins of 5 cents:", c5)
print("Coins of 2 cents:", c2c)
print("Coins of 1 cent:", c1c)