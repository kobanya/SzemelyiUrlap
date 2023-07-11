import tkinter as tk
from tkcalendar import DateEntry

ablak = tk.Tk()
ablak.title("Dátum mező példa")

datum_mezo = DateEntry(ablak, width=12, background='darkblue', foreground='white', borderwidth=2)
datum_mezo.pack(padx=10, pady=10)

ablak.mainloop()
