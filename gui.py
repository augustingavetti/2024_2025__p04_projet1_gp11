import tkinter as tk
from tkinter import ttk, messagebox
from tools import dec_to_bin, dec_to_hex, bin_to_dec, bin_to_hex, hex_to_dec, hex_to_bin

class ConvertisseurGUI:
    def __init__(self, master):
        self.master = master
        master.title("Convertisseur de Base")
        master.geometry("400x300")

        # Nombre à convertir
        tk.Label(master, text="Nombre à convertir:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        # Base initiale
        tk.Label(master, text="Base initiale:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.base_initiale = ttk.Combobox(master, values=["2", "10", "16"])
        self.base_initiale.grid(row=1, column=1, padx=10, pady=10)
        self.base_initiale.set("10")

        # Base cible
        tk.Label(master, text="Base cible:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.base_cible = ttk.Combobox(master, values=["2", "10", "16"])
        self.base_cible.grid(row=2, column=1, padx=10, pady=10)
        self.base_cible.set("2")

        # Bouton de conversion
        self.convert_button = tk.Button(master, text="Convertir", command=self.convertir)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Résultat
        tk.Label(master, text="Résultat:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.resultat_label = tk.Label(master, text="")
        self.resultat_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def convertir(self):
        try:
            nombre = self.nombre_entry.get()
            base_init = int(self.base_initiale.get())
            base_cible = int(self.base_cible.get())

            if base_init == base_cible:
                resultat = nombre
            elif base_init == 10 and base_cible == 2:
                resultat = dec_to_bin(int(nombre))
            elif base_init == 10 and base_cible == 16:
                resultat = dec_to_hex(int(nombre))
            elif base_init == 2 and base_cible == 10:
                resultat = bin_to_dec(nombre)
            elif base_init == 2 and base_cible == 16:
                resultat = bin_to_hex(nombre)
            elif base_init == 16 and base_cible == 10:
                resultat = hex_to_dec(nombre)
            elif base_init == 16 and base_cible == 2:
                resultat = hex_to_bin(nombre)
            else:
                raise ValueError("Conversion non supportée")

            self.resultat_label.config(text=resultat)
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

def main():
    root = tk.Tk()
    app = ConvertisseurGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()