import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import threading
import queue
import sys
import os
import pkg_resources

couleur_fond_hex = "#4a4a4a"

titre = "Lumia Bot Launcher v1.0"

chemin_bot = "main.py"

process = None

lock_file = "main.lock"  # Nom du fichier de verrou

def is_already_running():
    return os.path.exists(lock_file)

def create_lock_file():
    with open(lock_file, 'w') as lock:
        lock.write("1")

def remove_lock_file():
    if os.path.exists(lock_file):
        os.remove(lock_file)

def executer_bot():
    global chemin_bot, process
    if is_already_running():
        console.insert(tk.END, "L'application est déjà en cours d'exécution.\n")
        return
    
    create_lock_file()
    try:
        process = subprocess.Popen(
            ['python', chemin_bot],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        def lire_sortie():
            while True:
                ligne = process.stdout.readline()
                if not ligne:
                    break
                console.insert(tk.END, ligne)
                console.see(tk.END)

        t = threading.Thread(target=lire_sortie)
        t.daemon = True
        t.start()

        arreter_bouton.config(state=tk.NORMAL)
    except Exception as e:
        console.insert(tk.END, f"Erreur lors de l'exécution : {str(e)}\n")

def arreter_execution():
    global process
    try:
        if process is not None:
            process.terminate()
            process.wait()
        remove_lock_file()
        fenetre.destroy()
    except Exception as e:
        console.insert(tk.END, f"Erreur lors de l'arrêt : {str(e)}\n")

def executer_modules():
    try:
        os.system("module.cmd")
        console.insert(tk.END, "Installation des modules terminée, cliquez sur 'Exécuter'")
    except Exception as e:
        console.insert(tk.END, f"Erreur lors de l'exécution des modules : {str(e)}\n")

def redemarrer_programme():
    global process
    try:
        if process is not None:
            process.terminate()
            process.wait()
        process = subprocess.Popen(
            ['python', chemin_bot],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        def lire_sortie_nouveau():
            while True:
                ligne = process.stdout.readline()
                if not ligne:
                    break
                console.insert(tk.END, ligne)
                console.see(tk.END)

        t = threading.Thread(target=lire_sortie_nouveau)
        t.daemon = True
        t.start()

        arreter_bouton.config(state=tk.NORMAL)
        redemarrer_bouton.config(state=tk.NORMAL)
    except Exception as e:
        console.insert(tk.END, f"Erreur lors du redémarrage : {str(e)}\n")


fenetre = tk.Tk()
fenetre.title(titre)
fenetre.iconbitmap("lumia_bot.ico")
fenetre.configure(bg=couleur_fond_hex)

style = ttk.Style()
style.configure("Cadre.TFrame", background=couleur_fond_hex)

cadre_titre = ttk.Frame(fenetre, style="Cadre.TFrame")
cadre_titre.pack(pady=10)
cadre_titre.columnconfigure(0, weight=1)

titre_label = ttk.Label(cadre_titre, text=titre, font=("Helvetica", 16, "bold"), foreground="#FFFFFF", background=couleur_fond_hex)
titre_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

sous_titre_label = ttk.Label(cadre_titre, text="© 2023 - Le Homebrew France", font=("Helvetica", 12), foreground="#FFFFFF", background=couleur_fond_hex)
sous_titre_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

cadre_image = ttk.Frame(fenetre)
cadre_image.pack(side=tk.RIGHT, padx=0)

image = tk.PhotoImage(file="lumia_bot.png")
image = image.subsample(4)
image_label = ttk.Label(cadre_image, image=image, background=couleur_fond_hex)
image_label.pack()

boutons_cadre = ttk.Frame(fenetre, style="Cadre.TFrame")
boutons_cadre.pack(pady=20, padx=10, side=tk.LEFT)

executer_bouton = ttk.Button(boutons_cadre, text="Exécuter", command=executer_bot)
executer_bouton.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

modules_bouton = ttk.Button(boutons_cadre, text="Modules", command=executer_modules)
modules_bouton.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

arreter_bouton = ttk.Button(boutons_cadre, text="Arrêter", command=arreter_execution, state=tk.DISABLED)
arreter_bouton.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

redemarrer_bouton = ttk.Button(boutons_cadre, text="Redémarrer", command=redemarrer_programme, state=tk.NORMAL)
redemarrer_bouton.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

console_frame = ttk.Frame(fenetre)
console_frame.pack(pady=20, padx=10, side=tk.RIGHT, fill=tk.BOTH, expand=True)

console = tk.Text(console_frame, wrap=tk.WORD, height=20, width=80)
console.pack(fill=tk.BOTH, expand=True)

console_scrollbar = ttk.Scrollbar(console_frame, orient=tk.VERTICAL, command=console.yview)
console.config(yscrollcommand=console_scrollbar.set)
console_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

fenetre.mainloop()