from main2 import Grafo
import sys

if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
        print("Uso: python A2_3.py <arquivo>")
        sys.exit(1)

# Capturar os argumentos passados
arquivo = sys.argv[1]  # Primeiro argumento após o nome do script

g = Grafo(f"{arquivo}")

A = list()
S = dict()
# Inicializar cada chave v com uma lista que contém o próprio vértice
for v in range(g.qtd_vertices()):
    S[v + 1] = [v + 1]

E = list()
for i in g.arestas:
    u = i[0]
    v = i[1]
    w = g.peso(u, v)
    E.append((u, v, w))

# Ordenar E por ordem crescente de peso
E.sort(key=lambda x: x[2])
total_peso = 0

# Remover w da lista E
E = [(u, v) for u, v, w in E]

X = list()
for i in E:
    u = i[0]
    v = i[1]
    if S[u] != S[v]:
        A.append((u, v))
        X = S[u] + S[v]
        for j in X:
            S[j] = X

# Somar pesos das arestas na lista A
for i in A:
    total_peso += g.peso(i[0], i[1])

# Formatar a saída de A no formato "u-v"
arestas_formatadas = ", ".join(f"{u}-{v}" for u, v in A)

# Imprimir o peso total e as arestas formatadas
print(total_peso)
print(arestas_formatadas)