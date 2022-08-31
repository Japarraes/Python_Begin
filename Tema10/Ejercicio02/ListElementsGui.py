import tkinter
from tkinter import ttk


window = tkinter.Tk()

# Grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Labels - Configure su vehículo
lbConfig = ttk.Label(window, text="DISPOSITIVOS DISPONIBLES:", background="green")
lbConfig.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

device =["Portátil", "PC", "Ipad", "Tablet", "Movil", "SmartWatch"]
deviceList = tkinter.StringVar(value=device)
listbox = tkinter.Listbox(window, height=10, listvariable=deviceList)
listbox.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()