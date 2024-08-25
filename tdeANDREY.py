# Aluno: Matheus Teixeira Atner
import functools

# Lê o arquivo e converte as linhas para conjuntos
def ler_conjuntos(arquivo):
    with open(arquivo, 'r') as f:
        lines = f.readlines()
    conjuntos = [set(line.strip().split(',')) for line in lines]
    return conjuntos

# Carrega os conjuntos do arquivo
conjuntos = ler_conjuntos("conjuntos.txt")

# União
uniao = functools.reduce(set.union, [conjuntos[2], conjuntos[3]])
print(f"União: conjunto 1{conjuntos[2]} , conjunto 3{conjuntos[3]} . Resultado: {uniao}")

# Interseção
intersecao = conjuntos[5] & conjuntos[6]
print(f"Interseção: Resultado: {intersecao}")

# Diferença
diferenca = conjuntos[8] - conjuntos[9]
print("Diferença:", diferenca)

# Produto cartesiano
produto_cartesiano = [(x, y) for x in conjuntos[11] for y in conjuntos[12]]
print("Produto Cartesiano:", produto_cartesiano)

