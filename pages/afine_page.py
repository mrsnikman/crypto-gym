import tkinter as tk
import tkinter.messagebox as mb
from styles import Colors, Font, Sizes
from scripts.script_affine import encodeAffine, decodeAffine
#from pages.start_page import main_frame

def afine_frame(frame, window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text="Афинный Шифр", font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=30)
    
    tk.Label(frame, text="Путь к файлу: ", font=Font.little_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack()
    
    text_input = tk.Entry(frame, font=Font.standard_font, width=20, justify=tk.CENTER)
    text_input.pack(pady=10) 
    text_input.insert(0, 'texts/input/simples/text_simple.txt')

    tk.Label(frame, text="Ключ: ", font=Font.little_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack()
    
    key_input = tk.Entry(frame, font=Font.standard_font, width=20, justify=tk.CENTER)
    key_input.pack(pady=10) 
    key_input.insert(0, '2 5')

    encode_button = tk.Button(frame, font=Font.standard_font, text='Зашифровать', bg=Colors.button_color, width=13,
                            command=lambda: encode(frame, window))
    encode_button.pack(pady=10)

    decode_button = tk.Button(frame, font=Font.standard_font, text='Дешифровать', bg=Colors.button_color, width=13,
                            command=lambda: decode(frame, window))
    decode_button.pack(pady=10)

    help_button = tk.Button(frame, font=Font.standard_font, text='Помощь', bg=Colors.button_color, width=13,
                            command=lambda: help(frame, window))
    help_button.pack(pady=10)

    menu_button = tk.Button(frame, font=Font.standard_font, text='Выход', bg=Colors.button_color, width=13,
                            command=lambda: goto_menu(frame, window))
    menu_button.pack(pady=10)

    def goto_menu(frame, windows):
        frame.destroy();
        window.destroy();
        #main_frame(window);

    def encode(frame, windows):
        input_path = text_input.get()
        keyA = int(key_input.get().split()[0])
        keyB = int(key_input.get().split()[1])


        try:
            encoded=encodeAffine(input_path, keyA, keyB)
            mb.showinfo('Полученные значения', encoded)
        except:
            mb.showerror('Ошибка.', 'Проверьте правильность введённого пути или ключа.')
        
        
    
    def decode(frame, windows):
        input_path = text_input.get();
        keyA = int(key_input.get().split()[0])
        keyB = int(key_input.get().split()[1])

        try:
            mb.showinfo('Полученные значения', decodeAffine(input_path, keyA, keyB))
        except:
            mb.showerror('Ошибка.', 'Проверьте правильность введённого пути.')
    
    def help(frame, windows):
        mb.showinfo('Помощь. ', 'Афинный Шифр -  это частный случай более общего моноалфавитного шифра подстановки. Шифрование производится согласно формуле: Cj=(a*Mj+b)modn, а расшифрование производится через умножение на обратное число a^-1: Mj=(a^-1)*(Cj-b)modn. ')
    