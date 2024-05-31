import tkinter as tk
from styles import Colors, Font, Sizes
from texts import StartPage
from user import User
from pages.viginer_page import viginer_frame
from pages.afine_page import afine_frame

def main_frame(window):
    frame = tk.Frame(window, width=Sizes.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()

    tk.Label(frame, text="Меню", font=Font.base_font,
             bg=Colors.main_color,
             fg=Colors.text_color).pack(pady=50)

    Viginer_button = tk.Button(frame, font=Font.standard_font, text='Viginer', bg=Colors.button_color, width=9,
                            command=lambda: goto_viginer_page(frame, window))
    Viginer_button.pack(pady=30)

    Affine_button = tk.Button(frame, font=Font.standard_font, text='Affin', bg=Colors.button_color, width=9,
                            command=lambda: goto_affinne_page(frame, window))
    Affine_button.pack(pady=30)

    exit_button = tk.Button(frame, font=Font.standard_font, text='Exit', bg=Colors.button_color, width=9,
                            command=lambda: exit(frame, window))
    exit_button.pack(pady=30)

def goto_viginer_page(frame, window):
    frame.destroy();
    viginer_frame(frame, window)

def goto_affinne_page(frame, window):
    frame.destroy();
    afine_frame(frame, window)

def exit(frame, windows):
    frame.destroy();
    windows.destroy();