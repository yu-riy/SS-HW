import random


def increase(mass, count):
    def plus_one(mass, count):
        increased = mass[count] + 1
        mass[count] = increased
        return mass
    
    take_elem = mass[count]
   
    
    if count == 0:
        plus_one(mass, count)
                
    elif count in range(1, len(mass)) and mass[count] < 9:
        plus_one(mass, count)

    elif count in range(1, len(mass)) and mass[count] == 9:
        mass[count] = 0
        plus_one(mass, count-1)
            
   
    print(f"Рузльтирующий массив: {mass}")

while True:
    n = int(input("Введите, сколько разрядов будет иметь версия:\n"))
    
    version_mass = []
    for n in range (0, n):
        version_mass.append(random.randint(0, 9))
    print((f"Исходный массив: {version_mass}"))
    incr = int(input(f"Введите, какой разряд будет увеличен, от 1 до {n+1}:\n"))-1
    increase(version_mass, incr)


