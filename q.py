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