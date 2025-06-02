from main2 import Grafo
import queue
import sys
if len(sys.argv) != 3:  # Garantir que dois parâmetros foram passados
        print("Uso: python A1_2.py <arquivo> <vértice>")
        sys.exit(1)

# Capturar os argumentos passados
arquivo = sys.argv[1]  # Primeiro argumento após o nome do script
vertice = int(sys.argv[2])  # Segundo argumento (convertido para inteiro)
#algoritmo de busca em largura
def buscaEmLargura():
    g = Grafo(arquivo)
    V = list()
    s = vertice
    for i in range(g.qtd_vertices()):
        V.append(i+1)
    Cv = {v: False for v in V}    
    Dv = {v: 999999999999999 for v in V}
    Av = {v: None for v in V}
    Cv[s] = True
    Dv[s] = 0
    Q = queue.Queue()
    Q.put(s)

    while Q.empty() == False:
        u = Q.get()
        for i in g.vizinhos(u):
            if Cv[i] == False:
                Cv[i] = True
                Dv[i] = Dv[u] + 1
                Av[i] = u
                Q.put(i)
    return Dv, Av
Dv, Av = buscaEmLargura()
distancias = {}
for vertice, distancia in Dv.items():
    if distancia not in distancias:
        distancias[distancia] = []
    distancias[distancia].append(vertice)

# Imprime os vértices agrupados por distância
for dist, vertices in distancias.items():
    print(f"{dist}: {', '.join(map(str, vertices))}")

    

