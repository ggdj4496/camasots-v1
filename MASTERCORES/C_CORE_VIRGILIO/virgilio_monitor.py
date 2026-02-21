import tkinter as tk
import os
root = tk.Tk()
root.title("VIRGILIO CORE - VIGILANCIA")
root.attributes('-topmost', True)
tk.Label(root, text="VIRGILIO ACTIVO", fg="green", bg="black", font=('Courier', 20)).pack()
tk.Label(root, text="Sincronizando con Aria_v1...", fg="white", bg="black").pack()
print("VIRGILIO: Manifestado en pantalla.")
root.mainloop()
