import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    erro = 0
    for i, j in data:
        erro += ((b + w * i) - j) ** 2
    erro /= len(data)
    return erro



def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """

    deriv_theta_zero = 0
    deriv_theta_um = 0
    m = len(data)

    for x, y in data:
        deriv_theta_zero += 2 * ((w * x + b) - y)
        deriv_theta_um += 2 * x * ((w * x + b) - y)

    deriv_theta_zero /= m
    deriv_theta_um /= m

    b -= alpha * deriv_theta_zero
    w -= alpha * deriv_theta_um

    return b, w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """

    b_s = []
    w_s = []

    for i in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)

        b_s.append(b)
        w_s.append(w)

    return b_s, w_s
