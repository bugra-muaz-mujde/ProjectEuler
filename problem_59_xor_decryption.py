import time

start = time.time()

p59_cipher = open("p059_cipher.txt", "r")
encrypted_ascii_values = p59_cipher.read().split(",")
p59_cipher.close()


def decimal_to_binary(number):
    binary_list = [0] * 8
    for power in range(len(binary_list) - 1, -1, -1):
        if 2**power <= number:
            binary_list[(len(binary_list) - 1) - power] = 1
            number = number - 2**power
        else:
            binary_list[(len(binary_list) - 1) - power] = 0
    return binary_list


def binary_to_decimal(binary_list):
    decimal_number = 0
    for power, bit in enumerate(binary_list):
        if bit == 1:
            decimal_number += 2**((len(binary_list)-1) - power)
    return decimal_number


def a_xor_b(a, b):
    xor_list = [0] * len(a)
    for index in range(len(a)):
        if a[index] != b[index]:
            xor_list[index] = 1
        else:
            xor_list[index] = 0
    return xor_list


def decrypt(key_list, encrypted_list, ascii_list):
    index_number = 0
    text = ""
    while index_number < len(encrypted_list):
        for key_digit in key_list:
            decimal = binary_to_decimal(
                    a_xor_b(
                        decimal_to_binary(int(encrypted_list[index_number])), decimal_to_binary(int(key_digit))
                    )
                )
            index_number += 1
            try:
                text += str(ascii_list[decimal])
            except:
                text += " "
    return text



