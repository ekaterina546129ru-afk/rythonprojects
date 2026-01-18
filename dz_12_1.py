# Орешки
nuts = input()
nuts_list = nuts.split()

N = int(nuts_list[0])
M = int(nuts_list[1])
K = int(nuts_list[2])

nuts_for_food = N * M

if nuts_for_food >= K:
    print("YES")
else:
    print("NO")
