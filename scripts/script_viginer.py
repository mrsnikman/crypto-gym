# coding: utf-8
import codecs
from scripts.script_textToArr import textToArr

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