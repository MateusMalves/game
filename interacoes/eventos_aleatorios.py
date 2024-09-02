import random

def evento_aleatorio():
    eventos = [
        "Você encontrou uma armadilha!",
        "Um mercador aparece oferecendo itens.",
        "Você tropeçou e caiu.",
        "Um vento frio sopra pela caverna."
    ]
    return random.choice(eventos)
