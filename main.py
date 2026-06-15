# main.py
import pygame
import sys
import os

# Importando nossas configurações, interface e lógica (certifique-se de que src/logica.py existe)
from src.config import LARGURA, ALTURA, FPS, PRETO, BRANCO, AZUL, AZUL_CLARO
from src.interface import desenhar_texto, desenhar_botao
from src.logica import carregar_filmes, salvar_ranking, verificar_resposta, calcular_pontos

def iniciar_jogo():
    # 1. Inicialização do Pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Guess the Movie - Versão Final")
    relogio = pygame.time.Clock()
    
    # Fontes
    fonte_titulo = pygame.font.SysFont("Arial", 40, bold=True)
    fonte_normal = pygame.font.SysFont("Arial", 24)
    fonte_dica = pygame.font.SysFont("Arial", 20, italic=True)
    
    # 2. Carregar Dados do JSON
    caminho_json = os.path.join("assets", "filmes.json")
    filmes = carregar_filmes(caminho_json)
    
    if not filmes:
        print("Erro: O arquivo 'filmes.json' não foi encontrado na pasta 'assets'!")
        sys.exit()

    # Variáveis de Estado do Jogo
    estado = "JOGANDO" # Pode ser JOGANDO, VITORIA ou DERROTA
    indice_filme = 0
    vidas = 3
    pontuacao_total = 0
    dicas_pedidas = 0
    texto_digitado = ""
    
    # Função auxiliar para carregar a imagem e aplicar desfoque
    def carregar_imagem(indice):
        try:
            caminho_img = filmes[indice]["imagem"]
            img = pygame.image.load(caminho_img)
            return pygame.transform.scale(img, (400, 250))
        except FileNotFoundError:
            s = pygame.Surface((400, 250))
            s.fill((100, 100, 100))
            return s

    imagem_original = carregar_imagem(indice_filme)

    # 3. Loop Principal
    rodando = True
    while rodando:
        pos_mouse = pygame.mouse.get_pos()
        
        # 4. Tratamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if estado == "JOGANDO":
                # Interação com o Mouse
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    rect_botao_dica = pygame.Rect(LARGURA // 2 - 210, 360, 150, 40)
                    rect_botao_enviar = pygame.Rect(LARGURA // 2 + 60, 360, 150, 40)
                    
                    # Clicou em Pedir Dica
                    if rect_botao_dica.collidepoint(pos_mouse) and dicas_pedidas < len(filmes[indice_filme]["dicas"]):
                        dicas_pedidas += 1
                        
                    # Clicou em Enviar Resposta
                    elif rect_botao_enviar.collidepoint(pos_mouse) and texto_digitado.strip() != "":
                        if verificar_resposta(texto_digitado, filmes[indice_filme]["titulo"]):
                            # Acertou!
                            pontuacao_total += calcular_pontos(dicas_pedidas)
                            indice_filme += 1
                            dicas_pedidas = 0
                            texto_digitado = ""
                            
                            if indice_filme >= len(filmes):
                                estado = "VITORIA"
                                salvar_ranking(pontuacao_total)
                            else:
                                imagem_original = carregar_imagem(indice_filme)
                        else:
                            # Errou!
                            vidas -= 1
                            texto_digitado = ""
                            if vidas <= 0:
                                estado = "DERROTA"
                                salvar_ranking(pontuacao_total)

                # Interação com o Teclado (Digitação)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                        texto_digitado = texto_digitado[:-1]
                    elif evento.key == pygame.K_RETURN:
                        pass # Ignora o enter, o jogador deve clicar em "Enviar"
                    else:
                        # Limita o tamanho do texto para não sair da caixa
                        if len(texto_digitado) < 30:
                            texto_digitado += evento.unicode

        # 5. Atualização da Tela
        tela.fill(PRETO)
        
        if estado == "JOGANDO":
            # HUD (Vidas, Pontos e Progresso)
            desenhar_texto(tela, f"Vidas: {vidas}", fonte_normal, (255, 50, 50), 60, 30)
            desenhar_texto(tela, f"Pontos: {pontuacao_total}", fonte_normal, BRANCO, LARGURA - 80, 30)
            desenhar_texto(tela, f"Filme {indice_filme + 1}/{len(filmes)}", fonte_normal, BRANCO, LARGURA // 2, 30)
            
            # Efeito de Desfoque (Pixelização)
            # Quanto mais dicas pedidas, menor o fator de desfoque (mais nítido fica)
            fator_desfoque = max(1, 25 - (dicas_pedidas * 10))
            if fator_desfoque > 1:
                img_pequena = pygame.transform.scale(imagem_original, (400 // fator_desfoque, 250 // fator_desfoque))
                img_borrada = pygame.transform.scale(img_pequena, (400, 250))
            else:
                img_borrada = imagem_original
                
            rect_imagem = img_borrada.get_rect(center=(LARGURA // 2, 180))
            tela.blit(img_borrada, rect_imagem)
            
            # Caixa de Digitação Visual
            pygame.draw.rect(tela, BRANCO, (LARGURA // 2 - 200, 315, 400, 35), border_radius=5)
            desenhar_texto(tela, texto_digitado + "|", fonte_normal, PRETO, LARGURA // 2, 332)
            
            # Botões
            desenhar_botao(tela, fonte_normal, f"Dica ({len(filmes[indice_filme]['dicas']) - dicas_pedidas})", LARGURA // 2 - 210, 360, 150, 40, AZUL, AZUL_CLARO, pos_mouse)
            desenhar_botao(tela, fonte_normal, "Enviar", LARGURA // 2 + 60, 360, 150, 40, (0, 150, 0), (0, 200, 0), pos_mouse)
            
            # Exibir as dicas
            y_dica = 430
            for i in range(dicas_pedidas):
                desenhar_texto(tela, filmes[indice_filme]["dicas"][i], fonte_dica, BRANCO, LARGURA // 2, y_dica)
                y_dica += 30

        elif estado == "VITORIA":
            desenhar_texto(tela, "VOCE VENCEU!", fonte_titulo, (0, 255, 0), LARGURA // 2, ALTURA // 2 - 50)
            desenhar_texto(tela, f"Pontuação Final: {pontuacao_total}", fonte_normal, BRANCO, LARGURA // 2, ALTURA // 2 + 20)
            
        elif estado == "DERROTA":
            ddesenhar_texto(tela, "GAME OVER", fonte_titulo, (255, 0, 0), LARGURA // 2, ALTURA // 2 - 50)
            desenhar_texto(tela, f"Pontuação Alcançada: {pontuacao_total}", fonte_normal, BRANCO, LARGURA // 2, ALTURA // 2 + 20)

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_jogo()