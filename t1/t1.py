import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import alegrete

dataset = np.genfromtxt('alegrete.csv',delimiter = ',')
dataset=np.array(dataset)

#Gráfico dos dados
plt.figure(figsize=(6, 2))
plt.scatter(dataset[:,0], dataset[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('dataset Alegrete.csv')
plt.savefig('plotDados.png')

"""
### Execucao da regressao linear e calculo do EQM por epoca/iteracao

Considere o parâmetro b o coeficiente linear (theta_0, visto em aula) e w o coeficiente angular (theta_1, visto em aula).
"""

b_history, w_history = alegrete.fit(
    dataset,
    b=1,
    w=0.7,
    alpha=0.01,
    num_iterations=1000
)

# valores finais de theta0 e theta1
final_b, final_w = b_history[-1], w_history[-1]

mse_list = [alegrete.compute_mse(b, w, dataset) for b, w in zip(b_history, w_history)]
print(f"EQM final: {mse_list[-1]}")

plt.cla()
plt.plot(mse_list)
plt.xlabel('Epoca/iteracao')
plt.ylabel('EQM')
plt.savefig('eqm.png')

"""
### Plot da curva final"""

#Imprimir parâmetros otimizados
print (f'Curva encontrada: {final_w}*x + {final_b}')

#plota os dados
plt.figure(figsize=(4, 2))
plt.scatter(dataset[:,0], dataset[:,1])

# plota a curva de ajuste
pred = final_w*dataset[:,0] + final_b
plt.plot(dataset[:,0], pred, c='r')
plt.savefig('curvaFinal.png')
