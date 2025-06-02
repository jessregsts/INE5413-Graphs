from main2 import Grafo
import sys
if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
    print("Uso: python A2_2.py <arquivo>")
    sys.exit(1)

# Capturar os argumentos passados
arquivo = sys.argv[1]  # Primeiro argumento após o nome do script

def OT():
    g = Grafo("manha.net")
    # Ajuste para preencher a lista V com índices iniciando em 0
    V = list()
    for i in range(g.qtd_vertices()):
        V.append(i+1)
    
    C = {v: False for v in V}  # Dicionário para marcar vértices visitados
    T = {v: float('inf') for v in V}
    F = {v: float('inf') for v in V}
    O = list()  # Lista para a ordenação topológica
    tempo = 0
    for u in V:
        if C[u] == False:
            VisitOT(g, u, C, O, T, F, tempo)
    return O

def VisitOT(g, u, C, O, T, F, tempo): #g,v,C,T,F,tempo,O
    C[u] = True
    tempo = tempo + 1
    T[u] = tempo
    for i in g.vizinhos(u):  # Ajuste: `vizinhos` usa índices baseados em 1
        if not C[i]:  # Corrigir índice para base 0
            VisitOT(g, i, C, O, T, F, tempo)
    tempo = tempo +1
    F[u] = tempo
    O.insert(0, g.vertices[u])  # Inserir no início da lista para ordenação correta
print(OT())