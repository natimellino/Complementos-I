# Ejercicio 1: dado un grafo no dirigido, en formato de
# listas con pesos y un vértice origen 'v', aplica el
# algoritmo de Dijkstra para hallar el costo del camino
# más corto de v al resto de los vértices.

import math

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

# Extrae el nodo con el mínimo costo no visitado del diccionario de costos.

def extraer_minimo(costos, visitados):
  nodos = list(costos.keys())
  costoMinimo = math.inf
  minimo = 'a'

  for nodo in nodos:
    costoNodo = costos[nodo]
    if costoNodo < costoMinimo and nodo not in visitados:
      minimo = nodo
      costoMinimo = costoNodo

  return minimo


def dijkstra_2(grafo, v):
  vertices = grafo[0]
  aristas = grafo[1]
  matriz = matriz_costos(grafo)
  n = len(vertices) # Cantidad de vértices.
  visitados = []
  costos = dict()
  for vert in vertices:
    costos[vert] = math.inf
  costos[v] = 0
  caminos = dict()
  for vert in vertices:
    caminos[vert] = []

  while len(visitados) < n:
      nodoActual = extraer_minimo(costos, visitados)
      caminoActual = caminos[nodoActual]
      caminoActual.append(nodoActual)
      caminos[nodoActual] = caminoActual

      for x in adyacentes(grafo, nodoActual):
          if x not in visitados:
              i1 = grafo[0].index(nodoActual)
              i2 = grafo[0].index(x)
              costoNuevo = costos.get(nodoActual) + matriz[i1][i2]
              if costoNuevo < costos[x] or costos[x] == -1:
                    costos[x] = costoNuevo
                    caminos[x] = caminoActual.copy()
      visitados.append(nodoActual)

  for vertice in vertices:
      if costos[vertice] == math.inf:
          costos.pop(vertice)
          caminos.pop(vertice)
      elif vertice == v:
          caminos[vertice] = [v]

  return caminos

def dijkstra(grafo, v):
  vertices = grafo[0]
  aristas = grafo[1]
  matriz = matriz_costos(grafo)
  n = len(vertices) # Cantidad de vértices.
  visitados = []
  costos = dict()
  for vert in vertices:
    costos[vert] = math.inf
  costos[v] = 0
  caminos = [[]] * n

  while len(visitados) < n:
      nodoActual = extraer_minimo(costos, visitados)

      for x in adyacentes(grafo, nodoActual):
          if x not in visitados:
              i1 = grafo[0].index(nodoActual)
              i2 = grafo[0].index(x)
              costoNuevo = costos.get(nodoActual) + matriz[i1][i2]
              if costoNuevo < costos[x] or costos[x] == -1:
                    costos[x] = costoNuevo
      visitados.append(nodoActual)

  for vertice in vertices:
      if costos[vertice] == math.inf:
          costos.pop(vertice)

  return costos

# def main():
#   grafo = [['a', 'b', 'c', 'd'], [('a', 'd', 3), ('c', 'b', 1), ('a', 'c', 4), ('a', 'b', 1)]]
#   #print(matriz_costos(grafo))
#   aux(grafo, 'a')
#
# main()
