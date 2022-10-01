class AdjMatriz:
    def __init__(self, qty_vertex):
        self.create_matriz(qty_vertex)

    def create_matriz(self, vertex_qty):
        self.matriz = []
        firstline = [0]
        for i in range(1, vertex_qty):
            firstline = firstline + [i]

        self.matriz.append(firstline)

        for i in range(1, vertex_qty):
            self.matriz.append([i] + [0]*vertex_qty)

    def add_edge(self, s, d):
        self.matriz[s][d] = 1
        self.matriz[d][s] = 1

    def print_graph(self):
        linhas = len(self.matriz)
        colunas = linhas

        for i in range(linhas):
            for j in range(colunas):
                if(j == colunas - 1):
                    if(i==0):
                        print(" %d " %self.matriz[i][j])
                    else:
                        print("[%d]" %self.matriz[i][j])
                else:
                    if(j==0 or i == 0):
                        if(j==0):
                            print("%d" %self.matriz[i][j], end = " ")
                        else:
                            print(" %d " %self.matriz[i][j], end = " ")
                    else:
                        print("[%d]" %self.matriz[i][j], end = " ")
        print()

class BuildAdjMatriz:
    def __init__(self, graph):
        self.graph = graph
        self.vertices_qty = int(self.graph.vertices_quantity) + 1
        self.adj_matriz = AdjMatriz(self.vertices_qty)
        self.fill_adj_matriz()

    def fill_adj_matriz(self):
        for line in self.graph.readed_graph[1:]:
            line = line.split(' ')
            self.adj_matriz.add_edge(int(line[0]), int(line[1]))

    def represent_graph(self):
        self.adj_matriz.print_graph()