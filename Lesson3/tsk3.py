# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”})
products = []
property = {}
property_key_list = []
while input("Добавить параметр? да/нет ") == "да":
      property_key = input("параметр: ")
      property_key_list.append(property_key)
# print(property_key_list)
product_idx = 0
while input("хотите добавить товар? да/нет ") == "да":
      product_idx += 1
      prod_card_dict = {}
      for property_key in property_key_list:
            property_value = input(f"значение параметра:{property_key} ")
            prod_card_dict[property_key] = property_value

      # print(prod_card_dict)
      products.append((product_idx, prod_card_dict))
print(products)
# аналитика
analytics = {}
for property in property_key_list:
      analytics[property] = []
for product in products:
      analytics[property].append(product[1][property])
print(analytics)
