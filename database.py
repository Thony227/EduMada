import sqlite3

connexion = sqlite3.connect("edumada.db")
curseur = connexion.cursor()

print("connexion réussie")

curseur.execute("""
    CREATE TABLE IF NOT EXISTS eleves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        age INTEGER,
        classe TEXT
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

