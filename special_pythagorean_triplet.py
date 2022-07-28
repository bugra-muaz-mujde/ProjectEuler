import math

total = 1000

for a in range(2, (total-3) // 3):
    for b in range(a + 1, (total - 1 - a) // 2):
        if (a ** 2 + b ** 2) == (total - a - b) ** 2:
            print(int(a * b * math.sqrt(a**2 + b**2)))
