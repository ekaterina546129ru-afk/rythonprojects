N = int(input("введите N: "))
watermelons = []
min_watermelon = 0
max_watermelon = 0

for i in range(N):
    value = int(input(f"введите массу {i+1} арбуза: "))
    watermelons.append(value)


min_watermelon = watermelons[0]

for i in range(N):
    if watermelons[i] < min_watermelon:
        min_watermelon

    
    