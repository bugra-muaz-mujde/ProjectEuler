
coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
for index, coin in enumerate(coin_list):
    coin_list[index] = (5040 * 8) / (200 / coin)


print(sum(coin_list))