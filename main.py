# main.py
import pygame
import sys
import os

# Importando nossas configurações e funções
from src.config import LARGURA, ALTURA, FPS, PRETO, BRANCO, AZUL, AZUL_CLARO
from src.interface import desenhar_texto, desenhar_botao

def iniciar_jogo():
    # 1. Inicialização do Pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Guess the Movie - Protótipo")
    relogio = pygame.time.Clock()
    
    # Fontes
    fonte_titulo = pygame.font.SysFont("Arial", 40, bold=True)
    fonte_normal = pygame.font.SysFont("Arial", 24)
    fonte_dica = pygame.font.SysFont("Arial", 20, italic=True)
    
    # 2. Dados do Filme (Imagem e Dicas)
    # Tenta carregar a imagem, se não achar, cria um quadrado cinza temporário
    try:
        # Pega o caminho correto independente do seu sistema operacional
        caminho_imagem = os.path.join("assets", "filme1.jpg") 
        imagem_filme = pygame.image.load(caminho_imagem)
        # Redimensiona a imagem para 400x250 pixels
        imagem_filme = pygame.transform.scale(imagem_filme, (400, 250))
    except FileNotFoundError:
        print("Aviso: Imagem 'assets/filme1.jpg' não encontrada. Usando bloco cinza.")
        imagem_filme = pygame.Surface((400, 250))
        imagem_filme.fill((100, 100, 100))

    dicas_do_filme = [
        "Dica 1: É um filme de ficção científica.",
        "Dica 2: Possui sabres de luz e viagens espaciais."
    ]
    
    # Variáveis de controle do jogo
    dicas_pedidas = 0
    
    # 3. Loop Principal
    rodando = True
    while rodando:
        pos_mouse = pygame.mouse.get_pos()
        
        # 4. Tratamento de Eventos (Controles)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rect_botao_dica = pygame.Rect(LARGURA // 2 - 100, 380, 200, 50)
                
                # Só aumenta o contador de dicas se ainda houver dicas disponíveis
                if rect_botao_dica.collidepoint(pos_mouse) and dicas_pedidas < len(dicas_do_filme):
                    dicas_pedidas += 1

        # 5. Atualização da Tela (Renderização)
        tela.fill(PRETO)
        
        # Título
        desenhar_texto(tela, "Guess the Movie", fonte_titulo, BRANCO, LARGURA // 2, 50)
        
        # Desenhar a Imagem do Filme centralizada
        retangulo_imagem = imagem_filme.get_rect(center=(LARGURA // 2, 220))
        tela.blit(imagem_filme, retangulo_imagem)
        
        # Botão de Pedir Dica (desaparece ou muda se as dicas acabarem)
        if dicas_pedidas < len(dicas_do_filme):
            desenhar_botao(
                tela, fonte_normal, f"Pedir Dica ({len(dicas_do_filme) - dicas_pedidas} restam)", 
                LARGURA // 2 - 100, 380, 200, 50, 
                AZUL, AZUL_CLARO, pos_mouse
            )
        else:
            desenhar_texto(tela, "Sem mais dicas disponíveis!", fonte_normal, BRANCO, LARGURA // 2, 405)

        # Exibir as dicas na tela conforme foram pedidas
        posicao_y_dica = 460
        for i in range(dicas_pedidas):
            desenhar_texto(tela, dicas_do_filme[i], fonte_dica, BRANCO, LARGURA // 2, posicao_y_dica)
            posicao_y_dica += 30 # Desce 30 pixels para desenhar a próxima dica embaixo

        # Atualiza o display e controla o FPS
        pygame.display.flip()
        relogio.tick(FPS)

    # Encerramento seguro
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_jogo()