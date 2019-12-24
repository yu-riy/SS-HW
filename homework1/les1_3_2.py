#Камень-Ножницы-Бумага

import random
import time
def play_game():
    knb = {1: "Камень", 2: "Ножницы", 3: "Бумага"}
    user_choice = int(input("Нажмите цифру, чтобы выбрать: \n\
    1 - Камень\t\
    2 - Ножницы\t\
    3 - Бумага\n"))

    print(f"Вы выбрали {knb.get(user_choice)}")
    time.sleep(1)
    print("\nВыбирает компьютер...")
    time.sleep(1)
    a = int(random.randint(1, 3))
    print(f"\nКомпьютер выбрал {knb.get(a)}")

    if user_choice == 1 and a == 2 or \
       user_choice == 2 and a == 3 or \
       user_choice == 3 and a == 1:
        print("\nВы победили!")
    elif user_choice == a :
        print("\nНичья!")
    else:
        print("\nВы проиграли!")

#Основное тело
print("Хочу сыграть в игру\n")
while True:
    play_game()
    play_more = input("Сыграем еще? y/n")
    if play_more in ['y', 'Y']:
        continue
    else:
        break

    
