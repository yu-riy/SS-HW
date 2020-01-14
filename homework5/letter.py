import re

letter = """Yesterday, we bumped into Laura. It had to happen, but you can\'t
deny the timing couldn\'t be worse. The "mission" to try and seduce her
was a complete failure last month. By the way, she still has the ring
I gave her. Anyhow, it hasn\'t been a pleasurable experience to go
through it. I wanted to feel done with it first."""

#Разделение исходного текста на строки
substring = re.split("\.|\?|\!", letter)
#Удаление последнего пустого элемента списка
substring.pop()

print(substring)
def func(thestring):
    mass = []
    #Выбираем первую строку
    str = thestring[0]
    print(str)
    #Разбиваем на слова
    str_to_list = re.findall(r"\w+", str)
    
    #Перебор по элементам первой строки
    for i, str in enumerate(str_to_list):
        #Вычисление порядкового номера слов в строке
        wc = len(str_to_list[i])-1
        #Разбивает следующие строки на слова
        words = re.findall(r"\w+[^!\?\.\s]?\w+|\w", substring[i+1])
        #Наполняем итоговый список словаи
        mass.append(words[wc])
    #Сводим результат и выводим его на экран        
    result = (" ".join(mass)).capitalize()
    print(f"\n {result}.")

func(substring)
