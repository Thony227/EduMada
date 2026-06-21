from database import connexion, curseur

def ajouter_note(eleve_id, matiere, note):
    curseur.execute("INSERT INTO notes (eleve_id, matiere, note) VALUES (?, ?, ?)", (eleve_id, matiere, note))
    connexion.commit()

def moyenne_eleve(eleve_id):
    curseur.execute("SELECT AVG(note) FROM notes WHERE eleve_id = ?", (eleve_id,))
    resultat = curseur.fetchone()
    return resultat[0]