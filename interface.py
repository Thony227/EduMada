import tkinter as tk
from database import connexion, curseur
from utilisateurs import connexion_login
from classes import ajouter_classe
from eleves import ajouter_eleve, lister_eleve, modifier_eleve, supprimer_eleve

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

    if role == "directeur":
        bouton_classe = tk.Button(menu, text="Ajouter Une classe", command=ouvrir_fenetre_ajouter_classe)
        bouton_classe.pack()

    if role == "secretariat":
        bouton_eleve = tk.Button(menu, text="Ajouter un élève", command=ouvrir_fenetre_ajouter_eleve)
        bouton_eleve.pack()

        bouton_modifier = tk.Button(menu, text="Modifier un élève", command=ouvvrir_fenetre_modifier_eleve)
        bouton_modifier.pack()

        bouton_supprimer = tk.Button(menu, text="Supprimer un élève", command=ouvrir_fenetre_supprimer_eleve)
        bouton_supprimer.pack()

    bouton_liste = tk.Button(menu, text="Lister les élèves", command=ouvrir_fenetre_lister_eleves)
    bouton_liste.pack()

    menu.mainloop()

def ouvrir_fenetre_ajouter_classe():
    fenetre_classe = tk.Toplevel()
    fenetre_classe.title("Ajouter une classe")
    fenetre_classe.geometry("300x200")

    label_nom = tk.Label(fenetre_classe, text="Nom de la classe :")
    label_nom.pack()
    champ_nom_classe = tk.Entry(fenetre_classe)
    champ_nom_classe.pack()

    label_niveau = tk.Label(fenetre_classe, text="Niveau :")
    label_niveau.pack()
    champ_niveau = tk.Entry(fenetre_classe)
    champ_niveau.pack()

    def valider():
        nom_classe = champ_nom_classe.get()
        niveau = champ_niveau.get()
        ajouter_classe(nom_classe, niveau)
        fenetre_classe.destroy()

    bouton_valider = tk.Button(fenetre_classe, text="Valider", command=valider)
    bouton_valider.pack()

def ouvrir_fenetre_ajouter_eleve():
    fenetre_eleve = tk.Toplevel()
    fenetre_eleve.title("Ajouter un élève")
    fenetre_eleve.geometry("300x200")

    label_nom = tk.Label(fenetre_eleve, text="Nom de l'élève :")
    label_nom.pack()
    champ_nom_eleve = tk.Entry(fenetre_eleve)
    champ_nom_eleve.pack()

    label_age = tk.Label(fenetre_eleve, text="Âge de l'élève :")
    label_age.pack()
    champ_age_eleve = tk.Entry(fenetre_eleve)
    champ_age_eleve.pack()

    label_classe_id = tk.Label(fenetre_eleve, text="ID de la classe :")
    label_classe_id.pack()
    champ_classe_id = tk.Entry(fenetre_eleve)
    champ_classe_id.pack()

    def valider():
        nom_eleve = champ_nom_eleve.get()
        age = int(champ_age_eleve.get())
        classe_id = int(champ_classe_id.get())
        ajouter_eleve(nom_eleve, age, classe_id)
        fenetre_eleve.destroy()

    bouton_valider = tk.Button(fenetre_eleve, text="Valider", command=valider)
    bouton_valider.pack()

def ouvvrir_fenetre_modifier_eleve():
    fenetre_modifier = tk.Toplevel()
    fenetre_modifier.title("Modifier un élève")
    fenetre_modifier.geometry("300x200")

    label_eleve_id = tk.Label(fenetre_modifier, text="ID de l'eleve : ")
    label_eleve_id.pack()
    champ_eleve_id = tk.Entry(fenetre_modifier)
    champ_eleve_id.pack()

    label_nom = tk.Label(fenetre_modifier, text="Nom de l'élève : ")
    label_nom.pack()
    champ_nom_eleve = tk.Entry(fenetre_modifier)
    champ_nom_eleve.pack()

    label_age = tk.Label(fenetre_modifier, text="Age de l'élève : ")
    label_age.pack()
    champ_age_eleve = tk.Entry(fenetre_modifier)
    champ_age_eleve.pack()

    label_classe_id = tk.Label(fenetre_modifier, text="ID de la classe : ")
    label_classe_id.pack()
    champ_classe_id = tk.Entry(fenetre_modifier)
    champ_classe_id.pack()

    def valider():
        eleve_id = int(champ_eleve_id.get())
        nom_eleve = champ_nom_eleve.get()
        age = int(champ_age_eleve.get())
        classe_id = int(champ_classe_id.get())
        modifier_eleve(eleve_id, nom_eleve, age, classe_id)
        fenetre_modifier.destroy()

    bouton_valider = tk.Button(fenetre_modifier, text="Valider", command=valider)
    bouton_valider.pack()

def ouvrir_fenetre_supprimer_eleve():
    fenetre_supprimer = tk.Toplevel()
    fenetre_supprimer.title("Supprimer un élève")
    fenetre_supprimer.geometry("400x300")

    Label_id_a_supprimer = tk.Label(fenetre_supprimer, text="ID de l'élève : ")
    Label_id_a_supprimer.pack()
    champ_id_a_supprimer = tk.Entry(fenetre_supprimer)
    champ_id_a_supprimer.pack()

    def valider():
        id_a_supprimer = int(champ_id_a_supprimer.get())
        supprimer_eleve(id_a_supprimer)
        fenetre_supprimer.destroy()

    bouton_valider = tk.Button(fenetre_supprimer, text="Valider", command=valider)
    bouton_valider.pack()

def ouvrir_fenetre_lister_eleves():
    fenetre_liste = tk.Toplevel()
    fenetre_liste.title("Liste des élèves")
    fenetre_liste.geometry("400x300")

    zone_liste = tk.Listbox(fenetre_liste, width=50)
    zone_liste.pack()

    curseur.execute("SELECT nom, age FROM eleves")
    resultats = curseur.fetchall()
    for ligne in resultats:
        zone_liste.insert(tk.END, f"{ligne[0]} - {ligne[1]} ans")

def verifier_connexion():
    nom = champ_nom.get()
    mdp = champ_mdp.get()
    role = connexion_login(nom, mdp)

    if role is None:
        label_message.config(text="Connexion échouée")
    else:
        fenetre.destroy()
        ouvrir_menu_principal(role)

bouton_connexion = tk.Button(fenetre, text="Se connecter", command=verifier_connexion)
bouton_connexion.pack()

fenetre.mainloop()