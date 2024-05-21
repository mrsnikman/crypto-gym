# coding: utf-8
import codecs


def count_letters(file):
    file = codecs.open(file, encoding='cp1251')

    result = ""
    i = 0
    A= ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    for line in file:
        for i in range(len(line)):
            for j in range(33):
                if line[i] == A[j] or line[i] == A[j].upper():
                    result += line[i].lower()
                    
    print(result)


    
count_letters('text.txt')
            