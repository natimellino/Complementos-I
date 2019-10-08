# Ejercicio 1: dado un grafo no dirigido, en formato de 
# listas con pesos y un vértice origen 'v', aplica el
# algoritmo de Dijkstra para hallar el costo del camino
# más corto de v al resto de los vértices.

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
  minimo = nodos[0]
  for nodo in nodos:
    if costos.get(nodo) != 0 and not nodo in visitados and costos.get(nodo) < costos.get(minimo):
      minimo = nodo
  return minimo


# no anda esta berga revisar funcion extraer_minimo
def dijkstra_costos(matriz, grafo, v, costos):
  vertices = grafo[0]
  aristas = grafo[1]
  n = len(vertices) # Cantidad de vértices.
  visitados = []
  i = 0
  while len(visitados) < n:
    # En la primera iteración arranca siendo v el nodo actual.
    if i == 0:
      nodoActual = v
    # En el resto de los casos es el nodo con el valor mínimo no visitado.
    else:
      nodoActual = extraer_minimo(costos, v)
    for x in adyacentes(grafo, nodoActual):
      if not x in visitados:
        i1 = grafo[0].index(nodoActual)
        i2 = grafo[0].index(x)
        costoNuevo = costos.get(nodoActual) + matriz[i1][i2]
        if costoNuevo < costos.get(v) or costos.get(v) == 0:
          costos.pop(v)
          costos[v] = costoNuevo
    visitados.append(nodoActual)
    print(visitados)
    i+=1
  return costos

  
def aux(grafo, v):
  vertices = grafo[0]
  matriz = matriz_costos(grafo)  
  costos = dict()
  for vert in vertices:
    costos[vert] = 0
  costos = dijkstra_costos(matriz, grafo, v, costos)
  print(list(costos.items()))

def main():
  grafo = [['a', 'b', 'c', 'd'], [('a', 'd', 3), ('c', 'b', 5), ('a', 'c', 4), ('a', 'b', 1)]]
  #print(adyacentes(grafo, 'a'))
  #print(matriz_costos(grafo))
  aux(grafo, 'a')

main()