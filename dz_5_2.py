# Сбор земляники
X = int(input("Введите X(собрала Маша):"))
Y = int(input("Введите Y(собрал Миша):"))
Z = int(input("Введите Z(они съели):"))

sum_berries = X + Y - Z

if sum_berries >= 0:
    print (sum_berries)
else:
    print("Impossible")