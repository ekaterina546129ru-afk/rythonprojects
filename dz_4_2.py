# Известны оценки по информатике каждого ученика класса. Определить количество пятерок.

fiver = 0
students = int(input("Введите количество учеников:"))

for i in range(students):
    estimation = int(input("Введите оценку:"))
    if estimation == 5:
        fiver += 1
        print ("Количество пятерок:", fiver)