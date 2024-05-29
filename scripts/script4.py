# coding: utf-8
import codecs

def invNum(a, n): #Функция нахождения обратного числа
    i=1
    for i in range(n*n):
        if (a*i)%n-1==0:
            return i
        elif (a*(-i))%n-1==0:
            return -i

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
    code = []
    while len(key)<len(text):
        key*=2
    for i in range(len(text)):
        code.append(A[(text[i]+A.index(key[i]))%32])
    return code

def decodeWiginer(e, key):
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    code = []
    text=[]

    for l in range(len(e)):
        for i in range(len(e[l])):
            for j in range(32):
                if e[l][i] == A[j] or e[l][i] == A[j].upper():
                    text.append(j)

    
    while len(key)<len(text):
        key*=2
    for i in range(len(text)):
        code.append(A[(text[i]-A.index(key[i]))%32])
    return code

def index_of_coincidence(text):
    total = len(text)
    frequencies = {char: text.count(char) for char in text}
    ic = sum(value * (value - 1)for value in frequencies.values()) / (total * (total - 1))
    return ic

def everyNum(text, num, i):
    redtext=''
    for j in range(i,len(text),num):
        redtext+=text[j]

    return redtext


#b = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

#30, 12, 28, 10, 22, 21, 22


#for i in range(30):
#    for j in range(len(b)):
#        decodeAffin(b[j], i, [18, 27, 31, 27, 19, 19, 27, 21, 22])
#    print()



print()
e=encodeWiginer('text.txt', 'ключ')
for i in range(len(e)):
    print(e[i], end='')

print()

for num in range(9):
    for i in range(num):
        # Example usage
        cipher_text = everyNum(e, num, i)
        result = index_of_coincidence(cipher_text)
        print(num, result)


#x=decodeWiginer(e, 'ключ')
#for i in range(len(x)):
#    print(x[i], end='')

#t=input()

#print(invNum(5, 576)%576)          