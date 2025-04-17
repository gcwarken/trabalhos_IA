import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import alegrete

def carregaDataset():
    data = np.genfromtxt('alegrete.csv',delimiter = ',')
    data=np.array(data)
    return data

def plotDados(titulo, dataset):
    plt.figure(figsize=(6, 2))
    plt.scatter(dataset[:,0], dataset[:,1])
    plt.xlabel('x')
    plt.title(titulo)
    plt.ylabel('y')
    plt.savefig('plotDados.png')

def eqm(dataset):
    mse_list = [alegrete.compute_mse(b, w, dataset) for b, w in zip(b_history, w_history)]
    print(f"EQM final: {mse_list[-1]}")
    plt.plot(mse_list)
    plt.xlabel('Epoca/iteracao')
    plt.ylabel('EQM')
    plt.savefig('eqm.png')

def curvaFinal(dataset):
    #Imprimir parâmetros otimizados
    print (f'Curva encontrada: {final_w}*x + {final_b}')

    #plota os dados
    plt.figure(figsize=(4, 2))
    plt.scatter(dataset[:,0], dataset[:,1])
plot
    # plota a curva de ajuste
    pred = final_w*dataset[:,0] + final_b
    plt.plot(dataset[:,0], pred, c='r')
    plt.savefig('curvaFinal.png')

def descida():
    fig = plt.figure(figsize=(4, 2))
    ax = fig.add_subplot(111)

    # conjunto de dados
    ax.scatter(dataset[:,0], dataset[:,1])

    # linha com os valores iniciais dos parametros
    pred = w_history[0]*dataset[:,0] + b_history[0]
    line, = ax.plot(dataset[:,0], pred, '-',c='r')

    # funcao que atualiza a linha a cada passo
#    def animate(i):
#        pred = w_history[i] * dataset[:,0] + b_history[i]
#        line.set_ydata(pred)
#        return line,
#
#    # mude interval para trocar a velocidade da animacao
#    ani = animation.FuncAnimation(fig, animate, frames=len(b_history), interval=20, save_count=50)
#    HTML(ani.to_jshtml())


####################################################################################################

dataset = carregaDataset()
plotDados("Base alegrete.csv", dataset)

b_history, w_history = alegrete.fit(
    dataset, b=0, w=0,
    alpha=0.1, num_iterations=100
)

# valores finais de theta0 e theta1
final_b, final_w = b_history[-1], w_history[-1]

eqm()
curvaFinal()
