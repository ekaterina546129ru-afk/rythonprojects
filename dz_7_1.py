# 2.14. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали
# ее в конце. Найти полученное число.

number = int(input("Введите трехзначиное число: "))

first_digit = number // 100      
last_two_digits = number % 100 

new_number = last_two_digits * 10 + first_digit

print(f"Полученное чилсло {new_number}")

