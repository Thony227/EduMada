from database import connexion, curseur
from notes import moyenne_eleve

def generer_bulletin(eleve_id):
    curseur.execute("SELECT nom FROM eleves WHERE id = ?", (eleve_id,))
    eleve = curseur.fetchone()
    print(f"Bulletin de {eleve[0]}")

    curseur.execute("SELECT matiere, note FROM notes WHERE eleve_id = ?", (eleve_id,))
    notes = curseur.fetchall()
    for ligne in notes:
        print(f"{ligne[0]} : {ligne[1]}")

    moyenne_eleve(eleve_id)

def moyenne_matiere(matiere):
    curseur.execute("SELECT matiere , AVG(note) FROM notes WHERE matiere = ? GROUP BY matiere", (matiere,))
    resultat = curseur.fetchone()
    print(f"Matiere : {resultat[0]} | Moyenne : {resultat[1]}")