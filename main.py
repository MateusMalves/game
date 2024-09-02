from personagens.ficha_personagem import Personagem
from mestre_jogo.mestre import Mestre
from combate.sistema_combate import iniciar_combate
from combate.inimigos import Inimigo
from interacoes.eventos_aleatorios import evento_aleatorio
from interacoes.interface_usuario import obter_acao, exibir_resultado
from dados.dados import rolar_dado

# Criar personagem do jogador
jogador = Personagem(nome="Aragorn", classe="Guerreiro", forca=18, destreza=14, inteligencia=12, vida=100)
jogador.exibir_ficha()

# Iniciar o Mestre de Jogo
mestre = Mestre()
mestre.iniciar_jogo()

# Exemplo de combate
inimigo = Inimigo(nome="Goblin", forca=8, destreza=6, vida=30)
iniciar_combate(jogador, inimigo)

# Exemplo de evento aleatório
evento = evento_aleatorio()
exibir_resultado(evento)
