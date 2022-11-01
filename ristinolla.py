"""
Ristinolla tkinterillä
Ronja, Malaz, Pauliina
"""

import tkinter as tk
import customtkinter as ctk

ctk.get_appearance_mode()
ikkuna = ctk.CTk()
ikkuna.resizable(False, False)
ikkuna.title('Ristinolla')

ctk.CTkLabel(ikkuna, text = 'Ristinolla').pack()

pelialue = ctk.CTkFrame(ikkuna, width = 300, height = 300)
ruudukko = []
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = ctk.CTkButton(pelialue, text = '', width = 10, height = 5)
        self.button.grid(row = x, column = y)

    def CTkreset(self):  
        self.button.configure(text="", bg='white')  
        self.value = None  

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

pelialue.pack(pady=10, padx=10)  

ikkuna.mainloop()