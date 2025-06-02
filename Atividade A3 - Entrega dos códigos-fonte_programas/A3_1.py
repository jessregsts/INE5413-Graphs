from grafo import Grafo
import queue
from grafo import criaGrafoResidual
import sys

if len(sys.argv) != 4:  # Garantir que dois parâmetros foram passados
    print("Uso: python A3_1.py <arquivo> s t")
    sys.exit(1)

arquivo = sys.argv[1]
#INICIO - adaptado pelo Santiago
s = int(sys.argv[2])
t = int(sys.argv[3])
#FIM - adaptado pelo Santiago

grafo = Grafo(arquivo)
gRes = criaGrafoResidual(grafo)
#INICIO - adaptado pelo Santiago
def BfsEdmondsKarp(grafo, s, t):
#FIM - adaptado pelo Santiago    
    V = len(grafo.vertices)
    C = {v: False for v in range(1, V+1)}
    A = {v: None for v in range(1, V+1)}
    #INICIO - adaptado pelo Santiago
    #origem = grafo.vertices["s"] + 1
    origem = s
    #destino = grafo.vertices["t"] + 1
    destino = t
    #FIM - adaptado pelo Santiago

    C[origem] = True
    Q = queue.Queue()
    Q.put(origem)
    p = []

    while not Q.empty():
        u = Q.get()
        for i in grafo.vizinhos(u):
            if not C[i] and grafo.peso(u, i) > 0:  # Apenas arestas com capacidade > 0
                C[i] = True
                A[i] = u
                if i == destino:
                    # Reconstruindo o caminho
                    p.append(i)
                    while i != origem:
                        i = A[i]
                        p.append(i)
                    return list(reversed(p))
                Q.put(i)
    return None
#INICIO - adaptado pelo Santiago
def ford_fulkerson(g_residual, s, t):
#FIM - adaptado pelo Santiago    
    F = 0
    while True:
        # Encontra um caminho aumentante
        caminho = BfsEdmondsKarp(g_residual, s, t)
        if caminho is None:
            break  # Não há mais caminhos aumentantes
        
        # Determina a capacidade mínima no caminho
        fp = float('inf')
        for i in range(len(caminho) - 1):
            u, v = caminho[i], caminho[i + 1]
            fp = min(fp, g_residual.peso(u, v))
        
        # Atualiza o fluxo total
        F += fp
        
        # Atualiza as capacidades residuais no grafo residual
        for i in range(len(caminho) - 1):
            u, v = caminho[i], caminho[i + 1]
            matriz = g_residual.grafo_matriz()
            matriz[u - 1][v - 1] -= fp  # Reduz a capacidade na direção original
            matriz[v - 1][u - 1] += fp  # Aumenta a capacidade na direção inversa

    return F
#INICIO - adaptado pelo Santiago
print(ford_fulkerson(gRes, s, t))
#FIM - adaptado pelo Santiago
