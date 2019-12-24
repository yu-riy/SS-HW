# Task 3. Счастливый билет



#Общая функция ввода пользовательского значения и ее проверки
def input_and_check():
    while True:
        N = input()
        if N.isdigit() == False:
            print("Пожалуйста, введите число\n")
            continue
        if len(N) != 6 or int(N) not in range(1000000):
            print("Пожалуйста, введите именно шестизначное число\n")
            continue
        else:
            break
    return(list(N))

#Оcновная функция
def main_function():
    print("\nВведите номер Вашего билета, 6-тизначное число")
    ticket_number = (input_and_check())
    if ((int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]))\
           == (int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5]))):
        print("\nYES")
    else:
        print("\nNO")


#Цикл, в котором выполняется основная функция
while True:
    main_function()
    user_continue = input("\nПопробуем еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break
