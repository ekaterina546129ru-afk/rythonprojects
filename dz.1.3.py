def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
n = int(input("Введите год: "))
if is_leap_year(n):
    print(f"{n} год - високосный")
else:
    print(f"{n} год - невисокосный")
    