def invNum(a, n): #Функция нахождения обратного числа
    i=1
    for i in range(n*n):
        if (a*i)%n-1==0:
            return i
        elif (a*(-i))%n-1==0:
            return -i