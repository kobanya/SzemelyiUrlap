import tkinter
from tkinter import ttk

def adatok_mentese():
    nev = nev_bevitel.get()
    nem = nem_valtozo.get()
    szemszin = szemszin_valasztobox.get()

    osszesito_mezo["text"] = f"Név: {nev}\nNem: {nem}\nSzemszín: {szemszin}"

ablak = tkinter.Tk()
ablak.title("Adatbeviteli Űrlap")

# Név
nev_keret = tkinter.LabelFrame(ablak, text="Név")
nev_keret.pack(fill='x', padx=20, pady=5)
nev_bevitel = tkinter.Entry(nev_keret)
nev_bevitel.pack(fill='x', padx=5, pady=5)

# Nem
nem_keret = tkinter.LabelFrame(ablak, text="Neme")
nem_keret.pack(fill='x', padx=20, pady=5)
nem_valtozo = tkinter.StringVar(value="Nő")
nem_radiobutton1 = tkinter.Radiobutton(nem_keret, text="Férfi", variable=nem_valtozo, value="Férfi")
nem_radiobutton2 = tkinter.Radiobutton(nem_keret, text="Nő", variable=nem_valtozo, value="Nő")
nem_radiobutton1.pack(side='left', padx=5, pady=5)
nem_radiobutton2.pack(side='left', padx=5, pady=5)

# Szemszín
szemszin_keret = tkinter.LabelFrame(ablak, text="Szemszín")
szemszin_keret.pack(fill='x', padx=20, pady=5)
szemszin_valasztobox = ttk.Combobox(szemszin_keret, values=["Barna", "Zöld", "Kék", "Szürke"])
szemszin_valasztobox.pack(fill='x', padx=5, pady=5)
#keret
osszesito_keret = tkinter.LabelFrame(ablak, text="Adatok összesítése")
osszesito_keret.pack()
osszesito_mezo = tkinter.Label(osszesito_keret, text="", anchor='w', height=8, justify='left')
osszesito_mezo.pack(fill='x', padx=5, pady=5)


# Mentés gomb
mentes_gomb = tkinter.Button(ablak, text="Adatok mentése", command=adatok_mentese)
mentes_gomb.pack(fill='x', padx=20, pady=5)

ablak.mainloop()
