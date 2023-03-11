month = int(input("введите месяц в виде целого числа от 1 до 12: "))
season_dict = {0: "winter", 1: "spring", 2: "summer", 3: "autumn"}
if month < 12:
    print(season_dict.get(month // 3))
else:
    print(season_dict[0])

