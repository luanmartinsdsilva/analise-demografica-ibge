import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path
from scripts.ibge_utils import carregar_dados_ibge

st.set_page_config(page_title="Análise Demográfica - IBGE", layout="centered")

st.title("📊 Análise Demográfica do Brasil")
st.markdown("""
Este aplicativo utiliza dados do **IBGE (PNAD Contínua)** para analisar a
distribuição da população brasileira por **faixa etária**.

O objetivo é demonstrar habilidades em:
- leitura e tratamento de dados
- análise exploratória
- visualização interativa
- comunicação de insights
""")
st.caption("Fonte: IBGE – PNAD Contínua")

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data" / "ibge_idades.csv"

faixas, populacoes = carregar_dados_ibge(csv_path)

st.markdown("### Visualização")

mostrar = st.checkbox("Mostrar gráfico", value=True)

tipo = st.selectbox(
    "Escolha o tipo de gráfico:",
    ["Barras", "Pizza"]
)

if mostrar:
    fig, ax = plt.subplots()

    if tipo == "Barras":
        ax.bar(faixas, populacoes)
        ax.set_ylabel("População (mil pessoas)")
        ax.set_xlabel("Grupo de idade")
        plt.xticks(rotation=45)

    else:
        ax.pie(populacoes, labels=faixas, autopct="%1.1f%%")
        ax.axis("equal")

    st.pyplot(fig)

st.markdown("---")
st.write(
    f"A população analisada soma aproximadamente "
    f"**{sum(populacoes):,} mil pessoas**, distribuídas entre "
    f"**{len(faixas)} grupos etários**."
)
total = sum(populacoes)
maior_grupo = faixas[populacoes.index(max(populacoes))]
menor_grupo = faixas[populacoes.index(min(populacoes))]

col1, col2, col3 = st.columns(3)
col1.metric("População total (mil)", f"{total:,}")
col2.metric("Maior grupo", maior_grupo)
col3.metric("Menor grupo", menor_grupo)
st.subheader("📌 Principais insights")

total = sum(populacoes)

for faixa, pop in zip(faixas, populacoes):
    percentual = (pop / total) * 100
    st.write(f"- **{faixa}** representa aproximadamente **{percentual:.1f}%** da população analisada.")
st.subheader("🎛️ Filtro de faixa etária")

faixa_escolhida = st.selectbox(
    "Selecione uma faixa etária",
    faixas
)

indice = faixas.index(faixa_escolhida)
pop_escolhida = populacoes[indice]

st.info(f"A faixa **{faixa_escolhida}** possui aproximadamente **{pop_escolhida:,} mil pessoas**.")
