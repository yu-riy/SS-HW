#Morse decoder
#Объявляем словарь - соответствие символов коду Морзе
morse_dict = {\
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
    }

#Разбиваем код на слова, после удаления пробельных символов в начале и конце
morse = (input("Введите сообщение в коде Морзе:\n")).strip()
morse_list = morse.split("   ")

#Генерируем двумерный списоп - разбиваем слова на символы
morse_letters = [each.split() for each in morse_list]
#print(morse_letters)

#Функция, которая ставит в соответсвие символу в коде Морзе символ в Латинице
def morse_decode(dictionary, lst):
    decoded_morse = []
    for each in lst:
        print(each)
        for key, value in dictionary.items():
            if value == each:
                decoded_morse.append(key)
    return(decoded_morse)

#Применяем функцию на элементах массива с символами
morse_list[:] = [morse_decode(morse_dict, each) for each in morse_letters]
#Соединяем символы в слова
morse_list[:] = ["".join(each) for each in morse_list]
#Соединяем слова в предложения
answear = " ".join(morse_list)
print(answear)
