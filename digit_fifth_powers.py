
fifth_powers = []
powers_dict = {}

for digit in range(0, 10):
    fifth_powers.append(digit**5)

for power in range(0, len(fifth_powers)):
    for other_powers in range(0, len(fifth_powers)):
        pass