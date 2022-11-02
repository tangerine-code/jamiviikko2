from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter import ttk
from tkinter import Button
from ctypes import windll
import tkinter as tk
from tkinter.font import BOLD
from tkinter.messagebox import showinfo
import sys
import os
from PIL import Image, ImageTk

#_____________________________FUNKTIOT JA LUOKAT________________________________

def uusiksi():
    """Käynnistää ikkunan uudestaan. Funktio ei palauta mitään,
    jos haluaa laskea voitot ja häviöt niin täytyy ottaa talteen kaikki
     tiedot ennen tämän kutsumista kutsumista!"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

class hoveri(Button):
    """Pelialueen ruudukon nappien hover."""
    def __init__(self, root, kuva1, kuva2, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.kuva1 = ImageTk.PhotoImage(Image.open(kuva1))
        self.kuva2 = ImageTk.PhotoImage(Image.open(kuva2))

        self['image'] = self.kuva1
        
        self.bind('<Enter>', self.onEnter1)
        self.bind('<Leave>', self.onLeave1)

    def onEnter1(self, event):
        self.config(image=self.kuva2)  

    def onLeave1(self, event):
        self.config(image=self.kuva1)

def onEnter(event):
    """Kun kursori menee 'lopeta' napin päälle, kuva muuttuu tummemmaksi"""
    global lopeta
    lopeta = ImageTk.PhotoImage(Image.open(r'lopeta_hover.png'))
    lopeta_nappi.config(image=lopeta)

def onEnter2(event):
    """Kun kursori menee 'uudestaan' napin päälle, kuva muuttuu tummemmaksi"""
    global uudestaan
    uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan_hover.png'))
    uudestaan_nappi.config(image=uudestaan)   

def onLeave(event):
    """Kun kursori lähtee 'lopeta' napin päältä, kuva palaa entiselleen"""
    global lopeta
    lopeta = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
    lopeta_nappi.config(image=lopeta)

def onLeave2(event):
    """Kun kursori lähtee 'uudestaan' napin päältä, kuva palaa entiselleen"""
    global uudestaan
    uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
    uudestaan_nappi.config(image=uudestaan)

#__________________________________RUNKO________________________________________
root = Tk()
root.title("Ristinolla")
st = ttk.Style()
#Keskitetään runko ikkuna, määritellään koko, muutettavuus, prioriteetti
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)
root.title("Ristinolla")
root.attributes('-topmost', 1)

#_________________________________KUVAT_________________________________________

lopeta = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
kissa = PhotoImage(file=r"cat.png")
hiiri = PhotoImage(file=r"mouse.png")
peli_kuva1 = r"not_pressed.png"
peli_kuva2 = r"hover.png"
iconi =PhotoImage(r'icon.ico')

#________________________________PELIALUE_______________________________________

play_area = tk.Frame(root, width = 300, height = 400)  
XO_points = []

class XOPoint:
    """Peliruudukko."""
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
        self.value = None  
        self.nappi = hoveri(play_area,  kuva1 = peli_kuva1, kuva2 = peli_kuva2, 
        borderwidth = 0, width = 100, height = 100)
        self.nappi.grid(row = x, column = y, pady = 5, padx = 5) 

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

play_area.pack(pady = 10, padx = 10, side = tk.LEFT)

#______________________________PELAAJIEN NIMET__________________________________

lbl = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15', BOLD), 
fg='#543f2a')
lbl.place(x=410, y=35)

lbl2 = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15', BOLD), 
fg='#543f2a')
lbl2.place(x=410, y=60)

#____________________________UUDESTAAN JA LOPETA________________________________

lopeta_nappi = Button(root, image = lopeta, borderwidth=0, height= 75, width=189,
command=root.destroy)
lopeta_nappi.place(x=400, y=285)
lopeta_nappi.bind('<Enter>',  onEnter)
lopeta_nappi.bind('<Leave>',  onLeave)

uudestaan_nappi = Button(root, image = uudestaan, borderwidth=0, height= 75, width=189,
command = uusiksi)
uudestaan_nappi.place(x=400, y=200)
uudestaan_nappi.bind('<Enter>',  onEnter2)
uudestaan_nappi.bind('<Leave>',  onLeave2)
#___________________________________MUUT________________________________________

windll.shcore.SetProcessDpiAwareness(1)
root.iconbitmap(iconi)
root.mainloop()
