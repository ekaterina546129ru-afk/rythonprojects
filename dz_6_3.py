# 11.21. В массиве хранятся сведения о количестве осадков, выпавших за каждый
# день января. Определить общее количество осадков за январь.

import random

precipitation = []
sum_precipitation = 0
days_in_January = 31

for i in range (days_in_January):
    precipitation.append(random.randint(0,7))
  
for i in range (days_in_January):
    sum_precipitation = sum_precipitation + precipitation[i]

print (f"Общее количество осадков за январь: {sum_precipitation} ")

    