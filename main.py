from eleves import ajouter_eleve, lister_eleve, supprimer_eleve, modifier_eleve, lister_eleves_avec_classe, lister_eleves_avec_moyenne
from notes import ajouter_note, moyenne_eleve
from classes import ajouter_classe, lister_classes, assigner_titulaire, lister_classes_avec_enseignant
from enseignants import ajouter_enseignant, lister_enseignants
from absences import ajouter_absence, lister_absence
from sanctions import ajouter_sanction, lister_sanction

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
    print(".. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Veuillez entrer votre nom : ")
        age = int(input("veuillez entrer votre age : "))
        classe_id = int(input("ID de la classe : "))
        ajouter_eleve(nom, age, classe_id)
    elif choix == "2":
        lister_eleve()
    elif choix == "3":
        id_a_supprimer = int(input("ID de l'élève a supprimer : "))
        supprimer_eleve(id_a_supprimer)
    elif choix == "4":
        id_a_modifier = int(input("ID de l'élève a modifier : "))
        nouveau_nom = input("Veuillez saisir un nouveau nom : ")
        nouvel_age = input("Veuillez saisir un nouvel age : ")
        nouvelle_classe = int(input("ID de la classe : "))
        modifier_eleve(id_a_modifier, nouveau_nom, nouvel_age, nouvelle_classe)
    elif choix == "5":
        eleve_id = int(input("ID de l'élève : "))
        matiere = input("Veuillez entrer la matière : ")
        note = float(input("Veuillez entre la note : "))
        ajouter_note(eleve_id, matiere, note)
    elif choix == "6":
        eleve_id = int(input("ID de l'élève : "))
        moyenne_eleve(eleve_id)
    elif choix == "7":
        nom_classe = input("Veuillez entrer le nom de la classe : ")
        niveau = input("Veuillez saisir le niveau : ")
        ajouter_classe(nom_classe, niveau)
    elif choix == "8":
        lister_classes()
    elif choix == "9":
        nom = input("Veuillez entrer l'enseignant : ")
        matiere_principale = input("Veuillez entrer sa matière : ")
        ajouter_enseignant(nom, matiere_principale)
    elif choix == "10":
        lister_enseignants()
    elif choix== "11": 
        classe_id = int(input("ID de la classe : "))
        enseignant_id = int(input("ID de l'enseignant : "))
        assigner_titulaire(classe_id, enseignant_id)
    elif choix == "12":
        lister_eleves_avec_classe()
    elif choix == "13":
        lister_classes_avec_enseignant()
    elif choix == "14":
        lister_eleves_avec_moyenne()
    elif choix == "15":
        eleve_id = int(input("ID de l'élève : "))
        date = input("Date (JJ/MM/AAAA) : ")
        type_absence = input("Type (absence/retard) : ")
        justifie = int(input("justifié ? (1=oui 0=non) : "))
        ajouter_absence(eleve_id, date, type_absence, justifie)
    elif choix == "16":
        eleve_id = int(input("ID de l'élève : "))
        lister_absence(eleve_id)
    elif choix == "17":
        eleve_id = int(input("ID de l'élève : "))
        date = input("Date (JJ/MM/AAAA) : ")
        type_sanction = input("Type : ")
        motif = input("Motif du sanction : ")
        ajouter_sanction(eleve_id, date, type_sanction, motif)
    elif choix == "18":
        eleve_id = int(input("ID de l'élève : "))
        lister_sanction(eleve_id)
    elif choix == ".":
        break