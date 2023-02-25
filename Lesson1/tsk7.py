number = int(input("номер билетика:"))
first_3_digits = number // 1000
sum1 = first_3_digits % 10 + first_3_digits // 10 % 10 + first_3_digits // 100
second_3_digits = number % 1000
sum2 = second_3_digits % 10 + second_3_digits // 10 % 10 + second_3_digits // 100
if sum1 == sum2:
    print("yes")
else:
    print("no")
