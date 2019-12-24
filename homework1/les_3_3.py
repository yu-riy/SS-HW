#Определяем функцию, которая производит ввод переменных пользователя
#и рассчет конечного значения
print("Проводим расчет сульфида тория\n")
def mainfunction():
    while True:
            N = int(input("\nВведите сколько панелей нужно обработать (значения от 1 до 100): "))
            if N is None or N not in range(1, 100):
                print("Пожалуйста, введите число от 1 до 100\n")
                continue
            else:
                break

    while True:
            A = int(input("Введите размер стороны A панелей (значения от 1 до 100): "))
            if A is None or A not in range(1, 100):
                print("Пожалуйста, введите число от 1 до 100\n")
                continue
            else:
                break

    while True:
            B = int(input("Введите размер стороны B панелей (значения от 1 до 100): "))
            if B is None or B not in range(1, 100):
                print("Пожалуйста, введите число от 1 до 100\n")
                continue
            else:
                break
    result = 2 * N * (A * B)
    print(f"Всего потребуется {result} нанограмм сульфида тория для покраски {N} панелей")

#Главное тело
while True:
    mainfunction()
    user_continue = input("\nПроведем расчеты еще раз? y/n \n")
    if user_continue in ["y", "Y"]:
        continue
    else:
        break
