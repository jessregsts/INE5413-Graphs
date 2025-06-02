from grafo import Grafo
import itertools
import sys

if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
    print("Uso: python A3_3.py <arquivo>")
    sys.exit(1)
    
arquivo = sys.argv[1]

def subset_to_index(subset, vertices):
    index = 0
    vertex_list = list(vertices.keys())
    for v in subset:
        if v in vertex_list:
            index |= (1 << vertex_list.index(v))
    return index

def find_independent_sets(vertices, edges):
    subsets = list(itertools.chain.from_iterable(itertools.combinations(vertices, r) for r in range(len(vertices) + 1)))
    independent_sets = []
    for subset in subsets:
        is_independent = True
        for u, v in edges:
            if u in subset and v in subset:
                is_independent = False
                break
        if is_independent:
            independent_sets.append(subset)
    return independent_sets

def lawler_algorithm(g):
    vertices = list(g.vertices.keys())
    edges = [(str(u), str(v)) for u, v in g.arestas]

    num_subsets = 2 ** len(vertices)
    X = [float('inf')] * num_subsets
    X[0] = 0

    subsets = list(itertools.chain.from_iterable(itertools.combinations(vertices, r) for r in range(len(vertices) + 1)))
    subsets = sorted(subsets, key=len)

    # Lista para armazenar a cor de cada vértice
    coloring = {v: None for v in vertices}

    for S in subsets[1:]:
        index_S = subset_to_index(S, g.vertices)
        X[index_S] = float('inf')

        subgraph_edges = [(u, v) for u, v in edges if u in S and v in S]
        independent_sets = find_independent_sets(S, subgraph_edges)

        for I in independent_sets:
            index_I = subset_to_index(set(S) - set(I), g.vertices)
            X[index_S] = min(X[index_S], X[index_I] + 1)

    # Após calcular o número cromático, atribuir cores a cada vértice
    for vertex in vertices:
        # Encontrar a menor cor disponível para o vértice atual
        available_colors = set(range(1, X[-1] + 1))  # Todas as cores possíveis
        for u, v in edges:
            if u == vertex and coloring[v] in available_colors:
                available_colors.remove(coloring[v])
            if v == vertex and coloring[u] in available_colors:
                available_colors.remove(coloring[u])
        # Atribuir a menor cor disponível
        coloring[vertex] = min(available_colors)

    return X[-1], coloring

# Exemplo de uso
if __name__ == "__main__":
    g = Grafo(arquivo)  # Arquivo fornecido pelo usuário
    
    chromatic_number, coloring = lawler_algorithm(g)
    
    # Imprime o número cromático
    print(chromatic_number)
    
    # Ordena os vértices e imprime as cores atribuídas
    sorted_colors = [coloring[v] for v in sorted(coloring.keys(), key=int)]
    print(", ".join(map(str, sorted_colors)))
