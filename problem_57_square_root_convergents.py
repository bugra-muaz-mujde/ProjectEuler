import sys
sys.setrecursionlimit(1003)

def get_denominator(numerator, numerator_2, denominator, iteration):
    if iteration < 1:
        return numerator, numerator_2, denominator, iteration
    return get_denominator(
        2,
        denominator,
        ((numerator * denominator) + numerator_2),
        iteration - 1
    )


counter = 0
for iteration in range(2, 1000):
    results = get_denominator(2, 1, 2, iteration)
    if len(str(results[1] + results[2])) > len(str(results[2])):
        counter += 1
print(counter)