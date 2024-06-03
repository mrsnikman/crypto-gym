# coding: utf-8
import codecs

def textToArr(file):
    file = codecs.open(file, encoding='utf-8')

    a=[]
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
    for line in file:
        for i in range(len(line)):
            for j in range(len(A)):
                if line[i] == A[j] or line[i] == A[j].upper():
                    a.append(j)
    return a