import matplotlib.pyplot as plt
import numpy as np

# Gerar dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criar gráfico
plt.plot(x, y)
plt.title("Exemplo de Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
