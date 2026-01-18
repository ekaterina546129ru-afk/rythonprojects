# В массиве записаны оценки ученика по 10 предметам. Определить общее
# количество четверок и пятерок.

import random

grades = []

for _ in range (20):
    grades.append(random.randint(2, 5))
print (f"Оценки ученика: {grades}")
    
quantity_4 = grades.count(4)
quantity_5 = grades.count(5)

print (f"Количество четверок:{quantity_4}")
print (f"Количество пятерок:{quantity_5}")

good_grades = quantity_4 + quantity_5
print (f"Количество четверок и пятерок: {good_grades}")
