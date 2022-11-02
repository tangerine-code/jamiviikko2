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

#_______________________________________________________________________________
#Tähän väliin funktiot

def uusiksi():
    """Käynnistää ikkunan uudestaan. Tää funktio ei palauta mitään,
    eli jos haluaa laskea voitot ja häviöt niin täytyy ottaa talteen kaikki
     tiedot ennen tämän funktion kutsumista kutsumista!"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def onEnter(event):
    global img
    img = ImageTk.PhotoImage(Image.open(r'lopeta_hover.png'))
    lopeta_nappi.config(image=img)

def onEnter2(event):
    global img2
    img2 = ImageTk.PhotoImage(Image.open(r'uudestaan_hover.png'))
    uudestaan_nappi.config(image=img2)    

def onLeave(event):
    global img
    img = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
    lopeta_nappi.config(image=img)
def onLeave2(event):
    global img2
    img2 = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
    uudestaan_nappi.config(image=img2)

#_______________________________________________________________________________
#Runko
root = Tk()
root.title("Ristinolla")
st = ttk.Style()
#Keskitetään runko ikkuna jonka koko on 600x400px, eikä kokoa saa muutettua
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

#_______________________________________________________________________________
#Tähän väliin kaikki kuvat mitä tarvitaan

img = ImageTk.PhotoImage(Image.open(r'lopeta1.png'))
img2 = ImageTk.PhotoImage(Image.open(r'uudestaan1.png'))
kissa = PhotoImage(file=r"cat.png")
hiiri = PhotoImage(file=r"mouse.png")
koskematon = ImageTk.PhotoImage(Image.open(r"not_pressed.png"))
img3 = PhotoImage(file=r"hover.png")
iconi =PhotoImage(r'icon.ico')

# Pelialue

play_area = tk.Frame(root, width = 300, height = 400)  
XO_points = []  
class XOPoint:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
        self.value = None  
        nappi = Button(play_area, image = koskematon, borderwidth = 0, width = 100, height = 100)
        nappi.bind('<Enter>', onEnter)
        nappi.bind('<Leave>', onLeave)
        nappi.grid(row = x, column = y, pady = 5, padx = 5)
  
    def reset(self):  
        self.button.configure(text = "", bg = 'white')  
        self.value = None

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

play_area.pack(pady = 10, padx = 10, side = tk.LEFT)

#_______________________________________________________________________________
#Pelaaja tekstit, saisko vaikka värin muuttumaan kun on oma vuoro?

lbl = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15'))
lbl.place(x=410, y=35)

lbl2 = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15'))
lbl2.place(x=410, y=60)

#_______________________________________________________________________________
#Oikean alakulman nappulat "Uudestaan" ja "Lopeta"

lopeta_nappi = Button(root, image = img, borderwidth=0, height= 75, width=189,
command=root.destroy)
lopeta_nappi.place(x=400, y=285)
lopeta_nappi.bind('<Enter>',  onEnter)
lopeta_nappi.bind('<Leave>',  onLeave)

uudestaan_nappi = Button(root, image = img2, borderwidth=0, height= 75, width=189,
command = uusiksi)
uudestaan_nappi.place(x=400, y=200)
uudestaan_nappi.bind('<Enter>',  onEnter2)
uudestaan_nappi.bind('<Leave>',  onLeave2)

#_______________________________________________________________________________
#Lopetus hommat ja ikkunan terävyyden säätö
windll.shcore.SetProcessDpiAwareness(1)

root.mainloop()
