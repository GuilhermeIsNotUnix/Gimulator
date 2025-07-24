import ttkbootstrap as tb
from gimulator import SimuladorQuedaLivre

root = tb.Window(themename="cyborg")
simulador = SimuladorQuedaLivre(root)
root.mainloop()