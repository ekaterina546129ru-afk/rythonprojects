# 11.54. Дан массив. Найти:
# а) сумму элементов массива, значение которых не превышает 20;
# б) сумму элементов массива, больших числа a.

import random

my_collection = []

for i in range (10):
    my_collection.append(random.randint(1,50))
    
print (my_collection)

# а) сумму элементов массива, значение которых не превышает 20;

sum_a = 0

for i in range(10):
    if my_collection[i] <= 20:
        sum_a = sum_a + my_collection[i]

print (sum_a)

# б) сумму элементов массива, больших числа a.

a = 20
sum_b = 0

for i in range(10):
    if my_collection[i] >= a:
        sum_b = sum_b + my_collection[i]

print (sum_b)
        

    

