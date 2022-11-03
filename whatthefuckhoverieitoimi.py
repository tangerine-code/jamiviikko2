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

class pelipainike(Button):
    """Pelialueen ruudukon nappien hover."""
    def __init__(self, root, kuva1, kuva2, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.kuva1 = ImageTk.PhotoImage(Image.open(kuva1))
        self.kuva2 = ImageTk.PhotoImage(Image.open(kuva2))

        self['image'] = self.kuva1
        
        #self.bind('<Enter>', self.onEnter1)
        self.bind('<Leave>', self.onLeave1)        

    #def onEnter1(self, event):
    #    if self.image(self.kuva1):
    #        self.config(image=self.kuva2)
    #    else:
    #        pass

    def onLeave1(self, event):
        if len(kissa_pisteet) <= 0 and len(hiiri_pisteet) <= 0:
            self.config(image=self.kuva1)
        else:
            pass

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
koskematon = r"not_pressed.png"
hovervari = r"hover.png"
iconi =PhotoImage(r'icon.ico')

#________________________________PELIALUE_______________________________________

vuoro = kissa
kissa_pisteet = []
hiiri_pisteet = []
play_area = tk.Frame(root, width = 300, height = 400)  
#XO_points = []

class XOPoint:
    """Peliruudukko."""
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
        self.value = None  
        self.nappi = pelipainike(play_area, kuva1 = koskematon, kuva2 = hovervari, borderwidth = 0, width = 100, height = 100, command = self.set)
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
        check_win()

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

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
def check_win():
    for mahdollisuus in voittomahdollisuudet:
        if mahdollisuus.check(kissa):
            status_label.configure(text="Kissa voitti!")
            return
        elif mahdollisuus.check(hiiri):
            status_label.configure(text="Hiiri voitti!")
            return
    if len(kissa_pisteet) + len(hiiri_pisteet) == 9:
        status_label.configure(text="Tasapeli!")
        #disable_game() tähän sit ku fiksataan tällanen
        
play_area.pack(pady = 10, padx = 10, side = tk.LEFT)
#______________________________STATUS LABEL_____________________________________

status_label = tk.Label(root, text=" ", font=('Verdana', '15', BOLD), 
fg='#543f2a')
status_label.place(x=410, y=130)

#______________________________PELAAJIEN NIMET__________________________________

lbl = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15', BOLD), 
fg='#543f2a')
lbl.place(x=410, y=35)

lbl2 = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15', BOLD), 
fg='#543f2a')
lbl2.place(x=410, y=60)

#____________________________UUDESTAAN JA LOPETA________________________________

lopeta_nappi = Button(root, image = lopeta, borderwidth=0, height= 75, width=189, command=root.destroy)
lopeta_nappi.place(x=400, y=285)
lopeta_nappi.bind('<Enter>', onEnter)
lopeta_nappi.bind('<Leave>', onLeave)

uudestaan_nappi = Button(root, image = uudestaan, borderwidth=0, height= 75, width=189, command = uusiksi)
uudestaan_nappi.place(x=400, y=200)
uudestaan_nappi.bind('<Enter>', onEnter2)
uudestaan_nappi.bind('<Leave>', onLeave2)
#___________________________________MUUT________________________________________

status_label.configure(text="Kissan vuoro")
windll.shcore.SetProcessDpiAwareness(1)
root.iconbitmap(iconi)
root.mainloop()