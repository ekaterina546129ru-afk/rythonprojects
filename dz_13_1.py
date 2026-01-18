# 10.15. Найти все трехзначные простые числа. (Определить функцию, позволяющую
# распознавать простые числа.)

def is_simple(numbers):
    if numbers <= 100:
        return False
    
    if numbers == 2:
        return True
    
    if numbers % 2 == 0:
        return False
        
    return True
    
for numbers in range(100, 1000):
    if is_simple(numbers):
        print(numbers)