# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Guess the Movie

## 2. Integrantes do grupo

- Nome 1: Guilherme Henrique Ribeiro Silva

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> jogo de perguntas e respostas (Trivia / Quiz)

## 4. Descrição geral do jogo

O jogo apresentará ao jogador uma imagem borrada na tela, que corresponde a uma cena ou pôster de um filme famoso. O jogador controla a navegação por botões na tela (usando o mouse) ou atalhos no teclado para solicitar dicas textuais ou digitar/selecionar o nome do filme correto. O objetivo é adivinhar o filme consumindo o mínimo de dicas possível. À medida que o jogador erra ou pede dicas, o nível de desfoque (blur) da imagem diminui gradativamente, facilitando a visualização, porém reduzindo a pontuação máxima que ele pode obter naquela rodada.

## 5. Objetivo do jogador

> Responder corretamente quais são os filmes exibidos nas fotos, acumulando a maior pontuação possível ao final de uma rodada de perguntas e sobrevivendo com as vidas disponíveis.

## 6. Regras principais

- O jogador inicia a partida com 3 vidas e uma pontuação zerada.
- Cada filme começa com a imagem 100% borrada e uma pontuação máxima de 100 pontos configurada para aquela rodada.
- O jogador pode revelar até 2 dicas textuais por filme; cada dica solicitada reduz a pontuação máxima da rodada em 25 pontos.
- Cada palpite incorreto remove 1 vida do jogador e reduz ligeiramente o desfoque da imagem.
- Acertar o filme soma os pontos restantes da rodada à pontuação global do jogador e passa para o próximo filme.
- A partida é encerrada se o jogador perder todas as 3 vidas ou se conseguir responder com sucesso todo o banco de dados de filmes da partida.

## 7. Condição de vitória

> O jogador vence ao responder corretamente a lista de filmes pré-definida para a sessão (ex: um bloco de 10 filmes) antes que suas vidas cheguem a zero.

## 8. Condição de derrota ou encerramento

> A partida termina em derrota imediatamente quando as vidas do jogador chegam a zero devido a palpites errados.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

> O jogador atua através de uma interface gráfica estática e dinâmica de quiz. Ele interage utilizando o ponteiro do mouse para clicar em caixas de opções (múltipla escolha) ou utilizando o teclado para digitar o nome do filme em um campo de texto.

## Obstáculos, inimigos ou desafios

> O principal desafio do jogo é o fator visual limitante (imagem desfocada) combinado com o limite de tempo por rodada (opcional) e o banco de questões que exige conhecimento de cinema por parte do usuário.

## Itens, alvos ou objetos de interação

> Botões clicáveis na interface (Ex: "Pedir Dica", "Confirmar Resposta", "Pular"), campo de inserção de texto e caixas de exibição contendo as dicas liberadas.

## Pontuação, vidas, tempo ou progresso

> Exibição persistente no topo da tela indicando a pontuação atual do jogador, quantidade de vidas restantes (representadas por ícones de corações ou rolos de filme) e uma barra de progresso indicando em qual filme ele está (ex: 3/10).

## 10. Controles previstos

- Clique do Botão Esquerdo do Mouse: Interagir com os botões da interface, selecionar alternativas e focar no campo de digitação.
- Teclas Alfanuméricas (A-Z) e Espaço: Utilizados para digitar o nome do filme na caixa de texto (caso não seja múltipla escolha).
- Tecla Enter: Confirmar e enviar o palpite digitado.
- Tecla ESC: Pausar ou retornar ao menu principal.

## 11. Organização inicial do código

Organização planejada:

> - `main.py`: Ponto de entrada do programa, inicializa o Pygame e gerencia a alternância entre as telas (Menu, Jogo, Game Over, Vitória).
> - `src/config.py`: Armazena constantes do sistema (resolução da tela, definição de cores em RGB, caminhos de pastas e fontes).
> - `src/gerenciador.py`: Controla a lógica do quiz (computação de vidas, cálculo de pontuação, verificação se a resposta digitada está correta).
> - `src/interface.py`: Responsável por desenhar os elementos visuais na tela (botões, caixas de texto, textos e renderização das imagens).
> - `src/banco_dados.py`: Responsável por ler o arquivo de dados (JSON ou TXT) contendo os nomes dos filmes, caminhos das imagens e suas respectivas dicas.

## 12. Recursos externos previstos

Recursos previstos:

> - Imagens de cenas de filmes coletadas da internet em formato JPG/PNG.
> - Efeitos sonoros gratuitos (som de clique, som de acerto e som de erro) obtidos em plataformas como Freesound.
> - Fonte TrueType (.ttf) personalizada obtida no Google Fonts para estilizar a interface do jogo.
> - Arquivo de texto estruturado (JSON) montado manualmente para servir de base de dados para as perguntas.

## 13. Principais dificuldades esperadas

- Dificuldade 1: Processar e aplicar o efeito de desfoque (blur) nas imagens de forma eficiente em tempo de execução usando o Pygame ou a biblioteca PIL (Pillow).
- Dificuldade 2: Implementar um sistema amigável e funcional de caixa de digitação de texto (Input Box) nativo no Pygame para o jogador digitar as respostas.
- Dificuldade 3: Tratar pequenas variações na digitação do jogador (ex: ignorar letras maiúsculas/minúsculas e acentos) para evitar que ele perca vidas por erros de digitação de termos corretos.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo consistirá em uma tela que exibe uma imagem estática esticada (com efeito de desfoque simulado por versões previamente editadas da imagem), um sistema de múltipla escolha com 4 botões de opções de nomes de filmes, controle de pontuação simples, decréscimo de vidas por erro e telas textuais simples de "Vitória" e "Game Over".

## 15. Possíveis melhorias, caso haja tempo

- Melhoria 1: Implementar sistema de input de texto livre com algoritmo de aproximação de string (métrica de Levenshtein) para aceitar respostas com pequenos erros de digitação.
- Melhoria 2: Adicionar um cronômetro regressivo por rodada para aumentar a urgência e a dificuldade do jogo.
- Melhoria 3: Criar um sistema de Ranking (Leaderboard) persistente gravado em arquivo local para salvar as maiores pontuações já obtidas.