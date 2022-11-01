from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter import ttk
from tkinter import Button
from ctypes import windll
from tkinter.messagebox import showinfo
import sys
import os

#_______________________________________________________________________________
#Tähän väliin funktiot

def uusiksi():
    """Käynnistää ikkunan uudestaan. Tää funktio ei palauta mitään,
    eli jos haluaa laskea voitot ja häviöt niin täytyy ottaa talteen kaikki
     tiedot ennen tämän funktion kutsumista kutsumista!"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

#_______________________________________________________________________________
#Runko
root = Tk()
root.title("Ristinolla")
st = ttk.Style()
root.attributes('-topmost', 1)
#Keskitetään runko ikkuna jonka koko on 600x400px, eikä kokoa saa muutettua
window_width = 600
window_height =400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)
root.title("Ristinolla")
#root.configure(bg='#ebd7d7') taustaväri ehdotus, MUTTA jos käyttää niin 
# tarvitsee määritellä BG myös nappeihin ja labeleihin kaikkiin :(

#_______________________________________________________________________________
#Tähän väliin kaikki kuvat mitä tarvitaan

uudestaan = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\uudestaan1.png")
lopeta = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\lopeta1.png")
kissa = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\cat.png")
hiiri = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\mouse.png")
koskematon = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\not_pressed.png")
hoveri = PhotoImage(file=r"C:\Users\roksa\Desktop\JAMIsysky\hover.png")
iconi =PhotoImage(r'C:\Users\roksa\Desktop\JAMIsysky\icon.ico')

#_______________________________________________________________________________
#Pelaaja tekstit, saisko vaikka värin muuttumaan kun on oma vuoro?

lbl = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15'))
lbl.place(x=410, y=5)

lbl2 = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15'))
lbl2.place(x=410, y=40)

#_______________________________________________________________________________
#Oikean alakulman nappulat "Uudestaan" ja "Lopeta"

uudestaan_nappi = Button(image = uudestaan, borderwidth=0, height= 75, width=189,
command = uusiksi)
uudestaan_nappi.place(x=400, y=300)

lopeta_nappi = Button(root, image = lopeta, borderwidth=0, height= 75, width=189,
command=root.destroy)
lopeta_nappi.place(x=400, y=200)

#_______________________________________________________________________________
#Lopetus hommat ja ikkunan terävyyden säätö
windll.shcore.SetProcessDpiAwareness(1)
root.iconbitmap(iconi)
root.mainloop()