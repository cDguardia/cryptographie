# main.py

# Interface utilisateur graphique (Tkinter) pour chiffrer/déchiffrer un fichier avec RSA

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from chiffreur_dechiffreur import chiffrer_fichier, dechiffrer_fichier

class ApplicationRSA:
    def __init__(self, master):
        self.master = master
        master.title("RSA Chiffreur/Déchiffreur")
        master.geometry("600x450")

        # Mot de passe
        self.label_mdp = tk.Label(master, text="Mot de passe :")
        self.label_mdp.pack()
        self.entree_mdp = tk.Entry(master, show="*")
        self.entree_mdp.pack(fill=tk.X, padx=20)

        # Sélection de fichier
        self.bouton_fichier = tk.Button(master, text="Sélectionner un fichier", command=self.choisir_fichier)
        self.bouton_fichier.pack(pady=10)
        self.label_fichier = tk.Label(master, text="Aucun fichier sélectionné")
        self.label_fichier.pack()

        # Barre de progression
        self.progression = ttk.Progressbar(master, orient="horizontal", length=400, mode="determinate")
        self.progression.pack(pady=10)

        # Boutons d'action
        self.bouton_chiffrer = tk.Button(master, text="Chiffrer le fichier", command=self.chiffrer)
        self.bouton_chiffrer.pack(pady=5)
        self.bouton_dechiffrer = tk.Button(master, text="Déchiffrer le fichier", command=self.dechiffrer)
        self.bouton_dechiffrer.pack(pady=5)

        # Zone de sortie
        self.texte_resultat = tk.Text(master, height=10)
        self.texte_resultat.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Attributs internes
        self.chemin_fichier = None

    def choisir_fichier(self):
        chemin = filedialog.askopenfilename()
        if chemin:
            self.chemin_fichier = chemin
            self.label_fichier.config(text=os.path.basename(chemin))

    def chiffrer(self):
        mdp = self.entree_mdp.get()
        if not mdp or not self.chemin_fichier:
            messagebox.showerror("Erreur", "Mot de passe ou fichier manquant.")
            return
        try:
            self.progression.start()
            self.master.update()
            chemin_sortie = chiffrer_fichier(self.chemin_fichier, mdp)
            self.progression.stop()
            self.progression['value'] = 100
            self.texte_resultat.insert(tk.END, f"Fichier chiffré : {chemin_sortie}\n")
        except Exception as e:
            self.progression.stop()
            self.texte_resultat.insert(tk.END, f"Erreur : {str(e)}\n")

    def dechiffrer(self):
        mdp = self.entree_mdp.get()
        if not mdp or not self.chemin_fichier:
            messagebox.showerror("Erreur", "Mot de passe ou fichier manquant.")
            return
        try:
            self.progression.start()
            self.master.update()
            chemin_sortie = dechiffrer_fichier(self.chemin_fichier, mdp)
            self.progression.stop()
            self.progression['value'] = 100
            self.texte_resultat.insert(tk.END, f"Fichier déchiffré : {chemin_sortie}\n")
        except Exception as e:
            self.progression.stop()
            self.texte_resultat.insert(tk.END, f"Erreur : {str(e)}\n")

if __name__ == "__main__":
    os.makedirs("cles", exist_ok=True)
    os.makedirs("fichiers", exist_ok=True)

    root = tk.Tk()
    app = ApplicationRSA(root)
    root.mainloop()
