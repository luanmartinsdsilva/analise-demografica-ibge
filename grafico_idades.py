import matplotlib.pyplot as plt

# Dados do script anterior
idades_convertidas = [20, 15, 32, 15, 40, 21]

# Separar menores e maiores de 18
menores18 = [i for i in idades_convertidas if i < 18]
maiores18 = [i for i in idades_convertidas if i >= 18]

# Preparar dados para o gráfico
labels = ['Menores de 18', 'Maiores ou iguais a 18']
sizes = [len(menores18), len(maiores18)]
colors = ['#ff9999','#66b3ff']

# Criar gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Idades')
plt.axis('equal')  # para deixar a pizza circular
plt.show()
