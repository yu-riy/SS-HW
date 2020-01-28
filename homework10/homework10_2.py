class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


empl_john = Employee("John", 33)
empl_jack = Employee("Jack", 39)
empl_jim = Employee("Jim", 25)
empl_list = [empl_john, empl_jack, empl_jim]

class EmpTable:
    #def __init__(self):
    
    def getCode(self, emp):
        for i, each in enumerate(emp):
            
            print(f"This is {each.get_name()}, he is {each.get_age()} ")



table = EmpTable()
table.getCode(empl_list)

    
