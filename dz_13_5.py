# 10.37. Составить процедуру, "рисующую" на экране прямоугольник из символов "*". Задачу решить двумя способами:
# 1) не используя процедуру, разработанную в задаче 10.35;
# 2) с использованием процедуры, разработанной в задаче 10.35.

# 1)
def rectangle(weight, height):
    for i in range(height):
        for j in range(weight):
             print("*", end="")
        print()

print("Первый прямоугольник: ")
rectangle(7, 5)

# 2)
def second_rectangle(star):
    print("*" * star)
    
def is_second_rectangle(weight, height):
    for i in range(height):
        second_rectangle(weight)
        
print("Второй прямоугольник: ")
is_second_rectangle(7,5)