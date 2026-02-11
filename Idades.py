# Função para converter números por extenso até 99
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

    # Tenta número direto
    try:
        return int(texto)
    except ValueError:
        pass

    # Verifica casos especiais
    if texto in especiais:
        return especiais[texto]

    # Verifica dezenas exatas
    if texto in dezenas:
        return dezenas[texto]

    # Verifica combinação de dezenas + unidades (ex: "vinte e um")
    if " e " in texto:
        partes = texto.split(" e ")
        if len(partes) == 2:
            dez, uni = partes
            if dez in dezenas and uni in unidades:
                return dezenas[dez] + unidades[uni]

    # Se não reconhecer
    return None


# Função principal
def analisar_idade():
    idade_texto = input("Digite sua idade: ")
    idade = extenso_para_numero(idade_texto)

    if idade is None:
        print("Digite um número válido")
    elif idade >= 0:
        print("Idade digitada:", idade)
    else:
        print("Idade não pode ser negativa")


# Chamar a função
analisar_idade()
