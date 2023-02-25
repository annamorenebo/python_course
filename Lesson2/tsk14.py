lim_N = int(input("введите верхнюю границу"))
pow_2 = 2
k = 0
while pow_2 <= lim_N / 2:
    k = k + 1
    pow_2 = 2 ** k
    print(f"2^{k} = {pow_2}")
