import hashlib
from database import connexion, curseur

def creer_compte(nom_utilisateur, mot_de_passe, role):
    mdp_chiffre = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    curseur.execute("INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe, role) VALUES (?, ?, ?)", (nom_utilisateur, mdp_chiffre, role))
    connexion.commit()

def lister_utilisateur():
    curseur.execute("SELECT * FROM utilisateurs")
    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

def connexion(nom_utilisateur, mot_de_passe):
    mdp_chiffre = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    curseur.execute("SELECT role FROM utilisateurs WHERE nom_utilisateur = ? AND mot_de_passe = ?", (nom_utilisateur, mdp_chiffre))
    resultat = curseur.fetchone()

    if resultat:
        print(f"Connexion réussie ! Rôle : {resultat[0]}")
        return resultat[0]
    else:
        print("Nom d'utilisateur ou mot de passe incorrect")
        return None