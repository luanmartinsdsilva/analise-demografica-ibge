import matplotlib.pyplot as plt

# Dados do CSV convertidos
idades_convertidas = [20, 15, 32, 15, 40, 21]

# Criar histograma
plt.hist(idades_convertidas, bins=range(min(idades_convertidas), max(idades_convertidas)+2), 
         color='#66b3ff', edgecolor='black')

plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(range(min(idades_convertidas), max(idades_convertidas)+1))  # mostrar cada idade
plt.show()
