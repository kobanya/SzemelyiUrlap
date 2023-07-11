import tkinter as tk
from tkinter import ttk
import csv

def osszesites():
    nev = nev_bevitel.get()
    nem = nem_valtozo.get()
    szemszin = szemszin_valasztobox.get()
    hajszin = hajszin_valasztobox.get()
    szarmazas = szarmazas_valasztobox.get()
    testmagassag = "Magas" if testmagassag_valtozo.get() else "Alacsony"
    testsuly = "Nehéz" if testsuly_valtozo.get() else "Könnyű"

    osszesito_mezo.config(text=f"Név: {nev}\nNem: {nem}\nSzemszín: {szemszin}\nHajszín: {hajszin}\nSzármazás: {szarmazas}\nTestmagasság: {testmagassag}\nTestsúly: {testsuly}")

def adatok_mentese():
    nev = nev_bevitel.get()
    if nev == "":
        osszesito_mezo.config(text="A név mező nem lehet üres!", fg="red")
        return

    nem = nem_valtozo.get()
    szemszin = szemszin_valasztobox.get()
    hajszin = hajszin_valasztobox.get()
    szarmazas = szarmazas_valasztobox.get()
    testmagassag = "Magas" if testmagassag_valtozo.get() else "Alacsony"
    testsuly = "Nehéz" if testsuly_valtozo.get() else "Könnyű"

    osszesito_mezo.config(text=f"Név: {nev}\nNem: {nem}\nSzemszín: {szemszin}\nHajszín: {hajszin}\nSzármazás: {szarmazas}\nTestmagasság: {testmagassag}\nTestsúly: {testsuly}", fg="black")

    adatok = [nev, nem, szemszin, hajszin, szarmazas, testmagassag, testsuly]
    with open('adatlap.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(adatok)

    nev_bevitel.delete(0, tk.END)  # Mező törlése
    nem_valtozo.set("Férfi")   # Alapértelmezett beállítása
    szemszin_valasztobox.set("")  # Alapértelmezett beállítása
    hajszin_valasztobox.set("")  # Alapértelmezett beállítása
    szarmazas_valasztobox.set("")  # Alapértelmezett beállítása
    testmagassag_valtozo.set(False)  # Alapértelmezett beállítása
    testsuly_valtozo.set(False)  # Alapértelmezett beállítása
    osszesito_mezo.config(text="")  # Alaphelyzetbe állítás
    beolvasas()

def beolvasas():
    tree.delete(*tree.get_children())  # Korábbi adatok törlése

    with open('adatlap.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tree.insert('', 'end', values=row)

ablak = tk.Tk()
ablak.title("Adatbeviteli Űrlap")

# Táblázat keret
tabla_keret = ttk.LabelFrame(ablak, text="Adatok táblázata")
tabla_keret.pack(fill='both', padx=10, pady=10)

# Táblázat
tree = ttk.Treeview(tabla_keret, columns=("Név", "Nem", "Szemszín", "Hajszín", "Származás", "Testmagasság", "Testsúly"))
tree["show"] = "headings"
tree.heading("Név", text="Név")
tree.column("#1", width=350, anchor="w")
tree.heading("Nem", text="Nem")
tree.column("#2", width=80, anchor="w")
tree.heading("Szemszín", text="Szemszín")
tree.heading("Hajszín", text="Hajszín")
tree.heading("Származás", text="Származás")
tree.heading("Testmagasság", text="Testmagasság")
tree.heading("Testsúly", text="Testsúly")
style = ttk.Style()
style.configure("Treeview", rowheight=35)
tree.pack(fill='both', padx=10, pady=10)

# Név
nev_keret = tk.LabelFrame(ablak, text="Vezeték és keresztnév")
nev_keret.pack(fill='x', padx=20, pady=15)
nev_bevitel = tk.Entry(nev_keret)
nev_bevitel.pack(fill='x', padx=15, pady=5)
style.configure("TEntry", font=("Helvetica", 18))  # Betűméret beállítása

# Nem konténer
nem_kontener = tk.Frame(ablak) # konténerbe teszem, hogy egymás mellett jelenjenek meg
nem_kontener.pack(fill='x', padx=20, pady=5)
# Nem
nem_keret = tk.LabelFrame(nem_kontener, text="Neme")
nem_keret.pack(side='left', padx=20, pady=5)
nem_valtozo = tk.StringVar(value="Férfi") # alapértelmezett
nem_radiobutton1 = tk.Radiobutton(nem_keret, text="Férfi", variable=nem_valtozo, value="Férfi")
nem_radiobutton2 = tk.Radiobutton(nem_keret, text="Nő", variable=nem_valtozo, value="Nő")
nem_radiobutton3 = tk.Radiobutton(nem_keret, text="Egyéb", variable=nem_valtozo, value="Egyéb")
nem_radiobutton1.pack(side='left', padx=5, pady=5)
nem_radiobutton2.pack(side='left', padx=5, pady=5)
nem_radiobutton3.pack(side='left', padx=5, pady=5)

# Származás
szarmazas_keret = tk.LabelFrame(nem_kontener, text="Származás")
szarmazas_keret.pack(side='left', padx=20, pady=5)
szarmazas_valasztobox = ttk.Combobox(szarmazas_keret, values=["Európai", "Ázsiai", "Afrikai"])
szarmazas_valasztobox.pack(side='left', padx=5, pady=5)


# Szemszín
szemszin_keret = tk.LabelFrame(nem_kontener, text="Szemszín")
szemszin_keret.pack(side='left', padx=5, pady=5)
szemszin_valasztobox = ttk.Combobox(szemszin_keret, values=["Barna", "Zöld", "Kék", "Szürke"])
szemszin_valasztobox.pack(padx=5, pady=5)

# Hajszín
hajszin_keret = tk.LabelFrame(nem_kontener, text="Hajszín")
hajszin_keret.pack(side='left', padx=5, pady=5)
hajszin_valasztobox = ttk.Combobox(hajszin_keret, values=["Szőke", "Barna", "Fekete"])
hajszin_valasztobox.pack(padx=5, pady=5)

# Testi adottságok
testmagassag_keret = tk.LabelFrame(ablak, text="Testi adottságok")
testmagassag_keret.pack(fill='x', padx=20, pady=5)
testmagassag_valtozo = tk.BooleanVar()
testmagassag_checkbox = ttk.Checkbutton(testmagassag_keret, text="Magasabb mint 160 cm", variable=testmagassag_valtozo)
testsuly_valtozo = tk.BooleanVar()
testsuly_checkbox = ttk.Checkbutton(testmagassag_keret, text="Nehezebb mint 60 kg", variable=testsuly_valtozo)
testsuly_checkbox.pack(side='left', padx=5, pady=5)
testmagassag_checkbox.pack(side='left', padx=5, pady=5)

# Keret
osszesito_keret = tk.LabelFrame(ablak, text="Adatok összesítése")
osszesito_keret.pack(fill='x', padx=10, pady=10)
osszesito_mezo = tk.Label(osszesito_keret, text="", anchor='w', height=8, justify='left')
osszesito_mezo.pack(fill='x', padx=5, pady=5)

# Beolvasás gomb
beolvasas_gomb = tk.Button(ablak, text="Frissít", command=beolvasas)
beolvasas_gomb.pack(side="right", padx=20, pady=5)

# Összesítés gomb
osszesites_gomb = tk.Button(ablak, text="Összesítés", command=osszesites)
osszesites_gomb.pack(side="left", padx=20, pady=5)

# Mentés gomb
mentes_gomb = tk.Button(ablak, text="Mentés", command=adatok_mentese)
mentes_gomb.pack(side="right", padx=20, pady=5)

beolvasas()
ablak.mainloop()
