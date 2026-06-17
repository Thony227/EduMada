from database import connexion, curseur

def ajouter_sanction(eleve_id, date, type, motif):
    curseur.execute("INSERT INTO sanctions (eleve_id, date, type, motif) VALUES (?, ?, ?, ?)", (eleve_id, date, type, motif))
    connexion.commit()

def lister_sanction(eleve_id):
    curseur.execute("SELECT eleves.nom, sanctions.date, sanctions.type, sanctions.motif FROM sanctions JOIN eleves ON sanctions.eleve_id = eleves.id WHERE sanctions.eleve_id = ?", (eleve_id,))
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)
