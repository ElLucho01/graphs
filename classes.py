import numpy as np

#Declaración de los distintos tipos de grafos, cada uno contiene al menos la función de matriz adjacente y lista adjacente

class grafo_simple():
    def __init__(self, edge):
        tmp=[]
        for(u,v) in edge:
            if u!=v and (u,v) not in tmp:
                tmp.append((u,v))
                tmp.append((v,u))
        self.edges = tmp
        self.nodes ={u for u,v in edge} | {v for u,v in edge}
    
    def matrizAdj(self):
        n=len(self.nodes)
        matriz=np.zeros((n,n))
        for i, v in enumerate(self.nodes):
            for j,k in enumerate(self.nodes):
                if(v,k) in self.edges:
                    matriz[i,j]=1
        return matriz

    def listaAdj(self):
        adj = lambda n : {v for u,v in self.edges if u==n}
        return {v:adj(v) for v in self.nodes}
    
    def completarGrafo(self):
        edges=[]
        for i in self.nodes:
            for j in self.nodes:
                if(i!=j and (i,j) not in edges):
                    edges.append((i,j))
        return edges


class grafo_multiple():  
    def __init__(self, edge):
        tmp=[]
        for(u,v) in edge:
            if u!=v:
                tmp.append((u,v))
                tmp.append((v,u))
        self.edges = tmp
        self.nodes ={u for u,v in edge} | {v for u,v in edge}

    def matrizAdj(self):
        n=len(self.nodes)
        matriz=np.zeros((n,n))
        for i, v in enumerate(self.nodes):
            for j,k in enumerate(self.nodes):
                if(v,k) in self.edges:
                    matriz[i,j]=+1
        return matriz
    
    def listaAdj(self):
        adj = lambda n : {v for u,v in self.edges if u==n}
        return {v:adj(v) for v in self.nodes}

class grafo_dirigido(): 
    def __init__(self,edges):
        tmp=[]
        for (u,v) in edges:
            if (v,u) not in tmp:
                tmp.append((u,v))
        self.edges=tmp
        self.nodes={u for u,v in self.edges} | {v for u,v in self.edges}

        
    def matrizAdj(self):
        n=len(self.nodes)
        matriz=np.zeros((n,n))
        for i, v in enumerate(self.nodes):
            for j,k in enumerate(self.nodes):
                if(v,k) in self.edges:
                    matriz[i,j] = 1
        return matriz
    
    def listaAdj(self):
        adj = lambda n : {v for u,v in self.edges if u==n}
        return {v:adj(v) for v in self.nodes}

class grafo_ponderado():   
    def __init__(self,_edges):
        self.edges=_edges
        self.nodes={u for u,v in self.edges.keys()} | {v for u,v in self.edges.keys()}
        
    def matrizAdj(self):
        n=len(self.nodes)
        matriz=np.zeros((n,n))
        for i, v in enumerate(self.nodes):
            for j,k in enumerate(self.nodes):
                if(v,k) in self.edges:
                    matriz[i,j] = 1
        return matriz
    
    def listaAdj(self):
        adjacent=lambda n : {v for u,v in self.edges.keys() if u==n } | {u for u,v in self.edges.keys() if v==n}
        return {v:adjacent(v) for v in self.nodes}