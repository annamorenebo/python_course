inp_list = (input("введите целые числа через пробел:").split())
i = 0
while i < len(inp_list) - 1:
    inp_list[i], inp_list[i + 1] = inp_list[i + 1], inp_list[i]
    i += 2
print(" ".join(inp_list))
