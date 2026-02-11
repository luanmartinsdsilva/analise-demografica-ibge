def extenso_para_numero(texto):
    unidades = {
        "zero": 0, "um": 1, "dois": 2, "três": 3, "quatro": 4,
        "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9
    }
    especiais = {
        "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14,
        "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19
    }
    dezenas = {
        "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50,
        "sessenta": 60, "setenta": 70, "oitenta": 80, "noventa": 90
    }
    texto = texto.strip().lower()
    try:
        return int(texto)
    except ValueError:
        pass
    if texto in especiais:
        return especiais[texto]
    if texto in dezenas:
        return dezenas[texto]
    if " e " in texto:
        partes = texto.split(" e ")
        if len(partes) == 2:
            dez, uni = partes
            if dez in dezenas and uni in unidades:
                return dezenas[dez] + unidades[uni]
    return None

# Ler o arquivo CSV
idades_convertidas = []
try:
    with open("idades.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            idade = extenso_para_numero(linha)
            if idade is not None and idade >= 0:
                idades_convertidas.append(idade)
except FileNotFoundError:
    print("Arquivo 'idades.csv' não encontrado!")
    exit()

if not idades_convertidas:
    print("Nenhuma idade válida encontrada.")
    exit()

# Análises
quantidade = len(idades_convertidas)
media = sum(idades_convertidas) / quantidade
maior = max(idades_convertidas)
menor = min(idades_convertidas)
menores18 = [i for i in idades_convertidas if i < 18]
maiores18 = [i for i in idades_convertidas if i >= 18]

# Mostrar resultados
print("Idades válidas:", idades_convertidas)
print("Quantidade:", quantidade)
print("Média:", media)
print("Maior idade:", maior)
print("Menor idade:", menor)
print("Menores de 18 anos:", menores18)
print("Maiores ou iguais a 18 anos:", maiores18)

# Salvar resultado em arquivo
with open("resultado_idades.txt", "w", encoding="utf-8") as out:
    out.write("Idades válidas: " + str(idades_convertidas) + "\n")
    out.write("Quantidade: " + str(quantidade) + "\n")
    out.write("Média: " + str(media) + "\n")
    out.write("Maior idade: " + str(maior) + "\n")
    out.write("Menor idade: " + str(menor) + "\n")
    out.write("Menores de 18 anos: " + str(menores18) + "\n")
    out.write("Maiores ou iguais a 18 anos: " + str(maiores18) + "\n")

print("\n✅ Resultados salvos em 'resultado_idades.txt'")
