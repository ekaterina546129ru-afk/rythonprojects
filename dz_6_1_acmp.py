# Четырехзначный палиндром
number = int(input("Введите четырёхзначное число: "))

digit_1 = number // 1000
digit_2 = (number //100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10

if digit_1 == digit_4 and digit_3 == digit_2:
    print ("Yes")
else:
    print ("NO")
    