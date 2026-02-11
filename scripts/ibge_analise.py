import matplotlib.pyplot as plt
from pathlib import Path
from ibge_utils import carregar_dados_ibge

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "ibge_idades.csv"

faixas, populacoes = carregar_dados_ibge(CSV_PATH)

plt.figure()
plt.bar(faixas, populacoes)
plt.title("População do Brasil por Grupo de Idade (IBGE)")
plt.xlabel("Grupo de idade")
plt.ylabel("População (mil pessoas)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
