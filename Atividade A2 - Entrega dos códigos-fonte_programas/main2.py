class Grafo:
    def __init__(self, arquivo):
        self.matriz = None
        self.vertices = dict()
        self.arestas = list()
        self.leitura_arq(arquivo)
        
        
    def criar_matriz_zero(self, n_linhas, n_colunas):
        matriz = [[0 for _ in range(n_linhas)] for _ in range(n_colunas)]
        return matriz

    def add_matriz(self, v1, v2, dis, matriz, tipo):
        matriz[v1][v2] = dis
        if tipo == "*edges":
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
                    tipo = palavra[0]
                    linha = grafos.readline()
                    while linha:
                        npalavra = linha.split()
                        self.add_matriz((int(npalavra[0])-1), (int(npalavra[1])-1), float(npalavra[2]), self.matriz, tipo)
                        self.arestas.append(((int(npalavra[0])), (int(npalavra[1]))))
                        if palavra[0] == "*edges":
                            self.arestas.append(((int(npalavra[1])), (int(npalavra[0]))))
                        linha = grafos.readline()
                        if not linha:
                            break
                if (palavra[0] != "*vertices") and (palavra[0] != "*arcs") and (palavra[0] != "*edges"):
                    nome = " ".join(palavra[1:]).strip('"').strip("'")
                    self.vertices[(int(palavra[0]))] = f"{nome}"
                linha = grafos.readline()

    def qtd_vertices(self):
        if self.matriz:
            return len(self.matriz)
        return 0
    def qtdArestas(self, tipo):
        quant = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j] != 0:
                    quant += 1
        if tipo == "*edges":
            quant = quant//2
        return quant
                        
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
        


