# Aluno: Matheus Teixeira Atner

import functools


# Função para ler um arquivo e converter suas linhas em conjuntos
def ler_conjuntos(arquivo, ignorar_linhas=None):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    if ignorar_linhas:
        linhas = [linha for i, linha in enumerate(linhas) if i not in ignorar_linhas]

    conjuntos = [set(linha.strip().split(',')) for linha in linhas]
    return conjuntos

# Função para processar operações e exibir resultados
def processar_operacoes(conjuntos, nome_arquivo):
    print(f"\nResultados para o arquivo: {nome_arquivo}")

    # União dos conjuntos 2, 3 e 4
    if len(conjuntos) > 4:
        uniao = functools.reduce(set.union, [conjuntos[2], conjuntos[3], conjuntos[4]])
        print(f"União: {uniao}")

    # Interseção dos conjuntos 6, 7 e 8
    if len(conjuntos) > 7:
        intersecao = conjuntos[5] & conjuntos[6] & conjuntos[7]
        print(f"Interseção: {intersecao}")

    # Diferença do conjunto 9 com 10 e 11
    if len(conjuntos) > 10:
        diferenca = conjuntos[8] - conjuntos[9] - conjuntos[10]
        print(f"Diferença: {diferenca}")

    # Produto cartesiano dos conjuntos 12, 10 e 13
    if len(conjuntos) > 12:
        produto_cartesiano = [(x, y, z) for x in conjuntos[11] for y in conjuntos[9] for z in conjuntos[12]]
        print(f"Produto Cartesiano: {produto_cartesiano}")

# Processa o arquivo conjuntos1.txt
conjuntos1 = ler_conjuntos("conjuntos1.txt")
processar_operacoes(conjuntos1, "conjuntos1.txt")

# Processa o arquivo conjuntos2.txt, ignorando as linhas 11 e 12
conjuntos2 = ler_conjuntos("conjuntos2.txt", ignorar_linhas=[11, 12])
processar_operacoes(conjuntos2, "conjuntos2.txt")

# Processa o arquivo conjuntos3.txt
conjuntos3 = ler_conjuntos("conjuntos3.txt")
processar_operacoes(conjuntos3, "conjuntos3.txt")
