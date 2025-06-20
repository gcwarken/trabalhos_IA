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

- Heurística Custom:

Este heurística implementa um agente que escolhe seus movimentos utilizando o algoritmo minimax com poda alfa-beta, explorando jogadas futuras até uma profundidade limitada e avaliando os estados com uma heurística personalizada. A função de avaliação estima a qualidade de um estado considerando múltiplos fatores estratégicos: diferença no número de peças, controle de cantos e bordas (posições estáveis), mobilidade (quantidade de jogadas disponíveis) e um valor posicional baseado em uma matriz de pesos (EVAL_TEMPLATE). Esses fatores são combinados com pesos que variam conforme a fase do jogo (início, meio ou fim), permitindo que o agente adapte sua estratégia ao longo da partida e escolha movimentos mais vantajosos.









