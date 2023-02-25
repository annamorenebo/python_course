number = int(input("введите трехзначное число"))
summ_digits = number % 10 + number // 10 % 10 + number // 100
print("сумма цифр: ", summ_digits)
