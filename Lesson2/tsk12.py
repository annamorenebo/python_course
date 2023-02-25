import math
import random

number1 = random.randint(0, 1000)
number2 = random.randint(0, 1000)
print(f"Петя задумал:{number1}, {number2}")
S = number1 + number2
P = number1 * number2
print(f"сумма:{S}")
print(f"произведение:{P}")
D = S * S - 4 * P
a1 = (S + math.sqrt(D)) / 2
a2 = (S - math.sqrt(D)) / 2
print(f"Катя получила:{int(a1)}, {int(a2)}")
