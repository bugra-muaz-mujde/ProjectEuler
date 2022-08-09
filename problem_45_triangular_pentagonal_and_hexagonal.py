

def triangle(n):
    return int(n * (n + 1) / 2)


def pentagonal(n):
    return int(n * ((3 * n) - 1) / 2)


def hexagonal(n):
    return int(n * ((2 * n) - 1))


t = 285
p = 165
h = 143
start_numbers = [285, 165, 143]
perfect_triple = []

while True:
    triangle_number = triangle(t + 1)
    while True:
        pentagonal_number = pentagonal(p + 1)
        if pentagonal_number == triangle_number:
            perfect_triple.append(pentagonal_number)
            perfect_triple.append(triangle_number)
        elif pentagonal_number > triangle_number:
            break
        p += 1
    if len(perfect_triple) == 2:
        while True:
            hexagonal_number = hexagonal(h + 1)
            if hexagonal_number == triangle_number:
                perfect_triple.append(hexagonal_number)
            elif hexagonal_number > triangle_number:
                break
            h += 1
    t += 1
    if len(perfect_triple) == 3:
        t -= 1
        break
    else:
        perfect_triple = []

print(perfect_triple)