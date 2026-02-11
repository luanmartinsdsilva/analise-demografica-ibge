import csv
import matplotlib.pyplot as plt

idades = []

# 1️⃣ Ler o CSV
with open("idades.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        try:
            idade = int(linha[0])
            if idade >= 0:
                idades.append(idade)
        except:
            pass

# 2️⃣ Análises
menores = [i for i in idades if i < 18]
maiores = [i for i in idades if i >= 18]

print("Idades válidas:", idades)
print("Quantidade:", len(idades))
print("Média:", sum(idades) / len(idades))
print("Maior idade:", max(idades))
print("Menor idade:", min(idades))

# 3️⃣ Gráfico de Pizza
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.pie(
    [len(menores), len(maiores)],
    labels=["Menores de 18", "Maiores ou iguais a 18"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição por Faixa Etária")

# 4️⃣ Histograma
plt.subplot(1, 2, 2)
plt.hist(
    idades,
    bins=range(min(idades), max(idades) + 2),
    edgecolor="black"
)
plt.title("Histograma das Idades")
plt.xlabel("Idade")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.show()
