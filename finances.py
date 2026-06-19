from database import connexion, curseur

def ajouter_frais(eleve_id, montant_total, annee_scolaire):
    curseur.execute("INSERT INTO frais_scolarite (eleve_id, montant_total, annee_scolaire) VALUES (?, ?, ?)", (eleve_id, montant_total, annee_scolaire))
    connexion.commit()

def ajouter_paiement(frais_id, montant_paye, date_paiement):
    curseur.execute("INSERT INTO paiements (frais_id, montant_paye, date_paiement) VALUES (?, ?, ?)", (frais_id, montant_paye, date_paiement))
    connexion.commit()

def voir_situation_financiere(eleve_id):
    curseur.execute("""
        SELECT frais_scolarite.montant_total, frais_scolarite.annee_scolaire, SUM(paiements.montant_paye) as total_paye
        FROM frais_scolarite
        LEFT JOIN paiements ON paiements.frais_id = frais_scolarite.id
        WHERE frais_scolarite.eleve_id = ?
        GROUP BY frais_scolarite.id
    """, (eleve_id,))
    resultats = curseur.fetchall()
    for ligne in resultats:
        montant_total = ligne[0]
        annee_scolaire = ligne[1]
        total_paye = ligne[2] or 0
        reste = montant_total - total_paye
        print(f"Année : {annee_scolaire} | Total : {montant_total} | Reste : {reste} Ar")