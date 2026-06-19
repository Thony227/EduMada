from database import connexion, curseur

def moyenne_classe(classe_id):
    curseur.execute("""
        SELECT classes.nom_classe, AVG(notes.note)
        FROM classes
        JOIN eleves ON eleves.classe_id = classes.id
        JOIN notes ON notes.eleve_id = eleves.id
        WHERE classes.id = ?
        GROUP BY classes.id
    """, (classe_id,))
    resultat = curseur.fetchone()
    print(f"Classe : {resultat[0]} | Moyenne : {resultat[1]}")