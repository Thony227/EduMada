import tkinter as tk
from database import connexion, curseur
from utilisateurs import connexion_login
from classes import ajouter_classe, lister_classes
from eleves import ajouter_eleve, lister_eleve, modifier_eleve, supprimer_eleve
from notes import ajouter_note, moyenne_eleve
from enseignants import ajouter_enseignant, lister_enseignants
from absences import ajouter_absence, lister_absence

COULEUR_FOND = "#2C3E50"
COULEUR_TEXTE = "white"
COULEUR_BOUTON = "#3498DB"
POLICE = ("Arial", 10)
POLICE_BOLD = ("Arial", 10, "bold")

fenetre = tk.Tk()
fenetre.title("Edumada - Connexion")
fenetre.geometry("620x450")
fenetre.configure(bg=COULEUR_FOND)

label_titre =  tk.Label(fenetre, text="EduMada", bg=COULEUR_FOND, fg=COULEUR_TEXTE, font=("Arial", 20, "bold"))
label_titre.pack(pady=20)

label_nom = tk.Label(fenetre, text="Nom de l'utilisateur :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
label_nom.pack(pady=5)

champ_nom = tk.Entry(fenetre)
champ_nom.pack(pady=5)

label_mdp = tk.Label(fenetre, text="Mot de passe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
label_mdp.pack(pady=5)

champ_mdp = tk.Entry(fenetre, show="*")
champ_mdp.pack(pady=5)

label_message = tk.Label(fenetre, text="", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
label_message.pack(pady=5)

def ouvrir_menu_principal(role):
    menu = tk.Tk()
    menu.title("EduMada - Menu Principal")
    menu.geometry("620x450")
    menu.configure(bg=COULEUR_FOND)

    label_bienvenue = tk.Label(menu, text=f"Bienvenue ! Votre rôle : {role}", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_bienvenue.pack(pady=5)

    if role == "directeur":
        bouton_classe = tk.Button(menu, text="Ajouter Une classe", command=ouvrir_fenetre_ajouter_classe, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_classe.pack(pady=10)

        bouton_enseigant =tk.Button(menu, text="Ajouter un enseigant", command=ouvrir_fenetre_ajouter_enseignant, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_enseigant.pack(pady=10)

    if role == "secretariat":
        bouton_eleve = tk.Button(menu, text="Ajouter un élève", command=ouvrir_fenetre_ajouter_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_eleve.pack(pady=10)

        bouton_modifier = tk.Button(menu, text="Modifier un élève", command=ouvvrir_fenetre_modifier_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_modifier.pack(pady=10)

        bouton_supprimer = tk.Button(menu, text="Supprimer un élève", command=ouvrir_fenetre_supprimer_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_supprimer.pack(pady=10)

        bouton_absence = tk.Button(menu, text="Ajouter une absence", command=ouvrir_fenetre_ajouter_absence, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_absence.pack(pady=10)

    if role == "enseignant":
        bouton_note = tk.Button(menu, text="Ajouter une note", command=ouvrir_fenetre_ajouter_note, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_note.pack(pady=10)

    bouton_liste = tk.Button(menu, text="Liste des élèves", command=ouvrir_fenetre_lister_eleves, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_liste.pack(pady=10)
    
    bouton_moyenne = tk.Button(menu, text="Afficher la moyenne d'un élève", command=ouvrir_fenetre_moyenne_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_moyenne.pack(pady=10)

    bouton_liste_classe = tk.Button(menu, text="Liste des classe", command=ouvrir_fenetre_lister_classes, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_liste_classe.pack(pady=10)

    bouton_liste_enseignant = tk.Button(menu, text="Liste des enseignants" , command=ouvrir_fenetre_lister_enseignant, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_liste_enseignant.pack(pady=10)

    bouton_liste_absence = tk.Button(menu, text="Liste des absences d'un élève", command=ouvrir_fenetre_lister_absence, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_liste_absence.pack(pady=10)

    menu.mainloop()

def ouvrir_fenetre_ajouter_classe():
    fenetre_classe = tk.Toplevel()
    fenetre_classe.title("Ajouter une classe")
    fenetre_classe.geometry("620x450")
    fenetre_classe.configure(bg=COULEUR_FOND)

    label_nom = tk.Label(fenetre_classe, text="Nom de la classe : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_nom.pack(pady=5)
    champ_nom_classe = tk.Entry(fenetre_classe)
    champ_nom_classe.pack(pady=5)

    label_niveau = tk.Label(fenetre_classe, text="Niveau : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_niveau.pack(pady=5)
    champ_niveau = tk.Entry(fenetre_classe)
    champ_niveau.pack(pady=5)

    def valider():
        nom_classe = champ_nom_classe.get()
        niveau = champ_niveau.get()
        ajouter_classe(nom_classe, niveau)
        fenetre_classe.destroy()

    bouton_valider = tk.Button(fenetre_classe, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_lister_classes():
    fenetre_liste_classe = tk.Toplevel()
    fenetre_liste_classe.title("Liste des classes")
    fenetre_liste_classe.geometry("620x450")
    fenetre_liste_classe.configure(bg=COULEUR_FOND)

    zone_liste_classe = tk.Listbox(fenetre_liste_classe, width=50)
    zone_liste_classe.pack(pady=8)

    curseur.execute("SELECT nom_classe, niveau FROM classes")
    resultats = curseur.fetchall()
    for ligne in resultats:
        zone_liste_classe.insert(tk.END, f"{ligne[0]} - {ligne[1]}")

def ouvrir_fenetre_ajouter_enseignant():
    fenetre_ajouter_enseignant =tk.Toplevel()
    fenetre_ajouter_enseignant.title("Ajouter un enseignant")
    fenetre_ajouter_enseignant.geometry("620x450")
    fenetre_ajouter_enseignant.configure(bg=COULEUR_FOND)

    label_nom_enseignant = tk.Label(fenetre_ajouter_enseignant, text="Nom de l'enseigant :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_nom_enseignant.pack(pady=5)
    champ_nom_enseignant = tk.Entry(fenetre_ajouter_enseignant)
    champ_nom_enseignant.pack(pady=5)

    label_matiere_principal = tk.Label(fenetre_ajouter_enseignant, text="Matière principale :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_matiere_principal.pack(pady=5)
    champ_matiere_principal = tk.Entry(fenetre_ajouter_enseignant)
    champ_matiere_principal.pack(pady=5)

    def valider():
        nom_enseignant = champ_nom_enseignant.get()
        matiere_principale = champ_matiere_principal.get()
        ajouter_enseignant=(nom_enseignant, matiere_principale)
        fenetre_ajouter_enseignant.destroy()

    bouton_valider = tk.Button(fenetre_ajouter_enseignant, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_ajouter_eleve():
    fenetre_eleve = tk.Toplevel()
    fenetre_eleve.title("Ajouter un élève")
    fenetre_eleve.geometry("620x450")
    fenetre_eleve.configure(bg=COULEUR_FOND)

    label_nom = tk.Label(fenetre_eleve, text="Nom de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_nom.pack(pady=5)
    champ_nom_eleve = tk.Entry(fenetre_eleve)
    champ_nom_eleve.pack(pady=5)

    label_age = tk.Label(fenetre_eleve, text="Âge de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_age.pack(pady=5)
    champ_age_eleve = tk.Entry(fenetre_eleve)
    champ_age_eleve.pack(pady=5)

    label_classe_id = tk.Label(fenetre_eleve, text="ID de la classe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_classe_id.pack(pady=5)
    champ_classe_id = tk.Entry(fenetre_eleve)
    champ_classe_id.pack(pady=5)

    def valider():
        nom_eleve = champ_nom_eleve.get()
        age = int(champ_age_eleve.get())
        classe_id = int(champ_classe_id.get())
        ajouter_eleve(nom_eleve, age, classe_id)
        fenetre_eleve.destroy()

    bouton_valider = tk.Button(fenetre_eleve, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_ajouter_absence():
    fenetre_absence = tk.Toplevel()
    fenetre_absence.title("Ajouter un absence/retard")
    fenetre_absence.geometry("620x450")
    fenetre_absence.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_absence, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_absence)
    champ_eleve_id.pack(pady=5)

    label_date = tk.Label(fenetre_absence, text="Date(JJ/MM/AAAA) :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_date.pack(pady=5)
    champ_date = tk.Entry(fenetre_absence)
    champ_date.pack(pady=5)

    label_type_absence = tk.Label(fenetre_absence, text="Type(Absence/Retard) :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_type_absence.pack(pady=5)
    champ_type_absence = tk.Entry(fenetre_absence)
    champ_type_absence.pack(pady=5)

    label_justifier = tk.Label(fenetre_absence, text="Justifier? (1=oui 0=non) :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_justifier.pack(pady=5)
    champ_justifier = tk.Entry(fenetre_absence)
    champ_justifier.pack(pady=5)

    def valider():
        eleve_id = int(champ_eleve_id.get())
        date = champ_date.get()
        type_absence = champ_type_absence.get()
        justifie = int(champ_justifier.get())
        ajouter_absence(eleve_id, date, type_absence, justifie)
        fenetre_absence.destroy()

    bouton_valider = tk.Button(fenetre_absence, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvvrir_fenetre_modifier_eleve():
    fenetre_modifier = tk.Toplevel()
    fenetre_modifier.title("Modifier un élève")
    fenetre_modifier.geometry("620x450")
    fenetre_modifier.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_modifier, text="ID de l'eleve : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_modifier)
    champ_eleve_id.pack(pady=5)

    label_nom = tk.Label(fenetre_modifier, text="Nom de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_nom.pack(pady=5)
    champ_nom_eleve = tk.Entry(fenetre_modifier)
    champ_nom_eleve.pack(pady=5)

    label_age = tk.Label(fenetre_modifier, text="Age de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_age.pack(pady=5)
    champ_age_eleve = tk.Entry(fenetre_modifier)
    champ_age_eleve.pack(pady=5)

    label_classe_id = tk.Label(fenetre_modifier, text="ID de la classe : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_classe_id.pack(pady=5)
    champ_classe_id = tk.Entry(fenetre_modifier)
    champ_classe_id.pack(pady=5)

    def valider():
        eleve_id = int(champ_eleve_id.get())
        nom_eleve = champ_nom_eleve.get()
        age = int(champ_age_eleve.get())
        classe_id = int(champ_classe_id.get())
        modifier_eleve(eleve_id, nom_eleve, age, classe_id)
        fenetre_modifier.destroy()

    bouton_valider = tk.Button(fenetre_modifier, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_supprimer_eleve():
    fenetre_supprimer = tk.Toplevel()
    fenetre_supprimer.title("Supprimer un élève")
    fenetre_supprimer.geometry("620x450")
    fenetre_supprimer.configure(bg=COULEUR_FOND)

    Label_id_a_supprimer = tk.Label(fenetre_supprimer, text="ID de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    Label_id_a_supprimer.pack(pady=5)
    champ_id_a_supprimer = tk.Entry(fenetre_supprimer)
    champ_id_a_supprimer.pack(pady=5)

    def valider():
        id_a_supprimer = int(champ_id_a_supprimer.get())
        supprimer_eleve(id_a_supprimer)
        fenetre_supprimer.destroy()

    bouton_valider = tk.Button(fenetre_supprimer, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_ajouter_note():
    fenetre_note = tk.Toplevel()
    fenetre_note.title("Ajouter les notes")
    fenetre_note.geometry("620x450")
    fenetre_note.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_note, text="ID de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_note)
    champ_eleve_id.pack(pady=5)

    label_matiere = tk.Label(fenetre_note, text="Entrer la matière : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_matiere.pack(pady=5)
    champ_matiere = tk.Entry(fenetre_note)
    champ_matiere.pack(pady=5)

    label_note =  tk.Label(fenetre_note, text="Entrer la note : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_note.pack(pady=5)
    champ_note = tk.Entry(fenetre_note)
    champ_note.pack(pady=5)

    def valider():
        eleve_id = int(champ_eleve_id.get())
        matiere = champ_matiere.get()
        note = float(champ_note.get())
        ajouter_note(eleve_id, matiere, note)
        fenetre_note.destroy()

    bouton_valider = tk.Button(fenetre_note, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_moyenne_eleve():
    fenetre_moyenne = tk.Toplevel()
    fenetre_moyenne.title("Moyenne de l'élève : ")
    fenetre_moyenne.geometry("620x450")
    fenetre_moyenne.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_moyenne, text="ID de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=3)
    champ_eleve_id = tk.Entry(fenetre_moyenne)
    champ_eleve_id.pack(pady=5)

    label_resultat = tk.Label(fenetre_moyenne, text="", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_resultat.pack(pady=10)

    def afficher():
        eleve_id = int(champ_eleve_id.get())
        moyenne = moyenne_eleve(eleve_id)
        label_resultat.config(text=f"Moyenne de l'élève est : {moyenne}")

    bouton_afficher = tk.Button(fenetre_moyenne, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_afficher.pack(pady=10)

def ouvrir_fenetre_lister_eleves():
    fenetre_liste = tk.Toplevel()
    fenetre_liste.title("Liste des élèves")
    fenetre_liste.geometry("620x450")
    fenetre_liste.configure(bg=COULEUR_FOND)

    zone_liste = tk.Listbox(fenetre_liste, width=50)
    zone_liste.pack(pady=8)

    curseur.execute("SELECT nom, age FROM eleves")
    resultats = curseur.fetchall()
    for ligne in resultats:
        zone_liste.insert(tk.END, f"{ligne[0]} - {ligne[1]} ans")

def ouvrir_fenetre_lister_enseignant():
    fenetre_liste_enseignant = tk.Toplevel()
    fenetre_liste_enseignant.title("Liste des enseignants")
    fenetre_liste_enseignant.geometry("620x450")
    fenetre_liste_enseignant.configure(bg=COULEUR_FOND)

    zone_liste_enseignant = tk.Listbox(fenetre_liste_enseignant, width=50)
    zone_liste_enseignant.pack(pady=8)

    curseur.execute("SELECT nom, matiere_principale FROM enseignants")
    resultats = curseur.fetchall()
    for ligne in resultats:
        zone_liste_enseignant.insert(tk.END, f"{ligne[0]} - {ligne[1]}")

def ouvrir_fenetre_lister_absence():
    fenetre_absences = tk.Toplevel()
    fenetre_absences.title("Absences/Retards de l'élève")
    fenetre_absences.geometry("620x450")
    fenetre_absences.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_absences, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_absences)
    champ_eleve_id.pack(pady=5)

    zone_liste_absence = tk.Listbox(fenetre_absences, width=50)
    zone_liste_absence.pack(pady=10)

    def afficher():
        zone_liste_absence.delete(0, tk.END)
        eleve_id = int(champ_eleve_id.get())
        curseur.execute("SELECT date, type, justifie FROM absences WHERE eleve_id = ?",(eleve_id,))
        resultats = curseur.fetchall()
        for ligne in resultats:
            justifie = "OUI" if ligne[2] == 1 else "Non"
            zone_liste_absence.insert(tk.END, f"{ligne[0]} | {ligne[1]} | justifié : {justifie}")

    bouton_afficher = tk.Button(fenetre_absences, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE,font=POLICE_BOLD)
    bouton_afficher.pack(pady=10)

def verifier_connexion():
    nom = champ_nom.get()
    mdp = champ_mdp.get()
    role = connexion_login(nom, mdp)

    if role is None:
        label_message.config(text="Connexion échouée")
    else:
        fenetre.destroy()
        ouvrir_menu_principal(role)

bouton_connexion = tk.Button(fenetre, text="Se connecter", command=verifier_connexion, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
bouton_connexion.pack(pady=5)

fenetre.mainloop()