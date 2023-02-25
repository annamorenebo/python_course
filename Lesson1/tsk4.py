revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if costs < revenue:
    rent = (revenue - costs) / revenue
    print("прибыль, рентабельность ", rent)
    people = int(input("Введите число сотрудников: "))
    rentForPeople = (revenue - costs) / people
    print("прибыль фирмы в рассчете на одного сотрудника", rentForPeople)
elif costs == revenue:
    print("прибыли нет, убытка нет")
else:
    print("убыток")
