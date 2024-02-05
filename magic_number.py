formule_de_politesse = "Bonjour "

def saluer(nom: str) -> str:
    return formule_de_politesse + nom

print(saluer("Alice"))  # Affiche : Bonjour Alice