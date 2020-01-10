import re
import string

test = "@@~~~~@@+@~@-@@~@@*@@/@@"

mass = [each for each in test]
operators = [each for each in test if each in "+-*/"]
mass = [[] for x in range(len(operators) + 1)]
operands = re.split('[+-/*]', test)


dict = {ord("@") : "1"}

def replacement(list_item):
    list_item = list_item.translate(dict)
    return(list_item)
        
re.split("()", test)


massive = (re.findall("@+|~+|\++|\-+|\*+|\/+", test))

c = massive
massive[:] = [each.translate(dict) for each in massive]
print(c)


