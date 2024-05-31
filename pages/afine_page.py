import tkinter as tk
from styles import Colors, Font, Sizes
#from pages.start_page import main_frame

def afine_frame(frame, window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text="Афинный шифр", font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)
    
    text_input = tk.Entry(frame, font=Font.base_font, width=15, justify=tk.CENTER)
    text_input.pack(pady=10)

    confirm_button = tk.Button(frame, font=Font.base_font, text='Confirm', bg=Colors.button_color, width=9,
                            command=lambda: goto_menu(frame, window))
    confirm_button.pack(pady=30)

    menu_button = tk.Button(frame, font=Font.base_font, text='Exit', bg=Colors.button_color, width=9,
                            command=lambda: goto_menu(frame, window))
    menu_button.pack(pady=30)

    def goto_menu(frame, windows):
        frame.destroy();
        window.destroy();
        #main_frame(window);
        