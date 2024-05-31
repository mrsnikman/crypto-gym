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
    
    text_input = tk.Entry(frame, font=Font.base_font, width=15, justify=tk.CENTER)
    text_input.pack(pady=10)

    confirm_button = tk.Button(frame, font=Font.base_font, text='Confirm', bg=Colors.button_color, width=9,
                            command=lambda: encode(frame, window))
    confirm_button.pack(pady=30)

    menu_button = tk.Button(frame, font=Font.base_font, text='Exit', bg=Colors.button_color, width=9,
                            command=lambda: goto_menu(frame, window))
    menu_button.pack(pady=30)

    def goto_menu(frame, windows):
        frame.destroy();
        window.destroy();
        #main_frame(window);

    def encode(frame, windows):
        input_path = text_input;
        mb.showinfo('Полученные значения', encodeWiginer(input_path.get(), 'ананас'))
        