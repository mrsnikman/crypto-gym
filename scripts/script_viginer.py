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

def encodeWiginer(textpath, key):
    text = textToArr(textpath)
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
    code = ''
    while len(key)<len(text):
        key*=2
    for i in range(len(text)):
        code+=A[(text[i]+A.index(key[i]))%(len(A))]
    encoded_file = codecs.open("texts/output/output.txt", "w", encoding='utf-8')
    encoded_file.write(code)
    return code

def decodeWiginer(textpath, key):
    text = textToArr(textpath)
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
    code = ''
    while len(key)<len(text):
        key*=2
    for i in range(len(text)):
        code+=A[(text[i]-A.index(key[i]))%(len(A))]
    return code