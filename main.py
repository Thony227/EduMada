from eleves import ajouter_eleve, lister_eleve, supprimer_eleve, modifier_eleve, lister_eleves_avec_classe, lister_eleves_avec_moyenne
from notes import ajouter_note, moyenne_eleve
from classes import ajouter_classe, lister_classes, assigner_titulaire, lister_classes_avec_enseignant
from enseignants import ajouter_enseignant, lister_enseignants
from absences import ajouter_absence, lister_absence
from sanctions import ajouter_sanction, lister_sanction
from finances import ajouter_frais, ajouter_paiement, voir_situation_financiere
from bulletin import generer_bulletin, moyenne_matiere
from statistiques import moyenne_classe
from utilisateurs import creer_compte, lister_utilisateur, connexion_login

print("=== Connexion ===")
nom_utilisateur = input("Veuillez saisir votre identifiant : ")
mdp_chiffre = input("Veuillez saisir votre mot de passe : ")
role_connecte = connexion_login(nom_utilisateur, mdp_chiffre)

if role_connecte is None:
    exit()

while True:
    print("1. Ajouter un élève")
    print("2. Lister les élèves")
    print("3. Supprimer un élève")
    print("4. Modifier l'élève")
    print("5. Ajouter une note")
    print("6. Voir la moyenne d'un élève")
    print("7. Ajouter une classe")
    print("8. Lister des classe")
    print("9. Ajouter enseignant")
    print("10. Lister les enseignants")
    print("11. Assigner un enseignant titulaire a la classe")
    print("12. Lister les élèves avec leur classe")
    print("13. Lister les classe avec leur enseignant")
    print("14. Lister les élèves avec leur moyenne")
    print("15. Ajouter une absence")
    print("16. Lister les absences d'un élève")
    print("17. Ajouter une sanction")
    print("18. Lister les sanctions d'un élève")
    print("19. Ajouter les frais de scolarité")
    print("20. Paiement")
    print("21. Voir la situation financière")
    print("22. Générer le bulletin de l'élève")
    print("23. Moyenne de la Classe")
    print("24. Moyenne des Matiere")
    print("25. Creer un compte")
    print("26. Lister les utilisateurs")
    print("27. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        if role_connecte == "secretariat":
            nom = input("Veuillez entrer votre nom : ")
            age = int(input("veuillez entrer votre age : "))
            classe_id = int(input("ID de la classe : "))
            ajouter_eleve(nom, age, classe_id)
        else:
            print("Accès refuser - Réservé au secretaire")
    elif choix == "2":
        lister_eleve()
    elif choix == "3":
        if role_connecte == "secretariat":
            id_a_supprimer = int(input("ID de l'élève a supprimer : "))
            supprimer_eleve(id_a_supprimer)
        else:
            print("Accès refuser - Réservé au secretaire")
    elif choix == "4":
        if role_connecte == "secretariat":
            id_a_modifier = int(input("ID de l'élève a modifier : "))
            nouveau_nom = input("Veuillez saisir un nouveau nom : ")
            nouvel_age = input("Veuillez saisir un nouvel age : ")
            nouvelle_classe = int(input("ID de la classe : "))
            modifier_eleve(id_a_modifier, nouveau_nom, nouvel_age, nouvelle_classe)
        else:
            print("Accès refuser - Réservé au secretaire")
    elif choix == "5":
        if role_connecte == "enseignant":
            eleve_id = int(input("ID de l'élève : "))
            matiere = input("Veuillez entrer la matière : ")
            note = float(input("Veuillez entre la note : "))
            ajouter_note(eleve_id, matiere, note)
        else:
            print("Accès refuser - Réservé au enseignant")
    elif choix == "6":
        eleve_id = int(input("ID de l'élève : "))
        moyenne_eleve(eleve_id)
    elif choix == "7":
        if role_connecte == "directeur":
            nom_classe = input("Veuillez saisir le nom de la classe : ")
            niveau = input("Veuillez saisir le niveau de la classe : ")
            ajouter_classe(nom_classe, niveau)
        else:
            print("Accès refusé - Réservé au directeur")
    elif choix == "8":
        lister_classes()
    elif choix == "9":
        if role_connecte == "directeur":
            nom = input("Veuillez entrer l'enseignant : ")
            matiere_principale = input("Veuillez entrer sa matière : ")
            ajouter_enseignant(nom, matiere_principale)
        else:
            print("Accès refuser - Réservé au directeur")
    elif choix == "10":
        lister_enseignants()
    elif choix== "11": 
        if role_connecte == "directeur":
            classe_id = int(input("ID de la classe : "))
            enseignant_id = int(input("ID de l'enseignant : "))
            assigner_titulaire(classe_id, enseignant_id)
        else:
            print("Accès refusé - Réservé au directeur")
    elif choix == "12":
        lister_eleves_avec_classe()
    elif choix == "13":
        lister_classes_avec_enseignant()
    elif choix == "14":
        lister_eleves_avec_moyenne()
    elif choix == "15":
        if role_connecte == "secretariat":
            eleve_id = int(input("ID de l'élève : "))
            date = input("Date (JJ/MM/AAAA) : ")
            type_absence = input("Type (absence/retard) : ")
            justifie = int(input("justifié ? (1=oui 0=non) : "))
            ajouter_absence(eleve_id, date, type_absence, justifie)
        else:
            print("Accès refuser - Réservé au surveillant")
    elif choix == "16":
        eleve_id = int(input("ID de l'élève : "))
        lister_absence(eleve_id)
    elif choix == "17":
        if role_connecte == "enseignant":
            eleve_id = int(input("ID de l'élève : "))
            date = input("Date (JJ/MM/AAAA) : ")
            type_sanction = input("Type : ")
            motif = input("Motif du sanction : ")
            ajouter_sanction(eleve_id, date, type_sanction, motif)
        else:
            print("Accès refuser - Réservé au enseignant")
    elif choix == "18":
        eleve_id = int(input("ID de l'élève : "))
        lister_sanction(eleve_id)
    elif choix == "19":
        if role_connecte == "directeur":
            eleve_id = int(input("ID de l'élève : "))
            montant_total = float(input("Montant total : "))
            annee_scolaire = input("Année scolaire : ")
            ajouter_frais(eleve_id, montant_total, annee_scolaire)
        else:
            print("Accès refuser - Réservé au comptable")
    elif choix == "20":
        if role_connecte == "directeur":
            frais_id = int(input("Frais ID : "))
            montant_paye = float(input("Montant à payé : "))
            date_paiement = input("Payé le : ")
            ajouter_paiement(frais_id, montant_paye, date_paiement)
        else:
            print("Accès refuser - Réservé au comptable")
    elif choix == "21":
        if role_connecte == "directeur":
            voir_situation_financiere(eleve_id)
        else:
            print("Accès refuser - Réservé au comptable")
    elif choix == "22":
        if role_connecte == "enseignant":
            eleve_id = int(input("ID de l'élève : "))
            generer_bulletin(eleve_id)
        else:
            print("Accès refuser - Réservé aux enseignant")
    elif choix == "23":
        classe_id = int(input("ID de la classe : "))
        moyenne_classe(classe_id)
    elif choix == "24":
        if role_connecte == "enseignant":
            matiere = input("Saisir la matière : ")
            moyenne_matiere(matiere)
        else:
            print("Accès refuser - Réservé aux enseignants")
    elif choix == "25":
        nom_utilisateur = input("nom utilisateur : ")
        mdp_chiffre = input("mot de passe : ")
        role = input("role : ")
        creer_compte(nom_utilisateur, mdp_chiffre, role)
    elif choix == "26":
        lister_utilisateur()
    elif choix == ".":
        break