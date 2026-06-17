from database import connexion, curseur

def ajouter_enseignant(nom, matiere_principale):
    curseur.execute("INSERT INTO enseignants (nom, matiere_principale) VALUES (?, ?)", (nom, matiere_principale))
    connexion.commit()

def lister_enseignants():
    curseur.execute("SELECT * FROM enseignants")
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)