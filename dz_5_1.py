# "Орешки"


N = int(input("Введите N(шишки с орешками):"))
M = int(input("Введите M(количество орешков):"))
K = int(input("Введите K(количество орешков для пропитания):"))

nuts_for_food = N * M

if nuts_for_food >= K:
    print("Yes")
else:
    print("No")

