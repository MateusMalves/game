import random

def gerar_evento():
    eventos = [
        "Você entrou em uma caverna escura.",
        "Um goblin aparece do nada!",
        "Você encontrou um baú de tesouro.",
        "Você ouviu um barulho estranho à sua esquerda."
    ]
    return random.choice(eventos)
