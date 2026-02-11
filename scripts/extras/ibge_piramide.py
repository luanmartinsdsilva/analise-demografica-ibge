import csv
import matplotlib.pyplot as plt

faixas = []
populacoes = []

with open("ibge_idades.csv", encoding="utf-8-sig") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    linhas = list(leitor)

    # Cabeçalho e dados
    cabecalho = linhas[4][1:]
    dados = linhas[5][1:]

    for faixa, valor in zip(cabecalho, dados):
        faixas.append(faixa.replace('"', ''))
        populacoes.append(int(valor.replace('"', '')))

# Inverte para ficar estilo pirâmide (dos mais jovens para os mais velhos)
faixas = faixas[::-1]
populacoes = populacoes[::-1]

plt.figure()
plt.barh(faixas, populacoes)
plt.title("Pirâmide Etária do Brasil – IBGE (PNAD Contínua)")
plt.xlabel("População (mil pessoas)")
plt.ylabel("Grupo de idade")
plt.tight_layout()
plt.show()
