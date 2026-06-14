from database import connexion, curseur

def ajouter_eleve(nom, age, classe):
    curseur.execute("INSERT INTO eleves (nom, age, classe) VALUES(?, ?, ?)", (nom, age, classe))
    connexion.commit()

def lister_eleve():
    curseur.execute("SELECT * FROM eleves")
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

def supprimer_eleve(id_eleve):
    curseur.execute("DELETE FROM eleves WHERE id = ?", (id_eleve,))
    connexion.commit()

def modifier_eleve(id_eleve, nom, age, classe):
    curseur.execute("UPDATE eleves SET nom = ?, age = ?, classe = ? WHERE id = ?", (nom, age, classe, id_eleve))
    connexion.commit()
