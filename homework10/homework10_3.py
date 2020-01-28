class Circle():
    def __init__(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius

    def get_diametr(self):
        return (self.get_radius() * 2)
    
    def set_radius(self, new_radius):
        self.radius = new_radius

    def area(self):
        return self.radius**2*3.14
    
    def circle_lenght(self):
        return 2*self.radius*3.14

inp = int(input("Введите радиус окружности:\n"))
example = Circle(inp)

print("Исходный радиус:\n")
print(example.get_radius())
print("Установим новый радиус")
example.set_radius(5)
print("и получим его:\n")
print(example.get_radius())
print("Получим диаметр:\n")
print(example.get_diametr())
print(f"Площадь окружности {example.area()}")
print(f"Длинна окружности {(example.circle_lenght()):.2f}")
