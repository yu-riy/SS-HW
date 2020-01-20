#Вводим значения интервала
print("Задайте интервал, в котором мы хотим найти максимальную силу четного числа")
from_n = int(input("Введите, пожалуйства, начало интервала, целое число:\n"))
to_n = int(input("Введите, пожалуйства, конец интервала, целое число:\n")) + 1

#Оставляет только четные числа
interval = [x for x in range(from_n, to_n) if x % 2 == 0]
print(interval)

#Функция, которая рекурсивно себе вызывает, пока данное число из интервала
#делится на 2
def even_strong(number):
    #Локальная перемена счетчик, которая накапливает количество итераций
    z = 0
    #Рекурсивная функция
    def recursion(number):
        nonlocal z
        if number % 2 == 0 and number / 2 >= 1 or number / 2 <= -1:
            
            z += 1
            
            recursion(number / 2)
        
        return(z)
    return recursion(number)

#Список, в котором ключ - это элемент первичного интервала,
#а значение - результат выполнения функции
answear = {}
answear = {each: even_strong(each) for each in interval}
strongness = max(answear.values())
print(strongness)

#Функция, которая выбирает со словаря ключи по максимальному значению
#и возвращает минимальное из чисел
def get_keys(dictionary, number):
    strong = []
    for key, value in dictionary.items():
        if value == number:
            strong.append(key)
    return min(strong)


print(get_keys(answear, strongness))
