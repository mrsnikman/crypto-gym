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
    
    text_input = tk.Entry(frame, font=Font.standard_font, width=15, justify=tk.CENTER)
    text_input.pack(pady=10) 

    encode_button = tk.Button(frame, font=Font.standard_font, text='Зашифровать', bg=Colors.button_color, width=9,
                            command=lambda: encode(frame, window))
    encode_button.pack(pady=30)

    decode_button = tk.Button(frame, font=Font.standard_font, text='Дешифровать', bg=Colors.button_color, width=9,
                            command=lambda: decode(frame, window))
    decode_button.pack(pady=30)

    menu_button = tk.Button(frame, font=Font.standard_font, text='Выход', bg=Colors.button_color, width=9,
                            command=lambda: goto_menu(frame, window))
    menu_button.pack(pady=30)

    def goto_menu(frame, windows):
        frame.destroy();
        window.destroy();
        #main_frame(window);

    def encode(frame, windows):
        input_path = text_input;
        encoded=encodeWiginer(input_path.get(), 'ананас')
        mb.showinfo('Полученные значения', encoded)
        encoded_file = open("texts/output/output.txt", "w")
        encoded_file.write(encoded)
        
    
    def decode(frame, windows):
        input_path = text_input;
        mb.showinfo('Полученные значения', decodeWiginer(input_path.get(), 'ананас'))
        