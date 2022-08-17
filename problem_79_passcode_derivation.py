
f = open("p079_keylog.txt", "r")
pass_codes = f.read().split("\n")
f.close()

pass_codes = list(set(pass_codes))
pass_codes.sort()

pass_index = 0
pass_string = ""
chain_list = []
chain = []
while pass_index < len(pass_codes):
    current_number = pass_codes[pass_index]
    chain.append(current_number)
    for pass_code in pass_codes:
        if current_number[1:] == pass_code[:2]:
            chain.append(pass_code)
    chain_list.append(chain)
    chain = []
    pass_index += 1

print(chain_list)
print(pass_codes)
"""
73162890
316 -> 160 -> 2

316 -> 162 -> 620 -> 3
316 -> 162 -> 629 -> 890 -> 4

73162890
316 -> 168 -> 680 -> 3
316 -> 168 -> 689 -> 890 -> 4

716 -> 160
716 -> 162
716 -> 168

731 -> 316
731 -> 318
731 -> 319
"""