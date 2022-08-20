
def check_square(number):
    count = 1
    for index, digit in enumerate(str(number)):
        if index % 2 == 0 and index != len(str(number)) - 1:
            if int(digit) != count:
                return False
            count += 1
    return True


count = 0
for i in range(10**9 + 70, 2 * 10**9, 100):
    if check_square(i**2):
        print(i)
        break

