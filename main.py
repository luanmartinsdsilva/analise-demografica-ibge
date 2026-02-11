from pathlib import Path
from scripts.ibge_utils import carregar_dados_ibge
import matplotlib.pyplot as plt

def gerar_grafico_barras(faixas, populacoes):
    plt.figure()
    plt.bar(faixas, populacoes)
    plt.title("População do Brasil por Grupo de Idade (IBGE)")
    plt.xlabel("Grupo de idade")
    plt.ylabel("População (mil pessoas)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "ibge_idades.csv"

    faixas, populacoes = carregar_dados_ibge(csv_path)
    gerar_grafico_barras(faixas, populacoes)

if __name__ == "__main__":
    main()
