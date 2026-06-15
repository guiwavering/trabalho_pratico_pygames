# Guess the Movie 🎬

Este é um jogo de trivia (perguntas e respostas) onde o jogador precisa adivinhar qual filme está na imagem borrada. O projeto foi desenvolvido em Python utilizando a biblioteca Pygame, como requisito prático da disciplina.

## 🎯 Requisitos Implementados

- **Indicadores de Desempenho e Progresso:** O jogador inicia com **3 vidas**. Cada acerto soma pontos (máximo de 100 por filme, reduzindo 25 por cada dica solicitada). Há um contador de progresso na tela indicando a rodada atual (ex: Filme 1/10).
- **Condições de Fim de Jogo:** - **Vitória:** Acertar os filmes e chegar ao final da lista do banco de dados.
  - **Derrota:** Errar respostas até as vidas chegarem a zero.
- **Estruturas de Dados e Arquivos:** - **Leitura:** Os filmes, caminhos das imagens e dicas são carregados a partir de um arquivo `assets/filmes.json` (Lista de Dicionários).
  - **Escrita:** Ao encerrar a partida (vitória ou derrota), a pontuação final do jogador é salva (append) no arquivo `ranking.txt` na raiz do projeto.
- **Interação:** Sistema de digitação na tela e clique em botões para solicitar dicas, o que diminui dinamicamente o *blur* (desfoque) da imagem original.

## 📂 Estrutura do Projeto

* `assets/`: Contém as imagens `.jpg` e o banco de dados `filmes.json`.
* `src/`: Contém os módulos do jogo (`config.py`, `interface.py` e `logica.py`).
* `tests/`: Contém os testes automatizados da lógica do jogo.
* `main.py`: Arquivo principal contendo o loop do jogo.

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado na máquina.
2. Instale o Pygame executando no terminal:
   `pip install pygame`
3. Execute o jogo a partir da raiz do projeto:
   `python main.py`

## 🧪 Como Rodar os Testes

Para executar a primeira versão dos testes de unidade, abra o terminal na raiz do projeto e digite:
`python -m unittest tests/tests_logica.py`