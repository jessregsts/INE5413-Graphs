from main2 import Grafo
import sys

if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
    print("Uso: python A2_1.py <arquivo>")
    sys.exit(1)

# Capturar os argumentos passados
arquivo = sys.argv[1]  # Primeiro argumento será o nome do arquivo

def DFS_Visit(g, v, C, T, Ancestrais, F, tempo):
    C[v] = True
    tempo += 1
    T[v+1] = tempo
    for i in g.vizinhos(v):
        if C[i] == False:
            Ancestrais[i] = v
            DFS_Visit(g, i, C, T, Ancestrais, F, tempo)
    tempo += 1
    F[v+1] = tempo

def DFS(g):
    C = {v: False for v in range(1, g.qtd_vertices()+1)}
    T = {v: float('inf') for v in range(1, g.qtd_vertices()+1)}
    Ancestrais = {v: None for v in range(1, g.qtd_vertices()+1)}
    F = {v: float('inf') for v in range(1, g.qtd_vertices()+1)}
    tempo = 0
    for u in g.vertices:
        if C[u] == False:
            DFS_Visit(g, u, C, T, Ancestrais, F, tempo)
    return C, T, Ancestrais, F

g = Grafo(f"{arquivo}")

C, T, Ancestrais, F = DFS(g)

#criar um grafo transposto
A_t = list()
for i in g.arestas:
    A_t.append((i[1], i[0]))
g.arestas = A_t
C_t, T_t, Ancestrais_, F_t = DFS(g)
# Lista para armazenar as componentes fortemente conectadas
componentes = []
temp = []

# Percorre todos os vértices
for i in range(1, len(Ancestrais_)+1):
    if Ancestrais_[i] is None:  # Encontra o início de uma nova componente
        if temp:  # Se 'temp' contém vértices, armazena como uma nova componente
            componentes.append(temp)
            temp = []
        temp.append(i)  # Adiciona o vértice atual à nova componente
    else:
        temp.append(i)  # Adiciona o vértice à componente atual

# Adiciona a última componente após o loop
if temp:
    componentes.append(temp)

# Imprimir as componentes fortemente conectadas no formato solicitado
for componente in componentes:
    print(",".join(map(str, componente)))


        
            
