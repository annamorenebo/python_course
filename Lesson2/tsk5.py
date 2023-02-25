inp_list = input("введите слова через пробел:").split()
n = 0
for i in inp_list:
    n += 1
    print(f"{n}. {i[:10]}")
