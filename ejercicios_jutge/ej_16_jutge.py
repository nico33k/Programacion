num = []
num = input().split()
hour = int(num[0])
minut = int(num[1])
sec = int(num[2])
sec += 1
if sec == 60:
    sec = 0
    minut += 1
if minut == 60:
    minut = 0
    hour += 1
if hour == 24:
    hour = 0
print(f'{hour:02d}:{minut:02d}:{sec:02d}')