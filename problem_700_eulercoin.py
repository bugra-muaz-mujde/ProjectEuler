
sum_of_eulers = 1504170715041707
current_euler = 1504170715041707
euler_mod = 4503599627370517
n = 1
counter = 0
euler = 1
while True:
    euler = current_euler * n % euler_mod
    if current_euler > euler:
        n = round(euler_mod / current_euler) - 1
        sum_of_eulers += euler
        current_euler = euler
        counter += 1
        print(euler)
    else:
        n += 1

print(sum_of_eulers)


