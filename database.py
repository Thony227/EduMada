import sqlite3

connexion = sqlite3.connect("edumada.db")
curseur = connexion.cursor()

print("connexion réussie")

curseur.execute("""
    CREATE TABLE IF NOT EXISTS eleves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        age INTEGER,
        classe_id INTEGER,
        FOREIGN KEY (classe_id) REFERENCES classes (id)
    )
""")
connexion.commit()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleve_id INTEGER,
        matiere TEXT,
        note REAL,
        FOREIGN KEY (eleve_id) REFERENCES eleves (id)
    )
""")
connexion.commit()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_classe TEXT,
        niveau TEXT,
        enseignant_titulaire_id INTEGER,
        FOREIGN KEY (enseignant_titulaire_id) REFERENCES enseignants (id)
    )
""")
connexion.commit()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS enseignants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        matiere_principale TEXT
    )
""")
connexion.commit()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS absences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleve_id INTEGER, 
        date TEXT,
        type TEXT,
        justifie INTEGER,
        FOREIGN KEY (eleve_id) REFERENCES eleves (id)
    )
""")
connexion.commit()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS sanctions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleve_id INTEGER,
        date TEXT,
        type TEXT,
        motif TEXT, 
        FOREIGN KEY (eleve_id) REFERENCES eleves (id)
    )
""")
connexion.commit()
