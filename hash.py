import hashlib 

mot_de_passe = "azerty123"
mot_de_passe_chiffre = hashlib.sha256(mot_de_passe.encode()).hexdigest()
print(mot_de_passe_chiffre)