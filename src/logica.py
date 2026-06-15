# src/logica.py
import json

def carregar_filmes(caminho):
    """Lê o arquivo JSON e retorna a lista de filmes."""
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_ranking(pontuacao):
    """Salva a pontuação final no arquivo ranking.txt."""
    with open("ranking.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(f"Pontuação alcançada: {pontuacao}\n")

def verificar_resposta(palpite, correto):
    """Compara o palpite com a resposta certa ignorando maiúsculas e espaços."""
    return palpite.strip().lower() == correto.strip().lower()

def calcular_pontos(dicas_usadas):
    """Calcula os pontos baseados nas dicas (100 base, -25 por dica)."""
    return max(0, 100 - (dicas_usadas * 25))