import random

def atacar(atacante, defensor):
    dano = max(0, atacante.forca + random.randint(-2, 5) - defensor.destreza)
    defensor.vida -= dano
    return dano

def iniciar_combate(jogador, inimigo):
    print(f"Você está lutando contra um {inimigo.nome}")
    while jogador.vida > 0 and inimigo.vida > 0:
        dano = atacar(jogador, inimigo)
        print(f"Você causou {dano} de dano no {inimigo.nome}.")
        if inimigo.vida <= 0:
            print(f"Você derrotou o {inimigo.nome}!")
            break
        dano = atacar(inimigo, jogador)
        print(f"O {inimigo.nome} causou {dano} de dano em você.")
        if jogador.vida <= 0:
            print("Você foi derrotado!")
            break
