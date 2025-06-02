from main2 import Grafo
import sys
if len(sys.argv) != 3: 
    print("Uso: python A1_4.py <arquivo> <vertice>")
    sys.exit(1)

arquivo = sys.argv[1] 
vertice = int(sys.argv[2]) 

# Algoritmo de Bellman-Ford
def BellmanFord(s):
    g = Grafo(arquivo)
    E = g.arestas
    V = list()
    for i in range(g.qtd_vertices()):
        V.append(i+1)
    s=s
    Dv = {v: 999999999999 for v in V}
    Av = {v: None for v in V}
    Dv[s] = 0
    
    # Relaxamento das arestas
    for i in range(g.qtd_vertices()): 
                                        
        for (u,v) in E:
            if Dv[v] > Dv[u] + g.peso(u,v):
                Dv[v] = Dv[u] + g.peso(u,v) 
                Av[v] = u

    for (u,v) in E:
        if Dv[v] > Dv[u] +  g.peso(u,v):
            return 0, None, None
    return (1,Dv,Av) 

def reconstruir_caminho(Av, v):
    caminho = []
    while v is not None:
        caminho.insert(0, v)
        v = Av[v]
    return caminho

# Função principal
def main(s):
    r, Dv, Av = BellmanFord(s)

    if r == 0:
        print(r)
        return

    for v in sorted(Dv):
        if v != s:
            caminho = reconstruir_caminho(Av, v)
            caminho_str = ",".join(map(str, caminho))
            print(f"{v}: {caminho_str}; d={Dv[v]}")
        else:
            print(f"{v}: {v}; d=0")
s = vertice
main(s)