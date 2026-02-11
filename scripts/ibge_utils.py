import csv
from pathlib import Path

def carregar_dados_ibge(caminho_csv):
    caminho = Path(caminho_csv)

    faixas = []
    populacoes = []

    with caminho.open(encoding="utf-8-sig") as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        linhas = list(leitor)

        cabecalho = linhas[4][1:]
        dados = linhas[5][1:]

        for faixa, valor in zip(cabecalho, dados):
            faixas.append(faixa.replace('"', ''))
            populacoes.append(int(valor.replace('"', '')))

    return faixas, populacoes
