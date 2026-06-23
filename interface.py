import tkinter as tk
from database import connexion, curseur
from utilisateurs import connexion_login
from classes import ajouter_classe, lister_classes, assigner_titulaire, lister_classes_avec_enseignant
from eleves import ajouter_eleve, lister_eleve, modifier_eleve, supprimer_eleve, lister_eleves_avec_classe, lister_eleves_avec_moyenne
from notes import ajouter_note, moyenne_eleve
from enseignants import ajouter_enseignant, lister_enseignants
from absences import ajouter_absence, lister_absence
from sanctions import ajouter_sanction, lister_sanction
from finances import ajouter_frais, ajouter_paiement, voir_situation_financiere
from bulletin import generer_bulletin, moyenne_matiere
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import filedialog

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
    menu.geometry("1020x850")
    menu.configure(bg=COULEUR_FOND)

    label_bienvenue = tk.Label(menu, text=f"Bienvenue ! Votre rôle : {role}", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_bienvenue.pack(pady=5)

    if role == "directeur":
        bouton_classe = tk.Button(menu, text="Ajouter Une classe", command=ouvrir_fenetre_ajouter_classe, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_classe.pack(pady=10)

        bouton_enseigant = tk.Button(menu, text="Ajouter un enseigant", command=ouvrir_fenetre_ajouter_enseignant, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_enseigant.pack(pady=10)

        bouton_frais = tk.Button(menu, text="Ajouter les frais de scolarité", command= ouvrir_fenetre_ajouter_frais, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_frais.pack(pady=10)

        bouton_paiement = tk.Button(menu, text="Ajouter un paiement", command=ouvrir_fenetre_ajouter_paiement, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)
        
        bouton_situation_finaciere = tk.Button(menu, text="Voir situation financière", command=ouvrir_fenetre_situation_financiere, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

        tk.Button(menu, text="Assigner un titulaire", command=ouvrir_fenetre_assigner_titulaire, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

        tk.Button(menu, text="Retirer le titulaire d'une classe", command=ouvrir_fenetre_retirer_titulaire, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    if role == "secretariat":
        bouton_eleve = tk.Button(menu, text="Ajouter un élève", command=ouvrir_fenetre_ajouter_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_eleve.pack(pady=10)

        bouton_modifier = tk.Button(menu, text="Modifier un élève", command=ouvrir_fenetre_modifier_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_modifier.pack(pady=10)

        bouton_supprimer = tk.Button(menu, text="Supprimer un élève", command=ouvrir_fenetre_supprimer_eleve, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_supprimer.pack(pady=10)

        bouton_absence = tk.Button(menu, text="Ajouter une absence", command=ouvrir_fenetre_ajouter_absence, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_absence.pack(pady=10)

        

    if role == "enseignant":
        bouton_note = tk.Button(menu, text="Ajouter une note", command=ouvrir_fenetre_ajouter_note, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
        bouton_note.pack(pady=10)

        tk.Button(menu, text="Modifier une note", command=ouvrir_fenetre_modifier_note, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

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

    bouton_sanction = tk.Button(menu, text="Ajouter une sanction", command=ouvrir_fenetre_ajouter_sanction, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_sanction.pack(pady=10)

    bouton_liste_sanction = tk.Button(menu, text="Liste des sanctions d'un élève", command=ouvrir_fenetre_lister_sanction, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_liste_sanction.pack(pady=10)

    tk.Button(menu, text="Bulletin d'un élève", command=ouvrir_fenetre_bulletin, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    tk.Button(menu, text="Moyenne par matière", command=ouvrir_fenetre_moyenne_matiere, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    tk.Button(menu, text="Moyenne de la classe", command=ouvrir_fenetre_moyenne_classe, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    tk.Button(menu, text="Classes avec titulaire", command=ouvrir_fenetre_classes_avec_enseignant, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    tk.Button(menu, text="Élèves avec leur classe", command=ouvrir_fenetre_eleves_avec_classe, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

    tk.Button(menu, text="Élèves avec leur moyenne", command=ouvrir_fenetre_eleves_avec_moyenne, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

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
        ajouter_enseignant(nom_enseignant, matiere_principale)
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

def ouvrir_fenetre_ajouter_sanction():
    fenetre_sanction = tk.Toplevel()
    fenetre_sanction.title("Ajouter un sanction à un élève")
    fenetre_sanction.geometry("620x450")
    fenetre_sanction.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_sanction, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_sanction)
    champ_eleve_id.pack(pady=5)

    label_date_sanction = tk.Label(fenetre_sanction, text="Date(JJ/MM/AAAA) :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_date_sanction.pack(pady=5)
    champ_date_sanction = tk.Entry(fenetre_sanction)
    champ_date_sanction.pack(pady=5)

    label_type_sanction = tk.Label(fenetre_sanction, text="Type de sanction :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_type_sanction.pack(pady=5)
    champ_type_sanction = tk.Entry(fenetre_sanction)
    champ_type_sanction.pack(pady=5)

    label_motif_sanction = tk.Label(fenetre_sanction, text="Motif de sanction :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_motif_sanction.pack(pady=5)
    champ_motif_sanction = tk.Entry(fenetre_sanction)
    champ_motif_sanction.pack(pady=5)

    def valider():
        eleve_id = int(champ_eleve_id.get())
        date = champ_date_sanction.get()
        type_sanction = champ_type_sanction.get()
        motif = champ_motif_sanction.get()
        ajouter_sanction(eleve_id, date, type_sanction, motif)
        fenetre_sanction.destroy()
    
    bouton_valider = tk.Button(fenetre_sanction, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_ajouter_frais():
    fenetre_frais = tk.Toplevel()
    fenetre_frais.title("Ajouter les frais de scolarité")
    fenetre_frais.geometry("620x450")
    fenetre_frais.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_frais, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_frais)
    champ_eleve_id.pack(pady=5)

    label_montant_total = tk.Label(fenetre_frais, text="Montant Total :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_montant_total.pack(pady=5)
    champ_montant_total = tk.Entry(fenetre_frais)
    champ_montant_total.pack(pady=5)

    label_annee_scolaire = tk.Label(fenetre_frais, text="Année Scolaire", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_annee_scolaire.pack(pady=5)
    champ_annee_scolaire = tk.Entry(fenetre_frais)
    champ_annee_scolaire.pack(pady=5)

    def valider():
        eleve_id = int(champ_eleve_id.get())
        montant_total = float(champ_montant_total.get())
        annee_scolaire = champ_annee_scolaire.get()
        ajouter_frais(eleve_id, montant_total, annee_scolaire)
        fenetre_frais.destroy()
    
    bouton_valider = tk.Button(fenetre_frais, text="Valider", command= valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_valider.pack(pady=10)

def ouvrir_fenetre_ajouter_paiement():
    fenetre_paiement = tk.Toplevel()
    fenetre_paiement.title("Ajouter un paiement")
    fenetre_paiement.geometry("620x450")
    fenetre_paiement.configure(bg=COULEUR_FOND)

    label_frais_id = tk.Label(fenetre_paiement, text="Fais ID :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_frais_id.pack(pady=5)
    champ_frais_id = tk.Entry(fenetre_paiement)
    champ_frais_id.pack(pady=5)

    tk.Label(fenetre_paiement, text="Montant payé :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_montant_paiement = tk.Entry(fenetre_paiement)
    champ_montant_paiement.pack(pady=5)

    tk.Label(fenetre_paiement, text="Date(JJ/MM/AAAA) :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_date = tk.Entry(fenetre_paiement)
    champ_date.pack(pady=5)

    def valider():
        ajouter_paiement(int(champ_frais_id.get()), float(champ_montant_paiement.get), champ_date.get())
        fenetre_paiement.destroy()

    bouton_valider = tk.Button(fenetre_paiement, text="Afficher", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=5)

def ouvrir_fenetre_situation_financiere():
    fenetre_finance = tk.Toplevel()
    fenetre_finance.title("Situation financière")
    fenetre_finance.geometry("620x450")
    fenetre_finance.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_finance, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_finance)
    champ_eleve_id.pack(pady=5)

    zone_liste = tk.Listbox(fenetre_finance, width=60)
    zone_liste.pack(pady=10)

    def afficher():
        zone_liste.delete(0, tk.END)
        eleve_id = int(champ_eleve_id.get())
        curseur.execute("""
            SELECT frais_scolarite.montant_total, frais_scolarite.annee_scolaire, SUM(paiements.montant_paye)
            FROM frais_scolarite
            LEFT JOIN paiements ON paiements.frais_id = frais_scolarite.id
            WHERE frais_scolarite.eleve_id = ?
            GROUP BY frais_scolarite.id
        """,(eleve_id,))
        for ligne in curseur.fetchall():
            montant_total = ligne[0]
            annee = ligne[1]
            total_paye = ligne[2] or 0
            reste = montant_total -total_paye
            zone_liste.insert(tk.END, f"{annee} | Total: {montant_total} | Payé: {total_paye} | Reste: {reste} Ar")

    bouton_afficher = tk.Button(fenetre_finance, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def ouvrir_fenetre_modifier_eleve():
    fenetre_modifier = tk.Toplevel()
    fenetre_modifier.title("Modifier un élève")
    fenetre_modifier.geometry("620x450")
    fenetre_modifier.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_modifier, text="ID de l'élève : ", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
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
    fenetre_absences.title("Absence(s)/Retard(s) de l'élève")
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

def ouvrir_fenetre_lister_sanction():
    fenetre_sanctions = tk.Toplevel()
    fenetre_sanctions.title("Sanction(s) de l'élève")
    fenetre_sanctions.geometry("620x450")
    fenetre_sanctions.configure(bg=COULEUR_FOND)

    label_eleve_id = tk.Label(fenetre_sanctions, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_eleve_id.pack(pady=5)
    champ_eleve_id =tk.Entry(fenetre_sanctions)
    champ_eleve_id.pack(pady=10)

    zone_liste_sanction = tk.Listbox(fenetre_sanctions, width=50)
    zone_liste_sanction.pack(pady=10)

    def afficher():
        zone_liste_sanction.delete(0, tk.END)
        eleve_id = int(champ_eleve_id.get())
        curseur.execute("SELECT date, type, motif FROM sanctions WHERE eleve_id = ?",(eleve_id,))
        resultats = curseur.fetchall()
        for ligne in resultats:
            zone_liste_sanction.insert(tk.END, f"{ligne[0]} | {ligne[1]} | {ligne[2]}")

    bouton_afficher = tk.Button(fenetre_sanctions, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
    bouton_afficher.pack(pady=10)

def ouvrir_fenetre_connexion():
    fenetre_login = tk.Toplevel()
    fenetre_login.title("Connexion")
    fenetre_login.geometry("400X300")
    fenetre_login.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_login, text="Nom d'utilisateur :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_nom = tk.Entry(fenetre_login)
    champ_nom.pack(pady=5)

    tk.Label(fenetre_login, text="Mot de passe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_mdp = tk.Entry(fenetre_login)
    champ_mdp.pack(pady=5)

    label_erreur = tk.Label(fenetre_login, text="", bg=COULEUR_FOND, fg="red")
    label_erreur.pack()

    def valider():
        role = connexion_login(champ_nom.get(), champ_mdp.get())
        if role:
            fenetre_login.destroy()
            ouvrir_menu_principal(role)
        else:
            label_erreur.config(text="Identifiants incorrects.")

    bouton_login = tk.Button(fenetre_login, text="Se connecter", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def se_connecter():
    role = connexion_login(champ_nom.get(), champ_mdp.get())
    if role:
        fenetre.destroy()
        ouvrir_menu_principal(role)
    else:
        label_message.config(text="Identifiant incorrects." ,fg="red")

bouton_connexion = tk.Button(fenetre, text="Se connecter", command=se_connecter, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD)
bouton_connexion.pack(pady=10)

def ouvrir_fenetre_bulletin():
    fenetre_bulletin = tk.Toplevel()
    fenetre_bulletin.title("Bulletin de l'élève")
    fenetre_bulletin.geometry("620x450")
    fenetre_bulletin.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_bulletin, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_bulletin)
    champ_eleve_id.pack(pady=5)

    zone_liste = tk.Listbox(fenetre_bulletin, width=60)
    zone_liste.pack(pady=10)

    def afficher():
        zone_liste.delete(0, tk.END)
        eleve_id = int(champ_eleve_id.get())

        curseur.execute("SELECT nom FROM eleves WHERE id = ?", (eleve_id,))
        eleve = curseur.fetchone()
        zone_liste.insert(tk.END, f"Bulletin de : {eleve[0]}")
        zone_liste.insert(tk.END, "---")

        curseur.execute("SELECT matiere, note FROM notes WHERE eleve_id = ?", (eleve_id,))
        for ligne in curseur.fetchall():
            zone_liste.insert(tk.END, f"{ligne[0]} : {ligne[1]}")

        moyenne = moyenne_eleve(eleve_id)
        zone_liste.insert(tk.END, "---")
        zone_liste.insert(tk.END, f"Moyenne générale : {round(moyenne, 2) if moyenne else 'Aucune note'}")

    def telecharger_bulletin():
        eleve_id = int(champ_eleve_id.get())

        curseur.execute("SELECT nom FROM eleves WHERE id = ?", (eleve_id,))
        eleve = curseur.fetchone()
        if not eleve:
            return

        curseur.execute("SELECT matiere, note FROM notes WHERE eleve_id = ?", (eleve_id,))
        notes = curseur.fetchall()

        moyenne = moyenne_eleve(eleve_id)

    # Demande où sauvegarder
        chemin = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")],
        initialfile=f"bulletin_{eleve[0]}.pdf"
        )
        if not chemin:
            return

    # Génération du PDF
        c = canvas.Canvas(chemin, pagesize=A4)
        largeur, hauteur = A4

    # En-tête
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(largeur / 2, hauteur - 60, "EduMada")
        c.setFont("Helvetica", 13)
        c.drawCentredString(largeur / 2, hauteur - 85, "Bulletin de notes")

    # Ligne de séparation
        c.line(50, hauteur - 100, largeur - 50, hauteur - 100)

    # Nom de l'élève
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, hauteur - 130, f"Élève : {eleve[0]}")

    # Notes
        c.setFont("Helvetica", 11)
        y = hauteur - 170
        c.drawString(50, y, "Matière")
        c.drawString(300, y, "Note")
        y -= 20
        c.line(50, y, largeur - 50, y)
        y -= 20

        for ligne in notes:
            c.drawString(50, y, str(ligne[0]))
            c.drawString(300, y, str(ligne[1]))
            y -= 25

    # Moyenne
        c.line(50, y, largeur - 50, y)
        y -= 25
        c.setFont("Helvetica-Bold", 12)
        moy = round(moyenne, 2) if moyenne else "Aucune note"
        c.drawString(50, y, f"Moyenne générale : {moy}")

        c.save()


    tk.Button(fenetre_bulletin, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)
    tk.Button(fenetre_bulletin, text="Télécharger PDF", command=telecharger_bulletin, bg="#27AE60", fg="white", font=POLICE_BOLD).pack(pady=5)

def ouvrir_fenetre_moyenne_matiere():
    fenetre_matiere = tk.Toplevel()
    fenetre_matiere.title("Moyenne par matière")
    fenetre_matiere.geometry("620x450")
    fenetre_matiere.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_matiere, text="Nom de la matière :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_matiere = tk.Entry(fenetre_matiere)
    champ_matiere.pack(pady=5)

    label_resultat = tk.Label(fenetre_matiere, text="", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_resultat.pack(pady=10)

    def afficher():
        matiere = champ_matiere.get()
        curseur.execute("SELECT matiere, AVG(note) FROM notes WHERE matiere = ? GROUP BY matiere", (matiere,))
        resultat = curseur.fetchone()
        if resultat:
            label_resultat.config(text=f"{resultat[0]} : {round(resultat[1], 2)}")
        else:
            label_resultat.config(text="Matière introuvable.")

    tk.Button(fenetre_matiere, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def ouvrir_fenetre_moyenne_classe():
    fenetre_classe = tk.Toplevel()
    fenetre_classe.title("Moyenne de la classe")
    fenetre_classe.geometry("620x450")
    fenetre_classe.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_classe, text="ID de la classe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_classe_id = tk.Entry(fenetre_classe)
    champ_classe_id.pack(pady=5)

    label_resultat = tk.Label(fenetre_classe, text="", bg=COULEUR_FOND, fg=COULEUR_TEXTE)
    label_resultat.pack(pady=10)

    def afficher():
        classe_id = int(champ_classe_id.get())
        curseur.execute("""
            SELECT AVG(notes.note)
            FROM notes
            JOIN eleves ON eleves.id = notes.eleve_id
            WHERE eleves.classe_id = ?
        """, (classe_id,))
        resultat = curseur.fetchone()
        if resultat and resultat[0]:
            label_resultat.config(text=f"Moyenne de la classe : {round(resultat[0], 2)}")
        else:
            label_resultat.config(text="Aucune note pour cette classe.")

    tk.Button(fenetre_classe, text="Afficher", command=afficher, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def ouvrir_fenetre_assigner_titulaire():
    fenetre_titulaire = tk.Toplevel()
    fenetre_titulaire.title("Assigner un titulaire")
    fenetre_titulaire.geometry("620x450")
    fenetre_titulaire.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_titulaire, text="ID de la classe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_classe_id = tk.Entry(fenetre_titulaire)
    champ_classe_id.pack(pady=5)

    tk.Label(fenetre_titulaire, text="ID de l'enseignant :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_enseignant_id = tk.Entry(fenetre_titulaire)
    champ_enseignant_id.pack(pady=5)

    def valider():
        assigner_titulaire(int(champ_classe_id.get()), int(champ_enseignant_id.get()))
        fenetre_titulaire.destroy()

    tk.Button(fenetre_titulaire, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def ouvrir_fenetre_eleves_avec_classe():
    fenetre_ec = tk.Toplevel()
    fenetre_ec.title("Élèves avec leur classe")
    fenetre_ec.geometry("620x450")
    fenetre_ec.configure(bg=COULEUR_FOND)

    zone_liste = tk.Listbox(fenetre_ec, width=60)
    zone_liste.pack(pady=10)

    curseur.execute("""
        SELECT eleves.nom, eleves.age, classes.nom_classe
        FROM eleves
        JOIN classes ON eleves.classe_id = classes.id
    """)
    for ligne in curseur.fetchall():
        zone_liste.insert(tk.END, f"{ligne[0]} | {ligne[2]} | {ligne[1]} ans")

def ouvrir_fenetre_classes_avec_enseignant():
    fenetre_ce = tk.Toplevel()
    fenetre_ce.title("Classes avec leur titulaire")
    fenetre_ce.geometry("620x450")
    fenetre_ce.configure(bg=COULEUR_FOND)

    zone_liste = tk.Listbox(fenetre_ce, width=60)
    zone_liste.pack(pady=10)

    curseur.execute("""
        SELECT classes.nom_classe, classes.niveau, enseignants.nom
        FROM classes
        LEFT JOIN enseignants ON classes.enseignant_titulaire_id = enseignants.id
    """)
    for ligne in curseur.fetchall():
        titulaire = ligne[2] if ligne[2] else "Aucun titulaire"
        zone_liste.insert(tk.END, f"{ligne[0]} | {ligne[1]} | {titulaire}")

def ouvrir_fenetre_eleves_avec_moyenne():
    fenetre_em = tk.Toplevel()
    fenetre_em.title("Élèves avec leur moyenne")
    fenetre_em.geometry("620x450")
    fenetre_em.configure(bg=COULEUR_FOND)

    zone_liste = tk.Listbox(fenetre_em, width=60)
    zone_liste.pack(pady=10)

    curseur.execute("""
        SELECT eleves.nom, classes.nom_classe, AVG(notes.note)
        FROM eleves
        JOIN classes ON eleves.classe_id = classes.id
        LEFT JOIN notes ON notes.eleve_id = eleves.id
        GROUP BY eleves.id
    """)
    for ligne in curseur.fetchall():
        moyenne = round(ligne[2], 2) if ligne[2] else "Aucune note"
        zone_liste.insert(tk.END, f"{ligne[0]} | {ligne[1]} | Moy: {moyenne}")

def ouvrir_fenetre_retirer_titulaire():
    fenetre_retirer = tk.Toplevel()
    fenetre_retirer.title("Retirer le titulaire")
    fenetre_retirer.geometry("620x450")
    fenetre_retirer.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_retirer, text="ID de la classe :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_classe_id = tk.Entry(fenetre_retirer)
    champ_classe_id.pack(pady=5)

    def valider():
        curseur.execute("UPDATE classes SET enseignant_titulaire_id = NULL WHERE id = ?", (int(champ_classe_id.get()),))
        connexion.commit()
        fenetre_retirer.destroy()

    tk.Button(fenetre_retirer, text="Retirer", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

def ouvrir_fenetre_modifier_note():
    fenetre_modifier_note = tk.Toplevel()
    fenetre_modifier_note.title("Modifier une note")
    fenetre_modifier_note.geometry("620x500")
    fenetre_modifier_note.configure(bg=COULEUR_FOND)

    tk.Label(fenetre_modifier_note, text="ID de l'élève :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_eleve_id = tk.Entry(fenetre_modifier_note)
    champ_eleve_id.pack(pady=5)

    zone_liste = tk.Listbox(fenetre_modifier_note, width=60)
    zone_liste.pack(pady=5)

    def charger_notes():
        zone_liste.delete(0, tk.END)
        curseur.execute("SELECT id, matiere, note FROM notes WHERE eleve_id = ?", (int(champ_eleve_id.get()),))
        for ligne in curseur.fetchall():
            zone_liste.insert(tk.END, f"ID:{ligne[0]} | {ligne[1]} : {ligne[2]}")

    tk.Button(fenetre_modifier_note, text="Charger les notes", command=charger_notes, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=5)

    tk.Label(fenetre_modifier_note, text="ID de la note à modifier :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_note_id = tk.Entry(fenetre_modifier_note)
    champ_note_id.pack(pady=5)

    tk.Label(fenetre_modifier_note, text="Nouvelle note :", bg=COULEUR_FOND, fg=COULEUR_TEXTE).pack(pady=5)
    champ_nouvelle_note = tk.Entry(fenetre_modifier_note)
    champ_nouvelle_note.pack(pady=5)

    def valider():
        curseur.execute(
            "UPDATE notes SET note = ? WHERE id = ?",
            (float(champ_nouvelle_note.get()), int(champ_note_id.get()))
        )
        connexion.commit()
        fenetre_modifier_note.destroy()

    tk.Button(fenetre_modifier_note, text="Valider", command=valider, bg=COULEUR_BOUTON, fg=COULEUR_TEXTE, font=POLICE_BOLD).pack(pady=10)

fenetre.mainloop()