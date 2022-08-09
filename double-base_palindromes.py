
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


sum_of_all_numbers = 0

for positive_integer in range(1, 1000000):
    if is_palindrome(positive_integer):
        if is_palindrome(bin(positive_integer)[2::]):
            sum_of_all_numbers += positive_integer
print(sum_of_all_numbers)



