# Grupo
- Gabriel Costa Warken, cartão 179787, turma A (manhã)
- Joana Oliveira DAvila, cartão 274739, turma A (manhã)
- Diogo Brum Rivoire, cartão 344735, turma B (tarde)

  
# Parte 1
### Regressão Linear
Valores iniciais de b, w, valores de alpha e num_iterations que resultem na melhor execução da sua regressão linear.

###  Erro quadrático médio obtido na sua implementação da regressão linear.


# Parte 2
### Análise dos datasets 
(quantas classes, quantas amostras, qual o tamanho das imagens (altura x largura x canais de cor))

| Dataset        | Classes | Quantas Amostras | Tamanho das Imagens     |
|----------------|---------|------------------|--------------------------|
| Fashion-MNIST  | 10      | 60000            | 28 x 28 x 1 (escala de cinza) |
| MNIST          | 10      | 60000            | 28 x 28 x 1 (escala de cinza) |
| CIFAR-10       | 10      | 60000            | 32 x 32 x 3 (RGB)             |
| CIFAR-100      | 100     | 60000          | 32 x 32 x 3 (RGB)             |

### Suas conclusões considerando as questões do Exercício 1.
- Dataset CIFAR-10 : é mais fácil de executar, por já estar preenchido no código e o tempo de execução é mais rapído. 
- Dataset MNIST : tempo de execução foi grande, porém menor do que CIFAR-100 

### Suas conclusões considerando as questões do Exercício 2.
MNIST e Fashion MNIST possuem imagens pequenas (28x28) e apenas um canal (preto e branco), além de terem o mesmo número de classes (10) e uma boa quantidade de amostras por classe (6000). Como esperado, a acurácia no MNIST foi extremamente alta, e no Fashion MNIST também foi bastante satisfatória, mesmo sendo um conjunto mais desafiador. A simplicidade das imagens e a baixa dimensionalidade favorecem redes menores. CIFAR-10 e CIFAR-100 apresentam imagens coloridas (32x32x3) e, embora tenham o mesmo número total de amostras (60000), a distribuição por classe no CIFAR-100 é muito menor (600 imagens por classe contra 6000 no CIFAR-10), o que torna a generalização mais difícil.
# Extra 
Documentação do(s) extra(s) implementado(s), se aplicável.
