import csv

with open("ibge_idades.csv", encoding="utf-8-sig") as arquivo:
    leitor = csv.reader(arquivo)
    for i, linha in enumerate(leitor):
        print(f"{i}: {linha}")
        if i == 20:
            break
