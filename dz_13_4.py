# 10.36. Составить процедуру, "рисующую" на экране вертикальную линию из любого числа символов "*".
def vertical_line(star):
    
    for i in range(star):
        print("*")
        
vertical_line(int(input("Введите любое число: ")))