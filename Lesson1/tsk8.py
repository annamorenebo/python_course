n = int(input("сколько долек в шоколадке в длину?"))
m = int(input("сколько долек в шоколадке в ширину?"))
k = int(input("сколько нужно отломить?"))
if k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")
