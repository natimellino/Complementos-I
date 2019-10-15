# Algoritmo de Prim.

def matriz_costos(grafo):
  # Creamos la matriz.
  matriz = []
  cantVertices = len(grafo[0])
  for i in range(cantVertices):
    matriz.append([])
    for j in range(cantVertices):
      matriz[i].append(0)
  # El índice de cada vértice en la matriz se corresponde con el índice
  # que ocupa en la lista de vértices.
  for arista in grafo[1]:
    u = arista[0]
    v = arista[1]
    costo = arista[2]
    i1 = grafo[0].index(u)
    i2 = grafo[0].index(v)
    matriz[i1][i2] = costo
    matriz[i2][i1] = costo
  return matriz

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
    minA = aristas[0]
    minCosto = aristas[0][2]

    for arista in aristas:
        if arista[2] < minCosto:
            minA = arista
            minCosto = minA[2]

    return minA

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
    print(arbol)
    return arbol
