import tkinter as tk
from utilisateurs import connexion

fenetre = tk.Tk()
fenetre.title("Edumada - Connexion")
fenetre.geometry("300x200")


label_nom = tk.Label(fenetre, text="Nom de l'utilisateur :")
label_nom.pack()

champ_nom = tk.Entry(fenetre)
champ_nom.pack()

label_mdp = tk.Label(fenetre, text="Mot de passe :")
label_mdp.pack()

champ_mdp = tk.Entry(fenetre, show="*")
champ_mdp.pack()

label_message = tk.Label(fenetre, text="")
label_message.pack()

def ouvrir_menu_principal(role):
    menu = tk.Tk()
    menu.title("EduMada - Menu Principal")
    menu.geometry("400x300")

    label_bienvenue = tk.Label(menu, text=f"Bienvenue ! Votre rôle : {role}")
    label_bienvenue.pack()

    menu.mainloop()

def verifier_connexion():
    nom = champ_nom.get()
    mdp = champ_mdp.get()
    role = connexion(nom, mdp)

    if role is None:
        label_message.config(text="Connexion échouée")
    else:
        fenetre.destroy()
        ouvrir_menu_principal(role)

bouton_connexion = tk.Button(fenetre, text="Se connecter", command=verifier_connexion)
bouton_connexion.pack()

fenetre.mainloop()