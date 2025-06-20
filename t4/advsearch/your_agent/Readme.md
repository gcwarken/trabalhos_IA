# Grupo
- Gabriel Costa Warken, cartão 179787, turma A (manhã)
- Joana Oliveira DAvila, cartão 274739, turma A (manhã)
- Diogo Brum Rivoire, cartão 344735, turma B (tarde)

# Avaliação - Misere
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

- Heurística Custom:

Este heurística implementa um agente que escolhe seus movimentos utilizando o algoritmo minimax com poda alfa-beta, explorando jogadas futuras até uma profundidade limitada e avaliando os estados com uma heurística
personalizada. A função de avaliação estima a qualidade de um estado considerando múltiplos fatores estratégicos: diferença no número de peças, controle de cantos e bordas (posições estáveis), mobilidade (quantidade de jogadas disponíveis) e um valor posicional baseado em uma matriz de pesos (EVAL_TEMPLATE). Esses fatores são combinados com pesos que variam conforme a fase do jogo (início, meio ou fim), permitindo que o agente adapte sua estratégia ao longo da partida e escolha movimentos mais vantajosos.


Partidas:
Contagem de peças X Valor posicional: 37x27
Valor posicional X Contagem de peças: 4024
Contagem de peças X Heurística customizada: 39x25
Heurística customizada X Contagem de peças: 25x39
Valor posicional X Heurística customizada: 38x26
Heurística customizada X Valor posicional: 33x31


Heurística Seleciona: Heurística Custom


