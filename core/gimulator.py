import time
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class SimuladorQuedaLivre:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Queda Livre")

        # Entradas
        tb.Label(master, text="Altura (m):").grid(row=0, column=0)
        self.altura_entry = tb.Entry(master)
        self.altura_entry.grid(row=0, column=1)
        self.altura_entry.insert(0, "1.50")

        tb.Label(master, text="Tempo médio (s):").grid(row=1, column=0)
        self.tempo_entry = tb.Entry(master)
        self.tempo_entry.grid(row=1, column=1)
        self.tempo_entry.insert(0, "0.5506")

        self.resultado_label = tb.Label(master, text="", font=("Helvetica", 10, "bold"))
        self.resultado_label.grid(row=2, columnspan=2, pady=10)

        # Botão
        self.simular_btn = tb.Button(master, text="Simular", command=self.simular)
        self.simular_btn.grid(row=3, columnspan=2)

        # Canvas de animação
        self.canvas = tb.Canvas(master, width=200, height=400, bg="white")
        self.canvas.grid(row=4, columnspan=2, pady=10)
        self.bola = None

    def calcular_g(self, h, t):
        return (2 * h) / (t ** 2)

    def simular(self):
        h = float(self.altura_entry.get())
        t = float(self.tempo_entry.get())
        g = self.calcular_g(h, t)
        self.resultado_label.config(text=f"g estimado: {g:.4f} m/s²")

        # Configurações de simulação
        altura_canvas = 350  # pixel do chão no canvas
        raio = 10
        y0_pixel = 50  # topo da queda no canvas
        escala = (altura_canvas - y0_pixel) / h  # m → pixels

        if self.bola:
            self.canvas.delete(self.bola)

        self.bola = self.canvas.create_oval(90, y0_pixel, 110, y0_pixel + 20, fill="springgreen")

        # Simulação animada
        dt = 0.01
        v = 0.0
        y = h
        t_sim = 0.0

        def passo():
            nonlocal y, v, t_sim
            if y <= 0:
                return

            v += g * dt
            y -= v * dt
            if y < 0:
                y = 0

            y_pixel = altura_canvas - y * escala
            self.canvas.coords(self.bola, 90, y_pixel, 110, y_pixel + 20)

            t_sim += dt
            self.master.after(10, passo)

        passo()
