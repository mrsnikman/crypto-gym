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

def decodeAffin(a, b, Arr):
    A= ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    a=invNum(a, 32)%32
    text=[]
    for i in range(len(Arr)):
        text.append((Arr[i]-b)*a%32)
        print(A[text[i]], end='')
    print()

#b = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

#30, 12, 28, 10, 22, 21, 22
a= textToArr('text.txt')

#for i in range(30):
#    for j in range(len(b)):
#        decodeAffin(b[j], i, [18, 27, 31, 27, 19, 19, 27, 21, 22])
#    print()

print()
decodeAffin(3, 12, a)

t=input()
            