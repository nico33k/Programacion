num = int(input())
hour = num // 3600
rest = num % 3600
minut = rest // 60
sec = rest % 60
print(hour, minut, sec)