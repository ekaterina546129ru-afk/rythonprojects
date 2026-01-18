#2.19. Дано четырехзначное число. Найти:
#а) сумму его цифр;
#б) произведение его цифр.
number = int(input("Введите четырехзначное число: "))

number_str = str(number)

sum_of_digits = sum(int(digit) for digit in number_str)

product_of_digits = 1
for digit in number_str:
    product_of_digits *= int(digit)

print("Сумма цифр:", sum_of_digits)
print("Произведение цифр:", product_of_digits)