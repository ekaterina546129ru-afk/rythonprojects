import math

number = 0

while number <= 0:
    number = float(input("Введите число для извлечения квадратного корня:"))
    
    if number <= 0:
        print("Ошибка.Вы ввели число меньшее или равное нулю.")
         
result = math.sqrt(number)

print(f"Квадратный корень из числа {number} = {result}")