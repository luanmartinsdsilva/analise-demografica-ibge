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

# Lista para guardar idades
idades_convertidas = []

try:
    with open("idades.csv", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        print(f"{len(linhas)} linhas encontradas no arquivo.")  # debug
        for i, linha in enumerate(linhas):
            linha = linha.strip()
            if linha == "":
                print(f"Linha {i+1} vazia, ignorando.")  # debug
                continue
            idade = extenso_para_numero(linha)
            if idade is None or idade < 0:
                print(f"Linha {i+1} inválida: {linha}")  # debug
                continue
            idades_convertidas.append(idade)
except FileNotFoundError:
    print("Arquivo 'idades.csv' não encontrado na pasta do script!")
    exit()

if idades_convertidas:
    print("Idades válidas encontradas no arquivo:", idades_convertidas)
    print("Quantidade de idades:", len(idades_convertidas))
    print("Média das idades:", sum(idades_convertidas)/len(idades_convertidas))
else:
    print("Nenhuma idade válida encontrada no arquivo.")
