import copy, math
class Grafo:
    def __init__(self, arquivo):
        self.matriz = None
        self.arquivo = arquivo
        self.vertices = dict()
        self.arestas = list()
        self.entrantes = dict()
        self.saintes = dict()
        self.leitura_arq(arquivo)
       
        
    def criar_matriz_zero(self, n_linhas, n_colunas):
        matriz = [[0 for _ in range(n_linhas)] for _ in range(n_colunas)]
        return matriz

    def add_matriz(self, v1, v2, dis, matriz, palavra):
        matriz[v1][v2] = dis
        if palavra == "*edges":
            matriz[v2][v1] = dis

    def print_matriz(self):
        if self.matriz:
            for linha in self.matriz:
                print(linha)
        else:
            print("Matriz não inicializada.")

    def leitura_arq(self, arquivo):
        with open(arquivo, 'r') as grafos:
            linha = grafos.readline()
            while linha:
                palavra = linha.split()
                if palavra[0] == "*vertices":
                    self.matriz = self.criar_matriz_zero(int(palavra[1]), int(palavra[1]))

                if palavra[0] == "*arcs" or palavra[0] == "*edges":
                    linha = grafos.readline()
                    while linha:
                        npalavra = linha.split()
                        self.add_matriz((int(npalavra[0])-1), (int(npalavra[1])-1), int(npalavra[2]), self.matriz, palavra[0])
                        self.arestas.append(((int(npalavra[0])), (int(npalavra[1]))))
                        if npalavra[0] not in self.saintes:
                            self.saintes[npalavra[0]] = [npalavra[1]]
                        else:
                            self.saintes[npalavra[0]].append(npalavra[1])
                        if npalavra[1] not in self.entrantes:
                            self.entrantes[npalavra[1]] = [npalavra[0]]
                        else:
                            self.entrantes[npalavra[1]].append(npalavra[0])
                            if palavra[0] == "*edges":    
                                self.arestas.append(((int(npalavra[1])), (int(npalavra[0]))))
                        linha = grafos.readline()
                        if not linha:
                            break
                if (palavra[0] != "*vertices") and (palavra[0] != "*arcs") and (palavra[0] != "*edges"):
                    nome = " ".join(palavra[1:])
                    self.vertices[nome] = (int(palavra[0])-1)
                linha = grafos.readline()

    def qtd_vertices(self):
        if self.matriz:
            return len(self.matriz)
        return 0
    def qtdArestas(self):
        quant = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j] != 0:
                    quant += 1
        return quant//2
                        
    def grau(self, v):
        quant = 0
        for i in range(len(self.matriz)):
            if self.matriz[i][(v-1)] != 0:
                quant += 1
        return quant
    def rotulo(self, v):
        v1 = int(v)-1
        return self.vertices[v1]
    def vizinhos(self, v):
        lista = []
        for i in range(len(self.matriz)):
            if self.matriz[v-1][i] != 0:
                lista.append(i+1)
        return lista
    def haAresta(self, u, v):
        
        if self.matriz[u-1][v-1] != 0:
            return True
        return False
    def peso(self, u, v):
        if self.matriz[u-1][v-1] != 0:
            return self.matriz[u-1][v-1]
        return float('inf')
    def grafo_matriz(self):
        return self.matriz
    
    def de(self, v):
        if v in self.entrantes:
            return len(self.entrantes[v])

    def ds(self, v):
        if v in self.saintes:
            return len(self.saintes[v])
    def Ne(self,v):
        if v in self.entrantes:
            return self.entrantes[v]
    def Ns(self,v):
        if v in self.saintes:
            return self.saintes[v]
        
def criaGrafoResidual(g):
    # Cópia do grafo original
    gl = Grafo(g.arquivo)
    gl.vertices = g.vertices.copy()
    gl.saintes = copy.deepcopy(g.saintes)
    gl.entrantes = copy.deepcopy(g.entrantes)
    gl.arestas = g.arestas.copy()
    gl.matriz = copy.deepcopy(g.matriz)

    # Criar arestas de retorno
    for u, v in g.arestas:
        if gl.peso(v, u) is None:  # Verificar se não há aresta de retorno
            gl.add_matriz(v - 1, u - 1, 0)  # Adicionar aresta de retorno com peso 0
            gl.arestas.append((v, u))
            gl.saintes.setdefault(v, []).append(u)
            gl.entrantes.setdefault(u, []).append(v)

    return gl



