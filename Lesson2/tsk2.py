number = int(input("Введите целое положительное число: "))
max_dig = 0
while number > 0:
    dig = number % 10
    number = number // 10
    if dig > max_dig:
        max_dig = dig
print("самая большая цифра в числе: ", max_dig)
