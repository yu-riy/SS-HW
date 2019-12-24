# Task 1. Ремонт

#Общая функция ввода пользовательского значения и ее проверки
def input_and_check():
    while True:
        N = input()
        if N.isdigit() == False:
            print("Пожалуйста, введите число\n")
            continue
        if int(N) not in range(1, 1001):
            print("Пожалуйста, введите число от 1 до 1000\n")
            continue
        else:
            break
    return(int(N))

#Оcновная функция
def main_function():
    print("\nБудем подсчитывать площадь здания")
    print("\nВведите, пожалуйста, высоту здания, от 1 до 1000 метров :")
    heigh = input_and_check()
    print("\nТеперь введите, пожалуйста, ширину здания, от 1 до 1000 метров :")
    width = input_and_check()
    print("\nИ еще длинну здания, от 1 до 1000 метров :")
    lengh = input_and_check()
    print(f"\nИтак, у нас здание {lengh} на {width} на {heigh} метров")
    #Вычисляем площадь стен
    walls_area = 2 * (lengh * heigh + width * heigh)
    print(f"Значит нужно покрасить {walls_area} метров стен")
    paint_amount = int(walls_area / 16)
    print(f"А это {paint_amount} литров краски")

#Цикл, в котором выполняется основная функция
while True:
    main_function()
    user_continue = input("\nПроведем расчеты еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break
