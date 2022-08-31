import tkinter
from tkinter import ttk


window = tkinter.Tk()

## Función Limpiado de opciones de pantalla
def limpiarOpciones():
    miSelMotor.set(0)
    miSelCaja.set(0)


# Grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Labels - Configure su vehículo
lbConfig = ttk.Label(window, text="CONFIGURE SU VEHÍCULO:", background="green")
lbConfig.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# Labels - Configuración Motor
lbCambio = ttk.Label(window, text="Motor:", background="red", )
lbCambio.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# RadioButtons Motor
miSelMotor = tkinter.StringVar()
rb1 = ttk.Radiobutton(window, text="Gasolina", value="1", variable=miSelMotor)
rb2 = ttk.Radiobutton(window, text="Diesel", value="2", variable=miSelMotor)
rb3 = ttk.Radiobutton(window, text="Eléctrico", value="3", variable=miSelMotor)

rb1.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
rb2.grid(column=0, row=3, sticky=tkinter.W, padx=5, pady=5)
rb3.grid(column=0, row=4, sticky=tkinter.W, padx=5, pady=5)

# Labels - Configuración Caja de cambio
lbCambio = ttk.Label(window, text="Caja de Cambio:", background="red", )
lbCambio.grid(column=1, row=1, sticky=tkinter.W, padx=5, pady=5)

# RadioButtons Caja de cambio
miSelCaja = tkinter.StringVar()
rb4 = ttk.Radiobutton(window, text="Manual", value="1", variable=miSelCaja)
rb5 = ttk.Radiobutton(window, text="Automática", value="2", variable=miSelCaja)

rb4.grid(column=1, row=2, sticky=tkinter.W, padx=5, pady=5)
rb5.grid(column=1, row=3, sticky=tkinter.W, padx=5, pady=5)

# Botón Clear
btClear = ttk.Button(window, text="Clear", command=limpiarOpciones)
btClear.grid(column=2, row=4, sticky=tkinter.E)

window.mainloop()