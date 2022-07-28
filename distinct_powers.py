
distinct_powers = []
for a in range(2, 101):
    for b in range(2, 101):
        distinct_powers.append(a**b)

distinct_powers = list(set(distinct_powers))
print(len(distinct_powers))
