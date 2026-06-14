from eleves import ajouter_eleve, lister_eleve, supprimer_eleve, modifier_eleve
from notes import ajouter_note, moyenne_eleve

while True:
    print("1. Ajouter un élève")
    print("2. Lister les élèves")
    print("3. Supprimer un élève")
    print("4. Modifier l'élève")
    print("5. Ajouter une note")
    print("6. Voir la moyenne d'un élève")
    print("7. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Veuillez entrer votre nom : ")
        age = int(input("veuillez entrer votre age : "))
        classe = input("Veuiller entre votre classe : ")
        ajouter_eleve(nom, age, classe)
    elif choix == "2":
        lister_eleve()
    elif choix == "3":
        id_a_supprimer = int(input("ID de l'élève a supprimer : "))
        supprimer_eleve(id_a_supprimer)
    elif choix == "4":
        id_a_modifier = int(input("ID de l'élève a modifier : "))
        nouveau_nom = input("Veuillez saisir un nouveau nom : ")
        nouvel_age = input("Veuillez saisir un nouvel age : ")
        nouvelle_classe = input("Veuillez saisir une nouvelle classe : ")
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
        break
