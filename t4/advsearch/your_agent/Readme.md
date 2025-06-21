# Grupo
- Gabriel Costa Warken, cartão 179787, turma A (manhã)
- Joana Oliveira DAvila, cartão 274739, turma A (manhã)
- Diogo Brum Rivoire, cartão 344735, turma B (tarde)

# Avaliação - Tic-Tac-Toe Misere
(i) O minimax sempre ganha ou empata jogando contra o randomplayer?

- Sim, após vários testes, com variação de quem começa o minimax sempre ganhou ou empatou com o aleatório, ele nunca perdeu.

(ii) O minimax sempre empata consigo mesmo?

- Sim, o minimax sempre empatou consigo mesmo após vários testes serem feitos, não houve um caso onde um ganhou do outro.

(iii) O minimax não perde para você quando você usa a sua melhor estratégia?

- Sim, após várias tentivas, não teve um caso onde um jogador humano conseguiu ganhar do minimax.

Em conclusão, o desempenho do algoritmo está ótimo, um jogador não-inteligente quase sempre perde, e um jogador inteligente também não consegue ganhar do algoritmo.

# Heurísticas do Othello

- Heurística da Contagem de peças:

Este heurística define um agente que decide seus movimentos utilizando o algoritmo minimax com poda alfa-beta, com profundidade de busca limitada a 5, e uma heurística baseada apenas na contagem de peças. A função evaluate_count serve como função de avaliação para o minimax, retornando a diferença entre o número de peças pretas e brancas no tabuleiro atual; esse valor é positivo se o jogador tiver mais peças e negativo caso contrário, refletindo vantagem ou desvantagem numérica. A função make_move é o ponto de entrada do agente e retorna a melhor jogada calculada com base nessa heurística, tornando-o um agente que prioriza maximizar o número de peças do jogador no tabuleiro a cada rodada.

- Heurística do Valor posicional:

Esta heurística define um agente que utiliza o algoritmo minimax com profundidade 5 e poda alfa-beta para escolher movimentos, usando como função de avaliação uma heurística baseada na posição das peças no tabuleiro. A função evaluate_mask calcula o valor do estado atual somando valores posicionais pré-definidos em EVAL_TEMPLATE para as peças de cada jogador, atribuindo mais peso para posições estratégicas (como cantos e bordas), e retorna a diferença desses valores entre os jogadores, ajustada para a perspectiva do jogador atual. Assim, o agente busca maximizar o controle sobre posições vantajosas no tabuleiro, indo além da simples contagem de peças para uma avaliação mais estratégica.

- Heurística Customizada:

Este heurística define um agente que utiliza o algoritmo Minimax com profundidade 4 e uma heurística personalizada para avaliar os estados do jogo. A função evaluate_custom calcula uma pontuação combinando diversos fatores estratégicos: diferença de peças, controle dos cantos e bordas, mobilidade (número de jogadas possíveis), posicionamento com base em uma matriz de pesos (EVAL_TEMPLATE), penalidades por peças em posições perigosas, e estabilidade baseada no domínio dos cantos. A avaliação pondera essas características de forma dinâmica, ajustando sua importância conforme o progresso do jogo (fase inicial ou final). A função make_move usa essa heurística com o minimax para escolher a melhor jogada e inclui um fallback para selecionar um movimento aleatório caso nenhuma jogada seja retornada, evitando inatividade em situações críticas.

- Critérios de Parada: 

Todas as 3 Heurísticas tem como critério de parada quando o estado atual do jogo é terminal, indicando que a partida acabou, ou quando a profundidade máxima definida para a busca é atingida.

Partidas:
- Contagem de peças X Valor posicional: 37x27
- Valor posicional X Contagem de peças: 26x38
- Contagem de peças X Heurística customizada: 31x33
- Heurística customizada X Contagem de peças: 44x20
- Valor posicional X Heurística customizada: 41x21
- Heurística customizada X Valor posicional: 33x31


Heurística Selecionada para o Torneio: Heurística Customizada


