number = input()
number_list = number.split()

a = int(number_list[0])
b = int(number_list[1])
c = int(number_list[2])

if a * b == c:
    print("YES")
else:
    print("NO")