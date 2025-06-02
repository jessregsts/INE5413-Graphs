from main2 import Grafo
import sys
import random
if len(sys.argv) != 2:  # Garantir que dois parâmetros foram passados
    print("Uso: python A1_3.py <arquivo>")
    sys.exit(1)
        
def retorna_aresta_nao_visitada(g: Grafo, s: int, C):
    for i in g.vizinhos(s):
        aresta = (i,s)
        if aresta in g.arestas and C[aresta] == 0:
            return aresta
    return None

# Capturar os argumentos passados
arquivo = sys.argv[1]  # Primeiro argumento após o nome do script
# if arquivo != "ContemCicloEuleriano.net" and arquivo != "SemCicloEuleriano.net":
#     print(arquivo)
def buscarSubCicloEuleriano(g, s,C):
        ciclo = [s]
        t = s
        while 1:
            aresta = retorna_aresta_nao_visitada(g, s, C)

            if aresta == None:
                return 0, None
            else:
                s = aresta[0]
                C[aresta] = 1
                aresta = aresta[::-1]
                C[aresta] = 1
                ciclo.append(s)
            if t == s:
                break
        for x in ciclo:
            if retorna_aresta_nao_visitada(g, x, C) != None:
                (r,ciclo_) = buscarSubCicloEuleriano(g,x,C)
                if r == 0:
                    return 0, None
                ciclo[x:x] = ciclo_
            
        return 1, ciclo
# Algoritmo de Hierholzer
def Hierholzer():
    g = Grafo(arquivo)
    E = g.arestas
    V = list()
    for i in range(g.qtd_vertices()):
        V.append(i+1)
    s = 1
    C = {e: 0 for e in E}             
        
    (r,ciclo) = buscarSubCicloEuleriano(g, s,C)
    if r == 0:
        return 0, None
    else:
        for aresta in C.values():
            if aresta == 0:
                return 0, None
        return 1, ciclo
            
(r,ciclo) = Hierholzer()
print(r)
if r != 0:
    ciclo_str = ",".join(map(str, ciclo))
    print(ciclo_str)