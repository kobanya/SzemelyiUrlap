import tkinter
import tkinter as tk
from tkinter import ttk
import csv

def osszesites():
    nev = nev_bevitel.get()
    nem = nem_valtozo.get()
    szemszin = szemszin_valasztobox.get()
    testmagassag = "Magas" if testmagassag_valtozo.get() else "Alacsony"
    testsuly = "Nehéz" if testsuly_valtozo.get() else "Könnyű"

    osszesito_mezo["text"] = f"Név: {nev}\nNem: {nem}\nSzemszín: {szemszin}\nTestmagasság: {testmagassag}\nTestsúly: {testsuly}"

def adatok_mentese():
    nev = nev_bevitel.get()
    nem = nem_valtozo.get()
    szemszin = szemszin_valasztobox.get()
    testmagassag = "Magas" if testmagassag_valtozo.get() else "Alacsony"
    testsuly = "Nehéz" if testsuly_valtozo.get() else "Könnyű"

    osszesito_mezo["text"] = f"Név: {nev}\nNem: {nem}\nSzemszín: {szemszin}\nTestmagasság: {testmagassag}\nTestsúly: {testsuly}"

    adatok = [nev, nem, szemszin, testmagassag, testsuly]
    with open('adatlap.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(adatok)

        nev_bevitel.delete(0, tk.END)  # Mező törlése
        nem_valtozo.set("Férfi")   # Alapértelmezett beállítása
        szemszin_valasztobox.set("")  # Alapértelmezett beállítása
        testmagassag_valtozo.set(False)  # Alapértelmezett beállítása
        testsuly_valtozo.set(False)  # Alapértelmezett beállítása
        osszesito_mezo["text"] = ""  # Alaphelyzetbe állítás


ablak = tkinter.Tk()
ablak.title("Adatbeviteli Űrlap")

# Név
nev_keret = tkinter.LabelFrame(ablak, text="Név")
nev_keret.pack(fill='x', padx=20, pady=5)
nev_bevitel = tkinter.Entry(nev_keret)
nev_bevitel.pack(fill='x', padx=15, pady=5)

# Nem
nem_keret = tkinter.LabelFrame(ablak, text="Neme")
nem_keret.pack(fill='x', padx=20, pady=5)
nem_valtozo = tkinter.StringVar(value="Férfi") # alapértelmezett
nem_radiobutton1 = tkinter.Radiobutton(nem_keret, text="Férfi", variable=nem_valtozo, value="Férfi")
nem_radiobutton2 = tkinter.Radiobutton(nem_keret, text="Nő", variable=nem_valtozo, value="Nő")
nem_radiobutton1.pack(side='left', padx=5, pady=5)
nem_radiobutton2.pack(side='left', padx=5, pady=5)

# Szemszín
szemszin_keret = tkinter.LabelFrame(ablak, text="Szemszín")
szemszin_keret.pack(fill='x', padx=20, pady=5)
szemszin_valasztobox = ttk.Combobox(szemszin_keret, values=["Barna", "Zöld", "Kék", "Szürke"])
szemszin_valasztobox.pack(fill='x', padx=5, pady=5)

# Testmagasság
testmagassag_keret = tkinter.LabelFrame(ablak, text="Testmagasság")
testmagassag_keret.pack(fill='x', padx=20, pady=5)
testmagassag_valtozo = tkinter.BooleanVar()
testmagassag_checkbox = tkinter.Checkbutton(testmagassag_keret, text="Magasabb mint 160 cm", variable=testmagassag_valtozo)
testmagassag_checkbox.pack(side='left', padx=5, pady=5)

# Testsúly
testsuly_keret = tkinter.LabelFrame(ablak, text="Testsúly")
testsuly_keret.pack(fill='x', padx=20, pady=5)
testsuly_valtozo = tkinter.BooleanVar()
testsuly_checkbox = tkinter.Checkbutton(testsuly_keret, text="Nehezebb mint 60 kg", variable=testsuly_valtozo)
testsuly_checkbox.pack(side='left', padx=5, pady=5)

#keret
osszesito_keret = tkinter.LabelFrame(ablak, text="Adatok összesítése")
osszesito_keret.pack(fill='x', padx=10, pady=10)
osszesito_mezo = tkinter.Label(osszesito_keret, text="", anchor='w', height=8, justify='left')
osszesito_mezo.pack(fill='x', padx=5, pady=5)

# Összesítés gomb
osszesites_gomb = tk.Button(ablak, text="Összesítés", command=osszesites)
osszesites_gomb.pack(side="left", padx=20, pady=5)



# Mentés gomb
mentes_gomb = tkinter.Button(ablak, text="Adatok mentése", command=adatok_mentese)
mentes_gomb.pack(fill='x', padx=20, pady=5)

ablak.mainloop()
