from tkinter import *

def reload(x):
    return x

def create_wigets():
    
    menu = Entry(root)
    menu.grid(row=0, column=0, columnspan=3)
    root.mainloop() #отображение окна    
    return

if __name__ == '__main__':
    root = Tk()
    root.title('Тренажёр') #заголовок
    root['bg']='#fafafa'
    root.geometry('500x500')
    root.resizable(width=False, height=False)
    create_wigets();    

