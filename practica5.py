
def adyacentes(grafo, v):
  # Dado un vértice, devuelve una lista con
  # los vértices adyacentes a él.
  aristas = grafo[1]
  adyacentes = []
  for arista in aristas:
    if arista[0] == v:
      adyacentes.append(arista[1])
    elif arista[1] == v:
      adyacentes.append(arista[0])
  return adyacentes

def incidentes(grafo, vertice):
    aristas = []

    for arista in grafo[1]:
        if arista[0] == vertice or arista[1] == vertice:
            aristas.append(arista)

    return aristas

def minimaArista(aristas):
    # Dado un conjunto de aristas, devuelve la arista de menor peso.
    minA = aristas[0]
    minCosto = aristas[0][2]

    for arista in aristas:
        if arista[2] < minCosto:
            minA = arista
            minCosto = minA[2]

    return minA

# Algoritmo de Prim.

def prim(grafo):
    n = len(grafo[0])
    arbol = [[], []]
    aristas = []
    ultimoAgregado = grafo[0][0]

    while len(arbol[0]) < n:
        arbol[0].append(ultimoAgregado)
        for arista in incidentes(grafo, ultimoAgregado):
            if arista not in aristas:
                aristas.append(arista)
                
        lenAnterior = len(arbol[1])

        while len(arbol[1]) == lenAnterior:
            minArista = minimaArista(aristas)
            
            if minArista[0] in arbol[0]:
                ultimoAgregado = minArista[1]
            else:
                ultimoAgregado = minArista[0]
        
            if ultimoAgregado not in arbol[0]:
                arbol[1].append(minArista)
            else:
                aristas.remove(minArista)
    return arbol

# Algoritmo de Kruskal

def kruskal(G):
    aristasVisitadas = []
    vertices = G[0]
    aristas = G[1]
    arbol = [[], []]
    cv = len(vertices)  
    while len(arbol[1]) != cv - 1 and len(aristas) > 0:
        minArista = minimaArista(aristas)
        if minArista not in aristasVisitadas:
            aristasVisitadas.append(minArista)
            if not (minArista[0] in arbol[0] and minArista[1] in arbol[0]):
                arbol[0].append(minArista[0])
                arbol[0].append(minArista[1])
                arbol[1].append(minArista)
            else:
                aristas.pop(aristas.index(minArista))
        else:
            aristas.pop(aristas.index(minArista))
    return arbol

def main():
    grafo1 = (['a', 'b', 'c'], [('a', 'b', 1), ('b', 'a', 2),('c', 'b', 4),('b', 'c', 3),('b', 'c', 5)])
    grafo2 = (['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b', 1), 
                ('b', 'a', 2), ('c', 'b', 4),('b', 'c', 3),('b', 'c', 5),('e', 'f', 10)])
    print(kruskal(grafo1))

main()