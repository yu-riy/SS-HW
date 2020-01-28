import os

def print_file(filename):
    fd = open(filename, "r")
    delimiter = "*"
    mass = []
    for row in fd:
        mass.append(row.strip().split(delimiter))
    table_format(mass)
    fd.close()
    
#Форматированный вывод таблицы  
def table_format(body):
    #количество элементов
    lenght = len(body[0])
    #инициализация списка для определения ширины элементов
    width = [0]*lenght
    output = ""
    #наполнения списка по максимальной ширине элементов
    for row in body:
        for j, col in enumerate(row):
            width[j] = max(width[j], len(col))

    #форматированный вывод  
    for row in body:
        for each in range(len(row)):
            output += "| {:{}}".format(row[each], width[each])
        output += "|\n"
    print(output)
        

def append_table(filename, ui):
    fd = open(filename, "r")
    
    delimiter = "*"
    
    mass = []
    rows = 0
    for row in fd:
        mass.append(row.strip().split(delimiter))
        rows += 1
        
    books = []
    for row in range(1, len(mass)):
        books.append(mass[row][1])
    fd.close()
    
    if ui in books:
        print("Your book is already in the list!")
        your_book = books.index(ui)+1
        print(your_book)
        print(f"Book index is {mass[your_book][0]}, it is: {', '.join(mass[your_book][1:])}")
        
    else:
        print("There is no such book in the list...adding")
        
        fd = open(filename, "a+")
        index = str(rows - 1)
        b_author = str(input("Enter author:\n"))
        b_genre = str(input("Enter genre:\n"))
        b_publisher = str(input("Enter publisher:\n"))
        b_year = str(input("Enter year of publishment:\n"))
        b_price = str(input("Enter price:\n"))
        lst_book = [index, ui, b_author, b_genre, b_publisher, b_year, b_price]
        new_book = "*".join(lst_book)
        fd.write(new_book)
        fd.close()
        print(new_book)
          
while True:
    user_choice = int(input("Нажмите цифру, чтобы выбрать: \n\
    1: Вывести содержимое файла\n\
    2: Добавить книгу в список\n"))

    if user_choice == 1:
        print_file("book.txt")
        
    else:
        ui = input("Введите название книги\n")
        append_table("book.txt", ui)
    user_continue = input("\nПопробуем еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break

 
