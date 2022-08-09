
def get_factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


print(
    get_factorial(40) / (get_factorial(20) * get_factorial(20))
)
