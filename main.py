import classes as clase
#Inicialización de las aristas
E=[('a','b'),('c','a'),('c','b'),('b','d'),('a','b')]
E2=[(1,2),(3,4),(2,4),(1,2),(1,1)]
E3=[(1,2),(3,4),(2,4),(2,1),(2,1)]
E4={(1,2):1,(3,4):2,(2,4):1}
E5={('a','b'),('c','d'),('e','f'),('g','h'),('i','j')}
#Convertimos a las aristas en nodos
G=clase.grafo_simple(E5)
E6=G.completarGrafo()
G=clase.grafo_simple(E6)
print(G.matrizAdj())
