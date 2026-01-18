# Напечатать числа в виде следующей таблицы:
# а) 5
# 5 5
# 5 5 5
# 5 5 5 5
# 5 5 5 5 5
# б) 1 1 1 1 1
# 1 1 1 1
# 1 1 1
# 1 1
# 1
   
for i in range (6):
    for j in range (i):
        print ("5",end="  ")
    print ()

for i in range (5, 0,-1):
    for j in range (i):
        print ("1",end="  ")
    print ()
