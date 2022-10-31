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

ikkuna.mainloop()