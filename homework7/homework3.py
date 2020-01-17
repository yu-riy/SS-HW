str1 = 'rkqodlw\n'
str2 = 'world\n'

#Переводим строки в список
lst_a = list(str1)[:-1]
lst_b = list(str2)[:-1]

#Функция, принимает два списка и сравнивает их
def scramble(a, b):
    # list comprehension. Список из элементов массива b, которые входят в массив a
    x = [(lambda i, j: i)(i, j) for i in b for j in a if i == j ]
    # Если массив строка из массива х равна введеной строке, то ОК
    if "".join(x) == str2[:-1]:
        print("True")
    else:
        print("False")
        

scramble(lst_a, lst_b)

        
