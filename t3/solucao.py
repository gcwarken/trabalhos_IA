import heapq
from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __eq__(self, other):
        return isinstance(other, Nodo) and self.estado == other.estado

    def __lt__(self, other):
        return self.custo < other.custo

    def __hash__(self):
        return hash(self.estado)

def realiza_acao(estado:str, acao:str):
    match acao:
        case "acima":
            salto = -3
        case "abaixo":
            salto = 3
        case "esquerda":
            salto = -1
        case "direita":
            salto = 1
        case _:
            raise ValueError(f"Acao invalida: {acao}")

    pos_branco = estado.index('_')
    nova_pos_branco = pos_branco+salto

    estado_list = list(estado)
    estado_list[pos_branco], estado_list[nova_pos_branco] = estado_list[nova_pos_branco], estado_list[pos_branco]

    novo_estado = ''.join(estado_list)

    return novo_estado


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    set_acoes = set()

    pos_branco = estado.index('_')

    if pos_branco > 2:
        tupla = ("acima", realiza_acao(estado, "acima"))
        set_acoes.add(tupla)
    if pos_branco < 6:
        tupla = ("abaixo", realiza_acao(estado, "abaixo"))
        set_acoes.add(tupla)
    if pos_branco in {1,2,4,5,7,8}:
        tupla = ("esquerda", realiza_acao(estado, "esquerda"))
        set_acoes.add(tupla)
    if pos_branco in {0,1,3,4,6,7}:
        tupla = ("direita", realiza_acao(estado, "direita"))
        set_acoes.add(tupla)

    return set_acoes


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """

    filhos = set()
    sucessores = sucessor(nodo.estado)

    for suces in sucessores:
        filhos.add(Nodo(suces[1], nodo, suces[0], nodo.custo + 1))
    return filhos


def astar_hamming(estado:str)->list[str] | None:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    def heuristica_hamming(s: str) -> int:
        return sum(1 for i, c in enumerate(s) if c != '_' and c != "12345678_"[i])
    return astar(estado, heuristica_hamming)
    
def astar_manhattan(estado:str)->list[str] | None:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    def heuristica_manhattan(s: str) -> int:
        distancia = 0
        for i, c in enumerate(s):
            if c != '_':
                objetivo = "12345678_".index(c)
                l1, c1 = divmod(i, 3)
                l2, c2 = divmod(objetivo, 3)
                distancia += abs(l1 - l2) + abs(c1 - c2)
        return distancia
    return astar(estado, heuristica_manhattan)

def astar(estado: str, heuristica) -> list[str] | None:
    estado_objetivo = "12345678_"
    nodo_inicial = Nodo(estado, None, None, 0)
    fronteira = [(heuristica(estado), nodo_inicial)]
    explorados = set()
    custo_ate_agora = {estado: 0}

    while fronteira:
        _, atual = heapq.heappop(fronteira)

        if atual.estado == estado_objetivo:
            # Reconstrói o caminho de ações internamente
            caminho = []
            while atual.pai is not None:
                caminho.append(atual.acao)
                atual = atual.pai
            return caminho[::-1]  # Inverte para obter na ordem correta

        explorados.add(atual.estado)

        for filho in expande(atual):
            if (filho.estado not in explorados) or (filho.custo < custo_ate_agora.get(filho.estado, float('inf'))):
                custo_ate_agora[filho.estado] = filho.custo
                prioridade = filho.custo + heuristica(filho.estado)
                heapq.heappush(fronteira, (prioridade, filho))

    return None   

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
