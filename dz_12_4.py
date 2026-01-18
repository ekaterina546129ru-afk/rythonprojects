# Зарплата 
salary = input()
salary_list = salary.split()

A = int(salary_list[0])
B = int(salary_list[1])
C = int(salary_list[2])

max_valye = int(max(A, B, C))
min_valye = int(min(A, B, C))

answer = max_valye - min_valye

print(answer)