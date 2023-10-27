
names = {"Андрей": 25, "Мария": 30, "Иван": 20, "Наталья": 35, "Петр": 27}

while True:
    name = input("Введите имя человека: ")
    if name in names:
        print(f"Возраст {name}: {names[name]} лет")
    else:
        print("НЕТУ ТАКОГО")










def count_zeros_in_factorial(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

number = int(input("Введите число: "))
zeros = count_zeros_in_factorial(number)
print(f"Количество нулей в конце факториала {number}: {zeros}")
