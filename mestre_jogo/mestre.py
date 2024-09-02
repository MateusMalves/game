from narrativa import gerar_evento

class Mestre:
    def __init__(self):
        self.historia = []

    def iniciar_jogo(self):
        print("Bem-vindo à aventura!")
        while True:
            evento = gerar_evento()
            self.historia.append(evento)
            print(evento)
            acao = input("Qual é a sua ação? (explorar, atacar, fugir): ").lower()
            if acao == "fugir":
                print("Você fugiu da aventura!")
                break
            # Outras ações podem ser implementadas aqui
