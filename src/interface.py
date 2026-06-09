# src/interface.py
import pygame

def desenhar_texto(superficie, texto, fonte, cor, x, y):
    """Renderiza e centraliza um texto na tela."""
    img_texto = fonte.render(texto, True, cor)
    retangulo = img_texto.get_rect(center=(x, y))
    superficie.blit(img_texto, retangulo)

def desenhar_botao(superficie, fonte, texto, x, y, largura, altura, cor_normal, cor_hover, pos_mouse):
    """Desenha um botão interativo que muda de cor quando o mouse passa por cima."""
    retangulo_botao = pygame.Rect(x, y, largura, altura)
    
    # Verifica se a posição do mouse colide com o retângulo do botão
    if retangulo_botao.collidepoint(pos_mouse):
        pygame.draw.rect(superficie, cor_hover, retangulo_botao, border_radius=10)
    else:
        pygame.draw.rect(superficie, cor_normal, retangulo_botao, border_radius=10)
        
    # Desenha o texto bem no centro do botão
    desenhar_texto(superficie, texto, fonte, (255, 255, 255), x + largura // 2, y + altura // 2)
    
    return retangulo_botao