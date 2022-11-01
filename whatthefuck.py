from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter import ttk
from tkinter import Button
from ctypes import windll
from tkinter.messagebox import showinfo
#_______________________________________________________________________________
#Tähän väliin funktiot

def klikattu():
    viesti = f"höpönlöpönlöötä tää on vaan esimerkki"
    showinfo(
        title="tiedot",
        message=viesti
    )

#_______________________________________________________________________________
#Runko
root = Tk()
root.title("Ristinolla")
st = ttk.Style()
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
#Taustaväri viä valkoiseksi??

#_______________________________________________________________________________
#Tähän väliin kaikki kuvat mitä tarvitaan

uudestaan = PhotoImage(file=r"uudestaan1.png")
lopeta = PhotoImage(file=r"lopeta1.png")
# cat.png, mouse.png, hover.png, not_pressed.png, lopeta_hover.png, uudestaan_hover.png

#_______________________________________________________________________________
#Pelaaja tekstit, saisko vaikka värin muuttumaan kun on oma vuoro?

lbl = Label(root, text="Pelaaja 1: Kissa", font=('Verdana', '15'))
lbl.place(x=410, y=5)

lbl2 = Label(root, text="Pelaaja 2: Hiiri", font=('Verdana', '15'))
lbl2.place(x=410, y=40)

#_______________________________________________________________________________
#Oikean alakulman nappulat "Uudestaan" ja "Lopeta"

"""Tälle napille toiminto joka refressaa ikkunan"""
uudestaan_nappi = Button(image = uudestaan, borderwidth=0, height= 75, width=189,
command = klikattu)
uudestaan_nappi.place(x=400, y=300)

"""Lopeta ei tarvitse funktioo kun destroy command riittää"""
lopeta_nappi = Button(root, image = lopeta, borderwidth=0, height= 75, width=189,
command=root.destroy)
lopeta_nappi.place(x=400, y=200)

#_______________________________________________________________________________
#Lopetus hommat ja ikkunan terävyyden säätö
windll.shcore.SetProcessDpiAwareness(1)

root.mainloop()