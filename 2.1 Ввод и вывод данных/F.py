name = "Мандарины"#input()
price = 100#int(input())
weight = 5 # int(input())
money = 900 #int(input())
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - price * weight}руб")

# print("Чек")
# print(name, " - ", weight, "кг - ", price, "руб/кг", sep="")
# print("Итого: ", price * weight, "руб", sep="")
# print("Внесено: ", money, "руб", sep="")
# print("Сдача: ", money - price * weight, "руб", sep="")