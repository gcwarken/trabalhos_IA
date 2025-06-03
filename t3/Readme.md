# Grupo
- Gabriel Costa Warken, cartão 179787, turma A (manhã)
- Joana Oliveira DAvila, cartão 274739, turma A (manhã)
- Diogo Brum Rivoire, cartão 344735, turma B (tarde)


  ## Requisitos

Para executar a implementação, é necessário Python 3.10 ou superior.

As únicas bibliotecas utilizadas são da biblioteca padrão do Python:

- `heapq`
- `typing`

Portanto, **nenhuma instalação adicional** via `pip` é necessária.

## Execução

A execução pode ser feita em um único arquivo `.py`. Exemplo:

```bash
python nome_do_arquivo.py
```

## Teste Estado inicial "2_3541687"
Para executar o teste:
```bash
python -m unittest testa_solucao.TestaSolucao.test_relatorio
```

### Execução 1
- [A* com Hamming]
    - Tempo decorrido: 0.509188 segundos
    - Nós expandidos: 17337
    - Custo da solução: 23
    - Ações: ['esquerda', 'abaixo', 'direita', 'direita', 'acima', 'esquerda', 'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita', 'direita', 'abaixo', 'esquerda', 'abaixo', 'direita', 'acima', 'esquerda', 'esquerda', 'abaixo', 'direita', 'direita']

- [A* com Manhattan]
    - Tempo decorrido: 0.156651 segundos
    - Nós expandidos: 17337
    - Custo da solução: 23
    - Ações: ['esquerda', 'abaixo', 'direita', 'direita', 'acima', 'esquerda', 'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita', 'direita', 'abaixo', 'esquerda', 'abaixo', 'direita', 'acima', 'esquerda', 'esquerda', 'abaixo', 'direita', 'direita']

--> Ran 1 test in 0.741s

### Execução 2
- [A* com Hamming]
    - Tempo decorrido: 0.307944 segundos
    - Nós expandidos: 2092
    - Custo da solução: 23
    - Ações: ['abaixo', 'abaixo', 'direita',
'acima', 'esquerda', 'abaixo', 'esquerda', 'acima', 'direita', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima', 'direita', 'acima', 'esquerda', 'abaixo', 'direita', 'abaixo', 'direita']

- [A* com Manhattan]
    - Tempo decorrido: 0.151306 segundos
    - Nós expandidos: 2092
    - Custo da solução: 23
    - Ações: ['abaixo', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima', 'direita', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima', 'direita', 'acima', 'esquerda', 'abaixo', 'direita', 'abaixo', 'direita']

--> Ran 1 test in 0.465s

 ## Observação

- O algoritmo com heurística de Manhattan foi mais eficiente que o de Hamming.
- As heurísticas implementadas são admissíveis e garantem a optimalidade da solução encontrada.



## Resultado dos  5 testes iniciais
- Tempo de execução dos testes
  - Ran 5 tests in 18.336s
  - Ran 5 tests in 18.012s
  - Ran 5 tests in 20.672s
