#Класс обычного маркера
class Marker:
    def __init__(self, color):
        self.color = color
        self.ink_ratio = 1
        self.ink_consumption = 0.005

    #метод, который вычисляет объем печатных символов
    def print_amount(self, text):
        self.text_amount = 0
        for each in text:
            if each not in ["\t","\r"] and (each.isspace() == False):
                self.text_amount += 1
        return self.text_amount

    #метод, который выводит текс
    def marker_print(self, text, color):
        amount = self.print_amount(text)
        op = self.ink_ratio - amount * self.ink_consumption
        if self.ink_ratio == 0:
            print("Маркер кончился...")
            

        elif op > 0:
            self.ink_ratio -= amount * self.ink_consumption
            print(f"--Печатает цветом {color}")
            print(text)
             
        else:
            word_count = int(self.ink_ratio / self.ink_consumption)
            text_part = text[:word_count]
            print(f"--Печатает цветом {color}")
            print(text_part)
            print(f"\nЗаправка кончилась(")
            self.ink_ratio = 0
            
#Класс заправляемого маркера
class Refillable(Marker):
    def __init__(self, color):
        super().__init__(self)
    
    def refill(self):
        print(f"Уровень заправки равен {self.ink_ratio}...заправляем")
        self.ink_ratio = 1
        print(f"Теперь уровень заправки равен {self.ink_ratio}")
        
        
        
marker_bl = Marker("black")
marker_r = Refillable("red")
marker_g = Marker("green")
marker_b = Marker("blue")
                    
markers = {"black" : marker_bl ,\
           "red"  : marker_r ,\
           "green"  : marker_g ,\
           "blue"  : marker_b ,\
    }

#Список маркеров, уровень из заправка показывает опция 2
#Опция 1 выводит на печать текст пользователся, а также позволяет выбрать цвет
#маркера из меню 2
#Уровень заправки маркера после каждой итерации меняется, его изменение можно
#посмотреть в менб 2 осле каждой печати

while True:
    user_choice = int(input("\nНажмите цифру, чтобы выбрать: \n\
    1: Печатать текст\n\
    2: Показать список маркеров\n\
    3: Выход\n"))

    if user_choice == 1:
        input_text = input("Введите текст для печати\n")

        while True:
            input_color = input("Каким маркером хотите печатать\n")

            if input_color not in markers.keys():
                print("Такого цвета нет, пожалуйста попробуйте еще раз")
                continue
            else:
                break
        markers[input_color].marker_print(input_text, input_color)

        if input_color == "red" and markers[input_color].ink_ratio == 0:
            print("... заправить? y/n")
            user_continue = input("\nПопробуем еще раз? y/n \n")
            if user_continue in ["y", "Y"]:
                markers["red"].refill()
            else:
                break
        

    elif user_choice == 2:
        for key, value in markers.items():
            print(f"{key} имеет количество заправки {(markers[key].ink_ratio * 100):.3f}%")
        
    elif user_choice == 3:
         break



