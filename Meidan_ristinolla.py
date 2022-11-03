"""Pauliina, Ronja, Malaz 2022 Jamiviikko2"""
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
    """Käynnistää ikkunan uudestaan"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

class pelipainike(Button):
    """Pelialueen ruudukon nappien hover"""
    def __init__(self, root, kuva1, kuva2, kuva3, kuva4, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.kuva1 = koskematon
        self.kuva2 = hovervari
        self.kuva3 = kissa
        self.kuva4 = hiiri


        self['image'] = self.kuva1
        
        #self.bind('<Enter>', self.onEnter1)
        #self.bind('<Leave>', self.onLeave1)        

    # def onEnter1(self, event):
    #     if self.kuva1:
    #         self.config(image=self.kuva2)
        # elif self.kuva3:
        #     self.config(image=self.kuva3)
        # elif self.kuva4:
        #     self.config(image = self.kuva4)

    # def onLeave1(self, event):

    #     if self.kuva2:
    #             self.config(image=self.kuva1)
    #     elif self.kuva3:
    #             self.config(image=self.kuva3)
    #     elif self.kuva4:
    #             self.config(image = self.kuva4)
    #     else:
    #         pass

def lopetaEnter(event):
    global lopeta
    lopeta = ImageTk.PhotoImage(Image.open(r'lopeta_hover.png'))
    lopeta_nappi.config(image=lopeta)

def uudestaanEnter(event):
    global uudestaan
    uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan_hover.png'))
    uudestaan_nappi.config(image=uudestaan)

def lopetaLeave(event):
    global lopeta
    lopeta = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
    lopeta_nappi.config(image=lopeta)

def uudestaanLeave(event):
    global uudestaan
    uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
    uudestaan_nappi.config(image=uudestaan)

#__________________________________RUNKO________________________________________
root = Tk()
root.title("RISTINOLLA")
st = ttk.Style()
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)
root.attributes('-topmost', 1)

#_________________________________KUVAT_________________________________________

lopeta = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
uudestaan = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
kissa = PhotoImage(file=r'cat.png')
hiiri = PhotoImage(file=r'mouse.png')
koskematon = PhotoImage(file=r'not_pressed.png')
hovervari = PhotoImage(file=r'hover.png')
iconi =PhotoImage(r'icon.ico')

#________________________________PELIALUE_______________________________________

vuoro = kissa
kissa_pisteet = []
hiiri_pisteet = []
play_area = tk.Frame(root, width = 300, height = 400)

class XOPoint:
    """Peliruudukko"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.nappi = pelipainike(play_area, kuva1 = koskematon,
        kuva2 = hovervari, kuva3 = kissa, kuva4 = hiiri, borderwidth = 0,
        width = 100, height = 100, command = self.set)
        self.nappi.grid(row = x, column = y, pady = 5, padx = 5)

    def set(self):
        global kissa_pisteet
        global hiiri_pisteet
        global vuoro
        if not self.value:
            self.nappi.configure(image = vuoro)
            self.value = vuoro
            if vuoro == kissa:
                status_label.configure(text="Hiiren vuoro")
                kissa_pisteet.append(self)
                vuoro = hiiri
            elif vuoro == hiiri:
                status_label.configure(text="Kissan vuoro")
                hiiri_pisteet.append(self)
                vuoro = kissa
        voittajan_tarkistus()
for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

#___________________PISTEIDEN LASKU JA VOITTAJA JUTUT___________________________
class Voittotilanne:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def check(self, for_chr):
        p1_toteutuu = False
        p2_toteutuu = False
        p3_toteutuu = False

        if for_chr == kissa:
            for piste in kissa_pisteet:
                if piste.x == self.x1 and piste.y == self.y1:
                    p1_toteutuu = True
                elif piste.x == self.x2 and piste.y == self.y2:
                    p2_toteutuu = True
                elif piste.x == self.x3 and piste.y == self.y3:
                    p3_toteutuu = True
        elif for_chr == hiiri:
            for piste in hiiri_pisteet:
                if piste.x == self.x1 and piste.y == self.y1:
                    p1_toteutuu = True
                elif piste.x == self.x2 and piste.y == self.y2:
                    p2_toteutuu = True
                elif piste.x == self.x3 and piste.y == self.y3:
                    p3_toteutuu = True
        return all([p1_toteutuu, p2_toteutuu, p3_toteutuu])

voittomahdollisuudet = [
    Voittotilanne(1, 1, 1, 2, 1, 3),
    Voittotilanne(2, 1, 2, 2, 2, 3),
    Voittotilanne(3, 1, 3, 2, 3, 3),
    Voittotilanne(1, 1, 2, 1, 3, 1),
    Voittotilanne(1, 2, 2, 2, 3, 2),
    Voittotilanne(1, 3, 2, 3, 3, 3),
    Voittotilanne(1, 1, 2, 2, 3, 3),
    Voittotilanne(3, 1, 2, 2, 1, 3)
]

"""reset() missing 1 required positional argument: 'self' AIKA LOPPU KESKEN"""
# def reset(self):
#     self.config(image=self.kuva1)
#     if self.value == kissa:
#         kissa_pisteet.clear()
#     elif self.value == hiiri:
#         hiiri_pisteet.clear()
#     self.value = None

def voittajan_tarkistus():
    for mahdollisuus in voittomahdollisuudet:
        if mahdollisuus.check(kissa):
            status_label.configure(text="Kissa voitti!")

        elif mahdollisuus.check(hiiri):
            status_label.configure(text="Hiiri voitti!")

    if len(kissa_pisteet) + len(hiiri_pisteet) == 9:
        status_label.configure(text="Tasapeli!")

play_area.pack(pady = 10, padx = 10, side = tk.LEFT)
#________________________________LABELIT________________________________________

status_label = tk.Label(root, text=" ", font=('Verdana', '15', BOLD),
fg='#543f2a')
status_label.place(x=410, y=130)

label_kissa = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15', BOLD),
fg='#543f2a')
label_kissa.place(x=410, y=35)

label_hiiri = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15', BOLD),
fg='#543f2a')
label_hiiri.place(x=410, y=60)

#____________________________UUDESTAAN JA LOPETA________________________________

lopeta_nappi = Button(root, image = lopeta, borderwidth=0, height= 75, width=189,
command=root.destroy)
lopeta_nappi.place(x=400, y=285)
lopeta_nappi.bind('<Enter>', lopetaEnter)
lopeta_nappi.bind('<Leave>', lopetaLeave)

uudestaan_nappi = Button(root, image = uudestaan, borderwidth=0, height= 75, 
width=189, command = uusiksi)
uudestaan_nappi.place(x=400, y=200)
uudestaan_nappi.bind('<Enter>', uudestaanEnter)
uudestaan_nappi.bind('<Leave>', uudestaanLeave)
#___________________________________MUUT________________________________________

status_label.configure(text="Kissan vuoro")
windll.shcore.SetProcessDpiAwareness(1)
root.iconbitmap(iconi)
root.mainloop()