
def get_node_of_chain(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


longest_chain = 0
chain_counter = 1
longest_chain_number = 0
for collatz_number in range(2, 1000000):
    head_of_chain = collatz_number
    while head_of_chain != 1:
        head_of_chain = get_node_of_chain(head_of_chain)
        chain_counter += 1
    if longest_chain < chain_counter:
        longest_chain = chain_counter
        longest_chain_number = collatz_number
    chain_counter = 0

print(longest_chain_number)
print(longest_chain)