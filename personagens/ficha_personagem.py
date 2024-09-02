class Personagem:
    def __init__(self, nome, classe, forca, destreza, inteligencia, vida):
        self.nome = nome
        self.classe = classe
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.vida = vida
        self.inventario = []

    def exibir_ficha(self):
        ficha = f"""
        Nome: {self.nome}
        Classe: {self.classe}
        Força: {self.forca}
        Destreza: {self.destreza}
        Inteligência: {self.inteligencia}
        Vida: {self.vida}
        Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}
        """
        print(ficha)
    