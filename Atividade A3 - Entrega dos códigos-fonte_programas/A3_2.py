from collections import deque
from grafo import Grafo

import sys

if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
    print("Uso: python A3_2.py <arquivo>")
    sys.exit(1)

def hopcroft_karp(grafo):
    """
    Implementação do algoritmo Hopcroft-Karp para encontrar o emparelhamento máximo
    em um grafo bipartido utilizando a classe Grafo.

    Parâmetros:
        grafo: instância da classe Grafo representando o grafo bipartido.
    
    Retorno:
        Um par (m, mate) onde:
            m: tamanho do emparelhamento máximo.
            mate: dicionário representando o emparelhamento de cada vértice.
    """
    n = grafo.qtd_vertices()
    X = range(1, (n // 2) + 1)
    Y = range((n // 2) + 1, n + 1)

    mate = {v: None for v in range(1, n + 1)}
    D = {}

    def bfs():
        queue = deque()
        for x in X:
            if mate[x] is None:
                D[x] = 0
                queue.append(x)
            else:
                D[x] = float('inf')
        D[None] = float('inf')
        while queue:
            x = queue.popleft()
            if D[x] < D[None]:
                for y in grafo.vizinhos(x):
                    if D[mate[y]] == float('inf'):
                        D[mate[y]] = D[x] + 1
                        queue.append(mate[y])
        return D[None] != float('inf')

    def dfs(x):
        if x is not None:
            for y in grafo.vizinhos(x):
                if D[mate[y]] == D[x] + 1:
                    if dfs(mate[y]):
                        mate[y] = x
                        mate[x] = y
                        return True
            D[x] = float('inf')
            return False
        return True

    m = 0
    while bfs():
        for x in X:
            if mate[x] is None and dfs(x):
                m += 1

    return m, mate

# Função principal para ler o grafo e executar o algoritmo
def main():
    # Criar o grafo a partir do arquivo
    arquivo = sys.argv[1]
    grafo = Grafo(arquivo)

    # Resolver o problema com Hopcroft-Karp
    max_matching, mate = hopcroft_karp(grafo)

    # Imprimir o resultado
    print(max_matching)
    matching_edges = [
        f"{x}-{mate[x]}" for x in range(1, (grafo.qtd_vertices() // 2) + 1) if mate[x] is not None
    ]
    print(", ".join(matching_edges))

if __name__ == "__main__":
    main()
