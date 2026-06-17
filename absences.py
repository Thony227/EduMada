from database import connexion, curseur

def ajouter_absence(eleve_id, date, type, justifie):
    curseur.execute("INSERT INTO absences (eleve_id, date, type, justifie) VALUES (?, ?, ?, ?)", (eleve_id, date, type, justifie))
    connexion.commit()

def lister_absence(eleve_id):
    curseur.execute("SELECT eleves.nom, absences.date, absences.type, absences.justifie FROM absences JOIN eleves ON absences.eleve_id = eleves.id WHERE absences.eleve_id = ?", (eleve_id,))
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)