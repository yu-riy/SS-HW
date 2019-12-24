#Определяем переменные по условию задачи
var_sal = 50
var_str = 100
var_pun = 20

#Функция по условию 1 задачи. Сколько должен написать кода Василий
def vasya_wokr():
    while True:
        vasya_sal = int(input("Сколько хочет заработать Василий?': "))
        if vasya_sal is None or vasya_sal <= 0:
            print("Так нельзя!\nВведите положительное ненулевое число\n")
            continue
        else:
            break
    while True:    
        vasya_progul = int(input("\nА сколько дней Василий опаздывал на работу?': "))
        if vasya_progul is None or vasya_progul < 0:
            print("Так нельзя!\nВведите положительное ненулевое число\n")
            continue
        else:
            break
    shtraf = ((vasya_progul) // 3) * var_pun
    print("\nШтраф Василия за опоздания составляет: ", shtraf)
    codelines = ((vasya_sal + shtraf) * var_str) / var_sal
    if codelines % var_str != 0:
        total_codelines = codelines + (var_str - codelines % var_str)
        print(f"С учетом всего Василий должен написать {int(total_codelines)} строк кода")
    else:
        print(f"С учетом всего Василий должен написать {int(codelines)} строк кода")

#Функция по условию 2 задачи. Сколько можно опаздывать Василию
def vasya_late():
    while True:
        vasya_sal = int(input("Сколько хочет заработать Василий?': "))
        if vasya_sal is None or vasya_sal <= 0:
            print("Так нельзя!\nВведите положительное ненулевое число\n")
            continue
        else:
            break
    while True:
        vasya_codelines = int(input("\nА сколько Василий осилит написать строк кода?': "))
        if vasya_codelines is None or vasya_codelines <= 0:
            print("Так нельзя!\nВведите положительное ненулевое число\n")
            continue
        else:
            break
    if vasya_codelines < (vasya_sal * var_str) / var_sal:
        print("Так не получится!\nВасилий получает 100 долларов за строк кода!\n\
        Давайте попробуем еще раз!\n")
        vasya_late()
    else:
        progul = (var_sal * vasya_codelines / var_str - vasya_sal)/var_pun
        print(f"Количество допустимых опозданий Василия составляет от {int(progul*3)} до {int(progul*3+2)} дней")

#Функция по условию 3 задачи. Сколько заработает Василий
def vasya_zarplata():
    while True:
            vasya_codelines = int(input("Сколько Василий готов написать строк кода?': "))
            if vasya_codelines is None or vasya_codelines <= 0:
                print("Так нельзя!\nВведите положительное ненулевое число\n")
                continue
            else:
                break
    while True:    
        vasya_progul = int(input("\nА сколько дней Василий собирается опаздывать на работу?': "))
        if vasya_progul is None or vasya_progul < 0:
            print("Так нельзя!\nВведите положительное ненулевое число\n")
            continue
        else:
            break
    shtraf = ((vasya_progul) // 3) * var_pun
    print("\nШтраф Василия за опоздания составляет: ", shtraf)
    zarplata = ((vasya_codelines * var_sal) / var_str)
    if shtraf == 0:
        print(f"\nВасили может заработать {zarplata}")
    if shtraf > zarplata:
        print(f"\nПохоже, Василий много опаздывал и будет должен {zarplata}")
    else:
        print(f"\nВасилий планирует опаздывать, поэтому сможет заработать {int(zarplata)-int(shtraf)}")

#Главное тело
while True:
    user_choice = int(input("Нажмите цифру, чтобы выбрать: \n\
    1: Посчитать объем строк кода, что должен написать Василий\n\
    2: Посчтитать сколько Василий может позволить себе опозданий\n\
    3: Посчитать сколько Василий может заработать\n"))

    if user_choice == 1:
        vasya_wokr()
        
    elif user_choice == 2:
        vasya_late()
        
    else:
        vasya_zarplata()
    user_continue = input("\nПопробуем еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break


