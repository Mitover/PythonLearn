name = input()
number = int(input())
print(f"Группа №{number//100}.")
print(f"{number%10}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {number//10%10}.")


name = input()
number = input()
print("Группа  №" + number[0] + ".")
print(number[2] + "." + name + ".")
print("Шкафчик: " + number + ".")
print("Кроватка: " + number[1] + ".")