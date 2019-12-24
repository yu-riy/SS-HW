# Task 2. Песок

#Общая функция ввода пользовательского значения и ее проверки
def input_and_check():
    while True:
        N = input()
        if N.isdigit() == False:
            print("Пожалуйста, введите число\n")
            continue
        if int(N) not in range(1, 101):
            print("Пожалуйста, введите число от 1 до 100\n")
            continue
        else:
            break
    return(int(N))

#Оcновная функция
def main_function():
    print("\nВведите стоимость песка, не более 100 рублей за килограмм")
    print("\nпервого вида :")
    A1 = input_and_check()
    print("\nвторого вида :")
    A2 = input_and_check()
    print("\nи третьего вида :")
    A3 = input_and_check()
    print("\nТеперь введите объем тары в килограммах")
    print("\nпервая емкость :")
    B1 = input_and_check()
    print("\nвторая емкость :")
    B2 = input_and_check()
    print("\nтретья емкость :")
    B3 = input_and_check()
    sand_cost = sorted([A1, A2, A3])
    capacity = sorted([B1, B2, B3])
    result = sand_cost[0] * capacity[0] + sand_cost[1] * capacity[1] + sand_cost[2] * capacity[2]
    print(f"Всего получится заработать {result} рублей")


#Цикл, в котором выполняется основная функция
while True:
    main_function()
    user_continue = input("\nПроведем расчеты еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break
