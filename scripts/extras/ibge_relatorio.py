import csv

faixas = []
populacoes = []

with open("ibge_idades.csv", encoding="utf-8-sig") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    linhas = list(leitor)

    cabecalho = linhas[4][1:]
    dados = linhas[5][1:]

    for faixa, valor in zip(cabecalho, dados):
        faixas.append(faixa.replace('"', ''))
        populacoes.append(int(valor.replace('"', '')))

total = sum(populacoes)

maior_faixa = faixas[populacoes.index(max(populacoes))]
menor_faixa = faixas[populacoes.index(min(populacoes))]

with open("relatorio_ibge.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("RELATÓRIO DEMOGRÁFICO – IBGE (PNAD Contínua)\n\n")
    relatorio.write(f"População total analisada: {total} mil pessoas\n\n")
    relatorio.write(f"Faixa etária mais numerosa: {maior_faixa}\n")
    relatorio.write(f"Faixa etária menos numerosa: {menor_faixa}\n\n")
    relatorio.write("Distribuição por grupo de idade:\n")

    for faixa, pop in zip(faixas, populacoes):
        relatorio.write(f"- {faixa}: {pop} mil pessoas\n")

print("✅ Relatório gerado com sucesso: relatorio_ibge.txt")
