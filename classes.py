from database import connexion, curseur

def ajouter_classe(nom_classe, niveau):
    curseur.execute("INSERT INTO classes (nom_classe, niveau) VALUES (?, ?)", (nom_classe, niveau))
    connexion.commit()

def lister_classes():
    curseur.execute("SELECT * FROM classes")
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

def assigner_titulaire(classe_id, enseignant_id):
    curseur.execute("UPDATE classes SET enseignant_titulaire_id = ? WHERE id = ? ", (enseignant_id, classe_id))
    connexion.commit()

def lister_classes_avec_enseignant():
    curseur.execute("""
        SELECT classes.nom_classe, classes.niveau, enseignants.nom
        FROM classes
        JOIN enseignants ON classes.enseignant_titulaire_id = enseignants.id
    """)
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)