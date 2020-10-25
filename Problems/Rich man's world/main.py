deposit = int(input())
y = 0
while deposit <= 700000:
    deposit *= 1.071
    y += 1
print(y)
