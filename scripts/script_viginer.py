# coding: utf-8
import codecs

def textToArr(file):
    file = codecs.open(file, encoding='cp1251')

    a=[]
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    for line in file:
        for i in range(len(line)):
            for j in range(32):
                if line[i] == A[j] or line[i] == A[j].upper():
                    a.append(j)
    return a

def encodeWiginer(textpath, key):
    text = textToArr(textpath)
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    code = ''
    while len(key)<len(text):
        key*=2
    for i in range(len(text)):
        code+=A[(text[i]+A.index(key[i]))%32]
    return code

def decodeWiginer(textpath, key):
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    code = []
    text=textToArr(textpath)
    for l in range(len(text)):
        for i in range(len(text[l])):
            for j in range(32):
                if text[l][i] == A[j] or text[l][i] == A[j].upper():
                    text.append(j)