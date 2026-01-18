# Сбор земляники 
number = input()
number_list = number.split()

X = int(number_list[0])
Y = int(number_list[1])
Z = int(number_list[2])

if Z > (X + Y):
    print("Impossible")
else:
    answer = (X + Y) - Z
    print(answer)

