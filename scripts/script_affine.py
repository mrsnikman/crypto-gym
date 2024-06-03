# coding: utf-8
import codecs
from scripts.script_textToArr import textToArr
from scripts.script_invNum import invNum

def encodeAffine(textpath, a, b):
    text = textToArr(textpath)
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
    code = ''
    for i in range(len(text)):
        code+=A[(a*text[i]+b)%(len(A))]
    encoded_file = codecs.open("texts/output/output.txt", "w", encoding='utf-8')
    encoded_file.write(code)
    return code

def decodeAffine(textpath, a, b):
    text = textToArr(textpath)
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
    code = ''
    invA=invNum(a, len(A))
    for i in range(len(text)):
        code+=A[(invA*(text[i]-b))%(len(A))]
    return code