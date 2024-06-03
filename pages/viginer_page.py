import tkinter as tk
import tkinter.messagebox as mb
from styles import Colors, Font, Sizes
from scripts.script_viginer import encodeWiginer, decodeWiginer
#from pages.start_page import main_frame

def viginer_frame(frame, window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text="Шифр Вижинёра", font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)
    
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
    key_input.insert(0, 'ананас')

    encode_button = tk.Button(frame, font=Font.standard_font, text='Зашифровать', bg=Colors.button_color, width=13,
                            command=lambda: encode(frame, window))
    encode_button.pack(pady=10)

    decode_button = tk.Button(frame, font=Font.standard_font, text='Дешифровать', bg=Colors.button_color, width=13,
                            command=lambda: decode(frame, window))
    decode_button.pack(pady=10)

    menu_button = tk.Button(frame, font=Font.standard_font, text='Выход', bg=Colors.button_color, width=13,
                            command=lambda: goto_menu(frame, window))
    menu_button.pack(pady=10)

    def goto_menu(frame, windows):
        frame.destroy();
        window.destroy();
        #main_frame(window);

    def encode(frame, windows):
        input_path = text_input;
        try:
            encoded=encodeWiginer(input_path.get(), 'ананас')
            mb.showinfo('Полученные значения', encoded)
        except:
            mb.showinfo('Ошибка.', 'Проверьте правильность введённого пути.')
        
        
    
    def decode(frame, windows):
        input_path = text_input;
        try:
            mb.showinfo('Полученные значения', decodeWiginer(input_path.get(), 'ананас'))
        except:
            mb.showinfo('Ошибка.', 'Проверьте правильность введённого пути.')
       
        