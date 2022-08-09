
years_dict = {}
start_day = 2

for year in range(1901, 2001):
    years_dict[year] = start_day
    if year % 100 == 0 and year % 400 == 0:
        start_day += 2
    elif year % 4 == 0 and year % 100 != 0:
        start_day += 2
    else:
        start_day += 1
    if start_day > 7:
        start_day = start_day % 7


thirty_days = [4, 6, 9, 11]
month_list = []

for key in years_dict:
    start_day = years_dict[key]
    for month in range(1, 13):
        month_list.append(start_day)
        if month == 2:
            if key % 4 == 0:
                start_day += 1
        elif month in thirty_days:
            start_day += 2
        else:
            start_day += 3
        if start_day > 7:
            start_day %= 7
    years_dict[key] = month_list
    month_list = []

counter = 0
for year in years_dict:
    for index, month in enumerate(years_dict[year]):
        if month == 7:
            counter += 1
print(counter)





