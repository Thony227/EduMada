from database import connexion, curseur

def ajouter_eleve(nom, age, classe_id):
    curseur.execute("INSERT INTO eleves (nom, age, classe_id) VALUES(?, ?, ?)", (nom, age, classe_id))
    connexion.commit()

def lister_eleve():
    curseur.execute("SELECT * FROM eleves")
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

def supprimer_eleve(id_eleve):
    curseur.execute("DELETE FROM eleves WHERE id = ?", (id_eleve,))
    connexion.commit()

def modifier_eleve(id_eleve, nom, age, classe_id):
    curseur.execute("UPDATE eleves SET nom = ?, age = ?, classe_id = ? WHERE id = ?", (nom, age, classe_id, id_eleve))
    connexion.commit()

def lister_eleves_avec_classe():
    curseur.execute("""
        SELECT eleves.nom, eleves.age, classes.nom_classe
        FROM eleves
        JOIN classes ON eleves.classe_id = classes.id
    """)
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

def lister_eleves_avec_moyenne():
    curseur.execute("""
        SELECT eleves.nom, classes.nom_classe, AVG(notes.note)
        FROM eleves
        JOIN classes ON eleves.classe_id = classes.id
        JOIN notes ON notes.eleve_id = eleves.id
        GROUP BY eleves.id
    """)
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)
